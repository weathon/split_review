### Summary

This paper introduces Cuff-KT, a novel approach to address learner distribution shifts in Knowledge Tracing (KT) models. The authors propose a method that decouples the base KT model into a static backbone and a dynamic layer, allowing for the generation of personalized parameters without the need for fine-tuning. The proposed method is evaluated on three datasets, demonstrating improvements in predictive performance.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper introduces a novel approach to handling distribution shifts in KT models by generating personalized parameters for learners, which is a creative solution to the problem of distribution shifts.
2. The paper is well-structured and easy to follow, with clear explanations of the proposed method and experimental setup.

### Weaknesses

#### Some Related Works

[1] Knowledge Tracing with Dynamic Cognitive Model
[2] Knowledge Tracing with Dynamic Cognitive Model and Curriculum Learning

#### comment

1. The paper's novelty is questionable, as it appears to be a straightforward application of existing techniques such as dual-tower models, low-rank decomposition, and attention mechanisms. The use of a dual-tower model, while effective, is not a novel contribution in itself, and the paper does not sufficiently articulate how the specific combination of these techniques is uniquely suited to the problem of distribution shifts in Knowledge Tracing (KT). The application of low-rank decomposition and attention mechanisms, while common, needs a stronger justification in the context of the proposed method, especially given the existing literature on their use in KT.
2. The paper lacks a clear definition of the problem it aims to solve. It is unclear whether the goal is to improve the KT model's performance on shifted distributions or to enhance the generator's ability to adapt to these shifts. The paper needs to explicitly state the problem being addressed, and the distinction between the two potential goals needs to be clarified. The current framing makes it difficult to understand the specific contribution of the proposed method.
3. The paper does not adequately address the potential for overfitting, given that the generator is trained on the same data it is intended to generalize to. The paper should discuss the mechanisms in place to prevent the generator from simply memorizing the training data, and how this memorization might affect its ability to generalize to unseen distributions. The lack of discussion on this critical issue raises concerns about the robustness of the proposed method.
4. The paper lacks a thorough comparison with existing methods for handling distribution shifts, such as those based on meta-learning or domain adaptation. The paper should include a more comprehensive comparison with these methods to demonstrate the advantages of the proposed approach. The current comparison is insufficient to establish the superiority of the proposed method.
5. The paper does not provide sufficient details on the experimental setup, such as the specific hyperparameters used and the evaluation metrics. The lack of these details makes it difficult to reproduce the results and to assess the validity of the findings. The paper should include a more detailed description of the experimental setup, including the specific hyperparameters used and the evaluation metrics.
6. The paper does not discuss the limitations of the proposed method, such as its computational complexity or its sensitivity to the choice of hyperparameters. The paper should include a discussion of the limitations of the proposed method, and how these limitations might affect its practical applicability.

### Suggestions

The paper needs to clearly articulate the novelty of its approach by highlighting the specific ways in which the combination of dual-tower models, low-rank decomposition, and attention mechanisms is uniquely suited to address the problem of distribution shifts in Knowledge Tracing (KT). The authors should provide a more detailed explanation of how these techniques are adapted to the specific challenges of KT, and why they are more effective than existing methods. For example, the paper could discuss how the dual-tower model is used to capture the complex relationships between learner behavior and knowledge state, and how the attention mechanism is used to focus on the most relevant information. The paper should also provide a more detailed explanation of how the low-rank decomposition is used to reduce the dimensionality of the parameter space, and how this contributes to the adaptability of the model. The paper should also include a more thorough discussion of the limitations of the proposed method, such as its computational complexity and its sensitivity to the choice of hyperparameters. This discussion should include specific examples of how these limitations might affect the practical applicability of the method.

The paper needs to provide a clear and precise definition of the problem it aims to solve. The authors should explicitly state whether the goal is to improve the KT model's performance on shifted distributions or to enhance the generator's ability to adapt to these shifts. The paper should also discuss the relationship between these two potential goals, and how the proposed method addresses both. The paper should also discuss the potential for overfitting, and how the proposed method mitigates this issue. The authors should provide a detailed explanation of the mechanisms in place to prevent the generator from simply memorizing the training data, and how this memorization might affect its ability to generalize to unseen distributions. The paper should also include a more thorough comparison with existing methods for handling distribution shifts, such as those based on meta-learning or domain adaptation. The paper should include a more comprehensive comparison with these methods to demonstrate the advantages of the proposed approach. This comparison should include a discussion of the strengths and weaknesses of each method, and how the proposed method compares to each of them in terms of performance, computational complexity, and robustness.

Finally, the paper needs to provide a more detailed description of the experimental setup, including the specific hyperparameters used and the evaluation metrics. The authors should also discuss the sensitivity of the results to the choice of hyperparameters, and how this might affect the reproducibility of the findings. The paper should also include a discussion of the limitations of the experimental setup, and how these limitations might affect the validity of the findings. The paper should also include a more detailed discussion of the computational complexity of the proposed method, and how this might affect its scalability to larger datasets. The paper should also discuss the potential for bias in the experimental results, and how this might affect the generalizability of the findings. The paper should also include a discussion of the ethical implications of the proposed method, and how these implications might affect its practical applicability.

### Questions

1. How does the proposed method compare to existing approaches for handling distribution shifts in KT, particularly those based on meta-learning or domain adaptation?
2. What are the computational costs associated with the proposed method, and how does it scale to larger datasets?
3. How sensitive is the performance of the proposed method to the choice of hyperparameters?

### Rating

3

### Confidence

4

**********
