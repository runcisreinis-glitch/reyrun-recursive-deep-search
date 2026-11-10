#!/usr/bin/env python3
"""Read-only structural checks for research records (Python 3.9+, stdlib).

Commands: coverage journal.json | compare assessment.json | example
Output: JSON; exit 0 = structurally eligible, 1 = invalid data or unmet
comparison conditions, 2 = unreadable input. Coverage thresholds are separate
JSON fields: exit 0 does NOT mean that four languages or 30 queries were covered.
This is NOT proof of improvement, an autonomous engine, or version promotion.
All records are input assertions. The tool authenticates no identities, receipts,
hashes, executions, sources, or held-out tests. It makes no network requests.

SCHEMA (fields are required unless marked optional; unknown fields rejected):
coverage: {queries: [{language, query, method, executed}], metadata?: object}
  language: EN|DE|ZH|JA; method: M01..M19 (references/search-methods.md).
  Method coverage is informational; all 19 are not required for every task.
  query: nonempty text; executed: JSON boolean. Query deduplication uses NFKC,
  casefold, and collapsed whitespace. Counts do not prove execution or quality.
  Optional row fields:
    timestamp: ISO 8601 YYYY-MM-DDTHH:MM[:SS[.fraction]] with Z or +/-HH:MM;
    result_urls: list of http(s) URLs (may be empty for a search with no results);
    evidence: nonempty list of http(s) URLs or receipt:<ID>, without whitespace;
    notes: text (may be empty); query_id/source_batch: nonempty text.
  metadata is an arbitrary JSON object passed through as unverified input.
  language_coverage_complete: each language has >=1 recorded executed unique query.
  deep_profile_minimum_met: each has >=30 recorded executed unique queries.
  Neither threshold nor structural_eligibility is evidence of actual execution.
compare: {data_status, baseline, candidate, author_id, evaluator, context,
          split, budget, objective, audits, pairs}
  data_status: SYNTHETIC|RECORDED (both are input labels, not verification).
  baseline/candidate: {version: text, sha256: 64 hexadecimal characters};
    both declared versions and hashes must differ.
  author_id: text.
  evaluator: {id, trusted:true, external:true, self_assessment:false, evidence}
  context: {environment_id, model_id, evaluator_id, split_id} (texts).
  split: {id, dev_ids:[texts], test_ids:[texts], test_used_for_tuning:false};
    nonempty, unique, disjoint sets; id=context.split_id.
  budget: {unit: text, baseline: number>0, candidate: number>0};
    equal limits for EACH task; cost uses budget.unit.
  objective: {kind: quality|cost, min_gain: 0<x<=1,
              declared_before_test:true, evidence}; quality: mean gain;
    cost: relative total cost reduction without a mean quality decrease.
  audits: [{role, auditor_id, independent_initial:true, self_assessment:false,
            finding: text, evidence}]; four distinct IDs, none equal to author_id;
    role: optimism|skepticism|conservative|innovative, each exactly once.
    Findings may disagree; unanimity is not required.
  pairs: [{task_id, new_task:true, critical_regression:false, baseline, candidate}];
    task_id covers test_ids exactly, without duplicates.
  paired baseline/candidate: {version, context, quality:0..1, cost:number>=0,
                             evidence}; context equals the fixed context.
  evidence: nonempty list of http(s) URLs or receipt:<ID>, without whitespace.
example outputs a clearly SYNTHETIC assessment that can be passed to compare.
"""
import argparse
from collections import Counter, defaultdict
from datetime import datetime
import json
import math
from pathlib import Path
import re
import sys
import unicodedata
from urllib.parse import urlsplit

LANGUAGES = ("EN", "DE", "ZH", "JA")
METHODS = tuple(f"M{index:02d}" for index in range(1, 20))
ROLES = ("optimism", "skepticism", "conservative", "innovative")
NOTICE = ("Input structure and consistency only. Execution, sources, identities, "
          "held-out test integrity, and improvement are not proven.")


