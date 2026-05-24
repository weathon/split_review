Now I have sufficient calibration data. Let me synthesize everything into the final review.

## Summary of Calibration

**Round 1 bracket:** The paper sits somewhere between weak (2–3.5) and middle (3.5–7.5) bands. My initial estimate is that this paper is closer to the weak band.

**Round 2 narrowing:** I read multiple anchors:
- 1NYhrZynvC (2.50): Major theoretical flaws, mathematically incomplete claims, unclear convergence guarantees.
- 9mOs2Bxd3Q (3.50): Had errors in key equations but more extensive experiments with real networks.
- W98SiAk2ni (3.00): Novel framework but weak experiments, unclear practical utility.
- naEeJTlRsr (3.75): Incremental contributions but sound methodology.

The current paper has a **fatal conceptual error** (analyzing the wrong dynamical system), a **clear mathematical mistake** in the key derivation (Eq. 5), a **misclassification** of a standard convex function, and **only 2D toy experiments**. The theoretical flaws are more fundamental than those in the 3.50-range papers. It's closest in severity to 1NYhrZynvC (2.50).

**Final score: 2.5**

Now let me write the review.

The Fatal tier should contain the stability analysis issue and the integration error. Let me think about whether they're both truly fatal or if one is major.

The stability analysis issue: The paper analyzes the augmented second-order system (z = [θ; dθ/dt]) and draws conclusions about GD's stability from it. But:
1. The augmented system includes spurious zero eigenvalues from the reformulation
2. The linearization ignores the constraint x = -∇L(θ) that gradient flow satisfies
3. The conclusions (Table 1) contradict known results about gradient flow

This IS fatal because it invalidates the paper's core theoretical contribution (Sections 3-5, Theorem 2, Table 1).

The integration error in Eq. 5: ∫θ dt ≠ (1/2)θ². This is a clear mathematical error that breaks the connection between the continuous controller and the discrete algorithm. It IS also fatal because it means Algorithm 1 is not actually derived from the theory.

I'll put both as Fatal. The misclassification of the sphere as "convex but not strongly convex" goes as a Major weakness. Limited experiments go as Major.

Actually, let me be more careful. Let me check if the integration error is really as bad as I think.

The paper writes Eq. 5 as:
dθ'/dt = ∫ d²θ'/dt² dt = ∫ d²θ/dt² dt + ∫ u dt

u = -K₁θ - K₂ dθ/dt

∫ u dt = -K₁∫ θ dt - K₂∫ (dθ/dt) dt = -K₁∫ θ dt - K₂θ

The paper then claims ∫ θ dt = (1/2)θ², giving -(1/2)K₁θ² - K₂θ.

But ∫ θ dt is NOT equal to (1/2)θ² in general. The indefinite integral ∫ θ dt is the antiderivative of θ(t), while (1/2)θ² is the antiderivative of θ(t) dθ/dt = θ(t)θ'(t). These are different.

More precisely: d/dt[(1/2)θ²] = θ · dθ/dt, while ∫ θ dt is asking for a function whose derivative is θ. These are related but not equal: ∫ θ dt ≠ (1/2)θ² unless dθ/dt = 1.

Furthermore, in Algorithm 1, the update uses g_t = ∇L(θ_t) - K₁θ_t² - K₂θ_t (without the 1/2 factor). This is inconsistent with Eq. 5.

This is a genuine mathematical error. The algorithm doesn't actually implement the claimed controller.

OK, let me write the review now.Here is my final consolidated review:

---

## Summary

This paper proposes to analyze gradient descent (GD) through a second-order ODE derived from gradient flow, then designs a controller to stabilize the dynamics. The controller adds terms \(-K_1\theta^2 - K_2\theta\) to the gradient. The paper claims that GD is unstable for convex-but-not-strongly-convex and concave losses even when the learning rate satisfies the classical bound, and that the proposed "controlled gradient descent" (CGD) guarantees local asymptotic stability regardless of curvature.

## Strengths

- **Empirical demonstration of stabilization beyond the edge of stability (Section 7.2, Figure 3):** On a simple 2D quadratic, CGD with several hyperparameter choices remains stable at learning rates \(\eta=1.01\) where standard GD diverges. This visually validates that the proposed modification can increase learning-rate tolerance, even if the theoretical justification is flawed.

