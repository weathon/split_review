Having thoroughly verified the paper against all reviewer claims, I now produce the consolidated review.

---

## Summary

This paper investigates the pre-training dynamics of in-context learning (ICL) by disentangling it into two abilities — task recognition (TR) and task learning (TL). The authors propose competition metrics to quantify how TR and TL interact during pre-training, finding that (1) competition between TR and TL is widespread across 8 LLMs, (2) average competition intensity shows a negative correlation with final ICL performance, (3) pre-training factors (model size, dataset size, data curriculum) affect competition patterns, and (4) an adaptive ensemble that fuses checkpoints good at TR and TL can boost ICL performance, enabling two small models to outperform a single larger one.

## Strengths

- **First pre-training dynamics study of TR/TL competition**: The paper provides the first empirical analysis of how TR and TL interact during pre-training, not just at inference time. Using metrics (\(C_i^h\), \(C_i^s\)) on 8 LLMs with diverse training settings, it demonstrates that competition between these two abilities is widespread (Section 3.2, Figure 2). This opens a new direction for understanding ICL emergence.

- **Novel competition measurement framework**: The proposed metrics (ΔTR, ΔTL, \(C_i^h\), \(C_i^s\), \(R_i\)) offer a principled way to quantify when and how intensely one ability suppresses the other. The core idea of tracking opposite-signed changes with a noise floor (\(\epsilon=0.01\)) is intuitive and interpretable.

- **Practical mitigation via adaptive ensemble**: The method of selecting best TR/TL checkpoints and fusing them with performance-adaptive weights is well-motivated by the observation that the best TR and TL checkpoints are often not the final model. The results (Table 1) show consistent improvements across model combinations, and the ablation study (Table 2) confirms both adaptive weighting and best-checkpoint selection matter. Two smaller models (3B total) outperforming a single ≥6.9B model is a practically meaningful result.

- **Well-controlled model size analysis (Pythia suite)**: The model size analysis uses the Pythia suite, which the paper explicitly states "share the same training setting in addition to the number of parameters" (line 366). This provides clean evidence that larger models shift competition earlier and reduce average intensity. The observation of a possible power-law trend is intriguing, even if not rigorously fitted.

## Weaknesses

### Fatal
None. The core contributions — identifying competition, showing it correlates (suggestively) with ICL performance, and proposing an ensemble that works — are supported by some evidence, even if imperfectly.

### Major

- **Central correlation claim is not statistically established.** The paper reports a Pearson correlation of \(r = -0.591\) between average competition intensity and final ICL performance across 8 LLMs (Section 3.2, Figure 4). With \(N=8\), this correlation is not significant at conventional thresholds (\(p \approx 0.12\) for a two-tailed test; the critical value at \(\alpha=0.05\) is approximately \(|r| > 0.707\)). No p-value, confidence interval, or bootstrap estimate is reported, yet the paper repeatedly calls this a "strong negative correlation" and uses it to motivate the entire ensemble method (lines 9, 56, 74, 329, 338, 561). The claim of a "strong" or "validated" correlation is not supported by the evidence. This is the paper's central quantitative finding, and it rests on a non-significant result.

- **Confounded comparisons in dataset size and data curriculum analyses (Sections 3.3.2–3.3.3).** The dataset size analysis compares Pythia-2.8B vs. MiniCPM-2B and Pythia-6.9B vs. Amber-7B vs. OLMo-7B — models that differ in architecture, tokenizer, data composition, optimizer settings, and training recipes. The data curriculum analysis similarly compares MiniCPM-2B vs. Pythia-2.8B and CrystalCoder-7B vs. Amber-7B, also with multiple confounds. The paper attributes differences in competition dynamics to dataset size or curriculum alone, but these attributions are unsupported without controlling for the other confounds. The paper attempts no such controls and acknowledges only that models have "similar model size and dataset size." This substantially weakens three of the paper's main findings (quality curriculum postpones competition, domain curriculum reduces competition, specialization through data duplication).

