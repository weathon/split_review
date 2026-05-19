### Summary

This paper proposes a new approach to offline safe RL where the offline dataset lacks Markovian cost labels but includes a small set of safe demonstrations. The authors introduce a two-stage method called Diffusion-guided Safe Policy Optimization (DSPO). In the first stage, a return-agnostic discriminator is trained to generate trajectory-wise safety signals. In the second stage, a conditional diffusion model is trained to generate trajectories conditioned on both the trajectory return and the safety signal. The diffusion model is then used to derive a policy through behavior cloning. The method is evaluated on tasks from the SafetyGym, BulletGym, and MetaDrive environments, demonstrating that it can achieve a safe policy with high returns, outperforming various baselines.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper addresses a practical and important problem in offline safe RL by proposing a method that does not require Markovian cost labels in the offline dataset. This is a significant contribution as obtaining comprehensive Markovian cost labels can be difficult in many real-world scenarios.
2. The use of a conditional diffusion model to generate trajectories conditioned on both return and safety signals is a novel and interesting approach. The diffusion model's expressive capability allows it to capture the complex relationship between safety and return, leading to the generation of high-performing and safe trajectories.
3. The paper provides a thorough experimental evaluation of the proposed method across multiple environments, including SafetyGym, BulletGym, and MetaDrive. The results demonstrate that DSPO can achieve safe policies with high returns, significantly outperforming various established baselines.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a theoretical analysis of the proposed method. A theoretical understanding of why and how the method works would strengthen the paper's contribution. Specifically, the paper lacks any formal analysis of the convergence properties of the two-stage optimization process, or the conditions under which the learned safety signals accurately reflect true safety. Furthermore, there is no discussion on the potential for error propagation between the discriminator and the diffusion model.
2. The paper does not discuss the limitations of the proposed method in detail. For example, the paper does not discuss how the performance of DSPO scales with the complexity of the task or the size of the offline dataset. It is unclear how the method would perform in environments with very long time horizons or with high-dimensional state spaces. The paper also lacks an analysis of the sensitivity of the method to the quality and quantity of the safe demonstrations.
3. The paper does not provide a detailed analysis of the computational cost of the proposed method. Training a conditional diffusion model can be computationally expensive, and it is important to understand the trade-offs between performance and computational cost. The paper should include a breakdown of the computational resources required for each stage of the method, including the training time and memory usage, and compare these costs to other offline safe RL methods.

### Suggestions

The paper would benefit significantly from a more in-depth discussion of the theoretical underpinnings of the proposed method. While the empirical results are promising, a theoretical analysis could provide valuable insights into the method's behavior and limitations. Specifically, the authors should explore the convergence properties of the two-stage optimization process, perhaps by analyzing the loss landscapes of the discriminator and the diffusion model. It would also be beneficial to investigate the conditions under which the learned safety signals accurately reflect true safety, and to quantify the potential for error propagation between the discriminator and the diffusion model. This could involve analyzing the sensitivity of the diffusion model to noisy or inaccurate safety signals. Furthermore, the authors should consider providing a theoretical bound on the performance of the learned policy, perhaps by relating it to the quality of the safe demonstrations and the accuracy of the learned safety signals. Such analysis would greatly enhance the paper's contribution and provide a more solid foundation for future research.

To address the lack of discussion on the method's limitations, the authors should conduct a more thorough analysis of how the performance of DSPO scales with the complexity of the task and the size of the offline dataset. This could involve experiments on a wider range of environments, including those with longer time horizons and higher-dimensional state spaces. The authors should also investigate the sensitivity of the method to the quality and quantity of the safe demonstrations. For example, how does the performance of DSPO change when the number of safe demonstrations is significantly reduced, or when the safe demonstrations are noisy or suboptimal? It would also be useful to explore the method's robustness to out-of-distribution data, and to discuss the potential for the method to fail in certain scenarios. This analysis would provide a more complete picture of the method's strengths and weaknesses, and would help guide future research in this area.

Finally, the paper should include a detailed analysis of the computational cost of the proposed method. This should include a breakdown of the computational resources required for each stage of the method, including the training time and memory usage. The authors should also compare these costs to other offline safe RL methods, and discuss the trade-offs between performance and computational cost. For example, how does the training time of DSPO scale with the size of the offline dataset and the complexity of the environment? Are there any ways to reduce the computational cost of the method, such as by using more efficient training techniques or by reducing the size of the diffusion model? This analysis would be essential for practitioners who are considering using DSPO in real-world applications.

### Questions

1. How does the performance of DSPO scale with the size of the offline dataset and the complexity of the task?
2. What are the potential failure cases of DSPO, and how can they be mitigated?
3. How does the computational cost of DSPO compare to other offline safe RL methods?

### Rating

5

### Confidence

3

**********
