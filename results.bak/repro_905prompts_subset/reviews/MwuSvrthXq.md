Now I have sufficient context. Let me write the consolidated review.

## Summary

This paper proposes WeCAN, an end-to-end reinforcement learning framework for heterogeneous DAG scheduling with task-pool compatibility coefficients. It introduces a weighted cross-attention (WeCA) layer that places compatibility coefficients outside the softmax, enabling tasks with identical attributes but different compatibility profiles to receive distinct embeddings while preserving adaptability to varying environment sizes. The paper also provides a theoretical analysis of the optimality gap in list-scheduling-based methods and develops a skip-action mechanism that operates in the single-pass setting to close this gap. Empirical results on TPC-H and Computation Graphs datasets show consistent makespan improvements over heuristic and neural baselines, with inference times comparable to heuristics and orders of magnitude faster than multi-round neural methods.

## Strengths

- **Weighted cross-attention layer with theoretically motivated coefficient placement (Section 3.1, Eq. 3):** Placing the compatibility coefficient *outside* the softmax means that two tasks with identical feature vectors but different numbers of compatible pools receive different embeddings. This is a clean architectural contribution over prior methods (Zhou et al., 2022; Zhadan et al., 2023) that average compatibility coefficients or use fixed-size embeddings. The ablation (Table 3) confirms the outside placement outperforms the inside variant (~3.5% on TPC-H-30).

- **Skip-action mechanism with theoretical grounding (Section 4, Theorem 1–2):** The paper identifies that list scheduling (*S_list*) is not surjective, preventing optimal solutions from being representable. Enlarging the action space with skip actions and proving (in Appendix A) that the resulting (*B_f, T, S*) satisfies Assumption 1 and Theorem 1 is a principled theoretical contribution. The heavy-task experiments (Figure 3) empirically validate that skip matters: WeCAN with skip outperforms its own non-skip variant by ~5% on TPC-H-30-heavy.

- **Strong empirical performance with practical efficiency (Tables 1, 2):** On TPC-H-100 (918 tasks), WeCAN-S(256) achieves makespan 61373 vs. the best neural baseline One-Shot at 66173 (7.3% improvement) and best heuristic HEFT at 70137 (12.5% improvement), while WeCAN-Greedy runs in 1.72s — comparable to heuristics and two orders of magnitude faster than PPO-BiHyb (179s). Similar patterns hold across Computation Graphs datasets.

- **Robust generalization to varying environment sizes without retraining (Figure 2):** WeCAN maintains double-digit percentage improvements over the best heuristic under pool number, pool type, task number, and task type fluctuations, while One-Shot degrades sharply (e.g., 0.9% under pool type change). This directly validates the adaptive design of the WeCA layer.

- **Longest Directed Distance GNN (LDDGNN, Section 3.1):** Using longest directed path length as a learnable bias in GNN attention is a simple but effective adaptation of Graphormer-style encoding for DAG dependencies. The ablation confirms it outperforms standard GAT (forward and bidirectional) on both TPC-H-30 and TPC-H-50.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Figure 3 has confusing duplicate labels:** The caption lists "WeCAN-S(256)" twice in different colors (blue and green), and the table row repeats "WeCAN-S(256) | WeCAN-inside-S(256) | PRO-BALM | WeCAN-S(256) | CP". One of these is presumably the non-skip variant, but this is unclear from the figure and caption. This makes it difficult to interpret which variant is being compared.

- **Skip action not ablated on standard (non-heavy) instances:** The skip-action mechanism is evaluated only on heavy-task variants (Figure 3). Since the skip action could in principle degrade performance on standard instances (e.g., by introducing unnecessary waiting or increasing variance), the paper should report makespan with and without skip on the original TPC-H datasets to confirm there is no degradation.

- **Limited discussion of scalability limitations:** The WeCA layer computes attention between each task and each pool, which is *O(n_tasks × n_pools)* per layer. The largest experiment has 3 pools and ~1000 tasks. The paper would benefit from a discussion of how the method scales to scenarios with many pools (e.g., 100+ pools) and whether the quadratic task-pool interaction becomes a bottleneck.

- **The skip score parameterization's connection to Theorem 1(iv) is deferred to the appendix:** The parameterized form *u_skip = u_a(1 − k/(2n))^{u_b} + u_c* is asserted to be sufficient for the optimality guarantee in Theorem 1(iv), but the proof is in Appendix A (not available in the review copy). While this is not a flaw per se, the main text would benefit from at least an intuitive explanation of why this three-parameter form suffices, given its apparent restrictiveness.

### Trivial

- **Table 3 column heading ambiguity:** The column "Improvement" is described in the text as relative to "the best heuristic (Tetris)," but the heading does not specify this. For the WeCA-final-only row on TPC-H-50, the improvement is listed as −4.2%, which is a valid comparison against Tetris (the best heuristic on this dataset), but the negative value could be misinterpreted without context.

## Nice-to-Haves

- **Comparison against exact solutions for small instances:** For problems with 20–30 tasks, a comparison against the MILP formulation (Appendix A) solved optimally would contextualize the absolute quality of WeCAN's solutions and show how far from optimal they are.
- **Skip action on standard instances (as noted above under Minor):** This is the most impactful missing ablation.
- **Confidence intervals or significance tests for the environment fluctuation experiments (Figure 2):** The figure reports point estimates but no error bars or statistical significance tests.

## Removed Points

These points were considered but removed with justification:

