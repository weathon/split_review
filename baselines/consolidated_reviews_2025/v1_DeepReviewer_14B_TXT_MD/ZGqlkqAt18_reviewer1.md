### Summary

This paper proposes a method for offline safe RL without a marked cost function. Instead, the method uses a small number of safe demonstrations to guide the learning process. The core idea is to train a diffusion model that generates trajectories conditioned on safety signals derived from the safe demonstrations. The method, called Diffusion-guided Safe Policy Optimization (DSPO), consists of two stages. In the first stage, a return-agnostic discriminator is trained to provide trajectory-wise safety signals. In the second stage, a conditional diffusion model is trained using these safety signals and trajectory returns. The method is evaluated on tasks from the SafetyGym, BulletGym, and MetaDrive environments.

### Soundness

2

### Presentation

2

### Contribution

1

### Strengths

- The paper addresses a practical problem in offline safe RL, where Markovian cost functions are not always available. The proposed method can learn safe policies from offline datasets without cost labels, using only a small number of safe demonstrations. This setup is more realistic for many real-world applications.
- The paper provides a comprehensive evaluation of the proposed method across multiple environments, including SafetyGym, BulletGym, and MetaDrive. The experiments show that DSPO outperforms various baselines in terms of safety and task performance. The ablation studies and sensitivity analyses further validate the effectiveness of the proposed components and design choices.

### Weaknesses

#### Some Related Works

[1] Constrained decision transformer for offline safe reinforcement learning.
[2] Model-based safe reinforcement learning with divergence-constrained differential privacy.

#### comment

 - The novelty of the proposed method is limited. The idea of using a discriminator to distinguish between safe and unsafe trajectories and then using a diffusion model to generate safe trajectories has been explored in previous work [1]. The proposed method mainly combines existing techniques without significant innovation. Specifically, the use of a return-agnostic discriminator to provide safety signals, while potentially useful, does not represent a fundamental departure from existing approaches that use similar discriminators for imitation learning or safety certification. The conditional diffusion model, while effective, is also an existing technique, and its application here, while practical, lacks substantial novelty.
- The paper does not compare the proposed method with some recent offline safe RL methods, such as [2]. The lack of comparison with methods that explicitly address safety constraints through different mechanisms limits the ability to assess the relative strengths and weaknesses of the proposed approach. For example, methods that incorporate constraint satisfaction directly into the optimization process might offer different trade-offs between safety and performance.
- The experimental results are not convincing. In Table 1, the performance of DSPO is not significantly better than BC-Safe in many tasks. Additionally, the return of DSPO in the CarButton task is much lower than that of CDT-V, which is counterintuitive given that DSPO uses additional offline data. The similar performance to BC-Safe suggests that the method may not be effectively leveraging the full offline dataset in many scenarios, and the lower performance than CDT-V in CarButton raises concerns about the method's ability to effectively utilize the offline data in all environments.

### Suggestions

The paper would benefit from a more thorough analysis of the proposed method's novelty. While the combination of existing techniques is not inherently problematic, the paper needs to clearly articulate what specific challenges are addressed by this particular combination and how it differs from existing approaches. For example, the authors could investigate the specific properties of the return-agnostic discriminator that make it suitable for this task, and how it compares to other discriminators used in similar contexts. Furthermore, a more detailed analysis of the conditional diffusion model's behavior in the context of safe policy optimization would be beneficial. This could include an investigation of how the safety signals and trajectory returns interact to guide the diffusion process, and how this interaction differs from other applications of conditional diffusion models. The authors should also consider exploring alternative methods for generating safety signals, such as using a learned cost function, and compare their performance to the proposed approach.

To strengthen the experimental evaluation, the paper should include comparisons with a wider range of offline safe RL methods, particularly those that explicitly address safety constraints through different mechanisms. This would provide a more comprehensive understanding of the proposed method's strengths and weaknesses. The authors should also investigate the reasons for the similar performance to BC-Safe in many tasks. This could involve analyzing the trajectories generated by DSPO and BC-Safe to identify any differences in their behavior. Additionally, the authors should investigate the lower performance of DSPO compared to CDT-V in the CarButton task. This could involve analyzing the data used by each method, as well as the specific characteristics of the task that might contribute to this difference. It would also be beneficial to include statistical significance tests in the experimental results to provide a more rigorous assessment of the performance differences between the proposed method and the baselines.

Finally, the paper should provide a more detailed discussion of the limitations of the proposed method. This could include an analysis of the conditions under which the method is likely to fail or perform poorly. For example, the authors could investigate the sensitivity of the method to the quality and quantity of the safe demonstrations, as well as the complexity of the environment. The paper should also discuss potential avenues for future research, such as exploring alternative methods for generating safety signals, or incorporating constraint satisfaction directly into the optimization process. This would help to provide a more complete picture of the proposed method's contributions and limitations, and guide future research in this area.

### Questions

Please see the weaknesses.

### Rating

3

### Confidence

4

**********
