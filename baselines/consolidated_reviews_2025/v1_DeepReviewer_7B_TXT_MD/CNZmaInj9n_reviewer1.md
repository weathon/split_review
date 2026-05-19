### Summary

This paper proposes a new method for estimating Shapley values. The authors first unify various existing Shapley value estimation methods under a single framework. Then, they propose a simple and efficient estimator called SimSHAP, which minimizes the l2 distance to the approximated Shapley values within the Euclidean space. The authors demonstrate the effectiveness of SimSHAP through experiments on tabular and image datasets.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

- The authors unified various existing Shapley value estimation methods under a single framework, which provides a new perspective for understanding these methods.
- The authors proposed a simple and efficient estimator called SimSHAP, which minimizes the l2 distance to the approximated Shapley values within the Euclidean space. The authors show that SimSHAP achieves comparable accuracy and maintain competitive approximation accuracy while maintaining high efficiency.

### Weaknesses

#### Some Related Works

[1] FastSHAP: Real-Time Shapley Value Estimation
[2] Shapley explainability on the data manifold

#### comment

 - The authors did not compare SimSHAP with other state-of-the-art Shapley value estimation methods, such as FastSHAP [1] and SHAP-E [2]. It is unclear how SimSHAP performs compared to these methods in terms of both accuracy and efficiency.
- The authors did not compare SimSHAP with other gradient-based methods, such as Integrated Gradients and SmoothGrad. It is unclear how SimSHAP performs compared to these methods in terms of both accuracy and efficiency.
- The authors did not provide a theoretical analysis of the approximation error of SimSHAP. It is unclear how the approximation error of SimSHAP depends on the number of samples and the complexity of the model.
- The authors did not provide a theoretical analysis of the computational complexity of SimSHAP. It is unclear how the computational complexity of SimSHAP depends on the number of samples and the complexity of the model.

### Suggestions

The paper would benefit significantly from a more thorough empirical evaluation. Specifically, the authors should compare SimSHAP against a wider range of state-of-the-art Shapley value estimation methods, including FastSHAP [1] and SHAP-E [2], to demonstrate its relative performance in terms of both accuracy and efficiency. This comparison should be performed on a variety of datasets, including both tabular and image data, to assess the generalizability of SimSHAP. Furthermore, the authors should include comparisons with other gradient-based explanation methods, such as Integrated Gradients and SmoothGrad, to provide a more comprehensive understanding of SimSHAP's strengths and weaknesses. These comparisons should be conducted using standard evaluation metrics, such as the area under the ROC curve (AUC) for classification tasks and other relevant metrics for regression tasks. The authors should also provide a detailed analysis of the computational cost of SimSHAP, including the time and memory requirements for different dataset sizes and model complexities. This analysis should be compared with the computational cost of other methods to provide a clear understanding of the efficiency of SimSHAP.

In addition to the empirical evaluation, the authors should provide a theoretical analysis of the approximation error and computational complexity of SimSHAP. This analysis should include a discussion of how the approximation error depends on the number of samples used for estimation and the complexity of the model being explained. The authors should also discuss the computational complexity of SimSHAP in terms of the number of samples and the complexity of the model. This theoretical analysis would provide a deeper understanding of the properties of SimSHAP and its limitations. For example, the authors could investigate the convergence rate of SimSHAP and how it relates to the number of samples. They could also analyze the impact of the choice of the Euclidean space on the approximation error. Furthermore, the authors should provide a more detailed explanation of the unified framework for Shapley value estimation methods. This explanation should include a discussion of the assumptions and limitations of each method and how they relate to the proposed SimSHAP method. This would help the reader to understand the theoretical underpinnings of SimSHAP and its relationship to other methods.

Finally, the authors should clarify the practical implications of their work. While the paper presents a new method for estimating Shapley values, it is not clear how this method can be used in practice. The authors should provide concrete examples of how SimSHAP can be applied to real-world problems and how it can be used to gain insights into the behavior of complex models. This would help to demonstrate the practical relevance of the proposed method and its potential impact on the field. The authors should also discuss the limitations of their method and suggest directions for future research. This would help to guide future work in this area and to identify the open questions that remain to be addressed.

### Questions

- How does SimSHAP compare to other state-of-the-art Shapley value estimation methods, such as FastSHAP [1] and SHAP-E [2], in terms of both accuracy and efficiency?
- How does SimSHAP compare to other gradient-based methods, such as Integrated Gradients and SmoothGrad, in terms of both accuracy and efficiency?
- What is the theoretical analysis of the approximation error of SimSHAP?
- What is the theoretical analysis of the computational complexity of SimSHAP?

[1] https://arxiv.org/abs/1802.03301

[2] https://arxiv.org/abs/2305.14814

### Rating

5

### Confidence

3

**********
