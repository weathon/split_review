### Summary

This paper introduces a novel framework named SuperCAT, designed to enhance zero-shot remote sensing scene classification by integrating super-resolution technology with a cross-semantic attribute-guided Transformer (CAT) module. The framework aims to improve classification performance by addressing the unique challenges of remote sensing images, such as diverse object variations and non-uniform spatial resolutions. The authors claim that SuperCAT outperforms state-of-the-art methods on several benchmark datasets, demonstrating its effectiveness in classifying both seen and unseen classes in remote sensing images.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The integration of super-resolution with zero-shot learning in remote sensing is a novel approach that addresses the specific challenges of these images.
2. The paper provides a thorough description of the proposed framework, including the CAT module and feature refinement (FR) module, which contribute to the overall performance.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed explanation of how the semantic attributes are extracted and integrated into the model. The description of the word2vec method for attribute extraction is insufficient, particularly regarding the choice of the Word2Vec model and the specific word vectors used. The paper should clarify how the semantic attributes are encoded and used within the CAT module, including the specific transformations applied to the attribute vectors and how they interact with the visual features.
2. The methodology section does not provide sufficient detail on the implementation of the CAT module, particularly the cross-attention mechanism. The paper should elaborate on the specific attention mechanisms used, including the query, key, and value transformations, and how these are integrated within the CAT module. Furthermore, the paper lacks details on the feature refinement (FR) module, including the specific operations performed, such as concatenation or element-wise addition, and the rationale behind these choices.
3. The experimental section lacks a comprehensive comparison with other state-of-the-art zero-shot learning methods, particularly those that also utilize attention mechanisms or generative models. The paper should include a more thorough comparison with relevant baselines, including a detailed analysis of the performance differences and the reasons behind them. The paper also lacks ablation studies to demonstrate the contribution of each component of the proposed framework, such as the super-resolution module, the CAT module, and the FR module. This makes it difficult to assess the individual impact of each component on the overall performance.

### Suggestions

The paper should provide a more detailed explanation of the semantic attribute extraction process. Specifically, the authors should clarify the choice of the Word2Vec model and the specific word vectors used. They should also describe how the semantic attributes are encoded and integrated into the model, including the specific transformations applied to the attribute vectors and how they interact with the visual features. For example, are the attribute vectors concatenated with the visual features, or are they combined using a more complex operation? The paper should also include a visualization of the learned attribute embeddings to demonstrate their semantic meaning. Furthermore, the paper should discuss the limitations of using word2vec for attribute extraction and consider alternative methods, such as using pre-trained visual embeddings or learning visual-semantic embeddings jointly.

The methodology section needs to provide a more detailed explanation of the CAT module, particularly the cross-attention mechanism. The authors should elaborate on the specific attention mechanisms used, including the query, key, and value transformations, and how these are integrated within the CAT module. The paper should also provide a clear explanation of how the visual and semantic features are combined within the CAT module. For example, are the visual and semantic features concatenated, or are they combined using a more complex operation? The paper should also include a visualization of the attention maps to demonstrate how the model attends to different parts of the input features. Furthermore, the paper should discuss the limitations of the current attention mechanism and consider alternative approaches, such as using different attention mechanisms or incorporating spatial information.

The experimental section should include a more comprehensive comparison with other state-of-the-art zero-shot learning methods, particularly those that also utilize attention mechanisms or generative models. The paper should include a detailed analysis of the performance differences and the reasons behind them. The paper should also include ablation studies to demonstrate the contribution of each component of the proposed framework, such as the super-resolution module, the CAT module, and the FR module. This would help to assess the individual impact of each component on the overall performance. For example, the authors could evaluate the performance of the model with and without the super-resolution module, with and without the CAT module, and with and without the FR module. This would provide a more thorough understanding of the contribution of each component and help to identify the key factors that contribute to the model's performance.

### Questions

1. How does the proposed model handle the variability in object scales and aspect ratios in remote sensing images, given that super-resolution is primarily designed for image enhancement rather than object-level tasks?
2. What is the computational complexity of the proposed framework, especially the CAT module, and how does it compare to existing zero-shot learning methods?
3. How does the model ensure the robustness of the learned semantic attributes, especially when dealing with noisy or ambiguous remote sensing images?

### Rating

5

### Confidence

4

**********
