### Summary

The paper proposes a memory-efficient framework for 4D Gaussian Splatting, which includes a memory-efficient 4D Gaussian representation and an entropy-constrained Gaussian deformation technique. The memory-efficient 4D Gaussian representation reduces the storage overhead by 190× and 125× on the Technicolor and Neural 3D Video datasets, respectively, compared to the original 4DGS. The entropy-constrained Gaussian deformation technique improves the utilization rate of each Gaussian and reduces the number of Gaussians required for rendering. Experimental results demonstrate that the proposed method achieves significant storage reductions while maintaining comparable rendering speeds and scene representation quality.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper presents a novel memory-efficient 4D Gaussian representation that significantly reduces storage requirements without compromising rendering quality. The proposed method achieves a 190× reduction in storage on the Technicolor dataset and a 125× reduction on the Neural 3D Video dataset compared to the original 4DGS.

2. The paper introduces an entropy-constrained Gaussian deformation technique that expands the action range of each Gaussian and reduces the number of Gaussians required for rendering. This technique improves the utilization rate of each Gaussian and maintains high rendering quality with fewer Gaussians.

3. The paper provides extensive experimental results that demonstrate the effectiveness of the proposed method in reducing storage requirements while maintaining comparable rendering speeds and scene representation quality. The results show that the proposed method outperforms the original 4DGS and other state-of-the-art methods in terms of storage efficiency and rendering quality.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational complexity of the proposed method. While the paper mentions that the proposed method achieves significant storage reductions while maintaining comparable rendering speeds, it does not provide a detailed analysis of the computational complexity of the proposed method. It would be beneficial to include a more detailed analysis of the computational complexity of the proposed method, including the time and memory requirements for training and rendering.

2. The paper does not discuss the limitations of the proposed method. It would be beneficial to include a discussion of the limitations of the proposed method, such as the types of scenes or applications for which the proposed method may not be suitable.

3. The paper does not provide a comparison with other memory-efficient 4D Gaussian Splatting methods. It would be beneficial to include a comparison with other memory-efficient 4D Gaussian Splatting methods, such as Compact 4DGS and other related methods, to demonstrate the advantages and disadvantages of the proposed method.

### Suggestions

The paper would benefit from a more thorough analysis of the computational overhead introduced by the proposed memory-efficient 4D Gaussian representation and the entropy-constrained Gaussian deformation technique. While the paper claims comparable rendering speeds, a detailed breakdown of the time spent on different stages of the rendering pipeline, such as Gaussian sampling, color reconstruction, and rasterization, would be valuable. Specifically, the authors should analyze the impact of the proposed method on the memory bandwidth requirements and the computational cost of each stage. Furthermore, it would be beneficial to provide a comparison of the computational complexity of the proposed method with the original 4DGS and other state-of-the-art methods, including a discussion of the trade-offs between memory efficiency and computational cost. This analysis should include both training and rendering times, as well as memory usage during both phases.

In addition to the computational analysis, the paper should include a more comprehensive discussion of the limitations of the proposed method. This discussion should address the types of scenes or applications where the proposed method may not be suitable. For example, the authors should discuss the potential challenges in representing complex scene dynamics or high-frequency details with the proposed memory-efficient representation. It would also be beneficial to analyze the sensitivity of the method to different hyperparameter settings and to discuss the potential impact of these settings on the rendering quality and storage efficiency. Furthermore, the authors should discuss the limitations of the proposed method in terms of its ability to represent dynamic scenes, and how the method might be extended to handle more complex motion patterns. This discussion should also include the limitations of the method in terms of its ability to represent scenes with varying levels of detail.

Finally, the paper should include a more comprehensive comparison with other memory-efficient 4D Gaussian Splatting methods. The authors should not only compare the storage efficiency of the proposed method with other methods, but also compare the rendering quality and computational cost. This comparison should include a discussion of the advantages and disadvantages of the proposed method compared to other methods. For example, the authors should compare the proposed method with Compact 4DGS and other related methods, highlighting the specific scenarios where the proposed method outperforms or underperforms. This comparison should also include a discussion of the trade-offs between memory efficiency, rendering quality, and computational cost. The authors should also discuss the potential for combining the proposed method with other memory-efficient techniques to further improve the overall performance.

### Questions

Please see the weaknesses.

### Rating

6

### Confidence

3

**********
