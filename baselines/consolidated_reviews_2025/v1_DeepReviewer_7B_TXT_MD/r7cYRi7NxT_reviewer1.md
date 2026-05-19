### Summary

This paper introduces Hierarchical Side-Tuning (HST), a parameter-efficient transfer learning method for ViTs. HST employs a lightweight Hierarchical Side Network (HSN) to model multi-scale features, which interact with image features through a Transformation Bridge (T-Bridge). HST demonstrates state-of-the-art performance across 13 tasks on the VTAB-1K benchmark, with the highest average Top-1 accuracy of 76.1%. When applied to object detection and semantic segmentation tasks, HST achieves performance comparable to full fine-tuning while using fewer parameters.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed HST achieves state-of-the-art performance across 13 tasks on the VTAB-1K benchmark, with the highest average Top-1 accuracy of 76.1%. When applied to object detection and semantic segmentation tasks, HST achieves performance comparable to full fine-tuning while using fewer parameters.

### Weaknesses

#### Some Related Works

[1] Visual Prompt Tuning
[2] Parameter-Efficient Transfer Learning for Computer Vision
[3] Visual adaptation: A unified and generalizable framework for efficient transfer learning
[4] Visual prompt tuning: One-stage adaptation of vision models to new tasks and domains
[5] Visual Prompt Tuning: One-stage Adaptation of Vision Models to New Tasks and Domains
[6] Parameter-efficient transfer learning for vision tasks
[7] Visual Prompt Tuning: One-Stage Adaptation of Vision Models to New Tasks and Domains
[8] Parameter-Efficient Transfer Learning for Vision Tasks
[9] Visual Prompt Tuning: One-Stage Adaptation of Vision Models to New Tasks and Domains
[10] Parameter-Efficient Transfer Learning for Vision Tasks
[11] Visual Prompt Tuning: One-Stage Adaptation of Vision Models to New Tasks and Domains

#### comment

1. The paper lacks novelty. The proposed HST is similar to Visual Prompt Tuning (VPT) [1]. HST uses a lightweight Hierarchical Side Network (HSN) to model multi-scale features, which interact with image features through a Transformation Bridge (T-Bridge). The main difference is that HST adds a meta-register for global features. However, the meta-register is not a trainable module, and the global feature is simply the output of the last layer of the ViT. The overall framework is similar to VPT, and the paper does not provide a detailed comparison between the two methods.
2. The paper does not provide a comparison of the computational cost of HST with other parameter-efficient transfer learning methods. It is important to evaluate the efficiency of HST in terms of both training and inference time, as well as memory usage. The paper should include a detailed analysis of the computational overhead of the HST framework, including the number of parameters, FLOPs, and latency.
3. The paper does not provide a comparison of HST with other parameter-efficient transfer learning methods on object detection and semantic segmentation tasks. The paper only compares HST with full fine-tuning and some other parameter-efficient methods on image classification tasks. It is important to evaluate the performance of HST on more complex tasks, such as object detection and semantic segmentation, and compare it with other parameter-efficient methods. The paper should include a detailed analysis of the performance of HST on these tasks, including the number of parameters, FLOPs, and latency.
4. The paper does not provide a comparison of HST with other parameter-efficient transfer learning methods on different ViT architectures. The paper only evaluates HST on the ViT-B/16 architecture. It is important to evaluate the performance of HST on other ViT architectures, such as ViT-L/16 and ViT-H/14, and compare it with other parameter-efficient methods. The paper should include a detailed analysis of the performance of HST on these architectures, including the number of parameters, FLOPs, and latency.
5. The paper does not provide a comparison of HST with other parameter-efficient transfer learning methods on different pre-training datasets. The paper only evaluates HST on the MAE pre-trained ViT-B/16 architecture. It is important to evaluate the performance of HST on other pre-training datasets, such as ImageNet-21k and ImageNet-1k, and compare it with other parameter-efficient methods. The paper should include a detailed analysis of the performance of HST on these datasets, including the number of parameters, FLOPs, and latency.

### Suggestions

The paper should provide a more detailed comparison between HST and Visual Prompt Tuning (VPT), highlighting the specific differences in the architecture and functionality of the Hierarchical Side Network (HSN) and the Transformation Bridge (T-Bridge). The current description of the meta-register as a non-trainable component is insufficient; a more thorough explanation of its role and how it differs from the global feature output in VPT is needed. A detailed analysis of the computational complexity of HST, including the number of parameters, FLOPs, and latency, is crucial for evaluating its efficiency. The paper should include a comparison of these metrics with other parameter-efficient transfer learning methods, such as adapter-based approaches and low-rank adaptation methods, on various tasks and ViT architectures. This analysis should also consider the trade-offs between performance and efficiency, providing a clear understanding of the practical advantages of HST.

Furthermore, the paper needs to expand its experimental evaluation to include more complex tasks, such as object detection and semantic segmentation. The current evaluation is limited to image classification tasks, which may not fully demonstrate the capabilities of HST. The paper should compare HST with other parameter-efficient methods on these tasks, using standard evaluation metrics and datasets. Additionally, the paper should evaluate HST on different ViT architectures, such as ViT-L/16 and ViT-H/14, to assess its generalizability across different model sizes. The paper should also explore the performance of HST on different pre-training datasets, such as ImageNet-21k and ImageNet-1k, to evaluate its robustness to different pre-training strategies. These additional experiments would provide a more comprehensive understanding of the strengths and limitations of HST.

Finally, the paper should provide a more detailed analysis of the ablation study, particularly regarding the impact of the meta-register and the global feature. The current explanation is insufficient, and the paper should provide a more thorough analysis of how these components contribute to the overall performance of HST. The paper should also discuss the limitations of HST and suggest potential directions for future research. This would provide a more balanced and comprehensive evaluation of the proposed method. The paper should also include a discussion of the potential impact of the proposed method on real-world applications, highlighting the practical benefits and challenges of using HST in real-world scenarios.

### Questions

1. What is the difference between HST and VPT? 
2. What is the computational cost of HST compared to other parameter-efficient transfer learning methods?
3. How does HST perform on object detection and semantic segmentation tasks compared to other parameter-efficient methods?
4. How does HST perform on different ViT architectures?
5. How does HST perform on different pre-training datasets?

### Rating

3: reject, not good enough

### Confidence

5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

**********
