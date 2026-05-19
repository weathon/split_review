### Summary

This paper proposes a training-free CLIP adaptation method based on Gaussian Discriminant Analysis (GDA). The method is simple and effective, and it achieves comparable or superior results with state-of-the-art methods on few-shot classification, imbalanced learning, and out-of-distribution generalization.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The proposed method is simple and effective, and it achieves comparable or superior results with state-of-the-art methods on few-shot classification, imbalanced learning, and out-of-distribution generalization.
2. The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is a combination of existing techniques, including Bayes’ formula and the maximum likelihood estimator. The novelty is limited.
2. The performance gain is marginal. The proposed method achieves comparable or better performance than training-required methods. However, the performance gain is not significant.
3. The paper does not discuss the limitations of the proposed method. For example, the method assumes that the class means and covariance are sufficient to represent the data distribution, which may not hold true in complex real-world scenarios.

### Suggestions

The paper's core idea of adapting CLIP using Gaussian Discriminant Analysis (GDA) is interesting, but the current implementation lacks a significant leap in performance compared to existing methods. While the authors emphasize the training-free nature of their approach, the marginal gains raise questions about its practical utility. To strengthen the paper, the authors should explore more sophisticated techniques for deriving the linear classifier beyond the basic GDA approach. For instance, they could investigate methods that incorporate regularization or learn a more robust representation of the data. This could involve exploring different kernel functions or non-linear transformations to better capture the underlying data structure. Additionally, the authors should consider incorporating techniques that can handle more complex data distributions, such as those that are not well-represented by Gaussian distributions. This would make the method more robust and applicable to a wider range of real-world scenarios.

To address the limited novelty, the authors could explore more advanced techniques for parameter estimation within the GDA framework. Instead of relying solely on the maximum likelihood estimator, they could investigate methods that incorporate prior knowledge or learn a more robust representation of the data. For example, they could explore techniques that use Bayesian inference or incorporate regularization terms to improve the stability and generalization of the classifier. Furthermore, the authors should provide a more thorough comparison with existing training-required methods, highlighting the specific scenarios where their method excels and where it falls short. This would help to better contextualize the contribution of their work and identify areas for future research. A more detailed analysis of the computational cost of the proposed method compared to training-required methods would also be beneficial.

Finally, the paper should include a more detailed discussion of the limitations of the proposed method. The assumption that class means and covariances are sufficient to represent the data distribution is a strong one, and the authors should discuss how this assumption might affect performance in real-world scenarios where data distributions are more complex. They could also explore alternative assumptions or incorporate techniques that can handle more complex data distributions. Furthermore, the authors should investigate the sensitivity of the method to different hyperparameter settings and provide guidelines for selecting appropriate values. This would make the method more practical and easier to use for other researchers. The authors should also discuss the potential impact of the method's limitations on its applicability in real-world scenarios.

### Questions

Please see the weaknesses.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
