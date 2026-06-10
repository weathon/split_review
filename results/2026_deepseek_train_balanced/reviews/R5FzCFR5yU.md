## Summary

This paper identifies three scenarios where automatic differentiation (AD) fails to compute correct spatial derivatives in physics-informed neural networks (PINNs): non-analytic PDE coefficients, strong imposition of Dirichlet boundary conditions, and enriched inputs external to the computational graph. It proposes a hybrid framework that replaces AD with numerical differentiation operators (specifically finite-element gradient kernels) for spatial gradient computation. The method is validated on a 1D diffusion equation and a 2D linear elasticity problem on a complex geometry (Olympic rings), demonstrating accuracy and speed advantages over AD-based baselines.

## Strengths

- **Significant speedup for deep networks with model-independent gradient cost.** Figure 5 shows ~180× forward-pass and ~150× backward-pass speedup for a 20-layer network, because the numerical operator's cost depends only on mesh size, not model complexity. This is a concrete, measured advantage over AD for deep architectures.

- **Gradient operator extraction is more general than prior hybrid FE-PINN formulations.** As noted in Section 4 (line 44), prior work (Meethal et al., 2023; Eshaghi et al., 2024) embeds the full FE formulation as a problem-specific loss term, whereas the proposed method extracts only the gradient operator (geometry- and mesh-dependent), making it reusable across different PDEs and boundary conditions on the same domain.

- **Direct empirical demonstration of AD failure for tabulated coefficients.** Figure 3 (Section 5.2) shows that when the diffusion coefficient α is tabulated (not in the computational graph), the plain PINN converges to an incorrect linear solution while the hybrid approach converges to the correct analytical solution, validating the motivation in Section 3.1.

- **Clean controlled experiment confirming the enriched-input failure mechanism.** Figure 2 (Section 5.1) demonstrates that AD computes incorrect spatial derivatives when an externally-computed field φ(x) = sin(10πx) is an input, while numerical differentiation methods match the corrected derivative.

## Weaknesses

### Major

- **The paper overclaims "Theorem 3.2" as a substantive theoretical contribution.** Assumption 3.1 states that φ(x) is computed outside the deep learning framework, so its dependency on x is not in the computational graph. Theorem 3.2 then concludes that AD will not compute the physical spatial derivative — an immediate consequence of how AD works, not a result requiring proof or providing insight. The framing as a "formal proof" inflates what is essentially a definitional observation. The paper would be better served by stating this plainly rather than presenting it as a theorem.

- **The 2D elasticity comparison confounds multiple factors, making the error gap uninterpretable as a measure of gradient method superiority.** The hybrid approach operates on mesh nodes (5104 points) with a FEM gradient operator. The AD baselines' discretization (same mesh nodes? random collocation points?) is not specified. The reported errors of 94% (weak BC) and 19300% (strong BC) for AD PINNs on a simple linear elasticity problem indicate training collapse rather than merely poor gradient computation — likely because the characteristic function's discontinuity is mishandled and hyperparameters were not optimized for the AD baselines. The comparison conflates at least three changes: (a) numerical vs. automatic differentiation, (b) mesh-based vs. point-based discretization, and (c) strong vs. weak BC handling. A controlled ablation where only the gradient computation method varies is needed to attribute the improvement.

- **Claimed generality is not demonstrated by the experiments.** The paper tests only two PDEs: a 1D static diffusion equation and a 2D static linear elasticity problem — both linear, time-independent, with smooth solutions. The abstract claims the approach is "flexible and can be incorporated into any physics-informed model," yet no evidence is provided for time-dependent problems, nonlinear PDEs (e.g., Navier-Stokes), non-smooth solutions, or problems requiring higher-order derivatives. The method's reliance on a mesh and P1 FEM basis also raises questions about irregular geometries and adaptive meshing that are not discussed.

- **The enriched-inputs scenario (Section 3.3), one of the paper's three key motivations, is not experimentally validated.** The synthetic demonstration in Section 5.1 uses a known differentiable φ(x) = sin(10πx) where manual correction is possible. The paper acknowledges this limitation ("while a correction... is possible in this case, this should not be true in general") but provides no experiment where φ is truly non-analytic and the hybrid method succeeds where AD cannot be corrected.

### Minor

