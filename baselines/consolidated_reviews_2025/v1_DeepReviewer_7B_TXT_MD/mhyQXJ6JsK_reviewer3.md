### Summary

This paper proposes a novel approach to efficiently compute tensor products of irreducible representations (irreps) for the E(3) group, which is crucial for building equivariant neural networks for 3D data. The key idea is to connect Clebsch-Gordan coefficients with the Gaunt coefficients, enabling the transformation of tensor product operations into multiplication between spherical functions represented by spherical harmonics. This allows the use of the convolution theorem and Fast Fourier Transforms (FFT), significantly reducing the complexity from O(L^6) to O(L^3), where L is the maximum degree of irreps. The authors demonstrate the effectiveness of their approach through experiments on the Open Catalyst 2020 (OC20) dataset and the 3BPA dataset, showing both improved efficiency and competitive performance.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a novel approach to efficiently compute tensor products of irreducible representations (irreps) for the E(3) group, which is crucial for building equivariant neural networks for 3D data. This is a significant contribution to the field of equivariant neural networks.
2. The authors connect Clebsch-Gordan coefficients with the Gaunt coefficients, enabling the transformation of tensor product operations into multiplication between spherical functions represented by spherical harmonics. This allows the use of the convolution theorem and Fast Fourier Transforms (FFT), significantly reducing the complexity from O(L^6) to O(L^3), where L is the maximum degree of irreps.
3. The paper is well-written and easy to follow. The authors provide a comprehensive review of related works in this field, and the proposed method is clearly explained.
4. The authors demonstrate the effectiveness of their approach through experiments on the Open Catalyst 2020 (OC20) dataset and the 3BPA dataset, showing both improved efficiency and competitive performance.

### Weaknesses

#### Some Related Works


#### comment

1. The paper focuses on the E(3) group, which is a specific case of the more general SE(3) group. The authors should discuss the potential challenges and limitations of extending their method to SE(3), which includes rotations in 3D space and translations. Specifically, the method relies on a change of basis to a 2D Fourier basis, which may not directly translate to the 3D Fourier transform required for SE(3) operations. The authors should address how their approach would handle the additional translational degrees of freedom and whether the current framework can be adapted to incorporate these.
2. The paper mentions that the method can be applied to various equivariant operations, but the experiments are limited to a few specific tasks. It would be beneficial to see results on a wider range of tasks, especially those that are known to be challenging for equivariant networks. For example, tasks involving long-range interactions or complex geometric reasoning could reveal potential limitations of the proposed approach. The current experiments, while promising, do not fully demonstrate the general applicability of the method across diverse equivariant network architectures and problem domains.

### Suggestions

The authors should provide a more detailed discussion on the limitations of their method when applied to the SE(3) group. Specifically, they should address how the change of basis to a 2D Fourier basis can be extended to incorporate the 3D Fourier transform, which is necessary for handling translations within SE(3). A clear explanation of the mathematical challenges and potential solutions would significantly strengthen the paper. For instance, the authors could explore the use of tensor products of irreducible representations for SE(3) and discuss how their approach might be adapted to handle the additional complexity introduced by translations. Furthermore, it would be beneficial to discuss the computational cost of the proposed method in the context of SE(3) and compare it to existing approaches for SE(3) equivariant networks. This would provide a more complete picture of the method's applicability and limitations.

To further validate the robustness and general applicability of their method, the authors should include experiments on a broader range of tasks. This should include tasks that are known to be challenging for equivariant networks, such as those involving long-range interactions or complex geometric reasoning. For example, experiments on molecular property prediction or protein structure prediction could provide valuable insights into the method's performance in more complex scenarios. Additionally, it would be useful to compare the performance of the proposed method against other state-of-the-art equivariant networks on these tasks. This would help to establish the method's competitive performance and highlight its potential advantages over existing approaches. The authors should also consider including ablation studies to analyze the impact of different components of their method on the overall performance.

Finally, the authors should provide more details on the implementation of their method, including the specific choices of basis functions and the numerical techniques used for the FFT. This would allow other researchers to reproduce their results and build upon their work. A more detailed description of the experimental setup, including the specific datasets and evaluation metrics used, would also be beneficial. Furthermore, the authors should discuss the potential limitations of their method in terms of memory usage and scalability, especially when applied to large-scale datasets. Addressing these practical considerations would make the paper more complete and useful for the broader research community.

### Questions

1. Can the authors provide more details on the implementation of their method, including the specific choices of basis functions and the numerical techniques used for the FFT?
2. Can the authors provide more details on the experimental setup, including the specific datasets and evaluation metrics used?
3. Can the authors discuss the potential limitations of their method in terms of memory usage and scalability, especially when applied to large-scale datasets?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
