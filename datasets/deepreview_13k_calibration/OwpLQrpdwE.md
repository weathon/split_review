# Learning vector fields of differential equations on manifolds with geometrically constrained operator-valued kernels

- Decision: Accept
- Avg Score: 7.40
- Scores: 10, 6, 5, 8, 8

## Abstract
We address the problem of learning ordinary differential equations (ODEs) on manifolds. Existing machine learning methods, particularly those using neural networks, often struggle with high computational demands. To overcome this issue, we introduce a geometrically constrained operator-valued kernel that allows us to represent vector fields on tangent bundles of smooth manifolds. The construction of the kernel imposes the geometric constraints that are estimated from the data and ensures the computational feasibility for learning high dimensional systems of ODEs. Once the vector fields are estimated, e.g., by the kernel ridge regression, we need an ODE solver that guarantees the solution to stay on (or close to) the manifold. To overcome this issue, we propose a geometry-preserving ODE solver that approximates the exponential maps corresponding to the ODE solutions.  We deduce a theoretical error bound for the proposed solver that guarantees the approximate solutions to lie on the manifold in the limit of large data. We verify the effectiveness of the proposed approach on high-dimensional dynamical systems, including the cavity flow problem, the beating and travelling waves in Kuramoto-Sivashinsky equations, and the reaction-diffusion dynamics.

## Human Reviews

## Human Reviewer 1

### Rating
10

### Rating Number
10

### Confidence
4

### Summary
The authors propose a kernel method for learning and integrating ordinary differential equations on manifolds. The main contribution is the method for learning ODEs, called Geometrically constrained Multivariate Kernel Ridge Regression Method (GMKRR), a method that relies on the theory of Reproducing Kernel Hilbert Spaces. As for integrating, the author propose a new Euler method with a Normal direction correction.

### Strengths
The paper is very well written. The topic relies heavily on results from operator kernels, but I found that the introduction to the topic by the authors was adequate.
The contributions of the authors are novel and have promising applications in data-driven discovery of latent dynamics.
The experimental evaluation is good.

### Weaknesses
The method involves solving very large systems of equations at each step, and thus is computationally expensive. Nevertheless, the initial training time, (if existent, for instance when solving the system with a Cholesky decomposition) is much less compared with a PINN.
Furthermore, the timings are superior when compared with other data-driven methods, such as CANDyMan.

### Questions
Instead of the Euler-NC method, have you considered a second order Euler method for the ODE, by differentiating the kernel operator?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Authors propose a new method for solving ODEs on manifolds in the multidimensional case which is based on the geometrically constrained operator-valued kernel and a geometry-preserving ODE solver. The efficiency and advantages of the method are demonstrated experimentally for a number of multidimensional problems and in comparison with alternative approaches.

### Strengths
1. The presentation of the material in the text of the manuscript is consistent and neat.

2. The problem of solving such a class of equations is relevant for a wide range of applications.

3. It has been empirically demonstrated that the proposed approach significantly outperforms known baselines (SINDy methods, CANDyMan) in both accuracy and speed on several classes of problems.

### Weaknesses
Overall, the work appears to be of high quality and relevant, however I would like to clarify the issues listed below in the "Questions" section.

 1. In the abstract you note that "machine learning methods ... struggle with ... lack of interpretability". It is not entirely clear from the text of the manuscript whether your method solves this particular problem.

 2. Can you comment on whether NC Euler method (from sec. 3.2) is new and what alternative approaches exist for predicting dynamics on complex manifolds (if as you note RK2 method behaves badly here)?

 3. Section "Related work" lacks a description of the essence of CANDyMan approach.

 4. Is it possible to consider more baselines, e.g., method from the work "Neural Manifold Ordinary Differential Equations", described in "Related work"?

 5. There are probably a few typos. Line 074: "We supplement the papers with..." (probably should be singular, i.e., "paper"); Line 446 and 475: "submanifold manifold" (probably word "manifold" is redundant here); Line 449: "the cost ... faster" (maybe cost is lower or training is faster).

### Questions
1. In the abstract you note that "machine learning methods ... struggle with ... lack of interpretability". It is not entirely clear from the text of the manuscript whether your method solves this particular problem.

2. Can you comment on whether NC Euler method (from sec. 3.2) is new and what alternative approaches exist for predicting dynamics on complex manifolds (if as you note RK2 method behaves badly here)?

3. Section "Related work" lacks a description of the essence of CANDyMan approach.

4. Is it possible to consider more baselines, e.g., method from the work "Neural Manifold Ordinary Differential Equations", described in "Related work"?

5. There are probably a few typos. Line 074: "We supplement the papers with..." (probably should be singular, i.e., "paper"); Line 446 and 475: "submanifold manifold" (probably word "manifold" is redundant here); Line 449: "the cost ... faster" (maybe cost is lower or training is faster).

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper definitely proposes an interesting method to learn the dynamics of a dynamical system that lives on a low-dimensional manifold based on point cloud-type data. The "geometrical constraint" refers to that the bases for building the kernel regression are projected to (an approximate) tangent space of the observations. The procedure to obtain the kernel regression's solution is modified to leverage of the (estimated) intrinsic dimension $d$. Then a "geometry-preserving" integrator is applied to get the trajectory based on the $\mathbf{f}_{\epsilon}$ learned in the kernel regression.

### Strengths
- Efficient compared with the baseline.

### Weaknesses
 - Why just 1 baseline?
