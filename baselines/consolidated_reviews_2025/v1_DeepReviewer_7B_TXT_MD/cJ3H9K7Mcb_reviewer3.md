### Summary

This paper studies the brittleness of OOD generalization under different degrees of distribution shifts. The authors show that the robustness of models can be quite brittle and inconsistent under different degrees of distribution shifts. They also observe that large-scale pre-trained models are sensitive to novel distribution shifts.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The authors conduct extensive experiments to demonstrate the brittleness of OOD generalization under different degrees of distribution shifts.
2. The authors show that pre-trained models are sensitive to novel distribution shifts.
3. The authors provide some insights into the evaluation of OOD generalization.

### Weaknesses

#### Some Related Works


#### comment

1. The authors only consider the image classification task. It is unclear whether the observed brittleness is specific to this task or if it generalizes to other types of tasks, such as object detection or semantic segmentation.
2. The authors only consider the Gaussian noise as the type of distribution shift. It is unclear whether the observed brittleness is specific to this type of distribution shift or if it generalizes to other types of distribution shifts, such as changes in object pose, viewpoint, or background.

### Suggestions

The authors should broaden their investigation to include a more diverse set of tasks beyond image classification. Specifically, they should consider tasks such as object detection and semantic segmentation, which involve different types of data and model architectures. For object detection, the authors could evaluate the performance of models on datasets with varying levels of occlusion, scale changes, and background clutter. For semantic segmentation, they could assess the robustness of models to changes in object appearance, lighting conditions, and viewpoint. This would help to determine whether the observed brittleness is a general phenomenon or if it is specific to image classification. Furthermore, it would be beneficial to explore the impact of different model architectures on the observed brittleness. For example, the authors could compare the performance of convolutional neural networks with that of transformer-based models on these different tasks. This would provide a more comprehensive understanding of the factors that contribute to the brittleness of OOD generalization.

In addition to expanding the task scope, the authors should also investigate a wider range of distribution shifts. While Gaussian noise is a common type of perturbation, it is not representative of all real-world distribution shifts. The authors should consider other types of shifts, such as changes in object pose, viewpoint, background, and lighting conditions. For example, they could evaluate the performance of models on datasets with varying levels of occlusion, scale changes, and background clutter. They could also assess the robustness of models to changes in object appearance, lighting conditions, and viewpoint. This would help to determine whether the observed brittleness is specific to Gaussian noise or if it is a more general phenomenon. Furthermore, it would be beneficial to explore the impact of different types of distribution shifts on different tasks. For example, the authors could investigate whether the brittleness of OOD generalization is more pronounced in object detection tasks than in semantic segmentation tasks, or vice versa. This would provide a more nuanced understanding of the factors that contribute to the brittleness of OOD generalization.

Finally, the authors should provide a more detailed analysis of the underlying mechanisms that cause the observed brittleness. While the authors demonstrate that models can be brittle under different degrees of distribution shifts, they do not provide a clear explanation of why this occurs. It would be beneficial to explore the internal representations of the models and to analyze how they change under different types of distribution shifts. For example, the authors could visualize the feature maps of the models and to analyze how they are affected by different types of perturbations. This would provide a more mechanistic understanding of the observed brittleness. Furthermore, the authors could investigate the impact of different regularization techniques on the brittleness of OOD generalization. For example, they could explore the use of adversarial training or data augmentation techniques to improve the robustness of models to distribution shifts. This would provide practical guidance for developing more robust models.

### Questions

See the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
