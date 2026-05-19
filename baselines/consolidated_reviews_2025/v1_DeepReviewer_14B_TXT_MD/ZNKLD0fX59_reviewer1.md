### Summary

The paper introduces *CasualHDR*, a one-stage method to robustly recover the 3D HDR scene from casually captured videos. The key idea is to jointly optimize exposure time, camera response function, continuous-time camera motion trajectory, and the 3DGS-based HDR scene. Extensive experiments demonstrate that the approach outperforms existing reconstruction methods in terms of robustness and rendering quality.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The proposed *CasualHDR* framework can reconstruct 3D HDR scenes from casually captured videos at a low cost.
- The authors present both synthetic and real-world datasets, where each video contains severe variations in brightness and camera motion blur.
- The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

 - The paper lacks a detailed explanation of the optimization process, particularly regarding the interplay between the different components. For instance, how is the exposure time optimized for each frame, and what is the influence of the initial exposure time estimation on the final result? The paper should clarify whether the exposure time is a scalar value or a function of time, and how this is incorporated into the rendering equation. Furthermore, the paper does not discuss the potential for instability in the optimization process due to the non-linear relationship between exposure time and the resulting image brightness. Specifically, it is unclear how the method avoids getting stuck in local minima when jointly optimizing exposure time and scene radiance.
- The paper does not provide a detailed analysis of the computational cost of the proposed method, including training time and memory requirements. The paper should provide a breakdown of the computational cost associated with each component of the pipeline, such as the 3DGS reconstruction, exposure time optimization, and CRF estimation. This analysis should include the number of parameters, FLOPs, and memory usage for each component. Furthermore, the paper should discuss the scalability of the method to larger and more complex scenes, and how the computational cost scales with the number of input frames and the resolution of the output images.
- The paper does not discuss the limitations of the proposed method. For example, how does the method perform in scenes with very high or very low contrast? What are the limitations of the method in terms of motion blur? The paper should discuss the potential for artifacts in the reconstructed scene, such as ghosting or blurring, when the input video contains significant motion. It should also address the limitations of the method in handling scenes with complex lighting conditions, such as strong specular reflections or diffuse interreflections. A more thorough discussion of these limitations would provide a more balanced view of the method's capabilities.

### Suggestions

The paper should provide a more detailed explanation of the optimization process, including the specific algorithms used for optimizing each component, and the order in which these components are optimized. For example, the paper should clarify whether the exposure time is optimized using a gradient-based method, and if so, what is the loss function used for this optimization. The paper should also discuss the potential for instability in the optimization process and how this is addressed. Furthermore, the paper should provide a more detailed explanation of how the continuous-time camera motion trajectory is represented and optimized. It should clarify how the method handles cases where the camera motion is not smooth or contains abrupt changes in direction or speed. A more detailed explanation of these aspects would improve the reproducibility of the method and provide a better understanding of its inner workings.

The paper should include a comprehensive analysis of the computational cost of the proposed method. This analysis should include a breakdown of the computational cost associated with each component of the pipeline, such as the 3DGS reconstruction, exposure time optimization, and CRF estimation. The paper should provide the number of parameters, FLOPs, and memory usage for each component. The paper should also discuss the scalability of the method to larger and more complex scenes, and how the computational cost scales with the number of input frames and the resolution of the output images. Furthermore, the paper should compare the computational cost of the proposed method with existing methods, and discuss the trade-offs between computational cost and reconstruction quality. This analysis would provide a better understanding of the practical applicability of the method.

The paper should include a more thorough discussion of the limitations of the proposed method. This discussion should include a detailed analysis of the method's performance in scenes with very high or very low contrast, and in scenes with significant motion blur. The paper should also discuss the potential for artifacts in the reconstructed scene, such as ghosting or blurring, and how these artifacts can be mitigated. Furthermore, the paper should address the limitations of the method in handling scenes with complex lighting conditions, such as strong specular reflections or diffuse interreflections. The paper should also discuss the limitations of the method in terms of the dynamic range of the input video, and how this affects the quality of the reconstructed HDR scene. A more thorough discussion of these limitations would provide a more balanced view of the method's capabilities and help guide future research in this area.

### Questions

- Please provide more details on the optimization process, including the computational cost and memory requirements.
- Please discuss the limitations of the proposed method in more detail.
- Please provide more details on the datasets used in the experiments, including the data collection process and the characteristics of the scenes.

### Rating

6

### Confidence

4

**********
