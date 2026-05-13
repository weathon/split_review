# Improved Approximation Algorithms for $k$-Submodular Maximization via Multilinear Extension

- Decision: Accept
- Scores: 8, 8, 8, 6

## Abstract
We investigate a generalized form of submodular maximization, referred to as $k$-submodular maximization, with applications across the domains of social networks and machine learning. In this work, we propose the multilinear extension of $k$-submodular functions and unified Frank-Wolfe-type frameworks based on that. This continuous framework accommodates 1) monotone or non-monotone functions, and 2) various constraint types including matroid constraints, knapsack constraints, and their combinations. Notably, we attain an asymptotically optimal $1/2$-approximation for monotone $k$-submodular maximization problems with knapsack constraints, surpassing previous $1/3$-approximation results, and a factor-$1/3$ approximation for non-monotone $k$-submodular maximization problems with knapsack constraints and matroid constraints which outperforms previous $0.245$-approximation results. The foundation for our analysis stems from new insights into specific linear and monotone properties pertaining to the multilinear extension.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper studies monotone and non-monotone k-submodular maximization subject to various constraint systems. Prior work on this topic has studied combinatorial algorithms only -- this paper introduces a multilinear extension for k-submodular functions. Despite the power of the continuous approach for 1-submodular functions, it hasn't been applied to the k-submodular case. Via this method, the authors obtain improved approximation ratios in several constraint regimes, most notably O(1) knapsacks, where they achieve an asymptotically tight ratio.

### Strengths
- In some sense, developing continuous algorithms for the k-submodular case seems like a natural generalization of the 1-submodular methods. However, there were a number of challenges the authors had to adress, which is likely why prior work had avoided this direction. Everything looks easy in hindsight.
- Specifically, the way the authors addressed a certain feasibility issue (discussed on page 4) by shifting the optimization target from o^* is relatively novel. It is a little surprising to me, not that this method obtains a constant factor, but that it gets the optimal ratio in some settings (O(1) knapsacks). Other generalizations (such as rounding, approximate linearity, etc.) seem more straightforward.
- For non-monotone functions, the ratios aren't tight, but significant improvements in state-of-the-art are obtained.

### Weaknesses
 - Notation departs substantially from most of the other k-submodular papers I've seen. It took a bit of thought to see that everything is equivalent. Likely this could have been introduced in a more intuitive way that would make the paper more accessible.
