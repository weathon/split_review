## Summary

This paper proposes a control-theoretic approach to stabilizing gradient descent. The authors reformulate gradient flow as a second-order ODE, analyze its stability under different curvature regimes (showing that convex-but-not-strongly-convex losses can produce polynomial divergence via Jordan blocks), and introduce a controller designed to guarantee asymptotic stability regardless of curvature. The controller yields a simple gradient modification (Algorithm 1: CGD), tested on 2D toy problems.

## Strengths

- **Jordan-block analysis reveals a subtle instability mechanism.** Section 4.2.2 shows that when the Hessian is positive semidefinite (convex but not strongly convex), the second-order reformulation's Jacobian has a zero eigenvalue with Jordan blocks larger than 1×1, causing polynomial (not exponential) divergence. This is a mathematically interesting observation that goes beyond the standard eigenvalue-sign check.

- **Theorem 3 applies QEP theory to provide a clean stability guarantee.** The connection to the quadratic eigenvalue problem (Lemma 4 from Tisseur & Meerbergen) is novel for this context and yields a concise asymptotic-stability proof that does not rely on convexity, smoothness, or sharpness assumptions.

- **Algorithm 1 is simple and computationally cheap.** The gradient modification (-K₁θ² - K₂θ) adds negligible overhead to standard GD.

- **Empirical demonstration on toy problems.** The paper shows that CGD converges on small 2D problems where GD diverges, providing some evidence that the idea warrants further investigation.

## Weaknesses

### Fatal
None.

### Major

1. **The derivation from the continuous controller to the discrete algorithm (Equation 5) contains a calculus error.** The paper claims ∫θ(t) dt = ½θ(t)² (element-wise square). This is not correct in general — it would only hold if dθ/dt = 1 component-wise, which is not the setting of gradient descent. This means Algorithm 1 does not follow from the continuous controller as claimed. The theoretical guarantees of Theorem 3 therefore do not directly apply to the discrete algorithm; the connection between the stability analysis and the proposed algorithm is broken.

2. **The controlled system's equilibrium is at θ=0, not the loss minimizer.** For the controlled dynamics (Eq. 4 with Definition 4), setting velocities and accelerations to zero gives -K₁θ = 0, which implies θ = 0 (since K₁ ≻ 0). The paper incorrectly states (line 198) that the equilibrium is [θ*; 0] where θ* minimizes L. Theorem 3's asymptotic stability guarantee is convergence to the origin, not to any meaningful critical point of the loss. This issue is masked because every experiment uses loss functions minimized at θ=0.

### Minor

3. **The test functions in Section 7.1 are mislabeled.** L(θ) = θ₁² + θ₂² has Hessian diag(2,2) ≻ 0 and is therefore strongly convex, not "convex but not strongly convex." The quartic L(θ) = θ₁⁴ + θ₂⁴ has zero Hessian at the minimum and is not strongly convex there. The labeling reversal does not invalidate the experimental results but reflects confusion about the curvature regimes being tested.

4. **The instability analysis applies to the second-order reformulation, not directly to gradient flow.** The original gradient flow dθ/dt = -∇L(θ) at a strongly convex minimum has Jacobian -H(θ*) which is asymptotically stable. The n zero eigenvalues in the paper's 2n-dimensional reformulation are an artifact of the lifting. The paper claims GD can diverge "even when the learning rate satisfies the classical bound" based on this second-order analysis, but the connection between divergence in the reformulated system and divergence in actual GD is not established.

### Trivial

5. The paper lacks comparisons to any existing optimizer (momentum, Adam, Nesterov acceleration, SAM) even on the toy problems, making it hard to assess whether CGD offers practical advantages over known stabilization techniques.

## Nice-to-Haves

- Testing on problems where the minimum is not at the origin (e.g., L(θ) = (θ₁-a)² + (θ₂-b)² with a,b≠0) would reveal the controller's bias and test whether convergence to the true minimum still occurs.
- If the derivation in Equation 5 is acknowledged as heuristic rather than exact, the paper should clearly state that Algorithm 1 is inspired by the continuous analysis rather than derived from it, and discuss what properties are preserved.

## Removed Points

These points are flagged to be removed, treat them with caution:
- The harsh critic's claim that the paper "ignores a large literature on stabilization of optimization (momentum, Adam, Polyak–Łojasiewicz conditions, regularized Newton methods, etc.)" and "does not compare against any existing stabilization method" — this is a valid concern about missing baselines (kept as Trivial weakness 5) but the critic's framing that it's a fatal omission overstates the case for a primarily theoretical paper.
- The critic's claim that "the second-order reformulation creates artificial instabilities that do not exist in actual gradient descent" and that this is "structural" — this is partially valid but the critic overstates it. The paper's analysis is internally consistent for the reformulated system; the problem is that the paper doesn't adequately explain the relevance to actual GD. Kept as Minor weakness 4.
- The critic's claim that the paper's analysis has "no information" about gradient descent because "these zero eigenvalues are an artifact of lifting a first-order system" — this is somewhat true but the paper's analysis could still be meaningful; kept in a weakened form.

