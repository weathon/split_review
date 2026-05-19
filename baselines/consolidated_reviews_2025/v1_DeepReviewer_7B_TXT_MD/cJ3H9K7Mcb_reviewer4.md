### Summary

This paper studies the brittleness of OOD generalization under different degrees of distribution shifts. The authors show that the robustness of models can be quite brittle and inconsistent under different degrees of distribution shifts. They also observe that large-scale pre-trained models are sensitive to novel distribution shifts.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The authors conduct a comprehensive set of experiments to study the brittleness of robustness under different degrees of distribution shifts.
3. The authors also show that pre-trained models like CLIP are sensitive to novel distribution shifts.

### Weaknesses

#### Some Related Works


#### comment

1. The authors only consider the image classification task. It is unclear whether the observed brittleness is specific to this task or if it generalizes to other types of tasks, such as object detection or semantic segmentation.
2. The authors only consider the Gaussian noise as the type of distribution shift. It is unclear whether the observed brittleness is specific to this type of distribution shift or if it generalizes to other types of distribution shifts, such as changes in object pose, viewpoint, or background.

### Suggestions

The paper's focus on image classification, while providing a clear starting point, limits the generalizability of the findings. To strengthen the study, the authors should consider expanding their experiments to include tasks beyond image classification. For instance, object detection and semantic segmentation are crucial areas where OOD generalization is also of significant interest. Evaluating the brittleness of models on these tasks would provide a more comprehensive understanding of the phenomenon. Specifically, the authors could use datasets like COCO for object detection and ADE20K for semantic segmentation, and apply the same distribution shift strategies used in image classification. This would help determine if the observed brittleness is a general property of OOD generalization or if it is specific to image classification. Furthermore, the authors should investigate the impact of different model architectures on the observed brittleness. For example, comparing the performance of convolutional neural networks with transformer-based models on these different tasks could reveal interesting insights into the underlying mechanisms of brittleness.

Regarding the type of distribution shift, the exclusive use of Gaussian noise is a significant limitation. Real-world distribution shifts are often more complex and can involve changes in object pose, viewpoint, background, lighting conditions, and other factors. The authors should explore a wider range of distribution shift types to assess the robustness of their findings. For example, they could consider shifts in object pose by rotating images, shifts in viewpoint by changing the camera angle, or shifts in background by altering the scene composition. Additionally, they could investigate the impact of changes in lighting conditions, such as varying the brightness, contrast, or color temperature. This would provide a more comprehensive understanding of how different types of distribution shifts affect the brittleness of OOD generalization. The authors should also consider using more realistic distribution shifts that are derived from real-world data, rather than relying solely on synthetic perturbations. This would make the findings more relevant to practical applications.

Finally, the paper would benefit from a more in-depth analysis of the underlying mechanisms that cause the observed brittleness. While the authors demonstrate that models can be brittle under different degrees of distribution shifts, they do not provide a clear explanation of why this occurs. It would be valuable to explore the internal representations of the models and to analyze how they change under different types of distribution shifts. For example, the authors could visualize the feature maps of the models and to analyze how they are affected by different types of perturbations. This would provide a more mechanistic understanding of the observed brittleness. Furthermore, the authors could investigate the impact of different regularization techniques on the brittleness of OOD generalization. For example, they could explore the use of adversarial training or data augmentation techniques to improve the robustness of models to distribution shifts. This would provide practical guidance for developing more robust models.

### Questions

Please see the weakness.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
