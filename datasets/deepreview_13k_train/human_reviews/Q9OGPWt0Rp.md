# Connecting Solutions and Boundary Conditions/Parameters Directly: Solving PDEs in Real Time with PINNs

- Decision: Reject
- Scores: 5, 5, 8, 3

## Abstract
Physics-Informed Neural Networks (PINNs) have proven to be important tools for solving both forward and inverse problems of partial differential equations (PDEs). However, PINNs face the retraining challenge in which neural networks need to be retrained once the parameters, or boundary/initial conditions change. To address this challenge, meta-learning PINNs train a meta-model across a range of PDE configurations, and the PINN models for new PDE configurations are then generated directly or fine-tuned from the meta-model. Meta-learning PINNs are confronted with either the issue of generalizing to significantly new PDE configurations or the time-consuming process of fine-tuning. By analyzing the mathematical structure of various PDEs, in this paper we establish the direct and mathematically sound connections between PDE solutions and boundary/initial conditions, sources and parameters. The learnable functions in these connections are trained offline in less than 1 hour in most cases. With these connections, the solutions for new PDE configurations can be obtained directly and vice versa, without retraining and fine-tuning at all. Our experimental results indicate that our methods are comparable to vanilla PINNs in terms of accuracy in forward problems, yet at least 400 times faster than them (even over 800 times faster for variable initial/source problems). In inverse problems, our methods are much more accurate than vanilla PINNs while being 80 times faster. Compared with meta-learning PINNs, our methods are much more accurate and about 20 times faster than fine-tuning. Our inference time is less than half a second in forward problems, and at most 3 seconds in inverse problems (less than half a second for variable initial/source problems of linear PDEs). Our code will be made publicly available upon acceptance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses the limitations of Physics-Informed Neural Networks (PINNs), specifically the need for retraining when parameters or boundary/initial conditions of partial differential equations (PDEs) change. The authors propose a novel approach that leverages mathematical connections between PDE solutions and their boundary/initial conditions, sources, and parameters, enabling the model to solve new PDE configurations directly without retraining or fine-tuning. Experimental results show that this approach is up to 800 times faster than vanilla PINNs and 20 times faster than fine-tuning meta-learning PINNs, achieving inference times under half a second for forward problems and up to 3 seconds for inverse problems.

### Strengths
Unlike standard PINNs and meta-learning PINNs, this approach requires no retraining or fine-tuning to handle new PDE configurations, significantly reducing computational costs and simplifying model deployment. And the method achieves remarkable inference speed improvements, being up to 800 times faster than vanilla PINNs and around 20 times faster than meta-learning PINNs with fine-tuning. This efficiency makes it practical for real-time applications or situations where quick results are needed. Furthermore, by analyzing and leveraging mathematical structures in PDEs, the paper provides a principled method for establishing direct connections between PDE parameters and solutions. This reduces the reliance on purely data-driven methods and enhances interpretability.

### Weaknesses
 **1. Parameter Complexity and Scalability**: The paper does not provide a detailed analysis of the total number of parameters required by the proposed method. For example, on cases involving linear PDEs with variable boundary/initial conditions or sources, since the model learns independent PINNs for each basis function and then combines them to approximate the solution, it appears that the parameter count could increase significantly. While the approach achieves adaptability to varying PDE configurations without fine-tuning, it may come at the cost of a substantial increase in model parameters, which could limit scalability and efficiency in more complex scenarios. Specifically, the method's reliance on a separate neural network for each basis function, especially when dealing with higher-dimensional problems or more complex basis sets, could lead to a combinatorial explosion in the number of parameters. This increase in parameters may not only increase the computational cost of training but also the memory footprint of the model, potentially hindering its deployment on resource-constrained devices. The paper lacks a thorough discussion on how the number of basis functions scales with the complexity of the PDE and how this impacts the overall parameter count and computational efficiency.

**2. Extension to Non-Linear and Complex PDEs**: The current method is demonstrated on relatively straightforward cases involving convection, heat, and reaction equations, which are linear PDEs in terms of their derivative terms. However, extending this approach to more complex, non-linear PDEs, such as the Burgers' or Navier-Stokes equations, would be challenging. These equations introduce additional complexities, such as non-linearity and turbulent behavior, which may not be easily captured by the current model’s parameterization and scaling methods. For instance, the method's reliance on a polynomial model to represent the solution might not be sufficient to capture the intricate dynamics of turbulent flows, where the solution can exhibit chaotic behavior and rapid changes in space and time. This limitation suggests potential difficulty in generalizing the method to more complex or chaotic systems, which restricts its broader applicability. The paper should address the limitations of the polynomial model in capturing the complex solution manifolds of non-linear PDEs and propose potential solutions to overcome these challenges.

