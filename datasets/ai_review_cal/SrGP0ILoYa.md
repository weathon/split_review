- Decision: Reject
- Avg Score: 6.25
- Scores: 6, 6, 5, 8
Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper introduces TopER (Topological Evolution Rate), a graph embedding method that tracks how the number of nodes and edges accumulate during a filtration process and summarizes this evolution via linear regression coefficients (pivot *a* and growth *b*). The resulting 2D embedding for each filtration function is interpretable, computationally cheap (linear in graph size), and can be combined across multiple filtration functions for graph classification. The paper demonstrates competitive classification accuracy (best average deviation of 1.60% across eight datasets), linear-time scalability, and compelling 2D visualizations on molecular, biological, and social graph benchmarks.

## Strengths

- **Best overall rank in classification across 19 baselines (Table 1):** TopER achieves the lowest average deviation from the top result per dataset (1.60%), outperforming the next best method TopoGCL (1.76%). It achieves the best result on BZR (90.13%) and REDDIT-B (92.70%), and second-best on MUTAG (90.99%) and REDDIT-5K (56.51%). This is a concrete, measured claim supported by the table.

- **Linear-time computational complexity with demonstrated scalability (Section 4.1, Figure 3):** The method has overall complexity \(O(n(|\mathcal{V}|+|\mathcal{E}|))\) — far cheaper than the cubic cost of traditional persistent homology. Figure 3 validates this empirically, showing a 100K-node synthetic graph processed in ~2 minutes.

- **Ablation study confirms synergy of multiple filtration functions (Table 4):** Individual filtration functions yield modest performance (e.g., 73–83% on BZR), but combining all seven functions improves substantially (90.13% on BZR). This validates that different filtration functions capture complementary structural information.

- **Direct outperformance of persistent homology baselines (Table comparing TopER vs. PH):** On all six datasets where a direct comparison is available, TopER surpasses the best PH-based pipeline (e.g., 73.2 vs. 69.5 on IMDB-B, 50.0 vs. 46.5 on IMDB-M), supporting the claim that the simplified evolution-rate approach improves over traditional PH.

- **Interpretable 2D visualizations with structural meaning (Section 5.4, Figures 1–2):** The two parameters (pivot *a* and growth *b*) have clear interpretations — connectivity and edge-growth rate — that produce visually separable scatter plots. The cross-dataset visualization (Figure 1, left) showing MUTAG, COX2, and PROTEINS in a single panel is a genuine differentiator from GNN-based embeddings.

## Weaknesses

### Fatal

None.

### Major

- **Theoretical stability analysis does not align with the implemented method (Section 4.2 vs. Algorithm 1 / Definition 1).** The stability results (Theorem 1, Corollary 1) are stated in terms of pairs \(\{(\beta_0(\varepsilon_i),\beta_1(\varepsilon_i))\}_{i=1}^n\) — Betti numbers — with the bound involving the 1-Wasserstein distance between persistence diagrams. However, the actual TopER algorithm uses raw node counts \(|\mathcal{V}_i|\) and edge counts \(|\mathcal{E}_i|\) (Algorithm 1, Definition 1). These are structurally different quantities: e.g., a tree with 5 nodes and 4 edges gives \((|\mathcal{V}|,|\mathcal{E}|)=(5,4)\) but \((\beta_0,\beta_1)=(1,0)\). The paper states on line 151 that it uses \((\beta_0,\beta_1)\) "to keep the setting general," but this means the stated theorem is about a different procedure than what is actually implemented. The stability guarantee — listed as contribution bullet 4 — therefore does **not** apply to TopER as presented. This is a verifiable mismatch between the paper's theoretical claims and its practical method. The authors should either prove stability for the actual \((|\mathcal{V}_i|,|\mathcal{E}_i|)\) representation or explicitly qualify the theoretical claim.

### Minor

- **Threshold set construction for continuous filtration functions is unspecified (Algorithm 1, Section 4).** The method takes a threshold set \(\mathcal{I}=\{\varepsilon_i\}_{i=1}^n\) as input, but the paper never specifies how this set is constructed for continuous-valued filtration functions (closeness, centrality, Ricci curvatures). For degree-based filtrations the thresholds are naturally integer values, but for continuous functions the choice of granularity and spacing (uniform, quantile-based, etc.) could materially affect the \((|\mathcal{V}_i|,|\mathcal{E}_i|)\) curve and thus the regression coefficients. The scalability experiment (Figure 3) uses "100 filtration steps" but no general recipe is given. This is a reproducibility gap that the authors should close by specifying the protocol.

