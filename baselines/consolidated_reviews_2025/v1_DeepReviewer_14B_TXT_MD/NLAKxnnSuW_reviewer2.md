### Summary

This paper proposes a memory-efficient framework for 4DGS. The framework includes a new color decomposition representation and an entropy-constrained Gaussian deformation technique. Experiments show that the proposed method significantly reduces storage overhead while maintaining high-quality rendering.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The proposed DAC effectively reduces storage requirements compared to the original 4DGS.
2. The proposed deformation field, combined with entropy loss, enhances the utilization rate of Gaussians.

### Weaknesses

#### Some Related Works


#### comment

1. The FPS of the proposed method is lower than some other baselines, such as STG. Reducing the number of Gaussians might also decrease rendering speed, as fewer primitives need to be processed. 
2. The effect of the deformation field is not clearly visible. The authors should provide more visual results to demonstrate its effectiveness, such as showing the same scene at different viewpoints or times, or visualizing the motion trajectories of the Gaussians.
3. The authors apply the deformation field to the Gaussian centers, scales, and rotations. However, it is unclear whether this approach is more beneficial than applying the deformation to the 3D Gaussians obtained by slicing the 4D Gaussians.
4. The authors use an MLP to construct the color predictor, but it is unclear how the input features are selected. For example, why is the Gaussian center used instead of the position in space?
5. The authors use a frequency positional encoding function in the deformation field. It is unclear whether the parameters of the MLP are also frequency-based.
6. The authors claim that the deformation field is temporal-viewpoint-aware, but it is unclear whether the time input to the MLP is also frequency-encoded.
7. In Eq. (5), the authors use the multiplication operation in the Gaussian transformation. It is unclear whether the deformation output is a vector or a scalar, and how this operation is defined.

### Suggestions

The paper should provide a more detailed analysis of the trade-off between memory efficiency and rendering speed. While reducing the number of Gaussians is beneficial for memory, it is crucial to understand the impact on rendering performance. The authors should investigate the specific bottlenecks in their rendering pipeline and explore potential optimizations. For example, they could analyze the time spent on different stages of the rendering process, such as Gaussian selection, attribute retrieval, and shading, to identify areas for improvement. Furthermore, it would be beneficial to compare the rendering performance with other memory-efficient techniques, such as Gaussian pruning or quantization, to provide a more comprehensive evaluation of the proposed method's efficiency.

To better demonstrate the effectiveness of the deformation field, the authors should provide more visual results and quantitative analysis. Showing the same scene at different viewpoints and times would help to visualize the temporal coherence and view-dependent behavior of the deformed Gaussians. Visualizing the motion trajectories of the Gaussians would also provide a more intuitive understanding of the deformation field's impact. Additionally, the authors should consider providing quantitative metrics to evaluate the accuracy of the deformation field, such as the mean squared error between the deformed Gaussians and the ground truth motion. This would provide a more objective assessment of the deformation field's effectiveness. Furthermore, the authors should compare their deformation approach with other deformation techniques, such as those based on optical flow or scene flow, to demonstrate the advantages of their approach.

The paper should also provide a more detailed explanation of the color predictor and the deformation field. The authors should justify their choice of using the Gaussian center instead of the spatial position for color prediction. They should also clarify the role of frequency encoding in the MLP and its impact on the deformation field's expressiveness. Furthermore, the authors should provide a clear definition of the multiplication operation in Eq. (5) and its effect on the Gaussian parameters. A more thorough explanation of these design choices would improve the clarity and understanding of the proposed method. Finally, the authors should provide a more detailed explanation of how time is represented and processed in the MLP to ensure temporal coherence.

### Questions

Please see the weaknesses.

### Rating

6

### Confidence

4

**********
