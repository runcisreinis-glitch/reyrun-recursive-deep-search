# Executable delivery evidence check

Start with the four core languages EN/DE/ZH/JA. Additional executed languages use uppercase tags such as LV, FR or KO. For an explicitly narrower profile, honor the user and report the strict check as unavailable.

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

New strict deliveries use `reyrun-delivery-v7`. Retain earlier receipts with their original schema. The offline manifest checker can still read v6 archived deliveries without awarding new checks. Connected v7 workers add the per-topic reading levels and method summary below for published cases.

| Field | Required content |
| --- | --- |
| `schema`, `run_id`, `begin_sha256` | Schema name and the exact host input binding. |
| `answer` | `{path, sha256}` of the actual UTF-8 answer. |
| `task_clarity` | `goal`, `decision: ready`, `unresolved_ambiguities: []`, timezone-aware `checked_at`. Record this before searching. Preserve any real or clearly simulated clarification separately. |
| `queries` | Actual executed queries: `language` (core or additional), `query`, timezone-aware `executed_at`, and `receipt: {path, sha256}`. Each core language needs an executed query. Include all approved follow-up languages in this ledger. Duplicate queries do not add coverage. |
| `sources` | `id`, actual `url`, `type`, content `language` (executed language tag, mixed, or other), `read_state: read`, timezone-aware `read_at`, supported `scope`, and `evidence: {path, sha256}` for retrieved source content. A search snippet does not qualify as a read source. |
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

## Innovation and independent review records

Add an `innovation` object. For every `query` reference below copy the exact `{language, query}` pair from the executed query ledger.

- `transfers` contains at least two objects. Record `mechanism`, originating `domain`, `adaptation_gap`, `falsification_test`, `result` and `query`. Distinguish a tested result from an untested proposal.
- `usual_field_keyword` is the normal field term in the language of the `outside_query`. Record the actual executed query that omits it, using the usual query-reference structure.
- `overlooked_component` contains the executed `query`, concrete `finding`, and `status`. For `inspected`, cite the read ledger's `source_id`. If nothing qualified, use `no_candidate`.

Freeze the answer bytes before review. Give the same draft and its evidence to four independently dispatched, fresh sessions. Assign one role to each (`optimistic`, `skeptical`, `conservative`, `innovative`). Each sees the evidence without other reviews. Sequential isolated sessions are fine. The ordinary worker must never mint the dispatcher's receipts. Use an existing authorized dispatcher; no model service is bundled.

Each session writes a UTF-8 JSON report containing `role`, `instance_id`, `run_id`, `answer_sha256`, a concrete `finding`, `alternative` (a less obvious option or reason it failed), and `verdict` (`accept` or `concern`). The trusted dispatcher captures that session's real identifier and result, then records `{run_id, instance_id, report_sha256, isolated_initial_review: true}` as UTF-8 JSON in its own registry at `<review_receipt_dir>/<run_id>/<role>.json`. Preserve the exact receipt bytes in the job as well.

Add `independent_review` with `author_instance`, four `reports` rows (each has `role`, `instance_id`, `report: {path, sha256}` and `dispatch_receipt: {path, sha256}`), `decisions` mapping all four role names to their concrete dispositions, and `unresolved_critical: []`. Address meaningful disagreements explicitly. If a finding changes the answer, freeze the revision and obtain four fresh reviews for it. If only one chat can review, disclose that fact and continue a limited answer; never create four fictional IDs.

Standalone validation without the controller registry checks file structure and integrity and reports `controller_receipts_matched: false`. The strict host always requires independently retained receipt bytes. Trust ultimately rests on the dispatcher and the operating system's access controls. Neither a hash nor a successful check proves a novel result or factual correctness.

## Adaptive practitioner routes and practical delivery

Add `practitioner_routes.professions`. Each object has `profession`, `category` (`direct` or `adjacent`), a transferable `method`, and an array of actual `venues`. Include both a direct and an adjacent professional perspective. For each venue record the actual `url`, `name`, `type` (association, workshop, journal, forum, chat or other), executed `query` reference, `status` (read, inaccessible or no_relevant_result) and `finding`. A read venue requires `source_ids` including material from its own host. For inaccessible or empty results retain the query and the limitation; do not cite inaccessible testimony.

