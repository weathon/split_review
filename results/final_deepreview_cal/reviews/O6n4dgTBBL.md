Now I have sufficient calibration context. Let me write the final review.

**Calibration summary:**

- **Round 1 bracket**: Based on the three query bands, the plausible range was between ~2.5 and ~4.0. The paper has mathematical errors and factual mistakes, placing it below the 3.75 anchor (naEeJTlRsr, sound theory but incremental) and even the 4.00 anchor (OZZYqfplS3, sound theory with continuous-to-discrete gap concerns). 

- **Round 2 narrowing**: The 2.33 anchor (NbbsRnPBoS, narrow scope but sound math) and 4.25 anchor (gC0ikdZoz8, non-rigorous derivations but tested on NNs) helped calibrate. My paper has verifiable mathematical errors and factual mistakes, which is worse than the 2.33 paper's sin of narrow scope. The 4.25 anchor had questionable derivations but much more extensive experiments (CIFAR10, transformers) and no factual errors. My paper is clearly below both.

- **Final score**: 2.5. The paper has some interesting theoretical framing but is undermined by a genuine derivation error and factual mistakes. This is significantly below what could be considered for acceptance.

---

## Summary

This paper proposes a control-theoretic modification of gradient descent. The authors reformulate gradient flow as a second-order ODE d²θ/dt² = -H(θ)·dθ/dt, analyze its stability under various curvature settings, then introduce a controller u = -K₁θ - K₂ dθ/dt designed to make the system locally asymptotically stable for any curvature. They attempt to discretize this controlled ODE into a practical algorithm (CGD) that adds -K₁θ² - K₂θ to the gradient, and test it on three 2D synthetic functions.

## Strengths

- **Control-theoretic perspective on optimization**: Framing GD as a second-order dynamical system and applying controller design via the quadratic eigenvalue problem (Lemma 4, Theorem 3) is a conceptually interesting approach that connects two communities.

- **Theorem 3 is valid in continuous time**: The proof that the controlled ODE with K₁≻0 and H+K₂≻0 has all eigenvalues with strictly negative real parts (via the QEP) is mathematically sound as a continuous-time analysis.

- **Empirical stabilization on toy problems**: Figures 2 and 3 demonstrate that CGD converges on simple 2D quadratics where vanilla GD diverges (e.g., L = θ₁²+θ₂² with η=1.01 beyond the 2/sharpness threshold), providing proof-of-concept that the control approach can have practical effect.

## Weaknesses

### Major

1. **Mathematically invalid derivation connecting theory to algorithm (Equation 5 → Algorithm 1)**. The paper claims ∫u dt = -½K₁θ² - K₂θ where u = -K₁θ - K₂ dθ/dt. This requires ∫θ dt = ½θ², which is false for general θ(t). The integral of θ with respect to *time* does not simplify to ½θ² (which would be ∫θ dθ). The paper provides no justification for this step. As a result, Algorithm 1 is not provably derived from the controlled ODE, and the stability guarantees of Theorem 3 do not formally apply to the implemented method. This is a structural disconnect between theory and algorithm.

2. **Fundamental classification errors in loss functions**. The paper repeatedly misclassifies:
   - L(θ) = θ₁² + θ₂² as "convex but not strongly convex" (Section 7.1, Figure 2 caption). This function has Hessian = 2I, which is positive definite — it IS strongly convex.
   - L(θ) = θ₁⁴ + θ₂⁴ as "strongly convex quartic" (Section 7.1, Figure 2 caption). This function has Hessian = diag(12θ₁², 12θ₂²), which is zero at the origin — it is convex but NOT strongly convex.
   
   These are not typos; they are basic conceptual errors about the definitions that underpin the paper's theoretical narrative. They appear in both the text and figure captions, directly affecting the interpretation of the experimental results.

3. **Strawman framing of GD instability**. The paper analyzes the second-order reformulation d²θ/dt² = -H(θ)·dθ/dt and concludes GD is "only Lyapunov stable (not asymptotically)" even for strongly convex losses. This conclusion follows from the reformulation, not from GD itself. The Jacobian of the reformulated system has n zero eigenvalues as an artifact of the identity block **[0, I; 0, -H]** — these are not present in the original gradient flow dθ/dt = -∇L(θ). Standard GD with small enough step sizes is asymptotically convergent on strongly convex functions. The paper's central framing (Table 1, Theorem 2) attributes a problem to GD that only exists in the analyzed auxiliary system.

4. **Experiments grossly insufficient to support claims**. The paper is titled "Stabilizing Gradient Descent via Second-Order Control-Theoretic Dynamics" and Algorithm 1 is called "Controlled Gradient Descent for Neural Network Training," yet:
   - No experiments are conducted on any neural network or any problem with >2 parameters.
   - The only baseline is vanilla GD. No comparisons to momentum, Adam, gradient clipping, or weight decay (the -K₂θ term is essentially weight decay, which is not discussed).
   - All experiments are on three 2D synthetic functions, two of which are misclassified.
   
    The claims of "higher tolerance on learning rate" and "stabilizing neural network training" are unsupported by the evidence provided.

