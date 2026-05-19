Now let me run calibration searches to anchor my score.**Round 1 bracket: 5 to 6.5**

The paper makes genuine theoretical contributions (first consistency proof for Lasso-penalized DNN training) but has overclaimed applied results. Let me narrow down with round 2 calibration.Now I have all the information I need. Let me write the final review.

---

## Summary
This paper proposes using the Stochastic Neural Network (StoNet) — a composition of layer-wise Gaussian regressions — as a principled bridge between linear models and deep neural networks. Its two main contributions are: (1) Theorem 1 + Corollary 1, which establish, for the first time, consistency for Lasso-penalized DNN parameter estimation and structure selection via the StoNet–DNN asymptotic equivalence; and (2) a post-StoNet procedure that retrofits a small sparse StoNet onto the last-hidden-layer representations of a pretrained DNN for prediction uncertainty quantification.

---

## Strengths

- **First consistency proof for Lasso-penalized DNN training (Corollary 1, Section 3.1):** The paper establishes, through Theorem 1 and the asymptotic equivalence of Lemma 1, that training a DNN with a Lasso penalty yields consistent parameter estimation and structure selection. The paper explicitly notes this practice had been common (Scardapane et al., 2017; Lemhadri et al., 2019) without theoretical justification — filling this gap is a genuine contribution.

- **Explicit convergence rates in Theorem 1:** The paper provides concrete bounds $r_n$ depending on layer widths $d_{l,n}$, noise variances $\sigma_{l,n}^2$, sparsity exponents, and sample size $n$. This level of specificity goes beyond an asymptotic existence claim and gives operational meaning to the result.

- **Novel post-StoNet UQ procedure:** The idea of using last-hidden-layer representations from a pretrained DNN as compressed features for a sparse StoNet is conceptually clean and practically motivated. The intuitive justification in Section 6.2 — that the DNN's representation approximates a sufficient dimension reduction, simplifying the residual mapping — is coherent and well-articulated.

- **Recursive UQ via Eve's law (Section 4):** The derivation of prediction interval widths through iterated application of Eve's law across StoNet layers is a principled and elegant adaptation of classical statistical tools to the deep learning setting. Coverage rates on synthetic data (Table 1) confirm it works under controlled conditions.

- **Empirical validation of sparse structure recovery (Figure 2, Section 5):** The regularization paths for both StoNet and DNN correctly recover the 5 true variables from 20 under strong mutual correlation ($\rho = 0.5$), directly supporting Corollary 1.

---

## Weaknesses

### Fatal
None.

### Major

- **Misleading "superiority" framing relative to conformal prediction (Abstract, Section 6.2, Conclusion):** The paper repeatedly claims the post-StoNet procedure is "superior" to split conformal prediction on the basis of shorter prediction intervals. However, split conformal prediction (Vovk et al., 2005; Shafer & Vovk, 2008) provides a finite-sample, distribution-free marginal coverage guarantee regardless of model specification; the post-StoNet method provides only asymptotic, model-dependent coverage. Shorter intervals under a weaker guarantee is not superiority — it may simply indicate anti-conservatism. Table 3 reports *average* coverage rates across datasets, but average coverage can conceal systematic undercoverage on specific datasets or input regions. The abstract's claim that "numerical results suggest its superiority" and the conclusion's "significant improvement compared to the conformal method" are not honestly framed. The authors need to either (a) explicitly acknowledge the difference in guarantee types and reframe the comparison as a favorable empirical trade-off rather than algorithmic dominance, or (b) provide per-dataset coverage profiles and a more rigorous coverage analysis.

### Minor

- **Training residual variance near zero for overparameterized models (Section 4, Step i):** The UQ procedure estimates prediction variance by adding $\widehat{\Sigma}_{h+1,j}^{(t)}$ (propagated parameter uncertainty) and $\hat{\varsigma}_{h+1,j}^{2(t)}$ (training MSE). For overparameterized DNNs — the primary practical motivation — training MSE is near zero, making the residual term negligible. Intervals would then be driven entirely by propagated parameter uncertainty $\widehat{\Sigma}$. The paper does not discuss whether this is desirable behavior or whether held-out (rather than training) residuals should be used in such settings.

- **Synthetic validation uses data generated from the exact target model (Section 5):** The illustrative example (equations 8–9) generates data from exact DNN models and then validates the StoNet on them. The paper acknowledges this ("To make the tests more convincing, we particularly generated the data from true DNN models"), but this means Table 1's coverage rates represent a best-case validation rather than robustness evidence. Even mild misspecification of the StoNet structure could materially affect coverage, and this is not tested.

- **No evaluative evidence for feature identification in CoverType (Section 6.1):** Figure 3 displays a regularization path for the CoverType dataset, but there is no ground truth for feature importance on real data and no comparison to standard feature attribution methods (e.g., permutation importance or gradient-based measures). The section demonstrates the concept but provides no evaluative evidence that the StoNet's rankings are more accurate or calibrated than alternatives.

- **Slower rate for logistic output not discussed (Theorem 1, second rate formula):** The logistic-output case has a terminal term of order $n^{-2(1-\varepsilon)/3}$, which is strictly slower than the parametric $n^{-1}$ rate appearing in other terms. The implications of this slower rate for classification tasks — including how large $n$ must be for the bounds to be practically informative — are not discussed anywhere in the paper.

### Trivial
None.

---

## Nice-to-Haves

- A calibration plot (empirical coverage at a range of nominal levels, not just 95%) for the post-StoNet procedure would be the standard diagnostic in the calibration literature and would greatly strengthen the applied contribution.

- A worked discussion of how the layer widths $d_{l,n}$, noise variances $\sigma_{l,n}^2$, and $n$ must relate for $r_n = o(1)$ — even a simple example — would make Theorem 1 more operationally meaningful for readers.

