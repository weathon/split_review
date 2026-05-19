- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 6, 6
Now I have all the information needed. Let me synthesize the final consolidated review.

---

## Summary

This paper introduces H-Rockmate, a hierarchical framework for automatic re-materialization scheduling in arbitrary static computational graphs. It extends the prior Rockmate approach (which required sequential block structures) by proposing H-Partition (a greedy graph decomposition algorithm that builds a hierarchy of subgraphs) and H-Ilp (a linear programming solver that works on this hierarchy, combining sub-solutions under a given memory budget). The framework integrates TW-Remat and rk-Rotor as additional solvers at lower hierarchy levels. Experiments on GPT, ResNet, U-Net, and encoder-decoder Transformers show that H-Rockmate achieves comparable or better iteration-time/memory trade-offs while dramatically reducing solver time compared to Rockmate on non-sequential graphs (e.g., from 15 hours to 12 minutes on a 4-layer encoder-decoder Transformer).

## Strengths

1. **Dramatic solving-time improvement on non-sequential graphs compared to Rockmate**: Figure 2 shows that on a 4-layer encoder-decoder Transformer, Rockmate requires 15 hours to find a schedule, while H-Rockmate achieves a *better* iteration time in only 12 minutes — a 75× speedup. This is the paper's most compelling piece of evidence and directly supports the main claim that the hierarchical approach overcomes Rockmate's limitation on graphs without a clear sequential block structure.

2. **Near-optimal solution quality on small graphs**: Table 2 compares H-Ilp (with partitioning) against rk-Checkmate (the optimal ILP solver for the full graph) on a 2-layer encoder-decoder Transformer and a U-Net. Across multiple memory budgets, the overhead vs. Autodiff is within 1% between the two methods, demonstrating that partitioning introduces negligible degradation on graphs where an optimal comparison is feasible.

3. **Robustness to deeper hierarchy**: Figure 4 shows that on 6-layer and 8-layer encoder-decoder Transformers, increasing the depth of hierarchical decomposition (by reducing subgraph size) does not degrade the iteration-time/memory trade-off. This provides indirect evidence that the partitioning heuristic does not systematically sacrifice solution quality even when the hierarchy has multiple levels.

4. **Broader budget coverage via solver integration**: Figure 3c demonstrates that on the encoder-decoder Transformer, H-Ilp alone cannot find solutions at very low memory budgets, while TW-Remat can — but the reverse holds on U-Net. The H-Rockmate framework (H-Ilp + H-TWRemat) provides schedules across the full budget range, offering practical flexibility.

5. **Practical PyTorch integration**: The framework is presented as a one-line transformation (`model = HRockmate(model, sample, memory_budget)`) that is fully compatible with PyTorch Autograd, lowering the barrier to adoption compared to prior approaches (e.g., TW-Remat was only available for TensorFlow).

6. **Automatic decomposition requires no manual block identification**: H-Partition (Algorithm 1) greedily constructs subgraphs based on common-ancestor relationships, in contrast with Rockmate's need for an explicitly annotated sequential block structure.

## Weaknesses

### Fatal

None.

### Major

- **Near-optimality for large graphs (where partitioning is actually needed) is not directly supported.** The paper claims that H-Ilp finds "near-optimal solutions even on larger data-flow graphs" (Section 4, final paragraph). However, Table 2 validates near-optimality only on graphs small enough that rk-Checkmate (the optimal solver for the full graph) can still be run. On large graphs where partitioning is essential (e.g., the 4-layer encoder-decoder where Rockmate takes 15 hours), no comparison to an optimal baseline — or even to a known lower bound — is provided. Figure 4 shows that deeper partitioning does not degrade performance, which is necessary evidence but not sufficient for a *near-optimality* claim. This gap weakens one of the paper's headline claims; the authors should either qualify the claim ("near-optimal on graphs where optimal comparison is feasible" or "empirically robust to partitioning depth") or provide a bound or indirect comparison.

### Minor

- **No ablation study on the partitioning algorithm (H-Partition).** The H-Partition heuristic (greedy, based on common ancestors and a score function with hyperparameter α = 0.5) is a core component that determines which subproblems are available for the ILP solver. The paper does not compare it against simpler alternatives (e.g., random subgraph grouping of similar sizes, a graph-cut baseline like METIS, or even uniform splitting). Without such an ablation, it is unclear whether the heuristic's specific design is important, or whether any reasonable decomposition would yield similar results. The hyperparameter α (Equation 1) is also used at a single default value with no sensitivity analysis.

