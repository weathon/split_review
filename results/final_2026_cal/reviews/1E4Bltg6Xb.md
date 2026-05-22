Now I have enough calibration data. Let me write the consolidated review.

**Round 1 bracket**: Based on comparison with weak anchors (2.50–3.33, rejected papers), middle anchors (4.50–6.00, accepted posters), and strong anchors (8.00, strong accepts), I initially bracket this paper between 4.5 and 6.0.

**Round 2 anchors**: Reading SLAP (5.00, accepted poster) — similar contribution structure but weaker evaluation; Strict Subgoal Execution (5.00) — comparable in evaluation quality; Graph-Theoretic Intrinsic Reward (4.67) — similar mixed reviews; RsGCN (5.00, rejected with scores 4,6,4,6). The DFR paper stands above the 4.67–4.50 papers but is comparable to the 5.00 papers. It lacks the polish and rigor of 6.00 papers like DriveMamba.

**Final score**: 5.0. It has a clear, practical contribution and reasonable empirical support, but the baseline comparison is limited and the core design assumption is unvalidated.

---

## Summary

This paper addresses the global-vs-local state representation trade-off in RL-based Dynamic Path Planning (DPP) on urban road networks. The authors propose DFR, a hierarchical framework that first uses a pre-trained distance-based policy to extract a task-relevant subgraph (policy attention), then applies n-hop neighborhood selection to produce a compact, node-centric state. Experiments on three real-world city networks (Nanjing, Beijing Chaoyang, Shanghai Pudong) with three RL algorithms (DQN, PPO, GCN+DQN) show that DFR reduces planning time by 46–86% while maintaining or improving solution quality relative to a full-dynamics (AD) baseline.

## Strengths

- **Hierarchical refinement is well-motivated and yields measurable improvements.** DFR's two-stage compression (policy attention → n-hop neighborhoods) demonstrably resolves the global–local trade-off: Section 5.2 reports 85.59% planning-time reduction for DQN+DFR vs DQN+AD, while Figure 5 shows DFR-augmented models consistently achieve larger radar-triangle areas across all three algorithms and city subgraphs. This is direct evidence that DFR delivers useful compression without sacrificing decision quality.

- **Systematic ablation isolates the contribution of each component.** Section 5.3 provides a full grid of (k, n) combinations on Subgraph 1 (Figure 6, heatmaps). The ablation shows that disabling policy attention (k = −1.0) raises Mean GAP from 0.095 to 0.176, and reducing n from 4 to 1 similarly degrades performance. This gives convincing evidence that both stages of the pipeline contribute, and that the method is not just benefiting from dimensionality reduction alone.

- **Method is clean, interpretable, and offline-computable.** The policy attention subgraph is derived from a one-time pre-trained static shortest-path policy; the n-hop neighborhoods depend only on fixed topology. Both are pre-computable and reusable, incurring no online overhead. This makes the framework practically appealing for real-time urban routing.

- **Evaluation spans multiple RL paradigms and real networks.** Experiments use DQN (value-based), PPO (policy-gradient), and GCN+DQN (graph-based) on three real OSM-sourced city networks with different topologies and sizes. This breadth strengthens the claim that DFR is a general state-representation tool rather than a trick tuned to one algorithm.

## Weaknesses

### Major

- **Only compared against an infeasible baseline (All Dynamics).** The AD baseline feeds *all* edge weights as the state. With subgraphs containing 3,890+ edges, AD is a strawman — no practitioner would use it. The ablation study compares DFR variants against each other (e.g., k = −1.0, n = −1) but never against alternative principled compression methods of the same budget: random subgraph extraction, traffic-weighted (rather than distance-weighted) subgraph selection, or a learned embedding (e.g., an autoencoder on the full dynamics). Without these, the paper cannot attribute its gains to the *specific* distance-based policy attention mechanism rather than to the generic fact that dimensionality reduction helps. This is the paper's most significant evidential gap.

- **The core design assumption is unvalidated.** DFR's policy attention uses static shortest-distance paths to select the subgraph. The DPP objective, however, minimizes time-based traffic cost (Eq. 2), where a longer-distance but congestion-free route can be far cheaper. The paper offers no argument — empirical or theoretical — that the top-k distance-shortest paths are likely to contain the time-optimal path. The PSR grounding (Section 4.2) is too abstract to bridge this gap: it describes what a good state *should* do but does not prove the distance-filtered subgraph satisfies those requirements. The strong empirical results suggest the concern may not be fatal in practice, but the paper should at minimum report the overlap rate between DFR's subgraph and the ground-truth optimal path as a function of k.

- **No statistical significance reported for main metrics.** The paper reports mean GAP, SR, and CR as point estimates with no error bars, confidence intervals, or number of test episodes. Only planning time is reported with standard deviation (±). Given the stochasticity in RL training and scenario sampling, variance measures are essential. Similarly, the number of test queries used for evaluation is not stated.

### Minor

- **Convergence claim is unsupported.** The abstract and contributions claim "remarkable acceleration in convergence," but no learning curves comparing DFR against AD are provided. Figure 6 (bottom) shows curves only for different n values *within* DFR, not a DFR vs. AD convergence comparison.

