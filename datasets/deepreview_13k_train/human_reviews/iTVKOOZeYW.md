# $\psi$DAG : Projected Stochastic Approximation Iteration for DAG Structure Learning

- Decision: Reject
- Scores: 5, 5, 3, 6

## Abstract
Learning the structure of Directed Acyclic Graphs (DAGs) presents a significant challenge due to the vast combinatorial search space of possible graphs, which scales exponentially with the number of nodes. Recent advancements have redefined this problem as a continuous optimization task by incorporating differentiable acyclicity constraints. These methods commonly rely on algebraic characterizations of DAGs, such as matrix exponentials, to enable the use of gradient-based optimization techniques. Despite these innovations, existing methods often face optimization difficulties due to the highly non-convex nature of DAG constraints and the per-iteration computational complexity. In this work, we present a novel framework for learning DAGs, employing a Stochastic Approximation approach integrated with Stochastic Gradient Descent (SGD)-based optimization techniques. Our framework introduces new projection methods tailored to efficiently enforce DAG constraints, ensuring that the algorithm converges to a feasible local minimum. With its low iteration complexity, the proposed method is well-suited for handling large-scale problems with improved computational efficiency. We demonstrate the effectiveness and scalability of our framework through comprehensive experimental evaluations, which confirm its superior performance across various settings.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper studies structure learning in linear DAG models, e.g. to recover the underlying DAG from observational data. 
It follows score based learening approach and tries to optimize the square loss. It proposes to apply stochastic gradient descent to solve the optimization problem, and then introduces a procedure to estimate the topological ordering based on learned coefficient matrix.
The experiments are conducted on equal variance noise setting to compare with existing methods.

### Strengths
- The proposed method relies on SGD and is fast compared to other continuous optimization approaches for DAG learning.
- Simulation experiments are conducted to show the proposal gives faster convergence speed relative to the optimum.

### Weaknesses
 - The presentation is poor, many concepts are used without introduction, e.g. transitive closure, full DAG, $R$ in convergence statement.
- In the first step, SGD is applied to solve (11). But actually, the solution to (11) is simply W=I analytically. Also, fixing ordering, the third step  has analytical solution that is simply linear regression of each node onto preceding nodes. All SGD optimizations can be avoided.
- Ordering based DAG learning is a long line of research. This paper lacks citation and discussion on that. Especially, for the equal variance setup considered in this paper, there are scalable algorithms:

[1] Chen, W., Drton, M., & Wang, Y. S. (2019). On causal discovery with an equal-variance assumption. Biometrika, 106(4), 973-980.

[2] Gao, M., Tai, W. M., & Aragam, B. (2022). Optimal estimation of Gaussian DAG models. In International Conference on Artificial Intelligence and Statistics (pp. 8738-8757). PMLR.

- Where is the proof for Theorem 2? What is the $R$ in the statement? How do we relate this to other optimization results on DAG learning in literature?
- What is the intuition behind Alg 2? There is not explanation why it comes from and why we want to recover the ordering in this way. Any guarantee if it consistently outputs a valid ordering?

### Questions
- Where is the proof for Theorem 2? What is the $R$ in the statement? How do we relate this to other optimization results on DAG learning in literature?
- What is the intuition behind Alg 2? There is not explanation why it comes from and why we want to recover the ordering in this way. Any guarantee if it consistently outputs a valid ordering?

### Soundness
2

### Presentation
1

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
This paper proposes a novel stochastic approximation framework for learning DAGs, integrating SGD with efficient projection methods to enforce acyclicity. By addressing the non-convexity and complexity challenges of prior approaches, the method achieves low iteration complexity and demonstrates superior scalability and performance in extensive experiments.

### Strengths
1. This paper is well-written and easy to follow.
  
2. This paper introduces a novel stochastic approximation-based method for learning the DAG structure.
  
3. The paper provides comprehensive numerical experiments, which effectively demonstrate both the performance and efficiency of the proposed methods.

