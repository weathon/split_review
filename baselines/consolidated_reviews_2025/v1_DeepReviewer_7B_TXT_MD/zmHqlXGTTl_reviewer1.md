### Summary

This paper introduces a new task, LayoutSciPG, for scientific poster generation. To tackle this, the authors first built a new dataset, namely SciPG, with over 10,000 pairs of scientific papers and their corresponding posters. They then developed a multimodal extractor to capture both text and image elements from the paper, and implemented an interactive generator with an adaptive memory mechanism to seamlessly integrate the paraphrasing of extracted content with layout generation. Both qualitative and quantitative evaluations highlight the effectiveness of their approach.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper introduces a new dataset, SciPG, which could be useful for future research in scientific poster generation.
2. The paper proposes a novel approach to layout-aware scientific poster generation, which is a challenging task.
3. The paper presents both qualitative and quantitative evaluations of the proposed approach, which demonstrates its effectiveness.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a clear definition of the LayoutSciPG task, which makes it difficult to understand the problem being addressed. The paper should provide a formal definition of the task, including the input and output, and the evaluation metrics.
2. The paper does not provide a clear explanation of how the proposed approach addresses the challenges of the LayoutSciPG task. The paper should explain how the multimodal extractor and interactive generator work together to generate posters, and how the adaptive memory mechanism helps to handle long-term dependencies.
3. The paper does not provide a comparison with existing approaches for scientific poster generation. The paper should compare the proposed approach with existing approaches, and highlight the advantages and disadvantages of the proposed approach.
4. The paper does not provide a discussion of the limitations of the proposed approach. The paper should discuss the limitations of the proposed approach, and suggest future directions for research.

### Suggestions

The paper needs to clearly define the LayoutSciPG task, specifying the exact input (e.g., a structured representation of the scientific paper) and the desired output (e.g., a structured layout for a poster with specific elements). The current description is vague, making it difficult to understand the problem being solved. The authors should provide a formal definition, including the specific elements that need to be extracted from the paper and placed on the poster, and the relationships between these elements. For example, the definition should specify whether the input includes the paper title, authors, and venue, and how these are related to the poster layout. The evaluation metrics should also be clearly defined, including how they measure the quality of the generated posters. Without a clear definition, it is difficult to assess the significance of the proposed approach.

The paper should provide a more detailed explanation of how the proposed approach addresses the challenges of the LayoutSciPG task. The authors should explain the architecture of the multimodal extractor, including the specific layers and their functions. They should also explain how the interactive generator works, including how it integrates the paraphrasing of extracted content with layout generation. The adaptive memory mechanism should be explained in detail, including how it handles long-term dependencies and how it contributes to the overall performance of the approach. The paper should also provide a clear explanation of how the proposed approach differs from existing approaches for scientific poster generation. The authors should discuss the limitations of existing approaches and how their proposed approach addresses these limitations. For example, the paper should discuss how the proposed approach handles the complexity of scientific posters, which often include multiple figures, tables, and equations.

Finally, the paper should provide a more comprehensive evaluation of the proposed approach. The authors should compare the performance of their approach with existing approaches for scientific poster generation, using appropriate evaluation metrics. The paper should also discuss the limitations of the proposed approach, and suggest future directions for research. For example, the paper should discuss the limitations of the proposed approach in handling complex scientific posters, and suggest ways to improve the approach. The paper should also discuss the potential impact of the proposed approach on the scientific community, and how it can be used to improve the communication of scientific knowledge.

### Questions

1. What is the definition of the LayoutSciPG task?
2. How does the proposed approach address the challenges of the LayoutSciPG task?
3. How does the proposed approach compare with existing approaches for scientific poster generation?
4. What are the limitations of the proposed approach?

### Rating

3

### Confidence

4

**********
