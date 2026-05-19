### Summary

The paper introduces a new class of activation functions, called elephant activation functions, designed to reduce catastrophic forgetting in neural networks. These functions are designed to produce both sparse representations and sparse gradients, which the authors argue helps to reduce forgetting by ensuring that the network can both correct errors and retain previously learned information. The paper presents experimental results across various continual learning scenarios, including regression, class incremental learning, and reinforcement learning, demonstrating that elephant activation functions outperform traditional activation functions and other baselines in terms of reducing forgetting.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

- The paper provides a theoretical analysis of the proposed elephant activation functions, demonstrating their ability to generate sparse representations and sparse gradients under certain conditions.
- The paper presents experimental results across a range of continual learning scenarios, including regression, class incremental learning, and reinforcement learning, demonstrating the effectiveness of the proposed approach.

### Weaknesses

#### Some Related Works


#### comment

 - The paper is not well-written. There are many grammatical errors, which makes it difficult to read and understand the paper. For example, "In streaming learning for regression" should be "In a streaming learning setting for regression".
- The paper lacks a clear motivation for why the proposed approach is effective. While the authors argue that sparse representations and sparse gradients help to reduce forgetting, they do not provide a clear explanation of why this is the case. It is not clear how the sparsity of the representations and gradients directly leads to better performance in continual learning scenarios.
- The paper does not provide a detailed analysis of the computational cost of the proposed approach. While the authors claim that the approach is efficient, they do not provide any empirical evidence to support this claim. It is important to understand the computational overhead of using elephant activation functions compared to traditional activation functions, especially in resource-constrained environments.
- The paper does not compare the proposed approach to other state-of-the-art continual learning methods. While the authors compare their approach to some baselines, they do not compare it to other recent methods that have achieved state-of-the-art performance in continual learning. This makes it difficult to assess the true effectiveness of the proposed approach.

### Suggestions

The paper needs significant improvements in clarity and motivation. The writing should be thoroughly proofread to eliminate grammatical errors and ensure that the paper is easy to understand. The authors should provide a more detailed explanation of why sparse representations and sparse gradients are beneficial for reducing catastrophic forgetting. This explanation should include a clear theoretical justification and empirical evidence to support the claims. For example, they could analyze how the sparsity of the representations and gradients affects the network's ability to retain previously learned information and adapt to new tasks. Furthermore, the authors should provide a more detailed analysis of the computational cost of their approach. This analysis should include a comparison of the training time and memory usage of their method with traditional activation functions. It would be beneficial to show how the computational cost scales with the size of the network and the number of tasks. This analysis should be performed on a variety of hardware platforms to provide a comprehensive understanding of the computational overhead. Finally, the paper should include a more comprehensive comparison to other state-of-the-art continual learning methods. This comparison should include both performance metrics and computational cost. The authors should also discuss the limitations of their approach and identify areas for future research. This would help to provide a more balanced and complete assessment of the proposed method.

### Questions

- Could you provide a more detailed explanation of why sparse representations and sparse gradients are beneficial for reducing catastrophic forgetting? It would be helpful to understand the theoretical underpinnings of this claim.
- Could you provide a more detailed analysis of the computational cost of the proposed approach? It would be helpful to understand the trade-offs between performance and computational efficiency.
- Could you compare the proposed approach to other state-of-the-art continual learning methods? It would be helpful to understand how the proposed approach compares to other recent methods in terms of performance and computational cost.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
