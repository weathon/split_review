Now I have a thorough understanding of the paper and the reviews. Let me construct the final consolidated review.

---

## Summary

This paper introduces **Equal Long-term Benefit Rate (ELBERT)**, a long-term fairness notion for sequential decision-making that measures group well-being as the ratio of cumulative group supply to cumulative group demand. The key technical contribution is showing that the policy gradient of this ratio-based objective can be analytically reduced to a standard policy gradient via a fairness-aware advantage function (Propositions 3.1 and 3.2), enabling off-the-shelf policy optimization methods like PPO. Experiments on three environments (lending, infectious disease control, attention allocation) show ELBERT-PO achieves lower bias than baselines while maintaining competitive reward.

## Strengths

- **Novel framework for adapting static fairness to sequential settings via supply-demand ratios.** The paper defines Long-term Benefit Rate as the ratio of cumulative supply to cumulative demand, which naturally weights time steps by their demand (e.g., number of applicants). This cleanly handles varying temporal importance — something prior sum-of-stepwise-bias and cumulative-reward approaches can miss. The framework is general enough to cover multiple static fairness notions (EO, DP, incident coverage) as special cases by customizing supply and demand definitions (Section 5.1).

- **Analytical reduction of the policy gradient for a ratio objective to standard policy gradients.** Propositions 3.1 and 3.2 derive a fairness-aware advantage function that expresses the gradient of the ratio-based bias term as a linear combination of standard policy gradients of supply and demand. This is a neat theoretical contribution: because the Long-term Benefit Rate is a ratio of two cumulative sums, it does not have a recursive Bellman structure, and the reduction to standard policy gradients is non-trivial. It makes existing RL algorithms applicable without needing bespoke optimization.

- **Consistent empirical bias reduction across three diverse environments.** Results in Figure 3 show ELBERT-PO achieves the lowest bias in lending (0.02 vs. 0.08–0.16 for baselines), infectious disease control (0.01, tied with R-PPO but with higher reward), and multi-group attention allocation (lowest bias and highest reward). The lending result is particularly strong, reducing G-PPO bias by 87.5%.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **The paper's critique of prior long-term fairness notions is imprecisely framed.** The central example (Figure 1) claims that Chi et al. (2021) and Wen et al. (2021) define long-term bias as "difference of cumulative group fairness rewards (e.g. acceptance rates)," yielding zero bias. However, the cited works define group benefit more flexibly (e.g., cumulative counts of approvals), which would detect the bias in this example as a raw count difference. The criticism is fully valid for Yin et al. (2023) (sum of squared rate differences), but the framing conflates the two cases. This does not undermine the paper's technical contribution — the supply-demand ratio is a genuinely different and valuable formalism regardless — but the motivational argument is weaker than claimed. The paper would benefit from a more precise delineation of which prior metrics fail and why.

- **No direct experimental comparison against methods that explicitly optimize the fairness notions the paper criticizes.** The paper criticizes "sum of step-wise bias" (Yin et al., 2023) and "cumulative reward parity" approaches but includes no baseline that implements them. The baselines used (A-PPO, G-PPO, R-PPO) are from Yu et al. (2022) and represent different methodologies. To fully support the claim that prior long-term fairness notions lead to worse outcomes, the paper should compare against, e.g., a Lagrangian approach on cumulative reward parity or a PPO variant that minimizes sum-of-stepwise-DP-violations. Without this, the empirical story is incomplete.

- **Experimental results lack error bars or multi-seed statistics.** Figure 3 reports single bias/reward values per method and environment without variance estimates. In lending, the absolute bias values are small (0.01–0.02 range), and it is unclear whether the reported advantages over baselines are statistically significant. This is standard practice for RL evaluations and should be addressed.

- **The multi-group extension (Section 3.3) is underspecified.** The paper identifies the non-smoothness challenge of max/min operators and mentions "a smooth approximation using a weighted sum with softmax weights" but does not provide the exact formulation or analyze whether the approximation preserves the intended fairness property. The extracted text appears truncated, but even accounting for this, the treatment is significantly lighter than the two-group case.

- **Practical estimation challenges are not discussed.** The gradient expression in Proposition 3.2 includes denominator terms \(1/\eta_g^D(\pi)\) and \(\eta_g^S(\pi)/(\eta_g^D(\pi))^2\), which must be estimated from sample averages. When group demand \(\eta_g^D(\pi)\) is small (e.g., few applicants from a group), these estimates can have high variance, potentially destabilizing training. The paper does not address this.

