Now I have all the information needed. Let me compose the final consolidated review.

---

## Summary

This paper proposes TopGQ, the first post-training quantization (PTQ) framework for GNNs. It groups vertices by local topological properties (indegree + localized Wiener index) to share quantization parameters, and absorbs node-wise scales into the adjacency matrix for efficient integer-only inference. Experiments on six node-classification and two graph-classification datasets show that TopGQ matches or exceeds QAT-based GNN quantization methods while being orders of magnitude faster (up to 358× speedup in quantization time).

## Strengths

- **First PTQ framework for GNNs, with demonstrated order-of-magnitude speedups.** All prior GNN quantization methods (Degree-Quant, A²Q, SGQuant) require gradient-based retraining. TopGQ achieves competitive accuracy without backpropagation: e.g., on Reddit with 4-bit GraphSAGE, 93.93% accuracy in 0.02 hours vs. Degree-Quant's 89.86% in 42.27 hours (Table 1). This is a clear practical contribution.

- **Topology-based node grouping reduces quantization error compared to indegree-only grouping.** The paper identifies that indegree alone is insufficient to capture feature magnitude variance (Figure 2). Combining indegree with the localized Wiener index yields groups with tighter within-group value ranges and more even node distribution. The ablation study (Table 4) confirms that topology grouping dramatically improves PTQ accuracy (e.g., Reddit GCN 4-bit from 63.99% to 85.68%).

- **Scale absorption enables node-wise precision without extra inference cost.** By absorbing the scale diagonal matrix \(S_X\) into the adjacency matrix (Equation 15), TopGQ preserves fine-grained quantization where it matters most (isolating outlier nodes) while keeping matrix multiplication in integer arithmetic. Figures 5-6 show that this produces more uniform activation distributions across the integer range.

- **Comprehensive experimental evaluation with ablations.** The paper evaluates across 8 datasets, 3 architectures, and 2 bitwidths. Ablations isolate the effects of topology grouping (Table 4), compare against alternative centrality measures (Table 7), benchmark the accelerated Wiener index computation (Table 6), and report inference times (Table 5). This depth of analysis builds confidence in the design choices.

## Weaknesses

### Fatal
None.

### Major

- **The accelerated Wiener index algorithm is described inconsistently and insufficiently verified.** 
  *Equation (12) for the \(k=2\) case initializes the maximum case as \(4|V_{\text{sub}}|^2\), but Algorithm 1 (line 13) initializes the general case as \(k|V_{\text{sub}}|^2\) — a factor of two off for \(k=2\). This suggests confusion between ordered/unordered pair conventions that is not acknowledged.
  *The pseudocode (Algorithm 1) is ambiguous: it is unclear what \(h_m\) stores (directed pairs, undirected pairs, or vertices), how the union operations relate to the reachable-set cardinalities, and how the subtractive formula is derived from Equation (10–12). The relationship between \(\bigcup_{i=l}^k h_i\) and \(\Sigma_{v\in V_{\text{sub}}}|N_l(v)|\) is not justified.
  *Table 6 reports speedups of up to 602× against standard algorithms but never verifies that the computed Wiener indices are correct (e.g., by comparing against exact values on small graphs). Without such verification, the reader cannot rule out that the speedup comes from computing something other than the intended quantity.

  This is a **major** weakness because the efficiency claim of the entire method depends on this algorithm being correctly specified and implemented. The core idea (exploiting the diameter bound of a \(k\)-hop subgraph) is sound, but the presentation must be fixed and correctness validated for the contribution to be trustworthy.

- **The method for handling unseen node groups at inference time is not evaluated.** When an \((I, W_k)\) pair is not seen during calibration, nodes are assigned via a lexicographic nearest-neighbor rule (compare \(I\) first, then \(W_k\)). The paper does not report how many test nodes fall into this case, compare alternative assignment strategies (e.g., Euclidean distance in 2D, rounding to nearest bin), or analyze whether this rule introduces systematic grouping errors. If many unseen pairs arise (e.g., in inductive settings), the grouping could become incoherent. The impact on accuracy is unknown.

### Minor

- **Memory overhead of group-wise quantization is not discussed.** For large, heterogeneous graphs, the number of distinct \((I, W_k)\) pairs could approach the number of nodes, potentially making the storage of group-wise scale/zero-point parameters comparable to row-wise quantization — yet the paper contrasts its approach with row-wise methods without comparing memory costs. This omission does not invalidate the results but limits the completeness of the efficiency analysis.

- **No standard deviations or confidence intervals on accuracy.** Quantization outcomes can be sensitive to calibration data and random seeds. Reporting variability (e.g., over multiple calibration splits) would strengthen the empirical results, especially for cases where TopGQ slightly exceeds FP32 accuracy (e.g., Reddit GCN 94.38 vs. 94.32).

