"""CLI contract tests using synthetic data, with no network or research claims.

Run: python -m unittest discover -s tests -v
"""
import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "research_gate.py"
LANGUAGES = ("EN", "DE", "ZH", "JA")


def query(language="EN", text="agent procedural memory", executed=True):
    return {"language": language, "query": text, "method": "M01", "executed": executed}


def assessment():
    context = {"environment_id": "test-environment", "model_id": "test-model",
               "evaluator_id": "test-evaluator", "split_id": "test-split"}
    evidence = ["receipt:SYNTHETIC-NOT-AN-EXPERIMENT"]
    data = {
        "data_status": "SYNTHETIC", "author_id": "test-author",
        "baseline": {"version": "v1", "sha256": "a" * 64},
        "candidate": {"version": "v2", "sha256": "b" * 64},
        "evaluator": {"id": "test-evaluator", "trusted": True, "external": True,
                      "self_assessment": False, "evidence": evidence},
        "context": context,
        "split": {"id": "test-split", "dev_ids": ["development-task"],
                  "test_ids": ["held-out-task"], "test_used_for_tuning": False},
        "budget": {"unit": "tokens", "baseline": 1000, "candidate": 1000},
        "objective": {"kind": "quality", "min_gain": 0.1,
                      "declared_before_test": True, "evidence": evidence},
        "audits": [{"role": role, "auditor_id": "test-" + role,
                    "independent_initial": True, "self_assessment": False,
                    "finding": "Synthetic audit fixture.", "evidence": evidence}
                   for role in ("optimism", "skepticism", "conservative", "innovative")],
        "pairs": [{"task_id": "held-out-task", "new_task": True,
                   "critical_regression": False}],
    }
    for arm, score in (("baseline", 0.5), ("candidate", 0.7)):
        data["pairs"][0][arm] = {"version": data[arm]["version"], "context": context.copy(),
                                  "quality": score, "cost": 500, "evidence": evidence}
    return data


