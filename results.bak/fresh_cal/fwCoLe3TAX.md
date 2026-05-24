Now I have all the information I need. Let me produce the consolidated review.

---

## Summary

This paper proposes an RLHF method that automatically identifies two groups of trajectories (by maximizing variance of returns), then regularizes the policy to minimize performance variance across these groups while adaptively adjusting the KL penalty strength based on group membership. On Llama 2 7B, the method shows improved win rates against PPO-based baselines on both in-distribution and out-of-distribution dialogue and summarization tasks, with ablations confirming both components contribute.

## Strengths

- **Novel integration of automatic return-based grouping with adaptive KL in RLHF.** The combination is technically sound and empirically effective (Section 4, Eqs. 3–6). The ablation study (Table 2) shows that removing group invariant learning ("w/o GIL") drops win rate by 9.3% on Harmful and 6.1% on Helpful, demonstrating the grouping mechanism provides real benefit beyond standard PPO+KL.

- **Automatic group inference without manual annotation.** The critic-based classifier (Section 4.3, Eq. 4) infers group labels by maximizing return variance, removing the need for costly domain labels. The OOD evaluations (Figure 2) — where the method shows *increased* win rates on PKU-SafeRLHF and CNN Dailymail compared to in-distribution settings (e.g., win rate vs. PPO w/ KL on Harmful rising from 34.1% → 38.2%) — directly demonstrate improved generalization to unseen data.

- **Adaptive KL penalty is well-motivated and validated.** Section 4.4's dynamic KL (Eq. 6) applies larger constraints to high-performing data and relaxes them for challenging data. The training curves (Figure 3) show the dynamic KL variant achieves better rewards for the same KL divergence compared to fixed-KL variants, and the ablation (Table 2) shows removing it drops win rate by 5.2% (Harmful) and 4.9% (Helpful).

- **Consistent human and GPT-4 evaluations.** Table 1 reports both human and GPT-4 evaluations across three tasks, showing high consistency. The human evaluation results follow the same ranking as GPT-4, lending credibility to the automated evaluation used for ablations.

## Weaknesses

### Fatal

None.

### Major

1. **The "domain invariant learning" framing is mismatched with the actual mechanism.** The paper (line 29) explicitly states "We interchangeably use the terms 'groups' and 'domains'" and frames the contribution as discovering data domains in an invariant learning sense. However, the actual group inference mechanism (Eq. 4) maximizes *variance of returns* — this naturally produces groups that correspond to "high-return trajectories" vs. "low-return trajectories." The paper's own Figure 2 describes the groups as "simple group" (quick reward increase) and "difficult group" (slow improvement), confirming they are performance-based, not semantically distinct domains. The Group Invariant Constraint (Eq. 3) constrains *expected returns* to be equal across groups, not learned representations as in traditional invariant learning (IRM, Risk Extrapolation). **This does not invalidate the method** — return-based grouping combined with variance regularization is a technically reasonable contribution — but the paper oversells its connection to the invariant learning literature. The contribution would be more accurately described as "variance-regularized RLHF with adaptive KL based on automatically discovered performance groups."

2. **No uncertainty quantification or essential training details.** Table 1 reports win/tie/lose percentages as bare point estimates with no confidence intervals, bootstrap estimates, or standard errors. The number of evaluation samples is not reported. The number of human evaluators is not stated. Training hyperparameters (learning rate, batch size, number of PPO epochs, KL coefficient η, regularization coefficients β_critic and β_policy) are entirely absent. While point-estimate evaluation is common in this field, the absence of these details — especially given small margins (29.6% win vs. 29.5% lose against DPO on Harmful) — makes it impossible to assess whether reported differences are statistically meaningful.

### Minor

3. **The "highest-performing group" (g_high) is not defined.** Section 4.4 (Eq. 6) uses \(p_\phi(g_{\text{high}}|x,y)\) as the weight for the adaptive KL penalty but never states how g_high is determined. With binary groups (M=2, line 222), it can be inferred as the group with higher average return, but the paper should state this explicitly and discuss whether the identity of g_high can shift during the alternating updates and how this is handled.

