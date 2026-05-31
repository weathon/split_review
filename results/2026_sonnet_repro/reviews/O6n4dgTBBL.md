Now let me search calibration papers to properly score this work.Now I have enough anchors to write the final review. Let me synthesize everything.

---

## Summary

This paper reformulates gradient descent as a second-order ODE by taking the time derivative of gradient flow, analyzes local stability under three curvature regimes (strongly convex, convex-not-strongly-convex, concave) via Jacobian linearization, and proposes a control-theoretic modification intended to guarantee local asymptotic stability regardless of curvature. From the continuous-time controller it derives a practical update rule (Algorithm 1) and validates it on 2D toy problems.

---

## Strengths

- **Rigorous stability decomposition in Section 4 (Theorem 2).** The paper correctly analyzes the Jacobian structure of the second-order system for three curvature cases, uses Jordan block analysis to distinguish Lyapunov stability from asymptotic stability, and shows that even convex-not-strongly-convex losses admit "unstable" extended-state dynamics due to defective Jordan structure. The eigenvalue computation $\prod_{i=1}^n \lambda(\lambda + \lambda_i)$ and the resulting case splits are correct.

- **Theorem 3 is locally self-consistent.** The application of Lemma 4 (Tisseur & Meerbergen) to the quadratic eigenvalue problem $Q(\lambda) = \lambda^2 I + \lambda(H+K_2) + K_1$ is correctly executed: given $M \succ 0$, $C = H+K_2 \succ 0$, and $K = K_1 \succ 0$, all eigenvalues have negative real parts. Within its own scope, the proof is sound.

- **Clear, self-contained control-theoretic background.** Section 2 provides a compact treatment of Lyapunov/asymptotic stability and linearization (Theorem 1) that is appropriate for a machine-learning audience.

---

## Weaknesses

### Fatal

- **Equilibrium mismatch: the controlled system has equilibrium at θ = 0, not at loss minimizers.** In the controlled first-order system (Section 5):
  $$\frac{d}{dt}\begin{bmatrix}\boldsymbol{\theta}\\\hat{\boldsymbol{\theta}}\end{bmatrix} = \begin{bmatrix}0 & I\\ -K_1 & -(H(\boldsymbol{\theta})+K_2)\end{bmatrix}\begin{bmatrix}\boldsymbol{\theta}\\\hat{\boldsymbol{\theta}}\end{bmatrix}$$
  The equilibrium condition requires $-K_1\boldsymbol{\theta}^* = 0$; since $K_1 \succ 0$, this forces $\boldsymbol{\theta}^* = 0$. The paper never notes this — it claims to stabilize gradient descent at "an equilibrium $[\boldsymbol{\theta}^*; 0]$" for an arbitrary critical point $\boldsymbol{\theta}^*$ of $L$, but the controlled system actually admits an equilibrium only at $\boldsymbol{\theta} = 0$. Theorem 3's stability proof therefore applies only if the loss minimum coincides with the origin. All four experimental loss functions ($2\theta_1^2+0.5\theta_2^2$, $\theta_1^2+\theta_2^2$, $\theta_1^4+\theta_2^4$) have their minimum at the origin, systematically masking this issue. For any problem with a minimum at $\boldsymbol{\theta}^* \neq 0$, the algorithm converges to a wrong point.

- **Mathematical error in Eq. (5) breaks the theory-to-algorithm link.** The paper integrates the controller $\mathbf{u} = -K_1\boldsymbol{\theta} - K_2\frac{d\boldsymbol{\theta}}{dt}$ over time and writes:
  $$\int \mathbf{u}\, dt = -\tfrac{1}{2}K_1\boldsymbol{\theta}^2 - K_2\boldsymbol{\theta}$$
  The second term $\int K_2\frac{d\boldsymbol{\theta}}{dt}dt = K_2\boldsymbol{\theta}$ is correct. However, $\int K_1\boldsymbol{\theta}(t)\,dt \neq \tfrac{1}{2}K_1\boldsymbol{\theta}^2$ in general, because $\boldsymbol{\theta}(t)$ is a time-varying trajectory, not the variable of integration. The identity $\int \theta\, d\theta = \tfrac{1}{2}\theta^2$ holds only when integrating over $\theta$ itself, not over time. Algorithm 1's gradient correction $-K_1\theta_t^2 - K_2\theta_t$ therefore does not implement the theoretical controller, breaking the chain from Theorem 3 to the practical algorithm.

