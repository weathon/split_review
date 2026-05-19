- Decision: Accept
- Avg Score: 5.00
- Scores: 6, 6, 5, 3
Now I have a thorough understanding of both the paper and the reviewer inputs. Let me produce the consolidated review.

## Summary

This paper proposes Light-MILPopt, a four-stage pipeline (Problem Formulation via graph partition, Model-based Initial Solution Prediction via EGAT with half-convolutions, Problem Reduction via confidence-based variable reduction and KNN constraint reduction, and Data-driven Optimization) for solving large-scale MILPs using a lightweight (scale-limited) optimizer and a small training dataset. Experiments on four benchmark MILPs and a real-world case study show that the framework outperforms Gurobi, SCIP, and the GNN&GBDT baseline under the same wall-clock time while training on what the paper claims is only 1% of the benchmark data.

## Strengths

- **Clear empirical advantage over strong baselines under identical runtime.** Table 1 compares objective values under the same wall-clock time and shows Light-MILPopt (using SCIP limited to 30% or 50% of variables) achieves better solutions than Gurobi, SCIP, and GNN&GBDT on all four benchmarks and a real-world case study. This is the paper's central claim and is directly supported.

- **Large efficiency gains to reach the same solution quality.** Table 2 reports that Light-MILPopt reaches the same target objective values in a fraction of the time required by full-scale solvers and saves >90% of solution time over GNN&GBDT on most problems. This efficiency claim is concrete and well-motivated.

- **Constraint reduction via KNN is a novel component in the ML-based MILP pipeline.** Prior work (GNN&GBDT) focused on variable reduction only. The paper's KNN-based active constraint identification (Section 3.3) and progressive constraint set update (Section 3.4) are reasonable additions. The paper quantifies the impact in one case: in the SC scenario, constraint reduction cuts per-iteration time to 1/5.

- **Convergence analysis complements the main tables.** Figure 5 shows time-objective curves on three benchmarks, demonstrating that Light-MILPopt's convergence trajectory is competitive with Gurobi and GNN&GBDT, providing visual evidence beyond single-number comparisons.

## Weaknesses

### Major

- **No ablation study — the contribution of individual components is entirely unassigned.** The pipeline has four stages with multiple interacting subcomponents: graph partition (FENNEL), EGAT with half-convolutions, confidence-based variable reduction, KNN constraint reduction, subgraph clustering, hierarchical crossover, and progressive K update. The paper offers zero ablation experiments to isolate any single component's contribution. It is therefore impossible to tell whether the EGAT architecture matters, whether the graph partition is essential, or whether a simple heuristic paired with variable/constraint reduction would achieve most of the gains. Given that the GNN&GBDT baseline is also a multi-stage pipeline, the novelty claim hinges on demonstrating which proposed modifications drive improvement. Without ablation, the paper functions as an engineering demo rather than a scientific validation of its design choices.

### Minor

- **Benchmark instance dimensions are not reported.** The paper never states the number of variables or constraints in any of the four benchmark instances (SC, MVC, MIS, MIKS) or the real-world case study. This makes it impossible to verify the "large-scale" claim or to assess whether the problem sizes are comparable to those in prior work (GNN&GBDT, Neural Diving). The paper mentions "millions of variables" qualitatively (Section 3.1) but gives no concrete numbers for the evaluated instances.

- **The "1% training data" claim is ambiguous.** The paper states (Section 4.1): "using only 1% of the size of large-scale benchmark MILPs for training data." It is unclear whether this means 1% of the number of training instances, 1% of the total variables across instances, 1% of the constraint count, or something else. The actual training set size (number of instances, variables) is not reported, nor is a comparison to the training data used by GNN&GBDT. This weakens the paper's central claim about training efficiency.

- **The KNN constraint reduction's effectiveness is not empirically validated.** The paper assumes the predicted initial solution is close enough to the optimum that KNN on hyperplane distances identifies active constraints. While the paper acknowledges the initial prediction may be biased (Section 3.4) and uses a progressive K update, it provides no diagnostic: no precision/recall of active constraint identification, no comparison of the reduced constraint set against the true active set, and no measurement of how often the solver encounters infeasibility due to overly aggressive reduction. This is a methodological gap for a component the paper cites as a key novelty.

- **The "weak correlation among small-scale MILPs obtained by problem division" claim is asserted without support.** Section 3.2 states this as justification for concatenating per-subproblem predictions, but provides no analysis or evidence. For tightly constrained problems (e.g., set covering with overlapping constraints), this assumption may not hold and could affect prediction quality.

