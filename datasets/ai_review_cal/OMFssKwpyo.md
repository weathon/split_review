- Decision: Reject
- Avg Score: 3.80
- Scores: 3, 3, 5, 3, 5
Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

---

## Summary

This paper proposes SONNET, a probabilistic day-ahead net load forecasting method that (a) unsupervisely disaggregates net load into solar generation and load components using a physical model and load-similarity pairs, (b) feeds both disaggregated traces into a Transformer that uses self-attention on historical data and cross-attention with future weather forecasts, and (c) applies physics-based data augmentation to improve robustness to weather forecast errors. The method is evaluated on the DOE net load forecasting competition dataset across four U.S. locations with varying solar penetration.

## Strengths

1. **Unsupervised disaggregation achieves near-supervised accuracy (Table 1).** The proposed algorithm recovers solar generation from net load alone, with RMSE, MASE, and CV values very close to a supervised learner across four simulated solar penetration levels (0.18–1.57). This validates a key practical enabler: utilities have only net load data, and the disaggregation makes solar information available without ground-truth labels.

2. **Comprehensive ablation isolating each component's contribution (Tables 3–5).** Removing disaggregation, data augmentation, exogenous variables, or the Transformer architecture consistently degrades CRPSS across all locations. For example, removing data augmentation drops HI CRPSS from 0.31 to −0.05. The ablation on context length (Table 5) shows 14 days is optimal. This internal consistency is the paper's strongest evidence that each proposed component contributes meaningfully.

3. **Consistent outperformance of alternative predictors (Table 4).** SONNET (Transformer with cross-attention) beats LSTM+MLP, MLP+cross-attention, and XGBoostLSS across all four locations. This demonstrates the architecture's advantage over reasonable baselines and does not depend on the competition comparison.

4. **Evaluation across four climatically and operationally distinct locations.** TX (south central), OR (northwest), GA (southeast), and HI (Pacific island) span very different weather patterns and solar penetration levels (0.18–1.57 normalized capacity). Consistent results across these sites support generalizability. The HI case with poor forecast accuracy and near-unity solar penetration is a particularly challenging test.

5. **Physically motivated data augmentation.** Rather than adding generic noise, the augmentation recomputes solar generation through the physical model after perturbing irradiance and other weather features. This is principled, domain-specific, and the ablation (Table 3) shows it substantially improves robustness.

## Weaknesses

### Fatal
None.

### Major

1. **The comparison with competition teams is on a different playing field.** SONNET is evaluated with weather forecast errors simulated as i.i.d. Gaussian noise (parameterized by empirical σ_f), whereas the competition teams used actual weather forecasts with real error structure. The paper's headline claim — "significantly outperforms the state-of-the-art" (Table 2) — compares CRPSS values computed under these different conditions. While using empirical σ_f is a reasonable approximation, real forecast errors have temporal autocorrelation and non-Gaussian structure that the simulation does not capture. The paper does not acknowledge this limitation or provide a direct comparison on a common, realistic test set. The claim of SOTA outperformance is therefore overstated in its current form.

### Minor

2. **No uncertainty quantification on CRPSS values.** Table 2 reports averages over 20 experiments but omits standard deviations or confidence intervals. The reader cannot assess whether the reported advantages over competition baselines (which are themselves point estimates) are statistically meaningful. The ablation tables (3–5) similarly lack error bars. This is a common omission in the forecasting literature but matters here because the comparison involves multiple random draws.

3. **Disaggregation validated on only one four-week dataset (Austin, TX).** Section 5.1 explains that the DOE competition dataset lacks ground-truth solar generation, so a separate 4-week Austin dataset is used. While understandable, this means the disaggregation claim ("performance close to supervised learning") rests on a single location, season (summer), and time window. Generalization to other climates or seasons is untested.

4. **Disaggregation hyperparameters (γ, η, M) are not disclosed.** Algorithm 1 depends on weights γ and η that balance the loss terms and on M (number of time pairs). The paper does not specify their values or test sensitivity to them. This modestly impedes reproducibility.

