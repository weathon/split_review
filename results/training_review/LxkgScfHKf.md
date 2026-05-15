Now I have a thorough understanding of the paper. Let me write the final consolidated review.

---

## Summary

This paper identifies a sample-inefficiency problem in ConfTr (Stutz et al., 2022), a conformal training method for length efficiency optimization: the gradient of the population quantile threshold τ(θ) with respect to model parameters has high variance because it effectively depends on only a few order statistics near the quantile. The authors propose VR-ConfTr, which replaces the naive quantile-gradient estimator with a variance-reduced estimator (ε-estimator or ranking-based conditional average) grounded in a quantile sensitivity formula (Hong, 2009). Experiments on four image-classification datasets show faster convergence and smaller prediction set sizes compared to ConfTr.

## Strengths

1. **Well-motivated problem identification.** Section 2.3 provides a clear variance analysis showing that the naive quantile-gradient estimator (based on order statistics) has approximately O(1) variance that does not decrease with batch size. This formalizes a genuine bottleneck in ConfTr that prior work did not explicitly articulate. The analysis acknowledges that smooth sorting makes things *approximately* piecewise constant (citing Blondel et al., 2020; Cuturi et al., 2019), showing awareness of the subtlety the harsh critic raises.

2. **Principally grounded solution.** Proposition 3.1 (from Hong 2009) gives an exact formula for ∂τ/∂θ as a conditional expectation of ∂E/∂θ. The ε-estimator (equation 13) and ranking estimator follow naturally from this identity, providing a theoretically motivated path to variance reduction rather than an ad-hoc heuristic.

3. **Consistent empirical improvements across four datasets.** VR-ConfTr achieves faster convergence (e.g., 10× fewer epochs on MNIST, one-third the epochs on FMNIST) and smaller test CP set sizes on every benchmark (MNIST, FMNIST, KMNIST, OrganAMNIST). On OrganAMNIST, VR-ConfTr improves where ConfTr fails to beat the baseline, illustrating practical value.

4. **Clean plug-in framework (Algorithm 1).** The approach separates quantile estimation from gradient estimation, enabling future estimators to be integrated seamlessly — a nice architectural contribution.

## Weaknesses

### Major

1. **Missing uncertainty quantification in the main empirical results — a critical gap for a paper titled "Conformal Training with Reduced Variance."** 
   - Figure 3 shows training loss and test-set-size trajectories as single lines without error bands, confidence intervals, or overlays of multiple runs. Since the paper's central claim is variance reduction, the most direct evidence would be to show that the *variance* of training trajectories shrinks — yet this is absent.
   - Table 1 reports set-size improvements as percentages without standard deviations or confidence intervals. Accuracy standard deviations are given, but the primary efficiency metric lacks uncertainty quantification. The text states results are "averages over 5-10 training trials" (line 218) and even says "average length efficiency and its standard deviation" will be shown (line 204), yet the table does not deliver the latter.
   - Without quantifying the variance of training curves and final set sizes, the reader cannot assess whether the observed improvements are statistically significant or simply noise. This is the most consequential weakness.

2. **Omission of key experimental details that affect reproducibility.**
   - Model architectures (depth, width, number of parameters) are never specified — only that the same architecture was used across methods.
   - The target set-size κ in the conformal loss (equation 2) is not reported, making it hard to assess what "smaller set sizes" means relative to the optimization target.
   - Hyperparameters (learning rate, batch size, number of epochs, temperature T, choice of ε or m beyond the heuristic formula, optimizer) are not reported. The paper only says "hyper-parameters tuning" was performed and "hyper-parameters are identical across ConfTr and VR-ConfTr."
   - The paper does not verify that marginal coverage is empirically satisfied by the CP procedure for all methods. If coverage is violated, set-size comparisons lose meaning.

### Minor

3. **The variance analysis in Section 2.3 rests on approximations whose accuracy is not quantified.** The derivation assumes order statistics are "approximately independent" and ω(θ) is piecewise constant (or approximately so with smooth sorting). While these are reasonable for building intuition, the paper does not assess how large the approximation error is in practice or whether it could affect the conclusions. The analysis would be stronger with a more rigorous treatment of the smooth-sorting case.

