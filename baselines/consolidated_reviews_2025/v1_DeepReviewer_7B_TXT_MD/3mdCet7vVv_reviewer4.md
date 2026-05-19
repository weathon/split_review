### Summary

This paper presents Maestro, a novel method for training low-rank neural networks. The authors propose a progressive shrinking technique that dynamically adjusts the rank of each layer during training, guided by a hierarchical group-lasso penalty. This approach allows for a more efficient and effective training process compared to traditional methods. The paper provides theoretical insights into the properties of Maestro, including its connection to singular value decomposition (SVD) and principal component analysis (PCA). Empirical results demonstrate that Maestro achieves competitive or superior performance compared to existing methods on various datasets and architectures.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow. The authors clearly explain the motivation behind Maestro and provide a detailed description of the method, including the progressive shrinking and hierarchical group-lasso penalty.
2. The theoretical analysis is thorough and provides valuable insights into the properties of Maestro. The authors demonstrate that Maestro can recover SVD and PCA under certain conditions, which adds theoretical rigor to the paper.
3. The empirical results are comprehensive and demonstrate the effectiveness of Maestro on various datasets and architectures. The authors compare Maestro to several existing methods and show that it achieves competitive or superior performance.

### Weaknesses

#### Some Related Works


#### comment

1. While the paper demonstrates the effectiveness of Maestro on various datasets and architectures, it would be beneficial to include experiments on more complex and challenging datasets, such as those with higher dimensionality or more complex data distributions. This would provide a more comprehensive evaluation of the method's performance and generalizability.
2. The paper does not provide a detailed analysis of the sensitivity of Maestro to different hyperparameters, such as the learning rate, batch size, and the rank of the low-rank approximation. A sensitivity analysis would help to understand the robustness of the method and provide guidance on how to choose the optimal hyperparameters for different datasets and architectures.
3. The paper does not discuss the limitations of Maestro or potential failure cases. It would be helpful to provide a discussion of the scenarios where Maestro may not perform well, such as when the data distribution is highly non-linear or when the optimal rank is not well-defined. This would provide a more balanced view of the method's capabilities and limitations.

### Suggestions

The authors should consider expanding their experimental evaluation to include more complex datasets, such as those with higher dimensionality or more intricate data distributions. For instance, evaluating Maestro on datasets used in natural language processing or time-series analysis could provide a more comprehensive understanding of its performance in diverse scenarios. This would involve not only testing on larger datasets but also analyzing the computational cost and memory requirements of Maestro on these more challenging tasks. Furthermore, it would be beneficial to explore the performance of Maestro on datasets with varying degrees of non-linearity to understand its robustness under different conditions. Such experiments would provide a more thorough assessment of the method's generalizability and applicability to real-world problems.

To address the lack of hyperparameter sensitivity analysis, the authors should conduct a systematic study of how different hyperparameters affect the performance of Maestro. This should include a detailed exploration of the impact of the learning rate, batch size, and the rank of the low-rank approximation. For example, the authors could perform a grid search over a range of values for each hyperparameter and report the performance of Maestro on different datasets. This analysis should not only focus on the final performance but also on the convergence speed and stability of the training process. The results of this sensitivity analysis should be presented in a clear and concise manner, possibly using visualizations such as heatmaps or line plots. This would provide valuable insights into the robustness of Maestro and help practitioners choose appropriate hyperparameters for their specific tasks.

Finally, the authors should include a discussion of the limitations of Maestro and potential failure cases. This should involve identifying scenarios where Maestro may not perform well, such as when the data distribution is highly non-linear or when the optimal rank is not well-defined. For example, the authors could analyze the performance of Maestro on datasets with complex non-linear relationships or explore the behavior of Maestro when the optimal rank varies significantly across different layers. This discussion should also include an analysis of the computational cost and memory requirements of Maestro in these challenging scenarios. By acknowledging the limitations of Maestro, the authors can provide a more balanced and realistic assessment of its capabilities and limitations, which would be valuable for future research and practical applications.

### Questions

1. How does Maestro handle the case where the optimal rank is not well-defined or when the data distribution is highly non-linear?
2. What are the potential limitations of Maestro in terms of scalability to larger models and datasets?
3. How does the choice of hyperparameters affect the performance of Maestro, and what are the guidelines for selecting the optimal hyperparameters for different datasets and architectures?

### Rating

8

### Confidence

4

**********
