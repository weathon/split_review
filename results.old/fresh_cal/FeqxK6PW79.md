Now I have all the evidence I need. Let me construct the final consolidated review.

---

## Summary

This paper applies manifold learning tools (intrinsic dimension via TwoNN, mean absolute principal curvature via CAML) to analyze latent representations in transformer-based time series forecasting models (Autoformer and FEDformer). The main findings are: (1) ID and MAPC exhibit a two-phase profile across layers—flat/decreasing during encoding, increasing during decoding—that is consistent across architectures, datasets, and forecast horizons; (2) final-layer MAPC correlates positively with test MSE (opposite sign to classification CNNs); and (3) geometric profiles converge rapidly during training (within about five epochs). The paper addresses a genuinely understudied question and extends the manifold analysis paradigm from CNN classifiers to TSF transformers.

---

## Strengths

1. **Novel application of manifold analysis to TSF transformers.** While intrinsic dimension and curvature have been studied in vision CNNs (Ansuini et al., Kaufman et al.) and protein-sequence transformers (Valeriani et al.), this paper is among the first to systematically apply these tools to transformer-based time series forecasting models. The motivation (Section 1) and related work (Section 2) are well-positioned, and the research questions (how profiles change across layers, how they relate to performance, how they evolve during training) are clearly stated and worth investigating.

2. **Consistent two-phase geometric profiles across architectures, datasets, and horizons.** Figures 1–3 document the encoder-flat/decoder-increasing pattern for both Autoformer and FEDformer, on multiple datasets (traffic, electricity, weather, ETTm1) and all four forecast horizons (96, 192, 336, 720). That the same qualitative trend holds across these variations is the paper's strongest and most robust empirical result. The contrast with the "hunchback" ID profile in classification networks is a genuinely interesting observation.

3. **Qualitative correlation between MAPC and test MSE with opposite sign to classification.** Section 4.2 and Table 1 report positive correlation coefficients between final-layer MAPC and test MSE across all 12 model–dataset combinations (6 datasets × 2 models). Even if the individual correlation magnitudes are unreliable (see Weaknesses), the direction is consistent: **all** slopes are positive, which differs from the negative correlation found in CNN classifiers. This provides a suggestive finding about fundamental differences between regression and classification geometries.

4. **Training dynamics reveal rapid convergence.** Figure 5 shows that untrained profiles are random and converge to their final shape within a few epochs, with encoders stabilizing faster than decoders. This connects meaningfully to prior work on representation stabilization (Bonheme & Grzes) and the neural tangent kernel. Though demonstrated on only one dataset, the observation is plausible and well-framed.

---

## Weaknesses

### Fatal
None.

### Major

1. **Correlation analysis (Section 4.2) relies on statistically insufficient evidence.** Each correlation coefficient in Table 1 is computed from only **four data points** (one per forecast horizon per dataset). With n=4, correlation coefficients in the range 0.46–0.97 are not reliably distinguishable from noise, and no p-values or confidence intervals are reported. The average coefficients of 0.76 and 0.70 are therefore misleading as precise quantities. A proper analysis would either (a) use the 10 random seeds as independent trials (40 points per dataset), or (b) report confidence intervals on the correlations. The positive direction is robust across all 12 comparisons (qualitatively meaningful), but the paper's claim of "correlation" implying the MAPC can be used to "evaluate and compare deep neural networks based on statistics obtained directly from the train set" (line 110) is substantially over-claimed given the statistical weakness. Additionally, horizon length is a potential confounder (longer horizons produce both higher MSE and potentially different MAPC) that is neither controlled for nor discussed.

2. **No error bars or variability measures anywhere despite 10 seeds being collected.** The paper trains every configuration with 10 different random seeds (line 63) yet presents every figure as a single curve or point set without error bars, standard deviations, or any indication of variance across seeds. For an empirical analysis paper whose findings depend on profile shapes and correlation trends, this is a structural gap. The reader cannot assess whether observed patterns are robust across seeds or driven by a single outlier run.

