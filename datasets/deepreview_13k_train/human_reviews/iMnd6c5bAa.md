# Density Ratio Estimation-based Bayesian Optimization with Semi-Supervised Learning

- Decision: Reject
- Scores: 3, 3, 5

## Abstract
Bayesian optimization has attracted huge attention from diverse research areas in science and engineering, since it is capable of efficiently finding a global optimum of an expensive-to-evaluate black-box function. In general, a probabilistic regression model is widely used as a surrogate function to model an explicit distribution over function evaluations given an input to estimate and a training dataset. Beyond the probabilistic regression-based methods, density ratio estimation-based Bayesian optimization has been suggested in order to estimate a density ratio of the groups relatively close and relatively far to a global optimum. Developing this line of research further, supervised classifiers are employed to estimate a class probability for the two groups instead of a density ratio. However, the supervised classifiers used in this strategy are prone to be overconfident for known knowledge on global solution candidates. Supposing that we have access to unlabeled points, e.g., predefined fixed-size pools, we propose density ratio estimation-based Bayesian optimization with semi-supervised learning to solve this challenge. Finally, we show the empirical results of our methods and several baseline methods in two distinct scenarios with unlabeled point sampling and a fixed-size pool and analyze the validity of our proposed methods in diverse experiments.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes the DRE-BO-SSL method, which introduces the concept of semi-supervised learning to address the over-confidence (over-exploitation) issue observed in density-ratio-based Bayesian optimization problems. In general Bayesian optimization, Bayesian regression models such as Gaussian Process models are often used; however, this study focuses on the density-ratio-based approach discussed in works such as [Bergstra et al. (2011)], [Tiao et al. (2021)], and [Song et al. (2022)]. The main contribution of the proposed method is the incorporation of traditional semi-supervised learning approaches, such as label propagation and label spreading, into density-ratio-based Bayesian optimization. According to the authors, this allows for resolving the over-confidence (over-exploitation) problem in density-ratio-based BO.

### Strengths
- Bayesian optimization based on a standard Gaussian Process model incurs high computational costs when the sample size is large. The density-ratio-based approach, as discussed in works such as [Bergstra et al. (2011)], [Tiao et al. (2021)], and [Song et al. (2022)], could serve as an effective alternative. In this sense, the topic addressed in this paper is important.

- The authors' approach of identifying issues based on experimental observations, such as those in Figure 1, and formulating the problem generally to address these issues is practical, as it reflects real-world challenges in data analysis.

- The paper provides a clear and concise overview of existing methods such as density-ratio-based Bayesian optimization and label propagation, making it accessible even for readers who are not well-versed in this field.

### Weaknesses
- This study aims to tackle the over-confidence and over-exploitation problem in density-ratio-based Bayesian optimization. However, it remains unclear why a semi-supervised learning approach based on label propagation would effectively address this issue. Similarly, the rationale behind using the sampling method in Equation (10) for unlabeled point sampling was not clearly explained, making the motivation difficult to grasp. If the authors rely solely on experimental evaluations without clear explanations, presenting these findings at a top-tier conference like ICLR may be premature; more thorough discussions and theoretical analyses are needed.

- In my opinion, the proposed DRE-BO-SSL method lacks originality for top-tier conferences like ICLR, as it simply applies label propagation—traditional semi-supervised learning techniques—to existing density-ratio-based Bayesian optimization. Deeper considerations are necessary, such as whether other semi-supervised learning methods might prove ineffective or what outcomes might arise if a semi-supervised learning approach were applied to Gaussian Process-based Bayesian optimization.

### Questions
None.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposes semi-supervised learning (SSL) based Bayesian optimization (BO). The basic idea is to use label propagation (spreading) to utilize unlabeled points. The authors claim that SSL provides a better classification resulting from which a better solution should be obtained.

### Strengths
- To my knowledge, a combination of the density ratio based BO and SSL has not been widely studied.

- The paper is well-organized and easy to follow.

### Weaknesses
- The fundamental assumption of SSL is that p(X) provides some information about p(Y∣X) (since the unlabeled data are sampled from P(X)), which has been discussed in classical text such as [1]. However, there is no discussion or fundamental justification of the situations in BO where this hypothesis holds. In other words, the paper fails to show a rationale why SSL is effective for BO.

