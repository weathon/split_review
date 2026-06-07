## Summary

COPlanner proposes a symmetric planning-time framework for Dyna-style MBRL: the same UP-MPC (uncertainty-aware policy-guided MPC) component estimates multi-step ensemble disagreement, then uses it as a **penalty** during model rollouts (conservative) and as a **bonus** during environment exploration (optimistic). Integrated with MBPO and DreamerV3, it shows sample efficiency gains of ~40–100% on proprioceptive tasks and ~2× on visual tasks across 16 continuous control benchmarks.

## Strengths
- **Clean symmetric design.** The same UP-MPC procedure with sign-flipped α (+α_o or −α_c) serves both conservative rollouts and optimistic exploration, avoiding the need for separate exploration policies (Algorithm 2, lines 198 and 204; Eqs. 6 and 7). This is structurally different from prior work (LEXA, Plan2Explore, MEEE) and well-motivated.
- **Significant empirical gains on MBPO:** ~40% sample efficiency improvement on DMC tasks and ~100% on GYM tasks, with results averaged over 8 random seeds and 95% confidence intervals (Figure 2, lines 277–280). Concrete example: Walker-walk, MBPO needs 100k steps to reach score 700, COPlanner needs ~60k.
- **Gains extend to DreamerV3 on visual DMC:** >2× sample efficiency and 9.6% performance improvement over DreamerV3 (Figure 3, lines 318–319), also outperforming LEXA-reward-DreamerV3 on 8 visual tasks with 8 seeds and 95% CI.
- **Ablation confirms both components are necessary.** Figure 4 shows that either component alone gives less improvement, and their combination achieves the best results (lines 335–336), with specific failure modes identified (over-conservatism in sparse-reward settings for Rollout-only).
- **Fixed hyperparameters across all tasks per domain** (α_o=1, α_c=2, K=5, Hp=5 for proprioceptive; α_o=1, α_c=0.5, K=4, Hp=4 for visual), which reduces concern about per-task tuning inflating results.
- **Mechanistic evidence.** Figure 5 shows that COPlanner reduces model prediction error (MSE/KL) and rollout uncertainty (ensemble disagreement) compared to baselines, supporting the claimed mechanism.

## Weaknesses

### Fatal
None.

### Major
1. **Computational cost of UP-MPC not reported.** The UP-MPC planner is invoked at every action selection step — both for real-environment interaction (Algorithm 2, line 198) and for every step of every model rollout (Algorithm 2, line 204). For each invocation, it samples K action candidates, rolls each out for Hp steps through the dynamics model, computes ensemble disagreement at each step, and scores candidates. Given that MBPO typically performs thousands of model rollout steps per real-environment step, this represents a substantial increase in per-step computation. No wall-clock time, forward-pass counts, or training-time comparisons are reported. The authors implicitly acknowledge cost as a concern: "We can improve computational efficiency by parallelizing planning, which we leave for future work" (line 372). Without cost analysis, the practical trade-off between sample efficiency gains and per-step computation is unknown, weakening the practical contribution claim.

2. **"Plug-and-play" claim rests on only two base methods.** The paper asserts COPlanner "can be applied to any dyna-style model-based methods" (abstract and contributions, lines 13, 61) but tests integration with exactly two: MBPO and DreamerV3. While these are strong representatives spanning different architectures (ensemble-based Gaussian model with SAC vs. latent world model with actor-critic), two data points do not support a claim of universal applicability. The evidence supports "COPlanner improves MBPO and DreamerV3" — a claim that should be reflected in the paper's framing, or supported by at least one additional base method per domain.

