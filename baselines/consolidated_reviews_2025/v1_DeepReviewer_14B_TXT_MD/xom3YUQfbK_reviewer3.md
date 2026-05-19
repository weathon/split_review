### Summary

This paper introduces a framework that leverages LLMs to generate natural language descriptions of the differences between two ML models. The framework is flexible and can be used with various model types and datasets, and it is extensible, allowing the user to incorporate model-specific information. The authors evaluate their framework on three classification datasets using three state-of-the-art LLMs as verbalizers, and they conduct ablation studies to analyze the impact of different design choices. The results show that the framework is effective in verbalizing the differences between models, especially for parametric models like logistic regression and decision trees. The paper also discusses the potential of the framework for future research in model management tools.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper introduces a novel framework that leverages LLMs to generate natural language descriptions of the differences between two ML models. This is a unique approach that has not been explored in the literature before.
2. The framework is flexible and can be used with various model types and datasets, and it is extensible, allowing the user to incorporate model-specific information.
3. The authors evaluate their framework on three classification datasets using three state-of-the-art LLMs as verbalizers, and they conduct ablation studies to analyze the impact of different design choices. The results show that the framework is effective in verbalizing the differences between models, especially for parametric models like logistic regression and decision trees.

### Weaknesses

#### Some Related Works


#### comment

1. The paper only focuses on classification models and tabular data. The authors should discuss this limitation and propose potential solutions for other types of models and data.
2. The prompt is a key component of the framework, but it is not discussed in detail. The authors should discuss how they arrived at the current prompt and if they performed any prompt engineering.
3. The framework currently relies on sampling the input space to identify differences between models, which may miss subtle but important distinctions.

### Suggestions

The paper's focus on classification models and tabular data limits its applicability. The authors should explore how the framework could be extended to regression tasks, where the notion of 'differences' might be more nuanced. For example, instead of comparing class predictions, the framework would need to compare continuous output values, potentially requiring different verbalization strategies. Furthermore, the framework should be evaluated on non-tabular data such as images or text, which would require adapting the input representation and potentially the prompting strategy. The authors could consider using techniques like feature extraction or embedding methods to represent non-tabular data in a format suitable for the LLM. Addressing these limitations would significantly broaden the impact and usefulness of the proposed framework.

The prompt engineering process is critical to the success of this framework, yet it is not discussed in sufficient detail. The authors should provide a more thorough explanation of how they designed the prompt, including any iterative refinement or ablation studies they performed. For example, they could discuss the impact of different instructions, the format of the input data, and the inclusion of model-specific information. A detailed analysis of the prompt's sensitivity to various factors would provide valuable insights into the framework's robustness and generalizability. Furthermore, the authors should consider exploring different prompting techniques, such as chain-of-thought prompting or few-shot learning, to see if they can further improve the quality of the generated descriptions.

The current approach of sampling the input space to identify differences between models is a potential source of bias and may miss subtle but important distinctions. The authors should explore alternative strategies for selecting input samples that are more likely to highlight meaningful differences between models. For example, instead of random sampling, they could use techniques such as adversarial examples or samples that are near the decision boundary of one or both models. These samples are more likely to expose discrepancies in the models' behavior. Furthermore, the authors should discuss the limitations of relying solely on input-output comparisons and explore the possibility of incorporating model-specific information into the analysis. For instance, for decision trees, the framework could incorporate the tree structure and feature importance scores to provide more informative verbalizations. For logistic regression models, the framework could include the coefficients and intercepts to help explain the differences in model behavior.

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
