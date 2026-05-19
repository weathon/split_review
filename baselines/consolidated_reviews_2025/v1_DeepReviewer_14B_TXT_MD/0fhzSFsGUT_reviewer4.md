### Summary

The authors propose a novel approach to parallelize the training of reversible architectures. The main idea is to decouple the forward and backward passes, allowing stages of the network to be computed independently on different devices. This approach eliminates the need for weight stashing and reduces memory overhead. The authors demonstrate the effectiveness of their method on CIFAR-10, ImageNet32, and ImageNet datasets, achieving competitive accuracies compared to backpropagation.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow. The authors provide a clear explanation of the background, the problem they are addressing, and their proposed solution. The use of figures and tables helps to illustrate the concepts and results.

2. The proposed method is sound and well-motivated. The authors thoroughly discuss the related work and explain how their approach differs from and improves upon existing methods.

3. The experimental results are comprehensive and convincing. The authors evaluate their method on multiple datasets and compare it to several baselines. The results show that their method achieves competitive accuracies while reducing memory overhead.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the computational overhead of the proposed method. While the authors claim that their method reduces memory overhead, they do not provide a thorough analysis of the computational cost associated with the decoupled forward and backward passes. Specifically, the paper does not quantify the additional FLOPs or latency introduced by the reversible layers and the custom autograd framework. A breakdown of the computational cost per layer type (e.g., convolutional, linear) and a comparison to standard backpropagation would be beneficial.

2. The paper does not explore the impact of different reversible architectures on the performance of the proposed method. The authors focus on a specific type of reversible architecture, but it is unclear how the method would perform with other reversible architectures, such as those based on different coupling layers or attention mechanisms. A study on the sensitivity of the method to architectural choices would strengthen the paper.

3. The paper does not provide a detailed analysis of the convergence behavior of the proposed method. While the authors show that their method achieves competitive accuracies, they do not analyze the convergence speed or stability of the training process. It would be helpful to see learning curves and a comparison of the convergence behavior to standard backpropagation. Furthermore, the paper does not discuss the impact of the decoupled forward and backward passes on the optimization landscape.

### Suggestions

To address the lack of computational overhead analysis, the authors should include a detailed breakdown of the FLOPs and latency introduced by their method. This should include a per-layer analysis, comparing the computational cost of the reversible layers and the custom autograd framework to standard backpropagation. The authors should also provide a comparison of the training time per epoch for their method and standard backpropagation, using the same hardware and software configurations. This analysis should be performed on multiple datasets to ensure the results are generalizable. Furthermore, the authors should investigate the impact of different batch sizes on the computational overhead, as this can significantly affect the overall training time. This detailed analysis will provide a more complete picture of the computational trade-offs of the proposed method.

To address the lack of exploration of different reversible architectures, the authors should conduct experiments using a variety of reversible architectures, such as those based on different coupling layers (e.g., affine coupling layers, spline coupling layers) or attention mechanisms. This would help to understand the sensitivity of the proposed method to architectural choices. The authors should also analyze the impact of different architectural parameters, such as the number of layers or the size of the hidden dimensions, on the performance of the proposed method. This analysis should include a comparison of the accuracy, memory overhead, and computational cost for different architectures. This would provide a more comprehensive understanding of the applicability of the proposed method to different reversible architectures.

To address the lack of convergence analysis, the authors should include learning curves that show the training and validation loss and accuracy over time. This would allow for a comparison of the convergence speed and stability of the proposed method to standard backpropagation. The authors should also analyze the impact of the decoupled forward and backward passes on the optimization landscape. This could involve visualizing the loss surface or analyzing the gradient norms during training. Furthermore, the authors should investigate the impact of different optimization algorithms and learning rate schedules on the convergence behavior of the proposed method. This detailed analysis will provide a more complete picture of the convergence properties of the proposed method.

### Questions

1. How does the computational overhead of the proposed method compare to standard backpropagation?

2. How does the proposed method perform with different reversible architectures?

3. How does the convergence behavior of the proposed method compare to standard backpropagation?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
