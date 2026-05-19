### Summary

This paper proposes a cost-efficient reasoning pipeline for LLMs that uses a weaker but cheaper LLM to solve easy questions and a stronger but more expensive LLM to solve hard questions. The authors propose two methods for the answer consistency of the weaker LLM, including a vote-based method and a verification-based method. The authors conduct experiments on six reasoning datasets and show that the proposed method achieves comparable task performance with only 40% of the cost of GPT-4.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and effective, achieving comparable task performance with only 40% of the cost of GPT-4.
3. The authors conduct extensive experiments on six reasoning datasets and provide a thorough analysis of the results.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method relies on the consistency of the weaker LLM's answers, which may not always be reliable. The authors should discuss the limitations of this approach and potential failure cases. Specifically, the paper lacks a discussion on how the method would perform when the weaker LLM consistently makes errors, or when the consistency of the weaker LLM is low due to ambiguous or poorly phrased questions. This could lead to the cascade framework incorrectly routing questions to the weaker LLM, even when the stronger LLM is needed.
2. The authors should compare their method with other cost-efficient reasoning methods, such as prompt engineering or ensemble methods. The paper does not adequately position the proposed method within the broader landscape of cost-efficient reasoning techniques. A comparison with methods that use prompt optimization or ensemble techniques would help to clarify the advantages and disadvantages of the proposed cascade approach. For example, how does the proposed method compare to techniques that dynamically adjust prompts based on the input question, or to ensemble methods that combine the predictions of multiple LLMs?

### Suggestions

The paper should include a more detailed analysis of the failure modes of the proposed method. Specifically, the authors should investigate scenarios where the weaker LLM's consistency is low or unreliable. This could involve analyzing the types of questions that lead to inconsistent answers from the weaker LLM, and how these questions are routed to the stronger LLM. Furthermore, the authors should explore the impact of varying the number of samples used for consistency checking on the overall performance and cost of the cascade framework. It would be beneficial to see a sensitivity analysis of the threshold used for the consistency check, and how this parameter affects the trade-off between cost and accuracy. This analysis should also consider the computational overhead of the consistency check itself, and whether it is worth the cost for different types of questions.

To better position the proposed method, the authors should conduct a more comprehensive comparison with existing cost-efficient reasoning techniques. This should include a comparison with methods that use prompt engineering, such as those that dynamically adjust prompts based on the input question, and methods that use ensemble techniques, such as those that combine the predictions of multiple LLMs. The comparison should not only focus on the overall task performance, but also on the cost-efficiency of each method. For example, the authors should compare the cost of using prompt engineering to optimize prompts for the weaker LLM versus the cost of using the proposed cascade framework. Similarly, the authors should compare the cost of using ensemble methods to combine the predictions of multiple LLMs versus the cost of using the proposed cascade framework. This would provide a more complete picture of the advantages and disadvantages of the proposed method.

Finally, the authors should consider exploring the use of more sophisticated consistency measures. The current approach relies on a simple majority vote or a consistency check based on the output of the weaker LLM. However, there may be more advanced consistency measures that could provide more reliable routing decisions. For example, the authors could explore the use of techniques from the field of uncertainty quantification to estimate the confidence of the weaker LLM's predictions. This could involve using Bayesian methods or other techniques to model the uncertainty of the weaker LLM's predictions. This would allow for more informed routing decisions, and potentially improve the overall performance of the cascade framework.

### Questions

See weaknesses.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
