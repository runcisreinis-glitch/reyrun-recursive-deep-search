# Query transformations and practical examples

These are reusable query patterns, not a claim that every example string below was executed. Actual dated searches and source records belong in a research ledger. Keep the user's function fixed while changing vocabulary and discovery channel.

## 1. Improve an agent without retraining its language model

Original need: learn reusable procedures from failures and successful runs; keep model weights fixed.

| Route | EN | DE | ZH | JA |
|---|---|---|---|---|
| Direct | agent skill optimization execution feedback | Agenten Skill-Optimierung Ausführungsfeedback | 智能体 技能优化 执行反馈 | エージェント スキル最適化 実行フィードバック |
| Procedural memory | procedural memory failed trajectories | prozedurales Gedächtnis Fehlversuche | 程序性记忆 失败轨迹 | 手続き記憶 失敗軌跡 |
| Other mechanism | library learning repeated programs | Bibliothekslernen wiederkehrende Programme | 程序综合 可复用函数 库学习 | プログラム合成 再利用 ライブラリ学習 |
| Contrary evidence | skill evolution regression held-out leakage | Skill Optimierung Regression Testdatenleck | 技能进化 回归 测试集泄漏 | スキル進化 性能劣化 評価データ漏洩 |

Follow a promising paper to its actual evaluator and skill writer. Search commit history for an unimplemented write-back step. Library learning and compiler optimization are functional analogies, not synonyms for recursive improvement.

**Ready track:** compare working upstream optimization frameworks for the exact artifact being optimized.

**Synthesis track:** consider a trajectory-to-procedure extractor plus a tested optimizer only if the combination removes a demonstrated failure that the ready framework's ordinary adapter cannot solve. A cheap trial uses new tasks, fixed budget and a measurable reuse or error-rate criterion.

## 2. Reverse engineering and behavior recovery

Original need: recover a documented input/output behavior or file/protocol structure from authorized samples.

| EN | DE | ZH | JA |
|---|---|---|---|
| protocol inference input output traces | Protokollinferenz Ein-Ausgabe-Spuren | 协议推断 输入输出轨迹 | プロトコル推論 入出力トレース |
| program behavior equivalence differential testing | Verhaltensäquivalenz differentielles Testen | 程序行为等价 差分测试 | プログラム動作等価性 差分テスト |
| binary lifting intermediate representation | Binäranalyse Zwischendarstellung | 二进制提升 中间表示 | バイナリ解析 中間表現 |
| file format grammar inference incomplete implementation | Dateiformat Grammatik lernen unvollständige Implementierung | 文件格式 语法推断 未实现 | ファイル形式 文法推論 未実装 |

Search by the required observable function, then exact format names, signatures, symbols or error messages. Inspect independent format implementations, author artifacts, tests and patches. Do not equate a visually similar interface with equivalent behavior.

A valid synthesis names the missing parser or transformation, compatible components and differential tests. Claims such as “90% equivalent” require an explicit feature set and measured denominator.

## 3. Photographic images through code

Original need: recover scene structure from video and alter a specific part while retaining photographic appearance.

| EN | DE | ZH | JA |
|---|---|---|---|
| inverse graphics video scene reconstruction | inverse Grafik Szenenrekonstruktion Video | 逆图形学 视频 场景重建 | 逆グラフィックス 動画 シーン再構成 |
| multi-view geometry material estimation | Mehrbildgeometrie Materialschätzung | 多视图几何 材质估计 | 多視点幾何 材質推定 |
| image based rendering texture synthesis | bildbasierte Darstellung Textursynthese | 基于图像的渲染 纹理合成 | 画像ベースレンダリング テクスチャ合成 |
| relighting view synthesis disocclusion failure | Neubeleuchtung Ansichtssynthese Verdeckung Fehler | 重光照 新视角合成 遮挡 失败 | 再照明 新視点合成 遮蔽 失敗 |

Look outside text-to-image model catalogues: graphics papers, renderer examples, photogrammetry code, tracking modules, texture reconstruction and simulation. High source resolution alone does not establish unobserved geometry, material or view coverage.

For a mountain-to-snow edit, separate geometry, material, accumulation, illumination and temporal coherence. Compare complete tools with a component pipeline on held-out views. A view or content never observed must be inferred or synthesized; label the prior used.

## 4. Find a useful component in unfinished work

Original need: a small reusable module, not a whole unfinished platform.

| EN | DE | ZH | JA |
|---|---|---|---|
| not implemented evaluator write back | nicht implementiert Evaluator Rückschreiben | 未实现 评估器 写回 | 未実装 評価器 書き戻し |
| artifact supplementary source code | Artefakt Begleitmaterial Quellcode | 补充材料 源代码 附件 | 補足資料 ソースコード 添付 |
| abandoned fork fixed dependency | archivierter Fork Abhängigkeit behoben | 停止维护 分支 依赖修复 | 開発停止 フォーク 依存関係 修正 |

Follow paper → author → artifact/archive → precise revision → module → license → smallest test. Examine fork differences and unmerged fixes. State what was actually inspected.

An overlooked component is useful when its contract fits the missing function and it reduces the work or improves the result. Its obscurity is not evidence of value. Reject it when a ready tool supplies the same function more reliably at lower total cost.

## Cross-language procedure

Build several term families rather than translating one sentence four times. Use a lexical resource to suggest terms, then confirm native technical usage in primary sources. Map meanings across languages, retain English technical terms when local authors use them, and explicitly record semantic shifts.

For example, “self-improvement” may lead to motivational content while “execution-feedback-driven skill revision” exposes the needed mechanism. A compiler's rewrite system may supply an implementation pattern even when it never mentions an AI agent.

Keep at least one negative-control query or candidate: it shares topical words but lacks the required input/output behavior. If the search process ranks it highly, revise the relevance test.
