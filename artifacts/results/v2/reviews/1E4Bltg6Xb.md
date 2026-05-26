Now I have enough information to calibrate my score. Let me construct the final review.

**Round-1 bracket**: I initially bracketed this paper between 3.5 and 6.5 based on the topical calibration (mid-band anchors for "RL dynamic path planning state representation" had avg scores 4.00-6.00).

**Round-2 narrowing**: Reading mid-band anchors in detail confirmed that papers at 4.75-5.33 (CPP, text routing, predictive representations) share similar profiles: clear contributions with some reporting gaps and limited baselines. The DFR paper is slightly stronger than the CPP paper (4.75) and predictive representations paper (4.80) due to its multi-algorithm, multi-city evaluation and systematic ablation, but weaker than NaviFormer (6.00) which has cleaner reporting.

**Final score**: 5.0 — reflecting a paper with a genuine contribution and solid empirical validation, but whose impact is reduced by reporting gaps (CR anomaly, unclear AD baseline, missing experimental details) that must be cleaned up before the claims can be fully trusted.

Now let me compose the final review.

**Summary of removed points:**
1. "Subgraph selection conceptually mismatched" — The paper provides justification (Section 4.3, lines 149). The core concern (missing coverage validation) is kept as Minor, but the framing as "conceptually mismatched" is removed.
2. "RL-based distance policy is over-engineered" — Design choice, not a flaw. Yen's algorithm is an alternative, not a requirement.
3. "Time horizon effects" — Speculative.
4. "Method's success may reflect simulation setup" — Speculative.
5. "PSR grounding as a strength" — Overclaimed. The paper invokes PSR as motivation but doesn't implement or validate it (Section 4.2).## Summary

This paper proposes a Dynamics Feature Representation (DFR) framework for RL-based dynamic path planning in road networks. DFR uses a two-stage hierarchical compression: (1) a pre-trained *static-distance* RL policy selects top-*k* shortest paths to form a task-relevant subgraph ("policy attention"), and (2) an *n*-hop neighborhood of the agent's current node is extracted from that subgraph for the agent's state. Experiments on three real urban road networks (Nanjing, Chaoyang Beijing, Pudong Shanghai) compare DQN, PPO, and GCN+DQN agents with and without DFR. DFR reduces planning time by 46–86% across methods while maintaining or improving path quality (GAP and Success Rate), and achieves a Compactness Rate below 5.7% of the full dynamics dimensionality.

## Strengths

- **Substantial and consistent efficiency gains across algorithms and cities.** DFR reduces average planning time by 85.59%, 46.08%, and 79.32% for DQN, GCN+DQN, and PPO respectively compared to their All-Dynamics counterparts (Section 5.2). The radar charts (Figure 5) show larger triangle areas for DFR-enhanced models across all three subgraphs, indicating DFR simultaneously improves or maintains GAP and SR while dramatically reducing CR.
- **Algorithm-agnostic framework tested on diverse RL architectures.** DFR is evaluated with a value-based method (DQN), a policy-gradient method (PPO), and a graph-based method (GCN+DQN), and improves all three. This supports the generality claim beyond any single RL paradigm.
- **Systematic ablation study across the two hyperparameters (k, n).** The heatmaps (Figure 6) provide a detailed map of how Mean GAP, SR, and CR trade off as policy-attention strength (*k*) and neighborhood size (*n*) vary, yielding actionable deployment guidance (moderate *k*, smaller *n* for large graphs).
- **Evaluation on real road networks with a traffic parameterization.** Three urban subgraphs extracted from OpenStreetMap with a congestion-factor-based dynamics model (Equation 9) give the experiments more credibility than synthetic grid-world evaluations.

## Weaknesses

### Fatal
None.

### Major
None. (The weaknesses listed below are individually addressable and do not invalidate the core contribution, but in aggregate they should be addressed before the paper can be fully accepted.)

### Minor

1. **All-Dynamics (AD) state encoding is unspecified, leaving the comparison hard to interpret.** The paper never states how the AD baseline agents receive the full graph's edge weights. For DQN+AD and PPO+AD, which use MLP backbones (Section 5.1), a flat vector of all edge weights would be impractically high-dimensional and would trivially disadvantage AD. The GCN+DQN+AD baseline could handle graph-structured input, but its state encoding is also not described. Without this detail, the magnitude and source of DFR's advantage cannot be assessed fairly.

