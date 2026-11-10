# Typed multilingual term map

Use this map to expand search without silently changing the task. EN, DE, ZH and JA are automatic starting languages; do not ask the user to choose them. The user's current instructions take precedence.

## Record structure

Keep one record per term, sense and relation, linked to the exact query log:

| Field | Required content |
|---|---|
| `term_id`, `term`, `language` | Stable local identifier, original spelling and language. |
| `sense` | The intended technical meaning, including exclusions. |
| `relation_type`, `related_to` | A typed relation and its source concept/term ID. |
| `source_url`, `source_version`, `checked_at` | Dictionary entry/synset or exact author passage; version and observation date. |
| `query_branch`, `parent_query_id` | The branch this term creates and the actual preceding query, if any. |
| `function_contract` | Required input, operation, output, constraints and acceptance check. |
| `back_translation`, `contract_check` | Restated meaning and reason it preserves or changes the contract. |
| `status`, `decision_reason` | Candidate, accepted, rejected or unresolved; include why. |

A proposed term without an observed source stays a candidate. Do not fabricate a synset, quotation, executed query or successful check.

## Relation types

| Type | Meaning and treatment |
|---|---|
| `synonym` | Same selected sense; substitution must preserve the relevant statement. |
| `broader` / `narrower` | Generalization/specialization; record which requirement is relaxed or added. |
| `association` | Related topic, co-occurrence or similar context; never automatically synonymous. |
| `historical_name` | Earlier terminology supported by a dated source; check changed meaning. |
| `conceptual_translation` | A local expression for the intended concept; verify technical usage. |
| `functional_analogy` | Different domain sharing a mechanism; record input/output differences and transfer test. |
| `spelling_variant` | Orthography, abbreviation or script variant; does not establish semantic equivalence. |

WordNet relations between synsets, corpus co-occurrence and edit-distance suggestions are not all synonym relations. [OpenThesaurus FAQ](https://www.openthesaurus.de/about/faq) explicitly separates synonyms from broader concepts.

## Cross-language workflow

1. Freeze the function contract in plain language before choosing vocabulary.
2. Find local candidate expressions through dictionaries, author papers, documentation and code. Include original English technical terms where local authors use them.
3. Translate the concept, not merely the sentence. Preserve local terminology and its source; do not force four languages into identical phrases.
4. Back-translate the selected meaning into the working language, then compare inputs, operations, outputs, exclusions and acceptance conditions with the contract. Back-translation is a consistency check, not proof of equivalence.
5. Confirm usage in a relevant local primary source. If meaning broadened, label the branch accordingly; reject a drifted branch or retain it as an explicitly different alternative.
6. Run distinct branches for exact terms, verified synonyms, historical names, failures and functional analogies. Reassess every new branch against the original requirement. Record why it added useful evidence.

Illustration: “program synthesis,” DE “Programmsynthese,” ZH “程序综合/程序合成,” and JA “プログラム合成” are candidate concept expressions. They are not evidence that every returned project satisfies a particular input/output contract. “Procedural memory” and “skill evolution” require separate relation records; neither is automatically a synonym of the other.

## Sources and conditions

Checked 2026-11-08 UTC. Recheck the specific release, license and API before integration. These are term discovery resources, not a measured ranking or a promise of coverage for recent AI terminology.

| Resource | Access, license and correct use |
|---|---|
| [Princeton WordNet](https://wordnet.princeton.edu/) — EN | Synsets and typed semantic relations; no longer developed. Its [license](https://wordnet.princeton.edu/license-and-commercial-use) permits use/modification/distribution without fees while preserving notices. Use the selected sense, not every related word. |
| [Open English Wordnet](https://en-word.net/) — EN | CC BY 4.0; [2025 downloads](https://en-word.net/downloads) are available, dated 2025-12-31. Preserve attribution and relevant upstream notices. API documentation was linked but not readable in this audit; do not claim an API execution. |
| [OpenThesaurus](https://www.openthesaurus.de/about/download) — DE | Data: choose CC BY-SA 4.0 or LGPL. [API](https://www.openthesaurus.de/about/api): free, attribution link, contact in `User-Agent`, errors above 60 requests/minute/IP; downloads for bulk work, advance contact requested for sustained API use. `similar=true` means spelling similarity. Website software and data have separate licenses. |
| [Japanese WordNet](https://bond-lab.github.io/wnja/jpn/downloads.html) — JA | Version 2.1, 2026-10-24; download without application. [License](https://bond-lab.github.io/wnja/license.txt) permits use/modification/distribution without fees with notices retained; follow published attribution instructions. Human-checked synonym pairs are a separate resource derived from version 1.1. |
| [OMW](https://omwn.org/) / Chinese Open WordNet — ZH | OMW links wordnets; inspect each component's license. [COW license](https://github.com/omwn/omw-data/blob/main/wns/cow/LICENSE) allows use/modification/distribution without fees with notices retained. Do not assign one software license to every aggregated dictionary. |
| [J-GLOBAL/JST](https://jglobal.jst.go.jp/help/search/keyword) — JA | Native search offers synonym selection combined with OR. Use it to discover technical expressions. Bulk redistribution permission and an unrestricted thesaurus API were not established. |

[Leipzig corpus associations](https://wortschatz.uni-leipzig.de/de/documentation/faq) are additional leads; direct access and licensing were unresolved in this audit. HIT's 同义词词林（扩展版） likewise requires a dataset-specific redistribution license before packaging. Do not bundle dictionary datasets merely because their pages are public.

For each accepted term, preserve its source in the query ledger. More synonyms, languages or hits are costs and coverage signals; measure usefulness through distinct, verified findings that satisfy the original task.