Add `practitioner_routes.rounds` with `first_queries` (executed query references across EN/DE/ZH/JA), `first_result` (sufficient or insufficient) and `reason`. If insufficient, record `specific_gap`, distinct executed `followup_queries` including another relevant language and at least one new named professional venue; then `outcome` (resolved or remaining_gap) and `finding`. A resolved gap requires read `source_ids`. Bind each venue to the actual query that reached it. Do not guess when evidence runs out.

Add `practitioner_routes.adaptive_decisions` as an ordered array. Each row has a unique `id`, `after` (user_question for the initial row; otherwise an earlier decision ID), `stage` (profession, query, venue_language, validation or practical_option), `observation`, `shared_principle`, `alternative`, `test`, `outcome`, and an `anchor`. An initial anchor can be `{"kind":"question"}`; later cite a read source via `{"kind":"source","id":"s1"}` or an executed query via `{"kind":"query","ref":{"language":"LV","query":"…"}}`. Cover all five stages, and name the selected `profession` in a profession-stage row for every listed profession. Use real observations and explain where the unexpected route came from. Mark an untested proposal plainly.

Add `practical_answer` containing `direct_answer`, `alternatives` (or why none qualified), `benefits`, `leader`, and `latvia`. The benefits map contains time, money and effort. Each contains `basis` (measured, reasoned, unknown or not_applicable) and `explanation`; measured and reasoned benefits require a checked `claim_id`. Measured gains also require a `baseline` and `unit`. Both leader and Latvia contain `status` (verified, gap or not_applicable) and `reason`. A verified row requires read `source_ids`; include the leader's `criterion` or Latvia's `availability_or_delivery` and a timezone-aware `checked_at`. Present what matters for this question in the answer. Semantic reviewers must verify these records genuinely appear in or support the delivered conclusion. A checklist cannot establish novelty, professional identity, market leadership or quality by itself.

## Compare every significant action and final sentence

On each adaptive decision, supply `ordinary_approach`, `contribution` and `comparison_result` (`adds_value`, `retains_necessary_fact` or `revised`). Compare the actual action with the obvious default. If no useful difference can be explained, revisit the choice, perform a better test, then update the result. Also revisit intermediate findings during independent review. Scale the comparisons to the question.

After editing, generate units with `delivery_gate.sentence_units(final_text)`. Create one `sentence_review` row per unit, in order, with its exact `text`. Inside each row, supply a nonempty `sentences` array. Split multi-sentence units at actual language-aware sentence boundaries; preserve spaces so joined text reconstructs the unit. Each subrow includes `text`, `ordinary_approach`, `contribution`, `evidence_or_basis`, `utility`, and `result` (adds_value, retains_necessary_fact, revised or no_improvement). A revised row also records `previous_text`. If a sentence adds nothing, revise or remove it and recheck the full draft before sending it to the four reviewers. An essential unchanged fact or source may stay with its exact contribution; do not decorate it or invent novelty. A useful difference from a generic answer is not a claim of novelty within a profession. Any field-wide novelty claim needs appropriate independent evidence. Keep plain wording, numbers and qualifications intact.

The checker matches every final text unit and derives the count of unresolved comparisons from the sentence records. A no_improvement row blocks strict delivery. Only report zero after the checked records return that value. If review cannot finish, identify the actual unfinished items; never invent a zero or a reviewer.

## Map overlooked questions before the main search

Before running the first query, freeze a UTF-8 JSON plan: `run_id`, `begin_sha256`, `frozen_at` and `routes`. Each route has a unique `id`, specific `question`, at least two different `formulations`, `why_missed` and an intended `venue`. Add its artifact reference as `overlooked_search.plan`. Keep actual observations out of the frozen plan; write them separately under `overlooked_search.outcomes`, keyed by each route ID. Each outcome has `status` (read, no_result or unavailable), `finding`, executed `queries` and read `source_ids`. If a route cannot be executed, explain exactly why. The controller can retain a pre-search hash to corroborate timing. Self-reported timestamps without a witness remain attestations.

Record executed `baseline_queries` in the same block. Ordinary routes provide the comparison. For strict review, distinct queries exclusive to overlooked directions must outnumber the baseline queries. Query count is only a check on prioritization: reviewers must decide whether the search formulations were genuinely different and useful and reject padding.

