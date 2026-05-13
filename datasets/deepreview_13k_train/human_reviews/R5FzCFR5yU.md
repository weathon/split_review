# Hybrid Numerical PINNs: On the effectiveness of numerical differentiation for non-analytic problems

- Decision: Reject
- Scores: 1, 3, 6

## Abstract
This work demonstrates that automatic differentiation has strong limitations when employed to compute physical derivatives in a general physics-informed framework, therefore limiting the range of applications that these methods can address. A hybrid approach is proposed, combining deep learning and traditional numerical solvers such as the finite element method, to address the shortcomings of automatic differentiation. This novel approach enables the exact imposition of Dirichlet boundary conditions in a seamless manner, and more complex, non analytical problems can be solved. Finally, enriched inputs can be used by the model to help convergence. The proposed approach is flexible and can be incorporated into any physics-informed model. Our hybrid gradient computation proposal is also up to two orders of magnitude faster than automatic differentiation, as its numerical cost is independent of the complexity of the trained model. Several numerical applications are provided to illustrate the discussion.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
In this manuscript, the authors propose using numerical differentiation, instead of auto-differentiation, to deal with the physical derivatives of neural networks. The authors claim that numerical differentiation is faster than auto-differentiation. The authors also claim that it can solve several problems in the existing PINN framework. The authors conduct several numerical experiments in some cases.

### Strengths
It's really good that the authors attempt to find another way of doing differentiation in PINN. As stated in the manuscript, most works in this area focus on the network architecture or the loss function, but few focus on improving the pipeline defined by PINN or Neural Operator. Sometimes, it's really important to jump out from the existing framework to find a better way to solve the problem.

### Weaknesses
While it is important to identify some fundamental problems in the existing framework, the reviewer suggests that the author should check if these problems can be perfectly solved by the existing method. If so, the authors should first learn these existing methods. In this manuscript, the authors claim that the existing PINN framework has two weaknesses: 1. Auto-differentiation can not deal with tabulated coefficients, and 2. Auto-differentiation can not deal with the network using a scalar field as input. However, both of them can be perfectly solved by existing methods. For the first problem, one can use a smooth enough function to fit the tabulated coefficients and use this function as the coefficient function. For the second problem, defining the JVP/VJP function of the scalar field can perfectly solve the problem, which is available in most AutoDiff frameworks. Thus, the authors should first learn these methods and compare the proposed method with these solutions, which is missed in the current manuscript.

### Questions
Suggestions are listed in weakness.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors highlight certain limitations of automatic differentiation in computing PDE residuals used in physics-informed training. The solution is to compute residuals with classical discretization instead and use automatic differentiation only to compute derivatives with respect to neural network parameters.

### Strengths
The article is easy to read. The motivation of the authors and the experiments conducted are clearly explained. I also would like to thank the authors for reporting the time needed to obtain a solution with PiNN and by preconditioned conjugate gradient. This level of honesty feels refreshing.

### Weaknesses
There are two problems:
1. Major literature omissions
2. Examples showing fail of automatic differentiation are contrived

I will elaborate on them in the next section.

1. **Major literature omissions.**

   Many works have been available for quite some time that pursue the same research direction as the one chosen by the authors. At the very least authors should mention these works, better, an extended discussion, supported by numerical results, should be added that explicitly compares the method proposed in this work with the related ones. Below one can find several examples of articles that are related to the content of a current contribution.

   a. Finite element method-enhanced neural network for forward and inverse problems, https://amses-journal.springeropen.com/articles/10.1186/s40323-023-00243-1. Here finite element discretization is combined with a neural network operating over the discretized grid.

   b. Physics Informed Neural Network using Finite Difference Method, https://ieeexplore.ieee.org/abstract/document/9945171. In this paper, the authors use finite difference approximation with PiNNs.

   c. Hybrid Finite Difference with the Physics-informed Neural Network for solving PDE in complex geometries. https://arxiv.org/abs/2202.07926. Again, in this paper finite difference method is applied to enforce residual.

   d. hp-VPINNs: Variational Physics-Informed Neural Networks With Domain Decomposition. https://arxiv.org/abs/2003.05385 - the well-known article where authors use neural networks for trial space and polynomials for test space. This is again an example of classical discretization applied in conjunction with PiNNs.
   
   I suggest authors comment on the articles above and their relation to the content of a current contribution. Besides that, I would recommend performing a more thorough literature review to include other relevant contributions.