- **The comparison of Light-MILPopt vs. GNN&GBDT is incomplete.** Both methods use scale-limited solvers (30-50% of variables). The paper shows Light-MILPopt outperforms GNN&GBDT, but it is unclear which of the additional components (graph partition, EGAT, constraint reduction, hierarchical crossover) drives this advantage. An ablation could resolve this and is the most critical missing experiment.

### Trivial

- **Table 2's "±" notation is unexplained** (standard deviation? range across seeds?). The paper should clarify.
- **The repair mechanism for infeasibility** (Section 3.4, line 165) is mentioned but not described in sufficient detail to assess correctness.

## Nice-to-Haves

- A runtime breakdown by pipeline stage (graph partition, EGAT inference, KNN distance computation, SCIP solve, crossover) would clarify where the time savings actually come from and address the question of whether the pipeline's total computation exceeds direct solver cost.
- Comparing against "SCIP on the same reduced subproblem" (i.e., giving the baseline solver the same variable/constraint reduction that Light-MILPopt produces, without the GNN) would separate the value of the reduction engineering from the neural prediction components.
- A learning curve (performance vs. training set size) would substantiate the "small training dataset" claim by showing where performance plateaus.

## Removed Points

These points from the inputs were removed after verification against the paper:

**Critical Issue 1 (Harsh Critic) — "Lightweight optimizer is not lightweight, comparison is circular":** REMOVED. The paper is transparent that the "lightweight optimizer" is SCIP restricted to αn variables (Table 1 caption: "scale-limited versions of SCIP"). The claim is that the *pipeline* outperforms running the full solver on the full problem — a legitimate contribution if the reduction is effective. Table 1 already compares *under the same running time*, directly contradicting the critic's assertion that this comparison was not done. Characterizing the comparison as "tautological" or "circular" misreads the paper's contribution.

**Critical Issue 4 (Harsh Critic) — "Implausibly large improvements without variance context"** (the portion claiming target value is undefined and baselines may be misconfigured): REMOVED. Table 2 states "under the same target value" — a standard evaluation protocol in optimization. The critic's speculation about baseline misconfiguration is not grounded in the paper. The valid sub-concern about variance reporting is retained as a Minor weakness above.

**Section 2.4 note — "EGAT is a wiring, not new architecture":** REMOVED. This describes many ML papers and is not a fatal criticism; the combination of half-convolutions and attention is non-trivial, and the paper does not overclaim architectural novelty.

**Convexity criticism (Problem Reduction notes):** REMOVED. The critic claims "the convexity property does not apply to the mixed-integer feasible set," but the paper explicitly limits its convexity argument to the linear constraint relaxation ("When without considering the integer constraints..." — Section 3.3). This is standard practice and not an error.

**Geometric mean justification criticism:** REMOVED. A design choice without theoretical justification is common for heuristic pipeline components; this is not a substantive weakness.

**"No reference supports the GNN&GBDT severely decreases claim":** REMOVED. This is framing/motivation language, not a formal claim requiring citation. The paper lists specific limitations (graph size, training data requirements, lack of constraint reduction) that are self-contained reasoning.

**Strength Finder points removed:** All six claimed strengths are concrete, specific to the paper, and supported by the experimental sections. None are dropped.

## Novel Insights

The reviews surface a tension that the paper itself does not address: the pipeline is designed to demonstrate that lightweight resources suffice, but the lack of ablation makes it impossible to attribute the gains to the neural components (EGAT, GNN prediction) versus the engineering of problem reduction (graph partition, variable/constraint reduction, crossover). A natural follow-up insight is that the paper's strongest evidence — the 200× speedup on some benchmarks — would be far more convincing if accompanied by a "reduction-only" baseline that uses heuristics (e.g., random variable fixing, basic KNN constraint retention) without learning. The reviews collectively suggest the paper's real contribution may be the reduction framework rather than the neural prediction, but this is not testable from the presented evidence.

## Suggestions

1. **Add an ablation study** that strips the pipeline in stages: (a) no reduction at all (full SCIP baseline — already done), (b) variable reduction only (no constraint reduction, no graph partition), (c) variable + constraint reduction, (d) full pipeline including graph partition and crossover. This would isolate which components drive the gains and directly address the most critical weakness.

2. **Report instance dimensions** (n variables, m constraints) for every benchmark MILP used, and clarify what "1% of the size of the benchmark MILPs" means (number of instances? fraction of variables?).

3. **Add statistical confidence** — report results over multiple random seeds with standard deviations or confidence intervals, and clarify what the ± notation in Table 2 represents.

4. **Validate the KNN constraint reduction** with a diagnostic: measure precision/recall of active constraint identification against the true active set (discoverable by solving the full instance once) to demonstrate the heuristic works as intended.