## Novel Insights

None beyond the paper's own contributions — the reviewers' comments largely identify issues with the paper's argumentation rather than contributing new perspectives on the optimization problem itself.

## Suggestions

1. Fix the equilibrium issue by redesigning the controller (e.g., u = -K₁(θ - θ̂) - K₂dθ/dt where θ̂ tracks the current iterate with a delay, or simply acknowledge the bias and characterize it).
2. Correct the discrete conversion, or reframe Algorithm 1 as a heuristic inspired by the continuous analysis rather than derived from it.
3. Add comparisons to standard optimizers (momentum, Adam) on the toy problems to contextualize the method's performance.
4. Correct the curvature labels in Section 7.1.
5. Clarify in Section 4 that the instability analysis concerns the second-order reformulation, not gradient flow itself.

## Score and Decision

The paper has two verifiable mathematical errors (the integration step in Equation 5 and the equilibrium misidentification) that directly undermine its core claims about the connection between the continuous-time stability analysis and the discrete algorithm. While the Jordan-block analysis and the QEP-based stability proof (Theorem 3) are genuinely interesting, these errors prevent the paper's theoretical apparatus from supporting its algorithmic claims as currently argued. The experiments are limited to 2D toy problems with minima at the origin, which coincidentally avoids exposing the equilibrium bias. Against calibration anchors, the paper sits below papers with sound but incremental theory (~3.5–4.0) and is comparable to papers with interesting ideas but execution flaws that undermine the central argument (~3.0).

**Round 1 bracket:** 2.5–4.5.

**Round 2 narrowing:** Comparisons to "Dynamic Training Guided by Training Dynamics" (3.50, heuristic method with no theory but no errors), "Extending Stability Analysis to Adaptive Optimization" (3.50, sound theory but incremental), and "Revisiting High-Resolution ODEs" (3.75, correct theory, incremental contribution) all place the current paper lower because its mathematical errors are more severe than any weakness in those papers.

**Final score:** 3.0. **Decision:** Reject.

**Anchor papers retrieved (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| 1NYhrZynvC.md | 2.50 | R1 | Different topic (adaptive stepsize); paper is somewhat stronger |
| vBNTeQ7dPP.md | 2.50 | R1 | RL+control; different subfield |
| NbbsRnPBoS.md | 2.33 | R1 | Deep linear networks; comparable rejection level |
| 1MHgMGoqsH.md | 3.00 | R1 | MPC training framework; similar score level |
| naEeJTlRsr.md | 3.75 | R1,R2 | HR-ODEs for optimization; correct theory, incremental — our paper is weaker |
| sIE2rI3ZPs.md | 7.00 | R1 | Central flows; much stronger paper |
| 5uUr3WFmyZ.md | 5.00 | R1 | Hamiltonian descent; rigorous theory, our paper is weaker |
| dug02AimLZ.md | 6.25 | R1 | Second-order Nash; stronger theory |
| sbG8qhMjkZ.md | 8.00 | R1 | SVGD convergence; much stronger |
| cmfyMV45XO.md | 8.00 | R1 | Neural ODEs; much stronger |
| AoraWUmpLU.md | 8.00 | R1 | Neural ODEs; much stronger |
| cc8h3I3V4E.md | 8.00 | R1 | Nash equilibria; much stronger |
| OZZYqfplS3.md | 4.00 | R2 | PC stability; sound theory, our paper is weaker |
| 7AB077M4TY.md | 3.50 | R2 | Koopman training dynamics; heuristic but no errors, comparable |
| zPaTnGjgpa.md | 4.20 | R2 | GD instabilities; unclear claims but no math errors, our paper is weaker |
| W98SiAk2ni.md | 3.00 | R2 | Ensemble systems; similar score level |
| qZ4jYual5d.md | 3.50 | R2 | Lurie networks; different subfield |
| Cdng6X2Joq.md | 3.67 | R2 | CT-RL algorithm; different subfield |
| 9mOs2Bxd3Q.md | 3.50 | R2 | Adaptive optimizer stability; sound theory, our paper is weaker |
| GxrVyYoLSx.md | 3.50 | R2 | Fokker-Planck analysis; different subfield |

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>