2. **Examples showing failure of automatic differentiation are contrived.**

   The authors demonstrate three examples of when automatic differentiation fails. I will argue that all of them are highly artificial.

   **Tabulated data.**

   In this example diffusion coefficient $\alpha(x)$ appears in the conservative formulation of ODE $-\frac{d}{dx} \left(\alpha(x) \frac{d u}{dx}\right) = 0$ is known only in selected set of points. If one naively computes residual by automatic differentiation in these points, the resulting PiNN loss leads to a completely wrong solution. I have several objections:
   1. Under this scenario classical discretization method is also not defined unless one adapts the grid to the special locations where $\alpha(x)$ is known. Does it mean this example is problematic for classical methods too?
   2. A usual solution for this situation is known as interpolation and in more complex situations as data assimilation. This problem is well-studied and can be solved by various means. Can the authors try, say, cubic splines and report the result of PiNN training? To do that one defines $\alpha(x)$ as a function that performs cubic spline interpolation given its values at the known points, after that automatic differentiation can be used to compute derivatives. For that to work interpolation should be differentiable. Alternatively, derivatives can be estimated and tabulated. After that one can rewrite the equation in non-conservative form and run automatic differentiation for other parts of the residual.
   
   **Strong imposition of Dirichlet boundary conditions.**

   In this example, authors construct a mask that defines a physical domain and use it to exactly impose Dirichlet boundary conditions. There is a natural way to enforce boundary conditions for PiNNs exactly. The techniques are explained in "Exact imposition of boundary conditions with distance functions in physics-informed deep neural networks", https://arxiv.org/abs/2104.08426. One way to do that is to use Floater's mean value coordinates to form a smooth distance function for a given boundary and use, say, RBF (or transfinite interpolation, linear interpolation, or ordinary least squares, etc) to enforce the desired value on the boundary. The final ansatz reads $NN(x)\phi(x) + g(x)$, where $\phi(x)$ is smooth and vanishing on the boundary and $g(x)$ reproduces boundary conditions exactly.
   
   **Enriched input to the model.**

   In this hypothetical scenario, the authors suggest that it would be hard to provide the model with additional inputs and keep using automatic differentiation. The authors correctly mentioned that this is done in the domain of operator learning. The reason why automatic differentiation is hard is as follows "However, few works directly use this class of operators within a physics-informed framework. One of the reasons for the difficulty of implementing physics-informed neural operators is a direct consequence of Theorem 3.2: the PDE parameter given as input to the model should be constructed analytically to compute the PDE residuals with AD, therefore preventing the use of these models to real-life problems. For instance, Wang et al. (2021b) presented results based on analytic data, and Li et al. (2024) proposed function-wise differentiation as an alternative to AD." I find this presentation problematic:
   1. DeepONet can be trained on tabular data either with interpolation or when the formulation is not conservative, e.g., in the cited DeepONet paper this is the case for all PDEs considered: Burgers, diffusion-reaction, advection, eikonal.
   2. The reason FNO is not using automatic differentiation is that its process functions are explicitly discretized on a uniform grid. In other words, FNO is a function over functions. It is not possible to apply automatic differentiation because these functions do not have computation graphs in the usual sense.

To summarise, in my opinion, all given examples of automatic differentiation failure are highly unnatural. Any practitioner with basic knowledge of automatic differentiation will never try to arrange computations as the authors suggest. It seems to me that these modes of failure are too obvious and easily avoidable.

