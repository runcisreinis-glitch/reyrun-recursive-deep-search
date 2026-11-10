#!/usr/bin/env python3
"""Check a research delivery's evidence records and bytes, not factual truth.

The worker writes delivery-manifest.json inside its artifact directory. A trusted
controller runs this before accepting the delivery. Reviewer statements are
attestations, not authenticated identities or automatic semantic verification.
"""
import argparse
from datetime import datetime
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit


SCHEMA = "reyrun-delivery-v1"
LANGUAGES = {"EN", "DE", "ZH", "JA"}
CLAIM_TYPES = {"fact", "source_claim", "experience", "calculation",
               "inference", "hypothesis", "recommendation"}
PRIMARY_TYPES = {"official_documentation", "research_paper", "author_code",
                 "standard", "reproducible_measurement", "primary_source"}
SOURCE_TYPES = PRIMARY_TYPES | {"first_hand_experience", "secondary_source"}
MAX_FILE_BYTES = 4 * 1024 * 1024


class Invalid(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise Invalid(message)


def string(value, label):
    require(isinstance(value, str) and bool(value.strip()), label + " must be nonempty text")
    return value


def timestamp(value, label):
    string(value, label)
    try:
        result = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as error:
        raise Invalid(label + " must be an ISO timestamp") from error
    require(result.tzinfo is not None, label + " must include a timezone")
    return result


def artifact(root, reference, label):
    require(isinstance(reference, dict), label + " must be an artifact reference")
    raw_path = string(reference.get("path"), label + ".path")
    supplied = Path(raw_path)
    path = supplied if supplied.is_absolute() else root / supplied
    resolved = path.resolve()
    require(resolved.is_relative_to(root), label + " escapes the artifact directory")
    require(not path.is_symlink() and resolved.is_file(), label + " must be a regular file")
    require(0 < resolved.stat().st_size <= MAX_FILE_BYTES, label + " is empty or exceeds 4 MiB")
    digest = string(reference.get("sha256"), label + ".sha256")
    require(re.fullmatch(r"[0-9a-f]{64}", digest) is not None, label + " has invalid SHA256")
    data = resolved.read_bytes()
    require(hashlib.sha256(data).hexdigest() == digest, label + " bytes changed")
    return data


def validate(manifest_path, run_id=None, begin_sha256=None, artifact_dir=None):
    supplied_manifest = Path(manifest_path).absolute()
    require(not supplied_manifest.is_symlink(), "delivery manifest must not be a symbolic link")
    root = supplied_manifest.parent.resolve()
    if artifact_dir is not None:
        require(root == Path(artifact_dir).resolve(), "delivery manifest is outside the supplied job directory")
    manifest_path = supplied_manifest.resolve()
    require(manifest_path.parent == root, "delivery manifest escapes its job directory")
    require(manifest_path.is_file(), "delivery-manifest.json is missing")
    require(manifest_path.stat().st_size <= MAX_FILE_BYTES, "delivery manifest exceeds 4 MiB")
    raw = manifest_path.read_bytes()
    data = json.loads(raw)
    require(type(data) is dict and data.get("schema") == SCHEMA, "wrong delivery schema")
    string(data.get("run_id"), "run_id")
    digest = string(data.get("begin_sha256"), "begin_sha256")
    require(re.fullmatch(r"[0-9a-f]{64}", digest) is not None, "invalid begin hash")
    if run_id is not None:
        require(data["run_id"] == run_id, "delivery belongs to a different run")
    if begin_sha256 is not None:
        require(digest == begin_sha256, "delivery belongs to a different begin receipt")
    answer = artifact(root, data.get("answer"), "answer")
    require(answer.decode("utf-8").strip(), "answer is empty")
    clarity = data.get("task_clarity", {})
    require(clarity.get("decision") == "ready", "task requires clarification")
    require(clarity.get("unresolved_ambiguities") == [], "unresolved task ambiguity")
    string(clarity.get("goal"), "task goal")
    checked = timestamp(clarity.get("checked_at"), "preflight time")
    queries = data.get("queries")
    require(type(queries) is list and bool(queries), "executed query ledger is missing")
    languages, earliest, seen = set(), None, set()
    for query in queries:
        require(type(query) is dict, "query must be an object")
        language = query.get("language")
        require(language in LANGUAGES, "unrecognized core query language")
        text = string(query.get("query"), "query text")
        key = (language, text.strip().casefold())
        require(key not in seen, "duplicate query is not additional coverage")
        seen.add(key)
        languages.add(language)
        when = timestamp(query.get("executed_at"), "query time")
        earliest = when if earliest is None else min(earliest, when)
        artifact(root, query.get("receipt"), "query receipt")
    require(languages == LANGUAGES, "EN/DE/ZH/JA executed query coverage is incomplete")
    require(checked <= earliest, "task preflight was recorded after research began")
    sources = data.get("sources")
    require(type(sources) is list and bool(sources), "source ledger is missing")
    source_map = {}
    for source in sources:
        require(type(source) is dict, "source must be an object")
        sid = string(source.get("id"), "source ID")
        require(sid not in source_map, "duplicate source ID")
        require(source.get("type") in SOURCE_TYPES, "unrecognized source type")
        require(source.get("language") in LANGUAGES | {"mixed", "other"}, "source content language is missing")
        require(source.get("read_state") == "read", "a search snippet is not a read source")
        timestamp(source.get("read_at"), "source read time")
        url = string(source.get("url"), "source URL")
        require(urlsplit(url).scheme in {"https", "http"} and bool(urlsplit(url).netloc), "source needs an actual web URL")
        string(source.get("scope"), "source support scope")
        artifact(root, source.get("evidence"), "read source evidence")
        source_map[sid] = source
    claims = data.get("claims")
    require(type(claims) is list and bool(claims), "claim ledger is missing")
    claim_ids = set()
    for claim in claims:
        require(type(claim) is dict, "claim must be an object")
        cid = string(claim.get("id"), "claim ID")
        require(cid not in claim_ids, "duplicate claim ID")
        claim_ids.add(cid)
        string(claim.get("text"), "claim text")
        kind = claim.get("type")
        require(kind in CLAIM_TYPES, "unrecognized claim type")
        refs = claim.get("source_ids")
        require(type(refs) is list and all(isinstance(s, str) and s in source_map for s in refs), "claim cites an unknown source")
        require(len(refs) == len(set(refs)), "duplicate claim source")
        if kind in {"fact", "source_claim", "experience"}:
            require(bool(refs), "externally checkable claim lacks read evidence")
        if kind == "fact":
            require(any(source_map[s]["type"] in PRIMARY_TYPES for s in refs), "factual claim lacks primary support")
        if kind == "calculation":
            string(claim.get("formula"), "calculation formula")
            string(claim.get("inputs"), "calculation inputs and their provenance")
        if kind in {"inference", "hypothesis", "recommendation"}:
            string(claim.get("rationale"), "reasoned claim rationale")
    experience = data.get("practitioner_check", {})
    require(experience.get("status") in {"found", "gap", "not_applicable"}, "professional experience search disposition is missing")
    string(experience.get("reason"), "professional experience disposition reason")
    if experience["status"] == "found":
        refs = experience.get("source_ids", [])
        require(type(refs) is list and bool(refs) and all(s in source_map for s in refs), "practitioner sources are missing")
    writing = data.get("writing", {})
    require(writing.get("method") == "Humanizer", "actual Humanizer pass is not recorded")
    string(writing.get("version"), "Humanizer version")
    string(writing.get("editor"), "actual editor")
    artifact(root, writing.get("draft"), "writing draft")
    require(writing.get("final_sha256") == hashlib.sha256(answer).hexdigest(), "writing pass does not cover the delivered answer")
    semantic = writing.get("semantic_review", {})
    string(semantic.get("reviewer"), "semantic reviewer")
    require(semantic.get("full_text_checked") is True and semantic.get("factual_changes_resolved") is True, "full meaning and fact review is incomplete")
    invariants = semantic.get("invariants")
    require(type(invariants) is list and bool(invariants) and all(isinstance(s, str) and s.strip() for s in invariants), "writing invariants are missing")
    review = data.get("review", {})
    string(review.get("reviewer"), "evidence reviewer")
    for key in ("answer_claim_coverage_checked", "material_citations_checked", "source_entailment_checked"):
        require(review.get(key) is True, key + " is missing")
    require(review.get("unresolved_critical") == [], "unresolved critical evidence objections")
    checked = {"schema": SCHEMA, "evidence_contract_passed": True,
            "factual_quality_certified": False, "improvement_proven": False,
            "manifest_sha256": hashlib.sha256(raw).hexdigest(),
            "answer_sha256": hashlib.sha256(answer).hexdigest(),
            "run_id": data["run_id"], "query_count": len(queries),
            "source_count": len(sources), "claim_count": len(claims),
            "source_content_languages": sorted({source["language"] for source in sources}),
            "statement": "Required records, references, timestamps and artifact hashes passed. Semantic reviews remain attributed attestations; factual truth and reviewer identity are not machine-certified."}
    if "evaluation_fields" in data:
        fields = json.loads(artifact(root, data["evaluation_fields"], "evaluation fields"))
        require(type(fields) is dict and bool(fields), "evaluation fields must be a nonempty JSON object")
        require(review.get("evaluation_fields_checked") is True,
                "structured evaluation fields were not included in source and meaning review")
        checked["evaluation_fields"] = fields
    return checked


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    args = parser.parse_args()
    try:
        result = validate(args.manifest)
    except (Invalid, OSError, ValueError, TypeError, KeyError, AttributeError) as error:
        result = {"evidence_contract_passed": False, "factual_quality_certified": False,
                  "improvement_proven": False, "error": str(error)}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["evidence_contract_passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
