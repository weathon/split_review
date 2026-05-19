### Summary

This paper introduces a new self-improvement method called Meta-Rewarding, which iteratively improves the model's ability to judge its own responses and its ability to generate better responses. The method uses a meta-judge to evaluate the model's own judgments and provides feedback for training the model. The paper evaluates the method on AlpacaEval 2, Arena-Hard, and MT-Bench, and shows that it significantly improves the model's instruction-following ability and judgment accuracy.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper introduces a novel approach to self-improvement by introducing a meta-judge that evaluates the model's own judgments. This approach addresses the limitation of existing methods that only focus on improving the model's ability to generate better responses without improving its ability to judge its own responses.
2. The paper provides a clear and detailed description of the Meta-Rewarding method, including the meta-judge, the preference data creation process, and the training process. The paper also provides a comprehensive evaluation of the method on multiple benchmarks, including AlpacaEval 2, Arena-Hard, and MT-Bench.
3. The paper shows that the Meta-Rewarding method significantly improves the model's instruction-following ability and judgment accuracy. The results on AlpacaEval 2 show that the model achieves a 39.44% LC win rate, which is a significant improvement over the baseline model. The results on Arena-Hard show that the model is able to improve its score in all 4 iterations, demonstrating the effectiveness of the method in improving the model's ability to generate better responses.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost associated with the introduction of the meta-judge. While the framework shows improved performance, it is important to understand the trade-offs in terms of computational resources and training time. Specifically, the paper lacks a breakdown of the time spent on generating multiple judgments per response, selecting preferred and rejected judgments using the meta-judge, and training the model with the meta-judge-generated preference data. This makes it difficult to assess the practical feasibility of the approach, especially for large-scale models and datasets.
2. The paper does not explore the potential limitations of the meta-judge in handling nuanced or complex judgments. The effectiveness of the meta-judge in identifying and preferring higher-quality judgments could vary depending on the complexity and subtlety of the judgments. For example, in cases where multiple judgments are of similar quality, the meta-judge's ability to consistently select the best judgment might be limited. The paper should investigate how the meta-judge performs in scenarios with ambiguous or subjective judgments, and how it handles cases where the difference in quality between judgments is marginal.
3. The paper does not provide a thorough analysis of the impact of the length-control mechanism on the model's performance. While the mechanism is introduced to prevent response length explosion, it is important to understand its effect on the model's ability to generate comprehensive and detailed responses. The paper should investigate how the length-control mechanism affects the model's ability to capture and express complex ideas, and whether it introduces any biases or limitations in the generated responses.

### Suggestions

The paper would benefit from a more detailed analysis of the computational costs associated with the Meta-Rewarding framework. The authors should provide a breakdown of the time and resources required for each step of the process, including the generation of multiple judgments per response, the selection of preferred and rejected judgments using the meta-judge, and the training of the model with the meta-judge-generated preference data. This analysis should include a comparison with the computational costs of the Self-Rewarding baseline to quantify the additional overhead introduced by the meta-judge. Furthermore, the authors should explore the scalability of the approach by evaluating its performance with larger models and datasets. This would provide a more comprehensive understanding of the practical feasibility of the method and its potential for real-world applications. It would also be beneficial to investigate the impact of different hyperparameter settings on the computational cost and performance of the framework.

To address the limitations of the meta-judge in handling nuanced or complex judgments, the authors should conduct a more detailed analysis of its performance on complex and ambiguous judgments. This could involve creating a dataset of judgments with varying levels of complexity and subjectivity, and evaluating the meta-judge's ability to consistently select the best judgment. The authors should also investigate the meta-judge's sensitivity to different evaluation criteria and its ability to adapt to different types of judgments. Additionally, the paper should explore alternative meta-judge architectures or training methods that could improve its robustness and generalization capabilities. This could include techniques such as ensemble methods or adversarial training to enhance the meta-judge's ability to handle nuanced judgments. The paper should also discuss the potential limitations of the meta-judge in scenarios where the difference in quality between judgments is marginal and how it handles such cases.

Finally, the paper should provide a more thorough analysis of the impact of the length-control mechanism on the model's performance. The authors should investigate how the length-control mechanism affects the model's ability to generate comprehensive and detailed responses. This could involve evaluating the model's ability to capture and express complex ideas, and whether it introduces any biases or limitations in the generated responses. The authors should also explore alternative length-control strategies that could balance the trade-off between response length and quality. This could include techniques such as adaptive length control or dynamic response generation that adjusts the response length based on the complexity of the input prompt. The paper should also discuss the potential impact of the length-control mechanism on the model's ability to handle long and complex prompts and how it affects the overall performance of the framework.

### Questions

1. How does the computational cost of the Meta-Rewarding framework compare to the Self-Rewarding baseline? Could you provide a detailed breakdown of the time and resources required for each step of the framework?
2. How does the meta-judge perform in handling nuanced or complex judgments? Are there any specific scenarios where the meta-judge struggles to consistently select the preferred judgment?
3. What is the impact of the length-control mechanism on the model's ability to generate comprehensive and detailed responses? Does it introduce any biases or limitations in the generated responses?

### Rating

6

### Confidence

3

**********