### Major

- **Algorithm 1 modifies the optimization target.** Setting aside the integration error, Algorithm 1 updates with $g_t = \nabla_\theta L(\theta_t) - K_1\theta_t^2 - K_2\theta_t$. This is gradient descent on $L'(\theta) = L(\theta) - \frac{1}{3}K_1\theta^3 - \frac{1}{2}K_2\theta^2$ (element-wise). The fixed points satisfy $\nabla L(\theta^*) = K_1(\theta^*)^2 + K_2\theta^*$, not $\nabla L(\theta^*) = 0$. The paper never discusses this or provides any analysis of the distance between the modified and original objectives' minimizers. For neural network training, this means CGD converges to the wrong parameters.

- **No neural network experiments despite neural-network-focused motivation.** The abstract, introduction, and conclusion explicitly frame the contribution as addressing instability "of neural network training" and "deep learning models." Every experiment is a 2D function with minimum at the origin. The behavior of CGD on networks with large or distributed parameters — where $\|K_1\theta^2 + K_2\theta\|$ can vastly exceed $\|\nabla L\|$ — is entirely untested. The limitations section acknowledges the continuous-time/discrete-time gap but does not address the absence of any non-toy experiment.

### Minor

- **The "variational interpretation" claimed in the abstract is never shown.** The abstract states "the proposed controller admits a variational interpretation," and this claim is also noted in Section 6. No energy functional, no Euler–Lagrange equation, and no formal demonstration that the modified update equals the gradient of any function appears anywhere in the paper.

- **The stability claim for the "convex-not-strongly-convex" case (Section 4.2.2) is potentially misleading.** The paper concludes gradient descent is "unstable" in this regime because the augmented state $(θ, dθ/dt)$ has an oversized Jordan block. But the gradient flow trajectory for $θ$ itself simply stalls in a flat direction — $θ$ does not diverge. Classifying this as "instability" of the optimizer conflates the auxiliary velocity variable's behavior with the optimization variable's behavior.

### Trivial

- None beyond the issues already noted.

---

## Nice-to-Haves

- A correctly derived discretization that preserves the loss minimizers could be based on auxiliary velocity variables (heavy-ball or Nesterov-like momentum) rather than the incorrect integration in Eq. 5. Establishing the connection carefully — including a discrete-time stability analysis even for the quadratic case — would make the paper substantially more convincing.
- Experiments on a small neural network (e.g., an MLP on MNIST) are needed before the "neural network training" framing can be sustained.
- A condition that ensures the correction terms remain small relative to the loss gradient would help characterize when the equilibrium mismatch is negligible in practice.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: "The second-order ODE carries no more information than the first-order gradient flow."** While technically true that trajectories satisfying the first-order ODE also satisfy the second-order ODE, reformulating as a second-order system and then augmenting with a controller is a valid design strategy. The reformulation is standard but provides the right scaffolding for applying the quadratic eigenvalue framework. Removed as scope-creep criticism.

- **Harsh Critic: "The stability of the uncontrolled system is applied to the wrong dynamical system."** This is partially valid (the extended-state analysis broadens the perturbation family), but calling it "wrong" is overstated. The Jacobian linearization at $(θ^*, 0)$ is a valid local analysis. The Jordan-block argument for the convex-not-strongly-convex case is retained above as a Minor issue (potentially misleading framing) rather than a fatal error.

- **Strength Finder: "Rigorous stability characterization across curvature regimes… goes beyond standard sharpness-based analyses."** Partially retained (stability decomposition is sound), but the claim of going "beyond" standard analyses is weakened by the equilibrium-mismatch flaw undermining the controlled half. The characterization of the uncontrolled system in Section 4 is kept as a genuine strength.

- **Strength Finder: "Translation of the continuous-time controller into a lightweight algorithmic update."** Removed: this is precisely where the mathematical error occurs. The translation is incorrect.

- **Strength Finder: "Robustness of CGD to controller hyperparameters."** Removed: the ablation is on three settings of $(k_1, k_2)$ on a single 2D quadratic with minimum at origin. This does not constitute evidence of robustness beyond the experimental setting used.

