# Efficient optimization with orthogonality constraint: a randomized Riemannian submanifold method

- Decision: Reject
- Scores: 6, 5, 5, 8

## Abstract
Optimization with orthogonality constraints frequently arise in various fields such as machine learning, signal processing and computer vision. Riemannian optimization offers a powerful framework for solving these problems by equipping the constraint set with a Riemannian manifold structure and performing optimization intrinsically on the manifold. This approach typically involves computing a search direction in the tangent space and updating variables via a retraction operation. However, as the size of the variables increases, the computational cost of the retraction can become prohibitively high, limiting the applicability of Riemannian optimization to large-scale problems.  To address this challenge and enhance scalability, we propose a novel approach that restricts each update on a random submanifold, thereby significantly reducing the per-iteration complexity. We introduce two sampling strategies for selecting the random submanifold and theoretically analyze the convergence of the proposed method. We provide convergence results for general nonconvex functions and functions that satisfy Riemannian Polyak–Łojasiewicz condition as well as for stochastic optimization settings. Extensive experiments verify the benefits of the proposed method, showcasing its effectiveness across a wide variety of problem instances.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper proposes a randomized Riemannian submanifold method for solving optimization problems constrained to the set of $n\times p$ orthogonal frames, also called the Stiefel manifold. The main innovation of the algorithm is to randomly select an $r$-dimensional subspace, in which the current iterate is rotated in a way that locally decreases the objective. In this way, the method can be seen as a Riemmanian analogue to the random block coordinate descent for Euclidean optimization. 

There are two sampling distributions considered for the random selection of the $r$-dimensional subspace: Haar uniform sampling on the orthogonal group and random selection of indices (referred to in the paper as a random permutation matrix). Both of these have the complexity of $nr^2$ although the latter can be computed in a more efficient way due to not needing to perform QR decomposition.

The paper provides global convergence analysis to critical points and local to a local minima (under PL-ineq.) in expectation and also in high-probability. The method can be also extended/analyzed to the stochastic variant when the objective gradients are random with bounded variance.

