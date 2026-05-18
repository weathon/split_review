I now have a complete picture of the paper. Let me compile the final review.

## Summary

This paper proposes Continuous Ensemble Forecasting, a method for diffusion-based weather forecasting that generates temporally consistent ensemble trajectories by using a single fixed (or autocorrelated) noise sample across all lead times. The key idea is that by fixing the random seed in the probability flow ODE solver, the resulting forecasts at different lead times form smooth, continuous trajectories without requiring autoregressive rollouts. The method can also be combined with autoregressive steps (ARCI) to handle long lead times, while achieving arbitrary temporal resolution. On the WeatherBench 5.625° benchmark, ARCI matches the accuracy of state-of-the-art autoregressive diffusion models (AR-24h) while offering computational benefits and higher temporal resolution.

## Strengths

- **Parallel generation of temporally consistent ensemble trajectories**: The method generates forecasts for all lead times in parallel (no autoregressive steps), while maintaining temporal continuity. The temporal difference metric (Fig. 4) empirically validates that fixed-noise forecasts (ρ=0) closely track the data's temporal difference, confirming the method produces smooth trajectories.

- **High temporal resolution without accuracy loss**: ARCI-24/1h achieves the same forecast skill as AR-24h at 1-hour resolution over 10 days, while a purely autoregressive model at 1-hour steps (AR-1h) degrades severely (RMSE > 1300 vs. < 1000). This demonstrates a clear practical benefit: the ability to produce forecasts at arbitrary fine temporal resolution without the error accumulation that plagues small-step autoregressive models.

- **Competitive quantitative performance**: On the standard 5.625° WeatherBench benchmark, ARCI-24/6h matches AR-24h (the best autoregressive baseline) on most metrics for z500 and t850 at both 5- and 10-day lead times (Table 1), and outperforms the Graph-EFM latent-variable baseline. This shows the ARCI combination does not sacrifice accuracy for flexibility.

- **Generalization to unseen lead times**: ARCI-24/2h*, trained only on 2-hour intervals, performs nearly as well as ARCI-24/1h trained on all hourly steps (Fig. 4 description, line 335). This demonstrates the method can interpolate to finer temporal resolutions beyond its training setup, adding practical flexibility.

## Weaknesses

### Fatal
None.

### Major

- **The claim of sampling from the joint trajectory distribution p(X(𝒯)|X(Ω)) is unsupported by the evaluation.** The paper states "We treat this as a sample from p(X(𝒯)|X(Ω))" (line 143) and builds the theoretical motivation (Sec. 4.1) around identifying the latent noise space with the solution space of possible weather evolutions. However, the empirical evaluation uses only marginal metrics (RMSE, CRPS, SSR) at individual lead times — metrics that are insensitive to whether the joint distribution of forecasts across lead times is correct. The temporal difference metric (Fig. 4) checks smoothness but not joint probabilistic calibration (e.g., whether temporal autocorrelations of forecast errors match nature). The paper itself acknowledges the conditional determinism issue (Sec. 4.2), meaning the fixed-noise method imposes a structural constraint that cannot represent arbitrary joint distributions. Either (a) a joint-probabilistic evaluation (e.g., energy score over trajectories, rank histograms for sequences) or (b) an honest reframing of the contribution as a *deterministic coupling* heuristic that yields smooth trajectories with good marginal properties — rather than a provably correct joint sampling procedure — is needed to bring the claims in line with what is demonstrated. This is the paper's most significant weakness.

### Minor

- **The autocorrelated-noise extension (Alg. 2) is presented as addressing the conditional determinism issue but is not evaluated for joint forecast skill.** The paper states that Algs. 1 and 2 are "probabilistically equivalent for all time marginals" (line 221) and therefore only reports marginal metrics for one version. However, the autocorrelated noise is the mechanism proposed to remedy the conditional determinism shortcoming, and the place where it would make a difference is precisely in the joint/trajectory properties. The temporal difference plot (Fig. 4) shows that different ρ values affect trajectory smoothness, but no metric (e.g., energy score over trajectories, autocorrelation of ensemble mean errors) assesses whether this actually improves the joint distribution. The paper should either evaluate Alg. 2 with a joint metric or de-emphasize it as a contribution to joint forecasting.

