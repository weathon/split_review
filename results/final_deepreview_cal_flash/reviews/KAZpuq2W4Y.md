Now I have sufficient calibration data. Let me compile the final review.

**Calibration summary:**

Round 1 bracketing (broad):
- Weak band (score < 3.5): Mamba-HMIL (3.25) — rejected, poor novelty/writing. HOMIL is clearly stronger.
- Middle band (3.5–7.5): MFC (6.00), Sequential MIL (4.50), Set-Level Labels (5.67)
- Strong band (score > 7.5): Various 8.00 papers — exceptional. HOMIL is clearly weaker.

Round 2 narrowing:
- MFC (6.00, scores 5/8/3/8): Similar WSI MIL domain, same datasets. MFC has more severe methodology issues (unclear methods, missing derivations); HOMIL is better written and its idea is cleaner.
- Covariance-Hessian (5.00, scores 3/6/6/5): Similar use of covariance matrices. HOMIL is more practically motivated and better situated in the WSI MIL literature.
- ChannelViT (6.50, scores 5/5/8/8): Stronger experimental validation but less novelty in the WSI domain per se.

HOMIL is a well-written paper with a clear motivation and solid contributions (second-order moments in MIL, adaptive clustering for efficiency), but its empirical results are undermined by overlapping error bars and modest improvements, and there are methodological inconsistencies (covariance weighting terminology, ad-hoc vectorization). It sits between the 5.00 and 6.00 anchors — I place it at **5.5**.

## Summary

This paper proposes HOMIL, a multi-instance learning framework for whole-slide image classification that extends ABMIL by incorporating second-order statistical moments (covariance matrices) alongside the standard first-order (attention-weighted mean) aggregation. Adaptive DBSCAN clustering reduces computational cost by grouping similar patches before moment computation. Experiments on CAMELYON16 and TCGA-NSCLC show competitive accuracy and substantially lower runtime than many dynamic-aggregation baselines.

## Strengths

- **Novel application of second-order moments to MIL for WSIs.** The paper gives a clean statistical interpretation of ABMIL as first-order moment estimation and extends it to covariance-based second-order information. The ablation (Table 3) directly confirms that the second-order module contributes: removing it drops AUC from 99.23% to 98.51% and F1 from 96.54% to 94.94% on CAMELYON16.

- **Substantial efficiency gains from adaptive clustering.** DBSCAN naturally groups abundant normal tissue into large clusters and rare pathological regions into small clusters. This yields large speedups: HOMIL completes 5-fold evaluation on CAMELYON16 in 310s versus 7,200s for MambaMIL and 10,800s for HMIL, while achieving the highest accuracy (Table 1). The ablation confirms removing clustering increases runtime by 71% (to 530s).

- **Consistent top results across two benchmarks.** On both CAMELYON16 (metastasis detection) and TCGA-NSCLC (lung cancer subtyping), HOMIL achieves the highest ACC, AUC, and F1 among nine compared methods, showing generalization across different diagnostic tasks and tissue types.

- **Theoretical connection to ABMIL.** The paper notes that ABMIL is a special case of HOMIL when second-order moments are omitted and each cluster contains a single patch, providing a clean unifying perspective.

- **Attention-based fusion of first- and second-order representations.** The adaptive gating mechanism (Section 4.3.4) dynamically balances the two moment embeddings, and Figure 2b shows the second-order weight remains non-trivial (~0.4–0.45), supporting its complementary role.

## Weaknesses

### Fatal
None.

### Major

1. **Statistical significance of results not established.** The performance improvements over the strongest baselines are modest (on TCGA-NSCLC: +0.35% ACC over HMIL, +0.10% F1 over HMIL; on CAMELYON16: +0.50% ACC over MambaMIL, +0.21% AUC over S4MIL). The reported standard errors overlap substantially — e.g., on CAMELYON16, HOMIL AUC is 99.23±0.62 vs. S4MIL at 99.02±0.87, and ACC standard errors are 2–3% for several methods. The paper provides no statistical test (paired bootstrap, McNemar, or confidence intervals) to establish that differences are not due to chance variation. The abstract's claim that HOMIL "significantly improves the state-of-the-art performance" is therefore unsupported by the evidence presented.

