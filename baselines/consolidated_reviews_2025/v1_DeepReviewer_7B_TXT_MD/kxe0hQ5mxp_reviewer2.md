### Summary

This paper proposes a new class of activation functions, called elephant activation functions, that can generate both sparse representations and sparse gradients. The authors argue that this property helps to reduce forgetting in neural networks. The paper provides theoretical analysis and experimental results to support this claim.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The idea of using sparse activation functions to reduce forgetting is interesting.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a clear motivation for why the proposed approach is effective. While the authors argue that sparse representations and sparse gradients help to reduce forgetting, they do not provide a clear explanation of why this is the case. It is not clear how the sparsity of the representations and gradients directly leads to better performance in continual learning scenarios. The paper does not delve into the specific mechanisms by which sparsity reduces forgetting, such as how it prevents the network from overwriting previously learned information or how it facilitates the learning of new tasks without disrupting old ones. A more detailed explanation of the underlying theoretical principles is needed.
2. The paper does not provide a detailed analysis of the computational cost of the proposed approach. While the authors claim that the approach is efficient, they do not provide any empirical evidence to support this claim. It is important to understand the computational overhead of using elephant activation functions compared to traditional activation functions, especially in resource-constrained environments. The paper should include a comparison of training time and memory usage, and how these scale with the size of the network and the number of tasks.
3. The paper does not compare the proposed approach to other state-of-the-art continual learning methods. While the authors compare their approach to some baselines, they do not compare it to other recent methods that have achieved state-of-the-art performance in continual learning. This makes it difficult to assess the true effectiveness of the proposed approach. The paper should include a comparison to methods that explicitly address catastrophic forgetting, such as regularization-based methods, replay-based methods, and architecture-based methods.

### Suggestions

The paper would benefit significantly from a more detailed explanation of the theoretical underpinnings of why sparse activations and gradients lead to reduced forgetting. The authors should elaborate on how the sparsity of activations and gradients affects the learning dynamics of the network. For instance, they could discuss how sparse activations might limit the interference between different tasks, or how sparse gradients might help in disentangling the representations of different tasks. A more rigorous analysis of the gradient flow and how it is affected by the proposed activation functions would also be beneficial. Furthermore, the authors should provide a more concrete explanation of how the proposed activation functions achieve sparsity, and how this sparsity is related to the reduction of forgetting. This could involve a mathematical analysis of the activation function and its impact on the network's parameters and activations.

To address the lack of computational analysis, the authors should include a thorough empirical evaluation of the computational cost of their approach. This should include a comparison of training time and memory usage with traditional activation functions, as well as an analysis of how these costs scale with the size of the network and the number of tasks. The authors should also consider the computational cost of the proposed activation function itself, including any overhead associated with its implementation. This analysis should be performed on a variety of hardware platforms to provide a comprehensive understanding of the computational overhead. Furthermore, the authors should discuss the potential for optimizing the implementation of the proposed activation function to reduce its computational cost. This could involve techniques such as approximation or hardware acceleration.

Finally, the paper needs a more comprehensive comparison to state-of-the-art continual learning methods. The authors should include a comparison to methods that explicitly address catastrophic forgetting, such as regularization-based methods, replay-based methods, and architecture-based methods. This comparison should include both performance metrics and computational cost. The authors should also discuss the limitations of their approach and identify areas for future research. This would help to contextualize the contribution of the paper and provide a more complete picture of its strengths and weaknesses. The comparison should also include a discussion of the specific scenarios where the proposed method is expected to perform well and where it might not be suitable.

### Questions

Please see the weakness.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
