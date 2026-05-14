Now I have a thorough understanding of the paper, the reviews, and the calibration anchors. Let me write the consolidated review.

## Summary

The paper analyzes gradient descent through a second-order ODE lens (differentiating gradient flow to get d²θ/dt² = -H(θ)·dθ/dt), characterizes its stability across curvature regimes, and proposes a controller u = -K₁θ - K₂(dθ/dt) that would make the continuous-time second-order system locally asymptotically stable. From this controller, the authors derive a discrete algorithm called Controlled Gradient Descent (CGD) that adds -K₁θ² - K₂θ to the gradient.

## Strengths

- **Clear motivation and framing**: The paper correctly identifies that the stability of GD depends on Hessian eigenvalues and that continuous-time control theory provides a useful language for thinking about stabilization. The basic intuition of adding damping (velocity-dependent feedback) is well-motivated from mechanical systems.

- **The continuous-time controller analysis (Theorem 3) is mathematically valid**: For the second-order ODE d²θ/dt² = -(H+K₂)·dθ/dt - K₁θ, applying Lemma 4 from Tisseur & Meerbergen (2001) correctly shows that if I ≻ 0, H+K₂ ≻ 0, and K₁ ≻ 0, then all eigenvalues have negative real parts, making the controlled second-order system locally asymptotically stable.

- **Clean presentation of the second-order ODE reformulation**: The derivation from gradient flow (Eq. 1) to the second-order ODE (Eq. 2) via time-differentiation is clearly presented, and the eigenvalue analysis of the augmented Jacobian (Section 4) is competently executed for what it analyzes.

## Weaknesses

### Fatal

1. **The discrete algorithm does NOT follow from the continuous-time controller (derivation in Equation 5 is mathematically invalid).** 
   The paper claims that integrating the controlled acceleration gives a gradient update modified by -½K₁θ² - K₂θ. Specifically, the paper attempts ∫(-K₁θ) dt and claims the result is -½K₁θ². This is mathematically wrong: ∫θ dt ≠ θ²/2. The chain rule gives d(θ²)/dt = 2θ·(dθ/dt), so ∫θ dt = ∫θ(t) dt, which has no closed-form expression in terms of θ alone without solving the ODE. The paper confuses integration with respect to time (dt) with integration with respect to θ (dθ). No valid algebraic path connects the controlled second-order ODE (u = -K₁θ - K₂·dθ/dt) to Algorithm 1's update (which uses -K₁θ² - K₂θ). The algorithm is therefore **not derived from the theory**, and the claimed theoretical grounding of CGD is unsupported. This single issue invalidates the paper's central claim.

2. **The stability analysis is performed on a system that is not equivalent to gradient descent.**
   The paper augments the state to (θ, dθ/dt) and analyzes a second-order ODE derived from gradient flow. The Jacobian of this augmented system has n spurious zero eigenvalues that are artifacts of the non-minimal representation. The paper then claims GD is "only Lyapunov stable" for strongly convex functions (Table 1, Theorem 2), but standard gradient flow for a strongly convex function is *asymptotically* stable — the n zero eigenvalues are an artifact of the formulation, not a property of GD. The classification in Theorem 2 (Table 1) applies to the second-order ODE, not to gradient descent, and this gap is unacknowledged.

### Major

3. **The controller shifts the equilibrium and does not preserve the original minimizer.**
   The controlled continuous-time system d²θ/dt² = -(H+K₂)·dθ/dt - K₁θ has its unique equilibrium at θ = 0 (assuming K₁ ≻ 0). For any problem where the minimizer is not at the origin — i.e., L(θ) = (θ-c)² — the controller drives parameters toward zero rather than toward the true minimum. The synthetic experiments all place the minimizer at (0,0), concealing this bias. The discrete algorithm (Algorithm 1) has the same problem: it modifies the gradient by subtracting K₁θ² + K₂θ, so at equilibrium we require ∇L(θ) = K₁θ² + K₂θ, which generally does not hold at the true minimizer. The paper provides no analysis of how the controller affects the location of stationary points and no mechanism to correct this bias.

