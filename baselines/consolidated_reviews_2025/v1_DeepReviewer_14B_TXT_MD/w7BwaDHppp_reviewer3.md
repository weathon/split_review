### Summary

The paper proposes a new mapping function for unbounded neural radiance fields. The authors first analyze the existing mapping functions and explain their failures using stereographic projection. Then, they propose a new mapping function based on p-norm distance and a new ray parameterization. The proposed method achieves state-of-the-art novel view synthesis results on several challenging datasets.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The proposed method is novel and well-motivated. The analysis of existing mapping functions using stereographic projection is insightful. The proposed p-norm mapping function and ray parameterization are reasonable and effective.
2. The proposed method can be integrated into different types of NeRF frameworks and achieves state-of-the-art view synthesis results on several challenging datasets.
3. The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

1. The authors mention that the proposed p-norm mapping function is flexible and general to learn both bounded and unbounded regions in neural radiance fields. However, the experiments only demonstrate the effectiveness of the proposed method on unbounded regions. It would be better to conduct experiments on bounded regions as well.
2. The authors claim that the proposed method can be integrated into different types of NeRF frameworks. However, only MLP-based NeRFs are considered in the experiments. It would be better to conduct experiments on other types of NeRF frameworks.

### Suggestions

The paper would benefit from a more thorough evaluation of the proposed p-norm mapping function across diverse scene types. While the current experiments focus on unbounded regions, it is crucial to assess its performance in bounded scenarios to validate the claim of general applicability. Specifically, experiments should be conducted on datasets representing bounded scenes, such as those used in the original NeRF paper or other similar datasets. This would involve adapting the training and evaluation pipeline to accommodate the different scene characteristics and would provide a more comprehensive understanding of the method's strengths and limitations. Furthermore, it would be beneficial to analyze how the choice of the 'p' value in the p-norm affects the performance in bounded regions, as the optimal value might differ from unbounded scenarios. This analysis would provide insights into the robustness and adaptability of the proposed mapping function.

To strengthen the claim of general applicability across different NeRF frameworks, the authors should extend their experiments to include voxel-based methods like DVGO and TensoRF, as well as hash-based methods like iNGP. These methods have different underlying representations and sampling strategies, and it is important to demonstrate that the proposed mapping and parameterization can effectively improve their performance. For voxel-based methods, the authors should investigate how the proposed mapping interacts with the voxel grid structure and how it affects the sampling density. For hash-based methods, it would be interesting to see how the proposed mapping affects the hash table lookup and the overall rendering quality. The experiments should include a detailed analysis of the performance gains and any potential limitations or challenges that arise when integrating the proposed method into these different frameworks. This would provide a more robust validation of the method's generalizability.

Finally, the authors should provide a more detailed analysis of the computational overhead introduced by the proposed mapping and parameterization. While the paper mentions that the method can be integrated into different NeRF frameworks, it does not discuss the potential impact on training and rendering time. It would be beneficial to include a comparison of the computational cost of the proposed method with the baseline methods. This analysis should include the time required for computing the p-norm mapping, the new ray parameterization, and the overall impact on the training and rendering pipeline. This would provide a more complete understanding of the practical implications of using the proposed method and help the readers assess its feasibility for different applications.

### Questions

Please refer to the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
