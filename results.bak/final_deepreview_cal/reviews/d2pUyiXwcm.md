## Summary

This paper proposes SCaSML, a framework that corrects a pre-trained SciML surrogate (PINN, GP) for high-dimensional semi-linear parabolic PDEs by deriving the error's governing PDE (called the Structural-preserving Law of Defect) and solving it via Multilevel Picard (MLP) Monte Carlo simulation at inference time, without retraining. The method is motivated by an analogy to inference-time scaling in LLMs. The paper provides a theoretical product error bound (Theorem 2.5) showing that final error is the product of surrogate error and simulation error, yielding an improved convergence rate of \(O(m^{-\gamma-1/2})\). Experiments on PDEs up to 160 dimensions show 20–80% error reduction over the base surrogate.

## Strengths

- **Novel combination of defect correction + MLP preserving semi-linear structure (Fact 2.3).** The derivation showing that the defect PDE for a semi-linear parabolic equation retains the original semi-linear form is the key enabler for using Feynman–Kac-based stochastic solvers (specifically MLP) to correct the surrogate. Classical defect-correction methods rely on grid-based expansions that do not extend to Monte Carlo solvers; this work bridges that gap in a principled way.

- **Theoretical product error bound and improved scaling law (Theorem 2.5, Corollary 2.6).** The paper proves that the final \(L^2\) error is bounded by the *product* of the surrogate error and the MLP simulation error. This yields an improved convergence rate \(O(m^{-\gamma-1/2+\alpha(1)})\) with total budget \(2m\), which is strictly faster than the surrogate alone (\(O(m^{-\gamma})\)) or a pure Monte Carlo solver (\(O(m^{-1/2})\)). This theoretical result is clean and goes beyond generic hybrid claims.

- **Consistent error reduction across high-dimensional PDEs up to 160d (Table 1, Figure 3a).** The method reduces relative \(L^2\) error by 20–80% compared to the base surrogate on all five test problems: linear convection-diffusion (10–60d), viscous Burgers (20–80d), HJB/LQG (100–160d), and diffusion-reaction (100–160d). The naive MLP solver frequently fails or underperforms the surrogate, while SCaSML consistently improves upon it.

- **Inference-time scaling behavior demonstrated (Figure 3b).** SCaSML shows that allocating more Monte Carlo samples at inference time steadily reduces solution error across all tested systems, providing an *elastic compute* capability — users can trade additional inference compute for higher accuracy.

- **Surrogate-agnostic operation.** The method works as a plug-and-play corrector for both PINN and GP surrogates without modifying their architecture or training procedure (Table 1: VB-PINN vs VB-GP), demonstrating broad applicability.

- **Well-motivated why Monte Carlo is suited for the correction step (end of §2.1).** The paper explains that neural network surrogates suffer from spectral bias, leaving a high-frequency residual error that is irregular — precisely the regime where Monte Carlo methods excel, since their convergence rate is independent of smoothness.

## Weaknesses

### Major

- **Figure 4's scaling-law comparison is budget-asymmetric.** The x-axis is the number of training collocation points \(m\), but SCaSML uses \(m\) training points *plus* \(m\) inference-time MLP samples (total \(2m\)), while the GP surrogate uses only \(m\) points. The steeper slope for SCaSML reflects this larger total budget, not purely a better convergence rate per unit compute. The paper's theoretical discussion (Section 2.4) correctly states the total budget is \(2m\), and Appendix G.7 reportedly provides fixed-budget comparisons — but the main figure that visually anchors the headline claim lacks this context, making it misleading as presented. A plot with total computational cost on the x-axis, or a clear explanation that the x-axis is only the training portion of a \(2m\) budget, is needed.