### Minor
- **No ablation comparing multi-step vs. one-step uncertainty.** The paper's claimed advantage over MEEE is that multi-step uncertainty estimation over Hp steps is more informative than one-step uncertainty. An explicit comparison of Hp=1 vs. Hp=Hp_default within COPlanner would directly test this core mechanism and substantially strengthen the evidence.
- **Aggregate improvement percentages reported without confidence intervals.** The headline numbers (16.9% on proprioceptive DMC, 32.8% on GYM, 9.6% on visual DMC) are reported as exact point estimates (lines 63, 282, 284, 319) with no CI or standard error. Given that individual task curves show overlapping CIs in several cases, quantifying the uncertainty around these aggregates would be informative.
- **No hyperparameter sensitivity analysis.** Fixed α_c, α_o, K, Hp across tasks is a strength, but no analysis shows how performance varies when these are changed or whether the chosen values are near-optimal.
- **"Broken seed" in ablation not analyzed.** The paper mentions "a broken seed in Cartpole-swingup-sparse" for the Rollout-only variant (line 332) but does not report how many of 8 seeds showed this failure, whether the seed was excluded from the average, or whether this signals a systematic risk in sparse-reward settings.
- **Tension: policy trained on conservative rollouts used to propose exploration candidates.** Action candidates for optimistic exploration are sampled from the policy π_φ (Algorithm 1, line 133), but π_φ is trained on samples from conservative rollouts (Algorithm 2, line 208). If the policy converges to a narrow distribution around conservative high-reward actions, it may not propose diverse enough candidates for meaningful exploration. The paper does not discuss this.
- **Reward scale and α coefficient interaction not discussed.** The linear combination r + α·u with fixed α coefficients could produce task-dependent effects if reward scales differ substantially across tasks. The paper asserts robustness but does not analyze this.

### Trivial
None.

## Nice-to-Haves
- Report wall-clock time per environment step and total training time for COPlanner-MBPO vs. MBPO and COPlanner-DreamerV3 vs. DreamerV3.
- Add an ablation with Hp=1 to directly test the multi-step vs. one-step uncertainty claim.
- Analyze how many of the 8 seeds in the Cartpole-swingup-sparse Rollout-only condition showed catastrophic behavior.
- Provide confidence intervals or bootstrap ranges for the aggregate improvement percentages.
- Include a hyperparameter sensitivity plot for α_c, α_o, K, Hp on 1–2 representative tasks.

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- **Harsh critic's "uncertainty estimation on imagined trajectories" concern:** This is a known limitation of ensemble disagreement methods in MBRL generally, not specific to this paper. The paper already notes that any intrinsic reward method can be plugged in (line 147), providing a path around this limitation. Additionally, the paper's own analysis (Figure 5, Section 4.4) empirically shows that rollout uncertainty is actually *lower* with COPlanner, partially mitigating the concern. Demoted from "structural concern."
- **"Section numbering appears off":** The paper's section ordering (1 Introduction, 2 Preliminaries, 3 COPlanner Framework, 4 Related Work, 5 Experiment, 6 Conclusion) is correct. This is a parser artifact.
- **Strength Finder's generic strengths** (e.g., "addresses an important problem"): These lack specific evidence and are superficial. Removed.
- **DrQV2 comparison being "less informative":** Comparing with SOTA model-free methods is standard practice in MBRL papers and provides useful context. This is scope creep.
- **"No comparison to P2P" claim:** P2P is explicitly included as a baseline (line 254). The paper does analyze COPlanner vs. P2P, noting that P2P lacks effective exploration. This criticism is factually incorrect.

## Novel Insights
None beyond the paper's own contributions. The two reviewing perspectives converge on the paper's core strengths (clean symmetric design, solid empirical validation with 8 seeds and 95% CI, ablation, mechanistic analysis) and core weaknesses (missing computational cost analysis, limited empirical base for the universal-plug-and-play claim). Neither reviewer surfaces a fundamentally novel observation not already present in the paper or the reviews.

## Suggestions
1. **Report computational cost.** Add wall-clock time per training step and total training time for COPlanner vs. base methods. Even a simple table showing forward-pass counts per epoch would help readers assess the practical trade-off.
2. **Narrow the plug-and-play claim** to match the evidence ("COPlanner improves MBPO and DreamerV3") or add at least one more base method per domain.
3. **Add Hp=1 ablation** to directly test whether multi-step planning drives the improvement over one-step uncertainty methods.
4. **Report CIs for aggregate improvement percentages** (16.9%, 32.8%, 9.6%) to calibrate expectations about variability.
5. **Add a hyperparameter sensitivity plot** for α_c, α_o, K, Hp on 1–2 representative tasks.
6. **Analyze the "broken seed" systematically** — report how many of 8 seeds failed in that condition and whether the failure pattern is replicable.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>