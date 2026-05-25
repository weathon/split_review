Now I have all the information I need. Let me produce the final consolidated review.

---

## Summary

This paper analyzes gradient descent (GD) through a control-theoretic lens by formulating it as a second-order continuous-time dynamical system. Section 4 characterizes the stability of this system under different curvature regimes (strongly convex, convex-but-not-strongly, concave) using eigenvalue analysis. Section 5 introduces a linear state-feedback controller $u = -K_1\theta - K_2\dot\theta$ and proves (Theorem 3) that the controlled continuous system is locally asymptotically stable when $K_1\succ 0$ and $H+K_2\succ 0$. Section 6 attempts to convert this continuous-time controller into a discrete gradient modification (Algorithm 1), and Section 7 provides experiments on 2D toy objectives.

---

## Strengths

- **Second-order ODE formulation of GD dynamics (Section 4) is coherent.** Deriving $\ddot\theta = -H(\theta)\dot\theta$ from gradient flow and analyzing its local stability via the Jacobian's eigenvalue structure is mathematically sound. The classification (Lyapunov stable under strong convexity, unstable otherwise) follows correctly from the characteristic polynomial $\det(\lambda^2 I + \lambda H) = 0$ and the Jordan form analysis.

- **Theorem 3 is valid for the equilibrium at the origin.** Given the controlled continuous system $\ddot\theta = -(H+K_2)\dot\theta - K_1\theta$, the quadratic eigenvalue problem $Q(\lambda)=\lambda^2 I + \lambda(H+K_2) + K_1$ together with Lemma 4 (Tisseur & Meerbergen, 2001) correctly establishes that all eigenvalues have strictly negative real parts when $K_1\succ 0$ and $H+K_2\succ 0$, implying local asymptotic stability of the equilibrium $(\theta,\dot\theta)=(0,0)$.

- **The empirical results on 2D toy problems are suggestive.** The experiments show that the proposed CGD algorithm consistently avoids the divergence or oscillation that vanilla GD exhibits on these simple objectives, and that it tolerates learning rates beyond the $2/\lambda_{\max}$ threshold. The ablation with three different gain settings $(k_1=k_2\in\{0.05,0.1,0.2\})$ indicates the method is not overly sensitive to hyperparameter choice on these problems.

---

## Weaknesses

### Fatal

