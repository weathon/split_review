# Efficiently Computing Similarities to Private Datasets

- Decision: Accept
- Scores: 8, 6, 8, 8

## Abstract
Many methods in differentially private model training rely on computing the similarity between a query point (such as public or synthetic data) and private data. We abstract out this common subroutine and study the following fundamental algorithmic problem: Given a similarity function $f$ and a large high-dimensional private dataset $X \subset \R^d$, output a differentially private (DP) data structure which approximates $\sum_{x \in X} f(x,y)$ for any query $y$. We consider the cases where $f$ is a kernel function, such as $f(x,y) = e^{-\|x-y\|_2^2/\sigma^2}$ (also known as DP kernel density estimation), or a distance function such as $f(x,y) = \|x-y\|_2$, among others. 
    
Our theoretical results improve upon prior work and give better privacy-utility trade-offs as well as faster query times for a wide range of kernels and distance functions. The unifying approach behind our results is leveraging `low-dimensional structures' present in the specific functions $f$ that we study, using tools such as provable dimensionality reduction, approximation theory, and one-dimensional decomposition of the functions. Our algorithms empirically exhibit improved query times and accuracy over prior state of the art. We also present an application to DP classification. Our experiments demonstrate that the simple methodology of classifying based on average similarity is orders of magnitude faster than prior DP-SGD based approaches for comparable accuracy.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors consider the following question: Given a private dataset X in d-dimensional space and a similarity function f(a,b) (where a and b are d-dimensional points), output a private data structure that given any y approximates the $\sum_{x\in X} f(x,y)$. In particular, the authors consider f to be distance functions such as $\ell_p$ for $p = 1, 2,\ldots,$  and also Kernel density estimates such as gaussian, exponential and Cauchy kernels. The approximation obtained is $\alpha$-relative and also has an additive factor.

In comparison to prior work, for the case where f is the $\ell_p$ norm, the relative error produced in this paper seems higher (from a relative approximation standpoint) but lower in terms of the additive error. For the KDE queries, the errors are similar to before but the parameters d and \alpha in the query time of this result are decoupled. Finally, at least some of the results in this paper seems relatively simple leading to an implementation.

### Strengths
The paper provides a simpler algorithm with a slightly different (better in some settings) trade-off for privately approximating distances and KDEs. The problem is an important one with many usecases. For this reason, I think the result is interesting

The techniques used involve decomposing the distance calculation into approximating several one-dimensional approximations (at least for the $\ell_1$). The idea is simple and leads to implementations.

### Weaknesses
The result is an improvement over existing work only under certain settings. In particular, while the additive error is improved for $\ell_p$ norms, the relative error seems worse. This trade-off may not be ideal for all applications, especially those where relative error is a primary concern. The paper does not fully explore the implications of this trade-off in different use cases. Writing is good for the first two sections, but technical insights (especially pertaining to privacy) in the main paper is somewhat limited. The explanation of how the techniques interact with privacy, specifically the reduction of smooth kernels to exponential sums, lacks sufficient detail in the main body. The paper could benefit from a more thorough discussion of the privacy analysis and its nuances.

### Questions
NA

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper provides results for computing similarity-functions for queries and datasets under the constraint of differential privacy (DP). The approach they rely on mainly is leveraging the low-dimensional structures behind specific functions, whilst utilising tools, like dimensionality reduction, approximation theory, and one-dimensional decomposition of functions. They provide both theoretical and empirical results on their findings, and show that they improve on the state-of-the-art solutions for these problems.

Their algorithm for the $\ell_1$ distance function involves reduction to a series of one-dimensional decompositions. They work with Kernel Density Estimation (KDE) queries (for kernels, such as Gaussian, Exponential, and Cauchy), they use their new dimensionality reduction results that adapt the well-known JL matrices for their use-case. For the case of smooth kernels, they use functional approximation theory.

Some of their experiments are performed on the CIFAR-10 dataset.

### Strengths
1. The clear improvement on the prior work by Huang and Roth (2014) in terms of runtime and accuracy, both theoretically and empirically, is something to note.
2. Besides improving on prior work, this paper also has results for new kinds of queries, as well, for example $\ell_p$ distance queries.
3. The paper is easy to follow.

### Weaknesses
1. There is a $\sqrt{d}$ gap in the additive error for $\ell_1$ functions, and there isn't much intuition on why that may be happening or why it may be non-trivial to remove. Specifically, the paper decomposes the $\ell_1$ distance into a sum of one-dimensional distances, which introduces a composition overhead when using pure differential privacy. While the authors achieve a $\sqrt{d}$ factor improvement over the naive $O(d)$ composition, the fundamental issue of composing one-dimensional mechanisms remains, and it's unclear if this $\sqrt{d}$ factor is inherent to the approach or if there's a way to circumvent it within the pure DP framework. It would be beneficial to have a more in-depth discussion on the limitations of this decomposition approach and whether alternative strategies could potentially lead to tighter error bounds.
2. For the $\ell_1$ distance queries, the error for $\varepsilon=1$ seems very large. It will always be the case that the error decreases with increasing $\varepsilon$, but in any case, it seems like this work may not be as useful in the high-privacy regimes. The experiments show that for $\epsilon = 1$, the error is quite substantial, raising concerns about the practical applicability of the method in scenarios where strong privacy guarantees are paramount. While the authors show improvements over prior work, the absolute error magnitude at low $\epsilon$ values is a significant limitation. It's important to understand the trade-offs between privacy and accuracy, and the current results suggest a potential barrier for using this method in high-privacy settings.

### Questions
1. Is there any specific reason, why you considered pure DP only, but not zCDP or approximate DP?
2. Might be worth citing this work https://arxiv.org/abs/2106.00001, since it is recent and is relevant to DP dimensionality reduction.

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors proposed improved theoretical algorithms to compute similarity to high-dimensional private dataset for a rich class of functions. The authors give theoretical results on different distance functions and kernel functions that are advantageous over the existing results in error or query time. Further, some empirical results on $l_1$ query, dimensionality reduction and DP classification also show the advantages of the algorithm over the state-of-art benchmarks with careful discussions.

### Strengths
1. The authors presents solid theoretical results that improve over the existing literature on the error terms and query time for commonly used distance queries functions and KDE queries.

2. The authors presented a thorough comparisons of the proposed results with the state-of-art theoretical results in the literature.

3. Although the paper is technical, the authors provided sufficient empirical results to support the theory.

### Weaknesses
The paper structure can be improved. I find it more helpful to include some important formal results and algorithms in the main paper.

### Questions
None

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper gives novel results on the problem of computing the similarity between a query point and private data, in the context of differential privacy.

### Strengths
Originality:
Work seems original.

Quality:
Writing and presentation are very good.

Clarity:
Writing is very clear.

Significance:
The problem addressed is important for differential privacy.

### Weaknesses
None.

### Questions
Page 2:
Better put the definition of differential privacy in the main body.

Page 3:
What other notions of distance would it make sense to study?

Page 4:
I do not understand the discussion before Theorem 1.4.

Page 5:
Why is it the case that Corollary 3.2 allows you to express 1/(1 + h(x, y)) in such a way?

Page 7:
Second math display:
I do not see why the last equality holds.

Page 8:
Could you please edit the caption of Figure 1 to be more detailed?

Page 9:
I do not understand the comparison in Figure 3.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
