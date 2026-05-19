### Summary

The paper presents Maestro, a novel approach for training low-rank neural networks that leverages progressive shrinking and ordered dropout to optimize the rank decomposition of DNNs. The method introduces a hierarchical group-lasso penalty to progressively shrink the rank of layers, which is claimed to be more efficient than traditional SVD-based methods. The authors demonstrate the effectiveness of Maestro on various datasets and architectures, showing improvements in accuracy and computational efficiency compared to other compression techniques.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow, with a clear explanation of the proposed method and its theoretical underpinnings.
2. The authors provide a thorough comparison of Maestro with other low-rank approximation methods, demonstrating its superior performance in terms of accuracy and efficiency.
3. The paper includes a detailed ablation study that examines the impact of different components of the method, providing insights into the design choices.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost of Maestro compared to other methods. While the authors claim that Maestro is more efficient than SVD-based methods, they do not provide a quantitative comparison of the training time and memory usage. Specifically, the paper lacks a breakdown of the computational overhead introduced by the progressive shrinking and ordered dropout, making it difficult to assess the practical benefits of the method. A comparison of the number of floating-point operations (FLOPs) and memory access patterns would be beneficial.
2. The paper does not explore the scalability of Maestro to larger models and datasets. While the authors demonstrate the effectiveness of Maestro on several datasets and architectures, it is unclear how the method would perform on larger models with billions of parameters and datasets with trillions of samples. The paper should include experiments on larger models and datasets to demonstrate the scalability of the method and its applicability to real-world scenarios. The current experiments are limited to relatively small models and datasets, which may not be representative of the challenges encountered in practice.
3. The paper does not discuss the limitations of Maestro or potential failure cases. It is important to understand the scenarios where Maestro may not perform well, such as when the optimal rank is not well-defined or when the data distribution is highly non-linear. The paper should include a discussion of the limitations of the method and potential failure cases to provide a more complete picture of its applicability.

### Suggestions

To address the lack of detailed computational cost analysis, the authors should include a thorough comparison of the training time and memory usage of Maestro with other low-rank approximation methods. This comparison should include a breakdown of the computational cost of each step of the algorithm, such as the progressive shrinking and ordered dropout. The authors should also provide a quantitative comparison of the number of floating-point operations (FLOPs) and memory access patterns. This analysis should be performed on different datasets and architectures to demonstrate the scalability of the method. Furthermore, the authors should discuss the potential impact of the method on the training time and memory usage of different hardware platforms. This would provide a more complete understanding of the practical benefits of Maestro.

To address the lack of scalability analysis, the authors should include experiments on larger models and datasets. This could include experiments on models with billions of parameters and datasets with trillions of samples. The authors should also discuss the potential challenges of applying Maestro to such large models and datasets. This could include the need for more efficient implementations of the method and the need for more sophisticated hardware platforms. The authors should also discuss the potential impact of the method on the training time and memory usage of different hardware platforms. This would provide a more complete understanding of the applicability of Maestro to real-world scenarios.

To address the lack of discussion of limitations, the authors should include a discussion of the potential failure cases of Maestro. This could include scenarios where the optimal rank is not well-defined or when the data distribution is highly non-linear. The authors should also discuss the potential impact of the method on the generalization performance of the model. This could include a discussion of the potential for overfitting or underfitting. The authors should also discuss the potential impact of the method on the robustness of the model. This would provide a more complete understanding of the applicability of Maestro to real-world scenarios.

### Questions

1. How does Maestro handle the case where the optimal rank is not well-defined or when the data distribution is highly non-linear?
2. What are the potential limitations of Maestro in terms of scalability to larger models and datasets?
3. How does the choice of hyperparameters affect the performance of Maestro, and what are the guidelines for selecting the optimal hyperparameters?

### Rating

6

### Confidence

3

**********