---

## Novel Insights

The paper's stability decomposition (Section 4) — showing that even a convex-not-strongly-convex loss induces a defective Jordan block in the second-order ODE's Jacobian, predicting linear growth in the auxiliary velocity — is a clean and underappreciated observation. Although the reviewer criticism that this conflates the velocity variable with the optimization variable is valid, the Jordan block analysis correctly identifies a structural difference between strong convexity and mere convexity in the extended dynamical system. This geometric picture could be a useful pedagogical framing for understanding why momentum methods sometimes diverge in flat directions.

---

## Suggestions

1. **Fix the controller derivation:** rather than integrating the controller over time (the mathematically incorrect step in Eq. 5), implement it directly as a momentum-like auxiliary state. Define $v_{t+1} = \beta v_t - \eta \nabla L(\theta_t)$ and modify $\theta_{t+1} = \theta_t + v_{t+1} - K_2 v_t - K_1\theta_t$ (schematically), then prove discrete-time stability for quadratic losses.
2. **Fix the equilibrium:** redesign the controller so it vanishes at any critical point of $L$, not only at $θ = 0$. E.g., replace $K_1\theta$ with $K_1\nabla L(\theta)$, which vanishes at any minimizer of $L$.
3. **Run at least one neural network experiment** (e.g., two-layer MLP on MNIST) to validate the claimed applicability to deep learning.
4. **Clarify the stability claim in Section 4.2.2**: explain that "instability" refers to the extended state, and that the optimization variable $θ$ itself merely stalls rather than diverges.

---

## Score and Decision

**Calibration anchor summary:**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| a8XwgTZzE0.md (Grokking dynamical systems) | 2.00 | R1 | Less coherent than this paper; essentially unreadable; no correct derivations. Paper is better. |
| 2NwHLAffZZ.md (Linearization of GD) | 2.33 | R1 | Also rejected for fundamental flaws; similarly shallow theory. Comparable. |
| vBNTeQ7dPP.md (RL with stability guarantee) | 2.50 | R1 | Rejected; also has control-theory lens but poor experiments. Comparable. |
| W98SiAk2ni.md (Ensemble systems) | 3.00 | R1 | Rejected; some structure, real theoretical content but fundamental issues. Comparable. |
| Zap3nZhRIQ.md (Non-differentiability) | 3.00 | R1 | Reasonable claims with issues; no fatal math errors. Slightly better than the paper. |
| naEeJTlRsr.md (HR-ODEs) | 3.75 | R2 | Correct derivations; incremental but sound. Clearly better than this paper. |
| 1NYhrZynvC.md (Exact linear-rate GD) | 2.50 | R2 | Rejected for flawed derivations and impractical assumptions. Comparable. |
| NbbsRnPBoS.md (Deep linear networks) | 2.33 | R2 | Rejected; similar scope and issues. Comparable. |
| 5uUr3WFmyZ.md (Hamiltonian descent) | 5.00 | R2 | Full convergence proofs, stochastic settings, correct theory. Clearly stronger. |

**Round 1 bracket:** 2.0–4.0. The paper has a clean presentation and valid partial theory (Section 4) unlike the worst papers, but has at least two fatal/major verifiable flaws that differentiate it from papers in the 4–5 range.

**Round 2 narrowing:** The most comparable anchors are the 2.33–3.0 range papers (flawed derivations, toy experiments, some theoretical content). The HR-ODE paper at 3.75 has correct derivations and more depth — this paper falls below it. The paper scores around **3.0**: it has a coherent structure and a partially sound Section 4, but the mathematical error in Eq. 5 and the equilibrium mismatch are verifiable, fatal flaws that undermine the central contribution.

**Axis evaluation:**
- *Originality:* Moderate framing (control theory for GD stability), but the execution is flawed.
- *Importance of research question:* High — stabilizing GD is important.
- *Claims well-supported:* No — the central theorem-to-algorithm link is broken by Eq. 5.
- *Soundness of experiments:* Poor — 2D toy problems only, all centered at origin.
- *Clarity of writing:* Reasonable; the paper is readable.
- *Value to research community:* Low in current form due to fundamental errors.

**Final score: 3.0, Reject.**

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>