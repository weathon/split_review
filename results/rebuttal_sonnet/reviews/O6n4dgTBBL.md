## Summary

This paper reformulates gradient descent as a second-order ODE derived from gradient flow, analyzes local stability under three curvature regimes (strongly convex, convex-not-strongly-convex, concave) via Jacobian linearization, and proposes a control-theoretic modification intended to guarantee local asymptotic stability. A practical algorithm (Algorithm 1) is derived from the continuous-time controller and validated on 2D toy problems.

---

## Rebuttal Assessment

### Weakness 1: Equilibrium mismatch — controlled system equilibrates only at θ = 0
- **Author's response:** Acknowledge
- **Assessment:** Unconvincing (as a defense) — The author fully confirms the flaw. Paper Section 5 explicitly writes the controlled system as a linear map $J(\theta)\cdot[\theta; \hat{\theta}]$, and at equilibrium $(\theta^*, 0)$ the condition $-K_1\theta^* = 0$ forces $\theta^* = 0$ since $K_1 \succ 0$. The author confirms that all four experiments use loss functions with minimum at the origin, so the issue was systematically hidden. The paper text still claims stability "around an equilibrium $[\theta^*; 0]$" for arbitrary $\theta^*$, which is false. No revision has been made.
- **Score impact:** Weakness unchanged

### Weakness 2: Mathematical error in Eq. (5) — ∫K₁θ(t)dt ≠ ½K₁θ²
- **Author's response:** Acknowledge
- **Assessment:** Unconvincing (as a defense) — The author fully confirms the flaw. Paper Eq. (5) writes $\int K_1\theta(t)\,dt = \frac{1}{2}K_1\theta^2$, which conflates integration over the trajectory with integration over $\theta$ as a variable. The author states Algorithm 1 can be "motivated as an instantaneous, heuristic discretization" but concedes this "does not constitute a rigorous derivation from the continuous-time controller." The formal link from Theorem 3 to Algorithm 1 is broken and remains so.
- **Score impact:** Weakness unchanged

### Weakness 3: Algorithm 1 modifies the optimization target
- **Author's response:** Partially address
- **Assessment:** Unconvincing — The author confirms fixed points satisfy $\nabla L(\theta^*) = K_1(\theta^*)^2 + K_2\theta^*$, not $\nabla L(\theta^*) = 0$. The defense that all experiments have minimizers at the origin is technically accurate but simply confirms that the experiments were carefully (if inadvertently) chosen to avoid exposing this bias. No analysis of the bias magnitude or conditions under which it is negligible is provided.
- **Score impact:** Weakness unchanged

### Weakness 4: No neural network experiments despite neural-network-focused motivation
- **Author's response:** Acknowledge
- **Assessment:** Unconvincing — The author confirms every experiment is a 2D synthetic function with minimum at the origin and acknowledges the abstract and introduction overstate scope. No experiments have been added. The limitations section of the paper does not acknowledge the absence of NN experiments.
- **Score impact:** Weakness unchanged

### Weakness 5: "Variational interpretation" claim unsupported
- **Author's response:** Acknowledge
- **Assessment:** Unconvincing (as a defense) — The abstract (line 9) explicitly states "the proposed controller admits a variational interpretation." The author confirms no energy functional, no Euler–Lagrange equation, and no formal demonstration exist anywhere in the paper. The claim is simply false given the paper's content. Will be removed "in revision" but is not removed.
- **Score impact:** Weakness unchanged

### Weakness 6: Stability claim for "convex-not-strongly-convex" case potentially misleading
- **Author's response:** Partially address
- **Assessment:** Partially convincing — The author correctly notes that the instability result is formally valid within the paper's definitions (instability of the extended state $\mathbf{z} = [\theta; \mathbf{x}]$). The Jacobian analysis showing oversized Jordan blocks for the $\lambda = 0$ eigenvalue is technically correct. However, the author also concedes that classifying this as "instability of the optimizer" overstates the practical significance, since $\theta$ itself merely stalls. A clarifying remark is promised but not yet added.
- **Score impact:** Weakness downgraded (from minor flaw to acknowledged terminological imprecision)

---

## Strengths
- **Rigorous stability decomposition (Section 4 / Theorem 2):** The Jacobian block analysis for all three curvature regimes is mathematically correct. The Jordan-block argument distinguishing strong convexity from mere convexity in the extended dynamical system is valid and pedagogically useful.
- **Theorem 3 is locally self-consistent:** Application of Tisseur & Meerbergen (2001) Lemma 4 to the QEP $Q(\lambda) = \lambda^2 I + \lambda(H+K_2) + K_1$ is correctly executed *for the continuous-time controlled system at $\theta^* = 0$*.
- **Clear control-theoretic background (Section 2):** Compact, self-contained treatment of Lyapunov/asymptotic stability and linearization appropriate for ML audience.

