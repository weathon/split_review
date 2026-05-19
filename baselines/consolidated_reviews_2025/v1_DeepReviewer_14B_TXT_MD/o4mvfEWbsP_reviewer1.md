### Summary

This paper proposes a novel band selection method for hyperspectral images based on the Expectation Maximization (EM) algorithm. The author introduce a Sparsity Loss based on the EM algorithm to enhance sparsity in the levels of importance, which not only improves sparsity effects but also theoretically facilitates the exploration of relationships between spectral bands. The author provide comprehensive theoretical analysis and experimental validation to confirm the sparsity effects and the capability of the proposed method to accurately depict inter-band relationships. The method achieves state-of-the-art performance in band selection methods.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper introduces a novel approach to band selection using the EM algorithm, which is an innovative contribution to the field of hyperspectral image processing.
2. The paper provides thorough theoretical analysis and proofs to support the proposed method, enhancing the credibility of the approach.

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

None

### Rating

5

### Confidence

4

**********
