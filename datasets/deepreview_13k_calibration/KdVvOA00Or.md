# ReTaSA: A Nonparametric Functional Estimation Approach for Addressing Continuous Target Shift

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 6, 8, 8

## Abstract
\subfile{sections/abstract.tex}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work addresses the challenge of distribution shifts in deploying modern machine learning models, specifically focusing on the target shift problem within a regression context. It tackles the situation where the continuous target variable y exhibits different marginal distributions between the training and testing domains, while the conditional distribution of features x given y remains constant. Notably, the regression problem's infinite-dimensional target space necessitates unique solutions. The authors propose ReTaSA, a nonparametric regularized approach to estimate the importance weight function and provide theoretical justification for it, thereby effectively addressing the continuous target shift problem. Extensive numerical studies on both synthetic and real-world datasets confirm the effectiveness of the proposed method.

### Strengths
- The work focuses on addressing the challenge of classification tasks with an infinite-dimensional target space, while previous research on target shift primarily concentrated on scenarios where $y$ is categorical. This problem holds fundamental significance across various domains.

- By precisely estimating the importance weight function, the model can effectively adapt to variations in the target variable's distribution between the training and testing domains. A continuous importance weight function offers greater flexibility compared to discrete methods.

- The authors provide thorough theoretical justifications for consistency and error rate bounds, enhancing the paper's rigor and reliability.

- The paper's organization is well-structured, maintaining a clear and easily-followed flow from start to finish.

- Extensive references to related work offer a comprehensive overview of prior research, providing valuable context for the study and highlighting the authors' deep understanding of the field.

### Weaknesses
- Given the importance weight function, the estimation process might be sensitive to noise or outliers in the data. Specifically, how does the presence of anomalous data points in either the source or target domain affect the accuracy of the estimated importance weight function? Does the regularization technique adequately mitigate the influence of such noise, or are there scenarios where the estimates could still be significantly biased? It would be beneficial to see a more detailed analysis of the method's robustness under different noise conditions.

- Estimating a continuous importance weight function involves inherent uncertainty due to the probabilistic nature of the process. While regularization is employed, how is this uncertainty quantified and managed? For instance, how do the authors ensure that the confidence intervals around the estimated function are reliable, and how does the choice of regularization parameter affect these intervals? Further discussion on the propagation of uncertainty throughout the model would be valuable.

- Regularization can help stabilize the estimation process. However, the sample complexity required for accurate estimation of a continuous importance weight function remains a concern. What are the theoretical guarantees regarding the amount of data needed from both source and target domains to achieve a certain level of accuracy in the estimation? Are there specific conditions or assumptions under which the method is particularly data-intensive? Providing insights into the relationship between sample size, regularization strength, and estimation accuracy would strengthen the practical applicability of the method.

### Questions
See above "weaknesses" section.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the problem of label shift within a continuous label space, such as in regression with label shift. To tackle this issue, the authors propose a method based on importance weighting, which transforms the learning task into an estimation problem concerning the density ratio of the continuous variable $y$. The method has statistical consistency in estimating the weight function under certain identifiability assumptions. A practical algorithm is derived from the theoretical analysis.

### Strengths
1. This paper considers an interesting and important real-world problem with a compelling motivation.
2. This work provides the statistical consistency analysis for the proposed estimator in the continuous label space. This technical analysis has the potential insights to benefit studies in this area.

### Weaknesses
1. The experiments are currently limited to low-dimensional and small-scale datasets. This raises concerns about the generalizability of the proposed algorithm, especially given the increasing prevalence of high-dimensional data in machine learning applications, such as image and text processing. The performance of kernel density approximation, a key component of the proposed method, is known to degrade in high-dimensional spaces. Therefore, it is crucial to evaluate the algorithm's effectiveness on datasets with higher dimensionality to ascertain its practical applicability in real-world scenarios.

