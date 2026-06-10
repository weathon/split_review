Here is my consolidated final review.

---

## Summary

This paper proposes a backpropagation-free approach to solving time-dependent PDEs with neural networks by separating space and time: random neural basis functions (ELM or SWIM) are sampled once in the spatial domain, and the PDE is reformulated as an ODE for the time-dependent last-layer coefficients, solved with classical adaptive ODE solvers (RK45, LSODA). Boundary conditions are handled via a linear "boundary-compliant" layer or a penalty-augmented ODE. The method is benchmarked against PINNs, causal PINNs, IGA-FEM, and FEM across a range of challenging PDEs (high advection, long time spans, nonlinear shocks, complex geometries, high dimensions).

## Strengths

- **Benchmarked against classical numerical solvers (IGA-FEM/FEM), not only neural methods.** The paper explicitly departs from the common practice of comparing neural PDE solvers only among themselves. SWIM-ODE with under 500 basis functions achieves three orders of magnitude higher accuracy than FEM with 2000 finite elements on a nonlinear diffusion equation with complicated geometry (Section 4.3, line 180). This provides concrete evidence that the method competes with established numerical techniques.

- **Solves advection over 1000 time units with <0.001% relative L² error in 0.94 seconds.** Section 4.1 (line 161) reports solving the advection equation from t=0 to t=1000 — a regime where full-spatiotemporal neural solvers (PINN, plain ELM, plain SWIM) all fail — with a relative L² error under 0.001% and runtime under one second. This is a direct quantitative demonstration that the separation-of-variables approach overcomes a known and severe limitation of backpropagation-based neural PDE solvers.

- **Works for advection coefficients up to β=10⁴, where PINNs completely fail.** Section 4.1 (line 159) shows that ELM-ODE and SWIM-ODE handle convection coefficients as high as 10⁴, with errors 4–5 orders of magnitude lower than the curriculum learning approach of Krishnapriyan et al. (2021) at β=40, while PINN, plain ELM, and plain SWIM fail. This directly supports the claim that the method captures high-frequency temporal dynamics.

- **SVD layer demonstrably improves conditioning with quantified gains.** Section 3.5 (lines 123–124) introduces a truncated SVD that orthogonalizes the basis functions. The ablation study reports speed improvements of 1.2–77× and ODE system dimension reduction of 1.2–22×, with explicit quantification.

- **Gradient-guided adaptive collocation resampling for shock resolution.** Section 4.4 (line 184) proposes resampling collocation points based on a probability density p(x) ∼ |∇û(x, t_r)|, leveraging the solution gradient to concentrate points near shocks in Burgers' equation. SWIM-ODE is reported as an order of magnitude more accurate, twice as fast as regular PINN, and over ten times faster than causal PINN.

- **Demonstrated scalability to 10-dimensional PDEs.** Section 4.5 (line 191) shows ELM-ODE solving the heat equation in 3, 5, 7, and 10 dimensions. For the 3D case, ELM-ODE is reported as "around 10000 times more accurate and 100 times faster than PINNs," providing evidence for high-dimensional capability.

## Weaknesses

### Fatal
None.

### Major

1. **No explanation for handling second-order time derivatives (Section 4.2).** The paper formulates its framework around first-order-in-time PDEs (Equation 1: u_t + ...). However, Section 4.2 claims to solve a PDE with "fourth- and second-order derivatives in space and time, respectively," which implies a u_tt term. The paper never explains how a second-order time derivative is converted into the first-order form required by the method (e.g., by rewriting as a first-order system). This is a nontrivial step that the paper omits entirely, making the claimed results in this section unverifiable from the methodology presented.

2. **Nonlinear error accumulation mechanism is not analyzed.** For nonlinear PDEs, the ODE in Equation (5) evaluates the nonlinear term N(C(t)[Φ(X), 𝟙]) and projects it back onto the fixed random spatial basis via the pseudo-inverse. The projection error at each ODE step depends on whether the true nonlinear response lies in the span of the random basis. The paper provides no analysis of how these projection errors accumulate over integration time, nor does it present error-vs-time trajectories for the Burgers' equation (the main nonlinear test case). The Burgers' results are deferred to Table 19 in the appendix, and the main text offers only qualitative accuracy claims ("more accurate by order of magnitude"). Without error trajectories and stability analysis, the method's reliability for nonlinear problems over long time horizons is unclear.

### Minor

3. **PINN hyperparameter optimization is not documented with sufficient detail.** The paper states that "the number of basis functions differs for all methods and was chosen to optimize the individual results" (line 193), but provides no evidence of how PINN-specific hyperparameters (learning rate schedule, loss weighting, network depth/width, collocation point distribution, optimizer) were tuned. Given the well-documented sensitivity of PINNs to these choices (Krishnapriyan et al., 2021; Wang et al., 2021), the headline accuracy claims (1–5 orders of magnitude improvement) rest on an incompletely documented comparison.

