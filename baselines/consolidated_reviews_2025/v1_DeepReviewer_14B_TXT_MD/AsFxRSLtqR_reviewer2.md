### Summary

This paper introduces a benchmark, LR0.FM, to evaluate the impact of low resolution on the zero-shot classification performance of visual-language foundation models. The authors also propose a new metric, Weighted Aggregated Robustness, to better evaluate model performance across resolutions and datasets. Finally, the authors propose a simple strategy, LRTK0, to enhance the robustness of models without compromising their pre-trained weights.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The motivation is clear and the problem is significant.
3. The experiments are comprehensive.

### Weaknesses

#### Some Related Works


#### comment

1. The novelty of the proposed method is limited.
2. The authors claim that fine-tuned and higher resolution models are less robust against LR. However, it can be improved by simply augmenting the training data with LR images. The authors didn't discuss this.

### Suggestions

The paper introduces a benchmark for evaluating the robustness of visual-language foundation models to low-resolution inputs, which is a valuable contribution. However, the proposed method, LRTK0, while effective, lacks significant novelty. The core idea of adding trainable tokens to adapt to low-resolution inputs is not entirely new, and the paper could benefit from a more thorough discussion of how this approach differs from existing methods for handling domain shifts or low-resolution data. For example, the authors could explore and compare their method with techniques that explicitly model the degradation process or use adversarial training to improve robustness. A more detailed analysis of the limitations of LRTK0, especially in scenarios with extreme low-resolution or specific types of image degradation, would also strengthen the paper.

Furthermore, the claim that fine-tuned and higher-resolution models are less robust against LR, while interesting, needs more nuanced discussion. The authors should acknowledge that data augmentation with low-resolution images during fine-tuning is a common practice and can significantly improve robustness. The paper should include experiments that directly compare the proposed method with fine-tuned models that have been trained with LR augmentations. This would provide a more comprehensive understanding of the strengths and weaknesses of LRTK0. Additionally, the authors should investigate the impact of different types of low-resolution degradations (e.g., bicubic downsampling, Gaussian blur) on the performance of both the proposed method and fine-tuned models. This would provide a more complete picture of the robustness of different approaches.

Finally, the paper could benefit from a more detailed analysis of the computational cost of the proposed method. While the authors mention that LRTK0 does not compromise pre-trained weights, they do not discuss the additional computational overhead of training the LR tokens. A comparison of the training and inference time of LRTK0 with other methods would be valuable for practical applications. The authors should also explore the scalability of their method to larger models and datasets. This would help to assess the practical applicability of the proposed method in real-world scenarios.

### Questions

Please see the weaknesses.

### Rating

6

### Confidence

3

**********
