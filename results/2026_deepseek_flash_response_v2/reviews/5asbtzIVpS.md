## Summary

This paper proposes Forest-based Graph Learning (FGL), a novel paradigm for semi-supervised node classification that replaces standard message passing or global attention with aggregation over a forest of spanning trees. The method has four components: (1) graph pre-processing that adds edges via pseudo-label-based k-NN for connectivity and increased homophily; (2) a homophily-guided tree sampler that generates spanning trees from a learned distribution; (3) a linear-time tree aggregator (Theorem 1) achieving all-pair node interactions in O(n) time per tree; and (4) a tree fuser that merges information across trees. Theorem 2 provides a theoretical guarantee linking homophily estimation accuracy to tree quality. Empirically, FGL achieves an average rank of 1.22 across 9 benchmarks while being among the fastest methods.

## Strengths

1. **Genuinely novel paradigm with principled motivation**: The paper reinterprets graph learning through spanning trees — the minimal globally-connected subgraph — breaking the trade-off between cost-effectiveness and global receptive field that the paper identifies as the fundamental limitation of prior approaches (deep GNNs stacking layers vs. Graph Transformers with quadratic attention). This is a fresh perspective on a well-studied problem.

2. **Linear-time global aggregation (Theorem 1)**: The tree aggregator achieves all-pair node interactions in O(n) time per tree via two recursions (bottom-up aggregation then top-down distribution). This is verified by the complexity analysis (Section 4.5, O((n+m)Kd) total complexity) and runtime comparisons (Table 2), where FGL is 2–5× faster than competitive baselines like GCNII and DIFFormer while outperforming them in accuracy.

3. **Rigorous theoretical result linking homophily estimation to tree quality (Theorem 2)**: The theorem proves monotonicity, an upper bound based on the graph's homophilous connected components (NHCC), and asymptotic tightness — showing that as the edge-score ratio Δ = p/q increases, the expected homophily ratio of sampled trees approaches a structural upper bound. This is a non-trivial mathematical result that grounds the design of the homophily-guided tree sampler.

4. **Strong empirical results with thorough validation**: Table 1 shows FGL achieves an average rank of 1.22 across 9 diverse benchmarks (both homophilic and heterophilic). The ablation study (Table 3) systematically validates each component: the global submodule adds ~9 points on Texas, homophily-guided vs. uniform sampling adds ~9 points, and the forest-of-trees vs. single-tree design adds ~7 points. Table 4 further validates that better homophily estimators yield better downstream performance, providing empirical confirmation of Theorem 2.

5. **Fastest runtime among strong baselines**: Table 2 shows FGL achieves 0.005s/epoch on Cora and 0.246s on ArXiv — consistently faster than ANS-GT, GOAT, GCNII, and DIFFormer, while maintaining superior accuracy. The efficiency advantage is maintained across graph sizes.

## Weaknesses

### Fatal
None.

### Major

1. **Asymmetric evaluation design due to label-informed graph pre-processing**: Section 4.1 augments the graph by adding k-NN edges based on pseudo-labels from a model trained on labeled data, producing an augmented graph Ĝ with increased homophily and guaranteed connectivity. Baselines in Table 1 operate on the *original* graph G, while FGL operates on Ĝ. This means the comparison confounds the benefit of the forest-based paradigm with the benefit of a label-informed graph augmentation that baselines do not receive. The ablation study (Table 3) shows that even uniform tree sampling on Ĝ achieves 82.58 on Texas (exceeding all baselines), confirming that the augmentation alone provides a substantial advantage. However, the full FGL at 91.89 on Texas is 9+ points beyond the uniform-sampling variant, showing the paradigm itself contributes significantly. **To make a valid comparison, the paper should either (a) evaluate baselines on the same augmented graph Ĝ, or (b) restrict pre-processing to connectivity-only changes (without homophily-increasing k-NN) and report whether the method still works.** The paper does not currently acknowledge this asymmetry as a limitation, which is the most significant issue in the evaluation.

### Minor

1. **Overclaiming the "perfect estimation → perfect classification" extrapolation**: Line 305 states that Fig. 5 reveals "perfect estimation (accuracy is 1) leading to perfect classification." Fig. 5 only shows data up to p=0.9; extrapolation to 1.0 is speculative and unsupported. This claim should be removed or qualified.

2. **"Generality" of the tree aggregator is somewhat overstated in the main text**: Section 4.3 presents the aggregator framework as "general" (listing linear attention, linear RNNs, SSMs, and non-linear variants) but the concrete implementation (Eqs. 7–8) is linear. Property (II) — the disentangle property — requires reversibility, which many non-linear aggregators do not satisfy. While the appendix (stripped) may address non-linear variants, the main text would be clearer if it stated that practical non-linear options are limited to those satisfying Property (II) and gave at least one concrete example in the main text.

3. **Theoretical guarantee (Theorem 2) assumes oracle knowledge**: The theorem assumes ideal edge scores (p for homophilous edges, q for heterophilous, with p > q), which requires knowing edge types — the very unknown the method aims to solve. The practical relevance depends on the quality of the learned homophily estimator, and the paper does not theoretically bound the gap between the oracle and the learned estimator. This is common for "if-then" theorems in machine learning and does not invalidate the result, but the framing could be more careful about the practical reach of the guarantee.

