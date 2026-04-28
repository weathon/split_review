# Rethinking Moreau Envelope for Nonconvex Bi-Level Optimization: A Single-loop and Hessian-free Solution Strategy

- Decision: Reject
- Avg Score: 6.60
- Scores: 8, 6, 8, 5, 6

## Abstract
This work focuses on addressing two major challenges in the context of large-scale nonconvex Bi-Level Optimization (BLO) problems, which are increasingly applied in machine learning due to their ability to model nested structures. These challenges involve ensuring computational efficiency and providing theoretical guarantees. While recent advances in scalable BLO algorithms have primarily relied on lower-level convexity simplification, our work specifically tackles large-scale BLO problems involving nonconvexity in both the upper and lower levels. We simultaneously address computational and theoretical challenges by introducing an innovative single-loop gradient-based algorithm, utilizing the Moreau envelope-based reformulation, and providing non-asymptotic convergence analysis for general nonconvex BLO problems. Notably, our algorithm relies solely on first-order gradient information, enhancing its practicality and efficiency, especially for large-scale BLO learning tasks. We validate our approach's effectiveness through experiments on various synthetic problems, two typical hyper-parameter learning tasks, and a real-world neural architecture search application, collectively demonstrating its superior performance.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a single-loop algorithm for bilevel optimization problems.
The algorithm can handle non-smooth and smooth + non-smooth weakly convex inner functions. The authors provide convergence rates under very weak assumptions (smoothness of the outer and the inner problem).

### Strengths
To my knowledge, this work contains two major novelties:
- in the smooth case, convergence proof a single loop algorithm with weak assumptions (smoothness of the inner and the outer problem only, no need for bounded gradients)
- in the non-smooth case, to my knowledge, this is the first single-loop algorithm proposed
Maybe the authors and other reviewers can comment on this.

### Weaknesses
While the proposed algorithm is clearly defined, authors could do a better job at providing the intuitions: the directions $d_x^k$ and $d_y^k$ are given with little context. The same comment applies to the merit function and Lemma 3.1. Specifically, the update rules for $x$ and $y$ appear somewhat arbitrary without a clear explanation of their connection to the bilevel optimization problem. It is not immediately obvious why these specific gradient approximations are chosen, and how they relate to the overall goal of minimizing the outer objective while implicitly solving the inner problem. The merit function $V_k$ also lacks a clear motivation; it's not intuitive why the sum of the penalized objective and the distance between $	heta^k$ and the optimal solution of the Moreau envelope is a suitable measure for convergence. The role of the penalty parameter $c_k$ and its influence on the merit function's behavior also needs further clarification. The connection between Lemma 3.1 and the overall convergence proof is not immediately apparent, and a more detailed explanation of how the monotonic decrease of $V_k$ leads to the desired convergence results would be beneficial.

### Questions
- Could you comment on the novelty, is this the first analysis with such a weak set of assumptions? Or I am missing something?

- Could you give intuitions on the proof? (which is currently 10 pages long in the appendix) and intuitions on the merit function.
Maybe the authors could provide a proof sketch

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper applies the Moreau envelope for solving bilevel optimization with non-convex low-level optimization. The proposed algorithm extends such Moreau envelope framework from convex to non-convex settings, achieves a single loop structure, and avoids Hessian computation at the same time. A non-asymptotic convergence rate is derived and extensive numerical evaluations demonstrate faster convergence and superior performance.

### Strengths
1. Compared to previous bilevel optimization algorithms, the proposed MEHA algorithm is both single-loop and hessian-free, yielding an advantage in the efficiency of convergence. 

2. The numerical evaluation conducted is quite comprehensive, covering both synthetic experiments and various real-world tasks.

### Weaknesses
The only weakness the reviewer sees is the lack of technical novelty, as the analysis is largely based on previous work utilizing the Moreau envelope for convex low-level objectives (Gao et al., 2023), and other Hessian-free works. As a result, the proposed method seems like an extension / combination of previous methods.

### Questions
N/A

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper studied the nonconvex constrained bilevel optimization, where its upper level is nonconvex and its lower level is nonsmooth and weakly convex. It proposed an efficient single-loop gradient-based Hessian-free algorithm based on the Moreau envelope technique. Moreover, it provided the non-asymptotic convergence analysis for the proposed algorithm. Extensive experimental results demonstrate the efficiency of the proposed algorithm. In summary, the contributions of this paper are significant on the design method and solid convergence analysis.

### Strengths
This paper proposed an efficient single-loop gradient-based Hessian-free algorithm based on the Moreau envelope technique. Moreover, it provided the non-asymptotic convergence analysis for the proposed algorithm. Extensive experimental results demonstrate the efficiency of the proposed algorithm. In summary, the contributions of this paper are significant on the design method and solid convergence analysis.

