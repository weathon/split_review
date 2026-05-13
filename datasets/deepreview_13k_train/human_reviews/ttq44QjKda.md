# Bounds on $L_p$ Errors in Density Ratio Estimation via $f$-Divergence Loss Functions

- Decision: Accept
- Scores: 6, 5, 8, 5

## Abstract
Density ratio estimation (DRE) is a fundamental machine learning technique for identifying relationships between two probability distributions. $f$-divergence loss functions, derived from variational representations of $f$-divergence, are commonly employed in DRE to achieve state-of-the-art results. This study presents a novel perspective on DRE using $f$-divergence loss functions by deriving the upper and lower bounds on $L_p$ errors. These bounds apply to any estimator within a class of Lipschitz continuous estimators, irrespective of the specific $f$-divergence loss functions utilized.
The bounds are formulated as a product of terms that include the data dimension and the expected value of the density ratio raised to the power of $p$.
Notably, the lower bound incorporates an exponential term dependent on the Kullback--Leibler divergence, indicating that the $L_p$ error significantly increases with the Kullback--Leibler divergence for $p > 1$, and this increase becomes more pronounced as $p$ increases.
Furthermore, these theoretical findings are substantiated through numerical experiments.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper establishes L_p​ error bounds of the density ratio in Density Ratio Estimation under f-divergence loss. The bounds scale with $N^{-1/d}$ and certain p-Renyi divergence, but is independent from the specific choice of fff-divergence.

### Strengths
The problem of uncertainty quantification in density ratio estimation is an important fundamental question. This work contributes a new understanding of its theoretical limits by deriving L_p​ error bounds of the density ratio. The nearly matching upper and lower bounds are a strong point, and the independence on the specific f-divergence within the loss function is also intriguing.

### Weaknesses
The bound’s dependence on $N^{-1/d}$ means that in high-dimensional spaces (where d is large), the error bound becomes practically useless. There is also a lack of downstream application or implication of the theoretical results. As a whole, this raises questions on the meaningfulness of the bounds. 

The experiments presented exhibit high variance, which limits the interpretability and robustness of the empirical validation.

### Questions
How do these bounds compare to other known bounds in DRE or related density estimation methods?

### Soundness
2

### Presentation
2

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
* The paper provides new upper and lower bounds on the Lp errors of a specific density ratio estimator. (Equations 4,5, and 6).
This estimator is constructed by minimizing an f-divergence based loss function. 

These bounds provide new insights about how the dimensionality of the data, and the KL divergence between the distributions affect the error of the estimator.

### Strengths
* As far as I know, the derived lower and upper bounds on the density ratio estimator are new.
* The paper is well-written, and easy to follow.
* The presentation is clear.

### Weaknesses
The theoretical results are interesting. 
In my opinion, what is missing from the paper is to show that these theoretical results can make a difference in some important applications. The paper contains a nice list of motivations for density ratio estimation, but the experimental section only contains some simple toy problems, and therefore the impact of the theory in real applications is not perfectly clear.

### Questions
* Equation 5 (the upper bound) contains the expectation operator on the left-hand side. This expectation is missing from the lower side (Eq 4). Is it a typo?
* In Equations 4 and 5, is it possible to create bounds for dimensions 1, and 2 as well?
* The upper and lower bounds are only derived for a specific density ratio estimator. Is it known how the convergence rate of this estimator compares to other density ratio estimators?
* How can we use these theoretical results in applications?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes an approach to density ratio estimation based on $f$-divergences. This idea originated in a paper by Nguyen, Wainwright, and Jordan, who introduced this methodology, which also forms the foundation of generative adversarial networks (GANs). The dual representation of the $f$-divergence involves optimization over a function space, where the optimizer—obtained, for instance, using a neural network—provides an estimator for the likelihood ratio when evaluated on samples. The consistency of this estimator was established in Nguyen et al., and various convergence results have been proved over recent years. The main contribution of this paper is to provide upper and lower bounds on the $L^p$-error, assuming both measures have compact support and that the log-likelihood function is bi-Lipschitz. These bounds are the first of their kind.

