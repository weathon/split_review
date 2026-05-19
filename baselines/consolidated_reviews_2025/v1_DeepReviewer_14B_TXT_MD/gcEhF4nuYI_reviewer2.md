### Summary

The paper introduces a token-level pruning method for large language models (LLMs) that reduces computational costs during inference without retraining. It uses a learnable router to skip less important tokens across model blocks, guided by a sparsity scheduler and four low-dimensional factors. The authors conduct extensive experiments on various LLMs, showing that their method outperforms other state-of-the-art pruning methods in accuracy retention at comparable sparsity levels.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The proposed method achieves better accuracy retention compared to other state-of-the-art pruning methods at similar sparsity levels.
2. The authors provide extensive experimental results across different benchmarks and LLMs, demonstrating the robustness and effectiveness of their approach.
3. The method is innovative in its use of a learnable router and sparsity scheduler, which allows for fine-grained token pruning without the need for retraining.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method involves a complex training process with multiple steps, including sparsity scheduler searching, dynamic router training, and sparsity scheduler fine-tuning, which may be difficult to optimize and implement in practice.
2. The method relies on several hyperparameters, such as the loss weights (λd, λs, λg), which may require careful tuning for different models and tasks, potentially limiting its ease of use.
3. The paper does not provide a detailed analysis of the computational overhead introduced by the token router during inference, which could be significant, especially for longer sequences.

### Suggestions

The authors should provide a more detailed breakdown of the computational cost associated with the token router, including FLOPs and latency, across various sequence lengths and model sizes. This analysis should not only focus on the router itself but also consider the overhead of the additional operations required for the proposed method, such as the computation of the four low-dimensional factors and the argmax operation for gate selection. A comparison with other pruning methods should be included to contextualize the overhead of the proposed method. Furthermore, the authors should investigate the potential for optimizing the router implementation to reduce its computational footprint, such as using more efficient network architectures or quantization techniques. This would help to better understand the practical implications of the proposed method and its suitability for real-world applications.

To address the concern about hyperparameter sensitivity, the authors should conduct a more rigorous ablation study on the loss weights (λd, λs, λg) and other critical hyperparameters. This study should not only focus on the final performance but also on the convergence speed and stability of the training process. The authors should also explore adaptive hyperparameter tuning methods, such as Bayesian optimization or reinforcement learning, to reduce the need for manual tuning. Furthermore, the authors should provide clear guidelines on how to choose appropriate hyperparameter values for different models and tasks, based on the ablation study and other experiments. This would make the method more accessible and easier to use for practitioners.

Finally, the authors should provide a more detailed explanation of the training process, including the specific optimization algorithms used, the learning rate schedules, and the batch sizes. The authors should also discuss the convergence behavior of the training process and provide empirical evidence to support the claim that the method converges effectively. It would be beneficial to include visualizations of the training curves and the evolution of the sparsity patterns during training. This would help to better understand the dynamics of the proposed method and its robustness to different initialization conditions. The authors should also discuss the potential limitations of the training process and suggest possible solutions for addressing these limitations.

### Questions

1. How does the computational overhead of the token router compare to the computational savings achieved through token pruning, especially for longer sequences?
2. How sensitive is the method to the choice of hyperparameters, such as the loss weights (λd, λs, λg), and how can these be effectively tuned for different models and tasks?
3. What is the impact of the proposed method on the generalization capabilities of the pruned LLMs, especially when applied to out-of-domain tasks or datasets not seen during pruning?

### Rating

6

### Confidence

3

**********
