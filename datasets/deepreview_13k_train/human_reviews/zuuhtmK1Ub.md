# Differentiable Implicit Solver on Graph Neural Networks for Forward and Inverse Problems

- Decision: Reject
- Scores: 3, 1, 3, 1

## Abstract
Partial differential equations (PDEs) on unstructured grids can be solved using message passing on a graph neural network (GNN). Implicit time-stepping schemes are often favored, especially for parabolic PDEs, due to their stability properties. In this work, we develop a fully differentiable implicit solver for unstructured grids. We evaluate its performance across four key tasks: a) forward modeling of stiff evolutionary and static problems; b) the inverse problem of estimating equation coefficients; c) the inverse problem of estimating the right-hand side; and d) graph coarsening to accelerate forward modeling. The increased stability and differentiability of our solver enable excellent results in reducing the complexity of forward modeling and efficiently solving related inverse problems. This makes it a promising tool for geoscience and other physics-based applications.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces a novel framework that combines graph neural networks with the finite volume method, to address implicit schemes. (There was a challenge that differential equation solvers typically avoid due to the additional computation complexity of handling implicit equations.)

### Strengths
By employing an implicit scheme with optimized gradient computation, the proposed method reduces the required number of time steps. 
They present a differentiable framework for both forward and inverse methods, enabling a learnable numerical approach based on discrete time steps. 
Additionally, the paper explores applications in inverse problems, often employing irregular unstructured grids as used in practical scenarios.

### Weaknesses
While the underlying idea is promising, the paper would benefit from stronger experimental or theoretical justification for the proposed methodology. Additional clarity and motivation for the approach would enhance the paper’s impact.

While the authors discuss the limitations of automatic differentiation in JAX in line 74, further elaboration on the specific computational bottlenecks would improve the motivation for this approach. For instance, detailing the memory consumption or computational time scaling with problem size would be beneficial.

Graph neural networks are frequently used to manage unstructured grid points. Since the paper emphasizes integration with the finite volume method with its local conservation property in line 58, it would be beneficial to include experiments validating these conservation properties, such as demonstrating mass or energy conservation within the simulation.

Equation (12) appears to involve matrix inversion on the right-hand side of the proposed gradient formulation. Could the authors address whether this matrix inversion contributes to computational costs, comparable to previous methods? Specifically, a discussion on the sparsity of the matrix and the implications for inversion complexity would be valuable.

In Equations (12) and (13), gradient computations are proposed. An alternative approach might involve solving the implicit equation through optimization techniques commonly used in deep learning, such as constructing a minimization problem for Equation (5) combined with a data loss function, potentially avoiding matrix inversion. Could the authors discuss this approach, including potential challenges such as convergence issues or local minima?

While the finite volume method can accommodate various boundary conditions, the paper considers only Neumann boundary conditions. Is there a specific reason for this choice? Exploring the method's performance with other boundary conditions, such as Dirichlet or mixed conditions, would broaden the scope of the work.

In line 253, the authors claim lower computational costs for their method than the explicit Euler scheme, which requires smaller time steps. Could the authors provide a detailed comparison of the computational cost per each time step, including the cost of gradient computation, to support this claim? A breakdown of the computational complexity for each step would be helpful.

In Figure 2, the initial scale of the loss is relatively high, making it difficult to assess whether the loss converges to zero after 160 epochs. Given that a coarser grid, intended to reduce computation, may negatively impact estimation accuracy even if the loss function converges to zero, a guideline for determining sufficient loss minimization would be beneficial. For example, a discussion of the relationship between grid resolution and convergence criteria would be useful.

In Figures 3 and 4, the recovered permeability only captures general trends rather than precise values. However, the proposed method in (c) accurately approximates the true data distribution, which suggests that the problem may be inherently ill-posed, where the coefficient may not be unique in this setting. Could the authors clarify whether this issue arises from the problem or the numerical method? A discussion of the identifiability of the inverse problem would be relevant.

All experiments utilize a large number of data points, which may facilitate finding a solution. Additional experimental results with fewer grid points would strengthen the paper. This would help demonstrate the robustness of the method in data-scarce scenarios.

### Questions
1. In line 74, the authors discuss the limitations of automatic differentiation in JAX. Further elaboration on this limitation would improve the motivation for this approach.

2. Graph neural networks are frequently used to manage unstructured grid points. Since the paper emphasizes integration with the finite volume method with its local conservation property in line 58, it would be beneficial to include experiments validating these conservation properties. 

3. Equation (12) appears to involve matrix inversion on the right-hand side of the proposed gradient formulation. Could the authors address whether this matrix inversion contributes to computational costs, comparable to previous methods?

4. In Equations (12) and (13), gradient computations are proposed. An alternative approach might involve solving the implicit equation through optimization techniques commonly used in deep learning, such as constructing a minimization problem for Equation (5) combined with a data loss function, potentially avoiding matrix inversion. Could the authors discuss this approach?

5. While the finite volume method can accommodate various boundary conditions, the paper considers only Neumann boundary conditions. Is there a specific reason for this choice?

6. In line 253, the authors claim lower computational costs for their method than the explicit Euler scheme, which requires smaller time steps. Could the authors provide a detailed comparison of the computational cost per each time step to support this claim?

