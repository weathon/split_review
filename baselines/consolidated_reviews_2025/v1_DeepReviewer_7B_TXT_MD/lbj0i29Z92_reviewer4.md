### Summary

This paper introduces Meta-Rewarding, a method to improve the ability of large language models (LLMs) to judge their own responses. The method involves three main steps: generating multiple responses, evaluating these responses with a judge model, and selecting the best and worst responses for further training. The authors demonstrate that this approach leads to significant improvements in the model's ability to follow instructions and judge the quality of responses.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow. The authors clearly explain the motivation, methodology, and results of their work.
2. The proposed method is novel and addresses a critical limitation in current LLMs, which is the lack of self-improvement in judgment abilities. The use of a meta-judge to evaluate the judge's own judgments is a creative and effective way to improve the model's judgment skills.
3. The experimental results are compelling and demonstrate the effectiveness of the proposed method. The authors evaluate their approach on multiple benchmarks, including AlpacaEval 2, Arena-Hard, and MT-Bench, and show significant improvements in both instruction-following and judgment accuracy.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a thorough discussion of the computational cost associated with the proposed method. The authors should provide a detailed analysis of the computational resources required for each step of the Meta-Rewarding process, including the generation of multiple responses, the evaluation with the judge model, and the selection of best and worst responses. This analysis should include the time and memory requirements for each step, as well as the overall computational cost of the method. Furthermore, the authors should compare the computational cost of their method with that of existing approaches, such as Self-Rewarding, to provide a clear understanding of the trade-offs between performance and computational resources. This is particularly important for practical applications where computational resources may be limited.
2. The paper does not provide a detailed analysis of the sensitivity of the method to different hyperparameters. The authors should investigate how the performance of the method varies with different values of key hyperparameters, such as the number of responses generated per prompt, the number of iterations, and the learning rate. This analysis should include a discussion of the optimal values for these hyperparameters and the impact of suboptimal values on the performance of the method. Furthermore, the authors should provide guidelines for selecting appropriate hyperparameters for different tasks and datasets, which would make the method more accessible and practical for a wider range of users.
3. The paper does not explore the potential limitations of the method in handling complex or ambiguous judgments. The authors should investigate how the method performs in scenarios where the judgments are not clear-cut or where there is a high degree of subjectivity. This analysis should include a discussion of the types of judgments that the method struggles with and the potential reasons for these limitations. Furthermore, the authors should explore potential solutions to address these limitations, such as incorporating additional information or using more sophisticated evaluation metrics.

### Suggestions

The authors should provide a more detailed analysis of the computational cost of the Meta-Rewarding method. This analysis should include a breakdown of the time and memory requirements for each step of the process, such as response generation, judge evaluation, and response selection. The authors should also compare the computational cost of their method with that of existing approaches, such as Self-Rewarding, to provide a clear understanding of the trade-offs between performance and computational resources. This comparison should include a discussion of the scalability of the method with respect to the size of the model and the dataset. Furthermore, the authors should explore potential optimizations to reduce the computational cost of the method, such as using more efficient algorithms or parallelizing the computation. This would make the method more practical for real-world applications where computational resources may be limited.

To address the lack of hyperparameter analysis, the authors should conduct a thorough sensitivity analysis of the method to different hyperparameters. This analysis should include a systematic exploration of the impact of key hyperparameters, such as the number of responses generated per prompt, the number of iterations, and the learning rate. The authors should provide a detailed discussion of the optimal values for these hyperparameters and the impact of suboptimal values on the performance of the method. This analysis should also include a discussion of the trade-offs between different hyperparameter settings and the potential reasons for these trade-offs. Furthermore, the authors should provide guidelines for selecting appropriate hyperparameters for different tasks and datasets, which would make the method more accessible and practical for a wider range of users. This could include a discussion of how to choose the number of responses to generate, the number of iterations to perform, and the learning rate for different types of tasks and datasets.

Finally, the authors should investigate the limitations of the method in handling complex or ambiguous judgments. This analysis should include a discussion of the types of judgments that the method struggles with and the potential reasons for these limitations. For example, the authors could explore how the method performs in scenarios where the judgments are not clear-cut or where there is a high degree of subjectivity. The authors should also explore potential solutions to address these limitations, such as incorporating additional information or using more sophisticated evaluation metrics. This could include exploring the use of ensemble methods to combine the judgments of multiple models or using more robust evaluation metrics that are less sensitive to subjectivity. This analysis should also include a discussion of the potential impact of these limitations on the overall performance of the method and the types of tasks and datasets where the method is most likely to struggle.

### Questions

1. How does the computational cost of the Meta-Rewarding method compare to that of the Self-Rewarding method? Could you provide a detailed analysis of the time and memory requirements for each step of the Meta-Rewarding process?
2. What is the sensitivity of the Meta-Rewarding method to different hyperparameters, such as the number of responses generated per prompt, the number of iterations, and the learning rate? Could you provide a detailed analysis of how these hyperparameters affect the performance of the method?
3. How does the Meta-Rewarding method perform in handling complex or ambiguous judgments? Are there any specific scenarios where the method struggles to make accurate judgments? Could you provide a discussion of the potential limitations of the method in these scenarios?

### Rating

6

### Confidence

4

**********
