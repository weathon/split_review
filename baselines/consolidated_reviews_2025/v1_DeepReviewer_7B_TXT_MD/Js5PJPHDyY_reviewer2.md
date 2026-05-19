### Summary

This paper proposes a training-free CLIP adaptation method based on Gaussian Discriminant Analysis. The authors use Bayes’ formula and the maximum likelihood estimator to derive a linear classifier, which can be estimated from the data without any training. The method is evaluated on 11 datasets and shows comparable or better performance than training-required methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The proposed method is training-free, which is interesting and valuable for resource-constrained environments.
- The method is evaluated on 11 datasets, which shows the effectiveness of the proposed method.
- The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed method is a combination of existing techniques, including Bayes’ formula and the maximum likelihood estimator. The novelty is limited.
- The performance gain is marginal. The proposed method achieves comparable or better performance than training-required methods. However, the performance gain is not significant.
- The paper does not discuss the limitations of the proposed method. For example, the method assumes that the class means and covariance are sufficient to represent the data distribution, which may not hold true in complex real-world scenarios.

### Suggestions

The paper should more clearly articulate the specific scenarios where the proposed method offers a significant advantage over existing training-required approaches. While the training-free nature is a strength, the marginal performance gains raise questions about its practical utility. A more detailed analysis of the conditions under which the method excels, such as specific dataset characteristics or model architectures, would be beneficial. For example, it would be useful to investigate if the method performs better on datasets with specific types of image-text correlations or if it is more effective for certain types of base-to-new generalization tasks. Furthermore, the paper should explore the sensitivity of the method to the choice of hyperparameters, such as the regularization parameters in the covariance estimation, and provide guidelines for selecting appropriate values. 

To address the limited novelty, the authors could explore more sophisticated methods for deriving the linear classifier. For instance, instead of relying on a simple maximum likelihood estimator, they could investigate techniques that incorporate prior knowledge or learn a more robust representation of the data. This could involve exploring different kernel functions or non-linear transformations to better capture the underlying data structure. Additionally, the paper should provide a more in-depth analysis of the theoretical properties of the proposed method, such as its convergence behavior and generalization bounds. This would help to better understand the method's strengths and limitations and provide a more solid foundation for its practical application. The authors should also consider comparing their method to other training-free techniques, such as those based on knowledge distillation or feature alignment, to better contextualize its performance.

Finally, the paper should include a more thorough discussion of the limitations of the proposed method. Specifically, the assumption that class means and covariances are sufficient to represent the data distribution is a significant limitation that should be addressed. The authors should discuss the potential impact of this assumption on the method's performance in real-world scenarios where the data distribution may be more complex. For example, they could investigate how the method performs when the data is not well-represented by Gaussian distributions or when there are significant variations in the class covariances. Furthermore, the paper should discuss the computational cost of the proposed method, especially in comparison to training-required methods, and provide guidelines for its efficient implementation. Addressing these limitations would make the paper more robust and provide a more realistic assessment of the method's applicability.

### Questions

Please see the weaknesses.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