7. In Figure 2, the initial scale of the loss is relatively high, making it difficult to assess whether the loss converges to zero after 160 epochs. Given that a coarser grid, intended to reduce computation, may negatively impact estimation accuracy even if the loss function converges to zero, a guideline for determining sufficient loss minimization would be beneficial.

8. In Figures 3 and 4, the recovered permeability only captures general trends rather than precise values. However, the proposed method in (c) accurately approximates the true data distribution, which suggests that the problem may be inherently ill-posed, where the coefficient may not be unique in this setting. Could the authors clarify whether this issue arises from the problem or the numerical method?

9. All experiments utilize a large number of data points, which may facilitate finding a solution. Additional experimental results with fewer grid points would strengthen the paper.

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
3

### Summary
The work considers mesh coarsening, forward, and inverse problems and investigates the implicit solver. In the numerical experiments, the authors evaluated the performance of the method regarding each problem.

### Strengths
* The work tries to build a framework that works with mesh coarsening, forward, and inverse problems.

### Weaknesses
 * The novelty of the work is limited. Incorporating FVM into GNN is not new and considered in, e.g., [Jessica et al. ICML 2024 https://arxiv.org/abs/2311.14464 ] and [Horie et al. ICML 2024 https://arxiv.org/abs/2405.16183v1 ]. The construction of gradients presented in Section 2.3 seems strongly related to the adjoint method, which is a standard way to deal with inverse problems. The implicit method for GNN is considered in the area of implicit GNNs, e.g., [Gu et al. NeurIPS 2020 https://arxiv.org/abs/2009.06211 ]. The authors state that these are their novelty, but there is existing work for each. The authors should cite these works and clarify the added novelty from the authors.
* The evaluation is weak. There is only one baseline for the experiment in Section 3.2 and nothing for the ones in Section 3.3 and 3.4. With the current form, the reviewer cannot asses the effectiveness and superiority of the model.
* The presentation is not clear. The figure may miss the labels (a), (b), and so on for Figures 2, 3, and 4. It is not clear what is "data 1", "fitting 1", "data 2", and "fitting 2" in Figures 2 and 3.

### Questions
* What would be the limitation of the method?
* What would be the potential benefit of using machine learning for linear PDE over classical methods?

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes an integrated approach for solving forward and inverse problems by creating a new pipeline that combines Graph Neural Networks (GNNs) with Finite Volume Methods (FVM) to enable automatic differentiation with implicit-time stepping.

### Strengths
Figure 1 effectively illustrates the overall pipeline, demonstrating experimental results that apply the combination of GNN and FVM to both forward and inverse problems.

### Weaknesses
First and foremost, the paper feels incomplete. The biggest concern is the lack of discussion about other approaches that use GNNs or integrate FVM with deep learning to solve PDEs. A “Related Work” section should be added to explain how the proposed model differs from recent studies and highlight its novelty. Although Section 2 on theory explains the problem setup to some extent, more detailed steps and methods for training the proposed approach should be included. Section 3, the experimental part, merely lists the results for forward and inverse problems without discussing how this method compares to existing GNN- and FVM-based approaches. For instance, the study "Learning to Solve PDE-constrained Inverse Problems with Graph Networks" solves inverse problems using GNNs—how does the proposed method differ from this approach, and what advantages does it offer? Experimentally, does it outperform in solving inverse problems? The paper also lacks a discussion on the computational cost of the proposed method, specifically regarding the implicit time-stepping scheme and the need to solve a linear system at each step. The practical implications of this cost should be addressed, especially when compared to explicit methods or other GNN-based approaches. Furthermore, the choice of the stabilizer S(theta) is not sufficiently justified, and the paper should elaborate on how this choice affects the solution and how it is selected for different problems. Finally, the experimental section lacks a thorough analysis of the sensitivity of the method to various hyper-parameters, which is crucial for practical application.

### Questions
* Why should we only consider the Neumann boundary in equation (1)? Is it difficult to consider other Robin boundaries?

* I don't understand the role of R in equation (4). What does it mean as a measurement operator?

* Does S(theta) change depending on the equation of the PDE to be solved? Can you explain this further?

* In equation (8), we need to find A^{-1} in the end. Isn't the cost for this large?

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
3

### Summary
This paper explores the use of graph neural networks for solving forward and inverse problems and particularly focuses on the incorporation of implicit solver. However, the writing is subpar and the procedures and advantages are not well explained. The experiments are also lack comparison with other methods.

### Strengths
The question is interesting and combining GNN with finite element method seems natural.

### Weaknesses
1. The writing is subpar. There are many typos and grammatical errors. For example, "Compute $\nabla_bL$  with (12), whats is equivalent so the solution of a single linear system." should be "Compute $\nabla_bL$ with (12), which is equivalent to solving a single linear system."
2. One main focus of this paper is the incorporation of implicit solver. However, using an iterative solver and in a deep learning setting is well-studied in the Deep Equilibrium Models (DEQ) literature. The authors should compare their method with DEQ.
3. The experiments are not very convincing. The results in Section 3.4 is very poor and in no experiments the authors compare their method with other methods.

### Questions
See weakness

### Soundness
2

### Presentation
1

### Contribution
1
