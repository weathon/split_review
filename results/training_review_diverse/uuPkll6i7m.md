Now I have a thorough understanding of the paper. Let me organize my final review.

## Summary

This paper introduces the concept of *certified calibration* — worst-case bounds on calibration metrics (Brier score and Expected Calibration Error) under adversarial perturbations for models that provide certified predictions (e.g., via randomized smoothing). The paper makes three main contributions: (1) a tight closed-form bound for the Certified Brier Score (CBS); (2) a mixed-integer program (MIP) formulation with an ADMM solver to approximate the Certified Calibration Error (ACCE); and (3) Adversarial Calibration Training (ACT) to improve certified calibration. Experiments show that ACT can reduce the ACCE by up to 12% at radius 1.0 on CIFAR-10 without harming certified accuracy.

## Strengths

1. **First formalization of certified calibration under adversarial attacks.** The paper identifies and addresses a genuine blind spot: while individual confidences can be certified (Kumar et al., 2020), no prior work provides system-level calibration guarantees under attack. The CCE and CBS definitions are new.

2. **Tight closed-form bound for the CBS.** Theorem 1 provides an analytic, tight upper bound on the Brier score given confidence certificates, which is a clean theoretical result with immediate practical value.

3. **Effective MIP-based approximation for the CCE.** The mixed-integer program formulation (Equation 9) is non-trivial and technically sound. Figure 2 demonstrates that the ADMM solver uniformly yields larger (i.e., more accurate) ACCE values than baselines (dECE and Brier confidences), with differences up to ~0.2 — a strong qualitative improvement.

4. **Adversarial Calibration Training (ACT) improves certified calibration.** Table 2 shows that ACCE-ACT reduces the ACCE from 56.36 to 47.08 at radius 1.0 on CIFAR-10 (a 12% relative reduction) while maintaining certified accuracy. Figure 3 further shows that ACT can *jointly* improve certified accuracy and calibration, which prior adversarial training methods do not achieve.

5. **Calibration attacks are shown to be severe even on robust models.** Table 1 demonstrates that ACE attacks can increase AdaECE from 3.70% to 47.23% on an ImageNet ResNet50 with standard training, and from 9.03% to 13.54% with adversarial training — motivating the need for certification.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **No uncertainty quantification in experiments.** All reported numbers (ACCE, CBS, certified accuracy) are point estimates with no error bars, confidence intervals, or multiple-seed results. Given the stochasticity of randomized smoothing, Monte Carlo estimation, and the ADMM solver, it is unclear whether the observed improvements are statistically significant. This weakens the empirical contribution but does not invalidate the core ideas. (Section 5, Tables 1-2, Figures 1-3.)

2. **ACCE is an approximate certificate, not a true guaranteed bound.** The ADMM solver for the MIP is not guaranteed to find the global optimum on this non-convex problem, so the ACCE may underestimate the true CCE. The paper is upfront about this (calling it "approximate" throughout, using "Towards" in the title), but the term "certified calibration error" (CCE) for the theoretical construct paired with an approximate solver creates a gap between framing and delivery. The paper would benefit from discussing how far the ACCE might be from a true certificate (e.g., via convex relaxation bounds). (Sections 3.2-3.4.)

3. **ADMM solver details are underspecified.** The paper states "ADMM always converges in under 3000 steps" (line 182) without clarifying what convergence means (a local optimum? a feasible point?) or how binary constraints on **a** are handled (relaxation + rounding? alternating minimization?). The stopping criterion and sensitivity to ADMM hyperparameters (e.g., penalty parameter ρ) are not discussed. This limits reproducibility. (Section 3.4.)

4. **No explicit limitations section.** The paper would benefit from a paragraph discussing: (a) the approximate nature of the ACCE, (b) dependence on the binning scheme, (c) computational cost scaling, and (d) that confidence certificates from Kumar et al. (2020) themselves use Monte Carlo estimation. (Section 6.)

5. **The "novel calibration attacks" framing is slightly overstated.** The (η,ω)-ACE attacks are a parameterized family of the existing ACE attacks (Galil et al., 2021), which the paper explicitly acknowledges. This is not a serious flaw but the contribution claims could better calibrate reader expectations. (Section 2.3.)

### Trivial

None.

## Nice-to-Haves

- **Compare ACT against post-hoc calibration on the base model.** A natural question is whether simple post-hoc methods (e.g., temperature scaling) applied to the SmoothAdv baseline can achieve similar certified calibration improvements. This would help isolate the value of the proposed ACT training. This is not a required experiment — post-hoc methods may not preserve certification structure — but would strengthen the paper.
- **Sensitivity analysis on the number of bins.** The CCE depends on the binning scheme. Showing results with an alternative binning (e.g., different number of bins or adaptive binning) would demonstrate robustness.
- **Oracle bound for the ADMM solver.** For small subsets, solving the MIP exactly (e.g., via brute force or an exact MIP solver) would help gauge how close the ADMM approximation is to the true CCE.

## Removed Points

*(These points are flagged to be removed; treat them with caution.)*

- **"No comparison to post-hoc calibration" treated as major weakness.** Moved to Nice-to-Haves. Post-hoc calibration's compatibility with the certification framework (which requires bounds on confidences, not just point estimates) is non-trivial. The paper's stated scope is certified calibration, not empirical calibration.
- **"Sensitivity analysis on 15 bins" from the Harsh Critic.** The number of bins used (M=15) is specified in the appendix, which the parser stripped. Criticizing missing appendix content is removed per instructions.
- **"Paper does not mention code release."** Speculative and not a weakness of the technical content.
- **"Missing related works."** Removed per instructions — cannot verify existence of works not cited.
- **"The ACCE is not a true certificate" treated as fatal/major.** Downgraded to minor. The paper consistently uses "approximate" (in ACCE name, abstract, and body), the title says "Towards Certification," and the CCE definition is clearly separated from the ACCE approximation. The paper is honest about this limitation.

## Novel Insights

None beyond the paper's own contributions. The reviews confirm the paper's framing: the CBS bound is genuinely tight, the MIP formulation is a sound technical step, and ACT shows meaningful empirical gains. No reviewer raised a structural flaw that the authors had not already partially addressed.

## Suggestions

1. Add error bars (standard deviations or bootstrapped confidence intervals) to all experimental tables and figures. For ImageNet, show that the observed marginal effects are not dominated by noise.
2. Add an explicit paragraph on limitations after the conclusion, acknowledging the approximate nature of the ACCE, dependence on binning, and Monte Carlo noise in confidence certificates.
3. Clarify the ADMM solver: how binary constraints on **a** are enforced, what the stopping criterion is, and what "converges" means for the non-convex problem.
4. Consider including a small-scale experiment (e.g., on a subset with exact MIP solving) to bound the gap between the ACCE and the true CCE.

## Score and Decision

The paper makes a meaningful contribution by identifying and formalizing a novel problem (certified calibration), providing a tight bound for the CBS, a non-trivial MIP formulation for the CCE, and a practical training method (ACT). The weaknesses are real but not fatal: the lack of error bars and underspecified ADMM details are typical issues addressed at the camera-ready stage, and the approximate nature of the ACCE is explicitly acknowledged. The core claims — that the CBS bound is tight, that the MIP formulation yields better CCE approximations than baselines, and that ACT improves certified calibration — are supported by the presented evidence.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>