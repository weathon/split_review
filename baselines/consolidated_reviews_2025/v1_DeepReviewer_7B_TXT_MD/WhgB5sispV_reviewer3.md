### Summary

This paper introduces a novel approach for modeling dynamic scenes by approximating the spatio-temporal volume of a dynamic scene with a collection of 4D Gaussians. The proposed method, called 4D Gaussian Splatting, extends the concept of 3D Gaussian Splatting to the 4D domain, incorporating both spatial and temporal dimensions into the Gaussian representation. The authors also introduce Spherindrical Harmonics to model the time evolution of view-dependent color in dynamic scenes. The method is evaluated on both synthetic and real-world datasets, demonstrating superior visual quality and efficiency compared to existing methods.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed 4D Gaussian Splatting method is conceptually simple and straightforward to implement.
3. The experimental results demonstrate the effectiveness of the proposed method in dynamic novel view synthesis and rendering.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the computational complexity and efficiency of the proposed method. While the authors claim that their method is real-time, there is no quantitative analysis of the computational cost, memory usage, or rendering speed compared to other methods. This makes it difficult to assess the practical applicability of the method, especially for large-scale scenes or real-time applications with strict latency requirements.
2. The paper does not provide a thorough comparison with existing methods for dynamic scene rendering. While the authors mention some related works, there is no detailed comparison of the proposed method with other state-of-the-art techniques in terms of both performance and efficiency. This makes it difficult to understand the advantages and disadvantages of the proposed method compared to existing approaches.
3. The paper does not discuss the limitations of the proposed method. For example, how does the method handle scenes with complex occlusions, fast motion, or large-scale scenes? What are the potential failure cases of the method, and how can these be addressed in future work?

### Suggestions

The paper would benefit significantly from a more thorough analysis of the computational aspects of the proposed 4D Gaussian Splatting method. Specifically, the authors should provide a detailed breakdown of the time complexity for each stage of the pipeline, including the initialization of the 4D Gaussians, the optimization process, and the rendering stage. This analysis should not only consider the theoretical complexity but also provide empirical measurements of the actual runtime on different hardware configurations. Furthermore, a comparison of memory usage during different stages of the pipeline would be beneficial. This would allow readers to better understand the practical limitations of the method and its suitability for various applications. For example, the authors could report the time taken for each step of the algorithm, such as the time to compute the 4D Gaussian parameters, the time for the optimization process, and the time for rendering a single frame. This would provide a clearer picture of the computational bottlenecks and areas for potential optimization.

In addition to the computational analysis, the paper needs a more comprehensive comparison with existing state-of-the-art methods for dynamic scene rendering. The authors should not only compare the visual quality of the rendered scenes but also provide a quantitative comparison of the rendering speed and memory usage. This comparison should include a variety of methods, including both traditional approaches and more recent deep learning-based techniques. The authors should also discuss the specific scenarios where their method outperforms existing methods and vice versa. For example, it would be useful to see how the proposed method compares to other 4D Gaussian Splatting techniques in terms of rendering speed and memory efficiency. Furthermore, the authors should discuss the limitations of their method in comparison to other approaches, such as potential artifacts or limitations in handling complex scene geometries. This would provide a more balanced and comprehensive evaluation of the proposed method.

Finally, the paper should include a more detailed discussion of the limitations of the proposed method. The authors should address how the method handles complex occlusions, fast motion, and large-scale scenes. For example, the authors could discuss the challenges of modeling dynamic scenes with significant changes in viewpoint or the limitations of the method in handling scenes with complex object interactions. Furthermore, the authors should discuss potential failure cases of the method and how these can be addressed in future work. For instance, the authors could discuss the limitations of the 4D Gaussian representation in capturing highly complex or non-smooth motions. This would provide a more complete understanding of the method's capabilities and limitations and guide future research in this area.

### Questions

Please see the weakness.

### Rating

6

### Confidence

4

**********
