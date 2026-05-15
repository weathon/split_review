Now I have thoroughly verified all claims. Let me construct the final review.

---

## Summary

This paper proposes the first on-the-fly adaptation framework for speculative decoding in LLMs, comprising two components: (1) runtime optimization of the speculation window size (γ) via a latency-aware objective function and an online accuracy estimator, and (2) prompt-feature-based draft model selection using a linear model. The approach is evaluated across four LLMs, three GPU types, and four task categories, reporting 3.55–16.48% speedups over standard speculative decoding and 1.2–3.4× over autoregressive decoding.

## Strengths

- **Novel problem framing and first exploration of runtime adaptation for speculative decoding.** The paper correctly identifies that static γ and fixed draft models are suboptimal across varying prompts, tasks, and hardware. To my knowledge, no prior work has attempted to adapt both γ and the draft model entirely at inference time without heavy offline training. This is a legitimate gap and the paper's core direction is well-motivated.

- **Diverse experimental coverage across models, hardware, and tasks.** The evaluation spans four target models (LLaMA-70B, OPT-13B, BLOOM-7B, Dolly-12B), three GPU types (A100, RTX 4090, L40S), and four datasets (HumanEval, XSum, GSM8K, Alpaca). This breadth lends credibility to the generality of the approach.

- **Comparison of multiple adaptation strategies.** The paper explores four methods (online optimization, FSM, cache-enabled FSM, RL) and provides comparative throughput/acceptance-rate analysis in Figure 3. This gives practical insight into the trade-offs involved (e.g., RL yields high acceptance rate but lower throughput due to conservative γ choices).

- **Favorable comparison to SpecDec++ despite zero training cost.** Table 4 shows that the proposed method (even without draft model selection) achieves a 5.7% average latency improvement over SpecDec++ on two model–hardware configurations, while SpecDec++ requires 900+ GPU-hours for training data collection and model training. This is a meaningful result.

## Weaknesses

### Major

1. **"Drop-in / no offline calibration" claim is overstated for the draft model selection component.** The paper repeatedly asserts that the solution needs "no offline benchmarking or training" (Abstract, Introduction, Conclusion). However, Section 5 (lines 227–231) explicitly describes running speculative decoding on `r` linearly independent prompts *before deployment* to estimate the linear model parameters **Z**_c via ordinary least squares (Equation 10). This is a form of offline calibration/initialization. While it is far lighter than SpecDec++'s full training (r prompts vs. thousands of GPU-hours), the paper should acknowledge this upfront rather than claiming the entire system is "drop-in" with "no ahead-of-time preparation." The number `r` and how to select linearly independent prompts are also never specified, making it impossible to assess the overhead of this step.

2. **The single-token accuracy estimator (Equation 2) is biased and its properties are unanalyzed.** The estimator is defined as ΣV / (ΣV + Σ𝟙(V < γ)), where V is the number of accepted tokens in a window. The true per-token accuracy is ΣV / Σγ. Since each rejected window contributes only 1 (not γ - V) to the denominator, the estimate is systematically inflated in low-accuracy regimes. The paper provides no analysis of the direction or magnitude of this bias, nor does it justify why this particular form is appropriate for the objective in Definition 1. Because the entire online window-size optimization (Section 4.1) depends on this estimate, its unchecked bias is a concrete concern — though the empirical speedups suggest the algorithm remains functional despite it. The authors should characterize the bias, justify the heuristic, or switch to an unbiased estimate.

3. **Ablation between the two adaptation components is missing.** The headline speedup range (3.55–16.48%) comes from the full system with draft model selection (Table 3). Table 2 reports adaptive window size only, with different speedup ranges. But there is no direct ablation: what does the system achieve with adaptive window size alone vs. with draft model selection alone vs. with both? Without this, it is impossible to determine which component drives the gains and whether the added complexity of draft model selection (which requires offline calibration) is worthwhile.

### Minor

4. **No variance or confidence intervals reported for any throughput comparison.** The paper reports only point estimates (e.g., "7.69% improvement," "5.7% average improvement"). With only 25 calibration prompts and unspecified evaluation set sizes, these numbers could be within noise. Error bars or bootstrapped confidence intervals are standard practice for speedup comparisons and should be provided.

5. **The "9–18% increase in speedups" claim in Section 3 (line 100) is unsupported.** The paper states this as a motivation for per-prompt adaptation but provides no citation or experiment backing it. This is a significant number that frames the entire paper's motivation, yet it appears as an anecdotal claim.

