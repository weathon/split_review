### Summary

This paper proposes a two-stage inverse rendering framework that reconstructs and optimizes explicit geometry, materials, and lighting from multi-view images. The method uses multi-bounce path tracing and Monte Carlo integration for more realistic rendering, and incorporates reservoir sampling to reduce noise and enhance convergence. The paper demonstrates state-of-the-art performance in decomposition results, especially in complex shadow scenarios, and supports further applications like scene editing, relighting, and material editing.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The idea of using reservoir sampling to reduce the variance of direct lighting estimation is reasonable.
3. The idea of using explicit mesh-based representation to perform path tracing to estimate indirect lighting is reasonable.
4. The paper provides both qualitative and quantitative comparisons to demonstrate the performance of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a comparison of the training time of the proposed method with existing methods.
2. The paper does not provide a comparison of the inference time of the proposed method with existing methods.
3. The paper does not provide a comparison of the memory usage of the proposed method with existing methods.
4. The paper does not provide a comparison of the scalability of the proposed method with existing methods.

### Suggestions

The paper would benefit from a more thorough analysis of the computational costs associated with the proposed method. Specifically, a detailed breakdown of the training time, including the time spent on each stage of the two-stage inverse rendering framework, should be provided. This should include the time for geometry reconstruction, material estimation, and lighting optimization. Furthermore, it would be beneficial to compare the training time with other state-of-the-art methods, not just in terms of total time, but also in terms of the time spent on each component. This would allow for a better understanding of the computational bottlenecks of the proposed method and how it compares to existing approaches. For example, providing a table that shows the time spent on mesh optimization, material parameter estimation, and lighting optimization for both the proposed method and other methods would be very helpful.

In addition to training time, the paper should also include a detailed analysis of the inference time. This should include the time required to render a single image or a sequence of images using the reconstructed geometry, materials, and lighting. It would be useful to compare the inference time with other methods, especially those that use different rendering techniques. The paper should also discuss the factors that affect the inference time, such as the complexity of the scene, the number of light bounces, and the resolution of the output image. Furthermore, the paper should explore the trade-offs between inference time and rendering quality. For example, it would be interesting to see how the inference time changes when using different numbers of samples for Monte Carlo integration or different levels of detail for the mesh representation. This analysis would provide a more complete picture of the practical applicability of the proposed method.

Finally, the paper should provide a more detailed analysis of the memory usage of the proposed method. This should include the memory required to store the mesh, material parameters, and lighting information. It would be useful to compare the memory usage with other methods, especially those that use different scene representations. The paper should also discuss the factors that affect the memory usage, such as the complexity of the scene, the number of vertices in the mesh, and the number of parameters used to represent the materials and lighting. Furthermore, the paper should explore the trade-offs between memory usage and rendering quality. For example, it would be interesting to see how the memory usage changes when using different levels of detail for the mesh representation or different numbers of parameters to represent the materials and lighting. This analysis would provide a better understanding of the resource requirements of the proposed method and its suitability for different applications.

### Questions

Please refer to the weakness part.

### Rating

6

### Confidence

4

**********
