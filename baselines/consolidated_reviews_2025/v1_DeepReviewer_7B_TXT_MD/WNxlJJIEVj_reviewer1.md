### Summary

This paper proposes a novel offline reinforcement learning algorithm called Contrastive Diffuser (CDiffuser). The key idea is to leverage low-return trajectories to enhance the performance of diffusion-based RL methods. CDiffuser treats states with high returns as positive samples and those with low returns as negative samples. It then uses a contrastive mechanism to pull the states in generated trajectories toward high-return states and push them away from low-return states. This approach aims to improve the agent's ability to achieve higher returns by constraining the states of the generated trajectories to be more aligned with high-return states and less aligned with low-return states. The authors evaluate CDiffuser on 14 D4RL benchmarks and demonstrate its effectiveness compared to existing offline RL methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper introduces a novel application of contrastive learning to offline reinforcement learning, specifically within the context of diffusion-based methods. This creative combination of techniques addresses a significant challenge in offline RL: leveraging low-return trajectories to improve overall performance.

- The experimental results are comprehensive, covering 14 D4RL benchmarks. The authors provide thorough comparisons with existing offline RL methods, including both diffusion-free and diffusion-based approaches. The ablation studies and further investigations offer valuable insights into the effectiveness of CDiffuser.

- The paper is well-organized and clearly written, making it accessible to readers familiar with reinforcement learning and diffusion models. The authors provide a detailed explanation of the method, including the contrastive loss function and the integration with diffusion models.

- The authors also provide code for reproducibility, which is crucial for validating the results and building upon this work.

### Weaknesses

#### Some Related Works


#### comment

 - The paper assumes that low-return trajectories are inherently less useful for learning, which may not always be the case. In some environments, low-return trajectories might contain valuable information about suboptimal paths or common pitfalls that could help the agent learn more effectively. By treating all low-return trajectories the same, the method may discard potentially useful information.

- The contrastive mechanism relies on the quality of the state representations. If the state space is high-dimensional and complex, it may be challenging to define meaningful positive and negative samples. The paper does not discuss how the method handles such cases, which could limit its applicability in real-world scenarios.

- The paper does not explore the sensitivity of CDiffuser to different hyperparameters, such as the temperature parameter in the contrastive loss function or the number of negative samples. A thorough analysis of these parameters would provide valuable insights into the robustness and generalizability of the method.

- The paper focuses on offline RL, but it would be interesting to see how CDiffuser could be extended to online or offline-online settings. For example, could the contrastive mechanism be used to refine the policy during online interaction? Or could it be combined with other online learning techniques to improve sample efficiency?

### Suggestions

The paper presents an interesting approach by applying contrastive learning to offline RL, but there are several areas where the methodology and analysis could be strengthened. First, the assumption that all low-return trajectories are equally detrimental needs further consideration. Instead of treating all low-return trajectories uniformly, the method could benefit from a more nuanced approach that differentiates between trajectories based on their specific characteristics. For instance, some low-return trajectories might indicate areas where the agent is struggling to learn the optimal policy, while others might represent rare but important transitions that should be preserved. A potential improvement would be to incorporate a mechanism that assigns different weights to low-return trajectories based on their proximity to high-return trajectories or their novelty. This could be achieved by using a similarity metric in the state space to identify trajectories that are both low-return and close to high-return regions. This would allow the contrastive mechanism to focus on the most informative low-return trajectories, rather than treating all of them equally. Furthermore, the method could explore techniques like curriculum learning, where the agent is gradually exposed to more challenging low-return trajectories as it learns, rather than all low-return trajectories being presented at once.

Second, the paper should address the challenges of high-dimensional state spaces. While the use of a diffusion model for trajectory generation is a good step, the contrastive mechanism still relies on meaningful state representations. The paper should discuss how the method handles the curse of dimensionality in the state space. For example, in environments with high-dimensional observations, such as images, it might be necessary to use a dimensionality reduction technique or a feature extractor to obtain meaningful state representations before applying the contrastive loss. The paper could also explore the use of attention mechanisms to focus on the most relevant parts of the state space when defining positive and negative samples. This would help to reduce the computational cost and improve the effectiveness of the contrastive mechanism in high-dimensional state spaces. Additionally, the paper should investigate the impact of different state representation learning techniques on the performance of CDiffuser. This would provide valuable insights into the robustness of the method and its applicability to different types of environments.

Finally, the paper needs a more thorough analysis of the hyperparameters. The contrastive loss function involves several hyperparameters, such as the temperature parameter and the number of negative samples, which can significantly affect the performance of the method. The paper should include a sensitivity analysis of these parameters, showing how the performance of CDiffuser varies with different values. This analysis should also explore the interaction between these parameters and other hyperparameters of the diffusion model. Furthermore, the paper should provide guidelines for selecting appropriate values for these parameters in different environments. This would make the method more practical and easier to use for other researchers. The paper should also explore the potential of combining CDiffuser with other offline RL techniques, such as behavior cloning or policy regularization, to further improve its performance. This could lead to a more robust and versatile method for offline RL.

### Questions

- How does the method handle low-return trajectories that might contain valuable information about suboptimal paths or common pitfalls?

- How does the method scale to high-dimensional state spaces, and what techniques could be used to improve its performance in such cases?

- What is the sensitivity of CDiffuser to different hyperparameters, such as the temperature parameter in the contrastive loss function or the number of negative samples?

- How could CDiffuser be extended to online or offline-online settings, and what are the potential benefits of such extensions?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
