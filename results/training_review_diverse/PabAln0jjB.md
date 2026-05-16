Here is my consolidated final review:

## Summary

This paper proposes NS-DPO (Non-Stationary Direct Preference Optimization), a method for fine-tuning LLMs on offline preference datasets where human preferences may drift over time. The core idea is to introduce an exponential discount factor γ into the DPO loss, down-weighting older datapoints and up-weighting more recent ones, derived from a Dynamic Bradley-Terry model. The paper provides a theoretical regret bound of \(\tilde{O}(d B_T^{1/2} n^{-1/4})\) for log-linear policies and validates the approach on synthetic data as well as three LLM benchmark datasets (NSGO, UltraFeedback, TVHH) under both sudden changepoint and gradual preference shifts.

## Strengths

- **Novel contribution: first offline non-stationary preference optimization algorithm for LLMs.** The paper is clearly the first to address preference drift in the offline preference optimization setting, as opposed to prior work (e.g., Carroll et al., 2024) that focuses on online settings. The Dynamic Bradley-Terry modeling perspective is well-motivated and cleanly derived. (Lines 29–33, 39–41)

- **Theoretical regret bound for non-stationary preferences.** Under standard assumptions (boundedness, feature coverage, temporal coverage, variation budget), Theorem 1 provides a regret bound of \(\tilde{O}(d B_T^{1/2} n^{-1/4})\) for the log-linear policy class. This matches the complexity of stationary noisy-preference optimization (Chowdhury et al., 2024) while explicitly accounting for drift, and is a non-trivial extension of existing analysis. (Lines 197–210)

- **Consistent empirical advantage across diverse drift scenarios.** NS-DPO outperforms stationary DPO and IPO by up to 20% in reward accuracy across multiple dataset types (synthetic, NSGO, UltraFeedback, TVHH), multiple drift types (sudden changepoint, gradual), and multiple drift strengths. Importantly, on stationary data without drift (\(\rho_{\text{diff}} \leq 0.7\)), NS-DPO matches DPO's performance, showing no downside to using the method. (Figures 3–7, lines 297–336)

- **Simple and practical extension.** NS-DPO introduces a single scalar hyperparameter γ into the DPO loss without requiring architectural changes, model retraining, or increased computational complexity. The synthetic γ-ablation shows robustness across γ ∈ [0.5, 0.9]. (Equation 9, lines 297–301)

- **Construction of reusable non-stationary benchmark datasets.** The paper creates three controlled temporal preference datasets from existing resources (GlobalOpinionQA, UltraFeedback, Helpful & Harmless) by switching reward models or interpolating preference vectors. These provide a testbed for future research on preference drift. (Lines 247–269)

## Weaknesses

### Fatal
None.

### Major
None. The core claims (novelty of the method, theoretical bound, empirical effectiveness) are all supported by the presented evidence.

### Minor

1. **LLM experiments lack reported variance and use few runs.** The synthetic experiments report results over 10 seeds with standard deviation shading. The LLM experiments, by contrast, report averages over only 3 runs with no standard deviations, confidence intervals, or per-seed plots shown (Figures 5–7 captions). Given the stochasticity of LoRA fine-tuning, the observed advantage of NS-DPO could partially reflect random variation. This does not invalidate the results — the pattern is consistent across many datasets and conditions — but it weakens the statistical claim. (Line 235 vs. Figure 5–7 captions)

2. **No sliding-window baseline in LLM experiments.** SW-DPO (sliding window DPO) is tested in the synthetic log-linear setting but not in the LLM experiments. A simple baseline that trains DPO only on the most recent k time steps (e.g., k = 20, 50) would test whether exponential weighting is strictly better than hard truncation in the LLM regime. SW-DPO already provides this comparison in synthetic experiments, so the gap is not large, but extending it to LLMs would strengthen the empirical story. (Lines 273–274)

3. **Theory–practice gap is not discussed.** The theoretical guarantees (Section 4) assume log-linear policies \(f_\theta(x,a) = \phi(x,a)^\top\theta\), while the LLM experiments use Llama-2-7b-chat-hf with LoRA — a deep neural network. The paper is transparent about the scope of the theory ("for log-linear policies," line 39) and tests the log-linear case separately in synthetic experiments, so no claim is violated. However, the paper would benefit from an explicit acknowledgment that extending the theoretical guarantees to neural policy classes is an open question, and that the LLM experiments are best viewed as empirical validation of the method rather than of the theory. (Lines 39, 132, 217, 222–224)

