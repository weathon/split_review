### Summary

This paper addresses the challenge of safe offline reinforcement learning (RL) in safety-critical scenarios, where traditional online methods are impractical due to the inability to interact with environments. The authors propose a novel framework called State Decoupling with Q-Supervised Contrastive Representation (SDQC), which decouples global observations into reward- and cost-related representations for decision-making. This approach improves the generalization capability for unfamiliar global observations by clustering representations based on their similarity. The paper provides theoretical analysis demonstrating that SDQC generates a coarser representation while preserving the optimal policy, leading to enhanced generalization performance. Experiments on the DSRL benchmark show that SDQC outperforms other baseline algorithms, achieving almost zero violations in more than half of the tasks. The paper also includes ablation studies that validate the effectiveness of the Q-supervised contrastive loss in enhancing policy performance and safety.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel framework, State Decoupling with Q-Supervised Contrastive Representation (SDQC), for safe offline reinforcement learning (RL). This approach addresses the out-of-distribution (OOD) problem in offline safe RL by decoupling global observations into reward- and cost-related representations. This decoupling allows for more effective handling of safety constraints in unfamiliar environments.
2. Theoretical analysis is provided to demonstrate that SDQC generates a coarser representation while preserving the optimal policy. This theoretical foundation supports the effectiveness of the proposed method and provides insights into its generalization capabilities.
3. The paper is well-organized, with a clear introduction, detailed methodology, comprehensive experiments, and insightful discussions. The authors effectively communicate the motivation behind their approach and its potential benefits for safety-critical applications.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion of the limitations of the proposed method, such as scenarios where the decoupling of states might not be effective or the computational overhead associated with the contrastive learning process. Specifically, the paper lacks a discussion on the potential for the decoupling to fail in complex environments where reward and cost signals are intertwined, and how the method would perform in such cases. Furthermore, the computational cost of the contrastive learning process, including the number of parameters and training time, should be analyzed in more detail, especially in comparison to other safe offline RL algorithms.
2. The paper could provide more insights into the practical implementation details of the proposed method, such as the choice of hyperparameters and the sensitivity of the algorithm to these parameters. The paper should include a more thorough discussion on how the hyperparameters, such as the temperature parameters in the contrastive loss, the learning rates for the reward and cost networks, and the batch size, were chosen and how they affect the performance of the algorithm. A sensitivity analysis of these hyperparameters would be beneficial to understand the robustness of the method.
3. The paper could benefit from a more comprehensive comparison with existing state-of-the-art safe offline RL algorithms, including a detailed analysis of the performance differences and the specific scenarios where each algorithm excels. The comparison should not only focus on the final performance metrics but also on the learning speed, sample efficiency, and robustness to different hyperparameter settings. A more detailed analysis of the strengths and weaknesses of each algorithm in different environments would be valuable.

### Suggestions

The paper would significantly benefit from a more thorough investigation into the limitations of the proposed decoupling approach. Specifically, the authors should explore scenarios where the reward and cost signals are highly entangled, and analyze how the decoupling process might fail in such cases. For instance, in environments with complex dynamics or sparse reward/cost functions, the reward and cost representations might not be easily separable, leading to suboptimal performance. The authors should consider adding experiments in such challenging environments to demonstrate the robustness of their method. Furthermore, a more detailed analysis of the computational overhead associated with the contrastive learning process is needed. The authors should provide a breakdown of the computational cost, including the number of parameters, training time, and memory requirements, and compare these metrics with other safe offline RL algorithms. This would provide a more complete picture of the practical applicability of the proposed method.

To enhance the practical implementation details, the authors should provide a more comprehensive discussion on the choice of hyperparameters and their impact on the performance of the algorithm. The paper should include a sensitivity analysis of the hyperparameters, such as the temperature parameters in the contrastive loss, the learning rates for the reward and cost networks, and the batch size. This analysis should explore how different hyperparameter settings affect the learning speed, sample efficiency, and robustness of the algorithm. The authors should also provide guidelines for selecting optimal hyperparameters for different environments. This would make the proposed method more accessible and easier to implement in practice. Additionally, the authors should consider providing a more detailed explanation of the practical implementation of the proposed method, including the specific choices of neural network architectures and optimization algorithms.

Finally, the paper would benefit from a more comprehensive comparison with existing state-of-the-art safe offline RL algorithms. The comparison should not only focus on the final performance metrics but also on the learning speed, sample efficiency, and robustness to different hyperparameter settings. The authors should provide a detailed analysis of the strengths and weaknesses of each algorithm in different environments. This would provide a more complete picture of the relative performance of the proposed method and its potential advantages and disadvantages compared to existing approaches. The authors should also consider including additional baselines in their experiments to further validate the effectiveness of their method.

### Questions

1. How does the proposed method handle environments where the reward and cost signals are highly entangled and cannot be easily decoupled?
2. What are the computational costs associated with the contrastive learning process, and how do they compare to other safe offline RL algorithms?
3. How sensitive is the performance of the proposed method to the choice of hyperparameters, and what guidelines can be provided for selecting optimal hyperparameters?

### Rating

6

### Confidence

3

**********
