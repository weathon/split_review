Now I have a thorough understanding of the paper. Let me construct the final consolidated review.

## Summary

This paper proposes DiffILO, an unsupervised learning framework for solving binary integer linear programs (ILPs) without traditional solver labels. The core idea is to transform the discrete, constrained ILP into a continuous, differentiable (almost everywhere) merit function via probabilistic modeling, reparameterization via relaxed Bernoulli/Gumbel-Softmax, and penalty methods. A GNN predictor is trained end-to-end by minimizing this merit function. Experiments on set covering (SC), maximum independent set (IS), combinatorial auctions (CA), and two MIPLIB subsets show a 13.2× average training speedup over supervised Predict-and-Search, with competitive or better solution quality on most benchmarks.

## Strengths

- **Novel theoretical framework for unsupervised ILP learning.** The paper establishes equivalence theorems (Theorems 1–2) between the original ILP (P1) and the probabilistic reformulation (P2), an exact penalty theorem (Theorem 3) showing optimal solutions are preserved for sufficiently large penalty coefficients, and a differentiability guarantee (Theorem 5) for the surrogate loss. This provides principled motivation for the approach, going beyond prior problem-specific differentiable methods (Section 3.1–3.2).

- **Demonstrated 13.2× average training speedup.** Figure 3 shows that DiffILO achieves substantial training time reduction across all three main benchmarks compared to the supervised PS baseline, by bypassing expensive solver-based label collection (Section 4, Figure 3).

- **Competitive solution quality on IS and CA benchmarks.** On test instances, DiffILO achieves feasibility ratios of 97.1% (IS) and 99.4% (CA), substantially outperforming PS. Table 1 shows that DiffILO+Gurobi obtains objective values closer to best-known solutions than PS+Gurobi at 10s, 100s, and 1000s on SC and CA (Section 4, Figure 4, Table 1).

- **Case study provides insight into optimization dynamics.** The 2-variable illustrative example (Figure 7) demonstrates that DiffILO's stochastic optimization finds the optimal solution in all 20 runs, whereas optimizing the closed-form penalty function converges to a suboptimal solution in 11/20 runs, providing insight into why the sampling-based approach helps escape poor local minima (Section 4, Case Study).

## Weaknesses

### Fatal
None.

### Major

- **SC feasibility is poor (50.8%) without sufficient analysis.** DiffILO finds at least one feasible solution (among 30 samples) on only 50.8% of SC test instances. While PS is even worse, this means the method fails to produce any feasible solution on roughly half of SC instances. The paper reports this number transparently but does not analyze *why* SC is harder, nor does it discuss potential remedies (e.g., more samples, different penalty schedules, constraint tightening). The abstract's claim of "generating feasible and high-quality solutions" is in tension with this result, which represents a significant limitation for a method whose title promises "Differentiable Integer Linear Programming" in general (Section 4, Figure 4; compare with abstract lines 6–11).

- **The practical surrogate loss (P4) diverges from the theoretically analyzed exact forms (P2)/(P3) without analysis of the gap.** Theorems 1–3 establish equivalence between (P1) and the exact probabilistic formulation (P2)/(P3). However, training minimizes the surrogate (P4), which introduces three approximations: (i) Monte Carlo samples replace the exact expectation, (ii) the violation indicator uses rounded binary variables (ψ) while gradients flow through the continuous surrogate (ξ), and (iii) the penalty term is finite-sample. The paper acknowledges these approximations (Section 3.2, Eq. 2) but provides no analysis of how they affect the theoretical guarantees. Theorem 3 (exactness) applies to (P3), not (P4), and the relationship between optimal solutions of (P4) and (P1) is uncharacterized. This gap weakens the paper's central claim of a *theoretically grounded* unsupervised reformulation (Section 3.1–3.2).

### Minor

- **The gradient estimator's bias is unexamined.** The design choice — using ξ (relaxed Bernoulli) for gradient flow while using ψ (binary rounded) for the violation indicator — creates a straight-through-like estimator whose bias is not analyzed. The paper is transparent about this implementation (Eq. 2, lines 126–129; Remark 8) and provides Theorem 5 showing differentiability a.e., but does not characterize the bias, compare to alternatives (e.g., using ξ directly in a soft indicator), or discuss how it affects convergence. This is a methodological gap that makes it difficult to fully trust that the training dynamics solve the intended problem (Section 3.2).

- **Several implementation details needed for reproducibility are missing.** The paper specifies training epochs, cosine annealing, dynamic μ adjustment, and epoch selection criteria, but does not report the number of samples K per instance, the GNN architecture (layers, hidden dimensions), the learning rate values/schedule specifics, the optimizer choice (beyond mentioning SGD), or the μ schedule details. These are not trivial omissions — K and the penalty schedule directly affect the bias-variance tradeoff and feasibility outcomes — and they prevent independent reproduction (Section 3.3, Section 4 "Training and Inference").

