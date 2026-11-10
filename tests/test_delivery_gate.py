"""Synthetic integrity fixtures; these tests do not certify research truth."""
import copy
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import delivery_gate as gate


def make_fixture(root, run_id="fixture", begin_hash="a" * 64):
    def file(name, text):
        path = root / name
        path.write_text(text, encoding="utf-8")
        return {"path": name, "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
    answer = file("answer.md", "Synthetic claim, not a real research result. [Source](https://example.org/source)\n")
    draft = file("draft.md", "Synthetic draft.\n")
    receipt = file("receipt.json", '{"synthetic":true}')
    source = file("source.txt", "SYNTHETIC SOURCE: fixture for record validation only.")
    return {"schema": gate.SCHEMA, "run_id": run_id, "begin_sha256": begin_hash,
            "answer": answer,
            "task_clarity": {"decision": "ready", "goal": "SYNTHETIC validation",
                             "unresolved_ambiguities": [], "checked_at": "2026-11-09T00:00:00Z"},
            "queries": [{"language": lang, "query": lang + " synthetic query",
                         "executed_at": "2026-11-09T00:01:00Z", "receipt": receipt}
                        for lang in sorted(gate.LANGUAGES)],
            "sources": [{"id": "s1", "url": "https://example.org/source",
                         "type": "primary_source", "read_state": "read", "language": "EN",
                         "read_at": "2026-11-09T00:02:00Z", "scope": "Synthetic fixture only",
                         "evidence": source}],
            "claims": [{"id": "c1", "text": "Synthetic claim", "type": "fact", "source_ids": ["s1"]}],
            "practitioner_check": {"status": "not_applicable", "reason": "Synthetic fixture"},
            "writing": {"method": "Humanizer", "version": "3.1.0", "editor": "fixture-editor",
                        "draft": draft, "final_sha256": answer["sha256"],
                        "semantic_review": {"reviewer": "fixture-reviewer", "full_text_checked": True,
                                            "factual_changes_resolved": True, "invariants": ["Synthetic status"]}},
            "review": {"reviewer": "fixture-reviewer", "answer_claim_coverage_checked": True,
                       "material_citations_checked": True, "source_entailment_checked": True,
                       "unresolved_critical": []}}


class DeliveryRecords(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.data = make_fixture(self.root)
        self.manifest = self.root / "delivery-manifest.json"

    def check(self):
        self.manifest.write_text(json.dumps(self.data), encoding="utf-8")
        return gate.validate(self.manifest, "fixture", "a" * 64)

    def test_valid_records_pass_without_claiming_truth_or_improvement(self):
        result = self.check()
        self.assertTrue(result["evidence_contract_passed"])
        self.assertFalse(result["factual_quality_certified"])
        self.assertFalse(result["improvement_proven"])

    def test_missing_language_is_refused(self):
        self.data["queries"].pop()
        with self.assertRaisesRegex(gate.Invalid, "coverage"):
            self.check()

    def test_snippet_cannot_stand_in_for_read_source(self):
        self.data["sources"][0]["read_state"] = "snippet"
        with self.assertRaisesRegex(gate.Invalid, "snippet"):
            self.check()

    def test_unsupported_fact_is_refused(self):
        self.data["claims"][0]["source_ids"] = []
        with self.assertRaisesRegex(gate.Invalid, "lacks read evidence"):
            self.check()

    def test_secondary_source_alone_cannot_certify_a_fact(self):
        self.data["sources"][0]["type"] = "secondary_source"
        with self.assertRaisesRegex(gate.Invalid, "primary support"):
            self.check()

    def test_source_byte_change_is_refused(self):
        (self.root / "source.txt").write_text("Changed", encoding="utf-8")
        with self.assertRaisesRegex(gate.Invalid, "bytes changed"):
            self.check()

    def test_answer_edit_after_writing_review_is_refused(self):
        (self.root / "answer.md").write_text("New answer", encoding="utf-8")
        self.data["answer"]["sha256"] = hashlib.sha256((self.root / "answer.md").read_bytes()).hexdigest()
        with self.assertRaisesRegex(gate.Invalid, "does not cover"):
            self.check()

    def test_unresolved_task_cannot_pass(self):
        self.data["task_clarity"]["unresolved_ambiguities"] = ["Which device?"]
        with self.assertRaisesRegex(gate.Invalid, "ambiguity"):
            self.check()

    def test_preflight_after_search_is_refused(self):
        self.data["task_clarity"]["checked_at"] = "2026-11-09T01:00:00Z"
        with self.assertRaisesRegex(gate.Invalid, "after research"):
            self.check()

    def test_reference_cannot_escape_its_job_directory(self):
        self.data["answer"]["path"] = "../outside.md"
        with self.assertRaisesRegex(gate.Invalid, "escapes"):
            self.check()

    def test_symlinked_manifest_cannot_redefine_the_job_root(self):
        with tempfile.TemporaryDirectory() as other:
            outside = Path(other)
            data = make_fixture(outside)
            external_manifest = outside / "delivery-manifest.json"
            external_manifest.write_text(json.dumps(data), encoding="utf-8")
            self.manifest.symlink_to(external_manifest)
            with self.assertRaisesRegex(gate.Invalid, "symbolic link"):
                gate.validate(self.manifest, "fixture", "a" * 64, self.root)

    def test_host_supplied_job_root_is_not_replaced_by_another_directory(self):
        self.manifest.write_text(json.dumps(self.data), encoding="utf-8")
        with tempfile.TemporaryDirectory() as other:
            with self.assertRaisesRegex(gate.Invalid, "supplied job directory"):
                gate.validate(self.manifest, "fixture", "a" * 64, Path(other))

    def test_missing_semantic_review_is_refused(self):
        self.data["writing"]["semantic_review"]["full_text_checked"] = False
        with self.assertRaisesRegex(gate.Invalid, "incomplete"):
            self.check()

    def test_wrong_run_binding_is_refused(self):
        self.data["run_id"] = "different"
        with self.assertRaisesRegex(gate.Invalid, "different run"):
            self.check()

    def test_unresolved_review_objection_is_refused(self):
        self.data["review"]["unresolved_critical"] = ["Source contradicts claim"]
        with self.assertRaisesRegex(gate.Invalid, "critical"):
            self.check()

    def test_structured_trial_fields_require_review_and_remain_byte_bound(self):
        raw = b'{"current_status":"synthetic"}'
        (self.root / "evaluation.json").write_bytes(raw)
        self.data["evaluation_fields"] = {"path": "evaluation.json", "sha256": hashlib.sha256(raw).hexdigest()}
        with self.assertRaisesRegex(gate.Invalid, "not included"):
            self.check()
        self.data["review"]["evaluation_fields_checked"] = True
        self.assertEqual(self.check()["evaluation_fields"], {"current_status": "synthetic"})
        (self.root / "evaluation.json").write_bytes(b'{"current_status":"changed"}')
        with self.assertRaisesRegex(gate.Invalid, "bytes changed"):
            self.check()


if __name__ == "__main__":
    unittest.main()
