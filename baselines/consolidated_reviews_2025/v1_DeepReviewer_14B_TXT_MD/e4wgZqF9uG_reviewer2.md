### Summary

The paper investigates the potential of using monocular depth estimation as a pre-training task to enhance semantic segmentation. The authors propose that pre-training on depth prediction could provide a geometric understanding of scenes, which could benefit semantic segmentation. They conduct experiments using various datasets and architectures, comparing depth pre-training to traditional methods like ImageNet classification. The results indicate that depth pre-training can improve semantic segmentation performance, particularly in scenarios with limited labeled data. The paper also explores the impact of different factors, such as dataset size, resolution, and architecture, on the effectiveness of depth pre-training.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper presents a novel approach to pre-training for semantic segmentation using monocular depth estimation, which is a creative combination of geometric and semantic tasks.
2. The authors provide a comprehensive experimental evaluation, including ablation studies and comparisons with other pre-training methods, which strengthens the validity of their findings.
3. The research has the potential to reduce the reliance on large, human-annotated datasets for pre-training, which could be particularly beneficial for specialized domains where labeled data is scarce.

### Weaknesses

#### Some Related Works


#### comment

1. The paper's focus on specific datasets and architectures might limit the generalizability of the findings. It is unclear how the proposed approach would perform on a wider range of datasets and tasks. The experiments are primarily conducted on KITTI, Cityscapes, and NYU-V2, which are all urban driving datasets. This narrow focus raises concerns about the robustness of the conclusions when applied to more diverse scenarios, such as indoor environments, rural scenes, or datasets with different sensor modalities. The paper lacks a thorough investigation into how the pre-training performance varies across datasets with different characteristics, such as image resolution, object scale, and scene complexity.
2. The comparison with other pre-training methods is limited. While the paper compares against ImageNet pre-training, it does not explore other recent self-supervised learning techniques that have shown promise in representation learning. This omission makes it difficult to assess the relative advantages and disadvantages of depth pre-training compared to state-of-the-art methods. For example, contrastive learning methods, which have demonstrated strong performance in various vision tasks, are not considered.
3. The paper could benefit from a more in-depth analysis of the learned representations. It is not entirely clear what specific aspects of the depth information are most beneficial for semantic segmentation. The paper does not provide a detailed analysis of the feature maps learned during depth pre-training, nor does it explore the correlation between depth estimation accuracy and semantic segmentation performance. It remains unclear whether the improvement in segmentation is due to the geometric understanding provided by depth or other factors.

### Suggestions

To address the limitations in dataset generalizability, the authors should conduct experiments on a more diverse set of datasets. This should include datasets with varying characteristics, such as indoor scenes (e.g., ScanNet, S3DIS), rural environments (e.g., Fields, Farms, and Forests), and datasets with different sensor modalities (e.g., thermal images, LiDAR). Furthermore, the authors should analyze how the performance of depth pre-training varies across these datasets, and investigate the factors that contribute to these variations. This analysis should include a detailed examination of the dataset characteristics, such as image resolution, object scale, and scene complexity, and how these factors interact with the depth pre-training process. Such an analysis would provide a more comprehensive understanding of the generalizability of the proposed approach and identify potential limitations.

To provide a more thorough comparison with other pre-training methods, the authors should include experiments with recent self-supervised learning techniques. This should include contrastive learning methods, such as MoCo or SimCLR, and generative models, such as VQ-VAE or GANs. The comparison should not only focus on the final performance on semantic segmentation but also analyze the learned representations and their properties. For example, the authors could compare the feature maps learned by depth pre-training with those learned by contrastive learning, and investigate the differences in their ability to capture semantic information. This would provide a more comprehensive understanding of the relative advantages and disadvantages of depth pre-training compared to other state-of-the-art methods. The authors should also explore the impact of different pre-training dataset sizes and compositions on the final performance.

To gain a deeper understanding of the learned representations, the authors should conduct a more detailed analysis of the feature maps learned during depth pre-training. This could include visualizing the feature maps, analyzing their activation patterns, and investigating their correlation with depth and semantic information. The authors should also explore the relationship between depth estimation accuracy and semantic segmentation performance. For example, they could investigate whether improvements in segmentation are correlated with improvements in depth estimation accuracy, or whether other factors are more important. This analysis should also include an investigation into the specific aspects of depth information that are most beneficial for semantic segmentation. For instance, the authors could explore whether the improvement is due to the overall geometric understanding provided by depth, or whether specific depth features, such as object boundaries or surface normals, are more important.

### Questions

1. How does the performance of depth pre-training compare to other recent self-supervised learning methods, such as contrastive learning or generative models?
2. Can the authors provide insights into the specific features or aspects of depth information that contribute most to the improvement in semantic segmentation?
3. How does the choice of architecture for the depth estimation task affect the quality of the learned representations for semantic segmentation?
4. What are the computational costs associated with depth pre-training compared to other pre-training methods, and how does this impact the practicality of the approach?

### Rating

6

### Confidence

3

**********
