---
job_id: c05814a8-d216-43d9-a291-159a8f45fc52
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: O6n4dgTBBL.pdf
paper: Stabilizing Gradient Descent via Second-Order Control-Theoretic Dynamics
main_score_norm: 0.2
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, specifically optimization, learning theory, and control-theoretic analysis of gradient-based training dynamics.

## Minimum Quality
Pass ✅. The paper includes the expected research components, including abstract, introduction, related work, technical development, experiments, results discussion, and conclusion; although there are substantial correctness and clarity issues, they are better handled in full review than as a desk-reject criterion.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, reviewer-targeting instructions, or suspicious manipulative text in the provided paper content.

# Expected Review Outcome:
## Summary
This paper studies gradient descent through a continuous-time dynamical-systems lens. Starting from gradient flow, the authors differentiate once more to obtain a second-order ODE, analyze local stability through the Jacobian spectrum, and then introduce a linear controller of the form $u=-K_1\theta-K_2\dot\theta$ to stabilize the resulting dynamics. They further derive a modified update rule called controlled gradient descent (CGD), and evaluate it on a few low-dimensional synthetic objectives with different curvature profiles and learning rates.

## Strengths
The paper has a clear high-level goal, namely to connect optimization stability with tools from control theory and to propose an explicit stabilizing modification. This is a relevant topic for ICLR, especially given the continuing interest in edge-of-stability phenomena and dynamical-systems views of optimization.

I also appreciate that the paper tries to keep the technical story concrete. In particular, the block Jacobian in **Equation (3)** and the quadratic eigenvalue formulation in **Section 5** make it relatively easy to see what the authors are trying to control, namely the spectrum of a linearized second-order system. Even though I have important concerns about the correctness and interpretation, the intended mechanism is understandable.

The synthetic figures do help communicate the intended behavior. For example, **Figure 1** gives an immediate visual comparison between vanilla GD and the proposed controlled dynamics on a simple quadratic, and **Figure 3** is useful in showing the authors’ intended claim that the controller enlarges the stable learning-rate region around the classical threshold. Similarly, **Figure 2(d)-(f)** presents loss curves under several curvature choices, which at least gives some empirical evidence that the modified update can damp oscillatory or divergent trajectories in toy problems.

Finally, **Table 1** is useful as a compact statement of the paper’s claimed theoretical message. Even though I disagree with parts of that message, the table does make the paper’s stance explicit: the authors are claiming ordinary GD is at best Lyapunov stable under strong convexity in their continuous-time formulation, while their controller yields local asymptotic stability without curvature restrictions. Having the claims laid out this explicitly makes the paper easier to interrogate.

## Weaknesses
I have major concerns about the technical core of the paper. Unfortunately, these are not cosmetic issues, they directly affect the validity of the main claims.

1. **The central continuous-time reformulation already breaks the usual interpretation of gradient flow and leads to misleading stability conclusions.**  
   In **Section 3**, the paper starts from gradient flow
   $$
   \dot{\theta} = -\nabla L(\theta)
   $$
   and differentiates it to obtain
   $$
   \ddot{\theta} = -H(\theta)\dot{\theta},
   $$
   which is **Equation (2)**. Formally this identity holds along trajectories of gradient flow, but it does **not** define a new independent second-order dynamical system equivalent to gradient descent unless one also enforces the first-order constraint $\dot{\theta}=-\nabla L(\theta)$ for all time. Once the paper treats $(\theta,\dot\theta)$ as a free state in **Equation (3)** with dynamics
   $$
   \dot\theta = x,\qquad \dot x = -H(\theta)x,
   $$
   it has enlarged the state space from the gradient-flow manifold $\{x=-\nabla L(\theta)\}$ to all $(\theta,x)\in\mathbb R^{2n}$. Stability properties of this enlarged system are not the same as stability properties of gradient flow or discrete GD. This is the core conceptual mistake. The zero eigenvalues in the Jacobian arise because the enlarged system contains an entire set of equilibria $(\theta,0)$, not because ordinary gradient flow loses asymptotic stability in the way claimed.  
   Why this matters: many later claims, including **Theorem 2**, inherit conclusions about GD from a system that is not actually GD.

