Now I have a clear picture from all the anchors. Let me finalize the comparison.

**Round 1 bracket: 4.5 to 6.5**

**Round 2 comparison:**
- **sEv6vHIUnu (4.80)**: GNN for predictive representations. Incremental contribution (replace MLP with GNN), limited to 4 MiniGrid tasks. Our paper is clearly stronger — more novel mechanism, real-world graphs, systematic ablation, cross-validation.
- **z3L59iGALM (5.25)**: IRL at Google Maps scale. Most topically similar. Real-world deployment but mostly engineering contributions, static features only, outdated methods. Our paper is stronger in novelty of mechanism and addresses the dynamic case.
- **Pj3ErOxlLo (6.00)**: NaviFormer, joint route+path planning with Transformers. Similar profile — novel architecture, real data, ablation, but limitations in baselines and environments. Our paper has comparable strengths but the PSR overclaim and undefined ground truth pull it slightly below.
- **i8PjQT3Uig (6.67)**: Sparse encoding for world models. Cleaner contribution, better theoretical grounding, more comprehensive experiments. Our paper is clearly below this level.

Our paper sits between z3L59iGALM (5.25) and Pj3ErOxlLo (6.00), closer to the latter but pulled down by the unsupported theoretical claims and undefined evaluation metric. **Final score: 5.5**.

---

## Summary

This paper proposes DFR (Dynamics Feature Representation), a hierarchical framework for compressing global traffic dynamics into compact, decision-relevant state features for RL-based dynamic path planning (DPP) in urban road networks. DFR uses (1) a pre-trained distance-based policy to identify top-k shortest paths and extract a task-relevant subgraph, then (2) n-hop neighborhoods intersected with that subgraph to produce agent-centric local features. Experiments on three urban road networks with three RL algorithms (DQN, PPO, GCN+DQN) show DFR improves performance while dramatically reducing feature dimensionality.

## Strengths

- **Clear problem framing with principled motivation**: The paper articulates the completeness-efficiency trade-off in state representation for RL-based DPP well (Section 4.1), providing a principled rationale for why hierarchical refinement is needed rather than merely an engineering convenience.

- **Novel policy attention mechanism with a useful invariance insight**: Using a distance-based policy pre-trained on static shortest paths to identify task-relevant subgraphs is clever. The observation that inter-node distances are time-invariant (depending only on topology, line 149) means this pre-training is one-time and offline, decoupling expensive global sparsification from the online RL loop.

- **Systematic ablation study with granular evidence**: The heatmaps across k and n parameters (Section 5.3, Figure 6) provide detailed evidence of how the two components interact. At k=0.4, n=2, CR=1.474% (~98.5% compression) while Mean GAP improves from 0.170 (AD baseline) to 0.102 and SR improves from 0.884 to 0.895 — demonstrating that the compression actively removes noise rather than merely losing information.

- **Cross-algorithm and cross-geography validation**: Three RL algorithms (DQN, PPO, GCN+DQN) and three real OpenStreetMap urban graphs (Nanjing, Beijing Chaoyang, Shanghai Pudong) provide evidence that benefits are not algorithm- or geography-specific.

- **Practical planning-time speedups**: DFR reduces planning time by 85.59% (DQN), 46.08% (GCN+DQN), 79.32% (PPO), with absolute times of ~8ms for DQN/PPO, suggesting real-time applicability.

## Weaknesses

### Fatal

None.

### Major

- **Ground truth evaluation metric is undefined and its appropriateness is unclear**: The primary metric (Mean GAP) is computed against "the dynamic Dijkstra algorithm" (line 175), but this algorithm is never defined anywhere in the paper. It is unclear whether this computes the clairvoyant optimum from Equation 1, a myopic step-by-step optimum, or something else. Without a definition and justification, the experimental results cannot be interpreted at face value — a lower Mean GAP might indicate the policy is closer to the MDP optimum, or merely that it happens to resemble whatever algorithm was used. This must be clarified in rebuttal.

- **PSR theoretical claims are unsupported and misleading**: Section 4.2 (lines 129–135) invokes Predictive State Representations to claim that DFR "guarantees" compactness and theoretical sufficiency (line 135). The paper does not construct PSR core tests, does not prove any sufficiency condition, and does not demonstrate that W_t'' satisfies any PSR property. The phrase "From the PSR perspective, this design enables W_t'' to function as a predictive summary" is a conceptual analogy, not a theoretical result. The word "guarantees" is unjustified given the absence of any formal construction.

- **Static-distance filter has an unexamined structural limitation**: The policy attention mechanism selects edges based on top-k shortest paths under static distance only (Section 4.3, lines 141–143). If the true optimal dynamic path uses edges outside this set — because heavy congestion on the static shortest paths makes a longer detour faster — DFR cannot represent the relevant dynamics and cannot learn the optimal policy. The paper justifies the distance-based filter by arguing that "distance naturally serves as one of the most fundamental constraints" (line 149), but provides no analysis of how often the filter excludes edges that the optimal dynamic path actually uses, no bound on the suboptimality gap, and no empirical study of whether the excluded edges ever matter. The noisy relationship between k and performance (Mean GAP rises from 0.095 at k=0.4 to 0.113 at k=0.6 for n=4 in the heatmap) is consistent with the filter being imperfect, but the paper does not investigate this.

### Minor

- **Temporal correlation claim is overstated**: Section 4.2 claims DFR "implicitly captures short-term temporal correlations" and "operates over the sequential structure W_{:T} rather than on a single snapshot" (line 133). In fact, the policy attention and n-hop operations are applied to W_t independently at each timestep; there is no recurrent mechanism, no temporal aggregation, and no conditioning on past dynamics. The claim should be removed or substantiated with evidence.

