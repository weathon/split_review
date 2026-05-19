### Summary

This paper proposes to take advantage of low-return trajectories, by pulling the states in trajectories toward to high-return states and pushing them away from low-return states. The paper performs contrastive learning to constrain the states in the agent’s trajectory and enhance the policy learning. Experiment results on 14 D4RL datasets demonstrate the outstanding performance of CDiffuser.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. This paper is well written and easy to follow.
2. This paper proposes a novel method named CDiffuser which can make full use of low-return trajectories and improve the performance of offline RL algorithms.
3. This paper provides sufficient empirical experiments and the results are convincing.

### Weaknesses

#### Some Related Works


#### comment

1. The paper should provide more discussions of related work.
2. The paper should provide more theoretical discussions, e.g., the convergence of the proposed algorithm.

### Suggestions

The related work section should be expanded to include a more detailed discussion of how the proposed method compares to existing offline reinforcement learning algorithms that also utilize contrastive learning or similar techniques for state representation. Specifically, the authors should discuss the differences in how their method leverages low-return trajectories compared to other methods that might discard or down-weight such trajectories. A more thorough comparison with methods that use diffusion models for planning, highlighting the unique aspects of the contrastive learning approach, would also be beneficial. Furthermore, the discussion should include a more detailed analysis of the limitations of existing methods that the proposed approach aims to address, providing a clearer context for the novelty and contribution of this work.

Regarding the theoretical discussions, while a full convergence proof might be challenging, the authors should provide a more in-depth analysis of the optimization landscape and the properties of the proposed loss function. For instance, discussing the conditions under which the contrastive loss is well-behaved and how the choice of hyperparameters affects the optimization process would be valuable. The authors could also explore the relationship between the proposed method and existing theoretical frameworks for offline RL, such as pessimism or uncertainty quantification. Even without a formal convergence proof, providing insights into the stability and robustness of the algorithm through analysis of the loss function and its gradients would significantly strengthen the theoretical foundation of the paper. This could include discussing the potential for local minima and how the proposed method mitigates such issues.

Finally, the paper would benefit from a more detailed analysis of the sensitivity of the algorithm to its hyperparameters. While the authors mention that the algorithm is not highly sensitive, a more rigorous analysis, including a discussion of the range of effective hyperparameter values and the impact of different choices on the performance, would be beneficial. This could include a sensitivity analysis of the contrastive loss parameters, such as the temperature parameter in the softmax, and how these parameters interact with other aspects of the algorithm. Furthermore, the authors should discuss the computational cost of tuning these hyperparameters and provide guidelines for selecting appropriate values for different datasets. This would make the method more practical and accessible to other researchers.

### Questions

1. Is the proposed algorithm sensitive to hyper parameters?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
