# PhyMPGN: Physics-encoded Message Passing Graph Network for spatiotemporal PDE systems

- Decision: Accept
- Scores: 8, 8, 6, 10, 8

## Abstract
Solving partial differential equations (PDEs) serves as a cornerstone for modeling complex dynamical systems. Recent progresses have demonstrated grand benefits of data-driven neural-based models for predicting spatiotemporal dynamics (e.g., tremendous speedup gain compared with classical numerical methods). However, most existing neural models rely on rich training data, have limited extrapolation and generalization abilities, and suffer to produce precise or reliable physical prediction under intricate conditions (e.g., irregular mesh or geometry, complex boundary conditions, diverse PDE parameters, etc.). To this end, we propose a new graph learning approach, namely, Physics-encoded Message Passing Graph Network (PhyMPGN), to model spatiotemporal PDE systems on irregular meshes given small training datasets. Specifically, we incorporate a GNN into a numerical integrator to approximate the temporal marching of spatiotemporal dynamics for a given PDE system. Considering that many physical phenomena are governed by diffusion processes, we further design a learnable Laplace block, which encodes the discrete Laplace-Beltrami operator, to aid and guide the GNN learning in a physically feasible solution space. A boundary condition padding strategy is also designed to improve the model convergence and accuracy. Extensive experiments demonstrate that PhyMPGN is capable of accurately predicting various types of spatiotemporal dynamics on coarse unstructured meshes, consistently achieves the state-of-the-art results, and outperforms other baselines with considerable gains.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The work focuses on solving PDE with low-resolution unstructured meshes. In particular, the authors incorporate the discrete Laplace–Beltrami operator to express the diffusion process and a specific padding method to satisfy boundary conditions.

The experimental evaluation demonstrates that the introduced Laplace block (GNN + Laplace Beltrami operator) is strongly expressible to approximate Laplacian compared to the raw numerical scheme and machine learning models considered in the evaluation. In addition, the method has a stable prediction for long-time series prediction with generalization regarding initial condition, boundary condition, and Reynolds number to some extent.

### Strengths
* The numerical experiments are thorough, and the proposed method demonstrates its high performance in various tasks and generalization scenarios. In particular, the method can extrapolate the Reynolds number to some extent, which is impressive.
* The method is simple and easy to understand. Due to its simplicity, the reviewer expects the method to be compatible with other GNN-based methods, which would be solid knowledge to the community.

