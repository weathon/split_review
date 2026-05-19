Now I have all the evidence I need. Let me write the consolidated review.

## Summary

This paper proposes GOODRL, an offline-online deep reinforcement learning approach for dynamic workflow scheduling (DWS) in cloud computing. The method introduces three innovations: (1) a task-specific graph representation with a Graph Attention Actor Network that processes each task-machine pair separately, (2) a system-oriented graph representation with a Graph Attention Critic Network for value estimation, and (3) an offline-online training scheme combining imitation learning pre-training with gradient-controlled PPO and decoupled high-frequency critic updates. Experiments across multiple DWS scenarios show GOODRL achieving the best average rank (1.17) against heuristic (EST, PEFT, HEFT), GPHH, and DRL (ERL-DWS) baselines.

## Strengths

1. **Well-motivated architectural separation of actor and critic graphs.** Unlike prior scheduling methods that use the same graph for both actor and critic (e.g., Zhang et al. 2020; Song et al. 2022), GOODRL designs distinct representations — a task-specific graph for the actor (pairwise processing of each (observation, action) pair with focused node embedding) and a system-oriented graph for the critic (with bi-directional edges, machine-order connections, and self-attention). This separation is conceptually sound and addresses a genuine limitation of prior work.

2. **Strong empirical performance across diverse scenarios.** GOODRL achieves the best or near-best mean flowtime in all 12 offline and 4 online scenarios tested, with an average rank of 1.17 across both tables. The method substantially outperforms expert-designed heuristics (Gap up to 289.98%) and the GPHH baseline (Gap up to 39.49%), while scaling to 20,000 dynamically arriving workflows — a problem scale underexplored in prior learned scheduling work.

3. **Offline-online training framework with practical design elements.** The two-stage approach (imitation learning pre-training + PPO, then online fine-tuning with gradient control and decoupled critic updates) is well-motivated. The gradient control mechanism (Eq. 1) and high-frequency critic training address genuine challenges of online RL in scheduling (single long trajectory, non-stationary environment), and the ablation section claims both techniques are necessary for stable online performance.

## Weaknesses

### Major

1. **Section 4.2.2 (Critic Network Architecture Design) is effectively empty.** The section heading appears at line 90 followed only by an image reference and then immediately Section 4.3. No text describes the critic's GAT architecture, how the system-oriented graph is processed, the self-attention mechanism, or the output representation. Since the critic design is one of the paper's three claimed innovations, this is a structural defect that prevents evaluation of a core contribution. The critic architecture cannot be inferred from the actor's description in 4.2.1 because the paper explicitly motivates designing *different* representations for each.

2. **Ablation studies (Section 5.4) contain zero quantitative results.** The paper states that "Our-TSEM ... achieved the lowest cross-entropy loss" and "Ours-SOEM ... significantly outperforms" and "Ours-Online achieved superior online performance improvement" — but presents no tables, figures, or numerical values to substantiate any of these claims. Without quantitative ablation data, the individual contributions of the three claimed innovations (task-specific graph, system-oriented graph, online learning techniques) cannot be assessed. This is the most damaging evidential gap, as it means the paper's central claims rest on unsupported qualitative statements.

3. **No variance or statistical significance reported for any experimental result.** The paper states that "average performance is evaluated using five random seeds" (Section 5.1) but reports only point estimates ("Obj." and "Gap") in Tables 1 and 2 with no standard deviations, confidence intervals, or statistical tests. Given the known stochasticity of RL methods, the reader cannot determine whether GOODRL's improvements over baselines are reliable or noise. This is especially problematic for: (a) the two small scenarios where GPHH slightly beats GOODRL (by 1.24% and 0.15%), where variance could flip the comparison; (b) the online improvement of ≤1.24% of Ours-Online over Ours-Offline, where the claimed benefit may not be statistically significant.

4. **Insufficient DRL baselines and a potentially misconfigured DRL competitor.** The paper compares against only one DRL baseline (ERL-DWS), which achieves disastrously worse results (Gap up to 1128.92%). The paper acknowledges that even adding imitation learning to ERL-DWS yielded "no significant improvement." This extreme failure suggests ERL-DWS may not have been properly adapted to the DWS setting used here (different state representation, action space, reward structure), rather than being a fair comparison. Meanwhile, the paper's own related work section cites several GNN-based DRL scheduling methods (Zhang et al. 2020, 2024; Song et al. 2022; Su et al. 2023) that are not included in the experimental comparison.

5. **Online improvement over offline is marginal.** "Ours-Online" improves over "Ours-Offline" by at most 1.24% (one scenario), with smaller margins elsewhere. Without variance reporting, it is unclear whether this difference is significant. The paper's claim that online learning is a key innovation is weakened by this small effect size, and the cost-benefit of the added online training complexity is not discussed.

### Minor

1. **Hyperparameters and implementation details are largely unspecified.** The paper does not report: number of GAT layers and hidden dimensions, MLP sizes, attention heads, learning rates, PPO clip ratio, batch size, gradient control thresholds (τ₀, sliding window for μ and σ), or critic update frequency. These are needed for reproducibility.

