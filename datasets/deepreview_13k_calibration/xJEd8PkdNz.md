# Impact of Computation in Integral Reinforcement Learning for Continuous-Time Control

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 6, 8

## Abstract
Integral reinforcement learning (IntRL) demands the precise computation of the utility function's integral at its policy evaluation (PEV) stage. This is achieved through quadrature rules, which are weighted sums of utility functions evaluated from state samples obtained in discrete time. Our research reveals a critical yet underexplored phenomenon: the choice of the computational method -- in this case, the quadrature rule -- can significantly impact control performance. This impact is traced back to the fact that computational errors introduced in the PEV stage can affect the policy iteration's convergence behavior, which in turn affects the learned controller. To elucidate how computation impacts control, we draw a parallel between IntRL's policy iteration and Newton's method applied to the Hamilton-Jacobi-Bellman equation. In this light, computational error in PEV manifests as an extra error term in each iteration of Newton's method, with its upper bound proportional to the computational error. Further, we demonstrate that when the utility function resides in a reproducing kernel Hilbert space (RKHS), the optimal quadrature is achievable by employing Bayesian quadrature with the RKHS-inducing kernel function. We prove that the local convergence rates for IntRL using the trapezoidal rule and Bayesian quadrature with a Matérn kernel to be $O(N^{-2})$ and $O(N^{-b})$, where $N$ is the number of evenly-spaced samples and $b$ is the Matérn kernel's smoothness parameter. These theoretical findings are finally validated by two canonical control tasks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the impact of computation methods (quadrature rule for solving integrals) when applying reinforcement learning in continuous control tasks. Building upon the connections between HJB equation and Newton's method, the authors show that the computation error is an extra error term in each iteration of Newton's method. With the bounded error assumption, they provide a convergence results for Newton's methods with an extra error term (Theorem 1). Furthermore, the computation error bounds are also discussed by minimizing the worst case error under different quadrature rules and kernels. Finally, an end to end convergence result is provided (Theorem 3, Corollary 1).

### Strengths
This paper is well written and easy to follow. The problem of studying the impact of computational errors on continuous control in integral RL is well motivated and interesting. As the authors claim, this problem is widespread but understudied.

### Weaknesses
This paper is well written and easy to follow. The problem of studying the impact of computational errors on continuous control in integral RL is well motivated and interesting. As the authors claim, this problem is widespread but understudied.

However, the paper appears to rely heavily on existing results. Specifically, the convergence analysis of Newton's method with an extra error term and the error bound analysis on the computation step seem to be directly adapted from prior work. While the combination of these results in the context of integral reinforcement learning (IntRL) is novel, the paper lacks a clear articulation of the new techniques or insights developed to achieve this synthesis. A more detailed discussion of the novel analytical tools employed would strengthen the paper's contribution. For instance, what modifications were made to the existing convergence analysis to accommodate the specific challenges of IntRL, such as the absence of a discount factor? Furthermore, the reliance on affine nonlinear systems seems restrictive. A discussion on the potential for extending the analysis to a more general class of systems would be valuable. The assumptions of Theorem 2 also need further elaboration. Specifically, what properties of the system functions $f$, $g$, and the cost function $J$ are required to guarantee these assumptions? Providing concrete examples or sufficient conditions for these assumptions to hold would enhance the practical applicability of the theoretical results.

Finally, the experimental validation is limited to low-dimensional examples (3D linear and 2D nonlinear systems). While these serve as useful initial demonstrations, they do not fully reflect the challenges of high-dimensional, real-time applications. A more comprehensive evaluation involving higher-dimensional systems is needed to demonstrate the practical significance of the proposed approach. Analyzing how the computation error and convergence behavior change with increasing dimensionality would provide valuable insights into the scalability of the method.

### Questions
1. Are the affine nonlinear systems necessary? Can you consider a more general class of systems?  
2. The assumptions of Theorem 2 need more explanations. To guarantee those assumptions, what properties do you need for the systems functions $f$, $g$, and cost function $J$?
3. The experimental examples are basically toy examples (3d linear system and 2d nonlinear system). These are far from high-dimensional real-time applications. How the computation error and convergence will behave in higher dimensional cases need to be examined.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the continuous time RL and provides a detailed convergence rate discussion on the impact of policy iteration's computation errors when approximating the integration in the policy evaluation step. By showing that PI can be viewed as Newton updates and PI with computation errors can be viewed as Newton updates with errors, this paper established local convergence rates and uses simulation to demonstrate the tightness of the order of the convergence rate.