- **The paper would benefit from a clear delineation of where continuous-only forecasting works and where it does not.** CI-6h performs well at short lead times but degrades at 10 days (z500 RMSE 885.7 vs. AR-24h's 750.6, Table 1). The paper honestly acknowledges this (line 270, Limitations), but the framing of the contribution (contribution 1: "can generate ensemble member trajectories without iteration") is broad. Since the continuous-only mode is practically limited to short horizons (a few days), while long horizons require autoregressive steps, the paper should more explicitly demarcate these two regimes.

- **Evaluation limited to 5.625° resolution.** The paper acknowledges this in the Limitations (line 353), noting it has not been shown to scale to higher spatial resolution. While this is standard for a WeatherBench paper, it constrains the generality of the conclusions about operational applicability.

### Trivial

- No error bars are reported due to computational constraints (acknowledged line 354). Acceptable for a conference paper but weakens comparison reliability.
- The speed comparison (line 261: 32s for AR-6h → 8s for ARCI-24/6h) would be clearer if the wall-clock time for AR-24h were also reported, since ARCI-24/6h uses the same 24h autoregressive step size.

## Nice-to-Haves

- A sensitivity analysis on the autoregressive step size (e.g., 12h vs. 24h) would strengthen claims about the method's flexibility.
- A joint-trajectory evaluation metric for the autocorrelated-noise variant (e.g., energy score over 24h trajectories) would directly address the gap between claims and evidence.
- A summary table of model architectures, training hyperparameters, and computational budgets would improve reproducibility.

## Removed Points

- **Missing comparison with DYffusion** — The paper discusses DYffusion in Related Work (lines 103–105), noting it "still requires sequential computations for sampling the prediction," which constitutes a conceptual comparison. An experimental comparison would require re-implementing a different training framework and is not a standard requirement for a method paper proposing a different approach.
- **24h autoregressive step not motivated** — The paper says "Taking longer timesteps (24h) has been shown to give better results" (line 93) with citations. This is adequately motivated.
- **Formatting/style nitpicks** — Removed per instructions.
- **Reproducibility nitpicks about undisclosed hyperparameters** — Removed per instructions; such details are standard to leave for a code release or appendix.

## Novel Insights

None beyond the paper's own contributions. The reviews largely affirm the paper's claimed strengths (parallel generation, temporal consistency, high-resolution capability) while identifying a gap between the joint-distribution framing and the marginal-only evaluation. The core insight — that sharing noise across lead times in a diffusion model's ODE solver produces smooth forecast trajectories — remains the paper's primary contribution and is well-supported by the experiments.

## Suggestions

1. **Reframe the central claim or add a joint evaluation.** The simplest path is to drop the claim of "sampling from p(X(𝒯)|X(Ω))" and instead describe the method as constructing a deterministic coupling between marginal forecast distributions, yielding smooth trajectories by design. Alternatively, add a joint probabilistic metric (e.g., energy score over 24h trajectories, autocorrelation of forecast errors) to validate the joint distribution claim.

2. **Evaluate Alg. 2 with a trajectory-level metric.** Since the autocorrelated-noise extension is presented as the fix for conditional determinism, demonstrate that it actually improves the joint distribution (not just the temporal difference) relative to fixed noise.

3. **Add a clear delineation in the paper of where continuous-only forecasting is applicable vs. where ARCI is needed.** This would help readers understand the practical deployment envelope.

## Score and Decision

**Originality:** 7/10 — The noise-sharing idea is simple and intuitive, and while related ideas exist (DYffusion, continuous-time forecasting for deterministic models), the specific application to diffusion ensemble trajectories is novel.  
**Importance of research question:** 8/10 — Probabilistic high-temporal-resolution forecasting is practically important for decision support and extreme weather.  
**Claims supported:** 5/10 — The practical claims about temporal consistency, parallelization, and competitive marginal scores are supported. The joint-distribution claim is not.  
**Soundness of experiments:** 6/10 — Appropriate for a WeatherBench paper at this resolution, but the evaluation gap (marginal vs. joint) is a real limitation.  
**Clarity of writing:** 7/10 — Well-structured and readable. The theoretical motivation is intuitive if not rigorous.  
**Value to community:** 7/10 — The method is simple, effective, and likely to be adopted by practitioners working with diffusion-based forecasting.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>