### Weaknesses
 * The novelty of the proposed method is limited. The connection between GNN and the Laplace (–Beltrami) operator is not new (e.g., baselines in Section 4.1 and [Li et al. AAAI 2018 https://arxiv.org/abs/1801.07606 ]). Since the performance is better than the baseline, there might be a big improvement for the community, but it is unclear what it is. The author could have elaborated on what were the problems of existing methods and how they overcame the difficulties.
* The method to treat boundary conditions in unstructured meshes is also not new and proposed in [Horie et al. NeurIPS 2022 https://openreview.net/forum?id=B3TOg-YCtzo ]. At least the author should mention existing works and possibly compare the proposed method with them to discuss the pros and cons.
* For time-series training, the motivation to incorporate the first step in the loss (Eq 7). As mentioned in the paper, [Brandstetter et al. 2022] proposed a method called the pushforward trick, which computes the loss using only the last time step, demonstrating the trick performs better than adding noise. In the present work, Eq 7 seems to contradict the previous works. Thus, the authors should clarify the reason why they have the first step with noise and demonstrate the proposed one is better.

### Questions
* The method seems quite simple yet powerful, as seen in the numerical experiments. However, the reviewer wonders where the expressibility and generalizability come from. Could the authors explain the reason for high performance, connecting with the method proposed in the paper?
* Is the method generalizable regarding mesh resolution? For instance, learning on coarse meshes and predicting on finer meshes or vice versa would be interesting to see, while that would be out-of-scope of the work.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper is related to PDE systems solution in two-dimensional space on irregular domains. The problem is addressed with the mix of GNNs and classical numerical schemes. The authors propose several novel elements, such as trainable Laplace block, second order Runge-Kutta scheme for simulating temporal dynamics and a padding strategy to incorporate boundary conditions of different types. These improvements allowed the authors to achieve new quality of simulation. The obtained model has good generalization capabilities over initial conditions and over the unseen types of flow (such as another Reynolds number)

### Strengths
* The authors have shown that spatiotemporal dynamics can be modeled by GNN in spatial domain together with 2nd order numerical scheme in temporal domain
* The authors proposed and tested a combination of reasonable improvements to the previous works with similar techniques (Pfaff et al. 2021). There key additions are Laplace block and padding strategy for different types of boundary conditions
* The proposed improvements allowed authors to outperform the competitors in terms of quality for chosen test problems
* Generalization and ablation studies substantiate the authors contributions

### Weaknesses
The limitations of the work were not addressed properly. In particular:
* applicability to the PDE systems without the Laplace operator
* simulation for the big number of time steps (for example this occurs for weather simulations)
* boundary conditions padding for the domain with non-straight boundary – it’s not clear how to work with them

Also the experiments are insufficient:
* It’s important to investigate the computational requirements of the proposed approach for training and inference in dependence on the important parameters (number of time steps, size of the training dataset, etc.) in order to assess its applicability in practice
* Also it would be useful to understand how the segment size M in 3.4 influences the results and computational requirements

Also the paper is hard to read and it needs some restructurization. Probably  the introduction can be shortened a little bit together with the beginning of the abstract and authors could explain in more details how the model is trained and how different types of boundary conditions are introduced for curved boundary

### Questions
* Why in eq. (7) for loss function you use only first and last step? What will change if we will compare full rollouts?
* How the padding strategies will work for boundary conditions on irregular shapes?
* What do you mean when you say that boundary conditions are used as a priori physics knowledge?
* Will the Laplace block still be useful for PDEs without the Laplace operator?

also look for the suggestions arising from weaknesses

### Soundness
3

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
4

### Summary
The manuscript introduces a way to approximate a non-linear PDE operator with a GNN block completed with a Laplace operator block.
The examples include a varity of linear and linear PDEs.

### Strengths
The way to approximate a non-linear PDE operator with a GNN block completed with a Laplace operator block looks fairly original.

### Weaknesses
1.	The ultimate goal of the manuscript is to learn the nonlinear operator $F$.  However, it is not explained why it is needed while $F$ is known and given.
2.	The way how the authors approximate the nonlinear operator F, Eq. (6), evidently has some limitations. For example, it won’t work well when $F = (\Delta u)^2 $ and so on.  Consider being more specific in defing the operator F in Eq. (1).
3.	Section 4 is difficult to follow since the actual PDEs and their coefficients are not specified.
4.	It is not really explained why padding is needed to incorporate boundary conditions.

### Questions
1.	Could you give mathematical and physical interpretation of $z_i$, Eq. (5)? What activation functions are used to parametrize $z_i$? How do you formally differentiate between coarse and fine meshes?
2.	Section 3.4 implies that over all there are $T/M$ loss functions. Are these loss values combined together somehow? What is ground truth data in this setting?
3.	Could you include experiments with $F = \text{div} (D \nabla u)$ with either $D(x,y)=1 $ or $D(x,y)=1+4x+5y$ (or other varying from 1 to 10)? It will give to the reader a good understanding of approximation properties of Eq.(6).
4.	The discussion in the manuscript covers only 2D spatial data. Does the proposed method admit a generalization to the 3D case? How the Laplace block will like in this case?
5.	The RK2 and RK4 schemes are known to be applicable to non-stiff problems only due to stability limitations. What scheme would you suggest for a stiff PDE of form Eq. (1) and how would you implement such a scheme?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
10

### Rating Number
10

### Confidence
5

### Summary
I love the paper for its outperforming MGN; it has a solid baseline by DeepMind! It introduces PhyMPGN, a Physics-encoded Message Passing Graph Network that effectively models spatiotemporal PDE systems on irregular meshes using limited data. By integrating physics through a learnable Laplace-Beltrami operator and a novel boundary condition padding strategy, the approach ensures physically accurate predictions. PhyMPGN significantly outperforms existing methods, achieving over 50% performance gains and demonstrating strong generalization across various PDEs and conditions. The model's efficiency and robustness make it a valuable advancement for scientific simulations where data is sparse or complex geometries are involved.

### Strengths
Outperform a solid baseline; writing is good, presentation is good. The method is clear and new. The strength of this paper lies in its innovative integration of physics-based knowledge into graph neural networks, which enables accurate and efficient modeling of complex spatiotemporal PDE systems on irregular meshes with limited data. By employing a learnable Laplace block and a novel boundary condition padding strategy, PhyMPGN ensures solutions remain physically consistent and precise, overcoming limitations of traditional and purely data-driven methods. Additionally, the model's demonstrated ability to generalize well to different PDEs, geometries, and conditions, along with its significant performance gains over existing techniques, highlights its robustness and versatility for real-world scientific applications

### Weaknesses
There is some need for some clarification when it is for convection-dominant problem.

### Questions
I have several questions to help me understand the method thoroughly. Firstly, how will the model behave if we delete (or do not use) the Mesh Laplace? Will it still be better than MGN? Secondly, why second-order RK for MOL? What about RK4 or forward Euler? Do these different choices matter? Thirdly, I understand graph Laplace preserves some diffusion physics, which is excellent and universal enough. Still, for examples of inviscid first order PDE such as wave/ advection equation, or inviscid Burger equation,  Euler equations, will add graph Laplacian make the traveling feature blur?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces a graph learning approach called Physics-encoded Message Passing Graph Network (PhyMPGN) designed to model spatiotemporal PDE systems on coarse unstructured meshes using small training datasets. Authors incorporate a learnable Laplace block that encodes the discrete Laplace-Beltrami operator to constrain the GNN learning within a physically feasible solution space. Additionally, a boundary condition padding strategy is proposed to handle different types of boundary conditions, enhancing model convergence and accuracy. Extensive experiments demonstrate that PhyMPGN accurately predicts various spatiotemporal dynamics on coarse unstructured meshes with complex BCs, outperforming other baseline models with considerable gains.

### Strengths
1.	The integration of physics-encoded components within a message-passing GNN addresses the challenges of modeling spatiotemporal dynamics on unstructured meshes.
2.	The learnable Laplace block that encodes the discrete Laplace-Beltrami operator ensures solutions remain within a physically feasible space.
3.	The experiments are thorough, showcasing the model's ability to generalize across various spatiotemporal dynamics. The ablation studies further strengthen the validity of the proposed methods.
4.	The model demonstrates strong generalization capabilities despite being trained on small datasets.

### Weaknesses
1.	The authors state that traditional numerical methods require fine meshes and small time stepping. This overlooks implicit schemes, which can handle larger time steps while maintaining stability. Furthermore, the statement lacks nuance regarding the trade-offs between explicit and implicit methods, particularly in the context of stiffness in PDE systems. Explicit methods, while simple, are often limited by the Courant-Friedrichs-Lewy (CFL) condition, which dictates a relationship between time step size and mesh resolution for stability. Implicit methods, on the other hand, can overcome this limitation, allowing for larger time steps, but at the cost of solving a system of equations at each time step, which introduces computational overhead.
2.	The paper does not provide a comparative analysis of the computational speed or efficiency of PhyMPGN. This is a critical omission, as the practical applicability of a numerical method is often determined by its computational cost. The authors should provide a detailed breakdown of the computational complexity of their method, including the time required for training and inference, and compare it against other methods, both numerical and neural-based.
3.	The rationale behind focusing solely on coarse meshes is not explained. While coarse meshes can reduce computational cost, they also introduce discretization errors that can affect the accuracy of the solution. The authors should justify why they chose to focus on coarse meshes, especially given that the accuracy of the method is a key concern. Furthermore, the paper does not discuss the limitations of using coarse meshes, such as the inability to capture fine-scale features of the solution.

### Questions
1.	Could the authors clarify their statement regarding the limitations of traditional numerical methods? How does their approach compare with implicit numerical schemes in terms of stability and time-stepping requirements?
2.	Can the authors provide insights into the computational performance of their method? 
3.	What are the main obstacles in generalizing PhyMPGN to three-dimensional problems? How might the current architecture need to adapt to handle the increased complexity?

### Soundness
3

### Presentation
4

### Contribution
3
