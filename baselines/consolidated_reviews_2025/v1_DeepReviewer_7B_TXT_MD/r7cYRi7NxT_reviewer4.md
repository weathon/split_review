### Summary

This paper introduces a novel parameter-efficient transfer learning method, Hierarchical Side-Tuning (HST), designed to enhance the performance of Vision Transformers (ViTs) across a variety of visual tasks. HST leverages a lightweight Hierarchical Side Network (HSN) to model multi-scale features, which interact with image features through a Transformation Bridge (T-Bridge). The method demonstrates state-of-the-art performance across 13 out of 19 tasks on the VTAB-1K benchmark, achieving a Top-1 accuracy of 76.1% with only 0.78M parameters. In object detection and semantic segmentation tasks, HST matches or exceeds full fine-tuning performance while using fewer parameters, highlighting its efficiency and adaptability. The paper provides comprehensive experiments and comparisons with existing PETL methods, demonstrating the effectiveness and versatility of HST in various visual tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a novel parameter-efficient transfer learning method, Hierarchical Side-Tuning (HST), which leverages a lightweight Hierarchical Side Network (HSN) to model multi-scale features and interact with image features through a Transformation Bridge (T-Bridge). This approach is innovative and well-suited for enhancing the performance of Vision Transformers (ViTs) across various visual tasks.

2. The paper is well-structured and clearly written, making it easy to follow the proposed method and understand the experimental results. The authors provide a comprehensive description of the HST method, including the design of the Hierarchical Side Network (HSN) and the Transformation Bridge (T-Bridge), as well as the training and evaluation procedures.

3. The paper provides a thorough evaluation of the HST method across 19 visual tasks, including classification, object detection, and semantic segmentation. The results demonstrate that HST achieves state-of-the-art performance in 13 out of the 19 tasks on the VTAB-1K benchmark, with a Top-1 accuracy of 76.1% using only 0.78M parameters. This highlights the effectiveness and efficiency of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational complexity and efficiency of the proposed HST method. While the authors mention that HST achieves comparable performance to full fine-tuning with fewer parameters, they do not provide a thorough comparison of the computational cost, including training time and inference time. This information is crucial for assessing the practical applicability of the method, especially in resource-constrained environments.

2. The paper lacks a discussion on the limitations of the proposed HST method. While the authors demonstrate its effectiveness on a range of visual tasks, they do not address potential scenarios where the method might not perform well. For example, it would be beneficial to discuss the performance of HST on tasks with very complex or noisy data, or on tasks that require very specific types of visual understanding. This discussion would provide a more balanced and realistic assessment of the method's capabilities.

### Suggestions

The paper would benefit from a more detailed analysis of the computational cost associated with the HST method. While the authors mention parameter efficiency, a thorough comparison of training and inference times against other parameter-efficient transfer learning methods is needed. This should include a breakdown of the computational cost of each component of the HST method, such as the Hierarchical Side Network (HSN) and the Transformation Bridge (T-Bridge). For instance, the authors could provide a comparison of FLOPs, wall-clock time, and memory usage for HST and other methods like adapter-based approaches or low-rank adaptation methods. This would allow for a more comprehensive understanding of the trade-offs between performance and efficiency. Furthermore, it would be beneficial to analyze the scalability of the method with respect to the size of the input images and the number of parameters in the HST network. This analysis should include a discussion of how the computational cost scales with different input resolutions and model sizes, providing insights into the practical applicability of the method in various scenarios.

In addition to computational cost, the paper should include a more comprehensive discussion of the limitations of the proposed HST method. The authors should address potential scenarios where the method might not perform well, such as tasks with very complex or noisy data, or tasks that require very specific types of visual understanding. For example, it would be useful to evaluate the performance of HST on tasks with varying levels of image complexity, such as images with occlusions, cluttered backgrounds, or unusual viewpoints. Furthermore, the authors should discuss the sensitivity of the method to hyperparameter settings and provide guidelines for selecting appropriate values for different tasks. This would help users understand the robustness of the method and how to apply it effectively in different scenarios. It would also be beneficial to analyze the performance of HST on tasks that require very specific types of visual understanding, such as tasks involving fine-grained object recognition or scene understanding. This would provide a more complete picture of the method's capabilities and limitations.

Finally, the paper could benefit from a more detailed analysis of the performance of the HST method on different types of visual tasks. While the authors demonstrate its effectiveness on a range of tasks, a more granular analysis of the performance on specific sub-tasks or categories within each task would be valuable. For example, in the object detection task, it would be useful to evaluate the performance of HST on different object categories or on images with varying numbers of objects. This analysis would provide a more granular understanding of the method's strengths and weaknesses, and would help identify areas for further improvement. Furthermore, the authors should discuss the potential for combining the HST method with other techniques, such as data augmentation or ensemble methods, to further enhance its performance. This would provide a more comprehensive understanding of the method's potential and its applicability in various scenarios.

### Questions

See weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
