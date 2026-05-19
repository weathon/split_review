### Summary

This paper proposes a novel mapping function based on a p-norm distance, allowing for adaptive sampling of rays based on scene geometry. Additionally, it introduces a new ray parameterization technique that considers the distortion of the embedding space. The method is evaluated on multiple datasets, including challenging unbounded scene scenarios, and demonstrates state-of-the-art results.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is technically sound and addresses an important problem in NeRF rendering.
3. The authors provide extensive experiments to validate the effectiveness of their approach, demonstrating state-of-the-art results on challenging unbounded scene scenarios.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the computational overhead introduced by the proposed method. Specifically, the adaptive sampling strategy based on the p-norm distance and the ray parameterization technique may introduce significant computational costs, which could limit the practical applicability of the method, especially for real-time applications. A thorough analysis of the time complexity and memory usage of the proposed method compared to existing approaches is needed.
2. The effectiveness of the proposed method heavily relies on the accuracy of the estimated p-value using RANSAC. The paper does not provide a detailed analysis of the sensitivity of the method to the accuracy of the p-value estimation. If the p-value is not accurately estimated, the adaptive sampling strategy may not perform as intended, leading to suboptimal results. The paper should include an analysis of how the performance of the method varies with different levels of p-value estimation accuracy.
3. The paper does not provide a comprehensive comparison with other state-of-the-art methods for unbounded scene rendering. While the paper demonstrates state-of-the-art results on several datasets, it would be beneficial to compare the proposed method with a wider range of existing methods, including those that use different approaches for handling unbounded scenes. This would provide a more comprehensive evaluation of the proposed method and highlight its strengths and weaknesses.

### Suggestions

The paper should include a more detailed analysis of the computational cost associated with the proposed method. This analysis should include a breakdown of the time complexity of each step of the algorithm, including the adaptive sampling strategy and the ray parameterization technique. It would be beneficial to provide empirical results on the runtime of the method on different hardware configurations, including GPUs and CPUs, to demonstrate its practical applicability. Furthermore, the analysis should consider the impact of different parameter settings on the computational cost of the method, such as the number of samples per ray and the number of iterations in the RANSAC algorithm. This would provide a more complete understanding of the computational trade-offs of the proposed method.

To address the sensitivity to the p-value estimation, the paper should include a detailed analysis of how the performance of the method varies with different levels of p-value estimation accuracy. This analysis should include experiments with different levels of noise in the p-value estimation and different methods for estimating the p-value. The paper should also provide a discussion of the limitations of the RANSAC-based approach for estimating the p-value and explore alternative methods for estimating the p-value that are more robust to noise and outliers. This would provide a more comprehensive understanding of the robustness of the proposed method to errors in the p-value estimation.

Finally, the paper should include a more comprehensive comparison with other state-of-the-art methods for unbounded scene rendering. This comparison should include a wider range of existing methods, including those that use different approaches for handling unbounded scenes. The comparison should include both quantitative and qualitative results, including metrics such as PSNR, SSIM, and LPIPS, as well as visual comparisons of the rendered images. The paper should also discuss the strengths and weaknesses of the proposed method compared to existing methods, highlighting the specific scenarios where the proposed method performs best and the scenarios where it may not be the most suitable approach. This would provide a more complete evaluation of the proposed method and its place in the existing literature.

### Questions

1. How does the proposed method handle cases where the estimated p-value is inaccurate? Does the method have any mechanisms to mitigate the impact of inaccurate p-value estimation?
2. How does the proposed method compare to other state-of-the-art methods for unbounded scene rendering, particularly those that use different approaches for handling unbounded scenes?

### Rating

6

### Confidence

4

**********