2. **CR (Compactness Rate) values in the ablation study contain an inconsistency with the defined formula.** CR is defined as "the proportion of the reduced feature dimension after DFR to the original dimension" (Section 5.1). For the no-compression cell (*k*=-1.0, *n*=-1) the reported CR is 121.042 (Figure 6), which should be approximately 1.0 (or 100% depending on scaling) if the formula is applied correctly. This discrepancy also appears in other *n*=-1 cells (e.g., *k*=0.6, *n*=-1 gives CR=11.643 with no monotonic pattern). The anomaly is confined to the ablation's *n*=-1 column and does not affect the main DFR results (where CR remains below 5.7%), but it undermines trust in the metric's reporting and needs correction or clarification.

3. **No variance or statistical significance for the main performance metrics.** Mean GAP and SR are reported as point estimates (Figure 5, Figure 6 heatmaps) without error bars, confidence intervals, or indication of how many random seeds were used. Only planning time is reported with a standard deviation (Section 5.2). Without variance estimates, the comparative claims (e.g., "DFR-enhanced models exhibit larger triangle areas") cannot be assessed for statistical reliability.

4. **Missing validation that the static-distance subgraph covers near-optimal dynamic paths.** The paper argues (Section 4.3) that focusing on top-*k* shortest *distance* paths is justified because "distance naturally serves as one of the most fundamental constraints." However, when the optimization objective is dynamic travel time, optimal paths under congestion may deviate arbitrarily far from shortest-distance paths. The paper does not compute what proportion of ground-truth optimal paths (dynamic Dijkstra) lie within the selected subgraph, nor does it compare with alternative subgraph selection strategies (random sampling, traffic-variance-based, or dynamics-aware attention). The ablation shows that policy attention adds value over no attention, but does not isolate *which* property of the distance-based selection is responsible.

5. **Missing experimental details needed for reproducibility.** Three important details are absent: (a) graph sizes (number of nodes and edges for each subgraph), which are needed to interpret CR and the dimensionality challenge; (b) the stochastic process generating the congestion factor *β* over time (are *β* values independent across edges? temporally correlated?); (c) how the variable-sized *W''*ₜ (different number of edges for different current nodes) is fed into the fixed-size MLP input layer. These gaps make the experiments difficult to reproduce.

6. **The state at time *t* only reflects current-edge weights *W*ₜ, not temporal history.** Traffic dynamics have memory (congestion propagates spatially, events have duration), so a state based solely on the current snapshot may not be Markovian. The paper invokes Predictive State Representations (PSR) in Section 4.2 to argue that *W''*ₜ is a sufficient statistic, but provides no evidence that *W''*ₜ (derived only from current *W*ₜ) actually predicts future dynamics. This is a common limitation in RL-based DPP, but the paper overclaims temporal modeling (e.g., "implicitly captures short-term temporal correlations") without supporting evidence.

### Trivial

