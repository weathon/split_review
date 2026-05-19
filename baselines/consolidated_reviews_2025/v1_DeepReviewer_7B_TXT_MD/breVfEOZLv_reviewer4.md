### Summary

This paper proposes a novel adaptive confidence distillation method to enhance the performance of the student model. The proposed method can be used for both weak-to-strong and strong-to-strong distillation. The proposed method is evaluated on various tasks, including image classification, few-shot learning, noisy label learning, and transfer learning.

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


#### comment

1. The proposed method is very similar to Decoupled Knowledge Distillation (DKD) [1]. The main difference is that the proposed method uses the strong model's output to replace the weak model's output. However, the difference is minor, and the proposed method can be viewed as a specific case of DKD. The core mechanism of both methods involves a weighted combination of a hard target (from the weak teacher or strong student) and a soft target (from the strong student), with the primary distinction being the source of the hard target. This distinction, while present, does not fundamentally alter the underlying approach, raising concerns about the novelty of the proposed method. The use of the strong model's output as a proxy for a superior target, while intuitive, lacks a strong theoretical justification and may not generalize well across diverse scenarios.
2. The proposed method is only evaluated on image classification tasks. It is unclear whether the proposed method can be applied to other tasks, such as object detection and semantic segmentation. The lack of evaluation on more complex tasks limits the assessment of the method's robustness and applicability. The method's performance on tasks with different input modalities and output structures (e.g., bounding boxes vs. class labels) remains unknown, which is a significant limitation.
3. The proposed method is only evaluated on small-scale datasets, such as CIFAR-10/100 and ImageNet. It is unclear whether the proposed method can be applied to large-scale datasets, such as LAION. The absence of experiments on large-scale datasets makes it difficult to assess the method's scalability and its potential for real-world applications. The computational cost and memory requirements of the proposed method on large datasets are also unknown, which is a critical factor for practical deployment.

### Suggestions

The authors should provide a more rigorous theoretical analysis of the proposed method, particularly in comparison to Decoupled Knowledge Distillation (DKD). A detailed mathematical derivation that highlights the differences and advantages of the proposed approach is needed. The authors should also explore the sensitivity of the method to the choice of the strong model and provide guidelines for selecting an appropriate strong model for different tasks. Furthermore, a more in-depth analysis of the impact of the temperature parameter in the softmax function is necessary, including a discussion of how to choose an optimal value for different scenarios. The authors should also consider exploring alternative methods for generating soft targets, such as using different temperature parameters or employing more sophisticated temperature scaling techniques. This would help to demonstrate the robustness and generalizability of the proposed method.

To address the limited scope of the experimental evaluation, the authors should extend their experiments to include object detection and semantic segmentation tasks. This would provide a more comprehensive assessment of the method's applicability and robustness. The authors should also evaluate the method on large-scale datasets, such as LAION, to demonstrate its scalability and potential for real-world applications. The experiments should include a detailed analysis of the computational cost and memory requirements of the proposed method on large datasets. The authors should also compare the performance of the proposed method with other state-of-the-art distillation techniques on these tasks. This would provide a more comprehensive understanding of the method's strengths and weaknesses.

Finally, the authors should provide a more detailed discussion of the limitations of the proposed method and suggest potential avenues for future research. This should include a discussion of the scenarios where the proposed method may not perform well and the potential challenges in applying the method to different tasks and datasets. The authors should also explore the possibility of combining the proposed method with other distillation techniques to further improve its performance. This would help to demonstrate the potential for future research and development in this area.

### Questions

Please refer to the weakness.

### Rating

3

### Confidence

5

**********
