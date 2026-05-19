### Summary

This paper presents MEGA, a novel framework for memory-efficient 4D Gaussian Splatting (GS) that addresses the high memory consumption of dynamic 3D scenes. The authors propose a memory-efficient 4D Gaussian representation by decoupling the color attribute into a per-Gaussian direct current (DC) component and a shared lightweight alternating current (AC) color predictor. This approach eliminates the need for spherical harmonics coefficients, reducing memory usage by approximately 190x and 125x on the Technicolor and Neural 3D Video datasets, respectively, compared to the original 4DGS. Additionally, the authors introduce an entropy-constrained Gaussian deformation technique that expands the action range of each Gaussian and integrates a spatial opacity-based entropy loss to limit the number of Gaussians, thus improving rendering efficiency. Experimental results demonstrate that MEGA maintains comparable rendering speeds and scene representation quality while significantly reducing storage requirements and achieving a 190x-125x reduction in memory usage compared to the original 4DGS.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper introduces a novel memory-efficient 4D Gaussian Splatting framework, MEGA, which significantly reduces storage requirements while maintaining high rendering quality and real-time performance.
2. The authors provide extensive experimental results on two datasets, demonstrating the effectiveness of MEGA compared to the original 4DGS and other state-of-the-art methods.
3. The paper is well-structured and clearly written, making it easy to follow and understand the proposed method and its contributions.

### Weaknesses

#### Some Related Works


#### comment

1. The paper introduces a novel memory-efficient 4D Gaussian Splatting framework, MEGA, which significantly reduces storage requirements while maintaining high rendering quality and real-time performance.
2. The authors provide extensive experimental results on two datasets, demonstrating the effectiveness of MEGA compared to the original 4DGS and other state-of-the-art methods.
3. The paper is well-structured and clearly written, making it easy to follow and understand the proposed method and its contributions.

1. The paper introduces a novel memory-efficient 4D Gaussian Splatting framework, MEGA, which significantly reduces storage requirements while maintaining high rendering quality and real-time performance.
2. The authors provide extensive experimental results on two datasets, demonstrating the effectiveness of MEGA compared to the original 4DGS and other state-of-the-art methods.
3. The paper is well-structured and clearly written, making it easy to follow and understand the proposed method and its contributions.

1. The paper introduces a novel memory-efficient 4D Gaussian Splatting framework, MEGA, which significantly reduces storage requirements while maintaining high rendering quality and real-time performance.
2. The authors provide extensive experimental results on two datasets, demonstrating the effectiveness of MEGA compared to the original 4DGS and other state-of-the-art methods.
3. The paper is well-structured and clearly written, making it easy to follow and understand the proposed method and its contributions.

1. The paper introduces a novel memory-efficient 4D Gaussian Splatting framework, MEGA, which significantly reduces storage requirements while maintaining high rendering quality and real-time performance.
2. The authors provide extensive experimental results on two datasets, demonstrating the effectiveness of MEGA compared to the original 4DGS and other state-of-the-art methods.
3. The paper is well-structured and clearly written, making it easy to follow and understand the proposed method and its contributions.

### Suggestions

The paper's core contribution lies in its memory-efficient 4D Gaussian Splatting framework, MEGA, which achieves significant storage reductions by decoupling the color attribute into a per-Gaussian direct current (DC) component and a shared lightweight alternating current (AC) color predictor. While the results are compelling, the paper could benefit from a more detailed analysis of the trade-offs between memory savings and potential loss of rendering quality. Specifically, it would be valuable to see a more granular breakdown of where the memory savings are achieved – is it primarily in the color representation, or are there other factors contributing to the reduction? Furthermore, the paper should explore the limitations of the proposed method, such as potential artifacts or distortions that might arise from the color decomposition. A more thorough investigation into these aspects would strengthen the paper's claims and provide a more complete understanding of the method's capabilities.

To further enhance the paper, the authors should consider including a more comprehensive comparison with existing memory-efficient techniques for Gaussian Splatting. While the paper compares against the original 4DGS and some other methods, a more detailed comparison with techniques that also aim to reduce memory consumption would be beneficial. This would help to contextualize the contributions of MEGA and highlight its unique advantages. For example, it would be useful to see a comparison with methods that use quantization or other compression techniques to reduce the memory footprint of Gaussian splats. Additionally, the paper could explore the impact of different network architectures for the AC color predictor on the overall performance and memory efficiency. A sensitivity analysis of the AC predictor's architecture would provide valuable insights into the robustness and generalizability of the proposed method.

Finally, the paper could benefit from a more detailed discussion of the practical implications of the proposed method. While the results demonstrate real-time performance, it would be useful to explore the scalability of MEGA to larger and more complex scenes. The paper should also discuss the computational overhead associated with the color decomposition and the AC predictor. A more thorough analysis of these practical considerations would help to assess the real-world applicability of MEGA. Furthermore, the authors could explore the potential for further optimization of the method, such as through the use of more efficient data structures or algorithms. This would help to further enhance the practical value of the proposed method and make it more attractive for real-world applications.

### Questions

1. How does the proposed method handle dynamic scenes with significant occlusions or complex lighting conditions? Are there any specific techniques or modifications to address these challenges?
2. What are the computational costs associated with the color decomposition and the alternating current (AC) color predictor? How do these costs compare to the computational overhead of the original 4DGS?
3. How does the proposed method perform on scenes with varying levels of motion and complexity? Are there any limitations or challenges in applying MEGA to highly dynamic or intricate scenes?
4. Could the authors provide more details on the training process, such as the number of iterations, learning rate, and other hyperparameters? How sensitive is the performance of MEGA to these parameters?

### Rating

5

### Confidence

4

**********
