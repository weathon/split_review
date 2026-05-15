I have all the information I need. Let me now synthesize the final review.

---

## Summary

This paper proposes Continuous Ensemble Forecasting, a method that uses a lead-time-conditioned diffusion model with a fixed (or autocorrelated) noise vector across all lead times to generate temporally consistent ensemble trajectories in parallel, avoiding autoregressive rollout for intermediate times. The authors further introduce ARCI (Autoregressive Rollouts with Continuous Interpolation), which combines 24h autoregressive steps with continuous interpolation at finer resolution. Evaluated on WeatherBench at 5.625°, the method achieves competitive RMSE/CRPS/SSR scores at 6h and 1h resolutions, with the key advantage that 1h-resolution forecasts retain the skill of 24h-step autoregressive models.

## Strengths

- **Parallel ensemble generation without sequential rollouts**: Algorithm 1 generates all ensemble members and all lead times simultaneously (the inner loop "can be done fully in parallel for all *k* and *i*"). This is a genuine engineering advance over autoregressive diffusion models, reducing sampling time from 32s (AR-6h) to 8s (ARCI-24/6h) for a 10-day forecast at 6h resolution.

- **Arbitrary temporal resolution without accuracy loss**: Figure 5 shows that ARCI-24/1h matches the RMSE/CRPS of AR-24h at 1h resolution, while a naive AR-1h model degrades severely. The ARCI-24/2h* variant (trained only on 2h steps) generalizes to 1h steps, demonstrating interpolation capability — a practically useful property.

- **Competitive quantitative results**: Table 1 shows ARCI-24/6h consistently achieves second-best RMSE and CRPS across variables and lead times, closely trailing AR-24h and outperforming AR-6h, CI-6h, Graph-EFM, and the Deterministic baseline. The SSR values are closest to 1 among diffusion-based models, indicating reasonable calibration.

- **Honest discussion of limitations**: The paper explicitly acknowledges the conditional determinism problem (Section 4.2), the lack of error bars, the question of scaling to higher resolution, and the computational cost of ODE solving. This candor is appreciated, even though some of these limitations are substantive.

## Weaknesses

### Fatal
None.

### Major

- **The joint-distribution claim is not sufficiently supported, theoretically or empirically.** The paper frames the method as sampling from *p*(*X*(𝒯) | *X*(Ω)) — the joint trajectory distribution. The theoretical motivation in Section 4.1 identifies the noise latent space with the space of evolution functions, arguing that if the score network is well-trained, the distribution of functions *f*<sub>*θ*</sub><sup>*Z*</sup> "should mirror" that of the true solutions *f*<sup>*i*</sup>. However, the diffusion model is trained only on marginal distributions *p*(*X*(*t*) | *X*(Ω), *t*); there are infinitely many joint distributions over trajectories compatible with the same set of time-marginals. The paper offers no argument that the fixed-noise coupling — which selects exactly one specific temporal coupling — corresponds to the true temporal dependence structure of the weather system. The paper itself acknowledges the conditional determinism problem (Section 4.2) and introduces an autocorrelated noise extension, but the central claim that the method produces samples from the *joint* distribution remains unsubstantiated by either reasoning or experiment. The method demonstrably produces *smooth* and *temporally consistent* trajectories, but smoothness is not equivalent to correct joint distribution sampling.

- **No trajectory-level evaluation metrics are reported.** All quantitative evaluation (Table 1, Figure 5) is on per-lead-time metrics (RMSE, CRPS, SSR). The only temporal evaluation is the mean absolute temporal difference |*X*(*t*) − *X*(*t*−1)| in Figure 4, which measures smoothness but not whether the *evolution of uncertainty* across lead times is physically realistic. Metrics such as temporal rank histograms, transition-probability scores, autocorrelation of ensemble-mean errors, or the probability integral transform of successive differences are absent. Without these, the paper's strongest advertised contribution — correct ensemble *trajectories* (as opposed to marginally-correct but potentially wrong paths) — is not empirically established. The claimed contribution is reduced to "smooth trajectories with good marginal scores," which is still useful but less than advertised.

### Minor

- **The theoretical motivation, while not a rigorous proof, is presented as the "key insight"** (Section 4.1) but conflates a useful heuristic framing with a formal justification. The paper would benefit from more precise language: the identification between noise space and function space is an *interpretation* that motivates the algorithm, not a *derivation* that guarantees correct joint distribution sampling. The paper already hedges ("Under some regularity conditions," "should mirror") but the overall framing overreaches.

- **No comparison to linear interpolation of 24h forecasts as a baseline for the 1h-resolution experiment.** The paper mentions this baseline ("An alternative to directly producing forecasts… would be to linearly interpolate…") but the sentence is truncated and no such comparison appears in the main figures. If linear interpolation of AR-24h forecasts yields similar skill at 1h, the continuous model's sophistication would be unnecessary for fine resolution. This comparison is essential for interpreting Figure 5.