- **The diagnosis of AD failure for strong BC imposition is imprecise.** The paper attributes the failure to the characteristic function being "outside the computational graph" (line 78-84). However, the more fundamental issue is that the characteristic function is discontinuous — even if it were in the graph, AD would produce a Dirac delta at the boundary. The paper conflates two separate issues (graph exclusion vs. discontinuity) and would benefit from a clearer articulation.

- **The 1D tabulated-coefficient experiment uses a weak test case.** The diffusion coefficient α(x) = 0.1 + x is analytic with a trivial derivative α' = 1. A simple linear interpolation would recover this derivative. A genuinely non-analytic coefficient (e.g., piecewise constant, noise-corrupted, or data-derived) would make the practical motivation more compelling.

- **The method description lacks implementation details needed for reproducibility.** The gradient operator formula (Equation 11) omits specifics (quadrature rule, element-level assembly). It is also unclear whether the loss is evaluated at mesh nodes or quadrature points, and how boundary nodes are identified and fixed in the hybrid framework.

### Trivial

- The paper misspells "smooth" as "connex" in Assumption 3.1 (line 94), and "explanation" as "explaination" (line 113).

## Nice-to-Haves

- Acknowledge alternative workarounds for tabulated coefficients (differentiable interpolation, surrogate models) and explain why they are insufficient in the targeted settings.
- Provide a full training-time breakdown (forward pass, backward pass, gradient computation, parameter update) to clarify the source of speedups beyond the sub-component measurement in Figure 5.
- Discuss how mesh quality, coarseness, and refinement affect the accuracy of the numerical gradient operator and consequently the PINN solution.

## Removed Points

These points were flagged for removal (see filtering rules):

1. **"The strong BC novelty claim is misattributed to Lagaris et al."** — Lagaris et al. (1998) uses multiplicative distance functions (smooth), while the paper uses additive masking with a characteristic function (discontinuous). These are mathematically different mechanisms. Removed because the criticism overstates the overlap. The discontinuity issue is retained as a separate Minor weakness.

2. **"Tabulated α can be interpolated with a differentiable basis"** — This is a reasonable alternative approach but constitutes scope creep (the paper's point is about cases where α's functional form is unknown). Demoted to Nice-to-Have; not a core weakness.

3. **"The paper overstates the gap about 'few works address the computation of residuals by AD'"** — The paper's refined claim is that prior works "did not emphasize the theoretical limitations" of AD, which is a fair distinction. Removed as the criticism nitpicks a claim the paper already qualifies.

4. **"Two orders of magnitude speedup refers only to a sub-component"** — The abstract and Figure 5 specifically say "gradient computation," so the paper is precise. Removed; the critic misread. The absence of a full training breakdown is retained as a Minor weakness.

5. **All pure formatting/style nitpicks** — Removed per filtering rules (parser artifacts, not author errors).

6. **Strength Finder #1 (Theorem 3.2 as formal proof)** — Conflicts with the verified weakness that Theorem 3.2 is a trivial consequence. Removed.

## Novel Insights

None beyond the paper's own contributions. The core observation — that AD silently produces incorrect spatial derivatives when PDE coefficients or input fields are outside the computational graph — is useful and underappreciated in the PINN literature. But the reviewers do not surface any genuinely novel insight that the paper itself misses.

## Suggestions

1. **Add a controlled ablation for the 2D elasticity experiment.** Keep everything equal (same discretization points, same architecture, same optimizer, same BC treatment), varying only whether spatial gradients are computed by AD or the numerical operator. This would isolate the effect of the gradient method.

2. **Test a genuinely non-analytic coefficient.** Replace α(x) = 0.1 + x with a coefficient defined only as discrete tabulated values (e.g., from a random field or material database) to make the practical motivation concrete.

3. **Remove the "theorem" framing or restrict it to a plain observation.** Theorem 3.2 contributes no substantive theoretical structure and the overclaim distracts from the paper's real engineering contribution.

4. **Validate the enriched-inputs scenario.** Test a case where a non-analytic field φ (e.g., from tabulated data or an external simulation) is provided as input and the hybrid method succeeds where AD fails.

5. **Report full per-epoch training time breakdowns** (forward pass, gradient computation, backward pass) so readers can evaluate the practical speedup in context.

## Score and Decision

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>