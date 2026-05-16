Now I have all the information I need. Let me construct the final consolidated review.

## Summary

This paper proposes an online change-point detection method for black-box LLMs. The method features: (1) a CUSUM-type detection statistic based on entropy and Gini coefficient computed from tokenized response distributions (accessible without model internals), and (2) a UCB-based adaptive prompt selection strategy to identify change-sensitive prompts under a query budget. The method is evaluated on synthetic data (watermarking, model version swaps) and on real-world LLM API interactions spanning June–August 2024.

## Strengths

- **Novel combination of CUSUM with entropy/Gini metrics for black-box LLM detection**: The detection statistic is derived from tokenized responses only — no access to model parameters or log-probabilities — directly addressing the core challenge of black-box online detection (Section 3.1, Eqs. 1–2). This is well-motivated by the practical reality that many deployed LLMs expose only text output.

- **Adaptive prompt selection via UCB**: The UCB-based selection strategy dynamically identifies change-sensitive prompts under a query budget (Section 3.3, Algorithm 3). The ADD-ARL comparison (Figure 6b) shows that adaptive selection outperforms both random selection and individual a priori prompts, and the UCB score trajectories (Figure 6a) visually confirm convergence to sensitive prompts after a change.

- **Real-world validation on LLM APIs**: The method successfully detects a confirmed official update to Mistral AI's API on July 24, 2024 (Figure 7) using only daily queries. The detections of unconfirmed changes in GPT-4 Turbo and Jamba (Figure 8) provide plausible evidence of unreported model updates, which may be of independent interest to the community.

- **Unified normalization across heterogeneous metrics**: The paper normalizes all four metrics (FTE, FTG, NTE, NTG) to zero mean and unit variance using pre-change data, enabling a single drift parameter \(d\) and threshold \(b\) (Section 3.2). This is a practical design choice validated by the consistent behavior of the statistics in experiments.

## Weaknesses

### Major

- **No baseline comparisons for the detection statistic itself**: The paper evaluates its method in isolation. For the synthetic watermark and version-change experiments (Figures 3, 4, 5), only the proposed statistics are shown — no comparison against any alternative detection statistic (e.g., tracking mean response length, surrogate perplexity via a fixed tokenizer, or simpler variants using only one metric). The ADD-ARL comparison in Figure 6b compares only different prompt selection strategies (adaptive vs. random vs. individual), not different detection statistics. Since this is a new-method paper, the central claim that the entropy+Gini CUSUM statistic is effective cannot be properly assessed without baselines. Adding, at minimum, a comparison against using only first-token entropy or only first-token Gini would address this.

- **Insufficient statistical rigor in synthetic experiments**: Figures 3, 4, and 5 show single runs of the detection process with no confidence intervals, standard deviations, or replication results. Only the ADD-ARL comparison (Figure 6b) uses 20 repeated experiments. Synthetic experiments use one prompt (prompt 12) with no indication of how performance varies across different prompts, random seeds, or watermark strengths. Parameters \(C=20\), \(N=20\), and \(d=0.5\) are fixed with no sensitivity analysis or justification. This prevents judging the method's robustness or enabling meaningful comparison to future work.

- **Real-world detections lack false-positive rate analysis**: The detection procedure monitors four statistics per prompt across multiple prompts simultaneously, yet no correction for multiple testing is applied and no false-alarm rate is reported for the real data. The two "unconfirmed changes" (GPT-4 Turbo, Jamba) are presented as "strong evidence" without any statistical foundation — the same detection spikes could arise from the many parallel tests being tracked. No permutation test, bootstrap, or control-period analysis is provided to estimate whether these spikes exceed chance levels.

### Minor

- **Heuristic approximation of NTE/NTG ignores token-order information**: The approximation (Section 3.2) merges tokens across positions into a pooled empirical distribution \(\hat{P}_{1:N}\), which marginalizes across positions and discards token-order information. The paper notes this differs from the true joint distribution but does not discuss the limitation that changes affecting only token co-occurrence patterns (e.g., certain sequence-level watermarks) could be missed. A brief acknowledgment and comparison against a position-aware alternative (e.g., averaging per-position metrics) would strengthen the presentation.

