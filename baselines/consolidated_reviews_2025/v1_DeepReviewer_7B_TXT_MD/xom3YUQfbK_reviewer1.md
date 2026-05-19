### Summary

This paper presents a framework that uses LLMs to generate verbalizations of the differences between two models. The framework serializes a representative sample and the outputs of two models into a JSON format and passes it to an LLM to generate a textual description of the differences between the models. The authors propose a novel evaluation method to quantify the quality of the verbalizations. The authors conduct experiments on three datasets and compare three LLMs. The results show that the framework can effectively verbalize the differences between two logistic regression models, with Claude 3.5 Sonnet achieving the best performance.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

- The paper is well-written and easy to follow.
- The authors propose a novel evaluation method to quantify the quality of the verbalizations.
- The authors conduct experiments on three datasets and compare three LLMs.

### Weaknesses

#### Some Related Works

[1] ModelDICE: A Model-Based Method for Interpreting and Explaining Deep Models
[2] Interpretable feature extraction with learned sparse distributed representations

#### comment

 - The paper lacks a discussion of related work, such as feature extraction methods [1,2].
- The paper lacks a discussion of the limitations of the proposed framework.
- The paper lacks a discussion of the potential applications of the proposed framework.

### Suggestions

The paper would benefit significantly from a more thorough discussion of related work, particularly in the area of feature extraction. The current version omits relevant methods that aim to extract meaningful features from model predictions, which could provide valuable context for the proposed framework. For instance, techniques that learn sparse distributed representations or methods that identify stable features across different model predictions should be discussed. These methods often provide insights into what aspects of the input data are driving model decisions, and comparing the proposed framework against these approaches could highlight its strengths and weaknesses. A more comprehensive literature review would help to position the work more clearly within the broader field of model interpretability and explainability.

Furthermore, the paper should delve deeper into the limitations of the proposed framework. While the authors acknowledge that the framework is currently limited to comparing two models, they do not fully explore the implications of this constraint. For example, how would the framework handle scenarios where the models being compared have different architectures or training procedures? What are the computational costs associated with generating verbalizations for a large number of models? Addressing these questions would provide a more complete picture of the framework's applicability and scalability. Additionally, the paper should discuss the potential biases that might be introduced by the LLM used for verbalization. The quality of the verbalizations is likely dependent on the LLM's understanding of the underlying concepts, and this dependence should be acknowledged and explored.

Finally, the paper needs a more detailed discussion of potential applications for the proposed framework. While the authors mention that the framework could be used for model selection and debugging, they do not provide concrete examples of how this would work in practice. For instance, how would the framework be used to compare models trained on different datasets? What kind of insights could be gained from comparing models with different levels of performance? A more detailed discussion of potential applications would help to demonstrate the practical value of the framework and motivate further research in this area. The paper should also consider the ethical implications of using LLMs to generate verbalizations, particularly in sensitive domains where model explanations are critical.

### Questions

- How would the proposed framework handle scenarios where the models being compared have different architectures or training procedures?
- What are the computational costs associated with generating verbalizations for a large number of models?
- What are the potential biases that might be introduced by the LLM used for verbalization?

### Rating

3

### Confidence

4

**********
