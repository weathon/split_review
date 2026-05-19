### Summary

The paper introduces a new approach to offline safe reinforcement learning (RL) that does not rely on explicit cost labels in the dataset. The proposed method, DSPO, consists of two stages: first, a return-agnostic discriminator is trained to derive trajectory-wise safety signals, and second, a conditional diffusion model generates safe trajectories based on these signals. The policy is then derived by behavior cloning. The authors evaluate their approach on various tasks from SafetyGym, BulletGym, and MetaDrive, demonstrating its effectiveness in achieving safe policies with high returns.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The problem setup is interesting and practical.
3. The proposed method is technically sound and well-motivated.

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

The paper would benefit from a more thorough investigation into the limitations of the proposed method. Specifically, the authors should explore scenarios where the diffusion model might fail to generate safe trajectories, such as when the training data lacks sufficient coverage of the safe action space or when the safety constraints are highly complex and non-linear. It would be valuable to see experiments that systematically vary the diversity and quality of the safe demonstrations to understand the method's robustness. Furthermore, the paper should include a more detailed analysis of the computational cost associated with the two-stage optimization process, including memory requirements and time complexity, to assess its practical feasibility for real-world applications. The authors should also discuss the potential for the diffusion model to generate unsafe trajectories, especially in complex environments, and explore techniques to mitigate this risk, such as incorporating safety constraints into the diffusion model training or using a safety filter to post-process the generated trajectories. Finally, the paper should justify the use of behavior cloning for policy derivation, especially given that the diffusion model is trained to generate safe trajectories, and explore alternative policy derivation methods, such as reinforcement learning, which might be more suitable for learning from safe trajectories.

To address the lack of clarity regarding the training of the return-agnostic discriminator, the authors should provide a more detailed explanation of the loss function used and how it ensures that the discriminator's output is indicative of safety rather than just a proxy for return. The paper should also clarify how the discriminator's output is used to condition the diffusion model and how this conditioning ensures that the generated trajectories are safe. It would be beneficial to include a visualization of the discriminator's output and how it relates to the generated trajectories to provide a more intuitive understanding of the method. Additionally, the authors should explore the sensitivity of the method to the number and quality of safe demonstrations, and discuss how the method might scale with an increasing number of safe demonstrations. This could involve experiments with different numbers of safe demonstrations and different levels of diversity within the safe demonstrations to assess the method's robustness.

Finally, the paper should provide a more detailed explanation of how the trajectory-wise safety signals are used to guide the diffusion model. The authors should clarify how the return-agnostic nature of the safety signals ensures that the diffusion model does not rely on return information to generate safe trajectories. It would be helpful to see a more detailed analysis of the generated trajectories and how they relate to the safety signals. The paper should also discuss the potential for the diffusion model to generate trajectories that are not feasible or realistic, and how this might affect the performance of the method. The authors should also explore alternative policy derivation methods, such as reinforcement learning, which might be more suitable for learning from safe trajectories, and justify their choice of behavior cloning over these alternatives.

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
