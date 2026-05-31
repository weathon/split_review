Now let me perform calibration searches to determine the appropriate score.**Round 1 bracket: ~3.5 to 5.5.** The paper is above the weak (2.5–3.0) anchors but well below the strong (8.0) anchors. Let me narrow within this range.Now I have enough calibration anchors to write the final review. Let me synthesize everything.

**Calibration summary:**
- Dynamic TSP (3.0): limited novelty, no ablation, minimal baselines — worse than paper under review
- GCHRL subgoal (3.50): limited comparisons, limited settings — roughly comparable
- PSR GNN (4.80): cleaner benchmarks but limited scope — slightly better than paper under review
- NaviFormer (6.0): multi-dataset, ablations, competitive baselines — clearly stronger

**Round 1 bracket: 3.0–5.5**
**Round 2 narrowing: 3.0–4.5.** The paper is below the PSR (4.80) anchor (which used established benchmarks and cleaner experiments) and comparable to or slightly above the GCHRL (3.50) anchor. The AD baseline weakness is more severe here than the "insufficient comparisons" issue in GCHRL, but the DFR paper has more systematic ablations and multi-city evaluation. Final placement: **3.5**.

---

## Summary

This paper proposes the Dynamics Feature Representation (DFR) framework, a two-stage hierarchical state reduction approach for reinforcement-learning-based dynamic path planning on urban road networks. DFR first uses a pre-trained distance-based policy to identify the top-*k* shortest paths and form a task-relevant subgraph (called "policy attention"), then further restricts the state to *n*-hop neighborhoods around the current agent node. Experiments on three Chinese urban subgraphs (Nanjing, Beijing-Chaoyang, Shanghai-Pudong) with three RL algorithms (DQN, PPO, GCN+DQN) show improvements in success rate, mean GAP, and planning time over an All-Dynamics (AD) baseline.

---

## Strengths

- **Cross-algorithm and cross-city consistency (Section 5.2, Figure 5):** DFR-enhanced models produce larger radar-chart triangles (measuring 1−GAP, SR, and 1−CR) over all three RL algorithms and all three urban subgraphs, providing a systematic picture rather than cherry-picked results.
- **Quantified planning-time reduction:** Section 5.2 reports concrete planning-time improvements: 85.59% reduction for DQN, 79.32% for PPO, and 46.08% for GCN+DQN versus their AD counterparts, with mean planning times of 8.18 ± 1.74 ms (DQN/PPO) and 27.26 ± 6.8 ms (GCN+DQN).
- **Ablation study (Section 5.3, Figure 6):** A full heatmap grid over *k* ∈ {0.2, 0.4, 0.6, 0.8, 1.0, −1.0} and *n* ∈ {1, 2, 3, 4, −1} is provided, revealing an aggregation boundary for *n* and a more complex, non-monotone relationship for *k*—both are useful empirical observations about the trade-off between coverage and dimensionality.
- **Offline-precomputable subgraph:** Because the policy attention step uses only static graph topology (distances), the subgraph is pre-computed once and reused, keeping online overhead negligible. This is clearly explained in Section 4.3.

---

## Weaknesses

### Fatal
*None.*

### Major

- **AD baseline is a straw man, not a state-of-the-art comparison.** The sole competing state design ("All Dynamics") hands the complete global edge-weight vector to a 64-unit MLP. This is not how existing DPP or graph-RL practitioners represent state—giving a raw, high-dimensional edge vector to a small MLP is structurally guaranteed to perform poorly due to the curse of dimensionality alone. The paper's related work (Section 2) cites local-view methods (Zhao et al., 2025), global-view methods (Lin et al., 2025), and GNN-encoding methods (Du et al., 2024b) as distinct prior approaches, yet none appear as baselines. Without at least one realistic alternative—such as a fixed-radius local neighborhood, or GNN-encoded node embeddings from prior DPP work—it is impossible to determine whether DFR's gains come from the specific hierarchical design or simply from any state compression. This is the central evidentiary gap.