2. The paper does not provide a clear guideline or methodology for selecting the hyperparameter $\alpha$ for different datasets. This lack of clarity makes it challenging for practitioners to apply the proposed method effectively, as the optimal value of $\alpha$ likely varies depending on the specific characteristics of the data. A more systematic approach to determining $\alpha$ is needed.

3. While the paper acknowledges the potential instability of classical ratio estimation approaches when $p_s(y)$ approaches zero, it does not thoroughly investigate whether this issue is exacerbated in the continuous label space. The behavior of the estimator when $p_s(y)$ is small or when the support of $p_t(y)$ is not fully contained within the support of $p_s(y)$ needs further examination. A discussion of potential variance reduction techniques or alternative estimation strategies for these scenarios would strengthen the paper.

### Questions
See the comments in weakness part. As also, it is suggested to test the performance of the proposed algorithm on large-scale and high-dimensional datasets.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This manuscript studies the continuous target shift problem. To adapt to the target shift, the authors reweighed the training samples with the density ratio of the responses: $\omega(y)=p_t(y)/p_s(y)$. To estimate the weight $\omega(y)$, a two-step procedure is proposed. First, the authors employed a kernel density estimator to estimate the conditional density and then used the outcomes to solve a regularized least-squares problem to obtain the weights. Additionally, the authors discussed conditions for identifiability of the weight $\omega(y)$ and the consistency of the estimation results.

### Strengths
Overall, the manuscript is easy to follow and is technically sound. The empirical results also show improvement compared to the baselines.

### Weaknesses
I found the major issue is insufficient comparison with other prior works.
For example, Nguyen et al., (2016) studied the same problem with a slightly different estimation procedure. It would be nice to discuss and compare the method.

While the estimation procedure is straightforward, it would be nice to clarify what is the technical challenge and the novelty of this method.


Nguyen, T. D., Christoffel, M., & Sugiyama, M. (2016, February). Continuous target shift adaptation in supervised learning. In Asian Conference on Machine Learning (pp. 285-300). PMLR.

