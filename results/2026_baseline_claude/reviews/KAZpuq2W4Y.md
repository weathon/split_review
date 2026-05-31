## Summary
HOMIL (Higher-Order Multi-Instance Learning) extends the standard attention-based MIL (ABMIL) framework for whole-slide image (WSI) classification by incorporating second-order statistics (a covariance matrix over cluster-level patch features) alongside first-order moment aggregation. To handle the computational burden, DBSCAN is used for adaptive clustering, reducing patch sets to cluster representatives with variable granularity (fine-grained for rare pathological regions, coarse-grained for abundant normal tissue). The method is validated on CAMELYON16 and TCGA-NSCLC with nine baselines, achieving best performance on all metrics while remaining computationally efficient.

---

## Strengths

- **Clear statistical motivation**: The reinterpretation of ABMIL as first-order moment estimation and the principled extension to second-order moments (covariance) is well-articulated and provides a coherent conceptual framework for the contribution.

- **Consistent empirical improvement with efficiency**: HOMIL achieves the highest ACC, AUC, and F1 on both CAMELYON16 and TCGA-NSCLC while being substantially faster than most strong baselines (310s vs. TransMIL's 5175s, MambaMIL's 7200s, and HMIL's 10800s on CAMELYON16). This is a genuinely useful result: better accuracy *and* lower cost.

- **Fair experimental protocol**: All baselines share the same CONCH-extracted 512-dimensional features and the same 5-fold cross-validation splits, making the comparison methodologically sound.

- **Informative ablation**: Table 3 disentangles the contributions of clustering (CM) and second-order moments (SOM), confirming both components are additive and that the full model strictly dominates each ablated variant.

---

## Weaknesses

### Fatal
None.

### Major

1. **Inconsistency between the "attention-weighted covariance" claim and the actual formula.** Section 4.3.3 labels the computation an *attention-weighted* covariance matrix, but the formula is:
   $$\mathbf{C} = \sum_{k=1}^K \tilde{\mathbf{g}}_k \tilde{\mathbf{g}}_k^\top,$$
   which contains no attention weights $a_k$. The centering uses the attention-weighted mean $\mathbf{v}^{(1)}$, but the outer-product accumulation is uniform. A true attention-weighted covariance would multiply each term by $a_k$. This inconsistency between stated design intent and implementation is never acknowledged, and the choice (whether intentional or not) is not justified. This weakens the conceptual coherence of the paper's core contribution.

2. **Only two evaluation datasets.** Competitive WSI MIL papers routinely evaluate across 5–8 diverse datasets (e.g., TCGA-RCC, TCGA-BRCA, PANDA, TCGA-STAD). With only CAMELYON16 (binary, small-scale) and TCGA-NSCLC (binary, lung subtyping), it is impossible to assess whether the gains generalise to multiclass settings, finer-grained diagnoses, or different tissue types. This limits confidence in the generality of the contribution.

3. **Performance margins over the strongest baselines are within standard error on key metrics.** On CAMELYON16, HOMIL (96.98% ± 2.43%) vs. MambaMIL (96.48% ± 1.37%) is a 0.5% ACC gap—well within the reported SE bands. On TCGA-NSCLC, F1 improvement over HMIL is 0.10%. Without significance testing, it is not clear that these improvements are statistically reliable. The stronger results (AUC gains, efficiency) are more convincing.

### Minor

1. **Covariance compression via 1D row-wise convolution is ad hoc and unmotivated.** Compressing the $d\times d$ covariance matrix by applying independent 1D max-pooled convolutions to each row is a specific engineering choice, but alternatives (diagonal extraction, top-$r$ eigenvalues, Frobenius-norm features, or a simple linear projection on the vectorised lower triangle) are neither considered nor ablated. Why row-wise max-pooling is appropriate for capturing inter-feature correlations is not explained.

2. **The HMIL baseline shows an anomalous AUC of 94.44% on CAMELYON16** — more than 4 points below ABMIL (98.88%) — without any discussion. If this is a reproducibility issue with the authors' reimplementation, the comparison is potentially unfair; if it reflects a known limitation of HMIL, it deserves comment.

3. **The title claims "higher-order moments" (plural) but the method only implements second-order statistics.** No third- or higher-order moment is explored, making the title slightly over-promised.

### Trivial

- Figure 2 shows training curves for a single dataset without specifying which one.
- The DBSCAN outlier handling (non-core points forming single-element clusters) is mentioned but its practical frequency and effect are not quantified.

---

## Nice-to-Haves

- An ablation comparing different covariance compression strategies (diagonal, truncated SVD, learned linear projection) would substantially strengthen the design rationale.
- Extending evaluation to at least two additional datasets (e.g., TCGA-RCC for multiclass, PANDA for regression-like grading) would make the generalization claim far more convincing.
- Statistical significance tests (e.g., Wilcoxon signed-rank over folds) across baselines would clarify which improvements are robust.

---

## Novel Insights

The paper's most useful observation is that incorporating the unweighted outer-product covariance of attention-centered cluster features — even without direct attention weighting in the covariance terms — still provides complementary information to the first-order mean. This suggests that feature *spread* across clusters (not just their weighted average) encodes diagnostically relevant heterogeneity independent of which clusters are deemed most important by the attention mechanism. The fusion weight dynamics (Figure 2b), where $\alpha^{(1)}$ dominates at convergence but $\alpha^{(2)}$ stabilises at ~0.45, empirically support this complementarity. However, this insight would be more compelling with a theoretical account or at minimum with ablations varying how the covariance is weighted.

---

## Suggestions

- Resolve the attention-weighted vs. unweighted covariance discrepancy: either implement true $\sum_k a_k \tilde{\mathbf{g}}_k\tilde{\mathbf{g}}_k^\top$ and compare with the current formula, or clearly state that the covariance is *not* attention-weighted and justify the design.
- Add a row to Table 3 ablating the covariance compression strategy (e.g., diagonal only, top eigenvectors) to validate the 1D convolution choice.
- Evaluate on at least one additional dataset to substantiate the generalization claim.
- Report McNemar or Wilcoxon tests across the 5-fold splits for the key ACC/AUC comparisons.

---

## Score and Decision

The paper offers a sensible and well-framed contribution — using second-order patch statistics in WSI MIL is a natural extension, the efficiency story is compelling, and the ablation is informative. However, the conceptual inconsistency in the covariance formulation, limited experimental breadth (two binary datasets), and marginal performance gaps over the strongest baselines without significance testing all reduce confidence that this is a solidly mature contribution at the ICLR bar.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>