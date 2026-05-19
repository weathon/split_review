### Summary

This paper proposes a new method to accelerate the computation of the tensor products of irreps for the E(3) group. The key idea is to connect the Clebsch-Gordan coefficients with the Gaunt coefficients, and then transform the tensor product of irreps to the multiplication between spherical functions represented by the spherical harmonics. By using the convolution theorem and Fast Fourier Transform, the complexity of the tensor product of irreps can be reduced from O(L^6) to O(L^3). The experiments on the Open Catalyst 2020 (OC20) dataset show the efficiency and effectiveness of the proposed method.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow. The authors provide a clear explanation of the proposed method and the related background knowledge.
- The proposed method is novel and effective. It reduces the complexity of the tensor product of irreps from O(L^6) to O(L^3), which is a significant improvement.
- The experiments on the OC20 dataset show the efficiency and effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

 - The paper focuses on the E(3) group, which is a specific case of the more general SE(3) group. The authors should discuss the potential challenges and limitations of extending their method to SE(3), which includes rotations in 3D space and translations. Specifically, the method relies on a change of basis to a 2D Fourier basis, which may not directly translate to the 3D Fourier transform required for SE(3) operations. The authors should address how their approach would handle the additional translational degrees of freedom and whether the current framework can be adapted to incorporate these.
- The paper mentions that the method can be applied to various equivariant operations, but the experiments are limited to a few specific tasks. It would be beneficial to see results on a wider range of tasks, especially those that are known to be challenging for equivariant networks. For example, tasks involving long-range interactions or complex geometric reasoning could reveal potential limitations of the proposed approach. The current experiments, while promising, do not fully demonstrate the general applicability of the method across diverse equivariant network architectures and problem domains.

### Suggestions

The authors should provide a more detailed discussion on the limitations of their method when applied to the SE(3) group. Specifically, they should address how the change of basis to a 2D Fourier basis can be extended to incorporate the 3D Fourier transform, which is necessary for handling translations within SE(3). A clear explanation of the mathematical challenges and potential solutions would significantly strengthen the paper. For instance, the authors could explore the use of tensor products of irreducible representations for SE(3) and discuss how their approach might be adapted to handle the additional complexity introduced by translations. Furthermore, it would be beneficial to discuss the computational cost of the proposed method in the context of SE(3) and compare it to existing approaches for SE(3) equivariant networks. This would provide a more complete picture of the method's applicability and limitations.

To further validate the robustness and general applicability of their method, the authors should include experiments on a broader range of tasks. This should include tasks that are known to be challenging for equivariant networks, such as those involving long-range interactions or complex geometric reasoning. For example, experiments on molecular property prediction or protein structure prediction could provide valuable insights into the method's performance in more complex scenarios. Additionally, it would be useful to compare the performance of the proposed method against other state-of-the-art equivariant networks on these tasks. This would help to establish the method's competitive performance and highlight its potential advantages over existing approaches. The authors should also consider including ablation studies to analyze the impact of different components of their method on the overall performance.

Finally, the authors should provide more details on the implementation of their method, including the specific choices of basis functions and the numerical techniques used for the FFT. This would allow other researchers to reproduce their results and build upon their work. A more detailed description of the experimental setup, including the specific datasets and evaluation metrics used, would also be beneficial. Furthermore, the authors should discuss the potential limitations of their method in terms of memory usage and scalability, especially when applied to large-scale datasets. Addressing these practical considerations would make the paper more complete and useful for the broader research community.

### Questions

Please see the weaknesses.

### Rating

8: accept, good paper

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
