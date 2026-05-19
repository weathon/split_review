### Summary

The paper proposes a one-stage method, CasualHDR, to recover the 3D HDR scene from casual videos with auto-exposure enabled. The proposed method jointly optimize exposure time, camera response function (CRF), continuous-time camera motion trajectory, and the 3DGS-based HDR scene. Extensive experiments demonstrate that the approach outperforms existing reconstruction methods in terms of robustness and rendering quality.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The proposed method can reconstruct 3D HDR scenes from casually captured videos, which is more flexible than previous methods that require multi-exposure LDR images as input.
2. The proposed method jointly optimizes exposure time, CRF, continuous-time camera motion trajectory, and the 3DGS-based HDR scene, which is novel and effective.
3. The proposed method outperforms existing reconstruction methods in terms of robustness and rendering quality on both synthetic datasets and real-world datasets.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the failure cases or limitations of the proposed method. It would be helpful to understand the scenarios where the method may not perform well or fail to reconstruct the 3D HDR scene accurately.
2. The paper could provide more insights into the computational cost and efficiency of the proposed method. It would be helpful to know the training and inference time, as well as the hardware requirements for running the method.
3. The paper could provide more details on the datasets used in the experiments, including the data collection process and the characteristics of the scenes.

### Suggestions

The paper would benefit from a more thorough investigation into the limitations of the proposed method. Specifically, the authors should analyze scenarios where the method struggles, such as scenes with extreme lighting variations, high levels of motion blur, or complex object geometries. For example, it would be valuable to see how the method performs in situations with very bright light sources that cause significant lens flare or very dark shadows that lack sufficient detail. Furthermore, the authors should explore the impact of inaccurate initial camera pose estimates on the final reconstruction quality. A detailed analysis of these failure cases would provide a more complete understanding of the method's robustness and applicability. This analysis should include both qualitative and quantitative results, such as visualizations of the reconstructed scenes and metrics that highlight the errors in these challenging scenarios. This would allow the reader to better understand the practical limitations of the approach.

To improve the practical value of the paper, the authors should provide a more detailed analysis of the computational cost and efficiency of their method. This should include a breakdown of the time spent on each stage of the pipeline, such as exposure time optimization, CRF optimization, and 3DGS training. It would also be helpful to know the memory requirements of the method, as well as the hardware used for the experiments. This information is crucial for researchers who want to reproduce the results or apply the method to their own datasets. Furthermore, the authors should discuss the scalability of the method to larger and more complex scenes. This analysis should include a discussion of the trade-offs between reconstruction quality and computational cost, and provide guidance on how to optimize the method for different applications. This would make the method more accessible and useful to the broader research community.

Finally, the paper should include more details about the datasets used in the experiments. This should include a description of the data collection process, the characteristics of the scenes, and the types of motions present in the videos. For example, the authors should specify the number of frames, the resolution of the images, and the range of exposure times used in the experiments. It would also be helpful to know the types of objects and materials present in the scenes, as well as the lighting conditions. This information is essential for understanding the generalizability of the method and for comparing it to other approaches. Furthermore, the authors should discuss the limitations of the datasets used and how these limitations might affect the results. This would allow the reader to better understand the scope of the method and its potential for real-world applications.

### Questions

Please refer to the weakness.

### Rating

6

### Confidence

3

**********
