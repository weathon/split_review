### Summary

The paper proposes a novel method for reconstructing 3D high dynamic range (HDR) scenes from casually captured videos with auto-exposure. The method, called CasualHDR, jointly optimizes exposure time, camera response function (CRF), continuous-time camera motion trajectory, and 3D Gaussian Splatting (3DGS)-based HDR scene representation. The key innovation is a unified differentiable physical imaging model that accounts for motion blur and varying exposure times, enabling robust recovery of HDR scenes from videos with severe motion blur and exposure variations. The method demonstrates superior performance compared to existing approaches on both synthetic and real-world datasets, enabling applications such as novel-view synthesis, image deblurring, and HDR editing.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel approach to 3D HDR reconstruction from casually captured videos, addressing a significant gap in the field. The method's ability to handle auto-exposure, motion blur, and varying exposure times is a notable advancement.
2. The unified differentiable physical imaging model is a well-thought-out solution that integrates multiple aspects of the imaging process, leading to robust and accurate reconstruction.
3. The experimental results are comprehensive, demonstrating the method's effectiveness on both synthetic and real-world datasets. The ablation studies provide valuable insights into the contribution of each component.
4. The paper is well-written and clearly explains the methodology, implementation details, and experimental setup. The figures and tables effectively support the textual content.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost of the proposed method. Specifically, it lacks a breakdown of the time spent on each stage of the pipeline, such as exposure time optimization, CRF optimization, and 3DGS training. This makes it difficult to assess the practical applicability of the method, especially for real-time or near-real-time applications. Furthermore, the memory requirements for each stage are not discussed, which is crucial for understanding the scalability of the approach on different hardware configurations.
2. The paper could benefit from a more in-depth discussion of the limitations of the proposed method. For example, how does the method perform under extreme lighting conditions, such as very low light or very bright light? Are there specific types of motion blur that are more challenging to handle? A more detailed analysis of failure cases would provide a more complete picture of the method's capabilities and limitations. Additionally, the paper does not discuss the sensitivity of the method to the accuracy of the initial camera pose estimation, which is a critical factor for successful 3D reconstruction.
3. The paper does not provide a detailed comparison of the proposed method with state-of-the-art methods in terms of computational efficiency. While the paper demonstrates superior reconstruction quality, it is important to understand the trade-offs between quality and computational cost. A quantitative comparison of training and inference times with other methods would be beneficial.

### Suggestions

The paper would significantly benefit from a more detailed analysis of the computational cost associated with each stage of the proposed pipeline. Specifically, the authors should provide a breakdown of the time spent on exposure time optimization, CRF optimization, and 3D Gaussian Splatting (3DGS) training. This analysis should include not only the total time but also the time per iteration or per frame, which would allow for a better understanding of the method's scalability. Furthermore, the memory footprint of each stage should be quantified, including the memory required for storing the 3DGS primitives, intermediate variables, and other data structures. This information is crucial for assessing the practical applicability of the method on different hardware configurations, such as GPUs with varying memory capacities. It would also be beneficial to analyze how the computational cost scales with the number of input frames and the resolution of the reconstructed scene. This analysis should be presented in a clear and concise manner, possibly using tables or graphs to illustrate the trends.

To enhance the discussion of the method's limitations, the authors should provide a more in-depth analysis of its performance under various challenging conditions. This should include a detailed evaluation of the method's robustness to extreme lighting conditions, such as very low light or very bright light, and different types of motion blur, such as fast camera movements or object motion. The authors should also investigate the sensitivity of the method to the accuracy of the initial camera pose estimation. It would be valuable to show examples of failure cases, where the method struggles to reconstruct the scene accurately, and analyze the reasons for these failures. This analysis should not only focus on the visual quality of the reconstruction but also on the accuracy of the estimated exposure times and CRF. Furthermore, the authors should discuss potential strategies for mitigating these limitations, such as incorporating additional regularization terms or using more robust optimization techniques.

Finally, the paper should include a more detailed comparison of the proposed method with state-of-the-art methods in terms of computational efficiency. This comparison should not only focus on the reconstruction quality but also on the computational cost, including training and inference times. The authors should provide quantitative comparisons of the time required to train the model and generate novel views, as well as the memory requirements. This comparison should be performed on a common dataset and using the same hardware configuration to ensure a fair evaluation. It would also be beneficial to analyze the trade-offs between reconstruction quality and computational cost, and to discuss the scenarios where the proposed method is most suitable. This analysis should provide a more complete picture of the method's practical applicability and help potential users make informed decisions about its use.

### Questions

1. How does the method perform on videos with significant camera rotation or translation? Are there any specific challenges in these scenarios?
2. Can the method handle videos with rapid changes in exposure time? How does the optimization process adapt to these changes?
3. What is the impact of inaccurate initial camera poses on the final reconstruction quality? How robust is the method to errors in camera pose estimation?
4. How does the method perform on videos with complex motion patterns, such as non-rigid object motion or occlusions?
5. Can the method be extended to handle other types of imaging devices, such as RAW images or different sensor types?

### Rating

6

### Confidence

3

**********