### Weaknesses
1. The stochastic approximation approach presented in this paper is limited to linear structural equation models (SEMs). In contrast, other methods such as GOLEM and DAGMA offer extensions to nonlinear SEMs. Expanding the proposed method to nonlinear settings could enhance its contribution.
  
2. The projection technique introduced in Algorithm 2 appears to lack a clear theoretical guarantee. Moreover, in line 339, the complexity of the projection method is stated as $\mathcal{O}(d^2)$. Given that the numerical experiments involve cases where $d$ can reach $10^4$, the complexity could escalate to approximately 108. This computational burden seems significant and may pose challenges for scalability in practice.
  
3. The paper could benefit from additional relevant references. For example, Deng et al. [A] propose a topological swap method to accelerate the optimization of the NOTEARS objective by identifying the topological order first and then learning the edge weights of the directed graph. This process aligns with the ideas explored in this paper, and including such a baseline would strengthen the completeness and contextualization of the work.

### Questions
1. Can the stochastic approximation method proposed in this paper be extended to nonlinear SEMs? If so, a discussion on the potential challenges or limitations in this direction would be insightful.
  
2. It appears that Theorem 2 may have been previously developed by Nemirovski and Yudin (1983). Could the authors clarify the novelty of this result, or highlight any differences from the original work?
  
3. Could the authors elaborate further on the scalability of the proposed method, particularly given the projection method’s complexity?
  
4. Would the authors consider including the topological swap method from [A] as a baseline? This comparison would provide additional insights into the performance of the proposed method relative to related approaches.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces $\psi$DAG, a new method for learning a directed acyclic graph (DAG) from observational data. The new method aims to improve on existing approaches in terms of scalability. Its theoretical complexity is $O(d^2)$, improving on $O(d^3)$ for popular alternatives. This theoretical improvement is demonstrated in computational experiments.

### Strengths
The scalability of $\psi$DAG is impressive, and I found the computational experiments convincing. The paper is well-written and contains a good mix of material.

### Weaknesses
1. One of the main contributions outlined on page 2 is a proof of Algorithm 1's convergence rate (Theorem 2). I could not see a proof of Theorem 2 in the paper or appendix.
2. The projection algorithm (Algorithm 2) is a key component of the computational machinery, but it remains opaque. It would be insightful to write this projection in terms of an optimization problem and discuss whether the algorithm attains a stationary point of this problem.
3. My primary concern with this paper is the lack of synthetic experiments comparing the *statistical* properties of the competing approaches. Only the computational merits of each approach are compared. It is essential to understand how $\psi$DAG performs on the synthetic data in terms of SHD, TPR, and FPR.
4. A few aspects of the real data example need clarification. First, the reason for having training and testing sets of size $n=853$ and $n=902$ instead of the whole dataset ($n=7466$) is not explained. Second, the role of the testing set is unclear, since the metrics reported do not require a testing set. Finally, I have seen DAGMA run on this dataset before, so I am confused about why it fails now.

### Questions
1. Page 1 Line 37: Missing an "and" at the end of the sentence.
2. Page 2 Line 86: Should it say "handling up to 10000 *nodes*"?
3. Page 3 Line 114: Is $X=(X_1,\ldots,X_n)$ a concatenation of column vectors? If so, I think the quantity on the RHS should be transposed. Same for $N$ on Line 126.
4. Page 3: I found it strange that the matrix $W$ is boldface while the matrix $X$ is not.
5. Page 4 Line 168: The $\overset{def}{=}$ looks different here compared with other equations.
6. Page 4 Line 185: The bit that says "where $\xi\in\Xi$ is a random variable drawn from the distribution $\Xi$" confused me. I think it should read "where $\xi$ is a random variable that follows the distribution $\Xi$".
7. Assumption 1: The quantity $\sigma_1^2$ is not defined.
8. Page 4 Line 211: The quantity $R$ is not explained.
9. Page 5 Line 263: $V_J$ should be $V_j$.
10. Figure 1: What is $\bar{x}$?
11. Page 7 Line 330: Can you be more precise than "closest"? Since the projection is heuristic, the word "close" might be better.
12. Page 7 Line 337: What does "topologically through" mean?
13. Figures 2, 3, and 4: The font size is too small for me to read without zooming in.
14. Page 15 Line 799: I am confused about the reference to GPUs in the computing section. Do any of the algorithms use GPUs?
15. Page 17 Line 866: If the edges in the ground truth DAG can be as small as 0.05, why apply a threshold of 0.3? That would make it impossible to ever recover the true graph.
16. Appendix A: I might have missed it, but I could not see the value of $\lambda$ used by $\psi$DAG.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper leverages stochastic optimization within a newly proposed framework for DAG learning, introducing a novel algorithm. The authors effectively demonstrate the efficiency of this algorithm through comprehensive experimentation.

