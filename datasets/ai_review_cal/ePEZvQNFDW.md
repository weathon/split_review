- Decision: Accept
- Avg Score: 5.00
- Scores: 5, 5, 5, 5
Now I have verified all claims against the actual paper. Let me produce the final consolidated review.

---

## Summary

This paper proposes Continuous Ensemble Forecasting (CEF), a method for sampling temporally consistent ensemble trajectories from diffusion models by using a fixed (or autocorrelated) noise source across lead times, and ARCI, which combines CEF with autoregressive rollouts on long steps while using CEF for fine-resolution interpolation. The core idea — freezing the driving noise so the ODE solver becomes a deterministic map from noise+lead-time to weather state — is simple and principled. On WeatherBench 5.625°, ARCI-24/6h produces 10-day forecasts at 6h resolution that closely track the best autoregressive baseline (AR-24h) while offering parallelism across lead times that reduces sampling time from 32s (AR-6h) to 8s per member.

## Strengths

- **Parallel generation of consistent ensemble trajectories without autoregressive iteration across lead times.** Algorithm 1 shows that sampling all lead times and all ensemble members can be parallelized (the inner loops over $i$ and $k$ are independent), while standard autoregressive diffusion models (e.g., GenCast) must roll out sequentially. This is supported by the concrete efficiency numbers: ARCI-24/6h reduces per-member sampling from 32s (AR-6h) to 8s (Experiments, Models section).

- **Generalization to lead times not seen during training.** The ARCI-24/2h* model, trained only on lead times spaced 2h apart, produces 1h-resolution forecasts with nearly identical skill to ARCI-24/1h (trained on every 1h step). Figure 9 (Fig. \ref{fig:scores-1h-main}) shows that the continuous models "do not lose performance by increasing the temporal resolution," and the text explicitly demonstrates generalization to unseen lead times. This is a non-trivial and well-evidenced property.

- **Autocorrelated noise extension to address conditional determinism.** Section 4.2 identifies a genuine limitation of fixed-noise CEF (conditional determinism given a state at a fixed time) and proposes Ornstein-Uhlenbeck noise as a principled fix. Figure 7 (Fig. \ref{fig:temp-diff-main}) provides empirical validation: with fixed noise ($\rho=0$) the temporal difference stays close to the data, while uncorrelated noise deviates significantly.

- **Clear mathematical motivation.** Section 4.1 formalizes the identification of the latent noise space with the space of possible dynamical evolutions via a commutative diagram (Fig. \ref{fig:diagram}), providing a principled conceptual justification for why freezing noise yields temporally consistent trajectories.

## Weaknesses

### Fatal

None. The paper's core claims are supported with evidence, and no verified flaw invalidates them.

### Major

- **No uncertainty quantification for the main quantitative comparison, despite small differences.** Table 1 shows ARCI-24/6h vs. AR-24h at 10 days: z500 RMSE 765.6 vs. 750.6 (~2% difference), t850 RMSE 3.29 vs. 3.25 (~1.2% difference). The paper claims ARCI "matches the best overall model AR-24h in almost all scores," but without error bars (or any ensemble-derived variance estimate) the reader cannot determine whether these small differences reflect actual model performance or sampling noise from 50 ensemble members. The authors acknowledge this in the Limitations (line 354), but for a claim that the method *matches* a baseline, this is a significant evidential gap. It weakens the paper's strongest quantitative result.

### Minor

- **Temporal continuity analysis is performed on a small-scale auxiliary model, not the main setup.** The temporal difference analysis (Fig. \ref{fig:temp-diff-main}) uses a CI-1h model trained only to 24 hours, not the main ARCI-24/6h model used for 10-day forecasts. While this still validates the CEF method's continuity property on its own terms, the paper's headline claim about "realistic temporal evolution" over 10 days at 6h resolution is not directly validated. Additionally, the paper acknowledges that the temporal difference metric could partly reflect blurriness (caption of Fig. \ref{fig:temp-diff-main}), but does not disentangle this.

- **No linear interpolation baseline.** The paper mentions (line 333) that an alternative to direct fine-resolution forecasting is to linearly interpolate coarser AR-24h outputs, but does not implement this comparison. Including it would isolate whether the "continuous" aspect provides value beyond trivial post-processing of a strong autoregressive model.

