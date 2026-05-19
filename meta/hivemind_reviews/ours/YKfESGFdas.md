## Summary
This paper proposes GeONet, a neural operator framework (based on DeepONet) that learns the Wasserstein geodesic connecting two endpoint probability distributions. The method uses a physics-informed loss derived from the Benamou-Brenier dynamic OT formulation — it jointly trains primal and dual networks that must satisfy the continuity equation and Hamilton-Jacobi equation respectively, along with boundary conditions on the primal density. The key innovation is that training requires only the endpoint distributions (μ₀, μ₁), not ground-truth geodesic data. After offline training, inference is instantaneous (a forward pass) and mesh-invariant, enabling zero-shot super-resolution.

## Strengths
1. **Novel problem formulation: operator learning for Wasserstein geodesic without geodesic training data.** The paper reformulates the Wasserstein geodesic computation as an operator learning problem where the training loss comes from the KKT optimality conditions (coupled PDEs) rather than from supervised geodesic data. This is a genuinely new framing that has not been explored in prior work. The comparison table (Table 1) correctly identifies that GeONet is the only method simultaneously offering operator learning, physics-informed learning, no need for known geodesic data, and mesh-independent output.

2. **Orders-of-magnitude faster inference than traditional OT solvers.** Once trained, GeONet's inference requires only a forward pass. The runtime comparison (Figure 5, Section 4.4) shows that GeONet's inference scales far better than POT on fine grids, achieving speedups of orders of magnitude on a log-log scale. This amortized inference property is valuable for applications requiring many geodesic computations.

3. **Mesh-invariant output enabling zero-shot super-resolution.** Because GeONet learns continuous functions of space and time (not grid-dependent discretizations), it can predict geodesics at higher spatial resolution than the training data without any retraining. Section 4 and Table 2 show that the high-resolution test errors are comparable to in-distribution errors, confirming this capability.

## Weaknesses
### Fatal
None.

### Major

1. **The CFM/RF comparison (Table 3) is not a valid evaluation of geodesic accuracy.** Conditional flow matching and rectified flow are generative models that produce *samples* along a stochastic transport path, not deterministic density fields solving the Wasserstein geodesic. Converting their sample outputs to grid-based densities introduces uncontrolled approximation error. More fundamentally, these methods target a *different* problem (stochastic flow / Schrödinger bridge rather than the deterministic Benamou-Brenier geodesic). The large errors reported for CFM/RF (90–112%) are an artifact of this mismatch and do not provide meaningful evidence that GeONet is superior. This experiment should either be removed or reframed as a qualitative comparison with explicit caveats.

2. **Missing comparisons to relevant neural OT and amortized methods.** The paper cites several directly relevant methods — single-pair neural geodesic solvers (Liu et al. 2021, 2023) and amortized OT map methods (Amos et al. 2023, Lacombe et al. 2023) — but provides no numerical comparison against them. Since the paper's main selling point is amortized inference, quantifying the accuracy/speed trade-off versus single-pair solvers and comparing to other amortized OT approaches is essential to validate the contribution. Without these comparisons, the reader cannot assess whether GeONet's amortization advantage justifies any accuracy loss.

3. **No ablation or sensitivity analysis.** The loss function has four weighting hyperparameters (α₁, α₂, β₀, β₁) whose values are not reported in the main text. The method has several design choices (modified MLP, Fourier features, dual network architecture) whose individual contributions are not ablated. There is no study of how test error scales with the number of training pairs n. This makes it difficult to understand which components are critical and how robust the method is to hyperparameter choices.

### Minor

1. **Validation only against a numerical solver, not against ground truth.** The L¹ error is measured against the output of POT's convolutional Wasserstein barycenter solver, which is itself a discretized, regularized numerical approximation. The paper acknowledges this (caption: "reference serves as a close approximation to the true geodesic") but does not validate against any case with an analytically known geodesic (e.g., single Gaussian distributions, where the geodesic is known in closed form via interpolation of means and covariances in the Bures metric). Such validation would substantially strengthen confidence that the method learns the true geodesic rather than just mimicking the solver.

2. **MNIST experiment is incompletely specified.** The paper does not state how the reference geodesic for MNIST is obtained (presumably by running POT on the 32-d latent representations?). The autoencoder architecture, reconstruction fidelity, and choice of latent dimension are not discussed. The paper honestly notes that "ambient-space error is much larger than the encoded-space error" and that geodesics in latent and ambient space do not coincide, which raises questions about what exactly is being evaluated.

3. **Boundary conditions for the dual variable are not enforced.** The KKT system (Eq. 13) includes BCs for μ only; there are no losses enforcing the known boundary conditions on u (u(x,0) = −φ*(x), u(x,1) = ψ*(x)). While the coupled PDE system may constrain u sufficiently in practice, the theoretical underdetermination is not discussed. An ablation showing whether adding these BCs changes results would clarify the concern.

4. **Runtime comparison uses mismatched accuracy settings.** The POT stopping threshold is 0.5 for 1D and 10.0 for 2D. A threshold of 10.0 in 2D is very loose, and the paper's justification ("even larger thresholds have limited effect on error") is not quantitatively supported. The paper should compare runtimes at matched accuracy levels (e.g., equal L¹ error on a hold-out set).

5. **The ± values in Table 1 are not precisely specified.** The paper reports "±" ranges but does not state whether these are sample standard deviations, standard errors, or confidence intervals, nor the number of test cases.

6. **OOD generalization is limited.** The 1D OOD errors (12–16%) are substantially higher than in-distribution errors. The OOD test only varies variance, not the number of mixture components — a more challenging and meaningful distribution shift.

### Trivial

None.

## Suggestions
1. **Remove or substantially reframe the CFM/RF comparison.** If kept, add explicit caveats that these methods solve a stochastic transport problem rather than the deterministic Wasserstein geodesic, and report their errors in a separate table with appropriate methodology discussion.

2. **Add a ground-truth validation experiment.** Test on single Gaussian pairs (or other cases with known closed-form geodesics) to demonstrate that GeONet actually recovers the true geodesic, not just the POT solver's output.

3. **Add comparisons to the neural OT methods cited in the paper** (Liu et al. 2021/2023, Amos et al. 2023, Lacombe et al. 2023) to contextualize the amortization advantage.

4. **Provide ablations** of the dual network, loss weights, and training set size to demonstrate robustness and justify design choices.

5. **Clarify the MNIST evaluation:** specify how the reference geodesic is computed (latent-space POT?), report autoencoder reconstruction fidelity, and discuss the implications of the latent/ambient geodesic mismatch.

## Score and Decision

The paper presents a genuinely novel and well-motivated approach to a problem of growing importance. The method is clearly described and the core idea (physics-informed operator learning for Wasserstein geodesics without geodesic training data) is creative. However, the experimental evaluation has several significant weaknesses: the CFM/RF comparison is invalid as an accuracy benchmark, essential baselines (single-pair neural geodesic solvers, amortized OT methods) are missing, and there are no ablation studies. These issues do not invalidate the core contribution but prevent the paper from convincingly supporting its claims. A substantially strengthened evaluation could make for a strong paper.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>

## Questions


## Decision
Reject
