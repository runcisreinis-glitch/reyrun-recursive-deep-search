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


SCHEMA = "reyrun-delivery-v4"
ROLES = {"optimistic", "skeptical", "conservative", "innovative"}
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


def query_reference(record, executed):
    require(isinstance(record, dict), "expected a reference to an executed query")
    key = (string(record.get("language"), "query language"),
           string(record.get("query"), "query text").strip().casefold())
    require(key in executed, "innovation references a query that was not executed")
    return key


def innovation_record(record, executed, sources):
    require(isinstance(record, dict), "innovation record is missing")
    transfers = record.get("transfers")
    require(isinstance(transfers, list) and len(transfers) >= 2,
            "record at least two different mechanism transfers")
    mechanisms = set()
    for transfer in transfers:
        mechanism = string(transfer.get("mechanism"), "transfer mechanism").strip().casefold()
        require(mechanism not in mechanisms, "duplicate mechanism transfer")
        mechanisms.add(mechanism)
        for label in ("domain", "adaptation_gap", "falsification_test", "result"):
            string(transfer.get(label), "transfer " + label)
        query_reference(transfer.get("query"), executed)
    normal = string(record.get("usual_field_keyword"), "usual field keyword").strip().casefold()
    _, query = query_reference(record.get("outside_query"), executed)
    require(normal not in query, "outside query still contains the usual field keyword")
    component = record.get("overlooked_component")
    require(isinstance(component, dict), "overlooked component check is missing")
    query_reference(component.get("query"), executed)
    require(component.get("status") in {"inspected", "no_candidate"}, "unknown component outcome")
    string(component.get("finding"), "component search outcome")
    if component["status"] == "inspected":
        require(component.get("source_id") in sources, "inspected component lacks read evidence")


