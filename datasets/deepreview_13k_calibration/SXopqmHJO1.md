# Characterizing linear convergence in optimization: Polyak-Łojasiewicz inequality and weak-quasi-strong-convexity

- Decision: Reject
- Avg Score: 5.00
- Scores: 8, 3, 3, 6

## Abstract
We give a complete characterization of optimization problems that can be solved by gradient descent with a linear convergence rate. We show that the well-known Polyak-Łojasiewicz inequality is necessary and sufficient for linear convergence with respect to function values to the minimum, while a property that we call "weak-quasi-strong-convexity", or WQSC, is necessary and sufficient for linear convergence with respect to distances of the iterates to an optimum.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
In this paper authors study the linear convergence conditions for gradient descent algorithm. They prove that well-known PL-condition is not just sufficient, but also necessary for gradient descent to have linear convergence in terms of functional residual. Additionally, authors introduce a new class of problems, that they call weak-quasi-strongly-convex. Authors claim, that on this class of problems gradient descent has linear convergence rate in terms of distance to the solution necessary and sufficiently.

### Strengths
The authors introduce two novel theoretical results. Firstly, they show that PL-condition is not just sufficient, but also necessary for linear convergence of gradient descent on smooth function. Secondly, the authors introduce the definition of weak-quasi-strongly-convex (WQSC) function. Moreover, the authors prove that the WQSC condition is necessary and sufficient for gradient descent to converge linearly in terms of distance to the solution. The WQSC condition is less strict than strong convexity, which broadens the class of problems, where we can obtain linear convergence with respect to distance to the solution. 
Overall, the result seems significant for the community while being very simple. In theory, it allows researchers to connect theoretical results for linear convergent methods and problems that satisfy the PL condition (see Theorem 10 in Appendix). In practice, the WQSC condition, while being a relaxation of the strong convexity condition, broadens the spectrum of problems, where GD has linear convergence in terms of distance to the solution.

### Weaknesses
Lack of experiments. It would be beneficial to provide some experiments on WQSC problem, which show linear convergence of GD on this problem.

### Questions
When you mention an equation, please, change \ref to \eqref, since it is a bit confusing.

### Soundness
4

### Presentation
4

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
The paper presents the necessary and sufficient conditions for the linear convergence of the gradient descent (GD) method. Specifically, the authors prove that the Polyak-Łojasiewicz (PL) condition is a necessary and sufficient condition for the function values to converge linearly to the minimum. In contrast, the weak-quasi-strong-convexity (WQSC) condition is a necessary and sufficient condition for the sequence of iterates to converge to the minimizer.

### Strengths
The authors clarify the necessary and sufficient conditions for the linear convergence of GD, including both the convergence of function values and the convergence of the sequence of iterates.

### Weaknesses
1. This paper lacks a clear comparison with existing work. Additionally, I am uncertain whether the authors are the first to suggest that the Polyak-Lojasiewicz (PL) condition is necessary for the linear convergence of function values in gradient descent.
2. According to Definition 2, there is only one global solution. If there were two distinct global solutions, the inequality in Definition 2 would not hold. Therefore, the WQSC condition proposed by the authors is essentially equivalent to the weak-strongly convex condition in (Alimisis (2024a) ). Am I correct in this assessment? If so, it should be noted that linear convergence under the weak-strong convexity property has already been established.

Line 42: Should the stepsize $\eta$ be in the range $(0,2/L)$ or $[0,2/L]$?
Line 46: The authors should reference original or classic sources. Additionally, they cite too many papers from arXiv, raising concerns about the reliability of the results in these papers.
Lines 269 and 346: Should we consider the step length $\eta$ as a constant, or as a variable that can converge to 0? I believe these two cases should not be conflated. Therefore, I suspect there may be an issue with the relevant proof. Specifically, in the proof of Corollary 6, the step size $\eta$ is initially fixed within the range $(0, 2/L)$, but later in the proof, it seems to be treated as a variable approaching zero. This is a contradiction and invalidates the proof. The corollary appears unnecessary, as the PL condition can be directly obtained by setting $\mu \equiv 2c / (2 \eta + 3 \eta^2 L)$ for fixed $c$ and $\eta$.

### Questions
Line 42: Should the stepsize $\eta$ be in the range $(0,2/L)$ or $[0,2/L]$?
Line 46: The authors should reference original or classic sources. Additionally, they cite too many papers from arXiv, raising concerns about the reliability of the results in these papers.
Lines 269 and 346: Should we consider the step length $\eta$ as a constant, or as a variable that can converge to 0? I believe these two cases should not be conflated. Therefore, I suspect there may be an issue with the relevant proof.

### Soundness
2

### Presentation
2

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
This paper characterizes the necessary and sufficient condition for the GD to have a linear convergence for smooth (possibly non-convex) functions with respect to the function value and the distances between the iterate and the optimum (that is a projection of the iterate to the solution set). The PL and WQSC conditions are known to provide a linear convergence for GD, and this paper shows that they are also necessary conditions.

### Strengths
See Weaknesses.

### Weaknesses
Theorems 5 and 7 are the main contributions of this paper, but they appear to be either equivalent or nearly identical to the closest results in Abbaszadehpeivasti et al. (2023) and Alimisis (2024a) mentioned by the authors.

