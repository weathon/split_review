### Summary

This paper proposes a new approach to verify the correctness of the reasoning steps in the multi-step reasoning of LLMs. The proposed approach, called self-check, checks each step by first extracting the target of the step, then regenerating an alternative step from the previous steps, and finally comparing the two steps. The results show that the self-check approach can improve the final answer accuracies of LLMs.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The proposed approach is simple and effective.
2. The proposed approach does not need any additional data or external resources.
3. The proposed approach can be applied to different domains.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed approach requires multiple calls to the LLM, which can be computationally expensive and time-consuming.
2. The proposed approach relies on the LLM's ability to extract the target of a given step and generate an alternative solution, which may not always be accurate.
3. The proposed approach is only tested on three datasets, which may not be sufficient to demonstrate its effectiveness on a wide range of multi-step reasoning tasks.

### Suggestions

The paper introduces an interesting self-checking approach for multi-step reasoning in LLMs, but there are several areas where the methodology and evaluation could be strengthened. First, while the simplicity of the approach is a strength, the computational cost of multiple LLM calls needs to be addressed more thoroughly. The paper should include a detailed analysis of the time complexity of the self-checking process, considering the number of steps in the reasoning chain and the overhead of each LLM call. Furthermore, it would be beneficial to explore techniques to reduce the number of LLM calls, such as caching intermediate results or using more efficient prompting strategies. A comparison of the computational cost of the proposed method with other verification techniques would also be valuable. This analysis should include not just the number of LLM calls, but also the actual time taken for each call, and the overall impact on the practical applicability of the method.

Second, the accuracy of the target extraction and alternative solution generation steps is crucial for the effectiveness of the self-checking approach. The paper should provide a more detailed analysis of the error rates in these steps, including examples of common failure modes. It would be useful to investigate the sensitivity of the method to the quality of the extracted target and the generated alternative solution. For example, how does the performance of the method degrade if the extracted target is slightly inaccurate or if the generated alternative solution is not sufficiently different from the original solution? The paper should also explore methods to improve the robustness of these steps, such as using multiple prompts or incorporating error detection mechanisms. A more rigorous analysis of the error propagation through the self-checking process would also be beneficial, to understand how errors in earlier steps can affect the accuracy of later steps.

Finally, the evaluation of the proposed approach is limited by the use of only three datasets. While these datasets are commonly used in the field, they may not be representative of all multi-step reasoning tasks. The paper should consider evaluating the method on a wider range of datasets, including those with more complex reasoning steps or different types of knowledge. It would also be beneficial to compare the performance of the proposed method with other state-of-the-art verification techniques on these additional datasets. This would provide a more comprehensive assessment of the generalizability and effectiveness of the self-checking approach. Furthermore, the paper should explore the impact of different LLMs on the performance of the proposed method, as the quality of the LLM's reasoning capabilities can significantly affect the accuracy of the self-checking process.

### Questions

1. How does the proposed approach perform on tasks that require different types of reasoning steps, such as logical reasoning or common-sense reasoning?
2. How does the proposed approach perform on tasks with different levels of difficulty, such as tasks with many steps or tasks with complex dependencies between steps?
3. How does the proposed approach perform on tasks that require the LLM to use external knowledge or information, such as tasks that require the LLM to use a calculator or a dictionary?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
