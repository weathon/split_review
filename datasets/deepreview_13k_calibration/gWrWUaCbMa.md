# A Truncated Newton Method for Optimal Transport

- Decision: Accept
- Avg Score: 5.67
- Scores: 6, 6, 5

## Abstract
Developing a contemporary optimal transport (OT) solver requires navigating trade-offs among several critical requirements: GPU parallelization, scalability to high-dimensional problems, theoretical convergence guarantees, empirical performance in terms of precision versus runtime, and numerical stability in practice. With these challenges in mind, we introduce a specialized truncated Newton algorithm for entropic regularized OT. In addition to proving that locally quadratic convergence is possible without assuming a Lipschitz Hessian, we provide strategies to maximally exploit the high rate of local convergence in practice. Our GPU-parallel algorithm exhibits exceptionally favorable runtime performance, achieving high precision orders of magnitude faster than many existing alternatives. This is evidenced by wall-clock time experiments on 4096-dimensional MNIST and color transfer problems. The scalability of the algorithm is showcased on an extremely large OT problem with $n \approx 10^6$, solved approximately under weak entopric regularization.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a truncated Newton method, a second-order algorithm, to solve the Entropic-regularized Optimal Transport problem.

### Strengths
The paper has interesting theoretical results, such as the connection to the Bellman equation (though I'm not sure if this is the first work to establish that connection) and the convergence in Chi-square distance of Sinkhorn algorithm (again, I'm not sure if this result is previously established and to the best of my knowledge this is the first time I see this result).

Theorem 3.2 is interesting since it's a log(1/eps) convergence result, though I skeptical of the dependence on other terms could harm the convergence. The authors should discuss this result, as to the best of my knowledge, the only other equivalent result is in this work [1] (UOT can be viewed as a generalization/approximation of OT, I think this work should be cited in discussion to this work as well).

The paper has strong experiment settings that show superior result on wall-clock time and the color transfer result is very nice. The authors also have a detailed description for an efficient implementation of proposed algorithm.

[1] "On Unbalanced Optimal Transport: Gradient Methods, Sparsity, and Approximation Error".
Quang Minh Nguyen, Hoang Huy Nguyen, Lam Minh Nguyen, Yi Zhou
Journal of Machine Learning Research, (JMLR), 2023

### Weaknesses
The complexity in Theorem 3.2 depends on the spectral gap of $P_{rc}$, but there is no control over this spectral gap. I suspect that this could lead to very poor convergence should the spectral gap is very bad. I recommend having some analysis on this term to make the results stronger. Additionally, it is possible for this term to be $n$ dependent too, so the $n$ dependence of the complexity might more than just $O(n^2)$. If that this is the case, the method is a tradeoff between $n$ and $\epsilon$.

The paper is a bit hard to read and it is hard to follow the intuition of the paper. The proof should have been explained better, such as the chi-square convergence. Furthermore, the notations are not clearly explained or presented (see below).

### Questions
Various notations used in the manuscript is not clear or hard to find the definition. For example, what is $\mu$? Some intuitive explanation of $P_{rc}$ would be nice also. I recommend adding more to the notation section and explain these better.

In the experiment section, can the authors compare the method with other second-order methods, if any?

Also, can you give an intuitive explanations of how you do the proofs (main ideas or a high-level analysis like an ODE analysis)? I'm very interested in the results, and maybe in the later iterations of the paper you can incorporate these proof sketches to help the readers also.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper introduces a truncated newton method for solving entropic optimal transport problem. The algorithm is GPU-parallel and is scalable for large OT problem.

### Strengths
1. The proposed algorithm has good practical performance under GPU settings. 
2. The author has done a good job in discussing the related work.

### Weaknesses
1. The definitions of $\epsilon$ and $\epsilon^\prime$ are not clearly differentiated. It would be beneficial to provide a more precise explanation of how these parameters relate to the dual gradient norm and the $\chi^2$ divergence, respectively. Furthermore, the role of $\tilde{\epsilon}$ and its connection to the overall convergence criteria needs clarification.

2. The proposed algorithm lacks a theoretical convergence analysis and a comprehensive assessment of its computational complexity. While popular OT solvers like Sinkhorn and APDAGD offer promising guarantees on total computational complexity, the theoretical complexity of this algorithm remains unclear to me. Specifically, the paper does not provide a global convergence rate proof, which is crucial for understanding the algorithm's efficiency in a broader context. Although the local convergence analysis is mentioned, it does not fully address the concerns regarding the overall computational cost, especially when compared to the $\tilde{O}(n^2 \varepsilon^{-1})$ rate of other methods. 

3. The explanation of the LogSumExp (LSE) reductions in Line 066-067 is not sufficiently detailed. Providing explicit formulas for the row and column reductions, denoted as $\mathrm{LSE}_r(X)$ and $\mathrm{LSE}_c(X)$, would improve the clarity and reproducibility of the method.

### Questions
1. Could the author make the theorems self-contained? For example, what is $\lambda_2$ in Corollary 3.4?
2. What does helper Sinkhorn mean in Line 196?
3. The definition for LSE is not clear in Line 066-067.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents a new Newton-based optimization method for entropic regularised optimal transport. The authors present a new three-stage method that combines truncated Newton method, conjugate gradient and mirror descent. Finally, the authors present experiments with fast convergence of the proposed method.

### Strengths
In the proposed framework, the authors propose a lot of engineering improvements to make the method more stable and effiicient from the practical point of view.

### Weaknesses
The Weaknesses and Questions are together. 

1. The section 2.1. is concerning and confusing.  First of all, lines 70-92 are almost exactly copied from  Kemertas et al. (2023), which is concerning. Secondly, the problem 2 is wrongly defined. It is not convex. It should be $+H(P)$. Thirdly, The dual problem is also unusual for me. Normally, the dual problem has a form of LogSumExp. In the paper, it is the sum of exponents. Please, provide how do you get formulas 3 and 4 in Appendix. 

2. The major results from my perspective are more focused on practice and involve a lot of engineering improvements. Hence, the major proof of success should be experiments. However, from my perspective, the experiments are not good enough for a practical paper. a) First of all, there is only one figure with 2 examples, which is not enough. b) Secondly, in Fig.2, the proper loss should be a duality gap, not a primal function value. As the primal function value excludes constraints' violation and can be misleading. Also, the figure with feasibility may also help in Appendix, as well as for the dual loss. c) The presented results in Fig.2 are presented without statistical measures. It means that it was only one run, which can be quite stochastic, especially with respect to wall-clock time. d) All methods are starting from different points, which is very concerning. e) The results are only presented with respect to wall-clock time. I would recommend adding another measure that is not based on code performance, for example number of calculated gradients or something like that. Otherwise, MDOT code can be optimized for performance and compete with other methods that are not optimized. f) Finally, I didn’t find any attached code to verify the performance.

3. Do I understand correctly, that at the beginning, in practice, there is a part of pure adaptive mirror descent to find a near solution as a starting point, and then the algorithm performs Algorithm 4?

### Questions
see weaknesses

### Soundness
2

### Presentation
2

### Contribution
2
