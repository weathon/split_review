# Graph Fourier Neural Kernels (G-FuNK): Learning Solutions of Nonlinear Diffusive Parametric PDEs on Multiple Domains

- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 3, 5, 8

## Abstract
Predicting the time-dependent dynamics of complex systems governed by non-linear partial differential equations (PDEs), with varying parameters and domains, is a difficult problem that is motivated by applications in many fields. We introduce a novel family of neural operators based on a \textbf{G}raph \textbf{F}o\textbf{u}rier \textbf{N}eural \textbf{K}ernel (G-FuNK), for learning solution generators of nonlinear PDEs with varying coefficients, across multiple domains, for which the highest-order term in the PDE is diffusive. 
G-FuNKs are constructed by combining components that are parameter- and domain-adapted, with others that are not. The latter components are learned from training data, using a variation of Fourier Neural Operators, and are transferred directly across parameters and domains. The former, parameter- and domain-adapted components are constructed as soon as a parameter and a domain on which the PDE needs to be solved are given. They are obtained by constructing a weighted graph on the (discretized) domain, with weights chosen so that the Laplacian on that weighted graph approximates the highest order, diffusive term in the generator of the PDE, which is parameter- and domain-specific, and satisfies the boundary conditions. This approach proves to be a natural way to embed geometric and directionally-dependent information about the domains, allowing for improved generalization to new test domains without need for retraining. Finally, we equip G-FuNK with an integrated ordinary differential equation (ODE) solver to enable the temporal evolution of the system's state. 
Our experiments demonstrate G-FuNK's ability to accurately approximate heat, reaction diffusion, and cardiac electrophysiology equations on multiple geometries and varying anisotropic diffusivity fields. 
We achieve low relative errors on unseen domains and fiber fields, significantly speeding up prediction capabilities compared to traditional finite-element solvers.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors proposes an interesting surrogate model that combines Graph as the discretization method for Fourier neural operators. I believe the manuscript may be accepted after a major revision.

### Strengths
The paper proposes merging graphs within the standard surrogate models, which allows estimating the solution of 2nd order PDEs with varying coefficients on complicated geometries.

### Weaknesses
I believe there are several important details missing in the manuscript. Below, I list them.

**Major:**

- Is there an error estimator in the prediction? How can one trust the outcome of fitted G-FUNK model for an unseen problem?
- Is there a way to enforce conservation laws (or some notion of structure preservation) in prediction if the underlying PDE admits such constraint?
- Does the solution/data need to be smooth? Can you try out viscous burger's equation with emerging discontinuity as viscosity goes to zero?
- Is the outcome ODE stable? Is there a guarantee on stability of ODE?
- Can you compare the Data-Generation/Training/Prediction time of proposed method versus the ones from a standard finite element/volume solver in the presented test cases? I believe comparing only the time/complexity of prediction against standard solver is very much misleading.
- If we know the underlying PDE, wouldn't it make sense to incorporate that in the loss, similar to what PINN does?
- Can the author show a case of extrapolation? To me, similar to PINNs, the proposed method can only be used as an efficient interpolator within the space of training data. This makes me doubt the claims on "parameter and domain-adaptation". For example, if you train your model to estimate heat equation in 1d problem inside the domain [0,1], can you test it on domain [-10,10] with different boundary conditions?

**Minor:**

- Abstract: “… for which the highest-order term in the PDE is diffusive...” What does it mean? Do you mean the highest-order term is even or, it has to be 2? I’m guessing second-order PDEs, which needs to be clarified in Abstract.
- Abstract: "without the need for retraining" and not "without need for retraining”.

### Questions
**Major:**

- Is there an error estimator in the prediction? How can one trust the outcome of fitted G-FUNK model for an unseen problem?
- Is there a way to enforce conservation laws (or some notion of structure preservation) in prediction if the underlying PDE admits such constraint?
- Does the solution/data need to be smooth? Can you try out viscous burger's equation with emerging discontinuity as viscosity goes to zero?
- Is the outcome ODE stable? Is there a guarantee on stability of ODE?
- Can you compare the Data-Generation/Training/Prediction time of proposed method versus the ones from a standard finite element/volume solver in the presented test cases? I believe comparing only the time/complexity of prediction against standard solver is very much misleading.
- If we know the underlying PDE, wouldn't it make sense to incorporate that in the loss, similar to what PINN does?
- Can the author show a case of extrapolation? To me, similar to PINNs, the proposed method can only be used as an efficient interpolator within the space of training data. This makes me doubt the claims on "parameter and domain-adaptation". For example, if you train your model to estimate heat equation in 1d problem inside the domain [0,1], can you test it on domain [-10,10] with different boundary conditions?

**Minor:**

- Abstract: “… for which the highest-order term in the PDE is diffusive...” What does it mean? Do you mean the highest-order term is even or, it has to be 2? I’m guessing second-order PDEs, which needs to be clarified in Abstract.
- Abstract: "without the need for retraining" and not "without need for retraining”.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a neural network model to learn a solution operator of time-dependent second-order semi-linear PDEs that takes diffusion tensor and random sample points of a family of domains as inputs.

### Strengths
The numerical demonstration is the cardiac EP example  is interesting since I understood the least. I will rely on an expert in this area to give a meaningful comment on this example.