- The comparison in Section 6.2 would be more honest if conformal prediction were applied to the last-hidden-layer representations (same feature space as the post-StoNet) rather than to the raw inputs; this controls for the informational advantage conferred by DNN compression.

- CIFAR-10 is a relatively simple benchmark; discussion of the method's expected behavior on harder tasks, or explicit acknowledgment of this limitation, would help scope the contribution appropriately.

---

## Removed Points

*These points were filtered out; treat with caution.*

- **Assumptions A1–A6 not stated in the main text:** The harsh critic argues that readers cannot evaluate Theorem 1 without knowing what assumptions are required. However, the paper's appendix (stripped by the parser) contains these assumptions; the main text references them by name. Per review rules, criticisms about missing appendix content are removed. The reviewer is correct that summarizing the key assumptions in the main body would improve accessibility, but this is a presentational nice-to-have, not a substantive flaw.

- **Post-StoNet applied to "too small" validation sets for asymptotic guarantees:** The harsh critic notes that a 5,000-sample validation set for CIFAR-10 may be too small for asymptotic approximations to be reliable. While valid in principle, demanding that practical papers provide sample-size analyses for every finite-sample approximation is not standard in the field, and the empirical results speak for themselves. Demoted to informational note.

- **Theory assumes the true model is an exactly-specified StoNet:** The harsh critic calls this a significant gap between theory and practice. This is correct but is a universal feature of statistical theory papers (assume the model is correct, apply to practice). The paper is explicit about this assumption ("For simplicity of theoretical development, we will assume..."), and this is standard.

- **The Strength Finder's generic framing of "universal approximation property" and "the StoNet bridges an important gap":** These were removed as too generic and not specific enough to constitute a grounded strength.

---

## Novel Insights

The most genuinely novel observation is the structural mechanism connecting sparse linear model theory to DNNs via the StoNet's Markov decomposition: because the StoNet's joint distribution factors into independent layer-wise regressions (equation in Section 3.1), Lasso theory for linear models can be applied layer-by-layer, and the resulting sparse estimator is then shown to be consistent for the DNN through the asymptotic equivalence of Lemma 1. This two-step transfer — from linear model theory to StoNet via the Markov structure, then from StoNet to DNN via asymptotic equivalence — is an elegant and potentially reusable theoretical template for importing other classical statistical tools into the deep learning setting beyond Lasso (e.g., SCAD, adaptive Lasso, or group penalties).

---

## Suggestions

1. **Reframe the conformal comparison honestly:** Replace "superiority" language with an explicit discussion of the trade-off: post-StoNet yields shorter intervals under an asymptotic, model-dependent coverage guarantee, whereas conformal prediction provides finite-sample, distribution-free coverage. Report per-dataset coverage at the 95% nominal level (not only averages) to let readers judge whether the coverage holds where it needs to.

2. **Address the training MSE issue in Section 4:** Discuss the behavior of the UQ procedure when applied to overparameterized models with near-zero training residuals. Consider recommending held-out (rather than training) MSE for overparameterized settings.

3. **Summarize key assumptions inline:** Even two sentences — "Assumption A5 is a beta-min condition; A6 is an irrepresentable condition for the StoNet Gram structure" — would allow readers to gauge the scope of Theorem 1 without consulting the appendix.

---

## Score and Decision

**Calibration anchors across rounds:**

| Paper | Avg Human Score | Round | Topical Comparison |
|---|---|---|---|
| nrDRBhNHiB (multiobjective DNN regularization path) | 4.5 | R1 | Weaker theory, no consistency results; paper under review is stronger |
| MY8SBpUece (non-linear feature learning theory) | 5.5 | R1 | Similar theoretical depth; no applied overclaiming; similar tier |
| NHhjczmJjo (transformers, sparse recovery theory) | 7.0 | R1 | Cleaner theory with tight proofs; paper under review has wider scope but overclaims |
| FT4gAPFsQd (DNN pruning theory) | 6.0 | R2 | Similar ambition, also rejected; paper under review has stronger novelty claim |
| Jc0FssXh2R (feature learning criterion, two-layer NN) | 6.25 | R2 | Accepted; clean theory, no overclaiming; paper under review has stronger novelty on theory side but significant applied overclaiming |
| eQggPqESBr (simplicity bias) | 5.5 | R2 | Rejected; similar theoretical scope limitation |
| vcX0k4rGTt (approximating full conformal prediction) | 5.75 | R2 | Accepted; similar topic (post-hoc UQ for DNNs, conformal comparison); clean comparison framing that paper under review lacks |
| rulxyXjf46 (conformal prediction via regression-as-classification) | 6.25 | R2 | Accepted; cleaner conformal framing, no overclaiming |

**Round 1 bracket:** 5 to 6.5.

**Round 2 narrowing:** The paper's theoretical contribution (Corollary 1 as a first consistency result) places it above pure algorithmic papers like nrDRBhNHiB (4.5). However, the overclaiming on the applied side — particularly the repeated "superiority" framing vs. a method with fundamentally stronger guarantees — and the limited experiment scope (one image benchmark, a handful of UCI datasets, only average coverage rates) place it below accepted papers with honest, clean comparisons like Jc0FssXh2R (6.25) and vcX0k4rGTt (5.75). The paper is comparable to MY8SBpUece (5.5) and eQggPqESBr (5.5), both rejected theoretical contributions with scope limitations.

The core theoretical contribution is real and novel; it would likely be accepted on its own. But as submitted, the paper's applied framing misleads about the nature of the comparison with conformal prediction — this isn't a minor presentation issue but a repeated claim in the abstract and conclusion that mischaracterizes what the results show. Combined, this puts the paper at **5.5**.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>