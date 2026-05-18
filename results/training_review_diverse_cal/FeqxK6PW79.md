Now I have all the information needed to produce the final consolidated review. Let me synthesize everything carefully.

## Summary
2-3 sentence summary of the paper's contribution.

This paper provides the first systematic manifold learning analysis of transformer-based time series forecasting (TSF) models, computing intrinsic dimension (ID) and mean absolute principal curvature (MAPC) across layers of Autoformer and FEDformer. The central finding is that TSF representations follow a consistent two-phase geometric profile — ID and MAPC stay fixed or decrease during encoding, then increase significantly during decoding — and that this pattern is shared across architectures, datasets, and forecast horizons. The paper also reports a positive correlation between final-layer MAPC and test MSE and analyzes the rapid convergence of geometric features during training.

## Strengths

- **First systematic manifold analysis of TSF transformers, revealing a consistent two-phase geometric profile.** The paper shows that during encoding ID/MAPC stay fixed or decrease, while during decoding both increase significantly. This pattern is demonstrated for two architectures (Autoformer, FEDformer) across traffic (Fig. 2), electricity, weather, and ETTm1 datasets (Figs. 3, 4) and four forecast horizons, establishing a novel characterization of how TSF transformer representations evolve with depth. The finding is robust and well-supported by the evidence presented.

- **Identifies fundamental differences between classification and regression tasks in manifold geometry.** The paper contrasts its findings with prior work on CNNs (Ansuni et al., Kaufman et al.), showing that TSF regression models lack the "hunchback" ID profile of classification networks and exhibit an opposite MAPC–accuracy trend (Sec. 4.1, 4.2). This task-specific characterization is a genuine contribution that deepens understanding of how architectural objectives shape learned representations.

- **Extensive empirical coverage for a descriptive study.** The analysis covers two architectures, seven benchmark datasets (ETTm1, ETTm2, ETTh1, ETTh2, weather, electricity, traffic), four forecast horizons (96, 192, 336, 720), and 10 random seeds per configuration, providing a reasonably comprehensive empirical foundation for the geometric observations.

- **Training dynamics analysis shows rapid manifold convergence.** The paper demonstrates that untrained models have random ID/MAPC profiles that converge within ~5 epochs (Fig. 6, Sec. 4.3), with encoder layers stabilizing faster than decoder layers, aligning with neural tangent kernel theory and prior work on representation stability.

## Weaknesses

### Fatal
None.

### Major

- **The MAPC–MSE correlation claim is not properly supported by the evidence presented.** The correlation analysis (Sec. 4.2, Fig. 5, Table 1) uses only four data points per dataset (one per forecast horizon), and these points are confounded with horizon. Longer horizons are known to produce both higher MSE and may systematically alter learned representations, meaning the reported correlation may simply reflect that harder tasks produce both higher error and different geometry. With n=4 per dataset, individual correlation coefficients as low as 0.46 (Autoformer, ETTm1) are not significant at conventional levels. The claim that this correlation "allows one to compare models without access to the test set" (abstract, Sec. 4.2) would require evidence across *different architectures or training runs at the same horizon*, which is not provided. The paper should either substantially qualify this claim or provide cross-architecture evidence.

- **The paper's title and framing overclaim relative to the evidence.** The paper is titled "Analyzing Deep Transformer Models for Time Series Forecasting via Manifold Learning" and repeatedly makes claims about "deep transformer models" in general, but all experiments use only two architectures (Autoformer and FEDformer). Important recent TSF transformers (e.g., PatchTST, TimesNet, iTransformer) are mentioned in related work but not analyzed. The claim that "deep transformer models exhibit similar geometric behavior across layers" (abstract) is a statement about Autoformer and FEDformer, not about the broader class. The paper should either include more architectures or carefully scope its claims.

### Minor

- **The dataset grouping claim ("related datasets attain similar manifolds") is asserted qualitatively without quantification.** The paper groups electricity/traffic together and weather/ETTm1 together based on visual similarity of profiles (Figs. 3, 4), but provides no measure of similarity (e.g., correlation of ID/MAPC values across layers between datasets) or statistical test of whether this grouping is meaningful. Quantifying this similarity would strengthen the analysis.

- **The training dynamics analysis is limited to a single dataset.** The convergence claim in Sec. 4.3 — that "approximately five epochs" suffices across all configurations — is illustrated with only the traffic dataset (Fig. 6). Showing this pattern on additional datasets would substantiate the claim.

- **The manifold estimation methods assume i.i.d. samples, applied to time series without discussion.** The TwoNN and CAML estimators both assume input points are drawn independently from the underlying manifold, but the paper's 500k/100k samples come from overlapping time series windows with strong temporal dependencies. The paper does not discuss whether this violates estimation assumptions or attempt to decorrelate/subsample to mitigate dependence. The estimates may be reliable despite this (many empirical papers use these tools on non-independent data), but the issue should be acknowledged.

