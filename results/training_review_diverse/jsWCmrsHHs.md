Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

## Summary

This paper proposes a deep reinforcement learning (DRL) guided improvement heuristic for job-shop scheduling (JSSP), departing from prior DRL-based construction heuristics. The method formulates JSSP as learning to search over complete solutions represented as disjunctive graphs, using a GNN policy network with two complementary modules — a Topological Embedding Module (TPM, based on GIN) and a Context-aware Embedding Module (CAM, based on GAT) — to select local moves from the N₅ neighbourhood. A message-passing evaluator is designed for batch GPU computation of schedules. Empirical results on seven classic benchmarks show that the learned policy substantially outperforms prior DRL-based methods and hand-crafted improvement rules, and generalizes well to very large instances and longer search horizons.

## Strengths

- **Novel DRL-based improvement heuristic that circumvents partial-solution limitations of construction heuristics**: Unlike prior DRL approaches that operate on incomplete schedules, this paper formulates JSSP as learning to search over complete solutions (disjunctive graphs). This directly addresses the bias issues arising from missing disjunctive arcs in partial solution representations (Section 1, Paragraph 3), which is a well-motivated and original framing.

- **GNN architecture with two complementary modules validated by ablation**: The dual-module design (TPM for topology, CAM for node heterogeneity) is structurally principled and the ablation study (Section 5.5) confirms that the combination converges faster and achieves lower gaps than either module alone, providing clear evidence of their complementary value.

- **Strong and consistent empirical performance**: With only 500 improvement steps, Ours-500 achieves substantially smaller gaps than all DRL baselines across nearly all problem sizes (e.g., 9.3% vs. 15.3% for ScheduleNet on Taillard 15×15; 2.8% vs. 6.1% on ABZ 10×10). With 5000 steps, Ours-5000 beats CP-SAT on Taillard 100×20 (3.0% vs. 3.9%) and outperforms it by double-digit percentages on extremely large instances (e.g., −24.31% on 200×40).

- **Message-passing evaluator enables efficient batch computation**: The proposed evaluator (Section 4.4, Theorem 2) is equivalent to CPM but processes multiple graphs in parallel on GPU. This is practically valuable for training and is used to accelerate baseline improvement heuristics as well.

- **Zero-shot generalization to much larger instances and longer search horizons**: Models trained on 20×15 instances generalize to problems up to 1000×40 (40,000 operations) and to 5000-step search horizons, demonstrating that the learned policy captures transferable knowledge beyond the training distribution.

## Weaknesses

### Fatal
None.

### Major
- **The n-step REINFORCE training algorithm is not described (Section 4.3)**. The section consists of a single sentence: "We propose an n-step REINFORCE algorithm for training the policy network." No details are provided about the number of steps *n*, whether a baseline is used and how it is estimated, the learning rate or its schedule, the batch size, the discount factor, the use of any entropy regularization or exploration strategy, or even the objective function. For a DRL methods paper, the training procedure is a core part of the contribution. This omission makes the method irreproducible as described and constitutes a significant technical gap. This is the single most important issue to fix.

- **The claim of linear time complexity (Theorem 1) is contradicted by the described action-scoring mechanism**. The action selection (Section 4.2.2) computes a score matrix *SC* of size |𝒪|×|𝒪| by multiplying the embedding matrix *h′* (size |𝒪|×q) by its transpose, which is an O(|𝒪|²·q) operation. Since |𝒪| = |𝒥|·|ℳ| + 2, this step is quadratic in the product of jobs and machines. The paper states the *policy network* has linear time complexity w.r.t. |𝒥| and |ℳ|, but the described forward pass includes a quadratic component. No proof or analysis is provided to justify the linearity claim, and no qualification distinguishes the GNN embedding phase (which is linear) from the action scoring (which is not). This claim should be retracted or carefully qualified with an honest complexity analysis.

### Minor
- **Reward sparsity is not discussed or ablated**. The reward (Eq. 1) is nonzero only when the new solution beats the incumbent, making most steps yield zero reward. The paper does not discuss how the REINFORCE algorithm handles this sparsity, nor whether alternative dense rewards (e.g., raw makespan difference) were considered. While the cumulative reward property (total improvement against initial solution) is a nice motivation, the absence of any discussion or ablation of this design choice leaves an open question about training efficiency.

- **Tabu search comparison could be interpreted more transparently**. At equal steps (5000), tabu search (TSN5) beats Ours by 1.9% relative gap; at equal time (90s), Ours wins. The paper attributes the step-equality gap to "the simplicity of our approach as a local search method without complex specialized mechanisms," which is a reasonable defense, but it does not discuss what this asymmetry implies: the learned policy is less effective *per move* than hand-crafted rules with tabu memory, and only wins on speed. A more balanced discussion would strengthen the paper.

