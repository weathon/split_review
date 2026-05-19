### Summary

This paper proposes two data augmentation methods for visual reinforcement learning: Diverse Data Augmentation (DDA) and Differential Diverse Data Augmentation (D3A). The key idea is to use a pre-trained encoder-decoder model to segment the "primary" pixels in the image (i.e. the pixels that are relevant to the task) and apply data augmentation only to the other pixels. The authors evaluate their methods on the DMControl Generalization Benchmark and show that they outperform existing methods in terms of generalization performance.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The proposed methods are simple and easy to implement.
- The paper is well-written and easy to understand.
- The experimental results are promising, showing that the proposed methods outperform existing methods on the DMControl Generalization Benchmark.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed methods are simple and easy to implement.
- The paper is well-written and easy to understand.
- The experimental results are promising, showing that the proposed methods outperform existing methods on the DMControl Generalization Benchmark.

- The proposed methods require a pre-trained encoder-decoder model, which may not be available for all tasks and environments. Furthermore, the generalization ability of the encoder-decoder model is unclear. The paper does not discuss the potential for the encoder-decoder to overfit to the training data used for its pre-training, which could limit the overall generalization performance of the proposed approach. The reliance on a pre-trained model introduces a dependency that could hinder its applicability in novel scenarios where such a model is not readily available or performs poorly.
- The design of the Q-value distance for assessing semantic-invariant state transformation is not convincing. The paper does not provide a clear justification for why the distance between Q-values of augmented and original observations is a good indicator of semantic invariance. It is unclear how this distance relates to the actual semantic content of the observations, and whether it is robust to different types of augmentations. The Q-value distance could be influenced by factors other than semantic changes, such as noise or subtle variations in the input that do not affect the underlying semantics.
- The proposed methods are only evaluated on the DMControl Generalization Benchmark, which may not be representative of all visual reinforcement learning tasks. The benchmark, while useful, may not capture the full spectrum of challenges present in real-world visual RL scenarios. The lack of evaluation on more diverse and complex environments limits the generalizability of the findings.

MISC:
- Figure 1: The text is too small to be easily readable.

### Suggestions

The paper should provide a more thorough analysis of the pre-trained encoder-decoder model's generalization capabilities. Specifically, the authors should investigate how the performance of the encoder-decoder on unseen environments correlates with the performance of the proposed data augmentation methods. This could involve evaluating the segmentation quality of the encoder-decoder on images from different environments and correlating this with the performance of the RL agent. Furthermore, the authors should explore the sensitivity of their method to the choice of pre-trained encoder-decoder. It would be beneficial to show results using different pre-trained models, or different architectures, to demonstrate the robustness of the proposed approach. The paper should also discuss the potential limitations of relying on a pre-trained model and explore alternative approaches that do not require such a dependency, or at least mitigate this dependency.

The justification for using Q-value distance as a measure of semantic invariance needs to be strengthened. The authors should provide a more detailed explanation of why this metric is a suitable proxy for semantic changes. It would be helpful to compare the Q-value distance with other metrics that directly measure semantic similarity, such as those based on feature embeddings from pre-trained vision models. The paper should also investigate the sensitivity of the Q-value distance to different types of augmentations and different Q-function approximators. It is important to understand the limitations of this metric and how it might affect the performance of the proposed method. The authors should also consider the potential for instability in Q-value estimates, especially during early training, and how this might impact the reliability of the proposed metric. A more robust approach might involve using a moving average of Q-values or a different metric altogether.

To improve the generalizability of the findings, the authors should evaluate their methods on a wider range of visual reinforcement learning tasks. This could include more complex environments with distractors, occlusions, and variations in lighting and viewpoint. The paper should also discuss the potential limitations of the proposed methods in such scenarios and explore ways to address these limitations. For example, the authors could investigate the use of more sophisticated data augmentation techniques that are robust to these challenges. Furthermore, the authors should consider evaluating their methods on tasks with different reward structures and action spaces to demonstrate the versatility of their approach. The current evaluation is limited to the DMControl suite, which may not fully capture the challenges of real-world visual RL problems.

### Questions

- How does the performance of the encoder-decoder model on unseen environments affect the performance of the proposed methods?
- Could you provide more details on how the Q-value distance is calculated and why it is a good measure of semantic-invariant state transformation?
- How do the proposed methods compare to other state-of-the-art methods in terms of computational cost and sample efficiency?

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
