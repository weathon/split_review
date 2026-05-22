Now I have a clear picture. Let me compile the final review.

**Round 1 bracket:** Based on calibration search, I initially bracket this paper between 2.5 and 4.0 — above papers with near-zero scores but below papers with broader validation (scores 3.5-4.0).

**Round 2 narrowing:** After comparing with anchors at scores 2.5 (Sp1zXxM8ik — CT-AGD, rejected, heuristic with weak theory), 3.0 (dojxn0hE8m — Rolling Ball, rejected, optimization heuristic), 3.5 (ToATXZ0E0f — SGD not Brownian motion, rejected, theory-heavy but limited), and 3.6 (WX8uuLUSR4 — Conflicting Biases, rejected, experiments on real data but weak theory), I calibrate:

This paper is cleaner and more novel in its framing than CT-AGD (2.5) and Rolling Ball (3.0). But unlike Conflicting Biases (3.6), its experiments are restricted to 2D toy problems, and unlike the SGD-not-Brownian paper (3.5), it has a clear mathematical error in its central derivation. The paper is most comparable to a well-framed idea with flawed execution — better than the 2.5-3.0 heuristics but not reaching 3.5-4.0 territory.

**Final score: 3.0**

---

## Summary
This paper proposes to analyze gradient descent through a continuous-time, second-order control-theoretic lens. It derives a second-order ODE from gradient flow, analyzes its stability under different curvature regimes (strongly convex, convex but not strongly convex, concave), and designs a linear controller that asymptotically stabilizes the continuous dynamics. From this controller, the paper attempts to derive a modified discrete gradient descent algorithm (CGD) that adds a gradient guidance term \( -K_1\theta^2 - K_2\theta \). Experiments are conducted on 2D synthetic objectives.

---

## Strengths

1. **Novel perspective linking control theory to GD stability analysis.** Framing gradient descent as a second-order dynamical system and applying linearization-based stability analysis (Theorem 1, Section 4) is a conceptually interesting departure from standard discrete-time analyses. The resulting characterization of stability under different curvature regimes (Theorem 2, Table 1) is mathematically sound *for the continuous-time system*.

2. **Valid asymptotic stability guarantee for the controlled continuous system.** Theorem 3, using Lemma 4 (the quadratic eigenvalue problem), correctly proves that the controlled second-order ODE (with linear controller \(u = -K_1\theta - K_2 d\theta/dt\)) is locally asymptotically stable regardless of curvature. This result is standard in control theory but its application to the GD setting is novel.

3. **Empirical demonstration of CGD on toy problems.** Figure 3 shows that CGD converges at \(\eta = 1.01\) for a sphere loss (sharpness = 2) where standard GD diverges, providing a concrete (if small-scale) demonstration of improved learning-rate tolerance.

---

## Weaknesses

### Major

1. **Mathematically invalid integration in Equation (5) — theory does not yield the proposed algorithm (structural).**  
   The paper claims to derive the CGD update by integrating the controlled second-order ODE. Equation (5) states:
   \[
   \frac{d\theta'}{dt} = \int \frac{d^2\theta'}{dt^2} dt = \int \frac{d^2\theta}{dt^2} dt + \int u dt = \frac{d\theta}{dt} - \frac{1}{2}K_1\theta^2 - K_2\theta,
   \]
   where \(u = -K_1\theta - K_2\frac{d\theta}{dt}\). The critical step is \(\int \theta\, dt = \frac{1}{2}\theta^2\), which is mathematically unfounded. For a trajectory \(\theta(t)\), the antiderivative \(\int \theta(t)\, dt\) is some function \(F(t)\) with \(dF/dt = \theta(t)\). It is not \(\frac{1}{2}\theta(t)^2\), which differentiates to \(\theta(t)\cdot d\theta/dt\). This error severs the claimed connection between the control-theoretic analysis (Section 5) and the proposed algorithm (Algorithm 1). The algorithm may still be a reasonable heuristic, but it is *not* derived from the theory as presented.

2. **Mismatch between the analyzed controller and the implemented algorithm.**  
   The stability analysis in Section 5 (Definition 4, Theorem 3) studies the *linear* controller \(u = -K_1\theta - K_2 d\theta/dt\) acting on acceleration \(d^2\theta/dt^2\). However, Algorithm 1 uses a *quadratic* parameter penalty \(-K_1\theta_t^2\) (element-wise square) added directly to the gradient (velocity). These are different dynamical systems. No theoretical claim about the stability of Algorithm 1 follows from Theorem 3, because the theorem applies to the linear system analyzed in Section 5, not to the quadratic-penalty discrete update in Algorithm 1.

3. **Continuous-time analysis does not directly support claims about discrete GD.**  
   The paper repeatedly states that GD "can diverge even when \(\eta < 2/L\)" and makes claims about discrete algorithm behavior, but Theorem 2 analyzes the continuous second-order ODE, not discrete gradient descent. The experiments in Figure 2 show GD *converging* (not diverging) for the ellipse with \(\eta=0.5\) — it oscillates but eventually reaches the minimum. The sphere loss example at \(\eta=0.995\) is described as showing "slow convergence or marginal instability," not divergence. The motivation is overstated relative to the actual evidence. The paper acknowledges this gap in the Limitations (Section 8) but the gap is substantial.