- **The OU process extension (Algorithm 2) is not validated on any downstream forecast metric.** Figure 4 shows that different *ρ* values change the temporal difference, but no RMSE/CRPS/SSR or calibration metric is reported for the autocorrelated noise variant. It is unclear whether the added stochasticity improves or degrades forecast quality.

- **No computational comparison with AR-24h specifically.** The 8s vs. 32s comparison is with AR-6h, but the main accuracy baseline is AR-24h. The wall-clock advantage of ARCI over AR-24h is presumably smaller and not quantified.

- **The OU process implementation is underspecified.** The recurrence in Algorithm 2 applies element-wise (a scalar *ρ* to each element of the state-shaped noise vector). The paper does not discuss whether the same *ρ* is used independently per grid cell and whether this loses spatial noise correlations that could affect the spatial smoothness of trajectories.

### Trivial

- The problem formulation in Section 3 does not state the concrete spatial grid size or variable count, which would help contextualize the experiments.
- Figure 4's caption does not specify whether the temporal difference is averaged over all grid points and all initialization times.
- The word "trajectories" in the abstract ("temporally consistent ensemble trajectories completely in parallel") could be read as implying the full joint distribution is sampled; "temporally consistent" and "from the joint distribution" are distinct claims.

## Nice-to-Haves

- A case study showing how individual ensemble member trajectories evolve for a specific weather event (e.g., a developing storm) would help the reader judge whether the trajectories diverge plausibly.
- Spatial maps of temporal differences would be more informative than the global average; different regions have very different variability.
- An ablation comparing CI-6h with and without fixed noise would isolate the effect of the coupling on trajectory quality.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Abstract oversells the method's accuracy":** The abstract says "competitive results," and Table 1 confirms ARCI-24/6h is consistently second-best, closely trailing AR-24h. "Competitive" is an accurate descriptor; this criticism is removed.
- **"Introduction conflates limited temporal resolution with error accumulation":** The paper states that small timesteps cause error accumulation, which forces 12h resolution. This is a causal statement, not a conflation. Removed.
- **"Truncated sentence about linear interpolation":** The sentence ending "In fig." is a parser artifact. The original submission likely contains the full reference. Removed per hard rule about parser artifacts.
- **"Missing error bars is a severe weakness":** The paper acknowledges this limitation. Single-run evaluation without error bars is standard practice for large-scale weather benchmarks at this resolution, not a severe flaw. Downgraded to minor and placed in Removed Points as per instructions.
- **"Section 5 Models — nice experiment but would be stronger with extrapolation to longer lead times":** The paper's scope is interpolation for fine temporal resolution after coarse autoregressive steps; demanding extrapolation beyond trained horizons is scope creep. Weak removed.
- **Strength Finder's "Principled mathematical motivation" strength**: This conflicts with the verified weakness about the theoretical framing being heuristic rather than rigorous. Moved here.
- **Strength Finder's generic or contextless claims**: All strengths from the Strength Finder were verified against the paper and substantive ones are retained above. No generic strengths were found that survived filtering.

## Novel Insights

None beyond the paper's own contributions. The key observation — that freezing the noise in a time-conditioned diffusion ODE solver produces smooth trajectories — is clearly stated in the paper, and no reviewer surfaces a genuinely unexpected implication beyond what the authors already discuss (e.g., the conditional determinism problem and the OU process fix).

## Suggestions

1. **Reframe the central claim.** Replace "sample from *p*(*X*(𝒯) | *X*(Ω))" language with a more precise characterization: the method produces temporally consistent trajectories whose *marginal* distributions at each lead time are correct (since the diffusion model is trained on time-conditioned marginals) and whose temporal smoothness is empirically demonstrated. Clarify that the coupling is a heuristic that yields smoothness and parallel sampling, not a theoretically grounded joint-distribution sampler.

2. **Add trajectory-level evaluation.** Temporal rank histograms, autocorrelation of ensemble-mean errors, or transition-probability scores would directly test whether the joint temporal structure is correct. This would either validate the stronger claim or honestly bound what the method achieves.

3. **Include the linear-interpolation baseline in Figure 5.** If AR-24h forecasts linearly interpolated to 1h perform similarly to ARCI-24/1h, this should be reported and discussed; if they do not, this strengthens the paper's case substantially.

4. **Validate the OU process extension (Algorithm 2) on forecast metrics.** Report RMSE/CRPS/SSR for different *ρ* values to show whether added stochasticity helps or hurts.

5. **Clarify the OU process implementation.** State explicitly whether the noise process is per-grid-cell and independent across spatial locations, or whether spatial correlations are maintained.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>