- **The "combination of strengths" contribution (#3) is underspecified and unvalidated.** The paper claims "a general framework to integrate previous and future re-materialization strategies at any level of the hierarchy, combining their strengths" (contributions list, bullet 3). Section 3.2.1 describes wrapping TW-Remat (H-TWRemat) and rk-Rotor as available solvers. But the paper does not clarify whether "combining" means the hierarchical framework genuinely integrates them into a single optimization — or whether H-Rockmate simply runs multiple solvers and selects the best schedule per budget (which is a useful engineering wrapper but not a novel technical contribution). No controlled experiment isolates the benefit of this integration over simply picking the best result from independently run solvers. The claim should be either removed, softened, or explicitly tested.

- **Clarity issues in Figure 3.** The caption mentions "H-Rockmate" as a separate curve from "H-Ilp" and "TW-Remat," but the text explains that H-Rockmate "integrates TW-Remat." It is ambiguous whether the H-Rockmate curve reflects a true integrated solver or a post-hoc best-of selection. The caption and legend should be reconciled and the mechanism clearly stated.

### Trivial

- **Score function justification (Section 3.1)**: The paper states the memory pressure "depends, less directly, on the length of the schedule" and uses a heuristic exponent α = 0.5. While this is a reasonable heuristic, the justification is imprecise. This is a minor presentation issue, not a technical flaw.

## Nice-to-Haves

- **Sensitivity analysis on hyperparameter α** (Equation 1) across a range of values (e.g., {0, 0.25, 0.5, 0.75, 1}) would strengthen confidence in H-Partition's robustness.
- **Medium-scale comparison**: Running H-Ilp (with partitioning) against the global optimal solver (rk-Checkmate) on a graph of intermediate size where both are feasible (e.g., ~200–300 nodes) would directly assess the optimality cost of partitioning where it actually matters.
- **Details on the ILP constraints** (Section 3.2.2): A brief example or pseudocode for the "correction terms" and "phantom nodes" constraints would improve reproducibility; however, the full formulation is presumably in the (stripped) appendix.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Linear complexity claim is misleading"** (Harsh Critic) — REMOVED. The paper's Section 3.3 clearly states that the *number of ILP solves* scales linearly with N and each subproblem has bounded size independent of N. The critic's concern about exponential worst-case of ILP in subproblem size is a misunderstanding: the claim is about scaling with N, not about ILP complexity in the subproblem size M^l, which is a constant.

- **"No comparison to gradient checkpointing"** (Harsh Critic) — REMOVED. Rockmate subsumes gradient checkpointing for sequential blocks, and the paper compares against Rockmate (the stronger baseline) and Checkmate (the optimal general-graph solver). Requesting this additional baseline is scope creep.

- **"Reproducibility details are sparse"** (Harsh Critic) — REMOVED. The paper describes its experimental setup (GPU, software versions, warm-up, measurement protocol) and plans to release the code. This meets the standard for an ML systems paper.

- **"Missing appendix content"** (multiple variations) — REMOVED. The appendix was stripped by the PDF parser; these materials exist in the original submission.

- **"Method not compared on GNNs"** (implied by "no diverse architectures" note) — REMOVED. The paper covers four architectures (GPT, ResNet, U-Net, encoder-decoder Transformer) spanning sequential and non-sequential graphs. This is adequate.

- **Strength about near-optimality** (Strength Finder) — PARTIALLY KEPT but QUALIFIED. The strength is valid for the small-graph evidence (Table 2) but conflicts with the verified weakness about lack of evidence for large graphs. The strength is retained with this qualification.

## Novel Insights

The reviews surface a tension in the paper's narrative that is not fully resolved in the current draft: the paper simultaneously claims (a) that H-Ilp provides "near-optimal" solutions through hierarchical decomposition, and (b) that combining multiple methods through the framework yields further improvements. If H-Ilp is near-optimal, then adding TW-Remat (a heuristic) should not improve solution quality for the same budget — yet Figure 3c shows it does on some architectures. This suggests that H-Ilp's near-optimality may be sensitive to the specifics of the graph structure and partition quality, or that "near-optimal" is being defined relative to achievable solutions under partition constraints rather than the true global optimum. The paper would benefit from explicitly addressing this distinction: near-optimal given a fixed partition vs. near-optimal in an absolute sense.

## Suggestions

1. **Conduct a partitioning ablation** by replacing H-Partition with a random grouping (same subgraph sizes) in the H-Ilp pipeline. If performance degrades, the heuristic's value is demonstrated; if not, the claim can be simplified.
2. **Qualify the "near-optimal" claim** to reflect that it is verified on small graphs where global optimum is computable, and provide a theoretical bound or additional empirical evidence for larger graphs (e.g., compare against a synchronous-cost-model lower bound).
3. **Clarify the "combination" mechanism**: State explicitly whether the H-Rockmate sweep in Figure 3 reflects an integrated hierarchical optimization or a post-hoc best-of-selection from multiple independent solvers. If the former, describe how the integration works at the ILP level.
4. **Reconcile the Figure 3 legend/caption** to avoid ambiguity about what "H-Rockmate" entails versus H-Ilp and TW-Remat.
5. **Include error bars** for at least a subset of measurements to corroborate the claim that standard error is two orders of magnitude below the mean.