- **The simple PTQ baseline (no grouping, no scale absorption) appears only in the ablation table (Table 4), not in the main comparison tables (Tables 1–3).** While the ablation is present in the paper, placing the PTQ baseline alongside the main results would make it easier for readers to assess the added value of topology grouping relative to trivial PTQ.

### Trivial
None worth enumerating beyond what has been captured above.

## Nice-to-Haves
- A theoretical complexity analysis of the accelerated Wiener index algorithm (asymptotic and empirical scaling with graph size).
- A formal derivation or correctness proof of the subtractive formula in Algorithm 1.
- A brief discussion of limitations (e.g., the method assumes graph connectivity is available at calibration time, which may not hold for streaming or encrypted graphs).

## Removed Points
These points were considered but removed as they are inaccurate, misread the paper, or violate the filtering rules:

1. **"Scale absorption is not properly ablated"** (Harsh Critic's Critical Issue #2). *Reason for removal:* The reviewer claimed Table 4 "only compares a baseline (no grouping) against topology grouping" and does not isolate scale absorption. This is factually incorrect. Table 4 has three conditions: Baseline (no grouping) → Topology Grouping (w/ Wiener index) → Full TopGQ (w/ scale absorption). The difference between rows 2 and 3 *is* the ablation of scale absorption. The reviewer appears to have overlooked the third row. The quantitative ablation is present, and the visualizations in Section 6.7 provide additional qualitative support.

2. **"The claim 'first PTQ for GNNs' may not hold if broader PTQ literature is surveyed."** *Reason for removal:* The paper's Related Work section (Section 3) specifically surveys *GNN* quantization methods (Degree-Quant, A²Q, SGQuant, EPQuant, SMP, Eliasof et al. 2023) and correctly identifies that all existing GNN quantization methods use QAT. The claim is bounded to the GNN domain and is supported by the cited literature. This is not a genuine weakness.

3. **"The paper lacks a survey of PTQ from the broader network quantization community."** *Reason for removal:* This asks the paper to expand its scope beyond what is reasonable. The paper is about GNN quantization and correctly situates itself within that subfield. General PTQ methods (e.g., for CNNs/Transformers) are not directly applicable to GNNs' unique aggregation structure.

4. **Various formatting and presentation nitpicks.** Removed per policy — these reflect PDF parser artifacts, not author errors.

## Novel Insights
The combination of the harsh critic and strength finder reveals a clear pattern: the paper's empirical contribution (first PTQ for GNNs with strong results) is well-supported and appears solid, but its *technical exposition* of the core algorithmic innovation (the accelerated Wiener index computation) is the weak link. This is a case where the experiments likely speak for themselves, but the paper would be significantly strengthened by a clean, consistent, verified description of the algorithm — and a simple correctness check on small graphs. Both reviewers agree on the paper's empirical quality and practical importance; the main risk is reproducibility due to unclear presentation, not methodological unsoundness.

## Suggestions
1. **Fix the factor-of-2 inconsistency in Algorithm 1.** Clarify whether the initialization should be \(2k|V_{\text{sub}}|^2\) or \(k|V_{\text{sub}}|^2\) and ensure it is consistent with Equation (12) and the ordered/unordered pair convention used throughout.
2. **Verification on small graphs.** Add a simple experiment (e.g., in the appendix) comparing the accelerated Wiener index against exact Floyd-Warshall computation on small graphs (\(|V| < 100\)) for \(k=2,3\) to confirm correctness.
3. **Rewrite Algorithm 1.** Provide explicit mathematical justification for the subtractive formula, clarify whether \(h_m\) stores vertices or pairs, and connect the pseudocode variables to the equations.
4. **Evaluate unseen-node assignment.** Report the fraction of test nodes with unseen \((I, W_k)\) pairs on each dataset, and compare the lexicographic rule against at least one alternative (e.g., 2D Euclidean nearest neighbor).
5. **Add memory analysis.** Quantify the number of distinct groups per dataset and compare the storage overhead of group-wise vs. row-wise quantization parameters.
6. **(Optional) Report variability.** Add standard deviations or ranges over multiple calibration runs for a representative subset of experiments.

## Score and Decision

**Score: 6.5** — The paper addresses an important problem with a novel and well-motivated approach. The experimental evidence for the PTQ framework's effectiveness is strong and comprehensive. However, the unclear and inconsistent description of the accelerated Wiener index algorithm is a significant weakness that undermines reproducibility and trust in a core technical component. The paper is above the acceptance threshold in terms of overall contribution, but the authors must address the algorithm presentation and verification issues before final publication.

**MY FINAL SCORE: <pineapple>6.5</pineapple>**
**MY FINAL DECISION: <orange>Accept</orange>**