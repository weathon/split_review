## Summary

This paper proposes NeRT, an implicit neural representation (INR) architecture for learning periodic signals. It decomposes a signal into a periodic factor (bounded in [-1,1], sinusoidal activations) and a scale factor (ReLU activations), multiplies them to reconstruct the signal, and uses a learnable Fourier feature mapping layer rather than the hand-crafted mappings used by prior INRs (FFN, SIREN). The empirical evaluation covers synthetic ODE/PDE data, periodic time series, and long-term time series, showing consistent extrapolation improvements over INR baselines.

## Strengths

- **Consistent and often large-margin improvement over INR baselines on extrapolation.** NeRT achieves substantially lower MSE than SIREN, FFN, and WIRE across all tasks. On Caiso periodic time series, NeRT's errors are approximately one-quarter of the baselines (Table 1). On 2D-Helmholtz extrapolation, it is the only INR that produces qualitatively correct results (Figure 4). On ETTh1 long-term series, NeRT achieves MSE 0.091 vs. SIREN 0.217 and FFN 0.341 (Table 2).

- **Learnable Fourier feature mapping is validated by direct ablation.** Table 3 compares the learnable Fourier mapping against a fixed-initialization variant on two datasets; the learnable version outperforms in both interpolation and extrapolation. This isolates the contribution of learning the Fourier parameters from the rest of the architecture.

- **Interpretable factor decomposition without explicit supervision.** The periodic/scale factorization (Eq. 3) is grounded in classical time-series decomposition (Cleveland et al., 1990) and produces visibly interpretable components (Figure 3c), while requiring only the composite signal for training.

- **Practical advantage over non-INR time series models.** As shown in Figure 7, NeRT uses a single trained model for varying prediction horizons, while Transformer-based and NODE-based baselines require separate retraining for each horizon length.

## Weaknesses

### Fatal

None.

### Major

1. **Pseudo-rigorous theoretical claims that do not withstand scrutiny.** Remark 3.1 claims that NeRT's kernel satisfies stationary/shift-invariant properties via NTK theory, and that the architecture "resorts to the extreme value theorem to perform prediction in OoD (extrapolation)." These assertions are not substantiated and, in the latter case, are essentially nonsensical — the extreme value theorem states that a continuous function on a closed interval attains its maximum/minimum; it has no bearing on out-of-distribution extrapolation. The NTK claim about the *learnable* Fourier mapping is also not properly justified: known NTK results (Tancik et al., 2020) apply to networks with *random* Fourier features, not learned ones. Section 2 references "our theoretical analysis (cf." without completing the sentence. For a paper submitted to a top venue, these passages read as padding rather than genuine analysis. **Either provide a proper theoretical argument or remove these references entirely.**

2. **Key hyperparameters that directly affect reproducibility are not reported.** (a) The regularization strength λ for the 3rd-order derivative penalty on the scale component (Section 3.3) is never stated. (b) The frequency sampling interval \[a,b\] for the learnable Fourier mapping ω_m (Eq. 2) is never specified — yet this is a critical design choice that affects the model's frequency coverage. (c) Model sizes (number of layers, hidden dimensions, total parameters) are claimed to be "set to be the same" across baselines (line 114) but the actual sizes are not reported. Without these, the reported results cannot be independently verified or reproduced.

3. **The "single model for interpolation and extrapolation" (Contribution 2) is an inherited property of the INR paradigm, not a novel contribution of this architecture.** SIREN, FFN, and WIRE can also be queried at any coordinate after training. The paper itself acknowledges that INRs "inherit" this trait (line 18). Listing it as a separate contribution overstates what is architecturally new. The paper should make clear that the novelty is in the *extrapolation quality* (how well it generalizes), not in the ability to query arbitrary coordinates.

### Minor

1. **The 489% outperformance claim (line 189) is ambiguous and poorly framed.** From the numbers in Table 2, "489%" appears to mean SIREN's MSE (≈0.40) is about 4.9× NeRT's MSE (≈0.08). This should be stated precisely (e.g., "NeRT achieves 4.9× lower MSE than SIREN") rather than as a percentage that could be misinterpreted as an exaggeration.

