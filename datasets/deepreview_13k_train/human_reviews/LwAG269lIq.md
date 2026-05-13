# Data-Driven Discovery of PDEs via the Adjoint Method

- Decision: Reject
- Scores: 3, 3, 3, 3

## Abstract
In this work, we present an adjoint-based method for discovering the underlying governing partial differential equations (PDEs) given data. The idea is to consider a parameterized PDE in a general form and formulate a PDE-constrained optimization problem aimed at minimizing the error of the PDE solution from data. Using variational calculus, we obtain an evolution equation for the Lagrange multipliers (adjoint equations) allowing us to compute the gradient of the objective function with respect to the parameters of PDEs given data in a straightforward manner. In particular, we consider a family of parameterized PDEs encompassing linear, nonlinear, and spatial derivative candidate terms, and elegantly derive the corresponding adjoint equations. We show the efficacy of the proposed approach in identifying the form of the PDE up to machine accuracy, enabling the accurate discovery of PDEs from data. We also compare its performance with the famous PDE Functional Identification of Nonlinear Dynamics method known as PDE-FIND \cite{rudy2017data}, on both smooth and noisy data sets. Even though the proposed adjoint method relies on forward/backward solvers, it outperforms PDE-FIND for large data sets thanks to the analytic expressions for gradients of the cost function with respect to each PDE parameter.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors claim that they can discover some PDE via an adjoint-based method.

### Strengths
The topic looks very interesting.

### Weaknesses
The manuscript has not been well-written, so that the reader cannot find their motivation clearly.
The theoretical part has been shown rigorously.
The experiment part: description not clear

### Questions
Hopefully, the authors can make your contribution clearly and make your experiment and theories to test your results.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper presents a method for reconstructing a parameterized partial differential equation (PDE) from observed data using the adjoint method. The authors claim that their approach offers a new perspective on PDE reconstruction by leveraging adjoint-based optimization, demonstrating the method on simple examples and show better performance compared to the well known PDE-FIND.

### Strengths
The paper is generally well-written, with clear explanations of the methodology and a solid foundation in the adjoint approach. The derivations are technically sound and should be accessible to readers familiar with inverse problems and PDEs.

### Weaknesses
(1) The approach presented here is relatively incremental, as the reconstruction of parameterized PDEs has been extensively studied within the inverse problem community for several decades. Many of the concepts explored, particularly adjoint-based parameter estimation, are already well-established. The paper would benefit from a more explicit discussion of how this work advances or differs from existing methods in the literature on PDE-constrained optimization and inverse problems. Specifically, the paper lacks a clear articulation of the novelty in applying the adjoint method to this specific problem of PDE discovery, beyond simply stating that it hasn't been done before. A more detailed comparison with existing methods, highlighting the advantages and disadvantages of the proposed approach in terms of computational efficiency, accuracy, and robustness, is needed.
(2) The demonstration example is limited to simple lower dimensional problems, which may not be sufficient to convincingly illustrate the method’s robustness or scalability to higher-dimensional, real-world PDEs. Given the computational efficiency implied by the adjoint method, testing on a more challenging, higher-dimensional example or a PDE with more complex dynamics would strengthen the paper. For example, the method could be tested on a 3D fluid flow problem or a system of coupled PDEs with non-linear terms to better demonstrate its applicability to real-world scenarios. This would also allow for a more thorough evaluation of the method's effectiveness in a broader range of realistic scenarios, including cases with noisy or incomplete data.
(3) The paper would benefit from a comparative analysis with other state-of-the-art methods for PDE reconstruction. This comparison could help clarify the unique contributions and limitations of the adjoint-based approach relative to current methods in data-driven PDE reconstruction. The comparison should not only focus on the final accuracy but also on the computational cost, convergence rate, and sensitivity to hyperparameter tuning. A more thorough comparison would help to understand the practical advantages and disadvantages of the proposed method.

### Questions
(1) Can you provide more complex examples in high dimensional space?
(2) Can you provide some a posteriori analysis analysis regarding the learning performance with respect to the given data or type of PDEs?
(3) Can you derive some well posed-ness of the parametrization of PDE? i.e, if I provide two similar parameterized PDEs, how about the learning performances regarding interpolation and prediction?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper considers the problem of identifying the parameters of a system of PDEs based on measurement data. The proposed method fits the solution of the PDE to the data while adapting its parameters. It uses the adjoint method that combines a data goodness-of-fit objective with a PDE satisfaction constraint using a Lagrangian formulation. Using variational techniques, it is then possible to obtain evolution equations for those weights (multipliers), which then allow the gradient objective to be computed with respect to the PDE parameters. The proposed method is compared with PDE-FIND for a number of PDEs in the standard setting as well as when the temporal data is coarse and when the data is noisy.

