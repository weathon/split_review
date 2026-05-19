### Summary

The paper introduces a novel framework for safe offline reinforcement learning (RL) aimed at addressing the generalization issues that arise when deploying safe RL agents in unseen environments. The authors propose State Decoupling with Q-supervised Contrastive representation (SDQC), a method that decouples the global observations into reward-related and cost-related representations for decision-making. This approach aims to improve the generalization capability of safe offline RL by creating a more robust representation that is less affected by out-of-distribution (OOD) states. The paper also provides theoretical analysis showing that SDQC generates a coarser representation while preserving the optimal policy, leading to enhanced generalization performance. Empirical results on the DSRL benchmark demonstrate that SDQC outperforms other baseline algorithms, especially in terms of achieving near-zero violations in more than half of the tasks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper addresses a significant challenge in safe offline RL by proposing a novel framework that decouples global observations into reward-related and cost-related representations. This approach is innovative and provides a new perspective on handling safety constraints in offline settings.
2. The authors provide a rigorous theoretical analysis that demonstrates the advantages of SDQC over bisimulation, showing that it generates a coarser representation while preserving the optimal policy. This theoretical foundation strengthens the credibility of the proposed method.
3. The empirical results on the DSRL benchmark are compelling, showing that SDQC outperforms other baseline algorithms, especially in terms of achieving near-zero violations in more than half of the tasks. This highlights the practical effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion of the limitations of the proposed method, such as scenarios where the decoupling of states might not be effective or the computational overhead associated with the contrastive learning process. Specifically, the paper lacks a discussion on how the method would perform in environments with highly entangled state representations where reward and cost are not easily separable. Furthermore, the computational cost of the contrastive learning process, including the number of parameters and training time, should be analyzed in more detail, especially in comparison to other safe offline RL algorithms.
2. The paper could provide more insights into the practical implementation details of the proposed method, such as the choice of hyperparameters and the sensitivity of the algorithm to these parameters. The paper should include a more thorough discussion on how the hyperparameters, such as the temperature parameters in the contrastive loss, the learning rates for the reward and cost networks, and the batch size, were chosen and how they affect the performance of the algorithm. A sensitivity analysis of these hyperparameters would be beneficial to understand the robustness of the method.
3. The paper could benefit from a more comprehensive comparison with existing state-of-the-art safe offline RL algorithms, including a detailed analysis of the performance differences and the specific scenarios where each algorithm excels. The comparison should not only focus on the final performance metrics but also on the learning speed, sample efficiency, and robustness to different hyperparameter settings. A more detailed analysis of the strengths and weaknesses of each algorithm in different environments would be valuable.

### Suggestions

The paper should include a more in-depth discussion of the limitations of the proposed method, particularly in scenarios where the decoupling of states might not be effective. For instance, in environments where reward and cost are highly intertwined and cannot be easily separated, the proposed method might struggle to learn effective representations. The authors should provide a theoretical analysis or empirical evidence to support their claims about the limitations of the method. Furthermore, the paper should include a detailed analysis of the computational overhead associated with the contrastive learning process. This analysis should include the number of parameters, training time, and memory requirements of the proposed method, and compare these metrics with other safe offline RL algorithms. This would provide a more complete picture of the practical applicability of the proposed method.

To enhance the practical implementation details, the paper should include a more thorough discussion on how the hyperparameters were chosen and how they affect the performance of the algorithm. The authors should provide a sensitivity analysis of the hyperparameters, such as the temperature parameters in the contrastive loss, the learning rates for the reward and cost networks, and the batch size. This analysis should include a discussion of the trade-offs between different hyperparameter settings and how these trade-offs affect the performance of the algorithm. The paper should also provide a more detailed explanation of the practical implementation of the proposed method, including the specific choices of neural network architectures and optimization algorithms. This would make the paper more accessible to practitioners and facilitate the adoption of the proposed method in real-world applications.

Finally, the paper should include a more comprehensive comparison with existing state-of-the-art safe offline RL algorithms. The comparison should not only focus on the final performance metrics but also on the learning speed, sample efficiency, and robustness to different hyperparameter settings. The authors should provide a detailed analysis of the strengths and weaknesses of each algorithm in different environments. This analysis should include a discussion of the specific scenarios where each algorithm excels and the reasons for these differences. The paper should also include a discussion of the limitations of the proposed method in comparison to other algorithms and suggest potential directions for future research.

### Questions

1. How does the proposed method handle environments where the reward and cost are highly entangled and cannot be easily decoupled?
2. What are the computational costs associated with the contrastive learning process, and how do they compare to other safe offline RL algorithms?
3. How sensitive is the performance of the proposed method to the choice of hyperparameters, and what guidelines can be provided for selecting optimal hyperparameters?

### Rating

6

### Confidence

3

**********
