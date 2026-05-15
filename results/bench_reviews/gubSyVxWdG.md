## Summary

This paper proposes a robust evaluation framework for heterogeneous treatment effect (HTE) estimators based on relative error. The key insight is that by identifying and enforcing specific moment conditions (Equation 4) through a novel weighted least-squares loss and constraint-based regularizer, the relative error estimator achieves √n-consistency and valid confidence intervals even when outcome regression models are misspecified — only correct specification of the propensity score model is required. The method is implemented via a Dragonnet-inspired neural architecture with shared representations. The authors also propose an extension that aggregates the learned outcome models across pairs of candidate HTE estimators to produce a new HTE learner.

## Strengths

- **Novel and principled methodological contribution**: The derivation of moment conditions (Equation 4) under which the relative error estimator is robust to outcome model misspecification is technically sound and clever. The design of the weighted least-squares loss ℒ_wls and constraint-based regularizer ℒ_const to enforce those conditions during nuisance parameter training is a genuine innovation directly motivated by the necessary theoretical conditions.

- **Convincing empirical evaluation for the core framework**: The proposed method achieves near-nominal 90% coverage across multiple estimator pairs on both IHDP and Twins (Figure 1), and substantially outperforms the plug-in Gao (2025) baseline on selection accuracy — e.g., 0.80 vs. 0.44 on IHDP (Table 2). The ablation study (Table 5) confirms that dropping ℒ_const severely degrades both HTE estimation and selection accuracy, isolating the contribution of the proposed loss design.

- **Relaxation of a practically restrictive condition**: The paper addresses a real bottleneck in prior work (Gao, 2025), which requires both propensity score and outcome models to be consistent at fast rates. The argument that outcome models are more susceptible to extrapolation error in practice (Section 3, Motivation) is well-reasoned, and the proposed solution convincingly reduces reliance on outcome model correctness.

- **Practical stability**: Sensitivity analyses demonstrate reasonable robustness to the hyperparameter λ₂ over a wide range (Table 4) and moderate robustness to propensity score perturbations (Table 6), supporting practical deployability.

## Weaknesses

### Major

- **Incomplete theoretical justification for the no-sample-splitting claim**: Theorem 1 asserts √n-consistency without sample splitting, assuming only n^{-1/4} convergence of nuisance estimators. The paper claims this as a key advantage over Gao (2025). However, the theoretical argument in Section 4.1 does not address the empirical process terms that typically necessitate sample splitting or cross-fitting in semiparametric inference with complex (neural network) nuisance models. The derivation relies on the moment conditions (4) eliminating first-order bias through E[Δ] = 0, but when nuisance parameters are trained on the same data used for the relative error estimator, the correlation between nuisance estimates and the estimating equation can introduce additional bias terms that the current analysis does not account for. The paper also does not verify that the neural network training procedure attains the assumed n^{-1/4} convergence rate. While the empirical coverage results are strong, the theoretical foundation for the no-sample-splitting claim remains incomplete. This weakens a central selling point of the method.

### Minor

- **The candidate set for HTE estimation is unspecified**: Table 1 reports "Ours" as the best-performing method across all metrics on IHDP and Twins, compared against 11 baselines. However, the paper never states which of those baselines (or which other estimators) constitute the candidate set K used to produce the aggregated estimator. Without this information, the reader cannot assess whether the comparison is fair — for instance, whether "Ours" benefits from access to estimators that are more informative than any single baseline. This should be straightforward to clarify.

- **Missing simple aggregation baseline for the HTE learner**: The aggregated HTE estimator in Section 5 averages the learned outcome models μ̂₁ − μ̂₀ over all pairs of candidate estimators. A natural baseline would be to simply average the original HTE predictions of the candidate estimators themselves, to disentangle the benefit of the neural network's learned outcome models from a generic ensemble effect. Comparing against such a baseline would strengthen the claim that the network architecture adds value beyond ensembling.

- **The standard-loss baseline for evaluation is partially addressed but incomplete**: Table 5's ℒ_wls & ℒ_ce row (without ℒ_const) is described as approximating Gao (2025) with the neural network as a nuisance estimator. However, a more informative ablation would replace ℒ_wls with standard MSE for outcomes (and standard cross-entropy for propensity) to isolate the benefit of the proposed WLS loss specifically. The current ablation shows the importance of ℒ_const but not the independent contribution of ℒ_wls over standard losses.

### Trivial

- **Sensitivity analysis on propensity score misspecification uses Gaussian noise** (Table 6): While informative as a first check, adding Gaussian noise to the true propensity score is not representative of realistic model misspecification (e.g., omitted interactions or nonlinearities). The conclusions about robustness should be qualified accordingly.

- **Hyperparameter sensitivity for ρ and λ₁ is deferred to appendix**: Results for penalty parameter ρ and cross-entropy weight λ₁ are only available in Appendix F.8 (stripped in the submission version). A brief summary in the main text would improve completeness.

