# Compact experience and required improvement diagnosis

The working memory must remain small enough to inspect and reuse. It stores
bounded method cards, distinguishes success from failure and inconclusive work,
and refuses writes when its committed state directory would exceed 5 MiB.
Every finished worker result must also contain an evidence-supported diagnosis
and an improvement decision. A plan is never reported as an executed search.

## Method cards

`finish` requires a `lesson_cards` list containing zero to four cards. Zero is
appropriate when no defensible method lesson was obtained; the required learning
diagnosis must still explain the outcome. Do not manufacture a successful method
to satisfy the format. Record real failed tactics so the next worker can avoid
repeating them under the same conditions.

State what succeeded. Finding and reading an applicable source can justify a retrieval lesson; it does not mean its proposed algorithm or experiment succeeded. Keep that distinction in `context` and `tactic`. Prefer `inconclusive` when the claimed benefit was not tested. For `no_change`, name the case-specific evidence gap and the next useful check rather than copying a generic absence-of-proof sentence.

Each supplied card has exactly these fields:

```text
{
  trigger: when this lesson matters,
  context: conditions that limit its applicability,
  tactic: what was actually tried,
  outcome: "success" | "failure" | "inconclusive",
  next_test: the next useful test or verification,
  evidence_sha256: [one to three actual observation artifact hashes]
}
```

The runtime supplies the scope, stable card ID, first and latest run IDs,
occurrence count and last completion sequence. The **entire stored card** must
fit within **1,500 Unicode characters**, including field names and provenance.
UTF-8 bytes are separately counted against the state directory ceiling. Long
cards are rejected, not silently truncated into a different claim.

Duplicate identity uses normalized trigger, context, tactic, outcome and next
test within the same scope: Unicode NFKC, case folding and collapsed whitespace.
An exact normalized repeat updates the existing card and count. It does not add
another copy. Different meaning, contexts or outcomes are not merged merely
because they seem similar. A card retains up to three recent representative
evidence hashes; the run records retain their additional evidence provenance.

`begin` selects a shared maximum of 16 recent observations and cards for the
exact task scope plus scope `*`. Selection uses recorded completion sequence,
not alphabetical run IDs. The selected entries are returned in chronological
order; within a completion, observations precede cards, with stable ordering
within each kind. A stored card never replaces the entire observation stream:
a newer failure without a card can therefore reach the next task. Both forms
may remain when their meanings differ, including contrary evidence. This is
explicit scope retrieval, not a claim of semantic vector search. Cards are
experience, not automatically accepted global rules. Changing the accepted
policy still requires the separate frozen evaluation and promotion process.

## Required diagnosis and improvement decision

`finish.learning` requires exactly these fields, with optional `research_evidence`:

```text
{
  diagnosis: observed outcome and likely cause,
  decision: "test_improvement" | "no_change",
  hypothesis: bounded proposed change, or empty when not justified,
  search_plan: [{language, query}],
  reason: supported no-change explanation, or other concise rationale,
  evidence_sha256: [actual observation artifact hashes],
  research_evidence: [{language, query, evidence_sha256}]
}
```

Diagnosis, hypothesis and reason are each limited to 1,000 characters. A
`test_improvement` decision requires a nonempty hypothesis and exactly one planned
query in **EN, DE, ZH and JA**. The worker must formulate those searches through
this same skill's function, mechanism, failure, synonym and source-verification
methods, at a depth appropriate to the task. Four language labels alone do not
establish useful formulation or native-language quality.

A `no_change` decision requires a specific nonempty explanation and actual
evidence hashes. It can honestly mean the evidence does not support a policy
change, the current method met the task, or a proposed improvement was rejected.
It must not disguise skipped diagnosis. No-change does not automatically mean
there is nothing worth researching next.

Every referenced evidence hash must match a real artifact already recorded in
this run's observations. A random SHA string, unsupported self-score or proposed
future receipt is rejected.

### Plans versus actual research

`search_plan` describes future work. It never sets
`improvement_research_recorded: true`.

After actual improvement research, the optional `research_evidence` list can
record up to 16 executed queries and the corresponding observation artifact
hashes. A nonempty list must cover EN/DE/ZH/JA. Its rows each contain a language,
the actual query and one to three hashes of real run artifacts. The runtime
checks their hashes and coverage; the host must preserve genuine search-tool
receipts and distinguish a combined result batch from query-specific results.

The returned `improvement_research_recorded` flag indicates that those structured
four-language records exist. It does not authenticate a network call merely
because an author wrote JSON. A real demonstration must use the actual recorded
tool executions. A plan-only run is reported as plan-only; do not call it an
executed improvement experiment.

