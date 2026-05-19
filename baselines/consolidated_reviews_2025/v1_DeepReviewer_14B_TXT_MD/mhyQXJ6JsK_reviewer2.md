### Summary

This paper introduces a novel approach to accelerate the computation of tensor products of irreducible representations (irreps) for E(3)-equivariant neural networks. The authors establish a connection between Clebsch-Gordan coefficients and Gaunt coefficients, which allows them to reformulate the tensor product operation as multiplication between spherical functions represented by spherical harmonics. By changing the basis to a 2D Fourier basis, they leverage Fast Fourier Transforms (FFT) to efficiently compute the tensor products, reducing the computational complexity from O(L^6) to O(L^3), where L is the maximum degree of irreps. The proposed method, called the Gaunt Tensor Product, is demonstrated to be effective in improving both the efficiency and performance of equivariant neural networks across various tasks and datasets.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper presents a novel approach to accelerate the computation of tensor products of irreps by leveraging the connection between Clebsch-Gordan and Gaunt coefficients. This connection allows for a reformulation of the tensor product operation, enabling the use of efficient FFT-based computations.
2. The proposed Gaunt Tensor Product significantly reduces the computational complexity from O(L^6) to O(L^3), which is a substantial improvement. This reduction in complexity enables the use of higher-degree irreps, potentially leading to improved model performance.
3. The authors demonstrate the effectiveness of their approach across various tasks and datasets, including the Open Catalyst Project and 3BPA datasets. The experiments show both increased efficiency and improved performance compared to existing methods.
4. The paper provides a comprehensive study on major operation classes widely used in equivariant models for the Euclidean group, demonstrating the generality of the proposed method and its applicability to different model designs.

### Weaknesses

#### Some Related Works


#### comment

1. While the paper provides a comprehensive study on major operation classes, it would be beneficial to explore the applicability of the Gaunt Tensor Product to a wider range of equivariant models and tasks. Specifically, the current evaluation focuses on a limited set of architectures and datasets. It is unclear how the proposed method would perform in scenarios involving more complex data structures or different types of equivariant layers. For instance, the method's performance on models employing different types of attention mechanisms or those designed for point cloud data could be further investigated.
2. The paper could benefit from a more detailed discussion of the practical implementation details and potential challenges in applying the proposed method to real-world problems. The current description lacks specifics on how the change of basis to the 2D Fourier basis is implemented in practice, and how the Gaunt coefficients are efficiently computed and stored. Furthermore, the paper does not address potential numerical stability issues that may arise when dealing with high-degree irreps or when performing repeated tensor product operations.

### Suggestions

To strengthen the paper, the authors should consider expanding their experimental evaluation to include a more diverse set of equivariant models and tasks. This could involve testing the Gaunt Tensor Product on models that utilize different types of equivariant layers, such as those based on attention mechanisms or those designed for point cloud data. Furthermore, it would be beneficial to evaluate the method's performance on datasets with varying levels of complexity and size. This would provide a more comprehensive understanding of the method's strengths and limitations, and would help to establish its general applicability. Specifically, the authors could consider including experiments on datasets with more complex molecular structures or on tasks involving 3D object recognition or scene understanding. Such experiments would help to demonstrate the robustness and versatility of the proposed method.

In addition to expanding the experimental evaluation, the authors should provide a more detailed discussion of the practical implementation details of the Gaunt Tensor Product. This should include a step-by-step explanation of how the change of basis to the 2D Fourier basis is performed, and how the Gaunt coefficients are computed and stored efficiently. The authors should also address potential numerical stability issues that may arise when dealing with high-degree irreps or when performing repeated tensor product operations. This could involve discussing techniques for mitigating numerical errors, such as using higher-precision arithmetic or employing regularization methods. Furthermore, the authors should provide a more detailed analysis of the computational cost of the proposed method, including the time and memory requirements for different values of L and different batch sizes. This would help to provide a more complete picture of the method's efficiency and scalability.

Finally, the authors should consider providing a more detailed comparison of their method with existing techniques for accelerating tensor product computations. This comparison should not only focus on computational efficiency but also on the accuracy and stability of the different methods. The authors should also discuss the trade-offs between the different approaches, and should provide guidance on when the Gaunt Tensor Product is most likely to be beneficial. This would help to position the proposed method within the broader context of equivariant neural networks and would provide valuable insights for practitioners.

### Questions

1. Could the authors provide more details on the practical implementation of the Gaunt Tensor Product, including the specific steps involved in changing the basis to the 2D Fourier basis and computing the Gaunt coefficients?
2. How does the proposed method handle numerical stability issues when dealing with high-degree irreps or repeated tensor product operations?
3. What are the potential limitations of the Gaunt Tensor Product, and in what scenarios might it not be the most suitable approach for accelerating tensor product computations?

### Rating

6: marginally above the acceptance threshold

### Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
