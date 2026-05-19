### Summary

This paper presents a systematic evaluation framework for assessing tabular data synthesis algorithms. The authors propose a new fidelity metric based on the Wasserstein distance, a new privacy metric based on membership disclosure score, and a new utility metric based on machine learning affinity. The authors conduct extensive experiments to evaluate 8 different synthesizers across 12 datasets and provide insights into the strengths and weaknesses of different types of synthesizers.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The paper is well-written and easy to follow.
- The proposed metrics are intuitive and reasonable.
- The experimental results provide valuable insights into the performance of different synthesizers.
- The proposed framework can be used to evaluate other synthesizers beyond the ones tested in the paper.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed metrics are not novel, as the Wasserstein distance and membership disclosure score are widely used in the literature.
- The paper does not provide a clear justification for why the Wasserstein distance is a better fidelity metric than other existing metrics, such as total variation distance or KL divergence. The authors should provide a more detailed analysis of the properties of the Wasserstein distance and how it addresses the limitations of other metrics in the context of tabular data synthesis.
- The paper does not provide a clear justification for why the membership disclosure score is a better privacy metric than other existing metrics, such as differential privacy or Rényi differential privacy. The authors should provide a more detailed analysis of the properties of the membership disclosure score and how it addresses the limitations of other metrics in the context of tabular data synthesis.
- The paper does not provide a clear justification for why the machine learning affinity score is a better utility metric than other existing metrics, such as classification accuracy or F1 score. The authors should provide a more detailed analysis of the properties of the machine learning affinity score and how it addresses the limitations of other metrics in the context of tabular data synthesis.
- The paper does not provide a clear explanation of how the proposed metrics are computed in practice. The authors should provide more details on the implementation of the proposed metrics and how they are used in the evaluation framework.

### Suggestions

The paper would benefit from a more thorough justification of the chosen metrics. While Wasserstein distance, membership disclosure score, and machine learning affinity are established metrics, the paper needs to articulate why they are particularly suitable for evaluating tabular data synthesis algorithms compared to other alternatives. For instance, the authors should discuss the specific properties of these metrics that make them appropriate for capturing fidelity, privacy, and utility in the context of tabular data. A detailed comparison with other commonly used metrics, such as total variation distance, KL divergence for fidelity; differential privacy, Rényi differential privacy for privacy; and classification accuracy, F1 score for utility, would strengthen the paper. This comparison should not only highlight the advantages of the proposed metrics but also acknowledge their limitations and how they address specific challenges in tabular data synthesis. Furthermore, the authors should provide a more in-depth analysis of the computational complexity of each metric and discuss the practical implications of these complexities for large-scale datasets.

To improve the clarity of the paper, the authors should provide a more detailed explanation of how the proposed metrics are computed in practice. This should include a step-by-step description of the algorithms used to calculate the Wasserstein distance, membership disclosure score, and machine learning affinity. For example, the authors should specify how the optimal transport plan is computed for the Wasserstein distance, how the membership disclosure score is calculated for different types of synthesizers, and how the machine learning affinity score is computed for different types of machine learning models. The authors should also discuss the practical challenges of implementing these metrics, such as the computational cost of calculating the Wasserstein distance for high-dimensional data and the sensitivity of the membership disclosure score to the choice of the training data. Providing concrete examples of how these metrics are applied to different types of tabular data would also enhance the paper's clarity and practical value.

Finally, the paper should include a more comprehensive experimental evaluation of the proposed metrics. While the paper presents results for 8 different synthesizers across 12 datasets, it would be beneficial to include a more detailed analysis of the sensitivity of the proposed metrics to different parameters and settings. For example, the authors should investigate how the Wasserstein distance is affected by the choice of the transport plan and how the membership disclosure score is affected by the choice of the training data. The authors should also compare the performance of the proposed metrics with other existing metrics on a wider range of datasets and synthesizers. This would provide a more robust evaluation of the proposed metrics and demonstrate their practical utility. Furthermore, the authors should discuss the limitations of the proposed metrics and identify areas for future research.

### Questions

- How do the proposed metrics compare to other existing metrics in terms of computational complexity and practical implementation?
- What are the limitations of the proposed metrics, and how can they be addressed in future work?

### Rating

5

### Confidence

3

**********
