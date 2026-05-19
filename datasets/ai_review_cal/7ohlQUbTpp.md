- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 6, 6, 5
Here is my final consolidated review.

---

## Summary

This paper proposes COLLAB, an inference-time alignment method that dynamically switches between multiple off-the-shelf LLMs at the token level. The switching is guided by an "implicit Q-function" that estimates the long-term utility of each token under each agent's policy w.r.t. a target reward. The paper provides a theoretical sub-optimality bound and presents experiments showing that COLLAB outperforms single-agent controlled decoding baselines (ARGS, TQ*) on average reward, GPT-4 win rate, diversity, and coherence.

## Strengths

- **Consistent empirical gains over strong single-agent baselines.** Across six evaluation setups (Figure 2), COLLAB achieves higher normalized average reward than individual agents using SoTA single-agent decoding (TQ*) and best-of-N sampling. The improvement is consistent across all reported setups, providing evidence that token-level multi-agent switching can improve alignment beyond what the best single agent achieves.

- **Ablation validates the role of agent diversity.** Figure 4a directly compares switching between similar (non-diverse) agents versus diverse agents. The diversity-based switching yields significantly higher average reward, providing causal evidence that the benefit comes from leveraging specialized models rather than just having multiple models.

- **Training-free and compatible with black-box agents.** The method works entirely at inference time using only next-token distributions from each agent, requiring no parameter updates or access to internal training rewards. This is a practical advantage for scenarios where model internals are proprietary or retraining is infeasible.

- **Multi-metric evaluation.** Beyond reward, the paper evaluates diversity and coherence (Figure 3), showing that alignment gains do not come at the cost of fluency or vocabulary diversity.

## Weaknesses

### Major

- **Underspecified Q-function estimation (core algorithmic step).** The algorithm's central operation (Algorithm 1, line 166) requires evaluating \(J_{\text{target}}^{\pi_i}(\mathbf{s}_t, z) = Q_{\text{target}}^{\pi_i}(\mathbf{s}_t, z) - \alpha\,\text{KL}(\pi_i\|\pi_{\text{ref}})\). The Q-function itself is defined as an expectation over full continuations under policy \(\pi_i\) (Equation 5). The paper provides no concrete method for computing or approximating this quantity in practice — no description of Monte Carlo rollouts, learned value functions, reward-model-based scoring, look-ahead horizon, or the number of rollouts per candidate token. The experimental section (line 190) specifies only \(\alpha=1\) and \(p=10\) top-p tokens. Without knowing how the Q-function is estimated, the algorithm is incompletely specified and the experiments cannot be reproduced. This is a significant methodological gap; the paper should clearly state the approximation used (or cite a specific technique from the controlled-decoding literature, e.g., Mudgal et al. 2024 or Chakraborty et al. 2024b).

- **Overclaimed theoretical interpretation.** Theorem 1 provides an upper bound on the sub-optimality of the multi-agent policy \(\pi_{\text{alg}}\) w.r.t. the optimal policy for the target reward: \(\Delta(\pi_{\text{alg}}) \leq \min_j [\delta_{*j} + \alpha\,\text{KL}(\pi_j\|\pi_{\text{ref}})] + \beta\,\text{KL}(\rho^{\pi^*}\|\rho_{\text{ref}})\). The paper claims (line 179) that this "guarantees that the performance … will improve over the best-performing policy" from the agent set. This does **not** follow from the bound. The bound upper-bounds sub-optimality relative to the (unavailable) optimal policy \(\pi^*\); it does not directly bound how \(\pi_{\text{alg}}\) compares to any individual agent \(\pi_j\) on the target reward. A direct comparison between \(\pi_{\text{alg}}\) and the best single agent would require additional analysis. The theoretical framing should be revised to accurately reflect what the bound actually shows.

- **Missing multi-agent baselines.** The paper compares COLLAB against single-agent controlled decoding (TQ*, ARGS) and best-of-N sampling. It does **not** compare against any existing multi-agent or collaborative decoding methods — e.g., collaborative decoding (Shen et al., 2024), FUDGE (Yang & Klein, 2021), proxy-tuning (Liu et al., 2024) — all of which are cited in the related work. Since the paper's contribution is explicitly a multi-agent method, the evaluation should include comparisons with other approaches that combine multiple models to demonstrate that the switching mechanism itself adds value beyond existing combination strategies.