class GateCLI(unittest.TestCase):
    def invoke(self, command, data=None, raw=None, code=0):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "input.json"
            path.write_text(raw if raw is not None else json.dumps(data, ensure_ascii=False),
                            encoding="utf-8")
            process = subprocess.run([sys.executable, str(SCRIPT), command, str(path)],
                                     capture_output=True, text=True, timeout=10)
        self.assertEqual(process.returncode, code, process.stdout + process.stderr)
        self.assertEqual(process.stderr, "")
        output = json.loads(process.stdout)
        self.assertIs(output["improvement_proven"], False)
        self.assertEqual(output["evidence_scope"], "input_assertions_only")
        self.assertIs(output["structural_eligibility"], code == 0)
        if code:
            self.assertTrue(output["errors"])
        return output

    def test_legacy_rows_remain_accepted(self):
        result = self.invoke("coverage", {"queries": [query()]})
        self.assertEqual(result["per_language"]["EN"]["recorded_executed_unique"], 1)
        self.assertIs(result["language_coverage_complete"], False)
        self.assertIs(result["deep_profile_minimum_met"], False)
        self.assertNotIn("metadata", result)

    def test_empty_journal_is_structural_success_not_coverage_success(self):
        result = self.invoke("coverage", {"queries": []})
        self.assertIs(result["language_coverage_complete"], False)
        self.assertIs(result["deep_profile_minimum_met"], False)
        self.assertIs(result["counts_are_execution_proof"], False)

    def test_enriched_rows_and_unverified_metadata(self):
        row = query()
        row.update({"timestamp": "2026-11-09T01:12:30.123+02:00",
                    "result_urls": ["https://example.org/paper?q=agent#code"],
                    "evidence": ["receipt:search-batch-1", "https://example.org/source"],
                    "notes": "Results belong to one combined search batch.",
                    "query_id": "q-1", "source_batch": "batch-1"})
        metadata = {"purpose": "synthetic test", "extension": {"allowed": [1, None, True]}}
        result = self.invoke("coverage", {"queries": [row], "metadata": metadata})
        self.assertEqual(result["metadata"], metadata)
        self.assertEqual(result["metadata_scope"], "unverified_passthrough")

    def test_valid_timestamp_forms_and_empty_results(self):
        for value in ("2026-11-09T01:12:30Z", "2026-11-09T01:12Z",
                      "2026-11-09T01:12:30-05:30", "2024-02-29T23:59:59.123456+00:00"):
            with self.subTest(timestamp=value):
                row = query()
                row.update({"timestamp": value, "result_urls": [], "notes": ""})
                self.invoke("coverage", {"queries": [row]})

    def test_malformed_timestamps_rejected(self):
        values = (None, 17, "", "2026-11-09", "2026-11-09T01:12:30",
                  "2026-11-09 01:12:30Z", "2026-02-29T01:12:30Z",
                  "2026-11-09T24:00:00Z", "2026-11-09T01:99:30Z",
                  "2026-11-09T01:12:30+24:00", "2026-11-09T01:12:30+00:99")
        for value in values:
            with self.subTest(timestamp=value):
                row = query()
                row["timestamp"] = value
                self.invoke("coverage", {"queries": [row]}, code=1)

    def test_malformed_result_urls_rejected(self):
        values = ("https://example.org", [None], ["relative/path"], ["ftp://example.org"],
                  ["https://"], ["https://example.org/a b"], ["https://example.org\t"],
                  ["https://example.org:bad"], ["https://example.org:65536"],
                  ["http://[invalid"], ["https://example.org\\path"], ["receipt:batch-1"])
        for value in values:
            with self.subTest(urls=value):
                row = query()
                row["result_urls"] = value
                self.invoke("coverage", {"queries": [row]}, code=1)

    def test_executed_requires_boolean(self):
        for value in (0, 1, "false", "true", None):
            with self.subTest(executed=value):
                self.invoke("coverage", {"queries": [query(executed=value)]}, code=1)

    def test_optional_field_types_and_evidence_are_checked(self):
        for field, value in (("notes", []), ("query_id", ""), ("source_batch", 3),
                             ("evidence", []), ("evidence", ["receipt:"]),
                             ("evidence", ["receipt:has space"]),
                             ("evidence", ["not-a-reference"])):
            with self.subTest(field=field, value=value):
                row = query()
                row[field] = value
                self.invoke("coverage", {"queries": [row]}, code=1)

    def test_unknown_top_and_row_fields_rejected(self):
        self.invoke("coverage", {"queries": [], "verified": True}, code=1)
        row = query()
        row["result_url"] = "https://example.org"
        result = self.invoke("coverage", {"queries": [row]}, code=1)
        self.assertIn("result_url", result["errors"][0])

    def test_metadata_must_be_an_object_with_finite_json_values(self):
        for value in (None, [], "metadata"):
            with self.subTest(metadata=value):
                self.invoke("coverage", {"queries": [], "metadata": value}, code=1)
        self.invoke("coverage", raw='{"queries": [], "metadata": {"overflow": 1e999}}', code=1)

    def test_duplicate_queries_normalize_unicode_case_and_whitespace(self):
        rows = [query(text="  Agent   SKILL "), query(text="Ａｇｅｎｔ skill", executed=False),
                query(text="agent skill"), query("DE", text="agent skill")]
        rows[2]["method"] = "M19"
        result = self.invoke("coverage", {"queries": rows})
        self.assertEqual(result["per_language"]["EN"]["unique_queries"], 1)
        self.assertEqual(result["per_language"]["EN"]["recorded_executed_unique"], 1)
        self.assertEqual(result["per_language"]["DE"]["recorded_executed_unique"], 1)
        self.assertEqual(result["duplicates"][0]["row_indices"], [0, 1, 2])
        self.assertEqual(result["per_language"]["EN"]["method_rows"]["M19"], 1)

    def test_thresholds_count_executed_unique_queries_in_each_language(self):
        rows = [query(lang) for lang in LANGUAGES]
        result = self.invoke("coverage", {"queries": rows * 30})
        self.assertIs(result["language_coverage_complete"], True)
        self.assertIs(result["deep_profile_minimum_met"], False)
        rows = [query(lang, text="synthetic query " + str(i))
                for lang in LANGUAGES for i in range(30)]
        rows[-1]["executed"] = False
        result = self.invoke("coverage", {"queries": rows})
        self.assertIs(result["deep_profile_minimum_met"], False)
        rows[-1]["executed"] = True
        result = self.invoke("coverage", {"queries": rows})
        self.assertIs(result["deep_profile_minimum_met"], True)

    def test_unknown_languages_and_methods_rejected(self):
        for field, value in (("language", "FR"), ("method", "M20"), ("method", "mechanism")):
            with self.subTest(field=field, value=value):
                row = query()
                row[field] = value
                self.invoke("coverage", {"queries": [row]}, code=1)

    def test_duplicate_json_keys_rejected(self):
        self.invoke("coverage", raw='{"queries": [], "queries": []}', code=1)
        self.invoke("coverage", raw='{"queries": [], "metadata": {"x": 1, "x": 2}}', code=1)

    def test_nonfinite_json_literals_and_syntax_errors_rejected(self):
        for raw in ('{"queries": [], "metadata": {"x": NaN}}',
                    '{"queries": [], "metadata": {"x": Infinity}}', '{broken'):
            with self.subTest(raw=raw):
                self.invoke("coverage", raw=raw, code=1)

    def test_quality_comparison_and_auditor_disagreement(self):
        data = assessment()
        data["audits"][1]["finding"] = "I object; the input assertions remain unverified."
        result = self.invoke("compare", data)
        self.assertAlmostEqual(result["recorded_quality_gain"], 0.2)
        self.assertEqual(result["data_status"], "SYNTHETIC")

    def test_cost_comparison_rejects_quality_loss(self):
        data = assessment()
        data["objective"]["kind"] = "cost"
        data["pairs"][0]["candidate"].update({"cost": 400, "quality": 0.5})
        result = self.invoke("compare", data)
        self.assertAlmostEqual(result["recorded_cost_reduction"], 0.2)
        data["pairs"][0]["candidate"]["quality"] = 0.4
        self.invoke("compare", data, code=1)

    def test_self_assessment_and_nonboolean_flags_rejected(self):
        for value in (True, "false", 0):
            with self.subTest(value=value):
                data = assessment()
                data["evaluator"]["self_assessment"] = value
                self.invoke("compare", data, code=1)
        data = assessment()
        data["evaluator"]["id"] = data["author_id"]
        self.invoke("compare", data, code=1)

    def test_invalid_auditor_id_roles_and_flags_rejected(self):
        for edit in ("author", "duplicate", "missing_role", "self", "not_independent"):
            with self.subTest(edit=edit):
                data = assessment()
                if edit == "author":
                    data["audits"][0]["auditor_id"] = data["author_id"]
                elif edit == "duplicate":
                    data["audits"][1]["auditor_id"] = data["audits"][0]["auditor_id"]
                elif edit == "missing_role":
                    data["audits"].pop()
                elif edit == "self":
                    data["audits"][0]["self_assessment"] = True
                else:
                    data["audits"][0]["independent_initial"] = False
                self.invoke("compare", data, code=1)

    def test_development_test_overlap_and_reuse_rejected(self):
        data = assessment()
        data["split"]["dev_ids"].append("held-out-task")
        self.invoke("compare", data, code=1)
        data = assessment()
        data["split"]["test_used_for_tuning"] = True
        self.invoke("compare", data, code=1)

    def test_unequal_exceeded_and_nonpositive_budgets_rejected(self):
        data = assessment()
        data["budget"]["candidate"] = 2000
        self.invoke("compare", data, code=1)
        data = assessment()
        data["pairs"][0]["candidate"]["cost"] = 1001
        self.invoke("compare", data, code=1)
        for value in (0, -1, True):
            with self.subTest(budget=value):
                data = assessment()
                data["budget"].update({"baseline": value, "candidate": value})
                self.invoke("compare", data, code=1)

    def test_critical_regression_rejected(self):
        data = assessment()
        data["pairs"][0]["critical_regression"] = True
        self.invoke("compare", data, code=1)

    def test_changed_version_hash_and_fixed_context_required(self):
        for edit in ("version", "hash", "context"):
            with self.subTest(edit=edit):
                data = assessment()
                if edit == "version":
                    data["candidate"]["version"] = data["baseline"]["version"]
                elif edit == "hash":
                    data["candidate"]["sha256"] = data["baseline"]["sha256"]
                else:
                    data["pairs"][0]["candidate"]["context"]["model_id"] = "other-model"
                self.invoke("compare", data, code=1)

    def test_test_set_requires_exact_unique_paired_coverage(self):
        data = assessment()
        data["split"]["test_ids"].append("unrun-task")
        self.invoke("compare", data, code=1)
        data = assessment()
        data["pairs"].append(copy.deepcopy(data["pairs"][0]))
        self.invoke("compare", data, code=1)

    def test_unknown_comparison_fields_and_no_gain_rejected(self):
        data = assessment()
        data["verified"] = True
        self.invoke("compare", data, code=1)
        data = assessment()
        data["pairs"][0]["candidate"]["quality"] = 0.5
        self.invoke("compare", data, code=1)

    def test_unreadable_input_returns_json_and_code_two(self):
        with tempfile.TemporaryDirectory() as directory:
            process = subprocess.run([sys.executable, str(SCRIPT), "coverage",
                                      str(Path(directory) / "does-not-exist.json")],
                                     capture_output=True, text=True, timeout=10)
        self.assertEqual(process.returncode, 2)
        output = json.loads(process.stdout)
        self.assertIs(output["structural_eligibility"], False)
        self.assertIs(output["improvement_proven"], False)

    def test_help_and_synthetic_example_are_explicit(self):
        process = subprocess.run([sys.executable, str(SCRIPT), "--help"],
                                 capture_output=True, text=True, timeout=10)
        self.assertEqual(process.returncode, 0)
        self.assertIn("Read-only structural checks", process.stdout)
        self.assertIn("deep_profile_minimum_met", process.stdout)
        self.assertIn("unknown fields rejected", process.stdout)
        process = subprocess.run([sys.executable, str(SCRIPT), "example"],
                                 capture_output=True, text=True, timeout=10)
        self.assertEqual(process.returncode, 0)
        data = json.loads(process.stdout)
        self.assertEqual(data["data_status"], "SYNTHETIC")
        self.invoke("compare", data)


if __name__ == "__main__":
    unittest.main()
