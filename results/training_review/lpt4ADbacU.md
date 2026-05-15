Now I have all the information I need. Let me produce the consolidated review.

## Summary

This paper introduces soft-hard functions (HSFs), a novel framework for incorporating both hard constraints and soft aspiration levels into multi-objective optimization (MOO). The authors propose a two-step pipeline: (1) MoSH-Dense, which uses Bayesian optimization with random scalarizations to densely sample the Pareto frontier respecting HSF bounds (with a regret guarantee in Theorem 1), and (2) MoSH-Sparse, which uses the SATURATE algorithm for robust submodular optimization to sparsify the dense set into a small, navigable set of high-utility Pareto-optimal points (with a near-optimality guarantee in Theorem 2 via Lemma 1's submodularity proof). The framework is validated across diverse domains including brachytherapy treatment planning with real patient data, LLM personalization, engineering design, and neural network selection.

## Strengths

- **Novel soft-hard bounds framework** — The paper formalizes a practically motivated preference structure (piecewise-linear utility with hard constraints, soft aspiration levels, and saturation) that is intuitive for domain experts and has been underexplored in prior MOO work. Section 2.2 provides a clear mathematical definition with six regimes, and the brachytherapy motivation (e.g., "cover at least 90% of tumor but ideally over 95%") makes the practical need concrete.

- **Principled two-stage pipeline with theoretical grounding** — Step 1 provides a Bayesian regret bound (Theorem 1) showing convergence of the expected SHF utility ratio to 1 as T→∞, following the structure of Paria et al. (2020). Step 2 proves the utility ratio set function is submodular (Lemma 1) and leverages SATURATE's near-optimality guarantee (Theorem 2, Krause et al. 2008). While the two guarantees are not explicitly composed, the chain is logically sound: D approximates X (Theorem 1) → C approximates D (Theorem 2).

- **Diverse and practically grounded experimental validation** — Experiments span a real cervical cancer brachytherapy case with expert-defined clinical bounds, LLM personalization via proxy tuning, engineering design (four-bar truss), and deep learning model selection. The brachytherapy experiment uses actual patient data and published clinical guidelines (Viswanathan et al. 2012), demonstrating genuine deployment relevance.

- **Introduction of tailored soft-hard evaluation metrics** — Section 5.2 defines Fill Distance, Positive Samples Ratio, Hypervolume, and Distance-Weighted Score adapted for soft/hard regions, providing domain-specific evaluation beyond standard MOO metrics.

## Weaknesses

### Fatal
None.

### Major
None that are fatal to acceptance. However, several issues merit attention:

### Minor

1. **Connection between Step 1 and Step 2 guarantees is not made explicit.** Theorem 1 shows the expected SHF utility ratio over D converges to 1 (i.e., D approximates X in the utility sense). Theorem 2 guarantees C is near-optimal relative to D. The paper never states the composition: as T→∞, C achieves near-optimal utility relative to X. While logically implied, this gap in exposition could lead readers to question whether the sparsification guarantee has any bearing on the original problem over X. The authors should explicitly connect the two theorems and discuss finite-sample implications.

2. **Discretization of Λ for SATURATE is unspecified.** SATURATE requires a finite set of submodular functions {F_1,...,F_m}. The paper's formulation uses a continuous preference simplex Λ, but never explains how Λ is discretized in the experiments, how many samples m are used, or how discretization granularity affects the theoretical guarantee (Theorem 2's cost depends on m = |Λ|). This is an implementation detail that must be specified for reproducibility and to bridge theory and practice. (The algorithm pseudocode in Algorithm 2 takes "F_1,...,F_{|Λ|}" as input, but the source of this discrete set is never described.)

3. **Abstract overstates "optimal" instead of "near-optimal" for the sparsification guarantee.** The abstract says "we prove that (2) obtains the optimal compact Pareto-optimal set of points from (1)," but Theorem 2 (SATURATE) provides a solution C_S such that |C_S| ≤ ψk with ψ>1 — i.e., near-optimal up to a logarithmic factor in cardinality. The body text correctly uses "near-optimal" (Section 1, Contribution 2), so this is an inconsistency. The SATURATE guarantee is strong but not exacly optimal.

4. **No sensitivity analysis for HSF parameters β and ζ.** The paper fixes β=1.0 (post-soft slope fraction) and ζ=2.0 (saturation multiplier) without motivation or robustness checks. Since the entire framework's behavior depends on these parameters, ablation over a range (e.g., β∈{0.25,0.5,1.0}, ζ∈{1.5,2.0,3.0} on at least one synthetic problem) would strengthen empirical validation.

5. **The ">99% of maximum desired utility" claim relies on a simulated λ\***. The Step 2 evaluation (Section 5.2.2) simulates the DM's unknown preferences λ* using a Gaussian centered at the soft bound. While this is a reasonable operationalization, results may be sensitive to this simulation choice. The 99% claim should be caveated as reflecting this simulation setup, and the paper's abstract/conclusion statements would benefit from this qualification.