### Strengths
The idea of updating the iterate only in a subspace by rotations is not yet well explored and practically useful generalization of the random Riemannian coordinate descent. The paper provides extensive convergence analysis for the methods (although I haven't checked the proofs in the appendices in great detail). The paper is also well written and clearly explains the main concepts. There are multiple numerical experiments in the paper.

### Weaknesses
### Writing comments
Although the paper is well written overall, I have some remarks on formulation of certain ideas:
* Line 161: the authors state that the random submanifold is defined by the random orthogonal matrix $P_k$. This is not true strictly speaking, in fact, I think it is only the first $r$-columns of the matrix $P_k$ that define the subspace for the rotation.
* Adding on the remark above: Isn't it then enough to generate only a random orthogonal frame from $St(n,r)$ that defines the subspace?
* Lines 172 - 178: This part describes one of the the main technical observations: that it is possible to do a local approximation of the $\tilde F(Y)$ by computing retraction around an identity matrix. Can this be theoretically shown that this is a local approximation? It is not immediately clear to me why this is the case?
* Eq. 4: there is a mistake/typo after the first equality
* Line 198: this is very minor remark, but does the order of the first $r$ indices in the sampled permutation matrix matter? In this sense, wouldn't it be sufficient to sample $r$ indices without replacement instead of the permutation? Practically this might be the same so it might not matter.  

### References on sketching
This method seems to be related to random subspace sketching. For example a very recent work of (Shustin & Avron, 2024; https://www.jmlr.org/papers/volume25/21-1022/21-1022.pdf) considers random sketching algorithm for fast optimization over orthogonal constraints. This would be good to discuss in the paper (if indeed related), and possibly also to compare against in the numerical experiments. 

### Numerical experiments
The paper provides numerous numerical experiments but I would like to see the study of dependency on the choice of the random subspace dimension $r$. In the first experiment, the orthogonal procrustes, I am missing the information of the choice of $r$ altogether. I would also like to see a discussion on the computational cost of the random Haar uniform sampling of O(n) as I imagine this will be computationally complex operation.  

Overall, I like the main paper idea, but I am missing more direct comparison with sketching methods in Riemnannian setting as well as the explanation why we can expect (4) to hold as a good first order approximation to minimizing $\tilde F$. I would also like to see the numerical section improved with more extensive discussion on the choice of $r$ and how it relates to the per-iteration cost.

### Questions
* Could you use fast random subsampling methods, such as random Fast JL transform?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a randomized submanifold algorithm for solving optimization problems with orthogonality constraints. The authors provide convergence guarantees for the proposed algorithm and conduct numerical experiments. Theoretical and numerical comparisons with existing literature are also presented.

### Strengths
1. The proposed randomized submanifold method includes several coordinate descent methods as specific examples and allows flexibility in setting the size of the submanifold.
2. Convergence is established in both expectation and high-probability settings, with clear derivations provided.

### Weaknesses
1. The algorithm does not achieve exact convergence, potentially due to the stochasticity in subspace selection. Is there a way to ensure exact convergence, for example, by adding restrictions on the sampling process?
2. It appears that the total computational complexity shows no improvement compared to Riemannian gradient descent and may even be higher when using orthogonal sampling. Additionally, the algorithm only converges to a neighborhood rather than a first-order stationary point.
3. The numerical comparisons are insufficient. It would be helpful to see the effects of different submanifold sizes $r$ and small $p$ values.

### Questions
1. Theorem 1. How to ensure $X_k$ remains inside $U$ under $X_{k_0} \in U$? The stochasticity induced by sampling seems problematic. Purely assuming all $X_k \in U$ may be too strong. 
2. Remark 3. The retraction is at cost of $\mathcal{O}(np^2)$, while calculating the Euclidean gradient is easy to be $\mathcal{O}(n^2p)$ flops, as seen in problems like PCA. Why does the Riemannian gradient descent  become impractical?
3. Theorem 2. Is it possible to design a verison of submanifold method that has exact convergence rather than high probability.
4. Figure 2. Many Stiefel maniofold applications are with small $p$. Could you also add some numerical experiments on small $p$ to see the comparsions?
5. Figure 5. The improvement on the accuracy appears marginal. The early-stage superior performance might also be achieved by using a larger step size.

### Soundness
2

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
5

### Summary
This paper proposes a randomized Riemannian submanifold descent method (RSDM) to address large-scale optimization with orthogonality constraints. Specifically, it mitigates the computational costs associated with the retraction in each iteration by updating on a low-dimensional random submanifold rather than the full Stiefel manifold. Two sampling strategies, orthogonal and permutation sampling, are provided. Theoretical analysis guarantees convergence, and extensive experiments demonstrate the effectiveness and efficiency of RSDM.

### Strengths
1. The proposed RSDM is novel, which updates on a low-dimensional random submanifold instead of the full Stiefel manifold. In this way, it reduces the computational costs in each iteration, contributing to large-scale optimization.
2. The paper provides a comprehensive theoretical analysis, including general nonconvex optimization problems, nonconvex functions satisfying the PL condition, and the results in stochastic settings. The discussion about the trade-off between efficiency and convergence is interesting.
3. The effectiveness and efficiency of the proposed algorithm are validated on an array of numerical experiments, and the source code is available.

### Weaknesses
1. The proposed RSDM is novel, which updates on a low-dimensional random submanifold instead of the full Stiefel manifold. In this way, it reduces the computational costs in each iteration, contributing to large-scale optimization.
2. The paper provides a comprehensive theoretical analysis, including general nonconvex optimization problems, nonconvex functions satisfying the PL condition, and the results in stochastic settings. The discussion about the trade-off between efficiency and convergence is interesting.
3. The effectiveness and efficiency of the proposed algorithm are validated on an array of numerical experiments, and the source code is available.

1. The contribution seems limited in the scenario when $p=\Omega(n)$. However, numerous applications typically involve the setting $p\ll n$. Specifically, as discussed in Remark 3, the total complexity of the standard Riemannian gradient descent is $O(np^2\epsilon^{-2})$, while the proposed method costs $O(n^3\epsilon^{-2})$, which appears as a theoretical gap.



### Questions
1. As cited in line 88 of the manuscript, the literature [1] proposed a randomized method, RSSM, which also updates on a low-dimensional random submanifold. Could you compare it with the method in this work in terms of computational cost per iteration? Additionally, is there any relationship between RSSM and RSDM?
2. In line 382 of the manuscript, it states that analysis for Theorem 3 can be easily extended to mini-batch gradient descent. Can the authors explain this point briefly?
3. In the experiments, the parameter $p$ is consistently close to $n$, for which the proposed RSDM outperforms other methods. It would be beneficial to demonstrate at what percentage of $n$ the value of $p$ needs to reach before RSDM begins to show its advantage.
4. In Section 7.4, the numerical results of the deep learning task seem confusing, where the accuracy hovers around $40\\%$ to classify CIFAR10. Additionally, only the tendency of accuracy is presented; including the training/test loss would be more illustrative.

I would like to increase my grade if the concerns are well addressed.

[1] Randomized submanifold subgradient method for optimization over Stiefel manifolds. 2024

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper deals with large-scale optimization problems with orthogonality constraints. To overcome the computational bottleneck of the retraction operator, the authors propose a novel "subspace" technique that updates variables on random submanifolds, reducing per-iteration complexity. They introduce two strategies for selecting these submanifolds and analyze the convergence of their methods for both general nonconvex functions and those with local Riemannian PL conditions. Besides, the approach is also applicable to certain quotient manifolds. Experimental results demonstrate the method's effectiveness across various problems.

### Strengths
1. This paper proposes a novel random submanifold descent method (with two sample strategies), which enables low-cost retractions and low per-iteration complexity. 
2. The authors provide a thorough convergence analysis under the non-convex setting, the local Riemannian PL setting, and the stochastic setting.
3. The proposed algorithm outperforms other existing methods in various problems.

### Weaknesses
1. In line 87, the authors mentioned the poor parallelization of existing methods. However, they did not say too much about why RSDM can be implemented in parallel. In line 93, the authors say “allowing parallel computation”. Adding more discussion and exploration in this aspect can greatly strengthen this paper. For example, elaborating more on the parallel implementation of RSDM or even showing the speedup compared to the sequential implementation in the experiment part would be helpful.
2. We know from Definition 1 that the Riemannian PL holds locally. In Line 304 of Theorem 1, it says “Suppose k0 large enough such that $X_{k0} \in U$”. I understand that this assumption is because the iterates may not always stay in the local region due to algorithmic randomness. Is it possible to get rid of such an assumption? This seems difficult to me. Similar things happen in other theorems.
3. In line 69 and Line 92, the authors say that the complexity of non-standard linear algebra reduces to O(r^3) from O(nr^2). I understand O(r^3) comes from the cost of retraction operation. However, the per-iteration cost is still O(npr) or O(nr^2) (see Section 4.1 and Section 4.2). It would be better to clarify these in the statement.
4. In line 142 and line 146, it is not suitable to use “denote … as …”. Besides, in line 155, what is the meaning of $X^*$?
5. It can be better to explicitly write down the expression grad F_k(I_n) arising in (4) using the Euclidean gradient. Although it is very simple, it can help readers understand lines 212-213.
6. In Line 222, why does the gradient computation only require O(nr^2)?
7. Could the authors add more discussions on the parallel implementation?
8. Could the authors get rid of the assumptions in Line 304? 
9. In line 484 of Section 7.3, it should be Figure 4 instead of Figure 2. In addition, if possible, could the authors also compare their RSDM with RSSM in (Cheung-Wang-Yue-So ‘24) in Line 577?
10. In Line 467-470, Can the phenomenon of switching from sublinear rate to linear rate be explained by the error bound property (or the Riemannian PL property)? See Theorem 1 and Theorem 2 in “Liu H, So A M C, Wu W. Quadratic optimization with orthogonality constraint: explicit Łojasiewicz exponent and linear convergence of retraction-based line-search and stochastic variance-reduced gradient methods[J]. Mathematical Programming, 2019, 178(1): 215-262.” The authors can add some discussion if this is related.
11. The update of RSDM is similar to the algorithm in "A Block Coordinate Descent Method for Nonsmooth Composite Optimization
under Orthogonality Constraints" (https://arxiv.org/pdf/2304.03641). For example, the formula in Line 215 is similar to (12) in the reference. Could the authors compare RSDM with the algorithm in the reference and highlight the differences more explicitly?

### Questions
1. In Line 69 and Line 92, the authors say that the complexity of non-standard linear algebra reduces to O(r^3) from O(nr^2). I understand O(r^3) comes from the cost of retraction operation. However, the per-iteration cost is still O(npr) or O(nr^2) (see Section 4.1 and Section 4.2). It would be better to clarify these in the statement.
2. In line 142 and line 146, it is not suitable to use “denote … as …”. Besides, in line 155, what is the meaning of $X^*$?
3. It can be better to explicitly write down the expression grad F_k(I_n) arising in (4) using the Euclidean gradient. Although it is very simple, it can help readers understand lines 212-213.
4. In Line 222, why does the gradient computation only require O(nr^2)?
5. Could the authors add more discussions on the parallel implementation?
6. Could the authors get rid of the assumptions in Line 304? 
7. In line 484 of Section 7.3, it should be Figure 4 instead of Figure 2. In addition, if possible, could the authors also compare their RSDM with RSSM in (Cheung-Wang-Yue-So ‘24) in Line 577?
8. In Line 467-470, Can the phenomenon of switching from sublinear rate to linear rate be explained by the error bound property (or the Riemannian PL property)? See Theorem 1 and Theorem 2 in “Liu H, So A M C, Wu W. Quadratic optimization with orthogonality constraint: explicit Łojasiewicz exponent and linear convergence of retraction-based line-search and stochastic variance-reduced gradient methods[J]. Mathematical Programming, 2019, 178(1): 215-262.” The authors can add some discussion if this is related.
9. The update of RSDM is similar to the algorithm in "A Block Coordinate Descent Method for Nonsmooth Composite Optimization
under Orthogonality Constraints" (https://arxiv.org/pdf/2304.03641). For example, the formula in Line 215 is similar to (12) in the reference. Could the authors compare RSDM with the algorithm in the reference and highlight the differences more explicitly?

### Soundness
4

### Presentation
4

### Contribution
4
