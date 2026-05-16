Now I have a thorough understanding of the paper and all reviewer claims. Let me construct the consolidated review.

## Summary

This paper introduces ELBERT (Equal Long-term Benefit Rate), a fairness notion for sequential decision-making that defines long-term group well-being as the ratio of cumulative group supply to cumulative group demand. The key insight is that prior long-term fairness metrics (sum of step-wise bias or cumulative reward parity) fail to account for varying temporal importance—different time steps may have different demand, so equal acceptance rates at each step can mask severe overall disparity. The paper also derives the policy gradient of this ratio objective, showing it reduces to a linear combination of standard policy gradients, enabling off-the-shelf RL optimization (ELBERT-PO). Experiments on three sequential environments (lending, infectious disease control, attention allocation) demonstrate bias reduction.

## Strengths

1. **Identifies a genuine blind spot in prior long-term fairness metrics.** The loan example (Figure 1, Section 1) is clean and compelling: both the sum-of-stepwise-bias metric (Yin et al., 2023) and the cumulative-reward-difference metric (Chi et al., 2021; Wen et al., 2021) report zero bias despite a 100/101 vs. 1/101 acceptance rate gap. ELBERT's supply-demand ratio correctly captures this because it aggregates supply and demand separately before taking the ratio.

2. **Analytical reduction of the ratio objective's gradient to standard policy gradients.** Propositions 3.1 and 3.2 show that ∇J(π) can be expressed as a linear combination of ∇η(π), ∇η_g^S(π), and ∇η_g^D(π), yielding a fairness-aware advantage function (Equation 4) that plugs directly into PPO. This is nontrivial because the objective is not in standard cumulative-reward form, and the reduction is the key technical enabler of the method.

3. **Empirically demonstrated bias reduction with competitive utility across diverse environments.** In lending, ELBERT-PO achieves bias 0.02 (87.5% reduction over G-PPO, >75% over A-PPO and R-PPO). In infectious disease, it achieves the lowest bias (0.01) while matching G-PPO's reward. In multi-group attention allocation, it simultaneously achieves the lowest bias and highest reward among all methods (Figure 3).

4. **General framework covering multiple static fairness notions.** The paper shows that fairness criteria used in prior work (Yu et al., 2022; D'Amour et al., 2020; Atwood et al., 2019) are all special cases of ELBERT via appropriate supply/demand customization (Section 5.1), demonstrating generality beyond a single fairness definition.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core theoretical contribution (gradient reduction) is sound, and the empirical results, while missing variance estimates, show differences large enough that the main conclusions are unlikely to be overturned by noise.

### Minor

1. **No variance or multiple-seed reporting in main experimental results.** The bar charts in Figure 3 and learning curves in Figure 4 are presented as point estimates with no error bars, confidence intervals, or number of random seeds stated in the main text. In RL-based bias mitigation, run-to-run variance can be substantial, and the claim that ELBERT-PO "consistently achieves the lowest bias" would be strengthened by standard practice (e.g., ≥5 seeds with error bars). While the observed differences are large enough to be credible, this is an evidential gap that prevents assessing statistical reliability.

2. **The zero-demand edge case is not addressed.** The Long-term Benefit Rate η_g^S(π)/η_g^D(π) is undefined when η_g^D(π)=0 (e.g., no group member ever appears). Likewise, the gradient formula in Proposition 3.1 involves division by η_g^D(π) and η_g^D(π)². The paper does not discuss how this case is handled in practice (e.g., additive epsilon smoothing).

3. **The α ablation study (Section 5.3, Figure 4) is limited to one environment.** The effect of the bias coefficient α on the fairness-reward trade-off is only shown for the attention allocation environment. Reporting this ablation on at least one additional environment (e.g., lending) would strengthen understanding of the method's sensitivity to α.

4. **The experimental comparison does not include methods that optimize the prior long-term fairness metrics the paper argues are flawed.** The paper cites Wen et al. (2021), Chi et al. (2021), and Yin et al. (2023) as prior work whose metrics suffer from the false-sense-of-fairness problem. The baselines (A-PPO, G-PPO, R-PPO) follow the set from Yu et al. (2022) and are all heuristics or short-sighted regularizers. Including a baseline that directly optimizes for return parity or sum-of-stepwise-bias would more directly test the paper's claim that ELBERT's metric structure is the key improvement. That said, the main argument against prior metrics is conceptual (demonstrated analytically in Figure 1), so this is not a fatal omission.

### Trivial

- The caption text on line 129 appears to have supply and demand swapped ("group supply D_g... and group demand S_g...") relative to the notation used elsewhere in the paper. This should be checked and corrected.

## Nice-to-Haves

- **Broader experimental scope**: Adding a more complex environment (larger state space, >5 groups with demographics) would test scalability of the multi-group softmax extension.
- **Qualitative trajectory analysis**: The loan example in Figure 1 motivates the metric; a similar "before vs. after training" breakdown for one experimental environment would strengthen the connection between the metric behavior and actual policy outcomes.
- **Zero-demand handling**: A brief note on how the ratio is regularized when demand approaches zero would improve reproducibility.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Multi-group smooth approximation details not given in main paper"**: The exact form of the softmax/softmin approximation and its gradient are standard content for the appendix, which the parser strips from all papers. This is not a missing piece in the original submission.
- **"R-PPO hyperparameter ω not reported"**: This is a trivial implementation detail that is very likely specified in the appendix (which is stripped). A footnote number "2" in the baselines description points to supplementary material.
- **"Prior work cumulative reward definition needs clarification"**: The paper states its interpretation explicitly ("difference of cumulative group fairness rewards"). The reviewer's concern is about reader expectations, not an error in the paper.
- **Several of the harsh critic's section-by-section notes**: These are presentation-level suggestions (e.g., "a brief clarification would avoid confusion") that do not constitute substantive weaknesses.

## Novel Insights

The most insightful observation from the reviews is that the paper's core argument operates at two levels—conceptual (the metric is flawed) and empirical (our optimizer works well)—but the experiments only test the latter. A fully convincing evaluation would also show that optimizing a flawed metric leads to a policy that still exhibits hidden bias when measured by ELBERT, making the two levels mutually reinforcing. This is not a fatal gap (the conceptual argument stands on its own), but it identifies a natural extension for follow-up work.

## Suggestions

1. **Add error bars from multiple random seeds** to all bar charts and learning curves (Figures 3 and 4). Report the number of seeds and the metric used (e.g., mean ± std over 5 runs). This is the single highest-leverage improvement for the camera-ready version.

2. **Address the zero-demand case explicitly** in the main paper. A one-sentence note (e.g., "In practice we add a small ε to η_g^D to avoid division by zero") would resolve a nontrivial technical concern.

3. **Extend the α ablation** to at least the lending environment to show that the fairness-reward dynamics generalize beyond attention allocation.

## Score and Decision

This paper presents a clean, well-motivated fairness notion with a genuine technical contribution in the gradient derivation. The weaknesses are real but not structural—the core claims are supported, and the empirical gaps are addressable. The lack of variance reporting limits confidence in the precise numeric claims but does not undermine the clear directional results across three environments. Missing baselines from prior long-term metrics would strengthen the narrative but are not required given the paper's primary conceptual argument.

**Score**: 6.0 — A solid paper with clear contributions and addressable weaknesses. The theoretical derivation is the standout contribution; the experiments would benefit from standard RL rigor (error bars) but the reported trends are consistent and large enough to be believable.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>