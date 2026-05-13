# Exact Community Recovery under Side Information: Optimality of Spectral Algorithms

- Decision: Accept
- Scores: 8, 6, 3, 6

## Abstract
In this paper, we study the problem of exact community recovery in general, two-community block models considering both Bernoulli and Gaussian matrix models, capturing the Stochastic Block Model, submatrix localization, and $\mathbb{Z}_2$-synchronization as special cases. We also study the settings where \emph{side information} about community assignment labels is available, modeled as passing the true labels through a noisy channel: either the binary erasure channel (where some community labels are known while others are erased) or the binary symmetric channel (where some labels are flipped). We provide a unified analysis of the effect of side information on the information-theoretic limits of exact recovery, generalizing prior works and extending to new settings. Additionally, we design a simple but optimal spectral algorithm that incorporates side information (when present) along with the eigenvectors of the matrix observation. Using the powerful tool of entrywise eigenvector analysis [Abbe, Fan, Wang, Zhong 2020], we show that our spectral algorithm can mimic the so called \emph{genie-aided estimators}, where the $i^{\mathrm{th}}$ genie-aided estimator optimally computes the estimate of the $i^{\mathrm{th}}$ label, when all remaining labels are revealed by a genie. This perspective provides a unified understanding of the optimality of spectral algorithms for various exact recovery problems in a recent line of work.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper considers the problem of recovery of two-community block
models. It sits in the context of a broad literature on detectability
limits, exact algorithms, etc. The particular setting considered by
the authors is one of a general sort of block-model random matrix
based on a given partition/distribution model, along with a vector of
"side-information" that is aligned with the block structure in some
way. The authors study the information theoretic limit of this
detection problem via simple spectral methods, and by studying
"genie-aided estimators."

### Strengths
This is a well-written paper -- there are quite a few moving parts
involved in this work, but the explanation was clear and easy to
follow. The authors ought to be commended for clear technical
communication. I do have onemajor misgiving about this, but that 
is saved for the weaknesses section.

I am admittedly not too familiar with the literature on exact recovery
of SBMs beyond the paper of Abbe (2018), but the results here seem
quite good, and fit into the surveyed prior results nicely. I
appreciate how the recovery guarantees are accompanied by specific
algorithms, rather than proving detectability in merely an abstract
way.

### Weaknesses
My critique of this paper is not one aimed at the strength of the
results -- indeed, I found the results to be nice, and the exposition
to be quite good. However, I have the sense that the main body of the
paper was merely a rough overview of the "real paper" hidden in the
appendix. I understand that for space reasons, lots of ML papers have
to put substantial content in the supplementary material. I don't have
a deep argument for why this is the case, but I get the feeling that
this work is better-suited for a journal format. For instance, one of
the main constructed algorithms that attains exact recovery
(Algorithm 2) is only given in the supplementary material. It would be
more appropriate to structure the paper so that the algorithm is given
and explained in the body of the paper, with other variants possibly left
to the supplement.

I should note that although I am a reader of theory papers of this
sort, I have not reviewed many of them in the context of ML
conferences, so I am ultimately willing to defer to the other
reviewers on this point.

Other notes:

(I am not holding the following against you in any way -- deadlines
can be tough!)

Please check the paper for spleling mistakes -- I spotted a few such
as "Gaussain Features" and "shifing the eigenvector combination."

### Questions
My only concern with this paper has to do with the formatting issue raised in the weaknesses section. If this is a typical approach that is commonplace and accepted in ML conferences, then I am willing to cede that point.

### Soundness
4

### Presentation
2

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the problem of exact community recovery for general two-community block models with node-attributed side information. The authors consider both Gaussian and Bernoulli matrix models for the edge observations, as well as a general side information channel, including Gaussian Features and Binary Erasure Channel. Based on the recent work of Dreveton et al. (2024) on the information-theoretic limit on this problem, the authors demonstrate the algorithmic achievability using a spectral algorithm that incorporates side information with the eigenvectors of the observed edge matrix. The main technical novelty lies in establishing a rigorous connection between the spectral estimator and the genie-aided estimator by the results on the first-order approximation of the eigenvectors in Abbe et al. (2020).