2. **The paper’s claim that strongly convex gradient flow is only Lyapunov stable, not asymptotically stable, is incorrect as stated.**  
   In **Page 5**, the discussion after **Theorem 2** concludes that under strong convexity the first-order system is only locally Lyapunov stable because the Jacobian has $n$ zero eigenvalues. But for standard gradient flow near a strict minimizer, the equilibrium is asymptotically stable under standard conditions; indeed linearizing $\dot\theta=-\nabla L(\theta)$ at $\theta^\*$ gives Jacobian $-H(\theta^\*)$, whose eigenvalues are strictly negative when $H(\theta^\*)\succ 0$. The paper’s weaker conclusion comes entirely from analyzing the augmented system in **Equation (3)** rather than the original gradient flow.  
   This is not a subtle interpretational disagreement, it overturns the paper’s headline contrast between “original GD” and the controlled version in **Table 1**. If the baseline stability claim is misstated, the table is not a reliable summary of the theory.

3. **The stability classification for the convex-but-not-strongly-convex case is overclaimed and partly wrong.**  
   In **Section 4.2.2**, the paper argues that if $H\succeq 0$ but has at least one zero eigenvalue, then the algebraic multiplicity of $\lambda=0$ exceeds the geometric multiplicity, so a Jordan block larger than $1\times 1$ must exist, hence instability follows. This reasoning is too quick and, in general, not established. The characteristic polynomial alone,
   $$
   \prod_{i=1}^n \lambda(\lambda+\lambda_i),
   $$
   does not by itself prove the defective Jordan structure claimed. The authors would need to explicitly characterize the Jordan form of
   $$
   J=\begin{bmatrix}0&I\\0&-H\end{bmatrix}
   $$
   when $H$ is singular. Some defective behavior may indeed occur, but the proof presented is not sufficient.  
   Why this matters: **Theorem 2** relies on this case distinction, and the paper uses it to motivate the need for the controller.

4. **The controller analysis proves stability of a different linearized system, not of the proposed optimization algorithm.**  
   In **Section 5**, the controlled dynamics are introduced as
   $$
   \ddot{\theta}' = -H(\theta)\dot\theta + u,\qquad u=-K_1\theta-K_2\dot\theta,
   $$
   and **Theorem 3** concludes local asymptotic stability from a quadratic eigenvalue argument. But this again analyzes the augmented second-order system, not the original gradient flow nor the actual discrete-time algorithm in **Algorithm 1**. The theorem therefore does not establish what the title suggests, namely stabilization of gradient descent itself. At most, it establishes a property of a particular controlled second-order ODE under assumptions such as $H(\theta)+K_2\succ0$.  
   The gap between this theorem and the optimization claim is acknowledged only briefly in the limitations, but in the main text the conclusions are phrased much more strongly than justified.

5. **Equation (5) is mathematically problematic and appears incorrectly integrated.**  
   The derivation in **Page 7** states
   $$
   \frac{d\theta'}{dt}=\int \frac{d^2\theta'}{dt^2}dt=\frac{d\theta}{dt}-\frac12K_1\theta^2-K_2\theta.
   $$
   This is not correct in vector/matrix form as written. If $u=-K_1\theta-K_2\dot\theta$, then integrating $u$ over time gives
   $$
   \int u\,dt = -\int K_1\theta(t)\,dt - K_2\theta(t) + C,
   $$
   not $-\frac12K_1\theta^2-K_2\theta$ in general. The expression $-\frac12K_1\theta^2$ is only suggestive of scalar integration of $\theta\,d\theta$, not time integration of $\theta(t)\,dt$, and it is especially dubious when $K_1$ is a matrix. There is also an omitted integration constant.  
   This is a serious issue because **Equation (5)** is exactly what the paper uses to derive the practical optimization rule in **Algorithm 1**. If the derivation is invalid, the proposed algorithm is not theoretically connected to the preceding control analysis.

