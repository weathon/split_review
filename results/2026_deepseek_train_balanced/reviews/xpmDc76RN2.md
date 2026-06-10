## Summary

This paper applies Restricted Strong Convexity (RSC) theory to analyze gradient descent optimization of operator networks (ULGNET, FEONet) trained with variational loss for solving elliptic PDEs. The main theoretical result (Theorem 3.4) derives a convergence rate depending on \((\kappa(A))^{-2}\), where \(A\) is the discretization matrix from the variational formulation, providing a theoretical basis for preconditioning benefits. The paper also establishes a formal connection between RSC quantities and the Neural Tangent Kernel (Theorem 3.5), and proposes an adaptive weight algorithm intended to prevent a key quantity (\(q_t\)) from vanishing during training.

## Strengths

- **Explicit derivation of condition number's effect on convergence rate**: Theorem 3.4 and the resulting expression for \(r_t\) (lines 210–212) show that the optimization convergence rate depends on \((\kappa(A))^{-2}\), providing a precise mathematical mechanism linking preconditioning to faster training. This extends prior observations about condition number affecting generalization and approximation errors (Hong et al., 2024) to optimization error, demonstrating all three error types benefit simultaneously.

- **Formal connection between RSC and NTK frameworks**: Theorem 3.5 (lines 238–257) derives explicit bounds on \(q_t\) in terms of NTK eigenvalues: \(\lambda_{\min}(K)^2/\lambda_{\max}(K) \leq q_t \leq \lambda_{\max}(K)^2/\lambda_{\min}(K)\). This bridges two previously separate theoretical frameworks for analyzing optimization in operator learning and provides a practical sufficient condition connecting network width to convergence guarantees.

- **Clear identification of why variational-loss operator networks are amenable to RSC analysis**: Section 2.2 (lines 90–113) correctly notes that because basis functions handle boundary conditions and the loss involves no network derivatives with respect to input variables, the unsupervised PDE problem reduces to a supervised least-squares form. This structural insight is non-trivial and justifies why RSC theory (typically applied to supervised settings) can be brought to bear on this problem class.

## Weaknesses

### Major

- **The core theoretical result is an application, not a development, of existing RSC theory**. The paper explicitly follows Banerjee et al. (2022) (line 134), and the loss \(\mathcal{L}^M(\theta) = \frac{|\Omega|}{M}\sum_j \|A\hat{\alpha}(\omega_j) - g_j\|_2^2\) (Equation 7) is structurally a standard supervised least-squares problem with an additional matrix \(A\) in the quadratic form. The resulting appearance of \(\kappa(A)\) in the convergence rate is a straightforward algebraic consequence of this structure. The paper does not argue that existing RSC theory fails for this loss class — it applies it. The claim of providing "an alternative convergence theory to the commonly used NTK-based approaches" (line 121) is accurate but overstated: the RSC framework inherits similar locality assumptions (parameters must stay in \(B_{\rho,\rho_1}^{\text{Spec}}(\theta_0)\)) to those the paper criticizes in NTK (line 20), a tension the paper never acknowledges or resolves.

- **The adaptive weight algorithm lacks a convergence guarantee for the modified loss**. Theorem 3.4 applies to the original loss \(\mathcal{L}^M\), not the adaptively weighted loss \(\tilde{\mathcal{L}}_t^M\). Whether gradient descent on the modified loss satisfies RSC or converges is never established. The algorithm's theoretical justification (lines 291–313) relies on an unverified assumption that \(\tilde{r}_0 \notin N(\nabla_\theta \alpha(\theta_t))\) for most \(t\), with the constant \(c_0\) defined via a minimum over \(t \geq 0\) (line 304) whose positivity is not proved. The derivation then jumps to a lower bound on \(q_t\) without showing how the algorithm ensures this bound is maintained. Without a convergence theorem, the algorithm is a heuristic with theoretical motivation but no theoretical guarantee — undermining the paper's framing as primarily a theoretical contribution.

- **The empirical evaluation is far too thin to validate the theory or the algorithm**. The experiments test only one PDE (1D Helmholtz equation) with one architecture (ULGNet). There are: (i) no proper baseline comparisons (no Adam, SGD, or other operator learning methods like DeepONet, FNO, PINO); (ii) no ablation isolating the adaptive weight algorithm without preconditioning, so its independent contribution cannot be assessed; (iii) no measurement of \(q_t\) trajectories during training, which would be the most direct validation of the algorithm's claimed mechanism; (iv) no error bars, confidence intervals, or standard deviations reported; (v) no training details disclosed (network depth/width, learning rate schedule, batch size, \(M\), \(N\)); (vi) the preconditioning methods ("Type 1" and "Type 2") are never defined. Results are described qualitatively ("Trial E attained the lowest relative \(L^2\) error") without reporting actual numerical values.