6. **No statistical significance assessment for the 3% brachytherapy improvement.** The bar plot (Figure 5/7) shows MoSH achieving >3% higher utility than the next best approach, but no p-values, confidence intervals, or effect-size measures are reported. With only error bars shown, it is unclear whether this advantage is statistically robust across runs.

### Trivial

- The abstract uses "optimal" when the body correctly says "near-optimal" (see Weakness 3 above).
- The notation \division appears throughout, likely a LaTeX formatting artifact from PDF extraction — not an author error.

## Nice-to-Haves

- **Full Cartesian-product pipeline comparison.** The paper evaluates Step 2 with different sparsification methods on the same dense set (Figure 5, first four plots) and evaluates different Step 1 methods with the same MoSH-Sparse sparsifier (Figure 5 bar plot). A full comparison of, e.g., (MOBO-RS + greedy sparsification) vs (MoSH-Dense + MoSH-Sparse) would strengthen the holistic claim. The current decomposition is reasonable but leaves this cross-product untested.

- **Qualitative visualization of the sparse set.** Showing the 5–10 points returned by MoSH-Sparse in objective space for the brachytherapy problem, with soft/hard bounds overlaid, would help readers assess whether the sparse set is indeed diverse and respects the bounds.

- **Comparison with a direct single-step method addressing the minimax problem.** The paper could discuss whether Equation (1) could be approximately solved in one stage (e.g., via an acquisition function that explicitly models robustness to unknown λ), clarifying the advantage of the two-step decomposition.

## Removed Points

These points were flagged by the reviewers but are removed or weakened after cross-checking against the paper:

- **Lemma 1 submodularity critique** — The harsh critic initially questioned whether max_{x∈C} s_λ(u_f(x)) is submodular, then performed their own analysis and retracted the concern, concluding "it is submodular." Removed because the critic themselves resolved this in the paper's favor.

- **β_t choice in UCB acquisition function** — The critic questioned β_t = √(0.125×log(2t+1)) as "not the typical choice." The paper explicitly cites Paria et al. (2019) for this choice, which is a standard reference. Removed as the criticism ignores the cited justification.

- **"Consistently leads" overclaim accusation** — The critic claimed the NN experiment contradicts the "consistently leads" claim. Verifying the paper: the NN experiment (Section 5.1.4) acknowledges "our algorithm does not surpass the baselines in all four of the metrics" but the "consistently leads" claim is about the SHF utility ratio (Step 2), not the four Step 1 metrics. The Step 2 plots and bar plot uniformly favor MoSH. The claim is supported by the evidence. Removed.

- **Step 2 algorithm novelty criticism** — The critic claimed SATURATE merely applies an existing method. The paper never claims SATURATE is novel; contribution 2 is the formulation of PF sparsification as RSOS, proving submodularity (Lemma 1), and connecting it to the HSF framework. The adaptation is the contribution. Removed as a strawman.

- **Pure formatting/style nitpicks** — Removed per hard rules.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any observation about the paper that the paper itself does not articulate.

## Suggestions

1. **Explicitly connect Theorem 1 and Theorem 2.** Add a sentence or short paragraph explaining that as T→∞, Theorem 1 guarantees the dense set D achieves the optimal utility over X in expectation, and Theorem 2 guarantees C achieves near-optimal utility relative to D. By composition, MoSH returns a set near-optimal for the original problem over X. This addresses the most concerning structural criticism directly.

2. **Specify the Λ discretization used in experiments.** Describe how many weight vectors are sampled, by what method (e.g., uniform grid, Dirichlet sampling), and how this choice affects the SATURATE guarantee. Add this to the Step 2 experiment setup.

3. **Add sensitivity analysis for β and ζ** on at least the Branin-Currin synthetic problem to demonstrate robustness of the HSF framework to parameter choice.

4. **Caveat the 99% claim** in the abstract/conclusion to clarify it reflects simulated λ* and may not generalize to all real DM preference distributions.

5. **Add a statistical significance test** for the 3% brachytherapy improvement, or at minimum report effect sizes and confidence intervals.

6. **Fix the "optimal"→"near-optimal" inconsistency** in the abstract to match the body's more precise language.

## Score and Decision

**Overall assessment:** The paper introduces a genuinely novel and practically motivated framework (soft-hard functions) for preference-guided multi-objective optimization. The two-step pipeline is technically sound, combining Bayesian optimization with submodular sparsification. The theoretical guarantees are appropriate (a regret bound for Step 1 and SATURATE's near-optimality for Step 2), though their composition could be made more explicit. The experimental validation is impressively diverse, including a real clinical brachytherapy case with expert-defined bounds — a rare and valuable contribution. The main weaknesses are presentation gaps (Λ discretization unspecified, connection between guarantees not made explicit, abstract overclaim of "optimal"), missing sensitivity analysis, and incomplete statistical reporting. None of these undermine the core contribution, but they reduce clarity and reproducibility. The paper would benefit from a revision addressing these issues but is otherwise a solid contribution to the MOO literature with clear practical relevance.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>