# Constrained Bi-Level Optimization: Proximal Lagrangian Value Function Approach and Hessian-free Algorithm

- Decision: Accept
- Scores: 5, 6, 8, 8, 5

## Abstract
This paper presents a new approach and algorithm for solving a class of constrained Bi-Level Optimization (BLO) problems in which the lower-level problem involves constraints coupling both upper-level and lower-level variables. Such problems have recently gained significant attention due to their broad applicability in machine learning. However, conventional gradient-based methods unavoidably rely on computationally intensive calculations related to the Hessian matrix. To address this challenge,  we begin by devising a smooth proximal Lagrangian value function to handle the constrained lower-level problem. Utilizing this construct, we introduce a single-level reformulation for constrained BLOs that transforms the original BLO problem into an equivalent optimization problem with smooth constraints. Enabled by this reformulation, we develop a Hessian-free gradient-based algorithm—termed proximal Lagrangian Value function-based Hessian-free Bi-level Algorithm (LV-HBA)—that is straightforward to implement in a single loop manner. Consequently, LV-HBA is especially well-suited for machine learning applications. Furthermore, we offer non-asymptotic convergence analysis for LV-HBA, eliminating the need for traditional strong convexity assumptions for the lower-level problem while also being capable of accommodating non-singleton scenarios. Empirical results substantiate the algorithm's superior practical performance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a single loop proximal Lagrangian Value function-based Hessian-free Bi-level Algorithm (LV-HBA) for solving constrained bilevel optimization where the lower-level problem involves constraints coupling both upper-level and lower-level variables.
The authors relax the strongly convex assumption on lower-level problem to the general convex case, and provide non-asymptotic convergence analysis for LV-HBA. They also provide numerical experiments on the synthetic problem, hyperparameter selection problem and data hypercleaning task.

### Strengths
The paper is well-written. The authors propose a single loop Hessian free method that we refer to as Lagrangian Value function-based Hessian-free Bi-level Algorithm (LV-HBA). The authors provide non-asymptotic convergence analysis for LV-HBA, relaxing the underlying assumptions for lower level problem from strongly convexity to only convexity.

### Weaknesses
Please see questions.

1. Can the authors elaborate why there is no need to assume the Lipschitz continuity of the upper level function $F(x,y)$, which is typically necessary in bilevel optimization even the lower function is strongly convex, e.g. Xiao et al. (2023b).
2. On page 6, the sentences after Assumption 3.2 say $f$ is $\rho_f$-weakly convex on $X\times Y$ with $\rho_f\ge 0$, which is potentially being smaller than $L_f$. Can you provide the exact form of $\rho_f$ or show the case of $\rho_f$ being smaller for some specific application? Does that mean we can only suppose $\rho_f = L_f$ in general?
3. Theorem A.1 says reformulation (4) is equivalent to constrained BLO problem (1). In the proof of Theorem A.1, it only illustrates that the feasible points of (4) and (1) are equivalent. It is unclear why this means the formulations (4) and (1) and are also equivalent. Can we conclude the optimal solution of (4) and (1) are equivalent?
4. In reformulation (5), how to choose the parameter $r$?
5. The proposed methods includes many hyperparameters, making difficult to implement in practice.

### Questions
1. Can the authors elaborate why there is no need to assume the Lipschitz continuity of the upper level function $F(x,y)$, which is typically necessary in bilevel optimization even the lower function is strongly convex, e.g. Xiao et al. (2023b).
2. On page 6, the sentences after Assumption 3.2 say $f$ is $\rho_f$-weakly convex on $X\times Y$ with $\rho_f\ge 0$, which is potentially being smaller than $L_f$. Can you provide the exact form of $\rho_f$ or show the case of $\rho_f$ being smaller for some specific application? Does that mean we can only suppose $\rho_f = L_f$ in general?
3. Theorem A.1 says reformulation (4) is equivalent to constrained BLO problem (1). In the proof of Theorem A.1, it only illustrates that the feasible points of (4) and (1) are equivalent. It is unclear why this means the formulations (4) and (1) and are also equivalent. Can we conclude the optimal solution of (4) and (1) are equivalent?
4. In reformulation (5), how to choose the parameter $r$?
5. The proposed methods includes many hyperparameters, making difficult to implement in practice.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a new single-loop Hessian-free algorithm for the solving Bi-Level Optimization (BLO) problems. 

