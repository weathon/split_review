### Summary

This paper proposes a novel method for fine-tuning vision-language models to enhance their generalization in few-shot learning scenarios. The authors introduce a consistency-guided approach that enforces alignment between the trainable and pre-trained models to prevent overfitting. The method incorporates adapters and prompts to further regularize the model and improve generalization. The authors demonstrate the effectiveness of their approach through extensive experiments on various datasets, showing state-of-the-art performance in base-to-novel generalization, cross-dataset evaluation, and domain generalization.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow. The authors provide a clear motivation for their approach and explain the technical details of their method in a straightforward manner.
2. The authors conduct extensive experiments on multiple datasets and tasks, demonstrating the effectiveness of their approach. The results show that the proposed method achieves state-of-the-art performance in various evaluation scenarios.
3. The authors provide a thorough ablation study to analyze the contribution of each component of their method. This helps to understand the importance of each component and provides insights into the design choices.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method introduces additional complexity compared to existing approaches, which may limit its practical applicability. Specifically, the introduction of adapters and prompts, while beneficial for generalization, adds more parameters and computational overhead during training and inference. This increased complexity could make it more challenging to deploy the model in resource-constrained environments or with limited computational resources. A more detailed analysis of the computational cost, including training time and memory usage, would be beneficial.
2. The paper does not provide a clear explanation of how the proposed method handles the trade-off between generalization and fine-tuning performance. While the authors mention that the consistency constraint helps to prevent overfitting, it is not clear how this constraint is balanced with the need to achieve good performance on the specific task. A more detailed discussion of the hyperparameter tuning process and the sensitivity of the results to different values of the consistency constraint would be helpful. It is unclear if the method is robust to different hyperparameter settings and if there is a principled way to choose the optimal value for a new task.
3. The paper does not discuss the limitations of the proposed method or potential failure cases. It is important to understand the scenarios where the method might not perform well or where it might be prone to overfitting. A discussion of the potential failure cases and limitations of the method would provide a more complete picture of its applicability and robustness.

### Suggestions

The authors should provide a more detailed analysis of the computational cost associated with their proposed method. This should include a breakdown of the training time and memory usage for different components of the model, such as the adapters and prompts. It would be beneficial to compare the computational cost of their method with existing approaches, such as MaPLe, to provide a clear understanding of the trade-offs between performance and computational efficiency. Furthermore, the authors should investigate the scalability of their method to larger datasets and models. This would help to assess the practical applicability of the method in real-world scenarios. The authors should also explore techniques to reduce the computational cost of their method, such as model compression or knowledge distillation.

To address the concern about the trade-off between generalization and fine-tuning performance, the authors should provide a more detailed analysis of the hyperparameter tuning process. This should include a discussion of the sensitivity of the results to different values of the consistency constraint and the other hyperparameters. The authors should also explore different strategies for hyperparameter tuning, such as grid search or Bayesian optimization, and provide guidelines for selecting the optimal values for a new task. It would be beneficial to show how the performance of the method varies with different values of the consistency constraint and to provide a principled way to choose the optimal value. The authors should also investigate the impact of different initialization strategies on the performance of the method and provide a discussion of the robustness of the method to different initialization schemes.

Finally, the authors should discuss the limitations of their method and potential failure cases. This should include a discussion of the scenarios where the method might not perform well or where it might be prone to overfitting. The authors should also investigate the sensitivity of the method to different types of data and tasks. It would be beneficial to provide a more complete picture of the applicability and robustness of the method by discussing its limitations and potential failure cases. The authors should also explore techniques to mitigate the limitations of the method and provide a discussion of the potential for future research.

### Questions

1. How does the proposed method compare to other state-of-the-art methods in terms of computational cost and memory usage?
2. How sensitive is the performance of the proposed method to the choice of hyperparameters, such as the consistency constraint weight and the learning rate?
3. What are the potential failure cases or limitations of the proposed method, and how can they be addressed?

### Rating

6

### Confidence

4

**********