4. **The paper does not analyze the bias introduced by the ε-estimator or ranking estimator in the main text.** Proposition 3.1 gives the exact quantile gradient, but the ε-estimator (13) approximates it by conditioning on a neighborhood rather than the exact level set, introducing bias. The heuristic m = αn / log log n is presented without justification or ablation. (The formal analysis is deferred to Theorem 3.1 in the appendix, which was stripped by the parser — but the main text should at least state the bias-variance trade-off qualitatively.)

5. **No wall-clock time comparison.** VR-ConfTr's ranking estimator averages ∂E/∂θ over m samples (m = αn/log log n) rather than just 2 order statistics, increasing per-iteration computation. The paper claims faster convergence in epochs but does not confirm this translates into real time savings.

### Trivial

6. Section 4's "warm-up" GMM experiment (Figure 2) references Theorem 3.1 but does not clearly describe what the figure demonstrates; the caption says "bias and variance for the quantile gradient estimates" without labeling what is being compared or how to interpret the axes.

## Nice-to-Haves

- An ablation study on the choice of m (number of top samples) for the ranking estimator, to validate the heuristic m = αn / log log n and assess sensitivity.
- An empirical distribution plot of gradient estimates (ConfTr vs. VR-ConfTr at a fixed training step) to visually confirm variance reduction.
- Application to regression tasks with continuous conformity scores, to demonstrate generality beyond multi-class classification.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"The variance analysis studies a straw-man estimator that differs from what ConfTr uses."** — REMOVED. The paper explicitly acknowledges smooth sorting ("approximately piecewise constant when using a smooth sorting such as in (Blondel et al., 2020; Cuturi et al., 2019)") and the analysis applies to any quantile estimator whose gradient depends primarily on data near the quantile threshold — which includes smooth differentiable quantile estimators. The analysis is a valid motivation for why variance reduction is needed.

2. **"The theoretical analysis (Theorem 3.1) is absent from the main text."** — REMOVED. Per hard rules, the appendix (which would contain this theorem) was stripped by the parser. The theorem exists in the original submission.

3. **"Missing related works"** — REMOVED per instructions; reviewers cannot verify the existence of missing citations without external sources.

4. **Formatting/style nitpicks and typo concerns** — REMOVED per parser-artifact rule.

5. **"The paper does not mention that ConfTr uses a differentiable quantile estimator"** — REMOVED as factually incorrect. Line 105 explicitly states "employ any smooth (differentiable) quantile estimator algorithm."

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective that the paper itself does not already articulate.

## Suggestions

1. **Add error bands to all training curves.** Replace the single-line plots in Figure 3 with mean ± std/confidence bands over the 5–10 runs the authors already collected. This is the single most impactful change — it directly demonstrates variance reduction or its absence.

2. **Report set-size results with standard deviations** in Table 1, not just percentage improvements. The text already promises this.

3. **Provide a table of all experimental hyperparameters** (architecture, optimizer, learning rate, batch size, epochs, temperature T, target size κ, the value of m used for each dataset) to enable reproducibility.

4. **Add a coverage check** confirming all methods empirically achieve the desired 1−α marginal coverage.

5. **Include a wall-clock time comparison** to show that faster epoch convergence translates to real time savings despite the potentially higher per-iteration cost of the ranking estimator.

6. **If Theorem 3.1 is in the appendix, state its conclusion (the bias-variance trade-off formula) in the main text** so the reader can understand the theoretical grounding without consulting the appendix.

## Score and Decision

The paper tackles a real and important problem in conformal training, proposes a theoretically motivated solution, and demonstrates consistent empirical improvements. However, the experimental evaluation has a critical gap: for a paper whose central contribution is *variance reduction*, the main results lack the uncertainty quantification (error bars on training curves, standard deviations on set-size improvements) that would substantiate this claim. The missing experimental details additionally hinder reproducibility. These issues are addressable but non-trivial.

Given the strengths — a well-motivated problem, a principled solution, and consistent improvements across four datasets — the paper has clear merit. But the evidential gap in the core claim is too large for acceptance in the current form. I recommend rejection with strong encouragement to revise and resubmit.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>