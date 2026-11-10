# Executable recursive research lifecycle

The standard-library program `scripts/recursive_search.py` persists experience,
loads it on the next invocation, freezes policy candidates, computes a declared
benchmark from answer artifacts, promotes an eligible policy and restores a
previous policy. It does not call a model, search the web or keep itself running.
The host agent performs the research and calls these lifecycle operations.

## What this adds beyond a static skill

1. `begin` returns the active policy's content hash and up to 16 recent, scoped
   observations and cards from finished ordinary research runs, selected in one
   shared completion-order window. Old cards do not hide newer failures. This output must enter the
   worker's actual context before the worker searches.
2. `finish` is bound to that exact begin receipt. The worker records how it used
   each loaded lesson and strategy, the outcome and hashed evidence files.
3. A useful observation survives the session but remains unvalidated. The worker
   may propose a bounded policy change using completed development runs.
4. A separate evaluator freezes held-out tasks, answer checks, model, environment,
   equal per-task budget and minimum gain before either comparison arm starts.
5. Evaluation computes scores from the recorded answers and frozen answer checks;
   manually supplied outcome scores do not decide acceptance. Four distinct
   reviewer records are also required.
6. Promotion changes the active policy pointer. The next `begin` returns the
   accepted hash and instructions. Rollback preserves the complete history.

Each new use can therefore start with relevant prior experience and a tested
policy revision, when one has qualified. A run that finds no supported improvement
must record that uncertainty instead of manufacturing a lesson or changing rules
to claim progress. There is no guarantee that every individual search improves.

## Host binding and authority

A working host must run `begin` before research, inject the returned brief, retain
the returned `begin_sha256`, and run `finish` when it has an outcome. Model
instruction compliance alone is not enforcement. A host wrapper can refuse to
accept an unbound result; the portable program cannot force an arbitrary AI or
application to call it.

The frozen constitution accompanies every brief: EN/DE/ZH/JA by default, explicit
user language overrides, existing permissions and budgets, evidence boundaries,
separate evaluation and honest claims. Candidate policies cannot change the
program's command schema or constitution fields. The host must still keep
candidate instructions subordinate to those rules.

For the Reinis OpenBot/Hermes deployment, use the existing shared context and
episode-publishing interfaces. Keep the canonical memory store authoritative;
do not create a second authoritative personal-memory database. A runtime state
directory can be an execution/provenance cache whose receipts and accepted
learning are published through that existing interface. Do not claim this binding
exists until an actual context receipt and next-run load have been checked.

Use an external scheduler only when continuous or scheduled work is authorized.
The host must enforce the task deadline, process ownership and resource caps.
This CLI starts no daemon, paid job, model download or network request.

## Commands and exit status

All paths supplied inside JSON must be absolute. Every invocation emits JSON.
Exit 0 means a command was processed; an evaluated candidate can validly be
rejected with `eligible: false`. Exit 1 means invalid input, inconsistent state or
an operation that is not allowed, such as promotion after rejection.

```sh
python3 scripts/recursive_search.py --state-dir /absolute/private/state init /absolute/init.json
python3 scripts/recursive_search.py --state-dir /absolute/private/state begin /absolute/request.json
python3 scripts/recursive_search.py --state-dir /absolute/private/state finish /absolute/result.json
python3 scripts/recursive_search.py --state-dir /absolute/private/state propose /absolute/candidate.json
python3 scripts/recursive_search.py --state-dir /absolute/private/state freeze /absolute/plan.json
python3 scripts/recursive_search.py --state-dir /absolute/private/state evaluate /absolute/evaluation.json
python3 scripts/recursive_search.py --state-dir /absolute/private/state promote /absolute/decision.json
python3 scripts/recursive_search.py --state-dir /absolute/private/state rollback /absolute/rollback.json
python3 scripts/recursive_search.py --state-dir /absolute/private/state status
python3 scripts/recursive_search.py --state-dir /absolute/private/state export
```

The paths above are placeholders, not completed execution receipts. Create real
inputs for the intended host. Do not publish a private `export`: it contains task
content, local paths, observations and evaluation records.

## JSON schemas

Unknown fields are rejected. IDs contain ASCII letters, digits, dots, hyphens or
underscores, start with a letter or digit, and are at most 96 characters. Numeric
values must be finite. Duplicate JSON keys are rejected.

### Initialize

```json
{
  "owner_id": "controller",
  "policy": {
    "version": "baseline-1",
    "instructions": "Follow SKILL.md and apply the strategies relevant to this task.",
    "strategies": [
      {"id": "source-check", "scope": "*", "instruction": "Read the current primary source before reporting readiness."}
    ]
  }
}
```

