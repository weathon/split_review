# Practical Kernel Learning for Kernel-based Conditional Independent Test

- Decision: Reject
- Scores: 5, 3, 5, 5

## Abstract
Conditional independence (CI) test stands as a fundamental and challenging task within modern statistics and machine learning. One pivotal class of methods for assessing conditional independence encompasses kernel-based approaches, known for their capability to identify general conditional dependence without necessitating assumptions about the conditional relationship or resorting to the simulation of intricate conditional distributions. As with any method utilizing kernels, selecting the appropriate kernel in kernel-based CI methods is critical for ensuring heightened test power and precise identification of conditional relationship. However, current methods typically involve the manual heuristic selection of kernel parameters, neglecting the inherent characteristics of the data and potentially leading to errors. In this paper, we propose a kernel parameter selection approach for the Kernel-based Conditional Independence test method (KCI). We decompose the statistic of KCI and treat the kernel applied on the conditioning set as a trainable component. The kernel parameters involved are then learned by maximizing the ratio of the estimated statistic to its variance, which approximates the test power at large sample sizes. Therefore, our method can learn the kernel parameters with increased test power at a very small additional computation cost. Extensive experiments demonstrate the effectiveness of our proposed approach in conditional independence testing and its enhancements to constrain-based causal discovery.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The submission describes an approach for data-driven kernel hyperparameters selection for improving the performance of kernel-based conditional independence hypothesis testing. 
The approach is based on an asymptotic approximation of the test power and its optimization.

### Strengths
- very interesting topic and problem
- mostly clearly written.
- simulation with ablation study, time complexity and details.

### Weaknesses
1. the theoretical framework is somehow confusing to me. As stated by the authors "no method can simultaneously control the
Type I error rate at the given significance level while maintaining adequate power" citing Shah & Peters (2020). But then the authors reach the conclusion that "the practical evaluation of CI methods necessitates a balanced assessment of both Type I and Type
II error rates, emphasizing the trade-off between error control and statistical power". In my understanding this is not what we require from a statistical testing procedure, it is essential to control type I error, at least under some assumptions.  
This is what Shah & Peters (2020) propose with the generalized covariance measure. 
Of course, in practice, rarely assumptions are met, but if the statistical method proposed is not able to control type I error at least under some assumptions how it can be considered a valid testing procedure? I feel this is the difference from hypothesis testing and binary classification. 
2. implications of 1. above are reflected in the evaluation in Figure 1, where it seems that only CIRCE is able to attain the required type I error control (of course with a higher type II error). Also about Figure 2 what is the meaning of testing CI with a 30 dimensional conditioning set with 1000 points without assumptions? It seems that is not possible and probably it should not be done no?

### Questions
see the weaknesses above and 

-  An operator "is not Hilbert-Schmidt in characteristic RKHS" does it means that is not bounded ?, that is has not a bounded HS norm? this should be clarified in the text.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper focuses on the parameter selection problem for kernel-based methods in conditional independence testing. By applying the decomposed statistic of kernel-based conditional independence test, the authors learn the kernel parameters by maximizing the ratio of the estimated statistic to its variance, which approximates the test power at large sample sizes.

### Strengths
This paper proposes a kernel parameter selection approach for the kernel-based conditional independence test. Appropriate experiments are conducted with some comparative methods.

### Weaknesses
The idea of learning kernel functions or kernel parameters is not new in the literature. Related papers include "Optimal kernel choice for large-scale two-sample tests", "Learning Deep Kernels for Non-Parametric Two-Sample Tests", and "Generative models and model criticism via optimized maximum mean discrepancy". This diminishes the novelty of the current paper.

### Questions
1. From my understainding, the feature map should be denoted by $\phi(x): \mathcal{X} \to \mathcal{H}_{\mathcal{X}}$. 

2. Section 3 includes several components, but it is unclear which parts are original contributions by the authors and which are drawn from existing literature. Please clarify this distinction, and provide appropriate references for any cited results.

3. Does the proposed method learn only the kernel bandwidths, or does it also learn the kernel functions? A more thorough discussion of the novelty of this method compared to existing approaches is necessary.

4. The asymptotic results are derived under fixed kernel parameters. How do the learned parameters affect these results? Moreover, how can the authors ensure that the proposed method, which uses the weighted sum of chi-squared to compute the $p$-value, controls the type I error at least asymptotically?

5. Could the authors provide a more detailed explanation of the impact of the conditional expectation bias?

6. Some phrases lack precision. For example, in "and Type II errro generally rises with increasing $Z$" and "slightly exceeding the significance level as $Z$ increases", it should refer to the increasing dimensionality of $Z$. In "$Z \sim N(0, d_Z)$", does $d_Z$ represent the dimension of $Z$?

7. Does the original form of KCI in Section 4.1.2 use the median heuristic for determining kernel bandwidth?

8. Does the discreteness of continuity of $X, Y, Z$ affect the performance of the proposed method, such as the choice of kernel?

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
This paper addresses the fundamental and challenging problem of conditional independence testing in statistics and machine learning. The authors propose to optimize kernel parameters by maximizing the ratio of the estimated Kernel-based Conditional Independence (KCI) test statistic to its variance. They assert that their approach enhances test power with minimal additional computational cost. Through extensive experiments, they demonstrate the effectiveness of this approach in accurately performing conditional independence tests.

