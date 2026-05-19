### Summary

This paper introduces a new problem setup for offline safe reinforcement learning, where the agent learns a safe policy from an offline dataset without cost labels, but with a small number of safe demonstrations. The authors propose a two-stage optimization method called Diffusion-guided Safe Policy Optimization (DSPO). In the first stage, they train a return-agnostic discriminator to derive trajectory-wise safety signals. In the second stage, they train a conditional diffusion model that generates trajectories conditioned on both the trajectory return and the safety signal. The evaluation experiments conducted across tasks from the SafetyGym, BulletGym, and MetaDrive environments demonstrate that the proposed approach can achieve a safe policy with high returns, significantly outperforming various established baselines.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a new problem setup for offline safe reinforcement learning, which is more practical in certain scenarios. This setup pushes the boundaries of safe reinforcement learning and makes it more applicable to real-world applications.
2. The proposed method is novel and effective. The two-stage optimization approach, which includes training a return-agnostic discriminator and a conditional diffusion model, is a creative solution to the problem of learning a safe policy from an offline dataset without cost labels.
3. The paper provides a comprehensive evaluation of the proposed method across various tasks from the SafetyGym, BulletGym, and MetaDrive environments. The results demonstrate that the proposed approach significantly outperforms various established baselines, indicating its effectiveness and potential for real-world applications.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a theoretical analysis of the proposed method. A theoretical understanding of why and how the method works would strengthen the paper's contribution. Specifically, the paper lacks a formal analysis of the convergence properties of the proposed two-stage optimization, and it is unclear how the return-agnostic discriminator interacts with the conditional diffusion model to ensure safe policy learning. The absence of theoretical guarantees makes it difficult to assess the robustness and reliability of the method.
2. The paper does not discuss the limitations of the proposed method in detail. For example, the paper does not discuss how the performance of DSPO scales with the complexity of the task or the size of the offline dataset. It is unclear how the method would perform in environments with very long time horizons or with high-dimensional state spaces. Furthermore, the paper does not address the potential sensitivity of the method to the quality and diversity of the safe demonstrations provided in the offline dataset.
3. The paper does not provide a detailed analysis of the computational cost of the proposed method. Training a conditional diffusion model can be computationally expensive, and it is important to understand the trade-offs between performance and computational cost. The paper should include a breakdown of the computational resources required for each stage of the method, including the training time and memory usage, and compare these costs to other offline safe RL methods. It is also unclear how the computational cost scales with the size of the offline dataset and the complexity of the environment.

### Suggestions

The paper would benefit significantly from a more rigorous theoretical analysis of the proposed method. Specifically, the authors should investigate the convergence properties of the two-stage optimization process. This could involve analyzing the loss functions used in both the discriminator and the diffusion model, and establishing conditions under which the optimization process converges to a safe and optimal policy. Furthermore, a theoretical analysis should address the interaction between the return-agnostic discriminator and the conditional diffusion model. It would be beneficial to provide some guarantees on the safety of the learned policy, perhaps by relating the discriminator's output to a safety metric or by bounding the probability of constraint violations. Such analysis would greatly enhance the paper's contribution and provide a more solid foundation for future research.

To address the lack of discussion on the method's limitations, the authors should conduct a more thorough analysis of how the performance of DSPO scales with the complexity of the task and the size of the offline dataset. This could involve experiments on a wider range of environments, including those with longer time horizons and higher-dimensional state spaces. The authors should also investigate the sensitivity of the method to the quality and diversity of the safe demonstrations provided in the offline dataset. For example, how does the performance of DSPO change when the number of safe demonstrations is significantly reduced, or when the safe demonstrations are noisy or suboptimal? It would also be useful to explore the method's robustness to out-of-distribution data, and to discuss the potential for the method to fail in certain scenarios. This analysis would provide a more complete picture of the method's strengths and weaknesses, and would help guide future research in this area.

Finally, the paper should include a detailed analysis of the computational cost of the proposed method. This should include a breakdown of the computational resources required for each stage of the method, including the training time and memory usage. The authors should also compare these costs to other offline safe RL methods, and discuss the trade-offs between performance and computational cost. For example, how does the training time of DSPO scale with the size of the offline dataset and the complexity of the environment? Are there any ways to reduce the computational cost of the method, such as by using more efficient training techniques or by reducing the size of the diffusion model? This analysis would be essential for practitioners who are considering using DSPO in real-world applications.

### Questions

1. How does the performance of DSPO scale with the size of the offline dataset and the complexity of the task?
2. What are the potential failure cases of DSPO, and how can they be mitigated?
3. How does the computational cost of DSPO compare to other offline safe RL methods?

### Rating

6

### Confidence

3

**********
