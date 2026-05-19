### Summary

This paper proposes a cascade approach for reasoning tasks, which uses a weaker LLM to solve easy questions and a stronger LLM to solve hard questions. The authors propose two methods to detect whether the weaker LLM can answer a question correctly. The experimental results demonstrate the effectiveness of the proposed approach.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed framework is simple and effective.

### Weaknesses

#### Some Related Works


#### comment

1. The novelty is limited. The idea of using a weaker LLM to solve easy tasks and a stronger LLM to solve difficult tasks is not new. The authors should compare their method with existing methods, such as the one in "Self-Consistency rectifies itself". The paper lacks a thorough comparison with existing methods, particularly those that also leverage consistency for routing decisions. The authors should clarify how their approach differs in terms of both methodology and performance, especially considering that the core idea of using consistency to determine when to invoke a stronger model is already present in prior work. A more detailed analysis of the differences in the consistency mechanisms and their impact on the final performance is needed.
2. The authors only compare the cost of using only the stronger LLM and their proposed method. It is better to also compare the cost of using only the cheaper LLM. The paper should include a comparison with a baseline that uses the cheaper LLM for all tasks. This is crucial for understanding the trade-offs between cost and performance. The authors need to demonstrate that their method provides a better cost-performance trade-off than simply using the cheaper LLM, even if it means sacrificing some accuracy. This comparison is essential for evaluating the practical utility of the proposed approach.
3. The authors only evaluate the performance of their proposed method on reasoning datasets. It would be better to also evaluate the performance on other tasks, such as translation. The evaluation is limited to reasoning tasks, which may not fully capture the general applicability of the proposed method. The authors should evaluate their method on a more diverse set of tasks, including tasks that require different types of reasoning or knowledge, such as translation or summarization. This would provide a more comprehensive assessment of the method's strengths and weaknesses.

### Suggestions

The paper would benefit significantly from a more rigorous comparison with existing methods that utilize consistency for routing decisions. Specifically, the authors should implement and compare their approach against methods like "Self-Consistency rectifies itself" and analyze the differences in the consistency mechanisms used. This comparison should not only focus on the final performance but also on the computational cost and the number of LLM calls required. A detailed analysis of how the proposed method's consistency measure differs from existing methods and how these differences impact the routing decisions and overall performance is crucial. The authors should also discuss the limitations of their approach in comparison to these existing methods, highlighting the scenarios where their method performs better or worse. This would provide a more nuanced understanding of the contribution of their work.

To address the lack of comparison with a baseline using only the cheaper LLM, the authors should include experiments that evaluate the performance of the cheaper LLM across all tasks. This would allow for a direct comparison of the cost-performance trade-off between the proposed method and the cheaper LLM. The authors should also analyze the cases where the proposed method performs worse than the cheaper LLM and discuss the reasons for these performance differences. This analysis should include a discussion of the types of tasks where the proposed method is most effective and the types of tasks where it is less effective. Furthermore, the authors should explore the possibility of using the cheaper LLM for tasks where it performs well and the more expensive LLM for tasks where it excels, potentially leading to a more cost-effective and accurate system. This would provide a more comprehensive understanding of the practical utility of the proposed approach.

Finally, the evaluation of the proposed method should be expanded to include a more diverse set of tasks beyond reasoning. This could include tasks such as translation, summarization, or question answering on different domains. This would provide a more comprehensive assessment of the method's general applicability and robustness. The authors should also analyze the performance of their method on tasks that require different types of reasoning or knowledge. This analysis should include a discussion of the types of tasks where the proposed method performs well and the types of tasks where it is less effective. This would provide a more complete picture of the strengths and weaknesses of the proposed method and its potential for real-world applications.

### Questions

Please refer to the Weaknesses.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
