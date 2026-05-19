### Summary

This paper proposes a method to reduce the cost of using large language models (LLMs) for reasoning tasks by using a cascade of LLMs. The idea is to use a weaker but cheaper LLM to answer easy questions and a stronger but more expensive LLM to answer hard questions. The paper proposes several methods for deciding when to route a question to the stronger LLM, based on the answer consistency of the weaker LLM. The paper also proposes a mixture of thought representations, which samples answers from both chain-of-thought and program-of-thought prompts. The paper evaluates the proposed methods on six reasoning benchmark datasets, using GPT-3.5-turbo and GPT-4 as the weaker and stronger LLMs, respectively. The results show that the proposed methods can achieve comparable performance to using only the stronger LLM but require only 40% of its cost.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

* The paper addresses an important problem of reducing the cost of using LLMs for reasoning tasks, which is relevant to many applications.
* The paper proposes a novel and effective method for building an LLM cascade, which leverages the answer consistency of the weaker LLM as a signal of question difficulty.
* The paper proposes a mixture of thought representations, which samples answers from both chain-of-thought and program-of-thought prompts, and shows that it can improve the performance of the LLM cascade.
* The paper evaluates the proposed methods on six reasoning benchmark datasets, covering mathematical, symbolic, and causal reasoning tasks, and shows that they can achieve comparable performance to using only the stronger LLM but require only 40% of its cost.
* The paper compares the proposed methods with other baselines, such as using only the weaker LLM or only the stronger LLM, and shows that they can outperform them in terms of cost and accuracy.

### Weaknesses

#### Some Related Works


#### comment

 * The paper does not provide a theoretical analysis of the proposed method, such as the optimality of the routing decision or the convergence of the mixture of thought representations. Specifically, there is no formal justification for why the answer consistency of the weaker LLM is a good indicator of question difficulty, nor is there a proof that the proposed routing strategy minimizes the overall cost. The paper also lacks a theoretical framework for understanding how the mixture of thought representations leads to improved performance, such as whether it reduces variance or bias in the answers.
* The paper does not explore the sensitivity of the proposed method to the choice of the weaker and stronger LLMs, or the possibility of using other LLMs or other types of models. For example, it is unclear how the performance would change if a different open-source model was used as the weaker LLM, or if a smaller, fine-tuned model was used as the stronger LLM. The paper also does not investigate the impact of different model sizes or architectures on the effectiveness of the proposed method.
* The paper does not discuss the limitations of the proposed method, such as the potential for error propagation or the dependence on the quality of the demonstrations. For instance, the paper does not analyze how errors in the weaker LLM's answers might propagate to the stronger LLM, or how the method would perform if the demonstrations were noisy or irrelevant. The paper also does not address the potential for the weaker LLM to be overconfident in its answers, leading to incorrect routing decisions.

### Suggestions

The paper would benefit from a more rigorous theoretical analysis of the proposed method. Specifically, the authors should provide a formal justification for using answer consistency as a proxy for question difficulty. This could involve analyzing the relationship between answer consistency and the probability of the weaker LLM producing the correct answer. Furthermore, the authors should investigate the optimality of the proposed routing strategy, perhaps by deriving a theoretical bound on the expected cost of the cascade. This analysis should also consider the impact of different consistency thresholds on the overall performance. Additionally, a theoretical framework for understanding the mixture of thought representations is needed. This could involve analyzing the properties of the different thought representations and how they interact to improve the overall performance of the cascade. For example, the authors could investigate whether the mixture of thought representations reduces variance or bias in the answers, or whether it leads to a more robust solution.

To address the sensitivity of the proposed method to the choice of LLMs, the authors should conduct a more comprehensive evaluation using a wider range of models. This should include open-source models of varying sizes and architectures, as well as smaller, fine-tuned models. The authors should also investigate the impact of different model sizes and architectures on the effectiveness of the proposed method. This could involve analyzing the relationship between model size and the accuracy of the weaker LLM, as well as the impact of different architectures on the consistency of the answers. Furthermore, the authors should explore the possibility of using other types of models, such as smaller, fine-tuned models, as the stronger LLM. This could potentially reduce the cost of the cascade while maintaining its performance. The authors should also investigate the impact of different prompt strategies on the performance of the cascade, such as using different few-shot examples or different prompt formats.

Finally, the paper should discuss the limitations of the proposed method in more detail. This should include an analysis of the potential for error propagation, as well as the dependence on the quality of the demonstrations. The authors should investigate how errors in the weaker LLM's answers might propagate to the stronger LLM, and how the method would perform if the demonstrations were noisy or irrelevant. The authors should also address the potential for the weaker LLM to be overconfident in its answers, leading to incorrect routing decisions. This could involve analyzing the relationship between the consistency score and the probability of the weaker LLM producing the correct answer. The authors should also discuss the limitations of the proposed method in terms of its applicability to different types of reasoning tasks, and how it might be extended to handle more complex or ambiguous questions.

### Questions

* How does the proposed method perform on other types of reasoning tasks, such as commonsense reasoning, natural language inference, or question answering?
* How does the proposed method compare to other methods for reducing the cost of using LLMs, such as pruning, quantization, or knowledge distillation?
* How does the proposed method handle ambiguous or complex questions that might have multiple valid answers or require multiple steps of reasoning?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
