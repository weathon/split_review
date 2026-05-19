### Summary

This paper proposes a fine-grained token-wise pruning approach for large language models (LLMs), introducing a learnable router to adaptively identify less important tokens within each block for selective skipping during inference. The authors present a comprehensive methodology, encompassing a search-based sparsity scheduler, a dynamic router trained with multiple loss functions, and sparsity scheduler fine-tuning. Experimental results demonstrate that this approach outperforms existing pruning methods across various benchmarks.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The motivation is clear and the writing is easy to follow.
2. The authors provide a thorough analysis of token redundancy across different blocks in LLMs, which is valuable for understanding model behavior.
3. The experimental results show that the proposed method outperforms other pruning methods.

### Weaknesses

#### Some Related Works

[1] SLEB: Token Pruning for Generative Language Models at Almost No Cost
[2] TokenPruner: Layerwise Token Pruning for Large Language Models
[3] ShortGPT: Accelerating Large Language Models by Merging Redundant Consecutive Tokens

#### comment

1. The novelty of this paper is limited, as token pruning has been extensively studied in prior works, such as SLEB [1], TokenPruner [2], and ShortGPT [3]. The authors should provide a more detailed comparison with these methods to highlight the unique contributions of their approach. Specifically, the paper lacks a detailed analysis of how the proposed method differs from these existing techniques in terms of the pruning granularity, the optimization strategy, and the computational overhead. A more thorough comparison should include a discussion of the specific scenarios where the proposed method is expected to outperform existing approaches, and vice versa.
2. The experimental comparisons are incomplete, as the authors do not include evaluations against SLEB [1], TokenPruner [2], and ShortGPT [3]. Additionally, the authors should consider including more recent baselines, such as ShortenedGPT [4], to provide a more comprehensive evaluation. The absence of these comparisons makes it difficult to assess the true performance of the proposed method relative to the state-of-the-art. The evaluation should also include a wider range of model sizes and tasks to ensure the generalizability of the results.
3. The authors should provide a more detailed analysis of the computational overhead introduced by the dynamic router, including the training time and memory requirements. The paper should also discuss the potential impact of the router on the overall inference latency, and whether the proposed method is suitable for real-time applications. A detailed analysis of the computational cost is crucial for evaluating the practical applicability of the proposed method.

### Suggestions

The paper would benefit significantly from a more in-depth analysis of the proposed method's novelty compared to existing token pruning techniques. While the authors mention that their method is token-wise, they need to clearly articulate how this differs from other token pruning methods in terms of the pruning granularity, the optimization strategy, and the computational overhead. For example, a detailed comparison of the search space and the optimization process used in this paper versus methods like SLEB, TokenPruner, and ShortGPT would be beneficial. The authors should also discuss the specific scenarios where their method is expected to outperform existing approaches, and provide a theoretical justification for these claims. Furthermore, the paper should include a more detailed analysis of the computational overhead introduced by the dynamic router. This analysis should include the training time and memory requirements, as well as the potential impact on inference latency. The authors should also discuss the trade-offs between the computational cost and the performance gains achieved by their method. It would be beneficial to provide a breakdown of the computational cost associated with different components of the router, such as the sparsity scheduler and the dynamic router itself. This would allow readers to better understand the computational bottlenecks and potential areas for optimization.

To strengthen the experimental evaluation, the authors should include a more comprehensive set of baselines, including SLEB, TokenPruner, ShortGPT, and ShortenedGPT. The evaluation should also include a wider range of model sizes and tasks to ensure the generalizability of the results. The authors should also provide a more detailed analysis of the performance of their method across different layers of the model. This analysis should include a discussion of why certain layers are more amenable to token pruning than others, and how the proposed method addresses these differences. The paper should also include a discussion of the limitations of the proposed method, and potential directions for future research. For example, the authors could discuss the potential impact of the proposed method on the model's ability to capture long-range dependencies, and how this might affect performance on tasks that require such dependencies. The authors should also consider evaluating their method on a wider range of tasks, including tasks that require more complex reasoning and understanding.

Finally, the authors should provide a more detailed explanation of the training process for the dynamic router. This explanation should include a discussion of the specific loss functions used, the optimization algorithm, and the hyperparameter settings. The authors should also provide a more detailed analysis of the convergence behavior of the dynamic router, and how the training process affects the performance of the proposed method. It would be beneficial to include a visualization of the training process, such as a plot of the loss function over time. This would allow readers to better understand the training dynamics and potential issues. The authors should also discuss the sensitivity of the proposed method to the choice of hyperparameters, and provide guidance on how to select appropriate values for these parameters. This would make the method more practical and easier to use for other researchers.

### Questions

See the weaknesses.

### Rating

5

### Confidence

4

**********
