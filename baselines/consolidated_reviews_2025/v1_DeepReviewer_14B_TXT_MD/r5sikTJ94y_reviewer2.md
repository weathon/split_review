### Summary

This paper addresses the issue of ADC quantization in In-Memory Computing (IMC) systems. The authors propose a method called RAOQ to mitigate ADC quantization error by adjusting the statistics of activations and weights through an activation-shifting approach (A-shift) and a weight reshaping technique (W-reshape). Additionally, they introduce a bit augmentation method (BitAug) to improve SGD-based optimization. The proposed RAOQ method demonstrates consistently high performance across different scales of neural network models for image classification, object detection, and natural language processing (NLP) tasks at various ADC bit precisions.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The authors provide a comprehensive analysis of the relationship between neural network activations, weights, and ADC quantization. This analysis serves as the foundation for their proposed methods.
2. The proposed RAOQ method consistently achieves high performance across different scales of neural network models and various ADC bit precisions. This demonstrates the effectiveness and robustness of their approach.
3. The authors evaluate their methods on a wide range of tasks, including image classification, object detection, and natural language processing (NLP). This showcases the versatility and applicability of their proposed techniques.

### Weaknesses

#### Some Related Works


#### comment

1. The authors propose the A-shift method to maximize the 2nd moment of the activation. However, the rationale behind this approach is not clearly explained. It is unclear why maximizing the 2nd moment specifically would lead to improved performance in the context of ADC quantization. A more detailed explanation of the underlying mathematical reasoning and its connection to quantization error is needed.
2. The authors introduce a kurtosis loss to encourage the weight distribution to have a larger variance. However, they do not provide a detailed explanation of how this loss function is incorporated into the training process. It is unclear how the kurtosis loss is balanced with the primary task loss, and how this balance affects the overall training dynamics. Furthermore, the specific implementation details of the kurtosis loss calculation are missing.
3. The authors introduce trainable parameters in both the A-shift and W-reshape methods. However, they do not provide any discussion or analysis of these parameters. It is unclear how these parameters are initialized, how they are updated during training, and what their sensitivity is to different initializations or learning rates. A more thorough analysis of these parameters is needed to understand their impact on the overall performance.

### Suggestions

The paper would benefit from a more detailed explanation of the A-shift method's rationale. Specifically, the authors should elaborate on why maximizing the 2nd moment of the activation is beneficial for ADC quantization. A mathematical analysis connecting the 2nd moment to the quantization error would be valuable. For instance, they could discuss how a larger 2nd moment affects the distribution of activation values within the quantization bins, and how this impacts the overall quantization accuracy. Furthermore, it would be helpful to provide a visual representation of the activation distribution before and after applying the A-shift method, to better illustrate the effect of maximizing the 2nd moment. This would provide a more intuitive understanding of the method's effectiveness.

To address the lack of clarity regarding the kurtosis loss, the authors should provide a more detailed explanation of its implementation. This should include the specific mathematical formula used to calculate the kurtosis loss, and how it is integrated into the overall loss function. It is crucial to explain how the kurtosis loss is weighted relative to the primary task loss, and how this weighting affects the training process. The authors should also discuss the potential trade-offs between minimizing the kurtosis loss and maintaining the model's accuracy on the primary task. Furthermore, it would be beneficial to provide an ablation study that examines the impact of different kurtosis loss weights on the final performance. This would help to understand the sensitivity of the method to the kurtosis loss parameter.

Finally, the authors should provide a more thorough analysis of the trainable parameters introduced in the A-shift and W-reshape methods. This should include a discussion of how these parameters are initialized, and how they are updated during training. It would be beneficial to provide a sensitivity analysis of these parameters, examining how the final performance is affected by different initializations and learning rates. The authors should also discuss the potential for these parameters to become unstable during training, and how this can be mitigated. Furthermore, it would be helpful to provide a visualization of how these parameters change during training, to better understand their role in the overall optimization process. This would provide a more complete understanding of the proposed methods.

### Questions

1. What is the rationale behind maximizing the 2nd moment of the activation in the A-shift method?
2. How is the kurtosis loss incorporated into the training process, and how does it affect the overall training dynamics?
3. How are the trainable parameters in the A-shift and W-reshape methods initialized and updated during training? What is their sensitivity to different initializations or learning rates?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