### Minor

3. **Only two models studied, but the title and framing claim generality about "Deep Transformer Models."** The paper focuses on Autoformer and FEDformer (2021–2022), both of which use the same series-decomposition architecture. The title's reference to "Deep Transformer Models" and claims about "transformer forecasting manifolds" (line 24) suggest broader generality than the evidence supports. Without testing whether the geometric patterns hold for other popular TSF transformers (e.g., PatchTST, iTransformer, Crossformer), it is unknown whether the findings are specific to the Autoformer/FEDformer decomposition architecture or general to all TSF transformers. (The paper does scope to these two in the text, but the mismatch with the title is noticeable.)

4. **Claims of profile "similarity" rely on visual inspection without quantitative measures.** Section 4.1 repeatedly states that ID/MAPC profiles are "similar" across architectures, datasets, and horizons, but no quantitative similarity metric is used (e.g., correlation of ID across layers between models, mean squared difference, or shape distance). The visual inspection claim is a reasonable starting point, but the paper would be stronger with even a simple quantitative comparison.

5. **Training dynamics shown for only one dataset (traffic).** Section 4.3 and Figure 5 use only the traffic dataset. While the observations are interesting, it is unclear whether the rapid convergence pattern generalizes across datasets. The paper acknowledges two-phase profiles vary across datasets (weather vs. electricity vs. ETT), so training dynamics may also vary.

6. **"Convergence within 5 epochs" lacks a quantitative convergence criterion.** The claim that profiles "converge" within approximately five epochs (line 140) is based on visual inspection of Figure 5. No threshold for convergence (e.g., relative change in ID/MAPC < 1%) is defined, and the epoch sampling schedule is not specified.

7. **i.i.d. assumption of the ID and curvature estimators is not discussed for time series data.** The TwoNN method (Facco et al., 2017) and CAML (Li et al., 2018) both assume i.i.d. samples. However, time series data has temporal dependence. The paper does not acknowledge this potential issue or test robustness (e.g., by computing ID on temporally shuffled data). The severity may be limited (the estimators rely on nearest-neighbor distances, which are based on the data distribution, not temporal ordering), but it warrants at least a discussion.

8. **Dismissal of the ETT "hunchback" ID profile as an artifact of low feature count is ad hoc.** The paper states (line 89) that the hunchback trend in ETT datasets "is due to ETT* datasets consisting of a total of seven features, and thus we do not consider this behavior to be characteristic to the network." No supporting experiment (e.g., sub-sampling features in other datasets to test whether the hunchback re-appears) is provided, making this a post-hoc explanation rather than a verified claim.

### Trivial

9. **The speculation about ETT-climate correlation (line 89) is out of place in a Results section.** Claiming that ETTm1 and weather share geometric features because "electricity transformer temperature (ETT) and climate change" are correlated is scientifically tenuous and does not belong in an empirical results section. The same point about dataset similarity could be made without this speculative justification.

---

## Nice-to-Haves

- **Use seed-wise replicates for the correlation analysis** (40 points per dataset instead of 4) to obtain credible correlation estimates with confidence intervals.
- **Add one or two more recent TSF models** (e.g., PatchTST or iTransformer) to test whether the two-phase profile and correlation pattern generalize beyond Autoformer/FEDformer.
- **Include a robustness check** for the i.i.d. issue: compute ID/MAPC on temporally shuffled data to test sensitivity to autocorrelation.
- **Add a simple non-transformer baseline** (e.g., DLinear, N-BEATS) to clarify whether the observed trends are specific to transformers or shared by all deep TSF models.
- **Quantify profile similarity** across architectures/datasets (e.g., cross-correlation of ID across layers) rather than relying on visual inspection.

---

## Removed Points

These points were raised by the reviewers but are removed or demoted with justification:

