# An Inexact Conditional Gradient Method for Constrained Bilevel Optimization

- Decision: Reject
- Scores: 6, 8, 5, 6

## Abstract
Bilevel optimization is an important class of optimization problems where one optimization problem is nested within another. %This framework is widely used in machine learning problems, including meta-learning, data hyper-cleaning, and matrix completion with denoising. 
While various methods have emerged to address unconstrained general bilevel optimization problems, there has been a noticeable gap in research when it comes to methods tailored for the constrained scenario. The few methods that do accommodate constrained problems, often exhibit slow convergence rates or demand a high computational cost per iteration.
To tackle this issue, our paper introduces a novel single-loop projection-free method employing a nested approximation technique. This innovative approach not only boasts an improved per-iteration complexity compared to existing methods but also achieves optimal convergence rate guarantees that match the best-known complexity of projection-free algorithms for solving convex constrained single-level optimization problems. In particular, when the hyper-objective function corresponding to the bilevel problem is convex, our method requires $\tilde{\cO}(\epsilon^{-1})$ iterations to find an $\epsilon$-optimal solution.  
Moreover,  when the hyper-objective function is non-convex, our method's complexity for finding an $\epsilon$-stationary point is  $\cO(\epsilon^{-2})$.  
To showcase the effectiveness of our approach, we present a series of numerical experiments that highlight its superior performance relative to state-of-the-art methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies bilevel optimization where:
- the inner problem is strongly convex,
- the upper problem is smooth (convex or nonconvex) and constrained over a compact and convex set.

Such problem can be handled with projected gradient descent, but the projection operation may be costly.
Instead, the authors propose a single-loop, inexact and projection free method, coined Inexact Bilevel Conditional Gradient, which only takes one step of Frank Wolfe on the lower problem  (Algorithm 1).
A key in the algorithm design is to view the part of the hypergradient involving an Hessian inverse (the costly part), as the solution of a quadratic optimization problem (Eq 8). The solution $v(x_k)$ of this optimization problem is the approximately updated from one iteration $k$ to the next.
The error in this approximate gradient computation is bounded in Lemma 2/Eq9, which in turns sheds light on how to select the parameter $\gamma$ in FW.

Convergence rates are obtained in terms of Frank-Wolfe gap (Eq 4, Corollary 1) for the non convex case, and suboptimality for the convex case (theorem 2).

### Strengths
The topic is very relevant, the paper is clearly written and I did not spot any error. Enriching the toolbox of numerical solutions for bilevel optimization is of great importance, given the latter's ubiquity in many fields, from inverse problems to machine learning.

### Weaknesses
 - The experimental validation could be more complete. In particular, the method is applied only to low rank penalty, the only case (up to my knowledge) where Frank Wolfe shows a real benefit. What are some other possible applications of the method, where it would outperform accelerated proximal gradient? In other words, what are common sets such that FW's linear minimization operator can be computed efficiently, but projection cannot?
- Although it is not proposed by the authors, what is the interest of the noisy matrix completion formulation compared to a bilevel procedure to tune the regularization strength $\lambda$ of a nuclear norm regularized matrix least square problem? ie
$$\min_{\lambda \geq 0} \Vert M_1 \odot(M - Y^\lambda) \Vert^2 \quad \mathrm{s.t.} \quad Y^\lambda = \text{argmin} \Vert{M_2 \odot (M - Y)}^2 + \lambda \Vert Y \Vert_*$$
- Some tricks exist when the upper optimization is constrained (eg, parametrizing the positive regularization hyperparameter as $\lambda = \exp(\mu)$ as in Pedregosa (2016), which may also improve numerical stability). How does the proposed method compare? when should one use a method or the other?
- The provided code is in Matlab, a proprietary software.


Remarks
- Given the practical focus of the paper, it seems far-fetched to not consider, above Section 3.1, that the cost of matrix matrix multiplication is $m^3$. Algorithms with lower exponents have huge constant terms and are not beneficial for the kind of $m$ that are dealt with in ML.


Cosmetic remarks (no answer needed)
- one can reformulate linear minimization subproblem : missing "the" before "linear"
- In equation below 6c, $x_k$ and $y_k$ should be in bold (twice).
- Page 2 $K$ is not defined in the convergence rate of the Ghadimi and Wang method.
- A reference to the Frank Wolfe gap (the fact that in the convex case it upper bounds the suboptimality, and that still in the convex case it is the duality gap) may help the reader not so familiar with FW in definition 1.
- numbering all equations would make communication (both with reviewers and amongst future readers) easier
- Remark 4.1 has a number format that does not correspond to the rest (Theorem 2, etc)

### Questions
See weaknesses above.


Remarks
- Given the practical focus of the paper, it seems far-fetched to not consider, above Section 3.1, that the cost of matrix matrix multiplication is $m^3$. Algorithms with lower exponents have huge constant terms and are not beneficial for the kind of $m$ that are dealt with in ML.


Cosmetic remarks (no answer needed)
- one can reformulate linear minimization subproblem : missing "the" before "linear"
- In equation below 6c, $x_k$ and $y_k$ should be in bold (twice).
- Page 2 $K$ is not defined in the convergence rate of the Ghadimi and Wang method.
- A reference to the Frank Wolfe gap (the fact that in the convex case it upper bounds the suboptimality, and that still in the convex case it is the duality gap) may help the reader not so familiar with FW in definition 1.
- numbering all equations would make communication (both with reviewers and amongst future readers) easier
- Remark 4.1 has a number format that does not correspond to the rest (Theorem 2, etc)

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a projection-free bilevel method which leverages the Frank Wolfe and fully single loop hypergradient estimation techniques. The proposed method achieves the best known convergence rate and performs well in practice.

