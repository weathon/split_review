### Summary

This paper presents the SuperCAT framework for zero-shot remote sensing scene classification, integrating super-resolution, feature generation, and refinement modules. The super-resolution module uses ResShift to enhance image resolution. The CAT module, with its SAVT and VSAT sub-modules, facilitates semantic-visual feature learning through collaborative loss. The f-VAEGAN generates synthetic visual features, while the FR module refines them using TCM and SLC losses. The framework shows improved classification performance across datasets.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The SuperCAT framework combines super-resolution with zero-shot learning for remote sensing images, which is less explored in previous works.
2. The paper provides a detailed description of the framework components, including the super-resolution module, CAT module, and feature refinement module.

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

1. How does the super-resolution module specifically contribute to the zero-shot learning task? What would be the impact on performance if the super-resolution module were removed or replaced with a simpler upsampling method?
2. What are the limitations of the proposed framework, and are there potential solutions? For example, how does the framework handle very low-resolution images, and could the feature generation and refinement modules be improved further?
3. What is the number of attributes associated with each dataset, and how are these attributes represented and utilized within the framework?

### Rating

3

### Confidence

5

**********