2. **Tension between method design and strongest results.** The method is architected around a periodic inductive bias (factor decomposition, sine activations, bounded periodic output), yet the paper states that its best quantitative results come from long-term time series where "periodicity is typically weak" (line 187). The Discussion (Section 4.3) touches on broader applicability but does not explain *why* a periodic architecture works on non-periodic data. This weakens the narrative coherence of the paper.

3. **Long-term time series evaluation is thin for a "scalability" claim.** Only two datasets (ETTh1, National Illness) are presented for the long-term forecasting experiments. While the paper cites space constraints, two datasets do not convincingly establish scalability, and the claim should be softened.

### Trivial

- Line 38 ("Our theoretical analysis (cf.") has an incomplete sentence structure.

## Nice-to-Haves

- Additional evaluation metrics beyond MSE (MAE, MAPE) for the time series experiments would strengthen the case.
- A comparison with NPP (Chen et al., 2022), which also learns periodic signals with a related approach, would be informative given the overlapping goals.
- Runtime or convergence speed comparison with INR baselines would be useful for practitioners.

## Removed Points

*These points were flagged by the reviewers but removed or demoted after cross-verification against the paper. They are retained here for transparency but should not be weighed in the final assessment.*

- **PINNs missing from PDE baseline comparison (removed):** The harsh critic criticized the absence of PINNs for the Helmholtz experiment. However, this experiment compares INR *architectures* on a PDE solution; PINNs use a different training paradigm (physics-informed loss) and are outside the paper's stated comparative scope. Not a valid weakness.
- **ω_m learnability ambiguity (removed):** The harsh critic questioned whether ω_m is learned or fixed. The ablation (line 202) clarifies that all parameters — ω_m, A_m, B_m, δ_m — are learnable. The paper is adequately clear.
- **Multiplicative vs. additive decomposition not justified (removed):** The harsh critic asked why multiplication (period × scale) rather than addition (trend + seasonality) is used. This is an architectural design choice tested empirically; the paper does not need to formally justify every design alternative.
- **Spatiotemporal coordinate ablation interpretation (removed):** The harsh critic said this ablation is "non-trivial to interpret." This is a standard ablation that tests whether a component helps; the interpretation is straightforward.
- **NTK theory as a strength (removed):** The strength finder listed the NTK connection as a strength. Since the corresponding weakness (overclaimed/pseudo-rigorous theory) is verified and substantive, the weakness wins per instructions.
- **"Could the metric be measuring a proxy?" / "are confounders controlled?" (removed):** These are generic area-of-concern speculations without concrete anchors in the paper.

## Novel Insights

None beyond the paper's own contributions. The reviewers' observations largely recapitulate what is visible in the paper: the method works well empirically but its theoretical framing is inflated, and many experimental details are underspecified.

## Suggestions

1. **Remove or properly ground all theoretical claims.** Either delete Remark 3.1 entirely, or replace it with a concrete, technically correct statement about what properties the architecture provably has. The extreme value theorem reference must be removed — it is incorrect as written and damages credibility.

2. **Report all missing hyperparameters in a dedicated table:** number of layers and hidden dimensions for NeRT and every baseline, the regularization strength λ, the frequency sampling interval \[a,b\], and the initialization ranges.

3. **Reframe the contributions.** Make Contribution 2 an explicit comparison against *non-INR* methods ("single model handles multiple horizon lengths unlike Transformer-based approaches") rather than a general architectural claim. Clarify in the introduction which properties are inherited and which are novel.

4. **Explain or contextualize the weak-periodicity results.** If the scale factor is capturing trend-like components that drive performance on non-periodic data, state this explicitly and show supporting analysis (e.g., visualize what the scale branch learns on these datasets).

5. **Cite specific baseline model sizes and report performance variability.** The standard deviations reported in the appendix should be brought into the main tables.

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>