- **The distinctive decoder increase could reflect architectural design (separate seasonal input) rather than a general geometric property.** The paper notes (line 53) that the decoder receives a separate data stream (seasonality information X_s). The observed "step" in the decoder could partly reflect the injection of this new input stream rather than a learned geometric property of the manifold per se. This does not invalidate the descriptive finding, but the alternative explanation deserves more discussion, and a control (e.g., tracking the X_s input manifold separately) would strengthen the interpretation.

### Trivial
None.

## Nice-to-Haves

- Comparing geometric profiles to a non-transformer TSF model (e.g., N-BEATS, a simple MLP, or DLinear) would clarify whether the observed two-phase pattern is specific to transformers or a general property of deep TSF models. This is not a weakness of the current paper (its scope is transformer analysis), but would strengthen the contribution if added.

- Reporting confidence bands or variance across the 10 seeds in the profile figures (rather than single curves) would help readers assess the robustness of the observed layer-wise patterns.

## Removed Points

These points were removed from the harsh critic's review because they do not survive fact-checking against the paper or violate the review guidelines:

- **"No comparison to non-transformer models" as a weakness.** The paper's stated scope is analyzing transformer-based TSF models. Demanding non-transformer baselines is scope creep — the paper should be evaluated on whether it analyzes transformers well, not on whether it also analyzes non-transformers. Moved to Nice-to-Haves.

- **"The paper should use other methods the reviewer prefers" (PatchTST, TimesNet, iTransformer as required baselines).** The paper transparently focuses on Autoformer and FEDformer as "established architectures that are still considered SOTA" (line 52). Including more architectures would strengthen breadth, but omitting them is not a flaw given the paper's stated scope. This is subsumed under the scope-overclaiming weakness above (which is about the paper's own claims, not about missing architectures per se).

- **Criticism that "the increase in the decoder could simply reflect the addition of a new data stream" is kept as a minor weakness** (see above), but the following related claim is removed: "the paper's comparison to classification results (Ansuni et al., Kaufman et al.) is interesting but superficial" — this is a subjective opinion, not a verifiable weakness, and the paper makes a genuine contrast with prior work.

- **"No discussion of the temporal structure of the data"** as a standalone criticism is subsumed under the i.i.d. assumption issue above.

- **The claim that "the observed 'step' in the decoder could be an artifact of the decomposition layer"** — the paper explains (line 54) why it samples after decomposition rather than attention (the Fourier Cross-correlation layer outputs near-identical values, giving zero curvature). This justification is reasonable. The concern is kept in weakened form in the Minor section.

## Novel Insights

The reviews surface one genuinely novel insight beyond the paper's own findings: the confound between horizon length and both MSE and MAPC in the correlation analysis implies that the paper's most practically-claimed result (using MAPC as a model comparison tool without a test set) would require demonstrating correlation *across models at fixed horizon*, which the current experimental design cannot provide. This reframes the paper's contribution: its strength lies in the descriptive geometric characterization, not in the predictive/proxy claim. The two-phase profile finding is the paper's genuine contribution, and the correlation claim should be either removed or substantially re-analyzed.

## Suggestions

1. **Reframe or remove the MAPC correlation claim.** Either provide cross-architecture or same-horizon evidence to support the claim that MAPC can be used to compare models without a test set, or clearly qualify that the observed relationship is across horizons within a model and does not generalize to cross-model comparisons.

2. **Include at least one additional recent TSF transformer architecture** (e.g., PatchTST) to broaden the scope of the claim that "deep transformer models exhibit similar geometric behavior," or explicitly scope the paper's claims to Autoformer and FEDformer.

3. **Quantify dataset similarity** using a simple metric (e.g., correlation of per-layer ID values between dataset pairs) rather than relying on visual grouping.

4. **Address the i.i.d. assumption** by acknowledging temporal dependencies in the data collection and, if possible, showing that subsampling with temporal spacing yields similar estimates.

5. **Show training dynamics on at least one additional dataset** beyond traffic to substantiate the rapid convergence claim.

## Score and Decision

**Originality:** 6/10 — First to apply manifold analysis to TSF transformers, but builds directly on established methodology from Ansuini et al. and Kaufman et al.  
**Importance of research question:** 7/10 — Understanding why TSF transformers work is important, and the manifold perspective is underexplored.  
**Claims supported:** 4/10 — The two-phase profile is well-supported; the MAPC correlation claim is not adequately supported; scope claims are overreaching.  
**Soundness of experiments:** 5/10 — Good coverage of datasets/horizons/seeds but methodological concerns (i.i.d. assumption, n=4 correlation, single-dataset dynamics).  
**Clarity of writing:** 7/10 — Well-organized and generally clear despite dense methodological content.  
**Value to community:** 6/10 — The descriptive findings provide a useful foundation for future work on TSF representation analysis.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>