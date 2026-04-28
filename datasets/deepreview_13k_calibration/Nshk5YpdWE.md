# Lagrangian Flow Networks for Conservation Laws

- Decision: Accept
- Avg Score: 7.33
- Scores: 8, 8, 6

## Abstract
We introduce \textit{Lagrangian Flow Networks} (LFlows) for modeling fluid densities and velocities continuously in space and time.
By construction, the proposed LFlows satisfy the continuity equation,
a PDE describing mass conservation in its differentiable form. 
Our model is based on the insight that solutions to the continuity equation can be expressed as
time-dependent density transformations via differentiable and invertible maps.
This follows from classical theory of the existence and uniqueness of Lagrangian flows for smooth vector fields.
Hence, we model fluid densities by transforming a base density with parameterized diffeomorphisms conditioned on time.
The key benefit compared to methods relying on numerical ODE solvers or PINNs is that the analytic expression of the velocity is always consistent with changes in density.
Furthermore, we require neither expensive numerical solvers, nor additional penalties to enforce the PDE.
LFlows show higher predictive accuracy in density modeling tasks compared to competing models in 2D and 3D,
while being computationally efficient.
As a real-world application, we model bird migration based on sparse weather radar measurements.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a neural network-based model designed to adhere to the continuity equation, even when dealing with scenarios where precise boundary and initial conditions are unknown. The core technical foundation relies on the classical theory of Lagrangian flows, providing a toolbox that ensures the evolution of density and velocities complies with the continuity equation.

### Strengths
The paper significantly contributes to the field of neural PDE methods by focusing on enforcing constraints. It marries neural networks with conditioning normalization flows, resulting in LFlows that satisfy the continuity equation by design.

The method is validated across various 2D and 3D problems, including a real-world bird migration dataset, which could potentially serve as a standard benchmark dataset for similar problems. Unlike previous methods that often require known PDEs, initial, and boundary conditions, this approach tackles data assimilation-style problems where many system parameters are unknown. This kind of problem could be particularly useful for biomedical imaging applications.

The paper rigorously compares its approach to Richter-Powell's divergence-free neural networks, showcasing the computational efficiency of its method without the need for higher-order autodiff. Additionally, it compares favorably against other standard baselines, such as PINNs, especially in spatially sparse settings.

### Weaknesses
The proposed method inherits limitations associated with normalizing flows and bijective layers, such as difficulties in handling discontinuities. This is a significant limitation, particularly when modeling phenomena that exhibit sharp transitions or shocks. Furthermore, while the method demonstrates computational efficiency compared to divergence-free networks by avoiding higher-order autodiff, the computational cost of training the normalizing flow itself, especially with complex architectures, is not thoroughly discussed. The paper also does not fully explore the potential for error accumulation when propagating densities over long time horizons, which is a critical aspect for practical applications. Finally, the method's reliance on bijective transformations might restrict its ability to model more complex, non-invertible dynamics, potentially limiting its applicability to a broader range of physical systems.

### Questions
Could the authors comment on the challenges they anticipate when scaling this approach to larger problems, such as modeling large turbulent flows in aerodynamics? How might the complexity of LFlows impact scalability in such scenarios?

How does the computational complexity of LFlows compare to existing methods for solving hydrodynamic flow problems, especially in high-dimensional scenarios? Are there specific trade-offs or advantages in terms of computational efficiency?

Does the methodology proposed in this paper have the potential to be generalized to tackle other partial differential equations (PDEs) beyond the continuity equation? If so, what challenges or modifications might be necessary when applying it to different PDEs?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper expresses the continuity equation into the time-dependent density transformation to model the fluid densities and velocities. By introducing differentiable and invertible maps, the proposed LFlows can ensure the continuity equation inherently. The authors provide complete proof to support their insights. Typical experiments are also included. Experimentally, LFlows performs best in both performance and efficiency.

### Strengths
1.	The paper starts from an interesting insight. The proposed method is reasonable and well-supported.

2.	The authors conduct extensive experiments, covering both simulated and real-world dataset. 

3.	The propose LFlows performs well in both performance and efficiency.

### Weaknesses
1.	About the presentation.

For me, the writings in Section 3.1 and 4 are confusing and hard-to-read.

In Section 3.1, the authors use several theorems in an informal way and sometimes not give the exact formalization of theorem. I prefer to place the definitions of theorems in the main text and leave the proof in appendix, such as Theorem 1,2 and the existence and uniqueness of Lagrangian flows for smooth vector fields.

In Section 4, I don’t think the implementation of LFlows are well described. The model architecture in Appendix A.3 should be placed in main text. Besides, the implementation for baselines should be deferred into the Appendix.

2.	How to adopt LFlows to process the spatially sparse data? More details are expected.

3.	About the noise observations in the real-world dataset. Since LFlows enable the strict continuity equation, does it come across problems when the input data is noisy even wrong? Some discussions are expected.

### Questions
All the questions are listed above.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes LFlow, a neural parameterization of both the density and the velocity field that adhere to the continuity equation. This is achieved with a link between time-conditioned diffeomorphisms and Lagrangian solution maps for the continuity equation. Two application settings were considered, where in one setting the user has sparse data on both density and velocity, and in another setting, the user has no data but knows the equations. Low-dimensional experiments are done to demonstrate the effectiveness of the proposed parameterization.

### Strengths
* The writing of the paper is clear.
* Both settings are interesting and the proposed method has been shown to outperform the alternatives (PINN, DFNN, SLDA).

### Weaknesses
 * To my knowledge, the idea of using the Lagrangian view of the continuity equation to build a neural parameterization that gives both velocity and density access is not new.
  * In Section 3.1 and 3.2 of [1], the TIPF parameterization appears to be identical to LFlow proposed in the present paper, with the only difference being that in (13) of the present paper, $\Phi_t$ appears instead of the inverse, which is the case of TIPF.
  * This is a minor difference for TIPF, since in [1] the conditional normalizing flow used is RealNVP [2], which has ready access to the inverse flow map.
  * Could the authors elaborate on the advantages of avoiding the inverse here?
  * Could the authors also comment on the choice of the Lipschitz-constrained invertible densenets as the backbone architecture? What is the advantage/disadvantage compared to e.g. RealNVP [2]?
* The experiments section is weak in my opinion, and weaker than that in [Richter-Powell 2022]. If I understand correctly, all experiments are in 2D. How would the parameterization fare in higher dimensions? Higher dimensional experiments are done in [Richter-Powell 2022]. In [1] it is found that TIPF does not work well in dimension >= 10. I suspect the same behavior occurs here, due to the reason that invertible pushforward networks might not be expressive (or might be hard to train).


### Questions
1. At the bottom of the first page, it reads "in setting (ii) we measure only the density of the fluid but we know additional equations defining the velocity." If density is already known for all time, then isn't it already enough to reconstruct the velocity without needing to know any additional equations, by simply solving the continuity equation?
2. In the evaluation in Section 5.2, the gold standard of $W_2^2$ is computed using discrete estimates (and then averaged). However, the discrete estimate of W2 is known to be biased. How can one be sure that the red bars on the right of Figure 3 are accurate? Would the bar shift if more samples were used?
3. In (15), how is the double integral computed in practice? It looks like it requires uniform samples from the domain $\Omega$, which could be very ineffective if the flow only concentrates on a small portion of the domain.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair
