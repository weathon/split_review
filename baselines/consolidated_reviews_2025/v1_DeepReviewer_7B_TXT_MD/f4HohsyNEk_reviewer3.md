### Summary

This paper proposes a method for reconstructing high-quality watertight manifold meshes from multi-view images. The method combines the benefits of both neural field rendering and differentiable rasterization-based mesh reconstruction. The method first uses the geometry initialization obtained from neural volume rendering and further optimizes the geometry as well as a compact neural texture representation with differentiable rasterization. The method is evaluated on several datasets and compared with existing approaches.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The method combines the benefits of both neural field rendering and differentiable rasterization-based mesh reconstruction.
- The method is evaluated on several datasets and compared with existing approaches.
- The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

 - The method relies on a good initialization from neural field representation, which may not be available for all scenes.
- The method may not work well for scenes with complex topologies or self-occlusions.
- The method is computationally expensive, especially for high-resolution meshes.

### Suggestions

The paper's reliance on a neural field representation for initialization is a potential limitation. While the authors claim this provides a good starting point, the quality of this initialization can significantly impact the final mesh reconstruction. For scenes with complex geometries or significant occlusions, the initial neural field representation might be inaccurate, leading to suboptimal mesh results. It would be beneficial to explore alternative initialization strategies or to incorporate a mechanism to detect and handle cases where the initial neural field is poor. For example, a multi-stage approach could be considered, where the initial neural field is refined using a more robust method before mesh extraction, or where the mesh extraction is guided by additional constraints derived from the initial neural field. Furthermore, the paper should provide a more detailed analysis of the failure cases, specifically quantifying the impact of poor initialization on the final mesh quality. This would help to understand the limitations of the method and identify scenarios where it might not be suitable.

The paper also raises concerns about the method's ability to handle complex topologies and self-occlusions. While the authors mention that the method can handle thin structures, it is not clear how it performs on scenes with highly intricate shapes or significant self-occlusions. The mesh extraction process, based on the marching cubes algorithm, can be sensitive to the quality of the underlying density field. In cases of severe self-occlusions, the density field might not accurately represent the underlying geometry, leading to inaccurate mesh extraction. It would be beneficial to explore alternative mesh extraction techniques or to incorporate a mechanism to handle self-occlusions more robustly. For example, a multi-resolution approach could be considered, where the mesh is extracted at multiple scales to capture both fine details and large-scale structures. Additionally, the paper should provide a more detailed analysis of the method's performance on scenes with varying levels of complexity and occlusions, including quantitative results that demonstrate the method's robustness.

The computational cost of the method is another area that needs further investigation. The paper mentions that the method is computationally expensive, especially for high-resolution meshes. While the authors introduce a faster implementation of Differentiable Marching Cubes (DiffMC), the overall computational cost of the method could still be a limiting factor for large-scale applications. It would be beneficial to explore techniques to reduce the computational cost of the method, such as using more efficient mesh extraction algorithms or optimizing the implementation of the differentiable rasterization process. Furthermore, the paper should provide a more detailed analysis of the computational cost of the method, including a breakdown of the time spent on each stage of the pipeline. This would help to identify the bottlenecks and guide future efforts to improve the efficiency of the method.

### Questions

- How does the method handle scenes with complex topologies or self-occlusions?
- How does the method perform on scenes with varying levels of detail?
- How does the method compare to other state-of-the-art methods in terms of computational cost?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