- **Compactness Rate (CR) exceeds 100%, contradicting its definition.** Section 5.1 defines CR as "the proportion of the reduced feature dimension after DFR to the original dimension, and lower is better." Figure 6's heatmap (reproduced in the paper's tables) reports CR = 121.042% for the baseline configuration (k=−1.0, n=−1) and CR = 95.640% and 75.514% for other n=−1 configurations. A proportion cannot exceed 100%. Either the metric is misdefined or the computation is erroneous. Since CR is one of three dimensions in Figure 5 and Figure 6 and directly supports the paper's efficiency claims, this inconsistency must be resolved.

- **Traffic dynamics generation process is not described.** Section 5.1 states that edge weights are parameterized by congestion factor β(v_i,v_j;t) ∈ [0.1, 1.5] and gives Equation 9, but never says how β evolves over time. Is it i.i.d. noise at each step, a stochastic process with autocorrelation, or drawn from real sensor data? This matters critically: DFR's PSR-grounded argument (Section 4.2) claims that W_t'' captures "temporally adjacent" dynamics and "local congestion propagation," but if β is i.i.d. per time step, there are no temporal correlations to capture and the temporal-dependency motivation disappears entirely.

- **Core convergence claim is not demonstrated.** The abstract states DFR "accelerates convergence compared to baselines." Figure 6 (bottom) shows training curves under k=0.6 for varying *n* values—but these compare DFR variants against *each other*, not against the DQN+AD baseline. The DQN+AD training curve does not appear on the same axes. The convergence claim is therefore asserted but not shown in the main text.

### Minor

- **Ablation conclusions generalized beyond their scope.** Section 5.3 concludes with the recommendation: "in large-scale graph deployment, configurations with moderate *k* and smaller *n* should be preferred." This recommendation is derived solely from experiments on Subgraph 1 (Nanjing), a small urban subgraph. Extrapolating this to "large-scale graph deployment" is not supported by the experiments.

- **Evaluation protocol is underspecified.** Section 5.1 says "each scenario corresponds to a single DPP task" but also says "source and goal nodes are randomly sampled" during 75,600 training episodes. The test-set size, OD sampling procedure, and number of held-out evaluation episodes are not stated in the main text. Without knowing whether results are averaged over 10, 100, or 1,000 test OD pairs, the precision of the reported improvements (e.g., mean GAP dropping from 0.170 to 0.095) cannot be assessed.

### Trivial

- The term "policy attention" suggests a learned, context-sensitive weighting, but the mechanism is a pre-computed hard selection of the top-*k* shortest paths via a static distance-based policy (Section 4.3). The paper acknowledges this is "hard, pre-computed attention," but the naming still creates unnecessary confusion with Transformer-style attention cited in Section 2.

---

## Nice-to-Haves

- Plotting DQN+AD and DQN+DFR training curves on the same axis would directly demonstrate the convergence claim made in the abstract.
- Specifying how β(v_i,v_j;t) is drawn (e.g., i.i.d. uniform, time-correlated Markov process, or real sensor traces) and showing autocorrelation statistics would ground the temporal-dependency justification.
- Including at least one prior-art DPP state representation—e.g., a fixed-radius local neighborhood, or a GNN-encoded state from an existing method—would allow readers to assess whether the hierarchical DFR design is essential or whether any dimensionality reduction strategy would produce similar gains.
- Reporting confidence intervals or standard deviations across multiple random seeds and OD pairs would clarify whether the reported improvements are statistically stable.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **PSR theoretical grounding is "decorative":** The harsh critic argues that the PSR claim is not formally proved. This is true—Equations 6, 7, 8 assert that optimal policies are approximately preserved, but no formal bound is given. However, this is common practice in applied RL/representation papers that invoke PSR as a conceptual framework. The PSR framing is informal but not dishonest. Demoted from Major to background context; not included as a standalone weakness.

- **"Not comparing with traditional DPP methods":** Footnote 3 explicitly states that RL's advantages over classical planners are well established. This is a scoping decision, not a weakness.

- **"Policy attention" naming critique:** The mechanism is clearly described (pre-computed, hard selection). The naming is imprecise but the paper acknowledges its nature. Trivial presentation concern, not a substantive flaw.

