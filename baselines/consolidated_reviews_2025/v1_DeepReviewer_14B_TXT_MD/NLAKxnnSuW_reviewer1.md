### Summary

This paper proposes MEGA, a memory-efficient framework for 4DGS. The framework includes a new color decomposition representation and an entropy-constrained Gaussian deformation technique. Experiments show that the proposed method significantly reduces storage overhead while maintaining high-quality rendering.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The proposed DAC effectively reduces storage requirements compared to the original 4DGS.
2. The proposed deformation field, combined with entropy loss, enhances the utilization rate of Gaussians.
3. The paper is generally well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

1. The FPS of the proposed method is lower than some other baselines, such as STG. Reducing the number of Gaussians might also decrease rendering speed, as fewer primitives need to be processed. The paper does not provide a sufficient analysis of the trade-off between memory efficiency and rendering speed. Specifically, the impact of the reduced Gaussian count on rasterization throughput should be investigated, as fewer Gaussians might lead to increased overhead in searching for relevant primitives.
2. The effect of the deformation field is not clearly visible. The authors should provide more visual results to demonstrate its effectiveness, such as showing the same scene at different viewpoints or times, or visualizing the motion trajectories of the Gaussians. Without these visualizations, it is difficult to assess the practical benefits of the proposed deformation model.
3. The authors apply the deformation field to the Gaussian centers, scales, and rotations. However, it is unclear whether this approach is more beneficial than applying the deformation to the 3D Gaussians obtained by slicing the 4D Gaussians. The paper lacks a comparative analysis of these two approaches, and it is not clear why the chosen approach is superior.
4. The authors use an MLP to construct the color predictor, but it is unclear how the input features are selected. For example, why is the Gaussian center used instead of the position in space? The paper should provide a justification for this choice, as the Gaussian center might not fully capture the spatial information relevant for color prediction.
5. The authors use a frequency positional encoding function in the deformation field. It is unclear whether the parameters of the MLP are also frequency-based. The paper should clarify the role of frequency encoding in the MLP and its impact on the deformation field's expressiveness.
6. The authors claim that the deformation field is temporal-viewpoint-aware, but it is unclear whether the time input to the MLP is also frequency-encoded. The paper should clarify how time is represented and processed in the MLP to ensure temporal coherence.
7. In Eq. (5), the authors use the multiplication operation in the Gaussian transformation. It is unclear whether the deformation output is a vector or a scalar, and how this operation is defined. The paper should provide a clear definition of the multiplication operation and its effect on the Gaussian parameters.
8. The authors claim that the deformation field is temporal-viewpoint-aware, but it is unclear whether the deformation output is a vector or a scalar, and how this operation is defined. The paper should provide a clear definition of the deformation output and its effect on the Gaussian parameters.

### Suggestions

The paper should provide a more detailed analysis of the trade-off between memory efficiency and rendering speed. Specifically, the authors should investigate the impact of the reduced Gaussian count on rasterization throughput. It would be beneficial to analyze the time spent on different stages of the rendering pipeline, such as Gaussian selection, transformation, and shading, to identify the bottlenecks. Furthermore, the authors should compare their method with other memory-efficient techniques, such as Gaussian pruning or quantization, to demonstrate the advantages of their approach. A more thorough analysis of the rendering performance would strengthen the paper's claims and provide a better understanding of the practical implications of the proposed method.

To better demonstrate the effectiveness of the deformation field, the authors should provide more visual results. For example, they could show the same scene at different viewpoints or times, and visualize the motion trajectories of the Gaussians. This would help to understand how the deformation field affects the Gaussian primitives and their contribution to the final rendering. Additionally, the authors should provide a quantitative evaluation of the deformation field, such as measuring the accuracy of the predicted Gaussian motions. This would provide a more objective assessment of the deformation model's performance. Furthermore, the authors should compare their deformation approach with other deformation techniques, such as those based on optical flow or scene flow, to demonstrate the advantages of their approach.

The paper should provide a more detailed explanation of the color predictor and the deformation field. Specifically, the authors should justify their choice of using the Gaussian center instead of the spatial position for color prediction. They should also clarify the role of frequency encoding in the MLP and its impact on the deformation field's expressiveness. Furthermore, the authors should provide a clear definition of the multiplication operation in Eq. (5) and its effect on the Gaussian parameters. A more thorough explanation of these design choices would improve the clarity and understanding of the proposed method. Finally, the authors should provide a more detailed explanation of how time is represented and processed in the MLP to ensure temporal coherence.

### Questions

1. The FPS of the proposed method is lower than some other baselines, such as STG. Reducing the number of Gaussians might also decrease rendering speed, as fewer primitives need to be processed. 
2. The effect of the deformation field is not clearly visible. The authors should provide more visual results to demonstrate its effectiveness, such as showing the same scene at different viewpoints or times, or visualizing the motion trajectories of the Gaussians.
3. The authors apply the deformation field to the Gaussian centers, scales, and rotations. However, it is unclear whether this approach is more beneficial than applying the deformation to the 3D Gaussians obtained by slicing the 4D Gaussians.
4. The authors use an MLP to construct the color predictor, but it is unclear how the input features are selected. For example, why is the Gaussian center used instead of the position in space?
5. The authors use a frequency positional encoding function in the deformation field. It is unclear whether the parameters of the MLP are also frequency-based.
6. The authors claim that the deformation field is temporal-viewpoint-aware, but it is unclear whether the time input to the MLP is also frequency-encoded.
7. In Eq. (5), the authors use the multiplication operation in the Gaussian transformation. It is unclear whether the deformation output is a vector or a scalar, and how this operation is defined.

### Rating

6

### Confidence

4

**********
