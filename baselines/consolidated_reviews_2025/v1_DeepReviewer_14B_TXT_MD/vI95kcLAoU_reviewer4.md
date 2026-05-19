### Summary

This paper proposes a method called Skip-Attention to improve the efficiency of vision transformers (ViT) by reusing self-attention computation from preceding layers to approximate attention at one or more subsequent layers. The authors introduce a simple parametric function to ensure that reusing self-attention blocks across layers does not degrade the performance. The effectiveness of the method is shown in image classification and self-supervised learning on ImageNet-1K, semantic segmentation on ADE20K, image denoising on SIDD, and video denoising on DAVIS. The authors achieve improved throughput at the same-or-higher accuracy levels in all these tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple yet effective. The idea of reusing self-attention computation from preceding layers to approximate attention at one or more subsequent layers is novel and interesting.
3. The authors conduct extensive experiments to demonstrate the effectiveness of the proposed method. The results show that the proposed method achieves improved throughput at the same-or-higher accuracy levels in all the tasks.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method may not be applicable to all types of vision transformers. For example, it may not be applicable to transformers with a large number of layers or a complex architecture.
2. The proposed method may not be able to handle tasks that require a high level of accuracy, such as object detection and instance segmentation.
3. The proposed method may not be able to handle tasks that require a large amount of data, such as video understanding.

### Suggestions

The paper introduces an interesting approach to improve the efficiency of vision transformers by reusing self-attention computations. However, the practical applicability of the proposed Skip-Attention method needs further investigation. Specifically, the method's effectiveness might be limited when applied to very deep transformer architectures. The paper should include experiments on a wider range of transformer models, including those with significantly more layers than the ones tested. It would be beneficial to analyze the performance of Skip-Attention on models like Swin Transformer V2 or other state-of-the-art architectures with a larger number of layers. Furthermore, the paper should provide a more detailed analysis of the computational cost and memory footprint of the proposed method, especially when applied to larger models. This analysis should include a breakdown of the FLOPs and memory usage for both the original and the modified models, which would help to better understand the trade-offs between accuracy and efficiency.

While the paper demonstrates the effectiveness of Skip-Attention on several tasks, it is important to acknowledge the limitations of the method in tasks requiring high accuracy. The paper should explicitly discuss the potential performance degradation when applying Skip-Attention to tasks like object detection and instance segmentation, where precise localization and fine-grained feature extraction are crucial. It would be beneficial to include experiments on these tasks to quantify the performance drop. Additionally, the paper should explore the impact of different hyperparameter settings for the parametric function used to approximate the attention maps. A sensitivity analysis of these parameters would provide valuable insights into the robustness of the method. The authors should also consider exploring adaptive strategies for determining which layers to skip, rather than relying on a fixed configuration, which could potentially improve the method's performance across different tasks and architectures.

Finally, the paper should address the limitations of the proposed method in handling tasks that require a large amount of data, such as video understanding. While the authors show results on video denoising, it is important to investigate the performance of Skip-Attention on more complex video understanding tasks, such as action recognition or video object tracking. The paper should also discuss the potential challenges of applying the method to long-range temporal dependencies in videos. It would be beneficial to explore techniques for adapting the proposed method to handle temporal information effectively. Furthermore, the paper should provide a more detailed analysis of the training time and convergence behavior of the proposed method, especially when applied to large datasets. This analysis should include a comparison of the training time and convergence speed of the original and modified models, which would help to better understand the practical implications of using Skip-Attention.

### Questions

1. How does the proposed method perform on other types of vision transformers, such as transformers with a large number of layers or a complex architecture?
2. How does the proposed method perform on tasks that require a high level of accuracy, such as object detection and instance segmentation?
3. How does the proposed method perform on tasks that require a large amount of data, such as video understanding?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
