## Summary

This paper introduces Forest-Based Graph Learning (FGL), a semi-supervised node classification paradigm that models message passing as propagation over sampled spanning trees. The core insight is that spanning trees are the minimal globally-covering subgraphs, enabling long-range information propagation without the depth-cost tradeoff of deep GNNs or the quadratic complexity of graph transformers. The method includes: (1) graph augmentation via pseudo-labels for connectivity; (2) a homophily-guided tree sampler with theoretical guarantees (Theorem 2); (3) a general linear-time tree aggregator (Theorem 1); and (4) a tree fuser combining multiple trees. Experiments on 9 benchmarks with 26 baselines show the best average rank (1.22) and strong efficiency gains, particularly on heterophilous graphs.

## Strengths

1. **Novel paradigm with clean theoretical motivation.** The cost decomposition (Eq. 1: Total cost = cost per structure × number of structures) provides an elegant lens for why both deep local and shallow global models are suboptimal, and positions spanning trees as a principled intermediate structure. This framing is genuinely insightful and distinguishes the paper from incremental GNN work.

2. **Rigorous theoretical grounding for homophily-guided sampling.** Theorem 2 establishes monotonicity, an upper bound, and asymptotic tightness for the expected tree homophily ratio as a function of the edge score ratio Δ = p/q. This gives a formal foundation for the sampling strategy, linking estimator quality to tree distribution quality.

3. **General tree aggregator with provable linear complexity.** Theorem 1 derives a two-recursion tree aggregator (Eqs. 5–8) that works for any aggregator satisfying Properties (I) and (II), with a concrete linear implementation. Section 4.5 confirms overall O((n+m)Kd) complexity. The generality claim is supported by explicit connections to linear attention, RNNs, and SSMs.

4. **Consistently strong empirical results.** Table 1 shows best average rank (1.22) across 9 diverse benchmarks, with highest accuracy on 6 of 9 datasets. On heterophilous graphs, gains are substantial (e.g., Cornell: 83.24 vs. next best 76.76; Texas: 91.89 vs. next best 78.92). The method also tops Arxiv (56.47) and Flickr (47.22).

5. **Competitive efficiency.** Table 2 shows wall-clock time per epoch beating all strong baselines (e.g., 0.005s on Cora vs. 0.010s for SGFormer; 0.246s on Arxiv vs. 0.545s for DIFFormer). This is a significant practical advantage.

6. **Well-designed ablation study.** Table 3 systematically isolates each component — uniform vs. homophily-guided sampling, single-tree vs. forest, with/without local/global submodules — cleanly validating the design choices. Figure 5 shows a clear monotonic relationship between estimator quality (p) and accuracy, bridging theory and practice.

## Weaknesses

### Fatal
None.

### Major

1. **Confounded effect of graph augmentation and forest paradigm.** The pre-processing step (Sec. 4.1) augments the graph by adding edges based on pseudo-labels, improving connectivity and homophily. The ablation in Table 3, row (1) — which removes only the global submodule while keeping the local module on the augmented graph — achieves 82.88% on Texas and 83.92% on Wisconsin. These numbers already far exceed baselines like GCNII (69.19%, 70.31%). This indicates that a substantial portion of the performance gain may stem from the augmented graph itself rather than the forest aggregation. The paper does not provide a controlled comparison where strong baselines (e.g., GCNII, SGFormer) also receive the same augmented graph, making it difficult to disentangle the benefit of the forest paradigm from the benefit of augmentation. This is the most significant evidential gap and weakens the claim that the forest paradigm is the primary driver of gains.