- **The adaptive weight algorithm's specification has confusing notation and an unclarified computational concern**. The text introduces \(\Lambda_t\), \(\Lambda_{i,t}\), \(\lambda_{ij,t}\), \(\mathbf{A}_t\), \(\mathbb{A}\), and \(\bar{\mathbf{A}}\) without consistent definitions (lines 279–289). The weight matrix \(\Lambda_{i,t}\) is defined as \(\operatorname{Diag}(\lambda_{i1,t},\dots,\lambda_{iN,t})(A^\top)^{-1}\), requiring the inverse of \(A^\top\). If computed per-iteration this is \(O(N^3)\); if precomputed once (which is feasible since \(A\) is fixed), the paper should state this clearly. The claim of "no extra computational costs" (line 7) requires clarification.

### Minor

- **The PDE in the preliminaries contradicts the "self-adjoint" claim**. The paper states it considers "self-adjoint second ordered Elliptic PDEs" (line 58) but then writes \(-\text{div}(a(x)\nabla u) + b(x)\cdot\nabla u + c(x)u = g\) (line 60). The convection term \(b(x)\cdot\nabla u\) breaks self-adjointness unless specific conditions hold, which are not discussed. This is a technical error in the problem setup.

- **The RSC framework's locality assumption is in tension with the paper's own criticism of NTK**. The paper faults NTK theory for requiring models to be "confined to the near-initialization regime" (line 20), yet Theorem 3.4 requires \(\theta_{t+1} \in B_{\rho,\rho_1}^{\text{Spec}}(\theta_0)\) (Assumption A1). The paper does not discuss whether this assumption is satisfied in practice or whether it is a lesser or greater restriction than NTK's requirements.

- **No comparison of when RSC provides tighter bounds than NTK, or vice versa**. Theorem 3.5 connects the two frameworks but the paper does not analyze which approach yields more informative guarantees for operator networks, missing an opportunity to differentiate its contribution.

- **The claim that \(m = \Omega((NM)^2)\) ensures positivity of \(q_t\) (line 260) is stated without derivation**. The provenance of this specific scaling from the stated eigenvalue bounds is unclear.

### Trivial

- None.

## Nice-to-Haves

- Plotting \(q_t\) trajectories with and without the adaptive weight algorithm would provide the most direct evidence for its claimed mechanism.
- Adding error bars, reporting numerical L² error values, and testing on at least one additional PDE (e.g., 2D or a different elliptic problem) would substantially strengthen the experimental section.
- A convergence theorem for the adaptively weighted loss, or at minimum a proof that the adaptive weights maintain the RSC property, would complete the theoretical contribution.

## Removed Points

These points are flagged to be removed; treat them with caution:

- Criticisms about the algorithm not being textually visible (image placeholder at line 283), garbled text ("aalsg loornitgh ams"), unresolved cross-references ("Section ??"), truncated references ("Choi et al.4"), and missing proof bodies ("Proof.1/2/3") — these are all PDF-parser artifacts; the original submission contains proper figures, proofs, and cross-references.
- Critic's claim that computing \((A^\top)^{-1}\) is an \(O(N^3)\) per-iteration cost — \(A\) is a fixed matrix derived from the PDE and basis functions, so the inverse can be precomputed once. The criticism as stated may be factually incorrect about per-iteration cost, though the paper should clarify this.
- Critic's claim that Table 1 contains "no numerical results readable" — the table is an image due to parser stripping; the original PDF has numerical values. However, the absence of standard deviations, confidence intervals, and numerical reporting in the text are real weaknesses retained above.
- Strength Finder's generic/superficial strengths (e.g., uncritical praise not anchored to specific evidence) — removed for lacking concrete content.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Provide a convergence theorem for the adaptive weight algorithm on the modified loss, or reframe it as a heuristic with empirical justification (and provide that empirical justification).
2. Strengthen experiments substantially: test on at least 2–3 PDEs including a 2D problem, report numerical L² errors with standard deviations across multiple random seeds, measure \(q_t\) trajectories, include standard optimizers (Adam) as baselines, and clearly define the preconditioning types.
3. Acknowledge and address the tension between the RSC locality assumption (A1) and the paper's criticism of NTK's near-initialization requirement.
4. Fix the self-adjoint claim (either remove it or restrict the PDE class appropriately) and simplify the notation in Section 4.
5. Report all training details (network architecture, hyperparameters, dataset sizes) to enable reproducibility.

## Score and Decision

The paper identifies a worthwhile problem and makes several genuine contributions: it recognizes operator networks with variational loss as a class amenable to RSC analysis, derives explicit condition-number dependence in the convergence rate, and formally connects RSC to NTK. However, the theoretical contribution is largely an application of existing RSC theory (Banerjee et al., 2022) to a structurally similar loss without new theoretical machinery, the adaptive weight algorithm lacks convergence guarantees for the modified loss, and the experimental evaluation is far too thin to validate either the theoretical assumptions or the algorithm's effectiveness. The gap between what is claimed and what is delivered is too wide for acceptance at a top venue in its current form.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>