# Differentially Private Bilevel Optimization

- Decision: Reject
- Scores: 6, 5, 8, 8

## Abstract
We present differentially private (DP) algorithms for bilevel optimization, a problem class that received significant attention lately in various machine learning applications.
These are the first DP algorithms for this task that are able to provide any desired privacy, while also avoiding Hessian computations which are prohibitive in large-scale settings.
Under the well-studied setting in which the upper-level is not necessarily convex and the lower-level problem is strongly-convex, our proposed gradient-based $(\epsilon,\delta)$-DP algorithm returns a point with hypergradient norm at most $\widetilde{\mathcal{O}}\left((\sqrt{d_\mathrm{up}}/\epsilon n)^{1/2}+(\sqrt{d_\mathrm{low}}/\epsilon n)^{1/3}\right)$ where $n$ is the dataset size, and $d_\mathrm{up}/d_\mathrm{low}$ are the upper/lower level dimensions.
Our analysis covers constrained and unconstrained problems alike, accounts for mini-batch gradients, and applies to both empirical and population losses.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper studies bilevel optimization under the central DP model. The authors leverage recent advancements in (non-private) first-order bilevel optimization and propose algorithms that cover both ERM and population loss.
The proposed algorithm avoids computing Hessian and uses only gradients, finding approximate solutions under certain conditions. Authors also show the mini-batch variant has similar convergence properties.

### Strengths
- The paper studies bilevel optimization under central DP, establishing first results in the area.
- It provides a mini-batch variant and addresses both ERM and population risks. 
- The paper has a well organized structure.

### Weaknesses
Since the paper is built on recent advancements in (non-private) first-order bilevel optimization, what are the technical challenges when moving from non-private to private case?
What are the technical difficulties of the analysis of the algorithm compared to the ones for non-private bilevel optimization?

I hope to see some empircal results if possible.

### Questions
Since the paper is built on recent advancements in (non-private) first-order bilevel optimization, what are the technical challenges when moving from non-private to private case?
What are the technical difficulties of the analysis of the algorithm compared to the ones for non-private bilevel optimization?

I hope to see some empircal results if possible.

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
3

### Summary
The paper presents DP algorithms for bilevel optimization problems, where upper-level objectives are smoot and the lower-level problems are smooth and strongly convex. The proposed gradient-based DP algorithms can avoid Hessian computations.

### Strengths
This framework can work with different inner algorithms with only dependency on its convergence rate and DP parameters.

### Weaknesses
While the methods outlined in the paper appear innovative, they lack a clear comparative analysis with existing methods. Fully first-order methods have already been established in non-DP settings; however, it's not apparent whether the DP version introduces significant additional complexities. 

The paper lacks empirical evaluation, which is noted as future work. This omission is unconventional and limits the ability to gauge practical effectiveness. Exploring the interaction between outer and inner algorithms through experiments could yield insightful results regarding their actual performances.

The "any desired privacy" mentioned in the contributions does not have a clear meaning because:
Adjusting a parameter to achieve a specific \epsilon,\delta value is almost always possible in all DP algorithms. The algorithm can meet any pair of \epsilon,\delta pair. However, through naive application of gaussian noise. While being correct, it does not exactly produce the desired privacy. Furthermore, meeting any privacy specification doesn't necessarily imply efficiency.

### Questions
The closest existing result is from Chen (2024), but due to the difference in the DP frameworks (central DP vs. local DP) it is hard to draw a direct comparation. Since both DP mechanisms are achieved by adding Gaussian noise, a question remains: When the scale of noise is identical, can the performance between these methods be effectively compared?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a method for differentially private bilevel optimization. In bilevel optimization, the constraint set itself is given as another optimization problem. This submission aims to produce a value with a small gradient norm (we do not assume the "upper" objective is convex).

This problem has received a lot of attention recently because of new approaches, based on penalizing/smoothing the objective, that only require first-order information. One recent paper considered bilevel optimization in the local model and assumed access to second-order information. This submission operates in the central model and only uses gradients.

The submission provides theoretical guarantees for the minimizing the norm of the empirical gradient and for the population term. It also analyzes a minibatch variant with roughly similar guarantees.

### Strengths
This submission provides a clear contribution. Private bilevel optimization is certainly worthy of study. The paper is written well.

### Weaknesses
The submission is not very deep: once the problem is stated and we've decided to following the non-private first-order penalty methods, the analysis strikes me as essentially a process of assembling the right tools and carefully applying them and tracking the error. (I don't mean to imply that this is trivial, just that the paper would appeal to a wider audience if it had new ideas for private optimization. Maybe it does, and I wasn't able to pick them up?)

We get guarantees for the gradient norm but the paper calls it "ERM." Is this a standard terminology for the non-convex problem?

### Questions
We get guarantees for the gradient norm but the paper calls it "ERM." Is this a standard terminology for the non-convex problem?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes a novel algorithm to solve differential private bilevel optimization problems, assuming that (1) the upper-level objective is smooth and Lipschitz and (2) the lower-level function is strongly convex and locally Lipschitz around optima. 
Compared to existing approaches, the proposed method is fully first-order and doesn’t need assumptions on privacy parameter $(\varepsilon, \delta)$

### Strengths
According to the author, the proposed method is the first fully first-order DP optimization method that solves the bilevel optimization problem. The proof seems correct to me and the paper is well-organized.

### Weaknesses
As the authors pointed out in the discussion section, the error rate for bilevel ERM, as well as the additive factor on the inverse batch size that appeared in minibatch bilevel ERM, could potentially be improved. The current analysis relies on strong convexity of the lower-level objective, which is a restrictive assumption. Specifically, the requirement that $g(x, y)$ is strongly convex in $y$ may limit the applicability of the proposed method to a narrower class of problems. The practical implications of this assumption should be further discussed, as many real-world bilevel problems may not satisfy this condition. Furthermore, while the method is presented as fully first-order, the practical implementation and computational cost of calculating the required gradients, especially in the context of nested optimization, should be examined in more detail.

### Questions
The proof technique assumes that the lower-level objective $g(x, y)$ is strongly convex in $y$. Can this assumption be weakened so that only the convexity of $g(x,y)$ is required?

### Soundness
3

### Presentation
4

### Contribution
3
