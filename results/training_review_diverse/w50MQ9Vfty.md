Here is my consolidated review.

## Summary

This paper proposes a novel experimental design for causal inference under network interference. The key idea is to partition the network into an independent set (no internal edges) and an auxiliary set, then separately control treatment assignments (via $\boldsymbol Z_I$) and interference exposure (via $\boldsymbol\rho_I = \boldsymbol\Gamma\boldsymbol Z_A$ on the independent set). The paper provides theoretical bounds on independent set size from a greedy algorithm, bias/variance expressions for direct, spillover, and total effect estimators, and simulations on synthetic graphs.

## Strengths

1. **Novel design enabling separate control of treatment and interference**: The partition into an independent set and auxiliary set is a principled innovation that directly addresses the entanglement problem. By construction, $\boldsymbol Z_I$ controls unit-level treatment while $\boldsymbol\rho_I = \boldsymbol\Gamma\boldsymbol Z_A$ is determined solely by the auxiliary set's assignments, giving experimenters separate handles on the two sources of variation (Section 3.2). This is a distinct conceptual advance over cluster-based designs that require isolated groups.

2. **Theoretical link between optimization objectives and estimator quality**: Theorems 3 (estimating direct effects), 4 (spillover effects), and 5 (total effects) provide analytic bias and variance expressions that explicitly connect the optimization objectives (minimizing $\|\boldsymbol\Delta\|_1$ for direct effects, maximizing $\mathrm{Var}[\boldsymbol\rho_I]$ for spillover/total effects) to estimator performance. Bias for direct effects is bounded by $2L\|\boldsymbol\Delta\|_1/n_I$, and spillover effect variance is inversely proportional to $n_I\mathrm{Var}[\boldsymbol\rho_I]$, giving a clear rationale for the proposed optimizations.

3. **General framework for multiple causal estimands**: The design supports direct, spillover, and total treatment effects within a single approach by adjusting the optimization of $\boldsymbol Z_A$ and the assignment $\boldsymbol Z_I$, unlike methods that target a single effect (Strengths Finder notes Karwa et al. focus only on treatment effects).

4. **Strong empirical trends across diverse graph models**: Simulations on Erdős–Rényi, Barabási–Albert, and small-world graphs (Tables 1–2, Section 5) consistently show the independent-set design achieving lower bias and variance than CR, full-graph, graph cluster, and ego-cluster designs. For example, in estimating spillover effects on an ER graph with $n=200, p=0.15$, IS yields bias 0.315 and variance 0.124 vs. the next best (Full) 0.366 and 0.178.

5. **Clear comparative framing via Table 1**: The systematic comparison with competing designs along network assumption, effective sample size, and interference control makes the trade-offs explicit and situates the contribution.

## Weaknesses

### Fatal
None.

### Major

1. **Mischaracterization of the variance-maximization optimization (Eq. 7, line 223)**: The paper states that maximizing $\boldsymbol Z_A^T\boldsymbol\Gamma^T(\boldsymbol I - \tfrac{1}{n_I}\boldsymbol 1\boldsymbol 1^T)\boldsymbol\Gamma\boldsymbol Z_A$ over $\{0,1\}^{n_A}$ is "concave quadratic programming." The matrix $\boldsymbol\Gamma^T(\boldsymbol I - \tfrac{1}{n_I}\boldsymbol 1\boldsymbol 1^T)\boldsymbol\Gamma$ is positive semidefinite, making the objective **convex**, not concave. Maximizing a convex quadratic over binary variables is NP-hard in general. The paper does not acknowledge this hardness, provides no approximation algorithm or rounding scheme, and the claim "the support can be expanded to its convex hull $[0,1]^{n_A}$ while keeping the same solution" — while technically true for the *optimal value* (max of a convex function over a hypercube is attained at a vertex) — does not render the problem tractable. This directly undermines the paper's claim (line 41) that assignments can be "optimized directly."

   Same issue affects the ℓ₁-minimization in Eq. (6): the objective is convex but the binary constraint makes it an integer program with no algorithm or approximation guarantee provided.

2. **No viable algorithm for the proposed optimizations**: The paper defines two optimization problems over $\boldsymbol Z_A \in \{0,1\}^{n_A}$ (Eqs. 6 and 7) as core to the method, but provides no algorithm, heuristic, relaxation, or complexity analysis for either. The greedy Algorithm 1 addresses only the independent set selection, not the assignment optimization. While future computational work is mentioned (line 387), the paper as written does not present a reproducible experimental design procedure. This is a gap in the contribution, not just a missing implementation detail.

### Minor

1. **Independent set size ($n_I$) not reported in simulations**: The simulation results (Tables 1–2) report bias and variance without ever reporting the achieved $n_I$ for each graph configuration. Since estimator variance scales inversely with $n_I$, the reader cannot assess whether the reported variance improvements are driven by larger independent sets or by the optimization of $\boldsymbol Z_A$. No standard errors on the Monte Carlo estimates are provided either.

