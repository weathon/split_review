Now I have sufficient data for calibration. Let me compile the final review.

**Calibration Analysis:**

Anchors retrieved:
- **Round 1, band <1.5**: Uj0h13lVrR (1.00), nSDOkm0SKo (1.00) — unrelated/low-quality papers. Not relevant comparisons.
- **Round 1, band 1.5–3.5**: 1NYhrZynvC (2.50) — "Exact linear-rate gradient descent": confused theory with missing assumptions, weak experiments. Our paper has cleaner theory but a math error in derivation.
- **Round 1, band 3.5–5.5**: zPaTnGjgpa (4.20) — "Can Stability be Detrimental?": GD stability/eigenvector rotation, experiments on real datasets. OZZYqfplS3 (4.00) — "Tight Stability, Convergence, and Robustness Bounds for Predictive Coding Networks": dynamical systems analysis of learning algorithm, experiments on MNIST/CIFAR, continuous-time gap concern. O0FOVYV4yo (5.00) — GD convergence analysis for overparameterized models.
- **Round 1, band 5.5–7.5**: sIE2rI3ZPs (7.00) — "Understanding Optimization in Deep Learning with Central Flows": extensive experiments on real neural networks, novel framework, well-written. Much stronger than our paper. 36L7W3ri4U (7.00) — game theory paper, less relevant.
- **Round 1, band 7.5–8.5**: 4xWQS2z77v (8.00) — "Exploring Loss Landscape via Convex Duality": rigorous convex analysis with phase transitions. Much stronger.
- **Round 1, band >8.5**: No results.

**Round 1 bracket:** Between 2.5 and 4.5. The paper has a genuine theoretical contribution and interesting idea, but the math error in the algorithm derivation, mislabeled experiments, and complete lack of real-world experiments place it below the score-4.0 anchors (which had at least some real experiments). The paper is better than the score-2.5 paper which had confused theory. Narrowing to 3.0–3.5.

**Final score: 3.0.** The paper's theoretical framework is clean and the control-theoretic idea is novel, but the math error in Equation 5 breaks the theory-to-algorithm bridge, the curvature labels are factually wrong, and all experiments are on 2D toy problems despite the deep learning framing. These issues collectively prevent the paper from supporting its claims, though the core idea has merit for a revised version.

---

## Summary
This paper formulates gradient descent as a second-order dynamical system, analyzes its stability under different loss curvature assumptions, and proposes a control-theoretic controller term ($u = -K_1\theta - K_2\dot{\theta}$) that guarantees local asymptotic stability. The controller is translated into an additive gradient modification $-K_1\theta^2 - K_2\theta$ (Algorithm 1). Experiments on 2D synthetic objectives demonstrate CGD converging where GD fails.

## Strengths
- **Well-executed stability analysis via Jordan normal form (Theorem 2, Sections 4.2.1–4.2.3):** The case-by-case analysis linking Hessian eigenvalue structure to stability outcomes is technically sound. For strongly convex losses, the paper correctly shows Jordan blocks for the zero eigenvalue are 1×1 (yielding Lyapunov stability), while for convex-not-strongly losses, larger Jordan blocks cause instability. This is a clean, well-argued decomposition.
- **Elegant controller design via quadratic eigenvalue problem (Theorem 3, Lemma 4):** The controller transforms the characteristic equation into a QEP $Q(\lambda) = \lambda^2 I + \lambda(H+K_2) + K_1$. Applying Lemma 4 (Tisseur & Meerbergen, 2001) with $M=I \succ 0$, $C=H+K_2 \succ 0$, and $K=K_1 \succ 0$ yields that all eigenvalues have strictly negative real parts. The reasoning chain is verifiable.
- **Empirical demonstration that CGD stabilizes where GD fails (Figures 2, 3):** Figure 3(c) shows CGD converges at $\eta=1.01$ (above the $2/\text{sharpness}=1.0$ threshold) while GD diverges, concretely demonstrating improved learning-rate tolerance. Across multiple settings in Figure 2, CGD consistently converges while GD oscillates or diverges.
- **Robustness to controller hyperparameters (Section 7.1 ablation):** Across $k_1=k_2 \in \{0.05, 0.1, 0.2\}$, CGD consistently converges, indicating the method does not require fine-tuning.