- **The novelty claim is slightly overstated.** The paper claims to be "the first method to employ pure ML techniques for training, without relying on traditional solvers" for "general ILPs." Prior work (Karalias & Loukas, 2020; Erdos Goes Neural) proposed similar differentiable, unsupervised approaches for combinatorial optimization on graphs. The paper acknowledges this work and distinguishes itself by targeting general ILPs rather than specific problems, which is a reasonable distinction. However, the experiments still cover only binary problems on three synthetic benchmarks and two MIPLIB subsets, and the neos results are honestly reported as inconclusive. The claim would benefit from tempering or more precise qualification (Section 1, line 28; Section 5, line 255).

### Trivial

- The gradient formula in the extracted text (Eq. 8, lines 179–183) contains apparent formatting artifacts. The original submission likely presents this clearly.
- The paper could benefit from error bars or standard deviations on key results in Table 1 and Figure 4 to aid statistical interpretation.

## Nice-to-Haves

- **Ablation on K (number of samples).** The paper uses K Monte Carlo samples but does not study how this affects gradient variance, feasibility rates, or convergence speed.
- **REINFORCE comparison.** Remark 5 claims REINFORCE is less efficient but provides no empirical comparison. A small experiment showing gradient variance or convergence would strengthen this design choice.
- **SC failure diagnosis.** A brief analysis of why SC is harder (e.g., constraint density, loose constraints, penalty landscape) and what changes might improve the 50.8% rate.
- **Convergence curves** of the training loss/feasibility on validation instances over epochs, beyond the final test results shown.

## Removed Points

- *"The paper does not specify the actual implementation" (of the gradient estimator).* — Factually incorrect; the paper explicitly describes using ξ for gradients and ψ for the indicator in Equation (2) and surrounding text (lines 126–129). Removed as factually wrong.
- *"Equation (8) is garbled."* — Parser artifact, not an author error. Removed per hard rule on formatting artifacts.
- *"The paper does not specify...the exact procedure for selecting the best epoch."* — The paper does specify this: "selecting the best epoch based on their average objectives" (line 216). Removed as factually wrong.
- *"The paper does not specify...the learning rate schedule beyond mentioning cosine annealing."* — The paper states "cosine annealing" is used; specific learning rate values are indeed missing but this is merged into the more general missing-details point above rather than listed as a separate weakness.
- *Claims about missing appendix or proofs.* — Not present in the critic's text; no removal needed.
- *Criticism about limited benchmarks / should cover more domains.* — The paper covers 3 main benchmarks + 2 MIPLIB subsets, which is reasonable for its scope. Scope-creep demands for broader coverage removed.
- *Several "Other Observations" (speedup is meaningful, case study too small, variance not discussed).* — The speedup observation is a strength already captured; the case-study-size concern is too minor to warrant inclusion; the variance concern is subsumed by Weakness 3.

## Novel Insights

Beyond the paper's own contributions, the most interesting signal from the reviews is the fundamental tension the paper illuminates but does not resolve: the gap between the theoretically elegant reformulation (exact equivalence of the probabilistic ILP to the original) and the messy practical estimator (biased, straight-through-like, finite-sample). The paper implicitly acknowledges this gap but treats it as a practical engineering detail. For future work, the key question is whether the bias of the gradient estimator actually *helps* (as the case study suggests — it helps escape local minima that the exact closed-form penalty gets stuck in) or whether it introduces harmful noise on larger problems (as the SC results might suggest). The paper's case study on a 2-variable problem provides a hint that the stochasticity is beneficial, but a systematic characterization of when the bias helps vs. hurts would be a significant contribution in its own right.

## Suggestions

1. **Analyze the theory-practice gap.** Either extend the theoretical analysis to cover the surrogate (P4), or explicitly characterize the conditions under which (P4)'s optima relate to (P1)'s. If the surrogate cannot be theoretically grounded, the paper should be clearer about the limits of its theoretical claims.

2. **Diagnose and discuss the SC failure.** Provide ablations (varying K, μ schedules, post-processing rounding/repair) to understand why SC is harder and whether it's inherent or fixable. This would significantly strengthen the paper's practical claims.

3. **Characterize the gradient estimator bias.** Even an empirical comparison (e.g., comparing against a fully soft indicator using ξ directly, or against REINFORCE on a small problem) would help readers understand whether the ψ-based indicator is essential or incidental.

4. **Release a detailed hyperparameter table** in a supplement or appendix covering: GNN architecture (layers, hidden dimensions, activation functions), K, learning rate, optimizer, μ initial value and update rule. This is essential for reproducibility.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>