2. **Inconsistency between claimed and implemented covariance aggregation.** The paper describes the second-order stream as computing an "attention-weighted covariance matrix of cluster features" (Section 4.1, Section 4.3.3). However, the formula in Section 4.3.3 gives **C = Σ_{k=1}^K \tilde{g}_k \tilde{g}_k^T** with no attention weights appearing in the sum. The centering uses the attention-weighted first-order mean v^{(1)}, but the outer-product sum itself treats all clusters uniformly. If attention-weighted covariance is intended, the implementation is inconsistent with the description. If the unweighted sum is intentional, the "attention-weighted" label is misleading. Either way, this discrepancy between stated design and actual computation needs resolution.

### Minor

1. **Ad-hoc covariance vectorization without justification or ablation.** The d×d covariance matrix is compressed to a d-dimensional vector via row-wise 1D convolution with T=4 kernels of dimension m=64, followed by two max-pooling operations (Section 4.3.3). No rationale is given for why four kernels of size 64 were chosen, and no ablation compares this to simpler alternatives (e.g., flattening the upper triangle, using the diagonal, or a learnable linear projection). This makes it hard to assess whether this complex vectorization is beneficial or merely incidental.

2. **Overclaimed language.** The abstract claims the method "greatly enhance[s] classification accuracy" and "significantly improves state-of-the-art." Given the modest margins and overlapping error bars (point 1 above), and the fact that the largest gains come from clustering + first-order rather than second-order alone, these claims overstate what the experiments demonstrate.

3. **Baseline hyperparameter tuning not reported.** The paper states all baselines use a "unified codebase" but does not clarify whether each baseline's hyperparameters were tuned or left at defaults. Without this information, the fairness of the comparison across methods is uncertain.

### Trivial
None.

## Nice-to-Haves

- A comparison with alternative vectorization strategies for the covariance matrix (e.g., using the diagonal, flattening the upper triangle, or a simple linear projection) would strengthen the paper by justifying or simplifying the current convolution-based approach.
- A brief visualization of cluster assignments overlaid on a WSI (e.g., showing small clusters on rare pathological regions and large clusters on normal tissue) would concretely illustrate the adaptive clustering motivation.

## Removed Points

- **Missing comparison with DeepO2P, bilinear pooling, or Gaussian covariance models.** Per policy, criticisms about missing related works are not included, as the reviewer may not know which works the authors deliberately chose to cite or omit.
- **Sensitivity of DBSCAN parameters relegated to inaccessible appendix.** The parser strips appendices; the appendix exists in the original submission and the paper mentions the sensitivity analysis is there.
- **"No analysis of cluster characteristics."** This is a suggestion for additional experiments rather than a flaw in the presented work; the paper provides the compression ratio and the ablation study adequately supports the clustering's effectiveness.

## Novel Insights

The reviews surface a central tension in this paper: the idea of using second-order moments in MIL is genuinely novel and well-motivated, and the efficiency gains from adaptive clustering are clearly demonstrated and practically significant. However, the actual accuracy improvements over strong baselines are smaller than the paper's rhetoric suggests, and the evidence that these improvements are statistically reliable is absent. The harsh critic correctly identifies the covariance weighting inconsistency and the ad-hoc vectorization as areas where the method's presentation needs tightening. The net assessment is that HOMIL makes a real contribution — introducing covariance into MIL aggregation for WSIs — but its current presentation overclaims the empirical results and contains unnecessary imprecision in the method description.

## Suggestions

1. Resolve the covariance weighting discrepancy: either incorporate attention weights into the outer-product sum to make it truly "attention-weighted," or rename the component (e.g., "covariance around the attention-weighted mean") and clarify in the text.
2. Add statistical significance tests (e.g., paired bootstrap or McNemar) for the key comparisons against the strongest baseline on each dataset.
3. Provide an ablation comparing the convolution-based vectorization against at least one simpler alternative (e.g., using the diagonal or a linear projection) to justify or simplify this design choice.
4. Tone down the claims in the abstract and conclusion to match what the evidence supports — "competitive performance" and "substantial efficiency improvements" rather than "significantly improves" and "greatly enhances."

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>