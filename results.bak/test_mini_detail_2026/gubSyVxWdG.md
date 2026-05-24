Now I have a clear picture of the calibration landscape. Let me write the final consolidated review.

## Summary

This paper addresses the important problem of evaluating heterogeneous treatment effect (HTE) estimators when ground truth is unavailable. Building on the relative-error framework of Gao (2025), the authors propose a robust estimator that relaxes the requirement for consistent outcome regression models: Theorem 1 shows that √n-consistency and asymptotic normality of the relative error estimator hold provided only that the propensity score model is correctly specified and nuisance parameters converge faster than n^{-1/4}, even if outcome models are misspecified. To realize this, they design a weighted least squares loss (ℒ_wls) and balance regularizers (ℒ_const) embedded in a Dragonnet-inspired neural architecture. Experiments demonstrate that the evaluation framework achieves near-nominal coverage and substantially higher selection accuracy than conventional nuisance estimators. The paper also proposes an enhanced HTE estimator that averages outcome regression predictions across estimator pairs.

## Strengths

1. **Theoretically grounded relaxation of outcome-model consistency**: Theorem 1 (Section 4.4) proves that the relative-error estimator is √n-consistent and asymptotically normal when only the propensity score needs to be correctly specified, even with misspecified outcome regression models. This is a clear theoretical advance over Gao (2025), which required consistency of all nuisance estimators (Condition 2). The derivation in Section 4.1 showing how the key orthogonality conditions (Equation 4) eliminate first-order bias from misspecified outcome models is technically sound and well-motivated.

2. **Novel loss functions with demonstrated empirical benefit**: The weighted least squares loss ℒ_wls and the balance regularizer ℒ_const are creative components with clear theoretical motivation. The ablation study (Table 5) convincingly demonstrates their importance: removing ℒ_const collapses selection accuracy from 0.80 to 0.14 on IHDP and from 0.94 to 0.14 on Twins. The hyperparameter sensitivity analysis (Table 4) shows stable performance across a range of λ₂ values, indicating the method does not require fragile tuning.

3. **Strong empirical performance of the evaluation framework**: The core evaluation results (Figures 1, 2; Table 2) show that the proposed method achieves near-nominal 90% coverage while delivering substantially higher selection accuracy than conventional nuisance estimators (Linear Regression, Boosting) used in Gao's framework. The improvement is particularly striking on IHDP (selection accuracy 0.80 vs. 0.44/0.48), demonstrating that the method produces tighter, practically informative confidence intervals while maintaining validity.

4. **Clear motivation and problem framing**: Sections 2-3 effectively explain why relative error is preferable to absolute error and carefully lay out the limitations of existing methods, specifically the extrapolation challenges faced by outcome regression models versus the relative robustness of propensity score estimation. This framing makes the contribution easy to understand.

## Weaknesses

### Major

1. **Potential circular evaluation of the enhanced HTE estimator**: The paper presents the enhanced HTE estimator (Section 5) as a contribution, with Table 1 reporting both in-sample and out-of-sample PEHE/ATE results showing large improvements over baselines. The experimental protocol splits data 2:1 into training and test sets, with candidate HTE estimators trained on the training fold and the neural network trained on the test fold. However, the paper does not clarify whether a separate held-out set was used to evaluate the neural network's outcome regression predictions. If the "out-of-sample" metrics for the proposed method in Table 1 are computed on the same test data used to train the neural network, those numbers are in-sample for the neural network. This would make the HTE estimation results in Table 1 uninterpretable as out-of-sample evaluations. This issue primarily affects the secondary contribution (Section 5) rather than the core evaluation framework (Figures 1-2, Table 2), but the paper presents both as contributions and the abstract states the learning algorithm "exhibits desirable performance" based on these results.