### Questions
Please refer to Weaknesses section.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces two methods, Fourier series decomposition and the scaling method for PINNs to solve linear PDEs and one extra method, polynomial model, to solve potentially nonlinear PDEs. The Fourier series decomposition method pretrains sufficiently many basis PINNs which approximate the solution of the given linear PDE with initial condition being a Fourier basis function (sin, cos with given frequencies), so that when a new initial condition comes with the same PDE, they only need to apply Fourier series decomposition and linearly combine the corresponding PINNs’ solution with the Fourier coefficients. The scaling method apply change of variables to convection equation to reduce the coefficient $\beta$ to 1 (the canonical convection equation) so that the convection coefficient is small enough for MLP to learn the solution, then the method scales back the PINN’s solution to get the original solution. The polynomial model turns the PDE (linearity does not matter) into a polynomial regression problem and use neural network to predict coefficients of the polynomial.

### Strengths
- The paper is overall written clearly.

- The motivation is clear; the extension of PINNs into parameterized PDEs has yet not been studied extensively.

- The proposed method in some sense inherits the idea of reduced-order modeling (e.g., reduced-basis method), which is known to be a very-well established method.

### Weaknesses
 - the Fourier series decomposition is a direct application of linearity of the three linear PDEs, and it is not expected that such method works for nonlinear equations (Burgers, etc.), so the application of this method can be still restricted. In 2D spatial domain, Fourier basis works only for rectangular domains with periodic boundary condition, leaving Poisson equation on other geometries of boundary (triangle, circle) and other types of boundary condition (Dirichlet, Neumann, etc.) unsolvable, while vanilla PINN works fine since it doesn’t need the Fourier basis on these domains. Going to a more general domain geometry or going to 3D domain could be very challenging.

- Polynomial method seems to be also restrictive. It is unclear how the method would provide prediction quality in extrapolation in the parameter space. Also, the number of polynomials seems to be fixed, which could be a strong modeling assumption. Lastly, did the authors consider different types of polynomials such as orthogonal polynomials? and how to handle the high-dimensionality?


- The scaling method (rebranding the change of variable) sounds a bit ad-hoc, which is designed for one class of equation only excluding Poisson). This method cannot be generalized to combined types of linear PDE, such as diffusion-reaction or diffusion-convection-reaction equations, which are the typical cases in PINN applications.


- Numerical experiments: Continuing from the previous comment, the numerical experiments do not include the cases with PDE equations such as diffusion-reaction or diffusion-convection-reaction equations. 

- The numerical experiments are performed on rather a simple side, for example, the convection equation with $beta <=10$. The paper could have more impact if the method is employed on a rather hard side of the settings. 

- As mentioned above in the polynomial method, it is unclear if the paper has performed tests regarding extrapolation in the parameter space / IC/ BC. 

- Some ablation studies would be needed: The effect of number of Fourier bases, training and test setup (e.g., the number of different conditions to build bases), the number/type of polynomials, etc.

- Missing references: There have been some papers tackling issues in solving parameterized PDEs with PINNs. Some comparisons and/or discussions are needed. 

  - Cho et al, Hypernetwork-based meta-learning for low-rank physics-informed neural networks, NeurIPS, 2023

  - Cho et al, Parameterized Physics-informed Neural Networks for Parameterized PDEs, ICML, 2024

### Questions
Please refer to the weaknesses for the questions.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
To me this paper addresses the retraining problem in PINNs for solving PDEs. The authors introduce three methods: a basis solution approach for linear PDEs with variable conditions, a polynomial model for variable parameters, and a scaling method for certain PDEs. These techniques establish direct connections between PDE solutions and their configurations, enabling real-time inference without retraining. Theoretical analysis and extensive experiments demonstrate that these methods achieve comparable or better accuracy than traditional PINNs, while being significantly faster (often less than half-second inference time) and more effective in inverse problems. I like how this work makes PINNs more practical for real-time applications in scientific computing and engineering design.

### Strengths
1 The paper presents mathematically sound methods to directly connect PDE solutions with boundary conditions, sources, and parameters, addressing a key limitation of existing PINNs.
2.Theoretical foundation: The authors provide rigorous mathematical analysis and proofs for their proposed methods, including error bounds.
3.Computational efficiency: The methods achieve real-time inference (less than half a second in most cases) for both forward and inverse problems, significantly outperforming vanilla PINNs and meta-learning approaches.
4.Accuracy: The proposed methods demonstrate comparable or superior accuracy to vanilla PINNs in forward problems and significantly better performance in inverse problems.
5.Versatility: The approach is applied to various types of PDEs, including linear and nonlinear equations and includes extensive comparisons with state-of-the-art methods across multiple PDE benchmarks.

