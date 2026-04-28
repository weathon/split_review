# An efficient algorithm for entropic optimal transport under martingale-type constraints

- Decision: Reject
- Avg Score: 4.25
- Scores: 6, 3, 3, 5

## Abstract
This work introduces novel computational methods for entropic optimal transport (OT) problems under martingale-type conditions.
The problems can map to a prevalent class of OT problems with structural constraints, encompassing the discrete martingale optimal transport (MOT) problem, as the (super-)martingale conditions are equivalent to row-wise (in-)equality constraints on the coupling matrix. Inspired by the recent empirical success of Sinkhorn-type algorithms, we propose an entropic formulation for the MOT problem and introduce Sinkhorn-type algorithms with sparse Newton iterations that utilize the (approximate) sparsity of the Hessian matrix of the dual objective. As exact martingale conditions are typically infeasible, we adopt entropic regularization to find an approximate constraint satisfied solution. We show that in practice the proposed algorithms enjoy both super-exponential convergence and robustness with controllable thresholds for total constraint violations.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper considers a linear program for the problem of optimal transport with martingale type constraints, which is in the form of standard Kantorocich relaxation with multiple additional linear constraints. Employing an entropic regularization, this work arrives at a dual (variational) framework, which is then solved by block coordinate ascend. A part of this procedure recovers the well-known Sinkhorn algorithm. However, an additional block appears due to the additional constraints, which is then maximized by the Newton's method. It is further shown that the underlying Hessian matrix is sparse, leading to less computations in the Newton steps.

### Strengths
The paper provides and discusses multiple examples that well justifies the underlying problem in various fields. In support of the choice of entropic regularization, the paper proves that the effect of this term vanishes at an exponential speed w.r.t the growth of the regularization parameter. The resulting algorithm is compared to a state-of-the-art first-orde method, which shows remarkable improvement in the speed of convergence.

### Weaknesses
I have few concerns related to the algorithmic choices and the theory that will explain tn the next part (questions).

The theoretical result is a streightforward generalization of the result in (Weed 2018), but still interesting.

The exaperiments certainly support that the algorithm is applicable to relatively large problems, but the setup of the experiments is still considered small in certain fields such as machine learning. However, this is a general limitation of the Kantorovich formulation, and is not necessarily a limitation for this paper.

### Questions
1- My main concern is that I am not sure if the choice of an entropy regularization makes sense for the additional constraints. For the standard OT problem, this choice is justified as the dual problem can be solved by exact block coordinate ascent, but if one needs to employ the Newton's method, then, why should not one use e.g. a logarithmic barrier (instead of entropic regularization), which also has the self-concordance property?

2- I appreciate the provided theoretical results, but I think that it still does not show how much the complexity grows with dimensions. A general concern about Theorem 1 is that although it is formulated as an exponential decay, it really shows the requirement that the regularization parameter grows proportionally with the inverse of the duality gap. In practice, the gap can be extremely small for large problems, leading to extremely large regularization parameters. As a result, it is interesting to see how the speed of convergence scales with the regularization parameter (is it linear, for example, as in (Altschuler 2017)?). The theoretical converghence analysis of the algorithm seems to be lacking.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes Sinkhorn-type algorithms with sparse Newton iterations to solve entropic optimal transport under martingale-type constraints. Some numerical experiments have been shown to validate the efficiency of the proposed algorithms.

### Strengths
Focusing on optimal transport with martingale conditions is interesting, given its applications, such as model-free optimal pricing, as highlighted by the authors. Additionally, it would be valuable to explore extensions of Sinkhorn-type and other OT solvers to address this novel class of optimal transport problems.

### Weaknesses
1. The paper lacks clarity in its structure. It is strongly recommended that the authors clearly state the main message at the beginning of each section and subsection. This would improve transitions and prevent readers from feeling confused.

2. Although the topic is interesting, the absence of a theoretical convergence analysis for the proposed algorithm raises concerns about its suitability for publication in high-tier machine learning conferences.

3. While the authors claim that the proposed algorithm performs well in practice, they have only benchmarked it against APDAGD. Given the availability of other computational methods for solving MOT, such as those proposed by Guo (2019), a more comprehensive comparison with existing literature in the numerical experiments is needed to robustly demonstrate the algorithm’s efficiency.

### Questions
1. How do the authors determine the switching criteria for transitioning to Newton's method, and what justifications support their choice?

2. To ensure a fair comparison, could the authors include the runtime of the warm initialization in the numerical experiments?

3. Could the authors clarify the technical challenges involved in extending the Sinkhorn algorithm

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
In this article, the author(s) consider the martingale optimal transport (MOT) problem, and develop a Sinkhorn-type algorithm for solving a relaxed version of MOT. A sparse Newton method is also used to accelerate the Sinkhorn-type algorithm for better convergence speed.

