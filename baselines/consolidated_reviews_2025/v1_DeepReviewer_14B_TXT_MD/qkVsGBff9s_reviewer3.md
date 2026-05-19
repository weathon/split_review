### Summary

This paper proposes a novel framework, State Decoupling with Q-supervised Contrastive representation (SDQC), for safe offline reinforcement learning. The key idea is to decouple the global observations into reward- and cost-related representations for decision-making, thereby improving the generalization capability for unfamiliar global observations. The authors theoretically prove that their Q-supervised method generates a coarser representation while preserving the optimal policy, resulting in improved generalization performance. The paper provides compelling experimental results on the DSRL benchmark, demonstrating that SDQC surpasses other baseline algorithms in terms of safety and performance.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow. The authors provide a clear motivation for their work and a thorough explanation of their proposed method.

2. The theoretical analysis is rigorous and provides a solid foundation for the proposed method. The authors prove that their Q-supervised contrastive learning method generates a coarser representation while preserving the optimal policy, leading to enhanced generalization performance.

3. The experimental results are compelling and demonstrate the effectiveness of the proposed method. The authors conduct extensive experiments on the DSRL benchmark and show that SDQC outperforms other baseline algorithms in terms of safety and performance.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion of the limitations of the proposed method and potential directions for future research. Specifically, the authors should address the computational cost associated with the contrastive learning component, and how this might scale with increasing state and action space dimensionality. Furthermore, the paper lacks a discussion on the sensitivity of the method to hyperparameter choices, particularly those related to the contrastive loss and the Q-function approximation. A more thorough analysis of these aspects would provide a more complete picture of the method's practical applicability.

2. The paper could include a more detailed analysis of the computational complexity of the proposed method and compare it to other state-of-the-art safe offline RL algorithms. The current analysis is insufficient to understand the practical implications of the proposed method's computational demands. For example, the authors should provide a breakdown of the time complexity for each step of the algorithm, including the contrastive learning phase, the Q-function update, and the policy extraction. This should be compared to the computational cost of other methods, not just in terms of wall-clock time, but also in terms of the number of operations required.

### Suggestions

To address the limitations regarding the computational cost and hyperparameter sensitivity, the authors should conduct a more thorough analysis of the method's performance under varying conditions. This should include experiments with different state and action space dimensionalities, as well as a sensitivity analysis of the key hyperparameters. Specifically, the authors should investigate how the performance of the method changes with different choices of the contrastive loss temperature parameter, the number of negative samples, and the learning rate for the Q-function. Furthermore, the authors should explore techniques to reduce the computational cost of the contrastive learning component, such as using more efficient similarity metrics or employing dimensionality reduction techniques before applying the contrastive loss. This would make the method more practical for real-world applications with limited computational resources. The authors should also consider providing guidelines for selecting appropriate hyperparameter values based on the characteristics of the environment and the available computational resources.

In addition to the computational analysis, the authors should also provide a more detailed discussion of the method's limitations in terms of its applicability to different types of environments. For example, the authors should discuss how the method might perform in environments with sparse rewards or high levels of stochasticity. Furthermore, the authors should explore potential extensions of the method to handle more complex constraints, such as time-varying constraints or constraints that depend on the history of past actions. This would broaden the applicability of the method and make it more relevant to a wider range of real-world problems. The authors should also consider comparing their method to other state-of-the-art safe offline RL algorithms in terms of their ability to handle different types of constraints and environments.

Finally, the authors should provide a more detailed analysis of the convergence properties of the proposed method. While the paper provides a theoretical analysis of the method's generalization capabilities, it lacks a discussion of the method's convergence behavior in practice. Specifically, the authors should investigate how the method's performance changes over time and whether it converges to a stable solution. This could involve plotting the learning curves for different environments and analyzing the variance of the performance over multiple runs. Furthermore, the authors should discuss the potential for instability in the learning process and how this might be mitigated. This would provide a more complete understanding of the method's behavior and its practical limitations.

### Questions

1. How does the proposed method handle the exploration-exploitation trade-off in the offline setting? Are there any specific strategies used to balance these two aspects?

2. Can the proposed method be extended to other types of constraints, such as time-varying constraints or constraints that depend on the history of past actions?

3. How does the performance of the proposed method compare to other state-of-the-art safe offline RL algorithms in terms of computational complexity and scalability?

### Rating

6

### Confidence

3

**********
