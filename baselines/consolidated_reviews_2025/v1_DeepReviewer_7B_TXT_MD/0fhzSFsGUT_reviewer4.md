### Summary

The paper introduces PETRA, a novel method for parallelizing the training of reversible neural networks. The key idea is to decouple the forward and backward passes and only communicate activations and gradients between each other. This allows for efficient model parallelism with minimal memory overhead. The authors demonstrate the effectiveness of PETRA on CIFAR-10, ImageNet32, and ImageNet, achieving competitive accuracy with standard backpropagation while enabling linear speedup compared to synchronous backpropagation.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper presents a novel and effective method for parallelizing the training of reversible neural networks. The decoupling of forward and backward passes is a clever idea that allows for efficient model parallelism with minimal memory overhead.
- The authors provide a clear and well-motivated explanation of the proposed method. The use of reversible neural networks is well-justified, and the authors provide a detailed description of how PETRA works.
- The paper includes a comprehensive set of experiments on CIFAR-10, ImageNet32, and ImageNet. The results demonstrate that PETRA achieves competitive accuracy with standard backpropagation while enabling linear speedup compared to synchronous backpropagation.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the computational cost of the proposed method. While the authors mention that PETRA achieves linear speedup compared to standard backpropagation, they do not provide a breakdown of the computational overhead introduced by the decoupled forward and backward passes. A more detailed analysis of the computational cost would be helpful to understand the trade-offs between accuracy and efficiency.
- The paper does not compare PETRA with other parallelization methods for reversible neural networks. While the authors mention that PETRA is a novel method, they do not provide a comparison with other existing methods. A comparison with other methods would help to understand the advantages and limitations of PETRA.

### Suggestions

The paper would benefit from a more thorough analysis of the computational overhead introduced by PETRA. While the authors claim linear speedup, a detailed breakdown of the time spent on forward and backward passes, as well as the communication overhead, is crucial. For instance, the authors could provide a comparison of the time taken for a single training step with PETRA versus standard backpropagation, and also analyze how this scales with the number of parallel workers. Furthermore, it would be beneficial to quantify the memory footprint of PETRA, especially in comparison to other parallelization techniques. This would help to understand the practical trade-offs between accuracy, speed, and memory usage. A more detailed analysis of these aspects would significantly strengthen the paper's claims and provide a more comprehensive understanding of PETRA's performance characteristics.

To further enhance the paper, a more comprehensive comparison with existing parallelization methods for reversible neural networks is necessary. The authors should not only compare the accuracy but also the computational cost and memory usage of PETRA with other methods. This comparison should include a discussion of the specific scenarios where PETRA is expected to outperform other methods and vice versa. For example, the authors could compare PETRA with methods that use gradient checkpointing or other techniques to reduce memory usage. A detailed comparison would help to position PETRA within the existing literature and highlight its unique advantages and limitations. This would also help the reader to understand the practical implications of choosing PETRA over other methods.

Finally, the authors should provide more details on the implementation of PETRA. For example, how are the activations and gradients stored and communicated between different workers? What are the specific data structures used? How does the method handle the synchronization of the different stages? Providing these details would make the paper more reproducible and allow other researchers to build upon this work. Furthermore, the authors could also discuss the limitations of PETRA, such as the potential for increased communication overhead in certain scenarios or the challenges of implementing PETRA on specific hardware platforms. Addressing these limitations would provide a more balanced and complete picture of the proposed method.

### Questions

- How does PETRA compare to other parallelization methods for reversible neural networks in terms of accuracy, computational cost, and memory usage?
- What are the limitations of PETRA, and in which scenarios is it expected to perform best?

### Rating

8: accept, good paper

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
