### Summary

This paper introduces an adaptive model merging approach called AdaMerging for multi-task learning (MTL). The method aims to improve the merging of multiple models, each fine-tuned for different tasks, into a single model without requiring the original training data. AdaMerging learns the merging coefficients in a task-wise or layer-wise manner using entropy minimization on unlabeled test samples as a surrogate objective function. The paper demonstrates that AdaMerging achieves significant performance improvements over existing task vector-based model merging methods, showing better generalization and robustness to distribution shifts.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces an innovative approach to model merging in multi-task learning by adaptively learning the merging coefficients. This is a novel contribution that addresses a key limitation in existing task vector-based methods, which rely on fixed merging coefficients.

2. The use of entropy minimization on unlabeled test samples as a surrogate objective function for optimizing the merging coefficients is an interesting and practical idea. This allows the method to be applied in scenarios where the original training data is not available, which is a common challenge in real-world applications.

3. The paper provides a thorough experimental evaluation of the proposed method across multiple tasks and model architectures. The results demonstrate significant improvements in performance, generalization, and robustness compared to existing methods.

### Weaknesses

#### Some Related Works


#### comment

1. The paper primarily focuses on classification tasks. It would be beneficial to explore the applicability of AdaMerging to other types of tasks, such as regression or tasks with structured outputs. The current evaluation does not provide sufficient evidence to claim the method's general applicability across diverse task types. For instance, how would the entropy minimization objective function translate to a regression setting where the output is continuous rather than discrete? The paper lacks a discussion on the potential modifications or alternative objectives that might be needed for such tasks.

2. The method relies on unlabeled test samples from the multi-task setup. The paper does not discuss the sensitivity of the method to the number of unlabeled samples used for optimization. It is unclear how the performance of AdaMerging would be affected by using a very small number of unlabeled samples, or if there is a point of diminishing returns with increasing sample size. A more detailed analysis of this aspect is needed to understand the practical limitations of the approach.

3. While the paper demonstrates improved performance, it does not provide a detailed analysis of the computational overhead of the proposed method compared to existing approaches. The process of iteratively updating merging coefficients using entropy minimization could introduce significant computational costs, especially when dealing with large models or datasets. The paper should include a quantitative comparison of the training time and memory requirements of AdaMerging with other model merging techniques.

### Suggestions

To strengthen the paper, the authors should investigate the performance of AdaMerging on a wider range of tasks beyond classification. Specifically, they should explore how the method can be adapted for regression tasks, which are common in many real-world applications. This could involve exploring alternative objective functions to entropy minimization, such as minimizing the variance of the predictions or using a pseudo-labeling approach. The authors should also provide a detailed analysis of the performance of AdaMerging on tasks with structured outputs, such as sequence-to-sequence tasks or tasks involving graph structures. This would provide a more comprehensive understanding of the method's generalizability and applicability.

Furthermore, the authors should conduct a thorough sensitivity analysis of the method's performance with respect to the number of unlabeled test samples used for optimization. This analysis should include experiments with varying numbers of unlabeled samples, ranging from very small to large, to determine the optimal number of samples needed to achieve good performance. The authors should also investigate the impact of the quality of the unlabeled samples on the method's performance. For example, how does the performance of AdaMerging change if the unlabeled samples are noisy or do not accurately represent the test distribution? This analysis would provide valuable insights into the practical limitations of the approach and help guide the selection of unlabeled samples in real-world scenarios.

Finally, the authors should provide a detailed analysis of the computational overhead of AdaMerging. This analysis should include a comparison of the training time and memory requirements of AdaMerging with other model merging techniques. The authors should also investigate the scalability of the method to large models and datasets. This could involve exploring techniques to reduce the computational cost of the iterative coefficient updates, such as using stochastic gradient descent or other optimization algorithms. The authors should also provide a discussion of the trade-offs between performance and computational cost, to help practitioners make informed decisions about the use of AdaMerging in different scenarios.

### Questions

1. How sensitive is the performance of AdaMerging to the number of unlabeled test samples used for optimization? Is there a minimum number of samples required to achieve good performance?

2. How does the computational overhead of AdaMerging compare to existing model merging approaches? What is the impact of the iterative coefficient updates on the overall training time?

3. Can the proposed method be extended to other types of tasks beyond classification, such as regression or tasks with structured outputs? What modifications would be needed to adapt the method to these tasks?

### Rating

6

### Confidence

4

**********
