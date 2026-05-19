### Summary

This paper proposes a novel PETL method named Hierarchical Side-Tuning (HST) for Vision Transformers (ViTs). The HST method employs a lightweight Hierarchical Side Network (HSN) to model multi-scale features, which interact with image features through a Transformation Bridge (T-Bridge). To evaluate HST, the authors conducted comprehensive experiments across a range of visual tasks, including classification, object detection, instance segmentation, and semantic segmentation. The results demonstrate that HST achieves state-of-the-art performance in 13 out of the 19 tasks on the VTAB-1K benchmark, with the highest average Top-1 accuracy of 76.1%. When applied to object detection and semantic segmentation tasks, HST achieves comparable performance to full fine-tuning with fewer parameters.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The proposed Hierarchical Side-Tuning (HST) method is novel and effective. The introduction of the Hierarchical Side Network (HSN) and Transformation Bridge (T-Bridge) allows for the modeling of multi-scale features and their interaction with image features, which is crucial for tasks requiring detailed visual understanding. The meta-register and fine-grained injection components further enhance the model's adaptability and performance.

2. The paper is well-structured and clearly written, making it easy to follow the proposed method and understand the experimental results.

3. The authors conducted extensive experiments across a wide range of visual tasks, demonstrating the effectiveness and versatility of the HST method. The results show that HST achieves state-of-the-art performance in many tasks, indicating its potential for practical applications.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational complexity and efficiency of the proposed HST method. While the authors mention that HST achieves comparable performance to full fine-tuning with fewer parameters, they do not provide a thorough comparison of the computational cost, including training time and inference time. This information is crucial for assessing the practical applicability of the method, especially in resource-constrained environments.

2. The paper lacks a discussion on the limitations of the proposed HST method. While the authors demonstrate its effectiveness on a range of visual tasks, they do not address potential scenarios where the method might not perform well. For example, it would be beneficial to discuss the performance of HST on tasks with very complex or noisy data, or on tasks that require very specific types of visual understanding. This discussion would provide a more balanced and realistic assessment of the method's capabilities.

### Suggestions

The paper would benefit from a more thorough analysis of the computational efficiency of the proposed HST method. While the authors mention parameter reduction, a detailed breakdown of the computational cost, including FLOPs, training time, and inference time, is necessary. This analysis should be compared against other parameter-efficient transfer learning methods, such as adapter-based approaches and low-rank adaptation methods, to provide a clear understanding of the trade-offs between performance and efficiency. Furthermore, it would be beneficial to analyze the computational cost of each component of the HST method, such as the Hierarchical Side Network (HSN) and the Transformation Bridge (T-Bridge), to identify potential bottlenecks and areas for optimization. This would provide valuable insights into the practical applicability of the method in resource-constrained environments.

In addition to computational efficiency, the paper should include a more comprehensive discussion of the limitations of the proposed HST method. The authors should address potential scenarios where the method might not perform well, such as tasks with very complex or noisy data, or tasks that require very specific types of visual understanding. For example, it would be useful to evaluate the performance of HST on tasks with varying levels of image complexity, such as images with occlusions, cluttered backgrounds, or unusual viewpoints. Furthermore, the authors should discuss the sensitivity of the method to hyperparameter settings and provide guidelines for selecting appropriate values for different tasks. This would provide a more balanced and realistic assessment of the method's capabilities and limitations, and would help guide future research in this area.

Finally, the paper should include a more detailed analysis of the performance of the HST method on different types of visual tasks. While the authors demonstrate its effectiveness on a range of tasks, they do not provide a detailed analysis of the performance on specific sub-tasks or categories within each task. For example, in the object detection task, it would be useful to evaluate the performance of HST on different object categories or on images with varying numbers of objects. This analysis would provide a more granular understanding of the method's strengths and weaknesses, and would help identify areas for further improvement. Furthermore, the authors should discuss the potential for combining the HST method with other techniques, such as data augmentation or ensemble methods, to further enhance its performance.

### Questions

1. Can the authors provide a detailed analysis of the computational complexity and efficiency of the proposed HST method compared to other parameter-efficient transfer learning methods?

2. What are the potential limitations of the proposed HST method, and how might these limitations affect its performance on specific types of visual tasks?

3. How does the performance of the HST method vary across different types of visual tasks, and are there specific tasks where it performs particularly well or poorly?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
