Now I have all the evidence I need. Let me construct the final consolidated review.

---

## Summary

This paper studies scaling laws for LLM finetuning across three methods (FMT, prompt tuning, LoRA), two language pairs, and three generation tasks (two translation, one summarization). It proposes a multiplicative joint scaling law $\hat{\mathcal{L}}(X, D_f) = A \cdot X^{-\alpha} \cdot D_f^{-\beta} + E$ linking finetuning data size with LLM model size, pretraining data size, and PET parameter size. Key empirical findings are that (a) LLM model size benefits finetuning more than pretraining data size, (b) scaling PET parameters is generally ineffective, and (c) the optimal finetuning method is highly task- and data-dependent. The experimental scope is substantial, involving 1B-to-16B models and up to 25M finetuning examples.

## Strengths

- **Proposes and validates a multiplicative joint scaling law for LLM finetuning.** The paper extends prior scaling laws from pretraining only (Kaplan et al., Hoffmann et al.) to the joint effect of multiple factors in finetuning. The multiplicative formulation consistently outperforms an additive baseline across all three scaling factors on held-out data (Table 1: e.g., 0.0048 vs 0.0079 for LLM model size; 0.004 vs 0.005 for PET parameter size).

- **Systematic and well-controlled experimental design.** The study covers three finetuning methods, two language pairs (En-De, En-Zh), three tasks, and four scaling factors with multiple data points per factor. Three random subsets per configuration are averaged to reduce noise, and held-out verification points are used to test generalization.

- **Empirical evidence that PET parameter scaling is ineffective.** Across settings, the scaling exponent $\alpha_t$ for both prompt length and LoRA rank is $|\alpha_t| \ll 10^{-2}$, often negative — indicating negligible or inverse returns from increasing PET capacity. LoRA shows better training stability than prompt tuning, but neither benefits meaningfully from more parameters.

- **Quantifies differential data-hungriness across finetuning methods.** The $\beta$ exponent for FMT consistently exceeds that for PET (e.g., $\beta_{\text{FMT}} \approx 0.20$ vs $\beta_{\text{prompt}} \approx 0.08$ on WMT En-De), confirming that FMT benefits more from additional finetuning data while PET saturates earlier.

- **Demonstrates PET preserves zero-shot generalization better than FMT.** On zero-shot translation tasks, prompt tuning and LoRA achieve higher BLEURT scores than FMT, especially with larger LLMs — a practically useful insight when generalization to related tasks is a priority.

## Weaknesses

### Fatal
None.

### Major

- **Pretraining data scaling is measured via intermediate checkpoints, confounding data quantity with training convergence.** The paper uses early pretraining checkpoints as a proxy for "smaller pretraining data" (line 88: "adopt intermediate pretrained checkpoints as the proxy due to computational budget constraint while acknowledge its sub-optimality"). An early checkpoint has seen fewer tokens but is also undertrained relative to the full budget. This conflates data quantity with training convergence. The concern is that this systematically underestimates the true benefit of more pretraining data, because early checkpoints underperform what a model trained from scratch on that same data budget would achieve. The central claim that $\alpha_m > \alpha_p$ (model size matters more than pretraining data size) rests on this comparison, and the paper does not discuss the direction or magnitude of the bias. While the paper acknowledges sub-optimality in a single sentence, it does not analyze how this might affect the relative scaling exponents. The claim may still hold, but the current evidence is less reliable than it would be with properly trained data budgets.

### Minor

- **The PET finetuning data range (up to 100K) is substantially smaller than the FMT range (up to millions), making the "generally ineffective" claim broader than the evidence fully supports.** The paper explicitly scopes itself to the "data-limited regime" (line 17), and the 100K ceiling is reasonable for typical PET deployment. However, the claim that PET parameter scaling is "ineffective" is stated without this scope qualifier (e.g., abstract says "PET parameter scaling is generally ineffective"). It is plausible that at larger finetuning data sizes (500K–1M), the capacity bottleneck from LoRA rank or prompt length becomes more relevant. Adding this scope caveat would strengthen the claim.

- **Extrapolation to the largest held-out model (16B) shows notable failures for some settings.** The paper acknowledges "high mismatch when extrapolating to 16B, particularly for LoRA and prompt on WMT19 En-Zh" (line 171) and attributes it to insufficient empirical data over model sizes. This is a reasonable explanation, but the 16B point is the most practically relevant extrapolation target. The fact that the law fails in some regimes limits its usefulness as a predictive tool. The abstract's statement that the law "generalizes to different settings" is somewhat at odds with this admitted failure.

