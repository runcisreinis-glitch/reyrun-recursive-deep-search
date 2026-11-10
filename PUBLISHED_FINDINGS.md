# Published findings and limits

The final research set contains 10 everyday questions, 10 questions of medium difficulty across several fields, and 10 difficult questions. It keeps 12 earlier cases and adds 18, for 48 distinct main research tasks across the final and historical collections. Seven new advanced cases include full mathematical proofs or derivations and executed calculations. Both 30-case collections are available in full in English and Latvian.

The separate search-strategy trial did **not** establish an accuracy improvement. The candidate was rejected as the new baseline, and the recorded decision remains `no_gain`.

## The three-task comparison

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

## Research coverage and corrections

The final 30 cases report 156 executed queries. Each case searched in English, German, Chinese and Japanese. A query in a language does not establish that a supporting primary source in that language was found and read. Access failures and limited source reads remain disclosed in the answers.

The original selection was too concentrated on IT in its medium group and lacked completed advanced mathematics tasks. The revised selection addresses those gaps while preserving the original answers. The historical total of 147 included four declared E10 queries whose full original outputs were not retained. The supported historical count is 143 distinct queries with retained receipts; missing receipts have not been reconstructed as if they were original evidence.

The questions were designed for validation, and simulated clarifications are labelled. One agent performed the main research for each example, followed by the reported reviews. The set does not demonstrate four independent agents searching every case. The mathematical arguments were read and checked against the stored calculations; no formal proof-assistant certification is claimed. The [release report](validation/2026-11-09-beta3/release-report.en.md) gives the retained findings and qualifications.

## What improved in the software

The recorded release passed 82 software tests. Two reproduced defects were repaired: an older lesson card could hide a newer contrary observation, and an unreferenced evidence object near the memory limit could prevent compaction from being saved. The current source, tests, calculation programs and calculation outputs are included so readers can inspect and rerun them. Software mechanism tests do not establish higher search accuracy.

All 18 new main tasks completed a recorded learning cycle, and 15 later tasks loaded earlier lessons. The chat orchestrated those operations. Loading experience does not prove that every subsequent answer improves or that an unattended service is running. The separate two-task execution demonstration is described here only at the level of its reported outcome: a later task loaded a saved lesson. Its internal execution records are excluded.

Useful fixes and compact lessons were retained. The prerequisite-prioritization candidate was not promoted. Lesson relevance, a trial with a cost objective, and the additional benefit of multiple search languages remain hypotheses requiring new tasks and fixed acceptance criteria.

## What this publication contains

This is an authored account of the findings. Full evaluator outputs, instruction snapshots, execution records, memory snapshots, raw logs, tool-query dumps and internal receipts are not included, either as separate files or copied into the combined experiment report. Those omissions limit independent reconstruction of the original orchestration. They do not remove the complete research answers, mathematical arguments, calculation code, reported negative result or stated limitations.

Read the [publication scope](PUBLICATION_SCOPE.md), [English research and experiment report](EXPERIMENTS.md), or [Latvian report](EXPERIMENTS.lv.md). The [file manifest](file-manifest.json) identifies the exact files in this edition. This publication makes no antivirus certification, general research-quality guarantee or claim of a permanently running improvement service.