- **UCB reward non-stationarity not discussed**: The reward \(U(t;x) = W(t;x) - W(t-1;x)\) is inherently non-stationary — its mean is near zero pre-change and shifts post-change. UCB's theoretical guarantees assume stationary rewards; the paper does not address this mismatch or provide justification for why the algorithm still works in practice.

- **No analysis of computational cost**: The method queries \(K\) prompts with \(C\) responses each per round, and each response is tokenized and truncated to \(N\) tokens. Even a brief discussion of the cumulative query cost (e.g., total tokens processed, API call count) would help practitioners assess practicality.

### Trivial

- **The "individual prompt" baseline in Figure 6b selects a single prompt a priori rather than the best prompt in hindsight**, which weakens the comparison and somewhat overstates the benefit of adaptivity. This does not affect the main conclusion (adaptive > random) but is worth clarifying.

## Nice-to-Haves

- A sensitivity analysis for \(d\), \(C\), and \(N\) in the synthetic experiments would strengthen the evaluation.
- Reporting synthetic experiments over multiple runs (e.g., 50+) with standard deviations for ADD and ARL.
- Computing an empirical false-alarm rate for real data, e.g., by applying the detector to a known-stable time window.
- Including an oracle baseline that always selects the most sensitive prompt (identified from pre-change exploration) in the ADD-ARL comparison.
- Clarifying how many rounds of interaction occur per day in the real-world API experiments.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Table 1 is missing"** — The paper references "Table 1" for the prompt list, but this table was almost certainly in the appendix, which the parser strips. The rules state to remove weaknesses about missing appendix content, as it exists in the original submission.
- **"The prompts themselves are not listed in the main text"** — Same as above: this is an artifact of the parser stripping the appendix/table.
- **"The paper does not specify how prompts were selected initially"** — The paper does specify on line 154-156: "Specially at time 1, we select all prompts for initialization." This is visible in the parsed text.

## Novel Insights

The harsh reviewer makes an insightful observation that the pooled-token approximation for NTE/NTG discards token-order information and could miss changes that only affect token *sequences*. This is a genuinely useful critique that could guide the authors toward a more rigorous analysis of when their approximation is valid versus when it may fail. The observation about UCB reward non-stationarity is also a non-trivial point — the paper applies a standard bandit algorithm to a fundamentally non-stationary reward signal without addressing the theoretical gap, which is worth examining.

## Suggestions

1. **Add baselines**: Compare your detection statistic against at least (a) a simple baseline like mean response length, (b) a variant using only first-token entropy, and (c) a variant using only first-token Gini. Report ADD-ARL trade-offs for each.
2. **Report replication**: Run synthetic experiments across multiple seeds/prompts and report standard deviations or confidence intervals for ADD and ARL.
3. **Validate real-world false alarms**: Apply the detector to a known-stable period and report the empirical false-alarm rate. Use a permutation test to assess whether the Mistral detection spike exceeds chance.
4. **Acknowledge the pooled-token limitation** explicitly and discuss whether token-order information could be material for certain types of changes.
5. **Add a brief computational cost discussion** — total API calls, token counts processed, or wall-clock time per round.

## Score and Decision

The paper tackles a well-motivated problem with a plausible approach, and the real-world detection of the confirmed Mistral update is a compelling result. However, the evaluation is currently a **demonstration** rather than a **validation**. The absence of baseline comparisons for the detection statistic, single-run synthetic results without confidence intervals, and lack of false-positive rate analysis for real-world data mean the evidence does not yet support the claimed effectiveness relative to alternatives. The core ideas are interesting, and the issues are fixable, but in its current form the evaluation is too thin for acceptance at a research venue.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>