Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary

This paper investigates how critical batch size (CBS) — the batch size threshold beyond which doubling batch size no longer proportionally reduces steps — scales with model size and data size in autoregressive language model pre-training. Through controlled experiments with models up to 1.2B parameters on C4, the authors find that CBS scales primarily with training data size ($B^* \propto N^{0.47}$ under Chinchilla scaling) while remaining nearly invariant to model size when data size is fixed ($B^* \propto N^{0.087}$). The paper provides theoretical justification through infinite-width limits of neural networks (for model-size invariance) and least-squares regression analysis (for data-size scaling).

## Strengths

- **Controlled decoupling of model size and data size effects on CBS (Sec. 3.2)**: The paper runs separate experiments holding data fixed while varying model size (Fig. teaser, right) and holding model fixed while varying data size (Fig. teaser, middle). This directly disentangles two factors that prior work (McCandlish et al., Kaplan et al., Chinchilla) scaled jointly. The observation that CBS grows under fixed-model/variable-data but is nearly flat under fixed-data/variable-model is the paper's central evidence.

- **Theoretical derivation of CBS scaling with data size via least-squares regression (Corollary 1, Sec. 4.2)**: Corollary 1 derives $B^* \eqsim D^{1-a/\min\{b,2a+1\}}$ for mini-batch SGD in well-specified linear regression under power-law source and capacity conditions. This provides a formal mechanism for CBS growth with data size when variance error dominates, going beyond the heuristic gradient-noise-scale argument of prior work.

- **Formal definition of CBS with a concrete operationalization (Definition 1, Sec. 3.1)**: The paper defines CBS as the batch size at which steps exceed the linear-scaling ideal by 20%, enabling systematic power-law fitting. This is a useful operationalization for a concept that was previously used informally.

- **Exponential weight averaging to avoid fixed training durations (Sec. 2.1)**: Using EWA to reach target validation losses without predefining total steps is a practical methodological contribution that enables CBS measurement for flexible training lengths.

- **Careful hyperparameter tuning per batch size**: The paper reports that optimizer hyperparameters ($\beta_2$, EWA decay rate $\tau$) are tailored to each batch size, reducing confounding factors that are often overlooked in scaling studies.

## Weaknesses

### Fatal
None.

### Major

- **No sensitivity analysis on the 20% overhead threshold (Definition 1)**: The paper defines CBS using a 20% overhead relative to linear scaling (line 109) and explicitly notes that "20% can be replaced by any other suitable measure" (line 111), yet never tests whether the fitted scaling exponents ($N^{0.47}$, $N^{0.087}$, $D^{c}$) are robust to choosing 10%, 15%, 25%, or 30% thresholds. The central claim that CBS grows with data size and not model size rests on comparisons of these exponents; if the exponents shift substantially under alternative thresholds, the conclusions could be an artifact of this single choice. This is the most impactful methodological gap because it directly affects the paper's core quantitative claims.

- **Controlled fixed-data experiment uses a target loss from the smaller 151M model, potentially confounding the model-size comparison (Sec. 3.2)**: When isolating model-size effects, the paper uses the 151M model's Chinchilla-optimal loss as the target for all larger models (line 131). Since larger models have greater capacity, this target may be relatively easier for them, potentially compressing the steps-vs-batch-size curve and attenuating any model-size-dependent increase in CBS. The observed near-invariance ($B^* \propto N^{0.087}$) could partly reflect this asymmetric difficulty rather than a genuine invariance. The paper would be strengthened by additional validation using per-model target losses calibrated to be equally demanding relative to each model's capacity.

- **Theorem 1 does not fully establish the claimed CBS invariance with model width (Sec. 4.1)**: Theorem 1 states that for a fixed batch size $B$, fixed training iterations $t$, and fixed learning rate schedule, loss converges as width increases. The paper then asserts (line 169) that this "implies" CBS does not scale with width. However, CBS is defined across batch sizes — it depends on how the steps-to-loss function changes as batch size varies. Pointwise convergence of individual loss curves at fixed $(B,t)$ does not guarantee convergence of the derived CBS without additional uniformity assumptions over batch sizes. The paper acknowledges this gap ("we expect that there exists a finite width $w$ such that the above theorem holds for all batch sizes $B$") but this is stated as an expectation, not proven. This weakens the theoretical justification for one of the paper's two main claims.

### Minor

- **No uncertainty quantification on scaling-law exponents**: The power-law exponents $0.47$ (Chinchilla setting) and $0.087$ (fixed-data setting) are fitted from 3–5 data points without confidence intervals, prediction intervals, or goodness-of-fit statistics. Without uncertainty quantification, the claim that $0.087$ is "weak" (near-zero) while $0.47$ is substantial cannot be evaluated for statistical significance.

