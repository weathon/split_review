### Summary

This paper introduces Cuff-KT, a novel method for addressing real-time learning pattern adjustment (RLPA) in Knowledge Tracing (KT). The method consists of a controller and a generator. The controller assigns values to learners based on their distribution changes, and the generator produces personalized parameters for the KT model at different stages or groups, enhancing its adaptability without the need for full retraining. Experiments on classic and recent datasets demonstrate that Cuff-KT significantly improves current KT models' performance under intra- and inter-learner shifts, with an average relative increase of 7% on AUC, effectively tackling RLPA.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is technically sound and well-motivated.
3. The experiments are comprehensive and well-designed.

### Weaknesses

#### Some Related Works


#### comment

1. The novelty of this paper is limited. The proposed method is a combination of existing techniques, including dual-tower models, low-rank decomposition, and attention mechanisms. The paper does not sufficiently articulate how the specific combination of these techniques is uniquely suited to the problem of distribution shifts in Knowledge Tracing (KT). The application of these techniques, while common, needs a stronger justification in the context of the proposed method, especially given the existing literature on their use in KT.
2. The paper lacks a clear definition of the problem it aims to solve. It is unclear whether the goal is to improve the KT model's performance on shifted distributions or to enhance the generator's ability to adapt to these shifts. The paper needs to explicitly state the problem being addressed, and the distinction between the two potential goals needs to be clarified. The current framing makes it difficult to understand the specific contribution of the proposed method.
3. The paper does not adequately address the potential for overfitting, given that the generator is trained on the same data it is intended to generalize to. The paper should discuss the mechanisms in place to prevent the generator from simply memorizing the training data, and how this memorization might affect its ability to generalize to unseen distributions. The lack of discussion on this critical issue raises concerns about the robustness of the proposed method.
4. The paper lacks a thorough comparison with existing methods for handling distribution shifts, such as those based on meta-learning or domain adaptation. The paper should include a more comprehensive comparison with these methods to demonstrate the advantages of the proposed approach. The current comparison is insufficient to establish the superiority of the proposed method.
5. The paper does not provide sufficient details on the experimental setup, such as the specific hyperparameters used and the evaluation metrics. The lack of these details makes it difficult to reproduce the results and to assess the validity of the findings. The paper should include a more detailed description of the experimental setup, including the specific hyperparameters used and the evaluation metrics.
6. The paper does not discuss the limitations of the proposed method, such as its computational complexity or its sensitivity to the choice of hyperparameters. The paper should include a discussion of the limitations of the proposed method, and how these limitations might affect its practical applicability.

### Suggestions

The paper needs to more clearly articulate the novelty of its approach by highlighting the specific ways in which the combination of dual-tower models, low-rank decomposition, and attention mechanisms is uniquely suited to address the problem of distribution shifts in Knowledge Tracing (KT). The authors should provide a more detailed explanation of how these techniques are adapted to the specific challenges of KT, and why they are more effective than existing methods. For example, the paper could discuss how the dual-tower model is used to capture the complex relationships between learner behavior and knowledge state, and how the attention mechanism is used to focus on the most relevant information. The paper should also provide a more detailed explanation of how the low-rank decomposition is used to reduce the dimensionality of the parameter space, and how this contributes to the adaptability of the model. Without a clear explanation of these adaptations, the novelty of the proposed method remains unclear.

The paper needs to provide a more precise definition of the problem it aims to solve. The authors should explicitly state whether the goal is to improve the KT model's performance on shifted distributions or to enhance the generator's ability to adapt to these shifts. The paper should also discuss the relationship between these two potential goals, and how the proposed method addresses both. The current framing makes it difficult to understand the specific contribution of the proposed method. For example, the paper could discuss how the controller is designed to detect distribution shifts, and how the generator is designed to adapt to these shifts. The paper should also discuss the limitations of the proposed method in addressing each of these potential goals. Without a clear definition of the problem, the significance of the proposed method is unclear.

The paper needs to address the potential for overfitting, given that the generator is trained on the same data it is intended to generalize to. The authors should discuss the mechanisms in place to prevent the generator from simply memorizing the training data, and how this memorization might affect its ability to generalize to unseen distributions. For example, the paper could discuss the use of regularization techniques, or the use of a separate validation set to evaluate the generator's performance. The paper should also discuss the potential for the generator to overfit to the training data, and how this might affect its ability to generalize to unseen distributions. Without addressing this issue, the robustness of the proposed method is questionable. Furthermore, the paper needs to provide a more thorough comparison with existing methods for handling distribution shifts, such as those based on meta-learning or domain adaptation. The paper should include a more comprehensive comparison with these methods to demonstrate the advantages of the proposed approach. The current comparison is insufficient to establish the superiority of the proposed method. The paper should also provide more details on the experimental setup, including the specific hyperparameters used and the evaluation metrics. Without these details, it is difficult to reproduce the results and assess the validity of the findings. Finally, the paper should discuss the limitations of the proposed method, such as its computational complexity or its sensitivity to the choice of hyperparameters. Without a discussion of these limitations, the practical applicability of the proposed method is unclear.

### Questions

1. How does the proposed method compare to existing approaches for handling distribution shifts in KT, particularly those based on meta-learning or domain adaptation?
2. What are the computational costs associated with the proposed method, and how does it scale to larger datasets?
3. How sensitive is the performance of the proposed method to the choice of hyperparameters?

### Rating

5

### Confidence

4

**********
