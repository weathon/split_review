Now I have all the information I need. Let me compose the final consolidated review.

## Summary

This paper proposes SONNET, a probabilistic day-ahead net load forecasting method with three main components: (1) a fully unsupervised BTM solar disaggregation algorithm that separates net load into solar generation and load traces using a physical model, (2) a Transformer architecture combining self-attention on historical patches with cross-attention on future weather/solar forecasts, and (3) a physical-model-based data augmentation scheme that simulates weather forecast errors. The evaluation uses the real-world dataset from the DOE net load forecasting competition across four diverse U.S. locations.

## Strengths

- **Unsupervised solar disaggregation achieves near-supervised accuracy.** Table 1 shows that across four solar penetration levels, the unsupervised algorithm yields RMSE, MASE, and CV values nearly identical to the supervised upper bound (e.g., RMSE of 0.02 vs. 0.01 at the highest penetration). This validates that meaningful solar generation can be recovered from net load alone without ground-truth labels.

- **Transformer architecture with cross-attention effectively integrates historical and future exogenous data.** The design — self-attention on patched historical series to encode temporal patterns, then cross-attention using future weather/solar forecasts as queries — is shown in Table 4 to significantly outperform LSTM+MLP, MLP+cross-attention, and XGBoostLSS across all four locations, demonstrating the benefit of the full attention-based architecture.

- **Physical-model-based data augmentation improves robustness to forecast errors.** The ablation in Table 3 shows that without data augmentation, CRPSS drops substantially for the high-solar-penetration site HI (from average levels to noticeably lower), while augmentation restores performance. This is a concrete, domain-specific augmentation that directly addresses a practical failure mode.

- **Comprehensive ablation studies isolate component contributions.** Tables 3–5 separately test removal of disaggregation, data augmentation, exogenous variables, alternative predictor models, and different context lengths. Each ablation degrades performance, supporting the claim that all proposed techniques are necessary. The "no exogenous variables / no disaggregation" condition yields negative CRPSS at several sites, while the full model achieves positive scores everywhere.

- **Validation on diverse climates and solar penetration levels.** The four DOE competition sites (TX, OR, GA, HI) span continental, maritime, humid subtropical, and tropical climates with solar penetration ranging from 0.18× to 1.57× of peak net load, supporting generalizability claims.

## Weaknesses

### Fatal

*None.*

### Major

- **The comparison with competition teams is not a controlled experiment, and the claim of "consistently outperforms" is not fully supported.** The paper compares SONNET's CRPSS (with *simulated* weather forecast errors at three levels: Normal, Challenging, Extreme) against the competition teams' scores (who used *real* weather forecasts with unknown error characteristics). The paper states that "even under the most challenging conditions with extreme forecast errors of weather features, SONNET still consistently outperforms these top teams." While this is an interesting directional claim, the comparison is not apples-to-apples — the competition teams' weather forecasts may have different error structures, biases, and correlations not captured by simple Gaussian noise at 2× empirical σ_f. Moreover, per the reviewer's reading of Table 2 (the table values are in an inaccessible image), SONNET under Extreme errors scores *below* the competition's top-1 for Oregon (0.72 vs. 0.85) and marginally below for Texas (0.66 vs. 0.67), which would directly contradict the "consistently outperforms" claim. The authors should either run a controlled experiment (e.g., apply the same simulated errors to reproduce baseline methods or compare using the same weather inputs) or significantly soften the claim.

- **Non-monotonic CRPSS across error levels raises serious concerns about the experimental methodology.** The paper reports CRPSS for SONNET at Normal, Challenging, and Extreme error levels. The reference model is a 30-day persistence model that does **not** use weather forecasts, so CRPS_ref is constant across all error conditions. Under CRPSS = 1 − CRPS_model/CRPS_ref, larger forecast errors should monotonically degrade (or at best, not improve) CRPSS. Yet the reported averages (per the reviewer, from Table 2) show non-monotonic behavior: e.g., Georgia goes from 0.49 (Normal) to 0.64 (Challenging) to 0.65 (Extreme), and Hawaii goes 0.35 → 0.51 → 0.49. CRPSS *improving* when weather forecasts become noisier is logically impossible under a correct implementation. Possible explanations include: uncontrolled random seeds across conditions, a bug in CRPSS computation, or variance so large that the point estimates are meaningless. The paper provides no error bars, confidence intervals, or standard deviations despite stating these are averages from 20 experiments × 10 replicates = 200 runs. This is the most damaging issue in the review — it undermines the credibility of the entire quantitative evaluation. *The authors must explain this discrepancy and provide proper uncertainty quantification.* Until resolved, the main experimental results cannot be trusted.

### Minor

- **The solar disaggregation is validated only on a small separate dataset, not on the competition test sites.** The disaggregation component is evaluated on a 4-week Austin, TX dataset (322 customers, August 2015 only), not on the four DOE competition sites where ground-truth solar is unavailable. The paper acknowledges this limitation (Section 5.1), and the ablation study (Table 3) provides indirect evidence that disaggregated solar helps forecasting. However, there is no direct validation that the unsupervised disaggregation transfers to climates as different as Hawaii (tropical, high cloud variability) and Oregon (maritime, low irradiance), where the physical model's assumptions (e.g., uniform tilt/azimuth) may break down. A simple robustness check — e.g., correlating estimated solar generation with solar irradiance on clear days for each site — would strengthen confidence.