6. **Algorithm 1 is underspecified and inconsistent with the preceding notation.**  
   The algorithm computes
   $$
   g_t=\frac{1}{|\mathcal B|}\sum_{(x_i,y_i)\in\mathcal B}\big(\nabla_\theta L(\theta_t;x_i,y_i)-K_1\theta_t^2-K_2\theta_t\big),
   $$
   then applies a standard GD step. Several problems appear here. First, the notation mixes the control term into the minibatch average as if it were sample-dependent, although it is not. Second, the control analysis was stated in continuous time in terms of $\dot\theta$ and $\ddot\theta$, but the algorithm contains no velocity state and no discretization of the second-order dynamics. Third, if $K_1$ and $K_2$ are matrices as in **Definition 4**, then the use of elementwise $\theta_t^2$ is inconsistent unless a diagonal restriction is imposed.  
   Why this matters: the paper presents Algorithm 1 as the practical realization of the theory, but the mapping from theorem to algorithm is not coherent.

7. **The paper repeatedly conflates continuous-time gradient flow with discrete-time gradient descent.**  
   The introduction opens with discrete GD, but the technical development in **Sections 3 to 5** is purely continuous time, and the conclusions are often phrased as if they directly characterize discrete GD. For example, the abstract says “the sign of the real parts of the Hessian’s eigenvalues directly governs the convergence behavior of gradient-based optimization,” which is far too broad. In continuous-time gradient flow, a positive-definite Hessian near a minimizer implies asymptotic decay of the linearization; in discrete-time GD, stability depends on the step size through factors like $1-\eta\lambda_i$. These are not interchangeable.  
   The paper does mention a “gap” in **Section 8**, but this is much too mild relative to how central the gap is. The main claims are framed as statements about gradient descent, while the proofs are about a different continuous-time controlled system.

8. **The empirical section is too narrow to support the claimed generality, and even some examples are poorly aligned with the theory.**  
   All experiments in **Section 7** are low-dimensional synthetic functions. There is no neural network experiment, despite the framing throughout the paper around training neural networks and “general loss landscapes.” Given the ambitious claims, this is a very thin empirical basis. Moreover, the “convex but not strongly convex sphere” in **Page 8** is given as $L(\theta)=\theta_1^2+\theta_2^2$, which is actually strongly convex, not merely convex. That is a surprisingly basic classification error and undermines confidence in the experimental setup.  
   Looking at **Figure 2**, the trajectories and loss curves show that the proposed method damps motion on selected toy problems, but that is much weaker than validating a general stabilization method for GD. If the authors want to sell this as a practical optimizer, at minimum I would expect comparisons on standard ML objectives and against stabilization-oriented baselines.

9. **The results are qualitative and lack proper quantitative benchmarking or meaningful baselines.**  
   The paper has only one explicit table, **Table 1**, and it is a theory-summary table rather than an experimental results table. There is no quantitative benchmark table comparing final loss, convergence rate, stability region, or sensitivity to hyperparameters across methods. This is a major omission because the practical contribution is an optimizer. The empirical section compares only against vanilla GD, while omitting obvious baselines such as momentum, damped heavy-ball variants, proximal regularization, or other control-inspired optimization methods.  
   Why this matters: even if the toy figures suggest some stabilization, it is impossible to judge whether the proposal is competitive, distinct, or merely acting like a crude regularizer.

10. **The literature positioning is incomplete for a paper making strong control-theoretic novelty claims.**  
   The related-work discussion cites classic optimization and edge-of-stability papers, but for a submission centered on “controlled gradient descent” and control-theoretic stabilization, the positioning feels underdeveloped. There is little engagement with recent work that also studies optimization through control-theoretic or Lyapunov/passivity frameworks, or that explicitly adds feedback/control terms to gradient dynamics. As written, the paper overstates the impression that no theoretically characterized stabilization methods exist.  
   This matters because the paper’s novelty is not just “we add a stabilizing term,” but “we do so from a control-theoretic second-order perspective.” That claim needs sharper differentiation.

11. **Some exposition is simply too loose for a theory paper.**  
   There are many local issues: the smoothness definition in **Page 1** appears malformed, notation alternates between $\theta$ and $\bm\theta$ and between $x$ and $\dot\theta$, “convex but not strongly concave” in **Theorem 2** is presumably meant to be “concave” or “non-convex/indefinite,” and several grammar issues obscure precise meaning. These are not my main objection, but they compound the difficulty of assessing the technical claims. For a paper whose contribution is mainly theoretical, this level of imprecision is a real problem.

