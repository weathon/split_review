Now I have sufficient calibration. Let me write the final consolidated review.

## Summary

This paper proposes the Dynamics Feature Representation (DFR) framework for RL-based dynamic path planning in urban road networks. DFR uses a hierarchical refinement process: first, a pre-trained distance-based policy attention mechanism selects a task-relevant subgraph via top-k shortest paths; second, an n-hop neighborhood method decouples this subgraph into node-related local features. The claim is that this two-stage compression preserves decision-relevant information while dramatically reducing the state dimension, enabling faster and more effective RL training. Experiments on three urban graphs (Nanjing, Chaoyang, Pudong) with DQN, PPO, and GCN+DQN show consistent improvements in Mean GAP, Success Rate, and planning time compared to the "All Dynamics" baseline.

## Strengths

- **Principled hierarchical refinement addresses a real trade-off.** The paper formalizes a three-level state refinement (Equation 5) that progressively distills global dynamics into compact features. The progression from global → task-relevant (via policy attention) → node-local (via n-hop) is well-motivated and directly targets the completeness-efficiency dilemma in RL-based DPP. This is a clean, interpretable design.

- **Policy attention is a novel approach to task-aware graph sparsification.** Pretraining a distance-based policy to select top-k shortest paths as a hard attention mask (Section 4.3, Figure 3) is a concrete technical contribution. Unlike soft attention mechanisms, this provides a pre-computable, interpretable, and offline sparsification prior, which is practically useful for real-time deployment.

- **Consistent empirical gains across three RL algorithms and three real graphs.** The radar charts in Figure 5 show that DFR-enhanced models (DQN+DFR, GCN+DQN+DFR, PPO+DFR) achieve larger triangle areas than their AD counterparts on all three subgraphs. The ablation study (Figure 6) systematically varies k and n, confirming that both components contribute to the gains. Planning time reductions of 46–86% over AD baselines are significant.

## Weaknesses

### Major

1. **Compactness Rate values are inconsistent with the definition.** CR is defined as "the proportion of the reduced feature dimension after DFR to the original dimension" (Section 5.1). For the AD baseline (k=-1.0, n=-1) — where no reduction occurs — this should be 1.0 (100%). The heatmap in Figure 6 shows CR = 121.042 for this configuration. Several other configurations also produce CR > 100% (e.g., k=1.0, n=-1: 95.640; k=-1.0, n=4: 5.399). The paper's own statement that "CR remains below 5.7% in all cases" for the DFR configurations indicates the authors intend these as percentages. But the AD value of 121.042% (21% above the theoretical maximum of 100%) is a concrete numerical error. This either indicates a bug in the CR computation, a mismatch between the definition and the actual calculation, or a data error. Since CR is used in the radar-chart aggregations (plotted as 1−CR), this inconsistency undermines the quantitative claims about dimensionality reduction. The authors must clarify and correct the metric.

2. **Insufficient baselines to isolate the contribution of DFR's specific design.** The paper compares DFR only against "All Dynamics" (AD). Any dimensionality reduction method is likely to improve RL performance over this extreme baseline due to the curse of dimensionality. The experiments lack: (a) a random subgraph baseline of comparable size, which would test whether the specific policy-attention subgraph matters beyond generic compression; (b) a local-only baseline using the n-hop neighborhood without the policy attention step, which would isolate the value of the global attention component; and (c) a comparison with GNN-based state embeddings (dismissed on efficiency grounds but not benchmarked). The ablation study (varying k, n) partially addresses this, but without a random compression control, it is unclear whether the improvements stem from DFR's specific design or simply from feeding a lower-dimensional input. The paper's central claim about the two-stage refinement being "task-aware" requires this stronger evidence.

3. **The central assumption that distance-based subgraphs capture time-optimal dynamics is not validated.** The policy attention mechanism selects subgraphs based on static shortest-distance paths. The DPP objective, however, optimizes for travel time under time-varying congestion. The paper argues (Section 4.3) that "distance naturally serves as one of the most fundamental constraints," but no evidence is provided that the set of edges on distance-shortest paths retains the dynamics relevant for time-optimal routing under adverse traffic. This is a structural gap: the feature selection criterion is unvalidated against the actual optimization objective. An offline analysis on the test data — computing the overlap between the optimal dynamic (time-based) paths and the static-distance subgraph — would directly address this concern.

### Minor

4. **No statistical rigor in the reported results.** The paper reports single trajectories per setting (Figure 6). No standard deviations, confidence intervals, or results from multiple random seeds are provided for any metric. Given the known variance in RL training, it is impossible to assess whether the observed improvements are statistically reliable. The radar-chart triangle-area aggregation is a non-standard metric whose interpretation and sensitivity to scaling across axes are not discussed.

5. **Graph statistics are not reported.** The number of nodes, edges, average degree, and the dimensionality of the "All Dynamics" state vector are never given for the three test subgraphs. This information is essential to interpret the CR values, the computational claims, and the generality of the findings.

### Trivial

6. The paper does not specify how multiple top-k shortest paths are computed (e.g., whether they are distinct paths, and if so, how diversity is ensured). This is a minor implementation detail that should be clarified.

## Nice-to-Haves

- The PSR grounding in Section 4.2 is asserted but not developed. The paper would benefit from either showing how the constructed features satisfy PSR conditions, or removing the connection as unnecessary.
- The paper tests only travel time as the dynamic cost. Testing on additional objectives (e.g., energy consumption, multi-criteria) would strengthen the generality claim.
- A discussion of how the method handles topology changes (road closures, new roads) would be useful, since the paper notes that the distance-based policy assumes a fixed graph.

## Removed Points

The following points from the reviewer inputs were removed with justification:

