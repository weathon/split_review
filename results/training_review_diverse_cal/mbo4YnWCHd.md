Now I have a thorough understanding of the paper and the reviewer claims. Let me compose the final consolidated review.

## Summary

This paper proposes a unified EM-based framework for non-negative tensor decomposition optimizing KL divergence for discrete density estimation. The key insight is establishing that the M-step optimization in EM for low-rank tensor learning reduces to a many-body approximation problem, for which the authors derive exact closed-form solutions for Tucker and Train decompositions (Equations 5 and 6), eliminating the need for gradient methods and learning rate tuning. The framework naturally extends to mixtures of low-rank structures (e.g., CP+Train), adaptive noise modeling, and more general tensor tree networks, all while maintaining sparsity-driven linear complexity in the number of observations. Empirically, the mixture model CPTrainON achieves competitive test cross-entropy on 7/8 real datasets against tensor-based baselines.

## Strengths

- **Unified EM framework for multiple low-rank structures optimizing KL divergence.** The paper provides a single EM algorithm that works with CP, Tucker, and Train decompositions (Section 3.1) by decoupling the M-step into independent many-body approximations. This goes beyond prior piecemeal approaches that required separate derivations for each low-rank format.

- **Closed-form M-step updates eliminating gradient methods.** The derivation of exact closed-form solutions for the many-body approximation in Tucker (Equation 5) and Train (Equation 6) decompositions is the paper's central theoretical contribution. These updates are simultaneous rather than factor-by-factor, and the EM formulation guarantees monotonic convergence without learning rate tuning.

- **Empirical demonstration that the CPTrainON mixture model outperforms tensor baselines.** CPTrainON achieves the best test cross-entropy on 7 out of 8 datasets compared to MPS, BM, and LPS (Table~\ref{tb:exp}), with standard errors reported.

- **Linear computational complexity in observations.** The framework exploits sparsity of the empirical tensor, achieving \(O(\gamma D N R)\) for EM-CP and \(O(\gamma D N R^2)\) for EM-Train via cumulative cores (Section 3.2), making it applicable to high-dimensional sparse data.

- **Extensions to tensor tree networks and adaptive noise.** Section 3.4 shows how complex low-rank structures decompose into independently solvable closed-form parts. The adaptive noise term (Section 3.5) is a learnable regularization that prevents overfitting without breaking convexity of the E/M steps.

- **Guaranteed monotonic convergence.** The EM algorithm ensures the objective increases monotonically each iteration (Theorem~\ref{th:conv} in supplementary), a formal guarantee not provided by gradient-based alternatives.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core contributions are sound and the methodology is clearly presented.

### Minor

- **Main empirical table lacks ablation of the framework's own components.** Table~\ref{tb:exp} compares only CPTrainON against three external tensor baselines (MPS, BM, LPS). The reader cannot tell from this table alone whether the mixture outperforms its constituents (vanilla CP, vanilla Train, CPTrain without noise/reordering). While Figure~\ref{fig:exp} (validation error vs. parameters) and the supplementary material partially address this, including component ablations in the main performance table would substantially strengthen the narrative about what drives the gains. The paper's own claim that "mixture of CP and Train generally performs well" would be better supported by clear ablative comparisons in the primary table.

- **Statistical significance of the claimed superiority is not established.** Standard errors are reported, but on several datasets (e.g., Chess2, Lymphography) the intervals overlap substantially across methods. The paper states "CPTrainON has the best generalization performance on all datasets except Chess2" without any significance test. Given only 10 random initializations, the observed rankings could be artifacts of noise. A minimal analysis—paired tests or effect sizes—would greatly increase confidence in the comparative claims.

- **The cross-entropy evaluation procedure on test data is underspecified.** The paper forms "test tensors" from test samples, but it is not explicit whether cross-entropy is computed only over the non-zero entries of these sparse test tensors or over the full tensor. This matters because a method assigning zero probability to unseen combinations would incur infinite cross-entropy, and the paper does not discuss smoothing for the test tensor.