4. **The experimental evaluation is insufficient to support the claims.**
   - Only three 2D toy problems are tested (two quadratics, one quartic), all with minimizers at the origin.
   - **Factual error**: The "convex but not strongly convex sphere" L(θ) = θ₁² + θ₂² has Hessian 2I, which is *positive definite* (λ_min = 2 > 0), meaning it is *strongly convex*. The paper misclassifies it.
   - No comparison to any baseline optimization method (momentum, Nesterov acceleration, Adam, Polyak stepsize, or even simple line search). This makes it impossible to assess whether CGD offers any practical advantage over existing approaches rather than just being a different (potentially inferior) heuristic.
   - No error bars, multiple seeds, or statistical quantification are reported.
   - The ablation on K₁=K₂ only varies both simultaneously, making it impossible to isolate the individual effects of each controller gain.

### Minor

5. **The claim about higher learning rate tolerance is not quantitatively characterized.**
   The paper states CGD "increases the 2/sharpness threshold" but provides no quantitative measurement of how much improvement is achieved. The demonstration on a single quadratic problem (sharpness=2, η around 1.0) merely reproduces known EoS behavior, and the improvement could be entirely due to added damping, with no ablation to isolate this from the origin-bias introduced by the K₁θ² term.

6. **Factual claim about prior work is overstated.**
   The Introduction states "no theoretically characterized algorithm exists that guarantees stabilized convergence of GD in general setting." This ignores the large body of work on adaptive methods, Polyak stepsizes, normalized GD, and the well-known stability condition η < 2/λ_max. The paper also ignores decades of control-theoretic optimization (e.g., PID controllers for gradient methods).

### Trivial

7. **The paper uses "-K₁θ²" (element-wise square)** in Algorithm 1, but the continuous-time controller uses "-K₁θ" (not squared). This inconsistency between the theory and the implementation is never explained. If the algorithm truly intends to use θ², this should be derived (or at minimum justified) separately.

## Nice-to-Haves

- Testing on objectives where the minimizer is not at the origin, to verify whether CGD converges to the correct point or whether the equilibrium bias is a real problem.
- Comparing against standard baselines (momentum, Nesterov, Adam) on the same toy problems.
- A discrete-time stability analysis of Algorithm 1 (e.g., on a scalar quadratic), to verify whether the algorithm actually converges under the claimed conditions rather than relying on continuous-time analysis of a different system.
- Providing a principled way to choose K₁ and K₂ (e.g., adaptive to Hessian spectral information) rather than fixed constants.

## Removed Points

*These points are flagged to be removed — treat them with caution.*

- **Strength (from Strength Finder): "Novel control-theoretic formulation for stabilizing GD"** — Removed because it conflicts with Verified Weakness #1 (the algorithm does not follow from the formulation) and #2 (the analysis is on the wrong system). The formulation may be novel in concept, but the verification confirms the execution is invalid, so this strength cannot be sustained.

- **Strength: "Rigorous characterization of instability across curvature regimes"** — Removed because it conflicts with Verified Weakness #4 (the paper misclassifies L=θ₁²+θ₂² as "convex but not strongly convex" when it is strongly convex) and Weakness #2 (the analysis is of the augmented second-order system, not GD). The characterization is neither rigorous nor correctly scoped.

- **Strength: "Theoretical guarantee of asymptotic stability via eigenvalue shifting"** — Moved to Removed Points because while Theorem 3 is technically valid for the continuous-time second-order system, it conflicts with Verified Weakness #1 (the algorithm does not implement this controller, so the guarantee does not transfer to the actual method). Since a strength and a verified weakness disagree, the weakness wins.

