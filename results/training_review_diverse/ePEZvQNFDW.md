Now I have all the information I need. Let me construct the final consolidated review.

---

## Summary

This paper proposes Continuous Ensemble Forecasting (CEF), a diffusion-based method that generates temporally consistent ensemble weather trajectories by freezing the driving noise across lead times. A single fixed noise sample is fed to an ODE solver for all lead times, making the score-network map deterministic in the noise, which yields trajectories that are continuous in time and can be sampled in parallel. The authors extend this with autoregressive rollouts combined with continuous interpolation (ARCI) to produce long-range forecasts at arbitrary temporal resolution. On WeatherBench data at 5.625°, ARCI-24/6h achieves results competitive with the best autoregressive baseline (AR-24h), and the method's ability to forecast at 1-hour resolution without the degradation seen in standard autoregressive 1-hour models is the strongest piece of evidence.

## Strengths

1. **Parallel, temporally consistent ensemble sampling.** Algorithm 1 is clean and well-motivated: freezing the noise across lead times turns the ODE solver into a deterministic map from noise to trajectory, enabling fully parallel sampling across both ensemble members and lead times. This directly addresses the computational bottleneck of iterative diffusion models. The paper reports a reduction from 32s (AR-6h) to 8s (ARCI-24/6h) per ensemble member.

2. **Fine temporal resolution without accuracy loss.** The hourly-forecast experiment (Figure 4/6) is the paper's strongest evidence. ARCI-24/1h achieves RMSE/CRPS nearly identical to AR-24h (the best model) at all lead times, while AR-1h degrades severely. The method even generalizes to unobserved lead times: ARCI-24/2h\* (trained only on 2-hour steps) performs similarly to ARCI-24/1h, demonstrating an ability to interpolate in lead time.

3. **Competitive probabilistic skill.** ARCI-24/6h is second-best overall in Table 1, closely matching AR-24h in RMSE, CRPS, and SSR across z500 and t850, while notably outperforming AR-6h and CI-6h. The method also beats the external baseline Graph-EFM.

4. **Principled motivation for noise freezing.** Section 4.1 formalizes the connection between latent noise space and the space of possible evolution functions via a commuting diagram (Figure 2), providing theoretical grounding for why freezing noise yields a valid sample from the trajectory distribution.

5. **Addresses conditional determinism with autocorrelated noise.** Algorithm 2 introduces an Ornstein-Uhlenbeck noise process to relax the overly deterministic conditional distributions that arise under fixed noise. Figure 3 shows that appropriate ρ values keep the temporal difference closer to the data's.

## Weaknesses

### Fatal
None.

### Major

1. **Missing comparison against linear interpolation of coarse AR forecasts.** The paper acknowledges this baseline explicitly ("An alternative … would be to linearly interpolate the forecasts sampled using an autoregressive model") but the sentence cuts off and no results are provided. For the hourly-resolution experiment, the natural question is whether ARCI-24/1h adds value beyond linearly interpolating AR-24h predictions at intermediate hours. Without this comparison, the central claim that the method enables "forecasts at an arbitrary fine temporal resolution without sacrificing accuracy" is incompletely supported — the fine-resolution forecasts could in principle be matched by a trivial post-processing step. This gap is the single most significant unaddressed question in the paper. The authors should provide this comparison (or a clear argument for why it is inappropriate given the probabilistic/ensemble setting) before acceptance.

### Minor

2. **Autocorrelated noise extension lacks evaluation on forecasting metrics.** Algorithm 2 is presented as a way to address the conditional determinism problem, but it is evaluated only on the temporal difference (ΔX) metric. No RMSE, CRPS, or SSR results are reported for any ρ > 0. While the ΔX plot shows the intended effect, the reader cannot determine whether the extension preserves or degrades probabilistic skill. The paper should report at least one forecasting metric for a representative ρ value.

3. **Temporal consistency evaluation relies on a single, limited metric.** The paper uses ΔX = |X(t) − X(t−1)| to argue for temporal consistency. While this captures continuity of the trajectory, small ΔX alone does not guarantee realistic temporal dynamics (a model predicting nearly the same state each hour could achieve small ΔX while being clearly wrong). The paper's strong RMSE results at 1h resolution partially mitigate this concern, but a complementary analysis (e.g., lag-1 autocorrelation, spectral content, or visual inspection of trajectory evolution) would strengthen the claim substantially.

