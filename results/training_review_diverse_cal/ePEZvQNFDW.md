Now I have all the information needed to verify reviewer claims against the paper. Let me construct the final consolidated review.

---

## Summary

This paper proposes Continuous Ensemble Forecasting, a diffusion-based method for ensemble weather forecasting that uses correlated (or fixed) noise across lead times to generate temporally consistent trajectories without autoregressive rollout. The core idea is that a fixed noise sample, run through a lead-time-conditioned probability flow ODE, yields a deterministic map that can be evaluated at arbitrary lead times in parallel. The paper also introduces ARCI (Autoregressive Rollouts with Continuous Interpolation), which combines a few coarse autoregressive steps (e.g., 24h) with continuous interpolation of intermediate timesteps to produce high-temporal-resolution forecasts (e.g., 1h) without the error accumulation that plagues purely autoregressive high-resolution models. Experiments on WeatherBench at 5.625° resolution show that ARCI achieves competitive RMSE/CRPS and produces 1h-resolution forecasts whose accuracy matches that of a 24h-step autoregressive model, while a naive 1h-step autoregressive model degrades severely.

---

## Strengths

1. **Novel mechanism for temporal consistency via correlated noise.** The central technical insight — that freezing or correlating the driving noise across lead times yields continuous trajectories from a model trained only on time marginals — is clearly articulated (Section 4, Algorithm 1) and experimentally supported. Figure 5 shows that fixed noise (ρ=0) yields a mean temporal difference much closer to data than uncorrelated noise (ρ→∞), and autocorrelated noise (ρ=ln10) further corrects a lead-time-dependent bias. This is a principled alternative to multi-step training objectives.

2. **ARCI achieves high temporal resolution without accuracy loss (Figure 6).** The most compelling evidence in the paper: ARCI-24/1h matches the RMSE/CRPS of AR-24h at every lead time up to 10 days at 1h resolution, while a purely autoregressive AR-1h model degrades rapidly. This directly demonstrates the practical value of the hybrid approach and fulfills the paper's central claim.

3. **Computational efficiency gain.** A 10-day 6h-resolution forecast takes 8s per member for ARCI-24/6h vs. 32s for AR-6h (Section 5, "Models"), because continuous timesteps are parallelized across lead times. The paper is transparent about the fact that ODE sampling itself remains sequential.

4. **Generalization to unseen lead times.** ARCI-24/2h* (trained only on 2h steps) produces 1h forecasts with nearly identical skill to ARCI-24/1h (trained on every 1h step). This demonstrates that the lead-time conditioning extrapolates beyond the training grid — a practically important property.

5. **Clear mathematical motivation.** Section 4.1 and Figure 2 formalize the connection between the latent noise space and the space of solution functions, providing a principled justification for why correlated noise can sample from the joint trajectory distribution. The discussion of conditional determinism as a limitation (Section 4.2) and the autocorrelated noise extension are thoughtful.

---

## Weaknesses

### Major

1. **Score network architecture is not described.** The paper refers to $S_\theta$ as "the neural network" throughout but never specifies its architecture — whether it is a U-Net, a vision transformer, a graph network, or something else. This omission is significant for a methods paper in a field where backbone choice heavily affects performance. Readers cannot tell whether the results are attributable to the proposed algorithm or to the architectural backbone. Code release is promised, but the paper itself should contain at minimum a description of the architectural family, number of parameters, and key design choices. *Verification: grep for "architecture", "U-Net", "transformer", "graph network" in the paper body yields no description of the score network's structure beyond generic mentions of Fourier embeddings and conditioning.*

2. **No uncertainty quantification on comparisons.** The paper reports point estimates of RMSE, CRPS, and SSR without error bars, confidence intervals, or bootstrap estimates. This is acknowledged in the Limitations ("due to computational limitations, we were not able to retrain our models several times and as such do not report error bars"), but the acknowledgement does not fix the problem. The differences between ARCI-24/6h and AR-24h in Table 1 are small and systematic (AR-24h is consistently better: e.g., z500 at 5 days: 544.2 vs. 560.9 RMSE), so the claim that ARCI "matches" AR-24h is softened but not disproven. However, several claims (e.g., "ARCI-24+6h outperforms all models at 6h resolution") are stated as definitive without any sense of variability. Bootstrapping over test-set initialization times would be feasible and would substantially strengthen credibility.

### Minor

1. **Temporal consistency evaluation is narrow.** The only metric used is the mean temporal difference $\Delta X = |X(t)-X(t-1)|$, which measures the average magnitude of step-to-step changes. While this is a reasonable first-order check of continuity, it does not assess whether the temporal evolution is dynamically plausible — e.g., whether two-point temporal correlations, power spectra, or advection patterns match those of real weather. The paper's claim that fixed-noise trajectories are "temporally consistent" rests primarily on this single metric. The paper acknowledges the bias (ρ=0 trajectories become smoother than data at longer lead times) and proposes autocorrelated noise as a fix, but does not evaluate whether the corrected trajectories are physically realistic beyond the ΔX measure. Expanding the evaluation to include temporal correlation functions or a case study of evolving features would strengthen the core claim.