### Strengths
This paper is the first I have encountered in differentiable DAG learning that integrates a stochastic algorithm, presenting a novel and compelling approach. A primary advantage of the stochastic algorithm lies in its computational efficiency, offering a marked improvement over conventional methods. The authors have also conducted an extensive set of experiments to substantiate the algorithm's efficiency, which I find to be thorough and convincing.

### Weaknesses
The paper’s approach is limited by its reliance on a simple linear model with equal variance noise, resulting in an easy optimization problem (least squares with $\ell_1$ penalty). When the graph order is fixed, the problem reduces to a Lasso optimization, which is computationally trivial for large dimensions (e.g., $d =1000,n =5000$), taking only a few seconds or minutes to solve. This simplicity undermines the significance of the study. The initial step of the proposed algorithm involves solving an unconstrained optimization problem using stochastic gradient descent (SGD), which, in the case of a linear model, will likely converge to a solution close to the zero matrix, given the enforced zero diagonal. This initial solution, being far from a valid DAG, provides little meaningful information for determining a useful ordering. Furthermore, the subsequent application of SGD to solve a LASSO problem is inefficient, as LASSO can be solved much more effectively with standard optimization techniques, rendering the use of SGD redundant in this context. To make the work more meaningful, the authors might consider applying their stochastic algorithm to more complex structural equation models (SEM), where optimization challenges are more substantial.

Additionally, several statements in the paper lack rigor. For example, the abstract and Theorem 2 claim that the algorithm converges to a feasible local minimum, but no theoretical proof or justification is provided for Algorithm 1, which is crucial given the NP-complete nature of the problem in (11). The claim that the minimum of the loss function within a fixed ordering corresponds to a local minimum of the overall loss function (11) is not generally true and requires rigorous proof with explicit assumptions, as demonstrated in prior work [4]. Original guarantee of local optimal solution from [1][2] can not be directly applied here, since it is unconstrained optimization and objective function is convex. Please refer to [3][4], these two paper study the local optimality of problem (11) indetails, they should be included and discussed appropirately in the paper. Furthermore, the transitive closure of $\mathcal{G}$ in lines 261-262 lacks a formal definition, which should be added for clarity.

The experimental setup also introduces concerns. The authors sample edge weights from a non-standard range, uniformly from $[−1, −0.05] \cup [0.05, 1]$, which deviates from established practices. Applying the same threshold (0.3) as methods like NOTEARS, DAGMA, and GOLEM in this unconventional setting risks removing correctly recovered edges, potentially skewing baseline performance and inflating the loss gap. This thresholding choice, while not affecting the optimization, does impact the evaluation and comparison with other methods. The chosen range and thresholding strategy deviates from common practices, which often use a range like $[-2, -0.5] \cup [0.5, 2]$ with a threshold of 0.3, and this difference makes it difficult to compare the results directly with existing literature. To address this, the authors should consider aligning with the edge weight sampling practices of prior studies to ensure comparability. Additionally, incorporating Structural Hamming Distance (SHD) as a recovery accuracy measure and including error bars to capture result variability would improve the robustness and interpretability of findings.

### Questions
No further quesions, questions are addressed above.

### Soundness
2

### Presentation
2

### Contribution
2
