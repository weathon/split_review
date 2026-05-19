### Summary

This paper investigates the potential of Mamba, a State Space Model (SSM), for 3D volumetric medical image segmentation. The authors compare Mamba-based networks to Transformer-based architectures, focusing on accuracy and computational efficiency across three public benchmarks: AMOS, TotalSegmentator, and BraTS. They introduce a U-shaped Mamba-based network, UlikeMamba, which incorporates custom-designed 3D depthwise convolutions and a multi-scale Mamba block to enhance feature representation. The study explores different scanning strategies, including single-scan, dual-scan, and a novel Tri-scan approach, to optimize spatial relationship modeling. Results indicate that UlikeMamba outperforms Transformer-based models, including nnUNet, CoTr, and U-Mamba, in both accuracy and efficiency. This work positions Mamba as a promising alternative for long-range dependency modeling in medical imaging.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. This paper provides a comprehensive evaluation of Mamba in 3D medical image segmentation, addressing key questions about its effectiveness, particularly in comparison to Transformer-based methods. 

2. The introduction of the Tri-scan approach and multi-scale Mamba block demonstrates improved performance in capturing spatial relationships and multi-scale features, which is crucial for complex segmentation tasks.

### Weaknesses

#### Some Related Works


#### comment

1. The introduction of the MSv4 module and Tri-scan strategy results in increased computational demands. 

2. The paper primarily focuses on comparisons with Transformer-based models and established CNN architectures. It lacks comparative analysis with other recent state-of-the-art models in medical image segmentation, such as those based on diffusion models or other recent advances beyond Transformers.

3. The paper does not provide detailed information on the number of scanning directions, their specific configurations, or the computational trade-offs associated with different scanning strategies. This makes it challenging to fully understand the implications of the proposed Tri-scan approach.

4. The study could benefit from providing more detailed insights into how Mamba captures long-range dependencies compared to Transformers, particularly in the context of 3D volumetric data. A more in-depth analysis of the underlying mechanisms would strengthen the claims made about Mamba's advantages.

### Suggestions

The paper would benefit from a more thorough analysis of the computational costs associated with the proposed MSv4 and Tri-scan strategies. While the authors acknowledge increased computational demands, a detailed breakdown of FLOPs, memory usage, and inference time for each component would be valuable. Specifically, the paper should quantify the overhead introduced by the multi-scale module (MSv4) and the three scanning directions of the Tri-scan approach, compared to a baseline Mamba model without these enhancements. This analysis should also consider the impact of these choices on different hardware platforms, such as GPUs with varying memory capacities. Furthermore, it would be beneficial to explore potential optimizations to mitigate the computational burden, such as pruning or quantization techniques, to make the model more practical for real-world applications.

To strengthen the paper's claims, a more comprehensive comparison with recent state-of-the-art models in medical image segmentation is needed. While the authors compare against Transformer-based models and established CNN architectures, the field has seen rapid advancements in other areas, such as diffusion models and models leveraging contrastive learning. Including a comparative analysis with these models would provide a more complete picture of the proposed method's performance relative to the current state of the art. This comparison should not only focus on segmentation accuracy but also consider other relevant metrics, such as robustness to noise, generalization to unseen data, and computational efficiency. Furthermore, the paper should discuss the specific advantages and disadvantages of Mamba compared to these alternative approaches, providing a more nuanced understanding of its potential impact.

Finally, the paper should provide a more detailed explanation of the scanning strategies employed by the Mamba model, particularly the Tri-scan approach. The current description lacks clarity regarding the specific order and direction of the scans, and how these choices impact the model's ability to capture spatial relationships. A more detailed explanation should include a visual representation of the scanning paths, as well as a discussion of the rationale behind the chosen scanning order. Furthermore, the paper should analyze the computational trade-offs associated with different scanning strategies, including the impact on FLOPs, memory usage, and inference time. This analysis should also consider the potential for adaptive scanning strategies that dynamically adjust the scanning pattern based on the input data, which could further improve the model's efficiency and performance.

### Questions

1. Could the authors provide more detailed comparisons with recent state-of-the-art models in medical image segmentation, particularly those that are not Transformer-based? 

2. Can the authors elaborate on the specific configurations and computational trade-offs of the different scanning strategies, especially the novel Tri-scan approach?

3. How does the paper address the increased computational demands introduced by the MSv4 module and Tri-scan strategy, particularly in resource-constrained environments?

### Rating

3

### Confidence

4

**********
