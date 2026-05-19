### Summary

This paper proposes a new unsupervised evaluation method for large language models (LLMs) that leverages a peer-review mechanism. The approach, called PiCO, allows LLMs to evaluate each other’s responses to unlabeled questions, with each model’s evaluation weighted by a learnable capability parameter. The goal is to optimize the consistency between a model’s evaluation capability and the scores it receives, thereby ranking models in a way that aligns with human preferences. The authors validate PiCO on three datasets (Chatbot Arena, MT-Bench, and AlpacaEval) using three metrics (PEN, CIN, and LIS) to measure alignment with human rankings. The results show that PiCO outperforms several baseline methods, suggesting its effectiveness as an unsupervised evaluation approach.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces an innovative unsupervised evaluation method that leverages peer review among LLMs, reducing reliance on human annotations.
2. The authors propose three new metrics (PEN, CIN, LIS) to quantify the alignment between model rankings and human preferences, providing a robust evaluation framework.
3. The paper includes a comprehensive experimental evaluation on multiple datasets, demonstrating the effectiveness of PiCO compared to baseline methods.

### Weaknesses

#### Some Related Works


#### comment

1. The paper assumes that high-level LLMs can provide more accurate evaluations, but it lacks a thorough analysis of the correlation between model size and evaluation accuracy. It is unclear if larger models consistently perform better as reviewers, or if other factors (e.g., training data, architecture) play a more significant role. The paper should include experiments that directly assess the relationship between model size and the quality of its reviews, perhaps by comparing models of varying sizes within the same family.
2. The paper does not discuss the computational cost of PiCO, which could be significant given the need for multiple models to evaluate each other’s responses. The paper should provide a detailed analysis of the computational resources required, including the number of forward passes, the memory footprint, and the overall time complexity. This analysis should also consider the impact of the number of models and the size of the dataset on the computational cost.
3. The paper does not analyze the sensitivity of PiCO to the choice of hyperparameters, such as the number of reviewers or the number of questions used. The paper should include a sensitivity analysis to show how these hyperparameters affect the performance of PiCO. For example, the paper should explore how the ranking changes when using different numbers of reviewers or when the number of questions is varied.
4. The paper does not compare PiCO with other unsupervised evaluation methods, such as self-evaluation or multi-agent debate. The paper should include a comparison with these methods to demonstrate the unique advantages of PiCO. Specifically, the paper should compare PiCO with methods that also use LLMs for evaluation, and discuss the differences in their approaches and performance.
5. The paper does not discuss the limitations of PiCO, such as potential biases in the peer-review process or scenarios where the method might fail. The paper should discuss potential failure modes, such as when the models have similar capabilities or when the questions are too difficult or too easy. The paper should also discuss the potential for bias in the peer-review process, such as models favoring responses that are similar to their own.

### Suggestions

The paper should include a more detailed analysis of the relationship between model size and evaluation accuracy. This could involve experiments with models of varying sizes within the same family, controlling for other factors such as training data and architecture. The analysis should not only focus on the correlation between model size and evaluation accuracy but also explore the conditions under which larger models provide more reliable reviews. For example, it would be beneficial to examine if the advantage of larger models diminishes when the evaluation task is relatively simple or when the models being evaluated are already highly capable. Furthermore, the paper should investigate whether specific architectural features or training techniques contribute to better evaluation capabilities, independent of model size. This would provide a more nuanced understanding of what makes a good reviewer model.

To address the computational cost concerns, the paper should provide a detailed analysis of the time and memory requirements of PiCO. This analysis should include a breakdown of the computational resources required for each step of the process, such as generating responses, performing evaluations, and optimizing the model weights. The paper should also explore techniques to reduce the computational cost, such as using smaller models for evaluation or employing more efficient evaluation methods. It would be beneficial to compare the computational cost of PiCO with other evaluation methods, such as human evaluation and self-evaluation, to provide a more comprehensive understanding of its practicality. Additionally, the paper should discuss the scalability of PiCO to larger model pools and more complex evaluation tasks, and provide guidelines for selecting the appropriate number of models and questions for different scenarios.

The paper should also include a more thorough analysis of the sensitivity of PiCO to its hyperparameters. This should involve experiments that systematically vary the number of reviewers, the number of questions, and the initialization of model capabilities. The paper should explore how these hyperparameters affect the stability and convergence of the optimization process, as well as the final ranking of the models. It would be beneficial to provide guidelines for selecting the optimal hyperparameters for different evaluation tasks, based on the characteristics of the dataset and the available computational resources. Furthermore, the paper should investigate the impact of different initialization strategies for the model capabilities, and explore whether adaptive hyperparameter tuning techniques can improve the performance of PiCO. Finally, the paper should compare PiCO with other unsupervised evaluation methods, such as self-evaluation and multi-agent debate, to highlight its unique advantages and limitations.

### Questions

1. How does the performance of PiCO vary with the number of LLMs in the pool?
2. What is the computational cost of PiCO compared to other evaluation methods?
3. How does PiCO handle situations where the models have similar capabilities?
4. What is the impact of different initialization strategies for model capabilities?
5. How does PiCO compare with other unsupervised evaluation methods, such as self-evaluation or multi-agent debate?

### Rating

6

### Confidence

4

**********