### Minor

- **No sensitivity analysis for the competition metric's threshold.** The metric uses \(\epsilon = 0.01\) as a noise floor (line 163), but the paper never tests whether the main results are robust to reasonable variations (e.g., 0.005, 0.02, 0.05). Given that many conclusions rest on fine-grained competition measurements, the threshold's influence is unknown.

- **Pythia-1B is an unexplained outlier in the model size analysis.** Figure 5b (line 374) shows Pythia-1B substantially deviates from the trend, but the paper merely notes "with the exception of Pythia-1B" without discussing why. This undermines confidence in the claimed power-law pattern.

- **Power-law claim is made without any statistical fit.** The paper states that competition intensity "scales as a power-law with model size" (line 378) but provides no curve fitting, goodness-of-fit metric, or quantitative evidence beyond visual inspection. This overstates what is at best a suggestive visual trend.

- **Ensemble evaluation could be strengthened with separated validation sets.** The paper selects checkpoints with the best TR/TL performance on the same 16 datasets used for final gold-ICL evaluation (Section 4.2, line 501). While the selection criterion (random/abstract accuracy) differs from the evaluation metric (gold ICL accuracy), the use of the same datasets for both selection and evaluation introduces a risk of indirect overfitting. A separate held-out set or cross-validation would make the results more rigorous. (Note: the reviewer's characterization as clear "test-set leakage" is overstated — the selection criterion is different from the evaluation metric — but the concern is real.)

- **The "stable–rise" pattern observation relies on the retrospective \(R_i\) metric.** The cumulative intensity \(R_i = \sum_{j=1}^i C_j^s / \sum_{j=1}^N C_j^s\) (Eq. 5) requires knowledge of future competition values to compute the denominator, making its interpretation descriptive rather than predictive. The paper presents this as a dynamic insight about competition evolution, but the pattern is a property of a retrospective normalization.

### Trivial

- The metric \(C_i^s\) can produce large values when both ΔTR and ΔTL are small (just above \(\epsilon\)) but opposite-signed — e.g., ΔTR = -0.011, ΔTL = 0.011 gives a ratio of 1.0. This is not a fatal flaw (the paper uses this to measure relative intensity), but it means small changes can be amplified.
- 16 checkpoints per model is a sparse sampling for tracking fine-grained dynamics (line 230), making the competition metrics sensitive to the chosen intervals.

## Nice-to-Haves

- **Separate validation set for ensemble checkpoint selection.** Using held-out data would place the ensemble results on firmer ground.
- **Statistical rigor for the correlation.** Bootstrapped confidence intervals or a Bayes factor for the N=8 correlation would honestly characterize the uncertainty rather than overclaiming.
- **Controlled follow-up for curriculum analysis.** Training the same architecture (e.g., Pythia-2.8B) on different curricula while holding everything else fixed would directly test the curriculum claims.
- **Sensitivity analysis** for the \(\epsilon\) threshold across Figures 2–6.

## Removed Points

- **"Data curriculum analysis fundamentally invalidates all conclusions about quality curriculum, domain curriculum, and specialization"** — Retained as a major weakness (confounded comparisons) but softened: the analysis supports suggestive observations, not causal conclusions. The reviewer's language ("fundamentally invalidates") overstates the case; the paper's claims about curriculum are presented as observations and possible reasons, not rigorous causal attributions. However, the confounds are real and the conclusions are weaker than stated.
- **"R_i early values depend on future observations, making the stable–rise interpretation circular"** — Retained as a minor weakness but the circularity charge is overstated. This is a standard way to analyze cumulative trajectories retrospectively (any normalized cumulative metric has this property). The observation is descriptive, not predictive.
- **"C^i both changes could be small, producing a large ratio from noise"** — Retained as a trivial concern. The ratio is actually well-behaved: small-decrease/small-increase ≈ 1, which is a moderate value, not an inflated one. The \(\epsilon\) threshold already filters out noise-driven tiny changes.
- **"The paper does not discuss prior work on model averaging for ICL or checkpoint selection"** — Removed per hard rule: DO NOT mention missing related works.
- **Strength Finder's claim that the negative correlation is "statistically significant"** — Removed. The paper does not report statistical significance, and with N=8 it is unlikely to be significant. This embellishment is dropped.
- **Strength Finder's claim of "Systematic isolation of pre-training factors' effects"** — Qualified. Only the model size analysis (Pythia suite) is well-controlled; the dataset size and curriculum analyses are confounded. The strength as stated is misleading.
- **"Power-law behavior of competition with model size" from Strength Finder** — Moved to Removed. The paper offers no curve fitting, so "power-law" is a visual speculation, not an established result. This is an overclaim by the Strength Finder.

## Novel Insights

Beyond the paper's own contributions, one genuinely novel observation emerges from the cross-review synthesis: the paper's central tension — that its main quantitative finding (negative correlation between competition and ICL) is too underpowered to bear the weight placed on it, while its most practically compelling result (the adaptive ensemble works) is largely independent of that correlation — suggests the paper could be restructured to decouple these contributions. The ensemble method is motivated by the observation that best TR/TL checkpoints differ from the final model (which is visually clear from Figure 1 regardless of the correlation) and by the plausible intuition that fusing complementary abilities is beneficial. The negative correlation, while intuitively appealing as a unifying claim, is the paper's weakest link statistically. A stronger paper would foreground the empirical finding that competition exists and the ensemble method works, while honestly reporting the correlation as suggestive (r = -0.59, N=8, p ≈ 0.12) rather than validated.

## Suggestions

1. **Report honest statistics for the correlation.** Provide the p-value, a 95% bootstrap confidence interval, or a Bayes factor. Reframe the claim from "validating a strong negative correlation" to "suggesting a negative trend that warrants investigation with more models."
2. **Add a sensitivity analysis** for \(\epsilon\) (0.005, 0.02, 0.05) in the appendix, showing the main figures are qualitatively robust.
3. **Separate selection and evaluation data** for the ensemble experiment, at minimum by reporting cross-validated results, to rule out overfitting.
4. **Weaken the causal language in Sections 3.3.2–3.3.3.** Replace "suggests that scaling up dataset size could postpone the competition" with "models trained with larger datasets exhibit competition later in training" — an observed correlation, not a demonstrated causal effect.
5. **Discuss the Pythia-1B outlier.** Is this a genuine deviation from the trend or an artifact of the specific architecture/data recipe at that scale?

## Score and Decision

**Originality**: 7/10 — First to study TR/TL competition dynamics during pre-training; the competition measurement framework is novel.  
**Importance of research question**: 8/10 — Understanding ICL emergence is a timely and important problem.  
**Claims supported**: 4/10 — Central correlation is not statistically established; factor analyses have confounds; ensemble results are the best-supported claim but have evaluation rigor concerns.  
**Soundness of experiments**: 5/10 — Model size analysis is well-controlled; other factor analyses are confounded; ensemble evaluation lacks separated validation sets.  
**Clarity of writing**: 7/10 — Generally clear, though overclaims the strength of the evidence.  
**Value to community**: 7/10 — The idea and measurement framework are valuable; the ensemble method has practical potential; but the empirical evidence needs strengthening.

The paper tackles a genuinely interesting question with a novel analytical framework and a practically motivated ensemble method. However, its central quantitative claim (the negative correlation) is not statistically supported, and two of its three factor analyses (dataset size, data curriculum) rely on confounded comparisons. The ensemble results are the strongest contribution but would benefit from more rigorous evaluation. The paper is worth publishing if the authors can address the major weaknesses, particularly by honestly characterizing the correlation evidence and clarifying the evaluation protocol. In its current form, the evidence overreaches the claims.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>