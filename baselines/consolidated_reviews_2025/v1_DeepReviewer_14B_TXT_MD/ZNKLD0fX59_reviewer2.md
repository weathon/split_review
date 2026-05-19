### Summary

This paper proposes a method called CasualHDR, which can reconstruct 3D HDR scenes from casually captured videos with auto-exposure enabled. The proposed method jointly optimizes exposure time, camera response function (CRF), continuous-time camera motion trajectory, and the 3DGS-based HDR scene. The proposed method is validated on both synthetic datasets and real-world datasets.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The proposed method can reconstruct 3D HDR scenes from casually captured videos with auto-exposure enabled, which is more convenient than previous methods that require multi-exposure LDR images as input.
2. The proposed method jointly optimizes exposure time, CRF, continuous-time camera motion trajectory, and the 3DGS-based HDR scene. Experiments demonstrate the effectiveness of each component.
3. The proposed method outperforms existing reconstruction methods in terms of robustness and rendering quality on both synthetic datasets and real-world datasets.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the failure cases or limitations of the proposed method. It would be helpful to understand the scenarios where the method may not perform well or fail to reconstruct the 3D HDR scene accurately. Specifically, the paper lacks discussion on how the method handles extreme motion blur, severe occlusions, or highly reflective surfaces, which are common challenges in real-world scenarios. Furthermore, it would be beneficial to understand the sensitivity of the method to noise in the input video, such as compression artifacts or sensor noise.
2. The paper could provide more insights into the computational cost and efficiency of the proposed method. It would be helpful to know the training and inference time, as well as the hardware requirements for running the method. The paper should also discuss the scalability of the method to larger and more complex scenes, and provide a breakdown of the computational cost associated with each stage of the pipeline, such as feature extraction, optimization, and rendering. This would allow for a better understanding of the practical applicability of the method.
3. The paper could provide more details on the datasets used in the experiments, including the data collection process and the characteristics of the scenes. This would help in understanding the generalizability of the proposed method to different types of scenes and lighting conditions. For example, the paper should specify the range of exposure variations, the types of materials present in the scenes, and the complexity of the geometry. This information is crucial for assessing the robustness and applicability of the method.

### Suggestions

To address the lack of analysis on failure cases, the authors should include a detailed discussion on the limitations of their method, specifically focusing on scenarios where the reconstruction quality degrades significantly. This should include a quantitative analysis of the impact of motion blur, occlusions, and reflective surfaces on the reconstruction accuracy. For instance, the authors could introduce metrics to quantify the level of motion blur and correlate it with the reconstruction error. They should also investigate the sensitivity of the method to different types of noise and discuss potential strategies to mitigate these issues, such as pre-processing techniques or robust optimization methods. Furthermore, a visual analysis of the failure cases, showing the input videos and the corresponding reconstructed HDR scenes, would provide valuable insights into the method's limitations.

To improve the discussion on computational cost and efficiency, the authors should provide a detailed breakdown of the time and memory requirements for each stage of their pipeline. This should include the time taken for feature extraction, optimization, and rendering, as well as the memory footprint of the different data structures. The authors should also discuss the scalability of their method to larger and more complex scenes, and provide an analysis of how the computational cost scales with the number of input views and the complexity of the scene geometry. It would be beneficial to compare the computational cost of their method with existing state-of-the-art methods, and discuss the trade-offs between reconstruction quality and computational efficiency. Additionally, the authors should specify the hardware requirements for running their method, including the GPU model, CPU, and memory requirements.

To enhance the description of the datasets, the authors should provide more detailed information on the data collection process and the characteristics of the scenes. This should include a description of the camera settings used to capture the videos, the range of exposure variations, and the types of materials present in the scenes. The authors should also provide a quantitative analysis of the complexity of the scene geometry, such as the number of vertices, edges, and faces in the reconstructed 3D models. Furthermore, the authors should discuss the limitations of their datasets and how they might affect the generalizability of their method. For example, if the datasets are biased towards certain types of scenes or lighting conditions, the authors should acknowledge this limitation and discuss its potential impact on the performance of their method in other scenarios.

### Questions

Please see the weaknesses.

### Rating

6

### Confidence

3

**********