### Trivial
- **Framing of computational efficiency relative to construction heuristics**: The paper describes itself as "computationally efficient" in the same paragraph where Ours-500 takes 9.3s on 15×15 Taillard while L2D takes 0.4s. While the claim is defensible in the broader context (the comparison includes slower improvement heuristics), the phrasing could mislead. The paper would benefit from explicitly distinguishing "efficient relative to other improvement heuristics" from "efficient relative to construction heuristics."

## Nice-to-Haves

- On the extremely large instances (Section 5.4), CP-SAT is given a 1-hour limit. Reporting CP-SAT's remaining gap (if estimable) or showing that its gap continues to shrink with longer runs would strengthen the claim that Ours finds genuinely better solutions, though the negative gap is already a strong result as presented.
- A brief discussion of how the critical path is selected when multiple exist (the paper mentions random selection at line 59, which is sufficient, but this could be elaborated).
- An analysis of the memory cost of the |𝒪|×|𝒪| score matrix for very large instances (e.g., 1000×40 → ~40k nodes → ~1.6B entries), since this could become a practical concern.

## Removed Points

- *Criticism that the paper does not report CP-SAT's gap to optimality on large instances*: For extremely large instances (200×40, 500×60, 1000×40), best-known solutions may not exist. CP-SAT with 1 hour is a standard and strong baseline; the negative gap vs. CP-SAT is already a valid and impressive result. This is a nice-to-have, not a weakness.
- *Criticism that the paper does not discuss how the critical path is chosen when multiple exist*: The paper explicitly states at line 59 ("randomly selects one if more than one exist"), so this criticism is factually incorrect.
- *Criticism about "missing appendix" or "missing proofs in appendix"*: The instructions forbid penalizing missing appendix content, as the parser may have stripped these sections.
- *Strength Finder's claim #3 about "provably linear computational complexity"*: This conflicts with a verified weakness (the action scoring is quadratic in |𝒪|), so it is removed per the conflict rule.
- *Criticisms about missing related works*: The instructions forbid introducing missing related works.

## Novel Insights

The most interesting observation emerging from the reviews is the tension between the paper's claimed linear complexity and the described quadratic action-scoring mechanism. If the quadratic scoring is retained, the paper should provide an empirical wall-time justification showing it does not dominate in practice (the runtime data in Table 1 suggests it grows sub-quadratically for the sizes tested, likely due to GPU-accelerated matrix multiplication with a small latent dimension q). Conversely, if the scoring can be made linear (e.g., by only scoring feasible N₅ pairs rather than all |𝒪|² pairs), that would make the theoretical claim match the architecture and strengthen the paper considerably. The missing training algorithm details also highlight a broader pattern: DRL-for-combinatorial-optimization papers often focus heavily on architecture design while treating the learning algorithm as a standard off-the-shelf component, but REINFORCE with sparse rewards is far from plug-and-play — the sparsity issue and the choice of n in n-step returns deserve serious discussion.

## Suggestions

1. **Fully specify the n-step REINFORCE algorithm**: Provide the exact update rule, the value of n, whether a baseline or critic is used, the learning rate and schedule, batch size, discount factor, entropy regularization (if any), and the number of training episodes/epochs. If the method uses a "customized" variant, explain what is customized and why.
2. **Clarify or retract the linear complexity claim**: Distinguish between the GNN embedding phase (linear in edge count) and the action scoring (quadratic in |𝒪|). Provide a rigorous complexity analysis or replace Theorem 1 with a more careful statement.
3. **Ablate the reward formulation**: Compare the incumbent-based sparse reward against a dense alternative (e.g., negative makespan or raw makespan improvement) to demonstrate whether sparsity helps or hinders learning.
4. **Reframe the tabu search discussion**: Acknowledge more directly that the per-step move quality of the learned policy is lower than tabu search, and position the computational advantage as the learned policy's main strength rather than an afterthought.
5. **Add practical guidance on the |𝒪|×|𝒪| score matrix**: Clarify whether full matrix multiplication is used or whether sparse/block approximations are employed for large instances, and discuss the memory footprint.

## Score and Decision

This paper makes a genuinely novel contribution — the DRL-guided improvement heuristic for JSSP is well-motivated, the GNN architecture is principled and validated by ablation, and the empirical results are strong and consistent across multiple benchmarks and problem sizes. However, two major issues prevent acceptance in the current form: (i) the training algorithm (Section 4.3) is completely underspecified, making the method irreproducible, and (ii) the linear complexity claim is unsupported and contradicted by the architecture. Both issues are addressable in a revision. The paper would be a solid contribution after these gaps are closed.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>