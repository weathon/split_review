### Summary

This paper proposes a fine-grained token-wise pruning approach for large language models (LLMs) to reduce computational overhead during inference. The method introduces a learnable router that adaptively identifies and skips less important tokens across model blocks, aiming to maintain high accuracy while achieving significant acceleration. Extensive experiments demonstrate that this approach outperforms existing pruning methods on several benchmarks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The proposed method achieves notable improvements over existing pruning techniques, particularly in accuracy retention at various sparsity levels.
2. The paper provides a comprehensive experimental evaluation across multiple LLMs and benchmarks, demonstrating the robustness and generalizability of the approach.
3. The introduction of a learnable router for token pruning is a novel contribution that addresses the limitations of traditional pruning methods.

### Weaknesses

#### Some Related Works


#### comment

1. The method introduces additional complexity with the learnable router and sparsity scheduler, which may increase the implementation difficulty and computational overhead during training. Specifically, the router, being a small neural network, adds parameters and requires backpropagation, potentially increasing training time and memory consumption. The sparsity scheduler, while aiming to optimize sparsity allocation, introduces another layer of optimization that needs to be carefully tuned, adding to the overall complexity of the training pipeline.
2. The paper lacks a detailed discussion on the computational overhead introduced by the token router during inference. While the paper mentions the router is small, it does not provide a quantitative analysis of the additional FLOPs or latency introduced by the router, which is crucial for practical deployment. The overhead of the router could potentially negate some of the benefits of token pruning, especially for shorter sequences where the relative cost of the router might be higher.
3. The experiments primarily focus on a few specific LLMs and benchmarks, which may not fully represent the method's effectiveness across a broader range of models and tasks. For example, the paper does not explore the performance of the method on models with different architectures, such as those with varying layer sizes or attention mechanisms. Additionally, the benchmarks used might not cover all the nuances of different NLP tasks, limiting the generalizability of the findings.

### Suggestions

The paper should provide a more detailed analysis of the computational overhead introduced by the token router. This should include a breakdown of the FLOPs and latency associated with the router, both during training and inference. It would be beneficial to compare the overhead of the router with the computational savings achieved through token pruning, across different sequence lengths and model sizes. This analysis should also consider the impact of the router on memory usage, as the additional parameters and activations could potentially increase memory consumption, especially for large language models. Furthermore, the paper should explore the trade-offs between router complexity and pruning efficiency, investigating whether a simpler router could achieve comparable results with lower overhead.

To address the limited scope of the experiments, the authors should evaluate the proposed method on a wider range of LLMs, including models with different architectures and sizes. This would help to demonstrate the generalizability of the approach and identify any potential limitations. Additionally, the paper should include experiments on a more diverse set of benchmarks, covering various NLP tasks such as text classification, question answering, and summarization. This would provide a more comprehensive evaluation of the method's effectiveness and its ability to maintain performance across different tasks. The authors should also consider evaluating the method on tasks that are more sensitive to token-level information, such as machine translation or text generation, to assess the impact of token pruning on these tasks.

Finally, the paper should provide a more in-depth discussion of the limitations of the proposed method. This should include a discussion of the potential challenges in applying the method to different types of models and tasks, as well as the trade-offs between accuracy and computational efficiency. The authors should also discuss the potential impact of the method on model robustness and generalization, and whether the pruning process could lead to a decrease in model performance on out-of-distribution data. This discussion should be supported by experimental evidence and should provide a balanced perspective on the strengths and weaknesses of the proposed approach.

### Questions

1. How does the computational overhead of the token router compare to the computational savings achieved through token pruning, especially for shorter sequences?
2. Can the proposed method be extended to other types of neural network models beyond LLMs, and what modifications would be necessary?
3. How does the method handle the potential impact of token pruning on the model's ability to generalize to unseen data or tasks?

### Rating

6

### Confidence

3

**********
