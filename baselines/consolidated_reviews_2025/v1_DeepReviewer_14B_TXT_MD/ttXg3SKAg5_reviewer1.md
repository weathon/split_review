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

1. The theoretical analysis makes assumptions about random initialization and equal presence of images and texts, which may not hold in real-world scenarios. Specifically, the assumption of equal presence of images and texts is a strong simplification that does not reflect the imbalanced nature of many real-world datasets, where one modality may be significantly more prevalent than the other. This imbalance could lead to a biased representation space that the theory does not account for. Furthermore, while random initialization is a common practice, the theory does not explore the impact of different initialization strategies on the resulting geometry.
2. The three-step method proposed by the paper is simple and may limit its applicability in more complex scenarios. The simplicity of the method, while advantageous for ease of implementation, might not be sufficient to address the complexities of real-world cross-modal learning tasks. For example, the method may not be robust to noisy or out-of-distribution data, and it is unclear how well it would generalize to more complex modalities or tasks beyond those tested in the paper. The method also lacks a clear mechanism for adapting to different levels of modality discrepancy.
3. The experimental results are good but not state-of-the-art. While the results demonstrate the effectiveness of the proposed approach, they do not surpass the performance of existing methods. This raises questions about the practical significance of the proposed method, especially given its simplicity. It is also unclear whether the method can achieve state-of-the-art results with more extensive hyperparameter tuning or architectural modifications.

### Suggestions

To address the limitations of the theoretical analysis, future work should explore the impact of imbalanced data distributions on the multi-modal representation space. This could involve developing a more refined theoretical framework that accounts for the varying prevalence of different modalities. For example, the theory could be extended to incorporate a weighting scheme that reflects the relative abundance of each modality, or it could explore the use of techniques like re-sampling or re-weighting to mitigate the effects of data imbalance. Furthermore, the theory should investigate the impact of different initialization strategies on the resulting geometry, as this could provide insights into how to optimize the learning process. It would also be beneficial to validate the theoretical findings with more extensive empirical analysis, including experiments on datasets with varying degrees of modality imbalance.

To enhance the applicability of the proposed method, future research should focus on developing more robust and adaptive techniques for cross-modal learning. This could involve incorporating more sophisticated alignment mechanisms that can handle complex modality discrepancies. For example, the method could be extended to include a non-linear transformation layer that maps the embeddings from different modalities into a common space. Additionally, the method should be evaluated on a wider range of tasks and modalities, including those that are more challenging and realistic. It would also be beneficial to explore the use of techniques like adversarial training or domain adaptation to improve the method's robustness to noisy or out-of-distribution data. The method should also be made more adaptive to different levels of modality discrepancy, perhaps by incorporating a mechanism that automatically adjusts the alignment process based on the characteristics of the input data.

Finally, to achieve state-of-the-art results, the proposed method should be further optimized and refined. This could involve exploring different architectural modifications or hyperparameter tuning strategies. For example, the method could be combined with other state-of-the-art techniques for cross-modal learning, such as attention mechanisms or graph neural networks. It would also be beneficial to conduct a more thorough analysis of the method's performance on different datasets and tasks, in order to identify its strengths and weaknesses. The method should also be compared with a wider range of baselines, including those that are specifically designed for low-data regimes. Furthermore, the paper should provide a more detailed analysis of the computational cost of the proposed method, and explore ways to reduce its complexity without sacrificing performance.

### Questions

1. How does the performance of the proposed method compare to other state-of-the-art methods in low-data regimes?
2. What are the limitations of the proposed method in terms of scalability and computational complexity?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
