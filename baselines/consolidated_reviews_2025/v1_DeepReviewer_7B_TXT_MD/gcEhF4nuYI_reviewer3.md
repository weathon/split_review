### Summary

This paper introduces a fine-grained token pruning method for large language models (LLMs). The authors propose a learnable router to adaptively identify less important tokens and skip them during inference, reducing computational costs without retraining the model. The method is evaluated on various benchmarks and compared with other pruning techniques, showing superior performance across multiple models and sparsity ratios.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow, with clear explanations of the methodology and experimental setup.
2. The authors provide a thorough analysis of token redundancy across different layers and blocks in LLMs, which helps to understand the motivation behind the proposed method.
3. The proposed method is evaluated on multiple LLMs and benchmarks, demonstrating its effectiveness and generalizability.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed discussion of the computational overhead introduced by the learnable router. While the authors mention that the router is lightweight, they do not provide specific details about its computational cost, such as the number of parameters, FLOPs, or memory usage. This makes it difficult to assess the practical applicability of the method, especially for resource-constrained environments.
2. The paper does not provide a detailed analysis of the impact of different hyperparameters on the performance of the proposed method. For example, the authors do not discuss how the number of hidden states used as input to the router, the number of layers in the router, or the learning rate affect the performance. This lack of analysis makes it difficult to reproduce the results and to apply the method to new tasks.
3. The paper does not provide a comparison with other token pruning methods, such as those based on attention scores or gradient information. This makes it difficult to assess the novelty and effectiveness of the proposed method compared to existing approaches. The authors should also discuss the limitations of their method and potential directions for future research.

### Suggestions

The authors should provide a more detailed analysis of the computational overhead introduced by the learnable router. This should include a breakdown of the FLOPs, memory usage, and parameter count for the router, as well as the overall model. It would be beneficial to compare these metrics with those of the original model and other pruning methods. Furthermore, the authors should investigate the scalability of the router with respect to the input sequence length and the number of tokens. This analysis should be included in the main paper, not just in the appendix, as it is crucial for understanding the practical applicability of the method. The authors should also discuss the potential for optimizing the router's architecture to reduce its computational cost, such as using a smaller number of layers or a more efficient activation function.

To address the lack of hyperparameter analysis, the authors should conduct a more thorough investigation of the impact of different hyperparameters on the performance of the proposed method. This should include a systematic exploration of the number of hidden states used as input to the router, the number of layers in the router, the learning rate, and the sparsity ratio. The authors should also discuss the sensitivity of the method to these hyperparameters and provide guidelines for selecting appropriate values. For example, they could use a grid search or a more sophisticated optimization technique to find the optimal hyperparameter settings. The results of this analysis should be presented in a clear and concise manner, possibly using tables or graphs, and should be included in the main paper. This would allow readers to better understand the method and to apply it to new tasks.

Finally, the authors should provide a more comprehensive comparison with other token pruning methods, including those based on attention scores or gradient information. This comparison should include a discussion of the advantages and disadvantages of each method, as well as a quantitative comparison of their performance on various benchmarks. The authors should also discuss the limitations of their method and potential directions for future research. For example, they could explore the use of different input features for the router, such as the attention weights or the gradient information. They could also investigate the use of more sophisticated training techniques, such as curriculum learning or adversarial training. This would help to further improve the performance of the method and to make it more robust to different tasks and datasets.

### Questions

1. How does the proposed method compare with other token pruning methods in terms of computational overhead and memory usage?
2. What is the impact of different hyperparameters on the performance of the proposed method?
3. How does the proposed method perform on tasks that require long-range dependencies, such as summarization or question answering?

### Rating

6

### Confidence

4

**********
