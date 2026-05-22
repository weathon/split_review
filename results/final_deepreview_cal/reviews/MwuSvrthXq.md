Now I have a strong calibration set. Let me synthesize my final review.

## Summary

This paper proposes WeCAN, an end-to-end RL framework for heterogeneous DAG scheduling with task-pool compatibility coefficients. It introduces weighted cross-attention (WeCA) layers that incorporate compatibility information while adapting to varying numbers of pools and task types, combined with a longest-directed-distance GNN (LDDGNN) for dependency encoding. A skip-action mechanism is introduced in the single-pass setting to address the optimality gap of list scheduling. Experiments on TPC-H and Computation Graphs datasets show strong makespan improvements over heuristics and two neural baselines.

---

## Strengths

1. **Novel and well-motivated weighted cross-attention architecture (WeCA).** Section 3.1 designs a WeCA layer that places compatibility coefficients as an attention bias *outside* softmax, so that tasks with identical attributes but different compatibility profiles receive distinguishable embeddings. The ablation study (Table 3) confirms the necessity of this design: removing or modifying WeCA reduces improvement from 14.0% to as low as 0.5% on TPC-H-30. The architecture inherently handles varying numbers of pools and task types, which is a clean improvement over prior work that relies on fixed-size embeddings or averaging.

2. **Substantive theoretical analysis of the list-scheduling optimality gap.** Section 4 provides formal proofs (Theorem 1 and 2) that list scheduling cannot guarantee optimal solutions and that the proposed skip-action mechanism can close this gap in the single-pass setting. This is a principled advance: prior single-pass neural schedulers (e.g., Jeon et al., 2023) inherit the list-scheduling gap without addressing it, while prior skip-action methods (e.g., Mao et al., 2016) require multi-round network processing.

3. **Strong empirical results with competitive runtime.** On TPC-H-30, WeCAN-S(256) achieves makespan 18964, outperforming the best heuristic (23170) by 18.1% and the best neural baseline (20399) by 7.1%, with a sampling runtime of 2.43s comparable to One-Shot (2.26s) and much faster than PPO-BiHyb (20.48s). The greedy mode achieves 0.15s, making it practical for time-sensitive applications. Results are consistent across TPC-H-50, TPC-H-100, and three Computation Graphs types.

4. **Generalization to varying environment sizes.** Figure 2 evaluates WeCAN under four types of environment fluctuation (more pools, more pool types, more tasks, more task types) with a fixed training distribution, and it consistently outperforms One-Shot. This directly supports the claim that the architecture "preserves adaptability and scalability across varying heterogeneous environment sizes."

---

## Weaknesses

### Major

1. **One-Shot baseline adaptation not described.** The paper compares against One-Shot (Jeon et al., 2023), a method originally designed for *homogeneous* DAG scheduling, and acknowledges that One-Shot "does not consider compatibility coefficients or pool allocation" (lines 62–63). Yet the experiments place One-Shot on heterogeneous problems with three pools and compatibility coefficients. There is no description of how One-Shot was adapted to this setting — how were pool assignments and compatibility coefficients handled? The paper reports 7.1–9.5% improvement over One-Shot-S(256), but the fairness of this comparison hinges entirely on an adaptation that is never specified. This is the most significant evaluation gap and should be addressed for the results to be fully interpretable.

2. **Variance-reduction claim for skip action is asserted without empirical support.** Section 4.2 argues that the skip-action design "clusters most poor solutions in the high-u_a, high-u_c region, rather than scattering them across the space; this concentration makes such regions easier to handle during training and reduces variance." No training curves, variance of returns, or distribution of sampled makespans are provided to support this claim. While the claim is plausible, the paper motivates the skip mechanism partly on variance grounds and should provide evidence. The absence weakens the theoretical narrative around the skip-action design.

### Minor

3. **Figure 3 labels are ambiguous.** The paper states that "WeCAN with the skip action achieves lower makespan than its non-skipping variant" (line 313), which indicates a comparison exists, but the figure labels as parsed show two "WeCAN-S(256)" entries (one blue at 8.3–8.9%, one green at –2.3% to 0.0%). The green bar is presumably a non-skip variant but its label is garbled. The figure needs cleaner labeling so the skip vs. no-skip comparison is immediately interpretable.

4. **Heavy-task experiment replaces only 1% of tasks.** The heavy-task evaluation (Section 5.3, line 313) replaces 1% of tasks with "heavy tasks." The paper later claims "the skip benefits more when the percentage of heavy tasks increases" (referencing Appendix C, which is stripped). The 1% rate seems low — a sensitivity analysis across multiple heavy-task rates (e.g., 1%, 5%, 10%) would strengthen the claim about the relationship between heavy-task proportion and skip-action benefit.