### Strengths
The article is well organized, and the overall motivation and story is clear. The MOT problem considered is an extension to the well-known OT problem, and developing efficient algorithm for solving MOT is helpful.

### Weaknesses
1. One of my major concerns for this article is the necessity of using a Sinkhorn-type algorithm for solving the entropic MOT problem. The Sinkhorn algorithm is efficient partly because it has closed-form formulas for the two alternating minimization steps. However, in the entropic MOT problem, the author(s) show that the $g$ variables need to be updated using Newton's method. If this is the case, what is the benefit of using the alternating minimization method? We can simply use limited-memory quasi-Newton methods, e.g., L-BFGS, to solve problem (7): L-BFGS is well tested and practically useful for smooth unconstrained problems, the per-iteration cost is also $O(n^2)$, and it has the benefit of avoiding an inner loop for sub-problems.

2. In the abstract, the author(s) state that "As exact martingale conditions are typically infeasible, we adopt entropic regularization to find an approximate constraint satisfied solution". However, I do not think the logic here is correct. The entropic regularization is not related to the feasibility of the solution, but is used to smooth linear programming (LP) problems for faster computation. The infeasibility issue is addressed by the relaxation of constraints given in equation (4).

3. It is good to have Theorem 1 for the approximation error, but is it a direct application of Corollary 9 of [1]? Because [1] provides analysis for general LP problems, and once you have transformed the problem into a standard form, the results should automatically hold.

4. The sparse Newton algorithm is a good addition to the Sinkhorn-type algorithm, but I feel it largely overlaps with the previous work [2]. Is it simply an application of [2] to entropic MOT?

5. For the sparse Newton method, the author(s) mention the super-exponential convergence rate, but I do not find any theoretical guarantee. So is it only from empirical observation? Also, I doubt whether the sparsified $H$ is guaranteed to be invertible. If not, how do you address it? The claim that the sparsified Hessian is the Hessian matrix of a concave function plus a non-positive diagonal matrix is also not clear. The Hessian matrix is derived from the dual function, and the dual function for MOT is much more complicated than the standard entropic regularized OT problem. The truncation method used is very similar to that in [2], and it is not clear how the authors can guarantee that the truncated Hessian still maintains the properties of a Hessian matrix of a concave function.

### Questions
See the "Weaknesses" section.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work introduces novel computational methods for entropic optimal transport (OT) problems under martingale-type conditions. The OT problems under martingale-type conditions are discussed up to the middle of page 5. Entropic formulation starts in (6) on page 5. Theorem 1 gives an inequality that justifies the entropic regularization formulation. Then optimizing the dual problem is proposed in Section 4, which is consistent with existing approaches. Sinkhorn-type algorithm is proposed. Given the structure of the objective function in dual, the Sinkhorn-type algorithm is reasonable. The sparsity of Hessian is noticed. So, the resulting algorithm is fast.

### Strengths
The literature of numerically solving OT problem is well presented.

### Weaknesses
Entropic regularization leads to a dual with similar properties to other OT problems. The resulting algorithm is a standard algorithm in the OT literature, the Sinkhorn-type algorithm. It seems that this paper isn't very novel. It's too similar to the existing numerical considerations for OT problems. The martingale-type conditions did not require new mathematical analysis to come up with an algorithm. The core issue is that while the martingale constraint introduces a specific structure to the problem, the entropic regularization effectively smooths away these specificities, leading to a dual problem that resembles standard entropic OT. The authors do not adequately demonstrate how the martingale structure is explicitly exploited in the algorithm design, beyond the general framework of Sinkhorn iterations. This raises concerns about the true impact of the martingale constraint on the algorithmic solution.

An observation is that in the dual problem (7), authors should explain how these variables connect with the variables in the primal problem (6). This may help the presentation of the paper.

The title of the paper is "An Efficient Algorithm for...". However, the paper spends multiple pages on martingale-type conditions and related problems. The numerical consideration is mainly summarized from the middle of page 5 to the middle of page 6. It sounds like the main work is to figure out the dual objective function and realize it is a convex function. The algorithmic analysis is thin, and this seems to be an inconsistency by this reviewer. The paper does not provide a rigorous analysis of the convergence rate or computational complexity of the proposed Sinkhorn-type algorithm, especially in the context of the specific martingale constraints. The lack of such analysis makes it difficult to assess the true efficiency gains compared to existing methods, and the claim of "efficient" is not fully supported by the presented results.

### Questions
No.

### Soundness
3

### Presentation
2

### Contribution
2
