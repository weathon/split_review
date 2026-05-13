# Learning Representations for Independence Testing

- Decision: Reject
- Scores: 5, 6, 5, 6

## Abstract
Many tools exist that attempt to detect dependence between random variables, a core question across a wide range of machine learning, statistical, and scientific endeavors. Although several statistical tests guarantee eventual detection of any dependence with enough samples, standard tests may require an exorbitant amount of samples for detecting subtle dependencies between high-dimensional random variables with complex distributions. In this work, we study two related ways to learn powerful independence tests. First, we show how to construct powerful statistical tests with finite-sample validity by using variational estimators of mutual information, such as the InfoNCE or NWJ estimators. Second, we establish a close relationship between these variational mutual information-based tests
and tests based on the Hilbert-Schmidt Independence Criterion (HSIC), showing that learning a variational bound in the former case
is closely related to learning kernels, typically parameterized by deep networks, in the latter. Finally, we show how to find a representation that maximizes the asymptotic power of an HSIC test, prove that this procedure works, and demonstrate empirically the practical improvement of our tests (with HSIC tests generally outperforming the variational ones) on difficult problems of detecting structured dependence.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper discusses methods for improving independence tests between random variables, focusing on high-dimensional data where traditional tests struggle. It introduces two main approaches: using variational estimators of mutual information (MI), such as InfoNCE and NWJ, and leveraging the Hilbert-Schmidt Independence Criterion (HSIC). The authors demonstrate that variational MI-based tests can be closely related to kernel-based HSIC tests, with both methods aiming to detect dependencies more efficiently. They propose a new method that learns representations to maximize the power of HSIC tests, showing that this approach outperforms standard variational methods in detecting complex dependencies.

### Strengths
The paper is technically well presented, and the claims are well supported, theoretically and experimentally. It introduces novel approaches for learning representations that enhances the power of independence tests, particularly in high-dimensional settings, improving upon traditional methods. Additionally, the work demonstrates theoretical validity and empirical effectiveness of the proposed approaches, complemented by extensive evaluations that reinforce its contributions to the field.

### Weaknesses
 - A notable issue is the lack of clarity regarding the aims and achievements of the paper. For instance, while it claims to present two approaches for independence testing, the conclusion suggests that it only studies one approach, leading to confusion about the overall contribution and focus of the work.
- The performance of HSIC-based tests is significantly influenced by the choice of kernel. While the paper proposes methods to optimize kernel selection, identifying the appropriate kernel for specific data types or distributions remains challenging and may not generalize well across diverse datasets. Specifically, the paper does not sufficiently address the practical challenges of selecting a kernel architecture, such as the number of layers and hidden units in an MLP, and how these choices affect the test's power. The paper should provide more guidance on how to choose the kernel architecture, or at least acknowledge this as a limitation.

- Although the proposed methods enhance sample efficiency compared to traditional tests, they still necessitate a considerable number of samples to effectively detect subtle dependencies in very high-dimensional data, which could limit their practicality in scenarios with restricted data availability. The paper does not provide a clear analysis of how the required sample size scales with the dimensionality of the data and the complexity of the underlying dependencies, making it difficult to assess the practical applicability of the proposed methods in different scenarios.

- Additionally, the paper does not provide theoretical rates for the convergence of test statistics and lacks a discussion on the asymptotic validity of power in its main content. The asymptotic properties of the proposed test statistics are not thoroughly explored, and the paper does not provide any theoretical guarantees on the convergence rate of the test statistics to their asymptotic distributions. This makes it difficult to assess the statistical consistency of the proposed tests.

- Furthermore, regarding Algorithm 1, the choice of $ n_{\text{perm}}$ is required; what are the best empirical strategies for selecting this parameter, and how does the choice impact the convergence rate?

### Questions
Please see the weakness section.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a method to learn representations that facilitates the detection of dependence. The authors instantiate their idea using variational estimators of mutual information and the Hilbert-Schmidt Independence Criterion. Finally, they provide theoretical and empirical evidence to demonstrate the effectiveness of their approach.

### Strengths
This paper is very well written and I was able to read it smoothly. The idea of minimizing the asymptotic power instead of the dependence metric itself is interesting. It is demonstrated in the experiments that their approach improves HSIC's power in high-dimensional problems.

### Weaknesses
A few concerns I have for this paper:

1. It seems to me that the authors didn't highlight their core contribution enough. The InfoNCE approach already exists in the literature and making an independence test out of it based on permutation is not very interesting; applying this trick to HSIC either. The interesting part to me is they propose to minimize the SNR -- a quantity that characterizes the statistical power -- instead of the test statistics themselves. However, this contribution is not supported in the experiments (or is not conveyed clearly). I would like to see a comparison between the InfoNCE (HSIC as well) that minimizes the lower bound (test statistic) versus the one that minimizes the SNR. If the latter shows significant improvement upon the former, I would then say the contribution is solid.

2. The authors didn't mention a closely related topic -- independence tests based on optimal transport (e.g., [1], [2], and references therein). In this line of work, the distance between the joint and the production of marginals is measured by the optimal transport distances.


### Questions
Questions:
1. Although using permutation tests is easy, it may be less effective and computationally costly. Is it possible to derive a limiting distribution for your test statistics? Also, the computational complexity of Phase Two in Algorithm 1 needs to be discussed.

