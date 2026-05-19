- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 5, 6
Now I have all the information I need. Let me synthesize the final review.

---

## Summary

This paper investigates negative side effects of certified adversarial training (specifically SA-DDQN) on the learned Q-function in deep reinforcement learning. It provides a theoretical construction in a linear MDP showing that the adversarial regularizer can cause both overestimation of optimal Q-values and reordering of suboptimal action rankings. The empirical study on Atari games compares vanilla DDQN to SA-DDQN trained policies, finding that adversarially trained policies exhibit (1) inconsistent action rankings (inconsonance), (2) less accurate Q-values for non-optimal actions, and (3) higher Q-values interpreted as overestimation.

## Strengths

- **Theoretical analysis (Section 3, Propositions 3.2, 3.3, Theorem 3.4):** The paper constructs a linear MDP with linear Q-function approximation and formally demonstrates that the SA-DDQN regularizer can, in principle, produce parameter vectors with lower regularized loss that simultaneously overestimate optimal Q-values and reorder suboptimal actions. This provides clear mathematical intuition for why such effects might arise, independent of the empirical study.

- **Inconsonance finding (Section 6.1, Figure 3):** The paper shows that in BankHeist, adversarially trained policies produce a smaller performance drop when forced to take the Q-function's worst-ranked action than its second-best action. This is a concrete, non-obvious empirical finding — the Q-function literally loses the correct relative ranking of suboptimal actions — and it is a novel contribution.

- **Performance-drop methodology (Section 6, Figures 1–2, Table 1):** The paper introduces a systematic way to probe Q-value accuracy for non-optimal actions by measuring the performance impact of forcing the policy to take lower-ranked actions in a controlled fraction of states. This goes beyond standard evaluation (which only cares about final episode return) and reveals degradation invisible to typical metrics.

- **Challenging the Bellemare et al. (2016) hypothesis (Section 6.4):** The paper observes that adversarial training simultaneously increases the action gap and produces higher Q-values, running counter to the hypothesized inverse relationship between action gap and overestimation bias. This observation is interesting and potentially valuable regardless of how one interprets the "overestimation" label.

## Weaknesses

### Fatal
None.

### Major

- **No episode reward comparison to support the overestimation claim (Section 6.3, Figure 4, Table 2).** The paper's central claim that adversarially trained policies "overestimate" Q-values rests on the assertion that the two policies "perform similarly (i.e. obtaining similar expected cumulative rewards without modification)" — yet **the paper provides no reward/return data anywhere in the main text.** Without knowing the true expected return, higher Q-values could simply reflect a genuinely better policy, not overestimation bias. The term "overestimation" is a specific claim about bias relative to ground truth, and the paper provides no ground-truth comparison. This is a critical gap that invalidates the overestimation claim as currently presented.

- **Insufficient evaluation rigor (Section 5).** Results are averaged over only 10 episodes — well below the standard practice of 100+ episodes for Atari environments, which have high per-episode variance. No random seeds are mentioned, so it is unclear whether results reflect a single training run. While the paper reports standard errors, 10 episodes is too few for reliable statistical inference. The strong universal claims ("vanilla trained deep neural policies have more accurate and consistent estimates") are not supported by data of this granularity.

### Minor

- **Inconsonance evidence limited to one game (Section 6.1, Figure 3).** The action ranking inconsistency is only demonstrated for BankHeist. The general claim of "loss of information in the state-action value function" would benefit from replication across more environments.

- **Theoretical analysis is an existence proof, not a mechanism demonstration (Section 3).** Theorem 3.4 shows that a θ with lower regularized loss and overestimation/reordering exists, but does not show that optimization (gradient descent on the regularized loss) would converge to such a θ rather than to θ*. The paper appropriately frames this as "theoretical motivation," but the gap between a constructed linear MDP and deep neural policies on Atari is not bridged. The claim that experiments "confirm that the theoretically-motivated problems [...] do indeed occur in practice" (line 152) overstates the link.

