My draft is complete. Let me finalize the review.

## Summary
This paper proposes a DRL-based improvement heuristic for the Job Shop Scheduling Problem (JSSP), shifting from the dominant construction-heuristic paradigm to learned local search over complete solutions. The method uses a dual-module GNN (TPM for topology, CAM for heterogeneous neighbor contexts) to encode disjunctive graphs, a message-passing evaluator for parallel schedule computation, and is trained via REINFORCE. Experiments on seven classic benchmarks show consistent outperformance over construction-based DRL methods (L2D, RL-GNN, ScheduleNet) and hand-crafted improvement rules (greedy, best-improvement, first-improvement), with zero-shot generalization to instances up to 1000×40 where it surpasses CP-SAT given a 1-hour time limit.

## Strengths

1. **Well-motivated paradigm shift from construction to improvement heuristics for learned JSSP solving.** The paper correctly identifies that partial-solution representations in construction methods ignore disjunctive arcs among undispatched operations and cannot capture structural differences between solutions (Section 1). Operating on complete solutions via disjunctive graphs addresses this limitation — a genuine architectural departure from L2D, RL-GNN, and ScheduleNet.

2. **Consistent and often large-margin superiority over all three DRL baselines and three hand-crafted improvement rules.** Table 1 shows Ours-500 (500 steps) outperforms L2D, RL-GNN, and ScheduleNet on nearly all benchmark sizes. Against hand-crafted rules starting from the same initial solutions, Ours-500 consistently achieves lower gaps (e.g., 9.3% vs. 11.7–12.3% on Taillard 15×15), isolating the benefit of the learned policy over hand-crafted heuristics.

3. **Zero-shot generalization to extremely large instances with negative gaps against CP-SAT.** Table 5 reports that a model trained only on 20×15 instances achieves gaps of −24.31% (200×40), −20.56% (500×60), and −15.99% (1000×40) relative to CP-SAT with a 1-hour limit, using only 500 improvement steps. This is strong evidence that learned improvement policies can scale far beyond training.

4. **Message-passing evaluator provably equivalent to CPM but amenable to batch GPU computation.** Theorem 2 (lines 189–193) establishes correctness of a parallelizable message-passing alternative to the sequential critical path method, addressing the neighborhood-evaluation bottleneck in traditional improvement heuristics.

5. **Learned policy avoids cycling that traps hand-crafted rules.** Section 5.3 documents that GD-500 and GD-5000 produce identical gaps (e.g., 11.9% on Taillard 15×15), indicating cycling, while Ours continues to improve from 500 to 5000 steps without explicit restart mechanisms — demonstrating a concrete advantage of long-horizon optimization.

6. **Ablation validates both TPM and CAM are necessary.** Section 5.6 shows that using only TPM or only CAM yields worse convergence than their combination, providing direct empirical justification for the dual-module architecture.

## Weaknesses

### Major

1. **The n-step REINFORCE training algorithm is essentially unspecified.** Section 4.3 (lines 180–182) consists of a single sentence: "We propose an n-step REINFORCE algorithm for training the policy network." There is no pseudocode, no policy gradient equation, no stated value of n, no mention of whether a baseline is used, no discussion of episode truncation or bootstrapping, no discount factor, and no optimizer details. While REINFORCE is a standard algorithm, the n-step variant involves specific design choices that directly affect learning behavior — especially given the sparse reward structure (Equation 3) where positive reward only occurs when the incumbent is beaten. This omission means the paper's central training procedure is not actually presented, which is incompatible with the standards of a top venue.

2. **The linear-complexity claim is inconsistent with the described action selection mechanism.** Theorem 1 (line 173) states "the proposed policy network has linear time complexity w.r.t both |J| and |M|," and the abstract claims "the computational complexity of our method scales linearly with problem size." However, the action selection step (lines 167–169) computes a score matrix via h' @ h'^T, where h' is a |O|×q matrix (|O| = |J|·|M|+2). This matrix multiplication is O((|J|·|M|)²), which is quadratic. While the GNN embedding computation itself is linear (and line 20 qualifies "when embedding disjunctive graphs"), Theorem 1 and the abstract carry no such qualifier. This contradiction needs resolution: either restrict the claim or modify the action selection.

3. **Missing critical details that compromise reproducibility.** (a) The dispatching rules used to generate the initial solution are only described as "basic dispatching rules" (line 66) with no specification of which rules are used — this directly affects the difficulty of the improvement task and the fairness of comparisons. (b) No confidence intervals, standard deviations, or multiple-seed results are reported for the main benchmark results (Table 1). The paper claims stability "for various problem sizes and different random seeds" (line 297) without showing supporting data. For a DRL paper with stochastic policies, this is a significant gap.

