### Summary

This paper proposes a method called Delta to mitigate hallucinations in large language models (LLMs) at inference time. The method involves randomly masking portions of the input prompt and contrasting the original and masked outputs to filter out hallucinated content. The authors evaluate the effectiveness of Delta on various question-answering datasets, showing significant improvements in context-dependent tasks.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and effective, achieving notable improvements in question-answering tasks.
3. The authors provide a clear explanation of the method and its underlying motivation.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a thorough discussion of the limitations of the proposed method. For example, the authors do not address how Delta might perform on tasks that require a high degree of creativity or reasoning, or how it might be affected by different types of input data.
2. The authors do not provide a detailed analysis of the computational cost of the proposed method. While they mention that Delta is computationally efficient, they do not provide specific metrics such as inference time or memory usage. This makes it difficult to assess the practical applicability of the method, especially in resource-constrained environments.
3. The paper does not explore the sensitivity of the proposed method to different hyperparameter settings. The authors mention that the method is robust to hyperparameter changes, but they do not provide a systematic analysis of how different values of the masking ratio, logit ratio, and adaptive plausibility threshold affect the performance of Delta. A more detailed analysis of the hyperparameter space would help to identify the optimal settings for different tasks and datasets, and would also provide insights into the robustness of the method.

### Suggestions

The authors should provide a more comprehensive analysis of the limitations of the Delta method. Specifically, they should investigate the performance of Delta on tasks that require higher levels of creativity or reasoning, such as complex problem-solving or creative writing. It would be beneficial to evaluate the method on datasets that specifically test these capabilities, such as those involving multi-hop reasoning or tasks that require generating novel solutions. Furthermore, the authors should discuss how Delta might be affected by different types of input data, such as noisy or ambiguous text, and how the method might be adapted to handle these challenges. A more thorough discussion of these limitations would provide a more balanced view of the method's applicability and potential for future research.

To address the lack of computational cost analysis, the authors should provide a detailed breakdown of the inference time and memory usage of the Delta method. This analysis should include a comparison of the computational overhead introduced by each component of the method, such as the masking, contrastive decoding, and adaptive plausibility constraints. The authors should also report the computational cost for different input sizes and model configurations. This would allow for a more precise understanding of the trade-offs between performance and computational cost, and would help to assess the practical applicability of the method in resource-constrained environments. Additionally, the authors should consider exploring techniques to optimize the computational efficiency of the method, such as using more efficient masking strategies or reducing the number of contrastive decoding steps.

Finally, the authors should conduct a more systematic analysis of the sensitivity of the proposed method to different hyperparameter settings. This analysis should include a detailed investigation of how different values of the masking ratio, logit ratio, and adaptive plausibility threshold affect the performance of Delta. The authors should report the optimal hyperparameter settings for different tasks and datasets, and they should also discuss the robustness of the method to variations in these settings. This analysis should also consider the interaction between different hyperparameters, as this could reveal potential trade-offs or synergies. The authors should also explore the use of automated hyperparameter optimization techniques to identify the optimal settings for different scenarios. This would provide a more complete understanding of the method's behavior and would help to identify the best settings for different applications.

### Questions

1. How does the proposed method perform on tasks that require a high degree of creativity or reasoning? Are there any specific types of tasks where Delta might struggle to mitigate hallucinations effectively?
2. What is the computational cost of the proposed method compared to the baseline model? How does the computational overhead introduced by each component of the method (e.g., masking, contrastive decoding, adaptive plausibility constraints) affect its practical applicability, especially in resource-constrained environments?
3. How sensitive is the proposed method to different hyperparameter settings? Are there specific ranges or values for the masking ratio, logit ratio, and adaptive plausibility threshold that consistently yield optimal performance across different datasets?

### Rating

5

### Confidence

4

**********
