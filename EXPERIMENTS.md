# REYRUN Recursive Deep Search: research and experiment report

Complete research answers, with authored findings and disclosed limits. Documentation edition: November 10, 2026. Software version: 2.0.0-beta.3.

This report contains every answer in the final 30-case selection and the historical 30-case collection, plus all six strategy-comparison research answers. The final selection keeps 12 earlier cases and adds 18; the two collections therefore cover 48 distinct main tasks. The comparison tasks are counted separately.

The internal evaluator audits, instruction snapshots, execution demonstrations, memory snapshots, raw logs, query dumps and internal receipts are excluded from this edition. The relevant reported findings are stated in an authored account. See [Publication scope](PUBLICATION_SCOPE.md) and the [exclusion manifest](exclusion-manifest.json).

[GitHub repository](https://github.com/runcisreinis-glitch/reyrun-recursive-deep-search) · [Download the repository ZIP](https://github.com/runcisreinis-glitch/reyrun-recursive-deep-search/archive/refs/heads/main.zip) · [Source code](scripts/recursive_search.py) · [Support the author](SUPPORT.md) · [More about Reinis on Facebook](https://www.facebook.com/reinis.runcis).

## What the results establish

The selected cases report 156 queries. Seven new mathematics cases include complete proofs or derivations and executed calculations. All 18 new main tasks completed a recorded learning cycle, with 15 later tasks loading earlier lessons; the chat orchestrated that work. In the separate three-task comparison, both methods met the fixed answer checks. The candidate used 43 web actions against 47 but achieved no measured accuracy gain and was not adopted.

The current four executable scripts, their tests and all calculation programs are included. The recorded release passed 82 software tests. The reported static source review found no direct HTTP/socket operations, payment execution, hidden downloader or `eval`/`exec` in those four scripts. Its internal receipt is excluded. `search_host.py` deliberately runs the external command configured by the user; that command has the access granted by its environment. Memory compaction can remove old evidence under an approved plan. The included code and protocols describe those operations. No antivirus certification or independent penetration test is claimed.

## Continuing the learning cycle

A connected [host wrapper](references/host-contract.md) runs the beginning and completion steps, passes saved lessons to the worker and rejects incomplete learning records. Persistent state and a configured research worker are required. Installing instructions alone does not create a continuously running service. A practical installation check is two real tasks, with evidence that the second loaded experience from the first.

The historical findings are preserved as research records. Translation and publication edits do not add a new experiment. Source URLs remain in the complete answers; the original query dumps and private execution evidence are outside this edition. Current publication hashes are in [file-manifest.json](file-manifest.json).

## Contents

- [Validation and development report](#release-report)
- [Final selection: all 30 answers](#final30)
- [Historical collection: all 30 answers](#historical30)
- [All six strategy-comparison answers](#comparison)
- [Published findings and limits](#findings)
- [Introductory cosmetics example](#cosmetics)
- [Introductory game-technology example](#gaming)
- [Introductory agent-architecture example](#architecture)


<a id="release-report"></a>

## Validation and development report

Release 2.0.0-beta.3 · research conducted on November 9, 2026.

The final validation set contains 10 everyday questions, 10 moderately difficult questions across different fields, and 10 difficult tasks. Each of the seven new advanced tasks includes a complete mathematical proof or derivation and a calculation that was actually run. Two reproduced failures in the learning memory were fixed, and the validated code passed 82 tests. A separate trial of a new search strategy returned **no_gain**: the candidate was not adopted as the new baseline method.

[All 30 answers](validation/2026-11-09-beta3/30-examples.en.md) · Evidence register · Machine-readable summary · [Compact lessons](references/observed-lessons.md).

The internal records referenced here are omitted from this edition; see [publication scope](PUBLICATION_SCOPE.md).

### 1. Why the selection changed

The original 30 research tasks were actually carried out, but an independent audit found that the medium group was too concentrated on IT and that the difficult group lacked completed advanced mathematics tasks. The final selection retains 12 suitable cases and adds 18 new ones. The original answers have not been deleted or rewritten: the [historical edition in English](validation/2026-11-09/30-examples.en.md) remains available. There are 48 distinct main tasks in total; the three comparison tasks are counted separately.

The internal records referenced here are omitted from this edition; see [publication scope](PUBLICATION_SCOPE.md).

The final selection has records of **156 executed queries**. Every case includes EN/DE/ZH/JA searches. A query in a language does not prove that a supporting primary source in that language was found and read. Access errors, unread excerpts, and cases where only a summary was read remain disclosed. This set is not presented as statistical proof that four languages outperform one.

The questions were designed for validation. Where clarification was needed, the supplied conditions are labelled as simulations, not fabricated confirmation from a conversation participant. The everyday cases also test incomplete or mistaken assumptions, beyond neatly phrased expert questions.

| ID | Question tested | Queries |
| --- | --- | ---: |
| E01 | Makeup disappears after an hour | 6 |
| E02 | Choosing trousers for a body shape | 5 |
| E04 | Will any 65 W USB-C charger work? | 6 |
| E05 | What laundry symbols mean | 4 |
| E07 | Freeing phone storage while keeping photographs | 4 |
| E08 | Does 5 GHz mean the internet is five times faster? | 4 |
| NE01 | Two decilitres of flour: volume or mass? | 5 |
| NE02 | Will one bucket of paint cover the room? | 5 |
| NE03 | Where the calories in cooked rice go | 5 |
| NE04 | White, cloudy drinking glasses | 5 |
| P02 | Translating a game while preserving placeholders | 5 |
| P04 | Converting HDR video to SDR | 4 |
| P05 | RAID1 and backups of family photographs | 4 |
| NP01 | A fertilizer trial on a sunny windowsill | 5 |
| NP02 | Curtain fabric and shrinkage | 6 |
| NP03 | Heating and mixing water | 5 |
| NP04 | Carbon, ion exchange, and reverse osmosis | 7 |
| NP05 | Whether to accept an additional order at a lower price | 6 |
| NP06 | A historical address in Riga | 9 |
| NP07 | Birds and window glass | 6 |
| F03 | An agent that tests its own improvements | 6 |
| F08 | A causal test of a memory improvement | 4 |
| F09 | An external payment after a process crash | 4 |
| NF01 | Inverting the heat equation | 5 |
| NF02 | A stochastic process and discrete variance | 5 |
| NF03 | Transient growth of a nonnormal matrix | 5 |
| NF04 | Duality without a finite multiplier | 5 |
| NF05 | Concentration of mass and passage to the limit | 5 |
| NF06 | The Strang scheme and oscillator energy | 6 |
| NF07 | The Galois group of a fifth-degree polynomial | 5 |

### 2. What answer validation covers

Each case retains its answer, sources, claim-to-source links, and the SHA-256 of its original file. New calculations also retain their code and output. The root agent independently read all seven mathematical proofs written by the new author, checked the arguments, and compared them with the stored numerical results. This is not certification by a formal proof assistant. See the mathematics review.

The internal records referenced here are omitted from this edition; see [publication scope](PUBLICATION_SCOPE.md).

One agent carried out the main research for each example, followed by the independent review described here. This set does not demonstrate four independent agents at the question-formulation and search stages of every case. An acceptance audit from four separate perspectives was actually performed for the strategy comparison described below.

The calculations and reasoning in the seven subject-area answers were independently reviewed. An additional agent checked the four new everyday answers and the historical-address/window cases against the stored primary-source excerpts, and repeated their calculations. There is no claim that every external source was reopened on the web in every audit. See the subject-area review and six-answer audit.

The internal records referenced here are omitted from this edition; see [publication scope](PUBLICATION_SCOPE.md).

Mathematical formatting and citation links were adapted for the public edition. Spacing was corrected in NE02; the ambiguous opening of NP04 was clarified to read, in translation, "A cartridge containing only activated carbon..." The original research answers remain unchanged. The export mapping records the checksums of both versions and the reasons for each edit.

The internal records referenced here are omitted from this edition; see [publication scope](PUBLICATION_SCOPE.md).

### 3. Learning between searches

All 18 new main tasks completed an actual begin/end record cycle. Three thematic series started with empty test memory; **15 subsequent tasks loaded previously saved lessons**. Their identifiers and the agent's record of using a lesson or finding it inapplicable are in the lifecycle evidence. For example, distinguishing quantity from unit was carried over from flour to paint and dry/cooked rice. The earlier numerical lessons were marked as inapplicable to the case about the material of drinking glasses.

The internal records referenced here are omitted from this edition; see [publication scope](PUBLICATION_SCOPE.md).

The chat orchestrated these begin/end steps. The strict file/reference validator was also run on the 14 new subject-area and mathematics answers. This does not establish that an automatic background service started those 18 research tasks. The previously saved two-task demonstration through the strict connector documents a separate real connector run and the loading of its lesson by the next task.

The internal records referenced here are omitted from this edition; see [publication scope](PUBLICATION_SCOPE.md).

The recurring cycle is executable: load relevant lessons → carry out the task → save useful findings, failures, and unresolved points → investigate a specific improvement hypothesis → compare it with the existing method → accept it only if the criteria are met. Loading lessons alone does not prove that every subsequent answer improves. This release tests memory operation and the selection of a separate candidate as two distinct things.

### 4. Two measured software improvements

| Failure before the fix | What changed | Actual verification |
| --- | --- | --- |
| An earlier lesson card could hide a later contradictory failure observation. | Observations and cards now share one chronological selection of 16 entries. | The next begin record also contains the newer failure text. |
| At the 5 MiB limit, an unreferenced evidence object left by a failed write prevented even the result of memory compaction from being saved. | Before the atomic save, only already unreferenced objects from the explicitly approved compaction plan are removed. Evidence still in use is retained until the state is successfully replaced. | With 5,242,680 bytes used and 200 bytes free, compaction succeeded and left 4806 bytes. A separate test with an injected write failure preserved the previous state and its evidence. |

Before, after, regression review, 82-test receipt, and full test log. These are explicitly labelled synthetic mechanism tests. Fixing a software failure does not establish an improvement in search accuracy.

The internal records referenced here are omitted from this edition; see [publication scope](PUBLICATION_SCOPE.md).

### 5. The separate search-strategy comparison

The candidate added one technique: first check the least-supported necessary condition that could change the decision. The idea came from applying claim/evidence reasoning to the search process. A separate idea involving unit typing was deferred to avoid combining two changes in one trial.

The criteria and budget, three tasks and correctness checks, existing policy, and candidate were fixed before either side ran. The underlying skill was not weakened for the baseline. Two fresh agent contexts ran the two sides with the same declared model configuration, task order, and limits: no more than 16 web actions, 8 queries, 12 reads, and 12 minutes per task. A failed request also counts as an action.

The internal records referenced here are omitted from this edition; see [publication scope](PUBLICATION_SCOPE.md).

The tasks checked the output units of a specific Depth Anything checkpoint, whether CLIP can produce a free-form descriptive sentence, and the use of DINOv2 for similarity search in a local library. No inference was run and no model weights were downloaded; the research examined documented capabilities and code.

| Metric | Existing method | Candidate |
| --- | ---: | ---: |
| Predefined factual and execution-honesty checks | 9/9 | 9/9 |
| Next-action category | 3/3 | 3/3 |
| Documented useful application of a component | 3/3 | 3/3 |
| Rationale and next-step fields | 6/6 | 6/6 |
| Queries | 15 | 15 |
| Reads, including failed attempts | 32 | 28 |
| Total web actions | 47 | 43 |
| Sum of durations from the first web request to completed artifacts | 456.14 s | 495.50 s |

Across the three new comparison tasks, both methods met all predefined answer criteria. The candidate used 43 web actions against the existing method's 47 but did not achieve the required accuracy gain, so it was not adopted as the new baseline. The result is **no_gain**, not a claim that the candidate is worse in every use. The saving of four actions is an observation from this one pilot; the candidate's combined task duration was also longer. An auditor recalculated the table's durations consistently, from the first real request to completed artifacts. The authors' own differently defined figures of 461.75 and 569.59 seconds are retained separately and do not support a direct speed comparison. The criteria were not switched to cost after the results became known. See the automatic evaluation, register of all six runs, and [complete answers in English](validation/2026-11-09-beta3/comparison/answers.en.md).

The internal records referenced here are omitted from this edition; see [publication scope](PUBLICATION_SCOPE.md).

Four different agents, none of whom wrote either side's answers, provided the optimistic, skeptical, conservative, and innovative reviews. These are not four opinions invented by one agent. Checking that fields are present is not a human readability study. The "innovation" score here measures a documented useful application of a component, not a historically novel discovery.

The internal records referenced here are omitted from this edition; see [publication scope](PUBLICATION_SCOPE.md).

The trial covers only three designed tasks and one answer per side. It used a shared file system with an instruction boundary, not operating-system isolation; model identity is declared by the environment. After the candidate had been fixed, the designer also prepared the initial reference answers. The root agent independently checked them against primary sources and fixed them before execution. Because agent slots were limited, the two sides started about six minutes apart. These limits prevent claims of statistical or universal superiority.

The baseline's completion input contained a schema error: the lesson-reference list included four files where three were allowed. The controller preserved the rejection and separate repair records, reducing only that reference list. All four observation-evidence references, the answers, durations, and queries remained unchanged. The answers were not rerun, and there was no hidden second attempt.

The internal records referenced here are omitted from this edition; see [publication scope](PUBLICATION_SCOPE.md).

After the rejection, another actual loading-verification cycle loaded the saved decision and unchanged baseline policy. It is not counted as another new web research task.

The internal records referenced here are omitted from this edition; see [publication scope](PUBLICATION_SCOPE.md).

### 6. What was retained, rejected, and deferred

| Status | Specific content |
| --- | --- |
| Retained | Both fixes for reproduced failures; source/answer checksums; compact lessons about units, concentration, number/object identity, and prerequisites for proof. |
| Rejected as the new baseline | The prerequisite-prioritization candidate did not achieve the required accuracy gain. Its results and the reason for rejection remain available. |
| Deferred with a testable hypothesis | Lesson-relevance selection, a separate trial with a cost objective, and an evaluation of the additional benefit of languages. These need new tasks and a predefined acceptance criterion. |

Memory is bounded. A compressed conclusion cannot retain all its source material indefinitely; raw evidence is discarded only under a documented plan. This release's complete private research records are stored separately. The public material contains the authors' answers, calculations, and compact provenance records, without full-text copies of third-party pages.

### 7. Corrected historical accounting and distribution scope

The original report's total of 147 included four declared initial E10 queries whose full output from that run was not retained. The independent check confirms 143 distinct queries with retained original receipts. The existing E10 recovery reads are linked to their sources; the missing receipts have not been invented. The new final selection's count of 156 applies only to its 30 cases.

The internal records referenced here are omitted from this edition; see [publication scope](PUBLICATION_SCOPE.md).

The original release used the public distribution page at https://reyrun-rekursive-deep-search.runcisreinis.chatgpt.site for its download, documentation, validation report, examples, video, and draft Facebook post. At that time, public mirrors on GitHub, Hugging Face, ModelScope, and Gitee had not been created. No Facebook post had been sent on the author's behalf.

Publication update, November 10, 2026: the public [GitHub repository](https://github.com/runcisreinis-glitch/reyrun-recursive-deep-search) has been created and its ownership and public visibility checked through the API. Repository creation is separate from verification that every file has been uploaded. The publication manifest records the files to compare after the upload. This update does not claim completed upload verification.

This is a research skill and an executable learning cycle for a connected agent environment. Downloading the package or pasting instructions into an ordinary chat does not itself start a round-the-clock process or guarantee persistent memory. Acceptance testing for a specific installation consists of a real first task, a second task, and evidence that the second task loaded experience from the first.


<a id="final30"></a>

## Final selection: all 30 answers

Validation date: November 9, 2026. Release: 2.0.0-beta.3.

This set contains 10 everyday questions in ordinary, sometimes unclear language, 10 moderately difficult questions across different fields and 10 difficult questions. Seven difficult examples include a complete mathematical derivation or proof and a verification calculation that was actually run.

The questions were prepared for validation; they are not interviews with 30 people. Explicit and simulated conditions are not claims about Reinis's actual home, health, finances or devices. Web searches, source reading and the stated calculations were actually performed. Physical tests that were not performed remain proposals.

The selection contains **12 retained and 18 new examples**, with **156 queries** in total. Every example includes searches in English, German, Chinese and Japanese. This does not mean that a suitable primary source was found and read in every language. Source-reading limits and failures remain in the private evidence register; the complete answer texts are published below.

The original 30 examples remain separately in the history. With the 18 additions, the research collection contains 48 distinct main tasks. The three new method-comparison tasks and repeated runs are not counted in that total.

Begin and end operations for this selection's research were manually orchestrated. Evidence files for the new medium and mathematics groups were also checked with a separate strict record validator. This does not claim that an independent background agent launched all the research.

[Validation report](validation/2026-11-09-beta3/release-report.en.md) · Source and claim register · [Original 30 examples in English](validation/2026-11-09/30-examples.en.md) · [Original Latvian edition](validation/2026-11-09/30-examples.lv.md).

The internal records referenced here are omitted from this edition; see [publication scope](PUBLICATION_SCOPE.md).

The English text is a translation of the recorded answers. Original query strings, source-language evidence, identifiers and execution receipts are retained privately and are not included in this publication. Translation does not mean that the original research was conducted in English only.

### Contents

#### 10 everyday questions

- [E01: Makeup disappears after an hour](#final30-e01)
- [E02: Choosing trousers for your height](#final30-e02)
- [E04: Will any 65 W USB-C charger work?](#final30-e04)
- [E05: What do the washing symbols mean?](#final30-e05)
- [E07: Freeing phone space while keeping photos](#final30-e07)
- [E08: Does 5 GHz mean five times faster internet?](#final30-e08)
- [NE01: Two deciliters of flour: volume or mass?](#final30-ne01)
- [NE02: Will one bucket of paint cover the room?](#final30-ne02)
- [NE03: Where do the calories in cooked rice go?](#final30-ne03)
- [NE04: White, cloudy glasses](#final30-ne04)

#### 10 moderately difficult questions across fields

- [P02: Translating a game while preserving placeholders](#final30-p02)
- [P04: Converting HDR video to SDR](#final30-p04)
- [P05: RAID1 and backups of family photos](#final30-p05)
- [NP01: A fertilizer trial on a sunny windowsill](#final30-np01)
- [NP02: Curtain fabric and shrinkage](#final30-np02)
- [NP03: Heating and mixing water](#final30-np03)
- [NP04: Carbon, ion exchange and reverse osmosis](#final30-np04)
- [NP05: Whether to accept a lower-priced additional order](#final30-np05)
- [NP06: A historical Riga address](#final30-np06)
- [NP07: Birds and window glass](#final30-np07)

#### 10 difficult questions

- [F03: An agent that tests its own improvements](#final30-f03)
- [F08: Causal evaluation of a memory improvement](#final30-f08)
- [F09: An external payment after a process crash](#final30-f09)
- [NF01: Inverting the heat equation](#final30-nf01)
- [NF02: A stochastic process and its discrete variance](#final30-nf02)
- [NF03: Transient growth of a nonnormal matrix](#final30-nf03)
- [NF04: Duality without a finite multiplier](#final30-nf04)
- [NF05: Mass concentration and passage to the limit](#final30-nf05)
- [NF06: The Strang scheme and oscillator energy](#final30-nf06)
- [NF07: The Galois group of a quintic polynomial](#final30-nf07)

### 10 everyday questions

<a id="final30-e01"></a>

#### E01 — Makeup disappears after an hour

**Original question and necessary conditions**

My face gets kind of shiny and my makeup disappears after an hour. What should I buy?

##### Clarification needed

What is your skin type, and is there any irritation? What makeup do you use, and would you prefer to start with an application technique? What is your budget, and which country are you in?

##### SIMULATED answer in the test task

Adult; oily T-zone, normal cheeks, no irritation; everyday makeup; application technique first; EUR 30 in Latvia.

This is a simulation supplied by the person setting the task, not an actual confirmation from a user.

##### Researched answer

I would start with thinner layers of makeup and a small amount of mattifying powder on the T-zone. You do not need to spend the full €30 straight away.

1. Apply a small amount of your usual moisturizer and let it settle. Your skin should not feel noticeably slippery before you apply foundation. You can adjust the amount separately for your oily T-zone and normal cheeks. [KOSE](https://www.kose.co.jp/kose/make/make104.html) describes this approach.
2. Apply a thin layer of foundation; add another layer only where you need more coverage. This is a [technique described by the makeup artists interviewed](https://www.allure.com/story/how-to-make-makeup-last-all-day), and it is worth trying with the foundation you already have.
3. Lightly press a little translucent powder onto your forehead, nose, and chin. Your cheeks do not automatically need an equally thick layer. The [manufacturer's guidance](https://www.essence.eu/de-de/make-up-tips/how-to-setting-powder) also recommends adjusting the amount of powder to different areas of the face.
4. When shine appears, first press a tissue gently against your skin without rubbing. Then touch up the makeup and, if necessary, add a very small amount of powder. This is how [CBC television makeup artists](https://www.hicbc.com/magazine/article/?id=metone-makecolumndo813-260829) do touch-ups.

If you do not have powder, [essence All About Matt, 8 g](https://www.drogas.lv/lv/kosmetika/sejai/kompaktpuderi-puderi/essence-all-about-matt-fixing-kompaktais-puderis-8g/p/BP_225741) is one option for an inexpensive trial. The Drogas page that was opened lists €3.39; check the price and availability before buying. The same page also includes customer complaints that the mattifying effect does not last long. This information cannot predict the individual result on your skin.

My suggestion: try this sequence for one day and inspect the T-zone specifically after an hour. If your makeup still disappears, the next step will be to check the particular combination of moisturizer, sunscreen, and foundation.

*Research provenance: E01; 6 queries; EN / DE / ZH / JA. SHA-256 of the original answer: `5449c7ead17b0ff512966b84a6d5d090392bbec8c7a4e179b0578a1ce863da2e`.*

<a id="final30-e02"></a>

#### E02 — Choosing trousers for your height

**Original question and necessary conditions**

I am 1.80 m tall. What trousers would suit me?

##### Clarification needed

What silhouette and use do you have in mind, and are you looking for a cut or a specific size? Do you know your waist measurement and inseam length?

##### SIMULATED answer in the test task

Everyday wear; prefers a straight silhouette; needs a method for trying trousers on; waist and inseam have not been measured; no specific size requested.

This is a simulation supplied by the person setting the task, not an actual confirmation from a user.

##### Researched answer

I would start with straight-leg casual trousers and compare two cuts: a regular straight cut and one with slightly more room in the thighs. This is my suggestion for trying them on, based on your preference. A height of 1.80 m alone cannot determine the waist size or leg length you need, or which silhouette you will like. Manufacturers treat these measurements separately. [Levi's measuring guide](https://www.levi.com/GB/en_GB/blog/article/how-to-measure-jeans)

When trying them on, check the following:

- Fasten the waistband and sit down. It should still feel comfortable when you are seated; there should be no strong pulling across the thighs or crotch.
- Look from the front, side, and back. Check whether the fabric around the hips is noticeably stretched or hanging too loosely.
- Try the movements you need in everyday life. If possible, take a few steps too. The Japanese tailoring company's [Dankan fitting guidance](https://dankan.co.jp/blogs/dankan-magazine/jeans-size-guide) emphasizes comfort while moving, as well as when standing in front of a mirror.
- Judge the length with the shoes you will wear. For a clean, straight silhouette, I would initially compare a leg that just touches the shoe with a slightly shorter version. That is a matter of taste.

At home, find trousers whose length you already like. Lay them flat and measure the inside seam from the crotch to the hem. Measure the waistband flat and multiply that width by two. [Levi's](https://www.levi.com/GB/en_GB/blog/article/how-to-measure-jeans) describes this method.

When comparing size charts, check whether they show body measurements or measurements of the garment itself. They are not automatically the same, and even the same letter size can differ between cuts. [GU's explanation](https://faq-tw.gu-global.com/articles/zh_TW/Knowledge/000010565)

*Research provenance: E02; 5 queries; EN / DE / ZH / JA. SHA-256 of the original answer: `e55a96805a78342837a6362c5f1e50e447ff72416058cec2ab1535aa407446f5`.*

<a id="final30-e04"></a>

#### E04 — Will any 65 W USB-C charger work?

**Original question and necessary conditions**

Will any 65W USB-C charger work with my laptop?

##### Clarification needed

What is the exact laptop model and charging port? Do you need a compatibility check or a specific purchase recommendation?

##### SIMULATED answer in the test task

ThinkPad T14 Gen 4 AMD, USB-C PD; compatibility checks needed, not a specific purchase recommendation.

This is a simulation supplied by the person setting the task, not an actual confirmation from a user.

##### Researched answer

Not every 65 W charger will work. For your **ThinkPad T14 Gen 4 AMD**, you need to check the USB Power Delivery mode, the power available from the particular port, and the cable. Lenovo lists both 45 W and 65 W USB-C adapters with PD 3.0 for this model; 65 W is also the manufacturer's requirement for rapid charging. [Lenovo specification](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_T14_Gen_4_AMD/ThinkPad_T14_Gen_4_AMD_Spec.PDF)

Check the label in this order:

1. Look for **USB PD / Power Delivery**, as well as “65 W” and a USB-C plug.
2. In the output table, look for **20 V ⎓ 3.25 A**, or a higher available current at 20 V, to obtain the full 65 W. The calculation is 20 × 3.25 = 65. The [Lenovo 65 W adapter description](https://m.lenovo.com.cn/wiki/product-1039806.html) also specifies this output.
3. Make sure that the relevant port supplies this power in the way you will use it. On a multiport charger, “65 W” may be the total power. For example, the [Buffalo specification](https://www.buffalo.jp/product/detail/print/bsacpd6505c2bk.html) gives one device up to 65 W, while two devices share 45 W and 20 W.
4. If the cable is detachable, it must also be rated for at least 65 W. At 20 V it needs to carry more than 3 A. A cable marked 60 W is insufficient for the full 65 W; [USB-IF](https://usb.org/cable_connector) explains that cable power capabilities differ and are identified separately in certification markings.

For a practical check, connect only the laptop first and see whether it displays a slow-charging message and whether the battery level rises while you work. [Microsoft](https://support.microsoft.com/de-de/windows/experience/power-battery/pc-is-charging-slowly-or-discharging-while-it-s-plugged-in) describes situations in which an unsuitable power supply causes a computer to charge slowly or continue discharging. This is a sequence of checks; no particular charger has been tested with your computer here.

*Research provenance: E04; 6 queries; EN / DE / ZH / JA. SHA-256 of the original answer: `c8478d1e38f89ef7bbac47764f96225e5e7e498f7f25b301d23bc4db2cb6d6c5`.*

<a id="final30-e05"></a>

#### E05 — What do the washing symbols mean?

**Original question and necessary conditions**

The garment shows 30 degrees, an underlined wash tub, and a crossed-out triangle. How should I wash it?

##### Researched answer

Choose **a gentle wash cycle at no more than 30 °C and a detergent without bleach**. If there is one line under the wash tub, the symbols mean the following:

| Symbol | What it requires |
|---|---|
| “30” inside the wash tub | The water temperature must not exceed 30 °C. |
| One line under the wash tub | Gentler mechanical treatment, a smaller laundry load, and gentler spinning. |
| Crossed-out triangle | Do not bleach, including with oxygen bleach. |

These meanings are explained in the [GINETEX care-symbol guide](https://ginetex.de/pflegekennzeichnung/pflegesymbole/) and the [Japanese Consumer Affairs Agency's chart](https://www.caa.go.jp/policies/policy/representation/household_goods/guide/wash_02.html).

In practice, use your washing machine's instructions to choose a cycle suitable for a gentle 30 °C wash. Simply lowering the temperature of a normal intensive cycle is insufficient: the line also calls for gentler agitation. For this setting, GINETEX recommends filling the drum no more than halfway and using a short spin or no spin. This label does not specify a universal spin speed. [GINETEX](https://ginetex.de/pflegekennzeichnung/pflegesymbole/)

Check the ingredients or instructions for both the detergent and any stain remover. A “for colors” label can help you find a suitable product, but the essential requirement is that it contain no bleach. The ban on bleaching also applies to a product you might add separately to treat a stain.

If there are **two lines** under the wash tub, an even gentler cycle is needed. Other symbols govern drying and ironing; these three do not tell you whether the garment can go in a tumble dryer.

*Research provenance: E05; 4 queries; EN / DE / ZH / JA. SHA-256 of the original answer: `d09651aa27257dad550470ee30cb329662c8253d1ec2a73280e26fbe1ece108c`.*

<a id="final30-e07"></a>

#### E07 — Freeing phone space while keeping photos

**Original question and necessary conditions**

My phone is running out of space. Will deleting in Google Photos free up the phone while keeping the pictures?

##### Clarification needed

Are you using Android or iPhone, is Google Photos backup turned on, and do you mean Free up space or Delete?

##### SIMULATED answer in the test task

Android; Google Photos backup enabled; explain Free up space and Delete without actually deleting anything.

This is a simulation supplied by the person setting the task, not an actual confirmation from a user.

##### Researched answer

**Yes, by using “Free up space on this device” after checking the backup.** Ordinary deletion in the Android app does something different.

| Action | What happens |
|---|---|
| **Free up space on this device** | Removes copies of photos and videos from the phone once they have been safely backed up. They remain in the Google Photos account. |
| **Delete / Move to trash** | Deletes pictures from Google Photos and the device; deletion of backed-up pictures also propagates to devices where backup is turned on. |

Google describes this distinction in its instructions for [freeing space on a device](https://support.google.com/photos/answer/6128843?co=GENIE.Platform%3DAndroid&hl=en) and [deleting photos](https://support.google.com/photos/answer/6128858?co=GENIE.Platform%3DAndroid&hl=en).

**I would proceed as follows:**

1. In the Google Photos profile, check that the correct Google account is selected and the status is **“Backup complete”**. Having backup enabled does not mean it has finished.
2. Open the information for a few important pictures and check for **“Backed up”**. As an additional check, open them in the same account at [photos.google.com](https://photos.google.com). Google explains [how to check the overall backup status and the status of an individual photo](https://support.google.com/photos/answer/6193313?co=GENIE.Platform%3DAndroid&hl=en).
3. Only then select **“Free up space on this device”**. Before confirmation, the app shows how much space it will free.

After removing the local copies, you will still see the pictures in Google Photos when signed into the account with an internet connection. They will no longer be available in the phone's ordinary gallery or offline. Recent files less than 30 days old may remain on the device, so this feature does not always remove every local copy. [Google Help](https://support.google.com/photos/answer/6128843?co=GENIE.Platform%3DAndroid&hl=en) states this.

This is an explanation of the actions; nothing has been deleted from the phone.

*Research provenance: E07; 4 queries; EN / DE / ZH / JA. SHA-256 of the original answer: `a87fa37d17041a24d4789ad062b1117241ac4be52b708b15389f582cb17b215d`.*

<a id="final30-e08"></a>

#### E08 — Does 5 GHz mean five times faster internet?

**Original question and necessary conditions**

What does 5 GHz on the router mean? Will the internet be five times faster?

##### Researched answer

**5 GHz is a Wi-Fi radio frequency band. It does not promise five times faster internet.** Gigahertz describes how frequently a radio wave oscillates; data transfer speed is measured, for example, in megabits per second, or Mbit/s. “5 GHz” is the name of the band in which the router and your phone or computer communicate. [Intel's explanation](https://www.intel.com/content/www/us/en/products/docs/wireless/2-4-vs-5ghz.html).

In practice, the choice usually looks like this:

| Band | When it may be preferable |
|---|---|
| **5 GHz** | Closer to the router, when you need higher data throughput and have a good signal. Wider channels are generally possible. |
| **2.4 GHz** | Farther from the router or behind several walls, if the 5 GHz connection becomes weak. However, there may be more interference in this band. |

These are tendencies, not guarantees for a particular apartment. [Buffalo](https://www.buffalo.jp/support/faq/detail/15959.html) notes that 5 GHz does not always provide a faster or more stable connection. [TP-Link](https://media.tp-link.com.cn/document/html1714457949100.html) also explains that the number of signal “bars” alone does not tell you the speed, because interference and channel quality matter.

**Internet speed is limited by the entire chain:** your internet service, router, device, and Wi-Fi conditions. For example, switching to 5 GHz alone will not turn a 100 Mbit/s connection into a 500 Mbit/s connection. This is a conclusion drawn from these limitations, not a measurement of your network. [Intel](https://www.intel.com/content/www/us/en/products/docs/wireless/2-4-vs-5ghz.html).

**I would start with a simple comparison:** if both bands are available separately, test each one several times with the same device in the same place. I would also compare the stability of video or calls. The best choice is the one that works well where you actually use the device.

*Research provenance: E08; 4 queries; EN / DE / ZH / JA. SHA-256 of the original answer: `6f96f040a16a7fe71cea977e04a72322a48b382a59dfcd2c97b10566eb8dd75e`.*

<a id="final30-ne01"></a>

#### NE01 — Two deciliters of flour: volume or mass?

**Original question and necessary conditions**

That cookie recipe says two deciliters of flour. So do I just put 200 on the scales and that's it, or do I need to do something else?

*Test conditions:* The recipe says 2 dl of wheat flour; no weight or particular flour brand is specified. Record any necessary clarification as a test result; do not invent a density value.

##### Researched answer

**Do not automatically weigh out 200 g.** The recipe's **2 dl is 200 ml**, which is a volume. To obtain grams, you need to know the mass of that amount; for flour, volume and mass do not have the same numerical value. The general relationship is mass = density × volume. [NIST's explanation of units](https://www.nist.gov/pml/special-publication-811/nist-guide-si-chapter-8).

For this recipe, use a measuring container with a 200 ml mark and do not compact the flour. If the recipe's author also provides an amount in grams, weighing that amount is the easiest option. Dr. Oetker explains that the mass of dry ingredients can differ for the same volume; King Arthur shows that compacting flour also affects the result. A single “grams per cup” figure found online should therefore not be presented as an exact conversion for your recipe. [Dr. Oetker](https://www.oetker.de/inspiration/tipps-tricks/t/mengenangaben-beim-backen-umrechnen), [King Arthur](https://www.kingarthurbaking.com/blog/2023/10/13/how-to-measure-flour).

If you want to use only scales next time, you can weigh the 200 ml measured for this particular recipe once and record the flour type and measuring method. This is a practical way to repeat the measurement; no flour was physically weighed in this test.

##### What we checked

Calculation: 2 × 100 = 200 ml. This alone does not establish the mass in grams. No invented flour-density value was used in the test. No additional question is needed to resolve the unit mix-up; ask for the recipe author's amount in grams only if an exact weight is required.

##### Innovation check

Two transferable methods were considered: checking units before conversion, and saving a one-off measurement for repeated use. The first exposes the incorrect equivalence in this question. The second would require an actual kitchen measurement and remains to be tried. These are adaptations of known methods, not a new theory of physics.

*Research provenance: NE01; 5 queries; EN / DE / ZH / JA. SHA-256 of the original answer: `a48ea1361fbe31664609f1f6c4294d0476059e8c11c4575fd35705bf5ecfc72a`.*

<a id="final30-ne02"></a>

#### NE02 — Will one bucket of paint cover the room?

**Original question and necessary conditions**

The room is four by three. I'll get one bucket of paint for all the walls. That'll be enough, right?

*Test conditions:* First name only the essential missing quantities. Then use a clearly labeled simulated clarification: length 4m, width 3m, height 2.5m, door + window area 5m², two coats, the chosen paint states 10m²/L for one coat; the ceiling will not be painted. Calculate the theoretical amount and distinguish it from the actual allowance.

##### Researched answer

**“Four by three” alone is not enough to tell.** How high are the walls, how much area do the windows and doors occupy, how many coats are planned, and what does the bucket say about liters and m²/L? We also need the wall's condition to estimate actual consumption. The manufacturer's calculator uses total wall width, height, and opening area as separate inputs. [Nippon Paint](https://www.nipponpaint.com.hk/en/calculator/).

##### Simulated clarification and calculation

These are the figures supplied in the test task, not assumptions about the user's room: 4 × 3 m, height 2.5 m, doors and windows totaling 5 m², two coats, 10 m²/L for each coat. The ceiling will not be painted.

| Step | Calculation | Result |
|---|---|---:|
| Perimeter of the walls | 2 × (4 + 3) | 14 m |
| Walls before subtracting openings | 14 × 2.5 | 35 m² |
| Area to paint | 35 − 5 | 30 m² |
| Total coverage for two coats | 30 × 2 | 60 m² |
| Paint at the stated coverage rate | 60 ÷ 10 | **6 L** |

The calculation was repeated using exact rational arithmetic in the saved code. **A 5 L bucket is too small under these conditions; 6 L is the theoretical minimum without an allowance.** To answer the question about “one bucket,” we still need to know its capacity.

Any allowance must be distinguished from these 6 L. For example, **if a 10% allowance is chosen for planning**, the result is 6.6 L; 10% is an illustrative choice here, not a universal manufacturer guarantee. Actual consumption depends on the particular paint and surface: Alpina's page gives single-coat consumption for a smooth surface and higher consumption for a rough surface. [Alpina product data](https://alpina-farben.de/produkt/alpina-wandfarbe/).

##### What to carry forward to the next task

The lesson from the earlier flour task was useful here: distinguish the units first. Floor m², wall m², m²/L for one coat, and liters in a bucket are different quantities. A small trial on a known wall area could provide a practical additional check to refine consumption for that surface. No wall was painted in this session; the benefit of such a trial has not been measured.

*Files for the executed calculation:* [calculation.json](validation/2026-11-09-beta3/calculations/NE02/calculation.json) · [calculation.py](validation/2026-11-09-beta3/calculations/NE02/calculation.py)

*Research provenance: NE02; 5 queries; EN / DE / ZH / JA. SHA-256 of the original answer: `b058bcc12b6b055d14cf572f8d12c2df1109424360d63cee952279434a44cc80`.*

<a id="final30-ne03"></a>

#### NE03 — Where do the calories in cooked rice go?

**Original question and necessary conditions**

The rice packet says three hundred and fifty, and the app says one hundred and twenty. Both are per hundred grams. Where do the calories go when I boil it?

*Test conditions:* The task concerns comparing dry and cooked mass, not individual dietary advice. Check both possible bases for recording the food. Calculation example: 100g of dry rice containing 350kcal weighs 280g after cooking without additions; assume that no food energy has been poured away in this example.

##### Researched answer

**First check whether both figures refer to the same state of the product: dry rice or rice that has already been cooked.** Rice absorbs water during cooking, so 100 g of cooked rice contains less of the original dry rice than 100 g of uncooked rice. This explains a large difference in calories per 100 g. [FAO on cooking rice](https://www.fao.org/4/ac344e/ac344e.htm), [Reishunger's explanation for its rice](https://www.reishunger.de/wissen/article/112/kalorien-von-100-g-gekochtem-reis).

##### Example supplied in the test task

Use exactly the given conditions: **100 g of dry rice contains 350 kcal, weighs 280 g after cooking, and no food energy has been drained away with water or added through other ingredients.**

- The entire cooked amount: **350 kcal**.
- Per 100 g: **350 ÷ 280 × 100 = 125 kcal**.
- A 140 g portion: **175 kcal**.

The calculation was also executed in the saved Python code. **125 kcal is the result for this example**, not a universal table value for all rice. It cannot be equated with the particular app's 120 kcal without knowing the rice type and preparation state selected there. For example, the ordinary preparation method described by Japan's Ministry of Agriculture gives a different increase in mass; one cooked-mass factor should not be treated as constant across all recipes. [MAFF](https://www.maff.go.jp/j/heya/kodomo_sodan/0103/01.html).

##### How to record it without confusion

If you weigh dry rice, use an entry for dry rice. If you weigh a cooked portion, choose the corresponding cooked-food entry or calculate the portion's share of the total amount you weighed. Oil, butter, and other additions must be recorded separately.

The claim that “nothing ever changes during cooking” would be too broad. FAO describes how cooking in excess water and draining it can also wash away starch and other components. Those losses are excluded by the conditions of this calculation example. [FAO on preparation losses](https://www.fao.org/4/t0567e/T0567E0i.htm).

##### A method to carry forward

The first method is to distinguish the total amount from the figure “per 100 g”; that was checked here by calculation. The second is to save a measured ratio of dry to cooked mass for one batch. The second remains a proposal here, because no actual rice was cooked or weighed.

*Files for the executed calculation:* [calculation.json](validation/2026-11-09-beta3/calculations/NE03/calculation.json) · [calculation.py](validation/2026-11-09-beta3/calculations/NE03/calculation.py)

*Research provenance: NE03; 5 queries; EN / DE / ZH / JA. SHA-256 of the original answer: `8d1e62bec67334265dfa32fa0241e748b46cfa9360404540c8e1110c815fc401`.*

<a id="final30-ne04"></a>

#### NE04 — White, cloudy glasses

**Original question and necessary conditions**

The glasses come out of the machine white and cloudy. Wash them again or throw them away? Does it even clean anything?

*Test conditions:* The machine model and water hardness are unknown. Distinguish a washing or deposit problem from permanent damage to the glass surface. Suggest a small, gentle test to tell them apart, with a clear limit; do not invent a diagnosis.

##### Researched answer

**Check one glass first; there is no need to throw them all away immediately.** Similar cloudiness can come from removable deposits or damage to the glass surface itself. Manufacturers distinguish these cases; repeated washing cannot restore an already etched surface. [Bosch](https://www.bosch-home.com/de/bosch-erleben/magazin/haushaltstipps/kalk-glaeser-entfernen), [GE Appliances](https://products.geappliances.com/appliance/gea-support-search-content?contentId=21917).

If it is an ordinary, undecorated drinking glass and its care instructions permit this, gently wipe a small cloudy area with a soft cloth dampened with white vinegar. Then rinse thoroughly and dry it. Panasonic describes this kind of spot cleaning for mineral marks. [Panasonic's guidance](https://jpn.faq.panasonic.com/app/answers/detail/a_id/100749/).

- **If the area becomes clear**, at least this part of the cloudiness was a removable deposit. It then makes sense to check water hardness, the machine's softening setting, and product dosing against the specific model's instructions.
- **If nothing changes**, surface damage is one possibility. One home test does not establish that, and it cannot tell you the condition of all the glasses either.
- **If the glass is valuable, old, painted, or already flaking**, do not automatically apply this household method to it. V&A conservators treat such objects separately and note that aggressive treatment can damage the surface itself. [V&A glass-care guidelines](https://vanda-production-assets.s3.amazonaws.com/2019/04/03/14/23/08/658c998f-990b-4586-9a81-b9e7eb95f620/caring_for_glass.pdf).

The next useful information would be the glass's care marking, the machine model, the product used, and whether white marks also appear on other dishes. Without this information, “the machine does not clean” or “all the glasses are ruined” would be guesses. Bosch recommends adjusting the machine settings to the water hardness. [The manufacturer's explanation](https://www.bosch-home.com/de/bosch-erleben/magazin/haushaltstipps/kalk-glaeser-entfernen).

##### What was done in this test

Sources were checked and a conditional sequence of actions was developed. No actual glasses, water, or machine were examined.

The innovation section transfers a materials-diagnosis method: first distinguish a removable surface layer from a change in the surface itself. A second method considered is to change one machine setting at a time and compare the result on one reference glass. This remains to be tried in practice, following the specific model's instructions. The conservation source helped define where the household method should no longer be applied.

*Research provenance: NE04; 5 queries; EN / DE / ZH / JA. SHA-256 of the original answer: `dfdeab62bd4a86a5588a0b76712c3cce1adf33b4934c1b41f469c9309f66fa99`.*


### 10 moderately difficult questions across fields

<a id="final30-p02"></a>

#### P02 — Translating a game while preserving placeholders

**Original question and necessary conditions**

I want to translate a single-player game into Latvian without losing placeholders or text context. Which open-source workflow should I choose?

TEST SIMULATION: JSON strings with {player_name}, plural forms, and dialogue IDs; modifying executable files is outside the task's scope.

##### Researched answer

For this JSON example, I would choose Git with Weblate and a verifiable import/export step. The assumption comes from the test clarification: the file contains `{player_name}`, plural forms, and dialogue IDs. The actual game's files have not been examined.

Weblate is a self-hostable, open-source solution with a [GPL-3.0-or-later license](https://docs.weblate.org/en/latest/contributing/license.html). Before translating, however, you need to identify the JSON variant: the [generic JSON parser](https://docs.weblate.org/en/latest/formats/json.html) does not itself support plural groups or context fields; the [i18next JSON v4 parser](https://docs.weblate.org/en/latest/formats/i18next.html) supports plurals. The game's schema must be the basis for the workflow, and i18next should be chosen only if the files actually conform to it.

I would structure the workflow as follows:

1. Preserve the originals and associate each translation with a stable dialogue ID. Translate the text values; preserve IDs, placeholder names, and the JSON structure.
2. Add the speaker, scene, previous and next lines, and a screenshot where needed for each dialogue. Store this extra context in Weblate or in a separate mapping by ID if the game file has no provision for it. [Weblate's context features](https://docs.weblate.org/ja/latest/user/translating.html).
3. Enable a check for the actual placeholder syntax. `python-brace-format` is suitable if the game uses the corresponding brace syntax; `strict-format` can prevent omission of a number placeholder in a singular form. Other syntax requires a different check. Automatic detection is no guarantee. [Checks](https://docs.weblate.org/en/latest/user/checks.html), [check conditions](https://docs.weblate.org/zh-cn/latest/user/checks.html).
4. Match plurals to the game's rules. CLDR defines `zero`, `one`, and `other` for Latvian cardinal numbers, including fractional-number conditions; the game may represent these categories in its own schema. [CLDR table](https://www.unicode.org/cldr/charts/49/supplemental/language_plural_rules.html).

A lighter alternative for one translator is [Translate Toolkit `json2po/po2json`](https://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/json2po.html) with a PO editor. This adds a conversion step whose reversibility must be checked; the source and translation revisions must match. The [Toolkit license text](https://github.com/translate/translate/blob/master/COPYING) is GNU GPL v3.

I would start with 30 varied strings. First import and export unchanged text, then compare the structure, IDs, and placeholders. For the translation, also check diacritics, text length, and plurals in the game itself. Acceptance condition: no missing key or unauthorized change to a placeholder. If the check fails, I would not start the full translation.

The documentation and Weblate's placeholder-checking class have been examined; installation and testing in the game have not been performed. A new translation platform is not justified at this point. The game's name and an actual JSON sample are still needed for a precise import tool.

*Research provenance: P02; 5 queries; EN / DE / ZH / JA. SHA-256 of the original answer: `48a22fa21d508f6a59b79dc60397392063cff8ed5fa0d121cd423fa5cb725364`.*

<a id="final30-p04"></a>

#### P04 — Converting HDR video to SDR

**Original question and necessary conditions**

I want to convert HDR video to SDR so the colors do not look gray. What do I need to know before using an FFmpeg command?

TEST SIMULATION: H.265, BT.2020/PQ, 10 bits; target SDR Rec.709; the user's file is unavailable.

##### Researched answer

The test clarification specifies H.265 video with BT.2020/PQ and 10 bits, with SDR Rec.709 as the target. This input needs both luminance-range conversion and correct color conversion. Simply changing the file's tag to “BT.709” is insufficient: FFmpeg's `setparams` changes property tags without recalculating the image itself. [Filter documentation](https://www.ffmpeg.org/ffmpeg-filters.html#setparams).

Before choosing the final command, I would check:

- `color_primaries`, `color_transfer`, and `color_space`: the color primaries, transfer function, and matrix.
- `color_range`: whether the input uses a limited or full signal range.
- The pixel format, bit depth, and available HDR luminance metadata.
- The FFmpeg version and available filters, as well as the device that will play the SDR video.

H.265 and 10-bit labels alone do not substitute for this color information. This read-only command is suitable for an initial check:

```bash
ffprobe -v error -select_streams v:0 -show_streams -of json "input.mp4"
```

It outputs stream information; it does not re-encode the video. [ffprobe documentation](https://ffmpeg.org/ffprobe.html).

For FFmpeg's standard `tonemap` filter, the sequence is to interpret the PQ input correctly, convert to linear light using floating-point data, map the tones to the SDR range, convert the colors, and output Rec.709. `zscale` helps perform these color and transfer-function conversions. The linear-light requirement is stated explicitly in both the [current documentation](https://www.ffmpeg.org/ffmpeg-filters.html#tonemap) and the [filter author's original discussion](https://ffmpeg.org/pipermail/ffmpeg-devel/2017-July/213824.html).

I would first try the chosen tone curve on a short clip containing a face, dark areas, and bright lights. During SDR playback, I would check black levels, highlight detail, and the final metadata. One curve, such as Hable, is not automatically suitable for every source.

Possible causes of a gray image include incorrect PQ interpretation, signal range, or player processing. Without the video, these remain hypotheses to test. The next step is the `ffprobe` output and a short sample; preserve the original. No video was re-encoded in this example.

*Research provenance: P04; 4 queries; EN / DE / ZH / JA. SHA-256 of the original answer: `5749bc25a330d96888a7ba606477742be8dabbc6ce4712aeb4bd4dd0e57bcd93`.*

<a id="final30-p05"></a>

#### P05 — RAID1 and backups of family photos

**Original question and necessary conditions**

Is a NAS with RAID1 a sufficient backup for family photos?

##### Researched answer

RAID1 alone is insufficient if the family photos exist only on the NAS. It stores identical data on both disks simultaneously and helps keep the system running if one disk fails. Deletion or harmful overwriting can affect both disks. Loss of the entire NAS also requires a copy outside that device. [Synology's explanation](https://blog.synology.com/de/was-ist-ein-backup/) and [Buffalo's RAID description](https://www.buffalo.jp/topics/trouble/detail/recovery_0005.html) make this distinction.

For family photos, I would use this arrangement:

1. Photo originals on the NAS or a computer.
2. A regular copy with previous versions on a separate drive; disconnect the drive after copying.
3. Another copy in a different location, for example on an encrypted drive at a relative's home. Cloud storage is an option, but it is not required.

This is my practical recommendation to prevent one failure from affecting every copy. The [CISA guide](https://www.cisa.gov/sites/default/files/publications/CISA_MS-ISAC_Ransomware%20Guide_S508C_.pdf) also recommends offline encrypted copies and regular restoration tests. The document itself dates from 2020; I am not presenting it as new research from 2026.

NAS snapshots are useful for recovering an earlier state. If stored only on the same device, they do not solve the problem of losing the entire device. Remote storage changes this situation: [QNAP's documentation](https://www.qnap.com/zh-tw/software/snapshots) describes copying snapshots to another NAS and restoring them there.

If the originals also remain on a phone or computer, the NAS may already be one backup. Check whether synchronization propagates deletion to the other location and whether older versions are retained.

A useful first test is to restore a few new, old, and previously deleted pictures into a separate folder. Open them and check the full resolution and the metadata you need. Set the copying frequency according to how much recent photo history you could accept losing. I have not performed this restoration test here.

*Research provenance: P05; 4 queries; EN / DE / ZH / JA. SHA-256 of the original answer: `cf6c32af9cc0dca17d9ad2afc21227eae813854d9ad6de4a8f1038e9a0dce400`.*

<a id="final30-np01"></a>

#### NP01 — A fertilizer trial on a sunny windowsill

**Original question and necessary conditions**

I have 12 identical potted basil plants. I want to compare two fertilizers; half the windowsill is sunnier. How can I compare them over 4 weeks without accidentally proving only the effect of sunlight?

*Test conditions:* Develop a workable layout, randomization, measurement plan, and limits on the conclusions. Several leaves from one plant are not independent plants. Do not assign a measured result to an experiment that has not been conducted.

##### Researched answer

Arrange the 12 plants in six pairs and randomly assign fertilizer A to one plant and B to the other within each pair. Put three pairs on the sunnier side and three on the less sunny side. Choose the two positions within each pair to be as similar as possible. Each fertilizer will then have six plants, with three in each light zone. This is a randomized block design: a block groups similar conditions, while fertilizers are compared within the block. [NIST's explanation](https://www.itl.nist.gov/div898/handbook/pri/section3/pri332.htm).

##### Layout and assignment

Number the plants from 1 to 12 before assigning fertilizers. I generated the table's assignment with Python and the fixed seed 20261109. No growth data have been collected yet. Within each pair, the left and right positions are adjacent and equally far from the glass. If the light varies in a different direction, turn the pairs accordingly so the lighting is as similar as possible within each pair.

| Pair | Light zone | Left position: plant, fertilizer | Right position: plant, fertilizer |
|---|---|---|---|
| 1 | Sunnier | 6, B | 7, A |
| 2 | Sunnier | 9, A | 11, B |
| 3 | Sunnier | 2, B | 10, A |
| 4 | Less sunny | 4, A | 12, B |
| 5 | Less sunny | 5, B | 8, A |
| 6 | Less sunny | 1, A | 3, B |

Keep the assignment for all four weeks. Alternatively, toss a coin once within each pair to decide which plant receives A; the other receives B. Do not rearrange the plants after seeing which is growing better. Do not move plants between pairs or let one shade another.

##### What to do and measure

Before starting, write down the comparison rule: use each product at the dose and frequency stated on its label. This compares two practical fertilization programs. Equal liquid volumes alone would not mean equal nutrient doses. Keep pot size, substrate, and care routine the same; include the water in the fertilizer solution in the total watering amount. Give each pot its own saucer so that drainage does not mix the treatments.

For this simple trial, I choose the increase in plant height in centimeters from day 0 to day 28 as the primary measure. It measures this growth characteristic; greater height alone does not establish leaf yield or flavor. Measure from the substrate surface to the tip of the same main shoot, at the same time of day, before or after watering according to one rule chosen in advance. Do not pinch off the tip during this period.

On days 0, 7, 14, 21, and 28, record each plant's height, leaf count, and damage, and add a photo with a ruler. Record the fertilizer and water doses, deviations, and approximate hours of direct sun. Water according to the same substrate-moisture rule, because pots in sunnier positions may need different amounts of water. Record the actual amount used. If a plant dies, record this and do not put a new plant in its place as a continuation.

12 plants multiplied by 5 measurement days gives 60 height records, but the experiment has 12 plants. A plant's leaves and weeks are not new, independent fertilizer replicates. Here I apply the [NC3Rs experimental-unit principle](https://eda.nc3rs.org.uk/index.php/experimental-design-unit) to treatment assigned separately to each pot.

##### How to compare

For each plant, calculate growth g = height on day 28 − initial height. Within each pair, calculate d = g(A) − g(B), then calculate the mean difference across the six pairs: (d1 + d2 + d3 + d4 + d5 + d6)/6. Also show all six individual differences and the three pairs in each light zone. Check whether one unusual plant or one zone drives the average. Preserve the pairs in the analysis; the NIST block model makes comparisons while accounting for the block. If a formal test is needed, there are only 2^6 = 64 possible ways to swap A/B assignments within pairs; choose the statistic and null hypothesis before looking at the results.

Four weeks and six plants per fertilizer provide a small comparison for these plants, this windowsill, and the chosen doses. Equal results will not establish complete equivalence between the fertilizers. Without an unfertilized group, you cannot tell whether both fertilizers outperform no fertilizer. A Japanese trial practitioner describes accounting for local conditions, replication, and repeated trials; this is a source for practical organization, not evidence for a particular basil fertilizer. [Kimura, 2025](https://www.kankyo-kanri.co.jp/post/show?id=363).

##### Two ideas to transfer

The blocking principle from industrial experiments can already be used in this plan. An inexpensive check before starting is to make sure that each pair contains A and B and that both positions receive similar light. If one position within a pair is in permanent shade, redesign the layout before fertilizing.

A second option is to read measurements blind from photos renamed with codes. [NC3Rs](https://eda.nc3rs.org.uk/experimental-design-blinding) describes concealing the treatment during outcome assessment. The hypothesis here is that coding will reduce the influence of the desired result on the height reading. Try it on five photos: repeat the reading in random order without looking at the A/B list. If a photo cannot be read reliably to the smallest division on your ruler, keep direct readings as the primary measurement. The benefit of this idea has not yet been measured here.

*Files for the executed calculation:* [calculation-output.json](validation/2026-11-09-beta3/calculations/NP01/calculation-output.json) · [calculation.py](validation/2026-11-09-beta3/calculations/NP01/calculation.py)

*Research provenance: NP01; 5 queries; EN / DE / ZH / JA. SHA-256 of the original answer: `2578c2c50eab70fef25501ea1989d4537ea515de93bd4ea59c511b6884b53bbf`.*

<a id="final30-np02"></a>

#### NP02 — Curtain fabric and shrinkage

**Original question and necessary conditions**

I am sewing two cotton curtains, each with a finished width of 130cm and height of 240cm. The side hems need 8cm in total across the width, and the top and bottom hems need 16cm in total along the length. The fabric is 150cm wide and shrinks 5% lengthwise and 3% across the width. Will 5.2m be enough, and how should I check before cutting?

*Test conditions:* Assume uniform shrinkage at the stated rates, with no pattern matching, defects, or extra allowance. Evaluate width and length separately; calculate the theoretical minimum and explain why a sample of the actual fabric is needed in practice.

##### Researched answer

At the stated shrinkage rates, 5.2 m is insufficient: the theoretical minimum is 5.389473684… m of unshrunk fabric. The 150 cm width is suitable. If fabric is sold by the centimeter, the amount must mathematically be rounded up to 5.39 m; this figure includes neither a practical allowance nor the fabric used for a sample.

##### Calculate width and length separately

Add the stated hem allowances to the finished curtain dimensions before compensating for shrinkage. After prewashing, you must be able to cut two rectangles, each 138 × 256 cm.

| Quantity | Calculation | Result |
|---|---|---:|
| Width of one panel after shrinkage, including side hems | 130 + 8 | 138 cm |
| Available fabric width after shrinkage | 150 × 0.97 | 145.5 cm |
| Minimum starting width for one panel | 138 / 0.97 | 142.268041… cm |
| Length of one panel after shrinkage, including hems | 240 + 16 | 256 cm |
| Starting length for one panel | 256 / 0.95 | 269.473684… cm |
| Total starting length for both panels | 2 × 256 / 0.95 | 538.947368… cm |

The two panels must be placed one after the other along the roll: two widths of 138 cm cannot fit side by side within 145.5 cm. The 256 cm side cannot be turned across the width either. The remaining width after shrinkage is 145.5 − 138 = 7.5 cm across the full width, not on each side. The calculations use exactly the task's dimensions and its assumption of a usable starting width of 150 cm.

The shrinkage percentage is calculated from the starting dimension: after washing, L × (1 − s) remains. To find the starting amount, therefore, divide the required final dimension by 0.95. Simply adding 5% to 5.12 m is insufficient: 5.12 × 1.05 = 5.376 m, which becomes 5.1072 m after 5% shrinkage. Separate measurement of changes in length and width is also specified by the [public scope description for AATCC TM135-2025](https://members.aatcc.org/store/tm135/543/) and the [BOKEN testing procedure](https://www.boken.or.jp/find_tests/textile_general_performance/dimensional_change/1134/).

##### What would happen with 5.2 m

520 × 0.95 = 494 cm. You need 512 cm, so after washing you would be 18 cm short. If the fabric were divided in half, each piece would be 247 cm; after allowing 16 cm for hems, the finished height would be 231 cm, which is 9 cm shorter than required. Before washing, the additional length required is 18.947368… cm.

5.4 m would theoretically work, because 513 cm would remain after shrinkage. That is only 1 cm more than the two panels to be cut combined, so 5.4 m cannot be described as a large practical allowance. Cutting a sample from that same length would have to be accounted for separately.

##### How to test your fabric

Take a piece of the same fabric, preferably a separate sample from the same batch, and mark the lengthwise direction. For a home test sample, you could choose, for example, a piece around 30 × 30 cm and mark three 20 cm distances inside it in each direction. Record the actual starting distances accurately; use internal points for measurement so that frayed edges do not interfere. This is a simplified home test, not a certified standards test.

Wash and dry it as you will later care for the curtains, following the fabric's care instructions. Smooth the dry fabric without stretching it and measure the same distances again. For each direction, the shrinkage percentage is 100 × (before − after) / before. BOKEN describes comparing marked lengths and widths in this way; in its formula, a negative dimensional change means shrinkage. [Method](https://www.boken.or.jp/find_tests/textile_general_performance/dimensional_change/1134/).

If a 20 cm lengthwise mark becomes 19 cm, that would be 5%; if a crosswise mark becomes 19.4 cm, that would be 3%. These are hypothetical check examples, not measurements of your fabric. If the dimensions keep changing after another identical care cycle, recalculate using the new data. The sewing studio SO's own knit-fabric experiment describes changes over several cycles; it cannot supply the shrinkage percentage for these cotton curtains. [SO's account of its experience](https://sewing-so.com/pages/水通し実験データ).

Before the final cutting, wash and dry all the fabric using the intended settings, check the usable width and actual length, and then mark two 138 × 256 cm panels. If a piece was cut from the roll for testing, subtract it from the available length. Exactly 5.2 m would be enough only if the measured lengthwise shrinkage did not exceed approximately 1.5385% and all the task's other conditions were met. The stated assumption of 5% rules this out.

##### Transfer of two mechanisms

The first idea is dimensional precompensation, as used in manufacturing parts. In the [Apple Rubber engineer's explanation](https://www.applerubber.com/hot-topics-for-engineers/350/), the starting dimension is found using final dimension / (1 − shrinkage). The formula also applies to this task, but rubber's shrinkage values must not be transferred to fabric. The reverse check of the calculation has already been executed: 538.947368… × 0.95 = 512 cm.

The second idea is to use a small production test sample before cutting the entire workpiece. This may reveal a difference between stated and actual shrinkage. The advantage can be tested here, but it has not yet been measured: the sample must be washed, and then both axes must be checked to confirm that the required dimensions remain. The fabric used for the sample is not hidden within the total minimum fabric amount.

*Files for the executed calculation:* [calculation-output.json](validation/2026-11-09-beta3/calculations/NP02/calculation-output.json) · [calculation.py](validation/2026-11-09-beta3/calculations/NP02/calculation.py)

*Research provenance: NP02; 6 queries; EN / DE / ZH / JA. SHA-256 of the original answer: `4c17373fee18434e2a383bc3b38f4411cc7ad64b87ae576a55040e687d80a629`.*

<a id="final30-np03"></a>

#### NP03 — Heating and mixing water

**Original question and required conditions**

How much electricity is theoretically needed to heat 80 litres of water from 10 to 60°C if the efficiency of the entire process is 90% and electricity costs €0.15/kWh? How much water at 60°C is needed to make 50 litres of a 40°C mixture with cold water at 10°C?

*Test conditions:* Use ρ = 1 kg/L and c = 4.186 kJ/(kg·K). Compare heat, electricity and cost; assume no heat loss and equal density when mixing. Do not include unspecified long-term storage losses or assumptions about market prices.

##### Researched answer

Heating 80 litres of water requires 4.6511 kWh of heat. At 90% process efficiency, this means 5.1679 kWh of electricity and €0.7752, or €0.78 rounded to cents. Making 50 litres of a 40 °C mixture requires 30 litres of water at 60 °C and 20 litres at 10 °C.

##### Heat, electricity and cost

All figures refer to the stated conditions of the theoretical problem: ρ = 1 kg/L, c = 4.186 kJ/(kg·K), efficiency of the entire heating process η = 0.90, and a price of €0.15/kWh.

The water has a mass of 80 kg and the temperature rise is 60 − 10 = 50 K. Use Q = mcΔT; this relationship also appears in the [KIT laboratory description](https://labs.physik.kit.edu/prakt-nebenfach-manuals/Experiments/Spezifische_w%C3%A4rme_Wasser/).

Q = 80 × 4.186 × 50 = 16 744 kJ = 4.651111… kWh.

The conversion uses 1 kWh = 3600 kJ, as listed in the [NIST unit table](https://www.nist.gov/pml/special-publication-811/nist-guide-si-appendix-b-conversion-factors/nist-guide-si-appendix-b9).

Efficiency is the ratio of useful output to energy input: η = Q/E. The [US Department of Energy](https://www.energy.gov/cmei/femp/articles/take-five-what-energy-efficiency) explains efficiency in these terms. Therefore:

E = Q/η = 4.651111…/0.90 = 5.167901… kWh.

Cost = 5.167901… × 0.15 = €0.775185….

| Quantity | Result |
|---|---:|
| Heat transferred to the water | 4.6511 kWh |
| Electrical energy supplied | 5.1679 kWh |
| Losses in the specified process, E − Q | 0.5168 kWh |
| Cost of this electricity | about €0.78 |

Losses are 10% of the electricity supplied. The electricity requirement therefore cannot be found simply by adding 10% to the heat requirement. Numerical reverse check: 5.167901… × 0.90 = 4.651111… kWh.

€0.15/kWh is the tariff given in the problem. Additional long-term storage losses are not included because none are specified. I also do not add tank heating a second time, because the problem already specifies the efficiency of the entire process. Assessing a real appliance would require a precise definition of what that efficiency covers. The [Nippon Heater technical calculation](https://www.nippon-heater.co.jp/designmaterials/calculation/) lists the water, tank and heat-loss components separately when calculating them from scratch.

##### 50 litres of water at 40 °C

Let x litres be the volume of hot water. The cold-water volume will be 50 − x litres. With equal density and specific heat capacity, and no heat loss, the heat released by the hot water equals the heat received by the cold water:

x × (60 − 40) = (50 − x) × (40 − 10).

20x = 1500 − 30x, so x = 30 L.

I use the [calorimetric balance described by KIT](https://labs.physik.kit.edu/prakt-klass-physik-manuals/P2/Spezifische_Waermekapazitaet/doc/Hinweise-Waermekapazitaet-Mischung/), applied here to two masses of the same kind of water. The common c and ρ cancel.

Check: 30 + 20 = 50 L and (30 × 60 + 20 × 10)/50 = 40 °C. The hot water releases 30 × 4.186 × 20 = 2511.6 kJ; the cold water receives 20 × 4.186 × 30 = 2511.6 kJ. The 90% efficiency is not applied again to this separate mixing step, whose condition is mixing without losses.

##### Two ideas transferred from other fields

Input/output comparison can be borrowed from process-efficiency accounting: measure electricity over a defined heating interval and compare it with mcΔT. The hypothesis is that this would help check whether the real appliance reaches the assumed 90% in that operating mode. A small test needs a separate electricity-metering interval, a known volume of water, and starting and final temperatures. Tank heat and other consumers must not be silently counted as heat in the water. No physical test was performed here.

The second mechanism, mixing two stocks to reach a target property, can be used as a simple quantity calculator: hot fraction = (T_target − T_cold)/(T_hot − T_cold). Here it is 30/50 = 0.60. Code checked both the volume and heat balances; the practical benefit and accuracy in a particular tank have not yet been measured. Applying this formula to other substances would require checking density, specific heat capacity and heat of mixing, so the water simplification is not used universally.


*Executed calculation files:* [calculation-output.json](validation/2026-11-09-beta3/calculations/NP03/calculation-output.json) · [calculation.py](validation/2026-11-09-beta3/calculations/NP03/calculation.py)

*Research provenance: NP03; 5 queries; EN / DE / ZH / JA. Original answer SHA-256: `1f4870d93ee5f77de086383a64dc84ee59d1ce1896c6a8e853a5240edc673a78`.*

<a id="final30-np04"></a>

#### NP04 — Carbon, ion exchange and reverse osmosis

**Original question and required conditions**

A tap-water analysis reports hardness of 280 mg/L as CaCO3 and free chlorine of 0.4 mg/L. Will an ordinary activated-carbon jug filter remove both chlorine and limescale? How can carbon, ion exchange and reverse osmosis be distinguished through actual testing?

*Test conditions:* No specific product is given. Compare the mechanisms supported by the relevant manufacturer/certification records and by before/after measurements. Do not claim that this water analysis alone establishes its complete safety for drinking.

##### Researched answer

A cartridge containing only activated carbon can reduce free chlorine; it should not be expected to reduce water hardness substantially. If a jug also reduces limescale formation, check whether it contains ion-exchange resin as well. Without the name of the particular cartridge, neither the percentage reduction nor its service life can be determined.

An example from manufacturer BRITA shows the distinction within one product family: it describes a carbon and ion-exchange combination separately from a carbon-only element that retains calcium and magnesium. This illustrates the mechanism and is not a recommendation to buy the brand. [Manufacturer FAQ, sections on filter contents](https://www.brita.at/faq/filter-filterkartuschen?sc=maxtra-pro).

##### How the three mechanisms differ

| Treatment | What it does in this problem | What to look for in documents and measurements |
|---|---|---|
| Activated carbon | Oxidation and reduction reactions also contribute to free-chlorine reduction; adsorption is used to reduce odour-causing substances. Reduction of dissolved Ca/Mg cannot be inferred from carbon alone. | A specific chlorine-reduction claim supported by evidence; a free-chlorine test before/after. Measure hardness separately. |
| Ion exchange | In softening, the resin replaces Ca/Mg with other ions. A sodium or potassium softener does not remove all dissolved salts. Jug-resin composition and carbonate-hardness reduction can differ. | A precise description of the resin and system; a total-hardness test. If carbonate-hardness reduction is specifically claimed, alkalinity is also needed. |
| Reverse osmosis | Pressure drives water through a semipermeable membrane; the system reduces dissolved substances. Many systems also contain other filters. | Membrane-system data and evidence of TDS reduction; conductivity/TDS and hardness before/after. Assess chlorine reduction from the documentation for the complete system. |

The [Japan Water Purifier Association](https://www.jwpa.or.jp/qa01.htm) describes carbon's chemical action. The [NSF standards overview](https://www.nsf.org/consumer-resources/articles/standards-water-treatment-systems) explains ion exchange and reverse osmosis, while [Hach](https://my.hach.com/parameters/hardness) describes resin exhaustion and hardness testing.

280 mg/L as CaCO₃ expresses hardness using a common equivalent. It does not mean that a litre contains 280 mg of suspended limescale particles that could simply be sieved out. Hach distinguishes hardness, mostly caused by calcium and magnesium ions, from alkalinity; for convenience, both can be expressed in mg/L as CaCO₃. A single total-hardness figure does not determine the carbonate fraction. [Definitions](https://my.hach.com/parameters/hardness).

##### What certification establishes

NSF/ANSI 42 includes requirements such as chlorine and taste/odour reduction. NSF/ANSI 44 covers cation-exchange softeners regenerated with Na/K salts; it does not automatically certify every jug cartridge. NSF/ANSI 58 requires TDS-reduction testing for RO systems, while several claims for other substances are optional. Check the listing for the exact model and cartridge, the particular substance, conditions of use and declared capacity. [NSF overview](https://www.nsf.org/consumer-resources/articles/standards-water-treatment-systems), [scope of NSF/ANSI 58](https://www.nsf.org/knowledge-library/nsf-ansi-58-reverse-osmosis-drinking-water-treatment-systems).

NSF's open component listing also contains an entry marked “Conforms to the material requirements only”. A certification logo or standard number on a component therefore does not by itself establish chlorine or hardness reduction. The listing read has an internal currency date of 1 September 2026; it is used to demonstrate the meaning of the note, not to confirm a particular product's status today. [NSF listing](https://info.nsf.org/Certified/DWTU/Listings.asp?Standard=042&TradeName=carbon&hdModlStd=ModlStd&submit3=Search).

##### Practical testing

First find the cartridge composition and preparation instructions, then install and flush it as directed. At the same session, collect inlet water and outlet water after filtration. Record the date, temperature, volume filtered and the litres previously passed through the cartridge.

Measure free chlorine with a DPD test specifically intended for free chlorine, with a range and resolution suitable for 0.4 mg/L and the expected lower value. Follow the kit's reading time; “total chlorine” is a different measure. Hach also describes chloramine interference in DPD free-chlorine measurements, so an unstable colour change should not be presented as a conclusive filter result. [Hach technical questions](https://sea.hach.com/parameters/faq).

For hardness, use a total-hardness titration kit whose range covers 280 mg/L as CaCO₃. EDTA drop titration is more suitable for a numerical comparison than coarse colour bands; Hach warns that test strips are not intended to give an accurate hardness value. [Measuring hardness](https://my.hach.com/parameters/hardness).

For RO, add a conductivity or TDS reading under the same temperature and calibration conditions. An electronic TDS figure may be calculated from conductivity: the [Hach manual](https://cdn.hach.com/7FYZVWYB/at/v5p779fgxpgwkr28fxxk3/DOC3439780079_10ed.pdf) explicitly specifies a conversion factor. Such a figure is not a direct measurement of Ca/Mg or chlorine. With sodium ion exchange, hardness can fall while other dissolved ions remain. Very low TDS alone also does not prove that RO was used: the documents and equipment construction establish the technology.

Repeat at least three pairs of before/after samples. For chlorine, also keep an unfiltered control sample for the same duration as filtration, so that the effect of time is not attributed to the filter. This is a proposed comparison plan. Repeat it at a later stage in the cartridge's use without exceeding the manufacturer's replacement rules.

Reduction (%) = 100 × (before − after) / before. In a hypothetical example, hardness of 280 → 140 mg/L would give 50%, while chlorine of 0.4 → 0.04 mg/L would give 90%. These post-filter figures were not measured. Report a result below the detection limit as, for example, “< test detection limit”, rather than treating it as exactly zero.

##### Two ideas transferred from other fields, and a limitation

The first is the laboratory approach of using different, complementary measurements: chlorine, hardness and conductivity. The hypothesis is that this can reveal cases where improved taste is confused with softening. The test consists of the sample pairs above and comparison with the cartridge documentation. An improvement in one indicator is not transferred to the others.

The second is testing a component over its service life: record the litres passed through it and repeat the same measurements. Resin exhaustion is also monitored through hardness in the industrial process described by Hach. The hypothesis for home use is that this could detect a declining effect in time; the replacement point cannot be calculated without measurements of the actual filter.

These two initial analysis values and the before/after tests described do not establish the water's complete safety for drinking. NSF also stresses that certification to one standard does not mean reduction of every possible contaminant. [NSF](https://www.nsf.org/consumer-resources/articles/standards-water-treatment-systems).


*Executed calculation files:* [calculation-output.json](validation/2026-11-09-beta3/calculations/NP04/calculation-output.json) · [calculation.py](validation/2026-11-09-beta3/calculations/NP04/calculation.py)

*Research provenance: NP04; 7 queries; EN / DE / ZH / JA. Original answer SHA-256: `c70408c0cdcf78bf8954df8482a6bf273fd2f85f0b6af28262f2cd154496466d`.*

<a id="final30-np05"></a>

#### NP05 — Whether to accept a lower-priced additional order

**Original question and required conditions**

A workshop sells a mug for €24; materials and packaging cost €9, and pay for each mug produced is €6. Monthly fixed costs are €360. Capacity is 120 mugs; the main order is for 40 mugs. An additional customer wants 30 at €18. Should the order be accepted, and how many mugs must be sold at the normal price to cover costs?

*Test conditions:* This is a hypothetical problem: taxes, commissions and external prices have already been excluded; the additional order does not displace the main order. Distinguish revenue, variable costs, contribution margin and profit; also show a condition under which the conclusion would change.

##### Researched answer

**Under the stated conditions, accepting the additional order is worthwhile: it produces €90 of additional profit. Selling only at the normal price, 40 mugs must be sold to cover monthly costs.** If all 30 additional-order mugs are also guaranteed to sell at €18, 30 mugs at the normal price are enough; the total quantity sold is then 60.

This is the hypothetical calculation in the problem, not an observed result from a workshop. I assume that the stated mugs produced are also sold and that the €360 fixed costs remain unchanged within the stated capacity.

##### Calculation

Variable cost per mug is **9 + 6 = €15**. I also include pay for each mug produced in the additional order: spare capacity does not eliminate piece-rate pay. At the normal price, a mug contributes **24 − 15 = €9** towards covering costs; at the special price, it contributes **18 − 15 = €3**.

Contribution margin is revenue minus variable costs. Profit remains after deducting fixed costs. I checked these definitions and the break-even formula in [ACCA's explanation of sales volume and costs](https://www.accaglobal.com/gb/en/student/exam-support-resources/fundamentals-exams-study-resources/f5/technical-articles/CVP-analysis.html).

| Measure | 40 mugs at €24 | Additional 30 at €18 | Both orders |
|---|---:|---:|---:|
| Revenue | €960 | €540 | €1500 |
| Variable costs | €600 | €450 | €1050 |
| Contribution margin | €360 | €90 | €450 |
| Fixed costs | €360 | €0 additional | €360 |
| Profit / increase in profit | €0 | +€90 | €90 |

A total of **70 mugs** must be produced, leaving **capacity for another 50 mugs** out of the 120-mug capacity. The user has already specified that the additional order does not displace the main order. With spare capacity, the order decision compares its additional revenue with its additional costs; unchanged total fixed costs are not added again to this decision. This reasoning is described in the [OpenStax chapter on special orders](https://openstax.org/books/principles-managerial-accounting/pages/10-2-evaluate-and-determine-whether-to-accept-or-reject-a-special-order); a similar spare-capacity example appears in [Niigata University teaching material](https://www.nuis.ac.jp/pub/common/pdf/2020/or_kanrikaikei_2.pdf).

##### How many must be sold to cover costs?

**Without the additional order:**


$$
Q=\frac{360}{24-9-6}=40.
$$


Check: 40 × 24 = €960 of revenue; 40 × 15 + 360 = €960 of costs. At 39 mugs there would be a €9 loss; at 41, a €9 profit.

**With the additional order definitely fulfilled:**


$$
9Q+30\times3-360=0,\qquad Q=30.
$$


In that case, 30 normal-price and 30 special-price mugs generate €1260 in revenue, €900 in variable costs and €360 in contribution margin. This is a different sales mix. The stated main order is already 40 mugs, so the actual scenario in the problem results in €90 profit, not zero.

##### When would the decision change?

The following examples **change the original conditions**; they are not hidden extra costs being added to the stated problem.

- If this order specifically caused additional one-off costs (K), the increase in profit would be **90 − K**. At €90, the order would no longer increase profit; above €90, accepting it would not be financially worthwhile.
- If capacity became full and the order displaced (q) normal-price mugs, with the same unit costs the increase would be **90 − 9q**. Ten displaced mugs would erase the entire benefit; 11 would give −€9, while replacing all 30 would give −€180.

Including the lost contribution margin of an alternative order is supported by [ACCA's material on relevant costs](https://www.accaglobal.com/gb/en/student/exam-support-resources/fundamentals-exams-study-resources/f5/technical-articles/relevant-costs.html). Its example of idle hours already paid for is not applied here to the €6 piece-rate pay: the conditions differ.

##### Two ideas transferred from other fields and their tests

**1. The value of capacity, from mathematical optimisation.** A resource's shadow price describes how an additional unit of the resource changes the objective value; I checked this concept in the [SAS documentation](https://support.sas.com/documentation/cdl/en/ormpug/66107/HTML/default/ormpug_optmodel_sect102.htm). Hypothesis: before rejecting a price, establish whether capacity is binding and which order would be lost. Here the remaining 50 places mean that the stated orders do not compete for capacity. The executed test compares displacement of zero and 10, 11 and 30 mugs. The idea is useful for checking conditions; this two-order problem does not require an optimisation program.

**2. Boundary testing, from experimental and software testing.** Hypothesis: the decision can be made testable by changing one assumption and checking both sides of the threshold. The code executed the 39/40/41 and 29/30/31 mug cases, as well as the €90 additional-cost threshold. All agree with the direct revenue and cost balance. This is a calculation test, not evidence about demand or production in a real business.

Sources were read on 9 November 2026. EN, DE, ZH and JA searches are preserved; these figures have not been compared with practical workshop observations. The calculation was checked with executed code and a review by one agent; independent external evaluation has not yet been performed.


*Executed calculation files:* [calculation-output.json](validation/2026-11-09-beta3/calculations/NP05/calculation-output.json) · [calculation.py](validation/2026-11-09-beta3/calculations/NP05/calculation.py)

*Research provenance: NP05; 6 queries; EN / DE / ZH / JA. Original answer SHA-256: `88e58e88ef87ca52b9b6672580a69df6bdc096c92c28f85b4a8734af264c9d61`.*

<a id="final30-np06"></a>

#### NP06 — A historical Riga address

**Original question and required conditions**

I found a street name and house number in an old Riga address book. Can I simply equate it with today's address? Create a verification procedure and demonstrate one real example of a Riga street renaming, with sources.

*Test conditions:* No specific private address is given. Do not invent a building's identity. Check the period in which the historical name was used and the possibility of changes to numbering and the street's route; use primary sources from the National Library of Latvia (LNB), archives, museums or the municipality. A foreign-language search may return no results; note that.

##### Researched answer

**An old street name and house number cannot automatically be converted into today's address.** First find the street and the relevant section at that time, then check the continuity of the number and the building itself. An identical number or similar name provides a search lead, not a proven match.

No specific year, name or private address is given, so I do not identify a building here. Below is an actionable verification procedure and a documented renaming example.

##### Verification procedure

1. **Record the original entry.** Save the address book's title, publication year, page number and page image. Transcribe the street, number, letter or building designation exactly as in the original. Compare the OCR text with the image; distinguish the book's publication year from the period its data describe. A real search starting point is the [LNB catalogue record for the 1846 Riga address book](https://dom.lndb.lv/data/obj/419752.html). This research read its metadata, not a particular house entry in the book.

2. **Build a dated chain of names.** Establish when the name was used, its German/Russian spelling variants and the renaming document. The [Museum of the History of Riga and Navigation describes the street-name index published by LNB and the museum](https://www.rigamuz.lv/rvkm/izdevumi/rigas-ielu-laukumu-parku-un-tiltu-nosaukumu-raditajs-no-18-gs-lidz-musdienam/); a bibliographic record does not mean that the required page of the book has been checked. The [LNB authority record for Brīvības iela](https://dati.lnb.lv/onto/nll_geo/lv/page/LNC10-000282215?clang=en) shows why periods matter: it gives 1942–1944 for the name Ādolfa Hitlera aleja and 1950 as the start of the name Ļeņina iela. These variants from different periods must not be treated as simultaneous addresses.

3. **Check the street section and route.** Locate intersections, the block, street ends and landmarks on a map from that period. Compare it with a modern map: has the street been divided, extended, merged or rerouted? The [LNB Maps Reading Room description](https://lnb.gov.lv/en/maps-reading-room/) says its map browser allows historical and modern data to be compared. This capability was checked in the source description; maps of a particular plot have not been overlaid here.

4. **Check the numbering separately.** Compare address books before and after the change, and look for a renumbering or address-assignment decision. Check the side of the street, neighbouring numbers, corner-building addresses, plot subdivision/merger, and whether the number refers to a building or another registered object. The [GEO RĪGA data description](https://georiga.eu/en/atvertie-dati/rigas-ielas-un-adreses/) distinguishes the address of a building or land parcel from the street name and centreline; addresses may be assigned, changed, clarified or abolished through a separate decision. A name change alone therefore does not prove that the number was retained.

5. **Establish continuity of the physical object.** If needed, use a building file, inventory plan, plot documents, house register or dated photograph. Compare location and building features; if the house was demolished, report the historical location separately from the object now occupying it. The [historical description of collection 1432 at the Latvian State Archives](https://www.archiv.org.lv/apraksti/F/LV_LVA_F1432_VI.pdf) explicitly describes house registers for demolished buildings, as well as incomplete or damaged entries. Mark an incomplete source rather than filling it with a guess.

6. **Record the result with its level of evidence.** A practical table is: “old address and year → street section → numbering source → building/plot source → present address → what remains unknown”. If the number or building link is missing, the result remains “street match found; building match not established”.

##### A real example: the division of Maskavas iela in 2024

Riga City Council's **decision No. RD-24-3402-lē of 21 February 2024**, officially published on **28 February**, establishes the following changes:

| Street before this renaming | Section or object | Name after the decision |
|---|---|---|
| Maskavas iela | From 13. janvāra iela to Lāčplēša iela | Lastādijas iela |
| Maskavas iela | From Lāčplēša iela to Riga's boundary | Latgales iela |
| The then-existing Latgales iela | The separate street identified in paragraph 1 of the decision | Jāņa Klīdzēja iela |

The source is the [municipal decision itself in the official gazette](https://www.vestnesis.lv/op/2024/42.20), especially paragraphs 1, 2.1, 2.2 and 4. It also provides for changes to the addresses of addressable objects.

**Checking the period:** 21 February is the adoption date; 28 February is the official publication date. The [municipality's announcement of 1 March 2024](https://www.riga.lv/lv/jaunums/jaunie-rigas-ielu-nosaukumi-ir-speka-izmainas-pilsetvide-tiks-veiktas-pakapeniski) confirms that the new names were already in force then, while signs and various external resources were changing gradually. I do not infer the exact effective date solely from the adoption date. Nor do I use this document to attribute uninterrupted use of the name “Maskavas iela” throughout the 19th and 20th centuries: the year of an older address book must be checked separately.

The example shows two mistakes to avoid. Not all of the old Maskavas iela became Latgales iela. Also, immediately before this renaming, “Latgales iela” denoted a different street from the section of the former Maskavas iela receiving that new name. **No row in the table proves that an old house number or the building itself has survived.**

##### Two ideas transferred from other fields

**Identity matching from databases.** Hypothesis: store the street name together with its time period and section, while storing building identity separately. In the inexpensive test that was executed, the three transitions in the decision were entered into code. “Maskavas iela” without a section yields **two candidates**; with a known initial section, it yields one name, but building identity remains undetermined. This directly prevents erroneous replacement of one name throughout the dataset. The test applies only to this 2024 decision.

**Spatial alignment from cartography.** Hypothesis: check a historical map against several clearly identified landmarks and defer the conclusion if neighbouring blocks do not match. The LNB service description establishes that the required comparison tool exists. A trial for a specific address has not yet been performed because no address was supplied; I do not invent distances or metre-level error estimates. The existing map browser should be the starting point before developing a separate georeferencing program.

EN, DE, ZH and JA queries were executed in this research. The ZH and JA results did not provide a citable primary source specifically for this Riga renaming; the gap has not been filled with a translated secondary text. Sources were read on 9 November 2026. Verification was performed by one agent; no particular house was located and no independent external review was performed.


*Executed calculation files:* [calculation-output.json](validation/2026-11-09-beta3/calculations/NP06/calculation-output.json) · [calculation.py](validation/2026-11-09-beta3/calculations/NP06/calculation.py)

*Research provenance: NP06; 9 queries; EN / DE / ZH / JA. Original answer SHA-256: `815e2ed72240d0b4127fba8c3ad37632ad6b1a9f62237d738f8719a7c501f58b`.*

<a id="final30-np07"></a>

#### NP07 — Birds and window glass

**Original question and required conditions**

Birds have flown into a large window twice. Is one bird-of-prey sticker in the middle enough? Compare solutions by mechanism, evidence and how I can check the change.

*Test conditions:* Do not recommend buying a particular brand. Explain surface placement, pattern-density requirements and the differences between solutions, distinguishing laboratory/research results from a guarantee for a particular window.

##### Researched answer

**One bird-of-prey sticker in the middle of the window is not enough.** A bird may avoid the sticker and try to fly through the clear space beside it. A practical choice is a dense, clearly visible pattern **on the exterior glass surface across the entire window**, or an external screen covering the whole hazardous area. The inadequacy of a single silhouette and the basic pattern requirements are explained in the [Canadian environment department's guidance](https://www.canada.ca/en/environment-climate-change/services/avoiding-harm-migratory-birds/faq-bird-collisions-glass-windows.html).

##### How to place the pattern

For a simple homemade dot or line pattern, I use these conditions:

- Put the pattern **outside**, on the surface producing the reflection visible to the bird.
- Cover all hazardous glazing, including the edges and large adjacent panes.
- Leave no gaps between markings exceeding **5 cm horizontally or vertically**.
- Make every element at least **5 mm wide**, with clear contrast against the background and reflected vegetation.
- After installation, inspect the pattern from outside at different times of day and from different angles.

This is the specific [general guidance from the Canadian department](https://www.canada.ca/en/environment-climate-change/services/avoiding-harm-migratory-birds/faq-bird-collisions-glass-windows.html). The [Swiss Ornithological Institute](https://www.vogelwarte.ch/de/ratgeber/vogelkollisionen-an-glas-vermeiden/) allows other spacings for certain line designs, for example up to 10 cm for vertical lines at least 5 mm wide. This does not mean that any sparse arrangement of stickers is equivalent. For this unmeasured window, I choose the denser, easily checked 5 × 5 cm approach; parameters from one tested design must not be freely mixed with those from another.

**Placement example only:** if a pane were 1 × 1 m, it could take 20 × 20, or **400 dots**, each 6 mm in diameter, with centres every 5 cm and the outer row's centres 2.5 cm from the edge. The gap between dot edges would then be 4.4 cm. This geometry was checked in code. It is not an estimate of your window's size or a measurement of protective effectiveness.

##### Comparing the solutions

| Solution | Mechanism | Evidence and practical condition |
|---|---|---|
| One hawk or other predator silhouette | Covers only a small area; reflections or an apparent passage remain in the clear areas | One or two stickers on a large pane are insufficient; shape alone does not replace dense coverage |
| Dense exterior dots, lines or patterned film | Visually interrupts the apparent flight path and makes the glass perceptible as an obstacle | Surface, density, contrast and full coverage must be addressed; a decorative film's name does not prove effectiveness |
| Exterior insect screen in a frame, or a suitable exterior covering | A visible obstacle; a screen may also physically separate the bird from the glass | It must cover the whole area. Check its fastening and clearance so that it acts as a barrier; no particular brand is required |
| Closed exterior shutter or blind | Covers the problematic glass area | Works only while closed and affects the view/light |
| Interior curtains or a pattern attached inside | May reduce transparency, but the exterior reflection can remain in front of the pattern | A supplementary or temporary measure; it cannot be assumed equivalent to exterior markings |
| UV solution | Changes a particular part of the light spectrum | Check the particular material, installation and study; the label “UV” alone does not guarantee a result |

The Canadian department mentions exterior screens and coverings as alternatives; the Swiss institute explains exterior marking, contrast, density and temporary curtain solutions. The physical-barrier explanation in the table is an inference about the mechanism, not a result from a particular screen tested here. [Source on conditions for the solutions](https://www.vogelwarte.ch/de/ratgeber/vogelkollisionen-an-glas-vermeiden/).

##### What the research supports

The [abstract read from Swaddle and colleagues' 2023 study](https://pubmed.ncbi.nlm.nih.gov/36751632/) compares two films on the interior and exterior surfaces of double glazing. These were controlled flight trials with zebra finches. On the exterior, the evidence of benefit was stronger for one film and weaker for the other; on the interior, the relevant protective effect was not found for either. This is an avoidance-behaviour result from a particular trial, not a fixed, guaranteed reduction in collisions at this window.

UV solutions should not all be treated as one category either. The [abstract of a 2025 Japanese study](https://www.jstage.jst.go.jp/article/jjo/74/2/74_243/_article/-char/ja) reports field observations on a university campus and fewer collisions at locations with UV-blocking film. The Swiss institute, meanwhile, warns of poor results for the UV sticker/film products it tested. Materials, light effects and study conditions differ. For the Japanese study, the abstract was read, not the full methodology, so I do not infer a universal material choice or installation specification from it. The practical recommendation favours a clearly visible exterior pattern.

##### How to check changes at your window

**Do not leave the window untreated merely to collect a new collision “control period”.** The two impacts that have already occurred justify an immediate improvement.

Before the change, save a photograph from outside, record the known dates of both collisions, and note whether the observation period is known at all. After installation, photograph the whole window and use a ruler to check the largest gaps. A single visible gap may matter more than the total sticker count.

During the first month, make the same brief daily check: marks on the glass, a bird near the window, an impact heard, or an event seen on camera. Record **“0 observed”** and separately **“not checked”**; do not count one event twice because you saw it and later found its mark. Note the time, light, reflection and damage to the markings. Continue recording for longer and compare seasonal and observation conditions that are as similar as possible.

One measure could be **observed collisions per window-day**, always accompanied by the inspection frequency. This initial rate cannot be calculated for the two earlier events without a known period. Less frequent observation can miss impacts, so zero is recorded as zero *observed* events. If a collision recurs, check the exterior surface, gaps, contrast and adjacent panes; adding only one new sticker at the problem spot may not be enough.

##### Two ideas transferred from other fields

**1. A physical barrier from engineering.** Hypothesis: if perception of an exterior pattern is uncertain in the particular light, a full exterior screen may provide a different protective mechanism. Its effectiveness at this window has not been tested. The inexpensive initial test is an exterior inspection: full coverage, fastening and clearance from the glass. Sources support the idea here, but no physical installation has been performed.

**2. Event recording from reliability analysis.** Hypothesis: recording exposure and unobserved periods helps avoid turning “nothing was noticed” into a guarantee. The [NIST method](https://www.itl.nist.gov/div898/handbook/apr/section4/apr451.htm) accounts for uncertainty even when no events occur in a test. In a mathematical illustration only, with a constant random-event rate and complete detection, zero events over 30 window-days gives a one-sided 95% upper rate bound of about **0.10 events per day**, not zero. This example, recalculated in code, is not a risk estimate for your window: bird activity, season and detection probability vary in reality. A simple record table is more justified here than a complicated prediction model.

Sources were read on 9 November 2026; EN, DE, ZH and JA queries are preserved. Attempts to open the PeerJ publisher's full text, the 2026 article found, and the Taiwanese practitioners' page returned 403 errors; their unread content is not evidence for this answer. The particular window was not observed here, and no independent external verification of the results was performed.


*Executed calculation files:* [calculation-output.json](validation/2026-11-09-beta3/calculations/NP07/calculation-output.json) · [calculation.py](validation/2026-11-09-beta3/calculations/NP07/calculation.py)

*Research provenance: NP07; 6 queries; EN / DE / ZH / JA. Original answer SHA-256: `1fd8403f3e4af2c0475d1af15b9ca82c1944b428147cafcef4f8404d3b260d23`.*


### 10 difficult questions

<a id="final30-f03"></a>

#### F03 — An agent that tests its own improvements

**Original question and required conditions**

How can an agent procedure be built that improves a search skill itself, without deceiving the evaluator or losing the ability to return to the previous version? Existing components and a possible synthesis.

##### Researched answer

##### I would start with GEPA and separately protected evaluation

A search procedure can be improved by comparing a small number of clearly separated candidates. The agent may change search rules and create candidates; an independent executor decides which version to accept. The instruction “do not deceive the evaluator” is insufficient. In the RewardHackingAgents study, modifying the evaluator and accessing hidden answers were separate paths to violations, so both must be protected. This is a finding from that particular study, not a guarantee against all attacks. [Primary study](https://arxiv.org/abs/2603.11337)

An existing starting point is MIT-licensed GEPA: it optimises text candidates using execution errors and evaluation feedback. An adapter for custom systems and a call budget are also documented. DSPy integration suits a workflow already built in DSPy; a direct GEPA adapter may be clearer for a separate search tool. The documentation was checked, but GEPA was not installed here and no comparison with our search tool was performed. [Authors' repository](https://github.com/gepa-ai/gepa)

I would use the following verification procedure.

1. Save the accepted version, its contents, dependencies and checksums. Create a separate candidate for each change.
2. Give training tasks to the candidate creator; keep final test tasks and reference answers in a different process and outside its write/access permissions. Fix the model, tools, budget and critical-error definitions before the comparison.
3. Compare the currently accepted procedure with the candidate on the same tasks. The evaluator recalculates results from actual sources and logs; the candidate's self-assessment earns no acceptance points.
4. Accept only the tested change and retain the previous version. On new work, check the checksum of the loaded version; rollback also restores the corresponding configuration. Git `revert` preserves the reversal in history, but does not itself undo external side effects. [Git documentation](https://git-scm.com/docs/git-revert)

Two ideas to test supplement the existing base. The first transfers prevention of recurring errors to agent memory: keep a short record of rejected candidates. The author of GEPA issue #379 describes a user-reported case of repeated unsuccessful fixes and a related proposal that is still open; it must not be described as an implemented feature. The second uses the principle of reproducible releases: accept only a version package whose result provenance has been checked by an independent verifier. [GEPA discussion #379](https://github.com/gepa-ai/gepa/issues/379)

The inexpensive test: two candidates, tasks separated in advance, and the same limit for each side. Reject the hypothesis of an advantage if the gain disappears under independent recalculation or critical errors increase. Even a successful comparison would support only the particular change on the tested tasks. Detailed evaluator feedback can also help adapt evasion, so the hidden test is not repeatedly used for training. [Authors' 2026 study](https://www.microsoft.com/en-us/research/publication/reward-hacking-challenges-oversight-of-autonomous-research-agents/)


*Research provenance: F03; 6 queries; EN / DE / ZH / JA. Original answer SHA-256: `80c06468dc92c897f893f015e3c3d37f65b131e650477584d8a82202265ec0bf`.*

<a id="final30-f08"></a>

#### F08 — Causal evaluation of a memory improvement

**Original question and required conditions**

I need a causal evaluation of changes to an agent's memory. How can better memory be distinguished from simply doing more searches or receiving easier tasks?

##### Researched answer

**Compare old and new memory on the same tasks, specifying search opportunities in advance.** A single results table in which the new version has more tool calls or a different selection of tasks does not isolate memory's contribution.

An existing starting point is LongMemEval: the authors' repository contains a set of 500 questions, conversation histories, answer-evaluation tools and comparisons for memory operations. It allows testing of information recall in conversations; the full quality of our agent's work still needs to be tested on its own tasks. [LongMemEval authors' repository](https://github.com/xiaowu0162/LongMemEval) A practical study by Redis authors separately compared retrieval of raw conversations, use of extracted memories, and their combination. The authors also warn that results published elsewhere and shown in their chart are not a controlled head-to-head comparison. [Primary-source experiment description](https://redis.github.io/redis-ai-research-public/longmemeval-agent-memory/)

I propose testing four combinations: **old/new memory × low/high number of searches**. A full factorial design includes every combination; [NIST](https://www.itl.nist.gov/div898/handbook/pri/section3/pri333.htm) describes its basis. At each search level, the controlled experiment fixes the number of calls and the external evidence, not just the allowed maximum. The model, prompt, token limit and initial history stay the same; the memory mechanism being tested changes.

Block tasks by difficulty and randomise execution order. Restore the initial memory state before every trial so that one version does not learn from the other's answer. The evaluator does not see the version name; the agent cannot modify reference answers, evaluation rules or hidden tasks. Evaluate factual correctness, refusal to guess, error severity, reading and writing costs, and uncertainty in the paired differences.

In a separate trial, let both versions choose their own number of searches within the same total budget. This measures the **effect of the whole procedure**, including its ability to save searches. Simply selecting only trials with equal call counts after receiving the results would be a different selection and could distort the conclusion.

I would initially test two possible improvements. Source references attached to every memory fact may reduce incorrect recall; this can be tested cheaply on questions containing conflicting dated facts. Retaining rare details alongside the summary may improve accuracy; test this with details discarded by the summary baseline. Both versions must have the same memory-size limit. If the gain disappears with fixed evidence, we cannot attribute it solely to a better memory representation.

Research in four languages was performed here. The described experiment still needs to be executed to measure differences in quality, time and cost.


*Research provenance: F08; 4 queries; EN / DE / ZH / JA. Original answer SHA-256: `e9732308415621f3d5811a191efcb0a98c72105dece05d1e9647e43155058c78`.*

<a id="final30-f09"></a>

#### F09 — An external payment after a process crash

**Original question and required conditions**

Can an LLM agent system guarantee exactly-once execution for all external payments if the process crashes after sending a request? Design a practical solution with its limitations.

##### Researched answer

**A universal “exactly once” guarantee cannot be given for all external payments.** If the service executes a request but the response is lost, the client's local state may be indistinguishable from a situation in which the request never reached the service. A blind retry may create a second payment, while not retrying may leave a payment unexecuted. The AWS authors' account directly addresses this ambiguity and client-assigned unique request identifiers. [AWS Builders’ Library](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/)

In practice, one payment effect can be achieved **within the idempotency contract of a particular service**. For example, Stripe API v1 stores the result of the first request with a given key only after endpoint execution begins. Repeating the same key returns the stored response, including a 500 error. If parameter validation fails, or there is a conflict with a concurrently executing request and endpoint execution does not begin, no idempotency result is stored; such a request can be retried. Keys may be deleted after at least 24 hours; reusing a key that has already been deleted creates a new request. API v2 documents different failure handling, so these rules must not be generalised. [Stripe idempotency](https://docs.stripe.com/api/idempotent_requests)

I would design the procedure as follows:

1. Before sending, save the payment intent, immutable parameters, unique intent ID and outbound job in one database transaction. One intent has one stable service key.
2. A separate worker sends the job. Queue retries use the same key and parameters; the agent cannot turn a retry into a new intent on its own.
3. Mark a timeout as **outcome unknown**, retain the service object ID if received, and reconcile the state with the service's data.
4. Process signature-verified notifications idempotently: record event IDs and do not depend on their arrival order. Stripe documents both duplicates and the absence of an ordering guarantee. [Notification documentation](https://docs.stripe.com/webhooks)
5. As the key approaches its retention limit, stop blindly retrying an ambiguous payment. Resolve it against the service's records or leave it for investigation, preserving the link to the original intent.

Existing components are the service SDK, a transactional database and an outbound-jobs table. AWS's documented *transactional outbox* approach links local changes to the job record, but it does not by itself make the external payment atomic with our database; duplicate messages still require an idempotent recipient. [AWS description of the approach](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html)

I would test two hypotheses: a stable intent key prevents a duplicate effect after a crash, and a separate check of ambiguous outcomes reduces stuck jobs. A fake payment service would be enough initially, with crashes induced before sending, after the effect and before saving the response, alongside key deletion and repeated notifications. The success criterion is at most one effect per intent and correctly reported uncertainty. Completion additionally depends on service availability and payment acceptance. Neither a test nor a payment was executed here; the four-language research produced a design, not proof of a universal guarantee.


*Research provenance: F09; 4 queries; EN / DE / ZH / JA. Original answer SHA-256: `75c719cea342922ccad16425e7db4c22898dcb6bc62dbe0bab8374b4f1b167ad`.*

<a id="final30-nf01"></a>

#### NF01 — Inverting the heat equation

**Original question and required conditions**

Consider u_t = u_xx on (0,π), with u(0,t) = u(π,t) = 0. We want to recover u(x,0) from u(x,1) with an L² noise level δ = 10^-6. Prove or disprove boundedness of the inverse operator in L² using normalised sine modes. Calculate the largest integer mode n whose signal at t = 1, from an initial coefficient of 1, still exceeds δ. Propose one regularisation and state precisely what it does not guarantee.

*Test conditions:* A justified proof, formulas, an executed numerical cross-check and a primary mathematical source are required. Do not present the noise threshold as a guarantee of unique recovery.

##### Researched answer

The inverse operator is not bounded with respect to the L² norm. The highest unit-amplitude mode whose signal at t = 1 strictly exceeds 10⁻⁶ is n = 3.

##### Proof

Choose $e_n(x)=\sqrt{2/\pi}\sin(nx)$. Then $\|e_n\|_2=1$, $e_n''=-n^2e_n$, and these functions form an orthonormal basis of $L^2(0,\pi)$. Section 1 of Tautenhahn and Schröter's paper directly addresses the stated boundary conditions and spectral representation. [Source](https://ems.press/content/serial-article-files/34869?nt=1).

If $f=u(\cdot,0)=\sum a_ne_n$, then

$$
Sf=u(\cdot,1)=\sum_{n\ge1}e^{-n^2}a_ne_n.
$$

All multipliers are positive, so the solution is unique for exact data in the operator's range. The natural domain of the inverse operator is

$$
\mathcal R(S)=\{g=\sum g_ne_n:\sum e^{2n^2}|g_n|^2<\infty\}.
$$

On this domain, $S^{-1}g=\sum e^{n^2}g_ne_n$. It is not a bounded operator defined on all of $L^2$.

Choose $g^{(n)}=Se_n=e^{-n^2}e_n$. Then

$$
\|g^{(n)}\|_2=e^{-n^2}\to0,\qquad
\|S^{-1}g^{(n)}\|_2=1.
$$

Boundedness would require $1\le C e^{-n^2}$ with one finite $C$ for all $n$, which is impossible. Equivalently, $\|S^{-1}e_n\|_2=e^{n^2}\to\infty$. No finite bound on the operator norm accommodates this sequence.

##### Noise threshold

For the coefficient $a_n=1$, the signal is $e^{-n^2}$. The condition is

$$
e^{-n^2}>\delta
\iff n^2<\log(10^6)
\iff n<3.71692218885.
$$

Thus $n_{\max}=3$. The executed calculation gave

$$
e^{-9}=1.23409804087\cdot10^{-4},\qquad
e^{-16}=1.12535174719\cdot10^{-7}.
$$

Because of the normalisation, the absolute value of each noise coefficient also does not exceed $\delta$ when the total $L^2$ noise norm is at most $\delta$. This threshold applies to a specified unit amplitude; visibility changes for other amplitudes.

##### Regularisation and its limitation

Spectral truncation can be used:

$$
R_Ng^\delta=\sum_{n=1}^N e^{n^2}\langle g^\delta,e_n\rangle e_n .
$$

It is bounded: $\|R_N\|=e^{N^2}$. The cited paper provides the basis for spectral filters and decomposition of regularisation error, while Rust's work discusses truncation of singular values in measurement inversion. [NIST record](https://www.nist.gov/publications/truncating-singular-value-decomposition-ill-posed-problems-0).

Orthogonality gives

$$
\|R_Ng^\delta-f\|_2^2
\le e^{2N^2}\delta^2+\sum_{n>N}|a_n|^2.
$$

At $N=3$, the noise error in the retained modes is at most $0.00810308393$, but the high-mode tail remains unknown. At $N=4$, this noise bound is already $8.88611052$.

Regularisation does not guarantee the exact initial state, unique recovery from noisy data, or uniformly small total error for all $f\in L^2$. It cannot estimate the discarded tail from $\delta$ alone. For a particular fixed $f$, choosing $N(\delta)\to\infty$ and $\delta e^{N(\delta)^2}\to0$ yields convergence, but no convergence rate is given without an additional smoothness condition. At $\delta=10^{-6}$, the value $N=3$ demonstrates the problem's unit signal; it is not a universally optimal parameter choice.

##### Testing two transfers from other fields

Singular-value truncation from image deblurring transfers directly to this problem: both methods limit division by small spectral multipliers. The executed comparison of the 3rd and 4th modes confirms the cost of noise amplification.

Averaging repeated measurements provides no guaranteed gain here because independent random noise has not been assumed. In a control example, the error $\delta e_4$ repeated 100 times did not decrease under averaging; the inversion error remained 8.88611052. We therefore reject this idea without a noise model.

The next useful test would compare noise and tail bounds for several values of N under an explicitly specified Sobolev-norm bound. No such additional smoothness assumption is given in this problem, and that test has not been performed.


*Executed calculation files:* [calculation-output.json](validation/2026-11-09-beta3/calculations/NF01/calculation-output.json) · [calculation.py](validation/2026-11-09-beta3/calculations/NF01/calculation.py)

*Research provenance: NF01; 5 queries; EN / DE / ZH / JA. Original answer SHA-256: `ea6ba290bb2b250082c0c16969d3a8b410e3dbc3dcf5e4651a14510a7caa5bbe`.*

<a id="final30-nf02"></a>

#### NF02 — A stochastic process and its discrete variance

**Original question and required conditions**

dX_t = -2X_t dt + 3dW_t, X_0 = 1. Derive the mean, variance and stationary distribution. Derive the Euler–Maruyama stationary variance and step-size stability condition; compare h = 0.25 with the continuous model and show what happens at h = 1.2.

*Test conditions:* A derivation, an executed numerical cross-check and an independent primary source are required. Do not replace a Monte Carlo result with a theoretical proof; if simulating, save the seed and code.

##### Researched answer

The limiting distribution of the given process is $N(0,9/4)$. The Euler–Maruyama scheme is stable at $h=0.25$, but its stationary variance is $3$, which is $33\frac13\%$ higher. At $h=1.2$, the mean oscillates with growing amplitude and the variance grows exponentially.

##### Exact solution

Multiplying the equation by $e^{2t}$ and using the Itô product formula gives

$$
d(e^{2t}X_t)=3e^{2t}dW_t,\qquad
X_t=e^{-2t}+3\int_0^t e^{-2(t-s)}\,dW_s.
$$

The integrand is deterministic and square-integrable. The Itô integral is a centred Gaussian variable, and the isometry gives

$$
\mathbb E X_t=e^{-2t},\qquad
\operatorname{Var}(X_t)=9\int_0^t e^{-4(t-s)}ds
=\frac94(1-e^{-4t}).
$$

Therefore, for $t>0$,

$$
X_t\sim N\left(e^{-2t},\frac94(1-e^{-4t})\right).
$$

The limit is $N(0,9/4)$. If also $X_0\sim N(0,9/4)$, independently of future Brownian increments, this distribution is preserved at all times. For the given $X_0=1$, the process is not initially stationary.

This Gaussian stationary distribution and its difference from the Euler scheme are discussed in a book excerpt published by Higham and Kloeden themselves. [SIAM](https://www.siam.org/publications/siam-news/articles/numerics-for-stochastics/).

##### Euler–Maruyama derivation

With independent $\xi_k\sim N(0,1)$,

$$
Y_{k+1}=(1-2h)Y_k+3\sqrt h\,\xi_k,\qquad Y_0=1.
$$

Write $a=1-2h$. Independence gives

$$
m_{k+1}=am_k,\quad v_{k+1}=a^2v_k+9h,\quad
m_k=a^k,\quad v_k=9h\sum_{j=0}^{k-1}a^{2j}.
$$

A finite stationary variance exists exactly when $|a|<1$, hence

$$
0<h<1,\qquad
v_h=\frac{9h}{1-(1-2h)^2}=\frac{9}{4(1-h)}.
$$

The stationary distribution is $N(0,v_h)$ because a stationary process can be constructed as a square-summable series of independent Gaussian innovations. The difference between two solutions with the same noise increments is $a^k(Y_0-\widetilde Y_0)$, which decays in this interval.

Here, stability means decay of initial differences and a bounded second moment; because of the additive noise, the process itself does not converge to zero. Section 6.1 of the original paper by Giles and colleagues gives the formula for a noise coefficient of $\sqrt2$; multiplying the variance by $9/2$ makes it agree with our derivation. [Paper](https://link.springer.com/article/10.1007/s11222-019-09890-0).

If $|a|\ge1$, no stationary probability distribution exists. Its characteristic function would have to satisfy

$$
|\varphi(t)|\le \exp\left[-\frac{9h\,t^2}{2}\sum_{j=0}^{k-1}a^{2j}\right]
$$

for every k. The sum diverges, so $\varphi(t)=0$ for every $t\ne0$, contradicting continuity at zero. At the boundary $h=1$, we have $a=-1$ and $v_k=9k$; unit modulus does not provide stability.

##### Executed numerical check

The check iterated the moment recurrences and compared them with the finite geometric sum; no Monte Carlo simulation was used.

| Model | Time | Mean | Variance |
|---|---:|---:|---:|
| Exact, $t=1$ | 1 | 0.1353352832 | 2.2087898125 |
| Euler, $h=0.25,\ k=4$ | 1 | 0.0625 | 2.98828125 |
| Exact limiting distribution | $t\to\infty$ | 0 | 2.25 |
| Euler, $h=0.25$, limit | $k\to\infty$ | 0 | 3 |
| Euler, $h=1.2,\ k=10$ | 12 | 28.9254654976 | 9401.4287353445 |
| Euler, $h=1.2,\ k=100$ | 120 | $4.10018609\cdot10^{14}$ | $1.89129667\cdot10^{30}$ |

At $h=1.2$, $a=-1.4$, so

$$
m_k=(-1.4)^k,\qquad
v_k=\frac{10.8}{0.96}(1.96^k-1).
$$

Meanwhile, the continuous model's variance approaches 2.25.

##### Two mechanisms transferred from other fields

The covariance equilibrium equation of a digital linear filter, $v=a^2v+q$, gives the same discrete variance. We tested this transfer using the moment recurrence for up to 100 steps; it provides a short, directly checkable stability test.

The second transfer matches noise strength to the desired equilibrium variance. Replacing $9h$ with $\frac94(1-a^2)$ gives the correct stationary variance within the stable interval. At $h=0.25$, the new innovation variance is 1.6875. However, the lag-one correlation remains 0.5, while for the exact process it is $e^{-0.5}=0.6065306597$. This correction fixes the equilibrium variance but does not reproduce the exact time dynamics.

An exact step is available for this linear process:

$$
X_{(k+1)h}=e^{-2h}X_{kh}
+\frac32\sqrt{1-e^{-4h}}\,\xi_k.
$$

It follows from the Itô integral already derived and preserves both the transition distribution and the stationary variance for any $h>0$. Its coefficients were checked numerically here; no simulation of random trajectories was performed.

The next comparison of methods should also check autocorrelation: equal stationary variance alone does not establish correct time dynamics.


*Executed calculation files:* [calculation-output.json](validation/2026-11-09-beta3/calculations/NF02/calculation-output.json) · [calculation.py](validation/2026-11-09-beta3/calculations/NF02/calculation.py)

*Research provenance: NF02; 5 queries; EN / DE / ZH / JA. Original answer SHA-256: `4671d84891be30d7d6d4967f0cf4134d5126f897ca2c06e65743e9e0332b248e`.*

<a id="final30-nf03"></a>

#### NF03 — Transient growth of a nonnormal matrix

**Original question and required conditions**

B = [[-1,20],[0,-1]]. All eigenvalues are negative; does it follow that ||exp(tB)||₂ ≤ 1 for all t ≥ 0? Derive the matrix exponential, the exact spectral norm and the time/value of its maximum. Distinguish asymptotic stability from transient amplification.

*Test conditions:* A proof, an executed numerical check and a primary source on the transient behaviour of nonnormal operators are required. Do not obtain the norm's maximum solely from a coarse numerical grid.

##### Researched answer

For the given matrix, $\|\exp(tB)\|_2$ initially grows above 1. The maximum norm is approximately $7.3760289344$, attained at $t_*=\sqrt{99}/10\approx0.9949874371$.

##### Matrix exponential and exact norm

Write $B=-I+N$, where

$$
N=\begin{pmatrix}0&20\\0&0\end{pmatrix},\qquad N^2=0.
$$

Since $I$ commutes with $N$,

$$
E(t)=e^{tB}=e^{-t}(I+tN)
=e^{-t}\begin{pmatrix}1&20t\\0&1\end{pmatrix}.
$$

Both eigenvalues of B are $-1$, but $BB^\top\ne B^\top B$, so the matrix is nonnormal.

Write $a=20t\ge0$. Then

$$
\begin{pmatrix}1&a\\0&1\end{pmatrix}^{\!\top}
\begin{pmatrix}1&a\\0&1\end{pmatrix}
=\begin{pmatrix}1&a\\a&a^2+1\end{pmatrix}
$$

with characteristic polynomial

$$
\lambda^2-(a^2+2)\lambda+1.
$$

The largest eigenvalue is

$$
\lambda_+=\frac{a^2+2+a\sqrt{a^2+4}}2
=\left(\frac{\sqrt{a^2+4}+a}{2}\right)^2.
$$

Therefore

$$
F(t):=\|E(t)\|_2
=e^{-t}\left(\sqrt{1+100t^2}+10t\right).
$$

This formula holds for every $t\ge0$.

##### Global maximum

Using $\log(\sqrt{1+y^2}+y)=\operatorname{arsinh}y$,

$$
\frac d{dt}\log F(t)
=-1+\frac{10}{\sqrt{1+100t^2}}.
$$

The derivative is positive for $0\le t<t_*$, zero at $t_*$, and negative for $t>t_*$, where

$$
1+100t_*^2=100,\qquad t_*=\frac{\sqrt{99}}{10}.
$$

Since $F(0)=1$ and $F(t)\to0$ as $t\to\infty$, this is the unique global maximum:

$$
\boxed{\max_{t\ge0}\|e^{tB}\|_2
=e^{-\sqrt{99}/10}(10+\sqrt{99})
=7.376028934374846\ldots}
$$


The numerical check compared the formula with a direct singular-value calculation at seven times and at the maximum point. At $t=0.01$, the norm is already 1.0939927522; at $t=10$, it is 0.00908021295. At the maximum, the unit initial vector found by SVD, approximately $(0.0500627751,\ 0.9987460731)$, reaches a norm of 7.3760289344. The time of the maximum was obtained analytically, not from a grid.

##### Exactly what stability means

For every initial vector $z_0$,

$$
z(t)=e^{tB}z_0\longrightarrow0,
$$

because $e^{-t}$ and $te^{-t}$ tend to zero. The equilibrium is asymptotically stable. At the same time, some initial vectors grow substantially before decaying.

This distinction between eigenvalue-determined asymptotics and the transient amplification of a nonnormal operator is studied in the original paper by Trefethen, Trefethen, Reddy and Driscoll. Our particular result of $7.376$ comes from the derivation above; it is not a number taken from the paper. [Copy available from the author](https://people.maths.ox.ac.uk/trefethen/publication/PDF/1993_57.pdf).

The initial direction maximising the operator norm at each time may change; the norm curve itself is not the trajectory of a single fixed initial vector.

##### Two tested mechanisms

The energy method from flow stability can serve as a quick local check:

$$
\frac d{dt}\|z\|_2^2=z^\top(B+B^\top)z,\qquad
\frac{B+B^\top}{2}=\begin{pmatrix}-1&10\\10&-1\end{pmatrix}.
$$

The eigenvalues of the symmetric part are $9$ and $-11$. For $z_0=(1,1)/\sqrt2$, the initial derivative of the squared norm is 18, so growth is indeed possible. This test establishes initial growth, not the value of its global maximum.

The second mechanism is weighted quadratic energy from control theory. We checked exactly that

$$
P=\begin{pmatrix}1/2&5\\5&201/2\end{pmatrix}>0,\quad
\det P=101/4,\quad B^\top P+PB=-I.
$$

Therefore $V(z)=z^\top Pz$ satisfies $V'=-\|z\|_2^2<0$ along a nonzero trajectory. The weighted norm decreases, but this statement does not alter the Euclidean-norm growth already calculated. We reject the hypothesis that finding a suitable energy would guarantee contraction specifically in the problem's given 2-norm.

The next useful test would assess the sensitivity of maximum amplification to the off-diagonal coefficient and rounding errors. The coefficient tested here is specifically 20.


*Executed calculation files:* [calculation-output.json](validation/2026-11-09-beta3/calculations/NF03/calculation-output.json) · [calculation.py](validation/2026-11-09-beta3/calculations/NF03/calculation.py)

*Research provenance: NF03; 5 queries; EN / DE / ZH / JA. Original answer SHA-256: `f28774c7a009d8b8162ade6f47f7831c5b86cecf29cb332d65b03d314140f1d4`.*

<a id="final30-nf04"></a>

#### NF04 — Duality without a finite multiplier

**Original question and required conditions**

Solve min_x x subject to x² ≤ 0. Derive the Lagrange dual problem, the primal and dual optimal values, attainment and the KKT conditions. Then repeat for x² ≤ ε² with ε > 0 and analyse ε → 0. Does a zero duality gap alone guarantee a finite optimal multiplier?

*Test conditions:* A formal derivation, an executed numerical cross-check for several ε values, and a source are required. Do not use Slater's condition when it is not satisfied.

##### Researched answer

A zero duality gap alone does not guarantee a finite optimal Lagrange multiplier. In this problem, the primal minimum is attained and equals 0; the dual supremum is also 0, but no finite $\lambda$ attains it.

##### The constraint $x^2\le0$

The only feasible point is $x^*=0$, so $p^*=0$. The Lagrangian is

$$
L(x,\lambda)=x+\lambda x^2,\qquad \lambda\ge0.
$$

For $\lambda>0$, completing the square gives

$$
L=\lambda\left(x+\frac1{2\lambda}\right)^2-\frac1{4\lambda},
\qquad g(\lambda)=\inf_xL=-\frac1{4\lambda}.
$$

For $\lambda=0$, $\inf_xx=-\infty$. Thus the dual problem is

$$
\sup_{\lambda\ge0}g(\lambda)
=\sup_{\lambda>0}\left(-\frac1{4\lambda}\right)=0.
$$

For every finite $\lambda>0$, $g(\lambda)<0$; the value 0 is approached only as $\lambda\to\infty$. Hence $p^*-d^*=0$, but there is no dual optimiser.

The KKT conditions would be

$$
x^2\le0,\quad \lambda\ge0,\quad \lambda x^2=0,\quad
1+2\lambda x=0.
$$

At the only feasible point $x=0$, the last condition becomes $1=0$. There is therefore no finite KKT pair. Necessity of KKT cannot be obtained from Slater's condition here, because no strictly feasible point $x^2<0$ exists.

Bertsekas's original MIT course lecture materials show this exact counterexample and its dual function. [Lecture 18](https://ocw.mit.edu/courses/6-252j-nonlinear-programming-spring-2003/c7aa97e88ae57f07d03679055aa3502a_6252_slides18.pdf).

##### The constraint $x^2\le\varepsilon^2,\ \varepsilon>0$

The feasible set is $[-\varepsilon,\varepsilon]$, and

$$
x^*_\varepsilon=-\varepsilon,\qquad p^*_\varepsilon=-\varepsilon.
$$

Now

$$
L_\varepsilon(x,\lambda)=x+\lambda(x^2-\varepsilon^2),\qquad
g_\varepsilon(\lambda)=-\frac1{4\lambda}-\lambda\varepsilon^2
\quad(\lambda>0),
$$

while $g_\varepsilon(0)=-\infty$. From

$$
g_\varepsilon'(\lambda)=\frac1{4\lambda^2}-\varepsilon^2=0,\qquad
g_\varepsilon''(\lambda)=-\frac1{2\lambda^3}<0
$$

we obtain the unique dual optimiser

$$
\lambda^*_\varepsilon=\frac1{2\varepsilon},\qquad
d^*_\varepsilon=g_\varepsilon(\lambda^*_\varepsilon)=-\varepsilon.
$$

The dual function tends to $-\infty$ at both ends of the open domain, so this is an attained global maximum. The primal minimum is also attained.

All four KKT conditions are satisfied:

$$
x_\varepsilon^{*2}-\varepsilon^2=0,\quad
\lambda^*_\varepsilon>0,\quad
\lambda^*_\varepsilon(x_\varepsilon^{*2}-\varepsilon^2)=0,\quad
1+2\lambda^*_\varepsilon x^*_\varepsilon=0.
$$

This time $x=0$ is strictly feasible, since $-\varepsilon^2<0$. Slater's condition applies for positive $\varepsilon$; the solution has also already been obtained by direct calculation.

##### The limit and exact arithmetic

As $\varepsilon\downarrow0$,

$$
x^*_\varepsilon\to0,\quad p^*_\varepsilon=d^*_\varepsilon\to0,
\quad \lambda^*_\varepsilon\to+\infty.
$$

The limits of the primal points and optimal values exist, but there is no finite limit of the dual optimisers.

| $\varepsilon$ | $x^*$ | $\lambda^*$ | $p^*=d^*$ |
|---:|---:|---:|---:|
| 1 | −1 | 1/2 | −1 |
| 1/10 | −1/10 | 5 | −1/10 |
| 1/100 | −1/100 | 50 | −1/100 |
| 1/1 000 000 | −1/1 000 000 | 500 000 | −1/1 000 000 |

All rows and KKT residuals were checked using exact rational numbers. For $\varepsilon=0$ and $\lambda=1,10,100,10^6$, the dual values are $-1/4,-1/40,-1/400,-1/4\,000\,000$: none is zero.

##### Two tests of transfers from other fields

We apply the economic-sensitivity or shadow-price interpretation to the actual right-hand-side constraint parameter $b=\varepsilon^2$:

$$
p(b)=-\sqrt b,\qquad p'(b)=-\frac1{2\sqrt b}=-\lambda^*.
$$

At $b=0$, there is no finite right-hand slope. If a finite subgradient $s$ existed there, we would need $-\sqrt b\ge sb$ for all $b>0$, hence $s\le-1/\sqrt b$ for every small b, which is impossible. This gives a geometric explanation of multiplier nonattainment. The derivative with respect to $\varepsilon$ itself is −1; the parameters must not be confused when interpreting the multiplier.

The second test uses dimensionless scaling $x=\varepsilon y$. For $\varepsilon>0$, we obtain $\min \varepsilon y$, $y^2\le1$, with multiplier $\mu^*=\varepsilon/2$. It is finite, but the original multiplier is

$$
\lambda^*=\mu^*/\varepsilon^2=1/(2\varepsilon).
$$

The exact calculation confirmed both relationships for every table row. At $\varepsilon=0$, the substitution is no longer invertible, so scaling does not resolve the degeneracy of the original formulation.

The next test is to examine the equivalent feasible-set formulation $x=0$ and distinguish its finite equality multiplier from the multiplier of the original $x^2\le0$ constraint. This was not executed in the present batch of calculations.


*Executed calculation files:* [calculation-output.json](validation/2026-11-09-beta3/calculations/NF04/calculation-output.json) · [calculation.py](validation/2026-11-09-beta3/calculations/NF04/calculation.py)

*Research provenance: NF04; 5 queries; EN / DE / ZH / JA. Original answer SHA-256: `6a4a886a11fbc2830b79b0df53d94d265f43a12327cfd75bbfa6f090f9d3ca20`.*

<a id="final30-nf05"></a>

#### NF05 — Mass concentration and passage to the limit

**Original question and required conditions**

On [0,1], take f_n(x) = n·1_(0,1/n)(x). Determine the pointwise/almost-everywhere limit, L¹ convergence and the weak limit of the measures f_n(x)dx. Prove the answers and state precisely why the limit cannot simply be moved inside the integral. Relate this to uniform integrability.

*Test conditions:* A proof using an arbitrary continuous test function and an executed numerical control example are required. Do not claim that this sequence proves the failure of all numerical integrators.

##### Researched answer

$f_n\to0$ at every point and almost everywhere, but there is no $L^1$ convergence. The measures $\mu_n=f_n(x)\,dx$ on the closed interval $[0,1]$ converge weakly to the Dirac measure $\delta_0$.

##### Pointwise and $L^1$ behaviour

At $x=0$, $f_n(0)=0$ for every n because the indicator's interval is open. For a fixed $x>0$, choosing $n>1/x$ also gives $f_n(x)=0$. The limit is therefore zero at every point of $[0,1]$.

However,

$$
\int_0^1f_n(x)\,dx=n\frac1n=1,\qquad
\|f_n-0\|_1=1
$$

for every n. The sequence does not converge to zero in $L^1$. It also does not converge in $L^1$ to any other function: for $m\ge n$,

$$
\|f_m-f_n\|_1
=(m-n)\frac1m+n\left(\frac1n-\frac1m\right)
=2\left(1-\frac nm\right).
$$

Setting $m=2n$ gives a distance of 1, so the sequence is not Cauchy in $L^1$.

##### Weak limit of the measures

Take an arbitrary $\varphi\in C([0,1])$. Then

$$
\int_{[0,1]}\varphi\,d\mu_n
=n\int_0^{1/n}\varphi(x)\,dx
=\int_0^1\varphi(y/n)\,dy.
$$

Using the modulus of continuity at zero,

$$
\left|\int\varphi\,d\mu_n-\varphi(0)\right|
\le\sup_{0\le x\le1/n}|\varphi(x)-\varphi(0)|
\longrightarrow0.
$$

Since $\int\varphi\,d\delta_0=\varphi(0)$, we obtain $\mu_n\Rightarrow\delta_0$. The proof applies to every continuous test function, not just a few moments.

The Dirac measure has mass 1 at the point 0; it cannot be written as an $L^1$ density with respect to Lebesgue measure because the integral of such a density over a singleton would be 0. Weak convergence of measures is therefore not $L^1$ convergence of this density sequence. The interval matters: on $(0,1)$, testing only against compactly supported continuous functions would give the vague limit 0, because their support is away from zero.

Rowell's MIT signal-processing lecture shows the connection with unit-area impulses. Here we interpret its impulse notation as the measure limit proved above; the pointwise limit remains zero. [Lecture](https://ocw.mit.edu/courses/2-161-signal-processing-continuous-and-discrete-fall-2008/a6d15b07b9720f44e4bc2e9da4d3a5a2_lecture_01.pdf).

##### Why the integral and limit cannot be interchanged

Here,

$$
\int\lim_nf_n=0,\qquad \lim_n\int f_n=1.
$$

The hypothesis of the dominated convergence theorem is not satisfied: no integrable $g$ dominates all $f_n$ almost everywhere. Otherwise,

$$
\int_0^{1/n}|g(x)|\,dx\ge1
$$

for every n, although absolute continuity of the integral of an integrable function requires these integrals to tend to 0. Such an integrable dominating function therefore cannot exist.

Uniform integrability is also absent. For each finite $K>0$, choosing $n>K$ gives

$$
\int_{\{|f_n|>K\}}|f_n|\,dx=1.
$$

The supremum of these integrals over n is therefore 1 for every K and does not tend to zero. Equivalently, the measure of the sets $A_n=(0,1/n)$ tends to 0, but $\int_{A_n}f_n=1$.

The uniform-integrability criterion and its connection with $L^1$ convergence for almost-everywhere convergent sequences are given in the statements and proofs of lemmas 3.6 and 3.7 at Ulm University. Definition 6.11 in the Chinese primary-source course gives the same tail criterion. [Ulm](https://www.mathematik.uni-ulm.de/stochastik/lehre/ss05/wt/skript/node41.html), [Peking University](https://math.pku.edu.cn/teachers/lidf/course/stochproc/stochprocnotes/html/_book/martingale.html).

The monotone convergence theorem is also inapplicable: the sequence is not pointwise monotonically increasing. Fatou's lemma remains valid and gives $0\le1$, not equality.

##### Executed cross-checks

| n | $\int f_n$ | $\int xf_n$ | $\int x^2f_n$ | $\int e^xf_n$ |
|---:|---:|---:|---:|---:|
| 10 | 1 | 1/20 | 1/300 | 1.0517091808 |
| 100 | 1 | 1/200 | 1/30000 | 1.0050167084 |
| 1000 | 1 | 1/2000 | 1/3000000 | 1.0005001667 |
| 1 000 000 | 1 | 1/2 000 000 | 1/3 000 000 000 000 | 1.0000005000 |

The respective formulas are $1,\ 1/(2n),\ 1/(3n^2),\ n(e^{1/n}-1)$; the last uses a numerically stable expm1 calculation. The table illustrates the limit but does not replace the proof for an arbitrary test function.

##### Two mechanisms transferred from other fields

The unit-impulse idea from signal processing provides the correct object for the mass that is preserved. The full test-function proof and calculated moments confirm this. We reject the hypothesis that the function itself becomes a Dirac density pointwise: the Dirac measure has no such density.

The second transfer adapts integration to the concentration scale. At $n=1000$, the ordinary midpoint sum with 100 equal subintervals gave 0 because its first point, 0.005, already lies outside the impulse's support $(0,0.001)$. After the substitution $x=y/n$, the same 100 midpoints give a mass of 1; for the test function $e^x$, the absolute error was $4.17\cdot10^{-12}$.

This is an example involving a particular fixed-grid formula. It does not prove the failure of all numerical integrators. The next test would also compare adaptive integration with unknown support and an explicitly defined error budget; that test has not been performed.


*Executed calculation files:* [calculation-output.json](validation/2026-11-09-beta3/calculations/NF05/calculation-output.json) · [calculation.py](validation/2026-11-09-beta3/calculations/NF05/calculation.py)

*Research provenance: NF05; 5 queries; EN / DE / ZH / JA. Original answer SHA-256: `a523076932500c82b629e80bfe43112b67b2dcb748d03dda97373662a58b7ca8`.*

<a id="final30-nf06"></a>

#### NF06 — The Strang scheme and oscillator energy

**Original question and required conditions**

For a harmonic oscillator, take A = [[0,1],[0,0]], B = [[0,0],[-1,0]] and the Strang step M_h = exp(hA/2)exp(hB)exp(hA/2). Derive M_h, determine the step sizes for which its powers are bounded, and examine h = 2 separately. Find a preserved positive-definite quadratic form in the stable interval. Compare with the explicit Euler method.

*Test conditions:* h > 0. An algebraic proof, an executed experiment over a larger number of steps, and a primary source are required. Unit-modulus eigenvalues alone are insufficient at the boundary case.

##### Researched answer

**The matrix powers are bounded exactly for $0<h<2$.** At $h=2$ they grow linearly; for $h>2$, exponentially. Within the stable interval, the step preserves the positive-definite form

$$
E_h(x,v)=\tfrac12\bigl(x^2+(1-h^2/4)v^2\bigr).
$$

The explicit Euler method is unstable for this undamped oscillator at every fixed $h>0$.

##### Matrix and algebraic stability proof

Since $A^2=B^2=0$, both exponential series terminate after the first-order term. Multiplying in the order specified in the problem,

$$
M_h=
\begin{pmatrix}1&h/2\\0&1\end{pmatrix}
\begin{pmatrix}1&0\\-h&1\end{pmatrix}
\begin{pmatrix}1&h/2\\0&1\end{pmatrix}
=
\begin{pmatrix}
1-h^2/2 & h-h^3/4\\
-h & 1-h^2/2
\end{pmatrix}.
$$

Write $a=1-h^2/2$, $c=1-h^2/4$. Then $a^2+h^2c=1$, $\det M_h=1$ and

$$
\chi_{M_h}(\lambda)=\lambda^2-2a\lambda+1.
$$


If $0<h<2$, then $c>0$, and

$$
P_h=\operatorname{diag}(1,c)>0,\qquad
M_h^\mathsf TP_hM_h=P_h.
$$

The identity follows by multiplying the matrices directly and using $a^2+h^2c=1$; it was also checked symbolically in the saved code. Therefore $E_h(M_hz)=E_h(z)$, and for all integers $k\ge0$,

$$
c\|M_h^kz\|_2^2
 \le (M_h^kz)^\mathsf TP_h(M_h^kz)
 =z^\mathsf TP_hz
 \le\|z\|_2^2.
$$

Thus

$$
\boxed{\|M_h^k\|_2\le(1-h^2/4)^{-1/2}\quad(k\ge0).}
$$

The bound applies to each fixed $h<2$; its constant is not uniform on approach to $h=2$.

More directly, $D=P_h^{1/2}$ gives

$$
DM_hD^{-1}=
\begin{pmatrix}a&h\sqrt c\\-h\sqrt c&a\end{pmatrix},
$$

which is an orthogonal rotation matrix. Its eigenvalues are $a\pm ih\sqrt c$, both with modulus 1. The rescaled coordinates explain why an ellipse is preserved while the ordinary energy $H=(x^2+v^2)/2$ can fluctuate.

Structure preservation and analysis of modified dynamics are also the subject of the original publication by Hairer, Lubich and Wanner. In this work, its abstract was read directly; the particular matrix and exact form above were derived independently.

##### Boundary case $h=2$

Here,

$$
M_2=\begin{pmatrix}-1&0\\-2&-1\end{pmatrix}=-I+N,
\qquad N=\begin{pmatrix}0&0\\-2&0\end{pmatrix},\quad N^2=0,\ N\ne0.
$$

The binomial formula gives

$$
\boxed{M_2^k=(-1)^k
\begin{pmatrix}1&0\\2k&1\end{pmatrix}.}
$$

For example, $\|M_2^k(1,0)^\mathsf T\|_2=\sqrt{1+4k^2}\to\infty$, and the exact operator norm is

$$
\|M_2^k\|_2=k+\sqrt{k^2+1}.
$$

Both eigenvalues are $-1$, but the matrix is not diagonalisable. The initial vector $(0,1)^\mathsf T$ does remain bounded; this does not make the matrix powers bounded as operators. At this step size, $P_h$ becomes only positive semidefinite. No other preserved positive-definite form can exist, because it would provide a contradictory proof of boundedness.

An analogue in digital-system analysis is a repeated uncancelled pole on the unit circle: it can produce a growing term. Section 2.4 of ADI's original teaching material explicitly separates this exception. Here we are checking powers of an autonomous matrix, so we do not equate this criterion with BIBO stability of a forced system.

If $h>2$, then $a<-1$, and the eigenvalues

$$
\lambda_\pm=a\pm h\sqrt{h^2/4-1}
$$

are real, reciprocal, and satisfy $\lambda_-<-1$. The trajectory of the corresponding eigenvector grows exponentially. Together with the boundary case, this proves the statement “exactly $0<h<2$”.

##### Euler method


$$
F_h=I+h(A+B)=
\begin{pmatrix}1&h\\-h&1\end{pmatrix},\qquad
F_h^\mathsf TF_h=(1+h^2)I.
$$

Since $F_h/\sqrt{1+h^2}$ is orthogonal,

$$
\boxed{\|F_h^k\|_2=(1+h^2)^{k/2}},\qquad
H(F_h^kz)=(1+h^2)^kH(z).
$$

This proves unbounded growth for all $h>0$ and every nonzero initial vector. Equations 14–15 in Pastewka's own course give the same energy growth; the Verlet variant covered in that course uses a different half-step order, so I do not transfer its energy form to our matrix.

##### Executed long-term experiment

The code first checked the matrix identities exactly with SymPy, then used NumPy to multiply the step matrix successively. For stable step sizes, 10 000 actual iterations were performed, calculating the operator norm and invariant defect at each one.

| $h$ | Steps | Largest observed $\|M_h^k\|_2$ | Proven bound | Largest $\|(M_h^k)^\mathsf TP_hM_h^k-P_h\|_2$ |
|---:|---:|---:|---:|---:|
| 0.1 | 10 000 | 1.001252349 | 1.001252349 | $7.26\cdot10^{-14}$ |
| 1 | 10 000 | 1.132782219 | 1.154700538 | 0 |
| 1.9 | 10 000 | 3.202563052 | 3.202563076 | $1.44\cdot10^{-12}$ |
| 1.999 | 10 000 | 31.626730169 | 31.626730190 | $2.05\cdot10^{-12}$ |

In the boundary case, 10 000 iterations gave exactly $\bigl(\begin{smallmatrix}1&0\\20000&1\end{smallmatrix}\bigr)$, while the norm is approximately 20 000.00005. At $h=2.1$, after 1000 steps the norm was $5.972479742\cdot10^{273}$. At $h=0.1$, Euler's method gave $4.044537936\cdot10^{21}$ after 10 000 steps, with a relative difference from the closed formula of $3.78\cdot10^{-15}$.

The numerical data confirm the particular implementation; the statement for all step counts rests on the algebraic proof. Preservation also does not imply an exact phase: the Strang rotation angle is $\theta=\arccos(1-h^2/2)$, while the exact solution's angle is $h$. At $h=0.1$, after 10 000 steps the accumulated angle difference, without reducing it modulo full revolutions, is $10000(\theta-h)=0.4171361154$ radians.

##### The two tested transfers and the next test

**H1 — A stored-energy certificate from passive-system analysis.** We sought a positive weight matrix that makes the discretised step an isometry. The resulting $P_h$, the symbolic identity and the long-term calculation support the hypothesis exactly for $0<h<2$. It does not guarantee exact preservation of the original energy or the correct phase.

**H2 — Extending the unit-circle condition of a digital resonator to the entire closed interval.** We checked whether eigenvalues of modulus 1 allow $h=2$ to be included. The exact Jordan formula and the 10 000-step test reject this extension. The query used outside the integration field was “lossless digital oscillator repeated pole unit circle stability Jordan block”.

Diagnosis: the critical point is the loss of positivity of the preserved form at the boundary; stability and phase accuracy are also different criteria. The next useful test is periodic alternation between two different, individually stable step sizes: each has a different $P_h$, so joint boundedness cannot be inferred automatically. This next test was not executed in this work.

Searches were performed in EN/DE/ZH/JA; 6 queries and 5 web calls with 7 opening attempts were executed. Failed responses from Geneva and alternative full-text sources were preserved. Four verification perspectives from one agent were used; they are not independent instances.

Primary sources: [Hairer, Lubich, Wanner (2003), abstract](https://www.cambridge.org/core/journals/acta-numerica/article/abs/geometric-numerical-integration-illustrated-by-the-stormerverlet-method/E55395D5DD7A4E0526D10EA74DA6C46B), [ADI, Chapter 2](https://www.adi.com/resource-library/dynamics-of-real-time-simulation-chapter-2/), [Pastewka, Euler-Integration](https://pastewka.github.io/Differentialgleichungen/lecture/chapter11.html).


*Executed calculation files:* [calculation-output.json](validation/2026-11-09-beta3/calculations/NF06/calculation-output.json) · [calculation.py](validation/2026-11-09-beta3/calculations/NF06/calculation.py)

*Research provenance: NF06; 6 queries; EN / DE / ZH / JA. Original answer SHA-256: `0482bf41d61c75dd8a560388ec7e5ef0eb4b087bcb653dafaf6ad414e6d350c2`.*

<a id="final30-nf07"></a>

#### NF07 — The Galois group of a quintic polynomial

**Original question and required conditions**

Determine the Galois group of f(x) = x^5-x-1 over Q and whether its roots can be expressed by radicals. Use exact factorisation modulo 2 and modulo 3, explaining why the corresponding cycle types determine the group. Check the discriminant and the hypotheses of every theorem used.

*Test conditions:* A complete argument, executed exact polynomial arithmetic and primary mathematical sources are required. A CAS group name alone is not a proof.

##### Researched answer

$$
\boxed{\operatorname{Gal}(x^5-x-1\,/\,\mathbb Q)\cong S_5.}
$$

**None of this polynomial's roots can be expressed by radicals over $\mathbb Q$.** The proof uses exact factorisation modulo 2 and 3, the theorems' hypotheses, and executed arithmetic certificates.

##### Discriminant and good primes

Let $f=x^5-x-1$, $g=f'=5x^4-1$. The polynomial is monic, so

$$
\operatorname{disc}(f)=(-1)^{5\cdot4/2}\operatorname{Res}(f,g)
=\operatorname{Res}(f,g).
$$

Using $f=(x/5)g-4x/5-1$, symmetry of the resultant and the remainder formula,

$$
\begin{aligned}
\operatorname{Res}(f,g)
&=\operatorname{Res}(g,f)\\
&=5^4\operatorname{Res}(g,-4x/5-1)\\
&=4^4g(-5/4)=5^5-4^4\\
&=\boxed{2869=19\cdot151}.
\end{aligned}
$$

The sign is positive. Resultant formulas for a monic polynomial and its derivative are presented in Milne's Propositions 4.35–4.36; all coefficients here are exact rational numbers.

Thus $f$ is separable. Also, $2869\equiv1\pmod2$ and $\pmod3$, so the reductions for both selected primes have no repeated roots. The code separately checked $\gcd(\bar f,\bar f')=1$ in both fields and calculated the discriminant as the exact determinant of the $9\times9$ Sylvester matrix.

##### Exact factorisations

###### Modulo 2


$$
\bar f=x^5+x+1=(x^2+x+1)(x^3+x^2+1)
\quad\text{in }\mathbb F_2[x].
$$

Both factors have value 1 at 0 and 1. A polynomial of degree two or three over a field is reducible exactly when it has a root in that field. Both factors are therefore irreducible; they are distinct and each occurs once.

###### Modulo 3


$$
\bar f=x^5+2x+2.
$$

The values at $0,1,2$ are all 2, so there are no linear factors. All monic irreducible quadratic polynomials over $\mathbb F_3$ and the division remainders are:

| Divisor | Remainder of $f$ modulo the divisor and 3 |
|---|---|
| $x^2+1$ | $-1$ |
| $x^2+x+2$ | $x-1$ |
| $x^2+2x+2$ | $x-1$ |

The list's completeness is checked by examining the nine polynomials $x^2+bx+c$, $b,c\in\mathbb F_3$: exactly these three have no root. None divides $f$.

If a degree-five polynomial were reducible, its irreducible factorisation would contain at least one factor of degree 1 or 2; two degrees both at least 3 would already exceed 5. Therefore

$$
\boxed{x^5+2x+2\text{ is irreducible over }\mathbb F_3.}
$$


This also supplies an exact justification for the factorisation printed by the CAS, rather than relying on the CAS conclusion. An additional check constructed a Bézout identity in $\mathbb F_3[x]$:

$$
u f+v(x^9-x)=1,
$$

where

$$
\begin{aligned}
u&=x^8+x^7+x^6+x^5-x^4-x^3-x^2-x-1,\\
v&=-x^4-x^3-x^2-x-1.
\end{aligned}
$$

This again confirms the absence of factors whose degree divides 2.

Since $f\in\mathbb Z[x]$ is monic and primitive, Gauss's lemma would allow any nontrivial factorisation over $\mathbb Q$ to be written as a product of monic factors with integer coefficients. Reduction modulo 3 would preserve both factors' positive degrees, giving a contradiction. Thus $f$ is also irreducible over $\mathbb Q$. Slides 22–24 of Mascot's own lecture discuss this particular example, its discriminant and both modular factorisations; their arithmetic was executed afresh in this work.

##### From cycle types to $S_5$

Let $K$ be the splitting field of $f$ over $\mathbb Q$. It is a finite, normal and separable extension. Its automorphisms faithfully permute the five distinct roots, so $G=\operatorname{Gal}(K/\mathbb Q)\le S_5$. Irreducibility also implies transitivity.

Dedekind's cycle-type theorem applies to a monic polynomial with integer coefficients and a prime not dividing its discriminant. The degrees of the distinct irreducible factors of the reduction then give the lengths of the disjoint cycles of an element of $G$. All these hypotheses were checked above; the claim is not that the entire Galois group is the cyclic group of the reduction.

Thus the factorisation modulo 2 gives

$$
\sigma=(ab)(cde)\in G,
\qquad \tau=\sigma^3=(ab)\in G,
$$

while irreducibility modulo 3 gives a 5-cycle $\gamma\in G$.

It remains to prove why, in this situation, $\gamma$ and $\tau$ generate $S_5$. Relabel the roots by $\mathbb Z/5\mathbb Z$ so that $\gamma(i)=i+1$. After a cyclic relabelling, $\tau=(0,d)$, where $d\ne0$. Then

$$
\gamma^k\tau\gamma^{-k}=(k,k+d)\in G.
$$

These transpositions are edges of a graph between vertices whose difference is $d$. Since 5 is prime, $d$ is invertible modulo 5 and the graph is connected.

The edge transpositions of a connected graph generate all transpositions: along a simple path $v_0,\ldots,v_m$, writing $t_j=(v_{j-1},v_j)$, we obtain

$$
(v_0,v_m)=t_1\cdots t_{m-1}t_m t_{m-1}\cdots t_1.
$$

All permutations are products of transpositions. Thus $G$ contains $S_5$, and since $G\le S_5$, we have $G=S_5$. The argument about a transitive group generated by transpositions is also explained in the first proof step of Conrad's own notes.

The primality of 5 is essential here. The statement “any $n$-cycle and any transposition generate $S_n$” is not a general theorem without additional conditions.

##### Why there is no expression by radicals

The Galois solvability theorem in characteristic 0 says that a polynomial is solvable by radicals exactly when its Galois group is solvable. The field $\mathbb Q$ has characteristic 0, and our polynomial is separable. Complex intermediate values and roots of unity are also allowed; prohibiting them is not the basis of this conclusion.

The group $S_5$ is not solvable. This can be checked here without a classification of groups: the conjugacy-class sizes of $A_5$ are $1,15,20,12,12$. They correspond to the identity, two disjoint transpositions, 3-cycles and the two classes of 5-cycles. The sizes come from centraliser orders $60,4,3,5,5$; all 60 elements were also examined exactly in the code.

A normal subgroup must be a union of conjugacy classes containing the identity, and by Lagrange's theorem its order must divide 60. Among the possible sums of class sizes, only 1 and 60 divide 60. Thus $A_5$ is simple. It is not abelian, so its commutator subgroup is a nontrivial normal subgroup and equals $A_5$. The derived series does not reach the identity. Since a subgroup of a solvable group is solvable, $S_5$ is also not solvable.

The conclusion applies even to each individual root. If one root lay in a finite radical extension, that extension could be embedded in a finite Galois extension with solvable group by adjoining the necessary roots of unity and conjugates. Normality and irreducibility of $f$ would place all roots of $f$ in it. Then $G$ would be a quotient of a solvable group, a contradiction. This construction of the extension is part of the proof of the theorem just stated.

##### Executed checks and two hypotheses

The saved code uses exact polynomial and integer arithmetic. It checked factor products, all nine quadratic candidates modulo 3, the Bézout identity, and the discriminant through two symbolic calculations and a separate determinant. No group-identification function was used.

**H1 — A graph-connectivity certificate for group generation.** The proof from edge transpositions covers every placement of the transposition relative to a 5-cycle. The code additionally checked all ten placements; each generated 120 elements. The hypothesis was confirmed for this problem. The query searched outside Galois theory was “connected graph edge transpositions generate symmetric group prime cycle”.

**H2 — Whether the discriminant is a square as a sufficient group identifier.** This feature is too weak. A nonsquare discriminant gives only $G\not\subseteq A_5$, not $G=S_5$. The code constructed the 20 affine permutations $x\mapsto ax+b$ on $\mathbb F_5$, $a\ne0$. This proper subgroup of $S_5$ is transitive, contains 5-cycles and odd permutations, but does not contain cycle type $(2)(3)$. The exact type counts were: identity 1, $(1)(2)(2)$ — 5, $(1)(4)$ — 10, $(5)$ — 4. The hypothesis that irreducibility and a nonsquare discriminant alone determine $S_5$ was therefore rejected. This affine group is not attributed to the given polynomial.

Diagnosis: the arithmetically decisive certificate is the pair of distinct factors of degrees 2 and 3, from which a transposition is obtained; the parity information from the discriminant alone cannot replace it. The approach does not need to change for this case. The next test of the transfer's limits would repeat cycle-and-transposition generation in a composite degree, such as 6, with different edge distances. That next test was not executed here, and no general improvement gain is claimed.

Searches were performed in EN/DE/ZH/JA; 5 queries, 5 web calls and 6 opens were executed. Internal checking used four perspectives from one agent.

Primary sources: [Milne, Fields and Galois Theory](https://www.jmilne.org/math/CourseNotes/FT.pdf), [Mascot, Galois theory, Chapter 3](https://www.maths.tcd.ie/~mascotn/teaching/2021/MAU34101/3%20GalPoly.pdf), [Conrad, The Galois Group of $x^n-x-1$](https://kconrad.math.uconn.edu/blurbs/gradnumthy/galoisselmerpoly.pdf).


*Executed calculation files:* [calculation-output.json](validation/2026-11-09-beta3/calculations/NF07/calculation-output.json) · [calculation.py](validation/2026-11-09-beta3/calculations/NF07/calculation.py)

*Research provenance: NF07; 5 queries; EN / DE / ZH / JA. Original answer SHA-256: `c9f59189d47f357533fb3bb00c5bdb27dee4054ac671143a59284690f5f9242d`.*


<a id="historical30"></a>

## Historical collection: all 30 answers

Test date: 9 November 2026.

This edition contains 10 everyday, 10 practical technical and 10 research questions. We prepared the questions for testing; these are not interviews with 30 people. Required user clarifications are clearly labelled as fictional test-scenario data. Web searches, source reading, answer writing and experience-preservation operations were actually executed.

Three separate executors worked on their own question groups. Each question involved searches in English, German, Chinese and Japanese. This does not mean that a useful, fully readable source was found in every language. Source gaps and pages that could not be opened are preserved in the test records.

The answers demonstrate use of the skill and its practical error checks. No controlled comparison was performed here to prove superiority over all other search engines or AI systems. Current prices, software versions and service capabilities must be checked again before use.

### What we changed after testing

Opening a source is now explicitly distinguished from reading the required passage. The search language is recorded separately from the language of the source content. Numerical recommendations are recalculated with the particular task's data, even when a specialist published the example. A new announcement is distinguished from independent verification and an accepted result.

Strict validation of evidence records was added to the execution connector. It refuses a completed run when required sources, claims, searches or editing records are missing. This check validates files and records; it does not itself prove that sentences are true. These 30 examples used the manual start/end cycle, while the new connector's checks were run separately.

### Results

147 queries were actually executed: EN 50, DE 33, ZH 33, JA 31. They include 143 distinct query texts and 4 repetitions after an interruption. The full results of E10's four initial tool calls had not been saved; during recovery, the sources were read again and the new calls saved. This gap is reported, not filled with invented records.

### Everyday questions

#### E01

My face gets kind of shiny and my makeup disappears after an hour. What should I buy?

##### Clarification needed

What is your skin type, and is there any irritation? What makeup do you use, and would you prefer to start with an application technique? What is your budget, and which country are you in?

##### SIMULATED answer in the test task

Adult; oily T-zone, normal cheeks, no irritation; everyday makeup; application technique first; EUR 30 in Latvia.

This is a simulation supplied by the person setting the task, not an actual confirmation from a user.

I would start with thinner layers of makeup and a small amount of mattifying powder on the T-zone. You do not need to spend the full €30 straight away.

1. Apply a small amount of your usual moisturizer and let it settle. Your skin should not feel noticeably slippery before you apply foundation. You can adjust the amount separately for your oily T-zone and normal cheeks. [KOSE](https://www.kose.co.jp/kose/make/make104.html) describes this approach.
2. Apply a thin layer of foundation; add another layer only where you need more coverage. This is a [technique described by the makeup artists interviewed](https://www.allure.com/story/how-to-make-makeup-last-all-day), and it is worth trying with the foundation you already have.
3. Lightly press a little translucent powder onto your forehead, nose, and chin. Your cheeks do not automatically need an equally thick layer. The [manufacturer's guidance](https://www.essence.eu/de-de/make-up-tips/how-to-setting-powder) also recommends adjusting the amount of powder to different areas of the face.
4. When shine appears, first press a tissue gently against your skin without rubbing. Then touch up the makeup and, if necessary, add a very small amount of powder. This is how [CBC television makeup artists](https://www.hicbc.com/magazine/article/?id=metone-makecolumndo813-260829) do touch-ups.

If you do not have powder, [essence All About Matt, 8 g](https://www.drogas.lv/lv/kosmetika/sejai/kompaktpuderi-puderi/essence-all-about-matt-fixing-kompaktais-puderis-8g/p/BP_225741) is one option for an inexpensive trial. The Drogas page that was opened lists €3.39; check the price and availability before buying. The same page also includes customer complaints that the mattifying effect does not last long. This information cannot predict the individual result on your skin.

My suggestion: try this sequence for one day and inspect the T-zone specifically after an hour. If your makeup still disappears, the next step will be to check the particular combination of moisturizer, sunscreen, and foundation.

#### E02

I am 1.80 m tall. What trousers would suit me?

##### Clarification needed

What silhouette and use do you have in mind, and are you looking for a cut or a specific size? Do you know your waist measurement and inseam length?

##### SIMULATED answer in the test task

Everyday wear; prefers a straight silhouette; needs a method for trying trousers on; waist and inseam have not been measured; no specific size requested.

This is a simulation supplied by the person setting the task, not an actual confirmation from a user.

I would start with straight-leg casual trousers and compare two cuts: a regular straight cut and one with slightly more room in the thighs. This is my suggestion for trying them on, based on your preference. A height of 1.80 m alone cannot determine the waist size or leg length you need, or which silhouette you will like. Manufacturers treat these measurements separately. [Levi's measuring guide](https://www.levi.com/GB/en_GB/blog/article/how-to-measure-jeans)

When trying them on, check the following:

- Fasten the waistband and sit down. It should still feel comfortable when you are seated; there should be no strong pulling across the thighs or crotch.
- Look from the front, side, and back. Check whether the fabric around the hips is noticeably stretched or hanging too loosely.
- Try the movements you need in everyday life. If possible, take a few steps too. The Japanese tailoring company's [Dankan fitting guidance](https://dankan.co.jp/blogs/dankan-magazine/jeans-size-guide) emphasizes comfort while moving, as well as when standing in front of a mirror.
- Judge the length with the shoes you will wear. For a clean, straight silhouette, I would initially compare a leg that just touches the shoe with a slightly shorter version. That is a matter of taste.

At home, find trousers whose length you already like. Lay them flat and measure the inside seam from the crotch to the hem. Measure the waistband flat and multiply that width by two. [Levi's](https://www.levi.com/GB/en_GB/blog/article/how-to-measure-jeans) describes this method.

When comparing size charts, check whether they show body measurements or measurements of the garment itself. They are not automatically the same, and even the same letter size can differ between cuts. [GU's explanation](https://faq-tw.gu-global.com/articles/zh_TW/Knowledge/000010565)

#### E03

Is 0.999… really 1? Explain without advanced mathematics.

Yes, in ordinary decimal notation, **0.999… is exactly 1**. The ellipsis means that the nines continue forever. The [Harvey Mudd College mathematician's explanation](https://math.hmc.edu/funfacts/why-does-0-999-1/) also stresses that one number can have two different representations.

A simple example uses thirds:

- Dividing 1 by 3 gives 0.333…; the threes do not end.
- Three thirds together equal 1.
- Multiplying 0.333… by 3 gives 0.999….

Both representations therefore describe the same quantity. This example is also used in a [University of Tokyo lesson for school students](https://www.ms.u-tokyo.ac.jp/video/open/2019jhschool-math/op2019-021.pdf).

The confusion arises because any **finite** string of nines really is less than 1:

| Representation | How far short of 1 it is |
|---|---:|
| 0.9 | 0.1 |
| 0.99 | 0.01 |
| 0.999 | 0.001 |

These are ordinary subtraction calculations. But 0.999… has no last nine after which some remaining difference could hide. However small a positive difference you imagine, a sufficiently long string of nines would already be closer to one than that.

The infinite notation denotes the number described by these increasingly accurate representations. That number is 1. It does not require waiting for someone to write every nine. The distinction between finite representations and the infinite decimal they denote is also explained in [Oliver Deiser's mathematics teaching text](https://www.aleph1.info/?call=Puc&permalink=ema12_3_1_Z6).

#### E04

Will any 65W USB-C charger work with my laptop?

##### Clarification needed

What is the exact laptop model and charging port? Do you need a compatibility check or a specific purchase recommendation?

##### SIMULATED answer in the test task

ThinkPad T14 Gen 4 AMD, USB-C PD; compatibility checks needed, not a specific purchase recommendation.

This is a simulation supplied by the person setting the task, not an actual confirmation from a user.

Not every 65 W charger will work. For your **ThinkPad T14 Gen 4 AMD**, you need to check the USB Power Delivery mode, the power available from the particular port, and the cable. Lenovo lists both 45 W and 65 W USB-C adapters with PD 3.0 for this model; 65 W is also the manufacturer's requirement for rapid charging. [Lenovo specification](https://psref.lenovo.com/syspool/Sys/PDF/ThinkPad/ThinkPad_T14_Gen_4_AMD/ThinkPad_T14_Gen_4_AMD_Spec.PDF)

Check the label in this order:

1. Look for **USB PD / Power Delivery**, as well as “65 W” and a USB-C plug.
2. In the output table, look for **20 V ⎓ 3.25 A**, or a higher available current at 20 V, to obtain the full 65 W. The calculation is 20 × 3.25 = 65. The [Lenovo 65 W adapter description](https://m.lenovo.com.cn/wiki/product-1039806.html) also specifies this output.
3. Make sure that the relevant port supplies this power in the way you will use it. On a multiport charger, “65 W” may be the total power. For example, the [Buffalo specification](https://www.buffalo.jp/product/detail/print/bsacpd6505c2bk.html) gives one device up to 65 W, while two devices share 45 W and 20 W.
4. If the cable is detachable, it must also be rated for at least 65 W. At 20 V it needs to carry more than 3 A. A cable marked 60 W is insufficient for the full 65 W; [USB-IF](https://usb.org/cable_connector) explains that cable power capabilities differ and are identified separately in certification markings.

For a practical check, connect only the laptop first and see whether it displays a slow-charging message and whether the battery level rises while you work. [Microsoft](https://support.microsoft.com/de-de/windows/experience/power-battery/pc-is-charging-slowly-or-discharging-while-it-s-plugged-in) describes situations in which an unsuitable power supply causes a computer to charge slowly or continue discharging. This is a sequence of checks; no particular charger has been tested with your computer here.

#### E05

The garment shows 30 degrees, an underlined wash tub, and a crossed-out triangle. How should I wash it?

Choose **a gentle wash cycle at no more than 30 °C and a detergent without bleach**. If there is one line under the wash tub, the symbols mean the following:

| Symbol | What it requires |
|---|---|
| “30” inside the wash tub | The water temperature must not exceed 30 °C. |
| One line under the wash tub | Gentler mechanical treatment, a smaller laundry load, and gentler spinning. |
| Crossed-out triangle | Do not bleach, including with oxygen bleach. |

These meanings are explained in the [GINETEX care-symbol guide](https://ginetex.de/pflegekennzeichnung/pflegesymbole/) and the [Japanese Consumer Affairs Agency's chart](https://www.caa.go.jp/policies/policy/representation/household_goods/guide/wash_02.html).

In practice, use your washing machine's instructions to choose a cycle suitable for a gentle 30 °C wash. Simply lowering the temperature of a normal intensive cycle is insufficient: the line also calls for gentler agitation. For this setting, GINETEX recommends filling the drum no more than halfway and using a short spin or no spin. This label does not specify a universal spin speed. [GINETEX](https://ginetex.de/pflegekennzeichnung/pflegesymbole/)

Check the ingredients or instructions for both the detergent and any stain remover. A “for colors” label can help you find a suitable product, but the essential requirement is that it contain no bleach. The ban on bleaching also applies to a product you might add separately to treat a stain.

If there are **two lines** under the wash tub, an even gentler cycle is needed. Other symbols govern drying and ironing; these three do not tell you whether the garment can go in a tumble dryer.

#### E06

I have a 3000x2000-pixel photo. Will it make a good A4 print?

**Yes, a 3000 × 2000-pixel photo can make a good A4 print**, provided the photo itself is sharp enough. This is an assessment based on resolution; without seeing the image, I cannot assess blur, noise or excessive compression artefacts. Adobe says that at least 220 pixels per inch is often enough for a photograph on an inkjet printer. [Adobe's explanation](https://helpx.adobe.com/photoshop/desktop/crop-resize-transform/resize-adjust-resolution/printer-resolution.html)

Your photo has a 3:2 aspect ratio, while [A4 measures 297 × 210 mm](https://www.adobe.com/uk/creativecloud/design/discover/a4-format.html). In landscape orientation, there are therefore two options:

| Placement | Calculated result |
|---|---|
| Fit the entire photo without cropping | An image of 297 × 198 mm, approximately 257 ppi; a total of 12 mm remains at the top and bottom. |
| Fill the entire A4 sheet while preserving proportions | Approximately 242 ppi; a little must be cropped from the photo's left and right edges. |

The calculations assume the full stated paper area, without additional cropping in the printer's borderless mode. The basic formula is the number of pixels divided by the print dimension in inches. [Adobe on the relationship between size and resolution](https://helpx.adobe.com/photoshop/desktop/crop-resize-transform/resize-adjust-resolution/image-size-resolution-and-resampling.html)

The A4 reference at 300 ppi is approximately **3508 × 2480 pixels**, as the [Canon table](https://ij.manual.canon/ij/webmanual/ProfessionalPrintLayout/All/1.0/SC/DPPG/dppg_f-02.html) also shows. Your image does not reach that count, but this does not automatically make the print poor.

I would start with the whole frame and small white borders, especially if subjects are near the photo's edges. If the result matters, print a small detail sample at the same scale it will have on A4. Simply changing the number “72” in the file to “300 ppi” without resampling the pixels does not create new detail.

#### E07

My phone is running out of space. Will deleting in Google Photos free up the phone while keeping the pictures?

##### Clarification needed

Are you using Android or iPhone, is Google Photos backup turned on, and do you mean Free up space or Delete?

##### SIMULATED answer in the test task

Android; Google Photos backup enabled; explain Free up space and Delete without actually deleting anything.

This is a simulation supplied by the person setting the task, not an actual confirmation from a user.

**Yes, by using “Free up space on this device” after checking the backup.** Ordinary deletion in the Android app does something different.

| Action | What happens |
|---|---|
| **Free up space on this device** | Removes copies of photos and videos from the phone once they have been safely backed up. They remain in the Google Photos account. |
| **Delete / Move to trash** | Deletes pictures from Google Photos and the device; deletion of backed-up pictures also propagates to devices where backup is turned on. |

Google describes this distinction in its instructions for [freeing space on a device](https://support.google.com/photos/answer/6128843?co=GENIE.Platform%3DAndroid&hl=en) and [deleting photos](https://support.google.com/photos/answer/6128858?co=GENIE.Platform%3DAndroid&hl=en).

**I would proceed as follows:**

1. In the Google Photos profile, check that the correct Google account is selected and the status is **“Backup complete”**. Having backup enabled does not mean it has finished.
2. Open the information for a few important pictures and check for **“Backed up”**. As an additional check, open them in the same account at [photos.google.com](https://photos.google.com). Google explains [how to check the overall backup status and the status of an individual photo](https://support.google.com/photos/answer/6193313?co=GENIE.Platform%3DAndroid&hl=en).
3. Only then select **“Free up space on this device”**. Before confirmation, the app shows how much space it will free.

After removing the local copies, you will still see the pictures in Google Photos when signed into the account with an internet connection. They will no longer be available in the phone's ordinary gallery or offline. Recent files less than 30 days old may remain on the device, so this feature does not always remove every local copy. [Google Help](https://support.google.com/photos/answer/6128843?co=GENIE.Platform%3DAndroid&hl=en) states this.

This is an explanation of the actions; nothing has been deleted from the phone.

#### E08

What does 5 GHz on the router mean? Will the internet be five times faster?

**5 GHz is a Wi-Fi radio frequency band. It does not promise five times faster internet.** Gigahertz describes how frequently a radio wave oscillates; data transfer speed is measured, for example, in megabits per second, or Mbit/s. “5 GHz” is the name of the band in which the router and your phone or computer communicate. [Intel's explanation](https://www.intel.com/content/www/us/en/products/docs/wireless/2-4-vs-5ghz.html).

In practice, the choice usually looks like this:

| Band | When it may be preferable |
|---|---|
| **5 GHz** | Closer to the router, when you need higher data throughput and have a good signal. Wider channels are generally possible. |
| **2.4 GHz** | Farther from the router or behind several walls, if the 5 GHz connection becomes weak. However, there may be more interference in this band. |

These are tendencies, not guarantees for a particular apartment. [Buffalo](https://www.buffalo.jp/support/faq/detail/15959.html) notes that 5 GHz does not always provide a faster or more stable connection. [TP-Link](https://media.tp-link.com.cn/document/html1714457949100.html) also explains that the number of signal “bars” alone does not tell you the speed, because interference and channel quality matter.

**Internet speed is limited by the entire chain:** your internet service, router, device, and Wi-Fi conditions. For example, switching to 5 GHz alone will not turn a 100 Mbit/s connection into a 500 Mbit/s connection. This is a conclusion drawn from these limitations, not a measurement of your network. [Intel](https://www.intel.com/content/www/us/en/products/docs/wireless/2-4-vs-5ghz.html).

**I would start with a simple comparison:** if both bands are available separately, test each one several times with the same device in the same place. I would also compare the stability of video or calls. The best choice is the one that works well where you actually use the device.

#### E09

The PDF contains images of text. I want to copy the Latvian text without paying or sending the document to an outside service. What should I use?

**I would start with [NAPS2](https://www.naps2.com/).** It is free, open-source software for Windows, macOS and Linux computers. You can import an existing PDF and use OCR, or text recognition, to add a copyable text layer.

**Steps:**

1. Download NAPS2 from the project's website and import the PDF.
2. Click **OCR**; on a Mac, this is **Tools → OCR**. Download the Latvian language data and select **Latvian**. NAPS2 uses Tesseract language files; the Latvian language code is **lav**. This is supported by the [NAPS2 documentation](https://www.naps2.com/doc/org-use) and [Tesseract language list](https://tesseract-ocr.github.io/tessdoc/Data-Files-in-different-versions.html).
3. Select **“Make PDFs searchable using OCR”** and save the result as a new PDF, retaining the original too.
4. Open the new PDF in a reader, select the text and copy it. NAPS2 itself has no separate OCR text export to TXT; for this purpose, the project instructions recommend copying from the saved PDF. [OCR instructions](https://www.naps2.com/doc/ocr).

The initial download of the program and language files requires internet access, but document recognition can run locally. The project author explains this in a [support discussion](https://sourceforge.net/p/naps2/discussion/general/thread/df4f787b95/), and the [deployment documentation](https://www.naps2.com/doc/org-use) also describes operation on a computer without internet access. Sending documents is a separate operation of the **Email PDF** feature; the [privacy policy](https://www.naps2.com/privacy-policy) describes that integration separately.

For your purpose, save the file in a local folder that is not synchronised with a cloud service, and do not use email sending. After downloading the program and language data, you can also process it with the internet disconnected.

**Try one page first:** compare Latvian macrons, palatalisation marks, numbers and text order with the original. If the result is poor, try the **Best** OCR mode; the documentation offers it as a slower option that sometimes recognises text better. The particular PDF was not processed in this test.

#### E10

Will putting warm food in the refrigerator damage it? What is a sensible way to handle a small pot of soup at home?

**A small amount of warm food generally does not damage the refrigerator by itself.** In its household guide, the FDA explicitly explains that putting hot food in the refrigerator does not harm the appliance and recommends dividing food into smaller containers so it cools faster. [FDA guidance](https://www.fda.gov/food/buy-store-serve-safe-food/refrigerator-thermometers-cold-facts-about-food-safety).

However, a larger amount of heat makes the refrigerator do more cooling and can warm nearby food. [Liebherr](https://www.liebherr.com/de-ch/gefrier-kuehlschraenke/freshmag/frische-ideen/warme-speisen-in-den-kuehlschrank-7712798) therefore recommends smaller portions and preliminary cooling, for example in a cold-water bath.

**For a small pot of soup, I would do this:**

1. If the soup is still very hot, briefly place the pot in cold water and stir with a clean spoon. The water should not enter the soup. Another option is to transfer the soup into smaller, shallow food containers.
2. Cover the containers and put them in the refrigerator soon, even if the soup is still slightly warm. Leave space around them for air circulation.
3. Check that the refrigerator maintains about **4 °C**. If its temperature is unknown, a refrigerator thermometer can check it.

Both the [Hong Kong Centre for Food Safety](https://www.cfs.gov.hk/sc_chi/consumer_zone/safefood_all/five_keys_apply_leftovers.html) and [Japan's Ministry of Agriculture](https://www.maff.go.jp/j/syouan/seisaku/foodpoisoning/frige.html) recommend dividing food into shallow containers and refrigerating it promptly; the latter also recommends approximately 4 °C and avoiding overcrowded shelves.

**Do not leave soup on the counter for hours while waiting for it to cool completely.** For households, the FDA recommends refrigerating food within two hours of cooking, or within one hour in heat above approximately 32 °C. These are maximum waiting limits, not targets to wait that long. The practical choice is to cool quickly and refrigerate sooner. [FDA](https://www.fda.gov/food/buy-store-serve-safe-food/refrigerator-thermometers-cold-facts-about-food-safety).

### Practical technical questions

#### P01

In a game, I see people talking about ESP, aimbots and kernel anti-cheat. What do they do, how do game mods differ from cheats, and where can I read something useful about this? I do not need instructions for cheats or bypasses.

ESP reveals information hidden in a game, an aimbot automates aiming, and kernel anti-cheat is part of the protection against unauthorised interference. They perform different jobs.

| Term | What it means in practice |
|---|---|
| ESP | Shows, for example, other players' locations even when they should not be visible. The PUBG team describes displaying these data through text or graphics. |
| Aimbot | Software helps direct aiming towards a target automatically. The pixelbot described by Riot is an example that analyses the image and performs input actions. |
| Kernel anti-cheat | A protection driver runs in the operating-system kernel with high privileges. A game client and server checks may operate alongside it. |

These differences are described by [PUBG developers](https://pubg.com/en/news/6957), [Riot engineers](https://www.riotgames.com/en/news/vanguard-on-demand) and the [Activision documentation](https://support.activision.com/cn/zh/articles/ricochet-overview).

A mod is a modification or addition to a game. The developer may support new maps, items and other changes, as provided for by [Steam Workshop](https://partner.steamgames.com/doc/features/workshop). Whether it is allowed depends on the particular game's rules and the function used. For example, Riot considers revealing hidden information and performing actions on the player's behalf to be an unauthorised advantage. The label “mod” does not itself grant permission. [Riot policy](https://support.riotgames.com/en-us/riot/events/third-party-applications).

To understand the technical side, I would start with [Paul Chamberlain's description of Fog of War](https://www.riotgames.com/en/news/demolishing-wallhacks-valorants-fog-war). The VALORANT anti-cheat developer explains how a server can avoid sending hidden opponents' locations to the client and describes his tests. The [PUBG Anti-ESP letter](https://pubg.com/en/news/6957) also shows a practical complication: replays and the death camera need information that must not be revealed to an active player. These are reports by the developers themselves; the game's protection was not tested here.

I would check the operating mode separately for each system. The [current Vanguard documentation](https://support.riotgames.com/de-de/riot/performance/what-is-vanguard) already describes a Pre-Check option to turn it on when requested, if the computer meets the relevant security requirements. Describing all kernel protection as “always on” would be inaccurate.

Before using a particular mod, the next step is to check that game's modification policy and whether the rules differ between single-player and multiplayer modes.

#### P02

I want to translate a single-player game into Latvian without losing placeholders or text context. Which open-source workflow should I choose?

TEST SIMULATION: JSON strings with {player_name}, plural forms, and dialogue IDs; modifying executable files is outside the task's scope.

For this JSON example, I would choose Git with Weblate and a verifiable import/export step. The assumption comes from the test clarification: the file contains `{player_name}`, plural forms, and dialogue IDs. The actual game's files have not been examined.

Weblate is a self-hostable, open-source solution with a [GPL-3.0-or-later license](https://docs.weblate.org/en/latest/contributing/license.html). Before translating, however, you need to identify the JSON variant: the [generic JSON parser](https://docs.weblate.org/en/latest/formats/json.html) does not itself support plural groups or context fields; the [i18next JSON v4 parser](https://docs.weblate.org/en/latest/formats/i18next.html) supports plurals. The game's schema must be the basis for the workflow, and i18next should be chosen only if the files actually conform to it.

I would structure the workflow as follows:

1. Preserve the originals and associate each translation with a stable dialogue ID. Translate the text values; preserve IDs, placeholder names, and the JSON structure.
2. Add the speaker, scene, previous and next lines, and a screenshot where needed for each dialogue. Store this extra context in Weblate or in a separate mapping by ID if the game file has no provision for it. [Weblate's context features](https://docs.weblate.org/ja/latest/user/translating.html).
3. Enable a check for the actual placeholder syntax. `python-brace-format` is suitable if the game uses the corresponding brace syntax; `strict-format` can prevent omission of a number placeholder in a singular form. Other syntax requires a different check. Automatic detection is no guarantee. [Checks](https://docs.weblate.org/en/latest/user/checks.html), [check conditions](https://docs.weblate.org/zh-cn/latest/user/checks.html).
4. Match plurals to the game's rules. CLDR defines `zero`, `one`, and `other` for Latvian cardinal numbers, including fractional-number conditions; the game may represent these categories in its own schema. [CLDR table](https://www.unicode.org/cldr/charts/49/supplemental/language_plural_rules.html).

A lighter alternative for one translator is [Translate Toolkit `json2po/po2json`](https://docs.translatehouse.org/projects/translate-toolkit/en/latest/commands/json2po.html) with a PO editor. This adds a conversion step whose reversibility must be checked; the source and translation revisions must match. The [Toolkit license text](https://github.com/translate/translate/blob/master/COPYING) is GNU GPL v3.

I would start with 30 varied strings. First import and export unchanged text, then compare the structure, IDs, and placeholders. For the translation, also check diacritics, text length, and plurals in the game itself. Acceptance condition: no missing key or unauthorized change to a placeholder. If the check fails, I would not start the full translation.

The documentation and Weblate's placeholder-checking class have been examined; installation and testing in the game have not been performed. A new translation platform is not justified at this point. The game's name and an actual JSON sample are still needed for a precise import tool.

#### P03

Is 12 GB of VRAM enough for a local 27B language model? What exactly should be counted?

TEST SIMULATION: nominal 4-bit weights, context 8192, one user; no performance guarantee.

Under the stated test assumptions, 12 GB of VRAM is not enough to keep all the 27B model's 4-bit weights and working memory on the graphics card. Local execution with partial offloading to the computer's RAM is nevertheless possible in suitable software.

The first calculation is straightforward:

`27 000 000 000 × 4 / 8 = 13 500 000 000 bytes`

That is 13.5 GB, or approximately 12.57 GiB, for ideally packed weights alone, already more than 12 GiB. Real quantisation may add scale factors and other data. For example, the [GGML Q4_0 block](https://github.com/ggml-org/llama.cpp/blob/master/ggml/src/ggml-common.h) stores a scale factor alongside the four-bit values.

All of these components must be counted:

- The actual weight size and its division between GPU and RAM.
- KV cache for the selected 8192-token context and one user.
- Temporary computation buffers and the runtime's memory.
- VRAM already used by the desktop and other programs.

KV size cannot be determined from “27B” alone: the particular architecture and cache data type are needed. Different attention schemes and cache strategies also have different memory use. [Transformers documentation](https://huggingface.co/docs/transformers/en/kv_cache).

[llama.cpp](https://github.com/ggml-org/llama.cpp) supports combined CPU and GPU execution, but its [parameters](https://github.com/ggml-org/llama.cpp/blob/master/tools/completion/README.md) separately control GPU layers, KV placement and cache type. There must be enough RAM, and speed needs to be tested on the particular hardware. A model that loads has not yet been tested at full context.

A useful counterexample is a [llama.cpp user report](https://github.com/ggml-org/llama.cpp/discussions/26736): in a different, large DeepSeek configuration, moving KV to RAM did not resolve the computation buffer's VRAM shortage. This is one user's experience, not a measurement of this 27B model.

The next step needs the exact model file, quantisation name, RAM capacity and free VRAM. Then check the weights, KV and computation buffers in the startup log and run a full-context trial. If everything must remain on the GPU, I would choose a smaller model or more VRAM; I would accept lower-bit quantisation only after testing quality. The model was not run here.

#### P04

I want to convert HDR video to SDR so the colors do not look gray. What do I need to know before using an FFmpeg command?

TEST SIMULATION: H.265, BT.2020/PQ, 10 bits; target SDR Rec.709; the user's file is unavailable.

The test clarification specifies H.265 video with BT.2020/PQ and 10 bits, with SDR Rec.709 as the target. This input needs both luminance-range conversion and correct color conversion. Simply changing the file's tag to “BT.709” is insufficient: FFmpeg's `setparams` changes property tags without recalculating the image itself. [Filter documentation](https://www.ffmpeg.org/ffmpeg-filters.html#setparams).

Before choosing the final command, I would check:

- `color_primaries`, `color_transfer`, and `color_space`: the color primaries, transfer function, and matrix.
- `color_range`: whether the input uses a limited or full signal range.
- The pixel format, bit depth, and available HDR luminance metadata.
- The FFmpeg version and available filters, as well as the device that will play the SDR video.

H.265 and 10-bit labels alone do not substitute for this color information. This read-only command is suitable for an initial check:

```bash
ffprobe -v error -select_streams v:0 -show_streams -of json "input.mp4"
```

It outputs stream information; it does not re-encode the video. [ffprobe documentation](https://ffmpeg.org/ffprobe.html).

For FFmpeg's standard `tonemap` filter, the sequence is to interpret the PQ input correctly, convert to linear light using floating-point data, map the tones to the SDR range, convert the colors, and output Rec.709. `zscale` helps perform these color and transfer-function conversions. The linear-light requirement is stated explicitly in both the [current documentation](https://www.ffmpeg.org/ffmpeg-filters.html#tonemap) and the [filter author's original discussion](https://ffmpeg.org/pipermail/ffmpeg-devel/2017-July/213824.html).

I would first try the chosen tone curve on a short clip containing a face, dark areas, and bright lights. During SDR playback, I would check black levels, highlight detail, and the final metadata. One curve, such as Hable, is not automatically suitable for every source.

Possible causes of a gray image include incorrect PQ interpretation, signal range, or player processing. Without the video, these remain hypotheses to test. The next step is the `ffprobe` output and a short sample; preserve the original. No video was re-encoded in this example.

#### P05

Is a NAS with RAID1 a sufficient backup for family photos?

RAID1 alone is insufficient if the family photos exist only on the NAS. It stores identical data on both disks simultaneously and helps keep the system running if one disk fails. Deletion or harmful overwriting can affect both disks. Loss of the entire NAS also requires a copy outside that device. [Synology's explanation](https://blog.synology.com/de/was-ist-ein-backup/) and [Buffalo's RAID description](https://www.buffalo.jp/topics/trouble/detail/recovery_0005.html) make this distinction.

For family photos, I would use this arrangement:

1. Photo originals on the NAS or a computer.
2. A regular copy with previous versions on a separate drive; disconnect the drive after copying.
3. Another copy in a different location, for example on an encrypted drive at a relative's home. Cloud storage is an option, but it is not required.

This is my practical recommendation to prevent one failure from affecting every copy. The [CISA guide](https://www.cisa.gov/sites/default/files/publications/CISA_MS-ISAC_Ransomware%20Guide_S508C_.pdf) also recommends offline encrypted copies and regular restoration tests. The document itself dates from 2020; I am not presenting it as new research from 2026.

NAS snapshots are useful for recovering an earlier state. If stored only on the same device, they do not solve the problem of losing the entire device. Remote storage changes this situation: [QNAP's documentation](https://www.qnap.com/zh-tw/software/snapshots) describes copying snapshots to another NAS and restoring them there.

If the originals also remain on a phone or computer, the NAS may already be one backup. Check whether synchronization propagates deletion to the other location and whether older versions are retained.

A useful first test is to restore a few new, old, and previously deleted pictures into a separate folder. Open them and check the full resolution and the metadata you need. Set the copying frequency according to how much recent photo history you could accept losing. I have not performed this restoration test here.

#### P06

If I give an AI a GitHub link to a skill, has it already installed it forever?

No. Providing a link does not by itself prove that the skill is installed. The agent may only read its text for this conversation. Installation requires saved files or a registered package, as well as a way for the particular agent program to find and use it. The [OpenAI skills documentation](https://developers.openai.com/api/docs/guides/tools-skills) describes these steps separately.

A skill is usually a folder containing `SKILL.md` and the required additional files. OpenAI's local execution uses file paths; in hosted execution, the skill is attached to the relevant environment. A hosted container's contents are discarded when the container ends or is deleted. “Available now” therefore does not mean “available in every future conversation”. [Execution types and lifecycle](https://developers.openai.com/api/docs/guides/tools-skills)

For example, the [OpenAI CLI skill-installation description](https://developers.openai.com/api/reference/cli) distinguishes `.agents/skills/` for a particular Codex project from `~/.agents/skills/` for the user's projects. It specifies using an installer or copying the entire skill folder and checking it in a new agent session. These paths are an example for that particular tool; the process can differ in another program.

Another agent environment uses a different process. The [Letta Code authors' instructions](https://github.com/letta-ai/letta-code#installing-external-skills) specify `letta skills install` with a GitHub address to put the skill in a particular agent's memory. `letta skills list --agent <agent-id>` checks that agent's skill list. Reading a link and installing a skill are separate operations in this example too.

For a convincing installation report, I would want to see:

- The saved location and the environment or user it covers.
- The particular version or Git commit identifier.
- Evidence that the agent finds the skill.
- A check of the necessary tools and connections.
- An example from a new session in which the skill was actually read and used.

This verification is my recommendation. The [Docs MCP instructions](https://developers.openai.com/learn/docs-mcp) also demonstrate the need for separate skill, connection and enabling steps.

Even a successful installation does not establish “forever”: the saved files must remain accessible and the next environment must load them. I did not install a new skill in this example and have not checked its availability in other sessions.

#### P07

What is practically usable in 2026 for local long-term agent memory, without mandatory cloud use? Compare several existing solutions.

I would start with the three solutions below. They are existing projects, but offer different integration scopes. The check was performed on 9 November 2026: I read repository configurations, the authors' example code and documentation. I did not perform installations or memory-quality tests. The table gives the package versions read from the `main` branch, not a promise that all sources are tied to a single immutable Git revision identifier.

| Solution | Version and licence checked | What I would choose it for |
|---|---|---|
| Mem0 OSS library | [2.2.1](https://github.com/mem0ai/mem0/blob/main/pyproject.toml), [Apache 2.0](https://raw.githubusercontent.com/mem0ai/mem0/main/LICENSE) | Adding memory to an existing agent. |
| Letta Code | [0.34.45](https://github.com/letta-ai/letta-code/blob/main/package.json), [Apache 2.0](https://github.com/letta-ai/letta-code/blob/main/LICENSE), with an exception for brand assets | When the agent environment itself, with persistent state and memory, is needed. |
| Graphiti | [0.31.2](https://github.com/getzep/graphiti/blob/main/pyproject.toml), [Apache 2.0](https://github.com/getzep/graphiti/blob/main/LICENSE) | When relationships between facts and their changes over time matter. |

**Mem0:** the authors' [local example](https://github.com/mem0ai/mem0/blob/main/docs/cookbooks/companions/local-companion-ollama.mdx) uses local Qdrant and Ollama for both the language model and text embeddings. I also read the [Ollama embedding-client code](https://github.com/mem0ai/mem0/blob/main/mem0/embeddings/ollama.py). However, the [ready-made server description](https://github.com/mem0ai/mem0/blob/main/docs/open-source/setup.mdx) lists a limited set of cloud providers for the default package. For a fully local starting point, I would therefore choose the library's documented configuration; the server image needs a separate check or adaptation.

**Letta:** the [old repository](https://github.com/letta-ai/letta) points to the current `letta-code`. The [self-hosting documentation](https://github.com/letta-ai/letta-docs-md/blob/main/self-hosting/index.md) provides a local mode without a Letta account: conversations, memory and other agent state remain on the computer. Model choice is separate: for fully local operation, a local provider such as Ollama must be connected. [Letta Cloud is the default](https://github.com/letta-ai/letta-code), so the required mode must be selected deliberately.

**Graphiti:** the [authors' README](https://github.com/getzep/graphiti) contains Ollama configuration code for the language model, embeddings and reranking. A graph database and integration with the agent must also be provided. This is a graph-building framework; the authors also note that small local models may not produce sufficiently reliable structured JSON output.

My choice would be Mem0 for an existing agent, Letta for a new agent environment, and Graphiti for a specific need to track the history of facts. Before longer use, I would check persistence after a restart, correction of a contradictory fact, source references, deletion and separation of users. After downloading the models, I would also test operation without an external network. This is a proposed acceptance test; I have not established network independence or quality on your computer here.

#### P08

My USB-C monitor shows no picture from the computer, even though the plug fits. Why?

A plug fitting does not establish video transmission. The computer's USB-C port may provide data and power without supporting the image signal the monitor needs. For a normal DP Alt Mode connection, this feature must be checked in the documentation for the particular port and monitor. [VESA](https://www.displayport.org/faq/) notes that the DP logo can help, but the device specification is decisive.

I would check in this order:

1. **The exact port.** Find the computer and monitor models, then check the selected USB-C socket in the manual. Different ports on one computer can perform different functions. DP support cannot be inferred solely from the socket's shape.
2. **Cable and power.** Try the cable supplied with the monitor or one already verified for video transmission. If the monitor requires a separate power supply, connect it. The [ASUS Japanese instructions](https://www.asus.com/jp/support/faq/1048768/) also recommend checking both ends of the connection.
3. **Monitor input.** Select the appropriate USB-C input in the monitor menu and make sure the computer is awake. The [ASUS troubleshooting description](https://www.asus.com/de/support/faq/1012723/) covers these steps and testing another cable or computer.
4. **Direct connection.** Remove the dock or adapter from the chain during the test. If a direct connection works, check the dock's capabilities, power and connections next. [ASUS USB-C support](https://www.asus.com/us/support/faq/1042417/) also recommends this.
5. **Change one component at a time.** Try another known-good cable and another computer that supports video output. If the monitor is detected but has no picture, try a lower resolution or refresh mode that it supports.

Check separately whether it is a DisplayLink monitor: [this type requires the appropriate driver](https://www.asus.com/jp/support/faq/1048768/). It must not automatically be confused with a DP Alt Mode connection.

Without the models and connection chain, the particular cause remains a hypothesis. The next step needs only the computer and monitor models, the port used, the cable or dock model, and the operating system. I have not tested the hardware itself here.

#### P09

How can I change my computer's DNS, and will that necessarily lower game ping?

Changing DNS does not guarantee lower game ping. DNS finds the address corresponding to a name; finding that address faster does not by itself reduce packet travel time on an existing connection to the same game server. This follows from the distinction between the two processes. [Google's technical explanation](https://developers.google.com/speed/public-dns/docs/performance) separately discusses DNS-query latency and the choice of geographically different server addresses.

An indirect effect is possible: another DNS may return a different server address. Whether the particular game chooses its server that way, and whether it helps, cannot be determined without measurement.

No operating system was specified, so the concrete example is **Windows 11**:

1. Record the current DNS settings and whether they are automatic.
2. Open **Settings → Network & internet → the Ethernet or Wi-Fi adapter in use**.
3. Under **DNS server assignment**, select **Edit → Manual**.
4. Enter your chosen service's addresses in the IPv4 DNS fields. For example, Cloudflare's standard DNS addresses are `1.1.1.1` and `1.0.0.1`. If you also configure IPv6 DNS, the corresponding addresses are `2606:4700:4700::1111` and `2606:4700:4700::1001`.
5. Save. Change the DNS fields specifically; the computer's IP address and gateway do not need to be replaced for this purpose.

This is [Cloudflare's documented setup example](https://developers.cloudflare.com/1.1.1.1/setup/windows/), not a claim that it will be the fastest DNS on your network. To undo the change, restore the recorded addresses or the automatic mode previously used. [Microsoft describes automatic DNS assignment through DHCP](https://support.microsoft.com/de-de/windows/experience/connectivity-networking/essential-network-settings-and-tasks-in-windows).

I would assess DNS response time and game ping separately. Before and after the change, take several measurements against the same game server under similar network load; also examine latency variation and packet loss. Record any change in the server's IP address. This is my proposed comparison; I did not change settings or measure performance here. For another system, adapt the exact menu path to its name and version.

#### P10

I also want to search for code in unfinished PRs and archives. How can I distinguish a useful component from a project that will cost more to maintain than an existing alternative?

I would start with one required function: what input, what result and which existing alternative to compare it with. Then the component's contribution can be assessed without taking on the entire project found.

GitHub's ordinary **Code Search searches default branches**. Code in an unmerged PR therefore cannot reliably be found through a general code search alone. The [GitHub documentation](https://docs.github.com/en/search-github/github-code-search/using-github-code-search) states this limitation explicitly.

I would start with searches like these; replace `OWNER/REPO` and `TERM` in the examples:

| Where to search | Example query |
|---|---|
| Unmerged PRs, including closed ones | `repo:OWNER/REPO is:pr is:unmerged TERM` |
| Draft PRs | `repo:OWNER/REPO is:pr draft:true TERM` |
| PRs in archived repositories | `is:pr archived:true TERM` |
| Code in archived repositories | `TERM is:archived` |
| Code in forks | `TERM is:fork` |

[PR search](https://docs.github.com/en/search-github/searching-on-github/searching-issues-and-pull-requests) and [Code Search syntax](https://docs.github.com/en/search-github/github-code-search/understanding-github-code-search-syntax) differ. In particular, do not confuse `archived:true` in PR search with `is:archived` in code search.

I would read a PR together with its discussion, reviewers' objections and tests. Its change branch can then be checked in a separate working copy with [`gh pr checkout`](https://docs.github.com/de/pull-requests/how-tos/review-pull-requests/checking-out-pull-requests-locally). For an archive, I would record a particular commit identifier: [GitHub explains](https://docs.github.com/en/repositories/working-with-files/using-files/downloading-source-code-archives) that branch and tag references can move.

My selection check would be:

- **Boundary:** can the function be used and replaced separately?
- **Permitted use:** do the particular files and dependencies have understandable licence terms? A public repository does not itself grant a free licence, as [GitHub](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository) explains.
- **Testability:** does a small example produce the required result and show failure behaviour?
- **Maintenance:** who will fix bugs, adapt dependencies and carry changes forward after updates?
- **Benefit:** what does this component do measurably better than the existing alternative?

The cost estimate would include adaptation, tests, subsequent fixes and dependency updates over the same period for both options. If substantial work is needed to revive the old project while the particular benefit remains unclear, I would choose the existing alternative. This is my decision method; I have not tested execution or integration of a particular PR, or any savings, here.

### Research questions

#### F01

Is there already a generally accepted proof of the Navier–Stokes existence and smoothness Millennium Problem? If not, what can our AI research project realistically test without pretending we have solved it?

### An announced solution is under review

On 9 November 2026, it would not be accurate simply to repeat that the problem remains unsolved. On 8 September, OpenAI published a claimed solution and a Lean formalisation. On 11 September, the Clay Institute wrote that the problem appeared to have been solved, but its current list places it under “Active problems”. The primary sources checked therefore support the wording “an announced solution is under review”; they do not by themselves establish a generally accepted, settled verdict. [Clay announcement](https://www.claymath.org/news/navier-stokes-announcement/) · [Clay list](https://www.claymath.org/millennium-problems/)

The precise version of the problem to which the result applies must be checked. The published work claims formation of a singularity with smooth external forcing, corresponding to alternatives C and D in the Clay formulation. It does not claim that this also solves the general case without external forcing. This can be checked by comparing the work's claim with Fefferman's official formulation, in which A and B require zero external forcing. [Authors' announcement](https://openai.com/index/navier-stokes-solution/) · [Official problem](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf)

Our project can start by checking the published work and then try two ideas for supporting tools.

1. Repeat the published certificate check. The existing base is the authors' Apache-2.0 repository with Lean, Mathlib and Lake; the documentation provides build commands. A separate Comparator check uses a comparable formalisation of the problem. Save the particular revision, dependencies, full execution log and theorem checked. The documentation was read in this research; the build was not executed. [Repository](https://github.com/openai/NavierStokesAndEuler) · [Comparator instructions](https://raw.githubusercontent.com/openai/NavierStokesAndEuler/main/ComparatorChallenges/README.md)
2. Form a small hypothesis about a proof-checking assistant tool: link each natural-language condition to its formal definition and report mismatches. A second experiment would transfer numerical simulation to rigorous error-bound verification for a particular set of data and time interval. A numerical impression of a singularity is insufficient: the official description itself stresses the numerical-instability problem. [Official problem](https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf)

The inexpensive initial test would be one precisely named lemma or one Comparator check with a CPU-time limit set in advance. Success would mean a recoverable verification result and an explicit list of hypotheses. If the problem statement changes or formal justification is missing, the result remains incomplete. Computing time, energy and implementation costs still need to be measured in this environment.

#### F02

Can a single high-resolution video uniquely recover an entire 3D scene and render unseen surfaces photorealistically?

### Complete unique recovery cannot be guaranteed

High resolution helps reveal visible details. More pixels do not create views behind objects. If the video never shows a surface and it does not affect visible reflections or shadows, several different versions of that surface can produce the same recording. The recording contains nothing with which to distinguish them. Reconstruction research explicitly identifies uncertainty in insufficiently observed regions, errors caused by moving objects, and inaccuracies in camera pose. [Authors' research](https://aaltoml.github.io/uncertainty-nerf-gs/)

A single video can nevertheless contain many useful viewpoints. For a static scene with camera movement, sufficient overlap and visible texture, I would start with COLMAP. Its authors recommend different camera positions, not just rotation in place, and warn about reflections and textureless surfaces. Camera trajectory and scene properties therefore need to be assessed alongside pixel count. [COLMAP tutorial](https://colmap.github.io/tutorial.html)

| Existing base | What to test |
|---|---|
| COLMAP | Camera poses and geometry from overlapping frames; the project's core code has a BSD licence. |
| MASt3R | A trained image-matching and 3D-estimation approach as a separate comparison; the code is CC BY-NC-SA 4.0, and weight usage also has dataset conditions. |

The documentation was read in this research; these tools were not installed or executed. MASt3R should not be presented as an open-source substitute with unrestricted commercial use. [COLMAP](https://github.com/colmap/colmap) · [MASt3R licences and installation](https://github.com/naver/mast3r)

A photorealistic image from a new viewpoint may be a plausible synthesis. Calling it a reconstruction of the particular place requires comparison with an independently captured image or another measurement. The original's unseen rear surface may be different.

I propose two testable synthesis hypotheses. The first adds a visibility mask and several independent model estimates to ordinary reconstruction to mark unsupported regions. The second uses this uncertainty to choose the next filming viewpoint. The authors' work discusses ensemble and additional-viewpoint approaches, but the advantage of our combination still needs to be measured. [Sources of uncertainty and methods](https://aaltoml.github.io/uncertainty-nerf-gs/)

For an initial test, choose one static object, a limited frame set and separately hidden test views. Compare the ordinary baseline, the mask and additional footage under the same computation limit. Reject the hypothesis if it does not reduce falsely confident reconstructions or if it worsens measured geometry. Record GPU time, memory and adapter work during the actual trial.

#### F03

How can an agent procedure be built that improves a search skill itself, without deceiving the evaluator or losing the ability to return to the previous version? Existing components and a possible synthesis.

### I would start with GEPA and separately protected evaluation

A search procedure can be improved by comparing a small number of clearly separated candidates. The agent may change search rules and create candidates; an independent executor decides which version to accept. The instruction “do not deceive the evaluator” is insufficient. In the RewardHackingAgents study, modifying the evaluator and accessing hidden answers were separate paths to violations, so both must be protected. This is a finding from that particular study, not a guarantee against all attacks. [Primary study](https://arxiv.org/abs/2603.11337)

An existing starting point is MIT-licensed GEPA: it optimises text candidates using execution errors and evaluation feedback. An adapter for custom systems and a call budget are also documented. DSPy integration suits a workflow already built in DSPy; a direct GEPA adapter may be clearer for a separate search tool. The documentation was checked, but GEPA was not installed here and no comparison with our search tool was performed. [Authors' repository](https://github.com/gepa-ai/gepa)

I would use the following verification procedure.

1. Save the accepted version, its contents, dependencies and checksums. Create a separate candidate for each change.
2. Give training tasks to the candidate creator; keep final test tasks and reference answers in a different process and outside its write/access permissions. Fix the model, tools, budget and critical-error definitions before the comparison.
3. Compare the currently accepted procedure with the candidate on the same tasks. The evaluator recalculates results from actual sources and logs; the candidate's self-assessment earns no acceptance points.
4. Accept only the tested change and retain the previous version. On new work, check the checksum of the loaded version; rollback also restores the corresponding configuration. Git `revert` preserves the reversal in history, but does not itself undo external side effects. [Git documentation](https://git-scm.com/docs/git-revert)

Two ideas to test supplement the existing base. The first transfers prevention of recurring errors to agent memory: keep a short record of rejected candidates. The author of GEPA issue #379 describes a user-reported case of repeated unsuccessful fixes and a related proposal that is still open; it must not be described as an implemented feature. The second uses the principle of reproducible releases: accept only a version package whose result provenance has been checked by an independent verifier. [GEPA discussion #379](https://github.com/gepa-ai/gepa/issues/379)

The inexpensive test: two candidates, tasks separated in advance, and the same limit for each side. Reject the hypothesis of an advantage if the gain disappears under independent recalculation or critical errors increase. Even a successful comparison would support only the particular change on the tested tasks. Detailed evaluator feedback can also help adapt evasion, so the hidden test is not repeatedly used for training. [Authors' 2026 study](https://www.microsoft.com/en-us/research/publication/reward-hacking-challenges-oversight-of-autonomous-research-agents/)

#### F04

Can an agent store infinite experience losslessly in 5 MiB of memory? What honest alternative can be built?

### 5 MiB can hold selected experience, not every arbitrary history

Infinite, arbitrary experience cannot fit losslessly into 5 MiB of memory. Counting memory states shows this: 5 × 1024 × 1024 × 8 = 41 943 040 bits. A fixed state of this size has finitely many possible configurations. There are more longer arbitrary histories, so different histories must end in the same state; both can no longer be uniquely recovered from it. This counting argument is known as the pigeonhole principle. [University proof exposition](https://www.informatik.hu-berlin.de/~koessler/Proseminar/Proseminar2015/JacobsSchubfach.pdf)

A particularly regular sequence, such as “always zero”, can be described briefly. Such an example does not change the guarantee for arbitrary data. Nor does a summary, model weights or a checksum preserve every deleted detail: the information required for recovery must exist somewhere. Information theory relates possible lossless compression to the source's predictability. [CMU teaching material](https://www.cs.cmu.edu/~15322/book/ch15/03.html)

For practical memory, specify in advance what will be retained and what may be lost. The total 5 MiB limit includes not only lesson cards but also indexes, versions, rejected-candidate records and evidence that must be preserved. Each card stores the situation, approach tried, result, limitation and source reference. Contradictory observations are not merged into one confident rule.

Letta is an existing base for broader memory: its documentation describes memory blocks in context and history in a database outside context. This helps organise a large history, but the documented approach does not prove a 5 MiB bound for the whole system. If an external archive is used, its size and retention period must be reported separately. [Letta authors' documentation](https://docs.letta.com/v1-sdk/concepts/stateful-agents)

For our bounded need, I would test two hypotheses. First, select cards by repeatedly measured usefulness for particular tasks, comparing this with simply retaining the newest cards. Second, reserve a small amount of space separately for failures and contradictions so that summaries of successes do not displace them. Answers to new tasks determine the value of both ideas. Compressed text size does not show it.

The inexpensive test is a prepared history exceeding the limit and hidden questions about its different parts. Measure correct recall, invented claims and bytes actually occupied on disk. Memory reduction preserves a deletion list; if mandatory records no longer fit, writing stops. Temporary rebuild files and working RAM must be counted separately. No such memory-quality experiment was executed in this research.

#### F05

How can we empirically determine whether German, Chinese and Japanese searches add more than English-only search under the same time budget?

### Compare the same tasks within the same time

We have not yet measured the advantage of four languages in this project. I would establish it through a comparison fixed in advance and paired by task: each task is performed by both an English-query procedure and an EN/DE/ZH/JA procedure. The model, tools and total time limit are the same; the multilingual side must also pay for terminology selection, translation and additional source reading within its time. Using the same task on both sides reduces confounding from task difficulty. This blocking follows NIST's experimental-design principle. [NIST](https://www.itl.nist.gov/div898/handbook/pri/section3/pri332.htm)

First define precisely what is changing. I would initially change only the query languages: both sides would be allowed to read sources found in any language. Otherwise both searching and information access would change at once. The English side may use its entire budget for additional English queries; the multilingual side receives no uncounted additional calls.

Before seeing results, divide tasks by topic and the potential importance of local sources. Randomise the order of the two variants. Use separate contexts and memory copies so that the second side does not see the first side's findings. On the live web, save receipts for results and opened pages because the index and pages change.

The primary measure would be correctness of verified claims needed to solve the task. Separately assess usefulness, unsupported claims, counterevidence found and costs. Translations and republications count as one original piece of evidence. Evaluators receive answers in Latvian without the procedure name; disputed claims are checked in the source.

The existing MIRACL dataset can separately test information retrieval: it has human-annotated relevance in many languages. But MIRACL's task is to search a same-language corpus; it does not by itself answer the question about four-language web research and final-answer quality. I would therefore supplement it with a separate test of our real tasks. [MIRACL authors' publication](https://transacl.org/index.php/tacl/article/view/4805)

There are two possible hypotheses: local terms find a previously undiscovered primary source; or additional languages mostly find duplicates and consume time. After the main test, languages can be added one at a time while retaining the same total limit. Before the work, define the minimum worthwhile gain and analyse paired differences with an uncertainty interval, treating the task as the unit. A small pilot helps calculate the sample size needed. If the interval also includes a practically worthless result, the conclusion remains uncertain; query count cannot replace an estimate of advantage.

#### F06

Can a decompiler precisely restore the original source code from an optimised binary? How should existing open-source solutions be compared with our own synthesis today?

### Original source code cannot generally be recovered

A decompiler can produce an understandable description of program behaviour, but an optimised binary usually does not determine one unique original text. GCC documents dead-code elimination, merging equivalent fragments and function transformations. If the compiler removed the differing source parts, the binary no longer contains information about which version was there. Researchers also explicitly describe type, structure and size information lost during compilation. [GCC](https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html) · [Primary decompilation study](https://www.s3.eurecom.fr/docs/asiaccs22_mantovani.pdf)

First choose the result to be achieved: identical original text, recompilable code, equivalent behaviour, or a result that is easier for an analyst to understand. These are different success criteria. Finding the actual source code externally can solve the first task for a particular file, but that is additional information.

I would choose Ghidra and RetDec as the comparison baseline.

| Tool | Supported scope of the choice |
|---|---|
| Ghidra | An Apache-2.0 project with decompilation, scripts and automated operation; suitable as the main adaptable base. |
| RetDec | An LLVM-based decompiler with C output; the repository states limited maintenance and multiple licensed components. |

The tool documentation was read, but installation and testing on our data were not performed. RetDec's limited maintenance is a concrete practical reason against a new long-term integration, not evidence of worse decompilation for every file. [Ghidra authors](https://github.com/NationalSecurityAgency/ghidra) · [RetDec authors](https://github.com/avast/retdec)

An inexpensive comparison would use our own small programs with known source code and clear licences. Compile them with fixed compiler versions and different optimisation levels, separately with and without debug information. Publish failures, CPU time spent and manual fixes. Textual similarity must not be relabelled as behavioural equivalence; the latter is checked with independent inputs and, for bounded fragments, formally stated conditions.

For our own solution, I would test two possibilities. First, a model restructuring Ghidra output improves readability, but every edit passes an independent behavioural check. Second, symbols, strings and calls are used to find candidates in an authorised source-code corpus. A candidate match is not yet proof of provenance; the version and build conditions must be checked.

One narrow family of functions and a fixed time limit are sufficient initially. I would continue building only if the synthesis outperforms an adapted existing baseline on the goal selected in advance and introduces no behavioural errors. Such a comparison is still needed to establish our system's advantage.

#### F07

Do identical model-weight files and a seed guarantee an identical answer on other graphics cards? What should be fixed for reproducibility?

**No, weight files and the same seed are not enough.** NVIDIA cuBLAS's reproducibility promise applies to a particular tool version, the same GPU architecture and the same number of SMs, with documented conditions for streams and algorithms. It is not a promise covering arbitrary graphics cards. [NVIDIA documentation](https://docs.nvidia.com/cuda/cublas/index.html#results-reproducibility)

The current vLLM documentation also says that reproducibility is not guaranteed by default. Offline mode allows deterministic scheduling or batch-independent execution; online mode documents the second solution. Even with these settings, the guarantee is limited to the same hardware and vLLM version. The seed determines random-number-generator state, not the entire computing environment. [vLLM maintainers' explanation](https://docs.vllm.ai/en/latest/usage/reproducibility/)

First define exactly what is to be repeated: intermediate-result bits, the token sequence, or answer quality. These are different criteria. For very close candidate tokens, even a small numerical difference can change the choice; subsequent generation then continues from a different sequence. This explains the mechanism; it is not a result measured on our hardware.

I propose preserving the following in a reproducibility package:

- Checksums of the weights, tokenizer, model configuration and exact input; the conversation template, decoding parameters and RNG states.
- The program revision, dependency and container versions, driver, CUDA, libraries, number format, quantisation and selected computation kernels.
- GPU model, device count and placement, parallelism settings, request batching, scheduler and cache mode.
- External-tool responses and retrieved documents if the model uses them, along with resulting tokens, errors and timings.

The existing base is a documented vLLM reproducibility mode with a fixed version. We would add an environment-description generator and a comparator that finds the first token or numerical divergence. **First hypothesis:** fixed scheduling reduces differences between repeated runs on one computer. **Second:** a more precise number format and matching kernels reduce divergence between two GPU configurations. Neither hypothesis promises universal bitwise identity.

An initial test needs only a set of prompts chosen in advance: repeated A/A runs and then A/B, changing hardware only. Record token agreement, the first divergence and actual costs. If even A/A differs, fix the baseline before comparing machines. No GPU tests were performed here; queries in four languages were executed, and the conclusion rests on the manufacturer and maintainer documentation read.

#### F08

I need a causal evaluation of changes to an agent's memory. How can better memory be distinguished from simply doing more searches or receiving easier tasks?

**Compare old and new memory on the same tasks, specifying search opportunities in advance.** A single results table in which the new version has more tool calls or a different selection of tasks does not isolate memory's contribution.

An existing starting point is LongMemEval: the authors' repository contains a set of 500 questions, conversation histories, answer-evaluation tools and comparisons for memory operations. It allows testing of information recall in conversations; the full quality of our agent's work still needs to be tested on its own tasks. [LongMemEval authors' repository](https://github.com/xiaowu0162/LongMemEval) A practical study by Redis authors separately compared retrieval of raw conversations, use of extracted memories, and their combination. The authors also warn that results published elsewhere and shown in their chart are not a controlled head-to-head comparison. [Primary-source experiment description](https://redis.github.io/redis-ai-research-public/longmemeval-agent-memory/)

I propose testing four combinations: **old/new memory × low/high number of searches**. A full factorial design includes every combination; [NIST](https://www.itl.nist.gov/div898/handbook/pri/section3/pri333.htm) describes its basis. At each search level, the controlled experiment fixes the number of calls and the external evidence, not just the allowed maximum. The model, prompt, token limit and initial history stay the same; the memory mechanism being tested changes.

Block tasks by difficulty and randomise execution order. Restore the initial memory state before every trial so that one version does not learn from the other's answer. The evaluator does not see the version name; the agent cannot modify reference answers, evaluation rules or hidden tasks. Evaluate factual correctness, refusal to guess, error severity, reading and writing costs, and uncertainty in the paired differences.

In a separate trial, let both versions choose their own number of searches within the same total budget. This measures the **effect of the whole procedure**, including its ability to save searches. Simply selecting only trials with equal call counts after receiving the results would be a different selection and could distort the conclusion.

I would initially test two possible improvements. Source references attached to every memory fact may reduce incorrect recall; this can be tested cheaply on questions containing conflicting dated facts. Retaining rare details alongside the summary may improve accuracy; test this with details discarded by the summary baseline. Both versions must have the same memory-size limit. If the gain disappears with fixed evidence, we cannot attribute it solely to a better memory representation.

Research in four languages was performed here. The described experiment still needs to be executed to measure differences in quality, time and cost.

#### F09

Can an LLM agent system guarantee exactly-once execution for all external payments if the process crashes after sending a request? Design a practical solution with its limitations.

**A universal “exactly once” guarantee cannot be given for all external payments.** If the service executes a request but the response is lost, the client's local state may be indistinguishable from a situation in which the request never reached the service. A blind retry may create a second payment, while not retrying may leave a payment unexecuted. The AWS authors' account directly addresses this ambiguity and client-assigned unique request identifiers. [AWS Builders’ Library](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/)

In practice, one payment effect can be achieved **within the idempotency contract of a particular service**. For example, Stripe API v1 stores the result of the first request with a given key only after endpoint execution begins. Repeating the same key returns the stored response, including a 500 error. If parameter validation fails, or there is a conflict with a concurrently executing request and endpoint execution does not begin, no idempotency result is stored; such a request can be retried. Keys may be deleted after at least 24 hours; reusing a key that has already been deleted creates a new request. API v2 documents different failure handling, so these rules must not be generalised. [Stripe idempotency](https://docs.stripe.com/api/idempotent_requests)

I would design the procedure as follows:

1. Before sending, save the payment intent, immutable parameters, unique intent ID and outbound job in one database transaction. One intent has one stable service key.
2. A separate worker sends the job. Queue retries use the same key and parameters; the agent cannot turn a retry into a new intent on its own.
3. Mark a timeout as **outcome unknown**, retain the service object ID if received, and reconcile the state with the service's data.
4. Process signature-verified notifications idempotently: record event IDs and do not depend on their arrival order. Stripe documents both duplicates and the absence of an ordering guarantee. [Notification documentation](https://docs.stripe.com/webhooks)
5. As the key approaches its retention limit, stop blindly retrying an ambiguous payment. Resolve it against the service's records or leave it for investigation, preserving the link to the original intent.

Existing components are the service SDK, a transactional database and an outbound-jobs table. AWS's documented *transactional outbox* approach links local changes to the job record, but it does not by itself make the external payment atomic with our database; duplicate messages still require an idempotent recipient. [AWS description of the approach](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html)

I would test two hypotheses: a stable intent key prevents a duplicate effect after a crash, and a separate check of ambiguous outcomes reduces stuck jobs. A fake payment service would be enough initially, with crashes induced before sending, after the effect and before saving the response, alongside key deletion and repeated notifications. The success criterion is at most one effect per intent and correctly reported uncertainty. Completion additionally depends on service availability and payment acceptance. Neither a test nor a payment was executed here; the four-language research produced a design, not proof of a universal guarantee.

#### F10

How can a self-improving image-reconstruction program be tested so that higher PSNR does not hide worse photographic quality and invented detail?

**Higher PSNR does not establish better photographic quality or correct detail.** Blau and Michaeli's study describes a limit between average distortion and perceptual quality. It does not mean that every PSNR increase automatically worsens every image. Cohen and colleagues, meanwhile, analyse how plausible-looking generative restoration can add details absent from the original. [Perception–distortion study](https://arxiv.org/abs/1711.06077); [study of invented details](https://arxiv.org/abs/2405.16475)

I would divide evaluation into three parts.

**Consistency with the observation.** On images with a known reference, calculate PSNR and structural similarity, fixing colour space, cropping, resolution and alignment in advance. Also retain results by scene and error maps; an average can hide one very poor case.

**Photographic quality.** An existing supplement is the authors' LPIPS implementation: it compares images using perceptually adapted features. Its documentation also specifies input scale and network variants, which must remain the same in a comparison. The authors' evaluation used human choices between two variants relative to a reference. [LPIPS code and evaluation description](https://github.com/richzhang/PerceptualSimilarity) In our test, people would blindly compare shuffled candidate pairs, both as full images and in important crops. LPIPS and human preference do not by themselves confirm that an image depicts the original details.

**Correctness of detail.** Separately check text, object counts, facial features, geometry and textures against the known reference or held-out additional viewpoints. If only one degraded image is available, entirely missing details may be plausible, but their correctness cannot be confirmed from that same image. Such regions must be marked as uncertain in the result.

The existing base is the current reconstruction program and a fixed evaluation suite; for upscaling, I would add simple interpolation. The self-improving agent changes the program only on the development set. The hidden test separates scenes, not neighbouring frames from one scene; the candidate cannot modify references, the evaluator or acceptance thresholds. The previous version remains restorable.

**First hypothesis:** acceptance based on multiple criteria, with severe detail errors prohibited, will produce more useful versions than PSNR optimisation alone. **Second:** comparing small input perturbations and multiple reconstructions will help detect unstable invented detail. Stability alone still does not prove correctness.

For an initial test of the hypotheses, I would choose a small, fixed set of scenes in advance, containing fine text, faces and repeated textures, and two candidates with the same resource limit. If the PSNR winner worsens the blind quality rating or introduces a critical mismatch, reject it. Record actual time and costs during the test. Four-language research and source reading were performed here; reconstructions, LPIPS calculations and the human experiment were not executed.

### How to use the skill in your environment

Give the agent the whole skill folder or the published project link. Ask it to read SKILL.md, follow the four-language research procedure and state precisely what has been activated. Following instructions in one conversation, permanent installation and connected experience memory are separately verifiable steps.

If the environment supports files and program execution, connect the start/end operations and check the second task: did it receive the lesson from the first task? Accept new methods only after a comparison defined in advance and independent checks. This provides a controlled path for development, not a guarantee that every next question will be easier or the answer always better.

### Support the author

Support details updated on 2026-11-10 at the author's request; experiment records above are unchanged.

My name is Reinis Runcis. I am paralyzed and live alone. Each day I fight to keep creating, and I share this work for free. Through my example, I hope to inspire others who feel there is no way out of their situation.

If this project is useful to you, or you would like to help me carry on, I would be grateful for a voluntary donation. Your support helps me in daily life and in my work on tools like this.

Swedbank · Recipient: **REINIS RUNCIS**  
IBAN: **`LV82HABA0551011504293`**

- [Stripe (EUR)](https://buy.stripe.com/dRm7sNfD2bOZckRb9A6g802)
- [Stripe (USD)](https://donate.stripe.com/cNifZj4Yog5fckR5Pg6g800)
- [PayPal](https://paypal.me/ReinisRuncisSupport)

**USDT · BSC / BEP-20**

`0x32834068Fa4fEe29fA10e2020e68Fb23d5fC1d21`

**USDT · Solana / SPL**

`Hy6hKMwMDgXFdaD3N5J1CNMs2LwiE22QdrQnEYoX3fZh`

[More about me on Facebook](https://www.facebook.com/reinis.runcis)

Support is voluntary and is not required to use the skill.


<a id="comparison"></a>

## All six strategy-comparison answers

The six research-answer bodies below are unchanged from the reviewed English edition. Primary-source URLs remain in the prose and each answer's structured source list. The structured fields are part of the authored answers; separate evaluator outputs, test fixtures and execution records are not included.

The [Latvian answers](validation/2026-11-09-beta3/comparison/answers.lv.md) and the [published findings](PUBLISHED_FINDINGS.md) provide the corresponding original-language answers and reported comparison outcome. This translation is not a new research run. See the [publication scope](PUBLICATION_SCOPE.md) for the evidence limits.

### baseline / IT01-depth-output

**There is no basis for adding the unit `m` to this checkpoint's output.** The card for `depth-anything/Depth-Anything-V2-Small-hf` identifies its output as relative depth, and the authors' repository also classifies the base models as relative-depth estimators. The card's general statement about relative and absolute depth does not establish that this particular checkpoint outputs metres. [Model card](https://huggingface.co/depth-anything/Depth-Anything-V2-Small-hf), [authors' repository](https://github.com/DepthAnything/Depth-Anything-V2).

The project author explains that the model predicts inverse depth: a smaller prediction corresponds to a more distant point. The component can therefore be retained for ordering image regions by relative proximity. That ordering does not itself provide physical distances in metres. [Author's explanation](https://github.com/DepthAnything/Depth-Anything-V2/issues/174).

The next step is to choose a separate checkpoint adapted for metric depth, such as `Depth-Anything-V2-Metric-Indoor-Small-hf` for indoor scenes. The author has already adapted that model, so you do not need to train a new one yourself. Under this task's action codes, however, the choice is `replace_core`. Before relying on its distances, measure its error on your own images against measured distances. [Metric model card](https://huggingface.co/depth-anything/Depth-Anything-V2-Metric-Indoor-Small-hf). A user in the project discussion describes incorrect scale when constructing a point cloud; that is a report of a particular experience, not a universal error measurement. [Experience report](https://github.com/DepthAnything/Depth-Anything-V2/issues/152).

I checked sources and configuration here. I did not run inference, install packages or download weights.

### evaluation_fields

```json
{
  "decision": {
    "requested_function_supported": false,
    "native_output_kind": "relative_depth",
    "action": "replace_core",
    "executed_here": false
  },
  "reuse": {
    "useful_function": "depth_ordering"
  },
  "explanation": "Depth-Anything-V2-Small-hf is a relative-depth checkpoint. Its output represents the relative proximity of image points, and the task's stated conditions do not justify a scale in metres. The project author explains that it predicts inverse depth. Adding a metre label does not turn the output into a metric distance.",
  "next_step": "Retain this model for ordering nearer and more distant image regions. For distances in metres, choose a separate checkpoint that the authors have adapted for metric depth, such as Depth-Anything-V2-Metric-Indoor-Small-hf for indoor scenes. Before use, check its error on your own images against measured distances. Only sources were checked here.",
  "sources": [
    "https://huggingface.co/depth-anything/Depth-Anything-V2-Small-hf",
    "https://github.com/DepthAnything/Depth-Anything-V2",
    "https://huggingface.co/depth-anything/Depth-Anything-V2-Small-hf/blob/main/config.json",
    "https://huggingface.co/depth-anything/Depth-Anything-V2-Metric-Indoor-Small-hf",
    "https://github.com/DepthAnything/Depth-Anything-V2/blob/main/metric_depth/README.md",
    "https://github.com/DepthAnything/Depth-Anything-V2/issues/174"
  ]
}
```

### baseline / IT02-clip-generation

**The official CLIP `ViT-B/32` does not generate a free-form descriptive sentence through the specified example.** `encode_image` and `encode_text` return feature vectors. Calling the model with an image and texts returns their similarities; the example supplies the texts in advance and scores those candidates. [Documented example and API](https://github.com/openai/CLIP).

This is also visible in `clip/model.py`: the text encoder produces a vector, while `forward` normalizes both types of vectors and returns similarity matrices. That execution path has no step that generates tokens for a new sentence. The requested free-form description would require a different or additional trained component with a text decoder, which is `replace_core` under the task's action codes. [Model code](https://github.com/openai/CLIP/blob/main/clip/model.py).

Similarity search can be retained for the library. The next component to build is a store containing each image's normalized `encode_image` vector and file path. Encode the text query with `encode_text`, then rank images by cosine similarity. This uses the documented vector-comparison mechanism. [API and normalization example](https://github.com/openai/CLIP). Relevance must be checked on your own library; the original model card says that languages other than English were not intentionally trained or evaluated. [Model card](https://github.com/openai/CLIP/blob/main/model-card.md).

I read the documentation and relevant code here. The model was not run, packages were not installed and weights were not downloaded.

### evaluation_fields

```json
{
  "decision": {
    "requested_function_supported": false,
    "native_output_kind": "embeddings",
    "action": "replace_core",
    "executed_here": false
  },
  "reuse": {
    "useful_function": "similarity_retrieval"
  },
  "explanation": "The official CLIP ViT-B/32 encodes supplied images and texts into vectors. Its forward returns similarities between the image and supplied texts, while the example calculates probabilities for texts specified in advance. This model and example have no decoder for freely generating image descriptions. Under the stated conditions, it therefore does not produce a complete new descriptive sentence.",
  "next_step": "For an image library, store each file's normalized encode_image vector and path; encode a text query with encode_text and rank images by cosine similarity between the vectors. A free-form descriptive sentence would require a different or additional trained component with a text-generation decoder, so the original constraint would have to change. The model was not run here.",
  "sources": [
    "https://github.com/openai/CLIP",
    "https://github.com/openai/CLIP/blob/main/clip/model.py",
    "https://github.com/openai/CLIP/blob/main/model-card.md",
    "https://github.com/openai/CLIP/blob/main/LICENSE",
    "https://github.com/openai/CLIP/blob/main/requirements.txt"
  ]
}
```

### baseline / IT03-dinov2-retrieval

**DINOv2 `ViT-S/14` provides an image representation that can support this search without training a new base model.** The authors' model card explicitly lists nearest-neighbour image retrieval; the ViT-S vector has 384 elements. Class labels are unnecessary for ranking image vectors against one another. [Model card](https://github.com/facebookresearch/dinov2/blob/main/MODEL_CARD.md).

The sources include model code, weight links and an example loading `dinov2_vits14`. `forward_features` supplies the global `x_norm_clstoken` and local image-patch features; the ordinary `forward` returns the global representation through an `Identity` head. [Repository](https://github.com/facebookresearch/dinov2), [model code](https://github.com/facebookresearch/dinov2/blob/main/dinov2/models/vision_transformer.py).

To build a search tool for your folder, the following processing still needs to be implemented:

1. Prepare local loading of the code and previously downloaded weights. The base-model loading code also accepts a weights path. [Loading code](https://github.com/facebookresearch/dinov2/blob/main/dinov2/hub/backbones.py).
2. Process all images consistently, obtain global vectors, apply L2 normalization separately, and store the vectors with file paths.
3. Calculate the same kind of vector for the submitted image, rank the library by cosine similarity, and return the chosen number of nearest results.
4. Add image submission and result display, then check relevance on your own examples. These are application-processing steps around the documented nearest-neighbour mechanism. [Model uses](https://github.com/facebookresearch/dinov2/blob/main/MODEL_CARD.md).

The choice is therefore `adapt_output`. Result quality still needs checking on your folder: a project user reported poorer retrieval after cropping an image; that is a report of a specific experience. [Discussion](https://github.com/facebookresearch/dinov2/issues/103). I did not run inference, install packages or download weights here.

### evaluation_fields

```json
{
  "decision": {
    "requested_function_supported": true,
    "native_output_kind": "embeddings",
    "action": "adapt_output",
    "executed_here": false
  },
  "reuse": {
    "useful_function": "similarity_retrieval"
  },
  "explanation": "DINOv2 ViT-S/14 provides an image representation with 384 elements, and the authors' model card documents nearest-neighbour image retrieval without further adaptation of the base model. The code exposes the global x_norm_clstoken and patch features. The published base model is a usable component; a personal folder still needs indexing, similarity ranking and an image-submission interface. These steps do not require a newly trained base model.",
  "next_step": "Prepare local loading of the repository and weights. With consistent preprocessing, obtain each library image's global 384-element vector, apply L2 normalization separately and store it with the file path. Obtain the same kind of vector for the submitted image, calculate cosine similarity, select the top-k files and display them in the interface. Before wider use, check relevance on examples from your folder, including rotated images. No execution was performed here.",
  "sources": [
    "https://github.com/facebookresearch/dinov2",
    "https://github.com/facebookresearch/dinov2/blob/main/MODEL_CARD.md",
    "https://github.com/facebookresearch/dinov2/blob/main/dinov2/models/vision_transformer.py",
    "https://github.com/facebookresearch/dinov2/blob/main/dinov2/hub/backbones.py"
  ]
}
```

### candidate / IT01-depth-output

### Conclusion

The unit **m** must not be attached to this checkpoint's output. `depth-anything/Depth-Anything-V2-Small-hf` produces a relative-depth map. The model card labels it relative, and the authors' repository associates this specific Transformers example with the relative base models. The card's broader discussion of absolute-depth results does not establish a metre scale for this checkpoint.

The component can be retained for a relative **nearer/farther ordering** of image regions. An adapter can resize the map, display it or read values from a selected region. These operations do not recover the missing physical scale; the author also requires true metric-depth values to adjust the scale. This conclusion applies to the stated conditions, which provide no such reference measurements.

If an estimated metric-depth map is needed without training a model yourself, the next step is to select the authors' published metric Small checkpoint: Hypersim for indoor scenes or Virtual KITTI 2 for outdoor scenes. Its example specifies output in metres. This changes the checkpoint (`replace_core`); accuracy for the particular scene still needs checking.

I checked documentation, configuration and output-head code here. The model was not run, weights were not downloaded and no installation was performed.

### evaluation_fields

```json
{
  "decision": {
    "requested_function_supported": false,
    "native_output_kind": "relative_depth",
    "action": "replace_core",
    "executed_here": false
  },
  "reuse": {
    "useful_function": "depth_ordering"
  },
  "explanation": "The specific depth-anything/Depth-Anything-V2-Small-hf checkpoint produces a relative-depth map without a justified scale in metres. The card's broader discussion of absolute depth concerns the model family; the authors' repository separates relative base checkpoints from specially adapted metric models. Interpolation or normalization does not add metric scale.",
  "next_step": "Retain this checkpoint for relative nearer/farther ordering. If an estimated metric-depth map is needed without training a model yourself, replace it with the authors' published metric Small checkpoint: Hypersim for indoor scenes or Virtual KITTI 2 for outdoor scenes, and check its error under the conditions of your own scene. This changes the checkpoint; the originally fixed Small-hf cannot perform the requested function.",
  "sources": [
    "https://huggingface.co/depth-anything/Depth-Anything-V2-Small-hf",
    "https://huggingface.co/depth-anything/Depth-Anything-V2-Small-hf/blob/main/config.json",
    "https://huggingface.co/docs/transformers/model_doc/depth_anything",
    "https://github.com/DepthAnything/Depth-Anything-V2",
    "https://github.com/DepthAnything/Depth-Anything-V2/blob/main/metric_depth/README.md",
    "https://github.com/huggingface/transformers/blob/v5.22.2/src/transformers/models/depth_anything/modeling_depth_anything.py",
    "https://github.com/DepthAnything/Depth-Anything-V2/issues/200",
    "https://github.com/LiheYoung/Depth-Anything/issues/226"
  ]
}
```

### candidate / IT02-clip-generation

### Conclusion

**No.** The official CLIP `ViT-B/32` and its published example do not produce a free-form image-description sentence. `encode_image` and `encode_text` return feature vectors, while `model(image, text)` returns similarities between an image and texts supplied in advance. The code's `forward` function also ends with those similarity tensors. The output family is `embeddings`.

An adapter can select the most suitable previously written sentence from a bank of candidates. It still chooses one of the supplied texts. A newly generated free-form description requires an image-captioning model with a trained text generator, or the addition of such a component. Under the task's definition, this is `replace_core` and requires changing the original constraint.

CLIP can be retained for **similarity search** in an image library. The next practical step is to store image vectors from `encode_image` with their file paths, encode an English query with `encode_text`, and rank images by similarity between normalized vectors. This is an adapter around the existing model and does not require training a new base model. It is a recommendation for using the documented functions; results on your own collection still need checking. An English query respects the language scope of the original model card.

I read documentation and code here. The model was not run, nothing was installed and model weights were not downloaded.

### evaluation_fields

```json
{
  "decision": {
    "requested_function_supported": false,
    "native_output_kind": "embeddings",
    "action": "replace_core",
    "executed_here": false
  },
  "reuse": {
    "useful_function": "similarity_retrieval"
  },
  "explanation": "The official CLIP ViT-B/32 encodes an image and previously supplied text into feature vectors. model(image, text) returns similarity logits, and the example chooses between text options supplied in advance. encode_text is not a sentence-generation decoder; this model and example do not produce new free-form image descriptions.",
  "next_step": "Free-form descriptions require an image-captioning model with a trained text generator, or the addition of such a component, so the original constraint must change. Retain CLIP for library search: use encode_image to generate and store image vectors with file paths, encode an English query with encode_text, and rank images by similarity between normalized vectors. This search adapter does not require a newly trained base model; result quality must be checked on your own collection.",
  "sources": [
    "https://github.com/openai/CLIP",
    "https://github.com/openai/CLIP/blob/main/clip/model.py",
    "https://github.com/openai/CLIP/blob/main/model-card.md",
    "https://github.com/openai/CLIP/blob/main/LICENSE"
  ]
}
```

### candidate / IT03-dinov2-retrieval

### Conclusion

**Yes.** The published DINOv2 `ViT-S/14` provides an image representation suitable for this purpose. The model card specifies 384-dimensional vectors and explicitly lists nearest-neighbour image retrieval without further training of the base model. Class labels are unnecessary for comparing a query vector with collection vectors in this way.

The model weights and feature-extraction code are ready: `forward_features` returns `x_norm_clstoken` and image-patch features. For a simple search over whole images, I would start with the CLS vector. An adapter is still needed for the final function, so the choice is **`adapt_output`**. The base model does not need to change.

Next steps for the adapter:

1. Apply the same preprocessing to the folder images and query image, obtain CLS vectors and L2-normalize them.
2. Store the collection vectors with image-file paths.
3. Compare the query vector with the collection using cosine similarity and return `top-k` results.
4. Add an interface for selecting an image and viewing the ranked results.

These are proposed data-processing steps around the documented representation. Quality still needs checking on the particular collection; obtaining the model alone does not provide a finished file-library application.

For local use, prepare the repository code, dependencies and weights file beforehand. The current `dinov2_vits14` function accepts `weights` with a local file path; the code supports loading through that path. The model card and the inspected code header specify the Apache-2.0 licence.

I checked sources and code here. The model was not run, weights were not downloaded and offline operation was not practically tested.

### evaluation_fields

```json
{
  "decision": {
    "requested_function_supported": true,
    "native_output_kind": "embeddings",
    "action": "adapt_output",
    "executed_here": false
  },
  "reuse": {
    "useful_function": "similarity_retrieval"
  },
  "explanation": "The published DINOv2 ViT-S/14 provides an image-feature representation; the model card specifies a 384-dimensional output and explicitly supports image retrieval with nearest neighbors without fine-tuning. forward_features returns x_norm_clstoken and patch features. Class labels and new base-model training are unnecessary for this retrieval path, but the published backbone alone is not a finished search interface for the user's folder.",
  "next_step": "Build a local adapter: prepare the repository code, dependencies and ViT-S/14 weights file; load dinov2_vits14 with weights pointing to the local file. Preprocess the collection and query consistently, extract x_norm_clstoken, L2-normalize the vectors, store them with file paths, calculate cosine similarity and return the top-k images. Add image selection and a results interface; check quality on your own collection. The base model does not need to change.",
  "sources": [
    "https://github.com/facebookresearch/dinov2",
    "https://github.com/facebookresearch/dinov2/blob/main/MODEL_CARD.md",
    "https://github.com/facebookresearch/dinov2/blob/main/dinov2/models/vision_transformer.py",
    "https://github.com/facebookresearch/dinov2/blob/main/dinov2/hub/backbones.py",
    "https://github.com/facebookresearch/dinov2/blob/main/dinov2/hub/utils.py"
  ]
}
```


<a id="findings"></a>

## Published findings and limits

The final research set contains 10 everyday questions, 10 questions of medium difficulty across several fields, and 10 difficult questions. It keeps 12 earlier cases and adds 18, for 48 distinct main research tasks across the final and historical collections. Seven new advanced cases include full mathematical proofs or derivations and executed calculations. Both 30-case collections are available in full in English and Latvian.

The separate search-strategy trial did **not** establish an accuracy improvement. The candidate was rejected as the new baseline, and the recorded decision remains `no_gain`.

### The three-task comparison

The candidate first checked the least-supported necessary condition that could change a decision. The tasks concerned the output units of a Depth Anything checkpoint, CLIP's ability to generate a new descriptive sentence, and DINOv2 for image similarity retrieval. The six complete research answers and their public source URLs are retained in [English](validation/2026-11-09-beta3/comparison/answers.en.md) and [Latvian](validation/2026-11-09-beta3/comparison/answers.lv.md).

| Reported measure | Existing method | Candidate |
|---|---:|---:|
| Factual and execution-honesty checks | 9/9 | 9/9 |
| Next-action category | 3/3 | 3/3 |
| Documented useful component application | 3/3 | 3/3 |
| Rationale and next-step fields | 6/6 | 6/6 |
| Search queries | 15 | 15 |
| Reads, including failed attempts | 32 | 28 |
| Total web actions | 47 | 43 |
| Combined duration, measured from the first web request to completed artifacts | 456.14 seconds | 495.50 seconds |

The accuracy gain on these checks was zero. Four fewer web actions did not satisfy the fixed requirement for an accuracy gain, and the candidate's combined duration was longer. The acceptance objective was not changed after the results were known. The earlier differently defined durations, 461.75 and 569.59 seconds, are not a directly comparable speed measure.

This was a pilot with three designed tasks and one answer per side. The two contexts used a shared filesystem with an instruction boundary; they were not isolated by the operating system. Model identity was declared by the environment. The task designer also prepared the initial reference answers after the candidate was fixed; those answers were checked against primary sources before the trial. The two sides started about six minutes apart. These conditions do not support a statistical or universal superiority claim. No model inference was run and no model weights were downloaded for this comparison.

### Research coverage and corrections

The final 30 cases report 156 executed queries. Each case searched in English, German, Chinese and Japanese. A query in a language does not establish that a supporting primary source in that language was found and read. Access failures and limited source reads remain disclosed in the answers.

The original selection was too concentrated on IT in its medium group and lacked completed advanced mathematics tasks. The revised selection addresses those gaps while preserving the original answers. The historical total of 147 included four declared E10 queries whose full original outputs were not retained. The supported historical count is 143 distinct queries with retained receipts; missing receipts have not been reconstructed as if they were original evidence.

The questions were designed for validation, and simulated clarifications are labelled. One agent performed the main research for each example, followed by the reported reviews. The set does not demonstrate four independent agents searching every case. The mathematical arguments were read and checked against the stored calculations; no formal proof-assistant certification is claimed. The [release report](validation/2026-11-09-beta3/release-report.en.md) gives the retained findings and qualifications.

### What improved in the software

The recorded release passed 82 software tests. Two reproduced defects were repaired: an older lesson card could hide a newer contrary observation, and an unreferenced evidence object near the memory limit could prevent compaction from being saved. The current source, tests, calculation programs and calculation outputs are included so readers can inspect and rerun them. Software mechanism tests do not establish higher search accuracy.

All 18 new main tasks completed a recorded learning cycle, and 15 later tasks loaded earlier lessons. The chat orchestrated those operations. Loading experience does not prove that every subsequent answer improves or that an unattended service is running. The separate two-task execution demonstration is described here only at the level of its reported outcome: a later task loaded a saved lesson. Its internal execution records are excluded.

Useful fixes and compact lessons were retained. The prerequisite-prioritization candidate was not promoted. Lesson relevance, a trial with a cost objective, and the additional benefit of multiple search languages remain hypotheses requiring new tasks and fixed acceptance criteria.

### What this publication contains

This is an authored account of the findings. Full evaluator outputs, instruction snapshots, execution records, memory snapshots, raw logs, tool-query dumps and internal receipts are not included, either as separate files or copied into the combined experiment report. Those omissions limit independent reconstruction of the original orchestration. They do not remove the complete research answers, mathematical arguments, calculation code, reported negative result or stated limitations.

Read the [publication scope](PUBLICATION_SCOPE.md), [English research and experiment report](EXPERIMENTS.md), or [Latvian report](EXPERIMENTS.lv.md). The [file manifest](file-manifest.json) identifies the exact files in this edition. This publication makes no antivirus certification, general research-quality guarantee or claim of a permanently running improvement service.


<a id="cosmetics"></a>

## Introductory cosmetics example

> My face gets shiny, but the foundation somehow settles into the lines... I want it to look nice, without that mask effect. I don't know what to buy.

It sounds as though you want a more even skin tone, less shine and light coverage that still looks like natural skin. **I would start by applying a thinner layer of your current foundation before buying another one.** This description does not yet tell me whether the main issue is the product, the amount used or what is underneath it.

#### Try this first

Next time, test about half your usual amount of foundation. Apply it only where you want to even the tone, then add extra coverage to specific patches. Keep the layer particularly thin wherever the product collects in lines. L'Oréal makeup specialists also recommend less product and thin layers; this is an application technique, not a guarantee for every face. [Source](https://www.loreal-paris.de/tipps-und-trends/make-up/welches-make-up-bei-falten-tipps)

When shine appears, gently press a clean tissue or blotting paper against the skin. Do not rub. Only then, if needed, apply a little powder to the shiny area. A Shiseido makeup consultant describes this sequence; the American Academy of Dermatology also recommends blotting excess oil with gentle pressure. [Shiseido](https://corp.shiseido.com/slqm/jp/information/information_251203.html) · [AAD](https://www.aad.org/public/everyday-care/skin-care-basics/dry/oily-skin)

#### If you do need to buy something: three options

- **Your current foundation and blotting papers.** I would choose this if you like the initial shade and coverage but your face becomes shiny later. Advantage: no need to buy another bottle of foundation. Drawback: papers alone do not fix product settling into lines, and you may need to use them again during the day. [AAD](https://www.aad.org/public/everyday-care/skin-care-basics/dry/oily-skin)
- **A skin tint.** I would choose this if avoiding a mask-like appearance matters most and partial coverage is enough. One example is **Maybelline Super Stay Skin Tint**, which the manufacturer describes as offering light to medium coverage. The tradeoff is that it also promises radiance, so it would be a less logical first trial if shine is your main concern. [Manufacturer's description](https://www.maybelline.de/alle-produkte/gesichts-make-up/foundation/super-stay-24h-skin-tint)
- **A matte foundation with light or medium coverage.** I would choose this if you want to even the tone and reduce shine. One example is **Maybelline Fit Me Matte + Poreless**, which the manufacturer describes in those terms. The tradeoff is that a matte finish can emphasize dry areas and lines; adding more product will not always fix that. [Product description](https://www.maybelline.de/alle-produkte/gesichts-make-up/foundation/fit-me-matte-poreless-makeup) · [L'Oréal application advice](https://www.loreal-paris.de/tipps-und-trends/make-up/welches-make-up-bei-falten-tipps)

Both names are category examples based on manufacturers' descriptions, not winners established by a comparative test. I cannot yet match a specific shade. A sample, if available, would help before buying a full bottle.

**Which foundation are you using now? Can you send its name or a photograph of the packaging?**


<a id="gaming"></a>

## Introductory game-technology example

**Wallhack and aimbot describe the advantage obtained; DMA describes an access mechanism.** These can be combined in one system. A "DMA aimbot" label therefore says nothing by itself about quality, safety or whether the demonstration is real.

### Three different concepts

**Wallhack and the broader ESP category** use information the game normally hides from the player: an opponent's position, outline or other data. This may involve displaying information available in memory as a separate overlay or changing rendering. One essential limit is that reading memory cannot recover a hidden position that the server never sends to the client. Riot describes precisely this *Fog of War* approach; practical use must also account for visibility changes and latency. [Riot's technical explanation](https://www.riotgames.com/en/news/demolishing-wallhacks-valorants-fog-war)

**Aimbot** automates aiming. Some variants use game data; others use computer vision to analyze visible screen pixels and adjust controls from those. "AI" may refer to a real recognition model or merely a marketing label. Screen analysis does not itself see through walls, nor does it prevent analysis of the player's resulting behaviour. *GAN-Aimbots* examines these approaches and behavioural imitation; its experimental outcome is not a guarantee for every game. [2022 study](https://arxiv.org/html/2205.07060v1)

**DMA, Direct Memory Access,** is direct hardware access to memory, also used normally by legitimate devices. A cheating system attempts to use it to obtain game data. It is not an invisibility card: an IOMMU limits which memory regions a device may access. The outcome depends on hardware, firmware and functioning protections. Microsoft documentation explicitly distinguishes Windows protection after system loading from protection during boot. [Microsoft](https://learn.microsoft.com/de-de/windows/security/hardware-security/kernel-dma-protection-for-thunderbolt)

### Who develops these systems, and what does anti-cheat do?

It helps to distinguish the author, adapter, seller and researcher. An author understands the game's data flow; another contributor may work on graphics, input automation or drivers. A seller may sell someone else's work. Researchers study similar mechanisms to test protections. These are different roles: a technical video proves neither authorship nor trustworthiness.

Anti-cheat commonly has several layers: game and system integrity checks, access monitoring, server-rule checks and behavioural analysis. A kernel driver provides different visibility from an ordinary program, but does not solve every problem. Architectures differ: Epic's described EAC Linux v2 plans to use platform protections and eBPF without its own anti-cheat kernel module. [Epic's architecture](https://onlineservices.epicgames.com/news/introducing-easy-anti-cheat-linux-v2?lang=ja)

**Server authority** means the server makes the final decision about game state. The server must still evaluate client requests; a central server alone does not prevent sending unnecessary information or automated aiming. [Unreal's networking model](https://dev.epicgames.com/documentation/en-us/unreal-engine/networking-overview-for-unreal-engine)

**Self-reported developer experience:** Inferna Studio writes that its own anti-cheat mistakenly banned a developer's account. This is one author's account, not an independently verified test or a measurement of false-ban frequency. It helps explain why a suspicious signal and proven cheating are not synonyms. [Experience report](https://infernastudio.com/articles/our-anti-cheat-banned-a-player-it-was-us)

### Where to learn, and which claims to question

[Reverse Engineering Stack Exchange](https://reverseengineering.stackexchange.com/tour), Ghidra project discussions and game-engine developers' documentation are useful for technical questions. **Ghidra** helps inspect compiled code; **debuggers** such as WinDbg let you inspect your own program's execution, memory and registers. These are general research tools. [Ghidra](https://github.com/NationalSecurityAgency/ghidra) · [WinDbg](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/)

When assessing a claim, I would ask three things:

- **What exactly is being demonstrated?** Version, environment, input, complete output and known limitations are more informative than a montage of selected wins.
- **Can the claim be tested?** "Never detectable," "works everywhere" and "AI, therefore safe" are not technical evidence.
- **Do the sources agree?** Repository history, the author's explanation and a repeatable demonstration help establish provenance. Review counts or a request to disable protections do not by themselves establish trustworthiness.

**A useful next step:** in your own offline Unity or Unreal scene, create two characters and a wall, enable the developer's diagnostic display, and compare "the data exists" with "the object is visible." Then use your own local client/server example to check which data is transmitted. This makes the source of the problem and the purpose of the protection easier to understand.


<a id="architecture"></a>

## Introductory agent-architecture example

Checked on November 9, 2026. This is the result of actual research and a testable architecture proposal; the external projects in this example have not been installed or measured.

### Question

"How can we build a local AI agent that leaves model weights unchanged, keeps a small experience library, and improves both its actions and the method it uses to choose what to learn from experience?"

### Answer

**I would start with an existing memory-and-skills foundation and test one addition: whether a particular memory actually improves the next decision.** Saving advice in memory does not establish that the model understood it or applied it in the right situation.

This is a promising direction, but it would be unjustified to say that nobody has implemented it. MemEvolve already studies development of both the agent's experience and the memory architecture itself. EvolveLab divides that into four changeable operations: transforming, storing, retrieving and managing experience. It provides a concrete research basis for the proposal. [Study](https://proceedings.mlr.press/v306/zhang26fa.html)

#### What can already be used

| Foundation | Why it is relevant | What to check before choosing |
|---|---|---|
| **ReMe** | File-based, selectable memory; the documentation also describes Hermes integration. Initial text search does not necessarily require a separate embedding model. | The specific Hermes version, automation-model costs and whether the chosen configuration can meet our memory limit. |
| **Memento-Skills** | An existing project whose workflow selects and executes skills, assesses failures and rewrites skills while leaving the base model unchanged. | How well that cycle works with our model and tasks; the project's demonstrations cannot answer that for us. |
| **MemEvolve / EvolveLab** | The most direct foundation for experiments that also change how experience is selected and managed. | Integration of research code, the specific module and its dependencies; it is not an everyday agent tested here. |

[ReMe primary source](https://reme.agentscope.io/zh/overview) · [Memento-Skills authors' description](https://www.memento.run/research/skills/) · [MemEvolve code](https://github.com/bingreeky/MemEvolve)

These repositories specify the Apache-2.0 licence; when adopting individual files, rights for dependencies, models and data must be checked separately. This evaluation read documentation and repository descriptions; it did not reproduce their results.

#### An addition worth testing

My proposal is **a library of short experience cards with applicability conditions and a tested selection procedure**. It is not a claim to the world's first architecture. The testable objective would be fewer repeated mistakes within a limited storage and search budget.

A card would contain the situation, action, outcome, evidence location and a condition under which the advice does not apply. For example: "If a search snippet and a project file disagree, check the specific current file. Documentation alone does not establish that the function works on your computer."

Before work, the agent would receive only relevant cards. Afterwards, it would save one material lesson or a supported conclusion that no new lesson was obtained. A separate test would compare three variants: no cards, the current selection procedure and the new selection procedure. That can distinguish the library's benefit from the model's existing ability to answer the question.

The need for such a test is reinforced by "Large Language Model Agents Are Not Always Faithful Self-Evolvers": its authors observed that models sometimes ignore or misinterpret compressed experience. This does not establish that short memory is useless; it requires checking whether the compressed version retains what the decision needs. [Study](https://arxiv.org/abs/2601.22436)

Practical experience also supplies a specific lead: after 24 generations of context compression, amtr's author describes a problem where a working hypothesis turns into an apparently confirmed conclusion. The author's adjustment is to preserve both what has been checked and what remains untested. This is the author's own observation, not proof of general effectiveness. [Author's experience and code link](https://zenn.dev/naoto256/articles/amtr-working-memory)

#### When a combined solution would be preferable to an existing one

I would first compare with a ReMe or Memento-Skills configuration using the same model, tools, memory budget and adaptation effort. If a small configuration change to an existing project meets the requirement, I would choose that.

I propose an initial test on 24 previously unused tasks, including inapplicable and outdated lessons. Before seeing results, we would set a target such as at least 20% fewer repeated mistakes, no new critical error and no increase in search actions. A separate reader would check whether the recommendation, rationale and next action are understandable. **20% is a proposed decision threshold, not an achieved result.** The small test would help decide whether to continue; it would not establish universal superiority.

Planning estimate: 12–24 working hours for a small connector, 16–32 hours to prepare tasks and evaluation, and 12–24 hours for fixes and a repeatable demonstration. That totals 40–80 hours, roughly 1–2 weeks for one developer with a working environment. Three variants times 24 tasks means 72 agent-task executions, not 72 individual model requests. The actual number and duration of model calls must first be measured in a small trial.

Electricity would be calculated as the measured average power of the entire computer in kW multiplied by active hours. Cost would use the actual tariff or service consumed. These quantities have not been measured here. I would initially reserve 2–4 hours a week for routine maintenance until the frequency of dependency issues and failures becomes clear.

**Decision: there is a basis for a bounded comparative experiment. There is not yet a basis for promising that our combined solution will outperform existing ones or that it already runs autonomously.**