- Theorem 5: The authors mention that Abbaszadehpeivasti et al. (2023) assumes extra assumption (see line 177), but I found that this is just a corollary of the Lipschitz gradient assumption. Theorem 5 in Abbaszadehpeivasti et al. (2023) therefore essentially assumes the same condition as Theorem 5 in this paper, so I should say that there is nothing new in Theorem 5. Specifically, the lower bounded curvature condition, which the authors claim is novel, is directly implied by the Lipschitz continuity of the gradient. If the gradient is Lipschitz continuous with constant L, then for any two points x and y, we have ||∇f(x) - ∇f(y)|| ≤ L||x - y||. This inequality, when combined with the smoothness assumption, inherently imposes a lower bound on the curvature, making the additional assumption in Theorem 5 redundant. The authors need to clarify why this is not the case, and provide a concrete example where Lipschitz gradient continuity does not imply the lower bounded curvature condition they impose.

- Theorem 7: The only difference between Theorem 7 of this paper and Theorem 5 in Alimisis (2024a) is the assumption on solution set; the former assumes that the solution set is convex, while the latter assumes that the solution set is a singleton set. Although I agree with the authors that their assumption is indeed weaker, I do not see this as a significant advancement, especially given that lines 346-347 were only required to address a non-singleton convex solution set. The extension to a convex set, while mathematically more general, does not introduce a fundamentally new insight or practical benefit in the context of the convergence analysis. The core argument and proof techniques remain largely the same, and the added complexity for the convex set case seems to be minimal.

Apart from the above, I do not find this paper's contributions sufficient for publication in ICLR. I recommend that the authors address the questions raised in the Conclusion to better motivate this work for the machine learning community.

### Questions
See Weaknesses.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper studies the linear convergence of gradient descent when applied to minimizing a smooth but possibly nonconvex function. The main contribution is two theoretical results characterizing the convergence rate of gradient descent under the PL inequality or Weak-Quasi-Strong-Convexity (WQSC) inequality.

The first result shows that the PL inequality is both necessary and sufficient for linear convergence of gradient descent, with convergence here meaning in terms of the function values f(x_k) - f*. Of course the sufficiency of PL inequality for this result is well-known but the reverse implication, that linear convergence implies the PL inequality, seems novel.

The second result shows something similar for functions satisfying the (WQSC) property and linear convergence with respect to the distance of the iterates to the set of solutions.

In this way, the authors seem to have solved the search for a "weak PL" condition that will ensure linear convergence - the PL inequality is necessary.

Some applications to neural networks are considered but no numerical investigations are done.

### Strengths
- The arguments appear to be correct and the results are stated clearly and precisely.

- The results are novel in the sense that previous results of this nature considered (slightly) narrower function classes. The characterization of linear convergence in terms of PL inequality is significant.

### Weaknesses
 - The results in this paper are, on the whole, incremental in nature. They mostly extend known results to the case where the set of optima is a convex set rather than assuming that it's a singleton. While it's no doubt an important distinction, the analysis involved is hardly changed. The core arguments for linear convergence under the Polyak-Łojasiewicz (PL) condition, and the Weak-Quasi-Strong-Convexity (WQSC) condition, follow similar lines to existing proofs, with the primary modification being the use of projections onto the convex set of minimizers. This adaptation, while technically sound, does not introduce fundamentally new analytical techniques or insights.

- The paper is purely theoretical, without any investigations into whether these results hold or give insight in practical scenarios. Although some effort is made in the appendix to discuss neural networks that may satisfy the hypotheses of the results here, they are under assumptions like Lipschitz-continuity of the gradient which is actually not typically satisfied by neural networks. The discussion of neural networks is also quite limited, lacking any concrete examples or empirical validation. The theoretical results would be more compelling if they were supported by numerical experiments demonstrating their relevance in practice, even on simple test cases.

- The related work is underdeveloped, with no mention of the Kurdyka-Łojasiewicz inequality or the associated results about error bounds and convergence rates. I think there is certainly a connection here that is at least worth referencing, if not developing further. The paper would benefit from a more thorough discussion of the relationship between the PL condition, the WQSC condition, and the broader landscape of convergence results, particularly those involving the Kurdyka-Łojasiewicz inequality. The current related work section does not adequately contextualize the contribution of this paper within the existing literature.

### Questions
- To your knowledge, is the work by Abbaszadehpeivasti et al. the only other result that shows necessity of PL for linear convergence? I was surprised that this has not been examined before given the large amount of literature on the PL (and KL) conditions.

- Are there notable functions covered by your relaxed assumptions that are not covered by the weak convexity assumptions in  Abbaszadehpeivasti et al. ? Their curvature lower bound can have a negative constant so it covers a pretty broad class of functions, c.f. Drusvyatskiy and Paquette 2019, if I am not mistaken.

- Similar question to the above - are there actual modern deep learning problems whose set of minimizers is convex that are not toy problems? It seems a bit exaggerated to consider the work of Alimisis 2024 in line 182 as having unrealistic assumptions for assuming that the minimizer is unique. While it is indeed unrealistic, from the point of view of realism/modern deep learning, I don't see why it's any more unrealistic than assuming that the set of minimizers is convex - as far as I know this is simply not the case in modern deep learning. Furthermore, from the point of view of theory, the difference between having a singleton minimizer or a convex set is small - you have many of the same inequalities just by taking the projection onto the set of minimizers, as is done in the current submission.

*References*

Efficiency of minimizing compositions of convex functions and smooth maps
Drusvyatskiy and Paquette 2019

### Soundness
4

### Presentation
2

### Contribution
2
