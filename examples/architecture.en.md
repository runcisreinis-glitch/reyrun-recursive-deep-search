# Third example: an agent that also improves how it learns

Checked on November 9, 2026. This is the result of actual research and a testable architecture proposal; the external projects in this example have not been installed or measured.

## Question

"How can we build a local AI agent that leaves model weights unchanged, keeps a small experience library, and improves both its actions and the method it uses to choose what to learn from experience?"

## Answer

**I would start with an existing memory-and-skills foundation and test one addition: whether a particular memory actually improves the next decision.** Saving advice in memory does not establish that the model understood it or applied it in the right situation.

This is a promising direction, but it would be unjustified to say that nobody has implemented it. MemEvolve already studies development of both the agent's experience and the memory architecture itself. EvolveLab divides that into four changeable operations: transforming, storing, retrieving and managing experience. It provides a concrete research basis for the proposal. [Study](https://proceedings.mlr.press/v306/zhang26fa.html)

### What can already be used

| Foundation | Why it is relevant | What to check before choosing |
|---|---|---|
| **ReMe** | File-based, selectable memory; the documentation also describes Hermes integration. Initial text search does not necessarily require a separate embedding model. | The specific Hermes version, automation-model costs and whether the chosen configuration can meet our memory limit. |
| **Memento-Skills** | An existing project whose workflow selects and executes skills, assesses failures and rewrites skills while leaving the base model unchanged. | How well that cycle works with our model and tasks; the project's demonstrations cannot answer that for us. |
| **MemEvolve / EvolveLab** | The most direct foundation for experiments that also change how experience is selected and managed. | Integration of research code, the specific module and its dependencies; it is not an everyday agent tested here. |

[ReMe primary source](https://reme.agentscope.io/zh/overview) · [Memento-Skills authors' description](https://www.memento.run/research/skills/) · [MemEvolve code](https://github.com/bingreeky/MemEvolve)

These repositories specify the Apache-2.0 licence; when adopting individual files, rights for dependencies, models and data must be checked separately. This evaluation read documentation and repository descriptions; it did not reproduce their results.

### An addition worth testing

My proposal is **a library of short experience cards with applicability conditions and a tested selection procedure**. It is not a claim to the world's first architecture. The testable objective would be fewer repeated mistakes within a limited storage and search budget.

A card would contain the situation, action, outcome, evidence location and a condition under which the advice does not apply. For example: "If a search snippet and a project file disagree, check the specific current file. Documentation alone does not establish that the function works on your computer."

Before work, the agent would receive only relevant cards. Afterwards, it would save one material lesson or a supported conclusion that no new lesson was obtained. A separate test would compare three variants: no cards, the current selection procedure and the new selection procedure. That can distinguish the library's benefit from the model's existing ability to answer the question.

The need for such a test is reinforced by "Large Language Model Agents Are Not Always Faithful Self-Evolvers": its authors observed that models sometimes ignore or misinterpret compressed experience. This does not establish that short memory is useless; it requires checking whether the compressed version retains what the decision needs. [Study](https://arxiv.org/abs/2601.22436)

Practical experience also supplies a specific lead: after 24 generations of context compression, amtr's author describes a problem where a working hypothesis turns into an apparently confirmed conclusion. The author's adjustment is to preserve both what has been checked and what remains untested. This is the author's own observation, not proof of general effectiveness. [Author's experience and code link](https://zenn.dev/naoto256/articles/amtr-working-memory)

### When a combined solution would be preferable to an existing one

I would first compare with a ReMe or Memento-Skills configuration using the same model, tools, memory budget and adaptation effort. If a small configuration change to an existing project meets the requirement, I would choose that.

I propose an initial test on 24 previously unused tasks, including inapplicable and outdated lessons. Before seeing results, we would set a target such as at least 20% fewer repeated mistakes, no new critical error and no increase in search actions. A separate reader would check whether the recommendation, rationale and next action are understandable. **20% is a proposed decision threshold, not an achieved result.** The small test would help decide whether to continue; it would not establish universal superiority.

Planning estimate: 12–24 working hours for a small connector, 16–32 hours to prepare tasks and evaluation, and 12–24 hours for fixes and a repeatable demonstration. That totals 40–80 hours, roughly 1–2 weeks for one developer with a working environment. Three variants times 24 tasks means 72 agent-task executions, not 72 individual model requests. The actual number and duration of model calls must first be measured in a small trial.

Electricity would be calculated as the measured average power of the entire computer in kW multiplied by active hours. Cost would use the actual tariff or service consumed. These quantities have not been measured here. I would initially reserve 2–4 hours a week for routine maintenance until the frequency of dependency issues and failures becomes clear.

**Decision: there is a basis for a bounded comparative experiment. There is not yet a basis for promising that our combined solution will outperform existing ones or that it already runs autonomously.**
