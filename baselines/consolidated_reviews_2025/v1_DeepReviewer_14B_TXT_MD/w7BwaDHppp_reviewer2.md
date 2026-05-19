### Summary

This paper proposes a novel projective mapping based on the p-norm distance for unbounded neural radiance fields. It also introduces a new ray parameterization to properly allocate ray samples in the geometry of unbounded regions. The authors show that the proposed method can be integrated into different types of NeRF frameworks and achieves state-of-the-art view synthesis results on several challenging datasets.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The proposed p-norm mapping function and ray parameterization are reasonable and effective.
2. The proposed method can be integrated into different types of NeRF frameworks and achieves state-of-the-art view synthesis results on several challenging datasets.
3. The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

1. The authors mention that the p-norm mapping function is flexible and general to learn both bounded and unbounded regions in neural radiance fields. However, the experiments only demonstrate the effectiveness of the proposed method on unbounded regions. It would be better to conduct experiments on bounded regions as well, to fully validate the claim of general applicability. The current experiments do not sufficiently demonstrate the method's performance in scenarios where the scene is fully contained within a bounded volume, which is a common use case for NeRF.
2. The authors claim that the proposed method can be integrated into different types of NeRF frameworks. However, only MLP-based NeRFs are considered in the experiments. It would be better to conduct experiments on other types of NeRF frameworks, such as those using voxel-based or hash-based representations. The lack of experiments on these alternative representations limits the generalizability of the claims, as different NeRF architectures may interact differently with the proposed mapping and parameterization.

### Suggestions

To address the limitations regarding the scope of the experiments, it is crucial to include evaluations on bounded scene datasets. Specifically, the authors should consider using datasets like the original NeRF synthetic datasets (e.g., the small teapots, the large teapots, or the ship) or real-world bounded scenes. This would provide a more comprehensive understanding of the proposed method's performance across different scene types. The evaluation should not only focus on PSNR but also include other metrics such as SSIM and LPIPS to provide a more complete picture of the reconstruction quality. Furthermore, it would be beneficial to analyze how the choice of the 'p' value in the p-norm affects the performance on bounded scenes, as the optimal value might differ from unbounded scenarios. This analysis would provide insights into the robustness and adaptability of the proposed mapping function.

To strengthen the claim of general applicability across different NeRF frameworks, the authors should extend their experiments to include voxel-based methods like DVGO and TensoRF, as well as hash-based methods like iNGP. These methods have different underlying representations and sampling strategies, and it is important to demonstrate that the proposed mapping and parameterization can effectively improve their performance. For voxel-based methods, the authors should investigate how the proposed mapping interacts with the voxel grid structure and how it affects the sampling density. For hash-based methods, it would be interesting to see how the proposed mapping affects the hash table lookup and the overall rendering quality. The experiments should include a detailed analysis of the performance gains and any potential limitations or challenges that arise when integrating the proposed method into these different frameworks. This would provide a more robust validation of the method's generalizability.

Finally, the authors should provide a more detailed analysis of the computational overhead introduced by the proposed mapping and parameterization. While the paper mentions that the method can be integrated into different NeRF frameworks, it does not discuss the potential impact on training and rendering time. It would be beneficial to include a comparison of the computational cost of the proposed method with the baseline methods. This analysis should include the time required for computing the p-norm mapping, the new ray parameterization, and the overall impact on the training and rendering pipeline. This would provide a more complete understanding of the practical implications of using the proposed method and help the readers assess its feasibility for different applications.

### Questions

1. How does the proposed method perform on bounded scene datasets?
2. How does the proposed method perform when integrated into voxel-based or hash-based NeRF frameworks?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