- The main text is really an extended abstract, with no proofs. And instead, arguments why the methods are interesting. In general, I would like to see at least some part of the technical arguments condensed in the main text -- but this is more a critique of the publication / reviewing model. Often, mistakes are found later (obviously didn't have time to check the 30-page appendix in full detail).
- Algorithms are of theoretical interest only, of order n^{poly(1/\epsi}. It is difficult to imagine a scenario where one would want to try to implement these algorithms. Thus, their ability to tackle big data k-submodular instances of problems relevant to the ML community is limited to non-existent.

### Questions
It seems like non-monotone k-submodular optimization just uses monotone methods with a partial monotonicity property implied by k-submodular. But these results don't appear to be tight, and the problem seems to be much less well understood. Can the authors shed any light on this?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper addresses the k-submodular maximization problem under matroid and knapsack constraints. k-submodular maximization is a generalization of submodular maximization where each element of an n-dimensional vector can take values from {0, ..., k}. The objective is to maximize a submodular function defined on these vectors, subject to given constraints.

The authors apply the multilinear extension technique—previously used in submodular maximization but novel to k-submodular maximization—achieving an improved approximation factor for this problem, particularly under the d-knapsack constraint. They have improvements for other constraints too, but most improvements are minor except for this specific constraint.

### Strengths
The main strength lies in applying the multilinear extension to k-submodular maximization, which could inspire similar approaches in related problems. Additionally, the improvement in the approximation factor under the d-knapsack constraint is noteworthy.

### Weaknesses
Although the algorithm provides a good approximation factor, its practical applicability is limited due to potentially high running times, and no experimental results are provided to assess real-world performance. Specifically, the paper lacks a detailed analysis of the computational complexity of the proposed algorithms, making it difficult to assess their scalability for large-scale problems. The absence of empirical validation leaves open the question of whether the theoretical approximation guarantees translate into practical performance gains. Additionally, while the first paragraph of introduction mentions applications, it’s unclear how relevant this problem is for the ML community, as it’s not as widely studied as submodular maximization, which may hold more appeal for ML research.

- On page 5, you mention that Niu et al. achieved a 1/3-approximation ratio for the non-monotone case under a single matroid constraint, but a worse result appears on page 2, Table 1.
- On page 2, the notation for min_0 and max_0 is inconsistent—sometimes with 0 as a subscript, other times appearing below them. Please standardize.

### Questions
Could you compare your results with those for submodular maximization to clarify the gap between this work and existing results for multilinear extension in submodular maximization?

### Soundness
3

### Presentation
4

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
This paper considers the problem of maximization of $k$-submodular functions, where elements in the ground set can be selected into one of $k$ sets. $k$-submodular functions are a generalization of ordinary submodular set functions, which correspond to the special case $k=1$. For the maximization of ordinary submodular set functions, the continuous multilinear extension has been used in order to yield algorithms with better approximation guarantees compared to combinatorial approaches such as greedy algorithms. In contrast, only combinatorial approaches have previously been proposed for $k$-submodular function maximization. Inspired by the effectiveness of continuous approaches in the ordinary submodular function case, this paper extends the definition of multilinear extension to $k$-submodular functions, and proposes algorithms using this multilinear extension to achieve better approximation guarantees that those existing for a variety of constraints (see Table 1). Their algorithms use Frank-Wolfe types of methods, which is different than continuous algorithms used for ordinary submodular functions.

### Strengths
- $k$-submodular functions have been a topic of recent interest, and this paper makes an important contribution by introducing an extended multilinear extension and proposing algorithms which have better approximation guarantees using the multilinear extension.
- They developed algorithms with theoretical performance guarantees stronger than those existing in the literature. Further, at least some of their guarantees matched the best known lower bound of Iwata et al. (2016). 
- They used Frank-Wolfe type of methods instead of simply extending the most standard algorithms using the multilinear extension for standard submodular functions such as that of Calinescu et al. [2011] (see reference below). They further explain the technical challenges that arise when simply trying to extend those standard approaches. They also had to use an alternative method of rounding. So their theoretical results do not seem trivial to me.
- Paper is very well-written and clear.

Calinescu, Gruia, et al. "Maximizing a monotone submodular function subject to a matroid constraint." SIAM Journal on Computing 40.6 (2011): 1740-1766.

### Weaknesses
 - There is no experimental evaluation of the algorithms, and in fact the algorithms might not be very practical to implement. Multilinear extension algorithms are often much slower and less practical compared to combinatorial ones for ordinary submodular functions, so one would probably expect that to also be the case in this setting. The paper does not provide any discussion on the computational complexity of the proposed algorithms, which is a significant concern given the use of Frank-Wolfe type methods that often require multiple iterations and gradient computations, potentially making them unsuitable for large-scale problems.
- This paper extends and combines ideas from many papers in the literature. For example, the ordinary submodular function multilinear extension is extended to the $k$-submodular case, and in addition Frank-Wolfe style algorithms have been used for ordinary submodular functions. One con then might be that there is not a huge amount of novelty, but I think it is still plenty sufficient for publication.

### Questions
* Is the definition of $k$-submodular presented in the paper the typical definition? And if it is not, is it clearly equivalent? I recall seeing different definitions of $k$-submodular in related work.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the problem of maximizing $k$-submodular functions under various constraints. By generalizing the multi-linear extension commonly used for standard submodular functions to apply to $k$-submodular functions, the authors introduce unified Frank-Wolfe-type frameworks to tackle these problems in a continuous domain. The proposed algorithm attains an approximation ratio of $1/2$ for monotone $k$-submodular optimization and $1/3$ for nonmonotone $k$-submodular optimization.

### Strengths
1. The problem of k-submodular maximization is important in many fields of machine learning and aligns well with the conference’s broader focus.
2. The paper provides solid and clear proof analysis and proposes a unified algorithm that achieves better approximation ratios compared with the previous method.
3. The proof sketch of Lemma 3.3 is presented clearly and highlights the technical novelty of the proof.

### Weaknesses
1. As has been highlighted in [1], the $k$-submodular functions can be reduced to general submodular functions under partition matroid.  Given this reduction, the idea of defining the multi-linear extension for $k$-submodular functions is less novel. Specifically, the reduction involves constructing a submodular function over a domain of size $nk$ where each element corresponds to a choice of one of the $k$ options for each of the $n$ original elements. The multi-linear extension, while technically different, seems like a straightforward adaptation of existing techniques for submodular functions, given this reduction.
2. Since this is a theoretical work with no experimental results, the primary contributions should ideally lie in offering new technical skills or insights to the submodular optimization community. However, most of the proof analysis appears standard. The core of the analysis relies on a Frank-Wolfe type approach, which is well-established in the field. While the authors adapt this approach to the $k$-submodular setting, the modifications and analysis do not introduce significant new techniques or insights beyond what is already known for standard submodular optimization.

### Questions
The paper is clearly written. My main question concerns the proof of Lemma 3.3. I understand that the best-known lower bound for the monotone case is $1/2$, but could you please give some intuition of why the algorithm can't achieve a better bound (e.g. $1-1/e$) by explaining some key aspects of the proof in Lemma 3.3? Additionally, I noticed that the query complexity of the algorithm, even for the monotone case, is somewhat inefficient. Would using a different concentration inequality, such as Hoeffding's inequality instead of the Chernoff bound, potentially improve the query complexity?

### Soundness
3

### Presentation
3

### Contribution
2
