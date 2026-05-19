### Summary

The authors propose a novel approach to parallelize the training of reversible architectures, which is based on a delayed, approximate inversion of activations during the backward pass. The proposed method allows for enhanced computational efficiency and reduces memory overhead by minimizing the necessity to store extensive computational graphs. The authors validate the efficacy of their method through rigorous testing on benchmark datasets such as CIFAR-10, ImageNet-32, and ImageNet, where it demonstrates robust performance with minimal impact on accuracy.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

The authors propose a novel approach to parallelize the training of reversible architectures, which is based on a delayed, approximate inversion of activations during the backward pass. The proposed method allows for enhanced computational efficiency and reduces memory overhead by minimizing the necessity to store extensive computational graphs. The authors validate the efficacy of their method through rigorous testing on benchmark datasets such as CIFAR-10, ImageNet-32, and ImageNet, where it demonstrates robust performance with minimal impact on accuracy.

### Weaknesses

#### Some Related Works


#### comment

The authors propose a novel approach to parallelize the training of reversible architectures, which is based on a delayed, approximate inversion of activations during the backward pass. The proposed method allows for enhanced computational efficiency and reduces memory overhead by minimizing the necessity to store extensive computational graphs. The authors validate the efficacy of their method through rigorous testing on benchmark datasets such as CIFAR-10, ImageNet-32, and ImageNet, where it demonstrates robust performance with minimal impact on accuracy.

### Suggestions

The authors should provide a more detailed analysis of the impact of the delayed, approximate inversion on the training dynamics. While the results show robust performance, it is crucial to understand how the approximation affects the convergence rate and the stability of the training process. Specifically, a study on the sensitivity of the method to different approximation parameters would be beneficial. For instance, how does the accuracy and training time vary with the degree of approximation in the inversion? Furthermore, it would be valuable to investigate the potential for error accumulation due to the delayed inversion and how this error might propagate through the network during training. This analysis should include both theoretical considerations and empirical results, possibly visualizing the error propagation and its impact on the loss landscape.

Additionally, the authors should explore the limitations of their approach in more detail. While the method demonstrates good performance on the tested datasets, it is important to understand the scenarios where it might not be as effective. For example, how does the method perform with very deep networks or with architectures that have complex skip connections? Are there specific types of layers or activation functions that are more challenging to approximate with the proposed delayed inversion? A thorough investigation of these limitations would provide a more complete picture of the applicability of the method. This could involve testing on a wider range of architectures and datasets, including those with known training difficulties. The authors should also consider comparing their method with other parallelization techniques, such as data parallelism or model parallelism, to better understand the trade-offs involved.

Finally, the authors should provide more insights into the practical implementation of their method. While the paper describes the core idea, it lacks details on how the delayed inversion is implemented in practice. For example, what are the computational costs associated with the inversion operation, and how do these costs scale with the size of the network and the batch size? Are there any specific hardware or software requirements for efficient implementation? Providing these details would make the method more accessible to other researchers and facilitate its adoption in real-world applications. The authors could also discuss potential optimizations for the inversion process, such as using low-precision arithmetic or specialized hardware accelerators.

### Questions

The authors should provide more insights into the potential limitations of their approach and discuss the trade-offs involved in using reversible architectures for parallel training. Additionally, it would be helpful to provide more details on the implementation of the proposed method and its computational complexity.

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
