### Summary

This paper introduces a generative pre-training approach for video understanding, inspired by image-based models like iGPT. The proposed model, named Toto, is a causal transformer that generates videos autoregressively, one token at a time. Toto is pre-trained on a large dataset of over 1 trillion visual tokens derived from diverse video sources, including internet-style exocentric videos and egocentric videos. The authors evaluate Toto across a range of downstream tasks, such as image recognition, video classification, object tracking, and robotic manipulation, demonstrating competitive performance with minimal inductive biases. The paper also explores the scaling behavior of Toto, showing a power law relationship between loss and compute.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper presents a comprehensive empirical study of a generative pre-training model for videos, evaluated across a diverse set of downstream tasks.
2. The model achieves competitive performance on various benchmarks despite having minimal inductive biases, suggesting the robustness of the pre-training approach.
3. The study includes extensive ablation experiments that provide insights into the effects of different design choices, such as tokenization methods and positional embeddings.

### Weaknesses

#### Some Related Works


#### comment

1. The pre-training approach builds on existing methods like iGPT, and while the application to video is novel, the core idea is not.
2. The paper lacks a detailed analysis of the computational costs associated with training and deploying Toto, which could be a concern given the model's size and the length of the video sequences it processes.
3. The paper does not thoroughly address the potential limitations of the pre-training approach, such as the risk of overfitting to the pre-training data or the challenges of adapting to tasks that are very different from those used for pre-training.

### Suggestions

The paper should include a more rigorous analysis of the computational demands of the Toto model. This should go beyond simply stating the number of parameters and include a breakdown of the FLOPs required for both training and inference. Specifically, the authors should analyze the computational cost per token during pre-training and downstream tasks, considering the impact of sequence length on overall computational burden. Furthermore, a comparison of computational costs with other state-of-the-art video models would provide valuable context for the community. This analysis should also consider the memory footprint of the model, which is a critical factor for deployment on resource-constrained devices. The authors should also explore techniques to mitigate the computational cost, such as model compression or quantization methods, which would enhance the practical applicability of the proposed approach.

To address the potential for overfitting, the authors should conduct a more detailed analysis of the model's performance on held-out data during pre-training. This should include an evaluation of the model's generalization capabilities across different datasets and tasks. The paper should also investigate the sensitivity of the model to the choice of pre-training data and the impact of data augmentation techniques. Furthermore, the authors should explore methods to improve the model's robustness to domain shifts, such as adversarial training or domain adaptation techniques. A thorough analysis of the model's failure cases would also provide valuable insights into its limitations and potential areas for improvement. This analysis should include specific examples of scenarios where the model performs poorly and a discussion of the underlying reasons for these failures.

Finally, the paper should provide a more in-depth discussion of the limitations of the pre-training approach, particularly concerning its adaptability to tasks that are significantly different from the pre-training tasks. The authors should explore the effectiveness of fine-tuning versus other adaptation methods, such as prompt tuning or meta-learning. A comparative analysis of these different adaptation strategies would provide valuable insights into the model's flexibility and limitations. The paper should also investigate the impact of the pre-training task on the model's performance on downstream tasks. For example, the authors could compare the performance of a model pre-trained on a video generation task with a model pre-trained on a video classification task. This analysis would help to identify the most effective pre-training strategies for different types of downstream tasks.

### Questions

1. How does Toto handle long-term dependencies in videos, especially in tasks like object tracking or action recognition, where understanding temporal context is crucial?
2. The paper mentions that Toto is pre-trained on a diverse set of videos. However, could you provide more details about the composition of this dataset? How does the choice of pre-training data affect the model's performance on different downstream tasks?
3. How does the model's performance scale with the amount of pre-training data? Is there a point of diminishing returns?
4. Given the model's complexity and the vast amount of data it's trained on, what are the potential ethical implications of this technology?

### Rating

6

### Confidence

3

**********
