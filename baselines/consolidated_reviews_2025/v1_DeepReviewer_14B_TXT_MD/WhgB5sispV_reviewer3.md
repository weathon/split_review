### Summary

This paper proposes a novel representation for dynamic scenes. The authors extend the recent work of 3D Gaussian Splatting into dynamic scenes by introducing a 4D Gaussian representation. The 4D Gaussian is defined by a mean vector and a 4x4 covariance matrix, which can be decomposed into a rotation matrix and a scaling matrix. The rotation matrix can be further decomposed into two quaternions. The authors also propose to use 4D spherindrical harmonics to model the time-evolved appearance of the Gaussians. The proposed method is evaluated on both multi-view and monocular dynamic scenes and achieves state-of-the-art performance in terms of rendering quality and training/inference speed.

### Soundness

4 excellent

### Presentation

4 excellent

### Contribution

4 excellent

### Strengths

- The proposed method is novel and effective. The authors extend the 3D Gaussian Splatting into dynamic scenes by introducing a 4D Gaussian representation. The 4D Gaussian is well-defined and can model the motion and deformation of the scene. The authors also propose to use 4D spherindrical harmonics to model the time-evolved appearance of the Gaussians, which is a novel idea and can capture the changing appearance of the scene over time.
- The paper is well-written and easy to follow. The authors provide a clear and concise explanation of the proposed method and the related work. The paper is also well-organized and has a clear structure.
- The proposed method is evaluated on both multi-view and monocular dynamic scenes and achieves state-of-the-art performance in terms of rendering quality and training/inference speed. The authors also provide ablation studies to analyze the effectiveness of the proposed components.

### Weaknesses

#### Some Related Works


#### comment

 - The authors do not provide any failure cases or limitations of the proposed method. It would be helpful to see some examples of scenes where the proposed method fails to reconstruct or render accurately. This would help to understand the limitations of the method and potential areas for improvement.
- The authors do not provide any analysis of the computational cost of the proposed method. It would be helpful to know the training and inference time of the proposed method and how it compares to other methods.

### Suggestions

The paper would benefit from a more thorough discussion of the limitations of the proposed 4D Gaussian Splatting method. While the results are impressive, it's crucial to understand the scenarios where the method might struggle. For example, how does the method perform with extremely fast or complex motions? Are there specific types of object deformations that are difficult to capture? Providing examples of such failure cases, perhaps with visualizations of the reconstructed Gaussian splats, would give a more complete picture of the method's capabilities and limitations. Furthermore, it would be beneficial to analyze the sensitivity of the method to the initialization of the Gaussian parameters. Does the method converge to a good solution regardless of the initial parameters, or are specific initialization strategies required for optimal performance? Understanding these aspects would help in assessing the robustness and generalizability of the approach.

In addition to the qualitative analysis, a more detailed quantitative analysis of the computational cost is needed. While the authors mention the training and inference speed, a breakdown of the time spent on different stages of the pipeline would be valuable. For instance, how much time is spent on the Gaussian parameter optimization, the spherical harmonics computation, and the rendering process? This would help in identifying potential bottlenecks and areas for optimization. Furthermore, it would be useful to compare the memory footprint of the proposed method with other dynamic scene representation techniques. This is particularly important for practical applications where memory resources might be limited. A comparison of the number of Gaussians used by the proposed method and other methods would also be beneficial, as this directly impacts both memory usage and rendering speed. Finally, it would be helpful to analyze the scalability of the method with respect to the complexity of the scene and the number of frames.

Finally, the paper could benefit from a more detailed discussion of the choice of the 4D spherindrical harmonics for modeling the time-evolved appearance of the Gaussians. While the authors mention that this is a novel idea, a more in-depth explanation of the rationale behind this choice would be beneficial. How does this representation compare to other methods for modeling time-varying appearance, such as using a separate network to predict the appearance at each time step? What are the advantages and disadvantages of using 4D spherindrical harmonics in terms of expressiveness, computational cost, and ease of implementation? A more thorough discussion of these aspects would help in understanding the design choices and the potential for further improvements.

### Questions

- How does the proposed method handle scenes with complex motions or deformations? Are there any limitations or failure cases?
- How does the proposed method compare to other dynamic scene representation techniques in terms of computational cost and memory usage?
- How does the proposed method handle occlusions and disocclusions in the scene?
- How does the proposed method handle changes in lighting conditions over time?

### Rating

8: accept, good paper

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
