### Summary

This paper proposes Fat-to-Thin Policy Optimization (FtTPO), a method for offline reinforcement learning (RL) with sparse policies. The method is based on a two-stage actor-critic framework, where the first stage learns a fat (dense) policy and the second stage learns a thin (sparse) policy. The paper shows that this approach can outperform existing offline RL algorithms on safety-critical treatment simulation and the D4RL Mujoco benchmark.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and effective.
- The paper provides a detailed explanation of the method and its implementation.

### Weaknesses

#### Some Related Works

[1] Supported Policy Optimization: Reinforcement Learning with Safe Actions
[2] Supported Policy Optimization with Safety Constraints
[3] Supported Policy Optimization with Safety Constraints: A Survey

#### comment

 - The paper does not provide a clear explanation of how the proposed method addresses the out-of-support action issue in offline RL. While the paper mentions that the method uses a fat policy to generate actions and a sparse policy to learn from them, it does not provide a detailed explanation of how this process mitigates the problem of out-of-support actions. Specifically, it is unclear how the fat policy ensures that it only generates actions within the support of the offline dataset, and how the sparse policy is trained to learn from these actions without encountering out-of-support actions during training.
- The paper does not compare the proposed method with existing methods for handling out-of-support actions in offline RL, such as Supported Policy Optimization (SPO) [1, 2, 3]. The lack of comparison with these methods makes it difficult to assess the novelty and effectiveness of the proposed method. It is important to understand how the proposed method performs relative to these existing approaches, especially given that SPO is a well-established method for addressing out-of-support actions.
- The paper does not provide a detailed analysis of the computational cost of the proposed method. While the paper mentions that the method is simple and effective, it does not discuss the computational resources required to train the fat and thin policies, or the inference time of the method. This information is important for assessing the practical applicability of the method, especially in resource-constrained environments.

### Suggestions

The paper should provide a more detailed explanation of how the proposed method addresses the out-of-support action issue. Specifically, it should clarify how the fat policy is trained to generate actions that are within the support of the offline dataset, and how the sparse policy is trained to learn from these actions without encountering out-of-support actions during training. A more rigorous analysis of the action selection process, including the specific mechanisms that prevent the generation of out-of-support actions, would be beneficial. For example, the paper could discuss the use of a projection step to ensure that the generated actions are within the support of the offline dataset, or the use of a regularization term to encourage the fat policy to stay within the support.

Furthermore, the paper should include a comparison with existing methods for handling out-of-support actions in offline RL, such as Supported Policy Optimization (SPO). This comparison should not only include a performance comparison, but also a discussion of the strengths and weaknesses of each method. For example, the paper could discuss the computational cost of SPO compared to the proposed method, or the sensitivity of each method to the choice of hyperparameters. This comparison would help to better understand the novelty and effectiveness of the proposed method, and would provide a more complete picture of the state-of-the-art in offline RL.

Finally, the paper should include a detailed analysis of the computational cost of the proposed method. This analysis should include the computational resources required to train the fat and thin policies, as well as the inference time of the method. The paper should also discuss the scalability of the method to larger datasets and more complex environments. This information is crucial for assessing the practical applicability of the method, and would help to determine whether the method is suitable for real-world applications. The paper should also discuss the memory requirements of the method, which is an important factor for resource-constrained environments.

### Questions

- How does the proposed method address the out-of-support action issue in offline RL?
- How does the proposed method compare with existing methods for handling out-of-support actions in offline RL, such as Supported Policy Optimization (SPO)?
- What is the computational cost of the proposed method?

### Rating

5

### Confidence

4

**********