It first creates a smooth proximal Lagrangian value function, effectively addressing the constrained lower-level problem. Subsequently, the authors present a single-level reformulation for constrained BLOs, converting the original BLO problem into an equivalent optimization problem with smooth constraints.

The paper includes a non-asymptotic convergence analysis for the proposed algorithm. Some experiments have been conducted to show the superior practical performance of the algorithm

### Strengths
S1. This paper proposes the first single-loop Hessian-free algorithm for solving the BLO problem.
S2. The authors introduce a new potential function, which is associated with the monotonically decreasing step size. Furthermore, they demonstrate how to select these step sizes to ensure the potential function exhibits the sufficient descent property.
S3. The authors have conducted experiments on five machine learning tasks to validate the performance of their proposed methods.

### Weaknesses
W1. There are an excessive number of stepsize parameters in use, and it remains uncertain whether the algorithm's performance is significantly affected by the choice of these parameters.

W2. While other bilevel optimization algorithms employ techniques such as Nesterov's momentum or utilize high-order information of the objective function, the plain and simple gradient descent/ascent algorithm may be slow in practical applications.

W3. Assumption 3.3 (ii) can be quite stringent since the global Lipschitz constant for both $L_{g_1}$ and $L_{g_2}$ have not been determined in advance for many applications.

W4. The choice for the parameter $r$ for the truncated proximal Lagrangian value function is not mentioned.

### Questions
See above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a novel gradient-based algorithm designed for a class of constrained Bi-Level Optimization (BLO) problems that have coupled lower-level (LL) constraints. In this problem, the lower-level problem takes the form:
$$
\min_y f(x,y), s.t. g(x,y) \leq 0.
$$
In contrast to existing methods relying on implicit differentiation techniques, this paper introduces a smooth proximal Lagrangian value function for the lower-level problem. This new value function enables the formulation of a single-level reformulation for the constrained BLO. Building upon this reformulation, a single-loop alternating gradient descent method is derived to efficiently tackle the constrained BLO. The paper establishes a non-asymptotic convergence result for the proposed algorithm. Additionally, the paper includes numerical experiments conducted on both illustrative toy examples and practical applications, demonstrating the algorithm's superior practical performance.

### Strengths
1.	This paper is well-organized and in general easy to follow. The assumptions concerning the functions and problem settings are clearly elucidated, facilitating a clear grasp of both the primary concept and the technical intricacies of the proposed approach.

2.	A noteworthy contribution to the bi-level optimization community is the introduction of the proximal Lagrangian value function and the resulting single-level reformulation for constrained BLOs. This addition holds significant promise for advancing the development of other efficient methods to the constraints BLOs.

3.	Notably, the proposed method distinguishes itself by its Hessian-free nature, obviating the need for any computations involving the Hessian matrix of the lower-level problem data. Furthermore, its single-loop structure renders it highly implementable and computationally efficient. An appealing aspect of this method is its ability to work without imposing the stringent requirement of strong convexity on the lower-level problem. Moreover, it exhibits versatility by accommodating scenarios in which the lower-level problem possesses multiple solutions, expanding its applicability to a broad spectrum of practical applications.

5.	The paper extensively explores the properties of the newly introduced proximal Lagrangian value function and the associated reformulation. Additionally, a non-asymptotic convergence analysis is included, further substantiating the contribution and the validity of the proposed approach.

### Weaknesses
1.	In Table 1, to the best of my knowledge, BVFSM does not require LL objective to be convex.