This is a configuration example, not a claimed experiment. A policy requires a
version, instructions and 1–64 strategies. Strategy scope is descriptive context;
the host decides relevance and accounts for every returned strategy at finish.

### Begin ordinary research

Required fields: `id`, `task`, `scope`, `model_id`, `environment_id`, and
`budget: {"unit": "search_calls", "limit": 12}`. The budget unit is chosen by the
host; the limit must be positive. The program checks the recorded cost against
that limit, while the host enforces actual spending and time.

The response includes `run_id`, `begin_sha256` and `brief`. The brief contains the
active `policy_sha256`, version, instructions, strategies, task, environment,
budget, constitution and `loaded_lesson_ids`. Each observation has a stable
`lesson_id` of the form `earlier-run/observation-id` and the status
`unvalidated_observation`. Ordinary research loads recent observations with the
same scope, plus observations with scope `*`. Evaluation runs do not receive
ordinary-run or earlier evaluation feedback.

### Finish

Required fields:

- `run_id` and the exact `begin_sha256` returned by begin.
- `answers`: a JSON object containing the actual structured answer. Keep the
  full readable response in an evidence artifact when appropriate.
- `metrics`: exactly `precision`, `utility`, `innovation`, `clarity` (each 0–1,
  or `null` when not evaluated) and nonnegative numeric `cost` in the declared
  budget unit. Never substitute zero for an unmeasured quality. These are stored as agent
  assertions, never used as acceptance scores. Cost is also an assertion unless
  the host provides independent metering.
- `observations`: 1–16 objects with `id`, `kind` (`failure`, `useful` or `unknown`),
  `text`, and 1–16 evidence objects. If no improvement is supported, use an honest
  `unknown` observation tied to the actual run receipt.
- `learning_use`: one `{lesson_id, status, reason}` record for every loaded lesson.
- `strategy_use`: one `{id, status, reason}` record for every loaded strategy.
  In both use lists, status is `applied` or `not_applicable`, with a specific
  reason. No missing, additional or duplicate IDs are accepted. An empty list is
  required when there were no loaded lessons. These declarations document use;
  they do not prove a model's internal reasoning.
- `learning`: the evidence-backed diagnosis and either a bounded improvement
  hypothesis with an EN/DE/ZH/JA search plan, or a supported no-change reason.
- `lesson_cards`: zero to four compact method cards. Both fields are mandatory;
  their exact schema and the 5 MiB state limit are defined in
  [compact-memory-contract.md](compact-memory-contract.md).

Each evidence object is `{"path": "/absolute/receipt.json", "sha256": "…"}`.
The tool checks actual file bytes against the supplied SHA-256 and copies them
to a content-addressed object. Artifacts must be regular files, at most 16 MiB;
symlink file targets are refused. Hashing authenticates bytes, not the truth of
their contents or the identity of their author.

### Propose

Required fields: `id`, `author_id`, `base_policy_sha256`, `policy`, `reason`, and
`source_run_ids`. The policy schema is the same as initialization. Its version
and content must differ from the active baseline. Source runs must be completed
ordinary research runs, never held-out trial runs. The proposal is frozen as
content and does not change the active policy.

### Freeze the comparison

Required fields: `id`, `candidate_id`, `evaluator_id`, `suite_path`, `dev_task_ids`,
`model_id`, `environment_id`, `budget`, and `objective`.

`evaluator_id` must differ from the candidate author. `dev_task_ids` must include
every candidate source run ID. The objective is
`{"metric": "precision", "min_gain": 0.1}`; any of the four metrics may be the
objective, and minimum gain must be greater than 0 and at most 1.

The suite is a separate absolute JSON file outside the learner state directory:

```json
{
  "id": "heldout-suite-id",
  "tasks": [{
    "id": "unseen-task-id",
    "prompt": "The actual held-out research question, without its answer.",
    "checks": [
      {"field": "recommendation.readiness", "op": "equals", "expected": "source-inspected", "metric": "precision", "critical": true}
    ]
  }]
}
```

The snippet demonstrates one check; a valid complete suite must contain checks
for **all four metrics** across its tasks. Each check requires `field`, `op`,
`expected`, `metric` and a literal boolean `critical`. Dot-separated fields
address nested keys in `answers`. Supported operators are `equals`, `contains`,
`at_most`, `at_least` and `present`; `present` expects literal `true`. Equality is
type-sensitive. A numeric check expects a finite nonnegative number.

The evaluator must justify the gold answers and design the checks before seeing
the candidate's held-out results. Precision can check known factual labels;
utility can check required actionable decisions; innovation can check a useful
mechanism independently established for the task; clarity can check that the
recommendation, reason and next action are unambiguously present or correctly
identified. These are **operational proxies**, not a complete definition of
those qualities. In particular, satisfying required answer fields does not prove
that a person understands the prose. Record actual user comprehension separately
when that matters; never relabel word count as understanding.

