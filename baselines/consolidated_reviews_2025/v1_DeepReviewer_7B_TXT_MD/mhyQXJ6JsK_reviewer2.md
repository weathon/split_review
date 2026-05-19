### Summary

This paper proposes a new approach to speed up the computation of the tensor products of irreps of the E(3) group. The idea is to use the connection between Clebsch-Gordan coefficients and Gaunt coefficients to change the basis of the tensor product of irreps from spherical harmonics to a 2D Fourier basis, which allows to use the convolution theorem and Fast Fourier Transforms to accelerate the computation. This reduces the complexity of full tensor products of irreps from O(L^6) to O(L^3), where L is the max degree of irreps. The proposed method is evaluated on the Open Catalyst 2020 (OC20) dataset, and the results show that the proposed method achieves better performance and efficiency compared to the baselines.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The proposed method is novel and effective. It uses the connection between Clebsch-Gordan coefficients and Gaunt coefficients to change the basis of the tensor product of irreps from spherical harmonics to a 2D Fourier basis, which allows to use the convolution theorem and Fast Fourier Transforms to accelerate the computation. This reduces the complexity of full tensor products of irreps from O(L^6) to O(L^3), where L is the max degree of irreps. The proposed method is evaluated on the Open Catalyst 2020 (OC20) dataset, and the results show that the proposed method achieves better performance and efficiency compared to the baselines.

2. The paper is well-written and easy to follow. The authors provide a clear explanation of the proposed method and the experimental results are well-presented.

3. The proposed method has the potential to be applied to a wide range of equivariant neural networks for the E(3) group, and it can be used to improve the efficiency of these networks without sacrificing accuracy.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is only evaluated on the Open Catalyst 2020 (OC20) dataset. It would be better to evaluate the proposed method on other datasets, such as the OC20 S2EF and 3BPA datasets, to demonstrate its generalizability and robustness.

2. The proposed method is only evaluated on equivariant neural networks for the E(3) group. It would be better to evaluate the proposed method on other equivariant neural networks for the E(3) group, such as the EquiformerV2 model, to demonstrate its generalizability and robustness.

### Suggestions

The paper introduces a novel approach to accelerate tensor product computations for E(3) group irreps using a change of basis to a 2D Fourier basis, which is a promising direction. However, the evaluation is limited to a single dataset and model architecture. To strengthen the paper, it is crucial to demonstrate the method's effectiveness across a broader range of datasets and model architectures. Specifically, the authors should consider evaluating the method on datasets like OC20 S2EF and 3BPA, which have different characteristics and challenges compared to the OC20 dataset. This would provide a more comprehensive understanding of the method's generalizability and robustness. Furthermore, the evaluation should not be limited to a single model architecture. The authors should evaluate the method on other equivariant neural networks for the E(3) group, such as the EquiformerV2 model, to demonstrate its generalizability and robustness across different model architectures. This would provide a more comprehensive understanding of the method's generalizability and robustness.

In addition to expanding the evaluation, it would be beneficial to provide a more detailed analysis of the computational benefits of the proposed method. While the paper mentions a reduction in complexity from O(L^6) to O(L^3), it would be helpful to include a more detailed breakdown of the computational costs, including the time and memory requirements for different values of L. This would allow readers to better understand the practical implications of the proposed method. Furthermore, it would be beneficial to compare the performance of the proposed method with other existing methods for accelerating tensor product computations. This would provide a more comprehensive understanding of the proposed method's advantages and limitations. The authors should also discuss the limitations of the proposed method and potential directions for future research. For example, it would be interesting to explore the applicability of the proposed method to other groups beyond the E(3) group.

Finally, the paper would benefit from a more detailed explanation of the connection between Clebsch-Gordan coefficients and Gaunt coefficients. While the paper mentions this connection, it would be helpful to provide a more in-depth explanation of the underlying mathematical principles. This would make the paper more accessible to a wider audience and would also help readers to better understand the theoretical foundations of the proposed method. The authors should also provide more details on the implementation of the proposed method. This would include a description of the specific algorithms used and the data structures employed. This would allow other researchers to reproduce the results and to build upon the proposed method.

### Questions

1. How does the proposed method perform on other datasets, such as the OC20 S2EF and 3BPA datasets?

2. How does the proposed method perform on other equivariant neural networks for the E(3) group, such as the EquiformerV2 model?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
