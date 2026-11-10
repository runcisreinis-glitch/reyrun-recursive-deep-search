"""Independent host-hook checks with a SYNTHETIC offline worker, not a model.

The tests demonstrate actual begin -> subprocess -> finish wiring and refusal
of an unbound or timed-out result. They do not prove research quality.
"""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


BASE = Path(__file__).resolve().parents[1]
RUNTIME = BASE / "scripts" / "recursive_search.py"
HOST = BASE / "scripts" / "search_host.py"

WORKER = r'''
import hashlib, json, os, pathlib, sys, time
request = json.load(sys.stdin)
assert request["protocol"] == "reyrun-search-worker-v1"
brief = request["brief"]
directory = pathlib.Path(request["artifact_dir"])
directory.mkdir(parents=True, exist_ok=True)
mode = sys.argv[1]
if mode == "timeout":
    (directory / "worker-pid.txt").write_text(str(os.getpid()), encoding="utf-8")
    time.sleep(10)
    raise SystemExit(0)
evidence = directory / "observed.json"
evidence.write_text(json.dumps({
    "status": "SYNTHETIC offline worker observation",
    "run_id": request["run_id"],
    "loaded_lesson_ids": brief["loaded_lesson_ids"]
}), encoding="utf-8")
result = {
    "run_id": request["run_id"],
    "begin_sha256": request["begin_sha256"],
    "answers": {"loaded_lesson_ids": brief["loaded_lesson_ids"],
                "status": "SYNTHETIC mechanism check; no research gain measured."},
    "metrics": {"precision": None, "utility": None, "innovation": None, "clarity": None, "cost": 0},
    "observations": [{
        "id": "offline-observation", "kind": "unknown",
        "text": "SYNTHETIC worker ran; research quality was not evaluated.",
        "evidence": [{"path": str(evidence), "sha256": hashlib.sha256(evidence.read_bytes()).hexdigest()}]
    }],
    "learning": {
        "diagnosis": "SYNTHETIC offline worker; no research gain was measured.",
        "decision": "no_change", "hypothesis": "", "search_plan": [],
        "reason": "A protocol exercise supplies no evidence for a research-policy change.",
        "evidence_sha256": [hashlib.sha256(evidence.read_bytes()).hexdigest()]
    },
    "lesson_cards": [],
    "learning_use": [{"lesson_id": item, "status": "applied",
                      "reason": "SYNTHETIC worker records which lessons it was actually supplied."}
                     for item in brief["loaded_lesson_ids"]],
    "strategy_use": [{"id": item["id"], "status": "applied",
                      "reason": "SYNTHETIC use acknowledgement, not a model cognition claim."}
                     for item in brief["strategies"]]
}
if mode == "badfinish":
    result["begin_sha256"] = "0" * 64
if mode == "missinglearning":
    result.pop("learning")
    result.pop("lesson_cards")
if mode == "delivery":
    sys.path.insert(0, sys.argv[2])
    from test_delivery_gate import make_fixture
    manifest = make_fixture(directory, request["run_id"], request["begin_sha256"])
    (directory / "delivery-manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
    result["answers"] = {"delivery_sha256": manifest["answer"]["sha256"]}
print(json.dumps(result))
'''

DIAGNOSTIC = r'''
import json, pathlib, sys, time
request = json.load(sys.stdin)
assert request["phase"] == "diagnostic_repair"
if sys.argv[1] == "timeout":
    time.sleep(10)
hashes = [ref["sha256"] for item in request["previous_result"]["observations"] for ref in item["evidence"]]
result = {"learning": {
    "diagnosis": "SYNTHETIC missing learning record was diagnosed from the actual result.",
    "decision": "no_change", "hypothesis": "", "search_plan": [],
    "reason": "An offline protocol fixture establishes no quality gain.",
    "evidence_sha256": hashes[:1]
}, "lesson_cards": []}
if sys.argv[1] == "invalid":
    result["answers"] = {"attempted": "unauthorized answer rewrite"}
print(json.dumps(result))
'''


