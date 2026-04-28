# High dimensional Bayesian Optimization via Condensing-Expansion Projection

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 5, 3

## Abstract
In high-dimensional settings, Bayesian optimization (BO) can be expensive and infeasible. The random embedding Bayesian optimization algorithm is commonly used to address high-dimensional BO challenges. However, this method relies on the effective subspace assumption on the optimization problem's objective function, which limits its applicability. 
In this paper, we introduce Condensing-Expansion Projection Bayesian optimization (CEPBO), a novel random projection-based approach for high-dimensional BO that does not reply on the effective subspace assumption. The approach is both simple to implement and highly practical. 
We present two algorithms based on different random projection matrices: the Gaussian projection matrix and the hashing projection matrix. 
Experimental results demonstrate that both algorithms outperform existing random embedding-based algorithms in most cases, achieving superior performance on high-dimensional BO problems.
The code is available in \url{https://anonymous.4open.science/r/CEPBO-14429}.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes CEPBO, a high-dimensional BO method following subspace embedding technique. In each iteration, CEPBO samples an embedding matrix A_t based on one of the two techniques: (1) Gaussian projection matrix (similar to the embedding matrix of REMBO) or (2) hashing projection matrix (similar to the embedding matrix of HESBO and BAxUS). CEPBO then project observed data in original space X to embedded space Y, build GP in Y. After maximizing acquisition function in Y, CEPBO project the proposed data point back to X to evaluate f(x).

### Strengths
-	The writing is easy to understand.
-	CEPBO generates new projection matrix every iteration, compared to REMBO, HeSBO and ALEBO use fixed matrix during the optimization process. Even more recent methods such as BAxUS [1] and Bounce [2] do not apply this technique. They only sample 1 projection matrix during each subspace.
-	The authors provide some theoretical analysis for CEPBO.

### Weaknesses
The use of low-dimensional space is not generally new, and it is not surprising that the method would yield certain benefits. However, the explanations and theory provide are insufficient to understand from which perspective the proposed method would offer such advantages.
My major concern is that the process of mapping the candidate point back to the pre-image will be arbitrary. Can the authors explain why they did not consider using the pseudoinverse of A? In general, finding the pre-image is an ill-posed problem. The authors have to be cautious about using A^\top. Can the authors guarantee that the deviation of the proposed method from the best result of the true pre-image will be minimal? The equality of the expectation of A^\topA and the identity matrix in Eq. (1) is insufficient.

### Questions
- My biggest concern is for the authors to provide empirical comparison against the method BAxUS. 
- In Section 3.4, addressing the boundary issue, the authors apply scaling to the two convex projections. What is the motivation for this scaling?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors consider low-dimensional Bayesian optimization (BO) using random linear projections. The variables for optimization are projected onto a low-dimensional space, and the next query point is selected using BO within this space. The point is then transformed back to the original variable space using the transpose of the projection matrix. The method is justified by the property that the “expectation” of the inner product of projection matrices is the identity matrix.

### Strengths
The paper explores a simple and fast method of using random projections to accelerate the BO. Many experimental results indicate that the proposed method is competitive.

### Weaknesses
The use of low-dimensional space is not generally new, and it is not surprising that the method would yield certain benefits. However, the explanations and theory provide are insufficient to understand from which perspective the proposed method would offer such advantages.
My major concern is that the process of mapping the candidate point back to the pre-image will be arbitrary. Can the authors explain why they did not consider using the pseudoinverse of A? In general, finding the pre-image is an ill-posed problem. The authors have to be cautious about using A^\top. Can the authors guarantee that the deviation of the proposed method from the best result of the true pre-image will be minimal? The equality of the expectation of A^\topA and the identity matrix in Eq. (1) is insufficient.

### Questions
The paper is clearly written, and I have no question.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work introduces a search strategy in high-dimensional BO problems called the 
Condense-Expansion Projection technique. It generates a random projection matrix to project the high-dimensional data to the low-dimensional embedding space. Then it projects the searched data point back to the high-dimensional space for evaluation in the original space. The random projection matrices are the existing Gaussian projection matrix and the hashing projection matrix. They result in the development of two algorithms: CEP-REMBO and CEP-HeSBO. The experiments demonstrate the effectiveness of the both algorithms on simulation and real-world datasets.

### Strengths
This work presents two algorithms based on the existing random projection matrices: the Gaussian projection matrix and the hashing projection matrix, and Condensing-Expansion Projection Bayesian optimization. Experimental results demonstrate that the algorithms outperform existing random embedding-based algorithms on high-dimensional BO problems. The presentation of this paper is good. The research field of this paper is significant. The overall structure is relatively clear.

### Weaknesses
This work could be improved from several angles.

1.It is common knowledge that approximation methods can reduce the performance of algorithms. And one of the main advantage of approximation methods is reducing the complexity of the algorithm. The motivation of this work is: “In high-dimensional settings, Bayesian optimization (BO) can be expensive and infeasible.” How does this work validate the motivation of “expensive”? Please provide a specific complexity analysis comparing the proposed method to standard high-dimensional BO, and to include runtime comparisons in the experiments. 

2.The Condensing-Expansion technique on random projections has been proposed and successfully applied in many fields, such as federated learning [1]. The random projection matrices are the existing Gaussian projection matrix and the hashing projection matrix. They have been applied in many fields. This work is a simple migration without novelty. It is trivial. Could you more clearly articulate the novelty of applying this technique to Bayesian optimization specifically? Are there unique challenges or benefits in this domain? Additionally, please provide a more thorough comparison to how these techniques are used in other fields to highlight any key differences or innovations in the proposed approach.

[1] Song Z, Wang Y, Yu Z, et al. Sketching for first order method: efficient algorithm for low-bandwidth channel and vulnerability[C]//International Conference on Machine Learning. PMLR, 2023: 32365-32417.

3.There is no organization section. To improve the readability of this paper, It would be better to add the organization section.

### Questions
See “Weaknesses”

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a high-dimensional Bayesian optimization framework that uses the Condensing-Expansion Projection technology to avoid the assumption of effective dimensions. The new algorithm CEPBO is proposed based on two methods of Gaussian and hash-augmented projection matrices. Experiments show the effectiveness of CEPBO in various optimization tasks.

### Strengths
- The novel method cleverly circumvents the strong assumption of "effective dimension", which is very exciting. If the doubts in "Questions" can be answered, this article will undoubtedly make a great contribution.

- Sufficient mathematical derivation and proof of the feasibility of Condensing-Expansion Projection.

- Sufficient experiments in real environments. Detailed experimental description in the Appendix.

### Weaknesses
- There is a notable absence of comparisons with more recent methods. The paper only compares REMBO (2013), HesBO (2019), and ALEBO (2020), which are several years old. It fails to include the latest embedding-based approaches such as CoBO [1], BAxUS [2], MAVE-BO [3], and DSO [4]. Additionally, other high-dimensional Bayesian optimization algorithms not based on embeddings, like Vanilla BO [5], and MCTS-VS [6], are also missing from the comparison. To my knowledge, TurBO [7] has demonstrated strong performance in handling high-dimensional optimization tasks, yet it is not included in the comparative experiments. 

- This paper merely demonstrates the feasibility of CEP (Formulas 2 and 3). Specifically, when the solution x is transformed into the solution \tilde{x} through CEP, the authors prove the effect of d on the difference between x and \tilde{x}. However, the selection of d directly affects the success probability of CEP, but how to determine the appropriate d is not discussed. From another perspective, in the method presented, the solution space is \mathbb{R}^D, and the search subspace is \mathbb{R}^d, which is a subspace of the solution space. The gap between these spaces is enormous, and for the optimal solution x^* \in X, the probability of successfully finding the optimal solution in the subspace has not been proven or theoretically guaranteed, which is the key issue.

- The experiment raises doubts about whether it was deliberately designed to create scenarios favorable to the algorithm. For example, in Figure 2, ALEBO did not converge on the Holder Table function, yet the results were truncated by the authors at 50 iterations. Similarly, the experiments on real-world problems involve dimensions no greater than 100, which cannot be considered as high-dimensional tasks. This raises doubts about whether CEPBO is truly capable of handling high-dimensional problems in practical applications.

- Typos. Although I focused on the content of the article, I still found many typos. This paper needs to be carefully checked, otherwise it cannot be published. For example, there are two "as" in line 144. In line 233 (line 9 of Algo.1), the subscript t of y_t is incorrectly bolded (at the end of this line). 

- The paper was not well prepared, with the above typos and many other details. For example, the text in Figure 3 is too small and completely unreadable.

[1] Advancing bayesian optimization via learning correlated latent space. NeurIPS 2023. 

[2] Increasing the scope as you learn: Adaptive bayesian optimization in nested subspaces. NeurIPS 2022. 

[3] An adaptive dimension reduction estimation method for highdimensional bayesian optimization. 2024. 

[4] Dual-space optimization: Improved molecule sequence design by latent prompt transformer. 2024. 

[5] Vanilla Bayesian Optimization Performs Great in High Dimensions. ICML 2024. 

[6] Monte carlo tree search based variable selection for high dimensional bayesian optimization. NeurIPS 2022. 

[7] Scalable Global Optimization via Local Bayesian Optimization. NeurIPS 2019.

### Questions
1. The comparison methods are outdated, and the experiments are unconvincing. As mentioned in the "weaknesses", high-dimensional Bayesian optimization is a rapidly evolving field, with at least 60 highly relevant works published since 2013, including at least 20 based on embeddings. Comparing only with the older methods like REMBO and HesBO is insufficient, and even ALEBO, published in 2020, is no longer the state-of-the-art. Can the authors conduct thorough comparative experiments with relevant works (such as [1-7]) from the past three years to demonstrate the superior performance of CEPBO?

2. Why did the authors limit the optimization in the benchmark function experiments to only 50 iterations? In Figure 2, ALEBO clearly does not converge on the Holder Table function. Does this seem fair and reasonable? Was the choice of 50 iterations deliberately designed by the authors?

3. A key issue in high-dimensional BO is the choice of subspace dimension. The related work relies on "whether the low-dimensional subspace can cover the effective subspace of the objective function". Although CEPBO does not explicitly rely on the concept of effective dimensionality, the method is still influenced by the potential complexity of the objective function. In practice, the selection of the low-dimensional space (i.e., the setting of d) directly impacts the algorithm's performance, as d determines the proximity between x and \tilde{x} in the Condensing-Expansion Projection. Although CEPBO relaxes the strong assumption of effective dimensionality, how to select d remains an unresolved issue. How do the authors address this problem?

4. Another key issue in high-dimensional BO is the boundary issue, which is affected by the choice of subspace boundaries and embedding matrix. The embedding matrix in this paper is fixed, so I won't address that further here. However, in Section 3.4, why is the scaling factor chosen as \sqrt{D}? From experience, I know that this is a crucial parameter, yet the authors have fixed it without providing any theoretical justification or hyperparameter analysis. I couldn’t find a relevant explanation for this decision. One of the key factors affecting the embedding methods is the ability to determine the scale of the embedding according to the problem. How do the authors address this problem?

5. The authors conducted experiments on 4 real-world problems. However, these problems are not high-dimensional tasks (the dimensions are 12, 14, 36, and 60 respectively). Could the authors add real-world high-dimensional tasks, such as problems with D > 200?

6. A small question: do all the proofs in the appendix assume that x takes values in the real space \mathbb{R}^D ? If the feasible domain of x is constrained, especially when it is not symmetric around the origin, do these theorems still hold?

7. Based on the above question, intuitively, the Condensing-Expansion Projection may be influenced by the shape of the feasible domain. Could the authors provide additional experiments under different function characteristics, particularly with complex feasible domains? Test functions can be found at https://numbbo.github.io/coco/testsuites/bbob. 

8. Based on the current experimental results, when the function has an intrinsic effective dimension d_e, if the experimental setting uses d > d_e, other methods based on the effective dimension assumption maybe outperform CEPBO, which may affect the practicality of CEPBO. Could the authors add these experiments? If CEPBO can achieve good performance, this paper will be very exciting and practical!

### Soundness
2

### Presentation
2

### Contribution
2
