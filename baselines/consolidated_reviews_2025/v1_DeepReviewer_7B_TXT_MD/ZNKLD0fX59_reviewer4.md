### Summary

This paper presents a method for reconstructing high dynamic range (HDR) scenes from casually captured videos with auto-exposure. The key innovation is a unified, differentiable pipeline that jointly optimizes HDR scene reconstruction, camera motion trajectory, exposure times, and camera response functions from videos with auto-exposure. The method uses a continuous-time BSpline representation for camera motion and a unified physical imaging model to handle motion blur and varying exposure. The approach is evaluated on both synthetic and real-world datasets, demonstrating superior performance in HDR reconstruction, novel view synthesis, image deblurring, and HDR editing compared to existing methods.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

The paper presents a novel and technically sound approach for HDR reconstruction from casually captured videos with auto-exposure. The unified, differentiable pipeline that jointly optimizes HDR scene reconstruction, camera motion trajectory, exposure times, and camera response functions is a significant contribution. The use of a continuous-time BSpline representation for camera motion and a unified physical imaging model to handle motion blur and varying exposure is well-motivated and technically sound. The paper is well-written and organized, with clear explanations of the technical details and a thorough discussion of the experimental results. The experimental results are comprehensive and demonstrate the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

The paper does not provide a detailed analysis of the computational cost of the proposed method, which is important for assessing its practical applicability. Specifically, the paper lacks a breakdown of the time spent on different stages of the optimization process, such as the joint optimization of camera trajectory, exposure times, and HDR scene reconstruction. This makes it difficult to understand the bottlenecks and potential areas for optimization. Furthermore, the paper does not discuss the memory requirements of the proposed method, which could be a limiting factor for processing high-resolution scenes or large video sequences. A more detailed analysis of the computational and memory requirements is crucial for assessing the practical applicability of the method. The paper also lacks a discussion of the limitations of the proposed method, such as its performance on scenes with extreme motion blur or very high dynamic range. It is important to understand the boundaries of the method's applicability and identify scenarios where it might fail. Finally, the paper does not provide a detailed comparison of the proposed method with other state-of-the-art methods for HDR reconstruction from videos, particularly those that also use a unified approach. It would be beneficial to include a more comprehensive comparison with methods that use different optimization strategies or different physical imaging models. The comparison should also include a discussion of the advantages and disadvantages of the proposed method compared to these alternatives.

### Suggestions

The paper would benefit significantly from a more detailed analysis of the computational cost associated with the proposed method. Specifically, the authors should provide a breakdown of the time spent on different stages of the optimization process, such as the joint optimization of camera trajectory, exposure times, and HDR scene reconstruction. This analysis should include the number of iterations required for convergence and the time spent on each iteration. Furthermore, the authors should discuss the memory requirements of the proposed method, including the memory usage for storing the scene representation, the optimization variables, and the intermediate results. This information is crucial for assessing the practical applicability of the method, especially for processing high-resolution scenes or large video sequences. A clear understanding of the computational and memory requirements is essential for determining the scalability of the method and identifying potential bottlenecks. The authors should also consider providing a comparison of the computational cost of their method with existing approaches, which would further highlight the advantages and disadvantages of their approach.

In addition to the computational analysis, the paper should include a more detailed discussion of the limitations of the proposed method. Specifically, the authors should discuss the performance of the method on scenes with extreme motion blur or very high dynamic range. It is important to understand the boundaries of the method's applicability and identify scenarios where it might fail. For example, the authors could analyze the performance of the method on scenes with rapid camera motion or with significant occlusions. Furthermore, the authors should discuss the sensitivity of the method to the quality of the input video, such as frame resolution, frame rate, and signal-to-noise ratio. This analysis would help to identify the scenarios where the method is most effective and where it may require additional processing or pre-processing steps. A more thorough discussion of the limitations would provide a more balanced and realistic assessment of the method's capabilities.

Finally, the paper should include a more comprehensive comparison of the proposed method with other state-of-the-art methods for HDR reconstruction from videos. This comparison should include a discussion of the advantages and disadvantages of the proposed method compared to these alternatives. The authors should consider including a comparison with methods that use different optimization strategies or different physical imaging models. For example, the authors could compare their method with methods that use a different representation for the scene or methods that use a different approach for handling motion blur. This comparison would help to better contextualize the performance of the proposed method and highlight its unique contributions. The authors should also discuss the potential for combining the proposed method with other techniques to further improve the performance of HDR reconstruction.

### Questions

How does the proposed method perform on scenes with extreme motion blur or very high dynamic range?
What is the computational cost of the proposed method compared to existing approaches? How does the runtime scale with the size of the input dataset?
How robust is the method to errors in camera pose estimation? Can the method be used with less accurate pose estimates from consumer-grade devices?
How does the proposed method compare to other state-of-the-art methods for HDR reconstruction from videos, particularly those that also use a unified approach?

### Rating

6

### Confidence

4

**********