2. **Misleading claim about "quadratic node-pair interactions" with linear complexity.** The abstract and contribution list state that the tree aggregator "realizes quadratic node-pair interactions" in linear time. In a tree of n nodes, there are O(n²) node pairs. The aggregator enables global information flow (each node's embedding integrates information from all other nodes via tree paths), but it does not explicitly model or compute pairwise interactions — there are no pairwise dot products or attention weights between distant nodes. The phrasing implies a stronger computational claim (implicitly computing all O(n²) pairs in O(n) time) than what is actually demonstrated. What the method achieves is *global context integration* via tree-structured propagation, not quadratic pairwise computation. This should be clarified.

### Minor

1. **Theory-practice gap in homophily estimation.** Theorem 2 assumes a clean separation of edges into homophilous (score p) and heterophilous (score q), with known p and q. In practice, the homophily estimator produces noisy, continuous attention scores trained on pseudo-labels. While Figure 5 empirically shows that higher p correlates with better accuracy using synthetic variation, and Table 4 compares estimator variants, the paper does not directly characterize how far the learned estimator is from the idealized setting of Theorem 2 on real data. An empirical plot showing estimated edge-score ratios vs. actual homophily ratios of sampled trees on real datasets would tighten the theory-practice connection.

2. **Unmotivated local module architecture.** The local module (Eq. 9) combines three terms — normalized adjacency, attention matrix, and identity — with hyper-parameters β₁, β₂ controlling their weights. The specific form and the rationale for this particular combination are not discussed or justified in the paper.

### Trivial

1. Standard deviations for main results are relegated entirely to the appendix (Table 10). Including them in the main Table 1 would help readers assess statistical significance at a glance.

## Nice-to-Haves

- Add an experiment where strong baselines (e.g., GCNII, SGFormer) are run on the same augmented graph that FGL uses. This would cleanly isolate the forest aggregation's contribution from the augmentation benefit.
- Report the value of the nearest-neighbor count k used in pre-processing (currently only in the appendix).
- Provide an empirical plot showing estimated edge-score ratio vs. actual homophily ratio of sampled trees on real datasets to more directly bridge Theorem 2 with practice.

## Removed Points

- "The homophily estimator training uses labels... The paper does not bound the degradation from estimation error in terms of final classification performance." — Partially kept as Minor 1, but the harsh critic's framing as a major "methodological gap" requiring formal bounds is disproportionate. Demoted from implied major to minor with different framing.
- "Note that (2) (w.o. Local Submodule) still performs well... indicating that the global forest alone is competitive" — Framed as a weakness in the harsh critic, but this is actually a positive result for the forest paradigm. Removed.
- "The mention of acceleration and extensions is speculative — none are implemented or tested. This weakens the generality claim." — These are presented as future directions, not claimed contributions. Removed as scope creep.
- "The decision to use a GCN for homophilous graphs and an MLP for heterophilous graphs is stated but not justified." — This is a reasonable design choice aligned with well-known GNN behavior on homo vs. hetero graphs. Removed.
- "The number of nearest neighbors k is not specified in the main text—it appears only in the appendix (stripped)." — The paper explicitly references the appendix for details; missing appendix content is a parser artifact. Removed per instructions.
- "Standard deviations not shown in this table (only in appendix)" — Softened to Trivial 1, since this is a presentation preference, not a substantive gap.
- Several Strength Finder claims about the problem being "important" — these are generic and not specific evidence. Merged into the kept strengths above.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Most important:** Add a controlled comparison where strong baselines (GCNII, SGFormer, APPNP) are evaluated on the same augmented graph that FGL uses, with the same pseudo-label augmentation. This would cleanly isolate whether the forest aggregation itself drives the gains, or whether the augmentation provides most of the lift. The ablation in Table 3 row (1) provides partial evidence but only for the local module, not for a full baseline method.

2. Clarify the "quadratic node-pair interactions" claim: state explicitly that the tree aggregator achieves *global context integration* (each node receives information from all other nodes via path-structured propagation) without explicitly computing O(n²) pairwise interactions. The term "quadratic node-pair interactions" should be replaced or carefully qualified.

3. Show the standard deviations in the main results table (Table 1) rather than only in the appendix, to let readers assess result stability at a glance.

## Score and Decision

### Calibration

**Round 1 — Bracketing:**
- *Low band (< 3.5):* WL-Tree (3.0, reject), Low Rank Kernel Models (3.0, reject), Hierarchical Graph Contrastive (2.6, reject), Chordal Sampling (3.0, reject). FGL is far above these.
- *Middle band (3.5–7.5):* Port-Hamiltonian DGN (7.0, accept), NeuralWalker (7.0, accept), Understanding Heterophily (5.8, reject), PolyGCL (7.25, accept).
- *High band (> 7.5):* General Graph Random Features (8.0, accept), JDR (8.0, accept).

**Initial bracket:** 6.5 – 8.0. FGL is clearly stronger than the 5.8 heterophily theory paper, and its paradigm novelty exceeds NeuralWalker (7.0) and Port-Hamiltonian (7.0). But the confounded evaluation (weakness Major 1) prevents it from reaching the clean 8.0 tier.

**Round 2 — Narrowing (5.5–8.5):**
- *Understanding Heterophily* (5.8): Much narrower contribution (pure theory, no method), limited experiments. FGL is clearly stronger.
- *PolyGCL* (7.25): Interesting spectral contrastive learning paper. FGL has a more novel paradigm, more extensive experiments (26 baselines vs. fewer), and comparable theoretical depth. FGL is slightly stronger.
- *NeuralWalker* (7.0): Similar scope (long-range propagation paradigm). FGL has stronger theoretical guarantees (Theorem 2), better efficiency results, and a more novel core idea (spanning trees vs. random walk + SSM combination). FGL edges ahead.

**Final placement:** FGL is stronger than the 7.0 anchors and comparable to PolyGCL (7.25). It is a genuine contribution with a novel paradigm, strong theory, and comprehensive experiments. However, the confounded evaluation (graph augmentation vs. forest paradigm, Major 1) and the overstated "quadratic node-pair interactions" claim (Major 2) keep it below the clean 8.0 tier of papers like JDR and g-GRF. Score: **7.5** — a strong accept.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>