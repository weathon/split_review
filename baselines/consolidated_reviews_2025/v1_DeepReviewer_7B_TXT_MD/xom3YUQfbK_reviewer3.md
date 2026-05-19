### Summary

The paper introduces the Model Manager framework, designed to facilitate the comparison of machine learning models by generating textual explanations of their differences. This framework leverages Large Language Models (LLMs) to produce natural language descriptions of how different models behave on the same dataset. The authors evaluate the Model Manager on three classification datasets (Blood, Diabetes, and Car) using Logistic Regression, Decision Trees, and K-Nearest Neighbors models. The evaluation focuses on the accuracy of the LLMs in predicting the outputs of one model based on the descriptions of both models and the input data. The results show that the Model Manager framework performs well in verbalizing the differences between Logistic Regression models, with Claude 3.5 Sonnet achieving the best performance. However, the framework faces challenges in comparing Decision Trees and K-NN models. The paper concludes that the Model Manager framework is a promising step toward transparent AI, but further research is needed to address the limitations, especially in handling more complex models and non-parametric methods.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper introduces a novel approach to model comparison by using LLMs to generate natural language explanations of model differences. This framework could be valuable for model selection and debugging in machine learning projects.
2. The authors provide a clear and detailed explanation of the Model Manager framework, including the prompt design and the evaluation methodology. The use of a JSON format for serializing model outputs and input data is a practical approach that enhances the framework's usability.
3. The paper includes a comprehensive evaluation of the Model Manager framework on three classification datasets and three different model types. The results provide insights into the strengths and limitations of the framework, particularly in comparing Logistic Regression models.

### Weaknesses

#### Some Related Works


#### comment

1. The paper's evaluation is limited to classification tasks and relatively simple models. The authors do not explore the applicability of the Model Manager framework to other types of machine learning tasks, such as regression or reinforcement learning. This limitation restricts the generalizability of the findings and raises questions about the framework's effectiveness in more complex scenarios.
2. The paper does not provide a detailed analysis of the computational cost associated with the Model Manager framework. The authors do not discuss the time and resources required to generate the textual explanations, which is an important consideration for practical applications. This lack of analysis makes it difficult to assess the feasibility of using the framework in real-world settings.
3. The paper does not explore the potential biases or limitations of using LLMs for generating textual explanations. The authors do not discuss how the LLM's training data or inherent biases might affect the accuracy and fairness of the generated explanations. This is a critical issue that needs to be addressed to ensure the reliability of the framework.
4. The paper's evaluation metrics are limited to accuracy-based measures. The authors do not explore other metrics, such as precision, recall, or F1-score, which could provide a more comprehensive assessment of the framework's performance. This limited evaluation makes it difficult to fully understand the strengths and weaknesses of the Model Manager framework.

### Suggestions

The authors should extend their evaluation to include regression tasks and more complex models, such as neural networks. This would provide a more comprehensive understanding of the Model Manager framework's applicability and limitations. Specifically, the framework should be tested on regression models like Support Vector Regression (SVR) and Random Forests, as well as on neural networks with varying architectures. This would help to determine whether the framework can effectively compare models across different task types and complexities. Furthermore, the evaluation should include a more diverse set of datasets, including those with higher dimensionality and more complex relationships between features and target variables. This would help to assess the robustness of the framework in more challenging scenarios.

To address the lack of computational cost analysis, the authors should provide a detailed breakdown of the time and resources required to generate the textual explanations. This should include the time taken for each step of the process, such as model serialization, prompt generation, and LLM inference. The authors should also explore the impact of different LLM sizes and prompting strategies on the computational cost. This analysis would help to determine the feasibility of using the framework in real-world settings, where computational resources may be limited. Additionally, the authors should investigate methods for optimizing the framework's performance, such as using more efficient LLMs or reducing the length of the input prompts. This would help to minimize the computational overhead of the framework.

The authors should also conduct a more thorough analysis of the potential biases and limitations of using LLMs for generating textual explanations. This should include an investigation of how the LLM's training data and inherent biases might affect the accuracy and fairness of the generated explanations. The authors should also explore methods for mitigating these biases, such as using debiasing techniques or incorporating fairness constraints into the LLM's training process. Furthermore, the authors should consider the ethical implications of using LLMs to generate explanations, particularly in sensitive domains where model explanations are critical. This would help to ensure the responsible use of the Model Manager framework and its impact on society.

### Questions

1. How does the Model Manager framework handle models with non-linear decision boundaries, such as Support Vector Machines or neural networks? Are there any specific adaptations or modifications needed to apply the framework to these models?
2. What are the computational costs associated with generating textual explanations using the Model Manager framework? How does the framework scale with the size of the model, the number of input features, and the complexity of the dataset?
3. How does the Model Manager framework ensure the fairness and interpretability of the generated textual explanations? Are there any mechanisms in place to mitigate potential biases introduced by the LLM?
4. How does the Model Manager framework handle cases where the models being compared have different architectures or training procedures? Are there any specific strategies or modifications needed to ensure accurate and meaningful comparisons?

### Rating

3

### Confidence

4

**********