## Weaknesses

### Fatal
None.

### Major
- **Mathematical error in deriving Algorithm 1 (Equation 5, line 224):** The paper claims that integrating the controller $u = -K_1\theta - K_2\dot{\theta}$ with respect to time yields $-\frac{1}{2}K_1\theta^2 - K_2\theta$. The second term is correct ($\int -K_2\dot{\theta}\,dt = -K_2\theta$), but the first is not: $\int -K_1\theta(t)\,dt$ does not equal $-\frac{1}{2}K_1\theta(t)^2$ in general. The result $-\frac{1}{2}K_1\theta^2$ comes from integrating with respect to $\theta$, not time, which requires $d\theta/dt = 1$. This error severs the mathematical bridge between the theoretically analyzed controlled system (which has proven stability guarantees via Theorems 2–3) and Algorithm 1. The algorithm is a well-defined update rule, but the theoretical justification is broken.

- **Factual errors in curvature classification of test functions (Section 7.1, lines 259–271):** The paper mislabels curvature: (1) $L(\theta) = \theta_1^2 + \theta_2^2$ is called "convex but not strongly convex sphere" (line 271), but its Hessian is $H=2I$, which is positive definite with $m=2$ — making it **strongly convex**. (2) $L(\theta) = \theta_1^4 + \theta_2^4$ is called "strongly convex quartic" (line 259), but the Hessian at the origin is zero, so no $m>0$ satisfies $H \succeq mI$ globally — it is convex but **not strongly convex**. The labels are swapped. Consequently, the paper's claim to test "across different curvature regimes" is undermined: the convex-but-not-strongly-convex case (distinctly characterized in Theorem 2) is never actually tested.

- **No experiments on neural networks despite the framing:** Algorithm 1 is titled "Controlled Gradient Descent for Neural Network Training" and the introduction frames the work around "modern deep neural networks." All experiments use 2D synthetic objectives. The headline claims about improving stability in deep learning training are unsupported by the evidence presented.

- **All stability guarantees are continuous-time but the algorithm is discrete:** Theorems 2 and 3 prove stability for continuous-time ODEs. The actual algorithm is a discrete update rule. Continuous-time stability does not imply discrete stability, and this gap is especially significant because the paper's headline claim of improved learning-rate tolerance is inherently discrete (the $2/\text{sharpness}$ threshold from Cohen et al., 2021). The paper acknowledges this gap only in Limitations (line 302) without addressing it.

