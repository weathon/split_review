### Summary

This paper proposes a novel approach for object completion, which is to reconstruct a complete object from its partially observed counterpart. The method, named MaskComp, leverages a mask denoiser to refine the mask and an image generator to produce the complete object. The iterative process of mask denoising and image generation is designed to progressively refine the mask and the generated object, leading to a more accurate completion. The authors demonstrate the effectiveness of MaskComp through experiments on two datasets, AHP and DYCE, and compare it with other state-of-the-art methods, including ControlNet and Stable Diffusion.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is novel and interesting.
3. The experiments are comprehensive and demonstrate the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the computational cost of the proposed method. Specifically, the iterative nature of the mask denoising and image generation process raises concerns about the practical applicability of the method. The authors should provide a more thorough analysis of the computational resources required, including memory usage and inference time, especially when compared to existing methods. It is unclear how the iterative refinement impacts the overall efficiency of the approach.
2. The paper does not provide a detailed discussion of the limitations of the proposed method. For example, it is unclear how the method performs under extreme occlusions or with objects that have complex shapes. The authors should discuss the potential failure modes of the method and provide guidance on when it is most appropriate to use MaskComp. The lack of discussion on failure cases makes it difficult to assess the robustness of the approach.

### Suggestions

The authors should provide a more detailed analysis of the computational cost of their method, including a breakdown of the time spent in each stage of the iterative process. This analysis should include not only the total inference time but also the memory footprint of the model, which is crucial for practical applications. It would be beneficial to compare the computational cost of MaskComp with other state-of-the-art methods, such as ControlNet and Stable Diffusion, under similar experimental conditions. This would provide a clearer understanding of the trade-offs between accuracy and efficiency. Furthermore, the authors should investigate the impact of the number of iterations on both the performance and computational cost. It is important to determine the optimal number of iterations to achieve a good balance between accuracy and efficiency. This analysis should include a discussion of how the iterative refinement process affects the convergence of the method and whether there is a point of diminishing returns.

In addition to the computational cost, the authors should provide a more thorough discussion of the limitations of their method. This should include an analysis of how the method performs under different types of occlusions, such as partial, random, and extreme occlusions. The authors should also discuss the impact of object shape complexity on the performance of MaskComp. For example, how does the method perform on objects with highly articulated structures or complex geometries? It would be beneficial to include experiments that specifically test the limits of the method and identify the scenarios where it is likely to fail. This analysis should also include a discussion of the potential failure modes of the method and provide guidance on when it is most appropriate to use MaskComp. The authors should also consider the impact of noise in the input data on the performance of the method. How does the method handle noisy or incomplete input data? This analysis should include a discussion of the robustness of the method to different types of noise and the potential for improvement in this area.

Finally, the authors should consider exploring alternative approaches to the iterative refinement process. For example, they could investigate the use of more efficient optimization techniques or explore alternative architectures for the mask denoiser and image generator. The authors should also consider the potential for using pre-trained models to improve the efficiency and performance of the method. This could include the use of pre-trained diffusion models or other pre-trained architectures. The authors should also explore the potential for using techniques such as knowledge distillation to transfer the knowledge from a larger model to a smaller model. This could lead to a more efficient and effective approach for object completion.

### Questions

1. How does the proposed method handle extreme occlusions or objects with complex shapes?
2. What is the computational cost of the proposed method compared to other state-of-the-art methods?
3. How does the iterative refinement process affect the convergence of the method?

### Rating

6

### Confidence

4

**********