### Strengths
The paper is very well written. Even though I am not an expert in this area, the detailed motivation and the clear illustration diagrams help me understand the importance of this problem and the key ideas behind the proofs. The connection between Newton updates and PI, and using approximate Newton to analyze PI with computation errors are also fascinating. Further, the proofs are quite involved too. Lastly, the numerical results demonstrate the tightness of the order of the convergence rate with respect to N.

### Weaknesses
See below.

### Questions
Q1: In Theorem 3, the computation error is treated as a constant value. How does this constant decay with the number of samples? 

Q2: Corollary 1 assumes that $i \to +\infty$. By using the decay rate of the computation error in Theorem 1, can the authors comment on a more realistic convergence rate based on different number of iterations $i$? Further, can the theoretical results provide some guidelines on how to choose the number of iterations to terminate at?

Q3: How does this result compare with LSPI, which is also based on a linear combination of basis functions?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper addresses the impact of computational methods on control performance in Integral Reinforcement Learning. The authors focus on the policy evaluation stage of IntRL, where the integral of the utility function needs to be computed using quadrature rules. They demonstrate that computational errors introduced during PEV can significantly influence the convergence behavior of policy iteration and the performance of the learned controller.

The authors show that computational errors in PEV manifest as an extra error term in each iteration of Newton's method. They provide a theoretical analysis, proving that the upper bound of this error term is proportional to the computational error. The paper further explores the case where the utility function resides in a reproducing kernel Hilbert space (RKHS), presenting local convergence rates for IntRL using both the trapezoidal rule and Bayesian quadrature with a Matern kernel.

### Strengths
- The authors demonstrated how computational errors in the PEV stage of IntRL affect the convergence behavior of policy iteration and the performance of the learned controller, which is previously unexplored.
- They also provided a solid theoretical analysis of the impact of computational errors, providing bounds and convergence rates that relate the computational method to control performance.
- Validation of the theoretical findings is also offered through simulations on canonical control tasks, showing the practical implications of the choice of computational method in IntRL.

The paper sheds light on the impact of computational methods on control performance in IntRL, providing both theoretical insights and practical guidelines for improving controller learning in continuous-time reinforcement learning scenarios.

### Weaknesses
 - The paper provides theoretical claims about the impact of computational methods on control performance in IntRL. However, the experimental validation seems to be limited in scope. The authors only consider canonical control tasks to validate their findings. The authors could consider a broader set of experiments, including more complex and real-world scenarios, to showcase the practical implications of their findings.


### Questions
Could you provide more details on the choice of the canonical control tasks used for experimental validation? Were any real-world scenarios or more complex tasks considered?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work investigates the effects of choice of quadrature rules for integral RL; especially when the true dynamics is unknown.
It discusses how the computational error in policy evaluation stage affects each iteration of PI, which is shown to be corresponding to the Newton’s method: theoretically, the work proves the local convergence rates for IntRL; and the findings are validated by some control tasks.
Furthermore, the work shows that the case where the utility function lives in an RKHS as corollary.

### Strengths
1. Conceptually this work may bring up a new research direction of studying the effects of “approximation error” for ODE or problems including integrals in ML field (e.g. for neural ODE).  This is the point I particularly find value in this work.
2. The claims are validated by simple yet informative experiments.

### Weaknesses
1. While CT formulation helps in some analysis or for some applications, it was a bit unclear what the motivations behind studying CTRL if the task can be done with DT formulations.
(Especially when the time interval is even; in which case DT can well manage.)
In particular, for DT and CT systems, there should be different conditions for the solutions to exist.
For contact-rich dynamics for example, this kind of analysis becomes harder for example.
(Does PIM ensures the existence of solutions throughout the whole process?)
Also, for stochastic systems, CT requires more conditions for certain analysis.
2. About approximation error of value functions; if we know the utility lives in certain RKHS, can we say anything about the value function which may validate the assumptions?  At least, there should be a trivial case for this assumption: if you know the value function exactly, that becomes a single basis function; when is it continuously differentiable?  A bit more discussions needed.
(also there is a type (additional “]”) for the interval for the integral value.)
3. In Appendix H; no approach to find a suitable T?  There may require some discussions on how rare the independence property fails for a random T.

### Questions
1. For Appendix G, not only for the figure for the utility itself, a plot for the integral of the utility and the worst case error would be informative too.
2. Are there any answer to the weakness points?

### Soundness
4 excellent

### Presentation
2 fair

### Contribution
3 good