- **Vanilla DDQN Q-values treated as implicit ground truth (Section 6).** The paper uses vanilla DDQN Q-values as the reference point for "accuracy," but DDQN itself is known to produce biased value estimates (typically underestimation due to the double-Q mechanism). Without measuring against Monte Carlo returns or true Q-values, the "inaccuracy" claim conflates bias from adversarial training with bias already present in the baseline.

- **Performance-drop interpretation has plausible alternatives (Sections 6.1–6.2).** The paper interprets a smaller performance drop under worst-action forcing as evidence that vanilla Q-values are "more accurate." An alternative explanation is that the adversarially trained policy, by design, deemphasizes precise value estimates for non-optimal actions and is therefore less sensitive to being forced into those actions for reasons unrelated to Q-value accuracy. The paper does not control for this.

### Trivial
None.

## Nice-to-Haves

- Report episode rewards for both policies across games with standard errors and multiple seeds to directly substantiate the "similar performance" claim.
- Validate action ranking via Monte Carlo rollouts computing empirical Q-values for a subset of states.
- Extend the inconsonance analysis to more games beyond BankHeist.
- Add training dynamics (e.g., Q-values over the course of training) to connect the theoretical regularizer mechanism to observed outcomes.
- Adopt standard Atari evaluation protocols: at least 100 episodes per evaluation point and 5+ independent seeds.

## Removed Points

- **"Theoretical example does not bridge to deep RL" (from Harsh Critic, #4).** The paper explicitly frames the theory as "theoretical motivation" and says "in the setting of linear function approximation" (line 70). It never claims the theory proves the deep RL results. The criticism overstates what the paper claims. This point was partially merged into the Minor weakness above about the theory-experiment gap.

- **"Theorem 3.4 merely states existence" (from Harsh Critic).** This is factually correct but the paper never claims otherwise — it is presented as a possibility proof. Merged into the Minor weakness above.

- **"Section 5 is extremely sparse" (from Harsh Critic).** The paper explicitly says "We explain in detail all the necessary hyperparameters for the implementation in the supplementary material." The rule about missing appendix sections applies; the parser strips those sections from all papers. Retained only as a note about main-text self-containedness (minor weakness).

- **Strength Finder claim #2: "Empirical evidence in Section 6.3 demonstrates that adversarially trained policies [...] achieve similar episode returns."** The paper does NOT actually demonstrate similar returns — it merely asserts "performing similarly" without providing the data. This strength is factually incorrect and removed.

- **"Only one adversarial training method (SA-DDQN) evaluated in main text."** The paper acknowledges this and says supplementary covers follow-up methods. This is a scope choice, not a flaw. Removed.

- **"No statistical significance tests" (from Harsh Critic).** The paper reports standard errors, which is a standard approach. Demanding specific significance tests is a formatting preference, not a weakness.

- **Performance-drop alternative explanation about "function approximation covers true values poorly but the policy is robust in a different sense."** This speculative alternative is too generic to constitute a concrete weakness. The more concrete alternative ("adversarially trained policy is simply less sensitive to forced actions") is retained in Minor.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add reward/return data.** The single most impactful addition: report episode rewards for both vanilla and adversarially trained policies across all tested games, with error bars. If the rewards are statistically indistinguishable, the overestimation claim becomes credible. If they differ, the paper must be reframed.
2. **Increase evaluation scale.** Run evaluations with at least 100 episodes per data point and 3–5 independent training seeds. This is standard for Atari work and would substantially strengthen all empirical claims.
3. **Acknowledge the DDQN baseline bias.** Discuss that vanilla DDQN itself has known biases (underestimation) and that the paper's claims about "overestimation" and "inaccuracy" are relative to this already-biased baseline, not to ground truth.
4. **Provide Monte Carlo validation.** For at least one game, compute empirical Q-values via long rollouts for a subset of states to directly verify which policy's Q-values are closer to the truth.