Under `overlooked_search.first_answer`, record the `strongest_finding` backed by `source_ids`, plus `options` keyed by conservative, innovative and frontier. For each give a concrete `option`, `readiness` (ready, limited, experimental, unverified or no_candidate) and `reason`. Frontier means the leading edge of the relevant field. Compare actual readiness; do not invent an option just to fill a category. A `price` row has status verified, gap or not_applicable and a reason. A verified price also requires amount, currency, scope, checked_at and read source_ids. Use the verified Latvian availability record where relevant. Add two to four different `next_directions`, each with a specific `question`, `where` and `purpose`. In the answer, fit these into short practical choices; keep internal records off the reader's page.

### First-hand sequence before official lookup

The frozen plan and clarification may precede internet lookup. Once research starts, first read an accessible professional or owner's first-hand account. This applies to ordinary comparison and overlooked routes alike. Search named communities, associations' member discussions, clubs, practitioners' workshop posts or public chats. Record an observed detail and check that specific detail in official material only after reading the account. A later official page can confirm a specification, version or price; the experience remains attributed to its actual author. Retain public URLs and bounded relevant evidence, avoid personal identifying details, and do not claim access to private groups.

Record `firsthand_sequences` rows with `covers` (route IDs `research:<plan route id>` and/or `profession:<normalized profession name>`), `relevance`, `status`, `human_source_id`, `experience_type` (practitioner, owner, operator or maintainer), `observed_detail`, `human_query`, `official_source_id`, `official_query` and `official_check`. Both query references address actual executions, and both source IDs reference read artifacts with URLs. Record what the official source actually confirms or contradicts. Cover every practitioner and overlooked route. One observation can serve several genuinely related routes if its relevance is explained. To pass strict checks the human query must precede the first-hand read, which must strictly precede the official query, which in turn precedes the official read. A missing human account or confirmation is a reportable gap, not a verified route. Machine checks cannot establish that a forum contributor really holds a claimed professional role.

### Worked questions for the overlooked map

The following concrete questions illustrate generation, not a profession list or pre-decided answers.

| Observation and specific question | Two searches worth trying | Why it is missed, where to check and how to test |
| --- | --- | --- |
| A waffle stays crisp on a rack but softens only after it is packed. How much steam can escape without making it cold? | “vented takeaway packaging crisp fries condensation” / “food delivery ventilation aperture heat retention cardboard” | Recipe searches focus on batter. Look for packaging engineers' design notes or delivery professionals' trials. Use the same waffle, box volume, travel time and temperature measurements in a vented versus unvented comparison. |
| A book title is legible at full size but disappears over a textured image in a phone thumbnail. Can a cartographer's label buffer improve recognition at the same font size? | “kartografische Beschriftung Puffer Lesbarkeit Hintergrund” / “map label halo radius contrast complex raster background” | Cover-design searches often change the font or enlarge the title. Read cartographers' actual labeling guidance and test identical thumbnail crops, with and without a restrained halo, at the target phone size. |

