# Learning to Solve Differential Equation Constrained Optimization Problems

- Decision: Accept
- Scores: 8, 8, 6

## Abstract
Differential equations (DE) constrained optimization plays a critical role in numerous scientific and engineering fields, including energy systems, aerospace engineering, ecology, and finance, where optimal configurations or control strategies must be determined %identified
for systems governed by ordinary %(ODE) 
or stochastic %(SDE)
differential equations. Despite its significance, the computational challenges associated with these problems %, including high dimensionality and the nonlinearity of DEs, 
have limited their practical use. %efficiency and precision 
To address these limitations, this paper introduces 
a learning-based approach to DE-constrained optimization  
that combines techniques from \emph{proxy optimization} \cite{kotary2021end} and \emph{neural differential equations} \cite{kidger2022neural}. The proposed approach uses a dual-network architecture, with one approximating the control strategies, focusing on steady-state constraints, and another solving the associated DEs. %our approach ensures that optimal solutions can be approximated while also considering dynamic constraints, in near real-time.
This combination enables the approximation of optimal strategies while accounting for dynamic constraints in near real-time.
Experiments across problems in energy optimization and finance modeling show that this method provides full compliance with dynamic constraints and it produces results up to 25 times more precise than other methods which do not explicitly model the system's dynamic equations.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In this paper the authors propose a dual learning approach for solving differential equation-based optimization problems, relevant to dynamic optimization and systems control. The authors present a financial and a power-grid case study, showcasing the accuracy and speed of their proposed method. The method includes several novel aspects and its applicability is well-motivated by the authors.

### Strengths
- Well-written paper, well organized and well-motivated.
- The selected case studies are important, challenging and sufficient to show the effectiveness of the proposed approach. 
- Authors have done a lot of interesting and relevant work, presenting many more comparisons and discussion in the Appendices.

### Weaknesses
Related works section: 
- This work is relevant to control applications, which is a really rich area with respect to literature. The Reviewer realizes that it would be impossible to review all of it, but some statements and key relevant areas could be better represented. Several questions on this have been added to the Questions section. 
- The motivation includes stochastic DE constrained optimization, which is not shown in results, rather briefly mentioned in Appendix A. The discussion provided in Appendix A is not sufficient to justify that this could extend to stochastic opt, which comes with more challenges. 
- The authors only solve up to a 57-bus system, which is a benchmark problem in power systems optimization. Real problems are much larger than this. The authors should discuss scalability of proposed method and challenges in each step as number or nodes, variables, constraints increases. 
- The authors use a local optimizer to generate data, ensuring near-optimal solutions are used to warm-start the solver. The sensitivity of the method to this is not discussed.

### Questions
- In the Related Works section, the authors do not mention collocation-based or differential algebraic programming (DAE), although these are mentioned later in the results/discussion section. How do these methods compare to proposed approach, why are they relevant?
- How does "multiparametric programming" (which is a field related to MPC, developed to identify "maps" of control actions under different parametrizations, for which authors have also previously used surrogate models) compare to proposed approach? 
- Finally, the authors mention that DE-optimization problems involve parametrization of the state variables, and thus traditional MPC is unsuitable. This statement must be made more clear because it is a little misleading. What is traditional MPC and why is it unsuitable? Due to implementation or computational cost concerns?
- How would the method steps (training for Fw, training for Nθ), using Langrangian approach scale for larger grid systems? Please discuss this in your conclusions. 
- How critical is it to the method to have near-optimal guesses to solve the optimization problem with IPOPT? Would this ever become an issue for larger systems? 
- For both surrogate models trained, what is the trade-off between training sample diversity (covering the entire space) vs. optimality (samples being close to optimal regions) for accuracy and constraint violation of the overall method?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes a novel method for solving optimization problems constrained by differential equations (DEs). This method combines neural networks with a proxy optimization model, employing a dual-network architecture: one network approximates control strategies, while the other solves the differential equations related to these decisions. Experiments have validated the effectiveness of this method in fields such as financial modeling and energy optimization. Compared to traditional proxy optimization methods, this approach shows higher accuracy when handling high-dimensional dynamic constraints.

### Strengths
1.	The writing is clear and well-structured, making complex concepts accessible.
2.	The methodology is rigorous and well-executed, with robust experiments that provide reliable results.
3.	The authors provide thorough comparisons with existing optimization methods, demonstrating significant performance improvements.