- **Algorithm 1 (solar disaggregation) is underspecified in key details.** The initial selection of time pairs, the size M, how "neighboring time slot pairs" are defined in step 15, and how the algorithm avoids converging to degenerate solutions (e.g., all selected pairs having nearly identical load, making L^(1) trivially low) are not fully described in the main paper. While the appendix (stripped by the parser) may contain these details, the main text needs sufficient specification for a reader to understand potential failure modes.

- **The CRPSS numbers are reported as point estimates without uncertainty quantification.** Given that the results are averages of 200 runs (20 experiments × 10 replicates), providing standard deviations, confidence intervals, or at minimum a range would be standard practice. This is particularly important given the suspicious non-monotonic trend discussed above. Without error bars, the reader cannot assess whether differences between conditions or between SONNET and baselines are statistically meaningful.

### Trivial

- The paper refers to using equation (1) — the CRPS formula — as the training loss. CRPS can indeed be used as a differentiable loss for quantile forecasts, but the description is slightly ambiguous about whether pinball loss or CRPS is actually optimized. Clarifying this in one sentence would help.

- Key architectural hyperparameters (patch length p, stride s, number of attention heads/layers, learning rate) are not stated in the main paper. If these are in the appendix (which the parser strips), a forward reference would help.

## Nice-to-Haves

- A discussion of limitations and failure modes (e.g., very low solar penetration where disaggregation adds little value; regions with extreme cloud variability where the physical model's parameter estimates become noisy; scenarios where the "neighboring time pairs have similar loads" assumption breaks down).
- A brief note on computational cost (training time and inference speed) relative to simpler baselines, which would help practitioners assess deployability.
- Additional direct validation of the disaggregation output on the competition sites (e.g., correlation with irradiance on clear days), even without ground-truth solar data.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"CRPS is a metric; the training loss should be the pinball loss averaged over quantiles."* — This is factually incorrect. CRPS has a closed-form differentiable expression for quantile-based forecasts and is routinely used as a training loss in probabilistic forecasting. The paper does not specify precisely *how* CRPS is minimized (e.g., via its closed form for step-function CDFs), but the criticism that CRPS "cannot" be used as a loss is wrong. **Removed: factually wrong.**

- *"Missing related works"* — The instruction forbids mentioning missing related works as I cannot verify which works exist outside this paper. **Removed per instructions.**

- *"Pure formatting/style nitpicks"* — Removed per instructions (parser artifacts, not author errors).

- *"Missing appendix content / missing proofs in appendix"* — Removed per instructions. The appendix is stripped by the parser; it exists in the original submission.

- *Criticism about "not yet released" or "cannot be independently verified" regarding the DOE competition results or any cited dataset* — Removed per instructions. All cited entities are assumed to exist and be released.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a pattern or deep insight about the literature that the paper itself does not already articulate.

## Suggestions

1. **Run a controlled comparison:** Apply the same simulated weather forecast errors to the competition teams' methods (or a reasonable reimplementation) rather than comparing SONNET's simulated-error scores against the competition's real-weather scores. This would resolve the unfair-comparison concern.

2. **Explain the non-monotonic CRPSS:** This is the single most damaging issue. Provide per-condition distributions (violin plots or box plots) of the 200-run CRPSS values to show whether the trend is a statistical artifact, and explain why CRPSS increases when forecast errors grow larger. If there is a bug, fix it and re-report. If the trend is real, provide a rigorous explanation — otherwise, the results are not credible.

3. **Add uncertainty quantification:** Report standard deviations, confidence intervals, or interquartile ranges for all reported CRPSS scores, especially given the use of random error sampling.

4. **Add direct validation of disaggregation on competition sites:** Even without ground-truth solar, show that estimated solar generation correlates with measured irradiance on clear-sky days, or that estimated load has smoother profiles consistent with known load patterns.

5. **Provide architectural hyperparameters in the main paper** (or clearly reference the appendix section where they appear) to ensure reproducibility.

## Score and Decision

The paper's core ideas — unsupervised disaggregation of net load, a Transformer with cross-attention on future exogenous data, and physics-based data augmentation — are well-motivated and the methodological design is sound. The ablation studies convincingly show that each component contributes. 

However, the experimental evaluation has two structural problems that prevent acceptance in the current form. First, the claim of "consistently outperforming the state-of-the-art" rests on an uncontrolled comparison against competition teams who used unknown real weather forecasts, and per the table values it appears factually incorrect for at least one site. Second and more damaging, the non-monotonic CRPSS trend — where forecast quality *improves* under larger weather forecast errors — is logically impossible under a correct implementation of CRPSS against a constant reference model, and the paper offers no explanation. Without resolving this discrepancy, the main quantitative results cannot be treated as reliable evidence.

The contribution is promising, but the evaluation needs a major rework before the paper can be accepted.

MY FINAL SCORE: <pineapple>4.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>