4. **Boundary penalty parameter κ=100 used without sensitivity analysis.** For non-zero Dirichlet BCs, the paper augments the ODE with a soft penalty (Equation 6) using κ=100 (line 117) but provides no ablation showing how accuracy depends on κ, nor any theoretical justification that the augmented system converges to the correct solution as κ → ∞. This matters because for long-time integration or strongly boundary-condition-driven problems, the soft constraint could introduce systematic error that grows with time.

5. **High-dimensional test case uses a separable solution that maximally favors the method.** The heat equation with sinusoidal initial conditions (Section 4.5) has a solution that is exactly separable in space and time — precisely the functional form of the paper's ansatz û(x,t) = C(t)Φ(x). While this is a reasonable starting point, it is the easiest possible case for the method. A non-separable or dimensionally coupled high-dimensional PDE would provide much stronger evidence for the claimed high-dimensional capability.

6. **Periodic BC construction overlaps with spectral methods and warrants clearer explanation.** Line 107 states that for periodic BCs, "[AΦ]_k(x) = sin(kx) (for k even) and [AΦ]_k(x) = cos(kx) (for k odd)." This construction effectively replaces the random neural basis with fixed trigonometric functions, which is a fundamentally different approach from the ELM/SWIM random-basis paradigm. The paper should clarify: is this a special case where the random basis is discarded, or is there a learned A that maps random Φ to these functions?

### Trivial
- The paper does not report ODE solver statistics (step counts, accepted/rejected steps, stiffness indicators) for any experiment, which would aid in assessing computational cost and reliability.

## Nice-to-Haves
- A computational cost breakdown (basis construction, SVD, pseudo-inverse computation, ODE integration) would clarify scalability to larger M and N_c.
- Error-vs-time trajectory plots for the Burgers' equation would be far more informative than a single aggregate accuracy number.
- A sensitivity study of κ for the boundary penalty method, and ideally a demonstration of exact boundary construction for non-zero Dirichlet conditions.
- Testing on a non-separable high-dimensional PDE (e.g., with coupling between dimensions) would substantially strengthen the high-dimensional claim.

## Removed Points

These points are flagged to be removed; treat them with caution:

- *"Key quantitative evidence is in the appendix"* — The main text reports specific numbers (0.94 seconds, 4–5 orders of magnitude, 10000× more accurate, etc.). Detailed tables in the appendix are standard practice for page-limited submissions; the main text provides sufficient quantitative anchors.
- *"PINN comparison is structurally stacked because the method replaces the difficulty"* — Replacing the difficult optimization with a simpler formulation is exactly the paper's contribution; comparing against PINNs to demonstrate that this substitution works is legitimate. The relevant question is whether the PINN baselines were fairly tuned (covered in Weakness 3), not whether the comparison is conceptually unfair.
- *"ELM/SWIM baseline configuration not explained"* — The paper states these baselines treat time as a spatial dimension and fail at high advection speeds, which directly supports the motivation. Additional tuning details would be nice but are not required.
- *"Parser artifacts in notation"* — These are PDF extraction issues, not author errors. Do not penalize.
- *"Missing related works"* — Cannot be verified without external sources.

## Novel Insights

The most insightful observation emerging from this review is that the paper's separation-of-variables approach — while elegant and practically effective for advection-dominated and diffusion problems — has an inherent tension between its "random basis" framing and the specific mechanisms required for boundary conditions and high-dimensional PDEs. The periodic BC construction (effectively trigonometric functions) and the soft penalty for Dirichlet BCs point to a deeper question: how much of the method's success comes from the random neural basis versus the classical ODE/spectral component? The paper would benefit from a controlled study that isolates the contribution of the random basis sampling (ELM/SWIM) from the boundary-compliant layer and the ODE solver itself. Additionally, the nonlinear error accumulation problem is not unique to this paper — it is a fundamental challenge for any reduced-order or projection-based method — and the paper's failure to address it leaves a gap that limits the method's deployability for nonlinear problems.

## Suggestions
1. Explain explicitly how PDEs with second-order time derivatives (u_tt) are recast into the first-order ODE framework of Equation (5), or restrict the scope of the claim to first-order-in-time PDEs.
2. Add error-vs-time trajectory plots for the Burgers' equation to demonstrate that projection errors do not accumulate catastrophically.
3. Add a sensitivity analysis of the boundary penalty parameter κ across at least one order of magnitude variation.
4. Test the method on a non-separable high-dimensional problem or add a discussion of why the separable case is sufficient as a proof of concept.
5. Provide a table summarizing PINN hyperparameter tuning details (architecture search ranges, learning rate schedules, loss weights tested, selection criteria) to support the fairness of the comparison.

## Score and Decision

MY FINAL SCORE: <score>5</score>
MY FINAL DECISION: <decision>Reject</decision>