### Strengths
The paper is well-structured, with clearly stated objectives and supported arguments. It provides background definitions and results on related models, which greatly aids in understanding the topic. The novel approach of connecting the eigenvectors to the genie-aided estimator is particularly intriguing, contributing to the design of an efficient spectral algorithm. Additionally, the rigorous mathematical derivations are well-organized in the appendix, offering solid theoretical support.

### Weaknesses
Due to the page limit, I feel that some important details have been deferred to the appendix. For instance, I would like to see a more rigorous discussion in the main context on the special form of the genie score vector, $z^* \approx Aw + \gamma I_n$; how $w$ can be derived from the model, any regularity conditions needed for this approximation, and whether this form extends to models beyond Gaussian and Bernoulli. I suggest moving part of the theoretical discussion into the main text and possibly relocating some of the preliminaries to the appendix.

Additionally, I am uncertain about the robustness of this algorithm, as the coefficients $c_i$ relating $w$ to eigenvectors must be computed from model parameters. However, in practice, we typically observe only the adjacency matrix and side information, without access to underlying parameters like $a_1, a_2, b$ in ${\rm SBM}_n(\rho, a_1,a_2, b)$. A discussion or clarification on this would be beneficial.

Another limitation of this paper is the lack of a numerical study. I suggest including simulation examples that compare the proposed algorithm’s performance (in terms of accuracy and computation cost) with the existing two-stage algorithms. This would strengthen the paper by demonstrating the practical advantages of this approach.

### Questions
1. On Page 6, $L(t)$ and $I^*$ are introduced to characterize the information theoretic limit. Are there any general sufficient conditions that ensure $L(t)$, and consequently $I^*$, are well-defined? 

2. In Section 5.1, degree-profiling algorithm is mentioned as having certain caveat. However, it is unclear to me what this algorithm refers to. Perhaps adding a brief summary of the key points of this algorithm would improve clarity.

3. On page 9, it is stated that an approximate linear combination coefficients $c_i$ such that $w\approx \sum_{i=1}^K c_i/\lambda_i^* u_i^*$. Is there any intuitive explanation for why $w$ is approximately in the span of $u_i^*$? Is this result purely from the computations of the specific model (Gaussian and Bernoulli), or is there a broader rationale suggesting that this holds across more robust models? 

4. Regarding the algorithm, do the parameters $c_i$ and $\gamma$ need be explicitly computed from the model parameters, or is there a possibility to estimate them using only the adjacency matrix $A$ and the side information?

5. This final question may not be directly related to the problem considered in the paper. Dreveton et al (2024) provides  the information theoretic limit of exact recovery in terms of $I^*$.  I am curious whether the regime $I^*<1$ can be further split. Specifically, could we identify a sub-regime where exact recovery is achievable even without the side information, and another sub-regime where side information is essential with some specific conditions?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper studies block models with two communities, where each community has a general form of edge distribution. Side information on nodes is also considered. The authors specifically focuses on the case of Bernoulli and Gaussian distributions. The paper then proposes a variant of spectral algorithm to recover the community structure in the model, and provides statistical bounds for exact recovery of the signal.

### Strengths
- The paper is well organized and easy to follow. The notations and definitions are mostly self contained.
- The authors provide the statistical bounds for exact recovery in the case of the Rank One Spike (ROS) model and the Stochastic Blockmodel (SBM).

### Weaknesses
My biggest concern is that some of the language in the paper seems overclaiming. For example, the authors state that the paper proposes a "unified model" and "unified proof framework". The amount of novelty and contribution is unclear to me. Can the authors specify, preferably in bullet points, their new results, algorithm, bounds, proof techniques, or experiments?

