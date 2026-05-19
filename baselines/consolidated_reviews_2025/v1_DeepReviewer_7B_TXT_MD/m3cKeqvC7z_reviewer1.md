### Summary

This paper explores the application of Mamba models for 3D medical image segmentation. It addresses three key questions: whether Mamba can replace Transformers, how it enhances multi-scale representation learning, and whether complex scanning strategies are necessary. The authors propose a U-shaped network with Mamba-based layers, incorporating 3D depthwise convolutions, multi-scale modeling, and a Tri-scan scanning strategy. Experiments on AMOS, TotalSegmentator, and BraTS datasets demonstrate that their approach achieves competitive accuracy and computational efficiency, outperforming advanced models like nnUNet and CoTr.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper is well-structured and easy to follow.
2. The authors conduct a comprehensive analysis of Mamba's potential in 3D medical image segmentation, addressing key questions and providing valuable insights.

### Weaknesses

#### Some Related Works


#### comment

1. The paper's primary contribution is the design of a U-shaped Mamba network with specific modifications, such as 3D depthwise convolutions, multi-scale modeling, and Tri-scan scanning. However, these modifications are incremental and lack substantial novelty. The use of 3D depthwise convolutions, while potentially beneficial for capturing spatial relationships, does not introduce a fundamentally new approach to feature extraction. Similarly, the multi-scale modeling and Tri-scan scanning, while empirically shown to improve performance, are not novel techniques in themselves, but rather specific implementations within the Mamba architecture. The paper does not adequately explore the theoretical underpinnings of why these specific combinations are optimal for 3D medical image segmentation, nor does it provide a detailed analysis of the computational trade-offs associated with these modifications.
2. The experiments are primarily conducted on three public datasets: AMOS, TotalSegmentator, and BraTS. While these datasets are relevant, the evaluation lacks diversity in terms of data types and modalities. The paper would benefit from testing the proposed method on a wider range of datasets, including those with different image characteristics and segmentation challenges, to demonstrate the generalizability of the approach. Furthermore, the paper does not provide a detailed analysis of the performance on different classes within the segmentation masks, which could reveal potential biases or limitations of the proposed method.

### Suggestions

To enhance the paper's contribution, the authors should delve deeper into the theoretical justification for their architectural choices. Instead of simply demonstrating that a U-shaped Mamba network with 3D depthwise convolutions, multi-scale modeling, and Tri-scan scanning performs well, they should provide a more in-depth analysis of why these specific combinations are effective for 3D medical image segmentation. This could involve exploring the spectral properties of the 3D depthwise convolutions, analyzing the receptive fields of the multi-scale modeling, and providing a theoretical framework for the Tri-scan scanning strategy. Furthermore, the authors should conduct a more thorough ablation study to isolate the impact of each modification, demonstrating the specific contribution of each component to the overall performance. This would help to clarify whether the observed improvements are due to the specific combination of techniques or if any of the individual components are redundant. The paper should also include a detailed analysis of the computational trade-offs associated with each modification, providing a clear understanding of the efficiency gains and losses.

To address the lack of diversity in the evaluation, the authors should consider including additional datasets that represent a wider range of medical imaging modalities and segmentation challenges. This could include datasets with different image resolutions, noise levels, and anatomical structures. Furthermore, the authors should provide a more detailed analysis of the performance on different classes within the segmentation masks, which could reveal potential biases or limitations of the proposed method. This analysis should include a discussion of the types of errors that the model makes, and how these errors might be addressed in future work. The authors should also consider comparing their method to other state-of-the-art segmentation techniques, including both Transformer-based and CNN-based approaches, to provide a more comprehensive evaluation of their method's performance. This would help to establish the relative strengths and weaknesses of their approach compared to existing methods.

Finally, the authors should provide a more detailed discussion of the limitations of their approach and potential avenues for future research. This could include addressing the computational cost of the proposed method, exploring alternative architectures for the Mamba network, and investigating the robustness of the method to different types of noise and artifacts. The authors should also discuss the potential impact of their work on the field of medical image segmentation, and how their method could be used to improve the accuracy and efficiency of clinical workflows. This would help to contextualize their work and highlight its potential significance.

### Questions

1. The paper focuses on 3D medical image segmentation, but it would be beneficial to discuss how the proposed method could be adapted or extended to other volumetric data modalities, such as CT or MRI scans.
2. The experiments are conducted on three public datasets, but it would be helpful to see how the method performs on datasets with different characteristics or modalities.

### Rating

5

### Confidence

4

**********