- **EWA validation for CBS measurement is incomplete (Sec. 2.1)**: The paper validates that EWA matches cosine scheduling at one batch size (Fig. scheduler_all), but CBS depends on the steps-to-target function across a range of batch sizes. Whether CBS values measured under EWA transfer to standard cosine-decay schedules is not directly shown.

- **The $\alpha=1$ assumption in the step-to-batch-size power-law fit is claimed to be equivalent to a fitted $\alpha$ without supporting evidence**: Line 118 states that both strategies "yield nearly identical forecasting results" but no data is shown. Since the CBS derivation $B^* = b/(5a) + 1.2B_{\text{opt}}$ assumes $\alpha=1$, a deviation from $\alpha=1$ would introduce systematic error.

### Trivial
None.

## Nice-to-Haves
- A limitations paragraph acknowledging that the experiments are limited to models ≤1.2B parameters and that the model-size invariance result may not hold at scales where depth scaling or other factors dominate.
- Clarifying the constant $C_{\text{Chin}}$ used in the Chinchilla step computation (line 84), which is not defined in the main text.

## Removed Points
- **"C_Chin not defined"**: This constant may be defined in the appendix (referenced at line 79). The rule about stripped appendices applies.
- **"Hyperparameter sensitivity not reported"**: The paper references appendix Cref{app:ablation} for hyperparameter tuning details, which is standard practice.
- **"Related work missing"**: Removed per instructions (no external sources to verify).
- **"Data resolution is thin"**: This is a generic criticism that does not identify a specific error; 5 model sizes × multiple data sizes is reasonable for scaling-law work.
- **"The paper should discuss scalability limits"**: Acknowledge as a nice-to-have rather than a weakness.
- **Hard Rules removals**: Formatting nitpicks, reproducibility concerns about hyperparameters, and speculative "could be" concerns removed per filtering discipline.
- **Strength Finder removals**: No strengths were removed — all were concrete and specific to the paper.

## Novel Insights
The harsh critic's observation about the fixed-data controlled experiment — that using the 151M model's Chinchilla target loss for all larger models asymmetrically advantages larger models — is a genuinely insightful methodological critique that goes beyond what a casual reader would notice. This is not a fatal flaw (the conclusion is triangulated through multiple experiments and theory) but it is a real confound that deserves explicit acknowledgement. The critic is right that a per-model target loss calibrated to each model's capacity would make the fixed-data comparison significantly more convincing. An interesting meta-point is that this design choice is natural (it's the simplest way to fix data size across models) yet subtly introduces an asymmetry that works in favor of the paper's claimed conclusion, making it an unintentionally optimistic experimental design.

## Suggestions

1. **Run sensitivity analysis on the 20% threshold**: Repeat the key scaling-law fits for thresholds at 10%, 15%, 25%, and 30%. If the exponents are stable across thresholds, report this as evidence of robustness. If they shift, report the range honestly and bound the conclusions accordingly.

2. **Validate the fixed-data experiment with per-model targets**: For at least one additional configuration, use a target loss that is comparably demanding relative to each model's saturation loss (e.g., a fixed percentage above each model's minimum achievable loss), and verify that the CBS near-invariance still holds.

3. **Add confidence intervals to scaling-law exponents**: Use bootstrap resampling or other methods to report uncertainty on the exponents $0.47$ and $0.087$, quantifying whether they are statistically distinguishable.

4. **Clarify the theoretical claim in Sec. 4.1**: Reframe Theorem 1's implication for CBS as a plausibility argument requiring uniform convergence, rather than a proven corollary. Acknowledge the gap explicitly.

5. **Validate EWA for CBS measurement**: Show that the steps-to-target function under EWA matches cosine decay at multiple batch sizes (not just one), or discuss the potential for systematic bias if it does not.

## Score and Decision

This paper addresses an important and underexplored question with a thoughtful experimental design. The core finding — that CBS scales with data size rather than model size, at least up to 1.2B parameters — is interesting, practically relevant, and reasonably well-supported by converging evidence from controlled experiments and theory. The formalization of CBS is a useful methodological contribution, and the theoretical analysis via least-squares regression provides a principled mechanism.

However, the paper's evidential foundation has significant gaps: the lack of sensitivity analysis on the 20% threshold, a potential confound in the fixed-data controlled comparison, and an overclaimed theoretical theorem. These do not invalidate the core claims but substantially weaken the quantitative precision and rigor of the evidence. The paper would benefit from a major revision addressing these issues. On balance, the contribution is positive and the claims are likely correct, but the current level of rigor is below what is needed for the claims to be fully established.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>