2.	The authors have not included some recent works that investigate algorithms for addressing constrained Bi-Level Optimization (BLO) problems through the value function approach, such as:

Fliege, J., Tin, A., & Zemkoho, A. (2021). Gauss–Newton-type methods for bilevel optimization. Computational Optimization and Applications, 78(3), 793-824.

Fischer, A., Zemkoho, A. B., & Zhou, S. (2022). Semismooth Newton-type method for bilevel optimization: global convergence and extensive numerical experiments. Optimization Methods and Software, 37(5), 1770-1804.

3.	On page 8,  $\|y^k-y^*(x)\|$ should be revised to `` $\left\|y^k-y^*(x^k)\right\| $ "?

4.	When the constraints of the LL problem are absent, i.e., when $g = 0$, does the introduced proximal Lagrangian value function revert to the classical Moreau envelope function of the LL objective? Furthermore, is there any relationship between the proximal Lagrangian value function and the augmented Lagrangian function of the LL problem?

### Questions
I think this work provides some good contributions to constrained bilevel optimization, and hence I tend to accept it. See my questions in the weakness part.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper studied a class of new constrained bilevel optimization, where the lower-level problem involves constraints coupling both upper-level and lower-level variables. Based on the Moreau envelope value function, this paper proposed an efficient single-loop Hessian-free gradient-based algorithm. Moreover, it studied the non-asymptotic convergence analysis for the proposed algorithm. Extensive experimental results verify the efficiency of the proposed algorithm. In summary, the contributions of this paper are significant on the design algorithm and solid theoretical analysis.

### Strengths
This paper studied a class of new constrained bilevel optimization, where the lower-level problem involves constraints coupling both upper-level and lower-level variables. Based on the Moreau envelope value function, this paper proposed an efficient single-loop Hessian-free gradient-based algorithm. Moreover, it studied the non-asymptotic convergence analysis for the proposed algorithm. Extensive experimental results verify the efficiency of the proposed algorithm. In summary, the contributions of this paper are significant on the design algorithm and solid theoretical analysis.

### Weaknesses
It is better to list some bilevel optimization examples in machine learning that have non-smooth and weakly convex lower level functions, which will strength the motivation of this work.

### Questions
Some questions:

1)	In the proposed LV-HBA algorithm, there exist many hyper parameters such as $\alpha_k,\beta_k,\eta_k,\gamma,c_k$. Although the authors provided the range of these parameters in the convergence analysis, I still think that the choice of these hyper parameters is not easy in practice. 

2)	In the experiments, how to choose these hyper parameters including the parameter $r$ in set $Z$ ?

3)	From the Theorem 3.1, the best convergence rata is $O(1/K^{1/4})$ when $p=1/4$ ?

4)	It is better to list some bilevel optimization examples in machine learning that have nonsmooth and weakly convex lower level functions, which will strength the motivation of this work.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper concerns bi-level optimization (BLO) problems with coupled inner constraints. By introducing the Moreau envelope of the Lagrange function, the lower-level problem can be reformulated into a smooth function value constraint. Then, a single loop algorithm is proposed based on the formulation. Non-asymptotic rate is established for the proposed method using a newly defined stationarity measure.

### Strengths
1. The smoothing technique based on the Moreau envelope is good. This provides a new reformation for the BLO.

2. The theoretical rate and numerical experiments are sufficient.

### Weaknesses
1.Assumption 3.1(i) seems too strong for me. Usually, the involved functions in BLO are assumed convex only w.r.t. $y$.

2. The stationarity measure needs further clarification. The proposed measure is based on (16). However, it is not clear how the stationary points of (16) are related to the original BLO.

3. The techniques in the theoretical proofs lack novelty, which directly takes advantage of analysis for penalty methods.

### Questions
What is the central benefit of using the Moreau envelope instead of the optimal value function, especially in the technical parts?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