### Weaknesses
1.	The authors do not adequately address potential limitations or challenges faced when applying their method in practice.
2.	The absence of diagrams or flowcharts makes complex concepts challenging to follow. Adding a diagram illustrating the dual-network architecture, particularly the interaction between the proxy optimization model F_\omega  and the solver N_\theta significantly improves understanding.


### Questions
1. Does the dual-network architecture need to consider synchronization issues during training? When one network changes, can the other network quickly adjust to adapt to the new state?
2. The authors have not sufficiently addressed the practical challenges of applying their method. Key aspects such as computational resource requirements, scalability to larger systems, and performance in the presence of noisy or incomplete data require comprehensive discussion.
3. The paper does not specify the numerical solvers used for comparison. In equations (3a) and (3b), where N_\theta approximates the evolution of state variables, how does the performance of the neural network solver compare to traditional numerical solvers like Runge-Kutta or Euler methods? A comparison focusing on accuracy, efficiency, and convergence is needed for completeness.
4. The loss function integrates the optimization of state and control variables, but how are the contributions of these two networks balanced?
5. The proposed network should discuss its numerical stability during the solving process, especially in cases where F is a highly nonlinear or stiff equation. How does the network avoid issues of gradient explosion or vanishing?
6. The discussion on Neural ODE in the abstract should include a reference to the paper by Chen et al. (2018) titled "Neural Ordinary Differential Equations," presented at NeurIPS, to provide necessary background and support for the proposed method.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces the Differential Equation Optimization Proxy (DE-OP) for solving differential equation (DE)-constrained optimization problems. The major contribution is a proposed primal-dual framework to ensure constraint satisfaction while allowing end-to-end differentiation. Experiments on several real-world background optimization problems show that the DE-OP achieves improvements in solution stability compared with existing static methods.

### Strengths
* The paper is well-structured and presented in a clear academic style. 
* The experiment results demonstrate that the DE-OP can be 25 times faster than existing methods, which is a great improvement. 
* Benchmarks are chosen as some real-world scenarios (AC-Optimal power flow optimization and dynamic portfolio optimization), which are beneficial for actual applications.
* The constrained optimization with differential equations is quite important for real-world control problems.

### Weaknesses
 * Contribution 2 appears to be more of a methodological explanation of DE-OP rather than a clear, original contribution. Clarifying its novelty could help highlight its value within the paper. 
* The description of the challenges addressed by DE-OP could be more specific. Currently, DE-OP mentions a wide range of problems such as NP-hard, high dimensionality, and nonlinearity that are common to many “learning-to-optimize” frameworks. A detailed description of the unique challenges faced by DE-OP would make the problem more specific.
* The proposed DE-OP is similar to many existing optimal control networks, such as the actor-critic model. Provide more details and comparisons between them or at least discuss the differences between DE-OP with neural networks for solving differential equations. 
* For equation (6), when L^{DE-OP} is minimized, how does DE-OP ensure constraint satisfaction? This is not explained in the main text, and Appendix C.1 only deals with the proxy optimizer approach, leaving this key detail ambiguous.
* In the experimental setting, baselines focus on “steady-state” aspects, raising questions about whether these baselines can effectively address the problem as formulated in Equation (1). This focus also raises potential fairness concerns in the comparison. Authors could either justify their choice of baselines more thoroughly, or include additional baselines that are more directly comparable to DE-OP in terms of handling dynamic aspects of the problem.
* The results in Table 1 do not strongly support DE-OP's superiority over baselines, as only stability violations are minimized, while other metrics do not place DE-OP even as the second-best method.  Please provide more context or discussion around these results. For example, you could explain why minimizing stability violations is particularly important in their problem setting or discuss the trade-offs between different performance metrics.

### Questions
* Is the upper bound on the number of points a typo? It seems should be T rather than \top
* It is hard to follow the paragraph "Optimizing over the distribution of instances". Why are the parameters \zeta used as input of the neural network? 
* How is the dataset D acquired for the experiment?
* Why is DE-OP compared to LSTM models in the experiments? Recurrent neural networks are generally unsuitable for DE-constrained optimization, so the rationale behind this comparison is unclear. Provide a clear justification for including LSTM models in the comparison. If there's a specific reason for this choice, please explain it.

### Soundness
2

### Presentation
3

### Contribution
2
