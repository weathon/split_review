### Summary

This paper introduces a inverse rendering method based on explicit mesh representation that reconstructs shape, material and lighting from multi-view images. In the first stage, the method uses InstantNGP and NeuS2 to create an initial mesh. In the second stage, it optimizes and refines the mesh. The method also uses physically-based multi-bounce path tracing for more accurate indirect illumination estimation, and uses reservoir sampling to reduce noise in Monte Carlo integration.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The use of multi-bounce path tracing and reservoir sampling seems novel in the context of inverse rendering.
2. The paper is well written and easy to follow.
3. The optimization pipeline can be useful for other inverse rendering methods that use explicit mesh representation.

### Weaknesses

#### Some Related Works


#### comment

1. The contributions of this paper are incremental, and the proposed pipeline is similar to that of NeRF2Mesh.
2. The pipeline is complex, requiring two separate stages and additional optimization techniques, which may be difficult to use in practice.
3. The paper lacks sufficient quantitative and qualitative comparisons with state-of-the-art methods, such as DiffIR, PhyIR, DIF-FRM, and TensoIR.

### Suggestions

The paper would benefit from a more thorough analysis of the limitations of existing mesh-based inverse rendering methods, specifically highlighting the challenges in optimizing geometry, material, and lighting simultaneously. While the authors mention that methods like NVDiffRec-MC optimize material and lighting before geometry refinement, they should elaborate on the specific issues that arise from this sequential approach, such as the propagation of errors from inaccurate initial geometry to material and lighting estimation. Furthermore, the paper should discuss in more detail the limitations of single-bounce path tracing in methods like NVDiffRec-MC, and how multi-bounce path tracing can alleviate these issues, particularly in complex lighting scenarios with indirect illumination, inter-reflections, and shadows. A more detailed discussion of these limitations would better position the contributions of the proposed method.

To address the concern about the complexity of the pipeline, the authors should provide a more detailed breakdown of the computational cost associated with each stage. Specifically, they should quantify the time required for mesh extraction in the first stage and the optimization process in the second stage, perhaps by reporting the number of iterations or the time per iteration. This would allow for a more informed assessment of the practical feasibility of the method. Furthermore, the authors should discuss the sensitivity of the method to the hyperparameters of the optimization process, such as the learning rate and the number of samples used for Monte Carlo integration. A sensitivity analysis would help to understand the robustness of the method and provide guidance for users on how to tune the parameters for different scenes. The authors should also consider providing a more detailed comparison of the computational cost of their method with other state-of-the-art methods, such as TensoIR, to better understand the trade-offs between accuracy and efficiency.

Finally, the paper needs a more comprehensive evaluation that includes comparisons with state-of-the-art methods. While the authors provide comparisons with NVDiffRec-MC, they should also include comparisons with other relevant methods, such as PhyIR and TensoIR, on a wider range of datasets, including both synthetic and real-world scenes. The evaluation should include both quantitative metrics, such as PSNR, SSIM, and LPIPS, and qualitative comparisons of the reconstructed geometry, material, and lighting. The authors should also provide a more detailed analysis of the strengths and weaknesses of their method compared to other methods, highlighting the specific scenarios where their method performs better or worse. For example, it would be useful to see how the method performs on scenes with complex geometry, highly specular materials, or challenging lighting conditions. A more thorough evaluation would provide a more complete understanding of the capabilities and limitations of the proposed method.

### Questions

1. The paper mentions that "they rely on radiance fields instead of physically-based rendering (PBR) to obtain second-bounce radiance." However, methods like TensoIR also use a PBR BRDF. Could the authors clarify this?
2. How does the performance of the first stage compare to other methods that extract a mesh from a density field, such as MC-SDF or NeuS-Mesh?
3. What is the computational cost of the first stage?
4. What is the total computational cost of the proposed method compared to other state-of-the-art methods, such as TensoIR?

### Rating

5

### Confidence

4

**********
