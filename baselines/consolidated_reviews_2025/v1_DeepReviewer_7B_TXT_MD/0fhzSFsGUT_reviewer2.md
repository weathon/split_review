### Summary

The authors propose a new parallelization technique for reversible networks. The main idea is to decouple the forward and backward passes and to use delayed gradients. The authors show that this method can be used to train reversible networks efficiently.

### Soundness

3 good

### Presentation

2 fair

### Contribution

2 fair

### Strengths

- The proposed method seems to be novel and interesting. 
- The authors provide a detailed comparison with other parallelization methods.

### Weaknesses

#### Some Related Works


#### comment

 - The experiments are limited to relatively small datasets (CIFAR-10, ImageNet32, and ImageNet). It would be beneficial to evaluate the method on larger datasets like ImageNet-1K to demonstrate its scalability and effectiveness in more complex scenarios.
- The paper does not provide a detailed analysis of the computational cost of the proposed method. While the authors mention that PETRA achieves linear speedup compared to standard backpropagation, they do not provide a breakdown of the computational overhead introduced by the independent forward and backward passes. A more detailed analysis, including the time spent on forward and backward passes, would be helpful.
- The authors do not compare their method with other state-of-the-art training techniques for reversible architectures. A comparison with other methods would help to better understand the advantages and limitations of PETRA.

### Suggestions

The authors should consider expanding their experimental evaluation to include larger datasets such as ImageNet-1K. This would provide a more comprehensive assessment of the method's scalability and effectiveness in real-world scenarios. Specifically, it would be beneficial to analyze the performance of PETRA on ImageNet-1K with different model sizes and parallelization configurations. This would help to understand the method's limitations and identify potential areas for improvement. Furthermore, the authors should provide a more detailed analysis of the computational cost of their method. This should include a breakdown of the time spent on forward and backward passes, as well as the memory usage. This analysis should be compared with the computational cost of standard backpropagation and other state-of-the-art training techniques for reversible architectures. This would help to better understand the trade-offs between the different methods and identify the most suitable method for different applications. The authors should also consider comparing their method with other state-of-the-art training techniques for reversible architectures. This would help to better understand the advantages and limitations of PETRA. For example, comparing PETRA with other methods that use delayed gradients or parameter sharding would provide a more comprehensive evaluation of its performance. This comparison should include a detailed analysis of the performance, memory usage, and computational cost of each method. This would help to identify the most suitable method for different applications and provide a better understanding of the trade-offs between different approaches.

### Questions

- How does PETRA perform on larger datasets like ImageNet-1K?
- Can you provide a more detailed analysis of the computational cost of PETRA compared to standard backpropagation?
- How does PETRA compare with other state-of-the-art training techniques for reversible architectures?

### Rating

6: marginally above the acceptance threshold

### Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
