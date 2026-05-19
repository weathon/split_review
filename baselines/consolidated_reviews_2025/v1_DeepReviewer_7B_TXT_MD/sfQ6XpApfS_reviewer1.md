### Summary

The paper proposes a new LLM-as-Judge evaluation method, PiCO, which assigns weights to each LLM and optimizes the weights to maximize the consistency of the LLMs' capabilities and scores. The authors introduce three metrics, PEN, CIN, and LIS, to evaluate the gap with human preferences. The authors conduct experiments on multiple datasets and metrics, demonstrating that the proposed PiCO framework can effectively obtain an LLM leaderboard closer to human preferences.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

The paper proposes a new LLM-as-Judge evaluation method, PiCO, which assigns weights to each LLM and optimizes the weights to maximize the consistency of the LLMs' capabilities and scores. The authors introduce three metrics, PEN, CIN, and LIS, to evaluate the gap with human preferences. The authors conduct experiments on multiple datasets and metrics, demonstrating that the proposed PiCO framework can effectively obtain an LLM leaderboard closer to human preferences.

### Weaknesses

#### Some Related Works


#### comment

1. The paper's novelty is limited, as it primarily combines existing techniques without introducing significant new concepts. The core idea of using consistency as an optimization target is not new, and the specific implementation of PiCO appears to be a straightforward application of this principle. The paper does not adequately demonstrate how PiCO differs fundamentally from other consistency-based evaluation methods.
2. The evaluation lacks a thorough comparison with recent state-of-the-art methods. The paper should include a more comprehensive comparison with other LLM-as-Judge approaches, especially those that also aim to optimize weights or use consistency measures. The current evaluation is insufficient to establish the superiority of PiCO.
3. The paper does not provide sufficient details on the computational cost and scalability of the proposed method. The optimization process, especially with the consistency constraint, could be computationally expensive, especially with a large number of models. The paper needs to quantify the computational resources required and discuss the scalability of PiCO to a larger set of models.
4. The paper's presentation could be improved for better clarity and readability. The description of the PiCO method and the optimization process is somewhat vague, making it difficult to understand the exact implementation details. The paper needs to provide a more detailed and clear explanation of the method.

### Suggestions

The paper needs to more clearly articulate the novelty of the PiCO method. While the idea of using consistency to optimize model weights is not new, the authors should highlight specific aspects of their approach that differentiate it from existing methods. For example, they could discuss how their consistency measure differs from others, or how their optimization algorithm is unique. A more detailed explanation of the theoretical underpinnings of the method would also be beneficial. The authors should also provide a more thorough analysis of the limitations of their approach and discuss potential avenues for future research. This would help to contextualize the contribution of the paper and provide a more balanced perspective on its strengths and weaknesses.

To address the lack of comprehensive evaluation, the authors should include a more extensive comparison with recent state-of-the-art LLM-as-Judge methods. This comparison should not only focus on the final ranking but also on other aspects such as the computational cost, the sensitivity to hyperparameters, and the robustness to different datasets. The authors should also consider using a wider range of evaluation metrics to assess the quality of the ranking. Furthermore, the paper should include a detailed analysis of the results, discussing the reasons for the observed performance differences and highlighting the strengths and weaknesses of PiCO compared to other methods. This would provide a more nuanced understanding of the method's performance and its potential for practical applications.

Finally, the paper needs to provide more details on the computational cost and scalability of the proposed method. The authors should quantify the computational resources required for the optimization process, including the time and memory usage. They should also discuss the scalability of PiCO to a larger set of models and different dataset sizes. This analysis should include a discussion of the potential bottlenecks and limitations of the method. The authors should also consider providing guidelines for practitioners on how to choose the appropriate parameters for their specific use cases. This would make the paper more useful for researchers and practitioners who are interested in applying PiCO to their own work.

### Questions

1. How does the proposed method handle potential biases in the LLMs used for evaluation?
2. Can the method be extended to other types of tasks beyond question answering?
3. What are the computational costs and scalability of the proposed method?

### Rating

3

### Confidence

4

**********