def practitioner_routes(data, query_times, sources, claims):
    plan = data.get("practitioner_routes")
    require(isinstance(plan, dict), "practitioner routes are missing")
    venues, professions, categories = {}, set(), set()
    for person in plan.get("professions", []):
        name = string(person.get("profession"), "profession").strip().casefold()
        require(name not in professions, "duplicate profession")
        professions.add(name)
        category = person.get("category")
        require(category in {"direct", "adjacent"}, "unknown profession category")
        categories.add(category)
        string(person.get("method"), "profession's relevant method")
        places = person.get("venues")
        require(isinstance(places, list) and places, "profession lacks real venue checks")
        for place in places:
            url = string(place.get("url"), "professional venue URL")
            require(urlsplit(url).scheme in {"https", "http"} and urlsplit(url).hostname,
                    "professional venue needs an actual web URL")
            string(place.get("name"), "professional venue name")
            require(place.get("type") in {"association", "workshop", "journal", "forum", "chat", "other"},
                    "unrecognized professional venue type")
            query = query_reference(place.get("query"), query_times)
            venues.setdefault(query, set()).add(url)
            require(place.get("status") in {"read", "inaccessible", "no_relevant_result"},
                    "professional venue access outcome is missing")
            string(place.get("finding"), "professional venue finding or access limitation")
            if place["status"] == "read":
                refs = place.get("source_ids")
                require(isinstance(refs, list) and bool(refs) and all(x in sources for x in refs),
                        "read professional venue lacks source evidence")
                require(any(urlsplit(sources[x]["url"]).hostname == urlsplit(url).hostname for x in refs),
                        "read professional venue has no evidence from its own host")
            else:
                require(not place.get("source_ids"), "unread venue cannot claim practitioner evidence")
    require(categories == {"direct", "adjacent"}, "both direct and adjacent professions must be considered")
    rounds = plan.get("rounds", {})
    verdict = rounds.get("first_result")
    require(verdict in {"sufficient", "insufficient"}, "first-round evidence assessment is missing")
    string(rounds.get("reason"), "first-round evidence assessment")
    first = {query_reference(r, query_times) for r in rounds.get("first_queries", [])}
    require({k[0] for k in first} >= LANGUAGES, "first round lacks the four core languages")
    if verdict == "insufficient":
        string(rounds.get("specific_gap"), "specific unresolved gap")
        follow = {query_reference(r, query_times) for r in rounds.get("followup_queries", [])}
        require(follow and follow.isdisjoint(first), "targeted second round lacks fresh executed queries")
        require(any(k[0] not in {q[0] for q in first} for k in follow),
                "second round needs an additional relevant search language")
        require(min(query_times[k] for k in follow) >= max(query_times[k] for k in first),
                "follow-up queries predate the initial round")
        old_places = {url for k in first for url in venues.get(k, ())}
        new_places = {url for k in follow for url in venues.get(k, ())}
        require(bool(new_places - old_places), "targeted second round lacks a new professional venue")
        require(rounds.get("outcome") in {"resolved", "remaining_gap"}, "follow-up outcome is missing")
        string(rounds.get("finding"), "follow-up finding or remaining limitation")
        if rounds["outcome"] == "resolved":
            refs = rounds.get("source_ids")
            require(isinstance(refs, list) and refs and all(i in sources for i in refs),
                    "resolved follow-up has no read source")
    trail = plan.get("adaptive_decisions")
    require(isinstance(trail, list) and trail, "adaptive decision trail is missing")
    stages, visited, selection = set(), set(), set()
    triggers = set()
    for step in trail:
        stage = step.get("stage")
        require(stage in {"profession", "query", "venue_language", "validation", "practical_option"},
                "unknown adaptive decision stage")
        stages.add(stage)
        step_id = string(step.get("id"), "adaptive decision ID")
        require(step_id not in visited, "adaptive decision ID is repeated")
        parent = step.get("after")
        require((not visited and parent == "user_question") or (visited and parent in visited),
                "adaptive decision must follow the question or an earlier observed step")
        visited.add(step_id)
        observation = string(step.get("observation"), "observed fact or obstacle")
        option = string(step.get("alternative"), "unconventional alternative derived from the observation")
        string(step.get("shared_principle"), "transferable principle")
        string(step.get("ordinary_approach"), "ordinary approach for this action")
        string(step.get("contribution"), "specific improvement or necessary factual preservation")
        require(step.get("comparison_result") in {"adds_value", "retains_necessary_fact", "revised"},
                "unresolved action comparison; revise this step and repeat the check")
        string(step.get("test"), "concrete falsification or validation test")
        string(step.get("outcome"), "observed outcome or explicit remaining limitation")
        require((observation.casefold(), option.casefold()) not in triggers,
                "adaptive decision repeats an unchanged observation and alternative")
        triggers.add((observation.casefold(), option.casefold()))
        anchor = step.get("anchor")
        require(isinstance(anchor, dict), "adaptive decision lacks a traceable anchor")
        if anchor.get("kind") == "question":
            require(parent == "user_question", "only the initial decision can cite the question alone")
        elif anchor.get("kind") == "query":
            query_reference(anchor.get("ref"), query_times)
        elif anchor.get("kind") == "source":
            require(anchor.get("id") in sources, "adaptive decision cites an unread source")
        else:
            raise Invalid("adaptive decision needs the question, an executed query or read source")
        if stage == "profession":
            name = string(step.get("profession"), "profession selected by this observation").strip().casefold()
            require(name in professions, "adaptive profession lacks a real practitioner route")
            selection.add(name)
    require(stages == {"profession", "query", "venue_language", "validation", "practical_option"},
            "adaptive decisions are missing from a search stage")
    require(selection == professions, "every professional route must have an observation-based selection")
    checks = data.get("practical_answer")
    require(isinstance(checks, dict), "practical answer checks are missing")
    string(checks.get("direct_answer"), "direct practical result")
    string(checks.get("alternatives"), "useful alternatives or reason none qualified")
    gains = checks.get("benefits")
    require(isinstance(gains, dict) and set(gains) == {"time", "money", "effort"},
            "time, money and effort dispositions are required")
    for kind, benefit in gains.items():
        require(benefit.get("basis") in {"measured", "reasoned", "not_applicable", "unknown"},
                "unknown benefit basis")
        string(benefit.get("explanation"), kind + " benefit explanation")
        if benefit["basis"] in {"measured", "reasoned"}:
            require(benefit.get("claim_id") in claims, "benefit lacks a checked claim")
        if benefit["basis"] == "measured":
            string(benefit.get("baseline"), "measured benefit baseline")
            string(benefit.get("unit"), "measured benefit unit")
    for name in ("leader", "latvia"):
        row = checks.get(name, {})
        require(row.get("status") in {"verified", "gap", "not_applicable"}, name + " relevance is missing")
        string(row.get("reason"), name + " reason or limitation")
        if row["status"] == "verified":
            refs = row.get("source_ids")
            require(isinstance(refs, list) and refs and all(i in sources for i in refs),
                    name + " verification lacks read sources")
            if name == "leader":
                string(row.get("criterion"), "explicit leadership criterion")
            else:
                string(row.get("availability_or_delivery"), "Latvian availability or delivery conditions")
                timestamp(row.get("checked_at"), "Latvian availability check time")