Freeze pins the suite's exact bytes. It rejects development/test ID overlap,
previously exposed identical task prompts, and any suite, task IDs or identical
prompts already reserved by another trial. Renamed or paraphrased duplicate
tasks still require evaluator judgment. The code does not detect semantic data
leakage. Gold answers are never included in a `begin` brief.

### Run the frozen arms

Call begin with exactly `id`, `trial_id`, `task_id`, and
`arm: "baseline"` or `arm: "candidate"`. It loads the pinned arm policy, task
prompt, environment and equal budget. Each trial/task/arm can start once; there
is no selecting the best of unregistered retries. Predeclare stochastic repeats
as separate cases in the original suite. A host interruption remains an open
run in `status`; do not claim a finished comparison or silently replace it.

Finish both arms using the normal finish schema. The answer is hash-bound to the
run and becomes part of the durable record. Keep the evaluator's gold answers
outside both worker contexts and write access.

### Evaluate

Required fields: `trial_id`, `evaluator_id`, `pairs`, `audits`.

Each pair is `{task_id, baseline_run_id, candidate_run_id}`. Pairs must cover the
frozen suite exactly, with distinct finished runs bound to the right trial, task,
arm and policy. Each audit is
`{role, auditor_id, path, sha256, finding, unresolved_critical}`. The finding is
nonempty text and `unresolved_critical` is a literal boolean. Roles are exactly
`optimism`, `skepticism`, `conservative`, `innovative`; auditor IDs must be distinct
and different from the candidate author. Audit files must be nonempty, validly
hashed and have distinct contents. These checks do not authenticate independent
people or model instances; the host must arrange the actual separate reviews.
Any declared unresolved critical objection blocks eligibility. Noncritical
disagreement remains in the record; acceptance is not a majority vote or a
requirement for unanimous praise. The evaluator is responsible for a faithful
summary of the actual audit, not merely a convenient boolean.

The evaluator rereads and verifies the frozen suite, compares recorded answers
with its checks and computes the fraction passing within each metric. Every
candidate critical check must pass. No metric's aggregate score may regress,
including clarity, and the declared objective gain must meet its frozen minimum.
Important individual failures should be critical; averaging can otherwise hide
an individual noncritical decline. Equal maximum budgets are checked. Actual
metering, acceptable quality/cost tradeoffs, statistical confidence and rubric
validity still belong to the independent evaluation protocol.

The response gives `eligible`, `computed_scores`, `bounded_benchmark_gain`,
`failures`, exact check outcomes and audit hashes. A valid rejection is preserved
and leaves the active policy unchanged.

### Promote or roll back

Promotion input is `{trial_id, evaluator_id}`. It requires an eligible evaluation,
unchanged frozen suite and the same still-active baseline. It changes the active
pointer and retains the prior version. Call begin again and verify its returned
policy hash before claiming the next worker actually loaded the accepted policy.

Rollback input is `{policy_sha256, reason}`. The target must previously have been
active. Candidate versions that never qualified cannot be activated through
rollback. History and rejection evidence are preserved.

## Storage, recovery and verification boundaries

`state.json` is replaced atomically after a transaction. It includes a checksum
and a chained event history. Evidence is stored at `objects/SHA256`. A process
lock prevents concurrent writes. An interrupted write can leave an unused object
or temporary file; the last committed state stays authoritative. A stale lock is
not automatically removed: first inspect its process and retained state, then
recover explicitly. Do not delete another live task's lock.

The committed learning state directory, including JSON and evidence objects, has
a 5 MiB write ceiling. Scoped lesson cards are at most 1,500 serialized characters.
The executable `compact` plan/apply operation deliberately removes specified raw
closed-run payloads while retaining policies, cards, rejection/trial records and
hash provenance. It is not lossless and creates no hidden growing archive. See
[compact-memory-contract.md](compact-memory-contract.md) for the explicit manifest,
controller retention policy and limits; unrelated host logs have a separate budget.

Hash checks catch accidental changes; they are not signatures. An agent with
arbitrary write access to this program, state and evaluator files can forge or
bypass the protocol. Separate filesystem/process permissions or a trusted host
controller are required for enforcement. Different IDs and different paths alone
do not create that isolation. Report the actual deployment boundary honestly.

Every response retains `improvement_proven: false`. A passing computation is
reported as a gain on the frozen answer checks, with its evidence and limitations.
Mechanism tests demonstrate persistence, load binding, evaluation, promotion and
rollback. They do not demonstrate general search superiority, human readability,
model-weight training or a functioning background service.
