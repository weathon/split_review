### Summary

This paper proposes a model-based reinforcement learning method that incorporates object-centric representations using segmentation masks. It is built upon the STORM algorithm, utilizing a pre-trained model for segmentation. The proposed method is evaluated on the Atari 100k benchmark and the game Hollow Knight, demonstrating superior sample efficiency and performance compared to the baseline.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The motivation and clarity of the paper are strong.
- The idea of integrating object-centric representations with the STORM algorithm is effective, yielding improvements in performance and sample efficiency.
- The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works

[1] Focus: Object-centric world models for robot manipulation.
[2] Object-centric learning with slot attention.

#### comment

 - The contribution of this paper is somewhat limited, as it primarily applies a pre-trained model for segmentation and integrates it with the existing STORM algorithm.
- The paper lacks comparisons with other object-centric representation methods, such as Focus [1] and Slot Attention [2].
- The number of trainable parameters for the proposed method is likely much higher than that of the baseline, which could make the comparison unfair.
- The proposed method requires prior knowledge, such as the number of objects and segmentation masks, which may limit its applicability in real-world scenarios.
- The paper does not address how the proposed method would handle more complex environments, such as Minecraft.

### Suggestions

The paper would benefit from a more thorough analysis of the computational overhead introduced by the object-centric approach. Specifically, a detailed breakdown of the parameter counts for each component (segmentation model, VAE, transformer, policy network) is needed to assess whether the performance gains are solely due to the increased model capacity or the effectiveness of the object-centric representation itself. It would be valuable to see experiments where the baseline model is scaled to have a similar number of parameters as the proposed method to isolate the impact of the architectural changes. Furthermore, the authors should investigate the sensitivity of the method to the quality of the segmentation masks. How does the performance degrade when the segmentation masks are noisy or incomplete? This analysis would provide a better understanding of the robustness of the proposed approach.

To address the lack of comparison with other object-centric methods, the authors should consider including at least one additional object-centric baseline, such as a simplified version of Slot Attention, even if it requires some adaptation to the visual RL setting. This would provide a more direct comparison of the proposed method's performance against other approaches that explicitly model objects. Furthermore, the authors should discuss the differences in the underlying assumptions and limitations of each method. For example, how does the reliance on pre-trained segmentation masks in the proposed method compare to the unsupervised object discovery approach of Slot Attention? A more detailed discussion of these differences would help to contextualize the contributions of the paper.

Finally, the authors should explore the limitations of the proposed method in more detail, particularly regarding its reliance on prior knowledge. While the use of segmentation masks and object labels is a practical approach, it is important to consider how the method could be extended to more complex scenarios where such information is not readily available. For example, could the method be combined with a unsupervised object discovery module to reduce the need for manual annotation? Additionally, the authors should discuss the potential challenges of applying the method to environments with a large number of interacting objects or more complex object dynamics. Addressing these limitations would provide a more complete picture of the applicability of the proposed method.

### Questions

- Could the authors provide statistics on the number of trainable parameters for each method?
- Could the authors include an ablation study on the number of objects?
- Could the authors discuss the potential limitations of the proposed method, such as its applicability to more complex environments like Minecraft?
- Could the authors consider adding other object-centric representation methods as baselines, such as Focus [1] and Slot Attention [2], to provide a more comprehensive comparison?

[1] Ferraro, Paul, et al. "Focus: Object-centric world models for robot manipulation." Advances in Neural Information Processing Systems 36 (2023): 20264-20276.
[2] Locatello, Francesco, et al. "Object-centric learning with slot attention." Advances in Neural Information Processing Systems 33 (2020): 11525-11538.

### Rating

5

### Confidence

3

**********
