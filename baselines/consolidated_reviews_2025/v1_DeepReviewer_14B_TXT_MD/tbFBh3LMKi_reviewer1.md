### Summary

This work aims to improve the performance of offline-to-online RL by using an on-policy objective for both offline and online learning, leveraging an ensemble of policies to address the mismatch issues in the offline phase, and employing a simple offline policy evaluation (OPE) approach for safe multi-step policy improvement.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The idea of using an on-policy objective for both offline and online learning is interesting.
3. The proposed method performs well on D4RL benchmarks, especially on the AntMaze tasks.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed offline policy evaluation (OPE) method relies on an approximate model (\hat{T}), which may introduce bias and error in the OPE results, potentially leading to inaccurate policy updates. Specifically, the method does not account for the compounding error that arises from using a learned dynamics model for multi-step rollouts, which can lead to inaccurate value estimates and suboptimal policy updates. Furthermore, the method does not explicitly address the uncertainty in the model predictions, which can be significant, especially when extrapolating beyond the offline dataset.
2. The proposed method does not introduce extra conservatism or regularization, which may lead to overestimation of the Q-values and subsequent suboptimal policies. The lack of explicit mechanisms to prevent overestimation, such as conservative policy optimization or value function regularization, makes the method vulnerable to the common pitfalls of offline RL, where overoptimistic value estimates can lead to poor generalization and performance.
3. The proposed method uses an ensemble of policies to address the mismatch issues between the estimated behavior policy and the offline dataset. However, it does not provide a clear explanation of how to effectively manage and coordinate the ensemble policies, which may lead to increased complexity and computational cost. The paper lacks details on how the ensemble policies are initialized, how their diversity is maintained during training, and how the final policy is selected from the ensemble. This lack of clarity makes it difficult to assess the practical viability of the approach.
4. The real-world robot experiments are not sufficient to fully demonstrate the effectiveness of the proposed method in real-world scenarios. The experiments are limited in scope and do not explore the challenges of real-world robotic systems, such as noisy sensors, model inaccuracies, and external disturbances. The paper would benefit from more extensive real-world experiments that demonstrate the robustness and generalizability of the proposed method.

### Suggestions

To address the limitations of the proposed offline policy evaluation (OPE) method, the authors should consider incorporating techniques to mitigate the error propagation from the approximate model. One approach is to use a pessimistic estimate of the value function, which can be achieved by subtracting a penalty term proportional to the uncertainty of the model predictions. This would help to prevent overestimation of the value function and improve the robustness of the policy updates. Another approach is to use a model-based approach that explicitly accounts for the uncertainty in the model predictions, such as Bayesian neural networks or ensemble methods. Furthermore, the authors should provide a more detailed analysis of the error characteristics of the learned dynamics model and how these errors affect the OPE results. This analysis should include an evaluation of the model's accuracy on out-of-distribution states and actions, as well as an assessment of the model's uncertainty estimates.

To mitigate the potential for overestimation of Q-values, the authors should explore incorporating explicit conservatism into the policy optimization process. This can be achieved by using techniques such as conservative policy optimization (CPO) or distributional reinforcement learning. CPO methods explicitly constrain the policy update to ensure that the new policy is not too far from the behavior policy, which can help to prevent overestimation and instability. Distributional reinforcement learning methods, on the other hand, can help to capture the uncertainty in the value function and prevent overestimation by learning a distribution over possible returns rather than a single expected value. The authors should also provide a more detailed analysis of the value function estimates and how they compare to the ground truth values, if available, or provide a theoretical analysis of the potential for overestimation.

Regarding the ensemble of policies, the authors should provide a more detailed explanation of how the ensemble is managed and coordinated. This should include details on how the ensemble policies are initialized, how their diversity is maintained during training, and how the final policy is selected from the ensemble. The authors should also provide a more detailed analysis of the computational cost of the ensemble method and how it scales with the number of policies. Furthermore, the authors should consider alternative approaches to addressing the mismatch between the behavior policy and the offline dataset, such as using a single policy with a more flexible parameterization or using techniques such as behavior cloning with regularization. The authors should also provide a more detailed comparison of the ensemble method to these alternative approaches.

### Questions

1. How does the proposed OPE method mitigate the bias and error introduced by the approximate model (\hat{T})?
2. How does the proposed method prevent the overestimation of Q-values without extra conservatism or regularization?
3. How does the proposed method effectively manage and coordinate the ensemble policies?
4. How does the proposed method perform in more complex real-world robot tasks?

### Rating

3

### Confidence

3

**********
