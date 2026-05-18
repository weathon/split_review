Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper introduces ELBERT (Equal Long-term Benefit Rate), a fairness notion for sequential decision-making in MDPs that measures group well-being as the ratio of cumulative supply to cumulative demand, thereby accounting for varying temporal importance that prior step-wise-sum metrics miss. The paper also proposes ELBERT-PO, which reduces the policy gradient of this ratio-based objective to standard policy gradients via a fairness-aware advantage function, enabling direct use of PPO for bias mitigation. Experiments on three environments (lending, infectious disease control, attention allocation) show ELBERT-PO achieves low bias while maintaining high reward.

## Strengths

1. **Identifies a genuine limitation in prior long-term fairness metrics.** The paper clearly demonstrates (Figure 1, Section 1) that summing step-wise acceptance rates or cumulative group rewards yields zero bias in a scenario where one group receives a 100/101 overall acceptance rate while the other receives only 1/101. By defining Long-term Benefit Rate as a ratio of cumulative supply to cumulative demand, ELBERT captures this disparity that prior metrics miss. This is the paper's core conceptual contribution.

2. **Provides a unifying framework for existing long-term fairness criteria.** Section 5.1 shows that the fairness metrics used in three different prior works (Yu et al., 2022; D'Amour et al., 2020; Atwood et al., 2019) are all special cases of ELBERT through appropriate choice of supply and demand functions. This unification is valuable for the community.

3. **Consistent empirical superiority across diverse environments.** In all three environments (Figure 3), ELBERT-PO achieves the lowest bias among baselines while maintaining competitive reward. In lending, it reduces bias by 87.5% vs. G-PPO and >75% vs. R-PPO and A-PPO. In the multi-group allocation task, it achieves both the lowest bias and highest reward.

4. **Addresses the multi-group non-smoothness challenge.** Section 3.3 identifies that using max/min over multiple groups causes non-smooth gradients and proposes a smooth surrogate that considers all groups. This is a practical improvement over naively optimizing the max-min gap.

5. **Ablation study on the bias-reward trade-off.** Figure 4 shows the effect of varying α, demonstrating that larger α reduces bias (with diminishing returns) and that lower bias does not necessarily hurt reward.

## Weaknesses

### Fatal
None.

### Major

1. **Baselines do not directly optimize the same ratio objective, weakening the experimental comparison.** The paper compares ELBERT-PO against A-PPO (per-step bias regularization), G-PPO (fairness-agnostic), and R-PPO (heuristic reward shaping with cumulative bias penalty). None of these baselines directly optimize the same cumulative supply/demand ratio. While R-PPO uses the cumulative bias signal Δ_t in its reward shaping, it does so heuristically rather than through direct policy gradient on the ratio objective. The most natural competitor—a constrained MDP/Lagrangian approach that treats the ELBERT ratio constraint explicitly—is absent. As a result, the experiments demonstrate that direct optimization of the ratio works, but do not fully answer whether the advantage comes from the ELBERT notion itself or simply from the optimization approach. This does not invalidate the paper's contribution, but it limits the strength of the empirical claims.

2. **No statistical significance or variance reporting.** The paper reports point estimates (e.g., "bias of 0.02") without error bars, confidence intervals, or multi-seed analysis in the text. Figure 3 shows learning curves, but it is unclear how many runs were conducted and whether the observed differences are reliable. Without this, the reader cannot assess the stability of the results or whether the reported improvements are statistically meaningful.

### Minor

1. **Characterization of prior work may be imprecise.** The paper interprets prior metrics (Yin et al., 2023; Chi et al., 2021; Wen et al., 2021) as using per-step *acceptance rates* (proportions) to compute cumulative fairness. The critic raises a valid question: if prior work instead defines group benefit as per-step *counts* of acceptances, then the cumulative difference in the Figure 1 example would be (0+100) − (0+1) = 99 (non-zero), not zero. The paper uses "e.g." (Section 1) which signals the interpretation is illustrative, but the strength of the motivating example depends on the interpretation being a faithful characterization. The paper would benefit from explicit quotations or reproductions of the relevant definitions from those works to justify this interpretation.

2. **Gradient derivation novelty is overstated.** The paper frames computing ∇_π b(π) as a challenge, claiming it "was previously unclear" how to do this. However, Propositions 3.1 and 3.2 follow directly from the chain rule and the policy gradient theorem applied to auxiliary reward functions S_g and D_g. The reduction is useful—it enables off-the-shelf PPO—but it is a straightforward application of existing tools rather than a deep technical result. The paper's value lies more in the ELBERT fairness notion and the observation that it can be optimized with standard methods, not in a difficult gradient derivation.

3. **Environment modifications are not described.** The paper states (Section 5.1) that it modifies the infectious disease and attention allocation environments "to be more challenging" but provides no details on what was changed or why. This makes it difficult for readers to assess whether the modifications inadvertently advantage ELBERT-PO or to replicate the experiments.

4. **No discussion of estimator variance or training stability.** The quantities η_g^S(π) and η_g^D(π) appear in the denominator and as weights in the fairness-aware advantage function. Their estimates can be noisy, especially early in training. The paper does not discuss whether any variance reduction techniques are used or how this noise affects training stability.

### Trivial
None.

## Nice-to-Haves

- Adding a constrained MDP or Lagrangian baseline that directly optimizes the ELBERT ratio constraint would significantly strengthen the experimental section.
- Reporting results with multiple random seeds and error bars would improve confidence in the empirical claims.
- An analysis of sensitivity to the softmax/min temperature hyperparameter in the multi-group setting would be informative.
- A discussion of estimator variance for η_g^S and η_g^D and any variance reduction techniques would be helpful for practitioners.

## Removed Points

These points from the reviews are removed per the filtering guidelines:

1. **"SD-MDP is a framing device, not a new formalism"** (Harsh Critic) — This is an observation, not a weakness. The paper does not claim SD-MDP as a major technical extension — it is clearly presented as a way to formalize supply and demand for fairness. This does not weaken the paper.

2. **"Multi-group extension using softmax/min is standard"** (Harsh Critic) — The paper's contribution is not in claiming novelty for softmax/min as an operator, but in identifying the non-smoothness problem with max/min in the fairness context and proposing a pragmatic solution. Calling this "standard" without evidence of prior use in this specific fairness context is an assertion, not a verified weakness.

3. **"Missing appendix results on original environments"** (Harsh Critic) — The paper states these results are in the appendix. Appendix content is stripped by the parser and is not missing from the original submission. Per the hard rules, this criticism is removed.

4. **"The paper does not show original environment results as a sanity check"** (Harsh Critic) — Same as above: these are in the appendix.

## Novel Insights

The harsh critic and strength finder converge on the same assessment from different directions: the paper's genuine contribution is the ELBERT fairness notion itself — the idea that cumulative supply/demand ratios capture temporal importance in a way that step-wise sums cannot. The gradient reduction, while practically useful, is mechanically straightforward. The main unresolved question is whether the experimental evidence is strong enough. The critic correctly identifies that the baselines are mismatched to the objective (in different ways), but the paper is not making a claim about "our optimizer beats your optimizer on your metric" — it's showing that a principled approach to the ELBERT objective outperforms heuristic prior methods on the same environments. A constrained-MDP baseline would clarify whether the advantage is from the notion or the optimization, but the existing results are still informative: ELBERT-PO works, works consistently, and does not sacrifice reward.

## Suggestions

1. **Add a constrained-MDP baseline.** The most impactful improvement would be a Lagrangian or primal-dual method that treats the ELBERT ratio constraint directly. This would show whether the advantage of ELBERT-PO comes from the ELBERT notion itself or from the specific optimization approach.

2. **Clarify the characterization of prior work.** Provide direct quotations or reproductions of the fairness definitions from Yin et al. (2023), Chi et al. (2021), and Wen et al. (2021) to justify the per-step-rate interpretation used in the motivating example.

3. **Report multi-seed results with error bars.** Add standard deviations or confidence intervals to all reported metrics to establish statistical reliability.

4. **Tone down the novelty claim around the gradient.** Acknowledge explicitly that the reduction is an application of the chain rule and policy gradient theorem to auxiliary reward functions. The practical value is in enabling PPO, not in deriving a difficult gradient.

5. **Describe the environment modifications.** A brief paragraph explaining what was changed in the infectious disease and attention allocation environments and why would aid reproducibility and assessment.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>