- **Ablation conducted on only one region**: The parameter sensitivity analysis (Section 5.3) is performed only on Subgraph 1 (Nanjing). The recommended parameter selection strategy (line 253) is thus based on a single datapoint, limiting confidence in its generality.

- **No statistical reporting for key metrics**: Mean GAP and SR are reported as point estimates without confidence intervals, standard deviations, or information about how many random seeds were used. In the heatmap (Figure 6), the reader cannot assess whether differences between e.g. SR=0.764 and SR=0.861 are statistically meaningful.

### Trivial

- **RL for static shortest paths is unexplained**: Section 4.3 uses RL to train π_d* for static shortest paths, but Dijkstra's algorithm solves this optimally in polynomial time. The paper does not explain why RL is needed for this pre-training step, or whether π_d* recovers true shortest paths or approximates them — which matters because approximation error propagates into which edges DFR includes.

- **Radar-chart visualization obscures quantitative comparison**: Figure 5 uses triangle areas to summarize three metrics with incomparable units and scales (1-GAP, SR, 1-CR), making precise quantitative comparison difficult. Standard tables alongside would improve interpretability.

## Nice-to-Haves

- Adding compression-matched baselines (e.g., random edge subsampling at matched CR) as explicit baselines in main results rather than only comparing against the full-dynamics AD baseline.
- Characterizing the filter's blind spot empirically: what fraction of edges used by optimal dynamic paths fall outside the top-k static shortest path subgraph?
- Testing on dynamics with spatial/temporal correlations rather than independent per-edge β sampling to better reflect real traffic conditions.
- Extending the ablation study to all three regions for more robust parameter guidance.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **Harsh Critic claim that "dynamic Dijkstra" is "myopic" and "provably suboptimal"** — REMOVED because this depends on assuming what "dynamic Dijkstra" means, which is not stated in the paper. The criticism about ambiguity of the ground truth is retained as Major Weakness 1, but the specific claim about suboptimality is speculative and unverifiable from the paper as written.

2. **Harsh Critic claim that the evaluation has a "critical flaw" making all results uninterpretable at face value** — DEMOTED from fatal to major. The paper does fail to define its ground truth algorithm, which is a real problem, but whether this rises to "fatal" depends on what "dynamic Dijkstra" actually is, which we cannot determine from the paper.

3. **Strength Finder "Theoretical grounding in Predictive State Representations"** — REMOVED as a strength because the harsh critic correctly identifies these claims as unsupported. The PSR language inflates rather than strengthens the contribution; it is listed as Major Weakness 2.

4. **Strength Finder "Explicit acknowledgment of limitations with a clear path forward"** — REMOVED as too generic to count as a substantive strength. Acknowledging limitations is standard practice, not a contribution.

5. **Harsh Critic demand for compression-matched baselines (random edge subsampling, GNN encoder)** — DEMOTED from major to Nice-to-Have because the ablation study already compares against no-policy-attention (k=-1.0) and no-n-hop (n=-1) variants, which serve as partial baselines isolating each component's contribution.

6. **Harsh Critic claim that "β produces independent, per-edge dynamics — no spatial or temporal correlation" is a weakness** — REMOVED as a standalone weakness. Simplifying assumptions in initial studies are not inherently problematic. Moved to Nice-to-Haves as a suggestion for more realistic evaluation.

7. **Harsh Critic section note about Equation 1 vs MDP ambiguity** — REMOVED because the paper explicitly states on line 57 that Equation 1 is "a theoretical benchmark for evaluating other strategies" since future dynamics are unknown in practice. The relationship between the two formulations is adequately clarified.

8. **Harsh Critic concern about "unexpected events like accidents or road closures" not reflected in experiments** — REMOVED. The introduction's mention of unexpected events is motivation/context, not a claim about what the experiments test. This is standard in papers and not a weakness.

## Novel Insights

None beyond the paper's own contributions. The hierarchical decomposition of state representation into task-relevant subgraph followed by agent-centric local features is a sensible design pattern that may be applicable beyond DPP, but the reviews do not surface genuinely novel insights beyond what the paper itself contributes.

## Suggestions

- Define "dynamic Dijkstra" explicitly and justify why proximity to its output measures policy quality under the MDP objective. If it is the clairvoyant optimum from Equation 1, state this clearly and explain the algorithm used to compute it. If it is something else, justify its use as ground truth.
- Either construct a proper PSR argument showing W_t'' satisfies a sufficiency condition, or remove the word "guarantees" and rephrase the PSR discussion as conceptual inspiration rather than theoretical foundation.
- Acknowledge and characterize the static-distance filter limitation: under what conditions might the optimal dynamic path use edges outside the top-k static shortest paths, and what does this imply for DFR's applicability?
- Add standard deviations or confidence intervals for Mean GAP and SR, and report the number of random seeds used.

## Calibration Summary

Round 1 bracketing placed this paper between 4.5 and 6.5. Round 2 anchors:
- sEv6vHIUnu (4.80, Reject) — GNN for predictive representations: our paper is clearly stronger (more novel mechanism, real-world data, systematic ablation)
- z3L59iGALM (5.25, Accept) — IRL at Google Maps scale: our paper has more novelty in mechanism, but z3L59iGALM has real-world deployment; our paper is comparable or slightly better
- Pj3ErOxlLo (6.00, Reject) — NaviFormer: similar strengths/weaknesses profile; our paper is slightly below due to unsupported theoretical claims and undefined evaluation metric
- i8PjQT3Uig (6.67, Accept) — Sparse encoding for world models: our paper is clearly below this level (cleaner contribution, better theoretical grounding)

The paper's genuine novelty and systematic ablation are offset by three major weaknesses: an undefined ground truth, unsupported theoretical claims, and an unexamined structural limitation. Score: 5.5.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>