- Line 136: the writing on why the kernel regression opts for the L2 regularization and not the L1 regularization SINDy used is not very convincing.                     
- The paper only compares the end results with SINDy-based method. I suggest doing a more lateral comparison within the method itself.
  - Why not comparing the performance of different kernels such as Matern?
  - One of the most important aspect in this method is to compute the projection (matrix) onto the tangent space. Yet, this part is shoveled into the appendix. For example, the robustness is never mentioned, how the sensitive the approximation to the projection matrix affects the accuracy of the whole method? I say this because for multiple toy models in this paper, the representation of the manifold is known, then the analytic tangential projection matrix can be formed, which sets a perfect playground for such a study.
  - Since one has $\mathbf{f}_{\epsilon}$ once trained, why not comparing Euler+NC with a symplectic integrator (such as semi-implicit which shares similar spirit with this correction method)?


- line 191: I am not sure if it is a typo but the squared exponential should not look like that, that is the Laplace kernel.

### Questions
N/A

### Soundness
3

### Presentation
3

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
This paper overcomes some of the limitations of SiNDY and CandyMan to learn ODEs with solutions represented manifolds. The authors show that by enforcing geometric constraints, they can improve efficiency in training as well as accuracy compared to other methods on toy examples by ensuring solutions lie close to a lower dimensional submanifold that can express the data.

### Strengths
The paper is well written and provides detailed theoretical justification for their framework with clear numerical experiments highlighting the proposed method’s superiority to state-of-the-art works in this area. They benchmark with several new methods that are suitable for the problems they focus on and outperform in both training efficiency and accuracy.

### Weaknesses
The authors mention that their approach overcomes limitations of other algorithms in regard to making predictions on out of distribution data, yet they don’t detail the extent of which their method can practically handle problems where the manifold doesn’t exhibit properties or yield constraints that allow you to represent your solutions on tangent planes of low dimensional submanifolds. It would be beneficial to provide specific examples of manifold types or problem domains where their method might struggle. For instance, while the method may perform well on systems exhibiting quasi-periodic behavior which can be effectively captured by low-dimensional manifolds, the performance on chaotic systems or systems with rapidly changing dynamics is not clear. The paper would benefit from a discussion on the limitations of the method when the underlying dynamics do not lend themselves to low-dimensional manifold representations.

### Questions
Are there specific types of out-of-distribution scenarios where the method is expected to perform well or poorly?

Can this method be used on domains or solutions that do not have or allow periodic behaviors that reduce the intrinsic dimensionality of the original solution manifold? It would be beneficial if the authors could provide a discussion on how the proposed method might be adapted for non-periodic systems.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper presents an approach for learning ODEs on manifolds using kernel methods such that learnt ODE solutions are constrained to lie on the learnt manifold. They also present a method for solving ODEs on manifolds more accurately than standard RK based approaches in terms of how closely solutions lie on said manifold.

### Strengths
- Learning ODEs constrained to evolve on manifolds using linear methods is a beautiful idea.
- The geometry-preserving time integrator is well-motivated and could have impacts well beyond learning differential equations from data. 
- The numerical studies convincingly demonstrate the proposed approach is better than the SINDy-style approaches they compare to.

### Weaknesses
 - While theoretically interesting, I think the authors could have done a better job of motivating their approach in the introduction from a practical perspective. In particular, it wasn't clear to me that the standard approach of learning latent differential equations, is limited in practice by the fact that learnt differential equations will deviate from the learnt manifold. Since the standard approach is is so widely used, providing concrete references / studies which demonstrate these issues in practice would have been helpful for motivating the work. 

 - I think it's arguable that the one of the biggest challenges with SINDy-style algorithms is that they struggle in the presence of noise, for example:

    - Messenger, Daniel A., and David M. Bortz. "Weak SINDy for partial differential equations." Journal of Computational Physics 443 (2021): 110525

    - Fasel, Urban, et al. "Ensemble-SINDy: Robust sparse model discovery in the low-data, high-noise limit, with active learning and control." Proceedings of the Royal Society A 478.2260 (2022): 20210904.

    Since your approach also requires estimating derivatives using finite differences, it would have been helpful to include some discussion on this issue. 

 - You mentioned that one of the goals of your work as compared to standard approaches for learning latent differential equations is to learn interpretable models. As I understand it, SINDy-style models are interpretable because they learn sparse approximations to differential equations. Since you relax the sparsity requirement, I struggled to understand how your proposed approach is more interpretable than neural-network based models.


*Additional feedback. To be clear, these points are here to help and will not be a part of the decision assessment.* 

 - When introducing SINDy, I think it would be helpful to include a reference to this work since I think they also proposed to learn sparse dynamics using dictionaries of basis functions in 2011.

    - Wang, W.X., et al. Predicting catastrophes in nonlinear dynamical systems by compressive sensing. Phys. Rev. Lett. 106, 154101 (2011).

 - The results from your numerical studies would be made stronger by including comparison to learning latent ODEs with neural networks, for example:

    - Toth, P., Rezende, D. J., Jaegle, A., Racanière, S., Botev, A., & Higgins, I. (2019). "Hamiltonian generative networks." arXiv preprint arXiv:1909.13789.
    - Chen, Ricky TQ, Yulia Rubanova, and David Duvenaud. "Latent ODEs for irregularly-sampled time series." Advances in Neural Information Processing Systems 32 (2019): 3.

### Questions
1. How do you view your approach as being more interpretable than neural-network based methods?
2. How do you suspect you suspect your approach will scale for problems with higher dimensional submanifolds?
3. How do suspect your method will perform in the presence of significant observation noise given that you are required to estimate the manifold and the time derivatives on the manifold from data?

### Soundness
4

### Presentation
3

### Contribution
4