- **Hyperparameter robustness (Section 7.1, Figure 2):** On three 2D toy problems, CGD converges reliably across three different settings of \(k_1, k_2\) (0.05, 0.1, 0.2), suggesting the method does not require precise tuning of the controller gains on these simple problems.

## Weaknesses

### Fatal

1. **The stability analysis is performed on the wrong dynamical system, and the conclusions about GD's stability are incorrect.** The paper derives a second-order ODE \(d^2\theta/dt^2 = -H(\theta)\,d\theta/dt\) by differentiating gradient flow, then augments the state to \(\mathbf{z}=[\theta; d\theta/dt]\) and analyzes the Jacobian of *this* augmented system. However, GD / gradient flow is the *first-order* system \(d\theta/dt = -\nabla L(\theta)\), whose stability is determined by the eigenvalues of \(-H(\theta^*)\). For strongly convex losses, gradient flow is *asymptotically stable* (all eigenvalues of \(-H(\theta^*)\) are negative), and for convex-but-not-strongly-convex losses it is *Lyapunov stable* (zero eigenvalues but \(1\times1\) Jordan blocks because \(H\) is symmetric). The paper's claimed conclusions in Table 1 — that GD is "not asymptotically stable" for strongly convex and "unstable" for convex-not-strongly — contradict these standard results. The augmented system contains spurious zero eigenvalues and Jordan blocks that arise from the state-space reformulation, not from GD's actual dynamics. The analysis ignores that the constraint \(d\theta/dt = -\nabla L(\theta)\) restricts trajectories to a subspace where these apparent instabilities do not manifest. This invalidates the core theoretical contribution (Theorem 2, Table 1, Sections 4.2.1–4.2.3).

2. **The conversion from the continuous controller to the discrete algorithm is mathematically unsound (Section 6, Eq. 5).** The paper integrates the controller term \(u = -K_1\theta - K_2\,d\theta/dt\) to obtain \(\int u\,dt = -\frac{1}{2}K_1\theta^2 - K_2\theta\). This step claims \(\int\theta\,dt = \frac{1}{2}\theta^2\), which holds only if \(d\theta/dt = 1\) (i.e., \(\theta(t) = t + \text{const}\)), which is generally false. The indefinite integral of \(\theta(t)\) is *not* \(\frac{1}{2}\theta(t)^2\). Furthermore, Algorithm 1 uses \(-K_1\theta^2\) *without* the factor \(1/2\) from Eq. 5, indicating an additional inconsistency. The proposed update rule does not implement the continuous controller through any well-defined discretization, breaking the theory-to-algorithm connection entirely.

### Major

3. **The experimental evaluation is far too limited to support the paper's claims.** All experiments are on 2D toy problems (ellipse, sphere, quartic). No experiments on real neural network training, no comparison to standard optimizers (momentum, Polyak heavy-ball, Adam, Nesterov), and no discrete-time stability analysis are provided. The example labeled "convex but not strongly convex sphere" uses \(L(\theta) = \theta_1^2 + \theta_2^2\), whose Hessian is \(2I\) — this function is **strongly convex**, not convex-but-not-strongly. This misclassification undermines the experimental validation of the theoretical curvature classification. Without realistic evaluation and baseline comparisons, the practical utility of CGD is unsubstantiated.

4. **The discrete-time gap is acknowledged but unaddressed.** The conclusion acknowledges "a gap remains between continuous-time differential equations and the actual discrete gradient descent updates," yet the paper provides no discrete-time stability analysis, which is essential since Algorithm 1 is a discrete algorithm. The continuous controller analysis in Sections 3–5 does not guarantee stability of the discrete iterates.

### Minor

5. **The origin and effect of the \(\theta^2\) term are not justified.** The update includes an element-wise square term \(-K_1\theta^2\) that is atypical for optimization. The paper does not analyze its effect on the optimization landscape, whether it biases solutions, or how it relates to known mechanisms (gradient clipping, regularization).

### Trivial

None.

## Nice-to-Haves

