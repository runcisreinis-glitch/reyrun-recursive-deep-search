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
    reports = []
    decisions = {}
    for role in sorted(gate.ROLES):
        instance = role + "-test-instance"
        report = file(role + "-report.json", json.dumps({
            "role": role, "instance_id": instance, "run_id": run_id, "answer_sha256": answer["sha256"],
            "finding": "Synthetic test finding for " + role, "alternative": "Test alternative for " + role,
            "verdict": "accept"}))
        dispatch = file(role + "-dispatch.json", json.dumps({
            "instance_id": instance, "run_id": run_id, "report_sha256": report["sha256"],
            "isolated_initial_review": True}))
        reports.append({"role": role, "instance_id": instance, "report": report, "dispatch_receipt": dispatch})
        decisions[role] = "Fixture reconciliation for " + role
    en = {"language": "EN", "query": "EN synthetic query"}
    transfers = [{"mechanism": "Fixture mechanism " + str(i), "domain": "Synthetic",
                  "adaptation_gap": "Synthetic gap", "falsification_test": "Synthetic test",
                  "result": "Not tested; schema fixture", "query": en} for i in (1, 2)]
    venue = {"url": "https://example.org/source", "name": "Synthetic professional venue",
             "type": "journal", "query": en, "status": "read", "finding": "Fixture", "source_ids": ["s1"]}
    professions = [{"profession": c + " test role", "category": c, "method": "Fixture method",
                    "venues": [dict(venue)]} for c in ("direct", "adjacent")]
    trail = []
    for i, stage in enumerate(("profession", "profession", "query", "venue_language", "validation", "practical_option")):
        trail.append({"id": str(i), "after": "user_question" if i == 0 else str(i-1), "stage": stage,
                      "observation": "Fixture finding " + str(i), "shared_principle": "Test principle",
                      "alternative": "Test option " + str(i), "test": "Test method", "outcome": "Fixture", "ordinary_approach": "Fixture baseline", "contribution": "Fixture delta",
                      "comparison_result": "adds_value", "anchor": {"kind": "question"} if i == 0 else {"kind": "query", "ref": en}})
        if stage == "profession":
            trail[-1]["profession"] = professions[i]["profession"]
    def q(lang):
        return {"language": lang, "query": lang + " synthetic query"}
    routes = [{"id": str(i), "question": "Fixture question " + str(i), "formulations": ["One " + str(i), "Two " + str(i)],
               "why_missed": "Fixture blind spot", "venue": "Test journal"} for i in range(2)]
    overlooked_plan = file("overlooked-plan.json", json.dumps({"run_id": run_id, "begin_sha256": begin_hash,
           "frozen_at": "2026-11-09T00:00:30Z", "routes": routes}))
    options = {k: {"option": "Synthetic " + k, "readiness": "unverified", "reason": "Test record"}
               for k in ("conservative", "innovative", "frontier")}
    return {"schema": gate.SCHEMA, "run_id": run_id, "begin_sha256": begin_hash,
            "answer": answer,
            "sentence_review": [{"text": part, "sentences": [{"text": part, "ordinary_approach": "Fixture baseline",
                "contribution": "Fixture delta", "evidence_or_basis": "Synthetic source", "utility": "Fixture",
                "result": "adds_value"}]} for part in gate.sentence_units((root / "answer.md").read_text())],
            "task_clarity": {"decision": "ready", "goal": "SYNTHETIC validation",
                             "unresolved_ambiguities": [], "checked_at": "2026-11-09T00:00:00Z"},
            "queries": [{"language": lang, "query": lang + " synthetic query",
                         "executed_at": ("2026-11-09T00:01:45Z" if lang == "DE" else "2026-11-09T00:01:00Z"), "receipt": receipt}
                        for lang in sorted(gate.LANGUAGES)],
            "sources": [{"id": "s1", "url": "https://example.org/source",
                         "type": "primary_source", "read_state": "read", "language": "EN",
                         "read_at": "2026-11-09T00:02:00Z", "scope": "Synthetic fixture only",
                         "evidence": source},
                        {"id": "human", "url": "https://example.org/forum/test", "type": "first_hand_experience",
                         "read_state": "read", "language": "EN", "read_at": "2026-11-09T00:01:30Z",
                         "scope": "Synthetic first-hand record", "evidence": source}],
            "claims": [{"id": "c1", "text": "Synthetic claim", "type": "fact", "source_ids": ["s1"]}],
            "innovation": {"transfers": transfers, "outside_query": en, "usual_field_keyword": "usualfield",
                           "overlooked_component": {"query": en, "status": "inspected",
                                                    "source_id": "s1", "finding": "Synthetic"}},
            "firsthand_sequences": [{"covers": ["research:0", "research:1", "profession:direct test role",
                "profession:adjacent test role"], "relevance": "Synthetic", "status": "verified",
                "human_source_id": "human", "experience_type": "practitioner", "observed_detail": "Fixture issue",
                "human_query": q("EN"), "official_source_id": "s1", "official_query": q("DE"),
                "official_check": "Fixture documentation checked after reading the observation."}],
            "overlooked_search": {"plan": overlooked_plan, "baseline_queries": [q("EN")],
                "outcomes": {str(i): {"status": "read", "queries": [q(lang)], "finding": "Synthetic",
                                      "source_ids": ["s1"]} for i, lang in enumerate(("DE", "ZH"))},
                "first_answer": {"strongest_finding": "Fixture", "source_ids": ["s1"], "options": options,
                    "price": {"status": "not_applicable", "reason": "Fixture"},
                    "next_directions": [{"question": "Next fixture " + str(i), "where": "Fixture venue",
                                         "purpose": "Fixture reason"} for i in (1, 2)]}},
            "practitioner_routes": {"professions": professions,
                "rounds": {"first_result": "sufficient", "reason": "Synthetic scope",
                           "first_queries": [{"language": l, "query": l + " synthetic query"}
                                             for l in sorted(gate.LANGUAGES)]},
                "adaptive_decisions": trail},
            "practical_answer": {"direct_answer": "Fixture answer", "alternatives": "Fixture option",
                "benefits": {name: {"basis": "not_applicable", "explanation": "Fixture"}
                             for name in ("time", "money", "effort")},
                "leader": {"status": "not_applicable", "reason": "Fixture"},
                "latvia": {"status": "not_applicable", "reason": "Fixture"}},
            "independent_review": {"author_instance": "synthetic-author", "reports": reports,
                                   "decisions": decisions, "unresolved_critical": []},
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

    def test_professional_routes_require_direct_and_adjacent_disciplines(self):
        self.data["practitioner_routes"]["professions"].pop()
        with self.assertRaisesRegex(gate.Invalid, "adjacent"):
            self.check()

    def test_official_search_cannot_precede_reading_the_human_account(self):
        for row in self.data["queries"]:
            if row["language"] == "DE":
                row["executed_at"] = "2026-11-09T00:01:10Z"
        with self.assertRaisesRegex(gate.Invalid, "before the official lookup"):
            self.check()

    def test_missing_experience_never_counts_as_verified(self):
        self.data["firsthand_sequences"][0]["status"] = "not_found"
        with self.assertRaisesRegex(gate.Invalid, "not found"):
            self.check()

    def test_every_profession_needs_traceable_human_evidence(self):
        self.data["firsthand_sequences"][0]["covers"].pop()
        with self.assertRaisesRegex(gate.Invalid, "each professional"):
            self.check()

    def test_overlooked_plan_frozen_after_first_queries_fails(self):
        block = self.data["overlooked_search"]
        path = self.root / block["plan"]["path"]
        plan = json.loads(path.read_text())
        plan["frozen_at"] = "2026-11-09T22:00:00Z"
        path.write_text(json.dumps(plan))
        block["plan"]["sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
        with self.assertRaisesRegex(gate.Invalid, "after searching"):
            self.check()

    def test_baseline_cannot_be_relabelled_as_overlooked(self):
        block = self.data["overlooked_search"]
        block["outcomes"]["0"]["queries"] = block["baseline_queries"]
        with self.assertRaisesRegex(gate.Invalid, "baseline outweighs"):
            self.check()

    def test_frontier_option_must_have_readiness(self):
        self.data["overlooked_search"]["first_answer"]["options"]["frontier"].pop("readiness")
        with self.assertRaisesRegex(gate.Invalid, "readiness"):
            self.check()

    def test_next_directions_cannot_repeat_one_question(self):
        rows = self.data["overlooked_search"]["first_answer"]["next_directions"]
        rows[1]["question"] = rows[0]["question"]
        with self.assertRaisesRegex(gate.Invalid, "duplicate next direction"):
            self.check()

    def test_an_unreviewed_final_sentence_cannot_pass(self):
        self.data["sentence_review"].pop()
        with self.assertRaisesRegex(gate.Invalid, "every delivered"):
            self.check()

    def test_sentence_comparison_with_no_value_requires_rework(self):
        self.data["sentence_review"][0]["sentences"][0]["result"] = "no_improvement"
        with self.assertRaisesRegex(gate.Invalid, "1 unresolved sentence"):
            self.check()

    def test_action_without_improvement_requires_rework(self):
        self.data["practitioner_routes"]["adaptive_decisions"][2]["comparison_result"] = "no_improvement"
        with self.assertRaisesRegex(gate.Invalid, "unresolved action"):
            self.check()

    def test_static_profession_list_without_observation_chain_is_refused(self):
        self.data["practitioner_routes"]["adaptive_decisions"][1]["after"] = "unobserved"
        with self.assertRaisesRegex(gate.Invalid, "earlier observed"):
            self.check()

    def test_missing_practical_option_stage_is_refused(self):
        self.data["practitioner_routes"]["adaptive_decisions"].pop()
        with self.assertRaisesRegex(gate.Invalid, "missing from a search stage"):
            self.check()

    def test_unread_forum_cannot_stand_in_for_experience(self):
        self.data["practitioner_routes"]["professions"][0]["venues"][0]["status"] = "inaccessible"
        with self.assertRaisesRegex(gate.Invalid, "unread venue"):
            self.check()

    def test_shallow_result_without_executed_followup_is_refused(self):
        rounds = self.data["practitioner_routes"]["rounds"]
        rounds.update(first_result="insufficient", specific_gap="Source omitted delivery.")
        with self.assertRaisesRegex(gate.Invalid, "fresh executed"):
            self.check()

    def test_targeted_additional_language_and_new_venue_can_document_a_remaining_gap(self):
        routes = self.data["practitioner_routes"]
        q = {"language": "LV", "query": "piegāde Latvijā"}
        self.data["queries"].append(dict(q, executed_at="2026-11-09T00:04:00Z",
                                        receipt=self.data["queries"][0]["receipt"]))
        venue = dict(routes["professions"][0]["venues"][0], query=q,
                     status="no_relevant_result", url="https://example.org/new-venue", source_ids=[])
        routes["professions"][0]["venues"].append(venue)
        routes["rounds"].update(first_result="insufficient", specific_gap="Shipping to Latvia",
                                followup_queries=[q], outcome="remaining_gap", finding="No shipping terms available")
        self.assertTrue(self.check()["evidence_contract_passed"])

    def test_claimed_leader_needs_criterion_and_evidence(self):
        self.data["practical_answer"]["leader"] = {"status": "verified", "reason": "Fixture", "source_ids": ["s1"]}
        with self.assertRaisesRegex(gate.Invalid, "leadership criterion"):
            self.check()

    def test_missing_independent_review_cannot_pass(self):
        self.data["independent_review"]["reports"].pop()
        with self.assertRaisesRegex(gate.Invalid, "four independent"):
            self.check()

    def test_one_instance_cannot_fill_two_roles(self):
        rows = self.data["independent_review"]["reports"]
        rows[1]["instance_id"] = rows[0]["instance_id"]
        with self.assertRaisesRegex(gate.Invalid, "reused an instance"):
            self.check()

    def test_review_for_an_old_draft_cannot_pass(self):
        new = b"Changed answer."
        (self.root / "answer.md").write_bytes(new)
        sha = hashlib.sha256(new).hexdigest()
        self.data["answer"]["sha256"] = self.data["writing"]["final_sha256"] = sha
        self.data["sentence_review"] = [dict(self.data["sentence_review"][0],
            text=new.decode(), sentences=[dict(self.data["sentence_review"][0]["sentences"][0], text=new.decode())])]
        with self.assertRaisesRegex(gate.Invalid, "not bound to this draft"):
            self.check()

    def test_missing_dispatch_receipt_cannot_pass(self):
        self.data["independent_review"]["reports"][0].pop("dispatch_receipt")
        with self.assertRaisesRegex(gate.Invalid, "dispatch receipt"):
            self.check()

    def test_unaddressed_review_cannot_pass(self):
        self.data["independent_review"]["decisions"].pop("skeptical")
        with self.assertRaisesRegex(gate.Invalid, "role-specific reconciliation"):
            self.check()

    def test_missing_innovation_cannot_pass(self):
        self.data.pop("innovation")
        with self.assertRaisesRegex(gate.Invalid, "innovation record"):
            self.check()

    def test_unexecuted_innovation_query_cannot_pass(self):
        self.data["innovation"]["outside_query"] = {"language": "EN", "query": "Never run"}
        with self.assertRaisesRegex(gate.Invalid, "not executed"):
            self.check()

    def test_normal_keyword_cannot_count_as_outside_search(self):
        self.data["innovation"]["usual_field_keyword"] = "synthetic"
        with self.assertRaisesRegex(gate.Invalid, "usual field keyword"):
            self.check()

    def test_an_unsuccessful_component_search_can_be_recorded(self):
        component = self.data["innovation"]["overlooked_component"]
        component.update(status="no_candidate", finding="No candidate met the scope.")
        del component["source_id"]
        self.assertTrue(self.check()["innovation_records_checked"])

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
