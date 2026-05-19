### Summary

The paper introduces a novel method for band selection in hyperspectral imaging using the Expectation Maximization (EM) algorithm. The method aims to address the limitations of existing band selection techniques by enhancing sparsity effects and effectively delineating relationships between spectral bands. The proposed approach is supported by theoretical analysis and experimental validation, demonstrating its robustness and practicality. It outperforms other sparsification methods in achieving significant sparsity effects and illustrating inter-band relationships, making it a valuable contribution to the field of hyperspectral imaging.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel approach to band selection using the EM algorithm, which is an innovative contribution to the field of hyperspectral image processing.
2. The paper provides thorough theoretical analysis and proofs to support the proposed method, enhancing the credibility of the approach.
3. The method demonstrates significant sparsity effects and effectively illustrates inter-band relationships, outperforming other sparsification methods.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational complexity of the proposed method, which is important for practical applications, especially when dealing with large-scale hyperspectral datasets.
2. The paper could benefit from a discussion on the limitations of the proposed method and potential avenues for future research. This would provide a more balanced perspective on the approach and its applicability.

### Suggestions

The paper should include a more rigorous analysis of the computational complexity, going beyond just stating the number of operations. Specifically, the authors should analyze the time and space complexity of their dynamic programming algorithm in terms of the number of spectral bands (B) and the number of selected bands (k). This analysis should consider both the forward and backward passes of the algorithm. It would be beneficial to provide a breakdown of the computational cost associated with each step, such as the calculation of the sparsity loss and the gradient computation. Furthermore, the authors should discuss how the computational cost scales with increasing B and k, and whether the method is suitable for very large hyperspectral datasets. A comparison of the computational complexity with other band selection methods would also be valuable to contextualize the efficiency of the proposed approach. This analysis should be supported by empirical results, showing the actual runtime of the algorithm for different dataset sizes and parameter settings.

To address the limitations, the authors should discuss the sensitivity of the method to the choice of the sparsity parameter and how this parameter affects the selected bands and the overall performance. The paper should also explore the potential impact of noise in the hyperspectral data on the performance of the proposed method. It would be beneficial to investigate how the method performs when the underlying assumptions of the EM algorithm are violated, such as when the data does not follow a Gaussian mixture model. Furthermore, the authors should discuss the potential limitations of the method in handling highly correlated bands and whether the method can effectively capture the complex relationships between bands in such cases. The authors should also consider the potential for the method to be extended to other types of data, such as multispectral data or time-series data, and discuss the challenges and opportunities associated with such extensions.

Finally, the paper should discuss the potential for the method to be used in real-time applications, where computational efficiency is critical. This discussion should include an analysis of the trade-offs between accuracy and computational cost, and whether the method can be optimized for real-time performance. The authors should also explore the potential for the method to be integrated with other hyperspectral image processing techniques, such as classification or segmentation, and discuss the benefits and challenges of such integration. The paper should also consider the potential for the method to be used in other applications, such as remote sensing or medical imaging, and discuss the potential for the method to be adapted to these applications. This discussion should provide a more comprehensive view of the applicability and limitations of the proposed method.

### Questions

Please see the Weaknesses.

### Rating

8

### Confidence

2

**********
