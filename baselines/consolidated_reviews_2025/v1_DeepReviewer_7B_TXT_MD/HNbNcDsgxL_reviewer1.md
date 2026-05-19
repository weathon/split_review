### Summary

This paper proposes a contrastive decoding method, Delta, to mitigate hallucinations in LLMs. The authors argue that hallucinations are often caused by the model's reliance on contextual cues, and they propose a method that randomly masks portions of the input prompt to generate outputs that are more likely to be filled with hallucinated content. By subtracting the hallucinated logits from the original logits, Delta extracts the "clean" logits—those less influenced by hallucinated content. This process reduces the likelihood of hallucinations, as demonstrated in question-answering tasks, where Delta achieved notable improvements.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper is well-structured and easy to follow, with clear explanations of the proposed method and its underlying motivation. The authors provide a detailed description of the Delta method, including the use of masking, contrastive decoding, and adaptive plausibility constraints. The motivation for addressing hallucinations in LLMs is well-articulated, emphasizing the importance of reliable and trustworthy outputs in real-world applications.

2. The authors conduct experiments on a variety of question-answering datasets, including SQuAD v1.1, v2, TriviaQA, and Natural Questions. The results show that Delta outperforms the baseline model in terms of accuracy and F1 score, particularly in context-rich datasets. The authors also compare Delta with other methods, such as Visual Contrastive Decoding (VCD) and Instruction Contrastive Decoding (ICD), demonstrating the effectiveness of their approach.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a thorough discussion of the limitations of the proposed method. For example, the authors do not address how Delta might perform on tasks that require a high degree of creativity or reasoning, or how it might be affected by different types of input data. Specifically, the paper does not explore the impact of Delta on tasks that require multi-hop reasoning or complex inference, which could reveal potential weaknesses in the method's ability to mitigate hallucinations in more complex scenarios. Furthermore, the paper does not discuss the potential for the method to introduce new types of errors or biases, which is crucial for a comprehensive evaluation.

2. The authors do not provide a detailed analysis of the computational cost of the proposed method. While they mention that Delta is computationally efficient, they do not provide specific metrics such as inference time or memory usage. This makes it difficult to assess the practical applicability of the method, especially in resource-constrained environments. The paper should include a breakdown of the computational overhead introduced by each component of the method, such as the masking, contrastive decoding, and adaptive plausibility constraints. This would allow for a more precise understanding of the trade-offs between performance and computational cost.

3. The paper does not explore the sensitivity of the proposed method to different hyperparameter settings. The authors mention that the method is robust to hyperparameter changes, but they do not provide a systematic analysis of how different values of the masking ratio, logit ratio, and adaptive plausibility threshold affect the performance of Delta. A more detailed analysis of the hyperparameter space would help to identify the optimal settings for different tasks and datasets, and would also provide insights into the robustness of the method.

### Suggestions

To address the lack of discussion on limitations, the authors should include a more thorough analysis of the method's performance on tasks that require higher levels of creativity and reasoning. This could involve evaluating Delta on datasets that specifically test these capabilities, such as those involving complex multi-hop reasoning or tasks that require generating novel solutions. The authors should also investigate how Delta performs on tasks with varying levels of contextual complexity, as this could reveal potential limitations in its ability to filter out hallucinations in different scenarios. Furthermore, the paper should include a discussion of potential biases that may be introduced by the method, and how these biases could be mitigated. This would provide a more balanced and comprehensive evaluation of the proposed approach.

To address the lack of computational cost analysis, the authors should provide a detailed breakdown of the inference time and memory usage of the Delta method. This should include a comparison of the computational overhead introduced by each component of the method, such as the masking, contrastive decoding, and adaptive plausibility constraints. The authors should also report the computational cost for different input sizes and model configurations. This would allow for a more precise understanding of the trade-offs between performance and computational cost, and would help to assess the practical applicability of the method in resource-constrained environments. The analysis should also consider the impact of different hardware configurations on the computational cost of the method.

Finally, the authors should conduct a more systematic analysis of the sensitivity of the proposed method to different hyperparameter settings. This should include a detailed investigation of how different values of the masking ratio, logit ratio, and adaptive plausibility threshold affect the performance of Delta. The authors should report the optimal hyperparameter settings for different tasks and datasets, and they should also discuss the robustness of the method to variations in these settings. This analysis should also consider the interaction between different hyperparameters, as this could reveal potential trade-offs or synergies. The authors should also explore the use of automated hyperparameter optimization techniques to identify the optimal settings for different scenarios.

### Questions

1. How does the proposed method perform on tasks that require a high degree of creativity or reasoning? Are there any specific types of tasks where Delta might struggle to mitigate hallucinations effectively?

2. What is the computational cost of the proposed method compared to the baseline model? How does the computational overhead introduced by each component of the method (e.g., masking, contrastive decoding, adaptive plausibility constraints) affect its practical applicability, especially in resource-constrained environments?

3. How sensitive is the proposed method to different hyperparameter settings? Are there specific ranges or values for the masking ratio, logit ratio, and adaptive plausibility threshold that consistently yield optimal performance across different datasets?

### Rating

3

### Confidence

4

**********