### Strengths
- The proposed method archives good results on the considered PDEs considered compared to PDE-FIND
- The experiments consider relevant settings, including coarse temporal resolution, noisy data, and ill-posed tasks
- Using the adjoint method, it is possible find straightforward algorithms based on gradient descent

### Weaknesses
1. The algorithms proposed in the work implicitly (i) solve the forward PDE (1), which can be challenging and time consuming (line 242); (ii) solve the adjoint PDE model (7), which again can be challenging and time consuming (line 243); and (iii) compute gradients of the adjoint variables $\lambda$, which are only know implicitly through (7) (line 244). The manuscript does not thoroughly discuss how this affects the computational complexity of the proposed method and whether the choice of solution algorithm could affect the performance of the proposed method. This is particularly important since other methods, such as PDE-FIND, do not appear to require such explicit forward evolutions. A direct comparison of computational cost, either in terms of complexity analysis or run time, with PDE-FIND is missing. The fact that the adjoint method may achieve better accuracy at a potentially higher computational cost is a crucial point that needs to be addressed. It is not clear from the manuscript how the proposed method differs from classical adjoint methods, proposed originally in the context of design or shape optimization (see, e.g., Jameson 2003). The text only mentions that “unlike the usual use of PDE-constrained adjoint optimization where the governing equation is known, in this paper we are interested in finding the form along with the coefficients of the PDE given data.” Nevertheless, the parameters of the PDE can be mapped directly to design parameters used in traditional adjoint methods. As such, there doesn’t seem to be any challenge requiring substantial contributions in the setting of this paper.

2. The paper is not clearly written. There are several typos (“Eq. equation” in lines 201, 215, 376, 482, 1172) and odd uses of language (“Here, $x(k)$ is coordinates”; ) that make it hard to follow. Many elements are either undefined or defined implicitly/informally. For instance, in (2) are those gradient products or an iterated differentiation (as in multi-index differentials from Sobolev spaces)? What is meant by “semi-discrete total variation of C” (line 176)? The definition is given without a reference or explanation. Additionally, the structure of the experiments is not clear as Section 3 named “Results” is followed by Section 4,5,6 named “Partial observations in time”... all containing experimental results as well. This lack of care in the writing renders the paper confusing for the reader.

3. Many results are provided without derivations or references. Since their definitions are incomplete, it is impossible to judge their validity. For instance, the derivations of (4) and (6) are only informally explained. And since nowhere is it defined in which functional space in which the solution $f$ of (1) must be in, it is impossible to judge the correctness of (4), even if the reader had to assume the smoothness/differentiability of $\lambda$. Additionally, since conditions such as $\lambda(x,t) \to 0$ for $x \in \partial\Omega$ are not justified and without knowing the functional (metric) space in which $\lambda$ is optimized, it is impossible to guarantee its differentiability in (4) and (6). Similar comments apply to the derivation of (7)-(8) from (6). The informal statement that "clearly, we are assuming that all considered derivatives of $\lambda$ exist" is not a rigorous justification, especially since an overly smooth $\lambda$ imposes stronger restrictions on the space of (weak) solutions considered.

4. The manuscript only considers very simple PDEs. In particular, the main text only tackles the 1D heat equation with D=1, the 1D Burgers equation, and a simple 1D wave equation. These are low-dimensional, simple first-order equations with very few parameters to fit. In fact, the proposed method does not appear to be able to handle PDEs beyond linear, first order in time (particularly since it must solve (1) explicitly). In particular, it does not consider very overparametrized models either (large $p$ or $d$). Hence, the performance of the method in PDEs whose solutions are challenging or where there is substantial uncertainty on the model (large $p$ or $d$) is not tested.

5. Point (4) is particularly critical given that the proposed method is only compared against one baseline (PDE-FIND) which is already somewhat dated (2017). Many other baselines are available, in particular, those detailed in the introduction. It is unclear why none were used in the experiments.

6. There is only very limited discussion on the use of l2 regularization. Particularly since it is well-known from polynomial fitting that the l2-norm is not well-adapted to find sparse solutions, i.e., where many values are 0. That is why, e.g., Brunton et al. 2016 use the l1 norm. While the thresholding heuristic employed by the paper is reminiscent of iterative hard thresholding (IHT) methods from compressed sensing (see, e.g., Blumensath and Davis, Applied Computational Harmonic Analysis, 2009) it does not inherit the same guarantees or theoretical advantages. In fact, this relation is not even mentioned in the manuscript.

### Questions
See Weakness above. We include here some additional minor issues:

