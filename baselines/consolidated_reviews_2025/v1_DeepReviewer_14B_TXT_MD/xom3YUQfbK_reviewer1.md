### Summary

The paper introduces "Model Manager", a framework that uses large language models (LLMs) to help users compare and understand the differences between machine learning models, addressing the challenge of navigating numerous, often poorly documented models (the "model lake"). The framework generates human-understandable explanations of the differences in predictions between two models by sampling inputs and feeding the results to an LLM, which then produces a natural language summary of the models' divergences. Model Manager is evaluated on three classification datasets using different model pairs (Logistic Regression, Decision Trees, and KNN), showing promising results, particularly for parametric models. The paper also includes ablation studies to analyze the impact of various design choices.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

- The paper is well written and easy to follow.
- The idea is interesting and original. The fact that the framework can be applied to multiple model families is promising.
- The authors provide a good evaluation of their method, including ablation studies to understand the impact of various design choices.

### Weaknesses

#### Some Related Works


#### comment

 - The paper only focuses on classification models and tabular data. The authors should discuss this limitation and propose potential solutions for other types of models and data.
- The prompt is a key component of the framework, but it is not discussed in detail. The authors should discuss how they arrived at the current prompt and if they performed any prompt engineering.
- The framework currently relies on sampling the input space to identify differences between models, which may miss subtle but important distinctions. The authors should propose potential improvements to address this limitation.

### Suggestions

The paper's focus on classification models and tabular data is a significant limitation that needs to be addressed more thoroughly. While the authors mention the framework's potential applicability to other model types, they do not provide concrete examples or discuss the specific challenges involved in adapting it to, for example, regression models, time-series data, or models that process unstructured data like images or text. For regression tasks, the framework would need to be adapted to compare continuous outputs, which may require different metrics and verbalization strategies. For instance, instead of comparing class assignments, the framework would need to compare the magnitude and direction of differences in predicted values. Furthermore, the framework's reliance on tabular data limits its applicability to a large portion of machine learning applications. The authors should explore how the framework could be extended to handle non-tabular data, such as images, where the input space is high-dimensional and structured differently. This could involve incorporating techniques for extracting relevant features from images or using alternative methods for comparing model outputs. The discussion should also include the computational challenges of sampling in high-dimensional spaces and how to address them.

The prompt engineering process requires more detailed explanation. The current description lacks sufficient information on how the prompt was developed and optimized. The authors should provide details on the specific steps taken to refine the prompt, including the different prompt variations that were tested and the rationale behind each change. It is crucial to understand how the prompt's structure, wording, and the inclusion of specific instructions affect the quality of the generated verbalizations. For example, the authors should discuss whether they experimented with different instructions for the LLM, such as asking it to focus on specific features or to provide explanations in different styles. Furthermore, the authors should discuss the potential for prompt sensitivity, i.e., how the performance of the framework might vary with different prompts. A more rigorous analysis of the prompt engineering process is essential to ensure the reproducibility and robustness of the results. The authors should also consider including an analysis of the prompt's limitations and potential biases.

The current approach of sampling the input space to identify differences between models is a potential source of bias and may miss subtle but important distinctions. The authors should explore alternative strategies for selecting input samples that are more likely to highlight meaningful differences between models. For example, instead of random sampling, they could use techniques such as adversarial examples or samples that are near the decision boundary of one or both models. These samples are more likely to expose discrepancies in the models' behavior. Furthermore, the authors should discuss the limitations of relying solely on input-output comparisons and explore the possibility of incorporating model-specific information into the analysis. For instance, for decision trees, the framework could incorporate the tree structure and feature importance scores to provide more informative verbalizations. For logistic regression models, the framework could include the coefficients and intercepts to help explain the differences in model behavior. The authors should also discuss the computational cost of these alternative strategies and how to balance the need for comprehensive analysis with the need for efficiency.

### Questions

Please see weaknesses.

### Rating

5

### Confidence

4

**********