Examples of later official checks after a first-hand starting point has been found: [QGIS's labeling documentation](https://documentation.qgis.org/3.44/de/docs/user_manual/style_library/label_settings.html) describes a text buffer; [Huhtamaki's packaging brochure](https://www.huhtamaki.com/globalassets/foodservice-eao/fs-campaign-takeaway-and-hd/packaging-that-delivers-brochure-2021.pdf) lists vented takeaway packaging. These are real leads, not field trials on book covers or waffles. Use similarly specific questions rooted in the current user's observations. Report a transfer as untested until a suitable comparison supports it.

## First-screen answer and optional evidence

Record `task_clarity.requested_geographies` during clarification (an array containing local and/or global only when relevant). `answer_layout.intro` must equal the first paragraph of the final answer and contain two or three complete sentences. The first paragraph answers the question on its own. Include exact `local` and/or `global` result excerpts or explicit remaining gaps when those scopes were requested. In `answer_layout`, `price` and `wait` each carry status verified, gap or not_applicable. A material price or wait needs exact `wording` from the intro, and verified claims require read `source_ids`. The price disposition must match the research.

For a verified leader, add `leader_measure` with `requested_metric`, `source_metric`, `population`, `place` and `period`. Canonicalize truly equivalent names for the same measure, retain the source's actual units, and never relabel a proxy as the target. If car sales by make and color are requested, check those dimensions, location and period. Active advertisements and first-time registrations are separate measures unless the question explicitly asks for them. When the required cross-tabulation is unavailable, mark the leader as unknown.

Specify `language` and `more_heading` in `answer_layout`. Leave a blank line after the opening, then print the heading. For Latvian use **Ja vēlaties uzzināt vairāk**. Under it, `topics` contains two to four distinct items for an ordinary chat. A v7 published case includes all distinct topics justified by the evidence, with a minimum of two and no upper limit. The separate suggestions in `next_directions` are possible new questions, not the count of completed reports. Each has one `insight` actually shown in the optional part, an `origin_id` from the first-hand sequences, read `source_ids` and an actual `research: {path, sha256}` artifact that includes those source URLs and the completed investigation. A future research suggestion is labelled as such and does not replace completed evidence. Put the conservative, innovative and frontier comparisons here when they are secondary to the opening.

For `format: html_details` include the completed HTML segment with a real `<details id="…"><summary>…</summary>…</details>` in the output and use its id as `target`. For `format: chat_link` put the actual Markdown link in the output. A `sandbox:` target must resolve to the same packaged artifact in a reader-accessible environment. For a hosted HTTPS target, attach `link_check: {path, sha256}` whose retained JSON records requested_url, HTTP status 200, checked_at and content_sha256 of the retrieved research document. A fragment requires the destination's actual section ID. The runtime must verify the reader's access independently of an editor-only login. Do not emit invented links or empty “open” controls.

## Published cases

Choose `task_clarity.format` as `chat` or `published_case`. Published cases require two genuine levels connected by a working button. Read and verify the published control in the supported interfaces; a JSON manifest alone cannot check a web interaction. The accessible reader level explains the question, practical result and what the visitor can do. The professional level includes methods, original or appropriately redacted data, findings, named read sources, limitations, separate reviewer arguments and the editor's conclusion. Avoid exposing private user data.

In `publication_layers`, `reader`, `professional`, `method` and `data` are artifact references. Include `source_ids` whose URLs appear in the professional file, and the published limitations excerpt in `limitations`. Freeze this substantive packet before requesting the reviews. For each topic set `reading_levels: {reader_excerpt, professional_excerpt, claim_ids}`. The excerpts must be distinct visitor-facing passages inside that topic's own report or linked HTML section. The shared claim IDs refer to the ledger findings both passages express. Review them side by side for equal scope, units and uncertainty. Let each professional report carry the evidence its finding warrants: sample, calculation, limitations, primary data and useful charts, as applicable. Never invent measurements to fill a format.

End the case with a short `method_summary: {decision_id, innovation_excerpt, recursion_status, lesson_ids, recursion_excerpt}` inside `publication_layers`. Point to what actually changed course, the outcome and where the reader can see the evidence. Link the decision ID to the adaptive trail. Both excerpts must appear in the published reader or professional text. For `recursion_status: applied`, name the relevant lesson IDs loaded and applied in this run; otherwise use `none_applied` and an empty array. State first-run, inaccessible or unhelpful prior experience accurately. Creating a note and applying a note are separate events. The strict host compares the claim to the worker's actual use of the supplied brief.

To compute `case_sha256`, start with the four artifact names and their SHA-256 values. Add `topics` as an array in display order of `{target, research_sha256, reading_levels}`; add the complete `method_summary` object. Use `json.dumps(packet, sort_keys=True, separators=(",", ":"))` with Python's default ASCII escaping; hash the resulting UTF-8 bytes with no newline. Each independent report must cover the exact `answer_sha256` and this `case_sha256`. If a substantive file changes, obtain fresh reviews for the revised packet.

Attach `editorial_decision` after review. Its `conclusions` must contain four role keys, each with the actual `instance_id`, exact `report_sha256` and its own `conclusion`. Label paraphrases and preserve original statements where authorized. `synthesis` weighs the arguments, disagreements, evidence and remaining uncertainty and explains the editor's final decision. Record `unresolved_critical`. Keep this editorial appendix separate from the frozen substantive material to avoid a circular hash. A case describing a prior experiment must explicitly distinguish a review of that experiment's frozen answer from a review of the expanded publication. Four headings or unbound summaries cannot satisfy strict publication mode.

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
