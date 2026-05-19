### Summary

This paper proposes a two-stage inverse rendering framework that jointly optimizes explicit geometry, materials, and lighting from multi-view images. The method uses a triangle mesh to represent geometry, which is refined through a physically-based inverse rendering model using multi-bounce path tracing and reservoir sampling. The method achieves state-of-the-art performance in both decomposition and relighting, and demonstrates applications in scene editing, relighting, and material editing.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method achieves state-of-the-art performance in both decomposition and relighting.
3. The paper provides a comprehensive comparison with existing methods, including both implicit and explicit representations.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is computationally intensive, requiring over 4.5 hours to train on a single NVIDIA RTX 4090 GPU. This high computational cost may limit its applicability in real-world scenarios, especially for large-scale scenes or real-time applications.
2. The paper lacks a thorough analysis of the impact of different mesh resolutions on the final reconstruction quality. It is unclear how the choice of mesh resolution affects the accuracy and detail of the reconstructed geometry, materials, and lighting. A more detailed investigation into this aspect would be beneficial.
3. The paper does not provide a detailed discussion of the limitations of the proposed method. For example, how does the method perform under different lighting conditions, such as strong shadows or complex occlusions? What are the failure cases of the method, and how can they be addressed in future work?

### Suggestions

The paper would benefit from a more detailed analysis of the computational cost associated with the proposed method. While the authors mention the training time, a breakdown of the time spent on different stages of the pipeline would be valuable. This would help identify potential bottlenecks and areas for optimization. For example, the time spent on mesh refinement, physically-based rendering, and reservoir sampling should be quantified. Furthermore, the authors should compare the computational cost of their method with other state-of-the-art inverse rendering techniques, not just in terms of training time, but also in terms of inference time and memory usage. This would provide a more comprehensive understanding of the trade-offs between performance and computational efficiency. The authors should also investigate the scalability of their method to larger and more complex scenes, as the current experiments are limited to relatively small datasets. This would help assess the practical applicability of the method in real-world scenarios.

To address the lack of analysis on mesh resolution, the authors should conduct a series of experiments with varying mesh resolutions and report the impact on the reconstruction quality. This should include a quantitative analysis of the geometric accuracy, material properties, and lighting quality. It would also be helpful to visualize the reconstructed results at different resolutions to provide a qualitative assessment of the impact of mesh resolution. The authors should also discuss the trade-offs between mesh resolution and computational cost, as higher resolution meshes may lead to better reconstruction quality but also increased computational burden. Furthermore, the authors should investigate the optimal mesh resolution for different types of scenes and lighting conditions. This would provide a more complete understanding of the method's behavior and limitations. The authors should also consider adaptive mesh refinement techniques that can dynamically adjust the mesh resolution based on the complexity of the scene and the desired level of detail.

Finally, the paper needs a more thorough discussion of the limitations of the proposed method. The authors should provide a qualitative analysis of the reconstructed results under various challenging conditions, such as strong shadows, complex occlusions, and non-Lambertian surfaces. The authors should also discuss the potential failure modes of the method and suggest possible solutions for addressing these issues. For example, the authors could explore techniques for handling strong shadows, such as using a more robust inverse rendering model or incorporating additional constraints. They could also investigate methods for handling complex occlusions, such as using a more sophisticated inpainting technique or incorporating additional information about the scene. The authors should also discuss the limitations of the method in terms of material properties, such as the ability to handle non-Lambertian surfaces or complex BRDFs. This would help to provide a more balanced and realistic assessment of the method's capabilities and limitations.

### Questions

Please refer to the weaknesses.

### Rating

6

### Confidence

3

**********