5. **The "without exogenous variables" ablation conflates two changes.** Table 3's row removes both exogenous variables (weather) and solar disaggregation simultaneously, making it impossible to attribute the degradation to one factor versus the other. A cleaner ablation would keep disaggregation while removing weather inputs.

6. **No ablation of the future-weather input.** The cross-attention module uses both historical weather and future weather forecasts. An ablation comparing "perfect future weather vs. noisy forecasts vs. no future weather" would clarify how much the architecture leverages this information.

7. **No comparison with simpler data augmentation (e.g., additive noise directly on net load).** The paper attributes the robustness gain to physics-based recomputation of solar generation, but does not test whether simply adding Gaussian noise to the net load input (without the physics step) would achieve a similar effect.

### Trivial
- The notation for the physical model parameters (β and γ used for both panel angles and the loss weights) is slightly confusing but not a real barrier.

## Nice-to-Haves
- Evaluate disaggregation sensitivity to the accuracy of the monthly solar capacity estimate C (the paper states utilities have "rough estimates" but does not test robustness to errors in C).
- Report directional statistics (e.g., how often SONNET beats each baseline in head-to-head comparisons across the 20 runs).
- Consider evaluating on a held-out real-data block with actual operational weather forecasts, even if only for a subset of locations, to complement the simulation-based evaluation.

## Removed Points

These points are flagged for removal; treat them with caution:

- **"Unfair comparison is fatal and invalidates the whole paper" (Harsh Critic).** Downgraded from Fatal to Major. The comparison issue is significant but does not invalidate the paper's contributions because: (a) the empirical σ_f used in the "Normal" condition is derived from real data, (b) the ablation studies and baseline comparisons (Tables 3–5) are internally valid and do not depend on the competition comparison, and (c) the method's components are validated independently. The paper's core thesis — that disaggregation + Transformer + data augmentation produces better net load forecasts — is supported by evidence that survives removing the competition comparison.

- **"LSTM variant uses a different architecture making it hard to isolate the effect of attention" (Harsh Critic).** This is the entire purpose of comparing architectures: to test whether the full Transformer outperforms alternative sequence models. The comparison is valid as an architecture-level ablation.

- **"Limited discussion of generalization; only four U.S. locations" (Harsh Critic).** Four climatically diverse locations spanning different solar penetration levels (0.18–1.57) is adequate for a paper in this domain, especially given the practical constraint of available data.

- **"The 'close' performance claim in Table 1 lacks percentage differences" (Harsh Critic).** The table reports RMSE, MASE, and CV for both unsupervised and supervised methods, and the paper states the performance is "very close." The reader can see the raw values; percentages would be a minor presentation improvement.

- **Strengths removed from Strength Finder:** Generic strengths about the problem being "important" or "timely" were removed as they add no discriminative value. All specific, evidence-anchored strengths were retained.

## Novel Insights

None beyond the paper's own contributions. The reviews did not generate an analysis that the paper itself does not already provide.

## Suggestions

1. **Address the competition comparison directly.** The paper should either (a) qualify the SOTA claim explicitly (e.g., "under simulated forecast errors matching the empirical variability"), (b) re-evaluate on a held-out period with real operational forecasts, or (c) at minimum calibrate the Gaussian simulation to match temporal autocorrelation properties of real forecast errors. Without this, the strongest claim in the paper remains unsupported.

2. **Add standard deviations or confidence intervals to all main result tables** (Tables 2–5). This is quick to compute from the 20 experimental replicates and would significantly strengthen the evidence.

3. **Disclose hyperparameters γ, η, M** for the disaggregation algorithm and ideally provide a sensitivity analysis.

4. **Run a cleaner ablation for exogenous variables** that keeps disaggregated solar in the input while removing weather variables, to separate the two confounded factors in Table 3.

5. **Add a simple augmentation baseline** (e.g., additive Gaussian noise directly on net load) to Table 3's ablation to confirm that the physics-based recomputation is the source of the robustness gain.
