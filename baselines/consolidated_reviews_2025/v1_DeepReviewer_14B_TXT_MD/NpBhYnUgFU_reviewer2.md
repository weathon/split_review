### Summary

This paper introduces a novel framework named SuperCAT, which integrates super-resolution technology with zero-shot scene classification tasks. The core of the SuperCAT framework is a cross-semantic attribute-guided Transformer (CAT) module. This module consists of a semantic attribute-to-visual Transformer (SAVT) and a visual-to-semantic attribute Transformer (VSAT), which extract attribute-based visual features and visual-based attribute features, respectively. Additionally, the paper utilizes f-VAEGAN to map semantic vectors to visual representations and employs a feature refinement (FR) module to enhance the visual features of both seen and unseen class samples in remote sensing images, thereby improving classification performance in zero-shot learning scenarios.

### Soundness

3

### Presentation

2

### Contribution

2

### Strengths

This paper proposes a SuperCAT framework that combines super-resolution with the zero-shot scene classification task to enhance the classification performance of remote sensing images. It utilizes semantic attributes across three remote sensing benchmark datasets to capture the unique characteristics of different scenes in zero-shot scene classification. The paper also explores feature generation (f-VAEGAN) and feature refinement (FR) modules to refine visual features for zero-shot scene classification in remote sensing images.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide sufficient explanation or experimental analysis for the super-resolution module's impact on overall performance. Ablation studies on the necessity and impact of the super-resolution module should be added.
2. The paper lacks an in-depth discussion of the framework's limitations and potential solutions.
3. The paper does not provide sufficient details about the semantic attributes used, including their number and how they are represented.

### Suggestions

The paper should include a more detailed analysis of the super-resolution module's contribution to the overall performance of the SuperCAT framework. Specifically, the authors should conduct ablation studies to quantify the impact of the super-resolution module on the final classification accuracy. This should include comparing the performance of the full framework with a version where the super-resolution module is bypassed or replaced with a simpler upsampling method. Furthermore, the authors should analyze the effect of different super-resolution techniques on the final results, which could provide insights into the optimal choice of super-resolution method for this specific task. The analysis should also include a discussion of the computational cost added by the super-resolution module and whether the performance gain justifies the added complexity. This would provide a more comprehensive understanding of the trade-offs involved in using the super-resolution module.

To address the lack of discussion on the framework's limitations, the authors should provide a more thorough analysis of potential failure cases and scenarios where the framework might not perform well. This could include situations with very low-resolution images, highly complex scenes, or classes with limited semantic information. The authors should also discuss the potential impact of noisy or inaccurate semantic attributes on the framework's performance. Furthermore, the paper should explore potential solutions to these limitations, such as incorporating more robust feature extraction techniques, using more sophisticated generative models, or exploring alternative loss functions. A discussion of the scalability of the framework to larger datasets and more complex classification tasks would also be beneficial. This would provide a more balanced view of the framework's capabilities and areas for future improvement.

Finally, the paper needs to provide more clarity on the semantic attributes used in the framework. The authors should specify the exact number of semantic attributes used for each dataset and provide a detailed description of how these attributes are represented (e.g., one-hot encoding, word embeddings). If word embeddings are used, the authors should specify the pre-trained model used to obtain these embeddings. The paper should also include a discussion of how the semantic attributes are selected and whether the framework is sensitive to the choice of attributes. Furthermore, the authors should analyze the impact of the quality and relevance of the semantic attributes on the overall performance of the framework. This would provide a better understanding of the role of semantic attributes in the framework and how to optimize their use.

### Questions

Please refer to Weaknesses.

### Rating

5

### Confidence

5

**********
