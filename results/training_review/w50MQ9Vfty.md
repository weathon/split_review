Now I have all the information I need. Let me construct the final review.

## Summary

This paper proposes an experimental design for causal inference under network interference by partitioning the network into an independent set (no internal edges) and an auxiliary set. Treatment assignments on the independent set (Z_I) and interference exposure (ρ_I, determined by Z_A) can be separately controlled, enabling estimation of direct, spillover, and total treatment effects. The authors provide a theoretical lower bound on the independent set size from a greedy algorithm, analytic bias/variance bounds for the estimators, and simulation evidence across Erdős–Rényi, Barabási–Albert, and small-world graphs.

## Strengths

- **Novel, well-motivated design that formally decouples treatment and interference for a subset of units.** By partitioning the network so that V_I has no internal edges, the interference on these units becomes a deterministic function of Z_A only, while Z_I can be independently randomized. This clean graph-theoretic insight (Section 3.2, Figure 1) gives principled separate control that is impossible on the full graph, as the paper explicitly argues (lines 23–27).

- **Theoretical lower bound on independent set size from a greedy algorithm (Theorem 1).** The bound |V_I| ≥ (n log s)/s for ER random graphs is non-trivial and is larger than the ego-clusters bound by a factor of log s, providing a concrete sample-size guarantee for the design.

- **Analytic bias/variance bounds that connect optimization objectives directly to estimator quality.** Theorem 2 shows bias and variance of the direct-effect estimator are controlled by ‖Δ‖₁ (the deviation of interference from target), which the optimization in (4) minimizes. Theorems 3–4 show variance of spillover/total effect estimators depends inversely on Var[ρ_I], which (6) maximizes. This tight coupling between design optimization and statistical performance is a strong feature.

- **Simulation evidence across three graph families.** Results in Tables 2–3 and Figure 2 show the IS design consistently achieves lower bias and variance than CR, Full, graph cluster randomization, and ego-clusters across ER, BA, and small-world graphs with varying parameters, supporting the claim of superiority over conventional designs.

## Weaknesses

### Fatal
None.

### Major

- **Spillover and total effect experiments only test the exactly specified linear model.** The DGP in line 312 matches the linear model (9) exactly — the same model under which Theorems 3–4 guarantee unbiasedness. This biases the comparison in favor of IS (which uses linear regression) against other methods. The paper mentions non-parametric alternatives in one sentence (line 239) but provides no experiments with nonlinear outcomes, model misspecification, or sensitivity analysis to show how violations of the linear assumption would affect estimates. Without this, the claimed generality for spillover/total effect estimation (lines 40–41) is not fully supported. This is the most substantive gap in the empirical evaluation.

### Minor

- **The direct-effect experiments also use a linear DGP for all methods**, though here the IS estimator is difference-in-means (model-free). The large performance gap on BA and small-world graphs (IS bias 0.225–0.278 vs. CR/Full bias 0.96–1.30, Table 3) is partly explained by interference being uncontrolled in other designs, but the paper does not explain what estimator the baselines use. If Full and Graph Cluster use a simple difference-in-means on all units (without adjusting for interference), the comparison is less informative. The paper should clarify the estimators used for each baseline.

- **The theoretical results are conditional** (Theorems 2–4 condition on Y, G, Z_A), and the bounds on ‖Δ‖₁ and Var[ρ_I] are not connected to the graph-size bound of Theorem 1. The paper never bounds these terms in expectation over the random graph distribution, so the link between the independent set size guarantee and estimator performance remains qualitative. While conditional bounds are common in causal inference, connecting them to unconditional guarantees would strengthen the theoretical narrative.

- **The total effect estimator uses Z_i = 1_{ρ_i > 0.5}** (line 180). As Theorem 4 shows, the variance depends on Corr(Z_I, ρ_I), and this hard-thresholding induces strong correlation that could inflate variance. The paper does not discuss alternative thresholding schemes or their impact on variance.

- **Table 1 reports sample size as (n log s)/s** for "Independent Set" without qualifying that this is a lower bound for ER graphs from Theorem 1, nor that the column heading "Sample Size" conflates different quantities (n for full designs, n/(s+1) for ego-clusters which is an upper bound). This table is useful for high-level comparison but overstates the precision of the claims.

### Trivial

