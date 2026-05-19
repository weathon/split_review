### Summary

This paper proposes an adaptive model merging approach for multi-task learning. Building upon the concept of "task vector" from previous work, the authors introduce learnable coefficients for each task vector, which can be optimized using a few unlabeled test samples through entropy minimization. This section requires further clarification. The authors conduct experiments on various datasets and demonstrate that their proposed methods outperform previous model merging approaches.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The experiments are comprehensive, and the results demonstrate significant improvements over previous model merging methods.

### Weaknesses

#### Some Related Works

[1] Task Arithmetic with Optimal Transport

#### comment

1. The primary contribution of this paper is the introduction of learnable coefficients for each task vector. As highlighted in the introduction, the challenge lies in optimizing these coefficients without access to the original training data. While the authors propose using a few unlabeled test samples and entropy minimization, this approach appears unusual. In the traditional evaluation setting, the test set should be kept separate until the final evaluation to avoid overfitting. By using the test set for optimization, the authors introduce a potential risk of overfitting to the test data. Additionally, the intuition behind minimizing entropy on unlabeled test samples is not entirely clear. While the authors draw inspiration from test-time adaptation (TTA) literature, the connection between TTA and model merging remains unclear. In TTA, the model weights are updated, whereas in this work, only the coefficients for task vectors are optimized. More detailed explanations and justifications are needed to clarify this aspect.
2. The authors propose two methods for optimizing coefficients: task-wise and layer-wise. However, the layer-wise approach seems to have a significantly better performance. It would be beneficial to explore additional techniques to enhance the task-wise method or provide an analysis explaining why the layer-wise approach is superior to the task-wise one.
3. The paper lacks a discussion of some recent related work, such as [A], which also addresses the issue of optimal coefficients. Although [A] requires the training data for each task, it would be valuable to include a discussion of this work.
4. In the baselines, the authors mention that the "Traditional MTL" approach fine-tunes the ViT model. It would be helpful to clarify whether this approach uses joint training or sequential training.
5. In Table 1, the authors do not include the performance of the pre-trained model. It would be beneficial to add this information to provide a baseline for comparison.

### Suggestions

The core weakness of this paper lies in its optimization strategy, which uses unlabeled test samples to learn merging coefficients. While the authors draw parallels to test-time adaptation (TTA), the fundamental difference between adapting model weights in TTA and adapting merging coefficients here is significant. In TTA, the model is adapted to the test distribution by directly modifying its parameters, often using techniques like gradient descent on the test data. This is typically done when the test data distribution is known to be different from the training distribution. However, in the context of model merging, the goal is to create a single model that performs well across multiple tasks, and the test data should ideally represent the target distribution for this multi-task model. Using the test data to optimize the merging coefficients introduces a risk of overfitting to the specific characteristics of the test set, which may not generalize well to unseen data. The authors should clarify the specific conditions under which this optimization strategy is beneficial and provide a more detailed analysis of the potential for overfitting. Furthermore, the intuition behind minimizing entropy on unlabeled test samples needs further elaboration. While a negative correlation between entropy and loss is observed, this does not automatically justify entropy minimization as a proxy for loss minimization. The authors should provide a more rigorous justification for this choice, perhaps by exploring the theoretical connections between entropy and generalization performance in the context of multi-task learning.

To address the performance gap between task-wise and layer-wise merging, the authors should investigate the underlying reasons for the superiority of the layer-wise approach. One possible explanation is that different layers in a neural network learn different levels of features, and allowing for layer-specific merging coefficients enables a more fine-grained control over the transfer of knowledge between tasks. For example, earlier layers might learn more general features that are shared across tasks, while later layers might learn more task-specific features. The task-wise approach, which uses a single coefficient for the entire task vector, might be too restrictive to capture this complexity. The authors could explore techniques to improve the task-wise method, such as using a hierarchical structure or incorporating some form of attention mechanism to weigh different parts of the task vector. Additionally, the authors should provide a more detailed analysis of the learned coefficients, including how they vary across different tasks and layers, and how they relate to the performance of the merged model. This analysis could provide valuable insights into the effectiveness of the proposed methods.

Finally, the paper would benefit from a more thorough discussion of related work, particularly those that address the issue of optimal coefficients for model merging. While the authors mention that some methods search for the optimal coefficients in the task vector space, they do not provide a detailed comparison of their approach with these methods. Specifically, the authors should discuss the advantages and disadvantages of their entropy minimization approach compared to other optimization techniques, such as grid search or Bayesian optimization. Furthermore, the authors should clarify the details of the "Traditional MTL" baseline, including whether it uses joint or sequential training, and provide the performance of the pre-trained model in Table 1. These details are crucial for a fair comparison with the proposed methods. The authors should also discuss the limitations of their approach, such as the potential for overfitting to the test data and the computational cost of optimizing the merging coefficients.

### Questions

Please refer to the weaknesses section.

### Rating

5

### Confidence

4

**********