def overlooked_map(root, data, executed, sources):
    result = data.get("overlooked_search")
    require(isinstance(result, dict), "missing pre-search map of overlooked questions")
    plan = json.loads(artifact(root, result.get("plan"), "frozen overlooked search map"))
    require(plan.get("run_id") == data["run_id"] and plan.get("begin_sha256") == data["begin_sha256"],
            "overlooked search map belongs to a different run")
    require(timestamp(plan.get("frozen_at"), "overlooked planning time") <= min(executed.values()),
            "overlooked search map was recorded after searching began")
    rows = plan.get("routes")
    require(isinstance(rows, list) and len(rows) >= 2, "need distinct overlooked directions")
    routes = {}
    questions = set()
    for route in rows:
        rid = string(route.get("id"), "overlooked route ID")
        question = string(route.get("question"), "specific overlooked question").strip().casefold()
        require(rid not in routes and question not in questions, "duplicate overlooked question or route")
        variants = route.get("formulations")
        require(isinstance(variants, list) and len({string(v, "query formulation").strip().casefold()
                                                   for v in variants}) >= 2,
                "each overlooked question needs multiple actual formulations")
        string(route.get("why_missed"), "why an ordinary search would overlook this question")
        string(route.get("venue"), "named intended professional venue or place to investigate")
        routes[rid] = route
        questions.add(question)
    baseline = {query_reference(q, executed) for q in result.get("baseline_queries", [])}
    require(baseline, "ordinary comparison search is missing")
    checks = result.get("outcomes")
    require(isinstance(checks, dict) and set(checks) == set(routes),
            "every overlooked direction needs an executed check or concrete limitation")
    unusual = set()
    for rid, row in checks.items():
        string(row.get("finding"), "overlooked route finding or access limitation")
        status = row.get("status")
        require(status in {"read", "no_result", "unavailable"}, "unknown overlooked route outcome")
        queries = {query_reference(q, executed) for q in row.get("queries", [])}
        if status != "unavailable":
            require(queries, "overlooked route has no actual query")
        refs = row.get("source_ids", [])
        require(isinstance(refs, list) and all(s in sources for s in refs), "unread overlooked route source")
        if status == "read":
            require(refs, "overlooked route found without read sources")
        if status == "unavailable":
            require(not refs, "unavailable route cannot claim to have read material")
        unusual.update(queries)
    require(len(unusual - baseline) > len(baseline),
            "ordinary baseline outweighs actual distinct overlooked-direction searches")
    sequences = data.get("firsthand_sequences")
    require(isinstance(sequences, list) and sequences, "missing first-hand practice before official verification")
    required_routes = {"research:" + rid for rid in routes}
    required_routes.update("profession:" + p["profession"].strip().casefold()
                           for p in data.get("practitioner_routes", {}).get("professions", []))
    covered, human_reads = set(), []
    for step in sequences:
        targets = step.get("covers")
        require(isinstance(targets, list) and targets and all(r in required_routes for r in targets),
                "unknown or missing first-hand research route")
        string(step.get("relevance"), "how the observation bears on these routes")
        require(step.get("status") == "verified",
                "first-hand experience or its official verification was not found; report the gap as limited")
        human = sources.get(step.get("human_source_id"), {})
        official = sources.get(step.get("official_source_id"), {})
        require(human.get("type") == "first_hand_experience", "professional or owner experience was not read")
        require(official.get("type") in PRIMARY_TYPES, "later official verification lacks a primary source")
        require(human["url"] != official["url"], "first-hand and official checks refer to the same page")
        require(step.get("experience_type") in {"practitioner", "owner", "operator", "maintainer"},
                "first-hand experience type is missing")
        string(step.get("observed_detail"), "specific detail reported first-hand")
        string(step.get("official_check"), "the later official check of that same detail")
        hq = query_reference(step.get("human_query"), executed)
        oq = query_reference(step.get("official_query"), executed)
        htime = timestamp(human["read_at"], "first-hand source read time")
        otime = timestamp(official["read_at"], "official source read time")
        require(executed[hq] <= htime < executed[oq] <= otime,
                "first-hand source must be read before the official lookup it informs")
        human_reads.append(htime)
        covered.update(targets)
    require(covered == required_routes, "each professional and overlooked route needs first-hand then official evidence")
    require(all(timestamp(src["read_at"], "official source read time") >= min(human_reads)
                for src in sources.values() if src.get("type") in PRIMARY_TYPES),
            "official material was read before the first human experience")
    finding = result.get("first_answer")
    require(isinstance(finding, dict), "first practical answer summary is missing")
    string(finding.get("strongest_finding"), "strongest supported finding")
    require(isinstance(finding.get("source_ids"), list) and finding["source_ids"] and
            all(i in sources for i in finding["source_ids"]), "strongest finding lacks read evidence")
    choices = finding.get("options")
    require(isinstance(choices, dict) and set(choices) == {"conservative", "innovative", "frontier"},
            "conservative, innovative and field-frontier options must be assessed")
    for name, choice in choices.items():
        string(choice.get("option"), name + " concrete option or explanation of gap")
        require(choice.get("readiness") in {"ready", "limited", "experimental", "unverified", "no_candidate"},
                "option needs an actual readiness or lack-of-evidence assessment")
        string(choice.get("reason"), name + " readiness evidence or limitation")
    price = finding.get("price")
    require(isinstance(price, dict) and price.get("status") in {"verified", "gap", "not_applicable"},
            "price disposition is missing")
    string(price.get("reason"), "price relevance or remaining gap")
    if price["status"] == "verified":
        require(isinstance(price.get("source_ids"), list) and price["source_ids"] and
                all(i in sources for i in price["source_ids"]), "price lacks current read evidence")
        for field in ("amount", "currency", "scope"):
            string(price.get(field), "price " + field)
        timestamp(price.get("checked_at"), "price check time")
    next_steps = finding.get("next_directions")
    require(isinstance(next_steps, list) and 2 <= len(next_steps) <= 4,
            "provide two to four different concrete follow-up directions")
    questions = set()
    for step in next_steps:
        q = string(step.get("question"), "next concrete question").strip().casefold()
        require(q not in questions, "duplicate next direction")
        questions.add(q)
        string(step.get("where"), "where to investigate next")
        string(step.get("purpose"), "how the next answer changes the practical choice")


