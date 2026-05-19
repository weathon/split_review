### Summary

This paper proposes a novel predictive differential training (PDT) framework that accelerates neural network training by predicting future weights using Koopman operator theory. PDT selectively applies these predictions to subsets of parameters exhibiting "good" prediction performance, while using a mask to control the prediction rate. The authors demonstrate that PDT consistently outperforms baseline methods across various architectures and optimizers, achieving faster convergence and higher accuracy with fewer epochs. The paper also includes a thorough analysis of the masking strategy and its impact on performance.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper introduces a unique approach to accelerating neural network training by leveraging Koopman operator theory for weight prediction.
- The masking strategy is well-designed and empirically validated, showing its effectiveness in selecting parameters for prediction.
- The experimental results are comprehensive, covering multiple architectures and optimizers, and demonstrating significant improvements in convergence speed and accuracy.
- The paper provides a detailed analysis of the masking strategy and its impact on performance, offering valuable insights for future research.

### Weaknesses

#### Some Related Works


#### comment

 - The paper could benefit from a more detailed discussion on the computational overhead of the Koopman-based predictions, especially in terms of memory usage and inference time.
- While the paper demonstrates the effectiveness of PDT on various architectures, it would be valuable to explore its performance on larger and more complex models, such as those with billions of parameters.
- The sensitivity of the masking strategy to different hyperparameters, such as the prediction interval and the number of past epochs, could be further investigated and discussed.
- The paper could provide more insights into the limitations of the proposed approach and potential areas for improvement.

### Suggestions

The paper should delve deeper into the practical implications of using Koopman operator theory for weight prediction. While the theoretical framework is interesting, the computational cost associated with DMD, particularly the memory footprint and inference time, needs more thorough analysis. The authors should provide a detailed breakdown of the memory usage for storing the Koopman matrices and the time required for performing the DMD algorithm at each step. Furthermore, it would be beneficial to compare the inference time of the proposed method with that of standard SGD, not just in terms of wall-clock time, but also in terms of operations per second. This would provide a more complete picture of the computational overhead introduced by the Koopman-based predictions. The authors should also explore techniques to mitigate these costs, such as low-rank approximations or efficient implementations of DMD.

To strengthen the empirical evaluation, the authors should conduct experiments on larger and more complex models, such as those with billions of parameters. This would demonstrate the scalability of the proposed approach and its applicability to real-world scenarios. The current experiments are limited to relatively small architectures, which may not accurately reflect the performance of the method on more complex models. The authors should also investigate the impact of different hyperparameters, such as the prediction interval and the number of past epochs, on the performance of the masking strategy. A sensitivity analysis of these parameters would provide valuable insights into the robustness of the method and its ability to generalize to different training scenarios. Specifically, the authors should explore how the optimal values of these parameters change with the size and complexity of the model.

Finally, the paper should provide a more comprehensive discussion of the limitations of the proposed approach and potential areas for improvement. For example, the authors should discuss the potential for error accumulation in the Koopman predictions and how this might affect the overall performance of the method. They should also explore the limitations of the masking strategy and whether it is always able to identify the most promising parameters for prediction. Furthermore, the authors should discuss the potential for instability in the training process when using predicted weights and how this can be mitigated. A more thorough discussion of these limitations would provide a more balanced and realistic assessment of the proposed method.

### Questions

- How does the computational cost of the Koopman-based predictions compare to standard SGD in terms of memory usage and inference time?
- What are the potential limitations of the masking strategy, and how can they be addressed?
- Can the proposed approach be extended to other types of neural network architectures, such as transformers or recurrent neural networks?
- How does the performance of PDT vary with different hyperparameters, such as the prediction interval and the number of past epochs?

### Rating

6

### Confidence

3

**********
