### Summary

This paper proposes a novel approach to panoramic image-to-image translation, leveraging the availability of pinhole images as a target domain to address the challenges of geometric distortions and limited datasets. The method incorporates a versatile encoder and spherical positional embedding to bridge the gap between panoramic and pinhole images, along with a distortion-free discrimination technique and panoramic rotation augmentation to handle large domain gaps and discontinuities. The authors validate their approach on the StreetLearn and Init datasets, demonstrating superior results in both quantitative and qualitative assessments.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow. The authors clearly articulate the motivation behind their approach and the technical details of their proposed method. The figures and diagrams effectively illustrate the architecture and the overall workflow, making it easier for readers to understand the key concepts and contributions.

2. The authors provide a thorough experimental evaluation of their method, comparing it against several state-of-the-art image-to-image translation techniques. The results demonstrate that the proposed approach achieves superior performance in both quantitative and qualitative assessments. The ablation studies further validate the effectiveness of the individual components of the model, providing insights into their contributions to the overall performance.

### Weaknesses

#### Some Related Works


#### comment

1. The paper's primary weakness lies in its limited exploration of the practical applications of panoramic image-to-image (Pano-I2I) translation. While the authors mention potential uses, such as immersive view generation and content adaptation, they do not provide concrete examples or detailed discussions on how their method could be applied in real-world scenarios. For instance, the claim that Pano-I2I can be used for novel view synthesis is not sufficiently substantiated, and it is unclear how the proposed method would handle the complexities of real-world scenes, such as varying lighting conditions, occlusions, and complex geometry. A more thorough analysis of the method's limitations and potential failure cases would strengthen the paper.

2. The paper lacks a comprehensive discussion on the computational cost and efficiency of the proposed method. While the authors mention the hardware used for training, they do not provide details on the training time, inference time, or memory requirements. This information is crucial for assessing the practicality of the method, especially for real-time applications. Furthermore, the paper does not compare the computational cost of the proposed method with other state-of-the-art image-to-image translation techniques, making it difficult to evaluate its efficiency relative to existing approaches.

### Suggestions

The authors should significantly expand the discussion on the practical applications of their panoramic image-to-image translation method. While the idea of using pinhole images as a target domain is interesting, the paper needs to provide more concrete examples of how this approach could be used in real-world scenarios. For instance, the authors could explore how their method could be applied in virtual reality (VR) or augmented reality (AR) applications, where immersive view generation is crucial. They should also discuss the challenges of applying their method to real-world scenarios, such as handling complex lighting conditions, occlusions, and varying scene geometries. A more thorough analysis of the method's limitations and potential failure cases would also be beneficial, providing a more balanced view of its capabilities. This could include a discussion of how the method might perform on images with different weather conditions, different camera viewpoints, and complex object arrangements. Furthermore, the authors should consider providing a qualitative analysis of the method's performance on real-world datasets, demonstrating its ability to handle the complexities of real-world scenes.

To address the lack of discussion on computational cost, the authors should provide a detailed analysis of the training and inference times, as well as the memory requirements of their method. This should include a comparison with other state-of-the-art image-to-image translation techniques, demonstrating the efficiency of the proposed method relative to existing approaches. The authors should also discuss the scalability of their method, considering how its performance and computational cost would change with larger datasets and more complex models. This would provide a more comprehensive understanding of the method's practicality for real-world applications. Furthermore, the authors should explore potential optimizations to reduce the computational cost of their method, such as model pruning or quantization, making it more suitable for resource-constrained environments. A detailed breakdown of the computational cost of each component of the model would also be beneficial, allowing readers to understand the bottlenecks and potential areas for optimization.

Finally, the authors should consider providing more details on the hyperparameter tuning process and the sensitivity of the method to different hyperparameter settings. This would help other researchers to effectively use and adapt the method for their own applications. The authors could also explore the use of adaptive hyperparameter tuning techniques, which could further improve the performance of the method. A more detailed analysis of the impact of different hyperparameters on the performance of the method would also be valuable, providing insights into the robustness and generalizability of the method. This could include a sensitivity analysis of the key hyperparameters, demonstrating how they affect the quality of the generated panoramic images.

### Questions

See the weaknesses.

### Rating

6

### Confidence

4

**********
