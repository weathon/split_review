Now I have a thorough understanding of the paper and can verify the reviewer claims against the actual content. Let me produce the final consolidated review.

## Summary

This paper proposes VP-OR, a two-stage reoptimization framework for MILPs under dynamic parameter changes. The first stage uses a GNN to predict marginal probabilities for binary variables and feasible ranges for integer/continuous variables (using a logarithmic transformation and binary encoding with a sign bit). The second stage iteratively selects which variables to fix using per-variable Beta distributions inspired by Thompson Sampling, with update rules driven by whether the resulting solution improves over previous iterations. Experiments on nine datasets from the MIP 2023 Competition compare against SCIP, Re Tuning (Patel, 2024), and two GNN-based baselines.

## Strengths

- **Novel handling of integer and continuous variables in reoptimization.** The paper extends GNN-based variable prediction beyond binary-only settings by using a logarithmic transformation followed by binary encoding with a sign bit (Section 3.2). This is a practical contribution since many real-world MILPs have few binary variables (e.g., the "vary matrix rhs bounds" dataset has 400 binary out of 27,710 variables). Table 1 demonstrates that the prediction model makes relatively few mispredictions across diverse datasets, suggesting the encoding scheme scales.

- **Leveraging historical branch-and-bound information as features.** The paper incorporates dual solutions and feasible basic variables from the leaf node of the base instance's branch-and-bound tree (Section 3.1), going beyond prior end-to-end methods that only use the optimal solution and problem structure. This is a conceptually sound approach—dual information from the leaf node can capture which variables and constraints are sensitive to parameter changes.

- **Consistent empirical advantage over strong baselines.** Despite the small test sets, VP-OR finds feasible solutions on all nine datasets within 10 seconds (Table 3), where even the first-place MIP 2023 competition method (Re Tuning) fails on some datasets. The relative gap results (Table 4) show VP-OR consistently achieving lower primal gaps, especially on bound-change and right-hand-side-change scenarios.

## Weaknesses

### Fatal

None.

### Major

- **The Thompson Sampling framing is misleading and the algorithm does not solve the described bandit problem.** The paper describes a combinatorial MAB with 2^{C(p, a%×p)} arms (line 165) but then implements a per-variable scoring heuristic: independently sample μ_i from each variable's Beta distribution, rank by min(μ_i, 1-μ_i) (binary) or μ_j (continuous/integer), and select the top a%. This is not Thompson Sampling over the arm space; it is a heuristic selection rule with Bayesian-inspired per-variable updates. The paper acknowledges an independence assumption (line 167) but the gap between claiming to solve a combinatorial MAB and implementing per-variable independent scoring is large. The update rules for the Beta parameters (lines 168–172) are also ad-hoc: for continuous/integer variables, the rule explicitly says "no immediate conclusion about its benefit can be drawn" when a newly selected variable coincides with improvement, meaning the algorithm never learns that adding a variable to the selected set is beneficial. The method may work well, but the bandit framing is not an accurate characterization, and the paper should either (a) reframe the online stage as a heuristic procedure with empirical motivation, or (b) justify why the per-variable independence assumption yields a valid approximation to the combinatorial bandit.

- **The experimental evaluation is too weak to support strong comparative claims.** Each dataset has only 5 test instances (line 178: 25 paired groups split into 20 training, 5 test). No confidence intervals, standard deviations, or statistical significance tests are reported for any metric in Tables 3, 4, or Figure 2. With 5 test instances per dataset, a single outlier or a different random split could produce different rankings. For a paper claiming to outperform multiple baselines across several benchmarks, this is insufficient evidence. At minimum, the authors should report results over multiple splits (e.g., cross-validation) with variance estimates, or use leave-one-out evaluation. This is the most significant barrier to accepting the paper's empirical claims.

### Minor

- **The GNN architecture is underspecified in the main text.** The paper states that the model was "implemented in PyTorch" and "optimized using Adam with training batch size of 16" but provides no details on number of GNN layers, hidden dimensions, edge/variable/constraint feature dimensions, message-passing scheme, or loss function. While some of these details may reside in the (stripped) appendix, the main text should at least summarize the architecture. This makes it difficult for readers to assess the method's complexity or reproduce it from the paper alone.

