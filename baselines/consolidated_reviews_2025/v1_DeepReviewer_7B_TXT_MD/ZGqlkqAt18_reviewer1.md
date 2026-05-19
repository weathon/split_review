### Summary

This paper introduces a two-stage optimization method called Diffusion-guided Safe Policy Optimization (DSPO) for learning safe policies from offline datasets without cost labels. The first stage involves training a return-agnostic discriminator to derive trajectory-wise safety signals, and the second stage uses a conditional diffusion model to generate safe trajectories. The policy is then derived by behavior cloning (BC). The authors evaluate their approach on various tasks from SafetyGym, BulletGym, and MetaDrive, demonstrating its effectiveness in achieving safe policies with high returns.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper proposes a novel approach to offline safe RL by learning safety signals without relying on explicit cost labels, which is a significant departure from traditional methods that assume Markovian cost functions.

2. The use of a transformer-based discriminator to derive trajectory-wise safety signals is innovative and allows for capturing complex, non-Markovian safety patterns that are difficult to identify with traditional cost-based approaches.

3. The conditional diffusion model effectively generates safe trajectories, and the use of behavior cloning (BC) for policy derivation is a simple yet effective way to distill the learned safety knowledge into a deployable policy.

4. The experiments are comprehensive, covering multiple environments (SafetyGym, BulletGym, and MetaDrive) and a variety of baselines, providing a thorough evaluation of the proposed method's effectiveness.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed discussion on the limitations of the proposed method, such as scenarios where the diffusion model might fail to generate safe trajectories or where behavior cloning might not effectively transfer the safety knowledge. Specifically, the paper does not address the potential for the diffusion model to generate trajectories that, while seemingly safe, might still violate subtle safety constraints not explicitly captured in the training data. Furthermore, the reliance on behavior cloning could lead to issues if the behavior cloning policy itself is unsafe or if the offline dataset contains a wide range of suboptimal trajectories, some of which might be unsafe.

2. The assumption of having a small number of safe demonstrations is not thoroughly discussed, and it is unclear how the method would perform with a larger or more diverse set of safe demonstrations. The paper does not explore the sensitivity of the method to the number and quality of safe demonstrations, nor does it discuss how the method might scale with an increasing number of safe demonstrations. It is also unclear if the method would be effective if the safe demonstrations are not representative of the overall safe action space.

3. The paper does not provide a clear explanation of how the return-agnostic discriminator is trained to derive trajectory-wise safety signals, and the connection between the discriminator's output and the subsequent diffusion model is not well-defined. The paper lacks a detailed explanation of the loss function used to train the discriminator, and how this loss function ensures that the discriminator's output is indeed indicative of safety, rather than just a proxy for return. The paper also does not clarify how the discriminator's output is used to condition the diffusion model, and how this conditioning ensures that the generated trajectories are safe.

4. The paper does not provide a detailed analysis of the computational cost associated with the two-stage optimization process, which could be a concern for real-time applications. The paper does not discuss the memory requirements for storing the discriminator and diffusion model, nor does it analyze the time complexity of the training and inference procedures. This lack of analysis makes it difficult to assess the practical feasibility of the method for real-world applications.

5. The paper does not discuss the potential for the diffusion model to generate unsafe trajectories, especially in complex environments where subtle safety violations might occur. The paper does not provide any analysis of the safety of the generated trajectories, nor does it discuss how the method might be made more robust to such violations. The paper also does not address the potential for the diffusion model to generate trajectories that are not feasible or realistic, which could limit the applicability of the method.

6. The paper does not provide a clear justification for using behavior cloning for policy derivation, especially given that the diffusion model is trained to generate safe trajectories. The paper does not discuss the potential for behavior cloning to introduce safety issues, especially if the behavior cloning policy is not well-trained or if the offline dataset contains unsafe trajectories. The paper also does not explore alternative policy derivation methods, such as reinforcement learning, which might be more suitable for learning from safe trajectories.

### Suggestions

The paper should include a more detailed discussion of the limitations of the proposed method, particularly regarding the potential for the diffusion model to generate unsafe trajectories and the reliance on behavior cloning for policy derivation. The authors should explore the sensitivity of the method to the number and quality of safe demonstrations, and discuss how the method might scale with an increasing number of safe demonstrations. It would be beneficial to include experiments that systematically vary the number and quality of safe demonstrations to assess the robustness of the method. Furthermore, the paper should provide a more detailed explanation of how the return-agnostic discriminator is trained, including the specific loss function used and how it ensures that the discriminator's output is indicative of safety. The authors should also clarify how the discriminator's output is used to condition the diffusion model, and how this conditioning ensures that the generated trajectories are safe. A more detailed analysis of the computational cost associated with the two-stage optimization process is also needed, including the memory requirements and time complexity of the training and inference procedures. This analysis should be performed on a range of environments to provide a more comprehensive understanding of the method's practical feasibility.

To address the concerns about the diffusion model generating unsafe trajectories, the authors should explore techniques to improve the safety of the generated trajectories. This could involve incorporating safety constraints into the diffusion model training process or using a safety filter to post-process the generated trajectories. The paper should also include a more detailed analysis of the safety of the generated trajectories, including metrics that quantify the degree of safety achieved. The authors should also justify the use of behavior cloning for policy derivation, and discuss the potential for behavior cloning to introduce safety issues. It would be beneficial to explore alternative policy derivation methods, such as reinforcement learning, which might be more suitable for learning from safe trajectories. The authors should also discuss the potential for the diffusion model to generate trajectories that are not feasible or realistic, and how this might affect the performance of the method.

Finally, the paper should provide a more detailed explanation of the experimental setup, including the specific parameters used for the diffusion model and the behavior cloning policy. The authors should also provide a more detailed analysis of the results, including a discussion of the strengths and weaknesses of the proposed method compared to the baselines. The paper should also include a more detailed discussion of the limitations of the proposed method, and suggest directions for future research. This would help to provide a more balanced and comprehensive assessment of the method's contributions and limitations.

### Questions

1. How does the method handle scenarios where the diffusion model might generate unsafe trajectories, especially in complex environments where subtle safety violations might occur?

2. How does the method scale with an increasing number of safe demonstrations, and what is the impact of the number and quality of safe demonstrations on the performance of the proposed approach?

3. Could the authors provide a more detailed explanation of how the return-agnostic discriminator is trained to derive trajectory-wise safety signals, and how the discriminator's output is used to condition the diffusion model?

4. What is the computational cost associated with the two-stage optimization process, and how does it compare to other offline safe RL methods?

5. How does the method ensure that the generated trajectories are safe, and what measures are taken to prevent the diffusion model from generating unsafe trajectories?

6. Why is behavior cloning used for policy derivation, and what are the potential risks of using behavior cloning in this context?

### Rating

3

### Confidence

4

**********
