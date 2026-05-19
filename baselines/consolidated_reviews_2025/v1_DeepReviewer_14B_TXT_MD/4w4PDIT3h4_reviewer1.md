### Summary

This paper proposes a novel method for visual reinforcement learning can generalize to unseen environments. Specifically, it introduces an encoder-decoder model that segments primary pixels to mitigate the impact of inappropriate data augmentation on critical information. The paper also proposes Diverse Data Augmentation (DDA) and Differential Diverse Data Augmentation (D3A) to further improve the generalization capability. The authors evaluate the methods on the DeepMind Control Suite and demonstrate significant improvements in generalization performance.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

- The paper proposes a novel method for visual reinforcement learning to generalize to unseen environments with data augmentation.
- The introduction is clear, and the method is described in detail.
- The experiments show the advantage of the proposed method compared to baselines.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed method relies on a pre-trained encoder-decoder model, which may not be available or suitable for all tasks and environments. The generalization ability of the encoder-decoder model is unclear. Specifically, the paper does not discuss how the encoder-decoder is trained, what data it is trained on, and how this training data might affect the overall generalization performance of the proposed method. The lack of ablation studies on the encoder-decoder's training data and architecture makes it difficult to assess its impact on the final results.
- The design of the Q-value distance for assessing semantic-invariant state transformation is not convincing. The paper does not provide a clear justification for why the distance between Q-values of augmented and original observations is a good indicator of semantic invariance. It is unclear how this distance relates to the actual semantic content of the observations, and whether it is robust to different types of augmentations. Furthermore, the paper does not discuss the potential sensitivity of this metric to the choice of Q-function approximator.
- It would be better to compare the proposed method with more recent methods, such as those presented in ISRL 2023 and 2024. The field of visual reinforcement learning is rapidly evolving, and the paper should demonstrate that the proposed method is competitive with the current state-of-the-art. The lack of comparison with recent methods makes it difficult to assess the true contribution of the proposed method.

### Suggestions

The paper should provide a more detailed explanation of the pre-trained encoder-decoder model, including its architecture, training data, and training procedure. It is crucial to analyze how the choice of training data affects the segmentation performance and the overall generalization capability of the proposed method. The authors should also conduct ablation studies to evaluate the sensitivity of the method to different encoder-decoder architectures and training strategies. Furthermore, it would be beneficial to explore alternative methods for obtaining the segmentation mask, such as using attention mechanisms or other forms of feature pooling, to reduce the reliance on a pre-trained model. This would also help to clarify the generalization ability of the encoder-decoder model and its impact on the overall performance.

The paper needs to provide a more rigorous justification for using Q-value distance as a measure of semantic invariance. The authors should explore alternative metrics that directly measure the semantic similarity between augmented and original observations. For example, they could use a pre-trained vision model to extract features from the observations and then compute the distance between these features. This would provide a more direct measure of semantic similarity. Additionally, the paper should investigate the sensitivity of the Q-value distance metric to different types of augmentations and different Q-function approximators. It is important to understand the limitations of this metric and how it might affect the performance of the proposed method. The authors should also consider the potential for instability in Q-value estimates, especially during early training, and how this might impact the reliability of the proposed metric.

The paper should include a more comprehensive comparison with recent state-of-the-art methods in visual reinforcement learning. This comparison should include methods that have been published in recent conferences and journals. The authors should also discuss the limitations of their method and how it compares to other approaches in terms of computational cost, sample efficiency, and robustness to different types of environments. The paper should also provide a more detailed analysis of the experimental results, including error bars and statistical significance tests. This would help to ensure that the reported improvements are statistically significant and not due to random chance. The authors should also consider evaluating their method on a wider range of tasks and environments to demonstrate its generalization capability.

### Questions

- How does the proposed method ensure the generalization of the encoder-decoder model?
- Could you provide a more detailed explanation of the design of the Q-value distance for assessing semantic-invariant state transformation?
- Is the Q-value distance metric stable during training?
- How does the proposed method compare to more recent methods in visual reinforcement learning?

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