### Trivial

5. **Section 5.1 says datasets are "scheduled on three heterogeneous resource pools"** but doesn't state whether the three-pool setup is fixed across training and test or how the pool capacities and compatibility coefficients are generated. These details are deferred to Appendix D (stripped). A brief summary in the main text would improve readability.

---

## Nice-to-Haves

- A clean ablation of the skip score formulation: comparing the learned parametric form $u_a(1-k/2n)^{u_b} + u_c$ against simpler alternatives (e.g., a learned scalar, a fixed schedule like "skip every M steps").
- Discussion of scaling limitations: how does WeCAN perform with very large numbers of pools (e.g., 100)? The paper tests only up to 3 pools (with fluctuations in Figure 2).

---

## Removed Points

These points were raised by the reviewers but are removed from the main review for the following reasons:

- **"Skip-action ablation is not properly isolated" (Harsh Critic #2).** The paper text (line 313) explicitly states "WeCAN with the skip action achieves lower makespan than its non-skipping variant," confirming that a non-skip variant was evaluated. The figure labels are garbled by PDF parsing, but the comparison exists. This criticism is factually incorrect against the paper as written.

- **"Missing related works"** — Removed per hard rules: I do not have external sources to verify claimed missing references.

- **"Training details and hyperparameters hidden in appendix"** — Removed per hard rules: these are present in the original submission's appendix, which is stripped by the parser.

- **"Code release would enhance reproducibility"** — Removed per hard rules: reproducibility nitpicks about code release should not be listed as weaknesses.

- **"No limitations discussion"** — While this is a valid suggestion, it is a generic point applicable to many papers and does not constitute a specific weakness of this work's core contributions.

---

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions

1. **Describe the One-Shot adaptation explicitly.** Clarify how pool allocation and compatibility coefficients were handled for the One-Shot baseline. If the original One-Shot code was modified, specify the modifications. If a heuristic pool assignment was used, state this and discuss whether a more integrated neural pool selection would constitute a stronger baseline.

2. **Add empirical support for the variance-reduction claim.** Provide training curves (makespan over training steps) and/or variance of returns comparing the skip-based design against a version where skip actions are always masked. This evidence would significantly strengthen Section 4.2.

3. **Clean up Figure 3 labels.** Ensure the non-skip variant has a distinct and correct label, and that all bars are clearly identified.

---

## Score and Decision

### Calibration Report

**Round 1 (Bracketing):**
- Low band (avg < 3.5): bntJK4NyIW (2.00, reject), ArJikvI6xo (3.40, reject), 10eQ4Cfh8p (3.00, reject), 2HN97iDvHz (3.00, reject). These are clearly weaker papers in distantly related areas. The current paper is substantially stronger.
- Mid band (3.5–7.5): WszeEzjcq2 (5.33, reject), CFLEIeX7iK (5.75, reject), 9qtswuW5ux (4.25, reject), CpiJWKFdHN (5.67, reject). These are NCO papers with various evaluation/novelty issues.
- High band (7.5+): 7BLXhmWvwF (8.00, accept), or8mMhmyRV (7.75, accept), etc. These are strong accepts in robotics/LLM domains, not directly comparable.

**Round 1 bracket:** Plausible score range between 5.5 and 7.0.

**Round 2 (Narrowing):** Searched for anchors in (4.5, 6.5) and (5.5, 7.5) on scheduling/CO topics:
- j8lqABLgub (6.00, accept) — theoretical scheduling paper, accepted. Clear theoretical contribution but narrower scope.
- 8QkpCRio53 (5.75, reject) — PO for CO. Limited evaluation (only TSP-100, CVRP-100). Weaker empirical validation than the current paper.
- AloCXPpq54 (6.00, accept) — SSCO with HRL. Accepted but has significant justification/presentation issues.
- 8WtBrv2k2b (5.00, reject) — quantum resource scheduling, less relevant.

**Comparison to anchors:** The current paper has stronger empirical evaluation than any of the round-2 anchors (multiple real-world datasets, ablations, generalization tests). Its main weaknesses (One-Shot adaptation documentation, variance claim support) are fixable documentation gaps rather than fundamental flaws. It compares favorably to the 6.0 anchors.

**Final score:** 6.5. Above the mid-band anchors due to stronger empirical scope and clear architectural novelty, but held back from the 7+ range by the evaluation documentation gaps.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>