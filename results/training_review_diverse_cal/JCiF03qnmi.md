Now I have all the information I need. Let me compose the consolidated final review.

---

## Summary

This paper investigates how critical batch size (CBS) scales with model size and data size in autoregressive language model pre-training. It proposes a formal definition of CBS, conducts controlled experiments on models from 85M to 1.2B parameters trained on C4, and fits scaling laws to decouple the effects of model and data size. The central finding is that CBS scales primarily with data size/training duration, not with model size — a result supported by theoretical analysis via infinite-width limits (µP) and least-squares regression with mini-batch SGD.

## Strengths

- **Controlled decoupling of model and data size.** The paper directly compares CBS growth under three conditions: Chinchilla-optimal scaling (both N and D increase), fixed model size with varying data, and fixed data size with varying model size. The dramatic drop in the scaling exponent (from 0.47 when both scale to 0.087 when only model size scales) provides clean empirical evidence that CBS depends primarily on data size. [Verified: lines 121–141, Figure teaser]

- **Formal, reproducible definition of CBS.** The paper gives a precise operational definition of CBS as the batch size at which the number of steps to reach minimal loss exceeds the linear extrapolation from the optimal batch size by 20% (Section 3.1). This enables reproducible measurement and quantitative scaling-law fitting.

- **Exponential weight averaging (EWA) methodology.** Using EWA to reach a target validation loss without pre-specifying total training steps is a practical innovation that enables variable-length training, essential for measuring CBS across different batch sizes and durations without committing to a fixed schedule. [Verified: line 90]

- **Theoretical grounding.** Two theoretical results provide complementary support: (1) an infinite-width argument (Theorem 3.1) showing that for fixed data, CBS should not scale with model width beyond a point, and (2) a least-squares regression analysis (Corollary 3.2) formally deriving $B^* \eqsim D^{1-a/\min\{b, 2a+1\}}$ under power-law conditions, showing that CBS grows with data when variance error dominates.

- **Quantitative scaling laws.** The paper fits explicit power laws: $B^* = 93.20 \cdot N^{0.47}$ for Chinchilla-optimal training and $B^* = 621.341 \cdot N^{0.087}$ for fixed data size, providing concrete, reusable estimates for practitioners. [Verified: lines 121, 124, 133]

## Weaknesses

### Fatal
None.

### Major

- **No sensitivity analysis for the CBS definition.** The paper defines CBS using a 20% overhead threshold and $B_{\text{opt}} = 256$, but never examines whether the fitted scaling exponents are stable under alternative choices (e.g., 10% or 30% overhead, $B_{\text{opt}} = 128$ or 512). The note that "20% can be replaced by any other suitable measure" (line 111) acknowledges the choice but does not test its impact. Without this check, the quantitative exponents (0.47, 0.087) could be artifacts of the specific threshold rather than robust properties of the optimization landscape. Similarly, the paper asserts $B_{\text{opt}} = 256$ lies in the linear regime (line 117, citing an appendix) but does not show how much the scaling results drift if a different $B_{\text{opt}}$ were used.

- **No uncertainty quantification on fitted scaling exponents.** The scaling laws are fitted on only 5 model sizes spanning a 14× range (85M–1.2B). Power-law exponents fitted over such a short range are inherently noisy, yet the paper reports exponents to three decimal places (e.g., 0.087, 0.47) without confidence intervals, bootstrap estimates, or leave-one-out validation. This is below the standard of rigor established by prior scaling-law work (e.g., Kaplan et al. 2020, Hoffmann et al. 2022), which typically report uncertainty or validate predictions on held-out points. The qualitative conclusion (CBS scales with data, not model) is likely robust, but the specific exponent values cannot be trusted without uncertainty bounds.

### Minor

- **Loose connection between theory and experiments.** The infinite-width argument (Theorem 3.1) relies on Maximal Update Parameterization (µP), but the experiments use standard Adam initialization — not µP. The paper acknowledges this gap (line 167) but does not bridge it (e.g., via a small-scale µP experiment or by arguing why the result should hold under standard initialization). Similarly, the linear regression analysis (Corollary 3.2) assumes squared loss, Gaussian data, constant learning rate, and SGD — far from autoregressive language modeling with Adam, cross-entropy loss, and learning rate schedules. While simplified theoretical models can provide useful intuition, the paper does not derive any empirically testable prediction from the theory (e.g., a specific functional form of CBS vs. D whose fitted exponent can be compared against the theoretical range), making the theory feel parallel to rather than integrated with the experiments.