- **High variance in classification results (Table 1).** TopER's standard deviations are substantially larger than most competitors (e.g., \(\pm6.64\) on MUTAG vs. \(\pm0.66\) for FC-V, \(\pm4.59\) on COX2 vs. \(\pm0.88\) for FC-V). While the average-deviation metric is favorable to TopER, the high variance suggests instability across CV folds and weakens the confidence in individual dataset comparisons. The paper does not discuss or explain this variability.

- **Comparison protocol for Table 1 baselines is not standardized.** Baseline numbers are taken from their original publications, which may use different train/test splits, evaluation protocols, and cross-validation strategies than the 90/10 stratified 10-fold CV used for TopER. While this practice is common in the literature, it introduces uncertainty in the comparisons. Additionally, the "Avg.↓" column aggregates over different numbers of datasets per model (since some models have missing entries), so it is an approximate rather than strictly comparable summary.

- **Clustering evaluation measures cross-dataset separability, not standard graph clustering (Section 5.3).** The clustering experiment pools graphs from all eight datasets and measures how well the embedding separates graphs by dataset-of-origin. This is a reasonable test of cross-dataset structure preservation, but it is a non-standard use of clustering metrics (Silhouette, CH, DB) and is not a standard graph-clustering benchmark (e.g., partitioning nodes within a graph or clustering graphs within a single dataset using class labels). The single baseline (Spectral Zoo) is also limited. The framing "excels at clustering tasks" in the abstract overstates what is demonstrated.

### Trivial

None.

## Nice-to-Haves

- A sensitivity analysis showing how the number and spacing of filtration thresholds affects classification accuracy and embedding stability would strengthen the method's validation.
- Including a few simple non-neural baselines (e.g., SVM on summary statistics like degree distribution moments or clustering coefficients) would help calibrate whether TopER's gains come from the topological evolution rate or from the classifier pipeline.
- Statistical significance testing (e.g., paired t-test across CV folds) between TopER and the best competitor per dataset would help assess whether the accuracy differences are reliable given the high variance.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"First topology-based..." claim questioned (Harsh Critic Section-by-Section Notes):** The critic questions whether TopER is truly the first method with these properties, citing "persistence image vectorizations with PCA, or some of the kernel-based methods" without specific references. Per policy, missing related works are not raised, and the critic provides no concrete evidence. **Removed.**

- **"Least squares regression specification" (Harsh Critic Section-by-Section Notes):** The critic asks whether the fit is zero-intercept or unconstrained. Standard least squares on \(\{(x_i,y_i)\}\) with two parameters \((a,b)\) is unconstrained by convention; the paper's definition and algorithm are clear. **Removed as a strawman.**

- **"Missing comparison with simple baselines on same hardware" (Harsh Critic Missing Parts):** This is a nice-to-have but not a required weakness, and the paper does compare against 19 published baselines. **Moved to Nice-to-Haves.**

- **Theoretical stability as a strength (Strength Finder Core Strength #3):** This strength conflicts with the verified weakness that the stability analysis does not apply to the implemented method. Per policy, when a strength and weakness disagree, the weakness wins. **Removed.**

- **"Outperformance of PH" as a separate strength for each dataset:** This is valid but already subsumed in the main listed strengths above. **Not removed but merged.**

## Novel Insights

None beyond the paper's own contributions. The reviews confirm that TopER's core idea — replacing expensive persistent homology with linear regression on node/edge count sequences — is novel and produces competitive results, but the key insights (interpretable 2D embedding, cross-dataset visualization, linear-time complexity) are all already presented in the paper.

## Suggestions

1. **Reconcile the stability analysis with the implemented method.** Either prove stability for the \((|\mathcal{V}_i|,|\mathcal{E}_i|)\) representation, or formally relate it to \((\beta_0,\beta_1)\) stability, or remove/qualify the theoretical claim as inapplicable to the current algorithm.
2. **Specify the threshold-set construction protocol** for continuous filtration functions (e.g., number of steps, spacing scheme) in the main text or visible appendix.
3. **Address the high variance** by discussing potential causes (e.g., the 90/10 split leaves small test sets for some datasets) and consider reporting additional metrics (e.g., median accuracy across folds).
4. **Rerun a small number of key baselines** (e.g., TopoGCL, GIN, FC-V) under the same 90/10 stratified CV pipeline to validate that the advantage holds under a common protocol.
5. **Reframe the clustering experiments** as "cross-dataset structure preservation" rather than "clustering tasks" to avoid overclaiming.
