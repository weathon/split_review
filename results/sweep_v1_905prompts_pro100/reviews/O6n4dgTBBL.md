Now I have sufficient calibration data. Let me synthesize everything into the final review.

**Bracket assessment:** 
- Round 1 placed the paper in the weak band (< 3.5)
- Round 2: compared against grokking paper (2.00), faster GD (2.33), MPC paper (3.00), exact-linear-rate GD (2.50)
- The paper under review has a verifiable fatal mathematical error that breaks the main contribution, plus mislabeled experiments. It is clearer than the grokking paper (2.00) but has a more concrete fatal error. It is worse than the MPC paper (3.00) which lacked a fatal error.
- **Final bracket: 1.5-2.5, with a score of 2.0**

---

## Summary

This paper reformulates gradient descent as a second-order ODE and analyzes its stability under different curvature conditions via control-theoretic linearization. It then designs a continuous-time controller (Theorem 3) that provably guarantees local asymptotic stability regardless of curvature. The authors attempt to translate this controller into a discrete "Controlled Gradient Descent" algorithm (Algorithm 1) by integrating the controlled ODE, and test it on 2D toy problems.

## Strengths

- **Valid continuous-time stability analysis (Sections 3–5):** The reformulation of gradient flow as a second-order ODE and the linearization-based stability characterization under different curvature assumptions (Theorem 2) is mathematically sound within its framework. The controller design and the proof of asymptotic stability via quadratic eigenvalue methods (Theorem 3, citing Tisseur & Meerbergen, 2001) are correct in continuous time.

- **Clear problem framing:** The paper correctly identifies that classical stability analyses of gradient descent impose restrictive curvature assumptions (strong convexity, smoothness), and the control-theoretic lens is a legitimate approach to relaxing these constraints. The structure of the paper — from gradient flow to second-order ODE, to Jacobian linearization, to controller design — is logically organized.

## Weaknesses

### Fatal

- **The derivation of the discrete algorithm from the continuous-time controller is mathematically incorrect (Section 6, Equation 5).** The controller is defined as **u** = −K₁**θ** − K₂(d**θ**/dt). The paper then writes ∫**u** dt = −½K₁**θ²** − K₂**θ** and uses this to obtain the modified gradient in Algorithm 1. But the time integral of **u** is ∫**u** dt = −K₁∫**θ**(t) dt − K₂**θ**(t). Replacing ∫**θ**(t) dt with ½**θ²** — which would be ∫**θ** d**θ**, not ∫**θ** dt — is a basic calculus error with no justification. Consequently, Algorithm 1 (which adds −K₁θ² − K₂θ to the loss gradient) does **not** instantiate the theoretically proven continuous-time controller. All experimental results are obtained with this ad-hoc modification, not with a method that follows from the theory. This error breaks the paper's central claim: that they have derived a theoretically grounded stabilized gradient-descent variant from control theory.

### Major

- **Mislabeled curvature in experiments (Section 7.1):** The paper labels L(**θ**) = θ₁² + θ₂² as a "convex but not strongly convex sphere." This function has Hessian = 2I (positive definite) and is strongly convex with parameter m = 2. The experiment therefore does not test the intended curvature regime where the Hessian has zero eigenvalues — the very case for which the theory in Section 4.2.2 predicts instability. All three test functions (ellipse, sphere, quartic) are effectively strongly convex at initialization, meaning the experiments fail to validate the theory's central claim about stabilizing non-strongly-convex problems.

- **The quartic experiment uses a learning rate that predictably causes GD divergence:** For L(**θ**) = θ₁⁴ + θ₂⁴ at θ₀ = (1,1), the sharpness is 12, giving the classical stability bound η < 2/12 ≈ 0.167. The experiment uses η = 0.5, so GD's divergence follows directly from the standard 2/sharpness bound and does not demonstrate a failure of existing theory that the paper's method uniquely addresses. The paper's narrative — that GD "can diverge even when the learning rate satisfies the classical bound" — is not demonstrated by this example.

- **The experiments are limited to 2D toy problems with scalar controller gains (k₁I, k₂I).** No higher-dimensional, non-convex, or neural-network settings are tested. Given the paper's framing around deep learning training dynamics, the empirical evidence is insufficient to support claims of practical relevance.

### Minor

- **The instability claim for convex-but-not-strongly-convex case (Section 4.2.2) operates in the lifted state space** (θ, dθ/dt), not in the original parameters θ alone. The Jordan-block argument shows instability of the augmented state, but this is not shown to imply instability of the original gradient flow on θ — gradient flow on a convex function is dissipative and typically converges to the set of minima. The paper should discuss this distinction explicitly, as it affects the interpretation of Theorem 2.

- **The eigenvalue-shifting / higher-tolerance-on-learning-rate claim (contribution bullet 3) is qualitative only.** The paper states that the controller "increases the 2/sharpness threshold" but never quantifies the new threshold — neither theoretically (since the discrete analysis is absent) nor empirically (no systematic sweep of learning rates to find the stability boundary for CGD).

### Trivial

