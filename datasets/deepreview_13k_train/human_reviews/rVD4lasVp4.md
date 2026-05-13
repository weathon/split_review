# A Lazy Hessian Evaluation Framework for Accelerating Stochastic Bilevel Optimization

- Decision: Reject
- Scores: 5, 5, 5, 5

## Abstract
Bilevel optimization has recently gained popularity because of its applicability in many machine learning applications.
Hypergradient-based algorithms have been widely used for solving bilevel optimization problems because of their strong theoretical and empirical performance in many applications. 
However, computing these hypergradients requires the evaluation of Hessians (or Hessian-vector products) of the lower-level objective, which presents a major computational bottleneck. 
To address this challenge, in this paper, we propose LazyBLO 
(**Lazy** Hessian Evaluation in **B**i**l**evel **O**ptimization), an algorithmic framework that allows infrequent Hessian computation during the execution of the algorithm for solving stochastic bilevel problems.
This allows the algorithm to execute faster compared to the state-of-the-art (SOTA) algorithms that evaluate either a single or multiple Hessians in each iteration. 
We theoretically establish the performance of vanilla SGD-based LazyBLO and show that, despite the additional errors incurred by the infrequent Hessian evaluations, LazyBLO surprisingly matches the computation complexity of the existing SGD-based bilevel algorithms.
Extensive experiments further demonstrate that LazyBLO enjoys significant gains in numerical performance compared to the SOTA approaches. 
To our knowledge, this is the first work to theoretically establish that multiple Hessian computations are not necessary within each iteration to guarantee the convergence of stochastic bilevel algorithms.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes a novel Lazy Hessian Evaluation method, which allows less Hessian vector product computation in overall iterations by using only one Hessian vector product for multiple hypergradient estimations.

### Strengths
1. This work aims to tackle a very important issue in bilevel optimization and such a method has never been tried in previous works. 
2. The numerical experiment shows a significant improvement in the proposed method.

### Weaknesses
1. Theorem 5.3 looks like the algorithm has some trouble in convergence when the gradient estimation variance is not arbitrarily small. The only way to solve this problem is to take a sample size that is large enough. Previous methods allow such error terms to diminish with iteration. This is a big disadvantage of this algorithm. As a result, Corollary 5.4 shows that the proposed method has bare improvement in partial gradient and HVP evaluations. 
2. It may be necessary to assume $l^*$ to be lower bounded for lines 372 and 428.

### Questions
1. Since the author assumes the strong convexity of the inner problem, why the challenge 2 is still challenging? 
2. The method only considers the computation of HVP. Can the author further explain how to reduce the computation of JVPs as mentioned in line 308?
3. Theorem 5.3 indicates that N=1 results in the optimal convergence rate, which is SOBA. Then how can the proposed method improve the convergent in theory? Combining the weakness mentioned above, the proposed method has marginally improved. 
4. Can we author explain what is the main reason for such a significant improvement in Table 2 since the theory can not show such an advantage?

### Soundness
2

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
This paper introduces LazyBLO, an algorithm designed to reduce the frequency of Hessian-vector product (HVP) evaluations in bilevel optimization, particularly for stochastic problems with nonconvex upper-level objectives and strongly convex lower-level objectives. By employing a lazy strategy, LazyBLO improves computational efficiency, achieving ${\cal O}(\epsilon^{-2})$ HVP complexity for stochastic cases. Theoretical convergence guarantees are provided for both nonconvex and strongly convex cases, and empirical results from data hyper-cleaning and deep hyper-representation tasks validate the effectiveness and HVP computational savings of the proposed method.

### Strengths
Proposed method is effective in saving HVP computation.

### Weaknesses
1. The convergence rate of the proposed method depends on increasing batch sizes. However, the current state-of-the-art theoretical guarantees for stochastic bilevel optimization do not require this, as demonstrated by methods such as ALSET, SOBA, FSLA, F$^2$SA, and etc.