class Invalid(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise Invalid(message)


def obj(value, fields, path, optional=""):
    require(type(value) is dict, path + ": expected an object")
    required, allowed = set(fields.split()), set((fields + " " + optional).split())
    missing, unknown = required - set(value), set(value) - allowed
    require(not missing and not unknown,
            path + ": invalid fields; missing=" + repr(sorted(missing)) +
            "; unknown=" + repr(sorted(unknown)))
    return value


def txt(value, path):
    require(type(value) is str and bool(value.strip()), path + ": expected nonempty text")
    return value


def boolean(value, path, expected=None):
    require(type(value) is bool, path + ": expected a JSON boolean")
    require(expected is None or value is expected, path + ": unexpected value")
    return value


def number(value, path, upper=None):
    require(type(value) in (int, float) and math.isfinite(value) and value >= 0,
            path + ": expected a finite nonnegative number")
    require(upper is None or value <= upper, path + ": limit exceeded")
    return value


def items(value, path, nonempty=True):
    require(type(value) is list and (value or not nonempty), path + ": expected a list with the required cardinality")
    return value


def ids(value, path):
    result = [txt(x, path) for x in items(value, path)]
    require(len(set(result)) == len(result), path + ": duplicate IDs")
    return set(result)


def evidence(value, path):
    for ref in items(value, path):
        txt(ref, path)
        parsed = urlsplit(ref)
        valid = parsed.scheme in ("http", "https") and bool(parsed.hostname)
        valid = valid or re.fullmatch(r"receipt:\S+", ref)
        require(bool(valid) and not any(c.isspace() for c in ref), path + ": invalid evidence reference")


def timestamp(value, path):
    value = txt(value, path)
    pattern = (r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}(?::\d{2}(?:\.\d+)?)?"
               r"(?:Z|[+-](?:[01]\d|2[0-3]):[0-5]\d)")
    require(bool(re.fullmatch(pattern, value)),
            path + ": expected an ISO 8601 timestamp with an explicit timezone")
    try:
        parsed = datetime.fromisoformat(value[:-1] + "+00:00" if value.endswith("Z") else value)
        require(parsed.utcoffset() is not None, path + ": timezone is required")
    except ValueError as error:
        raise Invalid(path + ": invalid timestamp") from error


def result_urls(value, path):
    for ref in items(value, path, False):
        txt(ref, path)
        try:
            parsed = urlsplit(ref)
            valid = parsed.scheme in ("http", "https") and bool(parsed.hostname)
            valid = valid and (parsed.port is None or 0 <= parsed.port <= 65535)
        except ValueError as error:
            raise Invalid(path + ": invalid http(s) URL") from error
        require(bool(valid) and not any(c.isspace() or ord(c) < 32 for c in ref)
                and "\\" not in ref, path + ": invalid http(s) URL")


def coverage(data):
    obj(data, "queries", "journal", "metadata")
    if "metadata" in data:
        require(type(data["metadata"]) is dict, "metadata: expected an object")
        json.dumps(data["metadata"], allow_nan=False)
    counts, executed, groups = defaultdict(set), defaultdict(set), defaultdict(list)
    methods = {lang: Counter() for lang in LANGUAGES}
    for index, row in enumerate(items(data["queries"], "queries", False)):
        path = "queries[" + str(index) + "]"
        obj(row, "language query method executed", path,
            "timestamp result_urls evidence notes query_id source_batch")
        if "timestamp" in row:
            timestamp(row["timestamp"], path + ".timestamp")
        if "result_urls" in row:
            result_urls(row["result_urls"], path + ".result_urls")
        if "evidence" in row:
            evidence(row["evidence"], path + ".evidence")
        if "notes" in row:
            require(type(row["notes"]) is str, path + ".notes: expected text")
        for field in ("query_id", "source_batch"):
            if field in row:
                txt(row[field], path + "." + field)
        lang, method = row["language"], row["method"]
        require(lang in LANGUAGES, "query.language: unknown language")
        require(method in METHODS, "query.method: unknown method")
        query = " ".join(unicodedata.normalize("NFKC", txt(row["query"], "query.query")).casefold().split())
        groups[(lang, query)].append(index)
        counts[lang].add(query)
        methods[lang][method] += 1
        if boolean(row["executed"], "query.executed"):
            executed[lang].add(query)
    result = {"structural_eligibility": True, "counts_are_execution_proof": False,
            "language_coverage_complete": all(len(executed[lang]) >= 1 for lang in LANGUAGES),
            "deep_profile_minimum_met": all(len(executed[lang]) >= 30 for lang in LANGUAGES),
            "per_language": {lang: {"unique_queries": len(counts[lang]),
                "recorded_executed_unique": len(executed[lang]),
                "method_rows": dict(methods[lang]),
                "missing_methods": [m for m in METHODS if not methods[lang][m]]}
                for lang in LANGUAGES},
            "duplicates": [{"language": lang, "normalized_query": query, "row_indices": indices}
                for (lang, query), indices in groups.items() if len(indices) > 1]}
    if "metadata" in data:
        result.update({"metadata": data["metadata"], "metadata_scope": "unverified_passthrough"})
    return result