- **The derivation of Algorithm 1 from the controlled ODE contains a calculus error that severs the link between theory and algorithm.** Equation (5) performs the integration:
  \[
  \frac{d\theta'}{dt} = \int \frac{d^2\theta}{dt^2}dt + \int u\,dt
    = \frac{d\theta}{dt} - \frac12 K_1\theta^2 - K_2\theta,
  \]
  where $u=-K_1\theta-K_2\frac{d\theta}{dt}$.  The term $\int u\,dt$ evaluates to $-K_1\!\int\theta\,dt - K_2\theta$.  The paper then asserts $\int\theta(t)\,dt = \tfrac12\theta(t)^2$.  This is incorrect: $\frac{d}{dt}\bigl(\tfrac12\theta^2\bigr)=\theta\odot\frac{d\theta}{dt}\neq\theta$ in general.  The correct integral $\int\theta(t)\,dt$ is not $\tfrac12\theta^2$; the error is also dimensionally inconsistent (left: $[\theta]\times[\text{time}]$, right: $[\theta]^2$).  Because Algorithm 1 and its claimed connection to the control-theoretic analysis rest entirely on this step, the paper's central algorithmic contribution is not actually derived from the theory presented.  The experiments may still show that CGD works, but the theoretical grounding that the paper promises is absent.

### Major

- **The stability guarantee (Theorem 3) is proved for the wrong equilibrium.** The controlled system is $\ddot\theta = -H(\theta)\dot\theta - K_1\theta - K_2\dot\theta$.  At $(\theta^*\!,0)$ (a minimizer of $L$), the right-hand side evaluates to $-K_1\theta^* \neq 0$ (since $K_1\succ 0$).  Hence $(\theta^*,0)$ is **not** an equilibrium of the controlled dynamics — the actual equilibrium is at $\theta=0$.  Nevertheless, the paper (Section 5, line 198) states: "system 4 is locally asymptotically stable around an equilibrium $\begin{bmatrix}\theta\\ \hat\theta\end{bmatrix} = \begin{bmatrix}\theta^*\\0\end{bmatrix}$" and Theorem 3 is presented as a stability guarantee for convergence to the minimizer.  The linearization argument is applied at a point that is not an equilibrium, so the standard local stability theorem (Theorem 1) does not apply.  Theorem 3 is mathematically correct only for the equilibrium $(0,0)$, not for $(\theta^*,0)$.  This undermines the paper's claim that the controller stabilizes GD to the loss minimizer.

- **The proposed algorithm does not converge to the minimizer of the original loss.** Algorithm 1 drives parameters toward $\nabla L(\theta) = K_1\theta^2 + K_2\theta$, which is a different fixed point than $\nabla L(\theta^*)=0$ unless $\theta^*=0$ or both controller gains are zero.  The paper never acknowledges this bias or quantifies its effect.  This means the method solves a modified optimization problem, not the original one — a fact that directly contradicts the framing of the contribution.

- **Experimental validation is limited to 2D synthetic problems with misclassified curvature.** All experiments use only three trivial 2D objectives ($2\theta_1^2+0.5\theta_2^2$, $\theta_1^2+\theta_2^2$, $\theta_1^4+\theta_2^4$).  No experiments on neural networks, higher-dimensional problems, stochastic gradients, or any benchmark are provided, despite the paper claiming relevance to "modern deep neural networks" and "general non-convex and non-smooth loss" throughout the introduction.  Furthermore, the test functions are mislabeled: $\theta_1^2+\theta_2^2$ has Hessian $2I$ everywhere and is **strongly convex**, not "convex but not strongly convex"; conversely $\theta_1^4+\theta_2^4$ has a vanishing Hessian at the origin and is **not strongly convex** globally, contrary to the "strongly convex quartic" label.  These mistakes erode confidence in the experimental analysis.

### Minor

- **Continuous-to-discrete gap is acknowledged but not addressed.** The limitations section notes that discretization effects may alter stability properties, but the paper provides no analysis, no discretization-aware stability condition, and no attempt to bound the gap.  Without this, the relevance of the continuous-time analysis to the discrete algorithm actually evaluated remains unclear.

- **Hyperparameter ablation is restricted to $K_1=K_2$ jointly varied.**  The individual effects of $K_1$ vs $K_2$ are not disentangled, and no guidance or analysis is given for how to choose these gains for a given problem.

- **No comparison against other optimizers.**  The paper compares only against vanilla GD.  Given the second-order nature of the formulation, a comparison with momentum methods (which also modify the dynamics via a velocity term) would help position the contribution.

### Trivial

- The "convex but not strongly concave" label in Theorem 2 appears to be a typo (likely meant "concave").
- The paper refers to $\frac{d\theta'}{dt}$ as "the gradient of $\theta$" — this is non-standard phrasing (the gradient of a scalar loss is intended, not the gradient of $\theta$).

---

## Nice-to-Haves

- A proper discrete-time analysis or a principled discretization (e.g., semi-implicit Euler: $v_{t+1}=v_t-\eta(H(\theta_t)+K_2)v_t-\eta K_1\theta_t$, $\theta_{t+1}=\theta_t+\eta v_{t+1}$) would connect the continuous-time control theory to a concrete discrete algorithm without the erroneous integration.
- A controller of the form $-K_1(\theta-\theta^*)-K_2\dot\theta$ would preserve the equilibrium at $\theta^*$; the paper could discuss why this is impractical (since $\theta^*$ is unknown) and propose alternatives.
- Even a single small-scale neural network experiment (e.g., an MLP on a synthetic non-convex problem or a small CNN on a subset of CIFAR-10) would substantially strengthen the practical claims.

---

## Removed Points

These points were raised by the reviewers but are filtered out here as not meeting the inclusion standards:

- *"The paper does not discuss momentum methods or PID control."* — Removed per the hard rule against citing missing related works (external verification cannot be assumed).
- *"No variance or statistical significance reported."* — Removed as a generic reproducibility nitpick inappropriate for deterministic toy experiments.
- *"The opening framing overstates the novelty."* — Removed as a subjective opinion about presentation tone.
- *"The paper should compare against Adam, Nesterov, etc."* — Removed as scope creep; the paper is about stabilizing GD, not comparing all optimizers.
- *"The ad-hoc integration in Equation 5 with no justification."* — Merged into the fatal weakness above (the error itself, not the lack of justification, is the issue).

---

## Novel Insights

None beyond the paper's own contributions. The core insight — that GD's continuous-time second-order dynamics can be stabilized by a PD controller — is interesting, but the reviewers' analysis does not surface any novel observation that the paper itself does not already claim.

---

## Suggestions

1. **Fix the derivation.** Replace the erroneous integration in Equation 5 with a proper discretization of the controlled second-order ODE (e.g., semi-implicit Euler) or reframe Algorithm 1 as a heuristic inspired by the continuous-time analysis, explicitly disclaiming a direct derivation.
2. **Correct the equilibrium analysis.** Acknowledge that the controlled system's equilibrium is at $\theta=0$, not $\theta^*$, and either (a) redesign the controller to preserve the correct equilibrium (e.g., $u=-K_1(\theta-\hat\theta)-K_2\dot\theta$ with an estimate $\hat\theta$), or (b) characterize and bound the bias introduced by the current controller.
3. **Rename and rescope the experimental section.** Remove claims about neural network relevance unless neural network experiments are added. Correct the curvature labels for the test functions. Add at least one higher-dimensional or non-convex benchmark.
4. **Disentangle the hyperparameters.** Investigate the effect of $K_1$ and $K_2$ separately.
5. **Compare against a momentum baseline** to clarify how the proposed controller differs from adding a velocity term.

---

## Score and Decision

**Score**: 2.5 — The paper presents an interesting control-theoretic perspective on GD and the continuous-time analysis in Section 4 is technically sound. However, the fatal calculus error in Equation 5 severs the claimed connection between theory and algorithm, the equilibrium analysis is applied to the wrong fixed point, and the experiments are limited to mislabeled 2D toy problems. These problems are not fixable through minor revisions.

**Decision**: Reject

MY FINAL SCORE: <score>2.5</score>
MY FINAL DECISION: <decision>Reject</decision>