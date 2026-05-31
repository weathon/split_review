## Summary

The paper proposes a graph self-attention framework (GAF) for solving N-1 Security-Constrained Optimal Power Flow (N-1 SCOPF). The architecture stacks GAT and GCN layers with residual connections and is trained to predict voltage magnitudes and angles, from which remaining variables are recovered via power flow equations. The Explained Variance Score (EVS) is introduced as a metric to directly assess fitting performance. Experiments on IEEE 9, 118, 300, and 2000-bus systems compare three model variants (simpleGAF, reGAF, large-reGAF) and show that larger models generally improve EVS.

## Strengths

- The paper addresses a practically important and computationally challenging problem (N-1 SCOPF) and the motivation for using graph-based models that can handle topological changes is well justified.
- The introduction of EVS as a complementary metric is useful: the paper convincingly demonstrates via Fig. 2 and Table 2 that feasibility metrics alone can be misleading when fitting quality is poor.
- The architecture is designed to handle both line and generator contingencies simultaneously, and the residual mechanism helps train deeper models.
- Experiments span a reasonable range of system sizes (9 to 2000 buses), and the results generally show that larger models yield better EVS for voltage magnitude/angle and for generator outputs on several test cases.

## Weaknesses

### Major

1. **Lack of comparison with existing methods.** The paper only compares its own architectural variants (simpleGAF, reGAF, large-reGAF). No baseline from prior work is included—not even a simple MLP, a standard GCN, or the augmented hierarchical GNN (Pham & Li, 2024) that is cited. Without any external baseline, the claimed advantages of the proposed approach cannot be assessed.

2. **Limited novelty of the architecture and metric.** Stacking GAT and GCN layers with residual connections is a standard design pattern; the paper does not introduce a new mechanism or provide theoretical justification. The EVS is a standard regression metric, not a novel contribution. Claims of being “first to propose solving N-1 SCOPF with larger-scale graph neural networks” are overstated given existing GNN works for N-1 SCOPF (e.g., the cited augmented hierarchical GNN).

3. **Incomplete experimental validation.** The paper does not test generalization to unseen fault topologies beyond the training set (all contingencies are assumed available during training). It also does not report training time, convergence behavior, or sensitivity to hyperparameters. The computational benefit (speedup) is reported only for inference, but training cost (4 GPUs) is not compared against any baseline.

4. **Inconsistent scaling behavior.** On the 2000-bus system (Table 4), large-reGAF actually decreases EVS for active power generation (99.60→98.28) compared to simpleGAF, undermining the claim that larger networks consistently improve fitting. The paper glosses over this counterexample.

### Minor

- The description of how multiple contingency scenarios are handled during training is unclear. It is not specified whether the graph input encodes the fault condition (e.g., via the adjacency matrix or additional node features) or if separate models are trained per scenario.
- The paper states that unsolvable scenarios are ignored (up to 1000 sampling attempts). This could introduce selection bias if some contingency types are systematically harder to solve.
- The scatter plot (Fig. 2) shows that even the large-reGAF prediction has considerable noise, yet the conclusions focus on the improvement over simpleGAF without quantifying remaining error.

### Trivial

- Minor terminology issue: “In this search” should be “In this research” (Section 2.2).
- The paper uses “§” formatting for section symbols, which is acceptable but non‑standard.

## Nice-to-Haves

- Include comparisons with at least one existing ML-based OPF method (e.g., DeepOPF-V, physics‑guided GCN, or the augmented hierarchical GNN) under the same experimental setup.
- Provide an ablation study to isolate the effect of each component (GAT vs. GCN, residual connections, depth/width scaling).
- Test generalization by training on a subset of contingencies and evaluating on unseen ones.
- Report training time and convergence behavior.

## Novel Insights

None beyond the paper’s own contributions.

## Suggestions

- Add a baseline comparison with a standard GCN, a multi-layer perceptron (with topology encoding), and the state‑of‑the‑art method cited in the paper (Pham & Li, 2024). This is essential to validate the claimed advantages.
- Clarify how the model handles variable topologies at input time (e.g., using the adjacency matrix of the current contingency as a graph input).
- Report EVS for all output variables on every test case, and discuss the case where larger models underperform (2000‑bus active power).
- Consider using a more direct metric for operational performance (e.g., actual constraint violation rate or cost error) in addition to EVS.

## Score and Decision

The paper tackles a relevant problem and makes a reasonable observation about the inadequacy of feasibility metrics. However, the contributions are incremental: the architecture is a standard combination of GAT and GCN, the proposed metric is well‑known, and the experimental evaluation lacks any external baseline. Given these limitations, the paper does not meet the novelty and rigor expected for ICLR.

MY FINAL SCORE: <score>3</score>
MY FINAL DECISION: <decision>Reject</decision>