def compare(data):
    obj(data, "data_status baseline candidate author_id evaluator context split budget objective audits pairs", "assessment")
    require(data["data_status"] in ("SYNTHETIC", "RECORDED"), "data_status: invalid value")
    author = txt(data["author_id"], "author_id")
    for arm in ("baseline", "candidate"):
        version = obj(data[arm], "version sha256", arm)
        txt(version["version"], arm + ".version")
        require(bool(re.fullmatch(r"[0-9a-fA-F]{64}", txt(version["sha256"], arm + ".sha256"))),
                arm + ".sha256: invalid format")
    require(data["baseline"]["version"] != data["candidate"]["version"], "version is unchanged")
    require(data["baseline"]["sha256"].lower() != data["candidate"]["sha256"].lower(), "declared content hash is unchanged")
    evaluator = obj(data["evaluator"], "id trusted external self_assessment evidence", "evaluator")
    require(txt(evaluator["id"], "evaluator.id") != author, "evaluator is the candidate author")
    for field, value in (("trusted", True), ("external", True), ("self_assessment", False)):
        boolean(evaluator[field], "evaluator." + field, value)
    evidence(evaluator["evidence"], "evaluator.evidence")
    context = obj(data["context"], "environment_id model_id evaluator_id split_id", "context")
    for field, value in context.items():
        txt(value, "context." + field)
    require(context["evaluator_id"] == evaluator["id"], "evaluator ID mismatch")
    split = obj(data["split"], "id dev_ids test_ids test_used_for_tuning", "split")
    require(txt(split["id"], "split.id") == context["split_id"], "split ID mismatch")
    dev, test = ids(split["dev_ids"], "dev_ids"), ids(split["test_ids"], "test_ids")
    require(not dev & test, "development and test tasks overlap")
    boolean(split["test_used_for_tuning"], "test_used_for_tuning", False)
    budget = obj(data["budget"], "unit baseline candidate", "budget")
    txt(budget["unit"], "budget.unit")
    for arm in ("baseline", "candidate"):
        require(number(budget[arm], "budget." + arm) > 0, "budget must be positive")
    require(budget["baseline"] == budget["candidate"], "budget limits are unequal")
    goal = obj(data["objective"], "kind min_gain declared_before_test evidence", "objective")
    require(goal["kind"] in ("quality", "cost"), "objective.kind: invalid value")
    require(number(goal["min_gain"], "min_gain", 1) > 0, "min_gain must be positive")
    boolean(goal["declared_before_test"], "declared_before_test", True)
    evidence(goal["evidence"], "objective.evidence")
    actors, roles = set(), []
    for audit in items(data["audits"], "audits"):
        obj(audit, "role auditor_id independent_initial self_assessment finding evidence", "audit")
        require(audit["role"] in ROLES, "audit.role: unknown role")
        actor = txt(audit["auditor_id"], "auditor_id")
        require(actor != author and actor not in actors, "each auditor must differ from the author and other auditors")
        actors.add(actor)
        roles.append(audit["role"])
        boolean(audit["independent_initial"], "independent_initial", True)
        boolean(audit["self_assessment"], "audit.self_assessment", False)
        txt(audit["finding"], "audit.finding")
        evidence(audit["evidence"], "audit.evidence")
    require(Counter(roles) == Counter(ROLES), "exactly the four specified audit roles are required")
    totals = {arm: {"quality": 0.0, "cost": 0.0} for arm in ("baseline", "candidate")}
    seen = set()
    for pair in items(data["pairs"], "pairs"):
        obj(pair, "task_id new_task critical_regression baseline candidate", "pair")
        task = txt(pair["task_id"], "task_id")
        require(task in test and task not in seen, "paired task is not unique in the test set")
        seen.add(task)
        boolean(pair["new_task"], "new_task", True)
        boolean(pair["critical_regression"], "critical_regression", False)
        for arm in ("baseline", "candidate"):
            run = obj(pair[arm], "version context quality cost evidence", "run")
            require(run["version"] == data[arm]["version"], "run version mismatch")
            require(run["context"] == context, "run context mismatch")
            evidence(run["evidence"], "run.evidence")
            totals[arm]["quality"] += number(run["quality"], "quality", 1)
            cost = number(run["cost"], "cost")
            require(cost <= budget[arm], "run budget exceeded")
            totals[arm]["cost"] += cost
            require(math.isfinite(totals[arm]["cost"]), "total cost is not finite")
    require(seen == test, "paired runs do not cover the entire declared test set")
    quality_gain = (totals["candidate"]["quality"] - totals["baseline"]["quality"]) / len(test)
    cost_base = totals["baseline"]["cost"]
    cost_gain = (cost_base - totals["candidate"]["cost"]) / cost_base if cost_base else None
    gain = quality_gain if goal["kind"] == "quality" else cost_gain
    require(gain is not None and gain > 0 and (gain >= goal["min_gain"] or
            math.isclose(gain, goal["min_gain"], rel_tol=1e-12, abs_tol=0)), "declared gain was not achieved")
    require(goal["kind"] != "cost" or quality_gain >= -1e-12, "cost reduction accompanies a quality decrease")
    return {"structural_eligibility": True, "data_status": data["data_status"],
            "paired_tasks": len(test), "recorded_totals": totals,
            "recorded_quality_gain": quality_gain, "recorded_cost_reduction": cost_gain}