2. **Unsubstantiated claim about sample splitting**: The paper asserts in Sections 1 and 4.4 that the method "does not require sample splitting" unlike Gao (2025). In the standard debiased machine learning literature (Chernozhukov et al., 2018), sample splitting or cross-fitting is used because flexible nuisance estimators can overfit and produce bias that does not vanish at the required rate. The paper provides no rigorous argument that its specific neural network training procedure avoids this problem — no Donsker-type conditions are invoked, no cross-fitting is described, and the theoretical analysis (Theorem 1) does not address whether the adaptive representation learning in the neural network affects convergence rates. The reference to Chernozhukov et al. (2018) and Semenova & Chernozhukov (2021) for convergence rates is insufficient because those works assume cross-fitting. This is fixable (adopt cross-fitting or provide a formal argument), but as presented the claim is unsupported.

3. **Gap between theoretical orthogonality conditions and soft-constraint implementation**: The theoretical derivation (Equation 4) relies on exact satisfaction of the orthogonality conditions at the population level to achieve the o_ℙ(n^{-1/2}) remainder. The actual implementation uses slack variables and a soft penalty (ρ-weighted ℒ_const) that only approximately enforces these conditions. The paper does not analyze the asymptotic bias introduced by this relaxation, nor does it provide conditions under which the gap is asymptotically negligible. The reference to Appendix F.4 for empirical validation does not substitute for theoretical analysis. This gap means Theorem 1 may not directly apply to the algorithm as implemented.

### Minor

4. **Propensity score sensitivity test tests noise, not misspecification**: The sensitivity analysis (Table 6) adds Gaussian noise to the true propensity score, which tests robustness to input noise rather than model misspecification. The scenario where the logistic representation cannot capture the true propensity score function (e.g., the true score depends on higher-order interactions not representable by the learned Φ) is not tested. This is a meaningful distinction because the method's theoretical guarantees rely on correct propensity score specification, and the experiment does not address what happens when this assumption is violated in a structural way.

5. **The enhanced HTE estimator's aggregation strategy lacks justification**: The uniform averaging over all estimator pairs (Section 5) is presented as a contribution without theoretical or empirical analysis of why this specific aggregation is beneficial. The paper acknowledges this as a limitation ("simple uniform averaging scheme... may underutilize the heterogeneous strengths of individual estimators"), but the experiments still present the aggregated estimator as a primary result without quantifying how much of the performance gain comes from averaging vs. from the neural network architecture itself. A comparison against using outcome regressions from a single pair would clarify this.

6. **Missing experimental details hinder reproducibility**: The paper does not report the number of neural network training epochs, learning rate schedule, how hyperparameters λ₁, λ₂, ρ were tuned, the architecture of the shared representation layers, or whether the same network architecture was used for all datasets. The paper states "See Appendix F.10 for training details of hyperparameter tuning," but the appendix was stripped. Even accounting for this, the main text should include at least the key architectural and training details.

7. **Notation confusion in Section 4.1**: The Taylor expansion uses the same symbol γ̃ for both the estimate and the probability limit, making the derivation unnecessarily hard to follow. The paper should use distinct symbols (e.g., γ̂ vs. γ̄) consistently throughout.

### Trivial

8. In Table 1, the column headers repeat (the final three columns appear to be duplicates), and in Table 5, column headers use superscript "ATE" where they likely mean "in" and "out" (e.g., `e_{PEHE}^{ATE}` should probably be `e_{PEHE}^{in}`). These appear to be formatting artifacts from PDF extraction.

9. The max operations in ℒ_const (Section 4.2) are not differentiable at the kink; the paper does not discuss how gradient-based optimization handles this (e.g., subgradient or smooth approximation).

## Nice-to-Haves

- A simulation study with known ground truth that systematically varies the degree of misspecification in both propensity score and outcome regression models, demonstrating the claimed robustness directly.
- Confidence interval widths or standard errors alongside coverage and selection accuracy in Table 2, to quantify whether the improvement in selection accuracy comes from tighter intervals (desirable) or other mechanisms.
- A more rigorous comparison with Gao (2025) using identical sample-splitting protocols to isolate the benefit of the proposed loss/architecture from the no-sample-splitting approach.

## Removed Points

