### Summary

This paper introduces a novel approach for dynamic scene representation and rendering using 4D Gaussian splatting. The authors propose a method to model the spatio-temporal volume of dynamic scenes with 4D Gaussians, extending traditional 3D Gaussian Splatting techniques to incorporate temporal dimension. The paper also introduces 4D Spherical Harmonics to model the time-evolving appearance of the 4D Gaussians, enhancing the realism of dynamic scene synthesis. The proposed method is evaluated on both synthetic and real-world datasets, demonstrating superior visual quality and efficiency compared to existing methods.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper presents a novel approach to dynamic scene representation by introducing 4D Gaussian splatting, which extends the existing 3D Gaussian Splatting technique to model the spatio-temporal volume of dynamic scenes. This approach is innovative and provides a new way to represent and render dynamic scenes.
- The authors introduce 4D Spherical Harmonics to model the time-evolving appearance of the 4D Gaussians, which enhances the realism of dynamic scene synthesis. This is a significant contribution to the field of dynamic scene rendering.
- The paper is well-written and easy to follow. The authors provide clear explanations of the proposed method and its components, making it accessible to readers with a background in computer graphics or machine learning.

### Weaknesses

#### Some Related Works


#### comment

 - The paper lacks a detailed analysis of the computational complexity and efficiency of the proposed method. While the authors claim that their method is real-time, there is no quantitative analysis of the computational cost, memory usage, or rendering speed compared to other methods. This makes it difficult to assess the practical applicability of the method, especially for large-scale scenes or real-time applications with strict latency requirements.
- The paper does not provide a thorough comparison with existing methods for dynamic scene rendering. While the authors mention some related works, there is no detailed comparison of the proposed method with other state-of-the-art techniques in terms of both performance and efficiency. This makes it difficult to understand the advantages and disadvantages of the proposed method compared to existing approaches.
- The paper does not provide a detailed discussion of the limitations of the proposed method. For example, how does the method handle scenes with complex occlusions, fast motion, or large-scale scenes? What are the potential failure cases of the method, and how can these be addressed in future work?

### Suggestions

The paper would benefit significantly from a more thorough analysis of the computational aspects of the proposed 4D Gaussian Splatting method. Specifically, the authors should provide a detailed breakdown of the time complexity for each stage of the pipeline, including the initialization of the 4D Gaussians, the optimization process, and the rendering stage. This analysis should not only consider the theoretical complexity but also provide empirical measurements of the actual runtime on different hardware configurations. Furthermore, a comparison of memory usage during different stages of the pipeline would be beneficial. This would allow readers to better understand the practical limitations of the method and its suitability for various applications. For example, the authors could report the time taken for each step of the algorithm, such as the time to compute the 4D Gaussian parameters, the time for the optimization process, and the time for rendering a single frame. This would provide a clearer picture of the computational bottlenecks and areas for potential optimization.

In addition to the computational analysis, the paper needs a more comprehensive comparison with existing state-of-the-art methods for dynamic scene rendering. The authors should not only compare the visual quality of the rendered scenes but also provide a quantitative comparison of the rendering speed and memory usage. This comparison should include a variety of methods, including both traditional approaches and more recent deep learning-based techniques. The authors should also discuss the specific scenarios where their method outperforms existing methods and vice versa. For example, it would be useful to see how the proposed method compares to other 4D Gaussian Splatting techniques in terms of rendering speed and memory efficiency. Furthermore, the authors should discuss the limitations of their method in comparison to other approaches, such as potential artifacts or limitations in handling complex scene geometries. This would provide a more balanced and comprehensive evaluation of the proposed method.

Finally, the paper should include a more detailed discussion of the limitations of the proposed method. The authors should address how the method handles complex occlusions, fast motion, and large-scale scenes. For example, the authors could discuss the challenges of modeling dynamic scenes with significant changes in viewpoint or the limitations of the method in handling scenes with complex object interactions. Furthermore, the authors should discuss potential failure cases of the method and how these can be addressed in future work. For instance, the authors could discuss the limitations of the 4D Gaussian representation in capturing highly complex or non-smooth motions. This would provide a more complete understanding of the method's capabilities and limitations and guide future research in this area.

### Questions

- How does the proposed method handle scenes with complex occlusions, fast motion, or large-scale scenes? What are the limitations of the method in these scenarios?
- What are the computational costs of the proposed method, including the time and memory requirements for training and rendering? How does it compare to other methods in terms of efficiency?
- How does the method perform in scenarios with significant changes in viewpoint or dynamic lighting conditions?

### Rating

6

### Confidence

4

**********
