# Informed Machine Learning with a Stochastic-Gradient-based Algorithm for Training with Hard Constraints

- Decision: Reject
- Scores: 5, 5, 6, 5

## Abstract
A methodology for informed machine learning is presented and its effectiveness is shown through numerical experiments with physics-informed learning problems.  The methodology has three main distinguishing features.  Firstly, prior information is introduced in the training problem through hard constraints rather than through the typical modern practice of using soft constraints (i.e., regularization terms).  Secondly, the methodology does not employ penalty-based (e.g., augmented Lagrangian) methods since the use of such methods results in an overall methodology that is similar to a soft-constrained approach.  Rather, the methodology is based on a recently proposed stochastic-gradient-based algorithm that maintains computationally efficiency while handling constraints with a Newton-based technique.  Thirdly, a new projection-based variant of the well-known Adam optimization methodology is proposed for settings with hard constraints.  Numerical experiments on a set of physics-informed learning problems show that, when compared with a soft-constraint approach, the proposed methodology can be easier to tune, lead to accurate predictions more quickly, and lead to better final prediction accuracy.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a new methodology in the area of physics-informed machine learning by incorporating “hard constraints” during stochastic-gradient-based training. The approach differs from traditional “soft-constrained” methods that add penalty terms to the objective function, which can be difficult to tune and less effective. The main innovation is a novel projection-based variant of the Adam optimizer (P-Adam), adapted for hard-constrained optimization. Numerical experiments show that this approach outperforms traditional Adam on four tasks: a 1D spring oscillator, a chemical engineering reaction model, 1D Burgers' equation, and 2D Darcy flow.

### Strengths
Strengths
- Unlike conventional methods based on penalty terms, the use of hard constraints directly embeds domain-specific knowledge. The performance improvements based on this are demonstrated in the case studies.
- The authors include a rigorous discussion of the optimization method, starting from the original constrained Sequential Quadratic Programming (SQP) framework settings. 
- The experimental results reveal that the proposed methodology leads to better prediction accuracy and requires fewer hyperparameter adjustments, which is advantageous for real-world applications where tuning may be computationally expensive.

