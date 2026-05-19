### Summary

This paper proposes a unified perspective on the estimation of Shapley values, which is a popular method to quantify the importance of each feature in black-box models. The authors first show that different existing stochastic estimators for Shapley values can be viewed as the linear transformation of the values obtained from sampled subsets. Based on this, the authors propose a new estimator, SimSHAP, which minimizes the l2 distance to the approximated Shapley values within the Euclidean space. SimSHAP is simple and efficient, and extensive experiments demonstrate that it significantly accelerates the computation of accurate Shapley values.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. This paper is well-written and easy to follow.
2. The authors unify various existing stochastic estimators for Shapley values and show that they can be viewed as the linear transformation of the values obtained from sampled subsets. This provides a unified perspective for understanding these methods.
3. The authors propose a new estimator, SimSHAP, which minimizes the l2 distance to the approximated Shapley values within the Euclidean space. This estimator is simple and efficient.
4. Extensive experiments demonstrate that SimSHAP significantly accelerates the computation of accurate Shapley values.

### Weaknesses

#### Some Related Works


#### comment

1. The authors did not compare SimSHAP with other state-of-the-art Shapley value estimation methods, such as FastSHAP and SHAP-E. It is unclear how SimSHAP performs compared to these methods in terms of both accuracy and efficiency.
2. The authors did not compare SimSHAP with other gradient-based methods, such as Integrated Gradients and SmoothGrad. It is unclear how SimSHAP performs compared to these methods in terms of both accuracy and efficiency.
3. The authors did not provide a theoretical analysis of the approximation error of SimSHAP. It is unclear how the approximation error of SimSHAP depends on the number of samples and the complexity of the model.
4. The authors did not provide a theoretical analysis of the computational complexity of SimSHAP. It is unclear how the computational complexity of SimSHAP depends on the number of samples and the complexity of the model.

### Suggestions

The paper would significantly benefit from a more comprehensive empirical evaluation. Specifically, the authors should include comparisons with FastSHAP and SHAP-E, which are established methods for Shapley value estimation. These comparisons should be performed on a variety of datasets, including both tabular and image data, to assess the generalizability of SimSHAP. Furthermore, the evaluation should not only focus on accuracy but also on computational efficiency, providing a clear picture of the trade-offs between accuracy and speed. The authors should also consider using a wider range of evaluation metrics, such as the area under the ROC curve (AUC) for classification tasks and other relevant metrics for regression tasks, to provide a more comprehensive assessment of the performance of SimSHAP. This would help to establish the practical value of SimSHAP in real-world applications.

In addition to comparing with existing Shapley value estimation methods, the authors should also compare SimSHAP with other gradient-based explanation methods, such as Integrated Gradients and SmoothGrad. These methods, while not directly estimating Shapley values, provide valuable insights into the importance of input features and should be included in the comparison. The comparison should be based on both accuracy and efficiency, and the authors should discuss the strengths and weaknesses of SimSHAP relative to these methods. Furthermore, the authors should provide a detailed analysis of the computational cost of SimSHAP, including the time and memory requirements for different dataset sizes and model complexities. This analysis should be compared with the computational cost of other methods to provide a clear understanding of the efficiency of SimSHAP. This would help to position SimSHAP within the broader landscape of explanation methods.

Finally, the authors should provide a theoretical analysis of the approximation error and computational complexity of SimSHAP. This analysis should include a discussion of how the approximation error depends on the number of samples used for estimation and the complexity of the model being explained. The authors should also discuss the computational complexity of SimSHAP in terms of the number of samples and the complexity of the model. This theoretical analysis would provide a deeper understanding of the properties of SimSHAP and its limitations. For example, it would be useful to understand how the approximation error changes as the number of sampled subsets increases, and whether there are any theoretical guarantees on the convergence of the estimator. This would help to establish the theoretical foundations of SimSHAP and its applicability in different scenarios.

### Questions

Please see the weaknesses.

### Rating

6

### Confidence

3

**********
