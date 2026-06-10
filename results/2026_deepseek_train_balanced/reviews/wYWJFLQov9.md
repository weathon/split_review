## Summary

ST-GCond proposes a graph dataset condensation method designed for transferability across tasks and datasets — a genuinely under-explored problem. The method combines three components: (1) MAML-style meta-optimization over label subsets for cross-task adaptability, (2) multi-teacher self-supervised distillation to inject "universal knowledge" for cross-dataset generalization, and (3) mutual information regularization to reconcile supervised and self-supervised objectives. Experiments on 10 datasets show strong results: state-of-the-art on 14/15 single-task settings, and 2.5%–18.7% improvements over existing condensation methods in cross-dataset scenarios.

## Strengths

- **First principled approach to transferable graph dataset condensation.** The paper identifies a genuine gap — existing graph condensation methods (GCond, SFGC, GEOM) are designed for a single dataset and task, and the paper provides concrete empirical evidence (Figures 1c, 1d) showing that they fail in cross-task and cross-dataset scenarios. This motivation is well-grounded and non-trivial.

- **Strong and broad empirical results.** ST-GCond achieves SOTA on 14 out of 15 dataset-ratio combinations in the single-task setting (Table 1), including "lossless" results (exceeding full-dataset GCN) on 3 of 5 datasets. In cross-dataset settings, it outperforms existing condensation methods by 2.5%–15.5% (node-level) and 4.1%–18.79% (graph-level) across 8 target datasets (Tables 2, 3). The evaluation covers 6 node-level and 5 graph-level datasets against 10 baselines — a thorough experimental scope.

- **Non-trivial adaptation of MAML to the condensation setting.** The meta-optimization (Section 3.2) is not a trivial copy of MAML: it samples class subsets as sub-tasks, performs fast adaptation on copies of the condensed graph parameters (not model parameters), and computes a meta-loss across adapted copies. The use of KRR as the surrogate condensing objective (Eq. 2) is also a deliberate design choice to enable the inner-loop adaptation, which gradient-matching or trajectory-matching objectives would not support cleanly.

- **Practical multi-teacher design that avoids per-task retraining.** Rather than training SSL models during condensation (which would be prohibitive), the method loads pre-trained SSL teachers and unifies their outputs into a common d-dimensional space via a soft synthetic label Yₛˢ (Section 3.3). The ablation (Figure 4c) shows increasing performance with more teachers, confirming that this design provides meaningful benefit.

## Weaknesses

### Major

None. The paper's core claims are supported by empirical evidence; no single issue invalidates them.

### Minor

- **"Task-disentangled" overclaims what the method actually does.** The method partitions the label set into subsets and applies MAML-style meta-optimization (Section 3.2). This is multi-task meta-learning over random class partitions, not representation disentanglement. There is no mechanism that separates task-specific from task-agnostic knowledge — no decomposition of latent factors, no orthogonalization, no independence constraints. The term "disentangled" suggests a principled information separation that the method does not implement. The method itself is sensible; the label is misleading.

- **Cross-task (type-changing) results are discussed selectively in the text.** For link prediction (Table 4), the paper states "better AUC and AP metrics on Cora, and the AP metric on Citeseer" (line 164) but omits Citeseer AUC entirely. For node clustering (Table 5), the text gives no concrete numbers — only a qualitative statement about "more pronounced improvements" with a speculative explanation. The tables (embedded as images) likely contain the full numbers, but the selective textual discussion weakens the reported evidence for cross-task transferability, which is a core claim. The abstract's "2.5% to 18.7%" range bundles this weaker scenario with the stronger cross-dataset results.

- **KRR-ST is listed as a baseline but never discussed in the results.** KRR-ST (Lee et al., 2024) is described as "one self-supervised condensation method" (line 34) and included in the baseline list (line 132). Since KRR-ST is explicitly designed for *transferable* dataset distillation, its omission from the cross-dataset and cross-task result discussions is a notable gap. It should either be included in the comparison or an explanation given for why it was excluded from the transfer settings where it is most relevant.

- **The sparsification threshold for adjacency generation is not addressed.** The structure generator produces Aₛ = g_φ(Xₛ) − δ (line 60), where δ filters edges below a threshold. Computing gradients through this thresholding operation is non-trivial — the paper does not discuss whether a straight-through estimator, soft thresholding, or another technique is used. Since the meta-optimization requires second-order gradients, this missing detail is relevant for reproducibility.

- **The Mutual Information loss has a conceptual tension with the stated goal that is not discussed.** The paper motivates soft labels Yₛˢ as carriers of "universal knowledge" beyond the supervised task, but then maximizes I(Yₛˢ; Yₛʰ) — which encourages the soft labels to be *more predictable from* the hard supervised labels. This seems to incentivize convergence toward supervised-task information rather than preserving orthogonal universal knowledge. The paper shows empirically that this works (ablation in Table 6), but does not address the apparent tension. A brief discussion would resolve this.

### Trivial

- Line 23: "underperform by 4.2% compared to the ground truth" — "ground truth" is ambiguous (full-dataset GCN training? some oracle?). The context makes it interpretable but the phrasing is imprecise.

## Nice-to-Haves

- A disentanglement analysis to support the "task-disentangled" claim (e.g., probing the condensed graph's representations on tasks orthogonal to the supervised labels).
- Computational cost comparison (condensation time) against GCond, SFGC, GEOM to help practitioners weigh the trade-off.

## Removed Points

These points were flagged during review aggregation but removed per filtering rules:

- **Theorem 1 missing proof/justification** — Removed per the instruction that "weaknesses about missing appendix, missing proofs in appendix, or absent references" should be removed because the parser strips those sections. The theorem statement is present in the main text; any proof or derivation may reside in the stripped appendix. The rule overrides this criticism.
- **Missing hyperparameters (α, β, inner loop LR)** — Sentence at line 134 is truncated ("We provide our..."), likely a parser artifact. These details may exist in the original submission's appendix.
- **Several speculative concerns about MI** (e.g., "could the metric be measuring a proxy?") — These are area-of-concern sweeps without concrete evidence in the paper text.
- **Nits about formatting, word choice, paragraph structure** — These are parser artifacts or style preferences not relevant to technical evaluation.
- **Strength from Strength Finder about "theorem linking condensed-graph MI to original-data MI"** — Removed because the theorem is unsubstantiated in the extracted text, making this claimed strength not verifiable. The empirical ablation supporting the MI component is a genuine strength, but the theorem framing is not.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the overclaiming in the "task-disentangled" framing and the selective reporting in cross-task results, but these are observational corrections rather than novel synthetic insights.

## Suggestions

1. Rename "task-disentangled meta optimization" to something more accurate (e.g., "task-aware meta-optimization" or "sub-task meta-adaptation") to avoid overclaiming.
2. Report all cross-task metrics in the text, not selectively. A single sentence with the full range for each table would suffice.
3. Either include KRR-ST in the cross-dataset/cross-task results or explain why it was excluded.
4. Briefly address the conceptual tension in the MI loss (maximizing I(Yₛˢ; Yₛʰ) while claiming Yₛˢ captures information *beyond* Yₛʰ) — a paragraph of discussion would resolve it.
5. Clarify how gradients are handled through the sparsification threshold δ in the adjacency generator.

## Score and Decision

The paper addresses a well-motivated problem with a sound combination of existing techniques and strong empirical validation across a broad experimental scope. The weaknesses are real but contained to presentation/overclaiming issues that do not threaten the core claims. The cross-task evidence is somewhat thinner than the cross-dataset evidence, but the overall contribution — the first principled method for transferable graph condensation — meets the ICLR bar.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>