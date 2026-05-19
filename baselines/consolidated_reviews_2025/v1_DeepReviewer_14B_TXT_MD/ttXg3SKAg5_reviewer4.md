### Summary

This paper provides a theoretical explanation of the geometry of the multi-modal contrastive representation space and introduces a three-step method, C3 (Connect, Collapse, Corrupt), to bridge the modality gap, enhancing the interchangeability of embeddings from different modalities. The proposed method significantly improves cross-modal learning from uni-modal data, achieving state-of-the-art results on zero-shot image/audio/video captioning and text-to-image generation.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper provides a theoretical explanation of the representation space geometry resulting from multi-modal contrastive learning.
2. The paper proposes a simple three-step solution to enhance the interchangeability of embeddings from different modalities, improving cross-modal learning with uni-modal data.
3. The paper shows the effectiveness of the method on image/audio/video captioning and text-to-image generation, achieving state-of-the-art results.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational complexity of the proposed method. It is unclear how the computational cost scales with the size of the input data and the number of modalities. A more rigorous analysis, including both time and space complexity, would be beneficial. For example, what is the impact of the number of negative samples used in the contrastive loss on the overall computational cost?
2. The paper does not provide a detailed analysis of the sensitivity of the proposed method to the choice of hyperparameters. While the authors mention using default hyperparameters, it is crucial to understand how the performance varies with different settings. For instance, how does the temperature parameter in the contrastive loss affect the final performance? A sensitivity analysis with a range of hyperparameter values would strengthen the paper.
3. The paper does not provide a detailed analysis of the limitations of the proposed method. It would be beneficial to discuss the scenarios where the method might fail or underperform. For example, are there specific types of data or tasks where the proposed method is not effective? A discussion of the limitations would provide a more balanced view of the method's applicability.

### Suggestions

To address the lack of computational complexity analysis, the authors should provide a detailed breakdown of the time and space complexity of each step in their proposed C3 method. This should include an analysis of how the computational cost scales with the size of the input data, the number of modalities, and the number of negative samples used in the contrastive loss. For example, the authors could analyze the number of floating-point operations required for each step and provide a theoretical estimate of the runtime. Furthermore, they should provide empirical results on the actual runtime of the method on different datasets and hardware configurations. This would give readers a better understanding of the practical applicability of the method.

Regarding the sensitivity to hyperparameters, the authors should conduct a thorough sensitivity analysis by varying the key hyperparameters and reporting the corresponding performance changes. This should include parameters such as the temperature parameter in the contrastive loss, the learning rate, and the batch size. The authors should present the results in a clear and concise manner, such as using plots or tables, to show how the performance varies with different hyperparameter values. This analysis should also include a discussion of the optimal hyperparameter settings and the trade-offs between different choices. This would help readers understand the robustness of the method and how to tune it for different tasks.

Finally, to address the limitations, the authors should provide a more detailed discussion of the scenarios where the proposed method might fail or underperform. This should include a discussion of the types of data or tasks where the method is not effective. For example, the authors could discuss whether the method is sensitive to noisy data or whether it performs well on tasks that require fine-grained understanding of the input. They should also discuss the potential limitations of the method in terms of its ability to generalize to unseen data or tasks. This would provide a more balanced view of the method's applicability and help readers understand its limitations.

### Questions

1. How does the computational complexity of the proposed method compare to existing methods for cross-modal learning?
2. How sensitive is the proposed method to the choice of hyperparameters?
3. What are the limitations of the proposed method, and in what scenarios might it fail or underperform?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