- The paper does not report standard errors or confidence intervals for the simulation results. With 2,000 replications these would be very small, but including them would improve presentation.

## Nice-to-Haves

- Testing the design under a nonlinear DGP (e.g., Y_i = α + βZ_i + γρ_i + δZ_iρ_i + ε) to assess robustness of the spillover/total effect estimators.
- An ablation comparing IS with random (unoptimized) Z_A versus IS with optimized Z_A — though the paper's CR baseline partially serves this purpose, it would be cleaner to vary only Z_A while keeping V_I fixed.
- Experiments with a misspecified observed graph (e.g., adding/dropping edges) to assess sensitivity to graph quality, which the paper itself lists as a limitation (line 386).

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The experimental comparison does not isolate the contribution of the independent set from the contribution of optimizing Z_A."** — Removed because it is factually wrong. The paper includes CR ("completely randomized design on the independent set") as a baseline, which uses the independent set partition without optimizing Z_A. Comparing CR vs. IS (both use the independent set; IS additionally optimizes Z_A) directly isolates the optimization component, as shown in Tables 2–3. The additional ask for a design that "optimizes Z_A but uses all units" is explicitly argued to be impossible (lines 23–27: "one cannot achieve separate controls on the treatment and the spillover of all units"). This is not a missing comparison; it is a request to solve a different problem.

- **"The bias bound in Theorem 2 is 2L‖Δ‖₁ / n_I, which could be large if L is large or ‖Δ‖₁ is not small."** — This is a generic observation about any upper bound. The whole point of the optimization (4) is to minimize ‖Δ‖₁. A bound being "potentially large" under unfavorable parameter choices is not a weakness of the paper.

- **"The paper overstates the extent of separation"** regarding Z_A and Z_I not being independent — removed. The paper claims separate *control* (line 178: "the unit-level treatments Z_I and the interference ρ_I can be separately controlled through Z_I and Z_A"), not stochastic independence. One can freely choose Z_I and Z_A as design parameters; this is a true statement and the paper does not mislead about it.

- **"The CR bias is sometimes close to IS (e.g., ER n=400, p=0.15)"** — Observations about diminishing gaps at larger n are not weaknesses; they describe scaling behavior. Moreover, the variance gap (CR: 0.096, IS: 0.067) remains meaningful.

- **"No statistical significance or confidence intervals"** — With 2,000 replications the Monte Carlo error is negligible. Mentioned as a minor presentation point above rather than a substantive weakness.

- Various style and formatting nitpicks from the section-by-section notes.

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface a genuinely novel observation that the paper itself missed.

## Suggestions

1. **Test nonlinear DGPs for spillover effects.** Add at least one experiment where the outcome model violates the linear additive assumption (e.g., includes an interaction Z_i × ρ_i or a nonlinear transformation of ρ_i) to demonstrate robustness and calibrate how severe the bias from misspecification can be.
2. **Clarify the estimators used by baseline methods** (CR, Full, Graph Cluster, Ego-Clusters) in both spillover and direct effect experiments. If baselines use simple difference-in-means on all units (ignoring interference), state this explicitly, and consider adding a baseline that uses a regression adjustment on the full graph as a fairer comparison.
3. **Add an unconditional expectation bound** for ‖Δ‖₁ or Var[ρ_I] under the ER random graph model to connect Theorem 1 (independent set size) to Theorems 2–4 (estimator performance).
4. **Discuss alternative Z_I assignments for total effect estimation** (e.g., independent Bernoulli instead of 1_{ρ_i>0.5}) and their impact on the correlation with ρ_I and the resulting variance.
5. **Quality the entries in Table 1** — indicate that the IS sample size is a lower bound for ER graphs, and that the ego-clusters entry is an upper bound.

## Score and Decision

This paper presents a genuinely novel and well-motivated design that cleanly leverages graph structure to achieve separate control of treatment and interference for causal inference on networks. The theoretical results (Theorems 1–4) are sound and correctly connect the optimization objectives to estimator performance. The simulations provide consistent support across multiple graph families. The main weakness is the reliance on a linear model for spillover/total effect estimation without testing robustness to model violations, and the lack of clarity about baseline estimators. These are addressable and do not undermine the core contribution of the independent-set design itself (which also shines for direct effect estimation via the model-free difference-in-means). The paper would benefit from additional experiments and clarifications but represents a solid contribution to the field.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>