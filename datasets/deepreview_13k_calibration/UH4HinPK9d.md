# Provably Accurate ODE Forecasting Through Explicit Trajectory Optimization

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 5, 3

## Abstract
This work introduces a method to enable accurate forecasting of time series governed by ordinary differential equations (ODE) through the usage of cost functions explicitly dependent on the future trajectory rather than the past measurement times. We prove that the space of solutions of an $N$-dimensional, smooth, Lipschitz ODE on any given finite time horizon is an $N$-dimensional Riemannian manifold embedded in the space of square integrable continuous functions. This finite dimensional manifold structure enables the application of common statistical objectives such as maximum likelihood (ML), maximum a posteriori (MAP), and minimum mean squared error (MMSE) estimation directly in the space of feasible ODE solutions. The restriction to feasible trajectories of the system limits known issues such as oversmoothing seen in unconstrained MMSE forecasting. We demonstrate that direct optimization of trajectories reduces error in forecasting when compared to estimating initial conditions or minimizing empirical error. Beyond theoretical justifications, we provide Monte Carlo simulations evaluating the performance of the optimal solutions of six different objective functions: ML, MAP state estimation, MMSE state estimation, MAP trajectory estimation, MMSE trajectory estimation over all square integrable functions, and MMSE trajectory estimation over solutions of the differential equation.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper investigates statistical estimation of finite-dimensional parameter via maximum likelihood (ML), maximum a posteriori (MAP), and minimum mean squared error (MMSE) in the space of feasible ODE solutions when ODE is known and the only thing to be estimated is the unknown initial condition. The main insight is based on the classical results on the existence and uniqueness of the solutions of an ODE with Lipschitz continuous vector field with a continuously differentiable derivative, in which case there exists diffeomorphism  between the (finite-dimensional) state space and manifold of trajectiories with a finite time-horizon. Using the diffeomorphism, estimation is seen as a supervised learning problem for which ML, MAP and MMSE estimation can be formulated and solved. 

Using standard argument, this setting is directly extended to estimating unknown initial condition $x_0\in{\mathcal X}$, parameters $\theta\in\Theta$ and input functions $u\in{\mathcal U}$, whenever $\mathcal X$, $\Theta$ and $\mathcal U$ are finite dimensional.

One illustrative example of the Lotka-Voltera predator-pray system is presented.

### Strengths
Paper has a clear story-line. Statistical estimation of the ODE parameters from the observed trajectories is an important scientific problem.

### Weaknesses
While I find the story-line of the paper nice and useful for readers interested in learning dynamical systems, my overall impression is that the submission is this form is not appropriate for acceptance for the ICLR. The main reasons are the following:

1) __Theoretical aspect.__ Main results of the paper seam, at best, based on well-known arguments, if not already present is the same form in the existing literature. How the paper is presented, my impression is that novelty is highly overstated. Giving proper references for all arguments based on classical ODE theory is necessary. Specifically, the paper claims a diffeomorphism between the state space and the trajectory space, but this is a direct consequence of the existence and uniqueness theorem for ODEs with Lipschitz continuous vector fields, and the presented argument does not add any new insight. The use of this diffeomorphism to frame the estimation problem as a supervised learning task is also not a novel contribution, as it is a standard technique in the analysis of dynamical systems.

2) __Methodological aspect.__  In related works many references study different problem - estimating dynamics when ODE is not known, which is not the problem that this paper studies. On the other hand, existing literature on the ML MAP and MMSE estimation of the initial conditions of a known ODE is not properly reviewed, and the novelty of the considered methodology lacks perspective. The paper does not adequately discuss the computational aspects of the proposed methods. For example, the optimization problem in Equation (6) is not convex and the authors do not discuss how they address this. Furthermore, the paper does not properly acknowledge the existing literature on parameter estimation in ODEs, which often uses techniques such as sensitivity analysis and adjoint methods, which are not discussed here. The paper should also discuss the identifiability of the parameters, which is a crucial aspect of parameter estimation in dynamical systems.

3) __Experimental aspect.__ One toy ODE model is by far bellow ICLR standard. No broader context presented. Such discussion is insufficient to draw any kind of reliable conclusions. Additional material in the Appendix is minor and in part (Section A.2) obvious. The empirical evaluation is limited to a single Lotka-Volterra system and does not demonstrate the general applicability of the proposed methods. The paper lacks any comparison to existing methods for parameter estimation in ODEs, making it difficult to assess the practical value of the proposed approach. The discussion of the results is also superficial, and the paper does not provide any insights into the limitations of the proposed approach.


__Minor issues:__

1) $\varphi$ is nowhere properly defined
2) Bellow Eq. (6) $R^{K\times K}$ should read $R^{N\times N}$
3) In Eq. (8) inner product is in $L^2(I)$ not an RKHS. Proposition with an RKHS should be stated, at least in the Appendix.
4)  Eq. (12) should be rewritten to avoid confusion. What is written now is that the empirical estimate equals the regression function.

