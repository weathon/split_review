### Summary

This paper proposes a new method for estimating Shapley values, called SimSHAP, which is a simple and fast amortized estimator. The authors unify existing stochastic estimators for Shapley values and show that these estimators can be viewed as linear transformations of importance sampling of feature subsets. The authors then propose SimSHAP, which minimizes the l2 distance to the approximated Shapley values within the Euclidean space. The authors conduct experiments on tabular and image datasets to demonstrate the effectiveness of SimSHAP.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The authors unify existing stochastic estimators for Shapley values and show that these estimators can be viewed as linear transformations of importance sampling of feature subsets. This provides a unified perspective for understanding existing stochastic estimators.
3. The authors propose SimSHAP, which minimizes the l2 distance to the approximated Shapley values within the Euclidean space. This approach is simple and efficient.
4. The authors conduct experiments on tabular and image datasets to demonstrate the effectiveness of SimSHAP.

### Weaknesses

#### Some Related Works

[1] FastSHAP: Real-Time Shapley Value Estimation

#### comment

1. The authors did not compare SimSHAP with other state-of-the-art Shapley value estimation methods, such as FastSHAP [1] and SHAP-E [2]. It is unclear how SimSHAP performs compared to these methods in terms of both accuracy and efficiency.
2. The authors did not compare SimSHAP with other gradient-based methods, such as Integrated Gradients and SmoothGrad. It is unclear how SimSHAP performs compared to these methods in terms of both accuracy and efficiency.
3. The authors did not provide a theoretical analysis of the approximation error of SimSHAP. It is unclear how the approximation error of SimSHAP depends on the number of samples and the complexity of the model.
4. The authors did not provide a theoretical analysis of the computational complexity of SimSHAP. It is unclear how the computational complexity of SimSHAP depends on the number of samples and the complexity of the model.

### Suggestions

The paper would benefit significantly from a more thorough empirical evaluation. Specifically, the authors should compare SimSHAP against a wider range of state-of-the-art Shapley value estimation methods, including FastSHAP and SHAP-E. These comparisons should be performed on a variety of datasets, including both tabular and image data, to assess the generalizability of SimSHAP. Furthermore, the authors should include comparisons with other gradient-based explanation methods, such as Integrated Gradients and SmoothGrad, to provide a more comprehensive understanding of SimSHAP's strengths and weaknesses. These comparisons should be conducted using standard evaluation metrics, such as the area under the ROC curve (AUC) for classification tasks and other relevant metrics for regression tasks. The authors should also provide a detailed analysis of the computational cost of SimSHAP, including the time and memory requirements for different dataset sizes and model complexities. This analysis should be compared with the computational cost of other methods to provide a clear understanding of the efficiency of SimSHAP.

In addition to the empirical evaluation, the authors should provide a theoretical analysis of the approximation error and computational complexity of SimSHAP. This analysis should include a discussion of how the approximation error depends on the number of samples used for estimation and the complexity of the model being explained. The authors should also discuss the computational complexity of SimSHAP in terms of the number of samples and the complexity of the model. This theoretical analysis would provide a deeper understanding of the properties of SimSHAP and its limitations. For example, the authors could investigate the convergence rate of SimSHAP and how it relates to the number of samples. They could also analyze the impact of the choice of the Euclidean space on the approximation error. Furthermore, the authors should clarify the practical implications of their work. While the paper presents a new method for estimating Shapley values, it is not clear how this method can be used in practice. The authors should provide concrete examples of how SimSHAP can be applied to real-world problems and how it can be used to gain insights into the behavior of complex models. This would help to demonstrate the practical relevance of the proposed method and its potential impact on the field.

Finally, the authors should address the concerns regarding the novelty of their work. While the authors unify existing stochastic estimators for Shapley values, the contribution of SimSHAP itself needs to be more clearly articulated. The authors should provide a more detailed explanation of how SimSHAP differs from existing methods and what specific advantages it offers. The authors should also discuss the limitations of their approach and identify areas for future research. This would help to provide a more balanced and nuanced perspective on the contribution of their work. The authors should also clarify the specific scenarios where SimSHAP is expected to perform well and where it might not be suitable. This would help to guide future research in this area and to identify the open questions that remain to be addressed.

### Questions

1. How does SimSHAP compare to other state-of-the-art Shapley value estimation methods, such as FastSHAP [1] and SHAP-E [2], in terms of both accuracy and efficiency?
2. How does SimSHAP compare to other gradient-based methods, such as Integrated Gradients and SmoothGrad, in terms of both accuracy and efficiency?
3. What is the theoretical analysis of the approximation error of SimSHAP?
4. What is the theoretical analysis of the computational complexity of SimSHAP?
5. What are the practical implications of your work? How can SimSHAP be used in real-world applications?

[1] https://arxiv.org/abs/1802.03301

[2] https://arxiv.org/abs/2305.14814

### Rating

5

### Confidence

3

**********