---

## Weaknesses

### Fatal
1. **Equilibrium mismatch (confirmed by authors):** The controlled system $\frac{d}{dt}[\theta;\hat{\theta}] = J(\theta)[\theta;\hat{\theta}]$ has equilibrium only at $\theta = 0$, not at arbitrary minimizers of $L$. The paper's claim that Theorem 3 guarantees stability "around an equilibrium $[\theta^*; 0]$" for arbitrary $\theta^*$ is false. All experiments use functions with minimum at the origin, masking this.

2. **Broken theory-to-algorithm link via Eq. (5) (confirmed by authors):** The derivation $\int K_1\theta(t)\,dt = \frac{1}{2}K_1\theta^2$ is mathematically incorrect. Algorithm 1 does not implement the theoretical controller of Theorem 3. The paper provides no separate discrete-time stability analysis.

### Major
3. **Algorithm 1 modifies the optimization target (confirmed by authors):** Fixed points of Algorithm 1 satisfy $\nabla L(\theta^*) = K_1(\theta^*)^2 + K_2\theta^*$, not $\nabla L(\theta^*) = 0$. The method converges to a biased solution for any $\theta^* \neq 0$, which was systematically avoided in experiments.

4. **No neural network experiments (confirmed by authors):** Every experiment is a 2D function with minimum at the origin. The abstract and introduction claim applicability to "neural network training" and "deep learning," which is entirely unvalidated.

### Minor
5. **Unsubstantiated "variational interpretation" (confirmed by authors):** The abstract's claim is false given the paper's content. No energy functional or formal variational argument appears anywhere.

6. **Misleading "instability" label for convex-not-strongly-convex case:** Instability is formally for the extended state, while $\theta$ merely stalls. Partially addressed by author's clarification in rebuttal, but not yet fixed in paper.

### Trivial
- None beyond the above.

---

## Nice-to-Haves
- A corrected controller that shifts with the minimizer (e.g., $K_1\nabla L(\theta)$ instead of $K_1\theta$) would fix both the equilibrium mismatch and the optimization target bias simultaneously.
- A momentum-based discretization (heavy-ball style) would avoid the incorrect time-integration and preserve the continuous-time stability intuition.
- At minimum one experiment on an MLP (e.g., MNIST) is needed before the "neural network" framing can be sustained.

---

## Novel Insights

The Section 4 Jordan block analysis — identifying that a convex-but-not-strongly-convex loss induces a defective Jordan block in the extended Jacobian — is a clean, underappreciated observation. Although its practical interpretation for optimization requires more care (the optimization variable stalls rather than diverges), the formal structure is correct and could form a useful pedagogical lens for understanding why momentum methods sometimes misbehave in flat directions. This is the one technically sound and modestly novel contribution of the paper; it is unfortunately a minor part of a system whose central algorithmic claims rest on incorrect derivations.

---

## Suggestions
1. Fix the equilibrium: replace $K_1\theta$ with $K_1\nabla L(\theta)$ so the controller vanishes at any critical point of $L$.
2. Fix the time integration: implement the controller directly as an auxiliary momentum variable rather than integrating over the trajectory.
3. Perform a discrete-time stability analysis for at least a quadratic loss, rather than relying on the (incorrectly derived) continuous-time guarantee.
4. Add at least one NN experiment, or remove all neural network framing from the abstract, introduction, and conclusion.
5. Remove the "variational interpretation" claim from the abstract, or provide the required derivation.

---

## Score and Decision

The rebuttal is notably honest: the authors acknowledge every weakness flagged as fatal or major. However, honesty does not fix the mathematical errors, and the guidelines are explicit that "a rebuttal that says 'we will add this in revision' does not count." Reading the paper directly confirms:
- Eq. (5) contains the incorrect identity $\int K_1\theta(t)\,dt = \frac{1}{2}K_1\theta^2$ (line 224).
- The controlled system's equilibrium is at the origin, not at arbitrary $\theta^*$ (lines 192–198).
- Algorithm 1 uses $g_t = \nabla L - K_1\theta_t^2 - K_2\theta_t$ (line 238), biased away from true minimizers.
- All experiments use objectives with minimum at the origin (lines 258–271).
- The abstract claims a variational interpretation (line 9) that has no derivation anywhere in the paper.

The rebuttal provides no new evidence or arguments that any of these flaws are absent or minor. The score does not improve — the only change is confirming the flaw in the convex-not-strongly-convex framing is terminological (the formal math is correct, the interpretation is imprecise), which slightly mitigates one minor weakness. Two fatal flaws confirmed, two major flaws confirmed, one unsupported abstract claim confirmed. The paper remains a reject at the same score.

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>