### Minor

1. **Reward sparsity is not discussed.** The reward (Equation 3) is max(Cmax(s*_t) − Cmax(s_{t+1}), 0): the agent only receives positive reward when it beats the incumbent. Over 500 steps, non-improving moves yield zero reward, and the cumulative reward collapses to the net terminal improvement. The paper does not discuss how the training algorithm handles this credit-assignment challenge or why this formulation was chosen over alternatives (e.g., shaping rewards based on per-move improvement).

2. **The ablation study is limited to 10×10 instances.** While the ablation (Section 5.6) confirms that combining TPM and CAM is beneficial, the results would be substantially stronger if repeated on larger problem sizes to verify that the benefit persists.

3. **No DRL-based improvement baseline is included.** The comparison with construction DRL baselines (L2D, RL-GNN, ScheduleNet) conflates the advantage of the improvement paradigm with the quality of the learned policy. The hand-crafted improvement baselines starting from the same initial solutions partially address this, but including a simpler DRL improvement policy (e.g., single-module GNN trained identically) would more directly isolate the benefit of the dual-module architecture.

4. **The N5 neighborhood restriction is not acknowledged as a limitation.** The policy is fundamentally constrained by the N5 neighborhood — it can never discover solutions requiring moves outside critical blocks on the critical path. This is a reasonable design choice but should be explicitly discussed.

### Trivial
None.

## Nice-to-Haves
- A runtime comparison of the message-passing evaluator vs. standard CPM on GPU would help quantify the claimed speedup.
- Reporting training curves for multiple problem sizes (beyond 10×10) would strengthen the empirical characterization.
- If the hyperparameters (learning rate, batch size, optimizer, GPU model) were present in a section stripped by the extraction process, ensure they appear in the main paper.

## Removed Points
These points were identified in the input reviews but removed or downgraded after verification against the paper.

- *"Tables 3 and 4 are referenced but not shown"* — These tables likely appear in figures or sections stripped by the automated extraction process. The original submission would contain them.
- *"No proof given for Theorem 2 / Corollary 1"* — Proofs are typically placed in the appendix, which is stripped by extraction. The paper states the claims and notes they are easy to prove.
- *"Missing related works"* — Removed per rule: the reviewer cannot confirm existence of unmentioned works.
- *"Comparison with DRL baselines is apples-to-oranges (structural issue)"* — Partially addressed by the paper: hand-crafted improvement rules starting from the same initial solution are included, which does isolate the learned-policy advantage. Downgraded from major to Minor #3.
- *"Reward function creates an extremely sparse signal (methodological concern)"* — Downgraded from major to Minor #1. The sparsity is worth discussing but characterizing it as a "structural" issue overstates the concern; the cumulative reward directly captures the objective and is a valid design choice.
- *"Missing hyperparameters (learning rate, batch size, optimizer, GPU)"* — The "Model and configuration" section header (line 216) is followed by what appears to be stripped content. Some details may exist in the original submission. The remaining substantiated concerns (unspecified initial-solution heuristics, missing confidence intervals) are retained in Major #3.
- *Strength: "Provably linear computational complexity of the policy network"* — Dropped because it conflicts with the verified weakness (Major #2) that the action selection involves quadratic computation. The runtime data in Table 1 shows favorable empirical scaling, but the theoretical claim as stated is inconsistent with the described architecture.

## Novel Insights
None beyond the paper's own contributions. The reviews surface standard methodological concerns (underspecified training procedure, complexity claim inconsistency, lack of statistical rigor) that are common in DRL-for-CO papers that emphasize architecture design while under-describing the learning algorithm.

## Suggestions
1. **Specify the n-step REINFORCE algorithm in full.** Provide the policy gradient equation, the value of n, whether a baseline is used (and if so, what), how episodes are truncated, and the discount factor. A pseudocode listing would be most helpful.
2. **Resolve the linear-complexity claim.** Either clarify that it applies only to the GNN embedding computation (not the full forward pass including the quadratic action scoring), or modify the action selection to achieve linear time (e.g., by restricting scoring to feasible neighbor pairs rather than computing the full |O|×|O| matrix).
3. **Report statistical significance.** Run experiments with at least 3–5 random seeds and report means and standard deviations in Table 1.
4. **Specify the initial-solution dispatching rules.** Name which rule(s) are used (e.g., SPT, MWKR, FIFO) so the improvement task is precisely defined.
5. **Discuss the reward sparsity issue** and how the training algorithm handles it — this will help readers evaluate the soundness of the learning setup.
6. **Expand the ablation** to at least one larger problem size to verify that the TPM+CAM combination remains beneficial when problems scale.

## Score and Decision
MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>