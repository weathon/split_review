### Summary

This paper proposes a self-checking method to verify the correctness of the reasoning steps of large language models (LLMs) in solving mathematical problems. The method consists of four stages: target extraction, information collection, step regeneration, and result integration. The authors use the results of this checking to perform weighted voting over multiple solutions to improve the final answer accuracy. Experimental results on three datasets (GSM8K, MathQA, and MATH) demonstrate that the proposed method achieves higher final answer accuracy compared to baseline methods. The authors also provide an analysis of the method's effectiveness in filtering out incorrect solutions and its robustness to different levels of confidence thresholds.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The proposed method is simple and easy to implement, requiring no additional training data or external resources.
2. The method is effective in improving the final answer accuracy of LLMs on mathematical reasoning tasks.
3. The authors provide a comprehensive analysis of the method's performance, including ablation studies and comparisons with baseline methods.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method relies on the LLM's ability to extract the target of a given step and generate an alternative solution independently, which may not always be accurate. The authors do not provide a detailed analysis of the error cases or the types of reasoning steps where the method struggles.
2. The method requires multiple calls to the LLM, which can be computationally expensive and time-consuming, especially for complex reasoning tasks. The authors do not discuss the computational cost of the method or its scalability to larger datasets.
3. The method is only evaluated on mathematical reasoning tasks, and it is unclear how well it would generalize to other types of reasoning tasks, such as logical or commonsense reasoning.

### Suggestions

The authors should provide a more detailed analysis of the error cases where the self-checking method fails. This analysis should include examples of specific reasoning steps where the LLM struggles to extract the target or generate an alternative solution. For instance, are there specific types of mathematical operations or logical inferences that are more prone to errors? A breakdown of the error types (e.g., arithmetic errors, logical fallacies, misinterpretations of the question) would be beneficial. Furthermore, the authors should investigate the impact of different prompting strategies on the accuracy of the target extraction and alternative solution generation steps. It would be useful to explore whether providing more explicit instructions or examples could improve the reliability of the self-checking process. This analysis should also consider the confidence scores assigned to each step, and how these scores correlate with the correctness of the final answer. Understanding the relationship between confidence and accuracy would help in setting appropriate thresholds for filtering out incorrect solutions.

To address the computational cost concerns, the authors should provide a more detailed analysis of the time complexity of their method. This analysis should include the number of LLM calls required for each step of the self-checking process, as well as the average time taken for each call. The authors should also discuss the scalability of their method to larger datasets and more complex reasoning tasks. For example, how does the computational cost scale with the number of reasoning steps or the size of the input? It would be beneficial to compare the computational cost of their method with other verification techniques. Furthermore, the authors should explore potential optimizations to reduce the computational overhead, such as caching intermediate results or using more efficient prompting strategies. This would make the method more practical for real-world applications.

Finally, the authors should evaluate their method on a broader range of reasoning tasks beyond mathematical reasoning. This would help to assess the generalizability of their approach and identify its limitations. For example, how well does the method perform on logical reasoning tasks, such as those found in the CommonSenseQA dataset, or commonsense reasoning tasks, such as those found in the SocialIQA dataset? The authors should also consider the impact of different types of reasoning steps on the performance of their method. Are there certain types of reasoning steps that are more difficult to verify than others? A more comprehensive evaluation would provide a better understanding of the strengths and weaknesses of the proposed method and guide future research in this area.

### Questions

1. How does the method perform on tasks that require different types of reasoning steps, such as logical reasoning or common-sense reasoning?
2. How does the method perform on tasks with different levels of difficulty, such as tasks with many steps or tasks with complex dependencies between steps?
3. How does the method perform on tasks that require the LLM to use external knowledge or information, such as tasks that require the LLM to use a calculator or a dictionary?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
