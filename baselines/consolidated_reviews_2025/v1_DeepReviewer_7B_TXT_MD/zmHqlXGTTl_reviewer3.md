### Summary

This paper introduces a new task called layout-aware scientific poster generation (LayoutSciPG), which aims to generate flexible and flexible posters from scientific papers. To achieve this, the authors constructed a large-scale dataset, SciPG, containing over 10,000 pairs of scientific papers and their corresponding posters. They then proposed a multimodal extractor-generator framework for LayoutSciPG. This framework consists of a multimodal extractor to retrieve key text and image elements from the papers and an interactive generator with an adaptive memory mechanism to seamlessly paraphrase the extracted elements and generate the corresponding layout positions. The experiments demonstrate the effectiveness of the proposed approach while highlighting remaining challenges.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper introduces a new task called layout-aware scientific poster generation (LayoutSciPG), which aims to generate flexible and flexible posters from scientific papers. This task is novel and addresses an important area in scientific communication.

2. The authors constructed a large-scale dataset, SciPG, containing over 10,000 pairs of scientific papers and their corresponding posters. This dataset is a valuable resource for future research in this area.

3. The paper proposes a multimodal extractor-generator framework to address the challenges of this new task, including multimodal extraction, multimodal generation, and large-scale training data.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a clear definition of the LayoutSciPG task, which makes it difficult to understand the problem being addressed. The paper should provide a formal definition of the task, including the input and output, and the evaluation metrics.

2. The paper does not provide a clear explanation of how the proposed approach addresses the challenges of the LayoutSciPG task. The paper should explain how the multimodal extractor and interactive generator work together to generate posters, and how the adaptive memory mechanism helps to handle long-term dependencies.

3. The paper does not provide a comparison with existing approaches for scientific poster generation. The paper should compare the proposed approach with existing approaches, and highlight the advantages and disadvantages of the proposed approach.

4. The paper does not provide a discussion of the limitations of the proposed approach. The paper should discuss the limitations of the proposed approach, and suggest future directions for research.

### Suggestions

The paper introduces a novel task, LayoutSciPG, and a corresponding dataset, SciPG, which is a valuable contribution. However, the paper lacks a clear and precise definition of the task itself. The authors should provide a formal definition, specifying the input (e.g., a structured representation of the scientific paper) and the desired output (e.g., a structured layout for a poster with specific elements). This definition should include the specific elements that need to be extracted from the paper and placed on the poster, and the relationships between these elements. For example, the definition should specify whether the input includes the paper title, authors, and venue, and how these are related to the poster layout. The evaluation metrics should also be clearly defined, including how they measure the quality of the generated posters. Without a clear definition, it is difficult to assess the validity and impact of the proposed approach.

Furthermore, the paper needs to provide a more detailed explanation of the proposed approach. The authors should elaborate on the architecture of the multimodal extractor-generator framework, including the specific layers and their functions. They should explain how the extractor captures both text and image elements from the paper, and how the generator integrates the paraphrasing of extracted content with layout generation. The adaptive memory mechanism should be explained in detail, including how it handles long-term dependencies and how it contributes to the overall performance of the approach. The paper should also provide a clear explanation of how the proposed approach differs from existing approaches for scientific poster generation. The authors should discuss the limitations of existing approaches and how their proposed approach addresses these limitations. For example, the paper should discuss how the proposed approach handles the complexity of scientific posters, which often include multiple figures, tables, and equations.

Finally, the paper needs to provide a more comprehensive evaluation of the proposed approach. The authors should compare the performance of their approach with existing approaches for scientific poster generation, using appropriate evaluation metrics. The paper should also discuss the limitations of the proposed approach, and suggest future directions for research. For example, the paper should discuss the limitations of the proposed approach in handling complex scientific posters, and suggest ways to improve the approach. The paper should also discuss the potential impact of the proposed approach on the scientific community, and how it can be used to improve the communication of scientific knowledge. The paper should also include a discussion of the ethical considerations of using AI to generate scientific posters, and how these considerations can be addressed.

### Questions

1. What is the definition of the LayoutSciPG task?

2. How does the proposed approach address the challenges of the LayoutSciPG task?

3. How does the proposed approach compare with existing approaches for scientific poster generation?

4. What are the limitations of the proposed approach?

### Rating

5

### Confidence

4

**********
