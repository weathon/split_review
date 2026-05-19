### Summary

This paper introduces a framework that leverages LLMs to generate natural language descriptions of the differences between two ML models. The framework is flexible and can be used with various model types and datasets, and it is extensible, allowing the user to incorporate model-specific information. The authors evaluate their framework on three classification datasets using three state-of-the-art LLMs as verbalizers, and they conduct ablation studies to analyze the impact of different design choices. The results show that the framework is effective in verbalizing the differences between models, especially for parametric models like logistic regression and decision trees. The paper also discusses the potential of the framework for future research in model management tools.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel framework that leverages LLMs to generate natural language descriptions of the differences between two ML models. This is a unique approach that has not been explored in the literature before.
2. The framework is flexible and can be used with various model types and datasets, and it is extensible, allowing the user to incorporate model-specific information.
3. The authors evaluate their framework on three classification datasets using three state-of-the-art LLMs as verbalizers, and they conduct ablation studies to analyze the impact of different design choices. The results show that the framework is effective in verbalizing the differences between models, especially for parametric models like logistic regression and decision trees.

### Weaknesses

#### Some Related Works


#### comment

1. The paper only focuses on classification models and tabular data. The authors should discuss this limitation and propose potential solutions for other types of models and data. For example, the framework's applicability to regression models is unclear, as the notion of differing outputs may need to be redefined in the context of continuous values. Furthermore, the framework's ability to handle non-tabular data such as images or text is not addressed, which limits its generalizability.
2. The prompt is a key component of the framework, but it is not discussed in detail. The authors should discuss how they arrived at the current prompt and if they performed any prompt engineering. The lack of detail makes it difficult to assess the robustness of the framework to variations in the prompt structure or wording. It is also unclear if the prompt is optimized for all model types and datasets.
3. The framework currently relies on sampling the input space to identify differences between models, which may miss subtle but important distinctions. The authors should propose potential improvements to address this limitation. The current sampling strategy may not be sufficient to capture the full range of differences between models, especially if the differences are concentrated in specific regions of the input space. This could lead to an incomplete or inaccurate verbalization of the model differences.

### Suggestions

The paper's focus on classification models and tabular data is a significant limitation that needs to be addressed. The authors should discuss how the framework could be extended to handle regression models, where the output is a continuous value rather than a class label. This would require a different approach to identifying and verbalizing differences, as the concept of 'differing outputs' is not directly applicable. For example, the framework could be adapted to compare the predicted values of regression models and verbalize the magnitude and direction of the differences. Additionally, the authors should explore the framework's applicability to non-tabular data such as images or text. This would involve developing methods for extracting relevant features from these data types and adapting the verbalization process to handle the unique characteristics of image and text data. For instance, the framework could be used to compare the predictions of image classification models or text sentiment analysis models, and verbalize the differences in their predictions based on the extracted features.

The prompt engineering process requires more detailed explanation. The authors should provide a comprehensive description of how they arrived at the current prompt, including any experiments or iterations they performed. This should include a discussion of the different prompt components and their impact on the verbalization quality. For example, the authors could discuss the effect of including model-specific information in the prompt, or the impact of different instructions on the LLM's output. Furthermore, the authors should analyze the robustness of the framework to variations in the prompt structure or wording. This could involve testing the framework with different prompts and evaluating the consistency of the verbalizations. The authors should also consider the potential for prompt bias and discuss how they mitigated this issue. A more detailed analysis of the prompt engineering process would enhance the reproducibility and reliability of the framework.

The current approach of sampling the input space to identify differences between models is a potential source of bias and may miss subtle but important distinctions. The authors should explore alternative strategies for selecting input samples that are more likely to highlight meaningful differences between models. For example, instead of random sampling, they could use techniques such as adversarial examples or samples that are near the decision boundary of one or both models. These samples are more likely to expose discrepancies in the models' behavior. Furthermore, the authors should discuss the limitations of relying solely on input-output comparisons and explore the possibility of incorporating model-specific information into the analysis. For instance, for decision trees, the framework could incorporate the tree structure and feature importance scores to provide more informative verbalizations. For logistic regression models, the framework could include the coefficients and intercepts to help explain the differences in model behavior. The authors should also discuss the computational cost of these alternative strategies and how to balance the need for comprehensive analysis with the need for efficiency.

### Questions

1. How does the framework handle cases where the two models being compared have very different performance levels? Does it generate different verbalizations for pairs of models with varying levels of performance difference?
2. How does the framework handle cases where the two models being compared have different types of errors? Does it generate different verbalizations for pairs of models with varying types of errors?
3. How does the framework handle cases where the two models being compared have different levels of confidence in their predictions? Does it generate different verbalizations for pairs of models with varying levels of confidence?
4. How does the framework handle cases where the two models being compared have different levels of interpretability? Does it generate different verbalizations for pairs of models with varying levels of interpretability?
5. How does the framework handle cases where the two models being compared have different levels of complexity? Does it generate different verbalizations for pairs of models with varying levels of complexity?

### Rating

5

### Confidence

4

**********
