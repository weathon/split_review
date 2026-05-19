### Summary

The paper introduces a method for reconstructing high dynamic range (HDR) scenes from casually captured videos using consumer-grade devices. The key innovation is a unified, differentiable pipeline that jointly optimizes HDR scene reconstruction, camera motion trajectory, exposure times, and camera response functions from videos with auto-exposure. The method uses a continuous-time BSpline representation for camera motion and a unified physical imaging model to handle motion blur and varying exposure. The approach is evaluated on both synthetic and real-world datasets, demonstrating superior performance in HDR reconstruction, novel view synthesis, image deblurring, and HDR editing compared to existing methods.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The unified approach of jointly optimizing HDR reconstruction, camera motion, exposure, and CRF is novel and addresses a key limitation of prior methods that require separate stages or manual tuning.
- The method is robust to real-world challenges like motion blur and varying exposure, which are common in casual videos captured by consumer-grade devices.
- Comprehensive experiments on both synthetic and real-world datasets demonstrate the effectiveness of the proposed method, outperforming existing approaches in novel view synthesis, deblurring, and HDR editing.
- The introduction of a new dataset of casually captured videos with ground truth HDR scenes is a valuable contribution to the community, providing a resource for evaluating HDR reconstruction methods under realistic conditions.
- The method is technically sound, with a well-motivated physical imaging model and a robust optimization strategy. The use of continuous-time BSpline representation for camera motion is well-suited for handling complex camera trajectories.
- The paper is well-written and organized, with clear explanations of the technical details and a thorough discussion of the experimental results.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the computational cost of the proposed method, which is important for assessing its practical applicability. Specifically, the paper lacks a breakdown of the time spent on different stages of the optimization process, such as the joint optimization of camera trajectory, exposure times, and HDR scene reconstruction. This makes it difficult to understand the bottlenecks and potential areas for optimization.
- The method relies on accurate camera poses, which can be challenging to obtain for casual videos captured by consumer-grade devices. The paper does not discuss the impact of pose estimation errors on the final reconstruction quality. It would be beneficial to include an analysis of how errors in camera pose estimation affect the accuracy of the HDR reconstruction, and whether the method is robust to such errors.
- The paper does not explore the limitations of the proposed method, such as its performance on scenes with extreme motion blur or very high dynamic range. It is important to understand the boundaries of the method's applicability and identify scenarios where it might fail. For example, the paper should discuss how the method performs when the motion blur is caused by fast camera movements or when the scene contains very bright or very dark regions that are difficult to capture in a single exposure.
- The paper does not provide a detailed comparison of the proposed method with other state-of-the-art methods for HDR reconstruction from videos, particularly those that also use a unified approach. It would be helpful to include a more comprehensive comparison with methods that use different optimization strategies or different physical imaging models. The comparison should also include a discussion of the advantages and disadvantages of the proposed method compared to these alternatives.

### Suggestions

The paper would benefit from a more detailed analysis of the computational cost of the proposed method. The authors should provide a breakdown of the time spent on different stages of the optimization process, such as the joint optimization of camera trajectory, exposure times, and HDR scene reconstruction. This analysis should include the number of iterations required for convergence and the time spent on each iteration. Furthermore, the authors should discuss the scalability of the method to larger datasets and more complex scenes. It would also be beneficial to explore techniques for reducing the computational cost, such as using more efficient optimization algorithms or parallelizing the computation. A thorough analysis of the computational cost is essential for assessing the practical applicability of the method and identifying potential bottlenecks.

The paper should also include a more detailed analysis of the impact of camera pose estimation errors on the final reconstruction quality. The authors should conduct experiments with varying levels of pose estimation errors and analyze how these errors affect the accuracy of the HDR reconstruction. This analysis should include a discussion of the robustness of the method to pose estimation errors and identify scenarios where the method might fail. Furthermore, the authors should explore techniques for improving the accuracy of camera pose estimation, such as using more robust pose estimation algorithms or incorporating additional constraints into the optimization process. A thorough analysis of the impact of pose estimation errors is crucial for understanding the limitations of the method and identifying areas for improvement.

Finally, the paper should include a more comprehensive comparison with other state-of-the-art methods for HDR reconstruction from videos. The comparison should include a discussion of the advantages and disadvantages of the proposed method compared to these alternatives. The authors should also explore the limitations of the proposed method, such as its performance on scenes with extreme motion blur or very high dynamic range. It would be beneficial to include experiments on a wider range of datasets and scenarios to assess the generalizability of the method. The comparison should also include a discussion of the computational cost and memory requirements of the different methods. A more comprehensive comparison is essential for understanding the contributions of the proposed method and identifying areas for future research.

### Questions

- How does the proposed method handle scenes with extreme motion blur or very high dynamic range?
- What is the computational cost of the proposed method compared to existing approaches? How does the runtime scale with the size of the input dataset?
- How robust is the method to errors in camera pose estimation? Can the method be used with less accurate pose estimates from consumer-grade devices?
- How does the proposed method compare to other state-of-the-art methods for HDR reconstruction from videos, particularly those that also use a unified approach?

### Rating

6

### Confidence

4

**********
