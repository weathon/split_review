### Summary

This paper proposes a new method called Skip-Attention to improve the efficiency of vision transformers (ViTs). The core idea is to reuse self-attention computations from previous layers to approximate attention in later layers, thereby reducing the computational cost without significantly sacrificing performance. The authors demonstrate the effectiveness of Skip-Attention on various tasks, including image classification, self-supervised learning, semantic segmentation, image denoising, and video denoising. The method achieves state-of-the-art or comparable performance while significantly reducing computational overhead.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The proposed method is simple yet effective, offering a practical solution to improve the efficiency of ViTs.
2. The paper provides extensive experimental results across multiple tasks and datasets, demonstrating the generalizability and robustness of the method.
3. The paper is well-written and easy to follow, with clear explanations of the proposed method and experimental setup.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the trade-offs between computational efficiency and performance. While the authors demonstrate that Skip-Attention achieves significant speedups, they do not provide a comprehensive analysis of how the performance varies with different skipping strategies or the impact of skipping on the model's ability to capture long-range dependencies. Specifically, the paper does not explore the sensitivity of the method to the number of layers skipped, nor does it analyze the impact of skipping on the model's ability to learn hierarchical features. A more thorough investigation into these aspects would be beneficial.
2. The paper does not explore the potential limitations of the proposed method in more complex or diverse datasets. It would be valuable to see how Skip-Attention performs on datasets with different characteristics, such as those with higher resolution images or more complex object relationships. The current evaluation is limited to relatively standard datasets, and it is unclear how the method would perform on more challenging scenarios. For example, the method's performance on datasets with significant occlusions or variations in lighting conditions is not evaluated.
3. The paper does not provide a detailed comparison with other efficient ViT architectures. While the authors mention that their method is orthogonal to other approaches, they do not provide a direct comparison with existing efficient ViT models. A more comprehensive comparison would help to contextualize the contribution of the proposed method and highlight its advantages and disadvantages compared to other state-of-the-art techniques. The paper should include a quantitative comparison with other efficient ViT models, such as those based on depthwise convolutions or other compression techniques.

### Suggestions

The authors should conduct a more thorough analysis of the trade-offs between computational efficiency and performance. This should include a detailed study of how the performance of Skip-Attention varies with different skipping strategies. For example, the authors could investigate the impact of skipping different numbers of layers, or skipping layers based on their importance. Furthermore, it would be beneficial to analyze the impact of skipping on the model's ability to capture long-range dependencies. This could be done by evaluating the model's performance on tasks that require capturing long-range relationships, such as image segmentation or object detection. The authors should also explore the sensitivity of the method to the number of layers skipped and the impact of skipping on the model's ability to learn hierarchical features. This analysis should include a quantitative evaluation of the model's performance on various tasks and datasets, as well as a qualitative analysis of the model's attention maps to understand how skipping affects the model's attention patterns.

To address the limitations regarding dataset diversity, the authors should evaluate the performance of Skip-Attention on more complex and diverse datasets. This should include datasets with higher resolution images, more complex object relationships, and significant occlusions or variations in lighting conditions. For example, the authors could evaluate the method on datasets such as COCO, PASCAL VOC, or other datasets with more complex object relationships. The authors should also compare the performance of Skip-Attention with other efficient ViT models on these datasets. This would help to demonstrate the generalizability and robustness of the method. The evaluation should include a quantitative analysis of the model's performance on various metrics, as well as a qualitative analysis of the model's attention maps to understand how the method performs on complex datasets.

Finally, the authors should provide a more detailed comparison with other efficient ViT architectures. This should include a quantitative comparison with existing efficient ViT models, such as those based on depthwise convolutions or other compression techniques. The comparison should be done on a variety of tasks and datasets to provide a comprehensive evaluation of the proposed method. The authors should also discuss the advantages and disadvantages of their method compared to other state-of-the-art techniques. This comparison should not only focus on the computational efficiency but also on the performance and generalization ability of the models. The authors should also discuss the limitations of their method and suggest potential directions for future research.

### Questions

Please see the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