### Strengths
The proposed method can learn the kernel parameters with increased test power at a small additional computation cost.

### Weaknesses
1. I think the main weakness of this paper lies in its novelty. The general idea is quite similar to Gretton et al. (2012). Though the authors claim that the CI testing requires indirectly considering the correlations between residuals rather than the original data, I don't see any specific methodological designs that incorporate this when optimizing kernel parameters.

2. The proposed method does not appear to show significant improvement based on the results presented in Figures 1 and 2.

### Questions
1. The authors suggest to optimize kernel parameters by maximizing the ratio of the estimated Kernel-based Conditional Independence test statistic to its variance. What is the convergence rate of these estimated parameters? Do they affect the asymptotic variance in equation (6)? Are there any theoretical guarantees of the proposed method?

2. In Section 2.1, the authors mention the necessity of a balanced assessment of both Type I and Type II error rates in the practical evaluation of CI methods. While I acknowledge the difficulty of CI testing problems, as highlighted by Shah and Peters (2020), I argue that controlling Type I error rates is paramount. Under what conditions can Type I error be effectively controlled by the proposed method?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents a method, termed POWER, designed for optimizing kernel parameters to improve the performance of kernel-based conditional independence tests. This method enables users to learn kernel parameters directly from the data, thereby enhancing the test's power. Experimental results demonstrate that it also positively impacts constraint-based causal discovery methods.

### Strengths
1. In contrast to previous methods that generally employ a median heuristic algorithm for selecting kernel parameters, this paper introduces a data-driven approach to identify the optimal parameters, thereby enhancing the test's power to some extent.

2. This study examines the effect of optimizing kernel parameters for various variables on the algorithm's power. Ultimately, the optimization is confined to the kernel function within the conditioning set, which maximizes the algorithm's power while maintaining manageable time complexity.

3. The experimental results demonstrate that the proposed POWER method outperforms both the original kernel parameter settings and several conditional independence baselines in certain settings. Furthermore, when applied to causal discovery, it generally produces superior results.

### Weaknesses
1. The method presented in this paper demonstrates only marginal improvements in power, yielding minimal gains compared to the original median heuristic algorithm.

2. The conditional mean of the statistic is estimated using kernel ridge regression; however, the paper derives the asymptotic normality of the oracle statistic only under the case when the conditional mean is known.

3. The proposed method has not been evaluated in scenarios characterized by higher dimensionality and smaller sample sizes. The maximum tested dimensionality of Z is only 30, and the minimum sample size is 200, which restricts the significance of the results.

### Questions
1. If the estimated conditional mean is incorporated into the statistic, does it still retain asymptotic normality? What conditions are necessary for it to maintain this property? If asymptotic normality is preserved, how does it affect the asymptotic variance? If the asymptotic variance changes, the methods for enhancing power derived from the original asymptotic variance may no longer be valid.

2. In the context of estimating conditional means for conditional independence testing, several more effective methods have emerged. Notably, generative models can serve this purpose. For instance, Shi et.al. (2021) employed Sinkhorn GAN for estimating conditional means. If these methods were to replace kernel ridge regression for estimating conditional means, what impact would this have on your approach?

3. Your method seems to overlook scenarios involving higher dimensionality of Z and smaller sample sizes. For example, dz=100 and n=500 as in Li et.al. (2024). 

4. In addressing the causal discovery problem, you have only presented the F1 scores for the POWER and Median methods, and the results appear to lack significance. Could you conduct additional experiments to provide further clarification?

5. Could you provide a theoretical explanation of how this method enhances statistical power? For example, you can derive its asymptotic power against local alternative under a specific model (Niu et.al. (2022)).

6. In theoretical frameworks, it is often essential to split samples—utilizing one subset to estimate the conditional mean and another to compute the statistic (Shi et.al. (2021), Shah et.al. (2020)). However, in practice, sample splitting may result in a reduction in statistical power. Did the authors evaluate the effects of data splitting on their methodology through simulation experiments to determine whether it is necessary to perform data splitting?

Reference:

1.	Shi, C., Xu, T., Bergsma, W., & Li, L. (2021). Double generative adversarial networks for conditional independence testing. Journal of Machine Learning Research, 22(285), 1-32.

2.	Niu, Z., Chakraborty, A., Dukes, O., & Katsevich, E. (2022). Reconciling model-X and doubly robust approaches to conditional independence testing. arXiv preprint arXiv:2211.14698.

3.	Shah, R. D., & Peters, J. (2020). The hardness of conditional independence testing and the generalised covariance measure.

4.	Li, S., Zhang, Y., Zhu, H., Wang, C., Shu, H., Chen, Z., ... & Yang, Y. (2024). K-nearest-neighbor local sampling based conditional independence testing. Advances in Neural Information Processing Systems, 36.

### Soundness
2

### Presentation
3

### Contribution
2