Beyond that, I have some more detailed questions:
- The paper aims to provide a unified framework of analysis for at-most-two-community block models, but the results in Theorem 1 and 2 only target two specific and arguably "simpler" classic models. Why is that? Is it possible to give a bound based on the definition of P+, P-, and Q, for instance?
- Section 3.1: Does the information-theoretic bounds in Prop 3.1 contain anything novel, or just cited as is from [Dreveton et al., 2024]? If it is the latter, I strongly believe it should be moved to the preliminary section and not put in the "Main Results".
- Theorem 1 and 2: The exact recovery condition depends on I* > 1. Is there any way to calculate this efficiently? From a reader's perspective, I'd love to see many examples of two community models and know how their parameters are related to this I*. For example, can the authors relate I* to p and q in the SBM?
- The proofs like the concentration inequalities and the spectral analysis in the paper seem standard. In fact the union bound strategy feels similar to the ones in E. Abbe's and Dreveton's work. What are the technical contribution of this paper? Is there any proof technique that can be used in the future?

Minor:
- Bern() used but not defined on the first page.

### Questions
- I understand this is a theoretical work, but have the authors verified their algorithm on any dataset? 
- What is the computational complexity in terms of n?
- Is it possible to generalize this work to the case of multiple communities? If not, what are the technical difficulties?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the problem of exact community recovery in two-community block models with node-attributed side information. The primary contribution is the design of an optimal spectral algorithm that achieves the information-theoretic limits in various settings. The general block model in this paper encompass  rank-one spike Gaussian model and SBM, and the side information incorporates GMM and two types of "noisy'' labels.

### Strengths
1. The paper is well-organized, and the arguments flow logically.

2. The claims are solid, and the proposed framework covers a broad range of interesting models.

3. The results provide theoretical insights into community detection with side information and demonstrate the optimality of spectral methods.

### Weaknesses
1. Some related literature is missing, e.g., [1]. Specifically, the SBM model with $\rho = 1/2$ and Gaussian Features aligns with Section 4 in [1] and should be cited and compared. Additionally, for the SBM with GF where $\rho = 1/2$ and $a_1 = a_2 = a$, the expression for $I^*$ takes a simple form in Equation (4.4) of [1]. Providing explicit forms of $I^*$ for other models would enhance interpretability of the results. The lack of comparison to existing work, especially regarding the specific parameter settings, makes it difficult to assess the novelty and contribution of the proposed approach.

2. For SBM with BEC/BSC, the algorithms assume prior knowledge of parameters $(\rho,\varepsilon, \alpha)$. The paper should mention this clearly and discuss why it's reasonable to assume this prior knowledge, or suggest how these parameters could be estimated. From a theory standpoint, achieving optimality might require paying a cost for adapting to these parameters, especially in regimes $\varepsilon = n^{-\beta}$ and $\alpha = n^{-\beta}$ for $\beta>0$. The paper does not address the practical challenges of estimating these parameters, which could significantly impact the performance of the proposed algorithms.

3. The two-community assumption limits the algorithm’s practical use. While I understand that the optimality of the spectral algorithm depends on this assumption, the statement in Appendix A, "The entire framework of genie-aided estimation naturally generalizes to the multi-community case," is confusing. Can the authors elaborate on how the spectral algorithm could be modified, for example, to handle $K=3$ communities? The current presentation lacks clarity on how the theoretical framework extends to more realistic multi-community scenarios.

4. There are no experiments. It would be helpful to include numerical experiments demonstrating the algorithm’s performance on the specific models considered. The absence of empirical validation makes it difficult to assess the practical relevance and performance of the theoretical results.

### Questions
See weaknesses above. Also, the paper could benefit from a careful proofreading. For example:

1. Gaussain -> Gaussian on page 3.
2. In Algorithm 7,  $\alpha_n$ is not defined. Should it be $\alpha$?
3. In Algorithm 6, the input section ends with two periods.

### Soundness
3

### Presentation
3

### Contribution
3