- **Efficiency quantification is incomplete.** Timing for 6h-resolution sampling is reported (8s per member for ARCI-24/6h vs. 32s for AR-6h), but for the 1h-resolution experiments (Figure 5, Fig. \ref{fig:scores-1h-main}) — where the efficiency argument is equally important — no wall-clock times are given. The paper also does not report timing for AR-24h, making it hard to assess the efficiency trade-off against the strongest baseline.

### Trivial

- **The abstract's phrasing "completely in parallel" could be clarified.** The parallelization applies to the lead-time and ensemble-member loops in Algorithms 1 and 2, which is a genuine benefit over autoregressive rollouts. However, each individual ODE solve still requires sequential denoising steps, as the limitations section (line 353) correctly notes. The wording in the abstract and Algorithm 1's comment ("Can be done fully in parallel") could give a slightly misleading first impression, and a small clarification would help.

## Nice-to-Haves

- **DYffusion as a baseline or more detailed conceptual comparison.** DYffusion also provides forecasts at arbitrary temporal resolution and has been applied to spatio-temporal forecasting. Direct comparison on the same setup would strengthen the empirical differentiation. If not feasible, a more thorough discussion of the differences (stochastic interpolation + deterministic forecasting vs. diffusion + noise control) would help readers situate the contribution.

- **Short-lead-time results (1–2 days) in Table 1.** The paper states CI-6h "performs well on short-term forecasting" but only shows 5- and 10-day results. Including 1- or 2-day metrics would substantiate this claim and better illustrate the CI vs. ARCI trade-off.

- **Ensemble-derived variance estimates as a lightweight substitute for error bars.** Even without retraining models, reporting the spread across the 50 ensemble members for RMSE/CRPS would give some sense of the uncertainty in the comparison.

## Removed Points

The following criticisms from the inputs were evaluated against the paper and removed with justification:

1. **"Error in Algorithm 3 notation (x_{jN+M:jN})"** — The critic appears to have misread; the paper correctly uses `x_{jN{-}M{:}jN}`. The notation is sound. *Removed: factually incorrect.*

2. **"Mathematical motivation lacks rigor" / "without theoretical justification"** — The paper explicitly acknowledges this (line 180: "leave a formal analysis for future work") and is honest that empirical validation is the current support. The paper is an empirical methods paper, and this level of formalism is appropriate. *Removed: acknowledged scoping choice, not a weakness.*

3. **"Missing reproducibility details (sampling steps, ODE solver type, noise schedule)"** — Per hard rules, nitpicks about undisclosed hyperparameters are removed. The paper specifies it follows the Karras et al. (2022) formulation, which is standard. *Removed: rule‑mandated removal.*

4. **"SSR interpretation as a weakness"** — The paper mentions SSR<1 as an observation about all diffusion models, not as a flaw to fix. *Removed: not a weakness of the paper.*

5. **"Figure 3 is decorative rather than evidential"** — Qualitative examples are standard in ML papers for illustration. The paper does not claim this figure as core evidence. *Removed: overly harsh characterization of a standard practice.*

6. **"Missing short-term (1‑day) results in Table 1"** — The claim about CI-6h's short-term performance is still supported by the 5‑day vs. 10‑day comparison already in the table. Adding 1‑day results would be a nice addition but is not a missing essential. *Moved to Nice‑to‑Haves.*

7. **"AR‑24h would be even faster (~4s?)"** — This is speculation; the paper does not report AR‑24h timing. *Removed: speculative claim without paper support.*

8. **Strength: "Mathematical motivation... principled justification"** — While the motivation is clear and helpful, the strength finder somewhat overstates its rigor. However, the conceptual contribution (noise‑space/solution‑space identification) is genuine. *Retained in strengths but with appropriate framing.*

9. **Strengths about "important problem" / generic framing** — The strength finder did not produce any purely generic strengths; all four had specific anchors. No removal needed.

## Novel Insights

None beyond the paper's own contributions. The two reviewer inputs did not produce an insight that the paper itself does not already articulate.

## Suggestions

1. **Add uncertainty quantification** — Even a simple estimate (e.g., bootstrap variance across test set initializations, or ensemble-derived spread for RMSE) would substantially strengthen the claim that ARCI "matches" AR-24h.
2. **Validate temporal continuity on the main ARCI-24/6h model** — Show the temporal difference metric (or a complementary metric like spectral energy distribution) over the full 10‑day horizon.
3. **Include a linear interpolation baseline** — Report RMSE/CRPS for AR-24h outputs linearly interpolated to 6h or 1h resolution to isolate the benefit of the learned continuous forecasting.
4. **Report wall-clock times for the 1h-resolution experiments** to complete the efficiency story.
