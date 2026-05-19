### Summary

This paper presents a novel two-stage inverse rendering framework that jointly reconstructs and optimizes explicit geometry, materials, and lighting from multi-view images. Unlike previous methods that rely on implicit irradiance fields or oversimplified path tracing algorithms, this approach first extracts an explicit triangular mesh in the initial stage. Subsequently, it employs a more realistic physically-based inverse rendering model in the second stage, utilizing multi-bounce path tracing and Monte Carlo integration. By leveraging multi-bounce path tracing, the method effectively estimates indirect illumination (including self-shadowing and internal reflections) and enhances the intrinsic decomposition of shape, material, and lighting. Moreover, the incorporation of reservoir sampling into the framework addresses the noise in Monte Carlo integration, enhancing convergence and facilitating gradient-based optimization with low sample counts. The paper demonstrates that the method achieves state-of-the-art performance in decomposition results, especially in scenarios with complex shadows. Additionally, the optimized explicit geometry supports further applications in scene editing, relighting, and material editing, compatible with modern graphics engines and CAD software.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel two-stage inverse rendering framework that combines explicit mesh representation with physically-based rendering techniques, including multi-bounce path tracing and reservoir sampling. This approach addresses the limitations of previous methods that rely on implicit representations or simplified path tracing, offering a more accurate and realistic solution for inverse rendering.
2. The method achieves state-of-the-art performance in decomposition results, particularly in complex shadow scenarios. The use of multi-bounce path tracing and reservoir sampling contributes to more accurate estimation of indirect illumination and enhances the overall quality of the reconstructed geometry, materials, and lighting.
3. The paper is well-organized and clearly presents the methodology, experiments, and results. The figures and tables effectively illustrate the performance of the proposed method compared to existing approaches, making it easy for readers to understand the contributions and advantages of the work.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a comparison of the training time of the proposed method with existing methods. It is crucial to understand the computational cost of the proposed approach relative to state-of-the-art techniques. The absence of this comparison makes it difficult to assess the practical applicability of the method, especially in scenarios where computational resources are limited or real-time performance is desired. A detailed breakdown of the time spent on each stage of the pipeline, such as mesh extraction, material estimation, and lighting optimization, would be beneficial.
2. The paper does not provide a comparison of the inference time of the proposed method with existing methods. While training time is important, the inference time is equally critical for practical applications. The paper should include a thorough analysis of the rendering speed of the proposed method, including the time required to generate a single rendered image or a sequence of images. This analysis should consider different scene complexities and rendering resolutions to provide a comprehensive understanding of the method's performance.
3. The paper does not provide a comparison of the memory usage of the proposed method with existing methods. Memory consumption is a significant factor, especially when dealing with complex scenes or high-resolution data. The paper should include a detailed analysis of the memory footprint of the proposed method, including the memory required for storing the mesh, material properties, and lighting information. This analysis should be compared with existing methods to understand the trade-offs between memory usage and performance.
4. The paper does not provide a comparison of the scalability of the proposed method with existing methods. It is important to understand how the method performs as the complexity of the scene increases. The paper should include experiments that evaluate the performance of the method on scenes with varying levels of geometric detail and material complexity. This analysis should consider the impact of scene complexity on training time, inference time, and memory usage.

### Suggestions

To address the lack of training time comparisons, the authors should include a detailed breakdown of the computational cost of each stage of their pipeline. This should include the time spent on mesh extraction, material estimation, and lighting optimization. Furthermore, it would be beneficial to compare the training time of their method with existing state-of-the-art inverse rendering techniques, using a consistent hardware setup and dataset. This comparison should not only focus on the total training time but also analyze the time spent on each component of the pipeline. For example, the authors could provide a table that shows the time spent on mesh optimization, material parameter estimation, and lighting optimization for both their method and other methods. This would allow for a more granular understanding of the computational bottlenecks and advantages of their approach. Additionally, the authors should consider providing a scalability analysis of the training time, showing how the training time increases with the complexity of the scene.

Regarding inference time, the authors should provide a comprehensive analysis of the rendering speed of their method. This should include the time required to generate a single rendered image or a sequence of images, considering different scene complexities and rendering resolutions. The analysis should also compare the inference time of their method with existing state-of-the-art techniques, using a consistent hardware setup and dataset. Furthermore, the authors should investigate the impact of different rendering parameters, such as the number of samples used for Monte Carlo integration, on the inference time. This would provide a more complete understanding of the trade-offs between rendering quality and speed. The authors could also explore the potential for optimizing the rendering process, such as using adaptive sampling techniques or pre-computing certain aspects of the rendering pipeline.

Finally, the authors should provide a detailed analysis of the memory usage of their method, including the memory required for storing the mesh, material properties, and lighting information. This analysis should be compared with existing methods to understand the trade-offs between memory usage and performance. The authors should also investigate the scalability of the memory usage, showing how the memory footprint increases with the complexity of the scene. This analysis should consider the impact of different scene complexities and rendering resolutions on memory usage. Furthermore, the authors should explore potential strategies for reducing the memory footprint of their method, such as using more efficient data structures or compression techniques. This would make their method more practical for use in resource-constrained environments.

### Questions

1. Could the authors provide a comparison of the training time of the proposed method with existing methods?
2. Could the authors provide a comparison of the inference time of the proposed method with existing methods?
3. Could the authors provide a comparison of the memory usage of the proposed method with existing methods?
4. Could the authors provide a comparison of the scalability of the proposed method with existing methods?

### Rating

6

### Confidence

4

**********