## Nice-to-Haves

- The uniform averaging over all estimator pairs in Section 5 is acknowledged as a limitation by the authors (Section 7). An adaptive or data-driven weighting scheme would be a natural next step.
- Reporting average confidence interval widths alongside coverage rates would provide a more complete picture of practical utility, particularly to quantify how much tighter the proposed intervals are compared to the Gao baseline.
- Showing empirical values of the moment condition violations before and after training would help readers understand how effectively the soft relaxation enforces the desired constraints.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"The proof strategy is outlined but not provided"** — Removed per hard rules: proofs are in the appendix, which is stripped in the parser output. The original submission includes them.

- **"Results for λ₁ and ρ are deferred to an appendix that is not available for review"** — Removed per hard rules: the appendix exists in the original submission; its unavailability is a parser artifact, not an author error.

- **"The choice of candidate estimators used to produce 'Ours' in Table 1 is never stated"** — This was partially removed; the substantive concern about transparency remains as a Minor weakness, but any implication of dishonesty or fabrication is removed. The paper clearly does have a method; the issue is clarity of reporting.

- **"The description of how the network is actually trained for HTE estimation (training set, candidate estimators, cross-validation) is missing"** — This overlaps with the Minor weakness about unspecified candidate set. The specific phrasing about missing training details is softened since Section 6.1 provides dataset splits and the appendix (F.10) contains hyperparameter tuning details. The core issue (unspecified candidate set K) is retained.

## Novel Insights

The paper's key novel insight is that robustness to outcome model misspecification in relative error estimation can be achieved by identifying and enforcing a specific set of moment conditions (Equation 4) through carefully designed loss functions, rather than requiring both nuisance models to be consistent. The connection between the Taylor expansion of the estimator and the derived moment conditions — and the translation of those conditions into a weighted least-squares loss for outcomes plus a constrained optimization for the propensity score — is elegant and non-obvious. This approach effectively decouples the evaluation framework's validity from outcome model correctness, which is a meaningful step beyond the doubly-robust-style conditions in prior work.

## Suggestions

- Clarify in Section 6.1 exactly which estimators form the candidate set K for the "Ours" method in Table 1, and discuss whether any of those candidates overlap with the listed baselines.
- Add a brief discussion in Section 4.4 addressing why sample splitting is unnecessary under the proposed framework — specifically, whether the moment conditions (4) are sufficient to eliminate empirical process bias, or whether additional regularity conditions (e.g., Donsker properties) are implicitly assumed.
- Include a simple-average-of-candidates baseline in Table 1 to isolate the contribution of the learned outcome models.
- Report confidence interval widths alongside coverage to quantify the practical tightening relative to the Gao baseline.

## Score and Decision

### Anchor comparisons

| Anchor | Score | Comparison |
|--------|-------|------------|
| `/home/wg25r/review_agent/human_reviews_2026/0Xi3WDwd5w.md` | 7.00 | Overlap-weighted meta-learner; stronger theoretical guarantees (Neyman orthogonality fully proven), comparable experimental scope. Current paper is weaker theoretically (incomplete no-splitting justification) but offers a more practical evaluation framework. |
| `/home/wg25r/review_agent/human_reviews_2026/rxZdaKhu2I.md` | 6.00 | Good allocations from bad estimates; elegant theoretical insight with weaker experiments. Current paper has stronger experiments and a more practical contribution but a similar theoretical gap. Comparable quality. |
| `/home/wg25r/review_agent/human_reviews_2026/dYaos1ITw4.md` | 6.00 | Topological causal effects; novel framework with strong theory. Current paper is comparably novel but has a weaker secondary contribution (HTE learner). |
| `/home/wg25r/review_agent/human_reviews_2026/O6iPDyUP97.md` | 4.67 | Treatment responder classification; decent theory but weaker empirical scope. Current paper is clearly stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/mPrnJcEhGR.md` | 4.00 | Bias-correction term estimation; limited to synthetic data, marginal gains. Current paper is substantially stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/NIA49K1k1N.md` | 3.50 | Assumption-lean inference; novelty concerns, missing confidence bands. Current paper is meaningfully stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/sJxz6o5jKM.md` | 3.00 | ECAM; major methodological gaps. Current paper is much stronger. |

The paper's core contribution — a robust evaluation framework for HTE estimators that relaxes outcome model requirements — is novel, well-motivated, and empirically validated. The evaluation experiments are convincing and the loss design is clever. The main weakness is the incomplete theoretical justification for the no-sample-splitting claim, which is a key differentiator from prior work. The HTE learning extension is underdeveloped but secondary to the paper's main contribution. Relative to the anchors, the paper sits between the 6.00 and 7.00 anchors but closer to 6.00 due to the theoretical gap and secondary weaknesses.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>