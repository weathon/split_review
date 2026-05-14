Now I have a thorough understanding of the paper and the calibration anchors. Let me synthesize the final review.

## Summary

This paper proposes a Dynamics Feature Representation (DFR) framework for RL-based dynamic path planning in urban road networks. DFR uses a two-stage hierarchical refinement: first, a pre-trained policy attention mechanism extracts a task-relevant subgraph based on the top-k static shortest paths between source and destination; second, an n-hop neighborhood method further decouples this into node-centric local features. Experiments on three real-world road networks (Nanjing, Beijing Chaoyang, Shanghai Pudong) with three RL algorithms (DQN, PPO, GCN+DQN) show that DFR consistently improves success rate and mean GAP while reducing feature dimensionality by over 94% and planning time by up to 85%.

## Strengths

- **Consistent empirical gains across multiple RL algorithms and real-world road networks.** DFR improves Mean GAP, Success Rate, and planning time for all three tested algorithms (DQN, PPO, GCN+DQN) on three distinct city graphs from OpenStreetMap. Figure 5 shows DFR-enhanced models consistently yield larger triangle areas (joint metric) than their All-Dynamics counterparts. Planning time reductions are substantial: 85.59% (DQN), 46.08% (GCN+DQN), and 79.32% (PPO). This breadth supports the claim that DFR is a general framework rather than an algorithm-specific trick.

- **The hierarchical refinement pipeline is clean and well-motivated.** The two-stage design (task-level filtering via policy attention, then agent-centric decoupling via n-hop neighborhoods) follows natural intuition — first identify which roads are topologically plausible given the origin and destination, then focus on the agent's immediate vicinity within that set. The ablation study (Section 5.3) systematically validates sensitivity to both parameters (k and n), showing that DFR configurations consistently outperform the no-DFR baseline across nearly all settings.

- **Practical efficiency for real-time deployment.** The policy attention subgraph and n-hop neighborhoods depend only on static road topology and are computed offline, while online collection of live dynamics is restricted to the small pre-computed subgraph. The paper reports average planning times of 8.18 ms for DQN/PPO and 27.26 ms for GCN+DQN, making the approach viable for real-time urban routing.

- **Thorough ablation study covering both parameters.** The heatmaps in Section 5.3 systematically explore k ∈ {0.2, 0.4, 0.6, 0.8, 1.0, -1.0} and n ∈ {1, 2, 3, 4, -1}, providing practical guidance (moderate k, smaller n) for deployment. The observation that performance plateaus as n increases (bottom of Figure 6) helps identify the point of diminishing returns.

## Weaknesses

### Fatal
None.

### Major
None that threaten the core claims, but the following issues are significant:

- **The Predictive State Representation (PSR) framing is decorative, not substantive.** The paper invokes PSR (Section 4.2) to argue that the compressed representation Wt'' is "theoretically sufficient" and preserves "all decision-relevant information." However, no formal guarantees are provided — no proof that the policy attention + n-hop pipeline satisfies the PSR sufficiency condition, no characterization of the information gap between Wt and Wt'', and no bound on how much the optimal policy degrades under refinement. The PSR reference serves as motivational framing rather than genuine theoretical grounding. The paper's empirical contribution stands on its own, but the claim of being "theoretically grounded" is overstated.

### Minor

- **The dynamics generation process is underspecified.** The paper defines edge weights via a congestion factor β(vi, vj; t) ∈ [0.1, 1.5] in Equation 9, but never describes how β evolves over time. Are edge weights temporally independent? Autoregressive? Spatially correlated? Since the entire premise of DFR is about capturing *dynamic* traffic conditions, the lack of specification for the dynamics model makes it difficult to assess what class of dynamics DFR actually helps with. This detail may exist in the released code, but it should be stated in the paper.

- **The GCN+DQN comparison does not control for model capacity.** The GCN baseline processes the full graph (AD) while GCN+DFR processes a much smaller subgraph. The paper attributes the improvement to better representation, but it could partly stem from the GCN operating on a more appropriately sized input for its capacity. A controlled comparison (e.g., matching parameter counts or FLOPs between AD and DFR variants) would strengthen the attribution.

- **The core filtering assumption is not directly validated.** The paper assumes that edges along the top-k static shortest paths contain the dynamics most relevant for decision-making. A direct validation experiment — measuring what fraction of edges on the truly optimal *dynamic* path fall within the policy attention subgraph — is missing. Without this, it remains unclear whether DFR works *because* of the distance-based filtering or despite it (e.g., because the n-hop neighborhoods capture enough local information regardless).

- **The ablation shows performance degradation at high k without a clear explanation.** When k increases beyond 0.6, Mean GAP sometimes increases and SR sometimes decreases. The paper attributes this to "more complex and less predictable" dynamics, but an alternative explanation is that non-shortest-path edges introduce noise. If the latter is true, it actually supports the filtering intuition — but the paper does not distinguish between these interpretations.

- **The theoretical optimality claim (Equations 6-8) is stated but never checked.** The paper claims π*(vt, vg; Wt'') ≈ π*(vt, vg; Wt) but provides no empirical verification of this approximation quality. Checking this would strengthen the connection between the method and the PSR framing.

### Trivial
None.

## Nice-to-Haves

- Systematic variation of dynamics characteristics (temporally independent vs. correlated, spatially localized congestion vs. uniform) to map the regime where DFR's distance-based filtering is most beneficial.
- A controlled experiment replacing policy attention with random subgraph selection of matched size, to directly test whether distance-based filtering provides benefits beyond dimensionality reduction.
- Failure case analysis: scenarios where the optimal dynamic path systematically avoids all top-k static shortest paths.