- **Criticism that "the enhanced HTE estimator is evaluated under a potentially circular data-use protocol that invalidates the headline results" as a fatal flaw**: This concern is real and retained as a Major weakness (#1). However, it primarily affects the secondary contribution (Section 5), not the core evaluation framework. It is serious but not fatal because the paper's main contribution is the evaluation framework, which does not suffer from this issue. The severity was reduced from Fatal to Major accordingly.

- **Criticism about "running time analysis compares the proposed method to TARNet, which are not comparable tasks"**: This is partially valid but the paper presents runtime as a computational complexity assessment, not a direct comparison. The criticism overstates the issue.

- **Criticism that "the enhanced HTE estimator aggregation is ad-hoc and lacks theoretical justification"**: Retained as Minor weakness (#5). The paper acknowledges this limitation; it's a valid point but not a critical flaw.

- **Criticism about "the conversion from constrained to unconstrained optimization relies on max operations that are not smooth"**: Retained as Trivial (#9). This is a standard implementation detail addressable with subgradient methods or smooth approximations.

- **Strength Finder's generic strengths about "important problem" and "well-motivated"**: Removed as they are generic and lack specific evidence anchors beyond what is already captured.

- **Strength Finder's claim about "Consistent empirical superiority in HTE estimation" (Table 1)**: Weakened due to the circularity concern (Weakness #1). The evaluation framework results are strong, but the HTE estimation results have a caveat.

## Novel Insights

The most interesting tension across the reviews is that the paper has two distinct contributions — the evaluation framework and the enhanced HTE estimator — that should be judged on different evidentiary standards. The evaluation framework is well-supported theoretically and empirically; the enhanced HTE estimator has weaker support due to experimental design concerns. This bifurcation is unusual: typically if the core method is sound, derived methods inherit that soundness. Here, the derived method introduces its own evaluation challenges that are orthogonal to the core contribution. A sharper paper would either present the enhanced estimator with a clean held-out evaluation or frame it as a preliminary illustration rather than a co-equal contribution.

## Suggestions

1. **Clarify the data flow for the enhanced HTE estimator experiments**: Specify exactly which data splits were used to train the neural network and evaluate the resulting HTE estimates. If the evaluation was in-sample for the neural network, redo the experiments with a properly held-out set (e.g., a 3-way split or nested cross-validation) and report the corrected results.

2. **Adopt cross-fitting or provide a rigorous justification for no sample splitting**: The simplest path is to adopt cross-fitting, which is standard in the DML literature and would directly address both the sample-splitting concern and reduce concerns about overfitting in the nuisance estimators. If the authors believe cross-fitting is unnecessary, provide a formal argument citing specific regularity conditions satisfied by the proposed training procedure.

3. **Analyze the soft-constraint gap**: Provide either (a) a theoretical analysis showing that the slack-variable solution converges to the exact constraint solution as n → ∞ under the proposed training procedure, or (b) empirical evidence (e.g., from Appendix F.4) demonstrating that the constraint violation shrinks with sample size.

4. **Focus the paper on the evaluation framework and de-emphasize the enhanced HTE estimator**: The evaluation framework is the stronger contribution. If the enhanced HTE estimator's evaluation cannot be cleanly resolved, consider presenting it as a secondary illustration with appropriate caveats rather than a co-equal contribution.

5. **Redesign the propensity score sensitivity experiment**: Test structural misspecification (e.g., using a misspecified logistic model with missing interaction terms) rather than adding noise to the true scores. This would directly address the paper's claimed robustness to propensity score misspecification.

## Score and Decision

### Round 1 — Bracketing

I queried the human-review corpus for HTE/evaluation papers in three score bands.

**Weak anchors (≤ 3.5):**
- `y1N4v2v5Xz` (avg 2.50, Withdrawn) — CLAGA paper: proposed a metric and method for CATE inconsistency. Fundamentally flawed theory (reviewers noted the metric didn't capture what was claimed, and the method was essentially regularization framed as something new). The current paper is clearly stronger: it has sound theory, a well-motivated problem, and convincing empirical results for its core contribution.

**Middle anchors (3.5–7.5):**
- `qG6O3jMkCj` (avg 4.80, Accept Poster) — SurvHTE-Bench: a benchmark paper for survival HTE. Comprehensive but descriptive; limited actionable insights; some synthetic data issues. The current paper has stronger theoretical grounding and more targeted experiments, but narrower scope.

- `rxZdaKhu2I` (avg 6.00, Accept Poster) — Good Allocations from Bad Estimates: clean theory showing CATE estimation vs. allocation sample complexity gap. Strong theory but limited experiments. The current paper has broader empirical validation and more complex methodology, but less elegant theory.

- `lGaZimFbss` (avg 5.00, Accept Poster) — MOGA: matching method for HTE. Solid theory with error bounds, but limited to semi-synthetic evaluation and missing some relevant baselines. Comparable in theoretical depth; the current paper has more comprehensive experiments for its core claim.

- `EnVaI6s64d` (avg 6.00, Accept Poster) — DSPNET for dynamic network interference. Strong empirical results but concerns about strong identifiability assumptions and limited realism. Comparable to the current paper in having a meaningful methodological contribution tempered by some limitations.

- `d2L1ndOKjq` (avg 6.67, Accept Poster) — CausalFM: foundation model for causal inference. Broad scope, strong theory, competitive results. Stronger in terms of breadth and ambition than the current paper.

**Strong anchors (≥ 7.5):** Not relevant — the current paper is clearly below this tier.

**Initial bracket:** 4.5 to 6.5.

### Round 2 — Narrowing

I queried for anchors in (4.5, 6.5) and (6.0, 8.0) on similar topics.

Reading the full reviews of `lGaZimFbss` (5.00), `EnVaI6s64d` (6.00), `d2L1ndOKjq` (6.67), and `0Xi3WDwd5w` (7.00):

- The current paper is **stronger than** `qG6O3jMkCj` (4.80) and `lGaZimFbss` (5.00): it has a clearer theoretical contribution and more targeted experiments that directly support the core claim. The MOGA paper at 5.00 had similar theory quality but weaker baselines and experimental validation.

- The current paper is **comparable to** `EnVaI6s64d` (6.00): both have meaningful methodological contributions with some limitations (DSPNET: strong identifiability assumptions, synthetic-only data; Current paper: soft-constraint gap, sample-splitting concern). The current paper has stronger theoretical guarantees but the DSPNET paper addresses a harder problem (dynamic networks with interference).

- The current paper is **somewhat weaker than** `d2L1ndOKjq` (6.67) and `0Xi3WDwd5w` (7.00): CausalFM has broader scope and cleaner evaluation; the WO-learner has tighter theory-experiment integration. The current paper's secondary contribution (enhanced HTE estimator) introduces concerns that these papers do not have.

The narrowing narrows the bracket to approximately **5.0–6.5**. The paper sits near the middle of this range because the core evaluation framework is genuinely strong, but the unresolved concerns about (a) the enhanced HTE estimator's evaluation, (b) the unsubstantiated no-sample-splitting claim, and (c) the soft-constraint gap prevent it from being placed alongside the cleaner, more tightly-integrated papers at 6.5+.

### Final Score

**Score: 5.5** — A solid paper with a meaningful theoretical and methodological contribution (the evaluation framework for HTE estimators with relaxed outcome-model requirements). The core claims about the evaluation framework are well-supported. However, the secondary contribution (enhanced HTE estimator) has an unresolved experimental design concern, the "no sample splitting" claim is unsubstantiated, and the gap between the theoretical orthogonality conditions and the soft-constraint implementation is not analyzed. These issues are fixable and do not invalidate the main contribution, but they prevent the paper from reaching a higher score in its current form.

**Decision: Accept (Poster)** — The evaluation framework contribution is significant and well-supported. The issues primarily affect the framing and the secondary contribution, and are addressable in a revision.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>