- A proper derivation connecting the continuous controller to the discrete algorithm (e.g., via a symplectic or semi-implicit Euler discretization).
- Discrete-time stability analysis of the proposed update, or at minimum experiments showing the relation between continuous stability thresholds and discrete behavior.
- Comparison to momentum-based methods (Polyak heavy-ball, Nesterov) on the EoS experiment, since momentum also changes effective damping.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *Criticism about missing related works:* Removed per guidelines (cannot verify existence of missing citations).
- *Formatting/style nitpicks about typos and presentation:* Removed per guidelines (parser artifacts, not author errors).
- *Strength Finder's generic strengths such as "addresses an important problem" or "tackles interesting question":* Removed per guidelines — generic or lacking specific concrete evidence.
- *Strength Finder's strengths that conflict with verified fatal weaknesses (e.g., "rigorous stability-curvature link via second-order ODE"):* The strength relies on the stability analysis that has been shown to be fundamentally flawed.
- *Strength Finder's "provable asymptotic stability" claim:* This depends on the flawed analysis of the augmented system; the core finding is invalidated by the fatal weaknesses.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fix the mathematical error in Eq. 5.** If the intention is to derive an update from the continuous controller, use a proper discretization method (e.g., semi-implicit Euler) that respects the relationship between the continuous and discrete dynamics.
2. **Re-analyze stability using the correct first-order system.** If the goal is to study GD stability, analyze \(d\theta/dt = -\nabla L(\theta)\) or the discrete GD iterates directly. The second-order ODE is a consequence of gradient flow, not a separate model of the optimizer's dynamics.
3. **Validate on real problems.** Test on at least one standard task (e.g., logistic regression on MNIST, a small MLP) with comparisons to SGD, SGD+momentum, and Adam. Show test performance, not just training loss.
4. **Fix the curvature misclassification.** The function \(\theta_1^2 + \theta_2^2\) is strongly convex; use a genuinely convex-but-not-strongly function (e.g., \( \theta_1^2\) alone, or a function with a flat direction at the optimum) for the corresponding experiment.
5. **Analyze the \(\theta^2\) term.** Provide intuition or analysis for why element-wise squaring the parameters is a sensible modification, and discuss potential biases or side effects.

## Score and Decision

### Comparative Calibration

**Round 1 (bracketing):** Searched across three bands:
- *Weak band (avg < 3.5):* Retrieved W98SiAk2ni (3.00, novel framework but weak experiments), vBNTeQ7dPP (2.50, strong assumptions/model gap), 1NYhrZynvC (2.50, major theoretical flaws).
- *Middle band (3.5–7.5):* Retrieved OZZYqfplS3 (4.00, PCN stability analysis), SXopqmHJO1 (5.00, PL condition characterization), UMOlFJzLfL (5.75, SGD stability characterization).
- *Strong band (>7.5):* Retrieved AoraWUmpLU (8.00, Neural ODE with solid proofs).

*Initial bracket:* The paper sits between 2.0 and 5.0.

**Round 2 (narrowing):** Searched inside (1.0, 4.0) and (1.5, 4.0):
- Read 1NYhrZynvC (2.50): Major theoretical flaws — claims about convergence mathematically incomplete, missing assumptions. **Comparable severity** to the current paper.
- Read 9mOs2Bxd3Q (3.50): Had errors in key equations (diagonalization assumption not justified) but more extensive experiments with real networks (ResNet, ViT). **Slightly stronger** than the current paper.
- Read naEeJTlRsr (3.75): Incremental contributions but mathematically sound methodology. **Stronger** than the current paper.

**Final placement:** The current paper has fundamental theoretical flaws (wrong system analyzed, mathematical error in derivation) that are more severe than the 3.50-range papers. Its severity is closest to 1NYhrZynvC (2.50).

**Score anchors considered (all rounds):**
| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| W98SiAk2ni | 3.00 | 1 | Weaker experiments but conceptually coherent |
| vBNTeQ7dPP | 2.50 | 1 | Similar severity — strong assumptions with model gap |
| 1NYhrZynvC | 2.50 | 2 | Most similar severity — major theoretical flaws |
| 9mOs2Bxd3Q | 3.50 | 2 | Stronger — had real-network experiments |
| naEeJTlRsr | 3.75 | 2 | Stronger — methodology sound |
| OZZYqfplS3 | 4.00 | 1 | Stronger — sound stability analysis |
| SXopqmHJO1 | 5.00 | 1 | Stronger — solid characterization |
| UMOlFJzLfL | 5.75 | 1 | Stronger — rigorous theory |
| AoraWUmpLU | 8.00 | 1 | Much stronger — solid proofs, real experiments |

MY FINAL SCORE: <score>2.5</score>
MY FINAL DECISION: <decision>Reject</decision>