- **The claim that ELBERT-PO obtains the same reward as G-PPO in infectious disease (Section 5.2) suggests the fairness constraint imposes no utility cost in that environment.** This is unusual and warrants explanation — is the environment too easy, the constraint ineffective, or the bias metric insensitive? The paper does not discuss this.

### Trivial
- Line 116 contains a labeling error in the fairness criterion definition (the supply/demand variable names appear to be swapped relative to the framework's convention, though the mathematical expression is correct for the EO metric).

## Nice-to-Haves
- Add a baseline that directly optimizes cumulative reward parity (e.g., a Lagrangian on total approvals per group) to test whether the criticized prior notions actually underperform.
- Provide a case study/trajectory visualization (e.g., for the lending environment) showing step-wise acceptance rates, cumulative counts, and Long-term Benefit Rate over time to concretely illustrate the "false sense of fairness."
- Analyze or bound the variance of the gradient estimator introduced by the denominator terms \(\eta_g^D(\pi)\).

## Removed Points
- **Criticism that the SD-MDP formalism is missing / incomplete**: The extracted text clearly has missing sections (Equation (1), Algorithm 1, full formalism of Section 2). These are parsing artifacts, not author omissions. The original submission contains this content.
- **Criticism that the multi-group smooth approximation "changes the objective" without analysis**: The extracted text for Section 3.3 is truncated — the full formulation and analysis exist in the original submission.
- **Criticism about missing limitations regarding group membership observability and stationarity of supply/demand**: These are scope-creep demands; no paper in this area addresses all of them, and the paper explicitly acknowledges the main limitation (not constraining demand itself).
- **Criticism that the paper "does not engage with specific metrics" in the related work discussion of Liu et al. (2018) and D'Amour et al. (2020)**: The related work section appropriately summarizes these papers at the appropriate level for a non-survey paper.
- **Claim that "the challenge [in Section 3.1] is overstated" because REINFORCE could be applied**: REINFORCE on the ratio objective is not straightforward because the ratio is not a cumulative sum of per-step rewards; the paper's identification of this as a challenge is correct, and the analytical reduction in Section 3.2 is a genuine contribution.
- **Formatting/style nitpicks and comments about parser-induced artifacts.**

## Novel Insights
The harsh critic identifies an interesting tension: the core example motivates ELBERT as fixing a flaw in prior metrics, but the paper's technical contribution (policy gradient for ratio objectives) is independently valuable regardless of whether prior metrics are "broken" in the specific way claimed. The real novelty is reframing long-term fairness as a ratio of two cumulative quantities (supply and demand) rather than a sum of per-step quantities — this shifts the optimization target from additive fairness to proportional fairness, which is substantively different even when both approaches would detect "bias" in simple examples. The reviewer also correctly notes that the multi-group setting introduces issues (non-smoothness, softmax approximations) that the paper treats too briefly.

## Suggestions

1. **Reframe the motivation** to focus on what the supply-demand ratio *adds* (normalization by varying demand, proportional fairness interpretation) rather than claiming prior metrics give "false" results. This avoids the debatable characterization of Chi et al./Wen et al. while keeping the genuine novelty.

2. **Add multi-seed results with error bars** to the experimental section to establish statistical significance of the bias reductions.

3. **Include at least one baseline** that directly optimizes a cumulative-sum fairness objective (e.g., a Lagrangian on total approvals) to empirically compare the ratio-based approach against additive approaches.

4. **Provide the exact formulation** of the multi-group smooth approximation and analyze its effect on the fairness objective (does it still minimize the range of Long-term Benefit Rates, or does it optimize a different quantity?).

5. **Discuss variance issues** with the denominator estimates \(\eta_g^D(\pi)\) and how they are handled in practice (e.g., clipping, warm-up, or importance sampling).

## Score and Decision

The paper makes a solid technical contribution — the policy gradient reduction for ratio fairness objectives is novel, theoretically sound, and practically useful. The supply-demand ratio framework cleanly unifies several fairness criteria under a single formalism. The empirical results are promising. The weaknesses are addressable and do not undermine the core technical contribution. However, the imprecise characterization of prior work and missing experimental rigor (no error bars, no direct baselines against criticized notions) prevent the paper from being a strong accept.

**MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>**