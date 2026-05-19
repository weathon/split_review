### Summary

This paper introduces Wanda, a pruning method for large language models (LLMs) that does not require retraining or weight updates. Wanda uses a simple pruning metric that combines weight magnitude with input activation norms, pruning weights with the smallest product. The method is evaluated on LLaMA and LLaMA-2 models across various sparsity levels and tasks, showing competitive performance compared to SparseGPT and other baselines. The authors also demonstrate that Wanda can be applied to structured sparsity, yielding similar results to SparseGPT.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. Wanda is a simple and effective pruning method that achieves competitive results without requiring retraining or weight updates. This makes it a practical solution for pruning large language models.
2. The paper provides a thorough evaluation of Wanda on LLaMA and LLaMA-2 models, demonstrating its effectiveness across various sparsity levels and tasks. The authors also compare Wanda to other baselines, including SparseGPT, showing that it performs competitively.
3. The paper is well-written and easy to follow, with clear explanations of the proposed method and experimental setup.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost of Wanda, especially in comparison to other pruning methods. While the authors mention that Wanda is faster than SparseGPT, they do not provide a detailed breakdown of the time and memory requirements for each step of the pruning process. This makes it difficult to assess the practical applicability of Wanda in resource-constrained environments.
2. The paper does not explore the impact of different hyperparameters on the performance of Wanda. While the authors mention that Wanda is robust to hyperparameter choices, they do not provide a detailed analysis of how different hyperparameters affect the pruning results. This makes it difficult to optimize Wanda for specific tasks or models.
3. The paper does not discuss the limitations of Wanda or potential areas for improvement. While the authors acknowledge that Wanda is not a perfect solution, they do not provide a detailed discussion of the scenarios where Wanda may fail or underperform. This makes it difficult to assess the generalizability of Wanda and its potential for future research.

### Suggestions

The authors should provide a more detailed analysis of the computational cost of Wanda, including a breakdown of the time and memory requirements for each step of the pruning process. This analysis should be compared to other pruning methods, such as SparseGPT, to provide a clear understanding of the trade-offs between computational cost and performance. Specifically, the authors should report the time required for the pruning metric calculation, the sorting of weights, and the actual pruning operation. This would allow readers to assess the practical applicability of Wanda in resource-constrained environments. Furthermore, the authors should investigate the impact of different hardware configurations on the computational cost of Wanda, as this may affect its performance in different settings. This analysis should include the impact of different memory architectures and processor speeds on the pruning process.

In addition, the authors should conduct a more thorough analysis of the impact of different hyperparameters on the performance of Wanda. While the authors mention that Wanda is robust to hyperparameter choices, they should provide a detailed analysis of how different hyperparameters affect the pruning results. This analysis should include a sensitivity analysis of the hyperparameters, showing how changes in these parameters affect the performance of Wanda. The authors should also provide guidelines for selecting appropriate hyperparameters for specific tasks or models. This would allow readers to optimize Wanda for their specific use cases. For example, the authors could investigate the impact of different sparsity levels on the performance of Wanda, as well as the impact of different pruning strategies, such as magnitude-based pruning or gradient-based pruning.

Finally, the authors should provide a more detailed discussion of the limitations of Wanda and potential areas for improvement. This discussion should include scenarios where Wanda may fail or underperform, as well as potential areas for future research. For example, the authors could investigate the impact of different model architectures on the performance of Wanda, as well as the impact of different training datasets on the performance of Wanda. The authors should also discuss the potential limitations of Wanda in terms of its ability to preserve the performance of the original model. This would allow readers to assess the generalizability of Wanda and its potential for future research. Furthermore, the authors should discuss the potential for combining Wanda with other pruning techniques to achieve better performance.

### Questions

1. How does the computational cost of Wanda compare to other pruning methods, such as SparseGPT, in terms of time and memory requirements?
2. What is the impact of different hyperparameters on the performance of Wanda, and how can they be optimized for specific tasks or models?
3. What are the limitations of Wanda, and what are the potential areas for improvement in future research?

### Rating

5

### Confidence

4

**********