- **Asymmetric clipping thresholds across methods (VB-PINN, LQG, DR).** In three of the four problem settings, the naive MLP solver uses a different (larger) clipping threshold than SCaSML: VB-PINN (MLP: 1.0, SCaSML: 0.01), LQG (MLP: 10, SCaSML: 0.1), DR (MLP: 10, SCaSML: 0.01). The paper justifies this by noting the defect is smaller in magnitude, which is reasonable since the SCaSML correction operates on a residual that should be small. However, no sensitivity study is provided to show that the relative advantage is robust to threshold choice. (Note: for the LCD problem, the same threshold \(0.5(d+1)\) is used for both methods — the harsh critic's claim of 0.01 for LCD is incorrect.)

- **Large computational overhead not convincingly justified.** SCaSML is 10–40× slower than the base surrogate in wall-clock time (Table 1). The error reduction (20–80%) is real, but the paper does not clearly articulate when this trade-off is worthwhile for practitioners. The claimed "elastic compute" paradigm suggests one could stop early when sufficient accuracy is reached, but no cost-benefit analysis or accuracy-vs-runtime Pareto plot is provided in the main text.

### Minor

- **The "smaller PINN outperforming larger PINN" elastic compute claim is asserted but not directly demonstrated.** The introduction claims that "a smaller base PINN can outperform a larger PINN under the same inference-time compute budget." This specific comparison — training a small surrogate + SCaSML vs. a larger surrogate alone under equal total budget — is not shown in the main text experiments. Figure 3b shows inference-time scaling for a *fixed* surrogate, which is necessary but not sufficient to support this stronger claim. The appendix may contain relevant experiments, but the main text claims this as a contribution without providing the evidence.

- **All MLP experiments use only \(n=2\) levels and \(M=10\) base samples.** The convergence theory would benefit from showing how deeper MLP hierarchies or larger sample budgets affect the error, especially since the total computational cost grows with \(M^l\) per level. An ablation on the number of levels and the base sample size would strengthen the empirical validation.

- **Gradient accuracy not reported.** The method also corrects \(\sigma^\top \nabla u\), but only errors on \(u\) itself are reported. For applications like hedging in finance or optimal control, the gradient is the primary quantity of interest.

### Trivial

- The notation "SCa\(^2\)SM\(^1\)" is inconsistent with the paper's own abbreviation "SCaSML" and is confusing.

## Nice-to-Haves

- A direct comparison against a simple control-variate Monte Carlo estimator (using the surrogate prediction as a control variate for the Feynman–Kac representation of the *original* PDE) would crisply demonstrate whether the full MLP machinery is necessary or whether simpler variance reduction suffices. The paper already notes it *is* using the surrogate as a control variate, but a simpler (non-MLP) version of this idea is a natural baseline that would sharpen the contribution.

- A clipping threshold sensitivity study for at least one PDE would help assure the reader that the relative advantage of SCaSML over naive MLP is robust.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"No control variate baseline" (Harsh Critic #2, Strengthening #2):** Removed because the paper explicitly states in the conclusion that "our framework uses the machine learning model as a control variate in stochastic simulations." The method *is* a control variate approach; asking for a separate "control variate baseline" misunderstands the method. The nice-to-have above suggests a simpler version as a baseline, which would strengthen the paper but is not a missing comparison.

- **"LCD clipping threshold of 0.01" (Harsh Critic #3):** Factually wrong. The paper states for LCD: "A clipping threshold of 0.5(d+1) is applied to the solution and gradients for *both* the naive MLP and SCaSML" (emphasis added). The same threshold is used for both methods on this problem.

- **"Naive MLP on LQG should give reasonable O(1/√N) error" (Harsh Critic, Numerical Results):** The naive MLP with \(n=2\) levels, \(M=10\) base samples, and clipping threshold 10 applied to a strongly nonlinear problem with a quadratic nonlinearity \(-\|\nabla u\|^2\) in 100–160 dimensions can easily fail catastrophically. This is not suspicious — poorly tuned MLP can diverge. The paper's contrast between naive MLP failure and SCaSML success is legitimate.

- **Criticism about the scaling law plot being a "fundamental flaw" (Harsh Critic #1):** Downgraded from Fatal to Major. While the budget-asymmetric x-axis is a real issue, the paper's theoretical section (2.4) explicitly accounts for the total budget of \(2m\), and Appendix G.7 is referenced for fixed-budget comparisons. The criticism is valid but does not invalidate the paper's core contribution — it is a presentation issue that can be fixed.

- **"No elastic-compute experiment" (Harsh Critic #4):** The general elastic compute concept (trading inference compute for accuracy) *is* demonstrated in Figure 3b. The specific claim about "smaller PINN beats larger PINN" is the part not directly shown, which is noted as a minor weakness above. The broader criticism overstated the problem.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fix Figure 4.** Replot with total computational cost (training + inference) on the x-axis, or at minimum add a dashed curve showing a budget-matched comparison. The caption should clearly state what the x-axis represents and how the total budgets compare.

2. **Add a clipping sensitivity study.** For at least one PDE (e.g., VB-PINN or LQG), run both SCaSML and naive MLP with a range of clipping thresholds and plot the resulting relative \(L^2\) errors. This would demonstrate robustness of the relative advantage.

3. **Add a small-vs-large surrogate experiment.** Directly test the "elastic compute" claim: train surrogates of increasing size/cost, then take the smallest surrogate + SCaSML with varying inference budgets and plot error vs total cost alongside the stand-alone larger surrogates. This would either validate or refute the headline claim.

4. **Report gradient errors.** Since the method also corrects \(\sigma^\top \nabla u\), showing gradient accuracy would significantly strengthen the practical relevance.

5. **Provide a cost-benefit analysis.** The 10–40× wall-clock increase over the surrogate alone needs context — e.g., a Pareto frontier of error vs. runtime, or a discussion of when the accuracy improvement justifies the cost (e.g., safety-critical applications, or when running a single high-precision query).

## Score and Decision

I bracket this paper relative to the calibration anchors:

**Round 1 — Bracketing.** Three queries returned anchors from three bands:
- Weak band (<3.5): PINN variants scoring 2.5–3.33 (e.g., "Hybrid Numerical PINNs" at 3.33, "Characteristic based NN" at 2.50)
- Middle band (3.5–7.5): Hybrid/defect-correction PDE papers scoring 4.0–6.8 (e.g., "Automatic Neural Spatial Integration" at 4.00, "Model-Agnostic Knowledge Guided Correction" at 5.00, "Flexible Active Learning of PDE Trajectories" at 6.80, "Progressively Refined Differentiable Physics" at 6.50)
- Strong band (>7.5): Top papers scoring 7.6–8.0

The paper clearly sits in the middle band: it is substantially stronger than the weak PINN variants (which lack theoretical contributions and work only on low-dimensional or 1D problems), but not as cleanly executed as the top-tier papers.

**Round 1 bracket:** [5.0, 6.5]

**Round 2 — Narrowing.** Two queries within (4.5, 6.5) and (5.5, 7.5) returned anchors including:
- "Model-Agnostic Knowledge Guided Correction" (avg 5.00): Similar hybrid surrogate+simulator idea but with a weaker theoretical component and only 2D Navier-Stokes experiments. The present paper has stronger theory and higher-dimensional experiments → **this paper is stronger**.
- "Metamizer" (avg 5.25): Neural optimizer for physics simulations, no theoretical convergence guarantees similar to this paper.
- "Learning a Neural Solver" (avg 5.60): Learned preconditioner for PINNs with mixed reviews (scores 3,6,8,8,3). Similar in having a theoretical claim that is not fully proven. Comparable paper quality.
- "Progressively Refined Differentiable Physics" (avg 6.50): Clean experiments on differentiable physics, though limited to 1D/2D problems and iterative linear solvers. The present paper tackles much higher dimensions (160d) and has a novel theoretical product bound, but has presentation weaknesses that PRDP doesn't.
- "Flexible Active Learning" (avg 6.80): Clean active learning framework for PDE surrogates, comprehensive experiments but lower-dimensional, no theoretical convergence guarantees.

The present paper is better than the 5.00–5.25 anchors (stronger theory, higher dimensions) but not as cleanly executed as the 6.50–6.80 anchors (budget-asymmetric Figure 4, asymmetric clipping, practical overhead unaddressed). A score of **5.5** best reflects this positioning.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>