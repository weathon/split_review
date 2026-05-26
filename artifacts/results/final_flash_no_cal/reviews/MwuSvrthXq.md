Now I have a comprehensive picture. Let me synthesize the final review.

## Summary

This paper presents WeCAN, an end-to-end reinforcement learning framework for heterogeneous DAG scheduling with task-pool compatibility. The method introduces (1) a weighted cross-attention (WeCA) mechanism that encodes compatibility coefficients outside softmax to capture task-pool suitability without fixed-size embeddings, (2) a longest-directed-distance GNN (LDDGNN) for encoding task dependencies, and (3) a skip-action mechanism in the single-pass setting that addresses the theoretical optimality gap of list scheduling. Experiments on TPC-H and synthetic computation graph datasets show WeCAN achieves up to 18.1% improvement over heuristic baselines and up to 9.5% over the best neural baseline, with greedy inference speed comparable to classic heuristics (0.15s on TPC-H-30 vs. 0.18-0.30s for heuristics).

## Strengths

- **Single-pass inference matches heuristic speed while improving solution quality.** WeCAN-greedy runs in 0.15s on TPC-H-30, comparable to heuristics (0.18-0.30s) and ~100× faster than PPO-BiHyb (20.48s), while delivering substantially lower makespan (Table 1). This directly substantiates the claim of rapid, high-quality schedule generation.

- **Weighted cross-attention (WeCA) captures heterogeneous compatibility without fixed-size embeddings.** The outside-softmax attention bias (Section 3.1) allows the network to distinguish tasks sharing identical attributes but differing compatibility profiles. Ablation results (Table 3) confirm that removing WeCA layers increases makespan by 15-18%, proving the mechanism's empirical importance. The design scales naturally to varying pool counts and task types.

- **Skip actions supported by both theory and targeted experiments.** Theorem 1 proves that Algorithm 1 with skip actions can assign positive probability to all feasible orders (including optimal solutions), while the non-skipping variant provably cannot. Figure 3 shows that on heavy-task instances, WeCAN-with-skip achieves 8.3% improvement over HEFT vs. 2.6% for the non-skipping variant, validating the theoretical analysis of where skip matters most.

- **Strong empirical results across diverse benchmarks.** On TPC-H (Table 1), WeCAN-S(256) outperforms the best heuristic by up to 18.1% and the best neural baseline by up to 7.7%. On Computation Graphs (Table 2), improvements reach 13.4% over heuristics and 9.5% over neural baselines. These gains are consistent across Erdős-Rényi, layer, and stochastic block model graphs.

- **Robust generalization to environment size fluctuations.** Figure 2 shows WeCAN maintains double-digit makespan improvements over heuristics under varying pool numbers, pool types, task counts, and task types, demonstrating that the architecture adapts to heterogeneous configurations without retraining.

- **Systematic ablation study validates architectural choices.** Table 3 examines WeCA placement (inside vs. outside softmax), decoder configuration, and GNN variants. Every architectural alteration worsens makespan, providing controlled evidence that each component (outside-softmax WeCA, LDDGNN) contributes positively.

- **Theoretical analysis of the list-scheduling optimality gap.** Section 4 formalizes a criterion (Assumption 1, Theorem 2) for generation maps to cover optimal solutions, characterizes the optimality gap, and explains why skip actions (and the proposed coefficient formula) produce a surjection that remedies it. This analysis grounds the skip-action design and identifies heavy-task cases as the primary beneficiaries.

## Weaknesses

### Major

None.

### Minor

- **Skip action not ablated on standard datasets.** The skip action is presented as a core contribution (contribution 3), but the paper provides no ablation comparing with vs. without skip on the standard TPC-H and Computation Graphs datasets (Tables 1-2). The only skip ablation (Figure 3) modifies datasets by inserting heavy tasks. While the theoretical analysis predicts skip primarily benefits heavy-task cases, the absence of any skip/no-skip comparison on the main benchmarks means the reader cannot assess whether skip contributes to, is neutral for, or slightly harms performance in the settings where the headline results are reported. This is a gap in the empirical validation of a central claimed contribution.

- **One-Shot baseline comparison could be better framed.** The paper correctly notes (line 29) that One-Shot "does not consider compatibility coefficients or pool allocation" — i.e., it was not designed for the heterogeneous setting. Yet One-Shot is used as a primary neural baseline in Tables 1-2 and Figure 2 without further qualification of the comparison's asymmetry. The large margins over One-Shot partly reflect this architectural mismatch, not just the superiority of WeCAN's design. Since WeCAN also outperforms PPO-BiHyb (which does handle heterogeneity) and all heuristics, the paper's core claims do not depend on the One-Shot comparison, but the framing of "outperforming state-of-the-art methods" would benefit from clearer acknowledgment of this asymmetry.

### Trivial

- **Pool-selection rules for list-scheduling baselines are unspecified.** The paper states (Section 5.1) "we apply three pool-selection rules and select the one with the best makespan" but does not identify what these rules are. This is a minor transparency issue for reproducibility.

- **Skip score formula is presented as a heuristic without analysis.** The formula $u_a(1 - k/(2n))^{u_b} + u_c$ is described as preventing the skip action from being "overly prioritized," but no analysis, ablation, or comparison to alternatives (e.g., learned binary skip decisions) is provided to justify this specific functional form. Given that the skip mechanism is a claimed contribution, a more principled or empirically motivated design rationale would strengthen the paper.

## Nice-to-Haves

- Report how often the skip action is taken in practice (e.g., frequency distribution across problem instances, or early vs. late in scheduling) to strengthen the connection between the theoretical analysis and empirical behavior.
- Provide a brief summary of key training hyperparameters (learning rate, hidden dimension, network depth) in the main text, even if full details are in the appendix.
- Extend the limitation discussion beyond "Extending to more complicated settings" to acknowledge the heuristic nature of the skip score formula and cases where skip could potentially be harmful (e.g., if it disrupts batch processing).

## Removed Points

- **Criticism about training hyperparameters not in main text:** Removed per instruction — the appendix (which contains these details) is stripped by the PDF parser; the paper references Appendix D, E, and H for experimental details.
- **Criticism that §4 theory-practice connection is "loose":** Removed — the paper explicitly constructs map $S_n$, explains why it is not used (high variance), and then describes how skip actions provide a practical alternative that clusters poor solutions. The connection is adequately articulated.
- **Criticism about "no evidence (e.g., empirical distribution of skip counts)" for the clustering claim:** This is a reasonable suggestion but framed as a missing analysis rather than an error. Moved to Nice-to-Haves above.
- **Strength Finder strength about "the problem is important":** Removed — generic; the retained strengths are concrete and evidence-backed.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Add a skip/no-skip ablation column to the ablation study (Table 3) on the standard TPC-H-30 and TPC-H-50 datasets. This directly addresses the most significant gap in the empirical evaluation.
2. When presenting One-Shot results, add a sentence clarifying that One-Shot was designed for homogeneous DAG scheduling and does not natively handle compatibility coefficients, so the comparison is between a heterogeneous-aware method and an unadapted homogeneous method.
3. Specify the three pool-selection rules used for the list-scheduling baselines.
4. Briefly justify or ablate the skip score formula, or at minimum acknowledge its heuristic nature more explicitly in the main text.

## Score and Decision

This paper makes a solid, well-supported contribution to heterogeneous DAG scheduling. The weighted cross-attention design is principled, the empirical results are strong and consistent across multiple benchmarks, and the theoretical analysis of the list-scheduling optimality gap provides formal grounding for the skip mechanism. The weaknesses are addressable and do not threaten the core claims. I recommend acceptance.

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>