12. **The figure and table evidence sometimes undercuts, rather than strengthens, the stated claims.**  
   **Figure 1(c)** shows CGD and standard GD having very similar early loss behavior on the quadratic example before standard GD plateaus at a higher loss, which is consistent with added damping but does not on its own demonstrate the claimed “higher tolerance on learning rate” in a principled sense. **Figure 3** does suggest better behavior near $\eta=1$, but because the controlled method introduces extra terms, this is not an apples-to-apples statement about GD stability bounds unless the induced objective or effective dynamics are analyzed. Likewise, **Table 1** states that original GD is not asymptotically stable even in the strongly convex case, which is exactly the kind of claim that should trigger more caution rather than serve as a clean summary.

Overall, the paper has an interesting instinct, but the current version overclaims, analyzes the wrong dynamical object, and derives the practical algorithm through a mathematically invalid step. Those are core issues, not polish issues.

## Questions
1. The most important point for rebuttal is conceptual: can the authors precisely explain in what sense the enlarged system in **Equation (3)** is equivalent to gradient flow or discrete GD? If the answer is “only along trajectories satisfying $x=-\nabla L(\theta)$,” then how should the stability conclusions in **Theorem 2** be reinterpreted?

2. Can the authors provide a corrected derivation of **Equation (5)**? In particular, how do they justify
   $$
   \int -K_1\theta(t)\,dt = -\frac12 K_1\theta^2
   $$
   in vector form, and where is the integration constant handled? If this step is not valid, what is the principled derivation of **Algorithm 1** from the controlled ODE?

3. What exactly is the equilibrium set of the augmented system? Since $(\theta,0)$ is an equilibrium for any $\theta$ in **Equation (3)**, how should one interpret “stability toward the optimum” versus stability toward an arbitrary zero-velocity state? A rebuttal that clarifies this geometry would substantially improve confidence.

4. Can the authors correct the experimental labeling of the “convex but not strongly convex sphere” in **Section 7.1**? As written, $L(\theta)=\theta_1^2+\theta_2^2$ is strongly convex. If a non-strongly-convex example was intended, please state it clearly and explain whether the conclusions change.

5. To support the optimization claim, could the authors provide at least one experiment on a standard ML model, plus comparisons with more meaningful baselines than plain GD, such as momentum/heavy-ball, Nesterov, damped second-order updates, or regularized variants? That evidence would materially affect my confidence in the practical significance.

6. The condition in **Definition 4** requires choosing $K_2$ such that $H(\theta)+K_2\succ0$, potentially for all $\theta$. How is this implemented in practice without access to the full Hessian or a global curvature bound, especially for nonconvex neural-network losses? A concrete recipe is needed.

7. Please sharpen the claims around “gradient descent can diverge even in simple convex settings” in the abstract and conclusion. Is this meant for the augmented second-order system, for continuous-time gradient flow, or for discrete GD with a large step size? These are very different statements.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
None.

## Soundness Rating
1: poor. The main technical claims are not adequately supported because the analysis studies an augmented second-order system that is not equivalent to GD, and the derivation of the actual algorithm via **Equation (5)** appears mathematically incorrect.

## Presentation Rating
2: fair. The paper is readable at a high level and the figures help, but the exposition is too imprecise for a theory-driven submission, with multiple notation issues, incorrect curvature labels, and overstatements that blur what is actually proved.

## Contribution Rating
1: poor. The control-theoretic framing is potentially interesting, but in its current form the paper does not establish a reliable theoretical or empirical contribution to optimization beyond toy demonstrations.

## Overall Rating
2: Reject, not good enough. The paper has an interesting motivation and some intuitive toy visualizations, but the central analysis is built on a problematic reformulation, the practical algorithm is derived through an invalid integration step, and the experiments are too limited to rescue the contribution.

## Reviewer Confidence
4: confident. I am confident in this assessment and carefully checked the core equations and the logic connecting the continuous-time analysis to the proposed algorithm.