Here is my consolidated final review.

---

## Summary

This paper applies manifold learning tools (intrinsic dimension via TwoNN, mean absolute principal curvature via CAML) to analyze latent representations of Autoformer and FEDformer across multiple time series forecasting benchmarks. It reports several observations: (i) ID and MAPC profiles follow a two-phase pattern (flat/decreasing in encoders, increasing in decoders) that is shared across architectures, datasets, and horizons; (ii) final-layer MAPC is positively correlated with test MSE (average r≈0.76 for Autoformer, 0.7 for FEDformer), opposite to the trend reported for classification CNNs; (iii) untrained manifolds are unstructured and converge within roughly five epochs. The paper is an empirical analysis paper — no new method is proposed.

## Strengths

- **Systematic characterization of geometric profiles across models, datasets, and horizons.** The paper demonstrates that Autoformer and FEDformer share similar ID and MAPC profiles (encoder: flat/decrease; decoder: increase) across six datasets and four forecast horizons (Figs. 1–3, 5), showing these patterns are consistent across diverse configurations. This is the first such analysis for transformer-based TSF models.

- **Discovery of a consistent MAPC–performance correlation with an opposite sign to classification CNNs.** The paper reports correlation coefficients between final-layer MAPC and test MSE across six datasets (Table 1), and notes that lower MAPC corresponds to better performance — contrasting with the positive correlation found in CNN classifiers by Ansuini et al. and Kaufman et al. This reversal is a genuinely novel finding that suggests regression and classification may require different geometric inductive biases.

- **Identification of two distinct geometric phases (encoder vs. decoder) consistent across architectures.** The paper describes a clear structural characterization: during encoding, ID and MAPC drop or stay fixed; during decoding, both increase (Sec. 4.1, Fig. 6). This differentiates TSF transformers from classification CNNs, which exhibit a "hunchback" ID profile. The contrast is explicitly and informatively discussed.

- **Observation of rapid manifold convergence during training.** The paper shows that untrained ID and MAPC profiles are unstructured, converge to their final configuration within approximately five epochs, and that the decoder converges more slowly than the encoder (Fig. 5). This provides practical insight for training acceleration (e.g., early stopping of encoder training).

- **Use of differentiable geometric tools (TwoNN, CAML) that are computationally feasible at scale.** The analysis pipeline processes 500k points for ID and 100k for MAPC per manifold at extrinsic dimension 512, demonstrating tractability for large-scale TSF analysis.

## Weaknesses

### Fatal
None.

### Major

1. **Fragile statistical evidence for the MAPC–performance correlation.** The central claim that "test MSE is proportional to the MAPC" (Fig. 4, Table 1) is supported by only four data points per dataset (one per horizon). Correlation coefficients with n=4 are highly unstable — a single point can change the sign or magnitude — yet no confidence intervals, p-values, or standard errors are reported. The coefficients themselves vary widely across datasets (e.g., 0.46–0.97 for Autoformer; 0.50–0.86 for FEDformer). The average of 0.76/0.7 is reported without uncertainty. The paper trains with 10 seeds; pooling across seeds would yield 40 points per dataset (4 horizons × 10 seeds) and enable proper statistical inference. The qualitative observation of a trend is valuable, but the current evidence does not support the strength of the claimed correlation.

2. **No uncertainty quantification across random seeds.** The paper states that each model/dataset/horizon combination is trained with 10 seeds (Sec. 3, Data collection), yet all figures and Table 1 report single-point estimates without error bars, standard deviations, or any indication of seed variance. The reader cannot assess whether the observed profiles and correlations are robust or driven by outlier seeds. This undermines confidence in every quantitative result — the most straightforward fix (plotting means ±1 std across seeds) would immediately address this.

3. **Training dynamics analysis is restricted to a single dataset (traffic).** Section 4.3 presents ID/MAPC evolution during training only for traffic. The paper then makes general claims about convergence speed ("requiring approximately five epochs to converge in all the configurations"), encoder vs. decoder convergence differences, and that "most learning takes place in the decoder." These may be dataset-specific. Without replication on at least one more dataset (e.g., electricity or weather), the training dynamics section reads as a single case study, and the broad claims are not supported by the evidence presented.

4. **The i.i.d. assumption underlying TwoNN and CAML is not discussed for time series representations.** TwoNN and CAML were developed for settings where data points are independent draws. The paper extracts latent representations from sequential (and potentially overlapping) time windows, where temporal dependencies could induce correlated distances and systematically bias both ID and MAPC estimates. The paper mentions the i.i.d. analogy only in passing (Sec. 1) and never addresses whether this is a concern for the reported estimates. This is a methodological blind spot — even an acknowledgment of the limitation would strengthen the paper's honesty, and a small synthetic validation (known manifold with injected temporal correlation) would substantially increase confidence in the findings.

### Minor

- **No sensitivity analysis for ID/MAPC estimation parameters.** The ID estimate uses 500k points and MAPC uses 100k points. It is not shown whether results are stable with respect to these choices (e.g., 50k vs. 1M points). Given that the paper's conclusions rest entirely on these estimates, some robustness check is expected.

