Now I have a thorough understanding of the paper. Let me synthesize the final review.

---

## Summary

This paper introduces PlaD, a dense-to-sparse training framework for deep reinforcement learning that combines two components — periodic replay-buffer reset and Dynamic Weight Rescaling (DWR) — to maintain neural network plasticity during pruning. The authors first develop the Weight Shrinkage Ratio (WSR) metric to document that dense DRL training exhibits increasing implicit sparsity (weights drifting toward zero), which they connect to known plasticity loss. PlaD is then evaluated on MuJoCo locomotion tasks with a SAC backbone, where it achieves dense-equivalent or superior normalized performance at sparsity levels exceeding 90%, substantially outperforming sparse-to-sparse baselines (SET, RigL, RLx2) and dense-to-sparse baselines (random/magnitude pruning).

## Strengths

- **Novel WSR metric and implicit-sparsity analysis.** Section 4 introduces the Weight Shrinkage Ratio (WSR) and demonstrates that even dense SAC/DQN training exhibits a clear upward trend in weight shrinkage toward zero (Fig. 2), with a corresponding increase in feasible pruning ratio (Fig. 3). This observation — that dense DRL naturally becomes more amenable to pruning over time — provides a concrete, data-driven motivation for the dense-to-sparse paradigm over the more common sparse-to-sparse approach, which enforces high sparsity from initialization.

- **Strong empirical results at extreme sparsity against diverse baselines.** In Fig. 5, PlaD outperforms all six baselines (Random, Magnitude, Static Sparse, SET, RigL, RLx2) in 10 out of 12 high-sparsity settings. For example, at 90% sparsity on HalfCheetah, PlaD achieves 99.2% of dense SAC performance versus 82.5% for the next-best baseline (RLx2 with 3M steps); on Ant at 90% it reaches 103.0% versus 71.7% for Magnitude. The advantage is consistent across multiple MuJoCo environments.

- **Ablation cleanly establishes that both components are necessary.** Table 1 shows that removing either memory reset or DWR causes clear performance deterioration. PlaD w/o DWR exhibits sharp performance drops with increased variance (e.g., Ant-v4, Hopper-v4), while PlaD w/o Reset reverts to near-Magnitude levels. This rules out the possibility that only one component is doing the work and confirms a genuine interaction.

- **Buffer-reset strategy is shown to be more effective than a static small buffer.** Fig. 6 demonstrates that periodic memory resets to 0.2M capacity significantly outperform a fixed 0.2M buffer in 3 of 4 tasks (e.g., Hopper-v4 by >30% relative to dense performance). This isolates the benefit of the reset dynamics from the trivial explanation of simply having a smaller buffer.

## Weaknesses

### Fatal

None.

### Major

- **The claim of *surpassing* dense SAC performance is not supported with raw return data.** The paper reports only normalized performance relative to vanilla SAC (e.g., "103.0%," "~130%"). No absolute returns, confidence intervals, or statistical significance tests are provided for the dense SAC baseline itself. This makes it impossible to assess whether the "exceeding dense" result is robust or could reflect noise in the normalization denominator. The relative comparisons to other sparse training methods are convincing regardless, but the headline claim that PlaD *exceeds* the dense model requires raw scores with uncertainty to be credible. The dense SAC baseline could be a standard implementation, but the reader has no way to verify this from the paper.

- **The claimed sparsity-plasticity link is correlational and not causally tested.** The paper observes that WSR and feasible pruning ratio increase over training, and then references prior work showing that plasticity declines over training (Nikishin et al., Sokar et al.). The connection is then used as central motivation for PlaD. However, WSR measures weight shrinkage toward zero — it is not a direct measure of plasticity (the ability to adapt to new information). No experiment manipulates sparsity and measures plasticity on a distribution shift or new task. This is a reasonable motivation for a method paper, but the paper overstates the connection as a core contribution. The method stands on its own empirical merits without needing to claim a causal sparsity-plasticity discovery.

### Minor

- **Key implementation details are underspecified.** The paper does not state the memory-reset frequency (only "periodically"), the pruning schedule (number of IMP rounds, fraction removed per round, or timing of pruning relative to resets), or the exact computational budget (FLOPs, wall time). These details are necessary for reproducibility and for assessing whether the method's advantage comes from more effective use of computation. Since the paper does not reference an appendix, these omissions are not covered by parser stripping.

- **No computational cost analysis despite efficiency motivation.** The paper motivates sparse training partly to reduce computation, but never reports wall-clock time, FLOPs, or memory usage for PlaD vs. baselines. Memory reset discards data and may increase environment interactions; without cost reporting, the practical efficiency claim is untested.

- **Large variance in several conditions raises reliability questions.** In the ablation (Table 1), some configurations show high standard deviations (e.g., Ant-v4 w/o DWR). While DWR is shown to mitigate this, the instability suggests the method's benefits can be seed-dependent in some settings.

