### Summary

This paper proposes a method to reconstruct HDR scenes from casually captured videos with auto exposure. The proposed method is based on 3D Gaussian Splatting (3DGS) and jointly optimizes camera trajectory, exposure time, and camera response function. The proposed method is evaluated on both synthetic and real-world datasets.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The proposed method is technically sound and well-motivated. The proposed method is able to jointly optimize camera trajectory, exposure time, and camera response function, which is a challenging problem in the literature.
2. The proposed method is evaluated on both synthetic and real-world datasets. The experimental results show that the proposed method outperforms existing methods in novel view synthesis, image deblurring, and HDR editing tasks.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is based on 3DGS, which is a very powerful representation but requires a large number of Gaussians to represent the scene. This may limit the applicability of the proposed method to large-scale scenes.
2. The proposed method requires a large number of Gaussians to represent the scene, which may limit the applicability of the proposed method to large-scale scenes.
3. The proposed method is only evaluated on a few real-world datasets. It would be better to evaluate the proposed method on more real-world datasets, especially those with more complex scenes and motion blur.

### Suggestions

The paper introduces a method for reconstructing high dynamic range (HDR) scenes from casually captured videos using 3D Gaussian Splatting (3DGS). While the approach is technically sound and demonstrates promising results, there are several areas where the methodology and evaluation could be strengthened. The core idea of jointly optimizing camera trajectory, exposure time, and camera response function within the 3DGS framework is novel and addresses a significant challenge in HDR reconstruction. However, the reliance on 3DGS inherently limits the scalability of the method to large-scale scenes due to the computational cost associated with managing a large number of Gaussian primitives. The paper should explore alternative scene representations or optimization strategies that could mitigate this limitation, such as hierarchical Gaussian Splatting or other sparse scene representations. Furthermore, the paper should provide a more detailed analysis of the computational complexity of the proposed method, including the number of Gaussians required for different scene complexities and the impact on reconstruction time. 

To further improve the evaluation, the authors should consider expanding the real-world dataset evaluation to include a wider variety of scenes with varying levels of motion blur and scene complexity. The current evaluation, while demonstrating the method's effectiveness, is limited by the number and diversity of the real-world datasets. A more comprehensive evaluation would include datasets with more challenging conditions, such as scenes with rapid camera motion, complex lighting variations, and significant occlusions. This would provide a more robust assessment of the method's generalizability and limitations. Additionally, the paper should include a more detailed comparison with existing HDR reconstruction methods, including both quantitative and qualitative analysis. This would help to better contextualize the performance of the proposed method and highlight its advantages and disadvantages compared to the state-of-the-art. The authors should also consider including a discussion of the limitations of the proposed method and potential avenues for future research.

Finally, while the paper focuses on casual videos with auto-exposure, it would be beneficial to explore the method's performance on videos with different exposure strategies or under more controlled conditions. This would provide a more comprehensive understanding of the method's robustness and applicability. The paper should also discuss the sensitivity of the method to the quality of the input video, such as frame resolution, frame rate, and signal-to-noise ratio. This would help to identify the scenarios where the method is most effective and where it may require additional processing or pre-processing steps. The authors should also consider providing a more detailed analysis of the impact of the optimization parameters on the reconstruction quality, which would help to guide the practical application of the method.

### Questions

1. How does the proposed method perform on scenes with more complex motion blur or more severe motion artifacts?
2. How does the proposed method perform on scenes with more complex lighting conditions or more severe color casts?
3. How does the proposed method perform on scenes with more complex occlusions or more severe self-occlusions?

### Rating

6

### Confidence

4

**********
