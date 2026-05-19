### Summary

The paper proposes PiCO, an evaluation method for large language models (LLMs) that leverages peer review among models themselves. In this approach, multiple LLMs (both open-source and closed-source) respond to the same set of unlabeled questions. They then evaluate each other's responses, with each model assigned a learnable capability parameter that influences the weight of its evaluation. The goal is to optimize the consistency between a model's capability score and the scores it receives from peer reviews. The method operates without human feedback, aiming to rank models in a way that aligns with human preferences. The authors validate PiCO on three datasets: Chatbot Arena, MT-Bench, and AlpacaEval, using three metrics (PEN, CIN, LIS) to measure alignment with human rankings.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

- The paper proposes an unsupervised approach to evaluate LLMs without human feedback. This is an interesting direction, as it could reduce the cost and time associated with human-in-the-loop evaluation.
- The paper introduces three new metrics (PEN, CIN, LIS) to measure the gap between model rankings and human preferences. These metrics provide a way to quantify the effectiveness of the proposed evaluation method.
- The paper presents a comprehensive experimental evaluation on three datasets, comparing PiCO with several baseline methods. The results show that PiCO outperforms baselines in most cases, suggesting the effectiveness of the proposed approach.

### Weaknesses

#### Some Related Works


#### comment

 - The paper assumes that "high-level" LLMs can provide more accurate evaluations of other models' responses. However, the paper does not provide sufficient evidence or analysis to support this claim. It is unclear whether larger models necessarily possess better evaluation capabilities, especially given the lack of analysis on the correlation between model size and evaluation accuracy. The paper should include a more rigorous analysis of whether larger models consistently provide better evaluations, or if other factors are at play.
- The paper does not discuss the computational cost of PiCO. The method requires each model to respond to questions and evaluate the responses of other models, which can be computationally expensive, especially when dealing with a large number of models or complex questions. The paper should include a detailed analysis of the computational resources required by PiCO, including the time and memory costs associated with both the response generation and the peer review process. This analysis should also consider the scalability of the method to larger model pools.
- The paper does not analyze the sensitivity of PiCO to the choice of hyperparameters. For example, the number of reviewers, the number of questions, and the initialization of model capabilities could affect the results. The paper should include a sensitivity analysis to show how these hyperparameters affect the performance of PiCO. Specifically, the impact of varying the number of reviewer models, the diversity of questions, and the initial capability scores should be explored to understand the robustness of the method.
- The paper does not compare PiCO with other unsupervised evaluation methods, such as self-evaluation or multi-agent debate. It is unclear how PiCO differs from or improves upon these existing methods. The paper should include a comparison with these methods to demonstrate the unique advantages of PiCO. A detailed comparison with methods like self-evaluation and multi-agent debate is necessary to highlight the specific contributions of PiCO.
- The paper does not discuss the limitations of PiCO. For example, the method may not work well if the models have similar capabilities or if the questions are too difficult or too easy. The paper should discuss the potential failure modes of PiCO, particularly in scenarios where model capabilities are closely clustered or when the difficulty of the evaluation questions is not well-matched to the models' capabilities. This discussion should include an analysis of how these factors might affect the reliability of the evaluation results.

### Suggestions

The paper should provide a more detailed analysis of the correlation between model size and evaluation accuracy. While the paper assumes that larger models are better evaluators, this assumption needs to be empirically validated. The authors should conduct experiments to determine if there is a strong positive correlation between model size and the accuracy of evaluations. This analysis should include models of varying sizes and should control for other factors that might influence evaluation performance. Furthermore, the paper should explore whether the evaluation capabilities of larger models are due to their size or other factors, such as training data or architecture. This analysis should also consider the possibility that smaller models might be better evaluators in certain scenarios, such as when the evaluation task requires specific knowledge or when the questions are relatively simple. The paper should also investigate the impact of different training strategies on the evaluation capabilities of the models.

To address the computational cost concerns, the paper should include a detailed analysis of the time and memory requirements of PiCO. This analysis should consider the number of models, the number of questions, and the complexity of the questions. The authors should also explore techniques to reduce the computational cost of PiCO, such as using smaller models for evaluation or using more efficient evaluation methods. The paper should also discuss the scalability of PiCO to larger model pools and more complex evaluation tasks. This discussion should include an analysis of the trade-offs between computational cost and evaluation accuracy. Furthermore, the paper should provide a comparison of the computational cost of PiCO with other evaluation methods, such as human evaluation and self-evaluation. This comparison should help to determine whether PiCO is a practical alternative to existing evaluation methods.

The paper should also include a sensitivity analysis of the hyperparameters of PiCO. This analysis should explore the impact of varying the number of reviewers, the number of questions, and the initialization of model capabilities. The authors should also investigate the impact of different initialization strategies for the model capabilities. The paper should also discuss the optimal choice of hyperparameters for different evaluation tasks. This discussion should include an analysis of the trade-offs between evaluation accuracy and computational cost. Furthermore, the paper should provide guidelines for selecting the hyperparameters of PiCO based on the characteristics of the evaluation task and the available computational resources. The paper should also explore the use of adaptive hyperparameter tuning techniques to optimize the performance of PiCO.

### Questions

- How does the performance of PiCO vary with the number of LLMs in the pool?
- What is the computational cost of PiCO compared to other evaluation methods?
- How does PiCO handle situations where the models have similar capabilities?
- What is the impact of different initialization strategies for model capabilities?
- How does PiCO compare with other unsupervised evaluation methods, such as self-evaluation or multi-agent debate?

### Rating

5

### Confidence

4

**********
