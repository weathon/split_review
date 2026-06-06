## Summary

DeepOPF-GAF proposes a graph self-attention framework for solving the N-1 Security-Constrained Optimal Power Flow (N-1 SCOPF) problem. The framework combines Graph Attention Networks (GAT) and Graph Convolutional Networks (GCN) with residual connections to handle variable topologies and multi-contingency scenarios simultaneously. The authors also advocate for using the Explained Variance Score (EVS) as a direct fitting quality metric, arguing it is more informative than standard feasibility metrics alone. Experiments are conducted on IEEE 9, 118, 300, and 2000-bus test systems.

---

## Strengths

- **Meaningful problem setting**: N-1 SCOPF is a practically important and computationally expensive problem; the framing of it as multi-task graph regression that requires variable topology adaptation is well-motivated, and using GNNs (rather than MLPs) to handle topology changes is a sensible design choice.

- **Multi-scale evaluation**: Experiments span four power system scales (9, 118, 300, 2000 buses), including a realistic large system (2000 buses), which is above what most prior work evaluates.

- **Insight about feasibility vs. fitting**: The paper makes a valid point (illustrated concretely in Fig. 2 and Table 2) that high constraint satisfaction rates are not sufficient to assess solution quality, and that a direct regression metric like EVS provides complementary information. This observation is practically useful to the field.

- **Architecture ablation**: Table 6 compares GAT-only, GCN-only, and the hybrid architecture under matched parameter budgets, providing evidence that the hybrid is beneficial because minimal topology changes are handled well by GCN while GAT handles adaptation.

---

## Weaknesses

### Fatal

None that completely invalidate the approach—the overall direction is sound.

### Major

1. **No comparison against prior methods.** The entire experimental section only compares variants of the proposed framework (simpleGAF / reGAF / large-reGAF) against each other. There is no comparison against any of the many prior methods discussed in the introduction: DeepOPF-V (Huang et al., 2021), the topology-aware GNN (Liu et al., 2022a), the physics-guided GCN (Gao et al., 2023), or the N-1 SCOPF baseline of Pham & Li (2024). Without external baselines, there is no evidence that the proposed approach offers any improvement over existing work. This is the most significant weakness.

2. **Unexplained negative optimality loss.** Several tables show negative $\eta_{opt}$ values (e.g., reGAF achieves −1.92% and large-reGAF achieves −1.26% on the 9-bus system; simpleGAF achieves −0.63% on 300-bus). A negative optimality loss means the ML prediction achieves a lower objective cost than the MIPS optimum, which is physically impossible if MIPS solves to optimality. This implies either a measurement error, a mismatch between the cost being minimized versus evaluated, or that the predicted solution is infeasible yet counted as having lower cost. The paper does not address this inconsistency.

3. **EVS is not a novel contribution.** The EVS (Explained Variance Score) is a standard, decades-old regression metric. The paper describes "introducing EVS" as one of its three main contributions, but this is merely applying a known metric to a new domain, which is incremental. Additionally, the paper conflates EVS with R² at times (Eq. 17 is actually the standard formula for the coefficient of determination / R²; EVS has a slightly different denominator in most standard definitions).

4. **Very small dataset.** Only 100 samples per fault scenario (80 train / 20 test) are generated. Given that contingency scenarios can number in the hundreds (N-1 means up to N lines + generators), the total effective training set is large, but per-scenario generalization is evaluated on only 20 test samples. No confidence intervals, standard deviations, or multiple seeds are reported, making it impossible to assess statistical significance of the reported differences.

### Minor

1. **Speedup versus accuracy trade-off is concerning but unaddressed.** The large-reGAF delivers the best EVS scores, but at dramatically reduced speedup—e.g., on the 300-bus system: ×125 vs ×955 for simpleGAF; on the 2000-bus: ×158 vs ×1712. A 6–11× reduction in speedup for marginal EVS improvement (e.g., 92.74→95.84 for $\eta_v^{EVS}$ on 300-bus) may not be justified in practice. The paper does not discuss this trade-off.

2. **Handling of topological variation is under-specified.** The paper claims the model handles variable topologies, but does not clearly describe how different contingency graphs (each a different graph structure) are passed through a single trained model. Does the model receive the full N-bus graph with edge masks, or individual modified graphs? This architectural detail is important for reproducibility and validity.

3. **Large language model analogy is hand-wavy.** The motivation that "N-1 SCOPF is multi-task learning, and LLMs succeed at multi-task with scale" is not rigorously substantiated and reads as a rhetorical device rather than a principled argument.

### Trivial

- Table 2 shows $\eta_{pg}^{EVS}/\eta_{qg}^{EVS}$ = −74.56/−111.84 for simpleGAF, meaning the simplest model performs worse than predicting the mean—this is the intended demonstration, but the magnitude suggests a fundamentally broken baseline, which slightly inflates the apparent advantage of larger models.

---

## Nice-to-Haves

- An empirical analysis of how the number of contingency scenarios scales with system size and how training time/data requirements grow accordingly.
- A wall-clock time breakdown separating GNN forward pass from post-hoc power flow reconstruction.

---

## Novel Insights

The paper's most useful insight—supported by concrete evidence—is that constraint satisfaction rate is a misleading metric for GNN-based OPF solvers: a model can satisfy all operational bounds while producing predictions far from the true solution values, because the feasible region is wide. This directly motivates using variance-explained-type metrics alongside feasibility metrics. While the metric itself is standard, the empirical demonstration of this disconnect (Fig. 2, Table 2 vs. EVS columns) is a concrete and practical contribution to the community's evaluation methodology.

---

## Suggestions

- Add at least one external baseline from prior N-1 SCOPF or OPF work to put results in context.
- Explain and correct or clearly caveat the negative optimality loss values; verify that feasibility is enforced before computing cost comparisons.
- Report means and standard deviations across multiple seeds or multiple test runs; the 20-sample test set is too small for confident conclusions.
- Clarify graph input representation for each contingency (masked edges vs. subgraphs), and provide architectural details sufficient for reproducibility (number of layers, heads, hidden dimensions per variant).

---

## Score and Decision

The paper addresses an important and underserved problem (N-1 SCOPF with GNNs at scale), and the EVS metric discussion adds practical value. However, the absence of any external baseline comparison is a critical gap that prevents the community from knowing whether this approach is competitive with the substantial existing literature. Compounding this, the negative optimality values are left unexplained, the dataset is very small, and the stated contribution of EVS is not novel. As submitted, the paper does not meet the bar for ICLR.

MY FINAL SCORE: <score>3</score>
MY FINAL DECISION: <decision>Reject</decision>