2. **Scope of theoretical guarantees narrower than claimed applicability**: Theorem 1 (independent set size) is proved only for Erdős–Rényi random graphs, yet the paper claims the method works on "arbitrary networks" (lines 43, 384). Theorems 4–5 (spillover and total effects) assume the linear additive model (Eq. 4), but the method is presented as a general framework. The paper would benefit from explicitly delineating which claims are theoretically supported and which are empirically demonstrated.

3. **Inconsistency in Table 1**: The table lists the network assumption for the Independent Set design as "random, sparse," while the text repeatedly claims applicability to arbitrary networks. This should be reconciled: the theoretical bound is for random sparse graphs, but the design itself can be applied to any graph (you can always find an independent set). Clarifying this would prevent confusion.

4. **No sensitivity analysis for the outcome model**: Simulations use a single linear data-generating process ($Y = \alpha + \beta Z + \gamma\rho + \epsilon$) with fixed effect sizes ($\beta=20, \gamma=10$). The method's behavior under nonlinear interference (e.g., threshold effects, interaction between $Z$ and $\rho$) is not explored, which limits the empirical support for generality.

5. **Strong unconfoundedness assumption**: Assumption 2 (network $\indep$ potential outcomes) is needed to address selection bias from the non-node-symmetric independent set algorithm, but its plausibility in real networks (where homophily and shared latent factors create dependence) is not discussed.

### Trivial
None that survive filtering (the paper has no formatting artifacts, typos, or missing appendices in the original).

## Nice-to-Haves
- A discussion of approximation algorithms or convex relaxations for the binary optimizations (Eqs. 6, 7) would significantly strengthen the contribution.
- Reporting $n_I$ for each simulation configuration and adding standard errors would improve transparency.
- A comparison of different independent set selection strategies (greedy vs. random vs. degree-based) would help practitioners.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Critic's claim that "the maximum over the continuous relaxation $[0,1]^{n_A}$ can be strictly larger than any binary solution" (Section 1 of Critic's Issues)**: This is mathematically incorrect for maximizing a convex function over a hypercube — the maximum is attained at an extreme point (a binary vector). The real issue is the mischaracterization as "concave" and the NP-hardness of finding the optimum, not a gap between the discrete and continuous optima.
- **"No confidence intervals or hypothesis tests in the simulations"**: Standard for simulation studies in causal inference papers at this level; not an omission.
- **"No handling of multiple treatments or continuous treatments"**: Scope-creep; the paper clearly focuses on binary treatment.
- **"No assessment of the impact of the independent set selection algorithm"**: A reasonable suggestion but not a flaw given the paper's scope.
- **"No discussion of the computational cost"**: Partially acknowledged as a limitation (line 386). The real gap is the lack of any optimization algorithm, not the absence of runtime analysis.
- **"Missing appendix, missing proofs in appendix"**: The paper's original submission (before parsing) may have included these; parser artifact.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fix the optimization characterization**: Correct "concave" to "convex" in line 223, add a discussion of NP-hardness, and either (a) provide a tractable approximation algorithm (e.g., randomized rounding of an SDP relaxation, or a greedy heuristic) with some guarantee, or (b) explicitly state that the optimization objectives are design criteria and the paper's theoretical results bound estimator performance for *any* $\boldsymbol Z_A$, with the optimization serving as a guide rather than a required step.

2. **Report $n_I$ and Monte Carlo uncertainty in simulations**: Add a column showing the average $n_I$ achieved by the greedy algorithm for each configuration, and report standard errors of the bias/variance estimates. This would allow readers to assess whether the improvements are primarily from larger $n_I$ or from the $\boldsymbol Z_A$ optimization.

3. **Reconcile Table 1 with the text**: Clarify that "random, sparse" refers to the *theoretical lower bound* on $n_I$, while the *method itself* applies to any graph (with $n_I$ determined empirically).

4. **Add at least one nonlinear outcome model** (e.g., $Y = \alpha + \beta Z + \gamma\rho + \delta Z\rho + \epsilon$) to the simulations to demonstrate robustness beyond the linear additive case.

## Score and Decision

This paper introduces a genuinely novel design idea — the independent-set partition for separate control of treatment and interference — that addresses a real problem in network causal inference. The theoretical connections between optimization objectives and estimator bias/variance are well-motivated. However, the central computational weakness (mischaracterized optimization, no algorithm provided, NP-hardness unacknowledged) is a significant gap. The paper's contribution lies in the design framework and theoretical bounds, which stand independently of whether the optimizations can be solved exactly. But the paper overstates its methodological completeness by claiming assignments can be "optimized directly."

The paper is acceptable in principle for a venue that values novel experimental designs with theoretical grounding, provided the authors clearly acknowledge the computational limitations and discuss practical approximations. It is not acceptable in its current form due to the misleading optimization claim and the lack of any implementable procedure for the $\boldsymbol Z_A$ assignment.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>