def sentence_units(text):
    """Nonblank text units for complete coverage, including links and list lines.

    Keep periods inside URLs, decimal values and ordinary inline abbreviations.
    When a unit still contains multiple human sentences, split the review into
    subrows while retaining the parent unit exactly.
    """
    split = re.compile(r"(?<=[.!?])[ \t]+(?=[A-ZÀ-ÞА-ЯЁ0-9\[\"“])|(?<=[。！？])(?=[^\s])|[\r\n]+")
    return [piece.strip() for piece in split.split(text) if piece.strip()]


def sentence_check(data, answer):
    rows = data.get("sentence_review")
    units = sentence_units(answer.decode("utf-8"))
    require(isinstance(rows, list) and len(rows) == len(units),
            "sentence review does not cover every delivered text unit")
    count = unresolved = 0
    for expected, row in zip(units, rows):
        require(row.get("text") == expected, "sentence review omits, changes or reorders final text")
        subrows = row.get("sentences")
        require(isinstance(subrows, list) and bool(subrows), "missing sentence-level comparison")
        require("".join(s.get("text", "") for s in subrows).strip() == expected,
                "sentence subrows do not reconstruct the reviewed unit")
        for line in subrows:
            count += 1
            for field in ("text", "ordinary_approach", "contribution", "evidence_or_basis", "utility"):
                string(line.get(field), "sentence " + field)
            status = line.get("result")
            require(status in {"adds_value", "retains_necessary_fact", "revised", "no_improvement"},
                    "unknown sentence comparison result")
            if status == "revised":
                string(line.get("previous_text"), "revised sentence's previous text")
                require(line["previous_text"].strip() != line["text"].strip(),
                        "revision did not change the sentence")
            if status == "no_improvement":
                unresolved += 1
    require(unresolved == 0, f"{unresolved} unresolved sentence comparisons; revise and repeat review")
    return {"sentences_checked": count, "unresolved_sentence_comparisons": unresolved}


