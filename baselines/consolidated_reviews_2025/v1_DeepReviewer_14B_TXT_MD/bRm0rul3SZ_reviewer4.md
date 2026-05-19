### Summary

This paper proposes a novel image-to-image translation model for translating panoramic images to pinhole images. The proposed model uses a versatile encoder and distortion-free discrimination to bridge the large domain gap between the two types of images. The model also uses spherical position embedding, sphere-based rotation augmentation, and ensemble techniques to address the discontinuities at the panorama edges. The proposed model is evaluated on the StreetLearn dataset and shows superior results in both maintaining structural coherence and rotation equivariance, clearly surpassing the existing I2I methods in qualitative and quantitative results.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper proposes a novel image-to-image translation model for translating panoramic images to pinhole images. The proposed model uses a versatile encoder and distortion-free discrimination to bridge the large domain gap between the two types of images. The model also uses spherical position embedding, sphere-based rotation augmentation, and ensemble techniques to address the discontinuities at the panorama edges. 
2. The proposed model is evaluated on the StreetLearn dataset and shows superior results in both maintaining structural coherence and rotation equivariance, clearly surpassing the existing I2I methods in qualitative and quantitative results.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational complexity of the proposed framework, which is an important factor to consider when evaluating the practicality of the method.
2. The paper does not discuss the limitations of the proposed framework, which is important for understanding the scope and applicability of the method.

### Suggestions

The paper should include a more thorough analysis of the computational demands of the proposed framework. Specifically, the authors should provide a breakdown of the time and memory requirements for each stage of the pipeline, including the deformable convolution, transformer encoder, and distortion-free discrimination. This analysis should not only report the overall training and inference times but also detail the FLOPs and memory footprint of each component. Furthermore, it would be beneficial to compare the computational cost of the proposed method with existing image-to-image translation techniques, providing a clear understanding of the trade-offs between performance and computational resources. This would allow readers to assess the practicality of the method for different applications and hardware setups. For example, reporting the training time per epoch on a specific GPU and the inference time for a single image would be very useful.

In addition to the computational analysis, the paper should also discuss the limitations of the proposed framework in more detail. The authors should explore the scenarios where the method might fail or produce suboptimal results. For instance, how does the framework perform when dealing with highly dynamic scenes, such as fast-moving objects or changing lighting conditions? It would also be valuable to investigate the robustness of the method to different types of input distortions, such as blur, noise, or compression artifacts. Furthermore, the authors should discuss the limitations of the spherical position embedding and sphere-based rotation augmentation, and how these techniques might affect the quality of the generated panoramas in certain cases. A discussion of the potential failure modes and limitations would provide a more complete picture of the method's capabilities and applicability.

Finally, the paper should include a more detailed discussion of the potential applications of the proposed framework. While the authors mention virtual reality and panoramic image editing, they should provide more concrete examples and use cases. For instance, how could this method be used in autonomous driving or robotics? What are the specific advantages of using this method over existing techniques in these applications? The authors should also discuss the potential for extending the framework to other types of image-to-image translation tasks, such as translating between different types of panoramic projections or between panoramic and perspective views. A more detailed discussion of the potential applications and extensions would highlight the broader impact of the proposed method.

### Questions

Please see the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