[1] Chapelle, et al., Semi-Supervised Learning, MIT Press, 2006.

- In fact, the relation between p(X) and p(Y|X) is highly unclear in the experimental settings, and therefore, it is unclear why SSL is effective. In the synthetic data, X is from uniform and nothing is related to Y. In tabular benchmark and NATS-Bench, the candidate points are uniform grid according to the tables in appendix. Therefore, it is quite unclear why unlabeled points is informative for applying SSL. In 64D MNIST, samples in the same three digits may consists of low-dimensional manifold. On the other hand, the number of three digits, the target to be optimized, would not continuous in the pixel space (e.g., 000 and 100 would be relatively close in the pixel space, but the value of y is largely different. In other words, proximity in X space is not fully informative about proximity in Y space). For me, validity as a BO benchmark problem of 64D MNIST is not clear.

- SSL methods used in the paper is most classical methods (proposed in 2002 and 2003), no more recent methods are mentioned in detail.

- How SSL avoids the overconfidence issue. Mathematical detailed mechanisms are not shown.

- It is unclear how the cluster assumption and f(z) is related. Since f(z) is (truncated) standard normal, the cluster structure should become quite simple and nothing is related to Y. Therefore, here again, I currently do not think f(z) satisfies the requirement of SSL.

### Questions
- How \zeta^-1 p(z=1|x)/(p(z=1|x) + p(z=0|x)) is derived from (2)?

- How the threshold for y is determined from zeta?

- In 64D MNIST, the authors mentioned that the problem is to find the 'minimum' multi-digit number. This means that there exists multiple global minimum? (i.e., all images with '000' are global minimum?)

### Soundness
2

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
4

### Summary
The paper proposes a novel Bayesian optimization (BO) method called DRE-BO-SSL, which combines semi-supervised learning (SSL) with Density Ratio Estimation-based BO (DRE-BO). It addresses the common issue of overconfidence in classifiers used in DRE-based BO methods like BORE and LFBO, particularly when early-stage data is limited. By incorporating SSL techniques—specifically estimating pseudo-labels through label propagation and label spreading—the method refines class label predictions and improves classifier accuracy. This approach enhances the exploration-exploitation trade-off, mitigating the tendency to over-exploit due to overconfident classifiers.
Instead of fitting a regressor to observed data, DRE-BO-SSL uses a classifier to guide the search, computing the acquisition function in terms of class probability ratios. Comparative experiments on synthetic and real problems demonstrate that DRE-BO-SSL outperforms traditional Gaussian Process-based BO and recent density ratio-based approaches across a wide range of tasks. The empirical results show that integrating SSL techniques into DRE-based BO effectively improves performance by leveraging unsupervised data sampling to address overconfidence issues.

### Strengths
The proposed method is novel and represents a good contribution to Density Ratio Estimation-based Bayesian Optimization (DRE-based BO). By using semi-supervised learning in DR-based BO to address the overconfidence issue, the authors offer a promising approach with nice empirical results. The concept of employing semi-supervised learning is intriguing and shows potential in solving the general overconfidence problem in DRE.

### Weaknesses
While the proposed method is novel, several significant issues need to be addressed:
- There is no clear explanation of how the overconfidence problem is resolved through the use of semi-supervised learning. Although Appendix C attempts to elucidate the reasoning or mechanism by which semi-supervised learning mitigates overconfidence, the explanation lacks clarity and fails to provide a compelling rationale. In fact, Figure 12 appears to indicate that unlabeled data may not be necessary, which contradicts the premise that semi-supervised learning is essential for addressing the overconfidence issue.

- As the authors themselves acknowledge, the proposed method does not offer theoretical guarantees within the context of Bayesian Optimization. This omission raises concerns about the method's validity and applicability.

These shortcomings suggest that the paper does not adequately justify the need for the proposed method, nor does it thoroughly explain how the method effectively addresses the identified problem. Addressing these issues would strengthen the contribution and impact of the work.

Another issue, rather minor compared to the above motivation issue, is that the presentation of the paper should be improved. For example, \zeta is used in the Introduction before it is properly defined in Section 3.

### Questions
- \Sigma, upper/lower bounds u,l for the truncated normal are not properly defined. How should we set or estimate these values?
- How this particular way of sampling is related to the cluster assumption?

### Soundness
3

### Presentation
2

### Contribution
2
