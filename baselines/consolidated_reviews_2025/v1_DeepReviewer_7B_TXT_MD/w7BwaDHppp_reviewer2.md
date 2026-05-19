### Summary

This paper introduces a novel mapping function that considers per-scene geometry to address the challenges of unbounded NeRF rendering. The authors propose a p-norm distance to adaptively sample rays, allowing for a more efficient use of the neural network's capacity. Additionally, they introduce a new ray parameterization technique that accounts for the distortion of the embedding space. The proposed method demonstrates state-of-the-art novel view synthesis results on challenging unbounded scene scenarios.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow, with a clear presentation of the proposed method and its motivation.
2. The proposed method is technically sound and addresses an important problem in NeRF rendering.
3. The authors provide extensive experiments to validate the effectiveness of their approach, demonstrating state-of-the-art results on challenging unbounded scene scenarios.

### Weaknesses

#### Some Related Works


#### comment

1. The method's reliance on RANSAC for p-value estimation may introduce computational overhead, especially for large-scale scenes or real-time applications. The paper does not provide a detailed analysis of the computational complexity of the RANSAC algorithm in this context, nor does it compare the runtime with other methods. This lack of analysis makes it difficult to assess the practical applicability of the method in scenarios with limited computational resources.
2. The performance of the proposed method may be sensitive to the choice of parameters, such as the number of points used in RANSAC and the range of the p-norm. The paper lacks a thorough sensitivity analysis of these parameters, which could affect the robustness and generalizability of the method. Specifically, the paper does not explore how the performance varies with different numbers of RANSAC iterations or different ranges for the p-norm parameter, making it unclear how to choose these parameters for optimal performance.
3. The paper could benefit from a more thorough comparison with recent state-of-the-art methods in NeRF rendering, particularly those that also address unbounded scenes. The current comparison is limited to a few methods, and it is not clear how the proposed method compares to the most recent advances in the field. A more comprehensive comparison would help to better contextualize the contributions of the paper and highlight its advantages and limitations.

### Suggestions

The paper would benefit from a more detailed analysis of the computational complexity of the proposed method, particularly concerning the RANSAC algorithm. The authors should provide a breakdown of the time complexity of each step in the RANSAC process, including the point sampling, distance calculations, and outlier rejection. This analysis should be compared to the computational cost of other methods, such as those that use a fixed p-norm or other adaptive sampling techniques. Furthermore, the authors should investigate the impact of different parameter settings on the runtime of the RANSAC algorithm, such as the number of iterations and the number of points used for outlier detection. This would provide a more complete understanding of the computational trade-offs involved in using the proposed method.

To address the sensitivity to parameter choices, the authors should conduct a thorough sensitivity analysis of the parameters used in the RANSAC algorithm and the p-norm distance. This analysis should include a systematic exploration of the parameter space, varying the number of points used in RANSAC, the number of iterations, and the range of the p-norm parameter. The authors should report the performance of the method for different parameter settings, using metrics such as PSNR, SSIM, and LPIPS. This would help to identify the optimal parameter settings for different scenarios and provide guidance for users of the method. Additionally, the authors should investigate the robustness of the method to different parameter choices, such as the sensitivity to outliers or the impact of parameter variations on the quality of the rendered images.

Finally, the paper should include a more comprehensive comparison with recent state-of-the-art methods in NeRF rendering, particularly those that address unbounded scenes. This comparison should include a variety of methods, such as those that use different mapping functions or ray parameterizations. The authors should report the performance of the proposed method and the other methods on a common set of datasets, using the same evaluation metrics. This would allow for a more objective assessment of the contributions of the paper and highlight its advantages and limitations. The authors should also discuss the differences between the proposed method and the other methods, and explain why the proposed method is better suited for unbounded scene rendering.

### Questions

1. How does the proposed method handle cases where the estimated p-value is inaccurate? Does the method have any mechanisms to mitigate the impact of inaccurate p-value estimation?
2. How does the proposed method compare to other state-of-the-art methods for unbounded scene rendering, particularly those that use different approaches for handling unbounded scenes?

### Rating

6

### Confidence

4

**********
