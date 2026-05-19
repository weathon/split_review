### Summary

This paper presents a systematic evaluation framework for assessing tabular data synthesis algorithms. The authors examine and critique existing evaluation metrics, and introduce a set of new metrics in terms of fidelity, privacy, and utility to address their limitations. Based on the proposed metrics, they also devise a unified objective for tuning, which can consistently improve the quality of synthetic data for all methods. The paper conducts extensive evaluations of 8 different types of synthesizers on 12 real-world datasets and identified some interesting findings, which offer new directions for privacy-preserving data synthesis.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow. The authors provide a comprehensive review of existing evaluation metrics and clearly articulate the limitations of these metrics. The proposed metrics are well-defined and justified, and the authors provide a clear explanation of how they address the limitations of existing metrics.

2. The paper presents a unified tuning objective that can consistently improve the quality of synthetic data for all methods. This is a significant contribution, as it provides a practical approach for improving the performance of data synthesis algorithms.

3. The paper conducts extensive evaluations of 8 different types of synthesizers on 12 real-world datasets. The results are presented in a clear and concise manner, and the authors provide a detailed analysis of the findings.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational complexity of the proposed metrics and framework. It would be helpful to understand the scalability of the approach, especially when dealing with large-scale datasets.

2. The proposed framework requires a careful selection of hyperparameters, which may not be straightforward in practice. The paper could provide more guidance on how to choose appropriate hyperparameter values for different datasets and applications.

### Suggestions

The paper should include a more thorough discussion of the computational complexity of the proposed metrics and framework. Specifically, the authors should analyze how the runtime of their methods scales with the number of rows and columns in the input datasets. For instance, the Wasserstein distance calculation, which is a core component of the fidelity metric, can be computationally expensive, especially for high-dimensional data. A detailed analysis of the time complexity of this step, along with other computationally intensive parts of the framework, would be beneficial. Furthermore, the authors should provide empirical results on the runtime of their framework for datasets of varying sizes to demonstrate its scalability in practice. This would help readers understand the practical limitations of the proposed approach and identify potential bottlenecks.

Regarding hyperparameter selection, the paper should provide more practical guidance on how to choose appropriate values for different datasets and applications. While the authors mention using Optuna for hyperparameter optimization, they do not provide specific recommendations for setting the search space or the optimization strategy. It would be helpful to include a discussion on how the choice of hyperparameters affects the trade-off between fidelity, privacy, and utility. For example, how does the privacy parameter epsilon in differentially private synthesizers affect the fidelity and utility of the synthetic data? The authors could also provide guidelines on how to adapt the hyperparameter selection process to different types of tabular data, such as data with varying degrees of skewness or cardinality. This would make the framework more accessible and useful for practitioners.

Finally, the paper could benefit from a more detailed discussion of the limitations of the proposed framework. For example, how does the framework perform when dealing with datasets that have a large number of missing values or outliers? Are there any specific types of data or synthesizers for which the proposed metrics are not well-suited? Addressing these limitations would provide a more complete picture of the strengths and weaknesses of the proposed approach and help guide future research in this area.

### Questions

Please refer to the weaknesses.

### Rating

6

### Confidence

3

**********
