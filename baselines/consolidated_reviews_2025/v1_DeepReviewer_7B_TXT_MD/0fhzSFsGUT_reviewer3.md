### Summary

This paper proposes a new method to parallelize the training of reversible neural networks. The authors show that by decoupling the forward and backward passes and only communicating activations and gradients between each other, they can achieve a linear speedup compared to standard backpropagation. The authors show that their method is competitive with standard backpropagation on CIFAR-10, ImageNet-32, and ImageNet.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper is well-written and easy to follow. The authors provide a clear motivation for their work and a detailed explanation of their method.
- The authors provide a comprehensive comparison of their method with other parallelization techniques, highlighting the advantages of their approach.
- The authors provide a detailed analysis of the memory and computational cost of their method, demonstrating its efficiency.

### Weaknesses

#### Some Related Works

[1] A Distributed Learning Approach to Training Deep Neural Networks
[2] Distributed Training of Deep Neural Networks: On the Communication Complexity Side of the Story
[3] Distributed Training of Deep Neural Networks: The Stability-Soundness Trade-Off

#### comment

 - The authors claim that their method is a novel alternative to backpropagation for parallelizing training of reversible neural networks. However, the idea of decoupling the forward and backward passes and only communicating activations and gradients between each other is not new. This idea has been explored in previous works, such as [1], [2], and [3]. The authors should acknowledge this and clearly state the novelty of their work in the context of these existing methods.
- The authors only evaluate their method on CIFAR-10, ImageNet-32, and ImageNet. While these are standard datasets, they are relatively small. The authors should evaluate their method on larger datasets, such as ImageNet-1K, to demonstrate its scalability and effectiveness.
- The authors do not provide a detailed analysis of the communication overhead of their method. While they claim that their method has a low communication overhead, they do not provide any empirical evidence to support this claim. They should provide a detailed analysis of the communication cost of their method and compare it with other parallelization techniques.

### Suggestions

The authors should more clearly differentiate their work from existing methods that decouple forward and backward passes. While the specific implementation details might differ, the core idea of decoupling the passes is not novel. The authors should focus on highlighting the specific advantages of their approach, such as the use of reversible architectures and the resulting memory savings, and how these advantages translate to improved performance or efficiency compared to existing methods. A more thorough discussion of the differences in implementation and the specific benefits of their approach is needed to justify the novelty claim. For example, a detailed comparison of the communication patterns and the computational costs associated with their method versus the methods in [1,2,3] would be beneficial.

To strengthen the empirical evaluation, the authors should include results on larger datasets such as ImageNet-1K. This would provide a more robust assessment of the scalability and effectiveness of their method. Furthermore, the authors should provide a more detailed analysis of the communication overhead. This analysis should include the amount of data communicated, the frequency of communication, and the impact of communication on the overall training time. The authors should also compare the communication overhead of their method with other parallelization techniques, such as data parallelism and model parallelism. This would provide a more comprehensive understanding of the trade-offs between different parallelization strategies. For example, a breakdown of the communication time and computation time for their method and other methods would be valuable.

Finally, the authors should provide a more detailed explanation of the memory savings achieved by their method. While they mention that their method has low memory overhead, they do not provide a quantitative analysis of the memory usage. They should provide a detailed breakdown of the memory usage for different components of their method, such as the activations, gradients, and model parameters. This would help to understand the memory efficiency of their method and how it compares with other parallelization techniques. For example, a comparison of the memory usage of their method with data parallelism and model parallelism would be helpful.

### Questions

- How does your method compare to the methods in [1], [2], and [3] in terms of communication overhead?
- What are the memory savings of your method compared to data parallelism and model parallelism?
- How does your method perform on larger datasets, such as ImageNet-1K?

[1] A Distributed Learning Approach to Training Deep Neural Networks

[2] Distributed Training of Deep Neural Networks: On the Communication Complexity Side of the Story

[3] Distributed Training of Deep Neural Networks: The Stability-Soundness Trade-Off

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