### Questions
When introducing kernel for the trajectories, due to the change of geometries between RKHS and  $L^2(I)$ spaces, the existence and the properties of the diffeomorphism should be at least commented. Also, can you please clarify when the optimization is done in the RKSH norm and when in $L^2$ norm. To me it seams that aspects of the statistical learning theory of kernel methods are not addressed properly. In particular, regression function in Eq. (12) may or may not belong to the RKHS defined by the kernel, and the minimisation is typically not done in $L^2$ but in RKSH.  In particular, can you please elaborate on "_MMSE trajectory estimate is optimal for any desired weighting of time horizons by the construction of Equation (6)._"

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a framework for predicting the behavior of ordinary differential equations. The research is centered on the study of smooth Lipschitz dynamical systems over a finite time interval and establishes that the set of possible trajectories forms a finite-dimensional Riemannian manifold. Through the integration of established estimation techniques, such as maximum likelihood, maximum a posteriori, and minimum mean squared error estimation, the authors introduce methods for computing the best-estimated trajectories. The paper also delves into the properties and conducts numerical experiments to illustrate specific estimations.

### Strengths
- The model formulation is rigorous, and the theoretical proofs are robust.

- After introducing the abstract framework, the paper discusses common estimation objectives and presents practical methods for computing trajectory estimations.

### Weaknesses
 - The commonalities and differences between the author's approach and related work in Section 1.1 are not clearly delineated. For instance:
  - Is the method proposed in this paper a variant of the Neural ODE method?
  - What advantages does the proposed method offer over existing Neural ODE methods in the context of time-series forecasting problems?
  - The relevance of discussing regularization methods for training neural networks to solve differential equations is not entirely clear.

- When the parameter space $\Theta$ s derived from a neural network, is it possible to verify whether $f$ is a smooth function, satisfying assumption 1?

- Could you please provide the definition of the function $\varphi$ (in page 4, line 15) and the notation $\varphi^{\gamma_i}(x_0)$ (in page 5, line 24)?

- What is the meaning of the bracketed term $[D\varphi^{\gamma_i}]$ in the equation (14)?

- Could you offer a comparison of the computational complexity between the proposed methods for computing trajectory estimations and the estimations of the initial condition?

- Regarding Figure 2, it appears to be somewhat confusing. 
  - Is the caption of each subfigure indicating the names of methods? How do they correspond to the six different forecasting objectives used in simulations?
  - Could you provide further insights into which surfaces of objective functions yield better results and which do not? Are these outcomes affected by changes in the initialization point?
  - For the statement 'the trajectory MSE illustrates a valley of initializations ... structure not captured by any competing technique',  it seems the State MSE also exhibits a valley structure. Could you elaborate on this observation?

### Questions
- The commonalities and differences between the author's approach and related work in Section 1.1 are not clearly delineated. For instance:
  - Is the method proposed in this paper a variant of the Neural ODE method?
  - What advantages does the proposed method offer over existing Neural ODE methods in the context of time-series forecasting problems?
  - The relevance of discussing regularization methods for training neural networks to solve differential equations is not entirely clear.

- When the parameter space $\Theta$ s derived from a neural network, is it possible to verify whether $f$ is a smooth function, satisfying assumption 1?

- Could you please provide the definition of the function $\varphi$ (in page 4, line 15) and the notation $\varphi^{\gamma_i}(x_0)$ (in page 5, line 24)?

- What is the meaning of the bracketed term $[D\varphi^{\gamma_i}]$ in the equation (14)?

- Could you offer a comparison of the computational complexity between the proposed methods for computing trajectory estimations and the estimations of the initial condition?

- Regarding Figure 2, it appears to be somewhat confusing. 
  - Is the caption of each subfigure indicating the names of methods? How do they correspond to the six different forecasting objectives used in simulations?
  - Could you provide further insights into which surfaces of objective functions yield better results and which do not? Are these outcomes affected by changes in the initialization point?
  - For the statement 'the trajectory MSE illustrates a valley of initializations ... structure not captured by any competing technique',  it seems the State MSE also exhibits a valley structure. Could you elaborate on this observation?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper discusses a new approach for the estimation of controlled ODE solutions based on the geometric properties of flow maps. The authors first provide an overview of the problem and present their main theoretical results. Then, they discuss how the theory translates into practical algorithms and finally show performance on a Lotka-Volterra ODE. Other ODEs are studied in the appendix. In the appendix, one can also find a detailed discussion of some interesting elements, such at tolerance and stepsize selection.

### Strengths
The paper is rigorous, very well-written, and interesting. For me, truly a joy to read. I learned a lot from this paper and find the idea very nice. I especially like the fact that the authors guide the reader through proofs and through the literature. This is very helpful. I am arguably not an expert on ODE estimation, but I worked on this a bit and find the contribution quite relevant for applications.

### Weaknesses
While I generally like the paper there are some points that need revision and better clarity.