- **Tucker decomposition's exponential complexity is a limitation stated too obliquely.** The complexity analysis gives \(O(\gamma D N R^D)\) for Tucker, and the experiments only test it on datasets with \(D \leq 4\). While this is acknowledged in passing ("due to its high computational cost"), the "unified framework" framing could create the impression that Tucker is on equal practical footing with CP and Train. The paper would benefit from stating this limitation more prominently than a single parenthetical remark.

### Trivial

- Dataset characteristics (D, I_d, N, sparsity) would improve interpretability if reported in the main paper rather than solely in the supplementary.

## Nice-to-Haves

- A brief sketch of why the closed-form solutions (Equations 5 and 6) are optimal (e.g., satisfying KKT conditions or decoupling properties) could improve reader confidence. The formulas are clearly stated and the proofs are in the supplementary (standard practice), but a short intuition would make the main paper more self-contained.
- Comparison against a simple non-tensor baseline such as a smoothed empirical distribution or naive Bayes would help contextualize whether the tensor machinery is beneficial for these specific datasets, though this is outside the paper's stated scope.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Closed-form solutions not substantiated in the main paper"** — The formulas (Equations 4, 5, 6) are directly stated in the main paper (Section 2.1). The derivations/proofs are in the supplementary, which is standard practice for mathematical contributions. The critic's suggestion that proofs belong in the main text does not reflect normal publication expectations.
- **"No baseline comparisons to simple non-tensor methods"** — The paper's stated scope is comparison to "conventional tensor-based approaches." Demanding non-tensor baselines is scope creep.
- **"Novelty of the many-body/low-rank connection"** — The paper explicitly acknowledges prior work (Ghalamkari 2023) and states "it is our contribution to clarify the relationship between general low-rank approximation and many-body approximation" (line 110). The contribution is properly scoped.
- **"Adaptive noise impact is modest"** — The paper transparently states "the noise term does not change the generalization performance significantly" and instead documents its value in preventing overfitting at large parameter counts (supplementary Figure 1). The critic's observation agrees with the authors' own characterization.
- **"Mode reordering effect not clearly separated"** — The paper states this is examined in the supplementary material, which is standard practice for secondary analyses.

## Novel Insights

None beyond the paper's own contributions. The reviews affirm the paper's core claims without introducing new perspectives not already in the paper.

## Suggestions

- Restructure the main empirical table (Table~\ref{tb:exp}) to include ablated variants: vanilla CP, vanilla Train, CPTrain (without noise/reordering), and CPTrainON alongside the external baselines. This would clearly isolate the contribution of each component.
- Add a brief sentence clarifying how test cross-entropy is computed: "The test cross-entropy is computed over the \(\sum_{\boldsymbol{i}} \mathcal{T}^{\text{test}}_{\boldsymbol{i}} \log \mathcal{P}_{\boldsymbol{i}}\) where \(\mathcal{T}^{\text{test}}\) is the test empirical tensor (non-zero only at observed test combinations)."
- Report whether the observed rankings in Table~\ref{tb:exp} are stable under paired comparison (e.g., McNemar's test or bootstrap confidence intervals for the difference).
- Add a brief footnote or sentence noting that Tucker complexity scales exponentially with D and is mainly suitable for low-dimensional data (\(D \lesssim 4\)), rather than burying this in the experimental setup paragraph.

## Score and Decision

The paper makes a genuine theoretical contribution: establishing the connection between many-body approximation and low-rank decomposition to derive closed-form EM updates, and providing a unified framework supporting mixtures, adaptive noise, and tensor tree structures. The technical development is sound, the complexity analysis clear, and the empirical results support the main claims. The weaknesses are presentation-level (underspecified evaluation details, missing ablations in the main table, unquantified significance) rather than structural. These are readily addressable in a revision.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>