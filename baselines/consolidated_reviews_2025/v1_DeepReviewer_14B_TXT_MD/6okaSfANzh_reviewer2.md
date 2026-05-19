### Summary

This paper proposes a cost-efficient reasoning framework based on LLM cascades. The authors introduce a routing mechanism that routes queries to stronger (costly) or weaker (budget) LLMs based on the consistency of the latter's answers. They explore various consistency measures, including sampling with different chain-of-thought prompts and program-of-thought prompts. Their experiments demonstrate that their approach achieves comparable accuracy to always using the stronger LLM while significantly reducing costs.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-motivated and tackles a practical problem in the usage of LLMs.
- The proposed method is simple and effective.
- The experiments are comprehensive and thorough.

### Weaknesses

#### Some Related Works


#### comment

 - The proposed method relies on the assumption that the weaker LLM is consistently incorrect on certain hard questions. This may not always be true in practice. In such cases, the proposed method may route queries to the stronger LLM unnecessarily, leading to incorrect decisions. Specifically, the method does not account for scenarios where the weaker LLM might produce correct answers by chance, or when the consistency metric fails to capture the nuances of question difficulty. This could lead to suboptimal routing, where the weaker LLM is used even when it should not be.
- The authors use GPT-3.5-turbo and GPT-4 as the weaker and stronger LLMs, respectively. However, the gap between these two models is too large. It would be interesting to see how the proposed method performs when the stronger and weaker LLMs are more comparable. The current setup might not accurately reflect real-world scenarios where the performance difference between available models is less pronounced. This makes it difficult to generalize the findings to situations where the choice of weaker LLM is more constrained.

### Suggestions

The paper would benefit from a more detailed analysis of the cases where the weaker LLM produces correct answers inconsistently. It would be useful to categorize the types of questions where this occurs and investigate whether specific characteristics of these questions contribute to the inconsistent behavior. For example, are these questions that require a specific type of reasoning, or are they simply edge cases that the weaker LLM struggles with? Furthermore, the authors should explore alternative consistency measures that are more robust to the issue of inconsistent correct answers. One potential approach could be to incorporate a measure of confidence in the weaker LLM's answers, rather than relying solely on consistency. This could involve analyzing the probability distribution of the generated tokens or using other methods to estimate the model's certainty. By combining consistency with confidence, the routing mechanism could make more informed decisions about when to escalate to the stronger LLM.

To address the concern about the large performance gap between GPT-3.5-turbo and GPT-4, the authors should conduct experiments with a more comparable set of LLMs. This could involve using different versions of the same model family or exploring open-source models with varying capabilities. For instance, they could compare the performance of different sizes of the Llama model family, or different versions of the Mistral model. This would provide a more nuanced understanding of how the proposed method performs under different conditions and would make the results more generalizable to real-world scenarios. Additionally, it would be beneficial to analyze the trade-offs between the cost savings achieved by using the weaker LLM and the potential loss in accuracy. This analysis should consider the specific characteristics of the tasks and the available LLMs.

Finally, the authors should investigate the impact of the choice of prompts on the performance of the proposed method. While the paper explores different prompting strategies, it would be valuable to analyze how sensitive the method is to the specific prompts used. For example, how does the performance change when using different chain-of-thought prompts or when varying the number of examples provided in the prompt? This analysis could provide insights into the robustness of the method and could help guide the selection of prompts in practical applications. Furthermore, the authors should explore the possibility of using adaptive prompting techniques, where the prompt is dynamically adjusted based on the characteristics of the input question. This could potentially improve the performance of the weaker LLM and reduce the need for escalation to the stronger LLM.

### Questions

- In the case where the weaker LLM produces correct answers with low consistency and the stronger LLM produces wrong answers with high consistency, how would the proposed method perform? 
- How does the proposed method perform when the stronger and weaker LLMs are more comparable?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
