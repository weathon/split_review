# Improved Active Learning via Dependent Leverage Score Sampling

- Decision: Accept
- Avg Score: 7.20
- Scores: 8, 6, 6, 8, 8

## Abstract
We present an active data collection method for sample efficient learning of high dimensional linear functions with spatial structure, such as high degree polynomials over low-dimensional surfaces. Our method uses leverage scores as a measure of data importance, and a non-i.i.d. pivotal sampling method to collect samples that are well-scattered across the domain. For $d$-dimensional linear function families, we prove that our approach solves the challenging agnostic learning problem with $O(d\log d)$ samples, matching leverage score based methods that use i.i.d. sampling. At the same time, our method performs far better empirically. On a set of test problems motivated by learning-based methods for solving parametric PDEs and uncertainty quantification, we reduce the number of samples required to achieve a given target accuracy by up to $50\%$ in comparison to existing methods.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors suggest a modification of the pivotal sampling algorithm which allows for better domain coverage in such an applications as approximating PDE solutions.

### Strengths
The paper is well-written with clear motivation for the main theoretical results and nice experimental illustrations. The modified pivotal sampling algorithm (Algorithm 2) is appealing and seems to be quite easy to implement.

### Weaknesses
My main concerns are stated below and are related with the technical novelty of the results of the analysis of Theorems~1.1 and 1.2. The auxiliary results for the proof of Theorem 1.1, specifically Lemma B.1, seem to be a direct consequence of existing matrix Bernstein inequalities, such as those found in [Vershynin, Section 5.4]. The provided justification for its necessity is not entirely clear, given the apparent applicability of standard matrix concentration results. Similarly, the approximate matrix multiplication results in the appendix appear to be well-established, as seen in [Tropp, 2012, Section 6.4]. It is not evident why these known results cannot be directly applied, and the authors should clarify the specific technical challenges that necessitate their alternative approach. Furthermore, while the experimental section demonstrates the approach, it could be strengthened by including higher-dimensional problems to better assess the scalability and robustness of the proposed method.

### Questions
I would like the authors to clarify the novelty of the suggested theoretical analysis. In particular, I do not understand why the auxiliary results for the proof of Theorem 1.1 do not follows directly from the literature? In particular, why the result of Lemma B.1 does not follow from the existing matrix Bernstein inequalities, see e.g. [Vershynin, Section 5.4]. The results on the approximate matrix multiplication (see the same appendix) also seems to be known [Tropp, 2012, Section 6.4]. It would be great if the authors could better elaborate on the novely, and technical novelty, of Theorems~1.1 and 1.2.

References:
[Vershynin, 2018] Vershynin, Roman. High-dimensional probability: An introduction with applications in data science. Vol. 47. Cambridge university press, 2018. https://www.math.uci.edu/~rvershyn/papers/HDP-book/HDP-book.pdf
[Tropp, 2015] Tropp, Joel A. "An introduction to matrix concentration inequalities." Foundations and Trends® in Machine Learning 8.1-2 (2015): 1-230. https://arxiv.org/pdf/1501.01571.pdf

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this work, the authors improve on active learning methods for linear and polynomial regressions under an agnostic noise setting. Here, the goal is to learn $x \in \mathbb{R}^d$ such that $Ax ≈ b$ while observing only a few entries of $b$. Prior works on active linear regression, studied for decades, assume $b$ to be equal to $Ax^*$ plus i.i.d. random noise. In this case, the problem can be addressed using tools from optimal experimental design. In the agnostic case, where such a noise model is not specified, near-optimal sample complexity results and use statistical leverage score-based sampling. In this work, the authors argue that "any" sampling strategy that has marginals proportional to leverage scores, satisfying a weak independence condition, will only need samples equal to those required using independent leverage score-based sampling up to constants (theoretical), given by $O(d\log d)$. They then propose a pivotal sampling-based approach (satisfying the criteria listed) which empirically performs much better, and also show theoretical improvements for the special case of polynomial regression, and uses $O(d)$ samples.