I am ready to change my opinion, if authors come up with convincing arguments, so I encourage authors to address my concerns in the rebuttal.

### Questions
I think it, is more instructive to focus on major problems. Typos and minor issues with the presentation will be completely ignored.

1. **Major literature omissions.**

   Many works have been available for quite some time that pursue the same research direction as the one chosen by the authors. At the very least authors should mention these works, better, an extended discussion, supported by numerical results, should be added that explicitly compares the method proposed in this work with the related ones. Below one can find several examples of articles that are related to the content of a current contribution.

   a. Finite element method-enhanced neural network for forward and inverse problems, https://amses-journal.springeropen.com/articles/10.1186/s40323-023-00243-1. Here finite element discretization is combined with a neural network operating over the discretized grid.

   b. Physics Informed Neural Network using Finite Difference Method, https://ieeexplore.ieee.org/abstract/document/9945171. In this paper, the authors use finite difference approximation with PiNNs.

   c. Hybrid Finite Difference with the Physics-informed Neural Network for solving PDE in complex geometries. https://arxiv.org/abs/2202.07926. Again, in this paper finite difference method is applied to enforce residual.

   d. hp-VPINNs: Variational Physics-Informed Neural Networks With Domain Decomposition. https://arxiv.org/abs/2003.05385 - the well-known article where authors use neural networks for trial space and polynomials for test space. This is again an example of classical discretization applied in conjunction with PiNNs.
   
   I suggest authors comment on the articles above and their relation to the content of a current contribution. Besides that, I would recommend performing a more thorough literature review to include other relevant contributions.