- The paper refers to the quartic θ₁⁴ + θ₂⁴ as "strongly convex" — it is convex but not strongly convex (the Hessian vanishes at the origin). This further muddles the curvature taxonomy already confused by the mislabeled sphere.

## Nice-to-Haves

- A proper discretization of the controlled second-order ODE (e.g., via a symplectic integrator or by solving for a second-order update rule analogous to momentum methods) would be the correct way to connect the continuous-time controller to a discrete algorithm, rather than the erroneous "integration" attempted in Equation 5.
- Extending experiments beyond 2D toy problems to settings with non-trivial curvature structure would substantially strengthen the empirical case for the approach.
- A quantitative characterization of the effective stability threshold after control (both theoretically and empirically) would support the learning-rate tolerance claims.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh critic's claim about "the connection to EoS and SAM is noted but not used to contextualize the experimental setup":** This is a fair observation but the paper does mention EoS in the context of the learning rate experiments (Section 7.2). The criticism is too broad. Removed.

- **Harsh critic's claim about "only one learning-rate value per surface is shown outside Figure 3":** The paper does show multiple learning rates in Figure 3 for the sphere, and multiple curvature settings in Figure 2. While limited, this is not a factual error. Demoted to part of the Major weakness about limited experiments.

- **Strength finder claim 3 (valid translation to discrete algorithm):** This is factually wrong — the derivation in Equation 5 contains a calculus error. Removed.

- **Strength finder claim 4 (empirical validation of theoretical claims):** The experiments test the incorrectly derived algorithm on mislabeled curvature cases, so they do not validate the theory. Removed.

- **Strength finder general claim about "the paper addresses an important problem":** Generic, no specific evidence. Removed.

- **Harsh critic's "Missing Parts and Places to Improve" section about missing appendix content:** The parser strips appendices; these sections exist in the original submission. Removed.

## Novel Insights

None beyond the paper's own contributions. The reviews confirm the continuous-time control-theoretic analysis is sound but identify a fatal gap in the discrete algorithm derivation that the authors and reviewers independently noted.

## Suggestions

- **Repair the derivation in Section 6.** The correct approach is to discretize the controlled second-order ODE directly (Equation 4), not to integrate it erroneously to recover a first-order gradient modification. A natural path: write the controlled dynamics d²θ/dt² = −(H+K₂)dθ/dt − K₁θ as a first-order system and apply a proper numerical integrator (e.g., semi-implicit Euler, symplectic methods), which would yield a two-state update rule analogous to momentum methods rather than a gradient-modification scheme.
- **Fix the curvature taxonomy in experiments.** Use a genuinely non-strongly-convex convex function (e.g., θ₁² + 0·θ₂², or a function with a flat direction) to test the zero-eigenvalue case, and correctly label θ₁²+θ₂² as strongly convex.
- **Systematically sweep learning rates to quantify the stability threshold** for the corrected algorithm, comparing it against the 2/sharpness bound for standard GD.

## Score and Decision

**Calibration anchors used:**

| Anchor ID | Avg Score | Round | Comparison |
|-----------|-----------|-------|------------|
| a8XwgTZzE0 | 2.00 | R1 | Grokking via dynamical systems — vaguer theory but no fatal derivation error. Our paper is clearer but has a more concrete fatal error. Comparable quality. |
| 1NYhrZynvC | 2.50 | R1 | Exact linear-rate GD — multiple issues with assumptions and comparisons, but no single fatal math error. Our paper is slightly weaker. |
| 1MHgMGoqsH | 3.00 | R1 | MPC for training NNs — motivation and comparison issues, but no fatal derivation error. Our paper is worse. |
| NbbsRnPBoS | 2.33 | R2 | Faster GD in deep linear networks — main theoretical result incorrect. Comparable to our paper. |
| cya3eEczAx | 1.67 | R2 | Adaptive proximal gradient — theoretical issues. Our paper has more valid theory (Sections 3-5) but a fatal bridge error. Slightly better. |

Round 1 bracket: 1.5–3.5. Round 2 narrowed to 1.67–2.50. The fatal derivation error and mislabeled experiments place this paper below the MPC paper (3.00) and the exact-linear-rate paper (2.50), but above the purely vague grokking paper at 1.67. The paper is most comparable to the "Faster GD in deep linear networks" at 2.33 and the grokking paper at 2.00 — it has clearer valid theoretical content than the grokking paper but a more fatal error. I score this at **2.0**.

**Originality:** The control-theoretic second-order reformulation is a somewhat novel angle on GD stability, though gradient-flow-as-dynamical-system is well-established. **Importance:** The question of stabilizing GD under general curvature is important, but the paper's contribution is undermined by the fatal error. **Claims supported:** The central claim (theoretically-grounded controlled GD) is not supported due to the derivation error. **Soundness:** The continuous-time theory is sound; the discrete algorithm derivation is not. **Clarity:** Reasonably well-organized but contains a hidden mathematical error. **Value to community:** Limited — the continuous-time insights may interest some readers, but no valid practical algorithm emerges.

MY FINAL SCORE: <score>2.0</score>
MY FINAL DECISION: <decision>Reject</decision>