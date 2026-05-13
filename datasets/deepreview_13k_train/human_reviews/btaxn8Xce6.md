# Astral: training physics-informed neural networks with error majorants

- Decision: Reject
- Scores: 5, 5, 6

## Abstract
The primal approach to physics-informed learning is a residual minimization. We argue that residual is, at best, an indirect measure of the error of approximate solution and propose to train with error majorant instead. Since error majorant provides a direct upper bound on error, one can reliably estimate how close PiNN is to the exact solution and stop the optimization process when the desired accuracy is reached. We call loss function associated with error majorant \textbf{Astral}: neur\textbf{A}l a po\textbf{ST}erio\textbf{RI} function\textbf{A}l Loss. To compare Astral and residual loss functions, we illustrate how error majorants can be derived for various PDEs and conduct experiments with diffusion equations (including anisotropic and in the L-shaped domain), convection-diffusion equation, temporal discretization of Maxwell's equation, and magnetostatics problem. The results indicate that Astral loss is competitive to the residual loss, typically leading to faster convergence and lower error (e.g., for Maxwell's equations, we observe an order of magnitude better relative error and training time). We also report that the error estimate obtained with Astral loss is usually tight enough to be informative, e.g., for a highly anisotropic equation, on average, Astral overestimates error by a factor of $1.5$, and for convection-diffusion by a factor of $1.7$.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper starts from the observation that the loss minimization used for pinns does not generally guarantee that the distance L2 of the approximated solution from the true solution is minimized. To overcome this problem, the authors propose new losses for PINNs, which are shown to bound the L2 distance. The authors then provide empirical evidence that these losses achieve lower relative L2 errors, particularly as the equation becomes more physically complicated.

### Strengths
- Bounding of new losses are clearly and consistently derived.
- Clear and pedagogical presentation.

### Weaknesses
 - The proposed solutions are specific to each equation, which limits the applicative scope of the results.