### Weaknesses
1. Limited scope: I feel like that the methods are primarily demonstrated on relatively simple PDEs and domains, although this is understandable. 
2.Dependency on analytical insights: The approach relies heavily on analytical understanding of the PDEs, which may limit its applicability to more complex systems where such insights are not readily available.
3.Scalability concerns: It's unclear how well the methods would scale to very high-dimensional problems or systems of coupled PDEs. I feel like in general PINN's scalability is an issue.
4.Limited exploration of nonlinear PDEs: While the Reaction equation is considered, the treatment of more general nonlinear PDEs is not extensively explored.

### Questions
1. What are the limitations of your methods for highly nonlinear PDEs?
2. How does the performance degrade as PDE complexity increases? Is there a threshold where meta-learning approaches become more effective?
3. How does your approach extend to PDEs with complex geometries or higher dimensions?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper addresses one limitation of PINNs in solving PDEs: the need for retraining when parameters or boundary/initial conditions change. The authors propose three new methods to directly connect PDE solutions with their configurations: a basis solution method for linear PDEs, a polynomial model for variable parameters, and a scaling method for certain PDEs. These approaches enable real-time inference without retraining, potentially allowing for faster, more efficient PDE solving in many-query scenarios. The methods are tested on several PDEs. Results indicate comparable accuracy to traditional PINNs but with significantly faster inference times, and improved performance over meta-learning PINNs. Theoretical analysis is provided to establish error bounds.  While the work shows some promises, its generalizability to more complex PDEs and real-world scenarios may require further investigation.

### Strengths
1. The proposed approaches are vaildated by several examples, and the results are promising  in terms of speed and accuracy compared to existing methods.

2. The authors provide some theoretical analysis to support their methods.

### Weaknesses
1. A significant limitation of the proposed methods is their strong dependence on the specific structure of the PDEs and their associated boundary and initial conditions. In these cases, the solution spaces are effectively reduced to finite-dimensional spaces, where all solutions can be expressed as simple transformations of basis functions within the solution space. This approach, while effective for the presented examples, raises questions about its generalizability. It remains unclear how these methods could be extended, even in principle, to more complex PDEs or realistic applications that may not conform to such simplified structures. The reliance on a Fourier basis for linear PDEs, while efficient for problems with periodic boundary conditions, may not be suitable for more general boundary conditions or complex geometries. Furthermore, the polynomial model approach, while applicable to parameter variations, does not address the fundamental issue of handling diverse initial conditions for nonlinear PDEs, as the superposition principle does not hold in such cases. For instance, the proposed solution form for the Burgers' equation, $u(x, t) = \sum_{i=0}^9 a_i u_i^{\cos }(x, t)+b_i u_i^{\sin }(x, t)$, does not satisfy the PDE due to the nonlinear term $u u_x$, rendering the approach inapplicable without significant modifications.

2. The paper lacks a crucial comparison with physics-informed neural operators, such as PI-DeepONet and PI-FNO. Given that the primary goal of this work is to address the limitations of PINNs in solving parametric PDEs, these physics-informed neural operator methods are highly relevant as they can also potentially address the same issues with PINNs that the authors are targeting. The absence of comparisons against these important baselines leaves a significant gap in the evaluation of the proposed methods' effectiveness and novelty relative to the current state-of-the-art in the field. The reported performance of PI-DeepONet, with errors exceeding 40% for relatively simple problems, is also unexpected and inconsistent with typical results reported in the literature. This discrepancy raises concerns about the experimental setup and the validity of the reported comparisons.

### Questions
1. Given the limitations discussed, could the authors elaborate on potential strategies to generalize their methods to more complex PDEs? Specifically:
    * For a general linear PDE system with non-zero initial and boundary conditions, how might one decompose the solution into a sum of basis solutions?
   * Consider a simple nonlinear PDE like the Burgers' equation, u_t + u u_x - ν u_xx = 0. How could the proposed methods be applied to learn the mapping from initial conditions to solutions at a given time t?


2. Based on the numerical problem setups presented in the paper, it appears that solving a finite number of PDEs would suffice. In this context, what advantages do the proposed methods offer over direct numerical solvers? Unlike typical PINN method papers that may provide novel insights in PINNs theory and training, this work seems to construct specific PDE problems and solve them using PINNs as a tool. Could the authors clarify the benefits of their approach compared to conventional numerical methods in these scenarios?

3. For Table 2, could the authors provide clarification on the reported inference time for vanilla PINNs? Does this represent the inference time after training the PINN models, or does it include the training time? If it denotes only the inference time, the reported values seem unexpectedly slow for what should be a straightforward model evaluation.

### Soundness
2

### Presentation
2

### Contribution
2
