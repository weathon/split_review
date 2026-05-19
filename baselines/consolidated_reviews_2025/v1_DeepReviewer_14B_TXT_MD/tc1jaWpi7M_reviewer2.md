### Summary

This paper proposes an object completion method, which iteratively refines the object mask and improves the completion quality. The proposed method is based on ControlNet, which is a conditional diffusion model. The authors also provide a mathematical explanation of the method. The authors demonstrate the effectiveness of the proposed method on two datasets.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The proposed method is novel and interesting. The authors also provide a mathematical explanation of the method.
2. The proposed method is compared with several state-of-the-art methods on two datasets, and the proposed method achieves the best performance.
3. The authors provide detailed ablation studies to analyze the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method seems to be time-consuming. The authors should provide the running time of the proposed method and the compared methods.
2. The proposed method is based on ControlNet, which is a conditional diffusion model. Is the proposed method applicable to other conditional diffusion models? For example, the proposed method can be implemented with ControlNet v2 and other conditional diffusion models.
3. The authors should provide the failure cases of the proposed method.
4. The authors should provide the limitation of the proposed method.

### Suggestions

The paper introduces an interesting iterative object completion method based on ControlNet, but several aspects could be improved to strengthen its impact. First, a more thorough analysis of the computational cost is needed. While the authors mention the iterative nature of their approach, they should provide a detailed breakdown of the time spent in each stage (mask refinement and image generation) and compare it with the runtime of other methods, not just a single number. This should include a discussion of the factors that influence the runtime, such as image resolution and the number of iterations. Furthermore, it would be beneficial to explore potential optimizations to reduce the computational burden, such as using more efficient segmentation models or reducing the number of sampling steps in the diffusion model. A clear understanding of the computational trade-offs is crucial for the practical application of the proposed method.

Second, the paper should delve deeper into the generalizability of the proposed method to other conditional diffusion models. While the authors state that their method is applicable to other models, they should provide empirical evidence to support this claim. Specifically, they should demonstrate the performance of their method when integrated with other conditional diffusion models, such as ControlNet v2 or other similar architectures. This would involve not only showing that the method works but also analyzing the performance differences and discussing the potential challenges and benefits of using different conditional diffusion models. This analysis should include a discussion of how the specific characteristics of each conditional diffusion model affect the performance of the proposed iterative refinement process. For example, how does the performance change when using a different conditioning mechanism or a different architecture for the diffusion model?

Finally, the paper needs a more comprehensive discussion of the limitations and failure cases of the proposed method. The authors should provide a detailed analysis of the scenarios where the method fails to produce satisfactory results. This should include a discussion of the types of objects or scenes that are particularly challenging for the method, as well as the factors that contribute to these failures. For example, does the method struggle with objects that have complex shapes or textures? Does it fail when the initial mask is significantly inaccurate? Furthermore, the authors should discuss the limitations of the method in terms of its applicability to different types of images or datasets. A thorough analysis of the limitations and failure cases is essential for understanding the scope and applicability of the proposed method and for guiding future research in this area.

### Questions

Please see the Weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
