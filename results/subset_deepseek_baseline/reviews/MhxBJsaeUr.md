## Summary
This paper studies asymmetric cooperative-competitive multi-agent reinforcement learning, where physically weaker agents (Ants) must learn to cooperate to defeat stronger opponents (Bugs) in a simulated sumo-style arena. The authors propose a two-phase curriculum learning framework combined with a Multi-Agent Transformer (MAT) architecture, and develop a three-stage attribution pipeline using integrated gradients to interpret how attention mechanisms drive emergent cooperative strategies. The work demonstrates that transformer-based policies outperform MLP baselines in enabling weaker agents to develop sophisticated coordination patterns.

## Strengths
- **Novel problem formulation**: The paper addresses an underexplored setting in MARL—asymmetric embodied confrontation where physically weaker agents must cooperate to defeat stronger opponents. This is a meaningful and challenging problem that bridges cooperative and competitive multi-agent learning.
- **Interpretability contribution**: The three-stage attribution pipeline that traces attention weights back to semantically meaningful observation dimensions is a genuine methodological contribution. The ability to map abstract attention scores to concrete physical cues (e.g., teammate relative positions, boundary distances) provides valuable insight into emergent strategies.
- **Well-designed curriculum**: The two-stage curriculum (first learning stable locomotion toward center, then learning adversarial engagement) is principled and empirically validated. The ablation studies clearly demonstrate its effectiveness over non-curriculum baselines.
- **Thorough empirical evaluation**: The paper includes multiple configurations (2v1, 3v1, 3v2), ablation studies for both curriculum and architecture, and robustness tests against different opponent types. The aggregated attribution analysis across 1024 episodes provides statistical reliability.

## Weaknesses

### Major
- **Limited architectural novelty**: The Multi-Agent Transformer is directly adopted from Wen et al. (2022) with minimal modification (single block, single head). The paper's core claim about "attention is advantage" would be stronger with architectural innovations or at least comparisons to other attention-based MARL methods (e.g., MADT, Agent-Transformer Memory). As presented, the contribution is more about applying an existing architecture to a new problem setting.
- **Insufficient baselines and comparisons**: The paper only compares MAT against MLP baselines. There are no comparisons to other state-of-the-art MARL algorithms (e.g., QMIX, MAPPO, COMA) or other attention-based approaches. This makes it difficult to assess whether the transformer advantage is specific to MAT or general to any expressive architecture.
- **The attribution analysis, while detailed, is largely descriptive rather than predictive**: The case study in Section 5.4 describes what agents attend to at different timesteps, but does not validate these attributions through intervention experiments (e.g., ablating specific observation dimensions to see if performance degrades as predicted). The paper would benefit from causal validation of the attribution findings.

### Minor
- **The claim that "weaker defeats stronger" is somewhat overstated**: In the 3 Ants vs. 2 Bugs setting, the Ants have numerical advantage (3 vs. 2), so it's not purely a case of weaker defeating stronger—it's more about numerical advantage compensating for individual weakness. The 2 Ants vs. 1 Bug setting is more appropriate for this claim but receives less attention in the main text.
- **The paper lacks analysis of failure cases or limitations**: When do the Ants fail? Are there specific Bug strategies that defeat the learned coordination? Understanding failure modes would strengthen the analysis.
- **The reward design for Stage 2 (Section 4.1.2) seems to implicitly encourage pushing opponents outward, but the paper doesn't discuss potential reward hacking or unintended behaviors.**

### Trivial
- The paper uses "Ant" and "Bug" as agent names, but the Bug is actually larger and stronger—this naming convention is slightly confusing.

## Nice-to-Haves
- Causal validation of attribution findings (e.g., ablating high-attribution observation dimensions and measuring performance drop)
- Comparison to additional MARL baselines (QMIX, MAPPO, COMA)
- Analysis of how the learned strategies generalize to unseen team sizes (e.g., 4 Ants vs. 2 Bugs)
- Discussion of whether the transformer advantage persists with larger numbers of agents

## Novel Insights
The paper's most novel insight is that attention-based architectures enable weaker agents to develop qualitatively different coordination strategies compared to MLP-based policies, and that these strategies can be systematically interpreted through gradient-based attribution. The finding that self-attention weights dominate (w_ii) while the observation already encodes teammate/opponent information is a subtle but important point—it suggests that the transformer's advantage comes not from cross-agent attention per se, but from its ability to selectively process and weight different components of a rich observation vector that already contains multi-agent information. The attribution analysis revealing that agents attend to different semantic cues (self-position, teammate relative positions, opponent boundary distances) at different phases of the episode provides concrete evidence for role specialization and task-phase-dependent attention allocation.

## Suggestions
1. Add comparisons to at least 2-3 additional MARL baselines (e.g., MAPPO, QMIX) to establish that the transformer advantage is not just about having a more expressive architecture.
2. Include intervention experiments that validate the attribution findings—for example, zeroing out high-attribution observation dimensions and measuring performance degradation.
3. Clarify the "weaker defeats stronger" framing by more explicitly discussing the role of numerical advantage vs. individual weakness.
4. Add a limitations section discussing when the learned strategies fail.

## Score and Decision

**Score**: 6

**Decision**: Borderline Accept

**Rationale**: The paper addresses a meaningful and underexplored problem, provides a well-designed curriculum, and makes a genuine contribution to interpretability in MARL through the three-stage attribution pipeline. However, the limited architectural novelty and insufficient baselines prevent it from being a strong accept. The work is solid and would benefit the community, but the claims about the transformer's advantage would be substantially stronger with more comprehensive comparisons and causal validation of the attribution analysis.

MY FINAL SCORE: <score>6</score>
MY FINAL DECISION: <decision>Accept</decision>