def example():
    context = {k: "SYNTHETIC-" + k for k in ("environment_id", "model_id", "evaluator_id", "split_id")}
    ref = ["receipt:SYNTHETIC-NOT-REAL"]
    data = {"data_status": "SYNTHETIC", "author_id": "SYNTHETIC-author",
        "baseline": {"version": "SYNTHETIC-v1", "sha256": "1" * 64},
        "candidate": {"version": "SYNTHETIC-v2", "sha256": "2" * 64},
        "evaluator": {"id": context["evaluator_id"], "trusted": True, "external": True,
                      "self_assessment": False, "evidence": ref}, "context": context,
        "split": {"id": context["split_id"], "dev_ids": ["SYNTHETIC-dev"],
                  "test_ids": ["SYNTHETIC-test"], "test_used_for_tuning": False},
        "budget": {"unit": "tokens", "baseline": 1000, "candidate": 1000},
        "objective": {"kind": "quality", "min_gain": 0.1, "declared_before_test": True, "evidence": ref},
        "audits": [{"role": role, "auditor_id": "SYNTHETIC-" + role,
                    "independent_initial": True, "self_assessment": False,
                    "finding": "SYNTHETIC example; findings may disagree.", "evidence": ref} for role in ROLES],
        "pairs": [{"task_id": "SYNTHETIC-test", "new_task": True, "critical_regression": False}]}
    for arm, score in (("baseline", 0.5), ("candidate", 0.7)):
        data["pairs"][0][arm] = {"version": data[arm]["version"], "context": context,
                               "quality": score, "cost": 500, "evidence": ref}
    return data


def unique_keys(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, "duplicate JSON key: " + key)
        result[key] = value
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    for command in ("coverage", "compare"):
        sub.add_parser(command, help="Check the structure of JSON input").add_argument("file", type=Path)
    sub.add_parser("example", help="Output a SYNTHETIC comparison example")
    args = parser.parse_args()
    if args.command == "example":
        print(json.dumps(example(), ensure_ascii=False, indent=2))
        return 0
    status = 0
    try:
        data = json.loads(args.file.read_text(encoding="utf-8"), object_pairs_hook=unique_keys,
                          parse_constant=lambda value: (_ for _ in ()).throw(Invalid("Invalid JSON number: " + value)))
        result = coverage(data) if args.command == "coverage" else compare(data)
    except (Invalid, ValueError, TypeError, OverflowError) as error:
        result, status = {"structural_eligibility": False, "errors": [str(error)]}, 1
    except (OSError, UnicodeError) as error:
        result, status = {"structural_eligibility": False, "errors": [str(error)]}, 2
    result.update({"improvement_proven": False, "evidence_scope": "input_assertions_only", "notice": NOTICE})
    print(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False))
    return status


if __name__ == "__main__":
    sys.exit(main())
