### Summary

This paper proposes a new model merging method called AdaMerging, which adaptively learns the coefficients for model merging without requiring the original training data. The method optimizes the merging coefficients by minimizing the entropy of the prediction loss on unlabeled test samples from the multi-task setup. Extensive experiments show that AdaMerging outperforms existing task vector-based merging methods in multi-task learning, generalization, and robustness.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. This paper proposes a new model merging method called AdaMerging, which adaptively learns the coefficients for model merging without requiring the original training data.
2. Extensive experiments show that AdaMerging outperforms existing task vector-based merging methods in multi-task learning, generalization, and robustness.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost associated with AdaMerging, particularly in comparison to other methods. Specifically, the paper lacks a breakdown of the time spent on entropy calculation, gradient computation, and model merging, making it difficult to assess the practical overhead of the proposed method. A comparison of training time and memory usage with baseline methods would be beneficial.
2. The paper does not explore the sensitivity of AdaMerging to different hyperparameter settings, such as the learning rate and the number of iterations used for entropy minimization. It is unclear how the performance of AdaMerging is affected by these choices, and the paper should include a sensitivity analysis to demonstrate the robustness of the method. For example, how does the performance change with different learning rates for the entropy minimization process, or with varying numbers of iterations?
3. The paper does not provide a comprehensive comparison with other state-of-the-art multi-task learning methods. While the paper compares AdaMerging with some existing methods, it would be beneficial to include a broader range of baselines, especially those that do not rely on task vectors, to better contextualize the performance of AdaMerging. This would help to understand the specific advantages and limitations of the proposed approach compared to alternative multi-task learning strategies.

### Suggestions

The paper would benefit from a more thorough analysis of the computational cost of AdaMerging. The authors should provide a detailed breakdown of the time spent on each step of the algorithm, including entropy calculation, gradient computation, and model merging. This analysis should be compared against the computational cost of baseline methods to provide a clear understanding of the overhead introduced by AdaMerging. Furthermore, the authors should investigate the memory footprint of the method, especially when dealing with large models and datasets. This would allow readers to assess the practical applicability of the proposed method in resource-constrained environments. A comparison of training time and memory usage with baseline methods would be crucial to understand the practical implications of using AdaMerging.

To address the lack of sensitivity analysis, the authors should conduct a systematic evaluation of AdaMerging's performance under different hyperparameter settings. Specifically, the impact of the learning rate and the number of iterations used for entropy minimization should be investigated. The authors should explore a range of learning rates and iteration counts, and report the corresponding performance of AdaMerging. This analysis should include a discussion of how these hyperparameters affect the convergence and stability of the method. Additionally, the authors should consider other hyperparameters that may affect the performance of AdaMerging, such as the batch size and the number of epochs used for training. This would provide a more comprehensive understanding of the robustness of the method and its sensitivity to different parameter settings.

Finally, the paper should include a more comprehensive comparison with other state-of-the-art multi-task learning methods. While the paper compares AdaMerging with some existing methods, it would be beneficial to include a broader range of baselines, especially those that do not rely on task vectors. This would help to better contextualize the performance of AdaMerging and highlight its specific advantages and limitations. The authors should consider including methods that use different approaches to multi-task learning, such as parameter sharing, knowledge distillation, or meta-learning. This would provide a more complete picture of the current state-of-the-art and allow readers to better understand the contribution of AdaMerging. The comparison should also include a discussion of the computational cost and memory requirements of the different methods.

### Questions

Please see the weaknesses.

### Rating

6

### Confidence

4

**********