### Strengths
— The paper is extremely well-written, providing a thorough discussion on the advantages and limitations of the authors’ work alongside prior research.

— The result on "any" sampling strategy is very interesting, even if it doesn’t improve upon previous theoretical guarantees for the given scenario.

— Most sampling-based results obscure significant constants, as noted by the authors regarding the theoretically optimal result due to [Chen and Price 2019], which, in practice, performs poorly. Therefore, the authors' provision of approaches with improved empirical performance, even with similar theoretical guarantees is an important contribution.

### Weaknesses
— The empirical evaluation lacks clarity regarding the improvements. The authors should explicitly state the claimed 50% reduction in samples in the technical sections.

— The theoretical improvements are solely for polynomial regression, which is essentially linear regression with an infinite number of rows. It would be interesting to explore whether the pivotal sampling method has other implications for different norms. For instance, can this "tournament" style technique be applied to all norms and their respective optimal sampling strategies?

— The selection of the tree in Algorithm 1 significantly impacts the performance of the sampling method. If the running time is a major concern in large-scale systems or datasets, it isn’t clear if a PCA-based approach is always feasible.

### Questions
Pg 3. Theoretic -> theoretical 

Pg 6. Bernouilli -> Bernoulli

As constants play a big role in the motivation of this work and their empirical improvements, a suggestion would be to note them down explicitly in the current work if possible.

The $\ell_\infty$ based independence condition. Can the main theorem result be stated in terms of the parameter $D_{inf}$? It would also be interesting to note the value in the case of independent uniform sampling. It suggests that the $D_{inf}$ is the same for any independent sampling approach.

In the experiments, it would be interesting to compare with [Chen and Price 2019] and also add a random permutation of rows as the leaves of the tree, in addition to PCA-based ones.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigates the active regression problem in the adversarial setting. The authors introduce a novel sampling methodology that promotes spatial coverage, combining it with leverage score sampling. The paper offers two theoretical contributions: the first establishes a sample complexity bound under the one-sided $\ell_{\infty}$ independence condition, while the second presents a bound applicable to a specific case of polynomial regression. Empirical results further validate the effectiveness of the proposed approach.

### Strengths
a. The proposed pivotal sampling method using a binary tree tournament is interesting and innovative.

b. The theoretical results are solid. The sample complexity bound for polynomial regression showcases an improvement of a logarithmic factor over the general case. The techniques employed in the analysis have potential implications beyond this specific research.

c. The authors provide empirical results to validate the effectiveness of the proposed pivotal sampling. These results clearly indicate that pivotal sampling significantly outperforms Bernoulli leverage sampling.

d. The presentation is clear and easy to follow.

### Weaknesses
 a. My primary concern pertains to the computational complexity of the proposed method. The paper lacks both theoretical analysis and empirical results in this regard, leaving an important aspect unaddressed.

b. The experimental setup in the paper includes only a single baseline, and it would be beneficial to include additional baseline methods, such as maximum leverage score sampling.

### Questions
a. Is there any theoretical analysis or empirical results regarding the computational complexity of pivotal sampling, particularly concerning the construction of the binary tree?

b. How does the proposed pivotal sampling method compare with maximum leverage sampling strategy?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a way to perform leverage score sampling that promotes spatial coverage for the problem of active linear regression. Motivated by the empirical successes of deterministic grid-based approaches to PDEs, the presented approach retains the strong theoretical guarantees of leverage score sampling with the spatially-well distributed samples of grid-based approaches. The key insight is to use a pivotal sampling algorithm where a binary tree that matches the geometry of the data is constructed deterministically and the samples are percolated up via head-to-head comparisons (probability weighted coin flip) at sibling nodes. This leads to the desirable behavior of spatial coverage since close neighbors in the tree are less likely to be both included. The authors conduct empirical evaluations that show the improved effectiveness of the proposed method.

