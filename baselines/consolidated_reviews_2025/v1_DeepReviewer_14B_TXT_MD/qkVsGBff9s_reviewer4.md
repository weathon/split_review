### Summary

The paper introduces a novel framework called State Decoupling with Q-supervised Contrastive representation (SDQC) for safe offline reinforcement learning. SDQC addresses the out-of-distribution problem by decoupling global observations into reward- and cost-related representations, improving generalization for unfamiliar observations. The approach is theoretically proven to generate a coarser representation while preserving the optimal policy, enhancing generalization performance. Experimental results on the DSRL benchmark demonstrate that SDQC outperforms other safe offline RL algorithms, achieving near-zero violations in many tasks and showing superior generalization in unseen environments.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel approach to safe offline reinforcement learning by decoupling state representations into reward- and cost-related components. This is a creative solution to the out-of-distribution problem, which is a significant challenge in offline RL.

2. The paper provides a solid theoretical foundation for the proposed method, proving that the Q-supervised contrastive learning approach generates a coarser representation while preserving the optimal policy. This theoretical backing adds credibility to the method's effectiveness.

3. The experimental results are compelling, demonstrating that SDQC outperforms other baseline algorithms on the DSRL benchmark. The method's ability to achieve near-zero violations in many tasks and its superior generalization in unseen environments highlight its practical significance.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion of the limitations of the proposed method and potential directions for future research. Specifically, the paper does not adequately address the potential for the decoupled representations to lose crucial information when the reward and cost functions are not easily separable in the state space. This could lead to suboptimal policies in complex environments where the optimal action depends on a nuanced combination of reward and cost considerations. Furthermore, the paper does not explore the sensitivity of the method to the choice of the contrastive loss function or the specific architecture used for the representation learning. A more thorough analysis of these factors would be beneficial.

2. The paper could include a more detailed analysis of the computational complexity of the proposed method and compare it to other state-of-the-art safe offline RL algorithms. The current analysis lacks a breakdown of the time and memory requirements for each component of the SDQC framework, such as the contrastive learning phase, the Q-function learning, and the policy extraction. A comparison with other methods should also consider the number of parameters and the training time required to achieve comparable performance. This would provide a more complete picture of the practical trade-offs associated with the proposed method.

### Suggestions

To address the limitations regarding the separability of reward and cost functions, the authors should investigate the performance of SDQC in environments where these functions are highly intertwined. For example, they could consider scenarios where the optimal policy requires a delicate balance between maximizing reward and minimizing cost, and where the state space contains regions where both reward and cost are high. Analyzing the behavior of SDQC in such environments would provide valuable insights into the robustness of the method. Furthermore, the authors could explore alternative decoupling strategies that are more adaptive to the specific characteristics of the reward and cost functions. This could involve incorporating a mechanism that dynamically adjusts the degree of decoupling based on the observed data or the current state of the agent. This would allow the method to better handle complex environments where the reward and cost functions are not easily separable.

To improve the analysis of the computational complexity, the authors should provide a detailed breakdown of the time and memory requirements for each component of the SDQC framework. This should include the cost of computing the contrastive loss, updating the Q-functions, and extracting the policy. The analysis should also consider the impact of different hyperparameters, such as the size of the representation space and the number of negative samples used in the contrastive learning process. A comparison with other state-of-the-art safe offline RL algorithms should be provided, including a discussion of the trade-offs between performance and computational cost. This comparison should not only focus on the overall training time but also on the memory requirements and the number of parameters. This would allow practitioners to make informed decisions about the suitability of SDQC for their specific applications.

Finally, the authors should investigate the sensitivity of the method to the choice of the contrastive loss function and the specific architecture used for representation learning. They could experiment with different loss functions, such as InfoNCE or triplet loss, and different architectures, such as convolutional or recurrent neural networks. This would provide a better understanding of the robustness of the method and its ability to generalize to different types of environments. Furthermore, the authors could explore techniques for regularizing the learned representations to prevent overfitting and improve generalization. This could involve adding a penalty term to the loss function that encourages the representations to be more compact or more invariant to irrelevant features.

### Questions

1. How does the proposed method handle the exploration-exploitation trade-off in the offline setting? Are there any specific strategies used to balance these two aspects?

2. Can the proposed method be extended to other types of constraints, such as time-varying constraints or constraints that depend on the history of past actions?

3. How does the performance of the proposed method compare to other state-of-the-art safe offline RL algorithms in terms of computational complexity and scalability?

### Rating

6

### Confidence

3

**********
