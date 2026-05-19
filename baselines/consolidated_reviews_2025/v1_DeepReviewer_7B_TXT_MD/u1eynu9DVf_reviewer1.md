### Summary

This paper addresses the issue of catastrophic forgetting in large language models (LLMs) during the refinement process, where updating a model with new data often leads to the loss of previously learned information. The authors propose a novel approach to forecast which examples will be forgotten after model refinement, focusing on the transfer of logit changes between examples. They introduce two methods: a trainable logit-based forecasting model and a black-box representation-based forecasting model. The paper demonstrates the practical utility of their approach by showing that forecasting examples that will be forgotten can reduce overall forgetting when used to guide model refinement. The authors evaluate their methods on three different LLMs, showing that their approach outperforms random replay and other continual learning methods in terms of reducing forgetting.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper addresses an important problem in the field of large language models, specifically the issue of catastrophic forgetting during model refinement. This is a relevant and timely topic, as the ability to update models without losing previously learned information is crucial for the practical application of LLMs.
2. The authors propose a novel approach to forecast example forgetting by analyzing the transfer of logit changes between examples. This is an innovative idea that moves beyond traditional methods of model refinement, such as random replay, and has the potential to improve the efficiency and effectiveness of model updates.
3. The paper provides a comprehensive evaluation of the proposed methods on three different LLMs, demonstrating their effectiveness across various model architectures. The experiments are well-designed and provide strong evidence for the benefits of the proposed approach.
4. The paper is well-written and organized, making it easy to follow the authors' arguments and understand their contributions. The use of figures and tables is effective in presenting the results and supporting the claims made in the paper.

### Weaknesses

#### Some Related Works


#### comment

1. The paper's main weakness is the limited novelty of the proposed methods. While the idea of forecasting example forgetting is interesting, the methods themselves are not particularly innovative. The logit-based forecasting model is essentially a simplified version of the NTK analysis, and the black-box representation-based model is a standard machine learning approach. The paper does not provide a strong theoretical justification for why these specific methods should work well for example forgetting, and the connection to the underlying mechanisms of catastrophic forgetting is not clearly established. The methods appear to be ad-hoc solutions rather than principled approaches derived from a deeper understanding of the problem.
2. The paper does not provide a detailed analysis of the computational cost of the proposed methods. While the authors claim that their methods are efficient, they do not provide any quantitative comparisons with other methods in terms of training time, memory usage, or inference time. This makes it difficult to assess the practical feasibility of the proposed methods, especially for large-scale models. The lack of a detailed computational analysis is a significant oversight, as efficiency is a critical factor in the adoption of any new method.
3. The paper does not explore the limitations of the proposed methods in detail. For example, it is unclear how the methods perform when the model is updated with a large number of examples, or when the examples are highly diverse. The paper also does not discuss the potential impact of different model architectures or training procedures on the performance of the methods. A more thorough analysis of the limitations would provide a more balanced view of the proposed approach.
4. The paper does not provide a clear explanation of how the proposed methods can be integrated into existing model refinement pipelines. While the authors demonstrate the benefits of their methods in a specific experimental setup, they do not discuss how these methods can be used in more general settings. This lack of practical guidance makes it difficult for other researchers to adopt the proposed methods in their own work.

### Suggestions

The paper would benefit significantly from a more rigorous theoretical grounding of the proposed methods. Instead of relying on empirical observations, the authors should attempt to connect their methods to established theories of catastrophic forgetting and knowledge transfer. For example, they could explore how the logit-based forecasting model relates to the concept of interference in neural networks, or how the representation-based model aligns with information-theoretic measures of knowledge retention. This would not only strengthen the theoretical foundation of the paper but also provide a deeper understanding of why the proposed methods work. Furthermore, the authors should provide a more detailed analysis of the assumptions underlying their methods and discuss the conditions under which they are expected to perform well. This would help to clarify the scope and limitations of their approach and make it more useful for practitioners.

To address the lack of computational analysis, the authors should provide a detailed comparison of the training time, memory usage, and inference time of their methods with other relevant baselines. This comparison should be conducted on the same hardware and software configurations to ensure a fair evaluation. The authors should also discuss the scalability of their methods to larger models and datasets. For example, they could analyze how the computational cost of their methods scales with the number of parameters in the model or the size of the training data. This would provide a more comprehensive understanding of the practical feasibility of the proposed methods. Additionally, the authors should explore potential optimizations to reduce the computational cost of their methods, such as using more efficient implementations or leveraging hardware acceleration.

Finally, the paper needs to provide more practical guidance on how to integrate the proposed methods into existing model refinement pipelines. The authors should describe a concrete workflow that researchers can follow to use their methods in their own work. This workflow should include clear instructions on how to train the forecasting models, how to use them to guide model updates, and how to evaluate the effectiveness of the proposed approach. The authors should also discuss the potential challenges and limitations of integrating their methods into different types of model refinement pipelines. This would make the paper more useful for practitioners and encourage the adoption of the proposed methods in the field.

### Questions

1. How does the proposed method compare to other state-of-the-art continual learning methods in terms of computational cost and performance?
2. Can the proposed methods be generalized to other types of models or tasks beyond language models?
3. What are the limitations of the proposed methods, and how can they be addressed in future work?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