- Empirical results are not sufficiently convincing. Only a few examples show an improvement in errors, but in most cases this remains of the same order of magnitude. It is therefore unclear whether these improvements are significant, or simply the result of statistical or numerical fluctuations.
- As has already been shown in several series of works, what affects the lack of convergence of PINNs is the poor conditioning of the problem (see for example https://doi.org/10.1016/j.jcp.2021.110768 or https://arxiv.org/abs/2310.05801) and solutions have since been successfully proposed to correct this problem (see for example https://arxiv.org/abs/2302.13163 or https://arxiv.org/abs/2402.10680), with a significant impact both on the minimization of the classical loss, and on the minimization of L2 and even H1 errors.
- Finally, questions of generalizing PINNs to different losses have already been explored in detail by Siddhartha Mishra's students. We refer you, for example, to the dissertations by Tim De Ryck (https://www.research-collection.ethz.ch/bitstream/handle/20.500.11850/674112/dissertation_deryck.pdf?sequence=1) or Roberto Molinaro (https://www.research-collection.ethz.ch/bitstream/handle/20.500.11850/646749/Thesis%2813%29.pdf?sequence=1).
- At the beginning of section 2, a proper definition of error and residual would be suited.

### Questions
- Perhaps the improvements you've seen in your experiences come from improved conditioning of the problem. If so, this could be an interesting line of research, since as things stand, the proposed corrections require expensive computational corrections. So it would be interesting if you could provide an analysis of the NTK spectrum with classical loss and with your loss, following the work presented in https://doi.org/10.1016/j.jcp.2021.110768.

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The manuscript proposes alternatives to the common, residual-based loss functions used in physics-informed neural networks. The authors argue that certain functional a posteriori error estimators better match the error (measured in energy norm) than the standard PINN loss formulation. Numerical examples for a number of different equations are presented comparing the standard residual/PINN approach to the one using a posteriori error estimators.

### Strengths
- Moving away from strong formulations to first-order systems (the error majorants presented are not exactly first order systems, but relatively close) seems like a good idea.

- Good error estimators are useful in practice.

### Weaknesses
 - Novelty: Although the proposed loss functions are not exactly first-order system reformulations of the considered PDEs, they share a similar spirit -- no second derivatives are needed but instead auxiliary variables are introduced. However, first-order system formulations are not novel, not even for neural network based solution methods for PDEs, see for example the works of [Cai, arXiv:1911.02109] or [Schwab, arXiv:2409.20264]. So I believe it is crucial to understand if the advantages of the proposed loss functions are due to the reformulation as a first-order system or if they are specific to the proposed losses. Can the authors comment on that? The advantages of first-order systems that I have in mind are: better conditioning than PINN type losses (thinking in terms of FEM results), and the fact that only first derivatives need to be computed. 

- Numerical results: The presented results confirm an improvement over the PINN baseline (in terms of errors), but it is not drastic. The relative L2 errors even seem to be comparable for the majority of the considered equations. Thus the value of the error majorants may lie mostly in what they are designed for -- estimating the error (after training) and the real question is: Are first-order systems (or Astral loss) computationally more efficient than the standard PINN formulation. This question is not sufficiently addressed in the present manuscript, and would need the experiments to focus on runtime and a thorough evaluation of automatic differentiation and implementation tricks. (For instance, it is often more efficient to compute the spatial derivatives in forward mode, incorporate tricks like the Forward Laplacian framework [ arXiv:2307.08214]  etc.)

- Recent work shows that PINNs are best optimized using second order methods. Improvement in accuracy can be drastic when changing from a stochastic first order method to a natural gradient or Gauss-Newton method see [Müller, arXiv:2302.13163] and [Rathore, arXiv:2402.01868]. It is important to take these recent developments into consideration for a thorough evaluation.

- More of a remark than a question: In Section 2.1, the authors give two motivating examples. The first one (the sinusoidal solution) shows that the function can be L2 close to the solution while having a large residual. The authors use this as an argument against residual based loss functions. I don't think this is fair, the same phenomenon happens for Astral loss. Can the authors comment?

- The standard PINN residual is, in fact, also an a posteriori error estimator for the error. Even for the error in the regularity spaces (H2 for Poisson etc). See the results in [Zeinhofer, arXiv:2311.00529]. Can the authors discuss why they prefer different a posteriori error estimators? I suppose it is because of unknown constants, but I would appreciate a clarification.

### Questions
- More of a remark than a question: In Section 2.1, the authors give two motivating examples. The first one (the sinusoidal solution) shows that the function can be L2 close to the solution while having a large residual. The authors use this as an argument against residual based loss functions. I don't think this is fair, the same phenomenon happens for Astral loss. Can the authors comment?

- The standard PINN residual is, in fact, also an a posteriori error estimator for the error. Even for the error in the regularity spaces (H2 for Poisson etc). See the results in [Zeinhofer, arXiv:2311.00529]. Can the authors discuss why they prefer different a posteriori error estimators? I suppose it is because of unknown constants, but I would appreciate a clarification.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes training physics-informed neural networks (PINNs) not via the usual residual-based loss, but via minimizing the so-called error majorant, a quantity that can be derived for certain classes of PDEs but that requires learning surrogate functions. The paper shows that the energy norm error correlates with the relative error of the PINN candidate function to a better degree than the residuals do. The results indicate that this approach of training PINNs results in smaller relative errors in many cases, and that further the runtime to achieve this error is smaller than for conventional training strategies.

### Strengths
The idea of training PINNs with the error majorant is a novel idea that, at least for some PDE classes, appears to be quite promising. The paper is generally well written and, for the most part, quite accessible. I particularly commend the intuitive motivation in Section 2.1, and the fact that a large number of PINNs (100) were trained for each setting, thus ruling out random effects. Some readers may consider the fact that the majorant must be derived/available for the considered PDE class as a shortcoming. In my experience with PINNs, in most forward problems, training often requires problem-specific adaptations (such as domain decomposition for large domains, collocation point weighting for stiff problems, etc.). I thus see the proposed approach as yet another such problem-specific adaption, but as an innovative one that leaves the established PINN paradigm of using the residual loss.

### Weaknesses
At some parts, the paper is not well written and somewhat unclear. For example, I think the authors switch between $\phi$ in Section 3, which is a general notation for the solution of the PDE, and problem-specific notation ($\phi$, $B$, $u$, etc.) in Section 4. In Section 5, the solution for diffusion is given as $u$, while in Section 4 it is given as $\phi$ (if I understand correctly). In Section 2.3, the surrogate function (flux) is denoted as $\tilde{F}$, while I think this corresponds to $\omega$ in Section 3. This makes reading the paper quite taxing. More importantly, it is sometimes not clear which functions are given and which are learned; and of those that are learned, which are the solution to the PDE ($\phi$) and which are surrogate functions ($\omega$). I thus suggest to homogenize notation.

Section 4 could be moved to the appendix, and the example in Section 2.3 or the general framework in Section 3 could be expanded. I think it must be more clear that surrogate functions need to be learned, which may be best accomplished by a schematic.

There are further considerations regarding the experimental section:
- In Section 5, it is not clear how the variational approach works. A few lines explaining this should be included in the revision.
- To judge the difficulty of the problems, I suggest to plot the solutions and PINN candidates for each of the considered problems.
- Table 1 could use vertical bars between Residual / Astral / Variational to better separate the results.
- Table 2 shows that the majorant is often a quite loose bound, contradicting the claims of the paper somewhat. Indeed, also for the mixed diffusion equation, the majorant is at least a factor of 3-4 of the natural energy error. It would be valuable to explain this phenomenon, and maybe also illustrate the error of the surrogate function required to approximate the natural energy error (e.g., the flux).
- Figure 1 requires axis labels.

Finally, I suggest that the paper undergoes proof reading by a native speaker, as some constructs read strangely and do not parse well.

### Questions
- What is the surrogate function $\omega$ for the elastoplasticity example in Section 4.4?
- How exactly does the variational approach work?
- What do the surrogate functions required for evaluating the natural energy error look like? What is the behavior of their errors?

### Soundness
3

### Presentation
3

### Contribution
4
