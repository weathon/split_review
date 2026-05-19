### Summary

This paper proposes a unified offline and online RL framework called Uni-O4, which leverages an on-policy objective for both offline and online learning. The key innovation is using an ensemble of policies and a novel offline policy evaluation (OPE) method to achieve stable multi-step policy improvement in the offline phase. The method demonstrates strong performance on simulated benchmarks and real-world robot tasks, outperforming state-of-the-art offline and offline-to-online RL algorithms.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper presents a novel unified framework that seamlessly integrates offline and online RL, addressing a key challenge in the field.
2. The use of ensemble policies and the proposed OPE method provide a simple yet effective way to improve performance in offline settings.
3. The experimental results are thorough, demonstrating strong performance across a range of simulated and real-world tasks.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost associated with the ensemble methods and OPE. This is a significant concern, as the practical applicability of the method could be limited by increased computational demands. Specifically, the paper lacks a breakdown of the time complexity for training the ensemble policies versus a single policy, and how this scales with the number of policies. Furthermore, the computational overhead of the OPE method, particularly the Monte Carlo rollouts, is not quantified, making it difficult to assess the overall efficiency of the approach.
2. While the real-world experiments are valuable, the paper could benefit from more extensive evaluation across a wider range of real-world tasks and scenarios to further validate the method's robustness and generalizability. The current real-world experiments, while demonstrating the method's potential, are limited in scope. For example, the paper does not explore the method's performance in more complex environments with higher dimensional state and action spaces, or in scenarios with more significant sensor noise and external disturbances. This limited evaluation makes it difficult to ascertain the method's true robustness and generalizability to diverse real-world applications.

### Suggestions

To address the lack of detailed computational analysis, the authors should provide a more thorough breakdown of the time complexity for each component of their method. This should include a comparison of the training time for the ensemble policies versus a single policy, as well as the computational cost of the OPE method, including the Monte Carlo rollouts. The analysis should also consider how these costs scale with the number of policies in the ensemble and the number of rollouts used in OPE. Furthermore, it would be beneficial to provide a practical analysis of the memory requirements of the method, as this can also be a limiting factor in real-world applications. This detailed analysis will allow readers to better understand the trade-offs between performance and computational cost, and will help to assess the practical applicability of the method.

To strengthen the real-world validation, the authors should conduct experiments on a wider range of tasks and scenarios. This should include more complex environments with higher dimensional state and action spaces, as well as scenarios with more significant sensor noise and external disturbances. For example, the authors could evaluate the method on tasks involving manipulation of deformable objects, or navigation in cluttered environments. Additionally, it would be beneficial to explore the method's performance in scenarios with different types of sensors, such as lidar or depth cameras. This more extensive evaluation will provide a more comprehensive understanding of the method's robustness and generalizability, and will help to identify potential limitations and areas for future improvement.

Finally, the authors should consider providing a more detailed analysis of the sensitivity of the method to hyperparameter settings. This should include an investigation of how the performance of the method varies with different choices of the number of ensemble policies, the number of Monte Carlo rollouts, and other relevant hyperparameters. This analysis will help to identify the optimal hyperparameter settings for different tasks and environments, and will provide valuable guidance for practitioners who wish to apply the method in their own work. Furthermore, it would be beneficial to explore the use of adaptive hyperparameter tuning techniques to automatically optimize the performance of the method for different tasks and environments.

### Questions

1. Can the authors provide a more detailed analysis of the computational cost of the ensemble methods and OPE compared to baseline approaches?
2. How does the performance of Uni-O4 vary with different choices of the number of ensemble policies?
3. Are there any specific real-world tasks or domains where the authors believe Uni-O4 would be particularly well-suited or challenging?

### Rating

6

### Confidence

3

**********
