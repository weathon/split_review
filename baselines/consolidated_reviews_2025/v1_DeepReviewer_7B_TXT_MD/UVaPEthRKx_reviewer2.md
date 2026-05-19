### Summary

This paper introduces Cuff-KT, a novel method for addressing real-time learning pattern adjustment (RLPA) in Knowledge Tracing (KT). Cuff-KT tackles the challenge of distribution shifts in learners' patterns, which can occur due to factors like cognitive fatigue and external stress. The method consists of a controller and a generator. The controller assigns values to learners based on their distribution changes, while the generator produces personalized parameters for the KT model at different stages or groups, enhancing its adaptability without the need for full retraining. Experiments on classic and recent datasets demonstrate that Cuff-KT significantly improves current KT models' performance under intra- and inter-learner shifts, with an average relative increase of 7% on AUC, effectively tackling RLPA.

### Soundness

2

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

[1] Knowledge tracing with dynamic cognitive model
[2] Knowledge tracing with dynamic cognitive model and curriculum learning
[3] Dynamic knowledge tracing

#### comment

1. The novelty of this paper is limited. The proposed method is a combination of existing techniques, including dual-tower models, low-rank decomposition, and attention mechanisms. The paper does not sufficiently articulate how the specific combination of these techniques is uniquely suited to the problem of distribution shifts in Knowledge Tracing (KT). The application of these techniques, while common, needs a stronger justification in the context of the proposed method, especially given the existing literature on their use in KT.
2. The paper lacks a clear definition of the problem it aims to solve. It is unclear whether the goal is to improve the KT model's performance on shifted distributions or to enhance the generator's ability to adapt to these shifts. The paper needs to explicitly state the problem being addressed, and the distinction between the two potential goals needs to be clarified. The current framing makes it difficult to understand the specific contribution of the proposed method.
3. The paper does not adequately address the potential for overfitting, given that the generator is trained on the same data it is intended to generalize to. The paper should discuss the mechanisms in place to prevent the generator from simply memorizing the training data, and how this memorization might affect its ability to generalize to unseen distributions. The lack of discussion on this critical issue raises concerns about the robustness of the proposed method.
4. The paper lacks a thorough comparison with existing methods for handling distribution shifts, such as those based on meta-learning or domain adaptation. The paper should include a more comprehensive comparison with these methods to demonstrate the advantages of the proposed approach. The current comparison is insufficient to establish the superiority of the proposed method.
5. The paper does not provide sufficient details on the experimental setup, such as the specific hyperparameters used and the evaluation metrics. The lack of these details makes it difficult to reproduce the results and to assess the validity of the findings. The paper should include a more detailed description of the experimental setup, including the specific hyperparameters used and the evaluation metrics.
6. The paper does not discuss the limitations of the proposed method, such as its computational complexity or its sensitivity to the choice of hyperparameters. The paper should include a discussion of the limitations of the proposed method, and how these limitations might affect its practical applicability.

### Suggestions

The paper needs to more clearly articulate the novelty of its approach. While the combination of existing techniques is not inherently problematic, the authors need to demonstrate a clear understanding of how their specific implementation differs from existing methods and why these differences are crucial for addressing the problem of distribution shifts in Knowledge Tracing. The paper should include a more detailed analysis of the limitations of existing methods and how the proposed approach overcomes these limitations. For example, the authors could discuss how their method addresses the specific challenges of adapting to distribution shifts in KT, such as the need to balance the trade-off between adapting to changes in the data distribution and maintaining the model's ability to generalize to new data. The authors should also provide a more detailed explanation of how the dual-tower model, low-rank decomposition, and attention mechanisms are specifically adapted to the problem of distribution shifts in KT, and why these adaptations are necessary.

The paper should also provide a more precise definition of the problem it aims to solve. The authors need to clearly distinguish between the goal of improving the KT model's performance on shifted distributions and the goal of enhancing the generator's ability to adapt to these shifts. The paper should explicitly state the problem being addressed and provide a clear rationale for why the proposed method is suitable for solving this problem. The authors should also discuss the limitations of their approach and how these limitations might affect the validity of their findings. For example, the authors could discuss the potential for the generator to overfit to the training data and how this might affect its ability to generalize to unseen distributions. The paper should also discuss the potential for the controller to make suboptimal decisions and how this might affect the overall performance of the system.

Finally, the paper needs to provide more details on the experimental setup and the evaluation metrics. The authors should include a detailed description of the datasets used, the specific hyperparameters used for each model, and the evaluation metrics used to assess the performance of the proposed method. The paper should also include a more thorough comparison with existing methods for handling distribution shifts, such as those based on meta-learning or domain adaptation. The authors should provide a more detailed analysis of the results, including a discussion of the statistical significance of the findings and the limitations of the proposed method. The paper should also discuss the computational complexity of the proposed method and how this might affect its scalability to larger datasets. The authors should also discuss the sensitivity of the results to the choice of hyperparameters and how this might affect the reproducibility of the findings.

### Questions

1. How does the proposed method compare to existing approaches for handling distribution shifts in KT, particularly those based on meta-learning or domain adaptation?
2. What are the computational costs associated with the proposed method, and how does it scale to larger datasets?
3. How sensitive is the performance of the proposed method to the choice of hyperparameters?

### Rating

5

### Confidence

4

**********
