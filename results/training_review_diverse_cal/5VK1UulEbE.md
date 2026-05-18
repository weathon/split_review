Now I have all the information I need. Let me write the final consolidated review.

## Summary

This paper proposes FredNormer, a plug-and-play frequency-domain normalization module for non-stationary time series forecasting. It provides a theoretical proof that standard z-score normalization uniformly scales all non-zero frequency components (preserving the relative proportion of stable vs. unstable frequencies), then introduces a method that computes frequency stability via the inverse coefficient of variation across the training set and applies learnable per-frequency weighting via linear projections in the Fourier domain. Extensive experiments across seven datasets and three backbone architectures show consistent and often large MSE improvements over baselines including RevIN and SAN.

## Strengths

1. **Large and consistent empirical gains across multiple backbones and datasets.** Table 1 shows FredNormer improves both PatchTST and iTransformer on all seven datasets, with particularly striking gains on ETTm2 (33.3% MSE reduction for PatchTST, 55.3% for iTransformer). Results include standard deviations and hold across four forecasting horizons.

2. **Head-to-head superiority over existing normalization methods.** Table 2 shows FredNormer achieves 18 top-1 and 6 top-2 results out of 28 settings when compared against RevIN and SAN across both MLP-based (DLinear) and Transformer-based (iTransformer) backbones. For example, on ETTh1 with DLinear, FredNormer (MSE 0.407) outperforms RevIN (0.460) and SAN (0.421).

3. **Complementarity with existing normalization.** The Ours* variant (FredNormer + SAN) frequently achieves the overall best results (e.g., 4 top-1 results for DLinear), demonstrating that the frequency-domain weighting captures dynamics missed by purely time-domain normalization methods.

4. **Practical efficiency.** Running time comparisons show FredNormer is 60–70% faster per epoch than SAN on DLinear and PatchTST across four datasets (Figure 3). The method uses only DFT and linear projections, adding minimal parameters.

5. **Ablation validates the stability metric over alternative frequency selection strategies.** Table 4 shows that replacing the proposed stability measure with a low-pass filter or random frequency selection consistently degrades performance (e.g., on ETTh1 with iTransformer at horizon 96: Ours 0.389 vs. low-pass 0.401 vs. random 0.407).

## Weaknesses

### Major

1. **Ambiguity in the baseline experimental setup.** The paper states "We combine our module with a z-score normalization-denormalization operation in all experiments" (line 425) but never clarifies whether the comparison baselines (RevIN, SAN) also include an explicit z-score step. RevIN already performs instance normalization (a form of z-score) as part of its pipeline, and SAN has its own normalization logic. If FredNormer receives an additional z-score normalization layer that the baselines do not, the comparison in Table 2 may not be apples-to-apples, and the large reported improvements (e.g., 55.3% on ETTm2) become difficult to attribute specifically to the frequency stability weighting. This needs explicit clarification.

2. **Incomplete ablation of key design choices.** The ablation in Table 4 replaces the stability measure with low-pass or random filtering, which does partially validate the metric. However, several other components are never isolated: (a) the 1D-differencing step (Algorithm 2, line 2) — a well-known stationarity-enhancing operation that could be a significant source of gains; (b) the separate linear projections for real vs. imaginary parts; (c) the contribution of the z-score normalization layer that FredNormer is combined with. Without ablating the 1D-differencing (e.g., comparing FredNormer with and without it), it is impossible to confirm that the frequency stability weighting — rather than the differencing or the extra normalization — is the primary driver of the reported improvements.

### Minor

3. **Overstatement of "sample-specific variation."** The paper claims the learnable weighting layer "introduces sample-specific variations" (abstract, Section 3). However, the frequency stability measure S(k) is a dataset-level statistic, and the linear projections W·S + B are computed from it, producing weighting coefficients that are identical across all samples. The only source of per-instance variation is the input sample's own FFT, not the weighting layer itself. The method is better described as a global learnable filtering operation conditioned on aggregate dataset statistics. This does not invalidate the method but the phrasing is misleading.