The next worker receives a `learning_requirement` in its begin brief: diagnose
the outcome, use this same skill to investigate a bounded improvement in the four
languages, and retain an honest supported no-change decision when evidence does
not justify a change. The host enforces presence and structure; actual research
quality remains an evidence and evaluation question.

## Host enforcement and one bounded repair

The normal host worker must return both `learning` and `lesson_cards`. When either
is absent or has the wrong container type, `search_host.py` records `step_missing`
and writes `repair-request.json`. It does not mark learning complete.

A controller can configure exactly one diagnostic repair attempt by adding both
of these fields to its trusted worker configuration:

```text
diagnostic_worker_argv: [the existing authorized worker executable and arguments]
diagnostic_timeout_seconds: positive seconds, at most 900
```

The diagnostic worker receives the same brief, `phase: "diagnostic_repair"`, the
original result and the repair request. It returns exactly
`{"learning": ..., "lesson_cards": ...}`. It cannot replace the answer, original
binding or permissions through this repair protocol. Its evidence must refer to
the original run's genuine observation artifacts. If new research is necessary,
perform it in a new bounded research run rather than fabricate missing receipts.

The repair deadline is the lesser of its configured allowance and the time left
in the **original** worker deadline. There is no additional unbounded budget or
retry loop. No configured hook, no time remaining, invalid repair or failed
validation leaves `accepted_host_completion: false` and
`learning_completed: false`. After a successful repair, the receipt keeps both
`step_missing` and `step_repaired` for traceability. The revised full result is
saved separately from the original worker stdout.

The hook uses a controller-selected existing worker. The skill does not pick a
paid model, start a daemon or expand permissions. A worker that already returns a
valid diagnosis receives no additional model call.

## State ceiling and explicit compaction

The write ceiling is **5 × 1,024 × 1,024 bytes** for the committed learning-state
directory, including `state.json`, evidence `objects` and other existing files
there. Both evidence-object writes and state commits check capacity first. A
failed commit cannot make a candidate accepted; an unreferenced object from a
failed transaction can remain within the ceiling until explicit compaction.

Atomic replacement can temporarily require an additional pending state-file copy.
The ceiling describes committed persistent learning files, not an operating-system
disk quota, RAM limit or a promise that temporary I/O is zero. External host job
logs, original task artifacts, evaluation files and canonical memory services have
their own retention rules. Do not claim the entire computer or all host logs are
bounded by this library's 5 MiB.

When capacity approaches the limit, use the executable two-step operation:

```sh
python3 scripts/recursive_search.py --state-dir STATE compact PLAN_INPUT.json
python3 scripts/recursive_search.py --state-dir STATE compact APPLY_INPUT.json
```

Plan input is `{"mode": "plan"}`. This is read-only and returns a deterministic
manifest with the current state hash, affected closed ordinary runs, raw objects
to remove and `plan_sha256`.

Apply input is:

```text
{
  mode: "apply",
  plan_sha256: the exact reviewed plan hash,
  acknowledge_raw_evidence_removal: true
}
```

An already authorized controller may apply that manifest automatically under its
stored retention policy. This protocol is not an instruction to ask the user for
permission again each time. A stale or changed plan is rejected and must be
recomputed against the current state.

After validating the exact acknowledged manifest, compaction may first delete
only objects that are already unreferenced by the currently committed state.
This permits recovery when a failed write left an orphan object near the limit.
Objects still referenced by that state remain until atomic replacement succeeds.
If replacement fails, the previous state and every object it references survive;
an already unreferenced orphan may have been removed. Recompute a fresh manifest
before retrying. This does not raise the 5 MiB ceiling.

Compaction retains active and rollback policies, candidate and rejection records,
all trial records, open runs, compact cards, answer hashes, evidence hashes and
source-run provenance. It replaces verbose closed ordinary-run payloads with
summaries, shortens their legacy observation text to 300 characters with explicit
truncation markers, summarizes old event payloads while preserving original hash
anchors, and removes raw objects no longer referenced by retained records.

**This is deliberately lossy.** Full old answers and raw evidence may no longer
be replayable from the learning directory alone. The manifest makes that removal
explicit. No hidden archive is created elsewhere. If retained essentials still
cannot fit, writes stop; the code does not silently discard rejected hypotheses,
accepted policy provenance or arbitrary user files to keep running.

For the local Reinis deployment, publish accepted lessons through the existing
canonical memory adapter. Do not create a competing authoritative personal-memory
database. This portable state is the bounded execution and learning cache; claim
the native integration only after its real context and next-load receipts exist.
