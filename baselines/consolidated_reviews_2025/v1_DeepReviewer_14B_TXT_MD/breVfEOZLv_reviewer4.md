### Summary

This paper proposes an adaptive confidence distillation method for weak-to-strong knowledge distillation in vision models. The method dynamically adjusts the supervision from a weaker model to enhance the performance of a stronger model. The approach is validated through experiments on various tasks, including few-shot learning, transfer learning, and learning with noisy labels, showing superior performance over traditional strong-to-strong distillation methods.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The adaptive confidence distillation method is a novel approach that addresses the limitations of traditional knowledge distillation by leveraging weaker models to guide stronger ones.
2. The paper provides extensive experimental results across different tasks and datasets, demonstrating the effectiveness of the proposed method.
3. The paper is well-structured and clearly explains the methodology, experiments, and results.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational overhead introduced by the adaptive confidence distillation method. It would be beneficial to include a comparison of training times and resource usage between the proposed method and traditional distillation techniques. Specifically, the paper lacks a quantitative analysis of the additional computational cost associated with the dynamic adjustment of supervision, such as the time spent calculating the adaptive weights and the impact on overall training time. A breakdown of the time complexity of each step in the proposed method compared to standard knowledge distillation would be valuable.
2. While the paper demonstrates the effectiveness of the proposed method on several vision tasks, it does not explore its applicability to other domains, such as natural language processing or multimodal tasks. Including experiments or discussions on extending the method to other domains would enhance the paper's impact. The current evaluation is limited to image classification, and it is unclear how the adaptive confidence mechanism would perform with different data modalities and model architectures. For example, the paper should discuss the challenges and potential adaptations required to apply this method to sequence-based tasks or tasks involving both text and images.
3. The paper could benefit from a more in-depth discussion on the limitations of the proposed method. For instance, under what conditions might the adaptive confidence distillation fail to improve the performance of the stronger model, or even degrade it? The paper should explore scenarios where the weaker model's guidance might be misleading or detrimental to the stronger model's learning process. This could include cases where the weaker model is too inaccurate or when the task is inherently unsuitable for weak-to-strong distillation.

### Suggestions

To address the lack of computational analysis, the authors should include a detailed breakdown of the time complexity of their adaptive confidence distillation method. This should include a comparison of the time spent on each step of the proposed method versus standard knowledge distillation, such as the calculation of adaptive weights and the forward/backward passes. The authors should also provide empirical results on the training time and resource usage, such as GPU memory consumption, for both the proposed method and baseline distillation techniques. This analysis should be performed across different datasets and model sizes to provide a comprehensive understanding of the computational overhead. Furthermore, the authors should discuss the potential for optimizing the implementation of their method to reduce the computational cost, such as using more efficient algorithms for calculating adaptive weights or employing techniques like gradient checkpointing.

To broaden the applicability of the proposed method, the authors should explore its potential in other domains beyond computer vision. Specifically, they should discuss how the adaptive confidence distillation method could be adapted for natural language processing tasks, such as text classification or machine translation. This would involve considering the differences in data modality and model architectures between vision and language tasks. For example, the authors could discuss how the concept of 'confidence' would be defined and calculated for sequence-based models, and how the adaptive weighting mechanism would be applied to the training process. Additionally, the authors should explore the potential for applying their method to multimodal tasks, such as vision-language tasks, where the goal is to learn joint representations of images and text. This would require addressing the challenges of aligning different modalities and defining a suitable confidence measure for multimodal data.

Finally, the authors should provide a more thorough discussion of the limitations of their proposed method. This should include a detailed analysis of the conditions under which the adaptive confidence distillation might fail to improve or even degrade the performance of the stronger model. For example, the authors should explore scenarios where the weaker model is too inaccurate or when the task is inherently unsuitable for weak-to-strong distillation. The authors should also discuss the sensitivity of their method to the choice of hyperparameters, such as the learning rate and the temperature parameter used in the distillation process. Furthermore, the authors should provide guidelines for selecting appropriate weaker models for a given stronger model and task, and discuss the potential for using ensemble methods to improve the robustness of the distillation process.

### Questions

1. Can the authors provide more details on the computational complexity of the proposed method compared to traditional distillation techniques?
2. How does the performance of the proposed method vary with different architectures of weaker and stronger models?
3. Are there any specific scenarios or tasks where the proposed method might not be effective?

### Rating

6

### Confidence

3

**********