- **Justification for skipping attention-layer sampling is not empirically validated.** The paper notes that the "Fourier Cross-correlation layer outputs almost identical values for all samples... yielding zero curvature estimates" and thus samples only after decomposition blocks. This is a reasonable practical choice, but no evidence is provided (e.g., a histogram showing near-zero variance at attention outputs). It is unclear whether this choice misses important geometric transformations occurring in attention.

- **The "hunchback" ID trend on ETT* datasets is dismissed somewhat too quickly.** The paper attributes the ETT* hunchback to these datasets having only seven features, treating it as a non-characteristic outlier. This explanation may be correct, but it is presented without supporting evidence. The alternative possibility — that TSF transformers genuinely behave differently on low-dimensional inputs — is not discussed.

- **ID was not examined for correlation with performance.** The paper analyzes MAPC–MSE correlation but does not report whether ID is also correlated with performance. If ID was examined and showed no correlation, that is a useful null result; if it was not examined, the omission is noticeable given that prior work (Ansuini et al.) found ID–performance correlations in classifiers.

- **The claim that "untrained profiles are random" is qualitative.** The dashed black curves in Fig. 5 do appear less structured, but "random" is not quantified (e.g., vs. a null distribution). Some metric comparing trained vs. untrained profile variance would strengthen this observation.

### Trivial
None beyond what has been noted as minor.

## Nice-to-Haves

- **Comparison to a non-transformer TSF baseline** (e.g., N-BEATS, DLinear). The paper studies transformer models, which is legitimate scope, but many observed effects could be general to deep TSF networks. Including one simpler architecture would sharpen the claim of whether these patterns are transformer-specific or general to deep forecasting.

- **Computational cost reporting.** For the MAPC-based model comparison approach to be practically useful (e.g., for model selection without test sets), one needs to know how expensive ID/MAPC estimation is relative to training.

- **Synthetic validation of manifold estimators on time series data.** A controlled experiment with known manifold structure and injected temporal correlation would validate that TwoNN/CAML recover correct estimates despite non-i.i.d. sampling.

## Removed Points

These points are flagged to be removed, treat them with caution:

- *"Only four datasets used for ID/MAPC profiles"* — The paper actually uses electricity, traffic, weather, ETTm1, ETTm2, ETTh1, ETTh2 (7 datasets); this criticism is factually wrong.
- *"Clinically relevant correlation"* (from Strength Finder) — This descriptor is nonsensical for a time series forecasting paper and was removed.
- *"Missing appendix" / "missing proofs in appendix"* — The appendix is present in the original submission but stripped by the parser; this is not a paper flaw.
- *"The paper does not cite/review related work on [X]"* — As per instructions, missing related works are not actionable without external verification.
- *Formatting/style nitpicks* — Parser artifacts, not author errors.

## Novel Insights

None beyond the paper's own contributions. The review surfaces the fragility of the central correlation claim and the missing uncertainty quantification, but these are weaknesses of the paper rather than novel interpretations. The paper's genuine novelty — the first systematic geometric characterization of TSF transformers and the discovery of an opposite-sign MAPC–performance correlation vs. classifiers — remains its core contribution.

## Suggestions

1. **Pool across seeds for the correlation analysis.** Instead of one point per horizon, report 4 horizons × 10 seeds = 40 points per dataset with confidence intervals. This would transform the fragile 4-point regression into a proper statistical test.

2. **Add error bars (±1 std over 10 seeds) to all geometric profiles.** This single change would address the most impactful methodological gap and immediately show whether the observed patterns are robust.

3. **Extend training dynamics to at least one more dataset** (electricity or weather) before claiming general convergence rates. This is a modest extension that would significantly strengthen Sec. 4.3.

4. **Acknowledge and discuss the i.i.d. limitation** for manifold estimation on sequential representations. Even a paragraph in the Discussion would suffice; a small synthetic validation would be ideal.

5. **Reframe the MAPC–MSE relationship** as a qualitative observed trend rather than a rigorously validated correlation, unless the statistical evidence (as in suggestion 1) is provided.

## Score and Decision

**Originality:** Good — first systematic manifold analysis of TSF transformers. **Importance of question:** Good — understanding TSF models is a timely problem. **Claims supported:** Partially — the profile observations are well-supported; the correlation claim is weakly supported; training dynamics are limited to one dataset. **Soundness of experiments:** Moderate — missing uncertainty quantification and an undiscussed i.i.d. assumption weaken the evidence base. **Clarity of writing:** Good — well-structured and readable. **Value to community:** Moderate — the qualitative observations are useful, but the key quantitative claim needs stronger evidence.

The paper tackles a worthwhile question and reports several intriguing qualitative observations. However, the evidence for the most important quantitative claim (MAPC–MSE correlation) rests on only four data points per dataset with no uncertainty quantification. The training dynamics analysis is restricted to a single dataset, and the manifold estimators' i.i.d. assumption is not discussed in the context of sequential time series windows. These are not superficial omissions; they affect the believability of the paper's central conclusions. While the contribution is potentially valuable, the evidential gaps are too large for acceptance in the current form.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>