### Strengths
1. The theoretical contribution of this paper is solid and well-established. By the dedicated analysis, they analyze the convergence rate of the proposed fully single loop projection-free bilevel method and demonstrate that it achieves the best-known convergence rate. 
2. They relax a relatively restrictive assumption -- gradient boundedness -- in bilevel optimization to the optimizing trajectory, which can then be implied by the boundedness of feasible set of upper-level variable and the gradient continuity.

### Weaknesses
1. It is good to analyze the convergence in both nonconvex and convex bilevel setting, but it is unclear that when the composite function $l(x)$ can be convex. The only example I come up with is when $f(x,y^*(x))$ is jointly convex and $y^*(x)$ is linear in $x$, which means lower-level objective is quadratic in $y$. It would be better to explain some sufficient condition for $l(x)$ being convex. Also, as the convexity is required for $l(x)$, there are possibly some over-claims in the contribution and conclusion section saying that 'when upper-level objective $f$ is convex, ...'.

2. The paper's analysis relies on the assumption that the optimizing trajectory is bounded, which, while relaxed from gradient boundedness, still requires careful consideration. While the authors mention that this can be implied by the boundedness of the feasible set of the upper-level variable and the gradient continuity, it would be beneficial to provide more concrete examples or scenarios where this condition is easily verifiable. The practical implications of this assumption should be further discussed, especially in cases where the feasible set is not explicitly defined or is very large.

### Questions
Is it possible to extend the convergence analysis of IBCG to tackle the stochastic bilevel problem like SBFW?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes conditional gradient methods for constrained bilevel problems with strongly convex and smooth lower-level problems. The authors develop algorithms with finite time convergence guarantees for solving this class of problems under a deterministic setting. Finally, the authors experimentally evaluate the proposed algorithms to corroborate the theoretical guarantees.

### Strengths
Here, I list the main strengths of the paper.

- The paper is well-written and easy to read. All the ideas are clearly presented with sufficient discussions.
- The authors remove the boundedness assumption on $\nabla_y f(x, \cdot)$ which has been used by previous papers to guarantee convergence of bilevel optimization algorithms. 
- In addition to the convex case, the authors have presented results for general non-convex settings too.
- The presented analysis captures the dependence on the condition number which is largely ignored in earlier studies. 
- Experiments show better performance of IBCG compared to the state-of-the-art.

### Weaknesses
Here, I list my **major** concerns:

- My major concern is with the novelty and the contributions of the paper. First of all, the setting considered and the underlying ideas presented in the paper have already appeared in an earlier paper  (Akhtar et al., 2022) where authors have proposed SBFW. In SBFW, the authors consider a constrained stochastic bilevel problem and develop conditional gradient algorithms for solving the problem. Secondly, the authors of (Akhtar et al., 2022) have considered stochastic problems which are certainly more challenging than the deterministic setting considered in this work. I believe although the authors have shown dependence on condition number and removed the boundedness assumption on the partial gradient of $f$ w.r.t. $y$ (by using compactness of the constraint set) the major contributions may not be enough. In addition, the approximation of the product of Hessian inverse and partial gradient by solving a quadratic problem is quite popular in bilevel optimization and has already appeared in the AmIGO algorithm proposed in (Arbel et al ICLR 2022) and other papers. The specific way the Hessian inverse is approximated, using a single step of gradient descent on a quadratic, while computationally efficient, doesn't seem fundamentally novel given the existing literature on implicit differentiation and bilevel optimization.

- Other than matrix completion and toy problems it would be interesting to see the performance of IBCG on large-scale machine learning problems. Will the algorithm be able to compete with stochastic algorithms in that case since the considered algorithm only works for the deterministic setting?


**Minor**

- Define $\Omega_1$ and $\Omega_2$ in equation (2).

- The definition of training and test data before equation (3) is not clear.

- What is $\omega$ in the discussion before Section 3.1.
 
- Please make sure that $\mathcal{O}$ and  $\tilde{\mathcal{O}}$ are used consistently throughout the paper.

- In the MAML problem are there algorithms that actually impose sparsity as shown in the formulation of equation (3)?

### Questions
Please see the weaknesses section above.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a novel single-loop projection-free method for the constrained bilevel optimization problem. The paper demonstrates that the method has an improved per-iteration complexity and optimal convergence rate guarantees matching the best-known complexity of projection-free algorithms for solving convex constrained single-level optimization problems. To be specific, the method requires approximately iterations to find an -optimal solution when the upper-level objective function  is convex, and approximately to find an ε-stationary point when  is non-convex.

### Strengths
(1) Comparing to the common projection-based methods for constrained bilevel problem, a novel projection-free method with optimal convergence guarantee and lower computational complexity is proposed.

(2) The non-asymptotic optimal convergence rate guarantees are characterized under different settings. And the numerical results are promising.

### Weaknesses
The extensive numerical experiments are recommended to conduct. 
For example: Since the step-size  is vital to the algorithm’s performance, the numerical experiments of IBCG with respect to the different step-sizes  are advised to conduct as a validation to the theoretical part.




Theorems 1and 2 give the convergence rate when the hyper-objective is convex and nonconvex. However, it is mentioned in the abstract and the conclusion that the convergence guarantees are achieved under the setting that the upper level objective  is convex and nonconvex. The convexity of  and  is not equivalent. Perhaps I have omitted something. How to make the connection between the function  and  to derive the optimal convergence guarantee when   is convex and nonconvex?

### Questions
Theorems 1and 2 give the convergence rate when the hyper-objective is convex and nonconvex. However, it is mentioned in the abstract and the conclusion that the convergence guarantees are achieved under the setting that the upper level objective  is convex and nonconvex. The convexity of  and  is not equivalent. Perhaps I have omitted something. How to make the connection between the function  and  to derive the optimal convergence guarantee when   is convex and nonconvex?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
