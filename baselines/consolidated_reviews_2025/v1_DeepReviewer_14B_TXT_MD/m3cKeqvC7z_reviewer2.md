### Summary

This paper investigates the potential of Mamba for 3D volumetric medical image segmentation. The authors address three main questions: whether Mamba can replace Transformers, enhance multi-scale representation learning, and whether complex scanning strategies are necessary. They conduct experiments on three public datasets (AMOS, TotalSegmentator, and BraTS) comparing a Mamba-based network (UlikeMamba) with a Transformer-based network (UlikeTrans). The key findings suggest that Mamba, especially when combined with 3D depthwise convolutions and a multi-scale block, outperforms Transformer-based models in accuracy and computational efficiency. They also propose a Tri-scan approach that improves performance in complex segmentation tasks.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper provides a comprehensive analysis of Mamba's capabilities in 3D medical image segmentation, addressing key questions about its effectiveness compared to Transformers.
2. The introduction of 3D depthwise convolutions and the multi-scale Mamba block are innovative and show improved performance in capturing both fine-grained details and broader anatomical structures.
3. The paper is well-organized and clearly presents its objectives, methodologies, and findings. The experimental setup and results are detailed, allowing for easy understanding of the research process.

### Weaknesses

#### Some Related Works


#### comment

1. While the paper demonstrates Mamba's effectiveness, it could benefit from a more thorough comparison with existing state-of-the-art models beyond the Transformer-based architectures to better contextualize its performance.
2. The paper primarily focuses on segmentation tasks. It would be valuable to explore Mamba's applicability to other medical imaging tasks, such as image registration or generation, to fully understand its potential in the medical domain.

### Suggestions

The paper would significantly benefit from a more comprehensive comparison against a wider range of state-of-the-art segmentation models, not just those based on Transformers. Specifically, including comparisons with models that utilize recurrent neural networks (RNNs) or other sequence modeling techniques, which are also relevant for capturing long-range dependencies, would provide a more complete picture of Mamba's relative performance. Furthermore, the evaluation should include models that employ different architectural designs, such as those based on convolutional neural networks (CNNs) with attention mechanisms, to assess whether Mamba's improvements are specific to comparisons with Transformers or are more general. This broader comparison would help to better contextualize the advantages and limitations of the proposed Mamba-based approach. The current evaluation, while thorough in its comparison to Transformers, leaves open the question of whether Mamba truly represents a significant advancement over other existing segmentation techniques.

To further strengthen the paper, the authors should explore the potential of Mamba in other medical imaging tasks beyond segmentation. While segmentation is a crucial task, the ability of Mamba to model long-range dependencies could be highly beneficial in tasks such as image registration, where aligning images from different modalities or time points requires capturing complex spatial relationships. Similarly, investigating Mamba's performance in image generation tasks, such as synthesizing medical images for data augmentation or anomaly detection, could reveal its versatility and potential impact in the medical domain. Exploring these additional tasks would not only broaden the scope of the paper but also provide a more comprehensive understanding of Mamba's capabilities and limitations in medical image analysis. This would also help to position the work more strategically within the broader landscape of medical image analysis research.

Finally, the paper should include a more detailed analysis of the computational cost and memory requirements of the proposed Mamba-based model, especially when compared to other state-of-the-art segmentation models. While the paper mentions computational efficiency, a more quantitative analysis of parameters such as FLOPs, memory usage, and inference time would be valuable for assessing the practical applicability of the proposed approach. This analysis should also consider the impact of different model sizes and configurations on both performance and computational cost, providing a more nuanced understanding of the trade-offs involved. Such an analysis would be particularly important for medical imaging applications, where computational resources are often limited.

### Questions

See Weaknesses.

### Rating

5

### Confidence

3

**********
