### Summary

This paper proposes a novel memory-efficient framework for 4D Gaussian Splatting, which reduces the number of Gaussians and the storage overhead of Gaussian attributes. Specifically, the authors propose a memory-efficient Gaussian representation and an entropy-constrained Gaussian deformation technique. The proposed method achieves a 190× and 125× reduction in storage compared to the original 4DGS.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide extensive experimental results on two datasets, demonstrating the effectiveness of the proposed method compared to the original 4DGS and other state-of-the-art methods.
3. The proposed method achieves a significant reduction in storage overhead while maintaining comparable rendering quality and real-time performance.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not discuss the limitations of the proposed method. For example, it would be helpful to understand the types of scenes or applications for which the proposed method may not be suitable.
2. The paper does not provide a comparison with other memory-efficient 4D Gaussian Splatting methods. It would be beneficial to include a comparison with other memory-efficient 4D Gaussian Splatting methods, such as Compact 4DGS and other related methods, to demonstrate the advantages and disadvantages of the proposed method.

### Suggestions

The paper would benefit from a more thorough discussion of the limitations of the proposed method. Specifically, the authors should address scenarios where the method might struggle, such as scenes with highly complex or rapidly changing dynamics. It would be valuable to explore the impact of the method on scenes with significant occlusions or lighting variations. Furthermore, the authors should discuss the potential for artifacts or distortions in the rendered images, particularly in areas with high-frequency details. A more detailed analysis of these limitations would provide a more balanced view of the method's capabilities and help guide future research. For example, the authors could investigate how the method performs on scenes with non-rigid object deformations or scenes with significant changes in viewpoint. This analysis should include both qualitative and quantitative results to provide a comprehensive understanding of the method's performance under different conditions.

In addition to the limitations, the paper would be strengthened by a more comprehensive comparison with other memory-efficient 4D Gaussian Splatting methods. While the paper demonstrates a significant reduction in storage compared to the original 4DGS, it is crucial to benchmark the proposed method against other state-of-the-art techniques. This comparison should include not only storage efficiency but also rendering quality and computational cost. For example, the authors could compare their method with Compact 4DGS and other related methods, highlighting the specific scenarios where their method excels or falls short. This would provide a more complete picture of the method's advantages and disadvantages and help readers understand its position within the broader landscape of memory-efficient 4D Gaussian Splatting techniques. The comparison should also include a discussion of the trade-offs between memory efficiency, rendering quality, and computational cost, providing a more nuanced understanding of the method's practical implications.

Finally, the authors should provide more details on the implementation of the proposed method. This includes the specific choices of hyperparameters, the training procedure, and the computational resources used for the experiments. This information is crucial for reproducibility and for other researchers to build upon the proposed method. For example, the authors could provide details on the specific network architecture used for the Gaussian representation and the deformation network. They should also discuss the optimization techniques used for training and the computational cost of the training process. This level of detail would allow other researchers to better understand the method and potentially adapt it to their own applications. Furthermore, the authors should provide a more detailed analysis of the computational complexity of the proposed method, including both training and rendering times.

### Questions

Please refer to the weaknesses.

### Rating

6

### Confidence

3

**********