2. **Computational cost of pairwise processing is not analyzed.** The actor processes |M| separate task-specific graphs through GAT layers at each decision step (where |M| is the number of machines). For large machine pools, this could be computationally expensive, but no runtime or memory analysis is provided.

3. **Transferability to FJSS is asserted without evidence.** Section 5.4 states in one sentence that GOODRL was applied to FJSS and "achieved a desirable trade-off" with "cost savings of up to 41%" — but no table, figure, or quantitative comparison is provided.

4. **The four workflow patterns used in experiments are not listed.** The paper mentions "Four popularly studied workflow patterns (Deelman et al." without completing the description, leaving the scenarios incompletely specified.

### Trivial

None beyond formatting issues arising from PDF parsing.

## Nice-to-Haves

- A cost-benefit discussion comparing the ≤1.24% online improvement against the complexity of maintaining an online training loop.
- A quantitative comparison of problem size (number of machines, workflows) with prior DWS studies to contextualize the claim of tackling "significantly larger" problems.
- Hyperparameter sensitivity analysis for the gradient control threshold τ₀.

## Removed Points

The following points from the input reviews were removed as they either misunderstand the paper, are factually incorrect, or fall under the removal rules:

- **"The missing appendix" concern**: The reviewer criticizes missing appendix content (proofs, pseudo-code). The parser strips these sections from all papers; they exist in the original submission.
- **"ERL-DWS was not properly configured" from Strength Finder**: This was reframed from a speculative critique to a verified concern (see Major weakness 4) based on the extreme 1128% gap and the paper's own admission that imitation learning did not help ERL-DWS.
- **Strength Finder claims about ablation "confirming" results**: These were removed because the ablation section contains no numerical evidence — the strength is based on statements the paper does not actually support with data.
- **Strength Finder's "comprehensive comparison against multiple strong baselines"**: Overstated; reduced to acknowledging the breadth of heuristic baselines while noting the single DRL baseline gap.
- **Strength Finder's "transferability shown to FJSS"**: Removed because the evidence is one sentence with no data.
- **Harsh critic's claim that results in "offline scenarios where GPHH beats GOODRL suggests the method is not universally dominant"**: This is not a weakness per se — no method is expected to be universally dominant, and the margins are very small (1.24%, 0.15%).
- **Harsh critic's suggestion about "scenario complexity not obviously larger than prior work"**: This is speculative and not verified against actual prior work problem sizes.

## Novel Insights

None beyond the paper's own contributions. The reviews primarily surface known issues (missing method sections, absent variance reporting, under-powered ablation) but do not contribute new scientific insights about the method or problem.

## Suggestions

1. **Complete Section 4.2.2** with a full description of the critic network architecture: the GAT layers, self-attention mechanism, how the system-oriented graph is processed, and the output representation. This is mandatory for the paper to be a complete submission.
2. **Add quantitative ablation results** with tables showing cross-entropy loss (for actor variants), value loss (for critic variants), and mean flowtime (for online variants), all with standard deviations over multiple seeds.
3. **Add variance reporting** (standard deviations over 5 seeds) to all cells in Tables 1 and 2, and consider adding statistical significance tests for key comparisons.
4. **Add at least one more GNN-based DRL baseline** from the methods cited in related work, or provide a clear argument for why they cannot be adapted to the DWS setting.
5. **Report key hyperparameters** (GAT layers/dimensions, learning rates, PPO parameters, gradient control thresholds) to support reproducibility.
6. **Include a runtime/inference latency analysis** given the pairwise processing of |M| graphs per decision step.

## Score and Decision

**Round 1 bracket:** I initially bracketed this paper between 3.0 and 4.5, based on the strongest relevant anchor (RAISE at 4.00) being a topically identical DWS paper with similar methodology but more complete presentation, and weaker anchors (MACE at 3.50) representing papers with incomplete evidence.

**Round 2 narrowing:** I examined detailed reviews for the most comparable papers:
- **RAISE (4.00, Reject):** Same DWS problem, same offline-online RL framing. RAISE had complete method description, proper ablation tables with numbers, and variance reporting. Despite being rejected for incremental contribution and marginal gains, RAISE is presentationally more complete than GOODRL. GOODRL has more severe completeness issues (missing section, no ablation data).
- **MACE (3.50, Reject):** DAG streaming scheduling. Had complete method description and ablation tables. Criticized for incremental novelty and limited baselines. GOODRL matches this in novelty but is worse in completeness.
- **GAA-PtrNet (4.50, Reject):** DAG scheduling with GNN+PtrNet. Had complete method, ablation studies, runtime analysis. GOODRL is less complete.

**Final score determination:** This paper has genuinely interesting and well-motivated ideas. However, the missing critic architecture section (one of three core contributions), the complete absence of quantitative ablation data, and the lack of variance reporting are not minor gaps — they are structural defects that prevent the paper from being properly evaluated in its current form. Even a strong rebuttal cannot fill a missing method section or supply absent ablation numbers. I place the paper below RAISE (4.00) due to these completeness issues, in the range of 3.0–3.5. Comparing to MACE (3.50), GOODRL has stronger empirical scope but worse presentation completeness. I score it at **3.0**.

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>