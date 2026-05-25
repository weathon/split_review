Now I have a thorough understanding of the paper. Let me construct the consolidated review.

---

## Summary

This paper proposes a Dynamics Feature Representation (DFR) framework for RL-based dynamic path planning in urban road networks. DFR employs a two-stage hierarchical refinement: (1) a policy attention mechanism that extracts a subgraph based on top-*k* static shortest paths, and (2) an *n*-hop neighborhood method that further decouples this subgraph into local features around the agent's current node. Experiments on three real-world road networks (Nanjing, Beijing-Chaoyang, Shanghai-Pudong) with DQN, GCN+DQN, and PPO show that DFR consistently outperforms all-dynamics (AD) baselines while reducing feature dimensionality and planning time.

## Strengths

1. **Consistent empirical improvement across multiple algorithms and cities.** Figure 5 shows that DFR-enhanced models (DQN+DFR, GCN+DQN+DFR, PPO+DFR) achieve larger radar coverage (1−GAP, SR, 1−CR) than their AD counterparts on all three real-world road networks. Concrete planning-time reductions of 85.59% (DQN), 46.08% (GCN+DQN), and 79.32% (PPO) are reported (Section 5.2). This provides solid evidence that DFR offers practical efficiency gains.

2. **Thorough ablation study covering the full (k, n) design space.** The heatmaps in Figure 6 systematically sweep k (policy attention) and n (hop neighborhoods), with 6 × 5 = 30 configurations plus the AD baseline. The ablation shows that DFR with k=0.4, n=4 achieves GAP 0.095 and SR 0.905 at CR <4.7%, compared to the global baseline (k=−1,n=−1) with GAP 0.176 and SR 0.864. This directly demonstrates that both components contribute to the improvement.

3. **DFR complements GCN-based representation learning.** Section 5.2 notes that GCN+DQN+AD achieves high SR but still exhibits high GAP (low 1−GAP), suggesting the GCN is insensitive to dynamic variations when feature dimensionality is high. Adding DFR reduces this gap, showing that feature selection adds value beyond what graph convolutions alone provide.

4. **Negligible online overhead due to offline precomputation.** Section 4.3 explains that both the distance-based policy (pre-trained once on static topology) and the n-hop neighborhoods depend only on the fixed graph structure, so they can be computed offline and reused. The dramatic planning-time reductions serve as empirical verification of this efficiency.

## Weaknesses

### Fatal

None.

### Major

1. **The core assumption — that static shortest-path subgraphs retain decision-relevant dynamics — is not directly validated.** DFR's first stage selects edges based on top-*k* shortest *distance* paths. Under time-varying congestion, the optimal travel-time path may be longer in distance (e.g., a highway detour avoiding gridlock) and fall outside the static distance-selected subgraph. The paper justifies this choice by saying "distance is one of the most fundamental constraints" (Section 4.3), but never directly measures whether the DFR subgraph actually contains near-optimal dynamic routes. Because the only comparison is against AD (all dynamics), which may be overwhelmed by high input dimensionality, DFR's superior results could stem from dimensionality reduction alone rather than from its specific selection logic. A direct coverage analysis (e.g., for each test scenario, compute the oracle optimal dynamic path and measure how often it lies within the DFR subgraph) is needed to substantiate the claim that the subgraph is "decision-relevant."

2. **Missing baselines that would isolate the effect of DFR's selection strategy.** The experiments compare DFR only against AD (all-dynamics) versions of the same algorithms. There is no comparison against:
   - A **random subgraph** of matching size, to determine whether any compression helps or DFR's specific selection matters.
   - **Dynamic Dijkstra** operating within the DFR subgraph, to directly measure the information loss from the filter independent of RL training.
   - A **static full-graph** baseline using Dijkstra on the current snapshot.
   
   Without these controls, it is unclear whether DFR's gains come from intelligent feature selection or merely from reducing the RL agent's input dimension.

### Minor

1. **Convergence acceleration claim is not directly supported.** The abstract and contributions claim that DFR "accelerates convergence compared to baselines." However, the only training curves shown (Figure 6 bottom) compare DFR variants (k=0.6 with varying n) *among themselves*, not against the AD baseline. Whether DFR converges faster than AD is not evidenced.

2. **PSR theoretical framing is not substantiated by the method.** Section 4.2 invokes Predictive State Representations to argue that the local features W''_t are "theoretically sufficient" and "temporally predictive." In practice, DFR performs no learning or enforcement of predictive properties — it selects edges based on static distance and spatial neighborhoods. The PSR discussion creates a misleading impression of formal rigor without a concrete link between the theory and what DFR actually computes. This passage should be either tightened or removed.

3. **No confidence intervals or variance estimates reported.** The main results (Figure 5) are presented as radar charts without numeric values for GAP and SR, and no error bars or standard deviations are reported anywhere in the paper. This makes it impossible to assess the statistical significance of the reported improvements.