6. **Several methods are described too qualitatively for reproducibility.** The FSM, cache-enabled FSM, and RL methods (Section 4.2) are described in prose only. For the RL method: no state space, action space, reward function, or training details are given. The FSM and cache methods lack clear algorithmic specification. These are presented as valid alternatives in the comparison (Figure 3) but cannot be reproduced or assessed for correctness.

7. **Theorem 2's condition (Equation 7) is underspecified for practical use.** The condition Δn > (Δc / Δρ)L involves Δn and Δρ, whose computation requires knowing the optimal γ (which is what the optimization is trying to find). The paper states these quantities "can also be determined" from α, but the circular dependency on the unknown optimal γ is not resolved. A worked example showing how to evaluate this condition from the linear model's α estimate would clarify the procedure.

8. **SpecDec++ comparison (Table 4) is limited to only two model–hardware pairs.** While this is understandable given the training cost of SpecDec++, the "5.7% average improvement" claim rests on just two data points and should be qualified accordingly.

### Trivial

- The algorithm description in Section 4.1 states that a_q, b_p(γ) are "derived by observing the most recent steps" without specifying how many steps or any decay factor.
- The feature vector dimension r in the linear model (Equation 8) is never specified, nor is the procedure for selecting r linearly independent prompts.

## Nice-to-Haves

- A time-series visualization showing how γ evolves during a single generation for different methods (online, FSM, RL) would help illustrate adaptation behavior.
- A cost/overhead breakdown: what fraction of total inference time is consumed by the adaptation logic (estimator updates, integer optimization, feature extraction)?
- Sensitivity analysis for the cap Acc_max and the moving-average window size for latency estimates.

## Removed Points

The following points from the harsh review are removed with justification:

- **"Equation 2 estimate is undefined under repeated partial acceptances"** — The estimator is well-defined for any sequence of windows; it simply has a bias. Removed as overstated.
- **"Theorem 1 is a tautological rearrangement of definitions"** — While the theorem is simple, it provides an explicit functional form linking throughput to key parameters. This is standard for a systems paper's theoretical framing. Removed as overly harsh.
- **"SPS 4.5–30.8% vs 3.55–16.48% is a discrepancy"** — These numbers come from different experimental setups (Table 2: adaptive window only; Table 3: full system with draft model selection). Not a contradiction. Removed as factually incorrect.
- **"Background section is cut off / incomplete"** — Parser artifact (reference to appendix content that the parser stripped). Removed per hard rules.
- **"No code or configuration provided"** — Reproducibility concern about missing artifacts. Removed per hard rules (implementations impractical to include).
- **"Hardware setup introduces variable communication overhead not accounted for"** — The paper explicitly addresses this (lines 256–257), explaining the two-GPU setup for 70B models and single-GPU for others. The criticism is answered in the paper. Removed.
- **The strength-finder's strength #2 about "significant and consistent speed improvements" and strength #3 about "theoretical foundation"** — Partially conflict with verified weaknesses (biased estimator, missing ablation). The improvement numbers are real but the theoretical foundation has gaps. Softened by noting the context.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a fundamentally new observation about the paper that the authors have not already identified.

## Suggestions

1. Qualify the "drop-in / no offline calibration" claim to accurately reflect the r-prompt initialization required by the draft model selection component, or separate the two contributions so the adaptive window size component is truly drop-in.
2. Analyze the bias of the accuracy estimator (Equation 2) — either theoretically through a derivation comparing expected values, or empirically through simulation — and discuss whether it affects the optimal γ selection.
3. Add an ablation study isolating three conditions: adaptive window only, draft model selection only, and both combined.
4. Report standard errors, confidence intervals, or per-prompt throughput distributions for all main speedup numbers.
5. Provide pseudocode for the online window-size optimization algorithm specifying: the recency window length, decay factor (if any), and how the integer optimization in Definition 1 is solved at each step.
6. Add a worked concrete example showing how Theorem 2's condition is evaluated in practice from the linear model's output.
7. Either remove or substantiate the "9–18% increase" claim in Section 3.

## Score and Decision

This paper tackles a genuinely novel and practically important problem — runtime adaptation of speculative decoding parameters without heavy training. The empirical results across diverse settings indicate the approach works, and the comparison to SpecDec++ is impressive given the zero-training advantage. However, the paper is weakened by an overclaimed "drop-in" characterization (the draft model selection component requires offline calibration), an unanalyzed biased accuracy estimator that the core optimization depends on, missing ablations between the two adaptation components, and a lack of statistical rigor. These are fixable issues, and the core contribution remains valuable.

**Score: 6.0**

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>