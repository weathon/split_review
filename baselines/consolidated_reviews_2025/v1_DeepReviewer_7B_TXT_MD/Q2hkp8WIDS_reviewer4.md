### Summary

This paper proposes a new model-based RL method called OC-STORM, which incorporates object-centric learning into the model-based RL framework. The proposed method uses Cutie to extract object features from raw observations and combines them with the raw observations to predict environmental dynamics. The authors evaluate the proposed method on the Atari 100k benchmark and the visually complex game Hollow Knight. The results show that OC-STORM outperforms the baseline STORM on 18 out of 26 Atari games and achieves the best-known sample efficiency on several Hollow Knight bosses.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The proposed method is simple and intuitive. It leverages the power of pre-trained foundation models to extract object features and incorporates them into the model-based RL framework. This approach is easy to implement and can be applied to a wide range of environments.
2. The proposed method achieves strong performance on the Atari 100k benchmark and the visually complex game Hollow Knight. The results demonstrate the effectiveness of the proposed method in improving sample efficiency and learning performance.
3. The paper is well-written and easy to follow. The authors provide clear explanations of the proposed method and the experimental setup.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method relies on the quality of the object segmentation masks provided by Cutie. If the segmentation masks are inaccurate or incomplete, the object features extracted by Cutie may be noisy or irrelevant, which could negatively impact the performance of the model-based RL framework. Specifically, the method does not address scenarios where objects are occluded or partially visible, which could lead to incomplete or inaccurate object representations. Furthermore, the method's reliance on a fixed set of object features extracted by Cutie may limit its adaptability to environments with novel object appearances or dynamics.
2. The proposed method is evaluated on a limited set of environments, including the Atari 100k benchmark and the visually complex game Hollow Knight. While these environments are challenging, they may not be representative of all real-world scenarios. The method's performance on more diverse and complex environments, such as those with continuous action spaces or more intricate object interactions, remains unclear. The lack of evaluation on environments with sparse rewards or long-term dependencies also limits the generalizability of the findings.
3. The proposed method is computationally expensive, especially when dealing with high-resolution images or complex environments. The use of a powerful pre-trained foundation model like Cutie, along with the model-based RL framework, requires significant computational resources. This could limit the applicability of the method in resource-constrained settings or for real-time applications. The paper does not provide a detailed analysis of the computational cost, making it difficult to assess the practical feasibility of the method.

### Suggestions

The authors should investigate the impact of noisy or incomplete object segmentation masks on the performance of the proposed method. One approach could be to incorporate a mechanism for detecting and handling segmentation errors, such as using a confidence score for each mask or employing a robust feature extraction method that is less sensitive to noise. Additionally, the authors could explore the use of alternative object segmentation methods or even learn object representations directly from the raw observations, which might be more robust to variations in object appearance and occlusion. Furthermore, the authors should consider the computational cost of the object segmentation step and explore ways to optimize it, such as using a lightweight segmentation model or parallelizing the segmentation process.

To address the limited evaluation scope, the authors should evaluate the proposed method on a more diverse set of environments, including those with continuous action spaces, sparse rewards, and long-term dependencies. This could involve testing the method on benchmark tasks from the DeepMind Control Suite or other challenging RL environments. The authors should also analyze the method's performance on environments with varying levels of visual complexity and object interactions. This would provide a more comprehensive understanding of the method's strengths and limitations. Furthermore, the authors should compare the performance of the proposed method with other state-of-the-art model-based RL algorithms on these diverse environments to provide a more robust evaluation.

Finally, the authors should provide a detailed analysis of the computational cost of the proposed method, including the time and memory requirements for training and inference. This analysis should consider the impact of different factors, such as the resolution of the input images, the complexity of the environment, and the size of the model. The authors should also explore ways to reduce the computational cost of the method, such as using model compression techniques or parallelizing the training process. This would make the method more practical for real-world applications and resource-constrained settings. The authors should also discuss the trade-off between performance and computational cost and provide guidance on how to choose the appropriate settings for different applications.

### Questions

1. How does the proposed method handle scenarios where the object segmentation masks provided by Cutie are inaccurate or incomplete?
2. How does the proposed method perform on environments with continuous action spaces or sparse rewards?
3. What is the computational cost of the proposed method, and how does it compare to other model-based RL methods?

### Rating

6

### Confidence

4

**********