2. **Examples showing failure of automatic differentiation are contrived.**

   The authors demonstrate three examples of when automatic differentiation fails. I will argue that all of them are highly artificial.

   **Tabulated data.**

   In this example diffusion coefficient $\alpha(x)$ appears in the conservative formulation of ODE $-\frac{d}{dx} \left(\alpha(x) \frac{d u}{dx}\right) = 0$ is known only in selected set of points. If one naively computes residual by automatic differentiation in these points, the resulting PiNN loss leads to a completely wrong solution. I have several objections:
   1. Under this scenario classical discretization method is also not defined unless one adapts the grid to the special locations where $\alpha(x)$ is known. Does it mean this example is problematic for classical methods too?
   2. A usual solution for this situation is known as interpolation and in more complex situations as data assimilation (a good example is https://www.ecmwf.int/en/forecasts/dataset/ecmwf-reanalysis-v5). This problem is well-studied and can be solved by various means. Can the authors try, say, cubic splines and report the result of PiNN training? To do that one defines $\alpha(x)$ as a function that performs cubic spline interpolation given its values at the known points, after that automatic differentiation can be used to compute derivatives. For that to work interpolation should be differentiable. Alternatively, derivatives can be estimated and tabulated. After that one can rewrite the equation in non-conservative form and run automatic differentiation for other parts of the residual.
   
   **Strong imposition of Dirichlet boundary conditions.**

   In this example, authors construct a mask that defines a physical domain and use it to exactly impose Dirichlet boundary conditions. There is a natural way to enforce boundary conditions for PiNNs exactly. The techniques are explained in "Exact imposition of boundary conditions with distance functions in physics-informed deep neural networks", https://arxiv.org/abs/2104.08426. One way to do that is to use Floater's mean value coordinates to form a smooth distance function for a given boundary and use, say, RBF (or transfinite interpolation, linear interpolation, or ordinary least squares, etc) to enforce the desired value on the boundary. The final ansatz reads $NN(x)\phi(x) + g(x)$, where $\phi(x)$ is smooth and vanishing on the boundary and $g(x)$ reproduces boundary conditions exactly.
   
   **Enriched input to the model.**

   In this hypothetical scenario, the authors suggest that it would be hard to provide the model with additional inputs and keep using automatic differentiation. The authors correctly mentioned that this is done in the domain of operator learning. The reason why automatic differentiation is hard is as follows "However, few works directly use this class of operators within a physics-informed framework. One of the reasons for the difficulty of implementing physics-informed neural operators is a direct consequence of Theorem 3.2: the PDE parameter given as input to the model should be constructed analytically to compute the PDE residuals with AD, therefore preventing the use of these models to real-life problems. For instance, Wang et al. (2021b) presented results based on analytic data, and Li et al. (2024) proposed function-wise differentiation as an alternative to AD." I find this presentation problematic:
   1. DeepONet can be trained on tabular data either with interpolation or when the formulation is not conservative, e.g., in the cited DeepONet paper this is the case for all PDEs considered: Burgers, diffusion-reaction, advection, eikonal.
   2. The reason FNO is not using automatic differentiation is that its process functions are explicitly discretized on a uniform grid. In other words, FNO is a function over functions. It is not possible to apply automatic differentiation because these functions do not have computation graphs in the usual sense.

To summarise, in my opinion, all given examples of automatic differentiation failure are highly unnatural. Any practitioner with basic knowledge of automatic differentiation will never try to arrange computations as the authors suggest. It seems to me that these modes of failure are too obvious and easily avoidable.

I am ready to change my opinion, if authors come up with convincing arguments, so I encourage authors to address my concerns in the rebuttal.

### Soundness
1

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper addresses the limitations of automatic differentiation (AD) in PINNs for non-analytic PDEs. The authors propose a hybrid approach that combines numerical solvers with deep learning models to replace AD for gradient calculations. The proposed method enables the exact imposition of Dirichlet boundary conditions. The proposed approach is flexible and can be incorporated into any physics-informed model. Gradient computation is up to two orders of magnitude faster than automatic differentiation.

### Strengths
- **Addresses AD Limitations**. The proposed method addresses cases where AD fails, e.g., when the PDE coefficients do not have an analytic form, or when enriched input data is fed to the deep learning model. 
- **BC Imposition**. The proposed method allows strong constraints of Dirichlet BCs.
- **Scalability and Efficiency**. The proposed approach shows significant speedups in gradient computation compared to AD-based PINNs. The numerical cost is independent of the complexity of the trained model. 
- **Flexiblility**. The proposed approach is flexible and can be incorporated into any physics-informed model.

### Weaknesses
 - **Generalization**. The proposed work could handle 1D and 2D PDEs with Dirichlet BCs. Yet, whether it could generalize to higher dimensions or more complex BCs remains unknown. Specifically, the method's performance with 3D geometries and its ability to handle non-rectangular domains is unclear. The current experiments do not provide sufficient evidence to support claims of broad applicability.
- **Dependency on External Numerical Solvers**. The reliance on external numerical solvers, while potentially offering benefits in terms of accuracy for specific cases, introduces a dependency that may limit the method's flexibility and ease of use. The need to interface with external solvers adds complexity to the implementation and may not be practical in all scenarios.
- **Insufficient PINN Baselines**: The experiments do not thoroughly compare with SOTA neural operators (e.g., FNO, GNO), which are considered an important baseline for PINN-based neural routines. The lack of comparison with these methods makes it difficult to assess the true novelty and effectiveness of the proposed approach. It is not clear if the observed speedups are unique to the proposed method or if they could be achieved with existing neural operator methods.
- **Presentation**. The presentation of this paper could be further improved. There are also typos (e.g., Eq. (19) is not properly aligned). The paper lacks a clear explanation of the limitations of the proposed method and how it compares to existing approaches. The experimental setup and results could be presented more clearly and thoroughly.

### Questions
- How does the proposed method perform on 3D PDEs or larger-scale problems?
- Can the method handle more complex boundary types (e.g., Neumann, Robin) just as effectively?
- Handling of Nonlinear Operators: How well does the hybrid method generalize to nonlinear PDEs?

### Soundness
3

### Presentation
2

### Contribution
3
