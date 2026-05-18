Now I have all the information needed. Let me write the consolidated review.

---

## Summary

This paper presents the first systematic manifold-learning analysis of transformer-based time series forecasting (TSF) models. Using intrinsic dimension (ID) and mean absolute principal curvature (MAPC) estimators, it characterizes the geometric properties of latent representations in Autoformer and FEDformer across 7 datasets and 4 forecast horizons. The main findings are: (1) ID and MAPC profiles exhibit a consistent two-phase pattern — relatively flat in the encoder, rising in the decoder; (2) final-layer MAPC is correlated with test MSE (lower curvature → lower error), an opposite trend to classification CNNs; and (3) untrained models' geometric profiles converge rapidly (within ~5 epochs) during training.

## Strengths

- **First systematic manifold analysis of TSF transformers.** The paper breaks new ground by applying ID and MAPC estimation to transformer-based forecasting models. This is explicitly identified as a gap: "to the best of our knowledge, there is no systematic work that analyzes transformer-based TSF deep neural networks from a manifold learning perspective" (Section 1). The study covers 7 datasets, 4 horizons, and 10 seeds per configuration.

- **Discovery of qualitatively different geometric profiles for regression TSF models vs. classification CNNs.** The paper demonstrates that TSF transformers show ID that is relatively fixed or increasing through the encoder and rises further in the decoder — contrasting sharply with the "hunchback" ID profile of CNNs (Section 4.1). Furthermore, the MAPC–error relationship is opposite: better TSF performance is associated with *lower* MAPC, whereas CNNs benefit from a large MAPC gap (Section 4.2). These task-specific differences are a genuine, non-obvious contribution.

- **Training dynamics analysis reveals rapid geometric convergence.** Figure 6 shows that untrained models have random ID/MAPC profiles that converge to their final shape within ~5 epochs, with the decoder converging more slowly than the encoder. This temporal characterization of manifold evolution is novel for the TSF setting (Section 4.3).

- **Principal curvature distribution analysis reinforces the two-phase pattern.** Figure 7 shows that encoder layers (1–4) share a narrow curvature range while decoder layers (5–7) exhibit a wider, distinct range, providing fine-grained evidence for the geometric two-phase behavior (Section 4.4).

## Weaknesses

### Fatal
None.

### Major

- **The MAPC–MSE correlation claim is severely underpowered.** Each correlation coefficient in Table 1 is computed from *only four data points* (one per forecast horizon: 96, 192, 336, 720) per dataset. With n=4, a Pearson r must exceed ~0.95 to reach significance at α=0.05 (df=2). Most reported coefficients (0.46–0.97) would not be statistically significant individually, and no p-values or confidence intervals are reported. There is also a known confound: longer horizons increase MSE and may increase MAPC for independent reasons. The paper's headline claim that MAPC allows comparing models "without access to the test set" (abstract, Section 5) is not supported by the evidence presented. This weakness cuts across Section 4.2, the abstract, and the conclusion. While the *consistency* of the positive direction across 6 datasets is suggestive, the individual correlations lack statistical foundation.

- **The i.i.d. assumption of TwoNN and CAML estimators is not validated for time-series data.** Both the intrinsic dimension estimator (TwoNN) and the curvature estimator (CAML) assume independent samples from a manifold. However, the "500k point samples from 𝒟" are latent representations of successive or overlapping time windows, which exhibit strong temporal autocorrelation. Temporal dependencies can artificially depress effective sample size and bias nearest-neighbor ratios used by TwoNN, potentially compromising all reported ID and MAPC values. The paper does not discuss this issue, test for it (e.g., by comparing shuffled vs. unshuffled representations), or cite prior work validating these tools for temporally correlated data (Section 3, Section 4). This is a methodological gap that casts uncertainty on the quantitative results.

- **No variability shown despite 10 seeds.** The paper states that each configuration uses 10 random seeds (Section 3), yet all figures (Figures 2–7) show only single curves per model/dataset/horizon combination with no error bars, shaded intervals, or indication of seed-to-seed variability. Without uncertainty quantification, the reader cannot assess whether the claimed differences between Autoformer and FEDformer, or between datasets, are robust or within estimation noise. This is especially critical for the correlation analysis in Table 1 and Figure 4, where confidence intervals around the coefficients are standard practice.

