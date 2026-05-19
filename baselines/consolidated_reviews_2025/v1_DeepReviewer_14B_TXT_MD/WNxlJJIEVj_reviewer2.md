### Summary

The paper introduces a novel method called Contrastive Diffuser (CDiffuser) for offline reinforcement learning (RL). The key idea is to leverage low-return trajectories by treating them as negative samples and high-return trajectories as positive samples in a contrastive learning framework. The method uses a diffusion model to generate subsequent trajectories and applies a contrastive mechanism to constrain the states of the generated trajectories towards high-return states and away from low-return states. The authors evaluate CDiffuser on 14 D4RL benchmarks and demonstrate its superior performance compared to several baselines. The paper also includes ablation studies and further investigations to analyze the key designs of CDiffuser.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow. The figures are clear and helpful in understanding the proposed method.

2. The idea of using contrastive learning to leverage low-return trajectories in offline RL is novel and interesting.

3. The experimental results are comprehensive and demonstrate the effectiveness of CDiffuser. The ablation studies and further investigations provide valuable insights into the method's design choices.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a theoretical analysis of the proposed method. It would be helpful to have some theoretical justification for why the contrastive mechanism works and how it affects the performance of the algorithm.

2. The paper does not provide a detailed analysis of the computational cost of CDiffuser compared to the baselines. This is an important consideration for practical applications.

3. The paper does not explore the sensitivity of the method to the hyperparameters, especially those related to the contrastive mechanism. It would be helpful to understand how the performance of the algorithm varies with different hyperparameter settings.

### Suggestions

The paper introduces an interesting approach by applying contrastive learning to offline RL, but it would benefit from a more rigorous theoretical grounding. Specifically, a theoretical analysis should explore why contrasting high and low-return trajectories leads to improved policy learning. For instance, it would be valuable to analyze how the contrastive loss affects the state visitation distribution and how this relates to the optimal policy. Furthermore, it would be beneficial to investigate the convergence properties of the proposed method, especially in relation to the diffusion model and the contrastive loss. A theoretical framework could potentially explain the observed empirical improvements and provide insights into the limitations of the approach. Such analysis could also help in identifying the conditions under which the method is expected to perform well and when it might fail.

In addition to theoretical analysis, a more detailed investigation into the computational cost of CDiffuser is needed. The paper should provide a breakdown of the computational complexity of each component of the method, including the diffusion model, the contrastive loss calculation, and the trajectory generation. This analysis should compare the computational cost of CDiffuser with the baselines, not only in terms of training time but also in terms of memory usage and inference time. It would also be helpful to discuss the scalability of the method to larger datasets and more complex environments. Furthermore, the authors should provide practical guidance on how to optimize the implementation of CDiffuser to reduce its computational cost. This would make the method more accessible to researchers and practitioners with limited computational resources.

Finally, a thorough sensitivity analysis of the hyperparameters is crucial for understanding the robustness and practical applicability of CDiffuser. The paper should explore how the performance of the algorithm varies with different settings of the hyperparameters, especially those related to the contrastive mechanism, such as the temperature parameter in the contrastive loss and the number of negative samples. It would be helpful to provide guidelines on how to choose appropriate hyperparameter values for different datasets and environments. This analysis should also investigate the interaction between different hyperparameters and identify the most critical ones that significantly affect the performance of the algorithm. A detailed sensitivity analysis would increase the reliability and reproducibility of the results and provide valuable insights for future research.

### Questions

1. Can the authors provide more insights into why the contrastive mechanism works and how it affects the performance of the algorithm?

2. How does the computational cost of CDiffuser compare to the baselines?

3. How sensitive is the method to the hyperparameters, especially those related to the contrastive mechanism?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