- **Ablation study limited to one subgraph and one algorithm.** The full (k, n) ablation in Section 5.3 is run only on Subgraph 1 (Nanjing) with DQN. Generalizability of the parametric trends to other graphs and algorithms (PPO, GCN+DQN) is not established.

- **Congestion model is simplistic.** The dynamics model uses a time-varying congestion factor β ∈ [0.1, 1.5] applied uniformly per edge, without spatial/temporal correlations (rush-hour waves, incident propagation). Whether DFR's distance-based filtering remains effective under more realistic dynamics is unclear and should be explicitly discussed as a limitation.

- **Scalability experiments on full city graphs are missing.** The experiments use 1–3 km radius subgraphs. The conclusion that "moderate k and smaller n should be preferred" for large-scale deployment (Section 5.3) is drawn from small-scale experiments without validation on the full city networks.

### Trivial

None.

## Nice-to-Haves

- Adding learning curves comparing DFR against AD (not just within-DFR variants) would substantiate the convergence claim.
- Reporting the overlap ratio between DFR's subgraph and the ground-truth optimal path as a function of k would directly validate the core design choice.
- Evaluating DFR with a more realistic traffic dynamics model (e.g., with spatial propagation) would strengthen claims of practical applicability.

## Removed Points

- "The planning time reduction claim is not a meaningful contribution — it is a direct consequence of the compression." — This is too dismissive. Showing that a specific compression achieves 85% reduction *while maintaining or improving* solution quality is meaningful. However, the point about comparing against other compression methods is kept in the Major weaknesses.
- "Beating AD is uninformative — it merely shows that dimensionality reduction helps." — Reformulated into the more precise critique that the paper lacks comparison against *other* principled compression methods.
- "Dynamic model realism — 'extremely simplistic'" — Downgraded to Minor. The model is simple but adequate for the paper's purpose of evaluating a state-representation method; it is a limitation worth flagging but not a fatal flaw.
- "The paper should report planning time relative to comparable compression methods" — Merged into the Major weakness about missing alternative compression baselines.
- "Missing parts: statistical significance, scenario count, convergence evidence" — All kept as Minor weaknesses because they are genuine gaps but none individually threatens the paper's core claims.
- "Scalability discussion unsupported" — Kept as Minor. The paper is transparent about using subgraphs; the extrapolation to full graphs is a reasonable directional suggestion from small-scale data, not a claim of proven scalability.
- Generic strengths from the Strength Finder ("the paper addresses an important problem," "realistic and diverse evaluation") were trimmed to avoid puffery, keeping only concrete, evidence-backed strengths.

## Novel Insights

None beyond the paper's own contributions. The key insight — using a static distance policy to produce a task-aware subgraph for RL-based DPP — is presented clearly in the paper. The reviews surface concerns about validating this assumption and broadening the baseline set, but do not uncover new latent contributions.

## Suggestions

1. **Add at least two alternative compression baselines:** (a) a subgraph formed by traffic-weighted shortest paths from historical averages, and (b) a random subgraph of the same dimensionality as DFR's output. This would directly test whether DFR's *distance-based* attention mechanism provides unique value.
2. **Validate the filtering assumption:** Report the fraction of test scenarios where the ground-truth (time-)optimal path lies entirely within DFR's extracted subgraph, as a function of k. A high ratio would substantiate the method's foundation; a low ratio would indicate the need for a different extraction criterion.
3. **Report variance:** Add error bars or confidence intervals for GAP, SR, and CR across multiple training seeds. State the number of test episodes used for evaluation.
4. **Add DFR vs. AD learning curves** to support the convergence acceleration claim.
5. **Discuss limitations explicitly:** Add a paragraph on why distance-based filtering may or may not capture time-optimal paths, and acknowledge the simplified congestion model as a scope limitation.

## Score and Decision

**Calibration anchors used:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| bisWxwcK8D (RL vehicle routing) | 2.50 | 1 | Much weaker — rejected, narrower scope and weaker evaluation. |
| MKM8iEaowV (trajectory planning) | 3.00 | 1 | Weaker — rejected, limited empirical validation. |
| UOYkiemcUP (autonomous driving RL) | 3.33 | 1 | Weaker — withdrawn/rejected, less thorough. |
| enprG5H9aD (SLAP) | 5.00 | 1,2 | Comparable — similar contribution structure but DFR has more systematic ablation. |
| VqnBaeu43F (policy compression) | 6.00 | 1 | Stronger — cleaner evaluation, but tested in fewer environments. |
| W8bKDPf1Ko (graph-theoretic reward) | 4.67 | 2 | Weaker — mixed reviews, narrower applicability. |
| cMpOvMuyYa (Strict Subgoal Execution) | 5.00 | 2 | Comparable — similar evaluation rigor. |
| gklDob3vVM (RsGCN) | 5.00 | 3 | Similar score — both have clear contributions but limited baselines; RsGCN was rejected, DFR has broader evaluation. |

**Round 1 bracket:** 4.5–6.0. **Round 2 narrowing:** Compared against SLAP (5.00), Strict Subgoal Execution (5.00), Graph-Theoretic Reward (4.67), and RsGCN (5.00). DFR has a clearer practical contribution than Graph-Theoretic Reward and similar evaluation rigor to SLAP and SSE. Loses points vs. 6.00 papers due to the AD-only baseline comparison and missing statistical rigor.

<score>5.0</score>
<decision>Accept</decision>