def independent_reviews(root, data, answer_digest, registry):
    receipt_dir = None
    if registry is not None:
        base = Path(registry)
        require(base.is_absolute() and base.is_dir() and base.resolve() == base,
                "controller review receipt directory must be an existing absolute directory without symlinks")
        require(not base.is_relative_to(root) and not root.is_relative_to(base),
                "controller review receipt directory must be separate from worker artifacts")
        require(re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,127}", data["run_id"]) is not None,
                "run ID cannot address the controller review registry")
        receipt_dir = base / data["run_id"]
        require(receipt_dir.is_dir() and not receipt_dir.is_symlink(),
                "no independently supplied controller receipts for this run")
    review = data.get("independent_review")
    require(isinstance(review, dict), "independent review records are missing")
    author = string(review.get("author_instance"), "answer author instance").strip().casefold()
    roles, instances, reports = set(), {author}, set()
    rows = review.get("reports")
    require(isinstance(rows, list) and len(rows) == len(ROLES), "four independent reports are required")
    for row in rows:
        role = row.get("role")
        require(role in ROLES and role not in roles, "missing or duplicate review role")
        roles.add(role)
        instance = string(row.get("instance_id"), "reviewer instance ID").strip().casefold()
        require(instance not in instances, "the author or another reviewer reused an instance")
        instances.add(instance)
        report = json.loads(artifact(root, row.get("report"), "independent report"))
        require(isinstance(report, dict) and report.get("role") == role and
                report.get("instance_id") == row["instance_id"] and
                report.get("run_id") == data["run_id"] and report.get("answer_sha256") == answer_digest,
                "review report is not bound to this draft, role, instance and run")
        finding = string(report.get("finding"), "independent finding").strip().casefold()
        require(finding not in reports, "duplicate review finding")
        reports.add(finding)
        string(report.get("alternative"), "reviewer alternative or reason to reject it")
        require(report.get("verdict") in {"accept", "concern"}, "missing review verdict")
        raw_receipt = artifact(root, row.get("dispatch_receipt"), "review dispatch receipt")
        if receipt_dir is not None:
            external = receipt_dir / (role + ".json")
            require(external.is_file() and not external.is_symlink() and
                    external.stat().st_size == len(raw_receipt) and external.read_bytes() == raw_receipt,
                    "worker receipt differs from the controller's isolated review receipt")
        receipt = json.loads(raw_receipt)
        require(isinstance(receipt, dict) and receipt.get("run_id") == data["run_id"] and
                receipt.get("instance_id") == row["instance_id"] and
                receipt.get("report_sha256") == row["report"]["sha256"] and
                receipt.get("isolated_initial_review") is True,
                "host dispatch receipt does not attest an isolated review of this report")
    decisions = review.get("decisions")
    require(isinstance(decisions, dict) and set(decisions) == ROLES,
            "missing role-specific reconciliation")
    for role, disposition in decisions.items():
        string(disposition, role + " reconciliation")
    require(review.get("unresolved_critical") == [], "unresolved critical four-review objection")


