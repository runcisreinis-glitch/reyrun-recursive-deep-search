# REYRUN Recursive Deep Search: validation and development report

Release 2.0.0-beta.3 · research conducted on November 9, 2026.

The final validation set contains 10 everyday questions, 10 moderately difficult questions across different fields, and 10 difficult tasks. Each of the seven new advanced tasks includes a complete mathematical proof or derivation and a calculation that was actually run. Two reproduced failures in the learning memory were fixed, and the validated code passed 82 tests. A separate trial of a new search strategy returned **no_gain**: the candidate was not adopted as the new baseline method.

[All 30 answers](30-examples.en.md) · Evidence register · Machine-readable summary · [Compact lessons](../../references/observed-lessons.md).

The internal records referenced here are omitted from this edition; see [publication scope](../../PUBLICATION_SCOPE.md).

## 1. Why the selection changed

The original 30 research tasks were actually carried out, but an independent audit found that the medium group was too concentrated on IT and that the difficult group lacked completed advanced mathematics tasks. The final selection retains 12 suitable cases and adds 18 new ones. The original answers have not been deleted or rewritten: the [historical edition in English](../2026-11-09/30-examples.en.md) remains available. There are 48 distinct main tasks in total; the three comparison tasks are counted separately.

The internal records referenced here are omitted from this edition; see [publication scope](../../PUBLICATION_SCOPE.md).

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

## 2. What answer validation covers

Each case retains its answer, sources, claim-to-source links, and the SHA-256 of its original file. New calculations also retain their code and output. The root agent independently read all seven mathematical proofs written by the new author, checked the arguments, and compared them with the stored numerical results. This is not certification by a formal proof assistant. See the mathematics review.

The internal records referenced here are omitted from this edition; see [publication scope](../../PUBLICATION_SCOPE.md).

One agent carried out the main research for each example, followed by the independent review described here. This set does not demonstrate four independent agents at the question-formulation and search stages of every case. An acceptance audit from four separate perspectives was actually performed for the strategy comparison described below.

The calculations and reasoning in the seven subject-area answers were independently reviewed. An additional agent checked the four new everyday answers and the historical-address/window cases against the stored primary-source excerpts, and repeated their calculations. There is no claim that every external source was reopened on the web in every audit. See the subject-area review and six-answer audit.

The internal records referenced here are omitted from this edition; see [publication scope](../../PUBLICATION_SCOPE.md).

Mathematical formatting and citation links were adapted for the public edition. Spacing was corrected in NE02; the ambiguous opening of NP04 was clarified to read, in translation, "A cartridge containing only activated carbon..." The original research answers remain unchanged. The export mapping records the checksums of both versions and the reasons for each edit.

The internal records referenced here are omitted from this edition; see [publication scope](../../PUBLICATION_SCOPE.md).

## 3. Learning between searches

All 18 new main tasks completed an actual begin/end record cycle. Three thematic series started with empty test memory; **15 subsequent tasks loaded previously saved lessons**. Their identifiers and the agent's record of using a lesson or finding it inapplicable are in the lifecycle evidence. For example, distinguishing quantity from unit was carried over from flour to paint and dry/cooked rice. The earlier numerical lessons were marked as inapplicable to the case about the material of drinking glasses.

The internal records referenced here are omitted from this edition; see [publication scope](../../PUBLICATION_SCOPE.md).

The chat orchestrated these begin/end steps. The strict file/reference validator was also run on the 14 new subject-area and mathematics answers. This does not establish that an automatic background service started those 18 research tasks. The previously saved two-task demonstration through the strict connector documents a separate real connector run and the loading of its lesson by the next task.

The internal records referenced here are omitted from this edition; see [publication scope](../../PUBLICATION_SCOPE.md).

The recurring cycle is executable: load relevant lessons → carry out the task → save useful findings, failures, and unresolved points → investigate a specific improvement hypothesis → compare it with the existing method → accept it only if the criteria are met. Loading lessons alone does not prove that every subsequent answer improves. This release tests memory operation and the selection of a separate candidate as two distinct things.

## 4. Two measured software improvements

| Failure before the fix | What changed | Actual verification |
| --- | --- | --- |
| An earlier lesson card could hide a later contradictory failure observation. | Observations and cards now share one chronological selection of 16 entries. | The next begin record also contains the newer failure text. |
| At the 5 MiB limit, an unreferenced evidence object left by a failed write prevented even the result of memory compaction from being saved. | Before the atomic save, only already unreferenced objects from the explicitly approved compaction plan are removed. Evidence still in use is retained until the state is successfully replaced. | With 5,242,680 bytes used and 200 bytes free, compaction succeeded and left 4806 bytes. A separate test with an injected write failure preserved the previous state and its evidence. |

Before, after, regression review, 82-test receipt, and full test log. These are explicitly labelled synthetic mechanism tests. Fixing a software failure does not establish an improvement in search accuracy.

The internal records referenced here are omitted from this edition; see [publication scope](../../PUBLICATION_SCOPE.md).

