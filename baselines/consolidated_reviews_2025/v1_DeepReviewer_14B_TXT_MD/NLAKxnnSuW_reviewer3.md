### Summary

This paper introduces MEGA, a memory-efficient framework for 4D Gaussian Splatting (4DGS) that addresses the high memory and storage requirements of representing complex dynamic 3D scenes. The framework reduces memory usage by decomposing color attributes into a per-Gaussian direct color component and a shared lightweight alternating current color predictor, eliminating the need for spherical harmonics coefficients. Additionally, an entropy-constrained Gaussian deformation technique is proposed to limit the number of Gaussians needed, further enhancing memory efficiency. The framework achieves significant storage reductions (190x and 125x on Technicolor and Neural 3D Video datasets, respectively) while maintaining comparable rendering speeds and scene quality, setting a new benchmark for memory-efficient dynamic scene representation.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel approach to compressing 4D Gaussian Splatting (4DGS) by decomposing color attributes into a per-Gaussian direct color component and a shared lightweight alternating current color predictor. This innovative method significantly reduces memory usage without compromising performance, addressing a critical limitation in 4DGS.

2. The proposed entropy-constrained Gaussian deformation technique is a creative solution to limit the number of Gaussians required, enhancing memory efficiency. This approach demonstrates originality in addressing the challenge of representing complex dynamic scenes with minimal memory footprint.

### Weaknesses

#### Some Related Works


#### comment

1. While the paper introduces a memory-efficient framework, it lacks a detailed analysis of the trade-offs between memory savings and potential impacts on rendering quality or flexibility. A more thorough discussion of these trade-offs would provide a clearer understanding of the framework's limitations and applicability in various scenarios. Specifically, the paper does not quantify the potential loss in high-frequency details or subtle color variations due to the compressed color representation. It would be beneficial to see a more rigorous analysis of how the direct color component and the shared AC predictor affect the reconstruction of complex scenes with intricate lighting and shading.

2. The paper could benefit from a more comprehensive comparison with existing state-of-the-art methods in terms of memory efficiency and rendering quality. Including such comparisons would help to better contextualize the contributions of the proposed framework and highlight its advantages over other approaches. The current comparison is limited, and a more detailed analysis against other compression techniques for 4DGS, or even against alternative scene representation methods, would strengthen the paper's claims. For example, a comparison with methods that use different types of basis functions for color representation or those that employ more aggressive pruning strategies would be valuable.

3. The paper's discussion on the scalability of the proposed framework to larger or more complex dynamic scenes is limited. Providing insights into how the framework performs under such conditions would enhance the paper's contribution to the field. The paper does not address how the memory savings and rendering quality scale with the number of Gaussians or the temporal duration of the scene. It is unclear if the proposed method would maintain its efficiency for very long or highly complex dynamic scenes, which is a crucial aspect for practical applications.

### Suggestions

To address the lack of detailed analysis on the trade-offs between memory savings and rendering quality, the authors should include a more in-depth quantitative evaluation of the impact of their compression techniques. This should involve not only overall metrics like PSNR or SSIM, but also metrics that are more sensitive to high-frequency details and color accuracy, such as perceptual metrics or frequency analysis. The authors should also provide visual examples that highlight the differences in rendering quality between the original 4DGS and their compressed version, particularly in scenes with complex lighting and shading. Furthermore, a discussion on the limitations of the direct color component and the shared AC predictor in representing certain types of color variations would be beneficial. This would provide a more complete understanding of the framework's capabilities and limitations.

To improve the comparison with existing state-of-the-art methods, the authors should include a more comprehensive benchmark against other compression techniques for 4DGS. This should include a comparison with methods that use different types of basis functions for color representation, such as spherical harmonics or Fourier bases, and those that employ more aggressive pruning strategies. The comparison should not only focus on memory efficiency but also on rendering quality and speed. It would also be valuable to compare the proposed method against alternative scene representation methods, such as neural radiance fields, to provide a broader context for the framework's contributions. This would help to better contextualize the advantages and disadvantages of the proposed approach.

To address the limited discussion on scalability, the authors should provide a more detailed analysis of how the framework performs with larger and more complex dynamic scenes. This should include experiments with scenes that have a larger number of Gaussians, longer temporal durations, and more complex motion patterns. The authors should also discuss the computational cost of the proposed deformation technique and how it scales with the complexity of the scene. It would be beneficial to provide insights into the memory usage and rendering speed for different scene complexities, which would help to understand the practical applicability of the framework. This analysis should also include a discussion of the limitations of the framework in handling extremely complex scenes and potential strategies for further optimization.

### Questions

1. Could the authors provide more details on how the direct color component and the shared alternating current color predictor are optimized during training? Specifically, how do these components interact to maintain rendering quality while achieving memory reduction?

2. How does the proposed entropy-constrained Gaussian deformation technique affect the flexibility and accuracy of representing complex motions in dynamic scenes? Are there specific types of motions or scene changes where this technique might be less effective?

3. The paper mentions using half-precision storage and zip compression to further reduce memory footprint. Could the authors provide more details on the implementation of these techniques and their impact on the overall performance and storage efficiency?

### Rating

6

### Confidence

4

**********
