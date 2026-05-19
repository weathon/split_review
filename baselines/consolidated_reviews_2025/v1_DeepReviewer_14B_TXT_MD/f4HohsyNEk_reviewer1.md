### Summary

This paper introduces a method to generate high-quality, watertight manifold meshes with neural textures. The geometry initialization is derived from neural volumetric fields, which is then optimized alongside a compact neural texture representation using differentiable rasterizers. Extensive experiments indicate that the proposed approach generates accurate mesh reconstructions that maintain faithful appearance, comparable to previous volume rendering methods while achieving significantly faster rendering speeds.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed Differentiable Marching Cubes (DiffMC) is promising, and the visual results demonstrate its effectiveness.
3. The visual results validate the method's ability to recover high-quality geometry.

### Weaknesses

#### Some Related Works


#### comment

1. The paper presents only a few examples of real-world data, and these examples exhibit obvious color shifts. It would be beneficial for the authors to explore more constraints to preserve color consistency.
2. The authors should consider using more datasets for comparison, such as the DTU dataset, to evaluate the method's performance in reconstructing geometric details in real-world scenarios. Specifically, a comparison against multi-view stereo (MVS) methods on this dataset would be valuable to understand the trade-offs.
3. The authors should provide more comparisons with different neural field representations, such as Nerf, which is widely used. This would help to contextualize the performance of the proposed method relative to established baselines and highlight its specific advantages and disadvantages.

### Suggestions

To address the color shift issue in real-world examples, the authors should investigate incorporating color calibration techniques during the image acquisition process. This could involve using a color chart or employing white balancing algorithms to ensure consistent color representation across different views. Furthermore, the authors could explore incorporating color consistency constraints directly into the optimization process. For example, they could add a loss term that penalizes color discrepancies between the rendered and input images, potentially using a perceptual color difference metric. This would encourage the model to learn a more accurate color representation while maintaining the fidelity of the reconstructed geometry. Additionally, exploring different neural texture representations that are more robust to color variations could also be beneficial.

For a more comprehensive evaluation of geometric detail reconstruction, the authors should conduct experiments on the DTU dataset, a standard benchmark for multi-view 3D reconstruction. This would allow for a direct comparison with state-of-the-art multi-view stereo methods. The evaluation should include quantitative metrics such as root mean squared error (RMSE) of the point cloud, as well as qualitative comparisons of the reconstructed meshes. Furthermore, the authors should analyze the method's performance on different scenes within the DTU dataset, as this would provide insights into its robustness across varying levels of geometric complexity and texture richness. It would also be beneficial to investigate the impact of different hyperparameter settings on the reconstruction quality, such as the resolution of the neural volumetric fields and the number of iterations used for optimization.

To better contextualize the performance of the proposed method, the authors should provide a more thorough comparison with different neural field representations, particularly NeRF. This comparison should include both quantitative and qualitative evaluations, focusing on aspects such as rendering speed, geometric accuracy, and visual fidelity. The authors should also analyze the trade-offs between these different neural field representations, highlighting the specific advantages and disadvantages of their proposed approach. For instance, they could investigate how the choice of neural field representation affects the level of detail captured in the reconstructed geometry and the computational cost of rendering. This would provide a more complete understanding of the method's capabilities and limitations and help guide future research in this area.

### Questions

Please refer to the weakness part.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