- **Criticism about "missing appendix, missing proofs"** — Removed per instructions: the parser strips appendices from all papers; they exist in the original submission.
- **Criticism about comparison fairness favoring the author's method** — The harsh critic's concern about unfair comparison is not applicable; the asymmetry (AD vs. DFR) favors the baseline, not the author's method.
- **Claim that the PSR section is "gratuitous"** — This is a judgment about theoretical framing depth, not a concrete weakness. The PSR connection is a reasonable conceptual grounding even if not fully developed.
- **"The claim of generality is unsupported"** — The paper tests 3 RL algorithms on 3 real graphs, which is a reasonable scope. The claim is appropriately qualified.
- **Formatting/style nitpicks and typo concerns** — Removed per instructions as parser artifacts.
- **Strength Finder's generic strengths** (e.g., "this paper addressed an important problem") — Removed per instructions: these are generic and lack specific content.
- **Criticism about wall-clock training time** — The paper reports planning time per query, which is the relevant metric for real-time deployment. Training time is a secondary concern.
- **Criticism about graphs changing (road closures)** — This applies to any graph-based method and is not specific to DFR. The paper acknowledges the assumption of fixed topology.

## Novel Insights

The harsh critic's observation that the CR metric likely has a definitional or implementation error is the most valuable novel insight. This is a concrete, verifiable problem that the authors must fix. The critic's suggestion to validate the distance-based subgraph assumption with an offline overlap analysis is also a practical and specific recommendation that would substantially strengthen the paper. Beyond these, the reviews do not reveal genuinely novel insights beyond the paper's own contributions.

## Suggestions

1. Fix the CR metric definition and ensure the reported values are consistent. Most likely, the CR values need to be re-normalized so that the AD case yields 1.0 (100%). Replot the radar charts and re-evaluate any claims about dimensionality reduction.
2. Add at least two control baselines: (a) a random subgraph of comparable size to DFR, and (b) a local-only (n-hop without policy attention) baseline. This is essential to demonstrate that DFR's specific design, not just dimensionality reduction, drives the improvements.
3. Run all experiments with at least 3–5 random seeds and report means and standard deviations for all metrics.
4. Add an offline validation of the core assumption: compute the overlap between the optimal dynamic (time-based) paths and the static-distance subgraph on the test data, and report the fraction of optimal-path edges that lie outside the DFR subgraph.
5. Report basic graph statistics (nodes, edges, average degree, AD state dimension) for each test subgraph.

## Score and Decision

**Calibration anchors:**

**Round 1 (bracketing):**
- **NIhRwzqhUz.md** (avg 3.0, weak band): Dynamic TSP paper, rejected. Weaker than current paper — less clean problem framing, less convincing experiments.
- **Gs8jWk0F01.md** (avg 2.2, weak band): Dynamic CVRP paper, rejected. Significantly weaker — limited novelty and poor experimental design.
- **4lqA5EuieJ.md** (avg 4.75, middle band): Graph prediction/interpretability paper, rejected. Comparable in overall quality — has a similar gap between a nice idea and incomplete validation.
- **nIEjY4a2Lf.md** (avg 6.0, middle band): Misspecified Q-learning theory paper, accepted. Stronger than current paper — rigorous theoretical analysis with tight bounds.
- **x7Q0uFTH2a.md** (avg 3.75, middle band): Bisimulation metrics paper, rejected. Weaker than current paper — writing quality issues and questionable theoretical claims.
- **5RUf9nEdyC.md** (avg 6.0, middle band): TEDDY graph sparsification, accepted. Stronger than current paper — more thorough experiments, clearer ablation.
- **9pW2J49flQ.md** (avg 8.0, strong band): DeepLTL paper, accepted. Significantly stronger — rigorous theoretical framing and comprehensive experiments.

**Round 2 (narrowing within bracket):**
- **Pj3ErOxlLo.md** (avg 6.0): NaviFormer, rejected. Slightly stronger than current paper — had comprehensive ablations and multiple datasets, but was rejected due to novelty concerns. Current paper has more novel methods but weaker experimental validation.
- **ZiF1bJ9K6B.md** (avg 4.75): Coverage path planning, rejected. Comparable to current paper — a reasonable RL-for-planning paper with solid experiments but limited novelty.
- **2NpAw2QJBY.md** (avg 5.25): Neural MAPF, accepted. Slightly stronger than current paper — cleaner problem framing and more convincing experiments despite some novelty concerns.
- **z3L59iGALM.md** (avg 5.25): Google Maps IRL, accepted. Comparable quality — real-world impact but mixed reviews on novelty. Current paper is more methodologically novel but less validated.
- **RB0RQ3XkYB.md** (avg 4.67): HLCA motion planning, rejected. Slightly weaker than current paper — the approach is less clearly motivated and the experimental evidence is thinner.

**Round-1 bracket:** Between 3.5 and 7.5, with the paper clearly above the weak band (3.0–3.75) and below the strong band (7.5+).

**Round-2 narrowing:** The paper sits between the 4.75–5.25 cluster (papers with moderate contributions and incomplete validation) and the 6.0 cluster (stronger papers with more thorough experiments). The CR metric inconsistency and limited baselines are concrete issues that place it below the 6.0 anchors. Compared to the 5.25 anchors (MAPF, Google Maps IRL), it has a more novel methodological contribution but weaker experimental validation. The paper is closest in quality to the 4.75–5.25 cluster.

**Final score: 5.0.** The paper has a genuine contribution and a well-motivated approach, but the CR metric inconsistency, limited baselines, and absence of statistical rigor prevent it from being acceptable at a top venue in its current form. The authors should address these issues in a revision.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>