2. Although the proposed method achieves the same convergence rate to fully single-loop bilevel algorithms with respect to $\epsilon$  for general nonconvex–strongly convex bilevel problems, the HVP computational complexity appears to be $T={\cal O}(N\epsilon^{-1})$, which is even higher than that of fully single-loop bilevel algorithms. This implies that the lazy strategy not only offers no theoretical improvement, but also is even worse than its non-lazy counterpart. Thus, the results presented here are not unexpected.

3. The motivation for reducing only HVP computations, rather than both HVP and JVP computations, is unclear. In fully single-loop bilevel methods, both HVP and JVP are computed once per iteration, unlike the Neumann series approach discussed in this paper. There is no apparent reason to prioritize reducing only HVP computations. HVP and JVP should be considered equally important, particularly in single-loop methods, which form the basis of the proposed approach. Besides, it is better to provide the computation complexity comparison of the proposed method in terms of HVP and JVP.

### Questions
It would be better to add the complexity of the proposed method in Table 1 for comparison as well.

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
2

### Summary
The paper introduces a bilevel optimization algorithm that reduces computational costs by infrequently computing Hessian.

### Strengths
The algorithm effectively addresses a major difficulty in bilevel optimization by reducing the need for frequent, costly Hessian computations.

### Weaknesses
While the problem of reducing Hessian computations is valid, the main technical novelty of LazyBLO is unclear. The approach reduces Hessian computation, which may seem like an incremental adaptation of existing methods rather than a novel algorithm. It would be helpful if you can specify them.

Could you provide more insights into how LazyBLO performs on problems where Hessian is unstable?

### Questions
1. While the problem of reducing Hessian computations is valid, the main technical novelty of LazyBLO is unclear. The approach reduces Hessian computation, which may seem like an incremental adaptation of existing methods rather than a novel algorithm. It would be helpful if you can specify them.
2. Could you provide more insights into how LazyBLO performs on problems where Hessian is unstable?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper provides a more efficient method, LazyBLO, for bilevel optimization that reduces the frequency of computing the hessian vectors. Provably, it converges faster and presents better experimental performance than other second-order, and first-order methods.

### Strengths
1. The presentation is very smooth and makes it easy to read. Notations are declared well.
2. I went through the proof details and it seems rigorous.
3. Codes are provided.

### Weaknesses
1. The paper does not seem very novel to me since the "lazy" strategies have already been tried though they may not be the lazy hessian in Bilevel optimization. I understood that no former works provided theoretical guarantees of Lazy hessian methods in BO. After I went through the proof details, it looked straightforward. However, I am open to changing my mind if I missed some important parts.
2. The order selections in the corollaries are a little confusing to me. In Corollary 5.4, I assume that N is chosen as a constant, T is at the order of $\epsilon^{-1}$, and batch sizes are all $\epsilon^{-1}$. Then LazyBLO requires $\epsilon^{-2}$ partial gradients but why $\epsilon^{-2}$ for hessian evaluations? Is it $\mathcal O(T)=\mathcal O(\epsilon^{-1})$. The selection in Corollary 5.7 is more unclear to me. With the choice of a constant level of batch sizes of $D^{f_y}$ and $D^{g_{yy}}$, N cannot be constant and I did not get your results. Correct me if I misunderstand it.
3. Normally, strong convexity will have a better convergence rate or better sample complexity. In the current version, both non-convex and strongly convex settings have the same complexity order in the partial gradients in your corollaries. Why is that?
4. The explanation in the experimental part is not clear. For example, table 2 shows the time to "converge" but there is no explanation of what the standard is (such as loss change is smaller than a threshold). Similarly, table 3 presents the number of hessian computing when reaching the same "training loss". Then how much? I suggest announcing those parts more clearly.
5. In Figure 3, can the authors provide a plot with #hessian computing as the x-axis?

### Questions
Please check the weakness.

### Soundness
2

### Presentation
3

### Contribution
2