## Removed Points

- **Criticism that static distance has "nothing to do" with dynamics and that policy attention serves a "fundamentally different problem."** The paper explicitly justifies (Section 4.3, lines 395-405) why distance serves as a fundamental constraint for identifying topologically relevant edges. The critic's "anecdotal counterexample" (a road 10% longer but 3× faster) ignores that the n-hop neighborhood method captures local context around the agent regardless of shortest-path status. The criticism is overstated; the paper's logic is a reasonable heuristic.

- **Criticism that Mean GAP against dynamic Dijkstra is "inappropriate."** Dynamic Dijkstra with full future knowledge is the standard optimal baseline in dynamic path planning literature. Interpreting GAP improvements as evidence of better dynamics representation is standard and valid.

- **PSR "lacks proof" and is "decorative naming."** This is partially valid — the PSR framing is indeed not a formal proof — but the tone that this makes the contribution "unsupported" is too harsh. The PSR reference is a conceptual motivation, not a claimed theorem. I have downgraded this to a minor weakness (the PSR framing is overstated) rather than a fatal flaw.

- **"The paper never verifies that the top-k shortest paths contain the edges whose dynamics matter."** This is a missing validation experiment but not a flaw in the existing experiments. I have recorded it as a minor weakness rather than a fundamental issue.

- **Formatting/style nitpicks and grammar concerns.** These are parser artifacts.

- **Accusation that the GCN baseline is fundamentally "unfair."** The comparison GCN+DQN+AD vs. GCN+DQN+DFR uses the same architecture; the only difference is the input. The capacity-matching concern is valid but minor, not "fatal."

## Novel Insights

An interesting tension emerges from the reviews that the paper itself does not fully explore: the static-distance filtering assumption is simultaneously the framework's greatest strength (computational efficiency, interpretability, offline pre-computation) and its most significant limitation (it may systematically miss edges whose *dynamic* behavior makes them optimal even though they are topologically suboptimal). The fact that DFR performs well empirically across three real-world networks suggests either that (a) optimal dynamic paths in practice rarely deviate entirely from the set of topologically plausible routes, or (b) the n-hop neighborhood provides sufficient coverage to compensate for missed edges. Distinguishing these would require an edge-inclusion analysis the paper does not provide. The reviewer correctly identified this gap but overstated it as a contradiction rather than an open question.

## Suggestions

1. **Specify the dynamics generation process.** State clearly how β(vi, vj; t) evolves over time: is it i.i.d. per timestep, autoregressive, or spatially correlated? This is essential for understanding what problem DFR actually solves.

2. **Add an edge-inclusion analysis.** For the learned dynamic-optimal paths, measure what fraction of edges fall within the policy attention subgraph. If this fraction is consistently high, the distance-based filtering assumption is validated. If not, the source of DFR's improvement needs re-examination.

3. **Add a random-subgraph control.** Replace policy attention with random selection of the same number of edges. If DFR's distance-based filtering outperforms random selection, the assumption that distance identifies relevant dynamics is directly supported.

4. **Tone down the PSR theoretical claim.** The paper should present PSR as inspiration/motivation rather than claiming the method is "theoretically grounded" by it. The empirical results are the main contribution and should be foregrounded.

5. **Control for model capacity in the GCN comparison.** Either match parameter counts or report a baseline where the GCN+AD model is given a comparable parameter budget to GCN+DFR.

## Score and Decision

**Calibration anchors** (all from /home/wg25r/review_agent/human_reviews_2026/):

| Path | Avg Score | Comparison |
|------|-----------|-----------|
| izL9UiBziW (DQN-path-planning) | 2.00 | Much weaker: single simple grid, no real graphs, no multi-algorithm eval. Current paper is clearly superior. |
| bisWxwcK8D (RL-VRP-dynamic) | 2.50 | Weaker: limited baselines, unclear benchmarking. Current paper has cleaner evaluation. |
| MKM8iEaowV (diffusion-RL-trajectory) | 3.00 | Weaker: methodology issues, unclear contribution. Current paper is more coherent. |
| DbrefyDn8R (state-abstraction-RL) | 4.00 | Comparable: both have clean ideas with clear limitations. Current paper has more practical relevance (real graphs) but less theoretical depth. |
| 38ioKDbyP7 (DP-Nav) | 4.00 | Comparable: both have real experiments with some missing controls. Current paper has broader algorithmic coverage. |
| mCpq1GCKxA (simplicial-embeddings) | 5.50 | Stronger: cleaner experimental design, deeper analysis. Current paper is weaker on theoretical framing and validation depth. |
| tHmiydOQhn (spectral-Bellman) | 6.00 | Stronger: substantive theoretical contribution, solid experiments. Current paper lacks comparable theoretical depth. |

The paper is stronger than the 2-3 range papers (real graphs, multiple algorithms, clear problem framing) and comparable to the 4.0 range papers. It is weaker than the 5.5-6.0 papers on theoretical rigor and validation depth. The primary contributions are the clean hierarchical framework and the consistent empirical gains across algorithms and graphs. The main limitations are the overstated PSR theoretical framing, the underspecified dynamics model, and the lack of direct validation of the core filtering assumption. The paper makes a genuine contribution to an important problem, but the gap between theoretical claims and evidence is notable.

**Score:** 5.0 — A solid paper with clear contributions and adequate experiments, held back by overstated theoretical claims and missing validation details. Appropriate for a poster.

**Decision:** Accept

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>