## 5. The separate search-strategy comparison

The candidate added one technique: first check the least-supported necessary condition that could change the decision. The idea came from applying claim/evidence reasoning to the search process. A separate idea involving unit typing was deferred to avoid combining two changes in one trial.

The criteria and budget, three tasks and correctness checks, existing policy, and candidate were fixed before either side ran. The underlying skill was not weakened for the baseline. Two fresh agent contexts ran the two sides with the same declared model configuration, task order, and limits: no more than 16 web actions, 8 queries, 12 reads, and 12 minutes per task. A failed request also counts as an action.

The internal records referenced here are omitted from this edition; see [publication scope](../../PUBLICATION_SCOPE.md).

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

Across the three new comparison tasks, both methods met all predefined answer criteria. The candidate used 43 web actions against the existing method's 47 but did not achieve the required accuracy gain, so it was not adopted as the new baseline. The result is **no_gain**, not a claim that the candidate is worse in every use. The saving of four actions is an observation from this one pilot; the candidate's combined task duration was also longer. An auditor recalculated the table's durations consistently, from the first real request to completed artifacts. The authors' own differently defined figures of 461.75 and 569.59 seconds are retained separately and do not support a direct speed comparison. The criteria were not switched to cost after the results became known. See the automatic evaluation, register of all six runs, and [complete answers in English](comparison/answers.en.md).

The internal records referenced here are omitted from this edition; see [publication scope](../../PUBLICATION_SCOPE.md).

Four different agents, none of whom wrote either side's answers, provided the optimistic, skeptical, conservative, and innovative reviews. These are not four opinions invented by one agent. Checking that fields are present is not a human readability study. The "innovation" score here measures a documented useful application of a component, not a historically novel discovery.

The internal records referenced here are omitted from this edition; see [publication scope](../../PUBLICATION_SCOPE.md).

The trial covers only three designed tasks and one answer per side. It used a shared file system with an instruction boundary, not operating-system isolation; model identity is declared by the environment. After the candidate had been fixed, the designer also prepared the initial reference answers. The root agent independently checked them against primary sources and fixed them before execution. Because agent slots were limited, the two sides started about six minutes apart. These limits prevent claims of statistical or universal superiority.

The baseline's completion input contained a schema error: the lesson-reference list included four files where three were allowed. The controller preserved the rejection and separate repair records, reducing only that reference list. All four observation-evidence references, the answers, durations, and queries remained unchanged. The answers were not rerun, and there was no hidden second attempt.

The internal records referenced here are omitted from this edition; see [publication scope](../../PUBLICATION_SCOPE.md).

After the rejection, another actual loading-verification cycle loaded the saved decision and unchanged baseline policy. It is not counted as another new web research task.

The internal records referenced here are omitted from this edition; see [publication scope](../../PUBLICATION_SCOPE.md).

## 6. What was retained, rejected, and deferred

| Status | Specific content |
| --- | --- |
| Retained | Both fixes for reproduced failures; source/answer checksums; compact lessons about units, concentration, number/object identity, and prerequisites for proof. |
| Rejected as the new baseline | The prerequisite-prioritization candidate did not achieve the required accuracy gain. Its results and the reason for rejection remain available. |
| Deferred with a testable hypothesis | Lesson-relevance selection, a separate trial with a cost objective, and an evaluation of the additional benefit of languages. These need new tasks and a predefined acceptance criterion. |

Memory is bounded. A compressed conclusion cannot retain all its source material indefinitely; raw evidence is discarded only under a documented plan. This release's complete private research records are stored separately. The public material contains the authors' answers, calculations, and compact provenance records, without full-text copies of third-party pages.

## 7. Corrected historical accounting and distribution scope

The original report's total of 147 included four declared initial E10 queries whose full output from that run was not retained. The independent check confirms 143 distinct queries with retained original receipts. The existing E10 recovery reads are linked to their sources; the missing receipts have not been invented. The new final selection's count of 156 applies only to its 30 cases.

The internal records referenced here are omitted from this edition; see [publication scope](../../PUBLICATION_SCOPE.md).

The original release used the public distribution page at https://reyrun-rekursive-deep-search.runcisreinis.chatgpt.site for its download, documentation, validation report, examples, video, and draft Facebook post. At that time, public mirrors on GitHub, Hugging Face, ModelScope, and Gitee had not been created. No Facebook post had been sent on the author's behalf.

Publication update, November 10, 2026: the public [GitHub repository](https://github.com/runcisreinis-glitch/reyrun-recursive-deep-search) has been created and its ownership and public visibility checked through the API. Repository creation is separate from verification that every file has been uploaded. The publication manifest records the files to compare after the upload. This update does not claim completed upload verification.

This is a research skill and an executable learning cycle for a connected agent environment. Downloading the package or pasting instructions into an ordinary chat does not itself start a round-the-clock process or guarantee persistent memory. Acceptance testing for a specific installation consists of a real first task, a second task, and evidence that the second task loaded experience from the first.