1) Experiments: They work pretty well, but two things are not clear to me (a) assumptions for computation of $\det D\psi$ and (b) what is the input to the training pipeline. (a) From the appendix, it seems you compute $\det D\psi$ assuming access to the exact solver. From what I understood in the paper, it instead seems you have access only to noisy measurements. Specifically, it's unclear how the Jacobian determinant is computed in practice when only noisy trajectory data is available, as this requires knowledge of the underlying vector field. (b) this is related. seems from the paper you assume access to a single noisy trajectory, but I guess you actually use more than one. Can you make this more clear to me? It would be helpful to clarify if multiple noisy trajectories are used, or if the single trajectory is augmented in some way (e.g., by adding noise or using a sliding window approach) to create a dataset suitable for training.

2) Comparisons with other methods: This is totally missing. Only variants of the proposed methods are discussed. While the discussion is still interesting, I would like the authors to show comparisons with other alternatives for solving the problem. In terms of Accuracy, Speed, Assumptions. For example, how does this method compare to standard approaches like Runge-Kutta methods, or more recent learning-based approaches for ODE solving? A comparison with these methods is needed to contextualize the performance and advantages of the proposed approach. I am totally happy to revise this score if you are able to show this.

Typos (minor):
- In Abb B, I would remind the reader of the definition of $\psi$. Also, in the proof of Lemma 1, $\forall x_0\in\mathcal{X}$, not $x$.
- After formula 9, I would perhaps explain better why "this potential concern is unfounded". I would also tone down the sentence.

### Questions
I have a question.

3) In the main paper assumptions, you have that $\mathcal{U}$ is a manifold. However, in App. B, you assume the inputs have a finite-sum structure. Hence, it seems to me the assumption on the input set is a bit stronger than what you claim. Am I right?

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a method for forecasting time series governed by ordinary differential equations (ODEs), focusing on future trajectories. The authors showed that the solution space of such ODEs is a finite-dimensional Riemannian manifold, allowing for applying statistical objectives like maximum likelihood and minimum mean squared error directly in the feasible ODE solutions space. This approach aims to reduce forecasting errors compared to traditional methods not based on the solution manifold, further supported by numerical examples.

### Strengths
1. The paper showed the space of trajectories on a finite time interval I, with a finite degree of freedom, is a finite-dimensional manifold embedded in the space of a square-integrable function.

2. The paper summarized several classic estimation methods for trajectory forecasting and numerically compared their effects on the Lotka--Volterra equation.

3. The paper is very clearly written.

### Weaknesses
1. I find the paper presents an overly simple idea with an unrealistic assumption. When the space of parameters $\Theta$, the space for the inputs $\mathcal{U}$ are both finite-dimensional, finding the unknown dynamics is, of course, a finite-dimensional problem. However, most of the time,  the space of parameters $\Theta$/the input space $\mathcal{U}$ are not finite-dimensional. This is why forecasting dynamics is hard. For example, suppose the initial condition is not known exactly but on an open interval, which is no longer finite-dimensional. In that case, we do not know what type of chaotic behavior will occur in the long-time horizon. The same thing applies to the parameter space. General variable coefficients, even for the smoothest functions in $C^\infty$, are in an infinite-dimensional space before further assumptions.

2. Even if we settle for finite-dimensional spaces for the initial condition, the parameters, the inputs, etc. (i.e., all the places where one can change the dynamics), the overall dimension can be large. Indeed, $C_{f,I}$ is the range of the forward problem, containing all possible trajectories. It is not possible to characterize the space analytically, so it will have to be done through the finite number of parameters mentioned above. In that sense, (13) becomes the standard parameterized minimization problem, like those we see in regressions. If we know a priori that the dynamics are only subject to a finite number of parameters, no one will use (12), which does not utilize this prior/expert knowledge.

3. The numerical examples are simple, and the white noise assumption for the data, as shown in (17), is also too simple. The proposed method will perform poorly if the noise can be fit into the trajectory manifold $C_{f,I}$. Specifically, if the noise process is not independent of the underlying dynamics, the method's performance will degrade significantly. For instance, if the noise is correlated with the system's state or has a temporal structure that mimics the system's behavior, the optimization process could converge to a suboptimal solution that fits the noise rather than the true dynamics.

4. The paper titled "**Provably accurate** ODE forecasting through explicit trajectory optimization". I don't see where the "provably accurate" is based. Both Theorem 1 and Proposition 1 are results with little to do with ODE forecasting. Theorem 1 is a consequence of the "finite dimension" assumption, and Proposition 1 is a property from differential manifold.

### Questions
1. The metric tensor K is diagonal, in the sense that it is zero if the time points don't match. This is very special and does not accommodate correlations in time. Why do the authors want to choose this?

2. Is the norm $ || \cdot||$ in (12) the same as in (13)? If so, are you not giving the manifold a particular metric but using the one for $L^2(I)$?

3. It was $\hat{x}$ in (13), but became $\tilde{x}$ in (16)?

4. Figure 2 is a bit confusing. For some, we need to look for the maximum, while for some, we need to look for the minimum. It is better that they are all for maximum or all for minimum. Otherwise, it is confusing and hard to compare across different figures.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
1 poor