- **Strength: "Explicit algorithmic instantiation"** — Removed. The algorithm exists but its derivation from the theory is invalid (Weakness #1), so presenting the algorithm as a strength that "bridges theory and application" is misleading when the bridge is broken.

- **Harsh critic's claim that "the paper provides no analysis of the discrete system's dynamics"** — Kept as Minor weakness but downgraded from "Structural" since the Limitations section does acknowledge the discretization gap (lines 1141-1149).

- **Harsh critic's claim that "the paper incorrectly interprets this as meaning GD is only Lyapunov stable"** — Kept and elevated to Fatal (Weakness #2) since it's a genuine issue about the object of analysis.

- **Harsh critic's claim about Lemma 4 applicability** — Removed. The paper states K₂ ≻ -H(θ) (Remark 2), ensuring H+K₂ ≻ 0, and M=I≻0, K₁≻0 by definition. So Lemma 4's conditions are satisfied. The reviewer's objection about symmetry is unnecessary since the QEP result holds for the specific structure used.

- **Harsh critic's claim about "missing related works"** — Removed per instructions ("DO NOT mention missing related works, as you do not have external sources to confirm their existence").

## Novel Insights

None beyond the paper's own contributions. The reviews surface no genuinely novel observation that the paper's authors themselves did not already recognize (at least at the conceptual level). The core issues identified — the invalid algorithm derivation, the mismatched system of analysis, and the equilibrium bias — are structural problems with the paper's execution, not new insights about optimization.

## Suggestions

The paper cannot be fixed with minor revisions. The derivation from continuous-time controller to discrete algorithm (Equation 5) is mathematically invalid and must be completely reworked. Additionally, the stability analysis claims need to be scoped to the system actually being analyzed (the second-order ODE), with clear acknowledgment that this system is not equivalent to gradient descent. The equilibrium bias of the proposed modification must be analyzed and corrected, and the experiments need to be substantially expanded (non-origin minimizers, baselines, higher dimensions, error bars). Given the fundamental nature of these issues, the authors should consider whether the continuous-time control theory can be rigorously connected to a discrete algorithm before attempting another submission.

## Score and Decision

**Calibration anchors used** (all papers from ICLR 2026 human review corpus):

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `b36drMoKir` (Gradient Flow Convergence Guarantee) | 0.50 | Incorrect proof — similar fatal error to this paper (invalid derivation), but that paper's errors were in the proof itself while this paper's error is in the algorithm derivation. Both fundamentally unsupported. |
| `WgMZPsdJmC` (Cauchy Method Steplength) | 0.50 | Extremely narrow scope (2D quadratics), poor presentation. This paper has slightly more substance but a comparable fatal flaw. |
| `hBNC8w9pd7` (Stability of Nonlinear Dynamics GD/SGD) | 4.00 | Correct analysis with limited novelty. This paper is substantially weaker — it has a fatal mathematical error that hBNC8w9pd7 does not. |
| `3U6wH7uAPZ` (Convergence Direction of GD) | 4.80 | Clean theoretical result, limited practical scope. The current paper's theoretical grounding is unsound by comparison. |
| `zbHlT1aRJM` (Exponential Objective Decrease) | 4.50 | Sound incremental analysis under (L0,L1)-smoothness. Technically correct but limited novelty. Current paper has fatal errors. |
| `yRtgZ1K8hO` (Polar Express) | 8.00 | Novel method with strong theory and validation. Incomparable quality level — rigorous and sound throughout. |
| `hBNC8w9pd7` | 4.00 | See above. |

Relative to these anchors, the paper falls between the 0.50 papers (fundamentally flawed contributions) and the ~4.00 papers (correct but limited). The fatal mathematical error in the algorithm derivation places it clearly below any paper whose theoretical claims are valid. The paper has more substance than the worst anchors but is fundamentally unsound in its central claim, placing it in the 1.0–2.0 range.

MY FINAL SCORE: <pineapple>1.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>