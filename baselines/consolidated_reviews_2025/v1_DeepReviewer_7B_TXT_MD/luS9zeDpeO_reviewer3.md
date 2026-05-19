### Summary

This paper considers safe multi-agent reinforcement learning (MARL) in homogeneous multi-agent systems, where agents aim to maximize the team-average return while satisfying safety constraints. The authors introduce a decentralized primal-dual actor-critic algorithm that utilizes entropy regularization to balance exploration and safety. The algorithm is proven to converge to a Nash equilibrium under certain assumptions. The authors also provide a practical version of the algorithm based on deep reinforcement learning (DRL) techniques, which is evaluated on three safety-aware continuous multi-robot coordination tasks.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

- The paper is well-organized and easy to follow.
- The problem of safe MARL in homogeneous multi-agent systems is well-motivated.
- The proposed algorithm is decentralized and can be implemented in a fully distributed manner.
- The authors provide theoretical analysis to show the convergence of the algorithm.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed algorithm is only applicable to homogeneous multi-agent systems. This is a significant limitation, as many real-world multi-agent systems involve heterogeneous agents with different capabilities and objectives. The paper does not adequately address the challenges of extending the proposed method to heterogeneous settings, which limits its practical applicability.
- The assumption that the global state and action information is available to each agent is unrealistic in many practical scenarios. This assumption simplifies the problem but does not reflect the challenges of decentralized learning where agents only have access to local observations and actions. The paper does not discuss the implications of this assumption on the performance of the proposed algorithm.
- The paper does not provide a detailed discussion of the limitations of the proposed algorithm. For example, the paper does not discuss the sensitivity of the algorithm to hyperparameter settings or the potential for instability in certain environments. A more thorough analysis of the algorithm's limitations would be beneficial.
- The experimental evaluation is limited to three relatively simple tasks. It is unclear how the proposed algorithm would perform in more complex and realistic scenarios. The paper should include experiments on more challenging tasks to demonstrate the robustness and scalability of the proposed algorithm.

### Suggestions

The paper should address the limitations of the homogeneous multi-agent assumption by exploring potential extensions to heterogeneous settings. This could involve investigating methods for handling agents with different action spaces or reward functions. For example, the authors could consider using techniques such as policy adaptation or multi-task learning to allow agents to learn different policies. Furthermore, the paper should discuss the challenges of extending the proposed algorithm to heterogeneous settings, such as the need for communication between agents or the potential for conflicts in objectives. The authors should also provide a more detailed analysis of the impact of the global state and action information assumption on the performance of the algorithm. This could involve comparing the performance of the algorithm in scenarios with and without this information. The paper should also include a discussion of the limitations of the proposed algorithm, such as its sensitivity to hyperparameter settings and potential for instability. This could involve conducting experiments to evaluate the performance of the algorithm under different hyperparameter settings and in different environments. Finally, the experimental evaluation should be expanded to include more complex and realistic tasks. This could involve using more challenging environments or tasks that are more representative of real-world scenarios. The paper should also compare the performance of the proposed algorithm to other state-of-the-art safe MARL algorithms.

### Questions

- How does the proposed algorithm perform in heterogeneous multi-agent systems?
- What are the limitations of the proposed algorithm?
- How does the algorithm perform in more complex and realistic scenarios?

### Rating

5

### Confidence

3

**********
