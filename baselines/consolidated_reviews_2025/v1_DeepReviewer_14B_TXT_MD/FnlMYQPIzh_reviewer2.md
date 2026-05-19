### Summary

This paper proposes a semi-structured intention framework, ConvINT, which provides a more comprehensive, aspect-aware, and flexible approach to effective CU. It organizes user intentions into four fundamental aspects: situation, emotion, action, and knowledge. To facilitate the large-scale application of this framework, the authors develop a Weakly-supervised Reinforced Generation (WeRG) approach to efficiently expand ConvINT annotations across extensive datasets.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The motivation is clear and the problem is worth exploring.
2. The paper is well written and easy to follow.
3. The proposed method is simple and effective.

### Weaknesses

#### Some Related Works


#### comment

1. The authors should provide a more detailed description of the four aspects in the ConvINT framework. For example, how are the boundaries defined for each aspect, and what specific annotation guidelines were provided to ensure consistency across different annotators? The current description lacks the necessary granularity to fully understand the framework's implementation.
2. The evaluation of the proposed ConvINT framework is limited to two datasets. It would be beneficial to see how the framework performs on a wider range of datasets, including those with different characteristics and domains. This would provide a more robust assessment of the framework's generalizability and applicability.
3. The paper lacks a detailed error analysis. It would be helpful to understand the types of errors the model makes when generating ConvINT annotations. Are there specific aspects that are more challenging to identify or annotate correctly? A detailed error analysis would provide valuable insights into the framework's limitations and potential areas for improvement.
4. The paper does not provide a detailed analysis of the computational resources required for training and inference. This information is crucial for assessing the practical feasibility of the proposed approach, especially when considering large-scale applications.

### Suggestions

To address the lack of detail regarding the ConvINT framework's aspects, the authors should provide a more granular explanation of each aspect (situation, emotion, action, and knowledge). This should include specific examples of how each aspect is identified and annotated in different contexts. For instance, when considering the 'emotion' aspect, the authors should clarify whether they are focusing on explicit emotional expressions or also considering implicit emotional cues. Furthermore, the annotation guidelines should be made more explicit, detailing how annotators were trained to distinguish between the four aspects and resolve ambiguous cases. This would involve providing examples of borderline cases and explaining the rationale behind the annotation decisions. A clear definition of the boundaries between these aspects is crucial for the reproducibility and reliability of the framework.

To strengthen the evaluation of the ConvINT framework, the authors should expand their experiments to include a more diverse set of datasets. This should include datasets from different domains and with varying characteristics, such as datasets with different types of user interactions or different levels of complexity. For example, evaluating the framework on datasets that involve more complex multi-turn dialogues or datasets with a higher degree of ambiguity would provide a more comprehensive understanding of its strengths and weaknesses. Additionally, the authors should consider comparing the performance of the ConvINT framework with other existing intention recognition methods, not just in terms of overall performance but also in terms of the quality of the generated annotations for each aspect. This would provide a more nuanced understanding of the framework's advantages and limitations.

Finally, a detailed error analysis is essential for understanding the limitations of the proposed approach. The authors should categorize the types of errors made by the model, such as misidentification of aspects, incorrect annotation boundaries, or failure to capture subtle nuances. This analysis should also consider the frequency of different error types and their impact on the overall performance of the framework. For example, are certain aspects more prone to errors than others? Are there specific types of user intentions that are more difficult to annotate correctly? This analysis should be accompanied by concrete examples of errors and a discussion of the potential causes. Furthermore, the authors should provide a detailed analysis of the computational resources required for training and inference, including the training time, inference time, and memory usage. This information is crucial for assessing the practical feasibility of the proposed approach, especially when considering large-scale applications.

### Questions

1. The authors should provide a more detailed description of the four aspects in the ConvINT framework.
2. The evaluation of the proposed ConvINT framework is limited to two datasets.
3. The paper lacks a detailed error analysis.
4. The paper does not provide a detailed analysis of the computational resources required for training and inference.

### Rating

6

### Confidence

4

**********
