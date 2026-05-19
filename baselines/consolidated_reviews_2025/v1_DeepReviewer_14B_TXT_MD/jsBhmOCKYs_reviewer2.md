### Summary

This paper presents a novel approach to domain adaptation in image restoration using diffusion models. The authors propose a method that performs domain adaptation in the noise space, leveraging the unique properties of diffusion models to align synthetic and real-world data distributions. The method introduces a diffusion loss that guides the restoration model to progressively align both restored synthetic and real-world outputs with a target clean distribution. Additionally, the paper proposes strategies such as channel-shuffling layers and residual-swapping contrastive learning to prevent shortcut learning during joint training. The effectiveness of the proposed method is demonstrated through experiments on three classical image restoration tasks: denoising, deblurring, and deraining.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel approach to domain adaptation in image restoration by utilizing the noise space of diffusion models. This is a creative and innovative solution that addresses the limitations of existing methods.
2. The proposed method is designed to be general and flexible, applicable to various image restoration tasks without requiring prior knowledge of noise distribution or degradation models. This makes the method highly versatile and practical for real-world applications.
3. The paper provides extensive experimental results on three classical image restoration tasks, demonstrating the effectiveness of the proposed method. The results show significant improvements over existing methods, highlighting the practical value of the approach.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the computational complexity and efficiency of the proposed method. Specifically, the paper does not provide a breakdown of the computational cost associated with the diffusion model, nor does it compare the training and inference times with existing methods. This makes it difficult to assess the practical applicability of the method, especially for resource-constrained environments.
2. The paper does not provide a thorough analysis of the limitations of the proposed method. For example, the paper does not discuss how the method performs under extreme noise conditions or with highly complex degradations. Furthermore, the paper lacks a discussion on the sensitivity of the method to hyperparameter settings, which is crucial for practical implementation.
3. The paper does not explore the potential of the proposed method for other low-level vision tasks beyond image restoration. For instance, it is unclear whether the noise-space domain adaptation approach can be effectively applied to tasks such as image enhancement or super-resolution. This limits the scope of the paper and leaves potential avenues for future research unexplored.

### Suggestions

The paper should include a detailed analysis of the computational complexity of the proposed method. This should include a breakdown of the computational cost associated with the diffusion model, as well as a comparison of the training and inference times with existing methods. Specifically, the authors should provide a table or graph showing the number of floating-point operations (FLOPs) and the memory usage of their method compared to other domain adaptation techniques. Furthermore, the authors should analyze the scalability of their method with respect to image size and the number of diffusion steps. This analysis should be performed on a standard hardware setup to ensure reproducibility and allow for a fair comparison with other methods. This would provide a more comprehensive understanding of the practical applicability of the proposed method, especially for resource-constrained environments.

To address the lack of analysis regarding the limitations of the proposed method, the authors should conduct experiments under more challenging conditions. This should include evaluating the method's performance under extreme noise levels, such as high-variance Gaussian noise or salt-and-pepper noise, and with complex degradations, such as those encountered in real-world scenarios. The authors should also perform a sensitivity analysis of the method to hyperparameter settings, such as the learning rate, the number of diffusion steps, and the weighting of the diffusion loss. This analysis should include a discussion of the optimal hyperparameter settings for different tasks and datasets. Furthermore, the authors should investigate the failure cases of their method and discuss the potential reasons for these failures. This would provide a more complete understanding of the method's limitations and guide future research.

Finally, the authors should explore the potential of the proposed method for other low-level vision tasks beyond image restoration. This could include tasks such as image enhancement, super-resolution, and inpainting. The authors should discuss the potential challenges and opportunities associated with applying their method to these tasks. For example, they could investigate whether the noise-space domain adaptation approach can be effectively applied to tasks that involve different types of degradations or require different types of prior knowledge. This would broaden the scope of the paper and highlight the versatility of the proposed method. Furthermore, the authors should provide a discussion of the potential limitations of their method when applied to other low-level vision tasks and suggest potential solutions to overcome these limitations.

### Questions

1. How does the proposed method perform in terms of computational complexity and efficiency compared to existing methods?
2. What are the limitations of the proposed method, and under what conditions might it fail to produce satisfactory results?
3. Can the proposed method be extended to other low-level vision tasks beyond image restoration, such as image enhancement or super-resolution?

### Rating

6

### Confidence

3

**********
