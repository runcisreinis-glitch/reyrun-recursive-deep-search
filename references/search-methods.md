# Search methods

Search EN/DE/ZH/JA automatically unless the user's instructions change coverage. Choose a bounded profile before research: an everyday or narrow question can start with 1–3 useful queries per language. The optional extensive profile selects at least 30 substantively different queries per language only when its breadth is justified by the task and budget. This is a chosen coverage budget, not a universal quality threshold. Reuse logs for narrow continuations; investigate missing evidence. Four translations do not establish independent search paths.

## Method catalogue

Keep these IDs stable for logs and the coverage helper. A = usual starting method; B = expansion; C = situational. These priorities are working defaults, not an empirically measured ranking.

| ID | Method | Priority | Action and acceptance check |
|---|---|---|---|
| M01 | Function before label | A | Specify inputs, outputs, failure and missing mechanism; test the required function. |
| M02 | Local concept families | A | Use the [typed term map](term-map.md); preserve meaning, source and relation type. |
| M03 | Purpose–mechanism matrix | A | Compare purpose, mechanism, inputs and outputs separately; topical similarity is insufficient. |
| M04 | Provenance chain | A | Follow experience → author → artifact → exact module → test. |
| M05 | Citation chaining | A | Follow citations from independent seeds; inspect their reasons. |
| M06 | Adaptive reformulation | A | Reformulate from new terms/failures while retaining the original contract. |
| M07 | Cross-domain mechanism | B | Search an adjacent field without the usual industry keyword; identify required adaptations. |
| M08 | A–B–C bridge | B | Connect need A, shared mechanism B and implementation C; test both links. |
| M09 | Failure and counterexample | A | Search exact errors, non-convergence, regressions and failed reproductions; match versions and environments. |
| M10 | Forks and history | B | Inspect patches, commits and pull/merge requests; distinguish proposed, merged and tested changes. |
| M11 | Executable evidence | A | Inspect files, tests, configuration, dependencies, license and example before judging readiness. |
| M12 | Contrary hypothesis | A | Seek leakage, selection effects and weakened evaluation; specify a rejection condition. |
| M13 | Historical names and authors | B | Search earlier terminology, author pages, predecessor code and later continuations. |
| M14 | Controlled relaxation | C | Relax one constraint temporarily; restore it and label nonconforming alternatives. |
| M15 | Symbol or fragment | C | Search a function, schema, filename or error line when project labels fail. |
| M16 | First-person experience | A | Record firsthand author, environment, comparison and outcome; distinguish promotion. |
| M17 | Independent channels | B | Compare scholarly, code and practitioner channels; deduplicate origins. |
| M18 | Marginal information | A | Continue branches resolving evidence gaps; stop unproductive repetition. |
| M19 | Language-independent classification | C | Use classifications such as IPC; patent disclosure does not establish code availability. |

## Routes beyond the four familiar platforms

Expand beyond GitHub, Hugging Face, ModelScope and Gitee according to missing evidence.

Use native search and documented public APIs. Check operators, authentication, pagination and limits; website access does not imply API access. Log actual access outcomes.

- **Author artifacts:** paper DOI/title, author identifiers and laboratory → project page → supplements, downloads, academic wiki attachments or institutional forge. Inspect files and licenses; a download link does not prove execution.
- **Zenodo:** use [record search](https://developers.zenodo.org/) and [software/related-identifier fields](https://help.zenodo.org/guides/search/). Follow a paper DOI through supplement, derivation and version relations; inspect the deposited version and file license.
- **Software Heritage:** follow original repository URLs, documented metadata search or SWHIDs into archived revisions and files. The [author walkthrough](https://annex.softwareheritage.org/public/guidelines/archive-research-software.pdf) demonstrates recovering a discontinued origin. Do not promise universal full-code search. Some [provenance endpoints](https://docs.softwareheritage.org/devel/swh-web/uri-scheme-api-provenance.html) require special permission; verify access before depending on them.
- **Institutional archives:** use [HAL fields and collections](https://api.archives-ouvertes.fr/docs/search), university repositories, NII author tools and ScienceDB records. [BASE OAI](https://oai.base-search.net/) requires approved IP access. An index entry is a discovery lead; read its linked artifact.
- **Other forges and histories:** inspect university GitLab, Codeberg and project-owned servers. Follow issue → patch → commit → merge request → fork differences. GitLab documents [fork listing](https://docs.gitlab.com/api/project_forks/) and [commit-to-request provenance](https://docs.gitlab.com/api/commits/). Mirrors are not independent implementations.
- **Historical and failure mechanisms:** combine older author terminology, [IPC versions/concordances](https://www.dpma.de/patente/recherche/), exact failures and adjacent-field mechanisms. Practitioner discussions supply leads; verify technical claims against primary sources and code.

[GitHub syntax](https://docs.github.com/en/search-github/searching-on-github/searching-in-forks) differs: repository search uses `fork:true`/`fork:only`; code search uses `is:fork`. Check other services separately.

## Testable combinations

Innovation means a useful mechanism transfer or combination with a compatibility gap and falsification test; global novelty is not implied.

1. **Bibliography + code identity:** join related DOIs, archived revisions and file hashes to locate a missing component. Reject the hypothesis if recovered files contain only the known implementation.
2. **Function contract + analogy + negative control:** use purpose/mechanism separation, typed terminology and deliberately misleading topical matches. Reject expansion that increases mentions without retrieving usable mechanisms.

Compare synthesis against the best suitable ready-made free solution found. Include adaptation, verification, maintenance and license compatibility. Predeclare the required benefit and budget; untested advantage remains a hypothesis.

## Logging and stopping

Record exact query, language, method ID, branch/parent, date, execution status, URLs, access failures and gains. Keep queries, tool calls, unique sources, opened sources and executed tests separate. Preserve project/module/data licenses individually.

Stop at sufficient coverage/evidence, or document the unresolved blocker. Structural compliance and completed searches do not establish measured superiority. Present selected results; retain the audit trail. Methodological sources: [sources.md](sources.md).
