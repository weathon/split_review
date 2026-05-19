### Summary

This paper studies the problem of learning cross-modal tasks with uni-modal data. The main contribution is a theoretical explanation of the representation space geometry resulting from multi-modal contrastive learning. The paper also provides a simple three-step solution to enhance the interchangeability of embeddings from different modalities. The approach is evaluated on image / audio / video captioning and text-to-image generation, and achieves good results.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The theoretical analysis of the multi-modal representation space is valuable and novel.
2. The paper is well written and easy to follow.
3. The experimental results are good.

### Weaknesses

#### Some Related Works


#### comment

1. The theoretical analysis makes assumptions about random initialization and equal presence of images and texts, which may not hold in real-world scenarios.
2. The three-step method proposed by the paper is simple and may limit its applicability in more complex scenarios.
3. The experimental results are good but not state-of-the-art.

### Suggestions

The theoretical analysis, while insightful, relies on simplifying assumptions that may not fully capture the complexities of real-world multi-modal data. Specifically, the assumption of random initialization and equal presence of images and texts is a strong one. In practice, pre-trained models often have non-random initializations, and datasets are frequently imbalanced, with one modality being more prevalent than the other. This imbalance could lead to a skewed representation space, where the modality with more data dominates the learned embeddings. Future work should explore how these factors affect the derived geometric properties and whether the proposed method remains effective under such conditions. It would be beneficial to investigate the sensitivity of the theoretical results to deviations from these assumptions, perhaps through simulations or by analyzing real-world datasets with varying degrees of imbalance and different initialization schemes.

The proposed three-step method, while simple and effective, might not be universally applicable to all cross-modal tasks. The method's reliance on collapsing the modality gap into a single point may be too restrictive for tasks where a more nuanced alignment is required. For example, in tasks involving fine-grained distinctions between modalities, such as detailed image captioning or audio event localization, a single-point alignment might lead to a loss of crucial information. Furthermore, the method's simplicity might limit its ability to handle complex scenarios where the relationships between modalities are highly non-linear or involve intricate dependencies. It would be valuable to explore more flexible alignment strategies that can adapt to different task requirements and data characteristics. This could involve incorporating non-linear transformations or learning task-specific alignment functions.

While the experimental results demonstrate the effectiveness of the proposed method, they do not achieve state-of-the-art performance. This suggests that there is still room for improvement, and the proposed method may not be the optimal solution for all cross-modal tasks. It would be beneficial to compare the proposed method with other state-of-the-art techniques and to analyze the reasons for the performance gap. This analysis could reveal potential limitations of the proposed method and guide future research directions. Furthermore, it would be valuable to explore the method's performance on a wider range of datasets and tasks to better understand its generalizability and robustness. This could involve evaluating the method on more challenging datasets or on tasks that require more complex cross-modal reasoning.

### Questions

Please see the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