- **No statistical uncertainty quantification.** The paper does not report standard deviations, confidence intervals, or results from multiple seeds/runs for any metric. Given the stochastic nature of language generation and evaluation, this makes it impossible to assess the reliability or significance of the reported improvements.

### Minor

- **Unclear mapping of the 71.89% win-tie rate claim.** The abstract reports a "71.89% GPT-4 based win-tie rate." Table 1 (which appears as an image) lists per-baseline win-tie percentages (e.g., 81.25%, 85.23%, 91.18%). It is unclear whether 71.89% is an aggregate average across baselines, a comparison against a specific baseline, or something else. The paper should state explicitly what this number refers to.

- **GPT-4 evaluation rubric not fully specified.** The paper states that GPT-4 rates responses "on relevance, accuracy, and insightfulness" (line 205) but does not provide the exact prompt or rating rubric used. For reproducibility, this should be included.

- **Incomplete specification of target reward model(s).** The paper defines the target reward function \(r_{\text{target}}\) abstractly (Section 3.1) and reports "average reward" as a metric, but does not specify which concrete reward model(s) are used as \(r_{\text{target}}\) in each evaluation setup. This makes it difficult to interpret the absolute reward values.

### Trivial

- None.

## Nice-to-Haves

- An ablation comparing different practical approximations of the Q-function (e.g., 1-step lookahead vs. full rollout, learned value function vs. reward-model scoring) would strengthen the paper and provide guidance to practitioners.
- Reporting computational cost (number of forward passes per token, total inference time relative to single-agent decoding) would help assess practicality.
- A comparison with an oracle that knows the best agent for each prompt would help calibrate the results by establishing an upper bound.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Figure 3 (coherence and diversity) is missing from the provided text."** — This is a parser artifact. The figure exists in the original submission as an image.
- **"Missing appendix, missing proofs in appendix"** — The parser strips appendix content from all extracted texts; these exist in the original submission.
- **Strength: "Theoretical sub-optimality bound revealing the key driver of performance"** — This strength conflicts with the verified weakness about overclaimed theoretical interpretation. The weakness is that the bound does not support the paper's central claim about improvement over single agents. Per the filtering rules, the weakness wins, so this strength is moved here.
- **"The bound is also vacuous if the best agent's reward differs significantly from the target reward"** — This is a generic concern about all bounds involving an unobserved gap; it is not a specific problem with the paper's analysis and is better captured by the already-retained weakness about overclaimed interpretation.
- **Various speculative criticisms about "confounders" and "proxy measurement"** — These are area-of-concern sweeps without concrete anchors in the paper, removed per the filtering discipline.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Specify the Q-function estimation method concretely.** State whether the expected future reward under each agent is approximated via full generation, truncated rollout, or a learned value function. Provide the number of samples, the look-ahead horizon, and the reward model(s) used. If the approach follows prior work (e.g., Mudgal et al. 2024), say so explicitly.
2. **Revise the theoretical claims.** Clarify that Theorem 1 bounds sub-optimality relative to the optimal policy, and remove the unsupported claim that the bound "guarantees improvement over the best-performing policy." Either provide a direct comparison or reframe the theory as an analysis of the algorithm's sub-optimality without overclaiming.
3. **Add multi-agent baselines.** Include comparisons with collaborative decoding (Shen et al., 2024) and proxy-tuning (Liu et al., 2024) to demonstrate the advantage of the Q-function-based switching mechanism over other multi-model combination strategies.
4. **Report error bars or multiple seeds.** Run experiments with at least 3 seeds and report means with standard deviations for all metrics.
5. **Clarify the 71.89% figure.** State explicitly which comparison(s) yield this number and whether it is an average or a single baseline comparison.
6. **Include the GPT-4 evaluation prompt and rubrics in the appendix**, along with the specific reward models used in each setup.