- **No uncertainty quantification on the fitted scaling law parameters.** The paper reports mean absolute deviation on held-out data but does not provide confidence intervals, standard errors, or bootstrap estimates for $\alpha$, $\beta$, or $E$. Given the small number of data points per dimension (e.g., 5 model sizes), the fitted exponents could be sensitive to individual data points. The paper does perform three random runs per configuration, which mitigates noise, but the stability of the scaling exponents themselves is not assessed.

- **Mild overclaim in the abstract relative to the empirical evidence.** The abstract claims the joint law "generalizes to different settings," but the body documents extrapolation failures at the largest model size on one language pair. A more precise framing — e.g., "generalizes across most settings we tested, with noted exceptions at the largest model sizes" — would better match the evidence.

### Trivial
None beyond what is already captured above.

## Nice-to-Haves

- **Hyperparameter sensitivity analysis for PET.** The paper notes training instability for prompt tuning but does not explore whether careful tuning of learning rates or initialization methods (known to matter for prompt tuning, per Lester et al.) could change the scaling behavior.
- **Ablation of the joint fitting procedure.** The authors fix $\beta$ and $E$ across factors and then refit per factor. Evaluating this choice (e.g., by fitting each factor independently and comparing) would strengthen confidence in the procedure.
- **A controlled comparison on a smaller model** to calibrate the pretraining data proxy (e.g., train a 1B model from scratch on multiple data budgets) would help validate whether the $\alpha_m > \alpha_p$ finding holds under proper scaling experiments.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"The multiplicative vs additive improvement is marginal."** The reviewer claimed held-out errors are "extremely close." In fact, the multiplicative formulation is consistently better across all three factors (e.g., 0.0048 vs 0.0079 for model size is a ~40% error reduction). The improvement is modest for pretraining data (0.0068 vs 0.0069), but the overall pattern supports the paper's conclusion. [Removed because the claim is overstated relative to the table.]

- **"The paper does not discuss how the proxy biases the comparison."** Partially removed — the paper does acknowledge sub-optimality (line 88), but indeed does not analyze the direction or magnitude of bias. This is kept in the Major section but softened from the reviewer's framing.

- **Criticism that the findings "may be an artifact of the experimental design."** This is too strong — the proxy issue reduces confidence but does not necessarily invalidate the finding, especially since the pattern ($\alpha_m > \alpha_p$) is consistent across multiple tasks and methods. Kept as Major with reduced severity.

## Novel Insights

None beyond the paper's own contributions — the reviews surface methodological caveats (pretraining proxy, PET data range) and presentation overclaims, but do not identify conceptual novelties the paper itself overlooks.

## Suggestions

1. **Address the pretraining data proxy.** Either (a) conduct a controlled validation experiment on a smaller model trained from scratch at multiple data budgets, or (b) at minimum, add a thorough discussion of the expected direction and approximate magnitude of bias, and temper the $\alpha_m > \alpha_p$ claim accordingly (e.g., "under our measurement methodology, the data suggest...").

2. **Qualify the PET parameter ineffectiveness claim by scope.** Change "generally ineffective" (abstract) to "ineffective in the data-limited regime studied here" to avoid overgeneralization beyond the 100K ceiling tested.

3. **Add uncertainty estimates.** Report bootstrap confidence intervals or standard errors for the fitted scaling exponents, especially given the limited number of data points per dimension.

4. **Tone down the generalization claim.** The abstract should acknowledge the extrapolation failures at 16B for some settings, to be consistent with the body.

## Score and Decision

This paper tackles an important and under-explored question — the scaling properties of LLM finetuning — and provides the most extensive empirical study I am aware of on this topic. The proposed multiplicative joint scaling law is a plausible framework, and the findings about PET parameter ineffectiveness, method-specific data-hungriness, and zero-shot generalization are all useful contributions. The experimental scope (three methods, three tasks, two language pairs, model sizes 1B–16B) is a significant strength.

The paper's most serious weakness is that the central comparative claim ($\alpha_m > \alpha_p$) rests on a measurement of pretraining data size that confounds data quantity with training convergence. This does not invalidate the paper — the joint scaling law, PET analysis, and many other findings are independent — but it does reduce confidence in one of the headline results. The other weaknesses (PET data range ceiling, extrapolation failures, no uncertainty quantification) are addressable and do not threaten the core contributions.

The paper is a solid empirical contribution that would benefit from caveating the affected claims and ideally providing a small-scale validation of the proxy method. As-is, the work has real value for the community but the strongest claim needs more careful evidentiary support.

**Score:** 6.5

**Decision:** Borderline / Weak Accept — the contribution is real but the pretraining data proxy issue weakens confidence in one of the three main findings. With revisions addressing this caveat, the paper would be clearly acceptable.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>