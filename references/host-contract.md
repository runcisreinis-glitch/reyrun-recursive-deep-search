# Bounded host wrapper

The strict host checks EN/DE/ZH/JA in the initial round and supports additional executed languages. When core evidence is insufficient, a targeted second round must include another appropriate language and a new professional venue. Honor explicit user restrictions and label incompatible strict profiles as limited.

`scripts/search_host.py` is an executable host entry point for one research
invocation. It calls the persistent lifecycle itself, gives the configured worker
the current brief, validates the returned binding and commits finish. It does not
report accepted host completion when the worker skips or misbinds those steps.

It contains no model, paid API, search service or daemon. The controller supplies
an existing worker. OpenBot or Hermes can use the same stdin/stdout protocol
through an adapter to their existing runtime.

## Invocation

Initialize the persistent state once with `recursive_search.py init`. Then call:

```sh
python3 scripts/search_host.py \
  --state-dir /absolute/private/state \
  --config /absolute/controller/worker.json \
  --request /absolute/task/request.json \
  --output-dir /absolute/task/new-job-directory
```

The command paths are placeholders. The output directory must not already exist.
An existing directory is a signal to inspect its receipt before any retry, not a
reason to overwrite evidence or run the worker twice.

The controller-owned configuration requires these fields:

```json
{
  "controller_id": "controller",
  "worker_argv": ["/absolute/python", "/absolute/existing-worker.py"],
  "worker_cwd": "/absolute/worker-directory",
  "timeout_seconds": 600
}
```

`controller_id` must match the state's `owner_id`. This is a consistency check,
not account authentication. The directory must exist, arguments must be an array
of nonempty strings, and timeout must be greater than zero and at most 900 seconds.
The wrapper invokes the configured program with `shell=False`. It never constructs
a shell command from the task, model response or downloaded instructions.

The trusted controller chooses and protects the executable, arguments and
configuration. Do not let the learner replace them or provide shell programs as
a workaround for that boundary. The worker inherits the host process environment;
configure that environment for the existing authorized worker. The wrapper does
not discover or request credentials, select a paid service or download a model.

The default `delivery_gate_mode` is `strict`. Read [delivery-manifest.md](delivery-manifest.md)
before implementing the worker. To complete strict delivery, configure `review_receipt_dir` with an absolute, controller-owned directory outside the job. A trusted dispatcher must launch four isolated reviewer sessions and save their receipts there. The worker can read or receive copies of its own receipts, but must have no write access to that directory. Enforce that separation with service accounts or a remote dispatch service. A shared OS identity by itself is not an isolation boundary. Without a dispatcher, identify the result as limited. The explicit `lifecycle_only` option is reserved
for labelled mechanism tests or an openly incomplete adapter. It does not produce
an accepted evidence-contract check. Existing adapters must add the manifest and
checked answer binding to use strict mode.

The request is exactly a `recursive_search.py begin` input, either an ordinary
research request or one frozen evaluation arm. See
[runtime-contract.md](runtime-contract.md) for its fields. Task, goal, context,
budget and constitution are passed from the recorded begin brief without adding
new permissions. Longer authorized work needs separately bounded invocations and
an external scheduler or supervisor, not a self-extended deadline.

## Worker input and output

The worker receives one UTF-8 JSON object through stdin:

```text
{
  protocol: "reyrun-search-worker-v1",
  run_id,
  begin_sha256,
  brief,
  artifact_dir,
  deadline_utc,
  delivery_gate_mode,
  delivery_manifest_schema,
  delivery_manifest_path
}
```

This schematic is a field description, not literal executable JSON. `brief`
contains the active policy, immutable constitution, scoped prior observations,
loaded lesson IDs and exact resource context. `artifact_dir` is the absolute new
job directory. The worker can place its research receipts there.

The worker adapter must put the brief and delivery requirements into the actual acting model's context
before research. Passing stdin proves delivery to the configured program; by
itself it does not prove that an arbitrary program forwarded those bytes to a
model. Verify a real adapter with its context receipt and the next invocation.

The worker returns exactly one finish-schema JSON object on stdout:

```text
{
  run_id,
  begin_sha256,
  answers,
  metrics,
  observations,
  learning_use,
  strategy_use,
  learning,
  lesson_cards
}
```