4. **Insufficient running time comparison.** The paper claims that FredNormer "does not compromise the efficiency compared to existing normalization methods" but only reports running time against SAN (the most complex baseline). RevIN, the simplest and most widely-used baseline, is not included in the efficiency comparison. Since RevIN adds negligible overhead, the claim of general efficiency is not fully substantiated.

5. **Overstated novelty framing.** The paper claims to be "the first to investigate a frequency-based module to tackle the distributional issue in non-stationary time series" (line 74). Related work such as CoST, FiLM, and Koopa already models time-invariant frequency patterns, albeit as part of full forecasting architectures rather than plug-and-play modules. The distinction (plug-and-play module vs. full model) is valid, but the novelty should be stated more precisely.

### Trivial

None.

## Nice-to-Haves

- Show standard deviations (or confidence intervals) for the results in Table 2, which currently reports only point estimates.
- Include a variant that removes the 1D-differencing to isolate its contribution to the overall gains.
- Directly validate the "stable frequency" concept by visualizing the top-M frequencies identified by the stability measure and demonstrating their correspondence to meaningful periodicities.

## Removed Points

- **Criticism about dimensionless property not being preserved after linear transformation** — Removed because it is factually incorrect. The quantity S = μ/σ is dimensionless; a linear transformation α·S + β of a dimensionless quantity remains dimensionless. The paper's claim about dimensionless comparison is valid.
- **Criticism that Theorem 1 is not connected to the method** — This criticism is over-stated. The paper uses the theorem as motivation: since uniform scaling (z-score) cannot change the proportion of stable frequency energy, non-uniform weighting is needed. The connection is logical, even if motivational rather than algorithmic. This point is subsumed by Minor weakness #3 (overstated novelty) and is not itself an independent fatal issue.
- **Criticism that the theoretical contribution is "trivial basic signal processing"** — While the mathematics is indeed straightforward given the linearity of the Fourier transform, formalizing the limitation of existing normalization methods in the frequency domain is a useful framing contribution. The simplicity of the proof does not make it wrong or useless. This is reflected in Minor weakness #5 (overstated novelty) rather than treated as a separate fatal flaw.

## Novel Insights

None beyond the paper's own contributions. The reviewers' comments largely converge on the paper's own characterization: the empirical contribution is the main selling point, while the theoretical framing and ablation thoroughness need improvement. No reviewer identified a previously unrecognized pattern or surprising phenomenon.

## Suggestions

1. Explicitly state in Section 4.1 whether all compared methods (FredNormer, RevIN, SAN) receive the same base preprocessing (z-score or otherwise), or whether z-score normalization is an integral part of FredNormer's pipeline comparable to how instance normalization is integral to RevIN.

2. Add an ablation removing the 1D-differencing (or replacing it with an alternative detrending method) to quantify its contribution relative to the stability weighting.

3. Include an ablation of FredNormer without the z-score normalization layer (i.e., frequency weighting only) to show the standalone contribution of the stability-based weighting.

4. Add RevIN to the running-time comparison in Figure 3 to substantiate the efficiency claim relative to the de facto standard normalization method.

5. Soften the claim about being "first" and instead describe the contribution as "first plug-and-play normalization module operating in the frequency domain."

## Score and Decision

This paper makes a useful empirical contribution: a simple, practical, model-agnostic normalization module that consistently improves forecasting across multiple architectures and datasets. The method is well-motivated and the experiments are extensive. However, two significant issues — ambiguity about the baseline setup and an incomplete ablation that fails to isolate the 1D-differencing and z-score components — prevent full confidence that the reported gains are attributable to the claimed mechanism. These issues are addressable but require clarification and additional experiments. The paper is above the acceptance threshold in its current form given the strength and consistency of its empirical results, but would benefit substantially from addressing these concerns.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>