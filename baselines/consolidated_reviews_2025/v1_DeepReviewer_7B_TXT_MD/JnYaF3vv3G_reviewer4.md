### Summary

This paper introduces LabelDP-Pro, a novel algorithm for label differential privacy (label DP) that leverages the input features to denoise the gradients before adding noise. The authors propose several denoisers, including SELFSPAN, ALTCONV, and ALTCONV denoiser, which project the noisy gradients onto the convex hull of the gradients of the batch of samples. The paper provides theoretical analysis of the proposed algorithm and demonstrates its effectiveness through extensive empirical evaluations on various benchmark datasets. The results show that LabelDP-Pro outperforms existing label DP methods in the high-privacy regime.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a novel algorithm for label DP that leverages the input features to denoise the gradients before adding noise. This approach is innovative and addresses the limitations of existing label DP methods that rely solely on randomized response.
2. The paper provides a comprehensive theoretical analysis of the proposed algorithm, including a discussion of the stability of the gradient projections and the convergence of the algorithm.
3. The paper presents extensive empirical evaluations of the proposed algorithm on various benchmark datasets, demonstrating its effectiveness and superiority over existing label DP methods in the high-privacy regime.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed discussion of the computational cost of the proposed algorithm. While the authors mention that the denoising step can be computationally expensive, they do not provide a quantitative analysis of the time and memory requirements of the algorithm. This makes it difficult to assess the practical applicability of the proposed method, especially for large-scale datasets.
2. The paper does not explore the robustness of the proposed algorithm to different types of input features. The authors assume that the input features are publicly available, but they do not investigate how the performance of the algorithm is affected by the quality or type of input features. For example, it would be useful to analyze the performance of the algorithm when the input features are noisy or when they are not representative of the underlying data distribution.
3. The paper does not provide a clear explanation of how the proposed algorithm can be integrated into existing deep learning frameworks. While the authors mention that the algorithm can be used with DP-SGD, they do not provide a detailed description of how to implement the algorithm in practice. This makes it difficult for other researchers to reproduce the results and to apply the algorithm to their own problems.

### Suggestions

The paper should include a more thorough analysis of the computational cost of the proposed algorithm. This should include a breakdown of the time complexity of each step of the algorithm, as well as a comparison of the computational cost of the proposed algorithm with that of existing label DP methods. The analysis should also consider the memory requirements of the algorithm, especially when dealing with large-scale datasets. Furthermore, the authors should provide empirical results on the runtime of the algorithm on different datasets and with different parameter settings. This would help to assess the practical applicability of the proposed method and to identify potential bottlenecks.

The paper should also investigate the robustness of the proposed algorithm to different types of input features. This should include an analysis of how the performance of the algorithm is affected by the quality or type of input features. For example, the authors could investigate the performance of the algorithm when the input features are noisy, or when they are not representative of the underlying data distribution. The authors could also explore the use of different feature selection or feature transformation techniques to improve the robustness of the algorithm. This would help to identify the limitations of the proposed method and to guide future research.

Finally, the paper should provide a more detailed explanation of how the proposed algorithm can be integrated into existing deep learning frameworks. This should include a step-by-step description of how to implement the algorithm in practice, as well as a discussion of any potential challenges or limitations. The authors should also provide code examples or pseudocode to make it easier for other researchers to reproduce the results and to apply the algorithm to their own problems. This would help to increase the accessibility and impact of the proposed method.

### Questions

1. How does the performance of the proposed algorithm vary with different choices of the denoiser? The paper introduces several denoisers, but it does not provide a detailed analysis of how the performance of the algorithm is affected by the choice of denoiser.
2. How does the proposed algorithm perform on datasets with different characteristics, such as datasets with high dimensionality or imbalanced label distributions? The paper evaluates the algorithm on several benchmark datasets, but it does not provide a detailed analysis of how the performance of the algorithm is affected by the characteristics of the datasets.

### Rating

6: marginally above the acceptance threshold

### Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
