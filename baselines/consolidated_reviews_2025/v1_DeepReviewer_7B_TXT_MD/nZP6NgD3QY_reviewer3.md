### Summary

This paper introduces AdaMerging, an innovative technique for merging pre-trained models across multiple tasks without needing the original training data. The method employs entropy minimization to adaptively determine the merging coefficients for task vectors, allowing for effective multi-task learning. The authors demonstrate the effectiveness of AdaMerging through extensive experiments, showing improvements in performance, generalization, and robustness compared to existing task vector-based methods.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The proposed method is well-motivated and addresses a significant challenge in multi-task learning: the requirement for original training data.
2. The experimental results are comprehensive and demonstrate the effectiveness of AdaMerging in various scenarios.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost associated with AdaMerging, particularly in comparison to other methods. Specifically, the paper lacks a breakdown of the time spent on entropy calculation, gradient computation, and model merging, making it difficult to assess the practical overhead of the proposed method. A comparison of training time and memory usage with baseline methods would be beneficial.
2. The paper does not explore the sensitivity of AdaMerging to different hyperparameter settings, such as the learning rate and the number of iterations used for entropy minimization. It is unclear how the performance of AdaMerging is affected by these choices, and the paper should include a sensitivity analysis to demonstrate the robustness of the method. For example, how does the performance change with different learning rates for the entropy minimization process, or with varying numbers of iterations?
3. The paper does not provide a comprehensive comparison with other state-of-the-art multi-task learning methods. While the paper compares AdaMerging with some existing methods, it would be beneficial to include a broader range of baselines, especially those that do not rely on task vectors, to better contextualize the performance of AdaMerging. This would help to understand the specific advantages and limitations of the proposed approach compared to alternative multi-task learning strategies.

### Suggestions

To strengthen the paper, the authors should provide a more detailed analysis of the computational cost of AdaMerging. This should include a breakdown of the time spent on each step of the algorithm, such as entropy calculation, gradient computation, and model merging. A comparison of these costs with baseline methods would be crucial to understand the practical implications of using AdaMerging. Furthermore, the authors should investigate the sensitivity of AdaMerging to different hyperparameter settings. This should include a systematic evaluation of how the performance of AdaMerging changes with different learning rates and numbers of iterations for the entropy minimization process. The authors should also explore the impact of other hyperparameters, such as the batch size and the number of epochs used for training. This analysis would help to demonstrate the robustness of the method and provide practical guidance for users.

In addition to the computational and sensitivity analyses, the authors should expand the comparison with other state-of-the-art multi-task learning methods. This should include a broader range of baselines, especially those that do not rely on task vectors, to better contextualize the performance of AdaMerging. For example, the authors could compare AdaMerging with methods that use parameter sharing or knowledge distillation. This would help to understand the specific advantages and limitations of the proposed approach compared to alternative multi-task learning strategies. The authors should also discuss the limitations of AdaMerging and identify areas for future research. This would provide a more balanced and comprehensive view of the proposed method.

Finally, the authors should provide more details on the implementation of AdaMerging. This should include a description of the specific optimization algorithm used for entropy minimization, as well as the details of the model merging process. The authors should also provide a clear explanation of how the merging coefficients are determined and how they affect the performance of the merged model. This would help to make the method more reproducible and easier to understand for other researchers. The authors should also discuss the potential limitations of the method and suggest directions for future research.

### Questions

1. How does the computational cost of AdaMerging compare to other multi-task learning methods?
2. How sensitive is AdaMerging to different hyperparameter settings, such as the learning rate and the number of iterations used for entropy minimization?
3. How does AdaMerging perform compared to other state-of-the-art multi-task learning methods that do not rely on task vectors?

### Rating

6

### Confidence

4

**********
