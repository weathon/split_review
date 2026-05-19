### Summary

This paper proposes a new pruning method for large language models. The proposed method is simple and effective, and it does not require retraining or weight updates. The method is evaluated on LLaMA and LLaMA-2 models, and the results show that it can achieve comparable performance to the state-of-the-art SparseGPT method.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The proposed method is simple and effective. It does not require retraining or weight updates, which makes it more efficient than existing methods.
2. The method is evaluated on LLaMA and LLaMA-2 models, which are large and widely used language models. The results show that it can achieve comparable performance to the state-of-the-art SparseGPT method.
3. The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method is only evaluated on LLaMA and LLaMA-2 models. It would be better to evaluate it on other large language models, such as the OPT and Falcon models. Specifically, the performance on models with different architectures and training procedures should be considered to ensure the generalizability of the method. The current evaluation is limited to a single family of models, which may not be representative of the broader landscape of large language models.
2. The proposed method is only compared with SparseGPT. It would be better to compare it with other pruning methods, such as magnitude pruning and unstructured pruning. This comparison should include a range of sparsity levels and evaluation metrics to provide a comprehensive understanding of the method's strengths and weaknesses relative to existing techniques. The lack of comparison with other pruning methods makes it difficult to assess the true novelty and effectiveness of the proposed approach.
3. The proposed method is only evaluated on zero-shot tasks. It would be better to evaluate it on few-shot tasks. The performance of pruning methods can vary significantly depending on the task setting, and evaluating on few-shot tasks would provide a more complete picture of the method's capabilities. This is particularly important for tasks where the model's ability to generalize from limited examples is crucial.

### Suggestions

To address the limitations in the evaluation, the authors should expand their experiments to include a wider range of large language models, such as the OPT and Falcon families. This would involve not only running the proposed pruning method on these models but also comparing the results against the state-of-the-art pruning techniques, including SparseGPT, magnitude pruning, and unstructured pruning. The evaluation should be performed across different sparsity levels and using a variety of evaluation metrics, such as perplexity, accuracy, and F1 score, to provide a comprehensive assessment of the method's performance. Furthermore, the authors should investigate the impact of different pruning granularities, such as layer-wise and block-wise pruning, to determine the optimal configuration for each model. This would provide a more nuanced understanding of the method's applicability and limitations.

In addition to expanding the model evaluation, the authors should also evaluate their method on few-shot learning tasks. This would involve adapting the pruned models to perform well in scenarios where only a limited number of examples are available for each class. The authors should compare the performance of their method against existing pruning techniques in this setting, using metrics such as accuracy and generalization ability. This would provide a more complete picture of the method's capabilities and its potential for real-world applications. Furthermore, the authors should investigate the impact of different few-shot learning strategies, such as meta-learning and few-shot prompting, on the performance of the pruned models. This would help to identify the most effective ways to leverage the pruned models in few-shot settings.

Finally, the authors should provide a more detailed analysis of the computational cost of their method, including the time and memory requirements for both the pruning and inference stages. This analysis should be compared to the computational cost of existing pruning methods, such as SparseGPT, to provide a more complete understanding of the method's efficiency. The authors should also investigate the impact of different pruning granularities on the computational cost, as this may affect the method's applicability in resource-constrained environments. This analysis should include a discussion of the trade-offs between computational cost and performance, which would help readers to make informed decisions about the use of the proposed method.

### Questions

1. How does the proposed method perform on other large language models, such as the OPT and Falcon models?
2. How does the proposed method compare with other pruning methods, such as magnitude pruning and unstructured pruning?
3. How does the proposed method perform on few-shot tasks?

### Rating

5

### Confidence

3

**********