### Strengths
The paper is a novel and original contribution to the field of density estimation and highly relevant to recent advances in generative modeling (for example through generative adversarial networks). To my knowledge this are the first $L^p$-error bounds in this context. 
The proof of the result is very clever and relies on a representation of the $f$-divergence (called the conceptual loss function) which provides access the density ratio.  The estimates are then obtained using a "nearest neighbor" approach and by showing that the conceptual loss function and the real loss function are close to each other.  I believe that the techniques of proofs will find other applications where $f$-divergences are used (e.g. in generative modeling).  I found the presentation of the results to be excellent  both, conceptually, in the main text and, technically in the supplementary material.  Also notable is that this result is practical as the implementation of the estimator is totally straightforward using a neural network architecture.

### Weaknesses
 + There is a very unfortunate typo in the informal theorem 3.5 where in the lower bound  $(1-p)$ should be $(p-1)$.   

+ An explanation of why the result does not depend on the $f$-divergence should be provided.  I believe this is because of the Lipschitz assumption on the log-likelihood and the compactness of the support. In that way the behavior of $f$ at $0$ and at $\infty$ are irrelevant. 

+ Some head-to-head experimental comparison with other density ratio estimators would have been helpful.

### Questions
+ Can you explain why the choice of $f$ in the divergence does not matter?  Does it only change the constant? 

+ What are the implications of your results on the analysis of GANs?

+ What are the implications of your results neural estimation of $f$-divergence (see e.g. the recent https://jmlr.org/beta/papers/v23/21-1212.html)?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This article presents an analysis of error rates for density ratio estimation (DRE) in the context of $L^p$-losses applied to $f$-divergence minimization. The study derives upper and lower error bounds, noting that these rates increase with \(p\) and exhibit the curse of dimensionality. Theoretical findings are supported by numerical illustrations, which help validate the proposed rates.

### Strengths
Problem is interesting. The proofs seem to be correct. Numerical illustrations support the theoretical findings.

### Weaknesses
While the work appears mathematically sound and introduces some interesting proof techniques, I am not inclined to recommend acceptance at this stage, primarily due to the following points:

- **Lack of Comparison with Recent DRE Literature**
    The paper would benefit from a more thorough comparison with recent work in DRE estimation, particularly research involving divergence-based losses. It is, at the current stage, not possible for me to set the results into the context of the large field of DRE (see questions).
- **Context for Techniques in Sections 4.1 and 4.2**
    The conceptual reformulation presented in Section 4.1 and the nearest-neighbor-based approach in Section 4.2 would benefit from contextualization. Comparing these methods with existing approaches would clarify their originality and contribution to the field. Specifically, it is unclear how these methods relate to established techniques for handling non-convexity or high-dimensional data in DRE.
- **Practical Applicability of Assumptions**
    The main results rely heavily on the Lipschitz continuity of both the function class used and the energy function of the distributions. However, ensuring these assumptions in practical settings may be challenging, especially when dealing with complex, multimodal distributions or highly irregular function classes. This reliance makes the interpretability of the bounds somewhat limited and may constrain practical applicability. It is crucial to discuss the implications of these assumptions for real-world datasets.
- **Interpretability of Practical Implications**
    It remains unclear what practical conclusions can be drawn from the theoretical results. For example, are there implications for algorithmic design that might mitigate the curse of dimensionality or handle large sample sizes effectively? The implications of error rate growth with respect to $p$ should also be discussed. Specifically, how do these theoretical findings translate into actionable guidance for practitioners choosing between different $L^p$ losses in DRE?
- **Minor Issues and Clarifications**
    The parameter $N$ in Theorem 3.5 is undefined. It should be clarified in what sense equation (4) holds---is this with high probability?

### Questions
+ Are conceptual reformulation presented in Section 4.1 and the nearest-neighbor-based approach in Section 4.2 widely used or newly adapted in the paper?
+ How does Assumption 3.3 relate to the pseudo-self-concordance of losses as discussed in [1]?
+ Could the proof techniques introduced here be compared to those used in [1, 2]? Is the presented approach more general than these prior works?
 + Can the derived rates with respect to sample size be directly compared to those established in the literature?

[1] Zellinger, W., Kindermann, S., and Pereverzyev, S. V. "Adaptive Learning of Density Ratios in RKHS." Journal of Machine Learning Research, 24:1–28, 2023.

[2] Menon, A. and Ong, C. S. "Linking Losses for Density Ratio and Class-Probability Estimation." International Conference on Machine Learning, pp. 304–313, PMLR, 2016.

----------------------------------------------------------------------------------------------------------
**after the rebuttal, I raised my score to 5**

### Soundness
3

### Presentation
2

### Contribution
2
