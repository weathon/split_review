### Summary

This paper proposes a new self-improvement method for LLMs that simultaneously improves the model’s response generation and judgment ability. The method is based on the Self-Rewarding method, which improves the model’s response generation ability by using the model’s own judgments as rewards. This paper extends the Self-Rewarding method by introducing a meta-judge that evaluates the model’s own judgments. The meta-judge provides feedback on the quality of the judgments, allowing the model to improve its judgment ability. The paper conducts experiments on several benchmarks, including AlpacaEval 2, Arena-Hard, and MT-Bench, and shows that the proposed method outperforms the Self-Rewarding method and other baselines.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a new self-improvement method that improves both the model’s response generation and judgment ability. This is a novel contribution that addresses a limitation of existing methods.
2. The paper provides a clear and detailed description of the proposed method, including the meta-judge and the training process. The paper also provides a thorough evaluation of the method on several benchmarks, including AlpacaEval 2, Arena-Hard, and MT-Bench.
3. The paper shows that the proposed method outperforms the Self-Rewarding method and other baselines on several benchmarks, demonstrating the effectiveness of the method.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost of the proposed method. It would be helpful to understand the trade-offs between the performance gains and the computational cost.
2. The paper does not provide a detailed analysis of the limitations of the proposed method. It would be helpful to understand the scenarios where the method may not perform well.
3. The paper does not provide a detailed analysis of the robustness of the proposed method to different hyperparameters. It would be helpful to understand the sensitivity of the method to different hyperparameters.

### Suggestions

The paper introduces an interesting approach by incorporating a meta-judge to evaluate the model's own judgments, which is a novel extension of the Self-Rewarding method. However, the paper would benefit from a more thorough analysis of the computational costs associated with the proposed method. Specifically, the authors should provide a detailed breakdown of the time and resources required for each step of the training process, including the generation of responses, the evaluation of judgments by the meta-judge, and the training of the model using the meta-judge's feedback. This analysis should also consider the impact of the number of judgments generated per response and the size of the model on the overall computational cost. Furthermore, it would be beneficial to compare the computational cost of the proposed method with that of the Self-Rewarding method and other relevant baselines to provide a clear understanding of the trade-offs between performance gains and computational overhead. This would allow readers to assess the practical feasibility of the method in different settings.

In addition to the computational cost, the paper should also include a more detailed analysis of the limitations of the proposed method. While the paper demonstrates the effectiveness of the method on several benchmarks, it is important to understand the scenarios where the method may not perform well. For example, the authors should investigate the performance of the method on more challenging or diverse datasets, such as those that require complex reasoning or creative problem-solving. It would also be helpful to analyze the sensitivity of the method to different types of prompts and to identify any potential biases or limitations in the evaluation process. Furthermore, the authors should discuss the potential impact of the meta-judge's performance on the overall performance of the method. If the meta-judge is not well-trained or if it is biased, it could negatively affect the model's judgment ability. A thorough analysis of these limitations would provide a more complete understanding of the method's strengths and weaknesses.

Finally, the paper should include a more detailed analysis of the sensitivity of the proposed method to different hyperparameters. The authors should conduct experiments with different values of key hyperparameters, such as the learning rate, the batch size, and the number of training iterations. This analysis should include a discussion of the impact of these hyperparameters on the performance of the method and provide guidance on how to choose appropriate values for different settings. It would also be helpful to analyze the stability of the training process and to identify any potential issues with convergence or oscillations. Furthermore, the authors should discuss the potential impact of different meta-judge architectures on the overall performance of the method. A thorough analysis of these hyperparameters would provide a more robust and reliable evaluation of the method and allow readers to better understand its behavior in different settings.

### Questions

1. How does the proposed method perform on more challenging or diverse datasets?
2. What is the impact of the meta-judge's performance on the overall performance of the method?
3. How sensitive is the proposed method to different hyperparameters?

### Rating

6

### Confidence

3

**********
