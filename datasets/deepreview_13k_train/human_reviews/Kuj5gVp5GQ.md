# Accelerating Sinkhorn algorithm with sparse Newton iterations

- Decision: Accept
- Scores: 6, 6, 8, 8

## Abstract
Computing the optimal transport distance between statistical distributions is a fundamental task in machine learning. One remarkable recent advancement is entropic regularization and the Sinkhorn algorithm, which utilizes only matrix scaling and guarantees an approximated solution with near-linear runtime. Despite the success of the Sinkhorn algorithm, its runtime may still be slow due to the potentially large number of iterations needed for convergence. To achieve possibly super-exponential convergence, we present Sinkhorn-Newton-Sparse (SNS), an extension to the Sinkhorn algorithm, by introducing early stopping for the matrix scaling steps and a second stage featuring a Newton-type subroutine.
    Adopting the variational viewpoint that the Sinkhorn algorithm maximizes a concave Lyapunov potential, we offer the insight that the Hessian matrix of the potential function is approximately sparse. Sparsification of the Hessian results in a fast \(O(n^2)\) per-iteration complexity, the same as the Sinkhorn algorithm. 
    In terms of total iteration count, we observe that the SNS algorithm converges orders of magnitude faster across a wide range of practical cases, including optimal transportation between empirical distributions and calculating the Wasserstein \(W_1, W_2\) distance of discretized densities. The empirical performance is corroborated by a rigorous bound on the approximate sparsity of the Hessian matrix.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Despite the success of the Sinkhorn algorithm, its runtime may still be slow due to the potentially large number of iterations needed for convergence. To achieve possibly super-exponential convergence, we introduce Sinkhorn-Newton-Sparse (SNS), an extension to the Sinkhorn algorithm, by introducing early stopping for the matrix scaling steps and a second stage featuring a Newton-type subroutine.

### Strengths
Sparsification of the Hessian results in a fast per-iteration complexity, the same as the Sinkhorn algorithm. In terms of total iteration count, we observe that the SNS algorithm converges orders of magnitude faster across a wide range of practical cases, including optimal transportation between empirical distributions and calculating the Wasserstein distance of discretized continuous densities. The empirical performance is corroborated by a rigorous bound on the approximate sparsity of the Hessian matrix.

### Weaknesses
1. The theoretical results in this paper seem to be simple corollaries of existing resluts.
For example, Eq. (7) which is crucial to the proof of Theorem 1, follows Corollary 9 of (Weed, 2018).
2. Theorem 1 requires that $\eta$ is large enough. However, I believe that a large $\eta$ will bring something negative.
Otherwise, why don't people minimize the original problem without the regularization? Thus, I think the author should remark the condition that $\eta$ is large enough of Theorem 1 and clarify how the value of $\eta$ affect the convergence rate.
3. The paper claims that ``to achieve possibly super-exponential convergence, we introduce Sinkhorn-Newton-Sparse (SNS)''. However, this paper does not provide any sound convergence analysis of SNS.

### Questions
No

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces the sinkhorn-newton-sparse algorithm to solve the regularised optimal transport problem as described in eq (1). This improves on the previous work by Brauer et al. to the case of sparse transport matrices. The authors define the notion of sparsity as in Definition 1 and provide the rate of convergence of the modified sinkhorn algorithm in theorem 1. The authors then provide the approximate sparsity rate for the newton step in theorem 2. The paper is closed with numerical examples.

### Strengths
There is a notable reduction in the number of iterations and the time to convergence while solving a problem using Algorithm 1. It also seems that the definition of sparsity plays a key role in the analysis.

### Weaknesses
One notable omission I felt was the lack of guarantees for computational complexity. Although the algorithm performs well numerically, there is no theoretical backing for that. It is also unclear how the approximate sparsity definition connects to the traditional definition in the Frobenius norm. The definition of sparsity seems to be a critical component of the analysis, yet the connection to existing notions of sparsity is not clearly established. Specifically, it is not clear why one would approximate the Hessian $M$ with a sparse $\bar M$ as opposed to directly working with $M$.

### Questions
Can the authors explain the notion of sparsity introduced in this paper? It seems to me that $\tau$ is just the proportion of non-zero elements. However, is it usual to approximate $M$ by a sparse $\bar M$?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a method for the fast numerical solution of the Kantorovich problem with entropic regularization. The submission is closely related to the cited work of Brauer, Clason, Lorenz and Wirth that explored the use of Newton iterations for this problem. The main contributions are two-fold:
1. The observation (that the authors prove) that after several Sinkhorn iterations, the Hessian matrix becomes close to sparse.
2. An algorithm based on this observation that combines several iterations of Sinkhorn followed by Newton iterations with a sparsified Hessian. The Hessian is sparsified by zeroing-out small entries.

### Strengths
* The paper focuses on the important and timely problem of efficiently computing regularized optimal transport.
* The authors clearly explain the potential advantages of second-order methods while noting the inefficiency of classic Newton iterations. This motivates their approach of using a sparse approximation to the Hessian.
* The convergence of the Hessian to a nearly-sparse matrix throughout the steps of the algorithm is proved (in both the Sinkhorn and Newton stages).
* The method is clearly explained and the results should be easy to reproduce.

