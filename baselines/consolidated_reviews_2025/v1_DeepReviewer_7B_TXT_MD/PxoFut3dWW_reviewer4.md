### Summary

This paper introduces Wanda, a simple yet effective pruning method for large language models (LLMs) that does not require retraining or weight updates. Wanda uses a pruning metric that combines weight magnitude with input activation norms, allowing it to prune weights with the smallest product of magnitude and norm. The authors demonstrate that Wanda achieves competitive performance compared to existing methods, such as SparseGPT, on LLaMA and LLaMA-2 models across various sparsity levels and tasks. The method is computationally efficient and can be applied to both unstructured and structured pruning scenarios.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow. The authors provide a clear explanation of the proposed method and its motivation, making it accessible to a wide audience.
2. The proposed method is simple and effective. Wanda is easy to implement and does not require retraining or weight updates, making it a practical solution for pruning large language models.
3. The authors conduct extensive experiments on LLaMA and LLaMA-2 models, demonstrating the effectiveness of Wanda across various sparsity levels and tasks. The results show that Wanda achieves competitive performance compared to existing methods, such as SparseGPT.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the computational cost of Wanda, especially in comparison to other pruning methods. While the authors mention that Wanda is faster than SparseGPT, they do not provide a detailed breakdown of the time and memory requirements for each step of the pruning process. This makes it difficult to assess the practical applicability of Wanda in resource-constrained environments.
2. The paper does not explore the impact of different hyperparameters on the performance of Wanda. While the authors mention that Wanda is robust to hyperparameter choices, they do not provide a detailed analysis of how different hyperparameters affect the pruning results. This makes it difficult to optimize Wanda for specific tasks or models.
3. The paper does not discuss the limitations of Wanda or potential areas for improvement. While the authors acknowledge that Wanda is not a perfect solution, they do not provide a detailed discussion of the scenarios where Wanda may fail or underperform. This makes it difficult to assess the generalizability of Wanda and its potential for future research.

### Suggestions

The authors should provide a more thorough analysis of the computational cost of Wanda, including a detailed breakdown of the time and memory requirements for each step of the pruning process. This analysis should be compared to other pruning methods, such as SparseGPT, to provide a clear understanding of the trade-offs between computational cost and performance. Specifically, the authors should report the time required for the pruning metric calculation, the sorting of weights, and the actual pruning operation. This would allow readers to assess the practical applicability of Wanda in resource-constrained environments. Furthermore, the authors should investigate the impact of different hardware configurations on the computational cost of Wanda, as this may affect its performance in different settings. This analysis should include the impact of different memory architectures and processor speeds on the pruning process.

In addition, the authors should conduct a more thorough analysis of the impact of different hyperparameters on the performance of Wanda. While the authors mention that Wanda is robust to hyperparameter choices, they should provide a detailed analysis of how different hyperparameters affect the pruning results. This analysis should include a sensitivity analysis of the hyperparameters, showing how changes in these parameters affect the performance of Wanda. The authors should also provide guidelines for selecting appropriate hyperparameters for specific tasks or models. For example, the authors could investigate the impact of different sparsity levels on the performance of Wanda, as well as the impact of different pruning strategies, such as magnitude-based pruning or gradient-based pruning. This would allow readers to optimize Wanda for their specific use cases.

Finally, the authors should provide a more detailed discussion of the limitations of Wanda and potential areas for improvement. This discussion should include scenarios where Wanda may fail or underperform, as well as potential areas for future research. For example, the authors could investigate the impact of different model architectures on the performance of Wanda, as well as the impact of different training datasets on the performance of Wanda. The authors should also discuss the potential limitations of Wanda in terms of its ability to preserve the performance of the original model. This would allow readers to assess the generalizability of Wanda and its potential for future research. Furthermore, the authors should discuss the potential for combining Wanda with other pruning techniques to achieve better performance.

### Questions

1. How does the computational cost of Wanda compare to other pruning methods, such as SparseGPT, in terms of time and memory requirements?
2. What is the impact of different hyperparameters on the performance of Wanda, and how can they be optimized for specific tasks or models?
3. What are the limitations of Wanda, and what are the potential areas for improvement in future research?

### Rating

6

### Confidence

3

**********
