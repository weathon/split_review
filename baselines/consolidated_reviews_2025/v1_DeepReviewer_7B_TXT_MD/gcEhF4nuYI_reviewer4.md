### Summary

This paper proposes a token-wise pruning framework for large language models (LLMs) that achieves strong performance without retraining. The framework consists of three main steps: (1) an initial sparsity search using a static router, (2) training a dynamic router with a four-factor input and three loss functions, and (3) fine-tuning the sparsity scheduler with the trained router. The authors demonstrate the effectiveness of their method through extensive experiments across various LLMs and benchmarks, showing superior performance compared to existing pruning techniques.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow. The authors provide a clear and detailed explanation of the proposed method, including the motivation, methodology, and experimental setup.
2. The authors conduct extensive experiments across multiple LLMs and benchmarks, demonstrating the effectiveness of their method. The results show that the proposed method outperforms existing pruning techniques, highlighting its potential for practical applications.
3. The authors provide a thorough analysis of the token redundancy across different blocks and layers in LLMs, which helps to understand the underlying mechanisms of token pruning.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the computational overhead introduced by the dynamic router. While the authors mention that the router is lightweight, they do not provide specific details about its computational cost, such as the number of parameters, FLOPs, or memory usage. This makes it difficult to assess the practical applicability of the method, especially for resource-constrained environments.
2. The paper does not provide a detailed analysis of the impact of different hyperparameters on the performance of the proposed method. For example, the authors do not discuss how the number of hidden states used as input to the router, the number of layers in the router, or the learning rate affect the performance. This lack of analysis makes it difficult to reproduce the results and to apply the method to new tasks.
3. The paper does not provide a comparison with other token pruning methods, such as those based on attention scores or gradient information. This makes it difficult to assess the novelty and effectiveness of the proposed method compared to existing approaches. The authors should also discuss the limitations of their method and potential directions for future research.

### Suggestions

The authors should provide a more detailed analysis of the computational overhead introduced by the dynamic router. This analysis should include a breakdown of the FLOPs, memory usage, and parameter count for the router, as well as the overall model. It would be beneficial to compare these metrics with those of the original model and other pruning methods. Furthermore, the authors should investigate the scalability of the router with respect to the input sequence length and the number of tokens. This analysis should be included in the main paper, not just in the appendix, as it is crucial for understanding the practical applicability of the method. The authors should also discuss the potential for optimizing the router's architecture to reduce its computational cost, such as using a smaller number of layers or a more efficient activation function.

To address the lack of hyperparameter analysis, the authors should conduct a more thorough investigation of the impact of different hyperparameters on the performance of the proposed method. This should include a systematic exploration of the number of hidden states used as input to the router, the number of layers in the router, the learning rate, and the sparsity ratio. The authors should also discuss the sensitivity of the method to these hyperparameters and provide guidelines for selecting appropriate values. For example, they could use a grid search or a more sophisticated optimization technique to find the optimal hyperparameter settings. The results of this analysis should be presented in a clear and concise manner, possibly using tables or graphs, and should be included in the main paper. This would allow readers to better understand the method and to apply it to new tasks.

Finally, the authors should provide a more comprehensive comparison with other token pruning methods, including those based on attention scores or gradient information. This comparison should include a discussion of the advantages and disadvantages of each method, as well as a quantitative comparison of their performance on various benchmarks. The authors should also discuss the limitations of their method and potential directions for future research. For example, they could explore the use of different input features for the router, such as the attention weights or the gradient information. They could also investigate the use of more sophisticated training techniques, such as curriculum learning or adversarial training. This would help to further improve the performance of the method and to make it more robust to different tasks and datasets.

### Questions

1. How does the proposed method perform on tasks that require long-range dependencies, such as summarization or question answering?
2. What are the potential limitations of the proposed method, and what are the directions for future research?

### Rating

6

### Confidence

4

**********
