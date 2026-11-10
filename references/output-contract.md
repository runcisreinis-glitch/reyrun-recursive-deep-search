# Two-track result contract

## Default answer

Adapt the form to the task. Everyday questions need a useful answer, practical alternatives and only material clarifications; conceptual questions need explanations and credible learning routes. The full two-track software comparison below applies when the task is to choose or build a technical solution. Never manufacture a synthesis project for a simple product or appearance question. A confusing question is a reason to interpret carefully, not to ridicule the user.

Lead with a concrete recommendation and the reason it fits the user's constraints. Then show the following two sections. Keep query counts, dictionaries and search routes in the background unless they explain a material gap or the user asks for them. Cite the evidence supporting each technical conclusion.

### A. Strongest ready options

Usually compare 2–5 meaningful alternatives. Fewer is acceptable when the evidence supports fewer; never manufacture a list.

| Field | Required content |
|---|---|
| Candidate | Canonical project link; current release or revision when verified. |
| Fit | Which original requirements it meets and fails. |
| Advantages | Concrete functions or measured results, with scope. |
| Drawbacks | Missing capabilities, known defects, resource demand and maintenance. |
| Rights | Code, model and data licenses separately; unknown stays unknown. |
| Resources | Hardware, dependencies, setup work and running cost; distinguish measured from estimated. |
| Validation | Documentation read, code inspected, installed, executed or independently reproduced. |
| Recommendation | Best fit for a stated use, not a universal winner. |

An installable upstream package that has not been run here must be labelled “upstream installation documented; not executed in this evaluation.” Do not call it locally verified.

### B. Unfinished work and synthesis

For each serious proposal, name:

- the best ready baseline, including the adapter it would itself need;
- a material requirement the baseline cannot satisfy or a credible cost/quality disadvantage;
- exact reusable file, function, artifact or algorithm from each component;
- the component's verified behavior, license and remaining uncertainty;
- the shared mechanism and the input/output adaptations;
- missing code, dependencies, training/data needs and integration work;
- the agent's evidence of capability, or the still-unproven part;
- the smallest executable slice and its rejection condition.

A project name plus a TODO list is not a synthesis plan. A copied interface does not establish the underlying algorithm. An attractive demonstration does not establish arbitrary-domain generalization.

## Synthesis decision

Use two separate decisions:

1. **Worth a cheap experiment:** the mechanism, baseline gap and cost assumptions are specific enough to justify a bounded test.
2. **Worth building:** the small test supports a material advantage over the ready baseline and integration remains feasible.

Do not imply that passing the first decision proves the second. Unknown rights or unavailable essential assets block a reuse recommendation until resolved; they do not prevent describing the research idea.

Before the test, define quality, critical constraints, comparison tasks, resource limits and the minimum useful gain. Hold other conditions constant where possible. Keep a baseline that uses the same tools and allowed adaptation effort. If the ready solution gains the same capability with a trivial adapter, the proposed custom system may have no advantage.

Accept a proposal when it meets an important unmet requirement, improves quality at justified total cost, or reduces total cost at acceptable quality. Weights belong to the user's objective. Do not invent a universal utility score or probability of success. State uncertainty directly and preserve the strongest contrary finding.

## Time, energy and cost

Separate engineering effort from elapsed time. Estimate work packages rather than asserting “I can do it in two weeks.”

| Quantity | Estimate format |
|---|---|
| Engineering | Range by adapter, data work, tests, deployment and maintenance. |
| Elapsed time | Range with staffing, access and dependencies stated. |
| Compute | CPU/GPU hours, model calls or tokens, hardware and batch assumptions. |
| Energy | Measured or assumed average whole-system kW × active hours; identify omitted cooling/overhead. |
| Money | Current quoted service price × usage, plus measured electricity tariff where available. |
| Maintenance | Expected update, regression and support work; uncertainty. |

Do not infer electricity use from GPU count or nameplate power alone. When hardware, power or price is unknown, give the formula and missing parameter rather than a fabricated number. The planning estimate is not a completed measurement or a promise.

## Minimal candidate record

Keep a durable record with fields: candidate_id, goal, ready_baseline, component_sources, revision, required_files, license_status, evidence_state, proposed_advantage, inference, integration_gap, effort_range, compute_range, energy_assumptions, cost_assumptions, capability_evidence, smallest_test, success_threshold, stop_condition, decision, checked_at.

A rejected proposal still needs its rejection reason. Reuse that result in the next search instead of rediscovering the same dead end.

## Customer-facing example structure

1. Recommendation and date.
2. Ready options table with strengths and drawbacks.
3. Synthesis shortlist, or “No synthesis currently justifies building.”
4. What a small experiment would settle and its bounded cost.
5. Material access, license or execution gaps.
6. Sources near the claims.

Do not expose internal agent transcripts, secret credentials or unrelated personal context. This is a concise output rule, not permission to conceal a material failure or uncertainty.
