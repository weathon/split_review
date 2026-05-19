### Summary

This paper uses sparse autoencoders (SAEs) to better understand the mechanism behind in-context learning (ICL). The authors identify two types of SAE features: task-execution features and task-detection features. Task-execution features are those that encode the model's knowledge of which task to execute and whose latent vectors causally induce the task zero-shot. Task-detection features are those that activate on instances of a complete task in the training data, specifically on the token that completes the task. The authors use a method called Task Vector Cleaning (TVC) to identify task-execution features and adapt the Sparse Feature Circuits (SFC) methodology to identify task-detection features. The authors conduct experiments on the Gemma-1 2B model to validate their findings.

### Soundness

2

### Presentation

1

### Contribution

2

### Strengths

1. The paper introduces two novel concepts: task-execution features and task-detection features. These features provide a more fine-grained understanding of the mechanisms behind in-context learning.
2. The paper adapts the Sparse Feature Circuits (SFC) methodology to work on the more complex ICL task and the larger Gemma-1 2B model. This adaptation allows the authors to discover and analyze the subgraph of key SAE latents involved in ICL.

### Weaknesses

#### Some Related Works


#### comment

1. The paper is poorly written and lacks clarity. The authors do not provide sufficient background information on the methods they use, such as Task Vector Cleaning (TVC) and Sparse Feature Circuits (SFC). The paper also lacks a clear explanation of the experimental setup and results. For example, the paper does not explain how the authors chose the hyperparameters for their experiments, or how they validated their findings. The description of the SFC adaptation is particularly vague, making it difficult to assess the novelty and rigor of the approach. It's unclear how the authors handle the complexities of applying SFC to a larger model and a more complex task like ICL, especially given the potential for increased spurious correlations and feature instability.
2. The paper does not provide a clear explanation of the significance of their findings. The authors do not explain how their findings relate to previous work on in-context learning, or how their findings could be used to improve the performance of large language models. The paper also lacks a discussion of the limitations of their approach and potential directions for future research. For instance, it is not clear how the identified features generalize across different tasks or datasets, or whether the identified features are robust to changes in the model architecture or training data. The paper also fails to discuss the computational cost of the proposed methods, which is a critical factor for practical applications.

### Suggestions

The paper needs significant improvements in clarity and technical depth. First, the authors should provide a more detailed explanation of the Task Vector Cleaning (TVC) and Sparse Feature Circuits (SFC) methods. For TVC, they should explain the optimization process, the objective function, and how it differs from existing methods. For SFC, they should clearly describe the modifications they made to adapt it to the ICL task and the Gemma-1 2B model. This should include a discussion of the specific challenges they encountered and how they addressed them. For example, how did they handle the increased dimensionality and complexity of the feature space? What specific criteria did they use to define a 'circuit' in the context of ICL? The authors should also provide a more detailed explanation of their experimental setup, including the specific datasets used, the hyperparameter settings, and the evaluation metrics. They should justify their choices and provide a sensitivity analysis of the hyperparameters. Furthermore, the authors should provide a more thorough analysis of their results, including statistical significance tests and visualizations. They should also discuss the limitations of their approach and potential directions for future research. For example, how do the identified features generalize to other models and tasks? How robust are the features to adversarial attacks or perturbations? What are the computational costs of the proposed methods? Addressing these points would significantly improve the paper's rigor and impact.

Second, the authors need to better contextualize their findings within the existing literature on in-context learning. They should discuss how their identified task-execution and task-detection features relate to previously proposed mechanisms for ICL, such as task vectors or attention-based mechanisms. They should also discuss how their findings could be used to improve the performance of large language models. For example, could the identified features be used to develop more efficient or robust ICL methods? Could they be used to diagnose or mitigate failure modes in ICL? The authors should also discuss the potential ethical implications of their work, such as the potential for misuse of ICL or the development of more powerful AI systems. A more thorough discussion of these points would make the paper more relevant and impactful.

Finally, the authors should provide more concrete examples and visualizations to illustrate their findings. For example, they could provide visualizations of the task-execution and task-detection features, or they could provide examples of how these features are used in specific ICL tasks. They could also provide a case study of how their methods could be used to improve the performance of a specific LLM. These concrete examples would make the paper more accessible and easier to understand. The authors should also consider releasing their code and data to facilitate reproducibility and further research.

### Questions

1. Can the authors provide more details on the Task Vector Cleaning (TVC) and Sparse Feature Circuits (SFC) methods? How do these methods work, and what are their limitations?
2. How do the authors validate their findings? What metrics do they use to evaluate the performance of their methods, and how do they ensure the robustness of their results?
3. How do the authors' findings relate to previous work on in-context learning? What are the novel contributions of this paper, and how do they advance our understanding of in-context learning?
4. How do the authors' findings relate to other related concepts, such as task vectors or attention-based mechanisms? Do the authors' findings support or contradict previous work on these concepts?
5. How do the authors' findings relate to the broader field of mechanistic interpretability? Do the authors' findings provide new insights into the mechanisms of large language models, or do they simply confirm existing knowledge?

### Rating

3

### Confidence

3

**********
