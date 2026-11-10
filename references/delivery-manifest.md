# Executable delivery evidence check

This beta adapter checks the default EN/DE/ZH/JA language profile. It does not yet support substituting a language in the strict manifest. Honour an explicit replacement request through manual research and disclose the missing adapter coverage; do not call that a strict-host pass. Extra authorized languages can have supplementary records.

`search_host.py` defaults to `delivery_gate_mode: strict`. The worker must write
`delivery-manifest.json` in the supplied `artifact_dir` before returning. Missing
or invalid evidence leaves the run unfinished and produces a repair request.
The controller may schedule a bounded repair; there is no unbounded retry.

This checker validates records, identifiers, timestamps and SHA-256 against actual
files. It cannot detect every omitted claim, authenticate a person behind a
reviewer ID or determine whether prose is true. The evidence reviewer must read
the sources and answer, check entailment and material omissions, and sign the
attributed review fields. Keep critical objections visible.

## Manifest fields

The schema is `reyrun-delivery-v1`. Required fields are:

| Field | Required content |
| --- | --- |
| `schema`, `run_id`, `begin_sha256` | Schema name and the exact host input binding. |
| `answer` | `{path, sha256}` of the actual UTF-8 answer. |
| `task_clarity` | `goal`, `decision: ready`, `unresolved_ambiguities: []`, timezone-aware `checked_at`. Record this before searching. Preserve any real or clearly simulated clarification separately. |
| `queries` | Actual executed queries: `language` (EN/DE/ZH/JA), `query`, timezone-aware `executed_at`, and `receipt: {path, sha256}`. Each core language needs an executed query. Duplicate queries do not add coverage. Additional explicitly authorized language research can be retained in supplementary records. |
| `sources` | `id`, actual `url`, `type`, content `language` (EN/DE/ZH/JA/mixed/other), `read_state: read`, timezone-aware `read_at`, supported `scope`, and `evidence: {path, sha256}` for retrieved source content. A search snippet does not qualify as a read source. |
| `claims` | `id`, `text`, `type`, `source_ids`. Every externally checkable delivered claim needs evidence. |
| `practitioner_check` | `status: found`, `gap` or `not_applicable`, and a concrete `reason`. `found` also requires `source_ids`. Expertise remains attributed. |
| `writing` | `method: Humanizer`, pinned `version`, actual `editor`, `draft: {path, sha256}`, `final_sha256` matching the answer, and `semantic_review`. |
| `review` | Actual `reviewer`, `answer_claim_coverage_checked: true`, `material_citations_checked: true`, `source_entailment_checked: true`, `unresolved_critical: []`. These are reviewer attestations, not automatically inferred truths. |

`semantic_review` needs `reviewer`, `full_text_checked: true`,
`factual_changes_resolved: true`, and a nonempty `invariants` list naming the facts,
numbers, uncertainty, source attribution and technical meanings preserved.

Supported source types are `official_documentation`, `research_paper`,
`author_code`, `standard`, `reproducible_measurement`, `primary_source`,
`first_hand_experience`, and `secondary_source`. Use the specific accurate type.
Primary support is required for a `fact`; a source author's statement can instead
be a `source_claim`, and an attributed observation an `experience`.

Claim types also include `calculation` (with `formula` and `inputs` including
their provenance), `inference`, `hypothesis`, and `recommendation` (each with
`rationale`). A hypothesis must remain identified as a hypothesis in the answer.

Artifact paths resolve inside the job directory. Each referenced file must be
nonempty and at most 4 MiB. Keep bounded extracts with enough context when a page
is longer; do not invent or silently truncate evidence essential to a claim.
The checker rejects paths outside the job, a final answer changed after editing,
missing sources, unresolved ambiguity and a preflight timestamp after searching.
Recorded timestamps and receipt authenticity still depend on the trusted host.

## Return binding

In strict mode, the worker finish record's `answers` must be exactly:

```json
{"delivery_sha256": "<SHA-256 of the manifest's answer file>"}
```

For a frozen benchmark requiring structured outputs, the manifest may additionally
reference `evaluation_fields: {path, sha256}` containing a nonempty JSON object.
The reviewer must include those values in the claim/source/meaning check and set
`review.evaluation_fields_checked: true`. Then `answers` also includes exactly
those parsed values under `evaluation_fields`. Frozen checks address paths such
as `evaluation_fields.current_status`. This keeps benchmark fields bound to
reviewed bytes rather than silently accepting another unreviewed answer.

The other lifecycle fields remain required. The reader-facing answer is the
validated file referenced by the manifest; stdout is the lifecycle record.

For a standalone check:

```sh
python scripts/delivery_gate.py /absolute/job/delivery-manifest.json
```

Success reports `evidence_contract_passed: true` and always
`factual_quality_certified: false` and `improvement_proven: false`. This separates
enforced record completion from the independent evaluation of research quality.

The explicit `lifecycle_only` host option supports synthetic protocol tests and
incomplete adapters. Its receipt reports `evidence_contract_passed: false` even
when begin/finish succeed. It must never be used to hide a failed research check.
