## Summary

This paper proposes an embodied multi-agent reinforcement learning (MARL) framework for studying asymmetric cooperative-competitive confrontations, where teams of weaker Ant agents learn to overcome stronger Bug opponents. The three main contributions are: (1) a two-phase curriculum training that bootstraps locomotion before introducing adversarial dynamics, (2) application of the Multi-Agent Transformer (MAT) architecture to model heterogeneous intra-team and inter-team interactions, and (3) a three-stage integrated-gradients attribution pipeline that traces attention weights back to semantically labeled observation dimensions to explain emergent tactics.

---

## Strengths

- **Genuine morphological heterogeneity**: Unlike particle-based multi-agent games, the Ant/Bug agents differ in mass, volume, degrees of freedom, torque, and joint range (Table in Figure 1). This creates physically grounded asymmetry where the capability imbalance is real, not artificial.
- **Effective curriculum with clear ablation**: Figures 5 and 6 cleanly show that curriculum-trained agents outperform non-curriculum baselines in both reward and win rate across all three population settings (2v1, 3v1, 3v2). The two-condition ablation (non-curriculum Bug vs. curriculum Bug opponents) strengthens the finding that curriculum robustness is genuine.
- **Interpretable attribution pipeline**: The three-stage framework systematically connects raw attention weights to semantic observation categories (self, teammate, opponent, rule-specific). Aggregating over 1,024 episodes reveals consistent attention patterns that align well with the observed emergent formations (rod/triangle blocking), providing more than anecdotal evidence.
- **Demonstration on a non-trivial task**: Achieving >90% win rate for 3 Ants vs. 2 Bugs (Transformer Ants vs. MLP Bugs) in a full-body physics simulation with the shrinking arena constitutes a demanding test of cooperative policy learning.

---

## Weaknesses

### Fatal
None.

### Major

1. **Low technical novelty in core methods**: The MAT architecture is adopted without modification from Wen et al. (2022). The two-phase curriculum is simple (stage 1: move to center, stage 2: chase opponent). Integrated gradients is a standard attribution method. The paper's contribution is essentially the combination and application of these existing tools to a new domain; none of the individual components are advanced or newly derived.

2. **Missing standard MARL baselines**: The architecture comparison is restricted to MLP vs. MAT. No comparisons with widely-used cooperative MARL algorithms (MAPPO, QMIX, QPLEX, HAPPO, etc.) are included. Without these, it is unclear whether the performance gains are specific to transformers or whether any centralized training with decentralized execution (CTDE) method would yield similar results on this task.

3. **Attribution methodology concerns**: (a) The decision to restrict the transformer to a single head and single block "to facilitate attribution" limits the model's expressiveness and conflates the attribution setup with the performance setup—the most interpretable network is used for all experiments, not just attribution. (b) Stage 1 finding that the diagonal weight $w_{ii}$ dominates is expected (each agent's policy is primarily driven by its own observation) and does not reveal anything surprising about cross-agent coordination. (c) The per-snapshot Stage 2/3 attribution in §5.4 interprets a single episode and single checkpoint; it is not clear how stable these per-step attributions are across different episodes or checkpoints.

4. **Reward confounding in curriculum ablation**: The non-curriculum baseline uses a composite reward (sparse elimination + dense centering + torque penalties + stillness penalties), while the curriculum uses a sequence of simpler rewards. Performance differences could partly reflect better reward shaping in the curriculum rather than the staged training structure itself.

### Minor

- Only three small-scale population settings are evaluated (2v1, 3v1, 3v2). The claimed scalability to "m Ants vs. n Bugs" is not empirically verified beyond these cases.
- Statistical significance is not reported for win-rate differences; the reported win-rate advantages (e.g., ~0.2–0.3 margin) could benefit from confidence intervals given stochastic policy evaluation.
- The connection between the attention-based insights from attribution and concrete design recommendations for future MARL systems is not articulated; the discussion stops at description rather than actionable conclusions.

### Trivial
None worth noting beyond parser artifacts.

---

## Nice-to-Haves

- Ablating the number of attention heads and transformer blocks to show how much of the performance advantage is lost vs. recovered with a more expressive (multi-head) transformer, while exploring whether attribution remains tractable.
- Including at least one additional MARL algorithm baseline (e.g., MAPPO) to contextualize where MAT sits in the performance landscape on this task.
- Showing stability of the attribution results across multiple checkpoints or seeds to strengthen the interpretability claims.

---

## Novel Insights

The paper demonstrates that applying pre-softmax integrated gradients across the three-component structure of attention (query, key, observation) enables a semantic read-out of what each agent "attends to" at each game phase (locomotion vs. formation vs. endgame survival). The observation that each Ant assigns the largest gradient attribution to its own diagonal attention weight $w_{ii}$ while still implicitly encoding teammate and opponent information through its observation vector—rather than via cross-agent attention—is a subtle and useful clarification of what "cooperation through attention" actually means architecturally: the emergent coordination is encoded in the observation rather than the attention topology itself.

---

## Suggestions

- Run the attribution pipeline on a multi-head configuration and verify that conclusions about cooperative cues are consistent across heads; this would either validate the single-head simplification or reveal richer structure.
- Add a direct comparison between MAT and MAPPO (a strong CTDE baseline) on win rate across all three population settings to establish whether transformer-specific structure is necessary.
- Provide learning curves with standard deviations (over at least three seeds) for the main win-rate comparisons in Figures 5 and 6.

---

## Score and Decision

The paper introduces a well-designed embodied arena for asymmetric MARL and the three-stage attribution pipeline is a thoughtful and partially novel tool for explaining transformer-based multi-agent decision-making. However, the core algorithmic components are borrowed without modification, the attribution's key finding (self-attention dominance) is unsurprising, and the absence of established MARL baselines leaves open how much the transformer architecture specifically matters versus good curriculum design. The work is a solid applied empirical paper but does not rise to the level of principled methodological or theoretical advance expected at ICLR.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>