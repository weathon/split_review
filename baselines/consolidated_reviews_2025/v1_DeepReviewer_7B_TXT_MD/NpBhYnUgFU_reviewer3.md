### Summary

This paper proposes a novel framework called SuperCAT for zero-shot remote sensing scene classification. The framework consists of a super-resolution module, a cross-semantic attribute-guided Transformer (CAT) module, a feature generating model (f-VAEGAN), and a feature refinement (FR) module. The super-resolution module enhances the resolution of remote sensing images, while the CAT module learns to obtain attribute-based visual features and visual-based attribute features. The f-VAEGAN generates synthetic features for unseen classes constrained by semantic vectors, and the FR module refines the visual features of both seen and unseen classes. The proposed method is evaluated on three benchmark datasets, and the experimental results demonstrate its effectiveness in zero-shot remote sensing scene classification.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper proposes a novel framework that combines super-resolution with zero-shot learning for remote sensing scene classification. This integration is innovative and addresses the unique challenges of remote sensing images, such as diverse object variations and non-uniform spatial resolutions.
2. The paper provides a thorough description of the proposed framework, including the super-resolution module, the CAT module, the f-VAEGAN, and the FR module. The authors also provide detailed explanations of the loss functions used in the training process.
3. The paper evaluates the proposed method on three benchmark datasets, and the experimental results demonstrate its effectiveness in zero-shot remote sensing scene classification. The results show that the proposed method outperforms state-of-the-art approaches on these datasets.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the computational complexity of the proposed framework. The authors should provide a detailed analysis of the time and memory requirements of each module, especially the CAT module, which involves multiple attention mechanisms and cross-attention operations. This analysis should include a comparison with existing methods to demonstrate the efficiency of the proposed approach.
2. The paper does not provide a comprehensive ablation study to evaluate the contribution of each component of the proposed framework. For example, the authors should evaluate the performance of the framework without the super-resolution module, the CAT module, or the f-VAEGAN. This would help to understand the importance of each component and to identify potential areas for improvement.
3. The paper does not discuss the limitations of the proposed method. For example, the authors should discuss the potential impact of the choice of pre-trained models on the performance of the framework, and the sensitivity of the framework to different hyperparameter settings. This discussion would provide a more complete understanding of the proposed method and its potential for future research.

### Suggestions

The authors should provide a more detailed analysis of the computational complexity of their proposed framework. Specifically, they should include a breakdown of the time and memory requirements for each module, particularly the CAT module, which involves multiple attention mechanisms and cross-attention operations. This analysis should not only consider the theoretical complexity but also provide empirical measurements on the actual runtime and memory usage. Furthermore, a comparison with existing methods in terms of computational cost would be beneficial to demonstrate the efficiency of the proposed approach. This analysis should also consider the impact of different input resolutions on the computational cost, as this can significantly affect the practical applicability of the method. It would be useful to see a table or graph that shows the computational cost of each module as a function of input size and resolution.

In addition to the computational analysis, a comprehensive ablation study is crucial for understanding the contribution of each component of the proposed framework. The authors should evaluate the performance of the framework with and without each module, including the super-resolution module, the CAT module, and the f-VAEGAN. This would help to quantify the importance of each component and identify potential areas for optimization. For example, the authors could start by removing the CAT module and observe the performance drop, then add it back and see the improvement. Similarly, they could evaluate the impact of removing the f-VAEGAN and the FR module. The ablation study should also consider different combinations of modules to understand their interactions and dependencies. The results of the ablation study should be presented in a clear and concise manner, with detailed explanations of the observed performance changes.

Finally, the authors should discuss the limitations of their proposed method. This discussion should include an analysis of the potential impact of the choice of pre-trained models on the performance of the framework. For example, the authors could discuss how different pre-trained models might affect the quality of the generated synthetic features and the overall classification performance. They should also discuss the sensitivity of the framework to different hyperparameter settings, such as the learning rate, batch size, and the parameters of the attention mechanisms. This discussion should also consider the limitations of the datasets used for evaluation, such as the size and diversity of the datasets. It would be beneficial to see a sensitivity analysis that shows how the performance of the framework changes with different hyperparameter settings. This discussion would provide a more complete understanding of the proposed method and its potential for future research.

### Questions

1. How does the proposed method handle the variability in object scales and aspect ratios in remote sensing images, given that super-resolution is primarily designed for image enhancement rather than object-level tasks?
2. What is the computational complexity of the proposed framework, especially the CAT module, and how does it compare to existing zero-shot learning methods?
3. How does the model ensure the robustness of the learned semantic attributes, especially when dealing with noisy or ambiguous remote sensing images?

### Rating

6

### Confidence

4

**********
