# Improving an agent's Markdown skill without training model weights

Research record: 9 November 2026, Europe/Riga. Selected documentation rechecked on 8 November 2026 UTC.

## Recommendation

Start with SkillOpt when the change should remain inside one skill document. Consider GEPA when an existing evaluator needs a configurable candidate search. Choose EvoSkill when the scope includes several skills or supporting files. ACE belongs in the comparison when the problem is retaining useful experience in the agent's working context.

These recommendations reflect the task and the sources inspected. None of the external projects below was installed or executed in our environment. A specific release and its dependencies must be pinned before an execution comparison.

## Task and evidence

The goal is to improve a repeatable procedure expressed in Markdown while keeping model weights unchanged. An acceptable pilot must compare the existing and revised skill on new tasks, preserve constraints, record cost and support rollback.

The underlying research completed 120 distinct queries: 30 each in EN, DE, ZH and JA. It covered mechanisms, code, failure reports and unfinished components. This example selects one question from that completed research; it does not claim a new 120-query run. The query log and source ledger preserve the evidence trail. Four selected project sources were rechecked for this release.

The internal records referenced here are omitted from this edition; see [publication scope](../PUBLICATION_SCOPE.md).

The language branches had different uses. Japanese practitioner material led to SkillOpt and a warning about transfer between models. Chinese and Japanese program-synthesis terms exposed library-learning mechanisms. German searches developed terminology and reproducibility checks. These observations describe discovery paths; they do not establish superiority of a language or method.

## Group 1: ready options to evaluate

“Ready” here means a published implementation with a documented use path. Deployment in our environment remains unverified.

| Option | Useful mechanism and advantage | Drawback or remaining work | Licence evidence |
|---|---|---|---|
| [SkillOpt](https://github.com/microsoft/SkillOpt) | Edits a skill document from scored task trajectories while leaving the target model unchanged. Its limited edits to text fit this task closely. | Needs representative tasks, an appropriate scorer and a working model backend. Improvements reported by its authors do not establish transfer to our workload. | Repository declares MIT; dependency and module review remains. |
| [GEPA](https://gepa-ai.github.io/gepa/guides/agent-skill/) | Searches candidate text using feedback. Its official skill includes evaluator guidance and a starting template, useful when a scoring function already exists. | A weak evaluator can reward an unsuitable procedure. Compatibility with our runner, the operating budget and deployment still need testing. | MIT; full repository licence text verified. Selected-module and dependency audit remains. |
| [EvoSkill](https://github.com/sentient-agi/EvoSkill) | Develops reusable skills and prompts against a benchmark. Its broader scope suits changes involving multiple files. | Its broader scope can mean more integration work than a narrow text-edit pilot. Its documentation lists continuous evolution and evolution without a benchmark as ongoing work. | Repository declares Apache-2.0; dependency and module review remains. |
| [ACE](https://github.com/ace-agent/ace) | Updates an agent's working context from experience. Useful if the observed failure is losing or poorly organising procedural knowledge. | Context maintenance is a different intervention from selecting a deployable Markdown skill. It needs a separate comparison against the existing memory. | Carried forward from the original research; the selected version and licence were not rechecked here. |

SkillOpt is the first pilot candidate because its change boundary matches the requested artifact. GEPA is a reasonable alternative when scoring and execution already exist. This evidence supports no universal ranking by quality, speed or cost.

## Group 2: unfinished projects and synthesis

### AutoSkill/SkillEvo: inspect before adopting

The [SkillEvo README](https://github.com/ECNU-ICALK/AutoSkill/blob/main/SkillEvo/README.md) describes replay pools, mutations and a local champion registry. It explicitly lists automatic write-back to the main SkillBank, retrieval-only evaluations and scheduling across many lineages as unfinished. The relevant documented entry point is `SkillEvo.cli`; its implementation was not executed here.

A possible benefit is reusing existing AutoSkill replay data. That benefit has not been demonstrated against the ready alternatives, and the required licence remains unresolved. Reject it as a deployment recommendation at this stage.

A cheap investigation would examine the licence and one replay record, then map the missing promotion/write-back contract without modifying an active skill store. Allow 0.5 to 2 hours of review, zero to four model calls and zero to 50,000 tokens. Under the illustrative price assumption below, additional model cost is $0 to $0.50. Stop if reuse rights or the data contract cannot be established.

### Existing runtime plus GEPA: test the need for an adapter

The documented component is GEPA's `.claude/skills/gepa-optimize-anything/`, including `templates/optimize_prompt.py`. The proposed connection would feed our existing task runner into a feedback evaluator, retain immutable test cases and accept or roll back a revised skill.

Missing work includes trace conversion, an evaluator, accepted-version storage and verification that the next task loads that version. A possible advantage is avoiding a change of execution environment. SkillOpt already documents integration paths, so that advantage cannot be assumed. A full custom build is unjustified until a small mapping test shows an unmet requirement.

Budget 1 to 3 hours for that mapping test, zero to eight model calls and zero to 100,000 tokens, or $0 to $1 under the same price assumption. Do not estimate a production build until the runtime interfaces and selected modules' licences have been checked.

## A bounded pilot and its estimated cost

These are planning assumptions, not measured results or provider prices. Assume one experienced implementer, existing model access and short text tasks. Prepare 12 fresh evaluation tasks, compare two skill versions and repeat each twice: 48 target runs, plus an estimated 4 to 12 proposal or review calls. Separate development tasks from those 12 evaluation tasks.

Allow 4 to 12 hours for setup and review and 0.5 to 3 hours of execution. A provisional budget is 0.1 to 1 million total tokens. At an assumed blended price of $1 to $10 per million tokens, model charges would be $0.10 to $10, excluding labour and hosting. This is an arithmetic scenario; replace it with the chosen provider's rates. There is no model-weight training in this pilot. Local inference hardware requirements depend on the chosen model and have not been measured. Energy use would be calculated as `energy (kWh) = average power (kW) × active time (h)`. Average power has not been measured, so no kWh estimate is given. These pilot estimates do not establish a production engineering schedule.

Freeze the task definition, scoring rules and budget before generating a candidate. Reject a critical regression even if the average score improves. Preserve both versions, inspect failed cases and verify the accepted version loads in a later task. A favourable pilot would support that specific configuration; this report contains no such execution result.

## Brief conclusions

For a first small test, choose SkillOpt when one Markdown skill needs to change. GEPA is useful for connecting an existing evaluator to candidate search, EvoSkill for broader changes, and ACE for accumulating working context. No external project has been run in our environment. SkillEvo and a custom GEPA integration remain research candidates. Their development is not justified until an advantage has been demonstrated and licences clarified. The stated time and cost ranges are planning assumptions.
