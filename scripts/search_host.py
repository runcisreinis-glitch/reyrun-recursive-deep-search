#!/usr/bin/env python3
"""One bounded, lifecycle-enforced research worker invocation; no built-in model.

python search_host.py --state-dir STATE --config CONFIG.json \
    --request REQUEST.json --output-dir NEW_JOB_DIR

Configured worker receives one JSON object on stdin and returns exactly one
recursive_search finish record on stdout. Logs belong on stderr. A valid finish
commit is required for accepted_host_completion=true. See host-contract.md.
"""
import argparse
from datetime import datetime, timedelta, timezone
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time

import recursive_search as runtime
import delivery_gate

PROTOCOL = "reyrun-search-worker-v1"


def lifecycle(state_dir, operation, data):
    store = runtime.Store(state_dir)
    with store.lock():
        store.load()
        result = getattr(runtime, operation)(store, data)
        return store.save(operation, result)


def stop_owned(process):
    """Best effort for our new POSIX group; Windows requires job supervision."""
    if process is None:
        return
    if os.name == "posix":
        try:
            os.killpg(process.pid, signal.SIGTERM)
        except ProcessLookupError:
            pass
        try:
            process.wait(timeout=1)
        except subprocess.TimeoutExpired:
            pass
        try:
            os.killpg(process.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
    elif process.poll() is None:
        process.terminate()
        try:
            process.wait(timeout=1)
        except subprocess.TimeoutExpired:
            process.kill()
    try:
        process.wait(timeout=2)
    except subprocess.TimeoutExpired:
        pass


def config_file(path):
    raw = runtime.read_file(str(path.absolute()))
    config = runtime.parse(raw)
    runtime.fields(config, "controller_id worker_argv worker_cwd timeout_seconds",
                   "diagnostic_worker_argv diagnostic_timeout_seconds delivery_gate_mode review_receipt_dir", label="host config")
    runtime.require(config.get("delivery_gate_mode", "strict") in {"strict", "lifecycle_only"},
                    "delivery_gate_mode must be strict or lifecycle_only")
    runtime.ident(config["controller_id"], "controller_id")
    for arg in runtime.sequence(config["worker_argv"], "worker argv", 1, 64):
        runtime.text(arg, "worker argument", 16000)
        runtime.require("\x00" not in arg, "NUL in worker argument")
    cwd = Path(config["worker_cwd"])
    runtime.require(cwd.is_absolute() and cwd.is_dir(), "worker_cwd must be an existing absolute directory")
    runtime.require(0 < runtime.number(config["timeout_seconds"], "timeout_seconds", 900),
                    "timeout must be positive and at most 900 seconds")
    runtime.require(("diagnostic_worker_argv" in config) == ("diagnostic_timeout_seconds" in config),
                    "diagnostic argv and timeout must be configured together")
    if "diagnostic_worker_argv" in config:
        for arg in runtime.sequence(config["diagnostic_worker_argv"], "diagnostic argv", 1, 64):
            runtime.text(arg, "diagnostic argument", 16000)
            runtime.require("\x00" not in arg, "NUL in diagnostic argument")
        runtime.require(0 < runtime.number(config["diagnostic_timeout_seconds"], "diagnostic timeout", 900),
                        "diagnostic timeout must be positive")
    return config, runtime.sha_bytes(raw)


def run(args):
    job_dir, process, started = None, None, time.monotonic()
    receipt = {"protocol": PROTOCOL, "accepted_host_completion": False,
               "improvement_proven": False, "timed_out": False,
               "step_missing": [], "diagnostic_attempts": 0,
               "evidence_contract_passed": False, "factual_quality_certified": False,
               "process_containment": ("owned POSIX process group; external supervisor needed for stronger containment"
                                       if os.name == "posix" else
                                       "direct process only; externally supervised Windows job required for tree containment")}
    try:
        config, config_sha = config_file(args.config)
        request = runtime.parse(runtime.read_file(str(args.request.absolute())))
        store = runtime.Store(args.state_dir)
        with store.lock():
            store.load()
            runtime.require(config["controller_id"] == store.data["owner_id"], "controller ID differs from state owner")
        target = args.output_dir.absolute()
        runtime.require(not target.exists() and not target.is_symlink(), "output directory already exists; inspect its receipt before retrying")
        target.mkdir(parents=True, exist_ok=False)
        job_dir = target.resolve()
        begun = lifecycle(args.state_dir, "begin", request)
        deadline = datetime.now(timezone.utc) + timedelta(seconds=config["timeout_seconds"])
        execution_deadline = time.monotonic() + config["timeout_seconds"]
        worker_input = {"protocol": PROTOCOL, "run_id": begun["run_id"],
                        "begin_sha256": begun["begin_sha256"], "brief": begun["brief"],
                        "artifact_dir": str(job_dir), "deadline_utc": deadline.isoformat(),
                        "delivery_gate_mode": config.get("delivery_gate_mode", "strict"),
                        "delivery_manifest_schema": delivery_gate.SCHEMA,
                        "delivery_manifest_path": str(job_dir / "delivery-manifest.json")}
        receipt["delivery_gate_mode"] = worker_input["delivery_gate_mode"]
        receipt.update(run_id=begun["run_id"], begin_sha256=begun["begin_sha256"],
                       policy_sha256=begun["brief"]["policy_sha256"],
                       loaded_lesson_ids=begun["brief"]["loaded_lesson_ids"],
                       config_sha256=config_sha, deadline_utc=deadline.isoformat(),
                       begin_event_sha256=begun["event_sha256"])
        payload = runtime.canonical(worker_input) + b"\n"
        runtime.atomic(job_dir / "worker-input.json", payload)
        stdout_path, stderr_path = job_dir / "worker-stdout.json", job_dir / "worker-stderr.log"
        with stdout_path.open("wb") as stdout, stderr_path.open("wb") as stderr:
            process = subprocess.Popen(config["worker_argv"], cwd=config["worker_cwd"],
                                       stdin=subprocess.PIPE, stdout=stdout, stderr=stderr,
                                       shell=False, start_new_session=(os.name == "posix"))
            receipt["worker_pid"] = process.pid
            runtime.atomic(job_dir / "host-receipt.json", runtime.canonical(receipt))
            try:
                process.communicate(input=payload, timeout=config["timeout_seconds"])
            except subprocess.TimeoutExpired:
                receipt["timed_out"] = True
                stop_owned(process)
                raise runtime.Invalid("worker deadline exceeded; run remains unfinished")
            finally:
                # A successful worker must not leave an unmanaged background job.
                stop_owned(process)
        receipt["worker_exit_code"] = process.returncode
        runtime.require(process.returncode == 0, "worker exited unsuccessfully; run remains unfinished")
        result = runtime.parse(runtime.read_file(str(stdout_path)))
        runtime.require(type(result) is dict, "worker output must be a JSON object")
        runtime.require(result.get("run_id") == begun["run_id"] and
                        result.get("begin_sha256") == begun["begin_sha256"],
                        "worker output not bound to this begin receipt")
        missing = [key for key, expected in (("learning", dict), ("lesson_cards", list))
                   if type(result.get(key)) is not expected]
        if missing:
            receipt["step_missing"] = missing
            repair = {"missing": missing, "allowed_change_fields": ["learning", "lesson_cards"],
                      "instruction": "Diagnose the observed outcome. Supply a supported no-change decision or a bounded hypothesis with an EN/DE/ZH/JA improvement search plan using the same skill. Do not invent progress.",
                      "same_skill": True, "languages": ["EN", "DE", "ZH", "JA"]}
            receipt["repair_request"] = repair
            runtime.atomic(job_dir / "repair-request.json", runtime.canonical(repair))
            runtime.require("diagnostic_worker_argv" in config,
                            "learning step missing; repair request saved, no diagnostic worker configured")
            remaining = min(config["diagnostic_timeout_seconds"], execution_deadline - time.monotonic())
            runtime.require(remaining > 0, "no original deadline budget remains for diagnostic repair")
            repair_input = dict(worker_input, phase="diagnostic_repair", repair_request=repair, previous_result=result)
            repair_payload = runtime.canonical(repair_input) + b"\n"
            runtime.atomic(job_dir / "diagnostic-input.json", repair_payload)
            receipt["diagnostic_attempts"] = 1
            with (job_dir / "diagnostic-stdout.json").open("wb") as output, (job_dir / "diagnostic-stderr.log").open("wb") as errors:
                process = subprocess.Popen(config["diagnostic_worker_argv"], cwd=config["worker_cwd"],
                                           stdin=subprocess.PIPE, stdout=output, stderr=errors, shell=False,
                                           start_new_session=(os.name == "posix"))
                receipt["diagnostic_pid"] = process.pid
                try:
                    process.communicate(input=repair_payload, timeout=remaining)
                except subprocess.TimeoutExpired:
                    receipt["timed_out"] = True
                    raise runtime.Invalid("diagnostic repair exceeded the original bounded deadline")
                finally:
                    stop_owned(process)
            runtime.require(process.returncode == 0, "diagnostic worker exited unsuccessfully")
            repaired = runtime.parse(runtime.read_file(str(job_dir / "diagnostic-stdout.json")))
            runtime.fields(repaired, "learning lesson_cards", label="diagnostic repair")
            result.update(repaired)
            runtime.atomic(job_dir / "validated-worker-result.json", runtime.canonical(result))
        if config.get("delivery_gate_mode", "strict") == "strict":
            try:
                checked = delivery_gate.validate(job_dir / "delivery-manifest.json",
                                                 begun["run_id"], begun["begin_sha256"], job_dir,
                                                 config.get("review_receipt_dir"))
                delivery_gate.require(checked["controller_receipts_matched"],
                                      "strict delivery needs independent controller dispatch receipts")
            except (delivery_gate.Invalid, OSError, ValueError, TypeError, KeyError, AttributeError) as error:
                receipt["step_missing"].append("delivery_evidence_contract")
                receipt["repair_request"] = {
                    "missing": ["delivery_evidence_contract"], "reason": str(error),
                    "instruction": "Repair the affected evidence records and review the answer within a new explicitly bounded attempt. Do not relabel an unchecked answer as verified."}
                runtime.atomic(job_dir / "delivery-repair-request.json", runtime.canonical(receipt["repair_request"]))
                raise runtime.Invalid("delivery evidence contract failed: " + str(error)) from error
            runtime.atomic(job_dir / "delivery-check.json", runtime.canonical(checked))
            bound_answers = {"delivery_sha256": checked["answer_sha256"]}
            if "evaluation_fields" in checked:
                bound_answers["evaluation_fields"] = checked["evaluation_fields"]
            runtime.require(result.get("answers") == bound_answers,
                            "strict finish answers must match the checked delivery and optional evaluation fields")
            receipt["evidence_contract_passed"] = True
            receipt["delivery_manifest_sha256"] = checked["manifest_sha256"]
            receipt["delivery_answer_sha256"] = checked["answer_sha256"]
        finished = lifecycle(args.state_dir, "finish", result)
        receipt.update(accepted_host_completion=True, answer_sha256=finished["answer_sha256"],
                       finish_event_sha256=finished["event_sha256"],
                       observations_staged=finished["observations_staged"],
                       learning_completed=True, learning_decision=finished["learning_decision"],
                       improvement_research_recorded=finished["improvement_research_recorded"],
                       lesson_card_ids=finished["lesson_card_ids"],
                       step_repaired=missing if receipt["diagnostic_attempts"] else [],
                       worker_output_path=str(job_dir / "validated-worker-result.json") if receipt["diagnostic_attempts"] else str(stdout_path),
                       statement="Worker result passed lifecycle binding and was committed; factual quality was not certified.")
    except (runtime.Invalid, OSError, UnicodeError, ValueError, TypeError, KeyError) as error:
        receipt["error"] = str(error)
        receipt["learning_completed"] = False
        stop_owned(process)
    receipt["elapsed_seconds"] = round(time.monotonic() - started, 6)
    if job_dir is not None:
        try:
            runtime.atomic(job_dir / "host-receipt.json", runtime.canonical(receipt))
        except OSError as error:
            receipt["receipt_write_error"] = str(error)
            receipt["accepted_host_completion"] = False
    return receipt


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    for name in ("state-dir", "config", "request", "output-dir"):
        parser.add_argument("--" + name, required=True, type=Path)
    result = run(parser.parse_args())
    print(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False))
    return 0 if result["accepted_host_completion"] else 1


if __name__ == "__main__":
    sys.exit(main())