def validate(manifest_path, run_id=None, begin_sha256=None, artifact_dir=None, review_receipt_dir=None):
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
    languages, earliest, seen = set(), None, {}
    for query in queries:
        require(type(query) is dict, "query must be an object")
        language = query.get("language")
        require(isinstance(language, str) and re.fullmatch(r"[A-Z]{2,3}(?:-[A-Z0-9]{2,8})*", language),
                "query requires an actual uppercase language tag")
        text = string(query.get("query"), "query text")
        key = (language, text.strip().casefold())
        require(key not in seen, "duplicate query is not additional coverage")
        languages.add(language)
        when = timestamp(query.get("executed_at"), "query time")
        seen[key] = when
        earliest = when if earliest is None else min(earliest, when)
        artifact(root, query.get("receipt"), "query receipt")
    require(languages >= LANGUAGES, "EN/DE/ZH/JA executed query coverage is incomplete")
    require(checked <= earliest, "task preflight was recorded after research began")
    sources = data.get("sources")
    require(type(sources) is list and bool(sources), "source ledger is missing")
    source_map = {}
    for source in sources:
        require(type(source) is dict, "source must be an object")
        sid = string(source.get("id"), "source ID")
        require(sid not in source_map, "duplicate source ID")
        require(source.get("type") in SOURCE_TYPES, "unrecognized source type")
        require(source.get("language") in languages | {"mixed", "other"}, "source content language is missing")
        require(source.get("read_state") == "read", "a search snippet is not a read source")
        timestamp(source.get("read_at"), "source read time")
        url = string(source.get("url"), "source URL")
        require(urlsplit(url).scheme in {"https", "http"} and bool(urlsplit(url).netloc), "source needs an actual web URL")
        string(source.get("scope"), "source support scope")
        artifact(root, source.get("evidence"), "read source evidence")
        source_map[sid] = source
    innovation_record(data.get("innovation"), seen, source_map)
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
    practitioner_routes(data, seen, source_map, claim_ids)
    overlooked_map(root, data, seen, source_map)
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
    sentence_summary = sentence_check(data, answer)
    independent_reviews(root, data, data["answer"]["sha256"], review_receipt_dir)
    checked = {"innovation_records_checked": True, "independent_reports_checked": 4,
            "controller_receipts_matched": review_receipt_dir is not None,
            "reviewer_identity_authenticated": False, "schema": SCHEMA, "evidence_contract_passed": True,
            "factual_quality_certified": False, "improvement_proven": False,
            "manifest_sha256": hashlib.sha256(raw).hexdigest(),
            "answer_sha256": hashlib.sha256(answer).hexdigest(),
            "run_id": data["run_id"], "query_count": len(queries),
            "source_count": len(sources), "claim_count": len(claims),
            "source_content_languages": sorted({source["language"] for source in sources}),
            "statement": "Required records, references, timestamps and artifact hashes passed. Semantic reviews remain attributed attestations; factual truth and reviewer identity are not machine-certified."}
    checked.update(sentence_summary)
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
    parser.add_argument("--review-receipt-dir", type=Path, help="Controller-owned independent dispatch records")
    args = parser.parse_args()
    try:
        result = validate(args.manifest, review_receipt_dir=args.review_receipt_dir)
    except (Invalid, OSError, ValueError, TypeError, KeyError, AttributeError) as error:
        result = {"evidence_contract_passed": False, "factual_quality_certified": False,
                  "improvement_proven": False, "error": str(error)}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["evidence_contract_passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
