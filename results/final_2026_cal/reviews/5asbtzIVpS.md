Now I have sufficient calibration data. Let me write the consolidated review.

**Calibration Summary:**

**Round 1 bracket**: 4.5 – 6.5

**Round 2 anchors read in full** (for narrowing):
- GRIPedge (avg 2.50, Reject) — Far weaker: limited novelty, no code, poor clarity. FGL is substantially stronger.
- CTNN (avg 5.00, Accept Poster) — Some thematic overlap (spanning trees for graph learning). CTNN had missing baselines and incremental novelty concerns. FGL has a more novel core idea, broader experiments, cleaner theory. FGL is stronger.
- TAQ-GAD (avg 5.00, Accept Poster) — Different task. FGL is comparable in rigor but has more questionable empirical claims.
- HarmonyGNNs (avg 6.00, Accept Poster) — Node classification with heterophily focus. FGL has a more novel paradigm but HarmonyGNNs doesn't have the pre-processing concern. Comparable quality but HarmonyGNNs cleaner empirically.
- From Fields to Random Trees (avg 6.67, Accept Poster) — Different domain (MAP inference). Hard direct comparison.
- IBG (avg 7.00, Accept Poster) — Stronger theory, broader evaluation across tasks. FGL is weaker.

**Final score**: 5.0. The paper has a genuinely novel paradigm and clean technical execution, but the experimental evaluation has a significant gap (no ablation controlling for graph pre-processing, missing heterophily-specific baselines) that undermines the main empirical claims.

---

## Summary

This paper proposes Forest-based Graph Learning (FGL), a new paradigm for semi-supervised node classification that replaces both deep local models and global attention with a forest of spanning trees. The core insight is that a spanning tree is the minimal subgraph connecting all nodes, so a few trees achieve global coverage with linear complexity. The paper provides: (1) a tree sampler guided by a homophily estimator, with a theoretical guarantee (Theorem 2) linking estimator accuracy to tree quality; (2) a linear-time tree aggregator that achieves quadratic node-pair interactions; and (3) extensive experiments on 9 datasets with 26 baselines, reporting strong results especially on heterophilous graphs (e.g., Texas 91.89%, Wisconsin 86.27%) with high efficiency.

## Strengths

- **Novel learning paradigm**: The central idea — using spanning trees as a structural intermediate for global message passing — is genuinely novel and well-motivated. The total-cost framing (Eq. 1) and the observation that spanning trees are the minimal globally-covering subgraph provide a clear conceptual departure from both deep GNNs and graph transformers. This is a genuinely new direction, not an incremental combination of existing ideas.

- **Clean theoretical guarantee (Theorem 2)**: The paper proves that as the edge-homophily estimator improves (ratio Δ = p/q increases), the induced tree distribution monotonically shifts toward higher-homophily trees with a known asymptotic upper bound determined by the graph's structural limitations. This provides a rigorous foundation for the homophily-guided sampling strategy and is empirically corroborated by the estimator comparison (Table 4, Fig. 5).

- **Efficient tree aggregator with quadratic interactions**: The tree aggregator (Theorem 1, Eqs. 7‑8) achieves all-pair node interactions on a tree in O(|V|) per tree by exploiting that neighbor aggregations differ by only one edge direction. This directly addresses the bottleneck of global attention methods while enabling genuinely global propagation. The efficiency results (Table 2) confirm the practical speed advantage (e.g., 0.005 s/epoch on Cora vs. 0.066 for GCNII).

- **Strong empirical results on heterophilous graphs**: The method achieves large absolute gains on Texas (91.89% vs. next best 78.92%), Cornell (83.24% vs. 68.65%), and Wisconsin (86.27% vs. 80.00%). The average rank across 9 datasets is 1.22, well ahead of the second-best SGFormer at 7.22.

- **Ablations validate forest components**: Table 3 shows that, given the augmented graph, the homophily-guided sampling, multiple trees, global submodule, and local submodule all contribute meaningfully (e.g., Texas: uniform sampling 82.58% → single homophily tree 84.83% → full FGL 91.89%). This confirms the forest paradigm adds value beyond the graph augmentation.

## Weaknesses

### Major