4. **Congestion dynamics are underspecified.** Section 5.1 states that β ∈ [0.1, 1.5] parameterizes edge weights, but does not describe how β values are sampled (uniform? truncated Gaussian? correlated across edges or time steps?). The temporal evolution of congestion is not characterized, making it difficult to assess how realistic or challenging the test scenarios are.

5. **Compactness Rate (CR) definition appears inconsistent with reported values.** CR is defined as "the proportion of the reduced feature dimension after DFR to the original dimension" (Section 5.1), so for AD (no reduction) CR should be 100%. Yet the ablation heatmap reports CR = 121.042% for the AD baseline (k=−1, n=−1), and several other cells show values that do not cleanly match the stated definition. This requires clarification.

### Trivial

- **Using RL to learn a static shortest-path policy π\*\_d is unnecessarily complex.** Section 4.3 trains an RL agent to find shortest-distance paths; Dijkstra's algorithm would solve this subproblem exactly with no approximation error. While this does not affect the main results (the pre-training is offline), the choice is not justified.

## Nice-to-Haves

- A direct path-coverage analysis: compute the optimal dynamic path (oracle with full future knowledge) for each test scenario and measure the recall (fraction of that path's edges/nodes contained in the DFR subgraph) as a function of k and n. This would directly validate or refute the core assumption.
- A random-subgraph baseline of the same size as DFR's output, controlling for the effect of dimensionality reduction alone.
- Comparison against Dynamic Dijkstra running on the DFR subgraph, to quantify information loss from the filter without confounding by RL training artifacts.
- Quantification of the one-time computational cost of pre-training the distance-based policy π\*\_d.

## Removed Points

These points from the reviewers are flagged as invalid or noise and should be treated with caution:

- "The dynamics are synthetic, not real traffic data… the paper styles itself as practical ('realistic urban graphs') yet tests on simulated dynamics." — The paper states "Experiments on realistic urban graphs" (emphasis on *graphs*). The graph topology is indeed realistic (OSM data). The criticism misreads "realistic urban graphs" as "realistic traffic dynamics." The use of synthetic congestion is a limitation but the paper does not claim otherwise.
- "The paper should use real traffic data." — The paper uses real road network topology; synthetic dynamics are standard for a proof-of-concept. This is scope creep.
- Nitpick about using RL for static shortest paths — this is a design choice, not a flaw, and is already listed under Trivial.
- Missing related work — excluded per filtering rules (cannot verify completeness without external search).
- Formatting/style complaints — excluded per filtering rules (artifacts of PDF extraction).

## Novel Insights

The reviewers' critique surfaces a broader question relevant to the RL-for-routing community: is task-*specific* compression (e.g., shortest-path subgraphs) necessary, or would any reasonable low-dimensional encoding of the full traffic state suffice? DFR's empirical gains over AD could be driven by the inductive bias of the shortest-path subgraph, by the mere reduction in input dimensionality, or by both. Distinguishing these requires a random-compression control that the paper lacks. This gap is not unique to this paper — many state-abstraction papers in RL compare only against the full-state baseline — and DFR would be strengthened by directly measuring whether its subgraph preserves oracle-optimal routes.

## Suggestions

1. **Validate the subgraph coverage directly.** For each test scenario, compute the optimal dynamic path (using Dijkstra on the known future sequence) and report what fraction of its edges/nodes the DFR subgraph contains, as a function of k and n. If coverage is high for the configurations that also perform well in RL, the method's rationale is supported.

2. **Add a random-subgraph baseline.** Keep the same reduced dimensionality as DFR but select edges/nodes randomly. If DFR outperforms random, the specific selection logic matters; if both beat AD equally, the benefit is purely from dimensionality reduction.

3. **Report numeric values and confidence intervals in the main radar-chart figure.** At minimum, add tables with mean GAP, SR, and CR values alongside the visual comparison.

4. **Clarify the CR metric definition or resolve the inconsistency** in the reported baseline value (121.042% for AD).

5. **Either remove the PSR framing or make the connection concrete.** If PSR theory is retained, explain how DFR's static-distance selection enforces predictive sufficiency — otherwise the passage misleads.

6. **Describe the congestion dynamics generation process** (distribution of β, temporal correlation, per-edge independence).

## Score and Decision

The paper tackles a practical and well-motivated problem (state representation for RL-based dynamic path planning) and proposes a clean, hierarchical compression framework. The empirical results are consistently positive across three algorithms and three cities, and the ablation study is thorough. The main weaknesses are (a) the core assumption that static shortest paths retain dynamic decision-relevant information is not directly validated, and (b) missing baselines prevent attribution of the gains to DFR's specific selection logic versus dimensionality reduction more broadly. These gaps are significant but addressable with additional analyses (subgraph coverage measurement, random-subgraph baseline). The PSR framing and missing confidence intervals are lesser issues. The paper represents a solid contribution that would benefit from strengthening before acceptance.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>