- **Empirical CBS and theoretical CBS are not defined on the same objective.** The empirical CBS is the batch size at which step-efficiency degrades by 20% (an overhead-based definition). The theoretical CBS in Corollary 3.2 is the batch size that minimizes sequential runtime while achieving the optimal *excess risk rate* (a rate-optimality definition). These are different optimization objectives, and the paper does not argue that they should coincide or that the scaling exponent from one transfers to the other. The claimed synergy between theory and experiment is weakened by this mismatch.

- **Fixed α = 1 without showing the comparison.** The paper states "We adopt the fixed α = 1 solution, as both strategies yield nearly identical forecasting results" (line 118) but provides no plot or table comparing the free-α vs. fixed-α fits. Readers cannot evaluate whether constraining α = 1 biases the subsequent CBS estimates or goodness-of-fit.

### Trivial
None.

## Nice-to-Haves

- **Sensitivity analysis for CBS threshold.** Re-plotting the key scaling figures using 10%, 30%, and 50% overhead thresholds (and alternative $B_{\text{opt}}$ values) would significantly strengthen confidence in the quantitative claims.
- **Uncertainty intervals.** Reporting bootstrap confidence intervals or leave-one-out predictions for the scaling exponents would align with standard practice in scaling-law papers.
- **Small-scale µP validation.** A brief experiment checking whether CBS indeed plateaus with width under µP initialization would bridge the largest gap between theory and experiment.
- **Multi-epoch clarification.** While single-epoch training is standard for large LMs, briefly discussing how the results would (or would not) translate to multi-epoch settings would prevent potential misinterpretation.

## Removed Points

- **Critic's Claim 3 (decoupling experiment confound).** The critic claims the target loss is defined as the validation loss of the 151M model at its Chinchilla step. However, the paper states (line 131): "record the target validation loss **for each model size**" — meaning each model has its own target loss (its loss after 3.072B tokens). The critic's specific concern ("under-training could compress the range of batch sizes that reach the target loss, artificially flattening the CBS-vs.-model-size curve") is based on this misreading. Removed as factually incorrect.

- **Critic's Claim 5 (data size vs. training duration conflation).** The paper explicitly states they use these interchangeably (line 40: "data size $D$ (or training duration thereafter, which we will use interchangeably)"). In single-epoch pre-training (the paper's setting and the norm for large LMs), they are equivalent. Moved to Nice-to-Haves as a clarification point rather than a genuine weakness.

- **Strength Finder's generic strengths about "important problem" / "interesting question".** The strengths provided by the Strength Finder were all substantive and specific (controlled experiments, formal definition, EWA methodology, theoretical justification, quantitative laws, hyperparameter tuning). None were generic. No strengths needed removal.

## Novel Insights

Beyond the paper's own contributions, the most striking insight from the reviews is that the near-zero exponent (0.087) for CBS vs. model size at fixed data size makes the scaling-law framing somewhat self-undermining: the main lesson is not a precise exponent but the qualitative saturation. This suggests that future work might profit more from analyzing why CBS plateaus (e.g., via gradient noise scale measurements or the µP lens) than from debating exact exponent values. The contrast between the clean theoretical prediction of saturation and the noisy empirical fit points to a gap where deeper experimental diagnostics (e.g., measuring gradient noise scale across model sizes) could yield more insight than simply adding more model scales.

## Suggestions

1. Add a sensitivity analysis for the CBS definition threshold (10%, 20%, 30%, 50% overhead) and $B_{\text{opt}}$ choice (128, 256, 512) in the appendix, showing that the scaling exponents and qualitative conclusions are stable.
2. Report bootstrap confidence intervals or leave-one-out cross-validation for the power-law exponents, and add error bands to Figures 3 and 4.
3. Run a small experiment with µP initialization (e.g., on the 85M–302M models) to verify that CBS plateaus with width as predicted by Theorem 3.1.
4. Include the free-α vs. fixed-α comparison plot to justify the α = 1 choice.
5. Explicitly note in Section 3.3 that the fixed-data-size experiment assigns each model its own target loss (its loss after 3.072B tokens), not the 151M model's loss, to prevent misreading.

## Score and Decision

This is a solid, well-executed paper with a clear contribution: the finding that CBS scales primarily with data size rather than model size is empirically well-supported through careful controlled experiments. The formal definition of CBS and the EWA methodology are genuine methodological advances. The main weaknesses — lack of sensitivity analysis on the CBS definition, absence of uncertainty quantification on scaling exponents, and loose theory-experiment connection — are real but do not invalidate the paper's core qualitative finding. These issues are addressable and would strengthen an already convincing paper. I recommend acceptance with the expectation that the above robustness checks be added in the final version.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>