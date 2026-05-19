### Summary

This paper proposes a novel representation learning method, SDQC, for safe offline RL, which aims to tackle the out-of-distribution problem during testing. SDQC decouples the global observations into reward- and cost-related representations for decision-making. The proposed method theoretically proves that SDQC generates a coarser representation while preserving the optimal policy. Experiments on DSRL benchmark problems provide evidence that SDQC surpasses other baseline algorithms.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-written and easy to follow.
- The idea of decoupling states into reward- and cost-related representations is novel.
- The proposed method is supported by both theoretical and empirical evidence.

### Weaknesses

#### Some Related Works

[1] Distributional-Discrepancy-Based Safe Reinforcement Learning.
[2] Safe Offline Reinforcement Learning with Real-Time Budget Monitoring.
[3] Causality-Based Offline Reinforcement Learning for Autonomous Driving.
[4] A Lyapunov-based Framework for Safe Reinforcement Learning Assuring Safety Constraints.

#### comment

 - The authors mention that the out-of-distribution problem is one of the major issues in safe offline RL. However, it seems that the proposed method does not directly address this problem. Instead, SDQC decouples the global observations into reward- and cost-related representations. While this approach may indirectly help with the OOD problem, the paper does not provide a clear explanation of how this decoupling specifically mitigates the issue. For instance, it is unclear how the learned representations are more robust to OOD states compared to standard representations.
- The authors claim that the proposed method possesses superior generalization ability when confronted with unseen environments. However, the generalization tests are conducted in similar environments. Testing in more diverse environments, such as those with different dynamics or reward structures, would provide stronger evidence for this claim. The current experiments do not sufficiently demonstrate the method's ability to generalize to significantly different scenarios.
- The authors may need to include more recent safe offline RL algorithms for comparison, such as [1, 2, 3]. The current comparison is limited and does not fully contextualize the performance of the proposed method within the broader landscape of safe offline RL.
- The authors may need to include more recent safe RL algorithms that can handle hard constraints, such as [4]. The paper should demonstrate how the proposed method compares to state-of-the-art techniques for handling hard constraints in safe RL.

### Suggestions

The paper would benefit from a more detailed explanation of how the proposed decoupling of reward and cost representations directly addresses the out-of-distribution (OOD) problem. While the idea of decoupling is interesting, the paper lacks a clear mechanistic explanation of how this leads to improved OOD generalization. For example, the authors could provide a theoretical analysis or empirical study that demonstrates how the learned reward and cost representations are less sensitive to OOD states compared to standard representations. This could involve analyzing the feature space of the learned representations and showing that they are more robust to changes in the input space. Furthermore, the authors should consider including experiments that explicitly test the method's performance on OOD data, such as by training on a subset of the environment and testing on a significantly different subset. This would provide more direct evidence for the method's ability to handle OOD scenarios.

To strengthen the claims about generalization, the authors should conduct experiments in more diverse environments. The current experiments are limited to variations of the same environment, which does not fully demonstrate the method's ability to generalize to significantly different scenarios. For example, the authors could test the method in environments with different dynamics, reward structures, or constraint functions. This would provide a more comprehensive evaluation of the method's generalization capabilities. Additionally, the authors should consider using metrics that specifically measure generalization performance, such as the performance gap between training and testing environments. This would provide a more quantitative assessment of the method's ability to generalize to unseen scenarios. The authors should also provide a more detailed analysis of the learned representations in different environments to understand how they adapt to changes in the environment.

Finally, the paper should include a more comprehensive comparison to recent safe offline RL algorithms, especially those that can handle hard constraints. The current comparison is limited and does not fully contextualize the performance of the proposed method within the broader landscape of safe offline RL. The authors should include algorithms such as those mentioned in the weaknesses section, and provide a detailed analysis of the strengths and weaknesses of each method. This would provide a more complete picture of the current state of the art and the contribution of the proposed method. Furthermore, the authors should discuss the limitations of the proposed method and identify potential areas for future research. This would help to guide future work in this area and ensure that the proposed method is used appropriately.

### Questions

Please see the weaknesses above.

### Rating

6

### Confidence

4

**********