- The distance-based policy used for subgraph selection is itself trained via RL, when classical *k*-shortest-path algorithms (e.g., Yen's) could serve the same purpose with no training variance. This is a design choice, not a flaw, but using Yen's algorithm would simplify the pipeline and improve reproducibility.

## Nice-to-Haves

- **Validate subgraph coverage:** For each test scenario, report the proportion of optimal (dynamic-Dijkstra) paths contained in the policy-attention subgraph, across traffic conditions.
- **Compare with an alternative subgraph-selection strategy** (e.g., random subgraph of the same size, or one based on historically high-variance edges) to isolate the benefit of the distance criterion.
- **Report standard deviations** over at least 3–5 random seeds for GAP, SR, and CR in both the main results (Figure 5) and the ablation (Figure 6).

## Removed Points

These points were flagged by reviewers but are removed per the filtering rules:

1. **"Subgraph selection is conceptually mismatched to the dynamic task"** (Harsh Critic Critical Issue 1) — The paper provides a reasoned justification (Section 4.3, "distance naturally serves as one of the most fundamental constraints") and the ablation shows the policy-attention component adds value. The valid core of this criticism (missing coverage validation) is retained as Minor #4 above. The framing as a "conceptual mismatch" overstates the issue given the empirical evidence.
2. **"RL-based distance policy is over-engineered; use Yen's algorithm instead"** — This is a design choice, not a flaw. Using RL for the static policy is a valid and common approach, and the pre-training is done once offline.
3. **"Time horizon H=100 may be insufficient"** — Speculative; the reported SR values (0.864–0.884 for baselines) suggest the horizon is generally adequate.
4. **"The method's success may reflect the specific simulation setup"** — Speculative, with no concrete evidence that the setup is biased.
5. **"PSR grounding as a strength"** (Strength Finder claim #2) — The paper invokes PSR as a theoretical motivation but does not implement or validate it, and the claim that it "guarantees" information preservation is overclaimed. Removed per conflict with Minor #6.

## Novel Insights

None beyond the paper's own contributions. The core idea—hierarchical state compression combining task-level subgraph selection (via static distance) with agent-local neighborhood extraction—is the main novelty. The review process did not surface any additional insight beyond what the paper itself proposes.

## Suggestions

1. **Clarify the AD baseline implementation.** Precisely describe how each AD agent (DQN+AD, PPO+AD, GCN+DQN+AD) encodes the full graph's edge weights. If the AD baseline uses a suboptimal representation (e.g., a flat vector of all edge weights into an MLP), acknowledge this limitation and consider adding a stronger baseline (e.g., a larger-capacity network for AD, or a GCN-based AD comparison).
2. **Fix or clarify the CR definition and values.** Either correct the CR values in Figure 6 (especially the *n*=-1 column) to match the stated formula, or explicitly state the formula that produces the reported numbers. Also report graph sizes (node/edge counts) to contextualize the CR values.
3. **Report statistical significance.** Add standard deviations or confidence intervals over at least 3 random seeds for GAP, SR, and CR. Without variance, the comparative claims are unverifiable.
4. **Add a coverage analysis for the policy-attention subgraph.** Report the fraction of dynamic-Dijkstra optimal paths that fall within the selected subgraph across a range of traffic conditions. This directly addresses the most significant conceptual concern about the method.
5. **Describe the dynamics generation process.** Specify how *β* values evolve over time (distribution, temporal/spatial correlation) to make the experiments reproducible.
6. **Describe the state-vector construction.** Explain how the variable-sized *W''*ₜ is processed into the MLP input (padding, aggregation, or a graph network).

## Score and Decision

**Calibration anchors used (all rounds):**

| Anchor ID | Avg Score | Round / Query | Comparison to this paper |
|-----------|-----------|---------------|--------------------------|
| NIhRwzqhUz | 3.00 | R1-topic-low | Much weaker — dynamic TSP, limited baselines |
| 58KF6ne6d4 | 3.00 | R1-topic-low | Weaker — CNC machining, unrelated domain |
| IcHHjgdb0o | 3.00 | R1-topic-low | Weaker — state representation learning, different domain |
| Gs8jWk0F01 | 2.20 | R1-topic-low | Much weaker — dynamic CVRP, poor scores |
| ZiF1bJ9K6B | 4.75 | R1-topic-mid | Comparable — CPP with RL, similar contribution level but more thorough experiments |
| Pj3ErOxlLo | 6.00 | R1-topic-mid | Stronger — NaviFormer, cleaner reporting and SOTA |
| uaKBM9sGEm | 4.00 | R1-topic-mid | Weaker — off-road driving, more methodological concerns |
| TOiageVNru | 6.00 | R1-topic-mid | Stronger — motion planning, well-executed |
| sEv6vHIUnu | 4.80 | R2-compression | Comparable — predictive representations with GNN, similar profile of a modest but clear contribution with reporting gaps |
| gWHiS8Z867 | 5.33 | R1-weakness-subgraph | Slightly stronger — text routing, fewer reporting issues |
| yEox25xAED | 6.60 | R1-weakness-subgraph | Stronger — grammar RL, accepted |
| 1OGhJCGdcP | 3.50 | R1-weakness-subgraph | Weaker — subgoal representations, limited experiments |

**Round-1 bracket:** 3.5 – 6.5 (topic-anchored queries placed the paper in the mid band).

**Round-2 narrowing:** Comparison with mid-band anchors positioned the paper slightly above the 4.75 CPP anchor (more algorithms, real cities) and slightly below the 5.33 text-routing anchor (which has fewer reporting issues). The 4.80 predictive-representations anchor is the closest comparator — both propose a representation-learning improvement within an existing RL pipeline and have similar strength of evidence.

**Final score:** 5.0 — a paper with a genuine contribution and solid empirical backbone, but whose clarity and trustworthiness are reduced by several addressable reporting gaps (CR inconsistency, unspecified AD baseline, missing variance, missing experimental details). These gaps are individually minor but collectively keep the paper from being a stronger contribution.

The paper does **not** suffer from a fundamental issue: the methodology is sound, the central claim is supported by the experiments presented, and the weaknesses are addressable.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>