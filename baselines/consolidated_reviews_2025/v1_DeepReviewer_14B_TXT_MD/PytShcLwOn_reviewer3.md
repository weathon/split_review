### Summary

This paper proposes a method to generate a sequence of 3D hand poses from a single image that contains a hand and an object. The proposed method consists of two parts: extracting an object feature using CLIP and generating a hand pose sequence using a diffusion model. The proposed method does not show a significant improvement in performance compared to two baselines, MDM-T and MDM-I.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

This paper proposes a new task and a new method for generating a hand pose sequence from a hand image. The proposed method utilizes an object feature extracted from a hand image to generate a hand pose sequence, and this object feature improves the accuracy of the method.

### Weaknesses

#### Some Related Works


#### comment

The largest problem with this paper is that the proposed method does not show a significant improvement in accuracy compared to two baselines, MDM-T and MDM-I. In addition, the proposed method is a simple adaptation of MDM to a new task, and the novelty is limited. The method's reliance on a single image to generate a sequence of hand poses is also a limitation, as it does not account for the inherent ambiguity in such a task. The evaluation metrics, while standard, may not fully capture the nuances of hand pose sequence generation, particularly regarding the naturalness and plausibility of the generated motions. The paper lacks a thorough analysis of failure cases, which would be beneficial in understanding the limitations of the proposed approach. Furthermore, the method's performance is not evaluated on a diverse set of objects, which could affect its generalizability.

### Suggestions

To address the limited improvement over baselines, the authors should explore more sophisticated methods for incorporating object features into the diffusion model. Instead of simply concatenating or adding the object feature to the text embedding, they could investigate attention mechanisms or learnable fusion layers that allow the model to dynamically weigh the importance of object features at different stages of the generation process. Furthermore, the authors should consider incorporating temporal constraints or priors into the model to ensure the generated hand pose sequences are smooth and physically plausible. This could involve using a temporal convolutional network or a recurrent neural network to model the temporal dependencies between hand poses. The authors should also explore the use of adversarial training to improve the realism of the generated hand pose sequences.

To enhance the novelty of the approach, the authors could investigate more advanced techniques for feature extraction from the input image. For example, they could explore the use of 3D convolutional networks or transformers to capture more detailed spatial and temporal information about the hand and object. They could also consider incorporating depth information or multi-view images to improve the accuracy of the generated hand pose sequences. Furthermore, the authors should explore the use of contrastive learning to learn more robust and discriminative features for the hand and object. This could involve training the feature extractor to distinguish between different hand-object interactions or different object types.

Finally, the authors should conduct a more comprehensive evaluation of the proposed method, including a detailed analysis of failure cases and a evaluation on a more diverse set of objects. They should also consider using more sophisticated evaluation metrics that capture the naturalness and plausibility of the generated hand pose sequences. For example, they could use metrics based on the smoothness of the hand motion or the physical plausibility of the generated poses. They should also compare their method to other state-of-the-art methods for hand pose estimation and motion generation, even if these methods are not directly applicable to the same task. This would provide a more comprehensive assessment of the strengths and weaknesses of the proposed approach.

### Questions

What is the difference in the number of parameters between the proposed method and the baselines? Is the increase in accuracy due to the increase in the number of parameters?

### Rating

6

### Confidence

3

**********
