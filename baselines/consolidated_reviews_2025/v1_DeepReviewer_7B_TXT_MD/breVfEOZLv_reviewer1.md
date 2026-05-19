### Summary

This paper proposes a weak-to-strong distillation method by adaptively balancing the supervision from the weak teacher and the soft labels from the strong student. The proposed method is evaluated on several tasks, including image classification, few-shot learning, noisy label learning, and transfer learning. The results show that the proposed method can outperform the strong-to-strong distillation methods and improve the performance of the teacher-student pairs with different architectures.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The proposed method is simple and easy to implement. The idea is straightforward and the formulation is clear. 
2. The experimental results show that the proposed method can outperform the strong-to-strong distillation methods and improve the performance of the teacher-student pairs with different architectures.

### Weaknesses

#### Some Related Works

[1] Decoupled Knowledge Distillation

#### comment

1. The proposed method is very similar to Decoupled Knowledge Distillation (DKD) [1]. The main difference is that the proposed method uses the strong model's output to replace the weak model's output. However, the difference is minor, and the proposed method can be viewed as a specific case of DKD. The core mechanism of both methods involves a weighted combination of a hard target (from the weak teacher or strong student) and a soft target (from the strong student), with the primary distinction being the source of the hard target. This distinction, while present, does not fundamentally alter the underlying approach, raising concerns about the novelty of the proposed method. The use of the strong model's output as a proxy for a superior target, while intuitive, lacks a strong theoretical justification and may not generalize well across diverse scenarios.
2. The proposed method is only evaluated on image classification tasks. It is unclear whether the proposed method can be applied to other tasks, such as object detection and semantic segmentation. The lack of evaluation on more complex tasks limits the assessment of the method's robustness and applicability. The method's performance on tasks with different input modalities and output structures (e.g., bounding boxes vs. class labels) remains unknown, which is a significant limitation.
3. The proposed method is only evaluated on small-scale datasets, such as CIFAR-10/100 and ImageNet. It is unclear whether the proposed method can be applied to large-scale datasets, such as LAION. The absence of experiments on large-scale datasets makes it difficult to assess the method's scalability and its potential for real-world applications. The computational cost and memory requirements of the proposed method on large datasets are also unknown, which is a critical factor for practical deployment.

### Suggestions

The authors should provide a more rigorous theoretical analysis of the proposed method, particularly in comparison to Decoupled Knowledge Distillation [1]. A detailed mathematical derivation that highlights the differences and advantages of the proposed approach is needed. The authors should also explore the sensitivity of the method to the choice of the strong model and provide guidelines for selecting an appropriate strong model for different tasks. Furthermore, a more in-depth analysis of the impact of the temperature parameter in the softmax function is necessary, including a discussion of how to choose an optimal value for different scenarios. The authors should also consider exploring alternative methods for generating soft targets, such as using different temperature parameters or employing more sophisticated temperature scaling techniques. This would help to demonstrate the robustness and generalizability of the proposed method.

To address the limited scope of the experimental evaluation, the authors should extend their experiments to include object detection and semantic segmentation tasks. This would provide a more comprehensive assessment of the method's applicability and robustness. The authors should also evaluate the method on large-scale datasets, such as LAION, to demonstrate its scalability and potential for real-world applications. The experiments should include a detailed analysis of the computational cost and memory requirements of the proposed method on large datasets. The authors should also compare the performance of the proposed method with other state-of-the-art distillation techniques on these tasks. This would provide a more comprehensive understanding of the method's strengths and weaknesses.

Finally, the authors should provide a more detailed discussion of the limitations of the proposed method and suggest potential avenues for future research. This should include a discussion of the scenarios where the proposed method may not perform well and the potential challenges in applying the method to different tasks and datasets. The authors should also explore the possibility of combining the proposed method with other distillation techniques to further improve its performance. This would help to demonstrate the potential for future research and development in this area.

### Questions

1. The proposed method is very similar to Decoupled Knowledge Distillation [1]. What is the difference between the proposed method and Decoupled Knowledge Distillation? 
2. The proposed method is only evaluated on small-scale datasets, such as CIFAR-10/100 and ImageNet. Can the proposed method be applied to large-scale datasets, such as LAION?

[1] Hao, Zhiwei, et al. "Decoupled knowledge distillation." Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. 2023.

### Rating

3

### Confidence

4

**********