1. *"Baselines are information-starved because they don't use compatibility coefficients"* — **Factually incorrect for HEFT.** HEFT (Topcuoglu et al., 2002) uses per-task-per-processor computation costs, which is exactly what the paper's compatibility coefficients represent. The paper itself cites Topcuoglu et al. (2002) for the definition of *K_acc*. HEFT is a standard and appropriate baseline. For One-Shot, the paper is transparent about its homogeneous-origin limitation; the comparison still demonstrates the value of handling heterogeneity.

2. *"The WeCA-inside vs WeCA-outside ablation is confounded"* — The ablation directly compares the two placements (outside vs. inside, where inside moves K_acc inside softmax as a bias term). This is a clean comparison between the two natural design choices, and the result supports the outside placement.

3. *"Missing network architecture specifics (embedding dimensions, layers, etc.)"* — These details are in Appendix G, which was stripped by the parser. The original submission contains them.

4. *"HEFT is better than Tetris on TPC-H-50"* — **Factually incorrect.** Table 1 shows Tetris (38654) < HEFT (39315) on TPC-H-50. Tetris is tied or better on all three TPC-H subsets.

5. *"No comparison with optimal solutions"* — Listed as nice-to-have; not a required baseline for a learning-based CO paper at this venue.

## Novel Insights

The most interesting insight across the reviews is the observation about the placement of the compatibility coefficient in the attention mechanism. While one might naturally assume that placing domain-specific coefficients inside the softmax (as additive biases) is the more principled approach, the paper shows that placing them *outside* — as multiplicative weights on the value vectors after softmax normalization — produces better embeddings and downstream performance. The reasoning is that this placement preserves information about the *total number* of compatible pools for each task, which would be lost inside the softmax due to normalization. This is a subtle but transferable design insight: for any cross-attention mechanism where entities have heterogeneous compatibility with a reference set, placing compatibility weights outside the softmax can better preserve aggregate compatibility information.

## Suggestions

1. Fix the duplicate labeling in Figure 3 — clearly distinguish the skip and non-skip variants with distinct names (e.g., "WeCAN-S(256)" and "WeCAN-no-skip-S(256)").
2. Add an ablation of the skip action on standard (non-heavy) TPC-H instances and report whether it degrades, improves, or leaves performance unchanged.
3. Add a limitations paragraph discussing the *O(n_tasks × n_pools)* complexity of the WeCA layer and how the approach scales to settings with many pools.
4. Add a brief intuitive explanation in the main text for why the three-parameter skip score form is sufficient for Theorem 1(iv), even if the formal proof is in the appendix.

## Score and Decision

### Calibration

**Round 1 — Bracketing:** Searched for DAG scheduling / RL / combinatorial optimization anchors across three bands. Weak anchors (score < 3.5) were mostly unrelated or had fundamental flaws. Strong anchors (score > 7.5) were top-tier theory or methods papers.

**Round 1 bracket:** 4.5 – 7.0.

**Round 2 — Narrowing:**
- *8WtBrv2k2b* (avg 5.00, Quantum Resource Scheduling): Reject. Had serious methodological gaps, unclear problem formulation, and weak baselines. **This paper is stronger** — the formulation is clear, the baselines are appropriate, and the experiments are substantially more complete.
- *DKfcxPxunu* (avg 5.75, Multi-Task VRP): Mixed reviews (3,8,6,6). Concerns about low novelty (essentially POMO + attribute input). **This paper is stronger** — the WeCA layer and skip-action theory are more novel contributions.
- *6hvtSLkKeZ* (avg 6.40, CCBPP Bin Packing): Accept. Novel problem formulation, good experiments, solid but incremental architecture. **Comparable** — this paper has stronger theory but the CCBPP paper has broader problem scope.
- *jKhNBulNMh* (avg 6.67, Symbolic Branching): Accept. Novel framework combining symbolic discovery with CO solvers. **Comparable** — different kind of contribution, but similar level of novelty and empirical support.

**Final score:** 6.0. The paper sits in the upper portion of the 4.5–7.0 bracket. Its architectural contribution (WeCA) and theoretical analysis (skip-action optimality gap) are genuine novelties, and the empirical validation is thorough. The weaknesses are minor and addressable. It is stronger than the 5.0–5.75 anchors and comparable to well-regarded 6.0–6.5 papers in the neural CO space.

### Anchors consulted

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| bntJK4NyIW | 2.00 | 1 | Much weaker — different topic, serious flaws |
| 10eQ4Cfh8p | 3.00 | 1 | Weaker — different topic, less rigorous |
| 2HN97iDvHz | 3.00 | 1 | Weaker — different topic |
| CJEBFNBLhO | 4.25 | 1 | Weaker — focused on environment engineering, not method |
| 8WtBrv2k2b | 5.00 | 2 | Weaker — serious methodological gaps |
| DKfcxPxunu | 5.75 | 2 | Weaker — lower novelty |
| rEQqBZIz49 | 5.20 | 2 | Different subfield (GNN architecture, not scheduling) |
| voLFfrWzFI | 4.75 | 2 | Weaker — DFL methodology paper |
| AloCXPpq54 | 6.00 | 1 | Comparable — similar tier |
| DhH3LbA6F6 | 6.00 | 1 | Comparable — similar tier |
| 6hvtSLkKeZ | 6.40 | 2 | Comparable — stronger experiments, weaker theory |
| jKhNBulNMh | 6.67 | 2 | Comparable — different contribution type |
| yEwakMNIex | 6.25 | 2 | Comparable — similar tier |
| GM7cmQfk2F | 7.00 | 2 | Stronger — more polished presentation |

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>