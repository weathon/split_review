## Summary

IGL-Bench is a comprehensive benchmark for imbalanced graph learning (IGL) that integrates **24 IGL algorithms** across **16 graph datasets** under standardized protocols. It systematically evaluates effectiveness (RQ1), robustness to varying imbalance ratios (RQ2), classifier boundary quality (RQ3), and efficiency (RQ4), covering both class-imbalance and topology-imbalance at node and graph levels. The paper fills a genuine gap: prior IGL works used inconsistent datasets, splits, and metrics, making results incomparable.

---

## Strengths

- **Substantially larger scale than any prior IGL comparison.** The benchmark integrates 24 distinct IGL algorithms and 16 diverse graph datasets covering node-level and graph-level tasks, and both class-imbalance and topology-imbalance problems (lines 8, 43, 86–103). Prior IGL papers typically compare only a handful of methods on a few datasets.

- **Multi-dimensional evaluation across effectiveness, robustness, and efficiency.** Unlike prior IGL papers reporting only accuracy on a single split, this benchmark systematically evaluates three dimensions (RQ1–RQ4, Sections 4.1–4.4), including quantitative control of imbalance ratios from balanced to extreme (ρ=100, line 181) and time/GPU-memory analysis (Figure 6).

- **Standardized experimental protocol enabling fair comparison.** The paper identifies that prior IGL works used inconsistent datasets, splits, and metrics (lines 37–40), and addresses this with a uniform 1:1:8 train/val/test split (line 111), consistent data processing, and a fixed set of metrics (Accuracy, Balanced Accuracy, Macro-F1, AUC-ROC) over 10 runs.

- **Specific, actionable findings that go beyond reporting numbers.** The benchmark produces concrete insights unavailable from individual papers: node-level class-imbalance and global topology-imbalance are orthogonal issues (line 185); data-augmentation methods outperform resampling on 6 of 9 datasets (lines 137–138); resampling-based methods show better robustness than re-weighting under varying imbalance ratios (lines 180–181); nearly half of IGL algorithms run out of memory on ogbn-arXiv (line 280).

- **Systematic coverage across the homophily spectrum.** Node-level datasets span strong homophily (Cora) to strong heterophily (Actor, Squirrel) (line 93). The analysis reveals performance patterns varying with homophily — e.g., Tail-GNN and GraphPatcher excel on high-homophily datasets while Cold Brew performs better on high-heterophily datasets (line 146).

- **Practical scalability constraints documented.** The efficiency analysis on ogbn-arXiv shows that nearly half of the 24 algorithms run out of memory (line 280), providing an important real-world deployment insight rarely reported in individual IGL papers.

---

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are supported by the presented evidence, and no verifiable issue from the paper as written undermines its main contribution.

### Minor

- **The RQ3 analysis on classifier boundaries is conceptually weak and does not convincingly answer its stated question.** The paper uses t-SNE visualizations (qualitative) and Silhouette scores (which measure cluster cohesion, not boundary clarity) to claim that "performance improvement in downstream tasks results from clearer classification boundaries" (lines 267–271). No quantitative correlation is established between Silhouette scores and task performance, and the connection between the evidence presented and the conclusion is asserted rather than demonstrated. This section either needs significant deepening (e.g., measuring classification margins, analyzing calibration, correlating scores with performance across algorithms) or should be dropped.

- **The interaction between the 1:1:8 split and imbalance induction is not discussed.** On a dataset like Cora (~140 labeled samples/class originally), a 1:1:8 split yields ~14 training samples per class. With an extreme imbalance ratio (ρ=100), the minority class would have essentially 0–1 training samples. The paper does not describe how such scenarios were constructed or handled (line 111), and does not discuss whether the validation and test sets were kept balanced or imbalanced. This level of detail is central to the benchmark's reproducibility promise.

- **Hyperparameter configuration for the 24 algorithms is not described in the main text.** The paper states it unifies experimental settings (lines 39, 45) but does not specify whether each algorithm's hyperparameters were tuned on a validation set or taken from the original papers, whether the same hidden dimensions, learning rate, and optimizer were used across all algorithms, or how backbone architectures were standardized. If this information is in the (stripped) appendix, it should be cross-referenced in the main body; otherwise it is a gap that limits reproducibility.

