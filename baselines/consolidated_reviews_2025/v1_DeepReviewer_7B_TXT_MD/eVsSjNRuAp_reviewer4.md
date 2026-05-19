### Summary

This paper introduces a novel predictive differential training (PDT) framework that leverages Koopman operator theory to accelerate neural network training. The PDT framework selectively applies predictions to subsets of parameters with "good" prediction performance, using a masking strategy to control the prediction rate. The authors demonstrate that PDT consistently outperforms baseline methods across various architectures and optimizers, achieving faster convergence and higher accuracy with fewer epochs. The paper also includes a thorough analysis of the masking strategy and its impact on performance.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel predictive differential training (PDT) framework that leverages Koopman operator theory to accelerate neural network training. This is a creative combination of control theory and deep learning optimization, which is a significant contribution to the field.
2. The masking strategy is well-designed and empirically validated, showing its effectiveness in selecting parameters for prediction. The authors provide a detailed analysis of the masking strategy and its impact on performance, offering valuable insights for future research.
3. The experimental results are comprehensive, covering multiple architectures and optimizers, and demonstrating significant improvements in convergence speed and accuracy.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion on the computational overhead of the Koopman-based predictions, especially in terms of memory usage and inference time. While the authors mention that the computational load of the Koopman-related calculations is comparable to that of batch-level updates, a more thorough analysis of the actual memory footprint and inference time would be valuable. This is particularly important for large-scale models where the overhead of these operations could become a bottleneck.
2. While the paper demonstrates the effectiveness of PDT on various architectures, it would be valuable to explore its performance on larger and more complex models, such as those with billions of parameters. The current experiments are limited to relatively small architectures, which may not accurately reflect the performance of the method on more complex models. It is unclear how the masking strategy would scale to models with significantly more parameters, and whether the benefits of selective prediction would still be maintained.
3. The sensitivity of the masking strategy to different hyperparameters, such as the prediction interval and the number of past epochs, could be further investigated and discussed. The paper mentions that the starting epoch for acceleration must be greater than or equal to the number of epochs used to build the snapshot, but it does not provide a detailed analysis of how this parameter affects the overall performance. A more thorough investigation of the sensitivity of the method to these hyperparameters would be valuable.

### Suggestions

The authors should provide a more detailed analysis of the computational costs associated with the Koopman-based predictions. This should include a breakdown of the memory usage for storing the Koopman matrices and the time required for performing the DMD algorithm at each step. It would be beneficial to compare the actual memory footprint and inference time of the proposed method with standard SGD, not just in terms of theoretical complexity, but also in terms of practical measurements. This analysis should also consider the impact of different hardware configurations on the computational overhead. Furthermore, the authors should explore techniques to mitigate these costs, such as low-rank approximations or efficient implementations of DMD, which could make the approach more practical for large-scale models. A detailed discussion of these practical considerations would significantly strengthen the paper.

To address the concern about the scalability of the method, the authors should conduct experiments on larger and more complex models, such as those with billions of parameters. This would demonstrate the applicability of the proposed approach to real-world scenarios. The authors should also investigate how the masking strategy scales with the number of parameters and whether the benefits of selective prediction are maintained in larger models. It would be valuable to analyze the performance of the method on different types of layers, such as convolutional layers and fully connected layers, to understand how the masking strategy interacts with different architectural components. Additionally, the authors should explore the impact of different hyperparameters, such as the prediction interval and the number of past epochs, on the performance of the masking strategy. A more detailed analysis of these parameters would provide valuable insights into the robustness of the method and its ability to generalize to different training scenarios.

Finally, the authors should provide more guidance on how to select appropriate values for the hyperparameters of the masking strategy, such as the prediction interval and the number of past epochs. The paper mentions that the starting epoch for acceleration must be greater than or equal to the number of epochs used to build the snapshot, but it does not provide a detailed analysis of how this parameter affects the overall performance. A more thorough investigation of the sensitivity of the method to these hyperparameters would be valuable. The authors should also discuss the potential limitations of the masking strategy and whether it is always able to identify the most promising parameters for prediction. A more comprehensive discussion of these practical considerations would enhance the paper's overall impact and usefulness.

### Questions

1. How does the computational cost of the Koopman-based predictions compare to standard SGD in terms of memory usage and inference time?
2. What are the limitations of the masking strategy, and how can they be addressed?
3. Can the proposed approach be extended to other types of neural network architectures, such as transformers or recurrent neural networks?
4. How does the performance of PDT vary with different hyperparameters, such as the prediction interval and the number of past epochs?

### Rating

6

### Confidence

2

**********