### Weaknesses
This paper proposes a neural network model to learn a solution operator of time-dependent second-order semi-linear PDEs that takes diffusion tensor and random sample points of a family of domains as inputs.
While the first input has been considered by many authors, the difficulty here is to allow the domain to be chosen from a family of domains, denoted by $\{\Omega_\alpha\}_{\alpha\in \mathcal{A}}$. My first thought is whether the setup makes sense since there is no discussion on the class of domains that are imposed. I believe this won't work on arbitrary classes of domains. For example, e.g., for Riemannian manifolds, I would believe that if any pair of manifolds in this class have Riemannian metrics that are diffeomorphic (or even stronger, such as conformally equivalent), then the learning problem makes sense. One would need a notion of continuity between any pair of domains in the class, otherwise, it is not feasible to interpolate (to have a map that can interpolate between the training domains).  In the numerical examples shown in the paper,  there is an affine transformation between any pair of arbitrary side lengths in the 2D Nonlinear Reaction-Diffusion. For the Cardiac Electrophysiology, although the measured data come from 25 patients, the PDE is solved on processed domains (finally 24 of these), and I suspect that these domains are diffeomorphic.

The only interesting numerical demonstration is the cardiac EP example since I understood the least. I will rely on an expert in this area to give a meaningful comment on this example. In terms of methodology, I cannot understand why the Graph Laplacian structure is helpful, unless when the derivatives in Eq. (2) are defined with respect to the Riemannian metric of the embedded manifolds. It is also not obvious to me why the construction of the G-FUNK layer should be a way to go since I cannot reason it from any basic principle. 

While some numerical results look interesting, I don't really understand why the approach should work in general due to the lack of theoretical justification. I am also not sure how the approach behaves if one increases the number of layers or parameters in each G-FUNK layer. Finally, the three numerical examples are low-dimensional problems (2D or 3D), I would naively believe the standard PDE solvers should be able to solve the problem accurately in a reasonable time. Solutions to these (FEM in the cardiac EP example) are being used to train the G-FUNK model.  Based on these concerns, I believe this paper is technically (or mathematically) not interesting and not suitable for publication in ICLR. I would urge the authors to consider submitting this work to a domain science journal that is relevant to personalized cardiac EP.

### Questions
NA

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposed Graph Fourier Neural Kernels (G-FuNK), which aim to solve time-dependent, nonlinear partial differential equations (PDEs) with varying parameters and domains. G-FuNK leverages parameter- and domain-adapted spectral method. These operators are particularly well-suited for problems involving anisotropic diffusion and complex geometries. The paper demonstrates G-FuNK's effectiveness on several applications, such as heat equation simulations, reaction diffusion equations, and cardiac electrophysiology, showing promising results in terms of accuracy and computational speed.

### Strengths
1. G-FuNK leverages parameter- and domain-adapted spectral method such that it is well-suited for problems involving anisotropic diffusion and complex geometries.

2. The application on Cardiac Electrophysiology is very interesting.

3. The paper presents a detailed comparison with FNO and GNN methods, showing that G-FuNK can outperform these methods

### Weaknesses
1. The limitations should be addressed.

2. The so-called graph fourier transform is actually spectral method, which need the eigenvectors pre-calculated first. This procedure could make the method not useful for large scale problem. Computational efficiency and scalability should be reported, including offline computational for the eigenvectors and online computation time. Comparison with FNO and GNN in terms of efficiency is also absent.

3. The novelty of graph fourier transform is limited. This is a widely studyed area in graph neural network community.

### Questions
1. Why do the authors use the neural ODE  model? Any gain from the specific model?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes  Graph Fourier Neural Kernels (G-FuNK) for learning solution generators of time-dependent partial differential equations (PDEs) on graphs. G-FuNK aims to be "geometry-invariant" by leveraging the spectral domain of graphs through the Graph Fourier Transform (GFT), similar to how the Fourier Neural Operator (FNO) achieve "discretization-invariance" in regular domain.

### Strengths
The writing is clear, and the combination of graph neural networks (GNNs) and FNO is well motivated and novel to the best of my knowledge. The numerical examples show a gradual increase in complexity, leading to the final example on cardiac electrophysiology, which is complex and demonstrates the practical utility of the proposed framework.

### Weaknesses
In Table 1, for the three methods (G-FuNK, FNO, GNN), the number of parameters can differ by orders of magnitude, making it challenging to evaluate the improvement in performance. 

The statement "Our method predicts entire trajectories in under 1 second, significantly outperforming traditional numerical methods. For example, cardiac EP simulations typically take at least 15 minutes on 12 CPU cores for one given set of initial conditions." could be more precise, particularly regarding the numerical solution being compared. It seems the cardiac EP simulations from numerical methods serve as the high-fidelity solutions that are used to generate the training data and evaluate the error. However, G-FuNK learns on reduced modes (k_max), which may lead to limited accuracy. It would be more informative if the numerical solutions are computed on coarser mesh that achieve similar of accuracy as G-FuNK, or using the reduced modes.

### Questions
Given that the paper focuses on PDEs on graphs, it seems that the "Multipole Graph Neural Operator for Parametric Partial Differential Equations" (MGKN), which claims to be mesh-invariant, would be a more suitable baseline for comparison. While the original MGKN framework does not explicitly tackle changing geometry, it seems it can still be applied in this setting, since only the graph is used as an input. There are also many similarities between these two approaches: the Fourier transform and inverse Fourier transform in G-FuNK play a role similar to kernel convolutions in MGKN, which are computed using the multipole algorithm. Additionally, both methods employ some form of truncation to make computation more tractable (e.g., limiting modes or long-range interactions). I would appreciate further discussion or comparison of these two approaches.

### Soundness
3

### Presentation
3

### Contribution
3