### Minor

- **Limited model scope.** Only two architectures (Autoformer, FEDformer) from 2021–2022 are analyzed. While the paper notes these are "still considered SOTA" (citing a 2024 reference), the findings may be architecture-specific rather than general properties of transformer-based TSF. The paper's framing ("deep transformer models") implies more breadth than two specific architectures support.

- **Training dynamics shown for only one dataset (traffic).** The conclusion that "untrained models converge within five epochs" is based on a single dataset. At least one additional dataset (e.g., electricity or weather) should be shown to establish generality (Section 4.3, Figure 6).

### Trivial
None.

## Nice-to-Haves

- The correlation analysis could be strengthened substantially by using all 10 seeds (10 × 4 = 40 points per dataset) and fitting a mixed-effects model that accounts for seed variance, or by treating horizon as a continuous variable and checking whether MAPC adds predictive power beyond horizon alone.
- Validating the TwoNN/CAML estimates on time-series data by comparing ID/MAPC on original vs. temporally shuffled representations would directly address the i.i.d. concern.
- Reporting the ID–MSE correlation would complete the geometric analysis, since the abstract refers to "geometric features" (plural) being correlated with performance, but only MAPC is checked.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"The two-phase narrative may be an artifact of architectural structure"** — This criticism misunderstands the paper's claim. The paper is descriptively characterizing what happens in encoder vs. decoder layers; the fact that the two-phase behavior aligns with the architectural split *is* the finding. The paper does not claim this is a mysterious or non-obvious phenomenon — it is a quantitative characterization of the geometric properties of each architectural component.
2. **"The ID estimates are very low"** — The paper explicitly addresses this: the low ID is consistent with the manifold hypothesis and prior work (line 88). The values (1.2–8.1 for D=512) are in line with existing CNN analyses.
3. **"No analysis of the intrinsic dimension–performance correlation"** — The paper's correlation analysis focuses on MAPC; not checking every possible geometric feature is not a weakness when the chosen feature (MAPC) already shows a pattern.
4. **"No analysis of the attention mechanism itself"** — The paper explains (line 54) that the Fourier Cross-correlation layer of FEDformer outputs near-identical values yielding zero curvature, making attention blocks unsuitable for this analysis. This is a practical limitation honestly stated, not an oversight.
5. **Generic strength** from Strength Finder about "First systematic manifold-learning analysis" — this is kept (it is well-supported by a specific citation). The training dynamics and curvature distribution strengths are also kept as they are specific and supported.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the underpowered correlation analysis and the unmet i.i.d. assumption but do not produce a genuinely novel insight about the paper's subject matter.

## Suggestions

1. **Re-do the correlation analysis with proper statistical support.** Aggregate over all 10 seeds (providing 40 points per dataset) and report confidence intervals and p-values for each correlation. Alternatively, treat horizon as a control variable in a partial correlation analysis to address the confound.
2. **Add a validation experiment for the i.i.d. assumption.** Compute ID and MAPC on temporally shuffled representations and compare to the reported values. If the estimates are unchanged, the concern is alleviated; if they change, quantify the bias.
3. **Add error bars or shaded intervals to all main figures** using the 10 seeds, and report the variance of ID/MAPC estimates (e.g., bootstrapped confidence intervals).
4. **Expand to at least one additional architecture** (e.g., PatchTST) to demonstrate that the two-phase geometric pattern is not specific to Autoformer/FEDformer alone.

## Score and Decision

The paper makes a genuine contribution by being the first to systematically characterize manifold geometry in TSF transformers, revealing interesting two-phase patterns and task-specific differences from classification CNNs. The descriptive findings (ID/MAPC profiles, training dynamics) are solid and novel. However, the headline correlation claim is underpowered (n=4) and the i.i.d. assumption for manifold estimators on temporally dependent data is unaddressed. The absence of any uncertainty quantification despite 10 seeds further weakens the empirical contribution. These gaps are significant but addressable — they do not invalidate the descriptive geometric analysis, which remains the paper's strongest contribution. With proper statistical validation and broader scope, the paper would be substantially stronger.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>