- **Claiming the paper lacks "missing related works":** Per hard rules, missing related work claims are removed as we cannot independently verify the existence of such works.

- **Strength Finder's "theoretical grounding via PSR":** The paper invokes PSR concepts but does not establish the formal conditions rigorously. Given the conflict with a verified weakness (informal PSR grounding), this claimed strength is removed.

---

## Novel Insights

None beyond the paper's own contributions. The DFR framework's hierarchical two-stage reduction (global-to-subgraph via policy attention, subgraph-to-local via *n*-hop) is a sensible engineering heuristic applied to RL-based DPP. The empirical finding that *n* has a well-defined "aggregation boundary" (performance plateaus beyond n=2–3) and that *k* has a non-monotone effect on performance are modest but useful practical observations for hyperparameter tuning in this setting.

---

## Suggestions

1. **Fix the CR metric.** Determine the correct formula and verify that all reported values fall in [0%, 100%]. If the AD baseline has no reduction (CR = 100%), make that explicit, and explain why k=−1.0 / n=−1 entries with policy attention or hop selection still have CR > 100%.
2. **Describe the dynamics model.** Add at least one sentence in Section 5.1 specifying the stochastic process governing β(v_i,v_j;t): its distribution, temporal autocorrelation, and whether it is calibrated to real traffic data or synthetic.
3. **Add a realistic local-view baseline.** Implement a fixed-radius neighborhood as a control: give the RL agent the edge weights within *r*-hop of the current node on the full graph, without any policy-attention subgraph filter. This directly tests whether the policy-attention step is necessary or whether any local state reduction works equally well.
4. **Show convergence curves against AD.** Plot DQN+AD and DQN+DFR (best *k*, *n*) on the same training axis to directly support the abstract's convergence claim.
5. **Specify the test set.** State the exact number of test OD pairs, whether they are held-out from training, and how they are sampled, so that reported metrics can be properly interpreted.

---

## Score and Decision

**Calibration anchors:**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| NIhRwzqhUz.md (Dynamic TSP) | 3.00 | R1 | Weaker: no ablation, less systematic experiments |
| 1OGhJCGdcP.md (GCHRL subgoal) | 3.50 | R2 | Comparable: limited comparisons, limited settings |
| sEv6vHIUnu.md (PSR GNN) | 4.80 | R2 | Stronger: cleaner benchmark, better-specified experimental setup |
| Pj3ErOxlLo.md (NaviFormer) | 6.00 | R2 | Clearly stronger: multi-dataset, competitive baselines, well-scoped claims |

**Round 1 bracket: 3.0–5.5.**
**Round 2 narrowing: 3.0–4.5.** The paper sits below the PSR anchor (4.80) primarily because: (a) the PSR paper uses a well-established benchmark with cleaner experimental design, whereas this paper's AD baseline is a straw man; (b) the CR metric anomaly is an uncorrected error in one of three headline metrics; (c) the dynamics model is entirely unspecified. The paper is at or slightly above the GCHRL anchor (3.5) because it does include multi-algorithm, multi-city experiments and a systematic ablation—more coverage than the GCHRL paper. However, the AD baseline weakness is *more* severe here: the comparison tells us DFR beats a design no one would actually use, leaving the actual improvement over real alternatives unknown.

**Final score: 3.5**

**Axes:**
- *Originality:* Low–moderate. The hierarchical k-shortest-path subgraph + n-hop local state reduction is sensible but not a significant methodological advance; it is closer to a well-motivated engineering choice than a conceptual contribution.
- *Importance of research question:* Moderate. DPP on urban networks is practically relevant.
- *Claims well supported:* Weak. The core comparative claim depends on an unrealistically weak baseline; the convergence claim is undemonstrated in figures; the CR metric has an unexplained anomaly.
- *Soundness of experiments:* Weak–moderate. Three cities, three algorithms, and an ablation study are positive, but the missing dynamics model specification and underspecified test protocol compromise interpretability.
- *Clarity of writing:* Acceptable, though several key experimental details are absent from the main text.
- *Value to research community:* Limited in current form; would increase substantially if the baseline and evaluation gaps were addressed.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>