### Minor
- **Parameterization dependence of the controller:** The controller adds $-K_1\theta^2 - K_2\theta$ where $\theta$ are raw parameter values. Reparameterizing $\tilde{\theta} = \theta - c$ (which doesn't change the loss) changes the controller to $-K_1(\tilde{\theta}+c)^2 - K_2(\tilde{\theta}+c)$. The controller's effect depends on the arbitrary origin of the parameter space. This is not discussed.

- **The condition $K_2 \succ -H(\theta)$ for all $\theta$ (Definition 4, Remark 2) is never operationalized:** This requires knowledge of the Hessian's spectral properties across the parameter space. No practical mechanism for satisfying it is provided, nor is the computational cost discussed.

- **No comparison with any baseline beyond vanilla GD:** Experiments compare only against vanilla gradient descent. No momentum, Adam, SAM, or other stabilized optimizer is included.

## Nice-to-Haves
- A simple discretization analysis showing the discrete version remains stable for finite learning rates.
- Testing on at least one genuinely convex-but-not-strongly-convex function and one non-convex function with correct labels.
- Comparing CGD to momentum-based methods and adaptive optimizers.
- Redesigning the controller to use parameterization-invariant quantities.

## Removed Points
These points are flagged to be removed, treat them with caution.
- None removed — all points verified against the paper text.

## Novel Insights
The paper's genuinely novel insight is identifying that GD's second-order reformulation naturally leads to a quadratic eigenvalue problem structure, enabling principled controller design via Lemma 4. The connection between control-theoretic QEPs and optimization stability is not obvious and could seed a productive research direction. However, the translation to a practical algorithm is undermined by the Equation 5 error, and the lack of discretization analysis and real experiments limits the immediate impact.

## Suggestions
- Fix the derivation in Equation 5 by either finding the correct first-order ODE or directly motivating Algorithm 1 from a discrete-time control framework.
- Correct the curvature labels and add a genuinely convex-but-not-strongly-convex test case (e.g., $L(\theta) = |\theta|^4$ with flat directions).
- Provide at least basic discretization analysis (e.g., stability for $\eta < \eta_{\max}(K_1, K_2)$).
- Add experiments on a neural network task, even a small one (e.g., 2-layer MLP on MNIST).
- Compare against momentum and adaptive optimizers.

## Reporting

**Anchors retrieved (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| Uj0h13lVrR | 1.00 | 1 | Unrelated GFlowNet paper; much worse |
| nSDOkm0SKo | 1.00 | 1 | Unrelated finance paper; much worse |
| 1NYhrZynvC | 2.50 | 1 | "Exact linear-rate GD": confused theory, missing assumptions; our paper has cleaner theory but math error |
| NbbsRnPBoS | 2.33 | 1 | "Faster GD in Deep Linear Networks": rejected with depth-hurts concerns; somewhat comparable |
| OcTUquFXfx | 2.60 | 1 | "Discovering Global Minima": rejected for weak evaluation; somewhat comparable |
| nM2kuesKpC | 3.00 | 1 | "D2P2-SGD": uniformly rejected; similar to our paper's situation |
| zPaTnGjgpa | 4.20 | 1 | "Can Stability be Detrimental?": similar topic, experiments on real data, rejected for overlapping claims |
| OZZYqfplS3 | 4.00 | 1 | "PC Networks Stability": dynamical systems analysis of learning, MNIST/CIFAR experiments, continuous-time gap concern |
| iqHh5Iuytv | 4.50 | 1 | "RNNs with gracefully degrading attractors": dynamical systems stability; different domain |
| O0FOVYV4yo | 5.00 | 1 | "Local PL and Descent Lemma for GD": convergence analysis; stronger theory |
| 36L7W3ri4U | 7.00 | 1 | "Beating PoA in Potential Games": game theory; less relevant |
| sIE2rI3ZPs | 7.00 | 1 | "Central Flows": extensive real experiments, novel framework; much stronger |
| NLbRvr840Q | 6.00 | 1 | "Hypergraph Dynamic System": control-diffusion ODE; different domain |
| mkNVPGpEPm | 6.67 | 1 | "Associative memory and dead neurons": Lyapunov analysis; different domain |

**Round 1 bracket:** 2.5–4.5. The paper has a genuine theoretical contribution (control-theoretic QEP for GD stabilization) but the math error in Equation 5, mislabeled experiments, and absence of real-world experiments place it below the 4.0 anchors (which had at least some real experiments). It's above the 2.5 paper which had confused theory and poor writing.

**Final calibration:** The paper sits at 3.0 — it has a clean theoretical framework and interesting idea, but the broken derivation, factually wrong curvature labels, and toy-only experiments prevent it from supporting its claims. The 4.0 anchor (OZZYqfplS3) had similar continuous-time gap concerns but better experiments (MNIST/CIFAR) and no math errors in derivation. Our paper's math error and mislabeled experiments are worse. The 2.5 anchor (1NYhrZynvC) had more confused theory; our paper is cleaner but still flawed. Score 3.0.

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>