### Weaknesses
Weaknesses
- The novelty of this work could use clarification. The new techniques do not seem to differ methodologically from the related algorithms presented, e.g., in  Márquez-Neila et al., Berahas et al., and Curtis et al., except the introduction of momentum methods. Moreover, projection of optimization steps given hard constraints has been demonstrated, e.g., by Chen et al. (https://arxiv.org/abs/2402.07251).
- The experimental settings considered have questionable relevance to the state of the art in this area. The methods are only compared against standard and soft-constrained Adam, rather than the bulk of methods for physics-informed machine learning. Moreover, the generalization to practical problems is unclear. Only small-scale problems are considered, enabling the use of non-stochastic gradient descent, and half the data in the batch setting (which may not be realistic).

### Questions
Questions
- Pg 3 suggests that the Lipschitz constants for the objective gradient and constraint Jacobian can be estimated. What effects does this have on the convergence or the exactness of the method?
- Can “almost-surely” be defined precisely throughout? Does this refer to a probability?
- Pg 6 suggests that only a few terms should be treated as “hard constraints.” Is there a systematic way to determine which terms should be treated as hard constraints?

### Soundness
3

### Presentation
3

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
This paper introduces an approach that characterized by three key aspects. Initially, it incorporates prior information into the training process via hard constraints instead of the more common contemporary technique of soft constraints. Furthermore, the approach abstains from using penalty-based methods. Instead, it relies on a recently introduced stochastic-gradient-based algorithm that is computationally efficient and employs a Newton-based method for constraint management. Lastly, a projection-based adaptation of the widely recognized Adam optimization algorithm is suggested for scenarios involving hard constraints. The numerical experiments achieve superior final prediction accuracy when contrasted with a soft-constraint method.

### Strengths
This article proposes a potential new method and demonstrates good results in numerical experiments.

### Weaknesses
 * The narrative in the first section of this paper is somewhat disorganized; it does not clearly articulate the motivation behind the paper, which is, why it is essential to employ key techniques such as hard constraints, and why penalty-related algorithms are not utilized. Since the number of hyperparameters for soft constraints is not significantly large, the core difference between soft and hard constraints is not clearly identified.

* The serious issue with this article is that it exaggerates their contributions. The contributions stated in section 1.1 (a), (b), and the entire content of section 2.1 are in fact all derived from [1]; the authors have not made any form of innovation. The only innovative part of the entire article is section 2.2.

* The innovation in section 2.2 is also quite confusing. Algorithm 2 is very similar to the algorithm in [2], with the only difference being the application of a projection operator to the gradient. However, the article's explanation of why the projection is used is confusing. The conclusion in the article is that when H is chosen as the identity matrix I, the gradient and the projected gradient are the same, but the problem is that this clearly does not hold for the Adam algorithm. The article does not provide any other explanation for this distinction, nor does it have convergence theory to support it. The experimental results alone are not convincing.

### Questions
*

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper investigates informed machine learning by proposing a novel approach that integrates hard constraints directly into the optimization process, as opposed to previous methods that formulate informed constraints as soft constraints relying on penalty techniques (e.g., augmented Lagrangian methods). Building upon a recent stochastic gradient descent (SGD) method for constrained optimization, the authors incorporate hard constraints using a Newton-based technique. By employing a projection-based approach, they enable the handling of hard constraints within the well-established Adam optimizer. The method is empirically demonstrated in several small-scale experiments to exhibit robust and superior performance compared to other methods that do not treat constraints as hard constraints.

### Strengths
- **Hard constraint handling in Adam** The paper proposes to integrate projected gradient descent with Lagrange multipliers into the stochastic optimization framework, specifically adapting the Adam optimizer to handle hard constraints. By modifying the standard Adam update rule to project gradients onto the null space of the constraint Jacobian, ensures current solution feasibility at each iteration.
- **Computational Efficiency in small constraint scale**: When the Hessian matrix is diagonally approximated and has a small constraint number (low-rank constraint Jacobian), the constraint-related equations can be solved efficiently which does not trigger much computationally overhead.

### Weaknesses
 - **Scalability of constraints**: While the authors argue that a small number of constraints often suffices for good performance, the scalability of the method as the number of constraints increases is not extensively discussed. As the number of constraints grows, the projection step may become less efficient, and solving the constraint-related equations can become computationally intensive. It would be beneficial for the authors to elaborate, either theoretically or empirically, on the algorithm's limitations and performance when dealing with a larger set of constraints. Specifically, the paper lacks a detailed analysis of how the computational cost scales with the number of constraints ($m$) and the dimensionality of the parameter space ($n$). While the authors mention a low-rank constraint Jacobian, the implications of this assumption on the overall computational complexity, particularly concerning the matrix inversion within the projection step, are not fully explored. A more rigorous analysis, perhaps including a discussion of the conditions under which the low-rank assumption holds, would be beneficial. This could be accomplished on more scalable problems, which also help tackle the limited empirical scope weakness mentioned below.

- **Lack of Convergence proof** Although the paper references the convergence properties of the SGD-SQP method, these theoretical guarantees do not naturally extend to the proposed P-Adam algorithm while left as future work. The paper does not provide a clear explanation of how the projection step within the Adam optimizer affects the convergence behavior. The theoretical analysis should address whether the projection maintains the convergence properties of the original Adam optimizer or if it introduces new challenges, such as potential oscillations or convergence to suboptimal solutions. A formal convergence analysis, even under simplified assumptions, would significantly strengthen the theoretical foundation of the proposed method.

- **Limited Empirical Scope** The experimental validation presented in the paper is limited to small-scale problems with relatively simple neural network models. This restricted scope makes it challenging to assess the method's effectiveness and scalability in more complex or large-scale applications. Expanding the empirical evaluation to include larger datasets and more sophisticated models would strengthen the paper's claims regarding the practical utility of the proposed method. The experiments should include a wider range of problem settings, such as those with higher-dimensional parameter spaces and more complex constraint functions. Furthermore, the paper should include a comparison with other state-of-the-art methods for constrained optimization, not just those that do not treat constraints as hard constraints. This would provide a more comprehensive evaluation of the proposed method's performance.

### Questions
- How is the method different and similar to reference [1], which deals with linear equality constraint in PINN through projection layers derived from KKT conditions

[1] https://arxiv.org/abs/2402.07251

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper brings together the stochastic gradient-based SQP framework by Berthas et al. and the popular Adam optimization algorithm for ML-based solving of partial/ordinary differentiable equations with hard constraints.

### Strengths
The topic of the study is interesting.
I am happy to revise my evaluation based on the answers to my questions.

### Weaknesses
One may argue that novelty and originality are limited.
Algorithm 1 and the underlying Theorem 1 are based on previous work (Berthas et al., 2021).
Except the empirical evaluations, the main novel aspect boils down to plugging in an Adam-like update rule into Algorithm 1.

The basic idea in Algorithm 2 that the „stochastic gradient gk is replaced by its orthogonal projection onto the null space of ∇c(wk )T“ in a mixture of Adam and Algorithm 1 is clear. However, this key aspect - perhaps almost trivial - should be spelled out because it is so important. That is, line 1 in Algorithm 2 should be derived as used in the algorithm with all intermediate steps.

The manuscript states „When the number of rows of J (i.e., m) is small, the overall cost is proportional to that of computing H−1g with a symmetric and positive definite H, as is required for an Adam-based method for the unconstrained setting.“ But there a no non-diagonal matrices in place in Adam, right? Is this under the assumption that H is diagonal (e.g. the identity matrix I)?  Why is the scaling of Adam and P-Adam then the same?

In fact, the scaling w.r.t. to the number of constraints could be problematic.
Although wall clock time experiments are always a bit problematic (e.g., the may depend on the solver), I suggest to plot performance over wall clock time depending on the number of hard constraints.
The number of hard constraints in the experience was always very small, some scaling experiments would be interesting to see.

The differences between the methods are not always very pronounced.
The are only small differences in general in the „Chemical Engineering Problem“ and between Adam(inc) and P-Adam in 1D Burgers’ Equation, and also in general on the „2D Darcy flow“ task.

Baseline experiments using  the stochastic gradient-based SQP with steepest descent as in Algorithm 1 are missing.
How much do we actually gain from moving to P-Adam if we tune the SGD learning rate?

The reader wonders how well the „hard“ constraints are met.  For example, what is the value of the mass balance during the course of optimisation for the different methods?
It would be nice to see the ODE-residual errors for the points that were treated as soft targets vs this which were linked to „hard“ constraints.

1D Spring: The times at which the ODE-residual terms were defined were 30 evenly spaced points over [0,1] (end page 6).
The P-Adam considered the hard constraints on ODE-residuals at the time points   {0.14, 0.4, 0.7}.
These were different points that the equally spaced 30, right?
If yes: Is this fair? Why was no subset selected? How do the results change if for the settings without hard constraints the three points are added to the soft constraints (i.e., 33 instead of 30 points are computed in the ODE-residual  error component of the error)?

The listing of the methods in lines 297-299 is confusing. Should it be „Adam(con)“ instead of „Adam(unc)“ in line 299?  

Rather put Appendix C on runtime in the main body of the paper and move some specification of the (standard) benchmark problems to the appendix.

### Questions
- How is line 1 in Algorithm 2 exactly derived? Could you spell this out so that it is easy to follow (it is one of the main aspects of the study)?
- Why is it correct to state (lines 240-243) that computing H^-1g is proportional to what is require in a standard Adam step?
- How much do we actually gain from moving from  stochastic gradient-based SQP as in Algorithm 1 to P-Adam if we tune the SGD learning rate?
- How is the wall-clock time scaling w.r.t to the number of "hard" constraints?
- How well are the "hard" constraints met in practice? Nor always exactly, right?

### Soundness
3

### Presentation
2

### Contribution
2
