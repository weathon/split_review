### Summary

This paper investigates the effectiveness of Mamba in 3D volumetric medical image segmentation. The authors address three key questions: Can Mamba replace Transformers for long-range dependency modeling? Can it enhance multi-scale representation learning? Are complex scanning strategies necessary? They conduct experiments on three public datasets (AMOS, TotalSegmentator, and BraTS) and introduce UlikeMamba, a U-shaped Mamba-based network. The findings suggest that Mamba outperforms Transformer-based models in both accuracy and computational efficiency, especially when combined with 3D depthwise convolutions and a multi-scale modeling strategy. The proposed Tri-scan approach further improves performance in complex segmentation tasks. Overall, the study positions Mamba as a promising alternative for 3D medical image segmentation.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper provides a comprehensive evaluation of Mamba's capabilities in 3D medical image segmentation, addressing key questions about its effectiveness compared to Transformers.
2. The introduction of 3D depthwise convolutions and the multi-scale Mamba block are innovative and show improved performance in capturing both fine-grained details and broader anatomical structures.
3. The paper is well-organized and clearly presents its objectives, methodologies, and findings. The experimental setup and results are detailed, allowing for easy understanding of the research process.

### Weaknesses

#### Some Related Works


#### comment

1. While the paper demonstrates Mamba's effectiveness, it could benefit from a more thorough comparison with existing state-of-the-art models beyond the Transformer-based architectures to better contextualize its performance.
2. The paper primarily focuses on segmentation tasks. It would be valuable to explore Mamba's applicability to other medical imaging tasks, such as image registration or generation, to fully understand its potential in the medical domain.

### Suggestions

To strengthen the paper, the authors should include a more comprehensive comparison against a wider range of state-of-the-art segmentation models. While the comparison to Transformer-based architectures is valuable, it is crucial to benchmark against other prominent techniques, such as those based on convolutional neural networks (CNNs) with attention mechanisms, or other sequence modeling approaches like recurrent neural networks (RNNs). This would provide a more complete picture of Mamba's relative performance and help to contextualize its advantages and limitations. For example, comparing against models like nnUNet, which is a widely used baseline in medical image segmentation, would be beneficial. Furthermore, the evaluation should include a variety of metrics beyond Dice score, such as Hausdorff distance and average surface distance, to provide a more comprehensive assessment of segmentation quality. This broader comparison would help to better understand the specific scenarios where Mamba excels and where it may fall short compared to other established methods.

Expanding the scope of the study beyond segmentation tasks would also significantly enhance the paper's impact. The authors should explore the applicability of Mamba to other relevant medical imaging tasks, such as image registration and generation. For image registration, Mamba's ability to model long-range dependencies could be beneficial for aligning images from different modalities or time points. In image generation, Mamba could be used to synthesize realistic medical images for data augmentation or anomaly detection. Investigating these tasks would not only demonstrate the versatility of Mamba but also provide a more comprehensive understanding of its potential in the medical domain. This would also help to position the work more strategically within the broader landscape of medical image analysis research. The authors could consider adapting the UlikeMamba architecture to these tasks and evaluating its performance against existing methods.

Finally, the paper should include a more detailed analysis of the computational cost and memory requirements of the proposed Mamba-based model. While the paper mentions computational efficiency, a more quantitative analysis of parameters such as FLOPs, memory usage, and inference time would be valuable for assessing the practical applicability of the proposed approach. This analysis should also consider the impact of different model sizes and configurations on both performance and computational cost, providing a more nuanced understanding of the trade-offs involved. Such an analysis would be particularly important for medical imaging applications, where computational resources are often limited. Furthermore, the authors should discuss the potential for optimizing the Mamba architecture for specific hardware platforms to improve its efficiency.

### Questions

1. Could the authors provide more detailed comparisons with existing state-of-the-art models beyond Transformers to better contextualize Mamba's performance?
2. Have the authors considered evaluating Mamba's performance on other medical imaging tasks beyond segmentation, such as image registration or generation?

### Rating

6

### Confidence

3

**********
