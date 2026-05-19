### Summary

This paper explores the potential of pre-training on geometric tasks, specifically monocular depth estimation, as a pathway to downstream transfer for semantic segmentation. The authors investigate different forms of supervision, including multi-view stereo, binocular stereo, and LiDAR data, and compare pre-training against baselines like ImageNet pre-training and no pre-training. The experiments are conducted using ResNet and DeepLabv3 architectures on KITTI, Cityscapes, and NYUv2 datasets. The results indicate that monocular depth pre-training can improve semantic segmentation performance, often outperforming ImageNet pre-training. The authors also explore the impact of various factors, such as training set size and network architecture, on the effectiveness of the proposed approach.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-organized and easy to follow, with clear explanations of the methodology and experimental setup. The authors provide a comprehensive overview of the related work and clearly articulate the motivation for their study.
2. The authors conduct a thorough set of experiments, covering various aspects of the proposed approach, including different forms of supervision, network architectures, and datasets. The results are presented clearly and are supported by appropriate visualizations.
3. The paper provides valuable insights into the potential of geometric pre-training for semantic segmentation. The findings suggest that pre-training on monocular depth estimation can be an effective strategy for improving downstream segmentation performance, particularly when compared to ImageNet pre-training.

### Weaknesses

#### Some Related Works


#### comment

1. The paper's motivation is not entirely clear. While the authors claim that monocular depth pre-training can provide a "human-free" approach to learning semantic concepts, it is not evident how this is achieved. The paper does not adequately explain the connection between depth estimation and the emergence of semantic understanding. Specifically, the paper lacks a clear explanation of how the geometric cues from depth estimation translate into the semantic features required for segmentation. The claim of a "human-free" approach is not well-supported by the methodology, as the depth estimation itself is trained on human-annotated data, even if it avoids human labeling in the downstream task.
2. The paper does not provide a clear definition of what constitutes "semantic understanding" in the context of this study. The authors use the term "semantic understanding" to refer to the emergence of "object-centric bias" in the feature space, but this definition is not sufficiently rigorous. The paper needs to clarify what specific properties of the learned features indicate that they are capturing semantic information, rather than just low-level geometric features. The connection between the learned features and the actual semantic labels is not clearly established.
3. The paper does not adequately address the potential limitations of the proposed approach. For example, it is not clear how the method would perform in scenarios with significant occlusions or lighting variations. The paper should discuss the robustness of the method to these challenges and provide some analysis of its performance under such conditions. Furthermore, the paper does not explore the computational cost of the proposed approach, which could be a limiting factor for practical applications.

### Suggestions

The paper would benefit from a more precise definition of "semantic understanding" and a more rigorous explanation of how depth estimation contributes to this understanding. The authors should clarify what specific properties of the learned features indicate that they are capturing semantic information, rather than just low-level geometric features. For example, they could analyze the feature maps to show how they respond to different object categories or scene contexts. This could involve techniques such as visualizing the activation maps or using probing techniques to assess the semantic content of the features. Furthermore, the authors should provide a more detailed explanation of how the geometric cues from depth estimation translate into the semantic features required for segmentation. This could involve analyzing the relationship between the depth maps and the resulting semantic predictions, and explaining how the depth information helps the network learn object-centric biases.

To address the limitations of the proposed approach, the authors should conduct a more thorough analysis of its robustness to various challenges, such as occlusions, lighting variations, and different viewpoints. This could involve testing the method on datasets with more diverse and challenging scenes, and providing a quantitative analysis of its performance under these conditions. The authors should also discuss the computational cost of the proposed approach and compare it to other pre-training methods. This would help to assess the practical feasibility of the method for real-world applications. Additionally, the authors should explore the potential of combining depth pre-training with other pre-training techniques, such as those based on image classification or object detection. This could lead to further improvements in segmentation performance and provide a more comprehensive understanding of the benefits of geometric pre-training.

Finally, the authors should clarify the connection between their findings and the broader context of geometric perception. While the paper focuses on the potential of depth pre-training for semantic segmentation, it should also discuss how this approach relates to other research in the field of geometric perception. This could involve comparing the proposed method to other approaches that use geometric cues for learning, and highlighting the unique contributions of the paper. The authors should also discuss the limitations of their approach in the context of the broader field of geometric perception, and suggest directions for future research. This would help to position the paper within the larger research landscape and highlight its significance.

### Questions

1. How does the proposed method compare to other pre-training approaches for semantic segmentation, such as those based on image classification or object detection? Are there any specific advantages or disadvantages of using depth pre-training compared to these other methods?
2. How does the method perform on datasets with more diverse and challenging scenes, such as those with significant occlusions or lighting variations?
3. What is the computational cost of the proposed approach, and how does it compare to other pre-training methods?

### Rating

5

### Confidence

4

**********