1. When considering sensitivity to noise (line 411), the noise variance is specified in percentage. With respect to what? Is it an SNR?
1. Where does the normalization of the integral in (3) come from? This doesn’t seem to make sense given that the manuscript considers a regular grid.
1. When discussing the learning rate, it is mentioned that “the gradient of the cost function is most sensitive to the highest order terms of the PDE.” Why is that the case?
1. When defining $f^*$ on line 121, shouldn’t it be $f^*: \Omega \times [0,T] \to \mathbb{R}^N$? As it is, the desired solution is only on $\mathcal{G}$. How would that be consistent with, e.g., coarser time grids?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
An adjoint-based equation discovery framework is proposed in this paper to discover the underlying governing partial differential equations (PDEs) of physical systems. The proposed method initializes a general PDE by considering derivatives and polynomials of the derivatives up to a finite degree. A loss function is formed by incorporating the error between the prediction from the general PDE and the training labels and the corresponding adjoint equations. After that, a PDE-constrained optimization problem is solved to estimate the parameters of the initial PDE model, such that the solution of the general PDE will accurately approximate the training labels. The successful optimization yields coefficients of only the relevant derivatives to take significant values, thereby uncovering the underlying governing equation.

### Strengths
1. The idea of using adjoint equations to uncover underlying equations is interesting, and it seems to be new in the literature. 
2. The theoretical derivations and analysis do a good job of explaining the key concepts of the framework. 
3. Even in partial observations, when data at fine mesh is not available, the adjoint equations can discretize the general PDE on a finer mesh and, therefore, outperform other methods in the low data limit.

### Weaknesses
1. The proposed framework is motivated by assuming a general PDE, which contains derivatives and their polynomials up to a certain degree. This is equivalent to basis functions in regression-based equation discovery frameworks, which is one of the major limitations of the basis-dependent discovery methods. Since, in an unknown scenario, the knowledge about the underlying physics will be minimal, one may need to consider a large number of basses/derivatives. In most of the examples, the authors consider only up to 3rd-order derivatives and their polynomials. Authors should consider a higher order of derivatives and polynomials, including cross-terms and mixed partial derivatives, to check the performance of their framework, both accuracy and computational efficiency. The interaction between these terms can lead to significant correlations, hindering the identification of the true governing equation and potentially causing overfitting, especially when extrapolating beyond the training data.
2. The proposed framework closely resembles the PINN-SR algorithm. Therefore, a comparison with PINN-SR algorithms is necessary to gauge the effect of the adjoint equations. The similarity lies in the use of basis functions to represent the PDE, and the optimization process to identify the coefficients. While the response modeling part of PINN-SR might be irrelevant here, the core idea of identifying parsimonious forms using basis functions is shared, making a direct comparison crucial.
3. The motivation for the equation discovery architecture is a little convoluted. The authors state that since data-driven simulators fail to learn the exact physics of dynamical systems, they fail to extrapolate beyond the training regime. Thus, we need an equation discovery framework, which post-discovery can be coupled with any standard numerical methods to obtain accurate predictions. While the second statement is true, it can be argued that after the discovery of a governing equation, one can still train a data-driven or physics-informed machine learning emulator for accelerating computational simulations. Therefore, the motivation needs to be reworked.
4. The Bayesian class of equation discovery algorithms also does a good job in distilling governing equation equations from data, particularly in noisy and low-data limits [1-3]. This paper should have discussed these frameworks. A comparison with a few such frameworks would further benefit the content of this paper.



### Questions
Please see below questions on the paper content:
1. line 87. PINN-SR uses the Adam optimizer, which can process data in batches. Thus, why do authors feel that PINN-SR will not scale well with the size of the data set?  
2. line 135. The vector $\boldsymbol{f}^p$ may be missing a comma.
3. line 189. Does the framework work only for zero boundary conditions? 
4. line 218. How $\sigma$ is selected. Consider an example of the Navier-Stokes equation, where the viscosity can be in the order of $10^{-4}$ to $10^{-5}$. In such cases, the proposed algorithm will discard the relevant terms.
5. line 282. Is this method applicable to time-independent systems like Darcy and Poisson's equations? If applicable, how averaging of gradients in algorithm 2 will be done in the absence of the time component.
6. Fig. 1(c). It is intriguing to see that the error increases with an increase in data in both methods.
7. Fig. 1(d). Since the proposed method uses a forward solver in the loop, is it not the computational time supposed to increase with increasing training samples?
8. Eq. (13-14). The authors show that even in ill-posed problems, the proposed method can provide an alternate sparse equation. However, estimating the error and visually observing the solution fields before concluding on the accuracy would be best. 

**Limitations:**
The proposed framework does not show discovery from irregular observations (both in time and space). This should be included in the limitations.

### Soundness
3

### Presentation
3

### Contribution
2
