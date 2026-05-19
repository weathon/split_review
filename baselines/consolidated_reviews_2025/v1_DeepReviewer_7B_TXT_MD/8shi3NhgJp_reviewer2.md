### Summary

The paper introduces Imprecise Bayesian Continual Learning (IBCL), a novel approach to continual learning that addresses the challenge of learning models for specified trade-offs between different tasks. Unlike traditional continual learning methods that focus on a single task or require retraining with all previous tasks, IBCL allows for generating models that balance multiple tasks according to user-defined preferences. The method uses a Bayesian framework, where the model's parameters are represented as random variables, and variational inference is employed to update the knowledge base as new tasks are encountered. This approach enables the model to adapt to new tasks without forgetting previously learned ones, all while maintaining computational efficiency and scalability.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper introduces a novel approach to continual learning, IBCL, which allows for generating models that balance multiple tasks according to user-defined preferences. This is a significant departure from traditional continual learning methods that focus on a single task or require retraining with all previous tasks.

2. The use of a Bayesian framework, where the model's parameters are represented as random variables, is a novel approach that enables the model to adapt to new tasks without forgetting previously learned ones.

3. The paper provides a thorough theoretical analysis of the proposed method, including proofs of probabilistic Pareto-optimality and sublinear buffer growth.

4. The paper is well-written and easy to follow, with clear explanations of the key concepts and methods.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a clear explanation of how the method handles the trade-off between different tasks. While the authors mention that the method can generate models that balance multiple tasks according to user-defined preferences, they do not provide a detailed explanation of how this is achieved. Specifically, it is unclear how the user-defined preferences are incorporated into the model's training process and how the model learns to balance these preferences. The paper should provide a more detailed explanation of the mechanism by which the model adapts to new tasks while maintaining performance on previously learned tasks, and how this adaptation is controlled by the user-defined preferences.

2. The paper does not provide a clear explanation of how the method handles the trade-off between different tasks. While the authors mention that the method can generate models that balance multiple tasks according to user-defined preferences, they do not provide a detailed explanation of how this is achieved. Specifically, it is unclear how the user-defined preferences are incorporated into the model's training process and how the model learns to balance these preferences. The paper should provide a more detailed explanation of the mechanism by which the model adapts to new tasks while maintaining performance on previously learned tasks, and how this adaptation is controlled by the user-defined preferences.

3. The paper does not provide a clear explanation of how the method handles the trade-off between different tasks. While the authors mention that the method can generate models that balance multiple tasks according to user-defined preferences, they do not provide a detailed explanation of how this is achieved. Specifically, it is unclear how the user-defined preferences are incorporated into the model's training process and how the model learns to balance these preferences. The paper should provide a more detailed explanation of the mechanism by which the model adapts to new tasks while maintaining performance on previously learned tasks, and how this adaptation is controlled by the user-defined preferences.

### Suggestions

The paper should provide a more detailed explanation of how the user-defined preferences are incorporated into the model's training process. Specifically, it should clarify how the preference vector is used to guide the variational inference process and how the model learns to balance these preferences. For example, the authors could explain how the preference vector is used to modify the loss function or the gradient updates during training. Furthermore, the paper should provide a more detailed explanation of how the model adapts to new tasks while maintaining performance on previously learned tasks. This could include a discussion of the mechanisms by which the model updates its knowledge base and how these updates are controlled by the user-defined preferences. The authors should also provide a more detailed explanation of the mechanism by which the model balances multiple tasks according to user-defined preferences. This could include a discussion of how the model learns to trade off performance on different tasks and how this trade-off is controlled by the user-defined preferences. 

To improve the clarity of the paper, the authors should provide a more detailed explanation of the experimental setup and results. This should include a description of the datasets used, the evaluation metrics, and the baselines used for comparison. The authors should also provide a more detailed analysis of the results, including a discussion of the strengths and weaknesses of the proposed method. For example, the authors could provide a more detailed analysis of the performance of the method on different tasks and different user-defined preferences. The authors should also provide a more detailed comparison of the proposed method with existing continual learning methods, highlighting the advantages and disadvantages of each method. This would help the reader to better understand the contribution of the proposed method and its potential impact on the field.

Finally, the paper should provide a more detailed discussion of the limitations of the proposed method. This should include a discussion of the assumptions made by the method and the potential challenges in applying the method to real-world problems. The authors should also discuss the computational complexity of the method and its scalability to large datasets. The paper should also discuss the potential for future research in this area, including the development of more efficient and effective continual learning methods. This would help the reader to better understand the potential impact of the proposed method and its limitations.

### Questions

1. How does the proposed method handle the trade-off between different tasks? Specifically, how are user-defined preferences incorporated into the model's training process, and how does the model learn to balance these preferences?

2. How does the proposed method handle the trade-off between different tasks? Specifically, how are user-defined preferences incorporated into the model's training process, and how does the model learn to balance these preferences?

3. How does the proposed method handle the trade-off between different tasks? Specifically, how are user-defined preferences incorporated into the model's training process, and how does the model learn to balance these preferences?

### Rating

5

### Confidence

3

**********
