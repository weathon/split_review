### Summary

This paper presents a systematic evaluation framework for assessing tabular data synthesis algorithms, addressing the limitations of existing evaluation metrics. The authors introduce new metrics for fidelity, privacy, and utility, and conduct extensive evaluations of various synthesizers on real-world datasets. The findings provide insights into the strengths and weaknesses of different approaches and offer guidance for privacy-preserving data synthesis.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

The paper introduces a novel framework for evaluating tabular data synthesis algorithms, addressing the limitations of existing evaluation metrics. The proposed metrics provide a more comprehensive assessment of fidelity, privacy, and utility.

The authors conduct extensive evaluations on a variety of real-world datasets, which enhances the credibility and applicability of their findings.

### Weaknesses

#### Some Related Works


#### comment

The paper does not provide a detailed analysis of the computational complexity of the proposed metrics and framework. It would be helpful to understand the scalability of the approach, especially when dealing with large-scale datasets. Specifically, the paper lacks a discussion on how the computational cost of the proposed metrics scales with the number of rows and columns in the dataset, which is crucial for assessing its applicability to real-world scenarios. Furthermore, the paper does not analyze the time complexity of the individual steps in the proposed framework, such as data preprocessing, model training, and metric calculation, making it difficult to pinpoint potential bottlenecks.

The proposed framework requires a careful selection of hyperparameters, which may not be straightforward in practice. The paper could provide more guidance on how to choose appropriate hyperparameter values for different datasets and applications. For example, the paper does not discuss how the choice of hyperparameters affects the trade-off between fidelity, privacy, and utility, which is a critical consideration in practical applications. Additionally, the paper does not provide any guidelines on how to adapt the hyperparameter selection process to different types of tabular data, such as data with varying degrees of skewness or cardinality.

### Suggestions

To address the lack of computational complexity analysis, the authors should include a detailed discussion on how the proposed metrics scale with the size of the dataset, both in terms of the number of rows and columns. This should include a breakdown of the time complexity of each step in the framework, such as data preprocessing, model training, and metric calculation. The authors should also provide empirical results on the runtime of the framework for datasets of varying sizes to demonstrate its scalability. Furthermore, it would be beneficial to discuss the memory requirements of the framework, especially when dealing with large datasets. This analysis should also consider the impact of different data types (e.g., numerical, categorical) on the computational cost. For example, the authors could analyze how the computation of the Wasserstein distance, a key component of their fidelity metric, scales with the number of rows and the dimensionality of the data. This would provide a more complete picture of the framework's computational overhead.

Regarding hyperparameter selection, the authors should provide more practical guidance on how to choose appropriate values for different datasets and applications. This should include a discussion on how the choice of hyperparameters affects the trade-off between fidelity, privacy, and utility. For example, the authors could analyze how the privacy parameter ε in differentially private synthesizers affects the fidelity and utility of the synthetic data. The authors should also provide guidelines on how to adapt the hyperparameter selection process to different types of tabular data, such as data with varying degrees of skewness or cardinality. This could involve providing a set of heuristics or rules of thumb that practitioners can use to guide their hyperparameter selection process. Furthermore, the authors could explore the use of automated hyperparameter tuning techniques, such as grid search or Bayesian optimization, to simplify the process for practitioners.

Finally, the authors should consider providing a sensitivity analysis of the proposed metrics with respect to the hyperparameters. This would help practitioners understand how changes in the hyperparameter values affect the evaluation results. For example, the authors could analyze how the fidelity metric changes when the privacy parameter ε is varied. This would provide a more complete understanding of the robustness of the proposed framework and its sensitivity to hyperparameter choices. This analysis should also include a discussion of the limitations of the proposed framework and potential areas for future research. For example, the authors could discuss the challenges of applying the framework to very high-dimensional data or data with complex dependencies.

### Questions

See weaknesses

### Rating

6

### Confidence

3

**********