class SearchHostHooks(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.state = self.root / "state"
        self.worker = self.root / "synthetic_worker.py"
        self.worker.write_text(WORKER, encoding="utf-8")
        self.diagnostic = self.root / "synthetic_diagnostic.py"
        self.diagnostic.write_text(DIAGNOSTIC, encoding="utf-8")
        initial = self.root / "initial.json"
        initial.write_text(json.dumps({
            "owner_id": "synthetic-host-owner",
            "policy": {"version": "synthetic-host-v1", "instructions": "SYNTHETIC offline hook exercise.",
                       "strategies": [{"id": "trace-input", "scope": "host-test",
                                       "instruction": "Record the supplied learning identifiers."}]}
        }), encoding="utf-8")
        self.execute([sys.executable, str(RUNTIME), "--state-dir", str(self.state), "init", str(initial)])

    def execute(self, argv, success=True):
        result = subprocess.run(argv, capture_output=True, text=True, timeout=15)
        if success:
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        else:
            self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(result.stderr, "", result.stdout + result.stderr)
        value = json.loads(result.stdout)
        self.assertIs(value["improvement_proven"], False)
        return value

    def run_worker(self, run_id, mode="normal", success=True, output=None, diagnostic=None, delivery_mode="lifecycle_only"):
        config = self.root / (run_id + "-config.json")
        config_data = {
            "controller_id": "synthetic-host-owner",
            "worker_argv": [sys.executable, str(self.worker), mode, str(BASE / "tests")],
            "worker_cwd": str(self.root), "timeout_seconds": 1 if mode == "timeout" else 10,
        }
        if delivery_mode is not None:
            config_data["delivery_gate_mode"] = delivery_mode
        if diagnostic is not None:
            config_data.update(diagnostic_worker_argv=[sys.executable, str(self.diagnostic), diagnostic],
                               diagnostic_timeout_seconds=2)
            if diagnostic == "timeout":
                config_data["timeout_seconds"] = 0.3
        config.write_text(json.dumps(config_data), encoding="utf-8")
        request = self.root / (run_id + "-request.json")
        request.write_text(json.dumps({
            "id": run_id, "task": "SYNTHETIC offline test of host supplied context.", "scope": "host-test",
            "model_id": "no-model-synthetic-worker", "environment_id": "synthetic-offline-host",
            "budget": {"unit": "synthetic-cost", "limit": 1},
        }), encoding="utf-8")
        output = output or self.root / ("job-" + run_id)
        result = self.execute([
            sys.executable, str(HOST), "--state-dir", str(self.state), "--config", str(config),
            "--request", str(request), "--output-dir", str(output)
        ], success=success)
        return result, output

    def exported(self):
        return self.execute([sys.executable, str(RUNTIME), "--state-dir", str(self.state), "export"])["state"]

    def test_two_worker_processes_receive_persisted_learning_and_commit_bound_results(self):
        first, first_dir = self.run_worker("first")
        self.assertIs(first["accepted_host_completion"], True)
        second, second_dir = self.run_worker("second")
        self.assertIs(second["accepted_host_completion"], True)
        supplied = json.loads((second_dir / "worker-input.json").read_text(encoding="utf-8"))
        self.assertEqual(supplied["protocol"], "reyrun-search-worker-v1")
        self.assertIn("first/offline-observation", supplied["brief"]["loaded_lesson_ids"])
        self.assertEqual(supplied["begin_sha256"], second["begin_sha256"])
        state = self.exported()
        self.assertEqual(state["runs"]["first"]["status"], "finished")
        self.assertEqual(state["runs"]["second"]["status"], "finished")
        self.assertIn("first/offline-observation", state["runs"]["second"]["result"]["answers"]["loaded_lesson_ids"])
        self.assertEqual(first["policy_sha256"], second["policy_sha256"])
        receipt = json.loads((second_dir / "host-receipt.json").read_text(encoding="utf-8"))
        self.assertIs(receipt["accepted_host_completion"], True)
        refused, _ = self.run_worker("third", output=first_dir, success=False)
        self.assertIs(refused["accepted_host_completion"], False)
        self.assertNotIn("third", self.exported()["runs"])

    def test_wrong_begin_digest_leaves_worker_result_unaccepted(self):
        result, output = self.run_worker("unbound", mode="badfinish", success=False)
        self.assertIs(result["accepted_host_completion"], False)
        self.assertEqual(self.exported()["runs"]["unbound"]["status"], "started")
        receipt = json.loads((output / "host-receipt.json").read_text(encoding="utf-8"))
        self.assertIs(receipt["accepted_host_completion"], False)

    def test_default_strict_host_refuses_missing_research_evidence(self):
        result, output = self.run_worker("no-evidence", success=False, delivery_mode=None)
        self.assertIs(result["evidence_contract_passed"], False)
        self.assertIn("delivery_evidence_contract", result["step_missing"])
        self.assertTrue((output / "delivery-repair-request.json").is_file())
        self.assertEqual(self.exported()["runs"]["no-evidence"]["status"], "started")

    def test_strict_host_commits_a_bound_delivery_fixture_without_certifying_truth(self):
        result, output = self.run_worker("evidence-fixture", mode="delivery", delivery_mode=None)
        self.assertTrue(result["accepted_host_completion"])
        self.assertTrue(result["evidence_contract_passed"])
        self.assertFalse(result["factual_quality_certified"])
        checked = json.loads((output / "delivery-check.json").read_text(encoding="utf-8"))
        self.assertEqual(result["delivery_answer_sha256"], checked["answer_sha256"])
        saved = self.exported()["runs"]["evidence-fixture"]["result"]["answers"]
        self.assertEqual(saved, {"delivery_sha256": checked["answer_sha256"]})

    def test_timeout_stops_the_owned_worker_and_does_not_commit_a_finished_run(self):
        result, output = self.run_worker("timed-out", mode="timeout", success=False)
        self.assertIs(result["accepted_host_completion"], False)
        self.assertEqual(self.exported()["runs"]["timed-out"]["status"], "started")
        supplied = json.loads((output / "worker-input.json").read_text(encoding="utf-8"))
        pid = int((Path(supplied["artifact_dir"]) / "worker-pid.txt").read_text(encoding="utf-8"))
        if os.name == "posix":
            with self.assertRaises(ProcessLookupError):
                os.kill(pid, 0)
        receipt = json.loads((output / "host-receipt.json").read_text(encoding="utf-8"))
        self.assertIs(receipt["accepted_host_completion"], False)

    def test_missing_learning_without_diagnostic_stays_unaccepted_with_repair_request(self):
        result, output = self.run_worker("missing-learning", mode="missinglearning", success=False)
        self.assertEqual(set(result["step_missing"]), {"learning", "lesson_cards"})
        self.assertEqual(result["diagnostic_attempts"], 0)
        self.assertTrue((output / "repair-request.json").exists())
        self.assertEqual(self.exported()["runs"]["missing-learning"]["status"], "started")

    def test_one_diagnostic_repairs_only_missing_learning_fields_and_commits(self):
        result, output = self.run_worker("repaired-learning", mode="missinglearning", diagnostic="valid")
        self.assertIs(result["accepted_host_completion"], True)
        self.assertEqual(result["diagnostic_attempts"], 1)
        self.assertEqual(set(result["step_repaired"]), {"learning", "lesson_cards"})
        original = json.loads((output / "worker-stdout.json").read_text())
        state_result = self.exported()["runs"]["repaired-learning"]["result"]
        self.assertEqual(state_result["answers"], original["answers"])
        self.assertEqual(state_result["learning"]["decision"], "no_change")

    def test_diagnostic_cannot_rewrite_answers_or_retry_after_bad_repair(self):
        result, _ = self.run_worker("invalid-repair", mode="missinglearning", diagnostic="invalid", success=False)
        self.assertEqual(result["diagnostic_attempts"], 1)
        self.assertIs(result["accepted_host_completion"], False)
        self.assertEqual(self.exported()["runs"]["invalid-repair"]["status"], "started")

    def test_diagnostic_timeout_respects_remaining_original_deadline(self):
        result, _ = self.run_worker("repair-timeout", mode="missinglearning", diagnostic="timeout", success=False)
        self.assertEqual(result["diagnostic_attempts"], 1)
        self.assertIs(result["timed_out"], True)
        self.assertLess(result["elapsed_seconds"], 2)
        self.assertEqual(self.exported()["runs"]["repair-timeout"]["status"], "started")


if __name__ == "__main__":
    unittest.main()
