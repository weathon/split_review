### Summary

This paper introduces NeuManifold, a two-stage approach for converting implicit neural representations into explicit, high-quality, watertight manifold meshes with neural textures. In the first stage, a neural field method (NeuS or TensoRF) is employed to initialize geometry and appearance. In the second stage, Differentiable Marching Cubes (DiffMC) extracts an initial mesh from the density grid, which is then refined through differentiable rasterization using nvdiffrast. The authors demonstrate competitive performance in terms of both mesh quality and novel view synthesis against prior methods on the NeRF-Synthetic dataset. Additionally, the proposed DiffMC method shows improvements over DMTet for non-linear fields. The resulting mesh-based representation integrates with GLSL shaders for real-time rendering.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is clearly written and easy to follow.
- The proposed DiffMC is novel and useful, particularly for density-based neural field methods.
- The method achieves high-quality mesh reconstruction results.
- The approach supports a wide range of applications including geometry editing, appearance editing, and physical simulation.

### Weaknesses

#### Some Related Works


#### comment

 - The paper lacks a detailed analysis of the computational cost of each stage, which would be valuable for understanding the overall efficiency of the pipeline. Specifically, a breakdown of the time spent in neural network inference, mesh extraction, and differentiable rasterization would be beneficial. Furthermore, the memory footprint of each stage should be considered, especially when dealing with high-resolution meshes or complex scenes.
- The evaluation could be strengthened by including more diverse datasets and real-world examples. The current evaluation is heavily reliant on the NeRF-Synthetic dataset, which may not fully represent the challenges of real-world scenarios with complex lighting, occlusions, and varying object scales. The inclusion of more diverse datasets, such as those with dynamic scenes or less controlled environments, would provide a more robust evaluation of the method's generalizability.
- The method currently has limitations when dealing with specular areas, which could be discussed in more detail. The paper should elaborate on the specific types of specularities that cause issues, such as high-frequency reflections or anisotropic reflections. Additionally, it would be helpful to analyze how the method's performance degrades as the specular component becomes more prominent in the scene.

### Suggestions

To address the lack of detailed computational cost analysis, the authors should provide a breakdown of the time spent in each stage of their pipeline, including neural network inference, mesh extraction using DiffMC, and differentiable rasterization. This analysis should not only include the total time but also the time per triangle or per vertex, which would be more informative for understanding the scalability of the method. Furthermore, the memory footprint of each stage should be analyzed, especially when dealing with high-resolution meshes or complex scenes. This analysis should be performed on a variety of hardware configurations to understand the method's performance across different platforms. The authors could also consider providing a comparison of their method's computational cost against other state-of-the-art mesh reconstruction techniques, which would help to contextualize the efficiency of their approach.

To strengthen the evaluation, the authors should include more diverse datasets and real-world examples. The current evaluation is heavily reliant on the NeRF-Synthetic dataset, which may not fully represent the challenges of real-world scenarios. The inclusion of datasets with complex lighting, occlusions, and varying object scales would provide a more robust evaluation of the method's generalizability. For example, the authors could consider using datasets with dynamic scenes or less controlled environments. Additionally, the authors should provide a more detailed analysis of the method's performance on these datasets, including both quantitative metrics and qualitative visualizations. This would help to identify the limitations of the method and provide insights into potential areas for improvement. The authors should also consider evaluating the method's performance on datasets with different types of objects, such as those with intricate geometries or fine details.

Finally, the authors should provide a more detailed discussion of the method's limitations when dealing with specular areas. The paper should elaborate on the specific types of specularities that cause issues, such as high-frequency reflections or anisotropic reflections. Additionally, it would be helpful to analyze how the method's performance degrades as the specular component becomes more prominent in the scene. The authors could also consider providing visualizations of the reconstructed meshes in specular regions, which would help to illustrate the limitations of the method. Furthermore, the authors should discuss potential strategies for addressing these limitations, such as incorporating inverse rendering techniques or using more advanced neural field representations that can better capture specularities. This would help to provide a more complete understanding of the method's capabilities and limitations.

### Questions

- How does the method handle specularities? The paper mentions that the method has limitations when dealing with specular areas. Could you elaborate on these limitations and potential strategies for addressing them?
- How does the method perform on real-world datasets with more complex scenes and lighting conditions? It would be interesting to see how the method generalizes to real-world scenarios beyond the synthetic dataset.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
