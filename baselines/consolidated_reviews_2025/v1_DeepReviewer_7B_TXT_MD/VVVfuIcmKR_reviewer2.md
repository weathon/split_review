### Summary

This paper investigates the modality gap in CLIP models, which refers to the geometric separation between feature embeddings of different modalities in the shared representation space. The authors demonstrate that this gap negatively impacts intra-modal tasks like image-to-image and text-to-text retrieval. To address this, they propose using modality inversion techniques to transform native modality inputs into the complementary modality, which improves performance on these tasks. They show that adding intra-modal loss or reducing the modality gap further mitigates intra-modal misalignment.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper introduces a novel approach to improve intra-modal performance by using modality inversion, which is a creative solution to a known problem in multimodal models.

2. The authors conduct extensive experiments across multiple datasets and models, providing strong empirical evidence for their claims.

3. The paper is well-structured and clearly explains complex concepts, making it accessible to a broad audience.

### Weaknesses

#### Some Related Works


#### comment

1. The paper's novelty is limited, as it primarily applies existing modality inversion techniques to intra-modal tasks without introducing significant new insights or methodologies. The core idea of using optimization-based transformations, while effective, lacks a novel theoretical contribution. The application of these techniques to intra-modal tasks, while presented as a contribution, is more of an extension of existing work rather than a fundamentally new approach. The paper does not delve into the theoretical underpinnings of why these transformations are effective in the context of intra-modal tasks, which weakens the overall impact.

2. The paper lacks a detailed analysis of the computational overhead introduced by the modality inversion techniques. The iterative optimization process required for these transformations can be computationally expensive, especially for large-scale datasets. The paper does not provide a clear comparison of the computational cost of their approach versus standard intra-modal methods, making it difficult to assess the practical applicability of their method. Furthermore, the paper does not explore potential optimizations or approximations to reduce the computational burden of the proposed approach.

3. The paper does not adequately address the potential limitations of the modality inversion techniques, such as their sensitivity to hyperparameter settings or the possibility of generating artifacts in the transformed features. The paper lacks a thorough investigation of how different hyperparameters affect the quality of the inverted features and the final performance on downstream tasks. Additionally, the paper does not discuss the potential for artifacts or distortions in the transformed features, which could negatively impact the performance of the model.

### Suggestions

The authors should provide a more in-depth theoretical analysis of why modality inversion techniques are effective for intra-modal tasks. This could involve exploring the mathematical properties of the transformations and how they relate to the underlying feature spaces. For example, they could investigate the geometry of the feature space and how the modality inversion process affects the distribution of features. This would provide a more solid foundation for their approach and differentiate it from a purely empirical study. Furthermore, the authors should explore the sensitivity of their approach to different hyperparameter settings. This could involve conducting a systematic analysis of how different learning rates, optimization algorithms, and regularization parameters affect the quality of the inverted features and the final performance on downstream tasks. This would provide valuable insights into the robustness of their method and help practitioners to effectively apply it in different scenarios. 

To address the computational overhead, the authors should investigate potential optimizations or approximations to reduce the computational burden of their approach. This could involve exploring techniques such as early stopping, adaptive learning rates, or parallelization. The authors should also provide a detailed comparison of the computational cost of their approach versus standard intra-modal methods, including a breakdown of the time and memory requirements for each step of the process. This would allow practitioners to make informed decisions about whether to use their approach in their specific applications. Additionally, the authors should explore the potential for generating artifacts or distortions in the transformed features. This could involve conducting a qualitative analysis of the inverted features and comparing them to the original features. The authors should also investigate techniques for mitigating any negative effects of these artifacts on the performance of the model.

Finally, the authors should include a more comprehensive discussion of the limitations of their approach. This should include a discussion of the potential for the method to fail in certain scenarios, as well as the potential for the method to introduce new biases or artifacts. The authors should also discuss the potential for future research to address these limitations. This would provide a more balanced and nuanced perspective on their work and help to guide future research in this area. The authors should also consider exploring alternative approaches to intra-modal learning that do not rely on modality inversion, and compare their performance to the proposed method.

### Questions

1. How does the computational cost of the proposed modality inversion techniques compare to standard intra-modal learning approaches?

2. Are there specific scenarios or types of data where the proposed method might not be as effective?

3. Can the authors provide more insights into the theoretical underpinnings of why modality inversion improves intra-modal performance?

### Rating

5

### Confidence

4

**********