2. **"Completely in parallel, with no autoregressive steps" is potentially misleading without immediate clarification.** The abstract and introduction emphasize parallel sampling with no autoregressive steps. While this refers to lead-time rollout (which is indeed parallelized), the ODE solver itself is sequential. The Limitations section clarifies this, but a reader skimming the abstract could overestimate the speedup. A brief upfront clarification (e.g., "no autoregressive rollout across lead times") would improve precision. This does not affect the technical contribution but is a presentation concern.

3. **Missing linear interpolation baseline for the 1h-resolution experiment.** The paper states (line 333, truncated): "An alternative to directly producing forecasts at a fine temporal resolution would be to linearly interpolate the forecasts sampled using an autoregressive model." This sentence appears cut off, but no such baseline is actually reported. Comparing ARCI-24/1h against linear interpolation of AR-24h's 24h-resolution forecasts would isolate the benefit of learned continuous forecasting over naive interpolation and strengthen the claim that ARCI adds value.

4. **"Outperforms all models at 6h resolution" (Section 4.1) is ambiguous.** Reading Table 1, AR-24h (a 24h-resolution model) achieves better scores than ARCI-24/6h on most metrics. The text appears to mean "among models producing 6h-resolution output" but does not say so explicitly. Given that AR-24h is consistently better, the phrasing could confuse readers.

### Trivial

- The sentence at line 333 beginning "An alternative to directly producing forecasts..." appears truncated mid-sentence (parser artifact likely unrelated to the original submission, but the missing baseline is noted above as a substantive gap).
- The paper would benefit from adding the autocorrelated noise (Algorithm 2) results to the main quantitative table, since the analysis in Figure 5 shows it addresses a real deficiency of the fixed-noise method.

---

## Nice-to-Haves

- **Experimental comparison with DYffusion (Cachay et al., 2023).** DYffusion is cited and discussed (lines 103–105) as a related approach for temporally consistent diffusion-like forecasting. The paper notes DYffusion has been applied to climate modeling but not weather forecasting. While this provides context, a direct experimental comparison — even if limited to a subset of metrics — would strengthen the evaluation. The authors could justify its absence with a brief statement about differing data setups or computational cost.
- **Autocorrelated noise results (Algorithm 2) in the main quantitative table.** Since Figure 5 shows that autocorrelated noise (ρ=ln10) corrects a temporal bias, including its RMSE/CRPS/SSR alongside the fixed-noise results would clarify whether this correction has any cost in predictive skill.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Continuous" label used loosely.** *(Reason: Terminology nitpick. The model is conditioned on lead time and evaluated on a fine grid; the paper is clear about what "continuous" means operationally.)*
- **Graph-EFM comparison fairness / model capacity.** *(Reason: The paper retrains Graph-EFM on the exact same data setup. The reviewer's concern about capacity differences is speculative and unsupported by evidence in the criticism.)*
- **Figure 5 results "complicate the narrative."** *(Reason: The paper already acknowledges that ρ=0 trajectories are blurrier/smoother than data and discusses autocorrelated noise as the remedy. No contradiction is hidden.)*

---

## Novel Insights

The reviews surface a recurring observation that the paper's strength lies not in the pure continuous forecasting method (CI-6h, which degrades at long lead times) but in the ARCI hybrid, which pragmatically combines the best of both worlds: autoregressive rollout at coarse resolution for long-lead accuracy, and continuous interpolation at fine resolution for temporal detail. This hybrid framing is more honest and more impactful than the "no autoregressive steps" framing in the abstract, and the paper might benefit from leading with it. Neither reviewer fully articulates this, but the contrast between Table 1 (where CI-6h is clearly the weakest diffusion model) and Figure 6 (where ARCI-24/1h is the clear success story) tells this story clearly.

---

## Suggestions

1. Describe the score network architecture (architecture family, parameter count, input/output specifications, key hyperparameters) in the main text or in a clearly referenced section.
2. Add bootstrapped confidence intervals (over test-set initialization dates) to all quantitative comparisons. Even a single-seed model can be evaluated with temporal bootstrapping.
3. Add a linear-interpolation baseline to the 1h-resolution experiment: interpolate AR-24h's 24h-step forecasts to 1h resolution and compare against ARCI-24/1h.
4. Add the autocorrelated noise (Algorithm 2) results to the main quantitative table for completeness.
5. Clarify in the abstract/introduction that "no autoregressive steps" refers to lead-time rollout, not to ODE sampling steps.
6. Expand the temporal consistency evaluation with at least one additional metric (e.g., lag-1 temporal correlation, or a case study of a propagating weather feature).

---

## Score and Decision

**Originality:** The core idea — correlating noise across lead times to produce continuous trajectories from marginal-conditioned diffusion models — is creative and not present in prior weather forecasting diffusion work. The ARCI hybrid is a pragmatic extension.

**Importance:** High-temporal-resolution probabilistic weather forecasts are practically important for extreme weather decision-making. The paper addresses a real limitation of existing autoregressive diffusion models.

**Claims support:** Weakened by the absence of error bars and the narrow temporal consistency evaluation. The main qualitative result (Figure 6) is convincing, but several comparative claims are stated more strongly than the evidence warrants.

**Soundness:** The methodology is sound and well-motivated theoretically. The experimental setup is standard (WeatherBench). The main gap is reproducibility (missing architecture details).

**Clarity:** Generally well-written. Algorithms are clearly presented. Some claims could be more precisely scoped.

**Value:** Positive. The ARCI method is practically useful and the correlated-noise mechanism is likely transferable to other spatio-temporal forecasting domains.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>