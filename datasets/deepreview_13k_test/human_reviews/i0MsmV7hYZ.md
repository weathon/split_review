# Advancing Counterfactual Inference through Quantile Regression

- Decision: Reject
- Scores: 3, 6, 5

## Abstract
The capacity to address counterfactual "what if" inquiries is crucial for understanding and making use of causal influences. Traditional counterfactual inference usually assumes a structural causal model is available. However, in practice, such a causal model is often unknown and may not be identifiable. This paper aims to perform reliable counterfactual inference based on the (learned) qualitative causal structure and observational data, without a given causal model or even directly estimating conditional distributions. We re-cast counterfactual reasoning as an extended quantile regression problem using neural networks. The approach is statistically more efficient than existing ones, and further makes it possible to develop the generalization ability of the estimated counterfactual outcome to unseen data and provide an upper bound on the generalization error. Experiment results on multiple datasets strongly support our theoretical claims.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper establishes a novel connection between counterfactual inference and quantile regression. The method proposed in this paper does not rely on a predefined causal model or even direct estimations of conditional distributions.

### Strengths
I believe that summarizing the idea through simulation is a good approach.

### Weaknesses
Overall, I think this paper is not sound. Specifically, I think Theorem 1 is not credible. 

---
1. I believe that the Introduction should provide a more detailed explanation of the main idea of the paper. Currently, I am unable to understand how the main idea of the paper is introduced in Section 1. Specifically, I am confused about why $P(Y \leq Y_{X=x'} | x',Z=0.5) = P(E \leq -0.5)$. If we are given $X=x'$, then $Y = Y_{X = x'}$. Therefore, it seems to me that $P(Y \leq Y_{X=x'} | x',Z=0.5) = P(E \leq -0.5) = 1$ since $Y = Y_{X = x'}$ given $X=x'$.

2. Theorem 1 does not appear to be formal. For instance, it is unclear what is meant by "corresponds". Does it mean that they are equal?

3. This paper lacks mathematical rigor, resulting in logical gaps in the proof of Theorem 1. These gaps undermine the credibility and validity of the results. For instance, in the proof of Theorem 1, what is meant by "$Y_{X=x'} \vert X=x, Y=y, Z=z$ can be calculated as $f^i(X=x',Z=z,E=e^i)$"? If this implies that they are equal, please explain the reasoning behind their equality. It appears to me that $f^i(X=x',Z=z,E=e^i)$ represents $Y_{X=x'}(e^i)$ when $Z=z$. Even if $e^i$ is evidence of $(X=x,Y=y,Z=z)$, it does not imply that $Y_{X=x'}(e^i)$ is equal to $Y_{X=x}' \vert X=x, Y=y, Z=z$. The former is a real value, while the latter is a random variable.

4. Other miscellaneous weaknesses are summarized in the Issues Section below.

### Questions
Here, I have combined questions and issues together.

1. In the abstract, “Traditional counterfactual inference usually assumes the availability of a structural causal model” is a false statement. No existing causal inference frameworks assume the availability of structural causal models. Instead, they assume a proxy of the causal model, such as a graph and a distribution (or data that follows the distribution). As an alternative to the graph, the conditional independence embedded by the structural causal model can be assumed (e.g., ignorability). Overall, the availability of the causal model is not assumed. However, some restrictions on the distribution in the form of a graph or independence are assumed. 

2. More explanation is needed for the equation $P(Y \leq Y_{X=x'} | x',Z=0.5) = P(E \leq -0.5)$.

3. What does $E \perp (X;Z)$ mean? Does it mean that $E \perp \{X,Z\}$ or $E \perp X \vert Z$?

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper addresses the estimation of counterfactual outcomes in structural causal models. Typically, this problem is solved by explicitly representing the causal relationships using unobserved noise terms as input, and subsequently reconstructing the noise to estimate counterfactual outcomes. However, this paper proposes a different approach, modeling counterfactual outcomes as a quantile regression problem. This method utilizes the fact that an intervention do(X = x) results in an interventional distribution for the target variable, while in the counterfactual case, fixing the noise yields a point estimate equivalent to a quantile of this interventional distribution.

### Strengths
The paper introduces a very interesting and novel approach to counterfactual estimation. In particular, the presented method also works in settings with samll sample sizes.

### Weaknesses
The paper and method is very interesting, but there are some unclear points:

- The link between quantile regression and counterfactuals within Pearl's framework is not well explained in Section 3. This could be clarified by explaining that typically one obtains an interventional distribution for Y|do(X=x) (rung 2), and the next step, proceeding to rung 3 in Pearl's framework, involves identifying a specific point on this conditional distribution, which is here formulated as a particular quantile of the interventional distribution. This would make the connection much clearer.
- Large part of the evaluations focus more on the "interventional" performance rather than the "counterfactual" performance. The average treatment effect evaluation actually assesses E[Y|do(T=0)] - E[Y|do(T=1)], which are quantities derived from rung 2 interventional causal queries that do not require counterfactuals for the estimation. While I see the point of formulating it as the difference over the counterfactual outcomes of individual observations, it actually reduces to the difference between the means of the interventional distributions. Here, additional comparision with point-wise counterfactuals would be more insightful, as done in the related deep-learning literature you are referencing.

### Questions
The following is a mix of remarks and questions:

- The introduction assumes a good understanding of counterfactuals in Pearl's framework, which may not be the case for all readers. The use of the term "counterfactual" varies across the literature, and it is particularly different in the PO framework in comparison to Pearl's framework (due to the explicit modeling of the noise), despite their logical equivalence under certain conditions.
- In the three-step procedure’s prediction step, it can be clearer specified that estimated noise values are utilized, instead of just mentioning "U".
- After introducing quantile regression in Section 2, at this point already, an explanation of why this problem is statistically simpler than estimating the conditional expectation would be insightful.
- Many deep learning models cited in related works are not used for comparison, despite being considered state-of-the-art for counterfactual inference. Why not?
- The paragraph after Theorem 1 needs more clarification: In what scenarios is it not idenfitifiable when using the mean, while it is using quantiles?
- While you only refer to "discrete data", it should be noted that the functional causal models listed (e.g., additive noise model) are intended for non-categorical data. In categorical cases, point estimates for counterfactuals are not possible.
- In the modeling part of your method, where do assumptions such as monotonicity come into play, and how they are encoded in the model? In the list of models you provide at the end of Section 3, this is for instance encoded by restricting the model classes to ensure invertibility with respect to E. Or in case of an autoregressive flow model, this is given by the invertibility property, etc.
- You sometimes use "U" and sometimes "E" for the noise. This could be more consistent.
- I definitely want to avoid a typical reviewer comment like "why didn't you compare it with xyz", but here I see some obvious points: Given the referenced works on counterfactual inference: 1) There is no comparision with the mentioned recent deep-learning works in the experiments. 2) A more direct estimation of the quality of the counterfactuals using artificial data, especially with a larger graph, would provide more insights than estimating treatment effect quantities (like you did in Table 1). As mentioned before, the latter does not even require counterfactual estimates (for Table 2). In this regard, even a simple comparision with additive noise models would be insightful.
- The PEHE and Rpol metrics are not introduced.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper formulates the counterfactual inference problem as a bi-level optimization problem and presents a neural network-based framework to implement it.

### Strengths
- The problem studied in this article is very interesting. Quantile estimation in counterfactual outcome estimation holds promise for future research.
- The proposed method has achieved significant improvements in both synthetic and semi-synthetic data, demonstrating the effectiveness of the proposed approach.

### Weaknesses
Novelty: **Collaborating Networks** [Zhou et al., 2021; [Zhou et al., 2022] have formulated the quantile regression as a bi-level collaborating optimization problem. The authors should compare and analyze the novelty of their work in relation to these studies.

Writing and Organization: The writing and organization need improvement. There are some confusing and contradictory arguments in the main text that the author should clarify further. In the Introduction section, notations X, Y, Z, and E are used before being defined. Figure 1 only shows the dose-response curve of X on Y, which is a typical continuous treatment setting. Additionally, the green nodes are not defined, and the τ-value is also not reflected in the figure. Figure 1 should be an abstract motivation of the problem, but it does not demonstrate the importance of Quantile Regression. I cannot obtain information from this figure that demonstrates Quantile Regression can help estimate causal effects.

Related Literature and Baselines: This paper is related to the **Quantile Treatment Effect** [Powell, 2020; Xie et al., 2020; Sun et al., 2021] and **Collaborating Networks** [Zhou et al., 2021; [Zhou et al., 2022]. It would be beneficial to provide a more thorough analysis with existing quantile causal models.

Wrong Critical Statement:  In causal inference, most works assume that the covariates Z are collected before the treatment X is administered, and the outcomes Y are observed after the treatment is implemented. This is fairly common in real-world applications. For example, doctors provide treatment based on the patient's health condition, and these variables also affect the patient's final treatment outcome. I believe that such causal models and assumptions are reasonable and valid. Therefore, I disagree with the author's criticism of the causal models proposed by (Johansson et al., 2016; Yoon et al., 2018; Bica et al., 2020; Liuyi Yao, 2018), claiming that they are often unknown and difficult to identify with limited samples.

Potential Contradictory Statement: There seems to be some inconsistency in the paper. On one hand, the paper states that causal models are often unknown and hard to identify in practical applications with finite samples. On the other hand, the paper relies on the same predefined causal model, requiring covariates Z as a set of common causes for X and Y. This seems to contradict the previous statement.

Question: Can the proposed method address unmeasured confounding bias, specifically eliminating the indirect effect from unmeasured confounders, i.e., $E \not\perp(X; Z; Y)$?

[Powell, 2020] Powell, David. "Quantile treatment effects in the presence of covariates." *Review of Economics and Statistics* 102.5 (2020): 994-1005.

[Xie et al., 2020] Xie Y, Cotton C, Zhu Y. Multiply robust estimation of causal quantile treatment effects[J]. Statistics in Medicine, 2020, 39(28): 4238-4251.

[Sun et al., 2021] Sun, Shuo, Erica EM Moodie, and Johanna G. Nešlehová. "Causal inference for quantile treatment effects." *Environmetrics* 32.4 (2021): e2668.

[Zhou et al., 2021] Zhou, Tianhui, et al. "Estimating uncertainty intervals from collaborating networks." *The Journal of Machine Learning Research* 22.1 (2021): 11645-11691.

[Zhou et al., 2022] Zhou, Tianhui, William E. Carson IV, and David Carlson. Estimating Potential Outcome Distributions with Collaborating Causal Networks. TMLR (2022).

### Questions
See Above.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
