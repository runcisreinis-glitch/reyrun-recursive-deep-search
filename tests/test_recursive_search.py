"""Independent CLI lifecycle checks. All research tasks and grades are SYNTHETIC.

These tests exercise persistence, frozen evaluation, rejection and rollback.
They do not establish better research quality or authenticate an external agent.
"""
import copy
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "recursive_search.py"
METRICS = ("precision", "utility", "innovation", "clarity")
ROLES = ("optimism", "skepticism", "conservative", "innovative")


class RecursiveLifecycle(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.state = self.root / "state"
        self.sequence = 0
        self.policy = {
            "version": "synthetic-v1",
            "instructions": "SYNTHETIC policy: check the available project evidence.",
            "strategies": [{"id": "inspect-source", "scope": "code-readiness",
                            "instruction": "Record what the repository actually contains."}],
        }
        self.cli("init", {"owner_id": "synthetic-owner", "policy": self.policy})

    def cli(self, command, payload=None, success=True):
        arguments = [sys.executable, str(SCRIPT), "--state-dir", str(self.state), command]
        if payload is not None:
            self.sequence += 1
            path = self.root / ("input-" + str(self.sequence) + ".json")
            path.write_text(json.dumps(payload, ensure_ascii=False, allow_nan=False), encoding="utf-8")
            arguments.append(str(path))
        result = subprocess.run(arguments, capture_output=True, text=True, timeout=15)
        if success:
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        else:
            self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(result.stderr, "", result.stdout + result.stderr)
        data = json.loads(result.stdout)
        self.assertIs(data["improvement_proven"], False)
        return data

    def artifact(self, name, contents="SYNTHETIC local evidence fixture; not a research finding."):
        path = self.root / name
        path.write_text(contents, encoding="utf-8")
        return {"path": str(path), "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}

    def begin(self, run_id, scope="code-readiness"):
        return self.cli("begin", {
            "id": run_id, "task": "SYNTHETIC: classify available implementation evidence.",
            "scope": scope, "model_id": "synthetic-model", "environment_id": "synthetic-environment",
            "budget": {"unit": "synthetic-cost", "limit": 20},
        })

    def completion(self, start, answers=None, observations=None, metric=0.8):
        brief = start["brief"]
        if observations is None:
            observations = [{
                "id": "no-established-gain", "kind": "unknown",
                "text": "SYNTHETIC lifecycle exercise; no research improvement is established.",
                "evidence": [self.artifact("run-" + brief["run_id"] + ".txt")],
            }]
        return {
            "run_id": brief["run_id"], "begin_sha256": start["begin_sha256"],
            "answers": answers or {"note": "SYNTHETIC lifecycle fixture"},
            "metrics": {**{key: metric for key in METRICS}, "cost": 3},
            "observations": observations,
            "learning": {
                "diagnosis": "SYNTHETIC mechanism fixture, not evidence of research improvement.",
                "decision": "no_change", "hypothesis": "", "search_plan": [],
                "reason": "The fixture supplies no measured reason to change research policy.",
                "evidence_sha256": list(dict.fromkeys(ref["sha256"] for item in observations for ref in item["evidence"]))[:3],
            },
            "lesson_cards": [],
            "learning_use": [{"lesson_id": lesson_id, "status": "applied",
                              "reason": "SYNTHETIC explicit application assertion."}
                             for lesson_id in brief["loaded_lesson_ids"]],
            "strategy_use": [{"id": item["id"], "status": "applied",
                              "reason": "SYNTHETIC explicit strategy assertion."}
                             for item in brief["strategies"]],
        }

    def seed(self):
        first = self.begin("development-run")
        observed = {"id": "stale-readme", "kind": "failure",
                    "text": "SYNTHETIC: README status disagreed with an implementation file.",
                    "evidence": [self.artifact("observed.txt")]}
        self.cli("finish", self.completion(first, observations=[observed]))
        return first

    def candidate(self):
        first = self.seed()
        policy = copy.deepcopy(self.policy)
        policy["version"] = "synthetic-v2"
        policy["strategies"][0]["instruction"] = (
            "Check the concrete module, dependencies and tests when README status is stale.")
        self.cli("propose", {
            "id": "candidate-1", "author_id": "synthetic-author",
            "base_policy_sha256": first["brief"]["policy_sha256"], "policy": policy,
            "reason": "SYNTHETIC: test a source-inspection rule on different tasks.",
            "source_run_ids": ["development-run"],
        })
        return first

    def suite(self, dev_overlap=False):
        tasks = []
        for index in range(2):
            task_id = "development-run" if dev_overlap and index == 0 else "heldout-" + str(index)
            checks = [{"field": metric, "op": "equals", "expected": "correct-" + metric,
                       "metric": metric, "critical": metric == "clarity"} for metric in METRICS]
            tasks.append({"id": task_id, "prompt": "SYNTHETIC held-out task " + str(index),
                          "checks": checks})
        path = self.root / "external-suite.json"
        path.write_text(json.dumps({"id": "synthetic-suite", "tasks": tasks}), encoding="utf-8")
        return path

    def freeze(self, suite_path=None, evaluator="synthetic-evaluator", success=True):
        return self.cli("freeze", {
            "id": "trial-1", "candidate_id": "candidate-1", "evaluator_id": evaluator,
            "suite_path": str(suite_path or self.suite()), "dev_task_ids": ["development-run"],
            "model_id": "synthetic-model", "environment_id": "synthetic-environment",
            "budget": {"unit": "synthetic-cost", "limit": 20},
            "objective": {"metric": "precision", "min_gain": 0.25},
        }, success=success)

    def evaluate_payload(self, candidate_answers=None, candidate_metric=0.8):
        pairs = []
        for index in range(2):
            pair = {"task_id": "heldout-" + str(index)}
            for arm in ("baseline", "candidate"):
                run_id = arm + "-" + str(index)
                start = self.cli("begin", {"id": run_id, "trial_id": "trial-1",
                                            "task_id": pair["task_id"], "arm": arm})
                # Neither oracle answers nor full checks may be injected into the actor's brief.
                encoded = json.dumps(start["brief"])
                self.assertNotIn("correct-precision", encoded)
                self.assertNotIn('"expected"', encoded)
                answers = {metric: "correct-" + metric for metric in METRICS}
                if arm == "baseline":
                    answers["precision"] = "incorrect-precision"
                elif candidate_answers:
                    answers.update(candidate_answers)
                self.cli("finish", self.completion(start, answers=answers,
                                                     metric=candidate_metric if arm == "candidate" else 0.8))
                pair[arm + "_run_id"] = run_id
            pairs.append(pair)
        audits = [{"role": role, "auditor_id": "synthetic-reviewer-" + role,
                   **self.artifact("audit-" + role + ".txt", "SYNTHETIC independent-role fixture: " + role),
                   "finding": "SYNTHETIC fixture finding for " + role,
                   "unresolved_critical": False}
                  for role in ROLES]
        return {"trial_id": "trial-1", "evaluator_id": "synthetic-evaluator", "pairs": pairs, "audits": audits}

    def promote(self, success=True):
        return self.cli("promote", {"trial_id": "trial-1", "evaluator_id": "synthetic-evaluator"}, success)

    def test_next_process_loads_previous_observation_without_promoting_policy(self):
        first = self.seed()
        second = self.begin("second-run")
        self.assertEqual(second["brief"]["policy_sha256"], first["brief"]["policy_sha256"])
        self.assertIn("development-run/stale-readme", second["brief"]["loaded_lesson_ids"])
        observation = next(item for item in second["brief"]["observations"]
                           if item["lesson_id"] == "development-run/stale-readme")
        self.assertIn("SYNTHETIC", observation["text"])
        self.assertEqual(observation["status"], "unvalidated_observation")

    def test_recent_learning_is_retained_by_completion_order_not_run_id_sort(self):
        older = self.begin("z-older-run")
        evidence = self.artifact("recency-fixture.txt")
        observations = [{
            "id": "old-" + str(index).zfill(2), "kind": "unknown",
            "text": "SYNTHETIC older observation " + str(index), "evidence": [evidence],
        } for index in range(16)]
        self.cli("finish", self.completion(older, observations=observations))
        newer = self.begin("a-newer-run")
        self.cli("finish", self.completion(newer, observations=[{
            "id": "newest", "kind": "unknown", "text": "SYNTHETIC newest observation.",
            "evidence": [evidence],
        }]))
        next_run = self.begin("next-learning-run")
        expected = ["z-older-run/old-" + str(index).zfill(2) for index in range(1, 16)]
        expected.append("a-newer-run/newest")
        self.assertEqual(next_run["brief"]["loaded_lesson_ids"], expected)

    def test_finish_requires_exact_begin_receipt_and_loaded_learning_acknowledgement(self):
        self.seed()
        start = self.begin("second-run")
        payload = self.completion(start)
        damaged = copy.deepcopy(payload)
        damaged["begin_sha256"] = "0" * 64
        self.cli("finish", damaged, success=False)
        damaged = copy.deepcopy(payload)
        damaged["learning_use"] = []
        self.cli("finish", damaged, success=False)
        damaged = copy.deepcopy(payload)
        damaged["strategy_use"] = []
        self.cli("finish", damaged, success=False)
        self.cli("finish", payload)
        self.cli("finish", payload, success=False)

    def test_changed_evidence_bytes_are_rejected_before_completion(self):
        start = self.begin("run-with-evidence")
        evidence = self.artifact("changing.txt")
        Path(evidence["path"]).write_text("Changed after its declared digest.", encoding="utf-8")
        payload = self.completion(start, observations=[{
            "id": "observation", "kind": "useful", "text": "SYNTHETIC evidence assertion.",
            "evidence": [evidence],
        }])
        self.cli("finish", payload, success=False)
        payload["observations"][0]["evidence"] = [self.artifact("replacement.txt")]
        payload["learning"]["evidence_sha256"] = [payload["observations"][0]["evidence"][0]["sha256"]]
        self.cli("finish", payload)

    def test_heldout_overlap_and_author_as_evaluator_are_rejected(self):
        self.candidate()
        self.freeze(self.suite(dev_overlap=True), success=False)
        self.freeze(self.suite(), evaluator="synthetic-author", success=False)
        self.freeze(self.suite())

    def test_suite_mutation_invalidates_the_frozen_trial(self):
        self.candidate()
        path = self.suite()
        self.freeze(path)
        payload = self.evaluate_payload()
        data = json.loads(path.read_text(encoding="utf-8"))
        data["tasks"][0]["checks"][0]["expected"] = "changed-gold"
        path.write_text(json.dumps(data), encoding="utf-8")
        self.cli("evaluate", payload, success=False)
        self.promote(success=False)

    def test_manual_high_grades_cannot_pass_a_failed_computed_benchmark(self):
        self.candidate()
        self.freeze()
        payload = self.evaluate_payload({"precision": "incorrect-precision"}, candidate_metric=1.0)
        # A completed evaluation can legitimately return a rejected verdict with exit zero.
        self.cli("evaluate", payload)
        self.promote(success=False)
        plan = self.cli("compact", {"mode": "plan"})
        self.cli("compact", {"mode": "apply", "plan_sha256": plan["plan_sha256"],
                             "acknowledge_raw_evidence_removal": True})
        retained = self.cli("export")["state"]
        self.assertEqual(retained["trials"]["trial-1"]["status"], "rejected")
        self.assertIn("candidate-1", retained["candidates"])
        self.assertEqual(self.begin("after-rejection")["brief"]["version"], "synthetic-v1")

    def test_clarity_regression_blocks_promotion_despite_precision_gain(self):
        self.candidate()
        self.freeze()
        payload = self.evaluate_payload({"clarity": "unclear-answer"})
        self.cli("evaluate", payload)
        self.promote(success=False)
        self.assertEqual(self.begin("after-clarity-rejection")["brief"]["version"], "synthetic-v1")

    def test_passed_computed_benchmark_promotes_then_rollback_changes_next_load(self):
        original = self.candidate()
        self.freeze()
        payload = self.evaluate_payload(candidate_metric=0.0)
        self.cli("evaluate", payload)
        self.promote()
        accepted = self.begin("after-acceptance")
        self.assertEqual(accepted["brief"]["version"], "synthetic-v2")
        self.assertNotEqual(accepted["brief"]["policy_sha256"], original["brief"]["policy_sha256"])
        self.assertEqual(accepted["brief"]["constitution"], original["brief"]["constitution"])
        self.assertEqual(accepted["brief"]["constitution_sha256"], original["brief"]["constitution_sha256"])
        self.cli("finish", self.completion(accepted))
        next_policy = copy.deepcopy(self.policy)
        next_policy["version"] = "synthetic-v3"
        next_policy["instructions"] = "SYNTHETIC next-generation candidate from accepted v2."
        proposal = {
            "id": "candidate-generation-3", "author_id": "synthetic-author",
            "base_policy_sha256": original["brief"]["policy_sha256"], "policy": next_policy,
            "reason": "SYNTHETIC check that a next generation must use the accepted base.",
            "source_run_ids": ["after-acceptance"],
        }
        self.cli("propose", proposal, success=False)
        proposal["base_policy_sha256"] = accepted["brief"]["policy_sha256"]
        self.cli("propose", proposal)
        plan = self.cli("compact", {"mode": "plan"})
        self.cli("compact", {"mode": "apply", "plan_sha256": plan["plan_sha256"],
                             "acknowledge_raw_evidence_removal": True})
        self.assertIn("candidate-generation-3", self.cli("export")["state"]["candidates"])
        self.cli("rollback", {"policy_sha256": original["brief"]["policy_sha256"],
                              "reason": "SYNTHETIC rollback check."})
        restored = self.begin("after-rollback")
        self.assertEqual(restored["brief"]["policy_sha256"], original["brief"]["policy_sha256"])

    def test_promotion_before_evaluation_is_rejected(self):
        self.candidate()
        self.freeze()
        self.promote(success=False)

    def test_repeated_auditor_identity_cannot_satisfy_independent_roles(self):
        self.candidate()
        self.freeze()
        payload = self.evaluate_payload()
        payload["audits"][1]["auditor_id"] = payload["audits"][0]["auditor_id"]
        self.cli("evaluate", payload, success=False)
        self.promote(success=False)

    def test_unresolved_critical_audit_objection_blocks_otherwise_passing_candidate(self):
        self.candidate()
        self.freeze()
        payload = self.evaluate_payload()
        payload["audits"][1]["finding"] = "SYNTHETIC unresolved critical objection."
        payload["audits"][1]["unresolved_critical"] = True
        result = self.cli("evaluate", payload)
        self.assertIs(result["eligible"], False)
        self.assertTrue(any("unresolved critical audit objection" in issue for issue in result["failures"]))
        self.promote(success=False)
        self.assertEqual(self.begin("after-critical-objection")["brief"]["version"], "synthetic-v1")

    def test_constitution_is_loaded_and_candidate_cannot_replace_its_fields(self):
        first = self.seed()
        self.assertEqual(first["brief"]["constitution"]["default_search_languages"], ["EN", "DE", "ZH", "JA"])
        replacement = copy.deepcopy(self.policy)
        replacement["version"] = "synthetic-invalid-policy"
        replacement["constitution"] = {"default_search_languages": ["EN"]}
        self.cli("propose", {
            "id": "invalid-constitution-candidate", "author_id": "synthetic-author",
            "base_policy_sha256": first["brief"]["policy_sha256"], "policy": replacement,
            "reason": "SYNTHETIC attempted change to fixed fields.", "source_run_ids": ["development-run"],
        }, success=False)
        next_run = self.begin("after-invalid-constitution")
        self.assertEqual(next_run["brief"]["constitution_sha256"], first["brief"]["constitution_sha256"])

    def test_null_quality_metrics_are_explicitly_unevaluated_and_do_not_control_acceptance(self):
        self.candidate()
        self.freeze()
        payload = self.evaluate_payload(candidate_metric=None)
        result = self.cli("evaluate", payload)
        self.assertIs(result["eligible"], True)
        self.assertEqual(result["computed_scores"]["candidate"]["precision"], 1.0)
        self.promote()

    def test_exceeded_budget_is_rejected_at_finish(self):
        start = self.begin("over-budget")
        payload = self.completion(start)
        payload["metrics"]["cost"] = 21
        self.cli("finish", payload, success=False)
        payload["metrics"]["cost"] = 20
        self.cli("finish", payload)

    def test_reinitialization_does_not_erase_existing_history(self):
        first = self.seed()
        self.cli("init", {"owner_id": "different-owner", "policy": self.policy}, success=False)
        next_run = self.begin("still-intact")
        self.assertEqual(next_run["brief"]["policy_sha256"], first["brief"]["policy_sha256"])
        self.assertIn("development-run/stale-readme", next_run["brief"]["loaded_lesson_ids"])

    def test_development_sources_cannot_be_omitted_from_frozen_split(self):
        self.candidate()
        self.cli("freeze", {
            "id": "trial-1", "candidate_id": "candidate-1", "evaluator_id": "synthetic-evaluator",
            "suite_path": str(self.suite(dev_overlap=True)), "dev_task_ids": ["unrelated-development-id"],
            "model_id": "synthetic-model", "environment_id": "synthetic-environment",
            "budget": {"unit": "synthetic-cost", "limit": 20},
            "objective": {"metric": "precision", "min_gain": 0.25},
        }, success=False)

    def test_evaluated_tasks_cannot_be_relabelled_as_fresh_heldout(self):
        self.candidate()
        path = self.suite()
        self.freeze(path)
        self.cli("evaluate", self.evaluate_payload())
        self.cli("freeze", {
            "id": "reused-trial", "candidate_id": "candidate-1", "evaluator_id": "synthetic-evaluator",
            "suite_path": str(path), "dev_task_ids": ["development-run"],
            "model_id": "synthetic-model", "environment_id": "synthetic-environment",
            "budget": {"unit": "synthetic-cost", "limit": 20},
            "objective": {"metric": "precision", "min_gain": 0.25},
        }, success=False)
        aliased = json.loads(path.read_text(encoding="utf-8"))
        aliased["id"] = "renamed-suite"
        for task in aliased["tasks"]:
            task["id"] = "renamed-" + task["id"]
        renamed_path = self.root / "renamed-suite.json"
        renamed_path.write_text(json.dumps(aliased), encoding="utf-8")
        self.cli("freeze", {
            "id": "renamed-trial", "candidate_id": "candidate-1", "evaluator_id": "synthetic-evaluator",
            "suite_path": str(renamed_path), "dev_task_ids": ["development-run"],
            "model_id": "synthetic-model", "environment_id": "synthetic-environment",
            "budget": {"unit": "synthetic-cost", "limit": 20},
            "objective": {"metric": "precision", "min_gain": 0.25},
        }, success=False)

    def test_no_posthoc_best_of_repeated_trial_runs(self):
        self.candidate()
        self.freeze()
        payload = {"id": "first-attempt", "trial_id": "trial-1", "task_id": "heldout-0", "arm": "candidate"}
        self.cli("begin", payload)
        payload["id"] = "second-attempt-same-case"
        self.cli("begin", payload, success=False)

    def test_existing_transaction_lock_does_not_mutate_history(self):
        original = (self.state / "state.json").read_bytes()
        lock = self.state / "transaction.lock"
        lock.write_text('{"pid": 99999999, "test": "SYNTHETIC held lock"}', encoding="utf-8")
        self.cli("begin", {
            "id": "blocked-run", "task": "SYNTHETIC lock test", "scope": "code-readiness",
            "model_id": "synthetic-model", "environment_id": "synthetic-environment",
            "budget": {"unit": "synthetic-cost", "limit": 20},
        }, success=False)
        self.assertEqual((self.state / "state.json").read_bytes(), original)
        self.assertTrue(lock.exists())
        lock.unlink()  # Only our synthetic fixture's lock; no production lock recovery.
        self.begin("after-lock-release")

    def test_injected_atomic_replace_failure_preserves_previous_state(self):
        original = (self.state / "state.json").read_bytes()
        payload = {
            "id": "interrupted-run", "task": "SYNTHETIC atomic-write fault test", "scope": "code-readiness",
            "model_id": "synthetic-model", "environment_id": "synthetic-environment",
            "budget": {"unit": "synthetic-cost", "limit": 20},
        }
        path = self.root / "interrupted-input.json"
        path.write_text(json.dumps(payload), encoding="utf-8")
        injection = (
            "import os, runpy, sys\n"
            "def fail_replace(*args, **kwargs):\n"
            "    raise OSError('SYNTHETIC injected atomic-replace failure')\n"
            "os.replace = fail_replace\n"
            "sys.argv = sys.argv[1:]\n"
            "runpy.run_path(sys.argv[0], run_name='__main__')\n"
        )
        result = subprocess.run(
            [sys.executable, "-c", injection, str(SCRIPT), "--state-dir", str(self.state), "begin", str(path)],
            capture_output=True, text=True, timeout=15,
        )
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIs(json.loads(result.stdout)["improvement_proven"], False)
        self.assertEqual((self.state / "state.json").read_bytes(), original)
        self.assertFalse((self.state / "transaction.lock").exists())
        self.cli("begin", payload)

    def test_learning_decision_needs_evidence_and_four_language_improvement_plan(self):
        started = self.begin("learning-contract")
        valid = self.completion(started)
        broken = copy.deepcopy(valid)
        broken.pop("learning")
        self.cli("finish", broken, success=False)
        broken = copy.deepcopy(valid)
        broken["learning"]["reason"] = ""
        self.cli("finish", broken, success=False)
        broken = copy.deepcopy(valid)
        broken["learning"]["evidence_sha256"] = ["0" * 64]
        self.cli("finish", broken, success=False)
        valid["learning"].update(decision="test_improvement", hypothesis="SYNTHETIC concrete test hypothesis.")
        self.cli("finish", valid, success=False)
        valid["learning"]["search_plan"] = [{"language": lang, "query": "SYNTHETIC " + lang + " mechanism search"}
                                            for lang in ("EN", "DE", "ZH", "JA")]
        broken = copy.deepcopy(valid)
        broken["learning"]["research_evidence"] = [{
            "language": "EN", "query": "SYNTHETIC incomplete actual-search record",
            "evidence_sha256": valid["learning"]["evidence_sha256"]}]
        self.cli("finish", broken, success=False)
        result = self.cli("finish", valid)
        self.assertIs(result["improvement_research_recorded"], False)
        self.assertEqual(result["learning_decision"], "test_improvement")

    def test_compact_cards_deduplicate_normalized_text_and_remain_scoped(self):
        card = {"trigger": "Stale README", "context": "SYNTHETIC source inspection",
                "tactic": "Read the implementation module", "outcome": "failure",
                "next_test": "Check another repository under the same budget."}
        saved_ids = []
        for run_id, scope, normalized in (("card-first", "scope-a", False), ("card-second", "scope-a", True),
                                           ("card-other-scope", "scope-b", False)):
            start = self.begin(run_id, scope=scope)
            payload = self.completion(start)
            supplied = copy.deepcopy(card)
            if normalized:
                supplied["trigger"] = "  STALE   readme  "
            supplied["evidence_sha256"] = payload["learning"]["evidence_sha256"]
            payload["lesson_cards"] = [supplied]
            saved_ids.append(self.cli("finish", payload)["lesson_card_ids"][0])
        self.assertEqual(saved_ids[0], saved_ids[1])
        self.assertNotEqual(saved_ids[0], saved_ids[2])
        state = self.cli("export")["state"]
        self.assertEqual(len(state["lesson_cards"]), 2)
        self.assertEqual(state["lesson_cards"][saved_ids[0]]["occurrences"], 2)
        loaded_a = self.begin("load-scope-a", scope="scope-a")["brief"]["loaded_lesson_ids"]
        loaded_b = self.begin("load-scope-b", scope="scope-b")["brief"]["loaded_lesson_ids"]
        self.assertEqual(loaded_a, ["card-first/no-established-gain", "card-second/no-established-gain", saved_ids[0]])
        self.assertEqual(loaded_b, ["card-other-scope/no-established-gain", saved_ids[2]])

    def test_old_card_does_not_hide_newer_failure_without_a_card(self):
        first = self.begin("older-card")
        payload = self.completion(first)
        payload["lesson_cards"] = [{
            "trigger": "SYNTHETIC relevant task", "context": "Earlier successful conditions",
            "tactic": "Use the earlier tactic", "outcome": "success",
            "next_test": "Check contrary evidence from subsequent runs.",
            "evidence_sha256": payload["learning"]["evidence_sha256"],
        }]
        saved = self.cli("finish", payload)
        second = self.begin("newer-failure")
        failed = {"id": "contrary-result", "kind": "failure",
                  "text": "SYNTHETIC newer evidence: the earlier tactic fails in these conditions.",
                  "evidence": [self.artifact("newer-failure.txt", "SYNTHETIC actual contrary fixture.")]}
        self.cli("finish", self.completion(second, observations=[failed]))
        next_run = self.begin("after-failure")
        ids = next_run["brief"]["loaded_lesson_ids"]
        self.assertIn(saved["lesson_card_ids"][0], ids)
        self.assertEqual(ids[-1], "newer-failure/contrary-result")
        self.assertEqual(next_run["brief"]["observations"][-1]["text"], failed["text"])
        self.assertEqual(next_run["brief"]["observations"][-1]["status"], "unvalidated_observation")

    def test_cards_and_observations_share_one_sixteen_item_recency_bound(self):
        started = self.begin("mixed-experience")
        evidence = self.artifact("mixed-evidence.txt")
        observed = [{"id": "observation-" + str(index).zfill(2), "kind": "failure",
                     "text": "SYNTHETIC observed limitation " + str(index), "evidence": [evidence]}
                    for index in range(16)]
        payload = self.completion(started, observations=observed)
        payload["lesson_cards"] = [{
            "trigger": "SYNTHETIC scope " + str(index), "context": "Bounded retrieval fixture",
            "tactic": "Record scoped evidence", "outcome": "inconclusive",
            "next_test": "Check a fresh task.", "evidence_sha256": [evidence["sha256"]],
        } for index in range(4)]
        saved = self.cli("finish", payload)
        loaded = self.begin("bounded-mixed-load")["brief"]["loaded_lesson_ids"]
        self.assertEqual(len(loaded), 16)
        self.assertEqual(loaded[:12], ["mixed-experience/observation-" + str(index).zfill(2)
                                      for index in range(4, 16)])
        self.assertEqual(loaded[12:], sorted(saved["lesson_card_ids"]))
        self.assertEqual(self.begin("unrelated-scope", scope="unrelated")["brief"]["loaded_lesson_ids"], [])

    def test_card_size_and_unobserved_evidence_are_rejected(self):
        started = self.begin("oversized-card")
        payload = self.completion(started)
        card = {"trigger": "x" * 490, "context": "y" * 490, "tactic": "z" * 490,
                "outcome": "inconclusive", "next_test": "n" * 490,
                "evidence_sha256": payload["learning"]["evidence_sha256"]}
        payload["lesson_cards"] = [card]
        result = self.cli("finish", payload, success=False)
        self.assertIn("1500", result["error"])
        for key in ("trigger", "context", "tactic", "next_test"):
            card[key] = "SYNTHETIC short " + key
        card["evidence_sha256"] = ["f" * 64]
        self.cli("finish", payload, success=False)
        card["evidence_sha256"] = payload["learning"]["evidence_sha256"]
        self.cli("finish", payload)

    def test_five_mib_cap_covers_objects_and_failed_state_commit(self):
        started = self.begin("capacity-check")
        original_state = (self.state / "state.json").read_bytes()
        cap = 5 * 1024 * 1024
        huge = self.artifact("oversized-evidence.txt", "x" * cap)
        payload = self.completion(started, observations=[{
            "id": "huge", "kind": "unknown", "text": "SYNTHETIC capacity fixture.", "evidence": [huge]}])
        self.cli("finish", payload, success=False)
        self.assertEqual((self.state / "state.json").read_bytes(), original_state)
        self.assertLessEqual(sum(path.stat().st_size for path in self.state.rglob("*") if path.is_file()), cap)
        payload = self.completion(started, answers={"bulk": "y" * cap})
        self.cli("finish", payload, success=False)
        self.assertEqual((self.state / "state.json").read_bytes(), original_state)
        self.assertLessEqual(sum(path.stat().st_size for path in self.state.rglob("*") if path.is_file()), cap)
        self.cli("finish", self.completion(started))

    def test_compaction_requires_current_manifest_and_ack_retains_open_run_and_hashes(self):
        completed = self.begin("compact-closed")
        raw = self.artifact("raw-evidence.txt", "SYNTHETIC raw evidence " * 4000)
        payload = self.completion(completed, answers={"verbose": "x" * 100000}, observations=[{
            "id": "closed-observation", "kind": "unknown", "text": "SYNTHETIC closed record.", "evidence": [raw]}])
        receipt = self.cli("finish", payload)
        before = (self.state / "state.json").read_bytes()
        plan = self.cli("compact", {"mode": "plan"})
        self.assertEqual((self.state / "state.json").read_bytes(), before)
        self.assertTrue(plan["raw_reproducibility_removed"])
        self.assertIn(raw["sha256"], [item["sha256"] for item in plan["remove_raw_objects"]])
        self.cli("compact", {"mode": "apply", "plan_sha256": plan["plan_sha256"],
                             "acknowledge_raw_evidence_removal": False}, success=False)
        opened = self.begin("compact-still-open", scope="different-open-scope")
        self.cli("compact", {"mode": "apply", "plan_sha256": plan["plan_sha256"],
                             "acknowledge_raw_evidence_removal": True}, success=False)
        plan = self.cli("compact", {"mode": "plan"})
        self.cli("compact", {"mode": "apply", "plan_sha256": plan["plan_sha256"],
                             "acknowledge_raw_evidence_removal": True})
        state = self.cli("export")["state"]
        closed = state["runs"]["compact-closed"]
        self.assertTrue(closed["compacted"])
        self.assertNotIn("answers", closed["result"])
        self.assertEqual(closed["result"]["answer_sha256"], receipt["answer_sha256"])
        self.assertEqual(state["runs"]["compact-still-open"]["brief"], opened["brief"])
        self.assertFalse((self.state / "objects" / raw["sha256"]).exists())
        self.assertLess((self.state / "state.json").stat().st_size, len(before))
        self.assertFalse(any("archive" in path.name or "backup" in path.name for path in self.state.rglob("*")))
        self.cli("finish", self.completion(opened))

    def test_compaction_recovers_near_capacity_orphan_without_raising_the_cap(self):
        started = self.begin("capacity-orphan")
        # Remove incidental savings in old event payloads before filling the
        # store. Recovery must reclaim the orphan, not rely on that spare space.
        for _ in range(2):
            plan = self.cli("compact", {"mode": "plan"})
            self.cli("compact", {"mode": "apply", "plan_sha256": plan["plan_sha256"],
                                  "acknowledge_raw_evidence_removal": True})
        original_state = (self.state / "state.json").read_bytes()
        cap = 5 * 1024 * 1024
        used = sum(path.stat().st_size for path in self.state.rglob("*") if path.is_file())
        huge = self.artifact("near-capacity-orphan.txt", "x" * (cap - used - 200))
        payload = self.completion(started, observations=[{
            "id": "large", "kind": "unknown", "text": "SYNTHETIC failed state transaction.",
            "evidence": [huge]}])
        refused = self.cli("finish", payload, success=False)
        self.assertIn("capacity exceeded", refused["error"])
        self.assertEqual((self.state / "state.json").read_bytes(), original_state)
        orphan = self.state / "objects" / huge["sha256"]
        self.assertTrue(orphan.exists())
        plan = self.cli("compact", {"mode": "plan"})
        self.assertIn(huge["sha256"], [item["sha256"] for item in plan["remove_raw_objects"]])
        result = self.cli("compact", {"mode": "apply", "plan_sha256": plan["plan_sha256"],
                                      "acknowledge_raw_evidence_removal": True})
        self.assertEqual(result["orphan_objects_removed_before_commit"], 1)
        self.assertFalse(orphan.exists())
        state = self.cli("export")["state"]
        self.assertEqual(state["runs"]["capacity-orphan"]["status"], "started")
        self.assertEqual(state["runs"]["capacity-orphan"]["brief"], started["brief"])
        self.assertLessEqual(sum(path.stat().st_size for path in self.state.rglob("*") if path.is_file()), cap)
        self.cli("finish", self.completion(started))

    def test_compaction_replace_failure_preserves_referenced_evidence_and_old_state(self):
        self.seed()
        exported = self.cli("export")["state"]
        reference = exported["runs"]["development-run"]["result"]["observations"][0]["evidence"][0]
        referenced_path = self.state / reference["object"]
        referenced_bytes = referenced_path.read_bytes()
        # Simulate an unreferenced object left by a previously interrupted
        # artifact transaction; no committed record owns these bytes.
        orphan_bytes = b"SYNTHETIC unreferenced failed-transaction object"
        orphan_path = self.state / "objects" / hashlib.sha256(orphan_bytes).hexdigest()
        orphan_path.write_bytes(orphan_bytes)
        plan = self.cli("compact", {"mode": "plan"})
        self.assertEqual(set(item["sha256"] for item in plan["remove_raw_objects"]),
                         {referenced_path.name, orphan_path.name})
        original_state = (self.state / "state.json").read_bytes()
        path = self.root / "interrupted-compact-input.json"
        path.write_text(json.dumps({"mode": "apply", "plan_sha256": plan["plan_sha256"],
                                    "acknowledge_raw_evidence_removal": True}), encoding="utf-8")
        injection = (
            "import os, runpy, sys\n"
            "def fail_replace(*args, **kwargs):\n"
            "    raise OSError('SYNTHETIC interrupted compaction state replacement')\n"
            "os.replace = fail_replace\n"
            "sys.argv = sys.argv[1:]\n"
            "runpy.run_path(sys.argv[0], run_name='__main__')\n"
        )
        result = subprocess.run(
            [sys.executable, "-c", injection, str(SCRIPT), "--state-dir", str(self.state), "compact", str(path)],
            capture_output=True, text=True, timeout=15)
        self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("interrupted compaction", json.loads(result.stdout)["error"])
        self.assertEqual((self.state / "state.json").read_bytes(), original_state)
        self.assertEqual(referenced_path.read_bytes(), referenced_bytes)
        self.assertFalse(orphan_path.exists())
        self.assertFalse((self.state / "transaction.lock").exists())
        self.assertEqual(self.cli("export")["state"], exported)
        # The acknowledged plan is now stale because the orphan was reclaimed;
        # a fresh plan can finish safely after the failed atomic replacement.
        plan = self.cli("compact", {"mode": "plan"})
        self.cli("compact", {"mode": "apply", "plan_sha256": plan["plan_sha256"],
                              "acknowledge_raw_evidence_removal": True})
        self.assertFalse(referenced_path.exists())


if __name__ == "__main__":
    unittest.main()
