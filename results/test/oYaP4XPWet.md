Now I have a thorough understanding of the paper and the reviews. Let me compose the final consolidated review.

## Summary

This paper extends the orthogonal statistical learning framework (Foster & Syrgkanis, 2023) to time-series causal forecasting by (1) introducing a cut-off τ that excludes recent treatments/outcomes from the conditioning set to avoid confounding from past decisions, and (2) generalizing the R-loss to categorical and high-dimensional treatments with one-hot, cumulative, and linear encodings. To evaluate causal models independently of the unconfoundedness assumption used during training, the paper further adapts Regression Discontinuity Designs (RDD) from econometrics to construct causal test sets. On a proprietary rail demand forecasting dataset, the proposed causal models improve RDD RMSE by ~36–37% over the best non-causal baseline. On the public MIMIC-III health dataset, the Causal TFT improves RDD RMSE by ~1.6% over the baseline TFT.

## Strengths

1. **Novel extension of orthogonal learning to time-series causal forecasting.** The paper formalizes daily treatment effects with a cut-off τ to avoid confounding from past treatments and extends the R-loss to categorical and linear high-dimensional treatments (Section 3.2, Propositions 2–3). This provides a principled framework that connects time-series forecasting to the well-grounded orthogonal learning literature, giving convergence-rate guarantees for CATE estimation under estimated nuisance parameters.

2. **Introduction of RDD as an evaluation methodology for causal time-series models.** The paper constructs causal test sets using Regression Discontinuity Designs under a continuity assumption that is orthogonal to the unconfoundedness assumption used during training (Section 4, Propositions 4–5). This addresses a real gap: the lack of evaluation methods for causal forecasting models that do not simply re-use the same assumptions made during model fitting.

3. **Strong empirical evidence on the rail demand forecasting dataset.** On a large proprietary dataset (~300K training time-series), the Causal iTransformer with linear encoding achieves an RDD RMSE of 0.1197 ± 0.0014, a 37% improvement over the best non-causal baseline (TFT, 0.1910 ± 0.0014) — a large, statistically unambiguous improvement (Table 1). The diagnostic figures (Figures 1–2) further show that non-causal models predict the *wrong sign* of the price-demand relationship, motivating the causal approach with concrete evidence.

4. **Flexible instantiation with multiple backbone architectures and treatment encodings.** The framework is implemented with both TFT and iTransformer backbones, and experiments evaluate one-hot, cumulative, and linear encodings (Sections 3.3, 5.1). This demonstrates generalizability and allows practitioners to choose encodings suited to their data dimensionality.

## Weaknesses

### Major

- **The RDD evaluation methodology lacks validation of its own accuracy, and uncertainty in the RDD estimates is not propagated into the metrics.** The paper treats RDD estimates as a reference for computing RMSE/MAE without quantifying the noise in those estimates themselves. The RDD estimator relies on Assumptions 3 (continuity) and 4 (unbiased specification errors), which are strong in a time-series context with discrete, irregularly spaced switching times. No simulation study is presented to verify that the RDD procedure recovers known CATE values under realistic noise, and no bootstrap intervals or error propagation is performed to assess whether model rankings are robust to RDD estimation uncertainty. The paper acknowledges the RDD estimates are "noisy" (line 320) and filters outliers at 2.5%, but this is insufficient to establish the reliability of the evaluation. Without validation, it is difficult to know whether the RDD estimates themselves have the fidelity needed to rank models — particularly on MIMIC where the improvement is small.

- **The choice of τ is not analyzed for sensitivity, and it is the key adaptation that distinguishes the time-series setting.** The cut-off τ is the core practical adaptation of orthogonal learning to time series (Section 3.2). On the rail dataset, τ is fixed at 0.33 (a proportion of the time series); on MIMIC, τ = t−1. The paper explains the rationale (past treatments confound the daily treatment effect) but provides no experiments varying τ. If τ is too small, residual confounding from early treatments may remain; if too large, the model loses predictive signal from recent observations. Without guidance or sensitivity analysis, the robustness of the method across datasets is unclear.

### Minor

- **On MIMIC, the reported improvement is small and its statistical significance is unclear.** The Causal TFT One-hot achieves RDD RMSE 2.861 ± 0.094 versus the TFT baseline 2.908 ± 0.102 — a ~1.6% improvement with overlapping standard deviations. While the improvement is directionally consistent across all five forecast horizons, the paper does not report whether this difference is statistically significant. The Causal Transformer baseline (Bica et al.) actually achieves numerically lower RDD RMSE than the Causal TFT at horizons τ+3 through τ+5 (e.g., 2.833 vs. 2.862), though with overlapping error bars. The public-dataset evidence for the method's superiority is therefore considerably weaker than the rail-dataset evidence, and the paper's central claim rests heavily on the proprietary rail experiment.

- **Different RDD kernel choices across datasets are not justified.** The rail evaluation uses a linear kernel with h=14, while MIMIC uses a rectangular kernel with h=5. The paper does not explain why different kernels and bandwidths were chosen, nor whether the model ranking is sensitive to these choices.

### Trivial

- None.

## Nice-to-Haves

- A simulation study (synthetic time-series with known CATE) validating that the RDD procedure recovers true effects under the stated assumptions with realistic noise levels would substantially strengthen the evaluation methodology.
- Reporting bootstrap-based confidence intervals on the RDD RMSE difference between models would clarify whether the MIMIC improvement is statistically significant.
- A sensitivity analysis varying τ (e.g., 0.2, 0.33, 0.5 on the rail dataset) would help users understand how to set this parameter in practice.

## Removed Points

- *Criticism that the Causal Transformer baseline has an "unfair advantage" the paper should be clearer about.* The paper already explicitly discusses this (lines 415–416: "Contrary to our Causal TFT, the Causal Transformer has access to the treatment sequence between τ and t..."). The paper is adequately transparent about this comparison issue.
- *Criticism about code release / reproducibility.* Per the instructions, cited entities and artifacts are assumed to exist.
- *Criticism that the orthogonal-learning theory extension is "straightforward."* Whether an extension is sufficiently novel is a matter of judgment, not a factual weakness. The paper is explicit that Proposition 3 applies Theorem 2 from Foster & Syrgkanis (2023) with d-dimensional treatments. The practical adaptations (τ, categorical/linear encodings) are what make the contribution useful; characterizing this as a weakness is an opinion, not a flaw. This point was moved here because it conflates "not surprising" with "not a contribution."
- *Various formatting/style nitpicks* per the parser artifact rule.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an insight about the paper that the paper itself does not provide.

## Suggestions

1. Add a simulation study validating the RDD procedure on synthetic data with known CATE before using it to rank models.
2. Report confidence intervals or bootstrap tests on the RDD RMSE differences (especially for MIMIC) to clarify statistical significance.
3. Perform and report sensitivity analyses for τ (e.g., 0.2, 0.33, 0.5 on rail) and for RDD kernel/bandwidth choices.

## Score and Decision

The paper addresses an important problem — training and evaluating causal forecasting models — and makes two meaningful contributions: a principled adaptation of orthogonal learning to time series with the τ cut-off, and an RDD-based evaluation methodology. The empirical results on the proprietary rail dataset are strong and consistent with the qualitative diagnostic evidence. However, the evaluation methodology is not adequately validated: the RDD estimates are treated as a reliable reference without quantifying their own uncertainty, and on the public MIMIC dataset the improvement is small and of questionable statistical significance. The lack of sensitivity analysis on τ further limits the practical guidance the paper offers. The contribution is real but the evidence is incompletely assembled. I recommend major revisions to address the validation concerns.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>