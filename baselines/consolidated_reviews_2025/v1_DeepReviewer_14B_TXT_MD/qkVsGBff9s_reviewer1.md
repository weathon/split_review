### Summary

This paper proposes a safe offline RL algorithm based on state decoupling, which aims to learn reward-related and cost-related representations separately. The algorithm is theoretically grounded and extensive experiments are conducted.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well-written and easy to follow. The idea of decoupling states into reward- and cost-related parts is intuitive and well-explained.
- The algorithm is theoretically grounded. The authors provide theoretical guarantees for the proposed algorithm.
- Extensive experiments are conducted, demonstrating the effectiveness of the proposed algorithm.

### Weaknesses

#### Some Related Works


#### comment

 - The motivation for the proposed method could be further clarified. In particular, it would be helpful to clarify the connections to offline RL and the specific challenges in offline safe RL that the proposed method addresses.
- The proposed method is somewhat complex. For example, it needs to separately train three diffusion models. This complexity could potentially limit its applicability in real-world scenarios.
- The empirical results are promising but not sufficient to fully demonstrate the effectiveness of the proposed method. It would be beneficial to include additional experiments, such as testing the algorithm's performance under different safety thresholds or in more complex environments.

### Suggestions

The paper would benefit from a more detailed explanation of how the proposed state decoupling approach specifically addresses the challenges inherent in offline safe RL. While the idea of separating reward and cost representations is intuitive, the paper needs to articulate why this decoupling is particularly beneficial in the offline setting, where data distribution shifts and limited exploration are major concerns. For instance, how does decoupling help mitigate the issue of compounding errors when learning from a fixed dataset? Does it improve the robustness of the learned policy to out-of-distribution states, which is a common problem in offline RL? Furthermore, the paper should discuss how the proposed method handles the trade-off between reward maximization and cost constraint satisfaction, especially when the reward and cost functions are conflicting. A more in-depth analysis of these aspects would strengthen the motivation and clarify the contribution of the proposed method to the field of offline safe RL.

To address the complexity of the proposed method, the authors should provide a more detailed analysis of the computational overhead associated with training three separate diffusion models. It would be helpful to quantify the training time and memory requirements compared to existing offline safe RL algorithms. Furthermore, the paper should discuss potential strategies for reducing the computational burden, such as sharing parameters between the diffusion models or using more efficient training techniques. The authors could also explore the sensitivity of the algorithm's performance to the choice of hyperparameters, particularly those related to the diffusion models. A thorough analysis of these practical aspects would help assess the feasibility of deploying the proposed method in real-world scenarios. It would also be beneficial to investigate the potential for simplifying the architecture without sacrificing performance, perhaps by exploring alternative policy parameterizations.

Finally, the empirical evaluation should be expanded to include a more comprehensive set of experiments. Specifically, the paper should investigate the algorithm's performance under varying safety thresholds. This would provide insights into the robustness of the method and its ability to adapt to different safety requirements. Additionally, it would be valuable to evaluate the algorithm in more complex environments with higher-dimensional state spaces and more intricate reward and cost functions. This would help demonstrate the scalability of the proposed method and its applicability to real-world problems. Furthermore, the paper should include ablation studies to analyze the contribution of each component of the proposed method, such as the state decoupling mechanism and the use of diffusion models. This would provide a deeper understanding of the algorithm's behavior and identify potential areas for improvement.

### Questions

- How does the proposed method specifically address the challenges in offline RL, particularly in terms of distribution shift and limited exploration?
- What is the computational overhead of training three separate diffusion models, and how does it compare to existing methods?
- How does the algorithm perform under varying safety thresholds? 
- What are the potential limitations of the proposed method, and how could they be addressed in future work?

### Rating

6

### Confidence

4

**********