### Minor

1. **The Jordan block argument in Section 4.2.2 is asserted without complete justification**. The paper states "the geometric multiplicity is strictly less than the algebraic multiplicity" without explicitly computing either multiplicity from the Jacobian structure. (The conclusion is correct for this specific Jacobian, but the argument as presented is incomplete.)

2. **No convergence rate or quantitative guarantee for the discrete algorithm**. The paper provides only asymptotic stability in continuous time. How does the controller affect convergence rate? Does the θ² term cause issues for large initial parameters? None of this is addressed.

3. **No statistical significance or variance reporting**. All experiments appear to be single runs.

4. **The paper overclaims in its title and abstract**: "Controlled Gradient Descent for Neural Network Training" despite no NN experiments.

### Trivial

None.

## Nice-to-Haves

- Testing on at least one small neural network (e.g., MLP on MNIST) with comparison to standard baselines beyond vanilla GD.
- A proper discretization analysis showing how the controlled ODE maps to a correct discrete update.
- Analysis of how the θ² term interacts with parameters far from the optimum.

## Removed Points

These points were identified in the raw reviews but removed per filtering rules:

- Critic's claim that "the second-order system's Jacobian at the origin may still be diagonalizable" for L=θ⁴ — this is incorrect; [[0,1],[0,0]] is a nontrivial Jordan block. Removed as factually wrong.
- Accusations that the paper lacks comparison to related work that the critic does not cite by name — removed per hard rules about missing related works.
- Formatting/style nitpicks — removed as parser artifacts.
- Critic's claim that GD is "not asymptotically stable" is introduced by the critic, not the paper's claim — wait, actually the paper DOES claim this. So this point is valid to retain (folded into Weakness #3).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Correct the derivation in Equation 5.** Provide a proper discretization of the controlled ODE (e.g., via symplectic integrator or implicit Euler) and verify whether the resulting algorithm resembles the proposed update. If it does not, the algorithm and theory are disconnected and must be reconciled.

2. **Fix all convexity classifications.** L(θ)=θ₁²+θ₂² is strongly convex; L(θ)=θ₁⁴+θ₂⁴ is convex but not strongly convex. These errors must be corrected throughout Section 7.1 and Figure 2.

3. **Reframe the contribution honestly.** Drop the claim that GD is unstable in settings where it is not. The paper's real contribution is a controlled ODE that guarantees asymptotic stability; this can be evaluated on its own merits without manufacturing a crisis in standard GD. Alternatively, analyze the actual behavior of discrete GD rather than only the second-order reformulation.

4. **Add experiments on at least one small neural network** (MLP on MNIST or similar) to verify that CGD does not introduce pathological behavior and that the stability improvement translates beyond 2D quadratics. Compare to momentum, Adam, and weight decay.

---

## Score and Decision

**Round 1 bracket:** [2.0, 4.0] — determined by comparing against the 3.75 anchor (naEeJTlRsr: sound theory, limited novelty) and the 2.33 anchor (NbbsRnPBoS: narrow scope, sound within scope). The presence of verifiable mathematical errors and factual mistakes places this paper below both.

**Anchors considered:**
| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| 1MHgMgoqsH | 3.00 | 1 | "Unifying BP and FF through MPC" — not accessible |
| 1NYhrZynvC | 2.50 | 1 | "Exact linear-rate gradient descent" — not directly comparable |
| NbbsRnPBoS | 2.33 | 1 | "Faster GD in Deep Linear Networks" — narrow scope but sound math; this paper has errors |
| W98SiAk2ni | 3.00 | 1 | "Ensemble Systems for Function Learning" — not directly comparable |
| naEeJTlRsr | 3.75 | 1,2 | "Revisiting High-Resolution ODEs" — sound theory, incremental; this paper has errors |
| pBQs8kQm63 | 5.50 | 1 | "Finite Sample Analyses for Continuous-time Linear Systems" — strong theory, no experiments |
| OZZYqfplS3 | 4.00 | 2 | "Tight Stability for Predictive Coding Networks" — sound theory, continuous-to-discrete gap |
| gC0ikdZoz8 | 4.25 | 2 | "Continuous-Time Analysis of Adam" — non-rigorous derivations but tested on NNs |

**Round 2 narrowing:** The 2.33 anchor (NbbsRnPBoS) was criticized for narrow scope and unrealistic assumptions but had sound math within scope. This paper has actual mathematical errors (Equation 5) and factual errors (convexity misclassification), making it weaker. The 4.25 anchor (gC0ikdZoz8) had questionable derivations but tested on actual neural networks with reasonable baselines. This paper falls below both.

**Final calibrated position:** The paper has some interesting ideas (control-theoretic stabilization of GD, QEP analysis) but is undermined by a genuine mathematical error in the core derivation, basic factual errors about convexity, a misleading framing, and experiments limited to 2D toy problems. This places it below the 3.00 floor typical of technically sound but limited papers.

<score>2.5</score>
<decision>Reject</decision>