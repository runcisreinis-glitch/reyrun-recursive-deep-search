# Sources and verification scope

Checked during 2026-11-08 UTC / 2026-11-09 Europe/Riga. This is a provenance index, not evidence that every linked program was executed. External candidate frameworks were not installed or benchmarked. Recheck the current version, needed module and applicable rights before implementation.

## Search methods

- [Bates, 1989: evolving queries and berrypicking](https://pages.gseis.ucla.edu/faculty/bates/berrypicking.html).
- [Wohlin, 2014: backward and forward snowballing](https://www.wohlin.eu/ease14.pdf).
- [SOLVENT, 2018: separate purpose, mechanism and results](https://josephcc.com/static/papers/53236685/paper.pdf).
- [ReformIR, 2026: query reformulation, drift and evaluation budgets](https://arxiv.org/abs/2605.00560).
- [ULB Münster LOTSE: concept and term matrix](https://www.ulb.uni-muenster.de/lotse/literatursuche/suchstrategien/thematisch_suchen/analysieren.html).
- [GitHub: searching forks](https://docs.github.com/en/search-github/searching-on-github/searching-in-forks).
- [DPMA: patent research and classification](https://www.dpma.de/patente/recherche/).

These sources support individual methods. They do not establish that this combined skill outperforms every alternative.

## Lexical resources

- [Open English Wordnet](https://en-word.net/) and [downloads](https://en-word.net/downloads): release and data terms.
- [Princeton WordNet](https://wordnet.princeton.edu/) and [license](https://wordnet.princeton.edu/license-and-commercial-use): senses and semantic relations; no longer actively developed.
- [OpenThesaurus data](https://www.openthesaurus.de/about/download), [API](https://www.openthesaurus.de/about/api) and [FAQ](https://www.openthesaurus.de/about/faq): separate synonyms, associations and spelling similarity.
- [Japanese WordNet downloads](https://bond-lab.github.io/wnja/jpn/downloads.html) and [license](https://bond-lab.github.io/wnja/license.txt): v2.1 was listed as 2026-10-24.
- [Open Multilingual Wordnet](https://omwn.org/) and [Chinese Open WordNet license](https://github.com/omwn/omw-data/blob/main/wns/cow/LICENSE): check component terms separately.
- [J-GLOBAL keyword help](https://jglobal.jst.go.jp/help/search/keyword): scientific term discovery and synonym expansion.

No dictionary database is bundled or automatically downloaded by this skill. See term-map.md for the required retrieval and meaning checks.

## Code beyond the common platforms

- [Zenodo API](https://developers.zenodo.org/) and [search guide](https://help.zenodo.org/guides/search/): software records and related identifiers.
- [Software Heritage author guidance](https://annex.softwareheritage.org/public/guidelines/archive-research-software.pdf): source preservation and archive identifiers.
- [Software Heritage provenance API](https://docs.softwareheritage.org/devel/swh-web/uri-scheme-api-provenance.html): permission requirement seen in indexed primary documentation; direct page access failed in this investigation. No API execution is claimed.
- [HAL search documentation](https://api.archives-ouvertes.fr/docs/search): institutional metadata search.
- [BASE OAI](https://oai.base-search.net/): access requires an application; not an anonymous universal API.
- [GitLab forks API](https://docs.gitlab.com/api/project_forks/) and [commits API](https://docs.gitlab.com/api/commits/): inspect changes and originating merge requests.
- [NII NTCIREVAL](https://research.nii.ac.jp/ntcir/tools/ntcireval-ja.html): author-hosted retrieval-evaluation artifact. Archive not unpacked, license not established and code not run here.
- [Codeberg introduction](https://docs.codeberg.org/getting-started/what-is-codeberg/): independent forge; no specific AI module was validated there in this release.

## Skill and optimization foundations

- [Agent Skills specification](https://agentskills.io/specification).
- [Hermes skills](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/skills.md) and [memory/review](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/memory.md).
- [SkillOpt](https://github.com/microsoft/SkillOpt): bounded instruction optimization; repository identifies MIT.
- [EvoSkill](https://github.com/sentient-agi/EvoSkill): skill evolution; repository identifies Apache-2.0.
- [GEPA](https://github.com/gepa-ai/gepa) and its [Agent Skill guide](https://gepa-ai.github.io/gepa/guides/agent-skill/).
- [ACE](https://github.com/ace-agent/ace): context adaptation.
- [Stitch artifact](https://github.com/mlb2251/stitch-artifact): library learning; transfer to visual recipes is a hypothesis.
- [AutoSkill/SkillEvo](https://github.com/ECNU-ICALK/AutoSkill/blob/main/SkillEvo/README.md): documented incomplete connections; license was not established in this investigation.
- [Valmont-F](https://github.com/fogbeam/Valmont-F): incomplete literature-discovery work; check original-code and data terms separately.

## Experience, contrary evidence and evaluation

- [SCIEN's SkillOpt trial, 2026-11-06](https://zenn.dev/scien/articles/5cfad6388c0f01): a limited first-hand report, not user consensus.
- [OpenEvolve MLX/Metal experiment analysis](https://github.com/algorithmicsuperintelligence/openevolve/blob/main/examples/mlx_metal_kernel_opt/EVOLUTION_ANALYSIS.md): one experiment's progress and remaining baseline gap, not a verdict on the entire framework.
- [DGM PR 12](https://github.com/jennyzzt/dgm/pull/12): proposed import fix; not executed here.
- [OpenSkill](https://github.com/OpenLAIR/OpenSkill): inspect files even when a README's code-release statement is stale.
- [SkillsBench v4](https://arxiv.org/abs/2602.12670v4), [DGM v2](https://arxiv.org/html/2505.22954v2) and [GEPA v2](https://arxiv.org/abs/2507.19457v2): research context; their reported results do not benchmark this skill.

The public example and its source ledger preserve the narrower claims used for a concrete decision.