Small comments:
1. Line 218. If $X \perp Y$ -> if $X \not\perp Y$.
2. Line 223. When HSIC = 0 the statistic is not mean zero.
3. Line 417 and 419. There is no $\lambda$ in $J_\lambda$.

### Soundness
3

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
3

### Summary
The authors introduce two methods for independence testing, which are based on known methodologies. Two approaches are explored:
1. Tests based on variational mutual information estimators, such as InfoNCE, 
2. The HSIC that aims to maximize test power in high-dimensional data.
By recasting the corresponding test as optimization problems over neural nets, the authors demonstrate that HSIC-based tests outperform MI-based ones, particularly for complex dependencies.

### Strengths
1. I like the idea of deriving an optimizer for independence testing directly from the hypothesis test error. This makes its motivation more explicit, rather than information theoretic methods which can be thought of as 'indirect', or inducing independence as a byproduct. The authors directly demonstrate how variational mi bounds are not aiming for P_e minimization.
2. The authors present formal guarantees of the proposed method and connect it to variational bounds of mutual information, which are highly popular methods that are widespread in the community. 
3. When discussing the expression in neural estimation that is effectively required for independence testing - I liked the permutation invariance interpretation. (A note for the authors - this can be also seen from the proof of the DV formula)

### Weaknesses
1. I feel that the paper could benefit from better representation, which makes it harder for the reader to understand theciontributions in a bird's view, e.g., some crucial parts are migrated to the appendix, such as the assumptions of the main theorem of the paper, while some parts do not benefit the presentation in my opinion, such as some of the very specific and technical details in Section 5.
2. As the authors utilize 'heavy' machinery such as NN optimization, I would expect at least one experimental results on real world high dimensional data.
3. Literature review: Independence testing has been previously explored in the form of optimization of families of functions. Specifically, classical methods such as canonical correlation analysis (Hoteling 67) and its many extensions tackle the problem of independence testing. In an information theoretic setting there are the Hirschfeld-Gebelein-Renyi coefficient. More recently, max-sliced mutual information (Tsur 24), which was shown useful for independence testing and was connected to constrained variational mutual information estimation.
4. Section 2 lacks a bottom line, and currently feels like it 'stops in the middle'
5. I am not sure the citation formal is valid.

Technical comments:
1. undefined acronyms - InfoNCE, NWJ,DV
2. line 101 - 'method method'
3. line 136 - 'feature'-'features'
4. line 147 - 'by by'

### Questions
1. Can the authors comment on the tightness of the bound presented in proposition 3 (beyond the asymptotics)?
2. Does the MMD in line 255 depend on the function $f$ or function family $\cal{H}$? it is not clear from the notation, while I am pretty sure it does.
3. Could the authors discuss the assumptions of Theorem 4? I would also expect a short discussion on their 'reasonability' i.e., which distributions are captued under such assumptions?
4. Theorem discusses the implication of a unique maximizer. Do we know when such a maximizer exists?
5. Did the authos perform any ablation on the method? It would be specifically interesting to see if the networks size should indeed be linear in the input dimension.
5. The presentation would benefit from clarifying what is K in the InfoNCE notation.
6. "Gaussian kernel with unit bandwidth ... this scheme can perform extremely poorly" - the intro would benefit from a short discussion on such cases, as they form some of the motivation for this work.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper introduces new methods to detect dependencies between random variables in high-dimensional data by utilizing variational estimators of MI  and the HSIC. It aims to improve the power of independence tests by leveraging deep learning techniques to learn effective representations of the data, making the dependencies between variables more explicit. The paper also highlights a connection between MI-based tests and HSIC-based tests, showing that they are closely related. The paper introduces the concept of maximizing test power using learned representations, specifically focusing on HSIC-based tests, which are generally found to outperform MI-based ones. The experiments are abundant and support the claims.

### Strengths
The paper is well-organized and clearly presented. The authors clearly explain their methods and provide intuitive connections between the variational bounds and kernel-based methods.

Theoretically, the paper is the first to construct a valid independence test based on the variational mutual information estimator in high dimensions. The paper provides theoretical insights into the connection between HSIC and MI tests and shows how to maximize the test power for independence testing using learned representations. 

Although the experiments were all conducted on synthetic datasets, the experimental validation is abundant with various settings. The empirical results show that the performance of proposed HSIC-based tests is nontrivial especially in high dimensions.

### Weaknesses
One limitation could be the lack of evaluation on real-world datasets despite the authors already presenting three quite informative synthetic datasets. Since the presented tests only focus on testing independence, experiments of causal discovery may not be suitable. But I think testing a pair of variables is still executable. Experiments on any real-world datasets are appreciated, e.g., https://www.cmu.edu/dietrich/causality/projects/causal_learn_benchmarks/. This is just an example, the author does not need to be constrained by this and can use any real-world dataset. If there are any reasons why experiments on real-world datasets may not be feasible or practical, I would be very interested in hearing them and would welcome the explanation with an open mind.

Another limitation, which is also discussed by the authors, is the scope only focusing on the independence test, which is considerably easier compared with the conditional independence test. 

A minor piece of advice: A paragraph or several sentences to highlight the difference between the traditional independence test and the independence test in high dimensions will be appreciated and suitable for readers from different levels.

### Questions
- What is the definition of K in Line 130?
- You mention future work on extending this approach to conditional independence testing and causal discovery. Can you provide more details on what specific challenges you foresee in adapting the current method for conditional independence?

### Soundness
3

### Presentation
3

### Contribution
3