4. **Unclear notation in complexity analysis**: Line 160 states O((n+m)Kd) where "K" is not clearly defined — it may refer to K_L, N_T, or another quantity. This should be clarified.

### Trivial
- Several strong baselines (GT, SAN, Graphormer, TDGNN) run out of memory on larger datasets (Arxiv, Flickr), partly inflating FGL's relative standing — though this is acknowledged and reflects a genuine scalability advantage.

## Nice-to-Haves
- Sensitivity analysis for the hyperparameter k (number of k-NN edges added during pre-processing).
- Standard deviations in the main Table 1 (currently deferred to the appendix, which was stripped).
- Evaluation on larger heterophilous benchmarks (e.g., Pokec, Penn94) to strengthen the heterophily claims.

## Removed Points
- *"The pre-processing uses labels twice"* — Standard pseudo-labeling practice in semi-supervised learning; not a flaw specific to this method.
- *"Wilson's algorithm complexity concern on dense augmented graphs"* — Speculative; the paper's "nearly O(n)" claim is standard for Wilson's algorithm expected runtime.
- *"Missing related works"* — Cannot verify without external sources.
- *"Formatting/style nitpicks and typo complaints"* — Parser artifacts, not author errors.
- *"Criticisms questioning existence/release status of cited models"* — All cited references are assumed to exist.
- *"Appendix-deferred proofs or missing appendix content"* — The appendix exists in the original submission; the parser stripped it.
- *Strength Finder generic strengths* (e.g., "addressed an important problem") — Removed as not specific to paper content.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. **(Most important)** Run a representative set of baselines on the augmented graph Ĝ to disentangle the effect of pre-processing from the forest-based paradigm. Alternatively, restrict pre-processing to connectivity-only edge additions (without label-informed k-NN) and report whether the method maintains its performance advantage.
2. Remove or qualify the "perfect estimation → perfect classification" extrapolation — it is not supported by the data shown.
3. Clarify the "K" notation in the complexity analysis (line 160).
4. If non-linear aggregators that satisfy Property (II) exist, give a concrete example in the main text rather than deferring entirely to the appendix.
5. Include standard deviations in the main comparison table for completeness.

## Score and Decision

**Calibration details:**

All anchor papers retrieved across rounds:

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| VyMW4YZfw7 (Simplify GNN with Low-Rank Kernel) | 3.00 | R1 | FGL has far stronger theory, novelty, and empirical results |
| ceNnsnA5gu (WL-Tree) | 3.00 | R1 | Different focus, but FGL has broader scope and stronger results |
| nFcgay1Yo9 (Scale-Free GLM) | 5.75 | R1 | FGL has more novel paradigm, stronger theory, broader evaluation; comparable weakness profile |
| hESD2NJFg8 (LLM-GNN) | 6.50 | R1 | FGL has stronger theory and more fundamental novelty; LLM-GNN has cleaner evaluation |
| zBbZ2vdLzH (Joint Graph Rewiring) | 8.00 | R1 | FGL has comparable novelty but the pre-processing concern prevents it from reaching this tier |
| viftsX50Rt (General Graph Random Features) | 8.00 | R1 | Strong theoretical paper; FGL has more applied focus with evaluation concerns |
| aFMiKm9Qcx (Central Spanning Tree Problem) | 4.75 | R2 | Different domain; FGL has far stronger empirical validation |
| 3fRbP8g2LT (Redundancy-Free Graph Networks) | 5.00 | R2 | FGL has stronger novelty and theory |
| hv3SklibkL (Graph Parsing Networks) | 6.00 | R2 | Comparable score band; FGL has more theoretical contributions |
| 5x88lQ2MsH (Bonsai) | 6.00 | R2 | FGL has stronger theory but comparable empirical quality; both have evaluation concerns |
| 3FJOKjooIj (Self-Supervised Heterogeneous Graph Learning) | 7.00 | R2 | Stronger evaluation practices but different subdomain; FGL's pre-processing concern is addressable |
| 4v4RcAODj9 (DUALFormer) | 6.50 | R2 | FGL has more novel paradigm and stronger theory; DUALFormer has fundamental questions about method claims |
| y21ZO6M86t (PolyGCL) | 7.25 | R2 | Strong theoretical paper in different subdomain (contrastive learning) |
| j4VMrwgn1M (Curriculum-Enhanced GT Distillation) | 6.75 | R2 | Comparable domain; FGL has more fundamental paradigm novelty |

**Bracket reasoning:** R1 placed FGL between 3.5 and 7.5 (clearly above weak papers, not at the 8.0 tier). R2 narrowed to 5.5–6.5 by comparing against anchors at 5.75, 6.00, 6.50, and 7.00. FGL is stronger than the 5.75 anchor (Scale-Free GLM) in novelty, theory breadth, and experimental scope, and is comparable to the 6.00–6.50 anchors (Bonsai, DUALFormer, LLM-GNN). The pre-processing evaluation concern is significant and prevents a higher score, but the core paradigm, theory, and ablation evidence are substantial contributions.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>