4. **Practical guidance for γ is heuristic and not ablated in LLM experiments.** The paper uses γ = 0.95 for most datasets and a formula \(\gamma = 1 - \frac{1}{100 - t_{cp}}\log(100)\) for TVHH, but no ablation on γ is performed for any LLM dataset. The synthetic γ-ablation suggests robustness (γ ∈ [0.5, 0.9]), but it is unclear whether this robustness transfers to the neural LLM setting. (Lines 273–274, 297–301)

5. **tDPO baseline is a weak comparator.** Appending the time step to the prompt is unlikely to help the model learn time-dependent preferences. The paper acknowledges that tDPO "does not show a significant difference from stationary DPO" (line 332), which undercuts its value as a baseline. A more informative baseline would encode time as a learned embedding or use a time-dependent reward head. This is a relatively minor point since the main comparison is against DPO and IPO, which are the standard methods.

### Trivial
- The paper's related work section (lines 27–37) is thorough but sequences citations in a somewhat dense block that could benefit from clearer thematic organization.

## Nice-to-Haves
- **Comparison to linearly decaying or other non-exponential weighting schemes.** Testing whether the form of the weight decay matters (exponential vs. linear vs. inverse) would help understand whether any time-aware weighting suffices or whether exponential weighting has specific advantages.
- **Discussion of computational overhead.** The paper mentions matching DPO's complexity in passing but could state explicitly that the only extra cost is storing and multiplying γ^{T-t_i} weights, which is negligible.
- **Data-driven γ selection.** Since \(B_T\) is unknown in practice, a brief discussion of adaptive γ selection (e.g., via change-point detection or validation on held-out recent data) would strengthen practical applicability.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"No comparison to linearly decaying weights"** — This is scope creep: it demands an entirely new experiment direction. Moved to Nice-to-Haves.
- **"No discussion of computational overhead"** — This is a wishlist item, not a weakness. Moved to Nice-to-Haves.
- **"tDPO is an odd choice; use learnable time embedding"** — The paper's choice of tDPO as a simple ICL baseline is defensible. Criticizing it as "odd" is a matter of taste. Moved to Minor item 5 above (reworded as an observation rather than a criticism).
- **"Missing minimax optimality discussion"** — The paper's regret bound is already compared to Chowdhury et al. (2024). Asking for lower bounds is a depth request beyond the paper's scope.
- **"No other metrics like KL penalty or human evaluation"** — Reward accuracy is the standard metric in this literature. Demand for additional metrics is scope creep for a method paper.
- **Strength Finder's claim that NS-DPO is "robust to the discount parameter"** — This is only shown in synthetic experiments, not in LLM experiments. However, the claim is still factually accurate as stated ("Synthetic experiments show..."), so it is kept as-is.

## Novel Insights

The reviews surface one genuinely interesting point beyond the paper's own contributions: the question of whether the exponential weighting scheme in NS-DPO yields qualitatively different behavior from hard truncation (sliding window / tail-DPO). In the synthetic experiments, NS-DPO converges faster than SW-DPO even when the latter uses the optimal window size (w = 33), because NS-DPO retains partial information from older datapoints rather than discarding them entirely. This suggests that exponential weighting is not merely a smooth approximation of truncation but may be strictly preferable when the drift is gradual or the optimal window size is unknown — a hypothesis worth testing directly in the LLM setting.

## Suggestions

1. **Add error bars to LLM experiments.** Run at least 5 seeds for each LLM condition and report means with standard deviations or bootstrapped confidence intervals. If compute is prohibitive, report the per-seed range.

2. **Add a tail-DPO (sliding window) baseline to at least one LLM experiment** (e.g., UltraFeedback at the most challenging change point), to directly test whether exponential weighting beats hard truncation in the neural setting.

3. **Add a brief "Limitations" paragraph** in the conclusion or after Section 4, explicitly stating that the theoretical guarantees assume log-linear policies and that extending them to neural networks is an open direction, while the empirical results suggest the method is practically effective.

4. **Include a γ-ablation on at least one LLM dataset** (e.g., TVHH gradual drift) to demonstrate that the robustness observed in synthetic experiments carries over to the neural regime.

## Score and Decision

This is a solid paper with a novel contribution, clean theoretical analysis, and broad empirical evaluation. The weaknesses are all minor and addressable: the empirical rigor can be improved with additional runs and a simple baseline, and the theory–practice gap can be resolved with a brief acknowledgment. No weakness threatens the core claims.

**Score: 7.0**

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>