### Weaknesses
It is better to list some bilevel optimization examples in machine learning that have non-smooth and weakly convex lower level functions, which will strength the motivation of this work.

It is also a concern that in the proposed algorithm 1, there exist five tuning parameters $\alpha_k,\beta_k,\eta_k,\gamma,c_k$. Although the authors gave the range of these parameters in the convergence analysis, I still think the choice of these tuning parameters is not easy in practice.

From the convergence analysis, I saw that the authors used the condition that $f(x,y)$ is a weakly convex. I suggest that the authors should add this condition in Assumption 3.2 of the paper.

The inequality (11) in Assumption 3.2 (ii) is a strict condition ? If not , please give an example.

### Questions
Some comments:

1)	In the proposed algorithm 1, there exist five tuning parameters $\alpha_k,\beta_k,\eta_k,\gamma,c_k$. Although the authors gave the range of these parameters in the convergence analysis, I still think the choice of these tuning parameters is not easy in practice. 

2)	From the convergence analysis, I saw that the authors used the condition that $f(x,y)$ is a weakly convex. I suggest that the authors should add this condition in Assumption 3.2 of the paper.

3)	The inequality (11) in Assumption 3.2 (ii) is a strict condition ? If not , please give an example.

4)	It is better to list some bilevel optimization examples in machine learning that have nonsmooth and weakly convex lower level functions, which will strength the motivation of this work.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper concerns bi-level optimization (BLO) problems with an inner constraint set. By introducing the Moreau envelope of the lower-level function, the BLO can be reformulated into a nonconvex optimization problem with a smooth constraint. A single loop algorithm is proposed based on the formulation, leveraging the structure of the Moreau envelope. The author also provides a non-asymptotic rate for the algorithm and conducts numerical experiments to show its superiority.

### Strengths
1. The application of the Moreau envelope gives a nice reformation for the BLO. Compared with traditional value function reformation, the Moreau envelope-based reformation is a smooth problem and easier to solve.

2. Non-asymptotic convergence rate is developed for the proposed method without using the PL condition.

### Weaknesses
1. In the nonconvex case, (4) is only a relaxed version of the original BLO. It is not clear whether the global optimal solutions, local optimal solutions, and stationary points of (4) are related to the original BLO. Specifically, the paper does not provide a clear connection between the stationary points of the relaxed problem and the original bilevel problem, especially when the lower-level problem is non-convex. This raises concerns about the practical relevance of the proposed stationarity measure. The analysis should clarify under what conditions the stationary points of the relaxed problem correspond to meaningful solutions of the original problem, and what guarantees can be provided in the general non-convex case.

2. Assumption 3.2 (ii) appears too technical and artificial. The author does not convince me of its practicability, because the given examples are simple and no theoretical results is ensuring Assumption 3.2 (ii). The assumption involves a Lipschitz condition on the proximal operator with respect to the upper-level variable, which is not standard and requires careful justification. The paper should provide more concrete examples of practical regularizers that satisfy this condition, especially in the context of non-convex lower-level problems. A more detailed discussion of the implications and limitations of this assumption is needed.

3. In Theorem 3.1, it is strange to say that "there exists $c_{\alpha},c_{\beta}>0$" as the upper bounds of the stepsizes $\alpha_k,\beta_k$. This appears to be impractical since only the existence of $c_{\alpha},c_{\beta}$ does not suggest how to choose the right stepsizes in implementation. The theorem should provide more concrete guidance on how to select appropriate step sizes in practice. The current formulation leaves a significant gap between the theoretical result and practical implementation, as the existence of such bounds does not translate into a practical method for choosing them.

### Questions
Do the models in the experiments satisfy the Assumptions previously assumed?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a stochastic first-order algorithm based on the Moreau envelope reformulation.  Non-asymptotic convergence analysis under weaker conditions than previous works is provided. The proposed algorithm is evaluated on various setups, including few-shot learning, data hyper-cleaning, and neural architecture search.

### Strengths
1. The method looks novel.
2. Experiments look good.

### Weaknesses
1. Although the assumptions are indeed weaker than previous works, the convergence measure is also different from many previous works, so the results may not be directly comparable. This makes it difficult to assess the true practical improvement of the proposed method over existing approaches. The use of a different convergence measure, while potentially necessary given the weaker assumptions, obscures the performance gains relative to methods that optimize for the hypergradient directly. It is unclear if the proposed measure is a meaningful proxy for hypergradient convergence in practice.
2. I think the recent paper which has a strong theoretical guarantee should be cited. Kwon, Jeongyeol, et al. "On Penalty Methods for Nonconvex Bilevel Optimization and First-Order Stochastic Approximation." arXiv preprint arXiv:2309.01753 (2023).

### Questions
1. What does the "Rethinking" in the title mean? Why do we need to rethink? What is the finding after rethinking?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