Diagnostic output belongs on stderr. `run_id` and `begin_sha256` must match the
actual input; the wrapper does not silently fill or correct them. All other
fields go through the strict lifecycle validator, including exact coverage of
loaded lesson and strategy IDs and hashing of the real evidence files.

In strict mode `answers` references exactly the checked delivery SHA-256, as
specified in the manifest contract. The final readable answer is that file.

The four ordinary outcome quality metrics can be `null` when not evaluated.
`cost` must be numeric, in the recorded budget unit, and within its limit. These
values remain worker assertions. They do not become measured quality or measured
spending merely because the wrapper stored them.

The required learning diagnosis, compact cards and optional single bounded repair
hook are specified in [compact-memory-contract.md](compact-memory-contract.md).
Missing learning fields produce `step_missing` and a concrete repair request;
they never silently count as completed learning. A search plan and recorded
four-language improvement research have separate status fields.

## What the wrapper enforces

1. The state exists and its owner matches the controller configuration.
2. A real begin transaction occurs before worker launch.
3. The worker receives the exact returned policy, prior experience and receipt.
4. The worker has a fixed execution timeout and runs as the controller's configured
   argument array; its returned text cannot change the command or deadline.
5. Malformed JSON, an unsuccessful worker exit, a timeout, a different run/hash or
   an invalid finish record prevents accepted host completion.
6. Strict mode requires a matching delivery manifest, actual artifact hashes,
   recorded preflight, four-language search, claim support and writing/review
   records. Missing evidence produces a concrete repair request before finish.
7. Accepted completion is emitted only after finish has committed to the durable
   state. The next invocation therefore loads the recorded experience through a
   new begin transaction.

The wrapper writes `worker-input.json`, `worker-stdout.json`,
`worker-stderr.log` and `host-receipt.json`. The host receipt records the policy
and begin hashes, configuration hash, loaded lesson IDs, deadline, worker PID,
finish event hash when successful, elapsed time and completion status. The
configured worker's stdout remains the lifecycle result; in strict mode the
manifest identifies the readable answer and its checked hash.

`delivery_answer_sha256` is the actual readable file's SHA-256. The older
`answer_sha256` field hashes the runtime's structured `answers` record; the two
hashes describe different objects and must not be substituted for each other.

Exit 0 means `accepted_host_completion: true`. Exit 1 means host completion was
not accepted. This flag verifies the lifecycle contract, not the answer's factual
quality, a model's internal reasoning or general search improvement. The result
always includes `improvement_proven: false`.

## Timeout, interruption and containment

On POSIX the wrapper starts its own process session/group. It sends termination
and, when needed, kill signals to that owned group; it also cleans up remaining
group members after the worker exits. A process that deliberately escapes that
group requires stronger external supervision. This is not an operating-system
sandbox or proof that every possible descendant is contained.

On Windows the portable wrapper can terminate its direct worker process. It does
not claim full process-tree containment. For the Reinis deployment, run it under
the existing externally supervised Windows `jobctl`/Job Object path and preserve
that supervisor's job ID and stop route. Do not stop unrelated processes.

The deadline bounds the configured worker execution. Exact token, network,
energy, memory, disk and service-cost caps require the actual worker or external
supervisor to enforce them. Stdout is checked against the lifecycle's artifact
size limit when read; stderr is a retained process log, not an independently
metered resource budget.

If the wrapper or machine is interrupted, the persistent run can remain
`started`, with no accepted finish. Inspect the host receipt and lifecycle status
before retrying. If finish committed but final receipt writing failed, the wrapper
returns failure conservatively; the existing finished run and event hash are the
evidence. Do not rerun a side effect based solely on the missing final receipt.

The worker must not have permission to modify protected state, evaluator files or
the controller in a deployment that claims enforcement against self-modification.
The wrapper uses the same operating-system identity by default and does not create
that separation. Connect the real host's process and filesystem boundaries; state
the actual boundary when demonstrating the prototype.

## Meaningful verification

A synthetic integration test should launch two distinct worker processes, finish
the first with a real fixture artifact, and check that the second receives and
accounts for the first run's lesson. Separate negative cases must reject a wrong
begin hash and terminate a timed-out owned worker without marking its run finished.
Those tests prove lifecycle enforcement and persistence with the fixture worker.
They do not prove a functioning model connection or better research quality.

Then run a real task through the configured existing worker, inspect the acting
model's context receipt, source evidence and readable answer, and verify a fresh
invocation receives the recorded learning. Report the actual model and host used.
