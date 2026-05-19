### Summary

This paper studies the problem of learning cross-modal tasks with uni-modal data. The authors provide a theoretical explanation of the representation space geometry resulting from multi-modal contrastive learning, and introduce a three-step method, C3 (Connect, Collapse, Corrupt), to bridge the modality gap, enhancing the interchangeability of embeddings from different modalities. The proposed method achieves good results on zero-shot image/audio/video captioning and text-to-image generation.

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

The theoretical analysis, while providing a valuable framework, relies on strong assumptions that need further investigation. Specifically, the assumption of equal presence of images and texts is a significant simplification. In real-world datasets, the distribution of modalities is often imbalanced, which could lead to a skewed representation space. The authors should explore the impact of varying modality ratios on the derived geometry. For example, how does the modality gap change when one modality is significantly more prevalent than the other? Furthermore, the assumption of random initialization, while common, may not fully capture the complexities of pre-trained models with non-uniform weight distributions. It would be beneficial to analyze how different initialization schemes affect the modality gap and the overall representation space. This could involve experiments with different initialization strategies and a more detailed theoretical analysis of their impact on the derived equations.

The proposed three-step method, while effective, is relatively simple and might not be sufficient for more complex cross-modal tasks. The method's reliance on collapsing the modality gap into a single point might be too restrictive. In reality, the relationship between modalities is likely more nuanced, and a single-point collapse might lead to a loss of valuable information. The authors should consider exploring more sophisticated methods for aligning the representation spaces, such as learning a non-linear transformation or a more complex mapping function. Additionally, the method's performance in low-data regimes needs further investigation. While the paper shows some results in this area, a more thorough analysis of the method's robustness to limited data would be beneficial. This could involve experiments with varying amounts of training data and a comparison with other methods specifically designed for low-data scenarios.

Finally, while the experimental results are promising, they do not reach state-of-the-art performance. The authors should provide a more detailed comparison with existing methods, including a discussion of the limitations of their approach. It is important to understand why the proposed method does not achieve state-of-the-art results and what steps could be taken to improve its performance. This could involve exploring different architectures, training strategies, or data augmentation techniques. Furthermore, the evaluation should be expanded to include a wider range of datasets and tasks to better assess the method's generalizability. The current evaluation is limited to a few specific tasks, and it is unclear how well the method would perform on other cross-modal tasks.

### Questions

Please see the weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
