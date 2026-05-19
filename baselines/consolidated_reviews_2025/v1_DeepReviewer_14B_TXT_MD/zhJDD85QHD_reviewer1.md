### Summary

This paper introduces Concept-based Explainable Image Representation (CEIR), a novel approach designed to enhance the interpretability of self-supervised learning representations in machine learning. By utilizing a Concept-based Model (CBM) with pretrained CLIP and concepts from GPT-4, CEIR projects input images into a concept vector space, allowing representations to align with human-understandable concepts. A Variational Autoencoder (VAE) then learns latent representations from these concepts, facilitating attributions to a semantically rich, interpretable concept space while maintaining robustness for downstream tasks. CEIR achieves state-of-the-art unsupervised clustering performance on benchmarks such as CIFAR10, CIFAR100, and STL10. Additionally, it leverages human conceptual understanding to extract related concepts from open-world images without fine-tuning, offering a new method for automatic label generation and manipulation.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

- The paper is clearly written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

 - The pipeline of this paper seems to be an incremental work of Label-free CBM, but this paper lacks comparisons with Label-free CBM.
- The concept pool generation process is highly similar to the concept pool in Label-free CBM, which also utilizes GPT-3 to generate concepts. 
- The concept filtering of this paper also adopts the class-related concepts from Label-free CBM.
- This paper introduces additional components, CLIP and VAE, to the framework of Label-free CBM. The contribution of this paper is to extend Label-free CBM from the classification task to the representation learning task, using the same concept pool generation process, concept filtering, and Label-free CBM framework. However, this paper does not compare with Label-free CBM on classification tasks.
- This paper lacks comparisons with other concept-based models on representation learning tasks.
- This paper lacks a comparison of its concept pools with those of other concept-based models.
- The main experiments in this paper lack comparisons with Label-free CBM and other concept-based models on both classification and representation learning tasks.
- The main experiments in this paper lack a comparison of the concept pools with those of other concept-based models.
- The paper seems to be an incremental work of Label-free CBM but does not cite Label-free CBM.

### Suggestions

The paper's primary weakness lies in its incremental nature compared to Label-free CBM, particularly given the lack of direct comparisons. While the authors introduce a VAE for representation learning, the core concept generation and filtering processes are very similar to Label-free CBM. To strengthen the paper, the authors should include a direct comparison with Label-free CBM on both classification and representation learning tasks. This comparison should use the same datasets and evaluation metrics to provide a clear understanding of the performance gains or losses. Furthermore, a detailed analysis of the computational overhead introduced by the VAE component is necessary, including training time, memory usage, and inference speed. This analysis should be compared against the computational cost of Label-free CBM to justify the added complexity. The authors should also explore the impact of different VAE architectures on the quality of the learned representations, providing a more comprehensive evaluation of their approach.

Another significant weakness is the lack of comparison with other concept-based models in the representation learning domain. The authors should include a thorough comparison with existing concept-based models, such as those based on concept bottleneck models or other interpretable architectures. This comparison should not only focus on quantitative metrics like clustering performance but also on the quality and interpretability of the learned concept representations. A detailed analysis of the concept pools used by different models is also needed. This analysis should include a comparison of the diversity, coverage, and human-interpretability of the concepts. The authors should also investigate how the choice of concept pool affects the performance of the model on downstream tasks. This would provide a more comprehensive understanding of the strengths and weaknesses of their approach compared to existing methods.

Finally, the paper would benefit from a more detailed discussion of the limitations of the proposed approach. For example, the authors should discuss the potential biases introduced by using GPT-4 for concept generation and how these biases might affect the learned representations. They should also explore the sensitivity of their approach to the choice of hyperparameters, such as the number of concepts and the VAE architecture. Furthermore, the authors should discuss the scalability of their approach to larger datasets and more complex tasks. Addressing these limitations would provide a more balanced and realistic assessment of the proposed method and guide future research in this area.

### Questions

- What is the computational overhead of the VAE component compared to Label-free CBM?
- How does the quality of the learned representations compare to that of Label-free CBM on classification tasks?
- How do the concept pools generated by this method compare in quality and diversity to those from other concept-based models?
- What are the trade-offs between interpretability and performance when using CEIR compared to Label-free CBM?

### Rating

3: reject, not good enough

### Confidence

5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

**********