- **The topology-imbalance definition groups distinct phenomena under one label.** Definition 2 (lines 70–72) lumps together (a) imbalanced node degree distribution and (b) under-reaching/over-squashing phenomena. Item (b) is an architectural limitation of GNN depth relative to graph structure, not an imbalance in the data distribution per se. While the paper is transparent about its definition, this conflation blurs the distinction between data-level imbalance and architectural reachability — problems that call for fundamentally different mitigation strategies. A justification or refinement of this categorization would strengthen the conceptual foundation.

- **No dedicated limitations or scope discussion.** The paper does not explicitly discuss the benchmark's limitations: most datasets are small and homophilic; imbalance is artificially induced; only semi-supervised node classification and graph classification are covered (no link prediction, no regression); and complex graph types (heterogeneous, directed, dynamic, temporal) are excluded. A limitations section would help users calibrate the benchmark's applicability. (The "Future Directions" section touches on some of these but does not frame them as limitations of the current work.)

- **Dataset statistics (number of nodes, edges, features, classes, homophily ratios) are not provided in the main text.** Lines 93–97 describe datasets qualitatively but omit basic quantitative characteristics that readers need to interpret results. If this information is in the appendix, a summary table or pointer should appear in the main paper.

### Trivial
- **LTE4G, TAM, and TOPOAUC are listed under both class-imbalance (line 100) and topology-imbalance (line 102) categories,** but the paper does not clarify whether they are configured differently for each setting (different hyperparameters, loss functions, or training objectives). A brief note would resolve this ambiguity.

---

## Nice-to-Haves

- **Simple non-graph-specific baselines** (weighted cross-entropy loss, random oversampling of node features, SMOTE on features) would help contextualize whether the graph-specific machinery in IGL algorithms is actually necessary. The paper is a benchmark for *graph-specific* IGL (line 42), so this is outside its stated scope, but adding 2–3 such baselines would substantially strengthen the conclusions the community can draw from the benchmark.

- **Statistical significance testing** (e.g., paired t-tests, Wilcoxon signed-rank, or a critical difference diagram) would add rigor to the algorithm rankings, though it is not standard practice in most GNN benchmark papers. With 24 algorithms across 16 datasets, some apparent "wins" are expected by chance.

---

## Removed Points

These points were considered but removed during synthesis; they are flagged for transparency:

1. **Missing imbalance ratio definitions** (harsh critic point 3, sub-point about exact ratios) — The paper explicitly references Table `\ref{tab:imb_definition}` (lines 80, 172) which defines ρ for each imbalance scenario. This table was in the appendix, which is stripped by the PDF parser; the hard rules require removing criticisms about missing appendix content.

2. **Claims that the paper does not specify imbalance construction procedure** (harsh critic point 3) — The reference to Table `\ref{tab:imb_definition}` and the qualitative "Low, Mid, High" levels (lines 285, 301, 315, 331) with ρ=100 for extreme (line 181) indicate the definitions existed in the full submission. 

3. **Criticism about dataset statistics being absent** — These likely appear in a table in the stripped appendix (the paper lists 16 datasets by name and category, lines 93–97, which is appropriate for the main body's scope).

4. **Criticism that the paper is not "first" to survey IGL** — The paper claims "first open-sourced benchmark" (line 42), which is a different claim from "first survey." A 2023 survey does not invalidate the benchmark claim.

---

## Novel Insights

None beyond the paper's own contributions. The two reviewer inputs largely converge on the same set of observations; no novel insight emerges from their interaction that is not already present in the paper or its straightforward critique.

---

## Suggestions

1. **Strengthen RQ3 by either deepening it or removing it.** Replace qualitative t-SNE plots with a quantitative analysis correlating embedding-space metrics (e.g., classification margin, per-class Silhouette scores) with downstream task performance across algorithms. If this cannot be done convincingly, drop the section to avoid weakening the otherwise rigorous empirical narrative.

2. **Add a brief paragraph specifying the imbalance construction procedure** — how the long-tailed distribution is created (downsampling majority? upsampling minority?), whether the validation and test sets are balanced or imbalanced, and how the 1:1:8 split is reconciled with extreme imbalance ratios on small datasets.

3. **Add a "Limitations" subsection** that explicitly discusses the benchmark's boundaries: artificial (not naturally occurring) imbalance, small-scale datasets, and the restriction to semi-supervised node classification and graph classification (no link prediction, regression, or complex graph types).

---

## Score and Decision

**MY FINAL SCORE:** <score>7.0</score>
**MY FINAL DECISION:** <decision>Accept</decision>