### Summary

This paper proposes MotionRL, a multi-reward optimization framework based on reinforcement learning that fine-tunes models for text-to-motion generation with consideration for human preferences. In the MotionRL framework, a Pareto-based multi-objective optimization strategy is introduced to balance text adherence, motion quality, and human preferences. The results, including experimental and user study results, demonstrate that MotionRL outperforms other algorithms in terms of metrics and human preferences.

### Soundness

3

### Presentation

2

### Contribution

2

### Strengths

- This paper presents a novel approach to aligning text-to-motion generation with human preferences using multi-objective reinforcement learning.
- The proposed method achieves state-of-the-art performance on the HumanML3D dataset.
- The authors conducted a user study to validate their approach.

### Weaknesses

#### Some Related Works


#### comment

 - The motivation for this study is not clearly articulated, and the issues with existing research are not well-defined. In the introduction, the authors state, "On one hand, they require the motion length as input to guide generation, which may lead to motion quality degradation, since the length is closely tied to the content of the motion sequence." However, it is unclear what specific problems this statement refers to. Additionally, the authors mention that existing methods ignore human preferences, yet they fail to provide a detailed explanation of the issues that arise from this oversight.
- The proposed method appears to be a combination of existing techniques. The use of reward-specific tokens and batch-wise Pareto-optimal selection are borrowed from previous works, which undermines the novelty of the proposed approach.
- The experimental results are not particularly compelling. In Table 1, the proposed method shows only marginal improvements over MoMask, with a 0.010 increase in FID and 0.004 in R-Precision. Additionally, the qualitative results presented in the paper are not particularly convincing. For instance, in Figure 4, the proposed method exhibits foot sliding, which is not observed in other methods.
- The user study results are not well-presented. In Figure 2(b), the success rates for MoMask and the proposed method are 35% and 40%, respectively, but these values are not visually distinguishable from each other.

### Suggestions

The paper needs a more robust justification for its approach. The introduction should clearly articulate the limitations of existing text-to-motion methods, providing specific examples of where they fail. For instance, when discussing the issue of motion length, the authors should elaborate on how forcing a specific length can lead to unnatural or distorted motions, perhaps by causing jerky movements or altering the overall dynamics of the motion. Similarly, the claim that existing methods ignore human preferences needs to be substantiated with concrete examples of how this manifests in the generated motions. Do they produce motions that are visually unappealing, physically implausible, or lack the subtle nuances that humans expect? Without these specific details, the motivation for the proposed method remains weak. The authors should also consider discussing the specific challenges of incorporating human feedback into text-to-motion generation, such as the subjective nature of human preferences and the difficulty of quantifying these preferences into a reward signal.

Furthermore, the novelty of the proposed method needs to be more clearly established. While the authors acknowledge that reward-specific tokens and batch-wise Pareto-optimal selection are borrowed from previous works, they fail to articulate how their approach differs from these existing techniques. It is not sufficient to simply state that these techniques are used in a different context. The authors should explain the specific modifications or adaptations they have made to these techniques to suit the text-to-motion domain. For example, how are the reward-specific tokens tailored to capture the nuances of motion generation? How does the batch-wise Pareto-optimal selection strategy address the specific challenges of multi-objective optimization in this context? Without a clear explanation of these differences, the proposed method appears to be a mere combination of existing techniques, lacking significant technical contribution. The authors should also consider comparing their approach to other methods that also use reinforcement learning for text-to-motion generation, highlighting the unique aspects of their method.

Finally, the experimental results need to be more convincing. The marginal improvements over MoMask in terms of FID and R-Precision are not compelling, and the qualitative results are problematic. The foot sliding issue in Figure 4 is a significant concern, as it indicates that the proposed method is not generating physically plausible motions. The authors should address this issue by either improving their method or providing a more detailed explanation of why this occurs. Additionally, the user study results should be presented in a more clear and distinguishable manner. Instead of relying on a bar chart where the success rates are difficult to differentiate, the authors should consider using a different visualization technique or providing the exact numerical values. The authors should also consider conducting a more comprehensive user study, perhaps by including a larger number of participants or by using a more detailed rating scale. This would help to validate the effectiveness of their method and provide a more robust evaluation of its performance.

### Questions

- What is the length of the motion sequences generated by the proposed method? How many motion sequences are sampled for each text prompt during inference?
- What is the success rate of the proposed method in Figure 2(b)? The success rates of MoMask and the proposed method are not visually distinguishable.

### Rating

5

### Confidence

3

**********