4. **No error bars or uncertainty quantification on main results.** The paper acknowledges this limitation, but the omission is consequential because the differences between ARCI-24/6h and the top baseline (AR-24h) are small (e.g., z500 RMSE at 5d: 560.9 vs. 544.2). Without bootstrap intervals or replication-based uncertainty estimates, it is unclear whether these gaps are meaningful or within noise. The authors should report at least temporal bootstrap intervals over test years.

5. **Varying conditioning window across models.** The paper states that all models condition on Ω = {0, −δ} with δ being the model's timestep. This means AR-24h and ARCI-24/6h condition on the previous 24h, while AR-6h and CI-6h condition on only the previous 6h. This asymmetry benefits models with larger δ. While the paper's primary comparison (ARCI vs. AR-24h) controls for this, the broader comparison table should note this difference explicitly.

6. **Computational efficiency claim is undersubstantiated.** The 32s vs. 8s timing is reported as a single number without breakdown of neural network evaluations, solver steps, or GPU utilization. A more detailed cost comparison would strengthen the efficiency motivation.

### Trivial

None.

## Nice-to-Haves

- Discuss why ARCI-24/6h does not quite reach AR-24h's performance (small gap). Is the score function less specialized when handling multiple lead times (6, 12, 18, 24h)?
- Report the number of ODE solver steps and solver type for reproducibility of the timing results.
- A brief note on whether the conditioning-window asymmetry in Table 1 systematically advantages models with larger δ.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *Harsh Critic's statement that the paper "does not acknowledge the missing interpolation baseline"* — The paper does acknowledge it in line 333 (the cut-off sentence "An alternative … would be to linearly interpolate…"). However, the acknowledgment is incomplete, and no results are provided. The substantive criticism (missing comparison) remains in Major Weakness #1.

- *Criticism that the ΔX metric alone invalidates the temporal consistency claim* — While ΔX alone is limited, the paper also provides strong RMSE/CRPS results at 1h resolution (Figure 4), showing the forecasts are accurate at fine timescales, which partially addresses this concern. The weakness is retained but downgraded to Minor.

## Novel Insights

The core insight — that freezing the driving noise across lead times in a diffusion model's probability-flow ODE yields deterministic maps that are continuous in lead time, enabling parallel generation of temporally consistent ensemble trajectories — is the paper's most novel contribution. The identification of the latent noise space with the function space of possible evolutions (Section 4.1) provides a principled lens that goes beyond heuristic engineering. The ARCI combination (autoregressive rollouts at coarse resolution + continuous interpolation at fine resolution) is a practical contribution that cleanly decouples long-range accuracy from temporal resolution.

## Suggestions

1. **Add the linear interpolation baseline** as discussed. Compare ARCI-24/1h against linearly interpolated AR-24h forecasts on RMSE, CRPS, and SSR. Even if RMSE is similar, highlight where ARCI adds value: probabilistic calibration at intermediate times, ensemble spread, or faster-evolving variables (e.g., wind).
2. **Report at least one forecasting metric for the autocorrelated noise extension** (Algorithm 2) at a representative ρ value to demonstrate that probabilistic skill is preserved.
3. **Add bootstrap confidence intervals** (over test-year initialization times) to Table 1 and Figure 4.
4. **Strengthen temporal consistency analysis** with a complementary metric (e.g., lag-1 autocorrelation of ensemble members, or power spectra).
5. **Clarify the conditioning window** for each model variant and discuss how it may affect comparisons.

## Score and Decision

This paper proposes a genuinely novel method for ensemble weather forecasting with diffusion models. The core idea (noise freezing for temporally consistent parallel trajectories) is clean, well-motivated, and yields competitive results — especially the hourly-resolution experiment which convincingly shows the method's advantage over standard autoregressive approaches. The weaknesses are real but addressable: the missing linear interpolation baseline is the most important gap, but it does not invalidate the paper's core contributions (parallel sampling, temporal consistency, flexible resolution). The autocorrelated noise extension needs validation, and the temporal consistency metric could be strengthened. On balance, this is a solid paper with clear contributions that, with the suggested additions, would be a strong submission.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>