- **"The decision to sample only after decomposition blocks limits the analysis"** — The paper explicitly justifies this choice (line 54: the FEDformer Fourier layer yields zero curvature estimates) and clearly defines the study path. This is a transparent scope choice, not a flaw. Demoted to Removed.
- **"Reproducibility details: precise epochs, convergence criterion, seed values not provided"** — The paper states it uses 10 seeds and the training dynamics figure visually shows the sampled epochs. While exact epoch numbers would be nice, this is a documentation nitpick below the level of a real weakness.
- **"Missing non-transformer analysis"** — The paper's stated scope is *transformer* models. Demanding non-transformer comparison is scope creep outside what the paper set out to do (analysis of TSF *transformer* models).
- **"The statement about ETT climate change correlation is irrelevant"** — Demoted to Trivial (point 9 above) rather than removed, as it is a minor stylistic issue.
- Various section-by-section notes about missing appendix content — the appendix was stripped by the PDF parser and exists in the original submission.

---

## Novel Insights

Beyond the paper's own contributions, the reviews collectively highlight an important tension: the paper's most novel claim (MAPC correlates with test MSE, opposite to classification) is also its weakest link statistically, while its less flashy claim (two-phase geometric profiles) is actually more robustly supported. This suggests the paper would be stronger if it recentered its narrative around the well-supported geometric characterization and presented the correlation finding as a suggestive but preliminary observation requiring larger-scale validation. The reviewers also surface a useful cross-cutting point: manifold analysis tools developed for i.i.d. classification settings need to be scrutinized more carefully when applied to temporally dependent time series data, which is a consideration the TSF community should adopt as a standard practice going forward.

---

## Suggestions

1. **Fix the correlation analysis.** Either compute correlations across seeds (40 points per dataset) or at minimum report confidence intervals for the n=4 correlations and acknowledge the limitation. Present this as a suggestive trend rather than a well-established finding.
2. **Add error bars to all figures.** Use the 10 seeds to show variability (shaded regions or error bars) for every ID/MAPC curve and correlation plot.
3. **Tone down the title and broad claims** if only two models are studied. Consider "Analyzing Autoformer and FEDformer..." or add at least one more recent TSF transformer to support the broader framing.
4. **Add a quantitative similarity measure** for profile comparisons (e.g., compute correlation between ID profiles across architectures for each dataset).
5. **Acknowledge and discuss the i.i.d. assumption** of the TwoNN and CAML estimators with respect to time series dependence, and ideally provide a robustness check.
6. **Move speculative material** (double descent, model expressiveness, ETT-climate links) to the Discussion and mark it clearly as hypothesis rather than result.

---

## Score and Decision

**Originality:** 7/10 — Novel application to an understudied domain (TSF transformers), building on established manifold methods from vision.

**Importance of research question:** 7/10 — Understanding why TSF transformers work is a timely and valuable direction.

**Claims well-supported:** 5/10 — The two-phase profile is well-supported. The correlation claim is under-supported. Training dynamics are limited to one dataset.

**Soundness of experiments:** 5/10 — Good experimental design (10 seeds, multiple datasets/horizons), but severely undermined by absence of error bars and weak statistical evidence for the central correlation claim.

**Clarity of writing:** 7/10 — Clearly written and well-organized. Speculation is mostly marked as such.

**Value to the research community:** 6/10 — The geometric characterization is a useful reference, but the statistical weaknesses reduce its immediate impact as a definitive study.

Overall: The paper makes a genuine contribution by being one of the first to characterize the geometric properties of latent manifolds in TSF transformers. The two-phase profile finding is robust and interesting. However, the paper's most prominent promotional claim—that MAPC correlates with test performance—rests on statistically weak evidence (n=4 correlations, no error bars), and the analysis is limited to two models of similar vintage and architecture. These issues are fixable with additional experiments and statistical rigor, and the core findings are worth preserving.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>