- **No ablation of the pre-processing (graph augmentation) step**: All ablations in Table 3 and all variants in Table 4 use the augmented graph. The pre-processing adds k-NN edges based on pseudo-labels from a classifier trained on labeled data, which increases graph homophily and ensures connectivity. Without a variant that runs FGL on the *original* graph (e.g., sampling trees per connected component or adding virtual nodes), it is impossible to attribute the reported gains to the forest-based paradigm versus the graph augmentation itself. This is especially critical for the heterophilous datasets where the margins are very large (e.g., Texas 91.89% vs. next best 78.92%), and the pre-processing step is explicitly designed to increase homophily. The paper's central claim — that FGL's forest paradigm enables superior global coverage — requires this ablation to be convincing.

- **Missing heterophily-specific baselines**: The paper includes 26 baselines but omits methods specifically designed for heterophilous graphs: H2GCN, LINKX, CPGNN, ACM-GCN, and GloGNN are standard on Texas/Cornell/Wisconsin/Actor and frequently report competitive numbers on these datasets. Without these comparisons, the paper's claim of state-of-the-art performance on heterophilous benchmarks is not properly supported. The current baseline set is heavily weighted toward graph transformers, which are known to struggle on these datasets, making the comparison less informative.

### Minor

- **Idealized assumptions in Theorem 2**: The theoretical analysis assumes binary edge scores (p for homophilous edges, q for heterophilous) whereas in practice the homophily estimator outputs continuous scores. The theorem provides qualitative intuition but does not guarantee monotonic improvement in the continuous regime. The paper acknowledges this implicitly through the empirical estimator comparison but does not discuss the gap.

- **The tree aggregator generality is claimed but untested**: Section 4.3 asserts that "many popular models can be adopted" (RNNs, SSMs, etc.) but only the linear weighted-sum/difference variant is implemented and tested. The generality claim is interesting but remains speculative without experiments.

- **k (number of nearest neighbors in pre-processing) not specified in main text**: The number k is critical — too large adds many potentially spurious edges — but is deferred to the appendix (which is not visible in the available text). Including this in the main paper or at least the experimental setup section would aid transparency.

### Trivial

- Standard deviations are reported in an appendix table (Table 10) but not in the main Table 1. While this is common practice, given the very large margins on heterophilous datasets, including at least a summary (e.g., "± x.x" in the main table) would be helpful.

## Nice-to-Haves

- An ablation running FGL on the *original* graph (per-component tree sampling or using virtual nodes for connectivity) would address the central concern about the pre-processing step and is the single most important missing experiment.
- Including heterophily-adapted baselines (H2GCN, LINKX, ACM-GCN) would substantially strengthen the SOTA claims on Texas/Cornell/Wisconsin.
- A study of the sensitivity to hyperparameter k (number of nearest neighbors in pre-processing) would be informative.

## Removed Points

The following points from the reviewers have been removed after cross-checking:

- **"The pre-processing introduces an unfair advantage that invalidates the comparison against baselines"** — softened to a missing-ablation criticism. The pre-processing is a legitimate part of the method's pipeline; the concern is about attribution of gains, not fairness of comparison.
- **"Double use of labels not discussed"** — Pseudo-labeling is a standard semi-supervised technique. The paper uses labels to train the pseudo-label classifier, then uses the same labels for the main classifier. This is not a data leakage problem in the usual sense and is standard practice.
- **"No standard deviations shown in main text"** — They are in the appendix (Table 10), which is common practice.
- **"Efficiency comparison may not include tree sampling time"** — Speculative; the paper states "per epoch" time and the reviewer has no evidence that tree sampling is excluded.
- **k not specified** — This is likely in the appendix; it's minor.
- Generic formatting/style complaints and speculation about unstated experimental details.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Run FGL on the original graph** (without pre-processing) using per-component tree sampling or virtual connector nodes. Report results on at least the heterophilous datasets (Texas, Cornell, Wisconsin, Actor). This single experiment would resolve the central attribution question.
2. **Add heterophily-adapted baselines** (H2GCN, LINKX, ACM-GCN) to the comparison on Texas, Cornell, Wisconsin, and Actor.
3. **Include k (nearest neighbors) and N_T (number of trees) in the main text**, ideally in the experimental setup paragraph.
4. **Add standard deviations or error bars to Table 1** in the main text.

## Score and Decision

**MY FINAL SCORE: <score>5.0</score>**
**MY FINAL DECISION: <decision>Reject</decision>**