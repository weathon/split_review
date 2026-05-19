### Summary

This paper proposes a cost-efficient method for using LLMs to perform reasoning tasks. The proposed method is based on the idea of LLM cascades, where a weaker LLM is used to answer easy questions and a stronger LLM is used to answer hard questions. The proposed method uses answer consistency as a signal of question difficulty and proposes several methods for answer sampling and consistency checking, including one that leverages a mixture of two thought representations (i.e., Chain-of-Thought and Program-of-Thought). The proposed method is evaluated on six reasoning benchmark datasets, and the results show that it can achieve performance comparable to using solely the stronger LLM but requires only 40% of its cost.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The proposed method is simple and effective. The idea of using answer consistency as a signal of question difficulty is intuitive and makes sense.
- The proposed method is evaluated on six reasoning benchmark datasets, and the results show that it can achieve performance comparable to using solely the stronger LLM but requires only 40% of its cost. This is a significant improvement in cost efficiency.
- The proposed method is compared to other baselines, including using only the weaker LLM or only the stronger LLM, and the results show that it outperforms them in terms of cost and accuracy.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed method relies on the assumption that the weaker LLM is consistently incorrect on certain hard questions. This may not always be true in practice. In such cases, the proposed method may route queries to the stronger LLM unnecessarily, leading to incorrect decisions.
- The authors use GPT-3.5-turbo and GPT-4 as the weaker and stronger LLMs, respectively. However, the gap between these two models is too large. It would be interesting to see how the proposed method performs when the stronger and weaker LLMs are more comparable.

### Suggestions

The paper's core idea of using a weaker LLM for simpler questions and a stronger LLM for more complex ones is promising for cost reduction. However, the current implementation relies heavily on the assumption that the weaker model will consistently fail on hard questions. This assumption needs further scrutiny. A more robust approach would involve a more nuanced method for determining question difficulty, perhaps by incorporating a measure of the weaker model's confidence in its answer, rather than relying solely on consistency. For example, the entropy of the probability distribution over possible answers could be used as a proxy for uncertainty, which might be a better indicator of when to escalate to the stronger model. Additionally, the paper should explore the impact of different consistency thresholds on the overall performance and cost. A sensitivity analysis of this threshold would be beneficial to understand the trade-offs between accuracy and cost.

Furthermore, the choice of GPT-3.5-turbo and GPT-4 as the weaker and stronger models, respectively, introduces a significant performance gap that might not be representative of real-world scenarios where the choice of models is often constrained by availability or cost. It would be valuable to evaluate the proposed method with a more comparable set of models, such as different versions of the same model family or open-source models with varying capabilities. This would provide a more realistic assessment of the method's effectiveness and its potential for practical application. The paper should also consider the impact of different prompt engineering techniques on the performance of both the weaker and stronger models, as this can significantly affect the overall results. A more thorough investigation of these factors would strengthen the paper's claims and increase its practical relevance.

Finally, the paper should explore the potential for adaptive routing strategies. Instead of a fixed threshold for consistency, the system could dynamically adjust the threshold based on the observed performance of the weaker model. For example, if the weaker model is performing well on a particular type of question, the threshold could be increased to further reduce costs. Conversely, if the weaker model is struggling, the threshold could be decreased to ensure accuracy. This adaptive approach could lead to further cost savings and improved performance. The paper should also consider the computational overhead of the consistency checking process and how it impacts the overall cost of the proposed method. A detailed analysis of these factors would provide a more complete picture of the method's practical implications.

### Questions

- How does the proposed method perform when the weaker LLM is not consistently incorrect on certain hard questions?
- How does the proposed method perform when the stronger and weaker LLMs are more comparable?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
