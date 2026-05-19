### Summary

This paper proposes a novel predictive differential training (PDT) framework that accelerates neural network training by predicting future weights using Koopman operator theory. The PDT selectively applies these predictions to subsets of parameters exhibiting "good" prediction performance, while using a mask to control the prediction rate. The authors demonstrate that PDT consistently outperforms baseline methods across various architectures and optimizers, achieving faster convergence and higher accuracy with fewer epochs. The paper also includes a thorough analysis of the masking strategy and its impact on performance.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a unique approach to accelerating neural network training by leveraging Koopman operator theory for weight prediction. This is a novel contribution to the field of deep learning optimization.
2. The masking strategy is well-designed and empirically validated, showing its effectiveness in selecting parameters for prediction.
3. The experimental results are comprehensive, covering multiple architectures and optimizers, and demonstrating significant improvements in convergence speed and accuracy.
4. The paper provides a detailed analysis of the masking strategy and its impact on performance, offering valuable insights for future research.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion on the computational overhead of the Koopman-based predictions, especially in terms of memory usage and inference time.
2. While the paper demonstrates the effectiveness of PDT on various architectures, it would be valuable to explore its performance on larger and more complex models, such as those with billions of parameters.
3. The sensitivity of the masking strategy to different hyperparameters, such as the prediction interval and the number of past epochs, could be further investigated and discussed.
4. The paper could provide more insights into the limitations of the proposed approach and potential areas for improvement.

### Suggestions

The paper should include a more thorough analysis of the computational costs associated with the Koopman-based predictions. Specifically, the memory footprint of storing the Koopman matrices and the time required for performing the DMD algorithm at each step should be quantified and compared against standard SGD. This analysis should not only focus on the theoretical complexity but also provide empirical measurements on different hardware configurations. Furthermore, the authors should explore techniques to mitigate these costs, such as low-rank approximations or efficient implementations of DMD, which could make the approach more practical for large-scale models. A detailed breakdown of the computational overhead would provide a more complete picture of the method's feasibility.

To strengthen the empirical evaluation, the authors should conduct experiments on larger and more complex models, such as those with billions of parameters. This would demonstrate the scalability of the proposed approach and its applicability to real-world scenarios. The current experiments are limited to relatively small architectures, which may not accurately reflect the performance of the method on more complex models. The authors should also investigate the impact of different hyperparameters, such as the prediction interval and the number of past epochs, on the performance of the masking strategy. A sensitivity analysis of these parameters would provide valuable insights into the robustness of the method and its ability to generalize to different training scenarios. It would be beneficial to show how these parameters are tuned for different model sizes and architectures.

Finally, the paper should provide a more comprehensive discussion of the limitations of the proposed approach and potential areas for improvement. For example, the authors should discuss the potential for error accumulation in the Koopman predictions and how this might affect the overall performance of the method. They should also explore the limitations of the masking strategy and whether it is always able to identify the most promising parameters for prediction. Furthermore, the authors should discuss the potential for instability in the training process when using predicted weights and how this can be mitigated. A more thorough discussion of these limitations would provide a more balanced and realistic assessment of the proposed method.

### Questions

Please refer to the weaknesses.

### Rating

6

### Confidence

2

**********
