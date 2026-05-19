### Summary

This paper presents an efficient approach for calculating tensor products of irreps for E(3)-equivariant neural networks, which are crucial for modeling 3D data. The proposed method leverages a change of basis from spherical harmonics to a 2D Fourier basis, utilizing Gaunt coefficients. This transformation enables the efficient computation of equivariant operations via Fast Fourier Transforms (FFT), reducing the computational complexity from O(L^6) to O(L^3), where L is the maximum degree of irreps. The authors introduce the Gaunt Tensor Product as a versatile method for constructing efficient equivariant operations across various model architectures. Experiments on the Open Catalyst Project and 3BPA datasets demonstrate both the increased efficiency and improved performance of the proposed approach.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper introduces a novel approach for efficient computation of tensor products of irreps by leveraging Gaunt coefficients and a change of basis to a 2D Fourier basis. This method significantly reduces computational complexity, addressing a critical bottleneck in equivariant neural networks for 3D data.

- The proposed Gaunt Tensor Product is versatile and can be integrated into various model architectures, making it a valuable contribution to the field of geometric deep learning.

- The paper provides a thorough mathematical foundation for the proposed method, connecting Clebsch-Gordan coefficients to Gaunt coefficients and establishing the equivalence between tensor products of irreps and multiplication of spherical functions.

- The authors demonstrate the effectiveness of their approach through experiments on major operation classes widely used in equivariant models for the Euclidean group.

### Weaknesses

#### Some Related Works


#### comment

 - The paper could benefit from a more detailed discussion of the practical implementation details and potential challenges in applying the proposed method to real-world problems. Specifically, the paper lacks a thorough exploration of how the theoretical speedups translate to actual computational gains in practical scenarios, considering factors such as memory access patterns, data transfer overhead, and the specific hardware used. The discussion should also address the potential numerical stability issues that might arise when dealing with high-degree irreps or when performing repeated tensor product operations.

- While the paper provides a comprehensive study on major operation classes, further investigation into the applicability of the Gaunt Tensor Product to a wider range of models and tasks could strengthen the claims. The current evaluation focuses on a limited set of architectures and datasets. It would be beneficial to see how the proposed method performs on more complex tasks, such as those involving larger molecular systems or more intricate 3D geometries. Furthermore, the paper should explore the limitations of the method when applied to tasks that require very high-degree irreps, as the computational savings might diminish in such cases.

### Suggestions

The paper should include a more detailed analysis of the practical implementation of the Gaunt Tensor Product. This should include a discussion of the memory layout of the data, the specific libraries used for FFT computations, and the optimization techniques employed to minimize data transfer overhead. For example, the authors could provide a detailed breakdown of the computational cost of each step in the algorithm, including the FFT, the element-wise multiplication in Fourier space, and the inverse FFT. They should also discuss the impact of different batch sizes and irrep degrees on the overall performance. Furthermore, the authors should investigate the numerical stability of the method, especially when dealing with high-degree irreps or when performing repeated tensor product operations. This could involve analyzing the condition number of the transformation matrices and exploring techniques for mitigating numerical errors, such as using higher-precision arithmetic or regularization methods. 

To further validate the versatility of the Gaunt Tensor Product, the authors should expand their experimental evaluation to include a wider range of models and tasks. This could involve testing the method on different molecular datasets, as well as on other types of 3D data, such as point clouds or meshes. The authors should also consider evaluating the method on tasks that require very high-degree irreps, to assess the limitations of the approach. In addition, the paper should include a comparison of the proposed method with other existing techniques for efficient computation of tensor products of irreps, such as those based on sparse tensors or low-rank approximations. This comparison should not only focus on computational efficiency but also on the accuracy and stability of the different methods. The authors should also discuss the trade-offs between computational cost and accuracy, and provide guidelines for choosing the appropriate method for different tasks.

Finally, the paper should provide a more detailed discussion of the limitations of the proposed method. This should include a discussion of the cases where the method might not be applicable or might not provide significant computational savings. For example, the authors could discuss the limitations of the method when dealing with very large systems or with tasks that require very high-degree irreps. They should also discuss the potential challenges in implementing the method on different hardware platforms, such as GPUs or TPUs. By providing a more comprehensive discussion of the limitations of the method, the authors can help the readers to better understand the scope and applicability of their work.

### Questions

N/A

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