- **No sensitivity analysis for the fixed-variable percentage (P=0.7).** Table 2 compares 50% vs. 70% fixed variables for binary vs. all-variable fixing, but the main experiments use P=0.7 with no ablation showing how this parameter interacts with prediction accuracy or problem structure. Given that this parameter directly controls the trade-off between search space reduction and risk of infeasibility, its impact should be characterized.

- **No ablation study isolating the contribution of each component.** The two-stage framework combines: (a) GNN predictions, (b) leaf-node features, (c) the online refinement stage. Without an ablation that compares against simpler alternatives (e.g., fixing variables directly from GNN confidence, or using the online stage without GNN predictions), it is unclear which component drives the gains. The claim about the Thompson Sampling stage's value is particularly in need of ablation given the framing concerns above.

- **The reward function is very sparse and the rationale for its design is unsupported.** The reward is 1 only when the solution improves over all previous solutions, and 0 otherwise. The paper asserts (line 166) that using the objective value directly would "reduce the motivation for exploration," but provides no ablation study comparing reward formulations. This claim needs empirical backing.

- **The relaxation mechanism's overhead is not separated.** When the fixed-variable subproblem is infeasible, the algorithm divides fixed variables into 10 groups and solves iteratively. Since the reported run times include this overhead, the paper should report how often infeasibility occurs and how much time the relaxation adds.

### Trivial

- **Convergence plots (Figure 2) are shown for only 3 of 9 datasets** without a clear selection criterion.
- **Training time of the GNN model is not reported**, which is relevant for practical deployment.

## Nice-to-Haves

- A discussion of the applicability of VP-OR when the base instance cannot be solved to optimality or when full branch-and-bound logs are not available. The current method assumes these, which limits deployment in some real-world settings.
- A discussion comparing the proposed confidence-threshold encoding for integer/continuous variables against simpler alternatives (e.g., directly widening bounds from the base solution).

## Removed Points

- **Criticism that PS and ND baseline adaptations for integer/continuous variables are not described**: The paper references an appendix for baseline implementation details ("See Appendix 2 for implementation details of these baselines," line 177). Since the parser strips appendices, this criticism cannot be verified and is removed per hard rules.
- **Criticism about method assuming base instance is solved to optimality**: This is inherent to the reoptimization setting and the paper is explicit about it. It belongs in Nice-to-Haves as a scope discussion point, not a weakness.
- **Strength about "Online refinement via Thompson Sampling for variable selection"**: This conflicts with the verified weakness that the Thompson Sampling framing is misleading. Per rules, when a strength and weakness disagree, the weakness wins. Moved here.

## Novel Insights

The most interesting tension in the reviews is between the paper's genuine empirical contribution (consistently finding feasible solutions where baselines fail) and the methodological imprecision of the online stage. The paper frames the variable selection problem as a combinatorial bandit but implements a per-variable heuristic that does not match the described formalization. This gap matters because it obscures what the online stage actually contributes: is it the Bayesian update mechanism that drives improvement, or simply the iterative refinement with any scoring rule? A properly controlled ablation—comparing the Thompson Sampling heuristic against greedy selection from GNN confidence, or against random iterative refinement—would resolve this and potentially strengthen the paper by showing which design choice is essential. The empirical results are promising enough to warrant a more rigorous evaluation and a more honest characterization of the method.

## Suggestions

1. **Reframe the online stage honestly.** Drop the pretense of solving a combinatorial bandit and describe the method as a per-variable heuristic that uses Beta-distribution sampling and score-based selection. If the Bayesian update scheme has theoretical justification (e.g., as an approximation to combinatorial Thompson Sampling), provide it; otherwise, acknowledge the heuristic nature explicitly.

2. **Strengthen the experimental evaluation.** Report results over multiple random train/test splits (e.g., 5-fold) with standard deviations or confidence intervals. With 50 instances per dataset, this is straightforward and would dramatically increase confidence in the claims.

3. **Run controlled ablation studies.** Isolate the value of (a) leaf-node features in the GNN, (b) the GNN predictions themselves, (c) the online refinement stage versus simply fixing the GNN's top-confidence predictions directly, and (d) the proposed reward function versus using objective values.

4. **Provide GNN architecture details** in the main text (layers, hidden dimensions, feature dimensions, loss function) to improve reproducibility.

5. **Characterize sensitivity to P** (the percentage of fixed variables) and report the frequency and cost of the infeasibility relaxation mechanism.

## Score and Decision

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>