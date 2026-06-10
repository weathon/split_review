## Summary

This paper proposes a Characteristic-Based Neural Network (CBNN) for solving 1D hyperbolic conservation laws (specifically Burgers' equation). The method partitions the spacetime domain into subdomains based on characteristic curves, trains separate neural networks on smooth subdomains using a loss derived from the characteristic equation, and tracks shock waves via forward Euler integration of the Rankine–Hugoniot condition. The paper reports L² errors around 2–3×10⁻⁴ on three Burgers' test problems and provides a Lemma bounding the MSE by the loss.

---

## Strengths

- **Independent subdomain training decouples smooth solution approximation from shock tracking (Sections 2.2–2.6).** Each smooth region is handled by a separate network trained on the simple single-term characteristic loss (Eq. 69), while shock positions are computed afterward by solving the Rankine–Hugoniot ODE via forward Euler. This avoids the complex multi-term loss functions and interface constraints required by methods like cPINN and NDNN.

- **Explicit formulas for shock wave interaction and generation (Sections 2.5–2.6).** The paper provides concrete expressions (Eqs. 121–122) for computing the time and position of shock interaction via linear interpolation, and a formula for identifying the shock generation point from the initial condition. These integrate cleanly into the CBNN framework and are demonstrated in the experiments.

- **Lemma 1 establishes MSE ≤ ℒ(θ) (Section 3, lines 146–168).** The paper proves that the mean-squared error of the neural network solution on sample points is bounded above by the characteristic loss — a property that provides a formal link between the training objective and solution accuracy, which is not available in typical PINN formulations.

---

## Weaknesses

### Fatal
None.

### Major

1. **No comparison to any baseline.** The introduction criticizes PINN, cPINN, NDNN, and PINNs-WE for requiring "complex loss functions" or "intricate tuning," yet the paper provides **zero experimental comparisons** to these or any other method. No PINN, no finite-volume, no Godunov, no WENO — not even a direct root-finding baseline that solves the implicit characteristic equation pointwise. Without baselines, the reported L² errors (2.64×10⁻⁴, 3.12×10⁻⁴, 2.28×10⁻⁴) are uninterpretable: classical finite-volume methods on a modest grid would achieve similar accuracy on these same 1D Burgers' problems at negligible cost and with no training phase.

2. **No justification that the neural network adds value over direct root-finding.** For smooth regions, the neural network is trained to satisfy the implicit characteristic equation *u*(*x*,*t*) = *u₀*(*x* − λ(*u*(*x*,*t*))*t*) (Eq. 69). For Burgers' equation (λ(*u*) = *u*) with the simple initial data used, this scalar nonlinear equation can be solved pointwise by Newton's method or bisection without any neural network — yielding the exact solution at any query point. The paper never discusses why a neural network approximation is necessary or beneficial, nor does it compare against a "no-NN" baseline. This undermines the core rationale for the method.

3. **Structural reliance on a priori knowledge of the characteristic decomposition.** The method as described (Sections 2.2–2.6) assumes the user can supply the full spacetime decomposition of the solution — which initial intervals propagate to which regions, where shocks form, and how they interact. The experiments use hand-crafted initial conditions whose exact solution (including shock positions and interaction times) is known analytically. The paper provides no automatic procedure for discovering this structure from an arbitrary initial condition. The shock-generation formula in Section 2.6 is a partial exception, but it is not demonstrated in any experiment and does not address the general case of multiple interacting waves. This sharply limits the method's applicability.

4. **The "theoretical result" does not support the convergence claims made.** Lemma 1 is a near-tautological inequality: MSE(*u_θ*) ≤ ℒ(*θ*) follows from the proof that |*G*(*u_θ*)| ≥ |*u_θ* − *ũ*| under the assumption that *u₀′* and *λ′* are both non-negative (lines 152–153). The proof's claim that this is "without loss of generality" is unjustified — it fails when *u₀′* and *λ′* have opposite signs, which occurs for many valid flux functions. Moreover, the paper references "Theorem 1" (line 170) which is never stated, claims that "error does not accumulate over time" without proof or sketch, and asserts convergence for shock positions without any analysis. The gap between Lemma 1 and a genuine convergence guarantee is substantial.

5. **Absence of all experimental details needed for reproducibility.** The paper does not specify: number of layers, neurons per layer, activation function, optimizer, learning rate, number of training epochs, number of collocation/training points per subdomain, training time, or how the gradient through the implicit loss (which involves *u_θ* inside the argument of *u₀*) is computed. The reported "MSE on sample points" does not clarify whether these are training or held-out test points, and no variance or multi-seed statistics are reported. These results cannot be reproduced or meaningfully evaluated.

6. **Only one equation tested, on three hand-picked problems.** All experiments use Burgers' equation — a single scalar 1D conservation law — with initial conditions chosen so that the exact solution (including shock positions) is known in closed form. No experiments on the Euler equations, traffic flow, Buckley–Leverett, or any other system. No experiment on shock wave *generation* (Section 2.6 describes it but does not demonstrate it). No runtime measurements.

### Minor

- **The rarefaction-wave example (lines 196–208) is presented under the subsection heading "ONE SHOCK WAVE" (Section 4.1).** This is misleading and suggests poor organization.

- **Equation (121) for the shock interaction position *x*** appears to contain an algebraic error.** The formula simplifies to (*s₂*Δ*s₂* − *s₁*Δ*s₁*)/(Δ*s₁* − Δ*s₂*), but standard linear interpolation of two crossing line segments gives (*s₂*Δ*s₁* − *s₁*Δ*s₂*)/(Δ*s₁* − Δ*s₂*). These differ unless the shock speeds are equal. The *t*** formula is correct.

- **References to non-existent sections.** The text repeatedly cites "section 3.1," "3.2," and "3.3" (lines 98, 130, 136, 140) that do not exist in the paper's structure. "Theorem 1" is referenced (line 170) but never defined.

- **Citation formatting error.** "Li et al.Liu et al. (2023)" (line 14) suggests a merged or garbled citation key.

### Trivial
- None beyond the minor issues above.

---

## Nice-to-Haves
- A comparison of training/inference time against a direct root-finding approach would clarify whether the neural network provides any practical advantage.
- Demonstrating the method on at least one additional conservation law (e.g., the Euler equations or a traffic-flow model) would broaden the empirical support.
- A discussion of limitations — particularly the reliance on known characteristic structure — would set appropriate expectations.

---

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"No code or data provided"* — The paper does not cite code, so noting its absence is not a rule violation, but this is a standard reproducibility concern that applies to most anonymous submissions. Downgraded from explicit listing to implied by Weakness 5 (lack of experimental details).
- *Strength: "Lemma 1 … a property not available in standard PINN formulations"* — The strength is factually overstated. PINNs have PDE residual-based loss functions; the comparison is apples-to-oranges because the two loss forms serve different roles. The strength is kept but contextualized in the main list.
- *Strength: "Quantitative accuracy on multiple discontinuity scenarios"* — Retained in summary but the lack of baselines makes the numbers uninterpretable; the main weight is on Weakness 1.

---

## Novel Insights

None beyond the paper's own contributions. The two reviews do not surface any synthesis that goes beyond what the paper states about itself, except to highlight the gap between the paper's claims and its evidence.

---

## Suggestions

1. **Add at least one baseline comparison** — PINN (to validate the criticism in the introduction) and a classical finite-volume/Godunov solver (to contextualize accuracy and cost).
2. **Provide full experimental specifications:** architecture, optimizer, learning rate, number of training points, training time, and variance over multiple seeds.
3. **Acknowledge and discuss the reliance on a priori characteristic decomposition**, and either (a) provide an automatic procedure for computing it from the initial data, or (b) clearly scope the method to problems where this decomposition is known.
4. **Compare against direct root-finding** on the implicit characteristic equation to justify the neural network component.
5. **Fix the section cross-references**, the "Theorem 1" orphan reference, the rarefaction-wave subsection placement, and verify the shock-interaction formula (Eq. 121).
6. **Address the gap in the proof of Lemma 1** — the sign condition on *u₀′* and *λ′* is not "without loss of generality."

---

## Score and Decision

**Score:** 1.5 — The paper proposes a coherent pipeline, but its central design choices are unverified against baselines, unevaluated against simpler alternatives (direct root-finding), and unsupported by sufficient experimental or theoretical evidence. The lack of architectural details makes the results non-reproducible, and the structural assumption of known characteristic decomposition severely limits the claimed generality.

**Decision:** Reject

MY FINAL SCORE: <score>1.5</score>
MY FINAL DECISION: <decision>Reject</decision>