### Questions
how to select $\alpha$ in terms of the sample size?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies unsupervised domain adaptation in the context of regression ($\mathbb{R}$-valued labels), under the *label shift* assumption (i.e., that the label distribution $P_Y$ changes while the conditional distribution $P_{X|Y}$ of the features given the labels is invariant. It is first argued that this problem can be solved by training a model under a modified training loss, which is reweighted by the ratio of the label distributions in the test and training domains (the *importance weight function* $\omega$). The remainder of the paper thus focuses on estimating $\omega$. It is shown that $\omega$ satisfies a particular intergral equation, whose other components can be estimated directly from observed data using kernel density estimation. Since this integral equation is typically undercomplete, Tikhonov regularization is added to identify a unique solution. Assuming the relevant data densities are sufficiently regular and bounded, the kernel and bandwidth are carefully selected, etc., the paper provides bounds on the rate at which the estimate of $\omega$ converges to the true $\omega$. The paper then presents experiments on both synthetic and real-world datasets, demonstrating that the proposed approach outperforms a prior kernel-mean-matching approach, both in terms of estimating $\omega$ and out-of-distribution adaptation performance.

### Strengths
The motivation and justification for the proposed approach is quite convincing; almost every step seems natural, and so it seems to me like the "right" solution to this problem, under the given assumptions. The high-level writing and flow of the paper are also quite clear. The method is supported both theoretically (with some caveats; see below) and empirically.

### Weaknesses
 **Major**

1. The paper should discuss the theoretical computational complexity and practical scalability of ReTaSA, in terms of the source and target sample sizes $n$ and $m$, data dimension $p$, etc. Relatedly, under "Related Work", the paper claims "empirical evidence from... our experimental studies confirms that KMM is computationally inefficient in categorical and continuous cases," but I couldn't find evidence of this in the paper.

2. I found several parts of the paper a bit vague or missing some details that would help the reader:
    1. Page 2, last sentence, "the target shift assumption implies that... (1)": I think it would be helpful to include a few more details on the steps by which the target shift assumption implies Eq. (1). I was eventually able to figure this out (using Bayes' rule), but it interrupted my reading of the paper and took a few minutes. This could easily be avoided by adding another intermediate equality in Eq. (1), without increasing the length of the paper.
    2. Page 3, just after Eq. (3), "$T$ and $T^*$
are adjoint operators because $\langle T\phi, \psi \rangle = \langle \phi, T^* \psi \rangle$": It's not immediately obvious why this is the case. Since this observation is important for the remainder of the paper, please include a more detailed explanation or proof to the main text, or indicate where this could be found (e.g., in an appendix).
    3. Page 3, just after Eq. (4), "where... $\rho(y)$ is a unknown function to be solved": I found this quite confusing because it sounded like $\rho = \omega$. Only later is it explained that $\rho = \omega - 1$. So perhaps this latter fact can be explained a few sentences earlier.

3. First Paragraph of Section 3: $\eta = p_t/p_s$ is estimated as the ratio of two density estimates. There is a significant body of work on density ratio estimation showing that estimating the ratio by the ratio of two density estimates is often suboptimal, both in theory and in practice (see, e.g., [K17, SSK10]). Given this, perhaps the paper should consider using direct density estimation methods for this step, both to improve practical performance and to relax the assumptions (specifically, Assumption 3).

4. There are some gaps between the theoretical results Section 4 and the real-world OOD generalization problem the paper seeks to solve:
    1. Theorem 1 bounds the $L^2$ error of the estimated $\rho$. However, $\rho$ is only a means to re-weighting the risk function to adapt to the test domain (as explained on Page 3), and it's not clear to me whether estimating $\rho$ well in $L^2$ distance is necessary or sufficient to adapt to the test domain. I think the paper should provide some more concrete connection between estimation of $\rho$ in $L^2$ distance and test-domain performance of the new risk minimizer.
    2. It's unclear (to me) how some of the main assumptions in Section 4 relate to the real-world problem being solved; see Major Questions 3. and 4. below.

**Minor**

1. Page 1, Paragraph 2: It's unclear to me why the Sequential Organ Failure Assessment (SOFA) example described here satisfies the label shift assumption (in particular, why $P_{X|Y}$ is invariant between domains). I think a more convincing example here would strengthen the motivation of the paper. Perhaps it is also worth pointing up that label-shift assumptions appear naturally under anti-causal structural assumptions (see, e.g., Section 5 of [S22]).
2. The paper would benefit from some discussion of ReTaSA's limitations or further open questions. Some examples:
    1. The paper focuses on the non-parametric setting. While this makes weak assumptions on the relationship between $x$ and $y$, Theorem 1 suggests that its performance scales poorly with the dimension $p$ of the feature $x$. Perhaps it is worth briefly commenting on whether a parametric variant of ReTaSA (e.g., assuming a linear relationship between $x$ and $y$) could be useful, e.g., for high-dimensional data?
    2. Do the authors believe the rate in Theorem 1 is minimax optimal under Assumptions 1-5?
    3. How robust is ReTaSA to small violations of the label-shift assumption (e.g., small changes in $P_{X|Y}$)?
3. Beginning of Page 4: Tikhonov regularization is added to address non-identifiability (i.e., $T^* T$ might not be invertible). Given this, it might be worth adding a sentence to point out that the regularized criterion has a unique solution (i.e., $\alpha I + T^* T$ is always invertible). This isn't completely obvious, especially in the infinite-dimensional setting.
4. Remark 1: If I am understanding correctly, perhaps it is worth noting that this estimate/approximation is simply the standard Nadaraya-Watson regression estimate of $\mathbb{E}[\rho(y)|x]$.
5. Remark 8, "Therefore, the assumption fits into the regime where the dimension of the feature is smaller than the smoothness level of densities and the order ofthe generalized kernel function.": I didn't understand this sentence. It sounds like it is saying that dim$(x) = p \leq \min\{k, \ell\} = \gamma$, but I don't see how this follows from the previous sentence (which is about $\alpha$).
6. Page 7, under "Evaluation Metrics", "We conducted all experiments with 50 replications on a Mac-Book Pro equipped with a 2.9 GHz Dual-Core Intel Core I5 processor and 8GB of memory.": This seems like the wrong place to include this information. Perhaps it should be in the first paragraph of Section 5?
7. Page 7, under "Experimental Results", Typo: "performs significantly better KMM-Adaptation" should be "performs significantly better *than* KMM-Adaptation"
8. Figure 2: The lines plotted here are essentially all flat, so the plot does not illustrate much. Perhaps it would be useful to show a larger range of (smaller) sample sizes?
9. Figure 3: I think the sub-captions are incorrect (they both say "vs Sample Size" but the $x$-axis here is $\mu_t$).
10. All Figures: Please increase the font size of the text in the plots (axis labels, legends, etc.).

### Questions
**Major**

1. I found Definition 2 quite confusing, for a few reasons:
    1. I don't see where Definition 2 is used anywhere in the paper.
    2. In contrast to Section 3, where the (presummably translation invariant?) kernels are written as a univariate function, the kernel here is written as a bivariate function. Is there a reason for this?
    3. I don't understand the condition $k_h(x, y) = 0$ if $x \notin [y - 1, y] \cap \mathcal{C}$. For example, usually, bivaraite kernels are symmetric in their arguments, but this appears not to be the case here.
    4. The use of $x$ and $y$ is a bit confusing here, as it suggests the kernel is applied to the covariate $x$ and the label $y$ discussed earlier in the paper (but I don't think this is the intent, since, e.g., the condition $x \notin [y - 1, y]$ really would not make any sense in this case). Perhaps different variables (e.g., $z_1$ and $z_2$) should be used here?
2. Page 3, Eqs. (2)-(3): I don't understand why $T$ and $T^*$ map $L^2$ to $L^2$. Is this an additional implicit assumption? Or does it follow from the forms (conditional expectations) of $T$ and $T^*$? Relatedly, just after Eq. (4), "$\mathbb{E}_s\\{\eta(x)\\} = 0$ so that $\eta(x) \in L^2(x)$": I didn't understand this implication; why is $\mathbb{E}_s\\{\eta^2(x)\\} < \infty$?
3. Assumption 2: Although I'm familiar with math behind this assumption, I found it hard to understand its ramifications in this context. I understand that the $\beta$-regularity space is the set of $\rho$ such that $T^* T \rho$ is approximately invertible, but is there a more concrete intuition, or maybe some examples, of what $\beta$-regularity looks like when $T$ is the conditional expectation operator? For example, if if $\\{\phi_i\\}_{i = 1}^\infty$ is the Fourier basis, then $\beta$ is related to the smoothness/differentiability of $\rho$.
4. Assumption 5: Similar to the previous point, can you provide some intuition or examples for when Assumption 5 is satisfied?


**Minor**

1. Assumption 4: "Letting $\gamma = \min\\{k, \ell\\}$...": $\gamma$ is never used again in this assumption. Is this an error? Perhaps $\gamma$ should be defined in Assumption 5 instead?
2. Remark 6: Does "consistent" here mean "in operator norm"? If so, please make this more explicit.
3. I didn't understand the definition of "Delta Accuracy" in the experiments. Could you please provide a mathematical formula? Would $100\%$ correspond to perfect prediction?
4. Page 8, Last Sentence, "In each trial, we... randomly select 80% of the players with the other positions as the training source data.": If I understand correctly, the idea here is to use the bootstrap to obtain confidence intervals on performance. If so, this resampling should be done *with replacement*. Or is there a different reasoning here?
5. Page 9, First Paragraph, "For the temperature value shift between the training source and testing dataset, we use the humidity for the importance weight estimation.": I didn't understand this sentence. What does it mean to "use the humidity for the importance weight estimation" (as opposed to using all of the available features)?
6. Page 9, Second Paragraph, "our method improves about 4% for the SOCR dataset": I don't see this 4% in Table 1. What exactly is this refering to?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