- **The non-monotonic performance pattern (peak at 85–90% sparsity, lower at 50%) is observed but not diagnosed.** The paper's explanation — that plasticity loss is "more impactful at higher pruning ratios" — is post-hoc and not tested through direct measurement (e.g., WSR or gradient metrics at different sparsity levels during PlaD training).

- **No comparison to direct plasticity-preserving methods.** The paper compares against sparse training baselines but not against well-known DRL plasticity methods such as Nikishin et al.'s network reset or Sokar et al.'s dormant neuron reactivation. A comparison would clarify whether PlaD's benefits derive from the memory-reset component alone (which is related to prior work) or from the combination with sparse training.

### Trivial

None.

## Nice-to-Haves

- Direct measurement of plasticity during PlaD training using established metrics (dormant neuron ratio from Sokar et al., gradient diversity, rank of the Jacobian) would substantiate the plasticity-based explanation.
- Hyperparameter sensitivity analysis for reset frequency and pruning schedule.
- Comparison against network-reset baselines (Nikishin et al.) adapted to the sparse training setting.
- Reporting raw dense SAC scores with confidence intervals would put the "exceeding dense" claim on firm ground.

## Removed Points

These points are flagged to be removed — treat them with caution:

- **Speculation that the dense baseline is "undertuned."** This is an unsupported assumption with no evidence. The paper uses standard SAC; questioning it without basis is speculative.
- **Demands for experiments on on-policy algorithms (PPO, TRPO), discrete action spaces, or visual observations.** The paper clearly scopes itself to continuous control with an off-policy algorithm (SAC). Expanding to entirely different algorithm classes and observation modalities would constitute a different paper. The memory-reset mechanism is specifically motivated by replay-buffer non-stationarity, which is an off-policy concern.
- **Criticism that DWR implementation details are under-specified.** The mathematical formulation in Section 5 (mean, standard deviation, normalization of pruned weights) is explicit. The description "applied to pruned weights \(a^l\) during sparse training" sufficiently implies per-forward-pass application.
- **Claim that WSR is "not a measure of sparsity."** The paper explicitly uses the term "implicit sparsity" and defines WSR accordingly; it never equates WSR with hard zero sparsity.
- **Generic request for "statistical tests."** The paper reports averages over 5 seeds with standard deviations, which is standard practice for deep RL benchmarks. Formal hypothesis testing is not the norm in this setting.

## Novel Insights

The harsh critic's observation about the non-monotonic performance pattern (PlaD performs worse than dense at 50% sparsity but exceeds it at 85–90%) is a genuinely useful diagnostic point that the paper does not adequately explain. If plasticity loss were the primary mechanism, one would expect the benefit to scale monotonically with sparsity, not appear only at extreme levels. The paper's explanation is post-hoc; probing the gradient dynamics or dormant neuron fraction across sparsity levels during PlaD training would be a natural follow-up. Beyond this, no genuinely novel insight emerges beyond the paper's own contributions.

## Suggestions

1. **Add a table with raw returns (mean ± std across 5 seeds) for the dense SAC baseline and for PlaD at each sparsity level.** This single addition would resolve the most serious concern about the "exceeding dense" claim.
2. **Specify the reset frequency and pruning schedule explicitly** (e.g., "buffer reset occurs every N environment steps; IMP proceeds in T rounds removing fraction f of remaining weights per round"). Include a brief pseudo-code or algorithm block.
3. **Add a wall-clock time or interaction-budget analysis** showing that PlaD's performance advantage does not come at the cost of substantially more environment steps or computation.
4. **Measure dormant neuron ratio or another established plasticity metric** during PlaD training to support the mechanistic explanation, rather than inferring plasticity from performance alone.

## Score and Decision

**Originality:** Medium. The WSR metric is new; the memory reset is adapted from prior work to the sparse training setting; DWR is a lightweight normalization technique. The combination is novel.

**Importance of research question:** Good. Sparse DRL is practically important for deployment-constrained settings, and plasticity loss is a known bottleneck.

**Claims supported:** Partially. The relative advantage over other sparse methods is well-supported. The absolute "exceeding dense" claim needs raw scores. The sparsity-plasticity link is motivational but not rigorously established.

**Soundness:** Solid for the comparative experiments and ablation. Weakened by missing raw baseline scores and implementation details.

**Clarity:** Clear. The paper is well-structured and the figures are informative.

**Value to community:** Positive. The method is simple, the results are strong, and the dense-to-sparse perspective is a useful alternative to the dominant sparse-to-sparse paradigm in DRL.

Based on the above assessment: the paper makes a real contribution (simple, effective method with strong results and clean ablations), but the headline claim about exceeding dense performance is incompletely evidenced, and several implementation details are missing. These are addressable in a revision and do not fatally undermine the work.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>