### Weaknesses
 * A potential red flag is that, in the numerical results, only a single entropic regularization coefficient is considered (\eta=1200). I suspect that this is a weak regularization term which results in rather sparse couplings and is therefore favorable to their method. It is OK if the method is not beneficial in the strong-regularization regime. However, this needs to be acknowledged in the paper and not swept under the rug. The choice of a single, potentially weak, regularization parameter limits the generalizability of the conclusions, as the performance of entropic regularization methods can vary significantly with the strength of the regularization. This makes it difficult to assess the practical applicability of the proposed method across different scenarios.

* The method is not compared to any other current methods aside from the classical methods on which it is based (Sinkhorn and Newton). The lack of comparison with state-of-the-art methods makes it difficult to assess the true contribution of the proposed approach. While the authors demonstrate improvement over Sinkhorn and Newton, it is crucial to benchmark against other recent advances in the field to understand the relative performance gains. This is especially important given the rapid progress in optimal transport algorithms.

### Questions
* For the numerical section, I would like to see numerical results for the same data sets with several regularization strengths (e.g. \eta=10,100,1000). Additionally, I think it is important to compare the proposed method to other current methods for accelerating OT with entropic regularization. In particular to "Massively scalable Sinkhorn distances via the Nystrom method" by Altschuler, Bach, Rudi, and Niles-Weed (2019). 

* Have you considered any quasi-Newton methods? Will these be applicable in the context of your paper?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors focus on accelerating the Sinkhorn algorithm for optimal transport (OT). The Sinkhorn algorithm is an iterative matrix scaling algorithm used to solve the entropy-reularized OT problem. Its per-iteration complexity is $O(n^2)$ for discrete distributions of size $n$. Its convergence rate behaves like a polynomial converging method, which can be slow. Other optimization methods like second-order methods enjoy super-exponential convergence, but a greater per-itereration cost $O(n^3)$ (e.g. Newton). Here they find a link between the Sinkhorn iterations and the sparsity of the Hessian of the Lyapunov potential. Once the Hessian is sparse, the per-iteration cost can reach $O(n^2)$, hence the same per-iteration cost as Sinkhron while benefiting from the faster convergence rate of the second-order methods. The authors propose to combine the two methods, i.e. Newton iteration once the Hessian is sparse, which improves the convergence rate. They provide quantitative results to validate the algorithm.

### Strengths
- The overall presentation of the manuscript is good, and the method is clear.
- The method accelerates the convergence of the Sinkhorn algorithm without increasing the per-iteration cost.  
- The method is theoretically motivated by theorem 1; we know that after some Sinkhorn steps the Hessian can be sparse, hence the per-iteration cost of Newton's methods is lower.

### Weaknesses
 - I find the evaluation a bit limited. In particular, it would be great to see more results for different regularization parameter, and include standard deviation in the tables. 
- It would be great to have comparison with other methods than Sinkhorn, although I agree that most methods can be combined with SNS, it would be beneficial to compare their convergence.
- Have you tried removing the Sinkhorn stage  ($N_1=0$) ? I would like to understand how much of the sparsity is due to Sinkhorn (Thm1) vs the `Sparsify` step in Alg.1, and its influence on the convergence.



### Questions
Questions and minor comments.

- I believe that to compute the optimality gap (e.g. Fig.1) you need a ground truth (i.e. the minimizer), in this case how is it computed ? Is it the OT plan without entropy regularization ?
- I might be missing something, but I don't see the target sparsity $\lambda$ in Alg.1.
- How do you choose the number of Sinkhorn steps $N_1$? Would it be possible to switch to the Newton stage once the Hessian is sparse enough ? 
- The related work section is great, but maybe you can add other references that speed up Sinkhorn using a factorization of the ground cost [1,3] or Chebyshev polynomials with a sparse graph [2]. 
- The results in Tab.1 are on the number of iterations until reaching machine accuracy. They don't inform us on the quality of the approximation. It could be interesting to compare the accuracy of the plan in the case where we have a closed form (e.g. entropic OT between Gaussian distributions [4]). 
- The authors could add a brief review of Newton’s algorithm since it is an important piece of the paper. In particular, on the importance of solving the Hessian system. 
- In eq. 1, you need to define $\eta$ and specify if it should be greater than zero.
- Having a preliminary or background section could help. Parts of the introduction could be in this section, and definition such as the optimality gap could be added in that section.
- In section 2 "Convergence of Sinkhorn", what is $\alpha$ ? Should it be $\eta$ ?

[1] Scetbon, Meyer, Marco Cuturi, and Gabriel Peyré. "Low-rank Sinkhorn factorization." International Conference on Machine Learning. PMLR, 2021.

[2] G. Huguet, A. Tong, M. R. Zapatero, C. J. Tape, G. Wolf and S. Krishnaswamy, "Geodesic Sinkhorn For Fast and Accurate Optimal Transport on Manifolds," 2023 IEEE 33rd International Workshop on Machine Learning for Signal Processing (MLSP).

[3] Scetbon, Meyer, and Marco Cuturi. "Linear time Sinkhorn divergences using positive features." Advances in Neural Information Processing Systems 33 (2020): 13468-13480.

[4] Mallasto, A., Gerolin, A., & Minh, H. Q. (2022). Entropy-regularized 2-Wasserstein distance between Gaussian measures. Information Geometry, 5(1), 289-323.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