### Strengths
* The problem of active linear regression is interesting and has applications to uncertainty quantification and parametric partial differential equations.
* The paper is very well-written and organized. There is a great overview of prior work as well as the contextualization of the results (e.g., the fact that the work builds on top of the recent result in Chernoff bounds under $\ell_\infty$ independence).
* The claims of the paper are adequately supported with rigorous theoretical analysis and empirical evaluations.
* The algorithm and its analysis is novel to the best of my knowledge. The presented analysis is general enough that it could be applied to any non-independent leverage score sampling method that obeys a weak one-sided  $\ell_\infty$ independence condition. This might be of independent interest to other researchers in the area. Leveraging 
* The empirical evaluations are compelling and clearly show the improved effectiveness of the dependent leverage score sampling method.

### Weaknesses
 * The presented analysis does not provide justification for the improved empirical effectiveness of the method (besides for $\ell_2$ polynomial regression). So, it is not clear theoretically why the method performs much better than independent leverage score sampling. Nevertheless, this is a limitation that the authors clearly concede and mention a few times throughout.

### Questions
The authors note that the algorithm of Chen and Price, 2019 is provably optimal, but that “in our initial experiments, it was not competitive with leverage score sampling in practice.” Why were these results not included in the main body of the paper? My understanding is that the Randomized BSS algorithm is only included as a result in Figure 8c of the appendix. It would be compelling to have comparisons to Chen and Price’s method in Fig. 4.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a novel leverage score sampling method based on spatial pivoting and therefore the samples are dependent. The main results involve a nearly optimal sample complexity of $O(d\log d+d/\epsilon)$ for active regression which matches the standard independent leverage score sampling, and a optimal bound of $O(d/\epsilon)$ for polynomial regression. The key proof ingredient for the first result is an adaptation of the $\ell_\infty$ independence result due to [KKS22] and how to generalize this property to approximate matrix product, and for the second result is similar to [KKP17]. They also perform extensive experiments for active regressions on PDEs and the experiments are convincing enough that their algorithm has good performance.

### Strengths
While the techniques are not completely novel, I do like the theoretical implications of this paper --- they essentially show that leverage score sampling with limited independence also provides theoretically matching bound compared to independent leverage score sampling. This inspires one to design leverage score sampling algorithm that can adaptively choose the samples based on particular structure of the problem. They also show a BSS-type result for polynomial regression without resorting to the BSS barrier function argument. This is very interesting because as far as I know, all sparsification results with $O(d/\epsilon)$ sample complexity are more or less variants of BSS. I believe results and techniques in this paper have further applications in other sparsification problems.

In addition, they perform many numerical experiments to show that their algorithm works well in practice. This is nice as it aligns with the idea that one can modify leverage score sampling based on problems to get better (practical) algorithms.

### Weaknesses
As noted in the strengths part, the techniques in this paper are not very novel. To get their first $d\log d+d/\epsilon$ sample complexity for active regression, they mainly utilize [KKS22]. The adaptation of the $\ell_\infty$ independence result from [KKS22] to the approximate matrix product setting, while requiring some effort, is not fundamentally new, and the core idea of using limited independence is already present in [KKS22]. The approximate matrix product result, while technically involved, follows a fairly standard approach of leveraging limited independence properties. For the second result regarding polynomial regression, it also mainly follows procedures from [KKP17], and the novelty is primarily in applying these techniques to the specific setting of spatially pivoted sampling. The core argument for the $O(d/\epsilon)$ bound relies on similar structural properties as in [KKP17], and the adaptation to the current sampling scheme, while non-trivial, does not introduce a fundamentally new proof technique. Therefore, while the results are interesting, the technical novelty is somewhat limited.

### Questions
A few comments regarding citation: the paper [KKS22] was published in SODA 2022. It's better to cite the proceeding version.

A question: it seems the binary tree-based approach to pre-partition the space based on the structure of the problem can also be extended to BSS-type sampling, e.g., see the data structures and algorithms in [SXZ22]. Do you think your argument and techniques can be generalized to BSS, to achieve an optimal sample complexity while leveraging particular structures?

[SXZ22]: Z. Song, Z. Xu and L. Zhang. Speeding up sparsification using inner product search data structures, 2022.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
