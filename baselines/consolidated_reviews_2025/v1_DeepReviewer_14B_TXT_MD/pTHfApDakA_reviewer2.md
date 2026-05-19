### Summary

The paper proposes a new method for LLMs to check their own reasoning. The method breaks down the verification of an answer into several stages: extract the goal of the current reasoning step, identify the information needed for this step, generate an alternative answer, and compare the alternative with the original answer. The paper shows that this method improves the accuracy of final answers on three datasets of mathematical problems.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The paper tackles a timely and important problem of how to check the answers of LLMs. The proposed method is intuitive and described in detail. The paper shows that the proposed method improves the accuracy of answers compared to several baselines.

### Weaknesses

#### Some Related Works


#### comment

I have several questions about the proposed method and the experimental results, which are outlined below.

1. The proposed method requires the answer to be provided in the form of several reasoning steps. This limits the applicability of the method, as not all LLMs provide multi-step reasoning. For instance, many models are optimized for direct answer generation, and forcing a multi-step format could introduce unnecessary complexity and potential errors. The method's reliance on this specific output format is a significant constraint.

2. The proposed method requires several calls to the LLM for each question. This is much more computationally expensive than simpler baselines, such as self-consistency. The paper does not provide a detailed analysis of the computational cost, making it difficult to assess the practical trade-offs between accuracy gains and increased resource consumption. The lack of such analysis is a notable weakness.

3. The experimental results do not show how the accuracy of each of the stages of the proposed method is. It would be helpful to see how often each stage succeeds and how they contribute to the final answer. Without this breakdown, it's hard to pinpoint the strengths and weaknesses of the proposed method and understand where improvements could be made. For example, is the goal extraction stage accurate, or does the majority of the error come from the alternative answer generation?

4. The experimental results show that the proposed method improves the accuracy of answers. However, it is not clear whether this improvement comes from the proposed method catching the errors of the LLM or helping the LLM generate better answers. It would be helpful to see the accuracy of the LLM with and without the proposed method on questions where the LLM generates the same answer with and without the proposed method. This analysis is crucial to understand the true impact of the method.

5. The paper does not explain how the final answer is extracted from the multi-step answers of the LLMs. For example, how is the answer extracted from the answer of GPT-3.5 in Table 1? The lack of clarity on this process makes it difficult to reproduce the results and assess the method's overall effectiveness.

### Suggestions

The paper presents an interesting approach to verifying LLM reasoning, but several aspects need further clarification and analysis. First, the method's dependence on multi-step reasoning limits its applicability. The authors should explore ways to adapt their method to models that primarily generate direct answers. This could involve incorporating a step that encourages models to produce intermediate reasoning steps, or developing a separate verification process for direct answers. Additionally, the paper should include a more detailed analysis of the computational cost of the proposed method. This should include a breakdown of the number of API calls, the time taken for each stage, and the overall resource consumption. A comparison with other verification methods, such as self-consistency, should be provided to contextualize the computational overhead. This analysis is crucial for assessing the practical viability of the method.

Second, the paper needs a more granular analysis of the performance of each stage of the proposed method. The authors should provide accuracy metrics for each stage, such as the goal extraction, information identification, alternative answer generation, and comparison stages. This would help identify bottlenecks and areas for improvement. For example, if the goal extraction stage is frequently inaccurate, it would be a key area to focus on. Furthermore, the paper should investigate whether the proposed method is primarily correcting errors or improving the LLM's reasoning process. This could be done by comparing the accuracy of the LLM with and without the proposed method on questions where the LLM generates the same answer in both cases. This analysis would help determine if the method is simply a post-hoc error correction mechanism or if it actively guides the LLM towards better reasoning. The paper should also clarify how the final answer is extracted from the multi-step reasoning. The authors should provide a clear description of the extraction process and include examples to illustrate how the final answer is derived from the generated reasoning steps. This is essential for reproducibility and for understanding the method's overall effectiveness.

Finally, the paper should include a more detailed discussion of the limitations of the proposed method. This should include a discussion of the types of errors that the method is not able to catch, and the potential for the method to introduce new errors. The authors should also discuss the generalizability of the method to other types of problems and datasets. This discussion would help to provide a more balanced and nuanced view of the method's strengths and weaknesses. By addressing these points, the paper can be significantly strengthened and its contributions more clearly articulated.

### Questions

1. The proposed method requires the answer to be provided in the form of several reasoning steps. This limits the applicability of the method, as not all LLMs provide multi-step reasoning.

2. The proposed method requires several calls to the LLM for each question. This is much more computationally expensive than simpler baselines, such as self-consistency.

3. The experimental results do not show how the accuracy of each of the stages of the proposed method is. It would be helpful to see how often each stage succeeds and how they contribute to the final answer.

4. The experimental results show that the proposed method improves the accuracy of answers. However, it is not clear whether this improvement comes from the proposed method catching the errors of the LLM or helping the LLM generate better answers. It would be helpful to see the accuracy of the LLM with and without the proposed method on questions where the LLM generates the same answer with and without the proposed method.

5. The paper does not explain how the final answer is extracted from the multi-step answers of the LLMs. For example, how is the answer extracted from the answer of GPT-3.5 in Table 1?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