4. **Insufficient empirical validation.**  
   All experiments are on 2D synthetic objectives (quadratic and quartic). There are no experiments on neural networks, real datasets, or even moderately higher-dimensional problems. The method is only compared against vanilla GD — no comparison with momentum, Adam, Polyak heavy-ball, Nesterov acceleration, or any other stabilization technique. The controller hyperparameters \((k_1, k_2)\) are simply set equal and swept over three values, with no analysis of how to choose them in practice or how they interact with different problem scales. This evidence is too thin to establish the method's practical value.

### Minor

1. The paper claims CGD provides a "higher tolerance on learning rate," but only tests the sphere loss at learning rates very close to the edge-of-stability threshold (\(\eta \approx 1\)). A broader sweep of learning rates across different problem classes would strengthen this claim.

2. The ablation study (Figure 2) tests only three settings of \(k_1=k_2\) (0.05, 0.1, 0.2) and always sets them equal. The effect of independently varying \(K_1\) and \(K_2\) and the interaction with different Hessian curvatures is not explored.

---

### Trivial
None.

---

## Nice-to-Haves
- A discrete-time stability analysis of the proposed update (e.g., via Lyapunov analysis for quadratic objectives) would bridge the theory-algorithm gap.
- Comparison with momentum-based methods (Polyak heavy-ball, Nesterov) would help situate CGD among existing stabilization techniques.
- Experimental validation on higher-dimensional problems (e.g., logistic regression, small neural networks) would significantly strengthen the empirical contribution.
- Guidance on selecting \(K_1, K_2\) in practice — e.g., how they should scale with problem dimension, learning rate, or Hessian spectrum.

---

## Removed Points
- *"No analysis of the discrete dynamics"* moved here: This is subsumed by Weakness #3 (continuous/discrete gap already listed).
- *"Missing comparison with existing stabilization methods"* moved here: Subsumed by Weakness #4.
- *"No guidance on setting controller hyperparameters"* moved here: Subsumed by Weakness #4.
- *"The experiments use only deterministic GD"* moved here: The paper explicitly scopes itself to deterministic GD; stochastic is listed as future work.
- Strength #4 from Strength Finder ("Derivation of a practical gradient guidance term") removed: The derivation is mathematically invalid, so this is not a valid strength.
- Strength #1 from Strength Finder removed in part: the claim that "GD can diverge even when \(\eta < 2/L\)" is not demonstrated for discrete GD; the analysis is for the continuous ODE.
- Harsh critic's claim about "Jordan blocks of size >1" being "irrelevant to discrete GD" removed: This is a valid analysis of the continuous ODE within the paper's stated framework; the paper never claims this Jordan block analysis directly applies to discrete GD.
- *"No experiments on stochastic gradients"* removed: explicitly listed as future work.
- Various formatting/style nitpicks removed per hard rules.

---

## Novel Insights
None beyond the paper's own contributions. The core weakness — that the derivation connecting theory to algorithm is invalid — is the central finding of this review.

---

## Suggestions
1. **Fix the derivation.** Either (a) present a correct derivation linking the continuous controller to a discrete update, (b) directly propose CGD as a heuristic inspired by control theory without claiming a derivation, with a new discrete-time stability analysis, or (c) change the algorithm to use a linear penalty \(-K_1\theta\) (matching the theory) and analyze that system.
2. **Expand experimental scope.** At minimum, validate on a few higher-dimensional problems (e.g., logistic regression on MNIST, a small MLP) with comparisons to momentum, Adam, and weight decay.
3. **Provide hyperparameter guidance.** Show how \(K_1, K_2\) should be set relative to the Hessian spectrum or learning rate.

---

## Score and Decision

**Calibration anchors (all rounds):**

| anchor_id | avg_score | round | comparison |
|-----------|-----------|-------|------------|
| cmuHsIGlqC | 3.00 | R1 | Sharpness of minima in deep MF — rejected, has a theoretical result but limited scope. Similar quality to current paper. |
| Op8RDj5qX1 | 3.00 | R1 | Optimizing optimizers — rejected, heuristic design with limited theory. Slightly weaker contribution than current paper. |
| UKcSMWt6UW | 4.00 | R1 | PGD local convergence — withdrawn, more rigorous theory but incremental. Current paper has comparable theoretical ambition but a mathematical error. |
| XtYcnbnJ1n | 5.00 | R1 | Adam min-max — rejected, has substantial theory and some experiments. Current paper is significantly weaker. |
| Sp1zXxM8ik | 2.50 | R2 | CT-AGD — rejected, heuristic method with weak theory. Current paper has a more novel framing but similar execution issues. |
| dojxn0hE8m | 3.00 | R2 | Rolling Ball Optimizer — rejected, heuristic optimization method. Comparable to current paper. |
| ToATXZ0E0f | 3.50 | R2 | SGD not Brownian motion — rejected, theory-heavy but limited scope. Current paper has a mathematical error that makes it weaker. |
| WX8uuLUSR4 | 3.60 | R2 | Conflicting Biases at EoS — rejected, experiments on real datasets but weak theory. Current paper has weaker experiments but different contribution type. |

**Round 1 bracket:** [2.5, 4.0]  
**Round 2 narrowing:** Compared to anchors at 2.5 (CT-AGD), 3.0 (Rolling Ball, Sharpness of minima), and 3.5-3.6 (SGD not Brownian, Conflicting Biases), the current paper sits near 3.0. It has a novel conceptual framing and some valid continuous-time analysis (unlike CT-AGD and Rolling Ball), but the mathematical error in Equation (5) and the extremely limited experiments prevent it from reaching the 3.5-4.0 range where papers have either sound theory or reasonable empirical breadth.

**MY FINAL SCORE:** <score>3.0</score>  
**MY FINAL DECISION:** <decision>Reject</decision>