4. **"First attempt to introduce group invariant learning into RL" is slightly overbroad.** Line 83 makes this claim with a "to the best of our knowledge" qualifier, which partially protects it. However, prior work on domain generalization in RL (cited in lines 79–80) and risk-sensitive objectives shares conceptual overlap. The paper should acknowledge this lineage more carefully and clarify that the novelty lies specifically in the *unsupervised group discovery within RLHF*, not in applying invariant learning to RL per se.

5. **The Group Invariant Constraint (Eq. 3) defines invariance on returns, not learned features.** The paper invokes IRM (line 81) as inspiration, but IRM operates on *feature representations* while this paper's GIC constrains *expected returns*. The paper should explicitly discuss this adaptation and justify why return-level invariance is the correct formalization for RL, rather than leaving the reader to bridge this gap.

### Trivial

6. **Training curves (Figure 3) only compare against PPO, not against PPO w/ KL or DPO**, making it harder to assess the method's training dynamics relative to all baselines.

## Nice-to-Haves

- A direct comparison against a simple variance-regularized PPO baseline (minimizing return variance across trajectories without group assignment) would isolate whether the grouping mechanism provides additional structure beyond variance minimization.
- Post-hoc analysis of group characteristics (e.g., trajectory length, topic distribution, response diversity) would clarify whether the discovered groups capture anything beyond return quantiles.
- Bootstrap confidence intervals for all win rates and explicit disclosure of the number of evaluation samples.

## Removed Points

These points from the inputs are removed with justification:

1. **"Comparison with DPO is not a controlled evaluation"** — Removed. The paper includes DPO as one of several baselines (PPO, PPO w/ KL, SFT, DPO) and acknowledges DPO ties on harmful queries (line 336). Controlled PPO-based comparisons are present. Including DPO is standard practice and not misleading.

2. **"The alternating update procedure lacks pseudocode / gradient details"** — Removed. The paper describes the mechanism (line 224: "jointly train φ and θ using alternating updates, similar to adversarial training"). While additional detail would help, this is not a unique deficiency for this paper.

3. **"Figure 3 does not show the GIL-only curve"** — Partially inaccurate. Figure 3 shows "Ours (fixed KL)" and "Ours (dynamic KL)" along with PPO. The fixed-KL variant IS the GIL-only variant (no adaptive KL). This is clear from context.

4. **"Reward distribution Gaussian claim is unsupported"** — Removed as overstated. The paper provides a visual comparison (Figure 4) and qualitative description. A formal normality test would strengthen it, but the visual evidence is not vacuous.

5. **"Missing related works"** — Removed per instructions (cannot verify external sources).

6. **"The paper claims 'first attempt' too broadly"** — Downgraded from the harsh critic's framing to Minor (point 4 above). The claim is qualified ("to the best of our knowledge") and partially defensible.

7. **Generic speculation about confounders not grounded in specific paper content** — Removed as it constitutes area-of-concern sweeping without concrete paper evidence.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Reframe the contribution honestly.** Replace "domain invariant learning" with language that accurately describes what the method does: automatically grouping trajectories by return level, regularizing to minimize cross-group variance, and adaptively controlling KL. The empirical results support this reframed contribution.

2. **Add confidence intervals to Table 1 and Figure 2** using bootstrap resampling over evaluation samples. Report the number of evaluation instances and the number of human evaluators.

3. **Explicitly define g_high** (Section 4.4) and discuss whether its identity can shift during training and how the optimization handles this.

4. **Provide training hyperparameters** (learning rates, batch sizes, PPO epochs, η, β_critic, β_policy) in a table to improve reproducibility.

5. **Add a direct variance-regularized baseline** (PPO with a penalty on return variance, no groups) to demonstrate that the grouping mechanism adds value beyond simple variance minimization.

## Score and Decision

This paper addresses an important problem (RLHF generalization) and proposes a practically effective technique. The empirical results are positive and the ablation study cleanly validates both components. However, the paper has a significant framing mismatch: it claims to perform "domain invariant learning" when the mechanism actually groups trajectories by return level. This overselling weakens the paper's credibility but does not invalidate the technical contribution. The lack of statistical rigor (no confidence intervals, no hyperparameters) is a further concern, though partially standard for this venue. With honest reframing and added reproducibility details, this is a solid contribution.

**Score: 6.0** — a paper with a real technical contribution and positive results, held back by a framing mismatch and presentation gaps that are addressable in revision.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>