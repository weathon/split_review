### Summary

This paper proposes a novel 1-bit fully quantized training (FQT) method that pushes the limit of FQT. Through convergence analysis, the authors propose Activation Gradient Pruning (AGP) to reduce the variance of the quantizer, thereby enhancing the convergence of quantized training. Subsequently, to address the issue of unaccelerated weight gradient computation, the paper presents a SCQ strategy. Finally, the paper proposes a framework that practically accelerates training, achieving a speedup of up to 5.13× compared to full precision training.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. This paper proposes a hardware-friendly 1-bit FQT method, which pushes the limit of FQT.
2. Through convergence analysis, the authors propose AGP to reduce the variance of the quantizer, thereby enhancing the convergence of quantized training.
3. Subsequently, to address the issue of unaccelerated weight gradient computation, the paper presents a SCQ strategy.
4. Finally, the paper proposes a framework that practically accelerates training, achieving a speedup of up to 5.13× compared to full precision training.

### Weaknesses

#### Some Related Works


#### comment

1. The authors mention that they make a first attempt towards achieving 1-bit FQT. However, there are some works on 1-bit QAT. The authors should discuss the differences between 1-bit QAT and 1-bit FQT. Specifically, the paper needs to clarify how the absence of gradient quantization in QAT impacts the training process compared to FQT, and what specific challenges arise when extending QAT techniques to a full 1-bit FQT setting. The discussion should include the implications for convergence, stability, and the potential for error accumulation during backpropagation.
2. The authors mention that AGP is an improvement based on per-group quantizers. However, the authors do not explain the limitations of per-group quantizers. The paper should elaborate on the specific drawbacks of per-group quantization, such as potential information loss due to coarse-grained quantization, and how AGP addresses these limitations. It should also discuss the trade-offs between the granularity of quantization and the resulting impact on model accuracy and training efficiency.
3. The authors mention that the convergence of FQT based on both Adam and SGD is influenced by the gradient variance, with SGD being more sensitive to variations in gradient variance. However, the authors do not explain the reasons behind this. The paper should provide a more detailed analysis of why SGD is more susceptible to gradient variance than Adam, possibly by examining the update rules of both optimizers and how they interact with noisy gradients. This should include a discussion of the adaptive learning rates in Adam and how they mitigate the effects of high gradient variance.
4. The authors mention that the current research frontier is 4-bit FQT. However, the authors do not explain why 4-bit FQT is the current research frontier. The paper should provide a more detailed explanation of the challenges that make 4-bit FQT a significant milestone, such as the trade-offs between computational efficiency, memory footprint, and model accuracy. It should also discuss the specific technical hurdles that need to be overcome to achieve effective training at this bit-width.
5. The authors mention that the speedup of the proposed method is well above a hundredfold. However, the authors do not explain why the speedup is well above a hundredfold. The paper should provide a more detailed analysis of the factors contributing to the observed speedup, including the computational cost of different operations in the training process and how the proposed method reduces these costs. It should also discuss the potential bottlenecks and limitations of the speedup, such as memory access patterns and communication overhead.

### Suggestions

The paper should provide a more thorough comparison between 1-bit QAT and 1-bit FQT. While both aim to reduce computational costs, the key difference lies in the quantization of gradients during backpropagation. QAT typically uses full-precision gradients, which limits the acceleration potential during training. The paper should discuss how the absence of gradient quantization in QAT affects the overall training process, particularly in terms of convergence speed and final model accuracy. Furthermore, the paper should elaborate on the specific challenges that arise when extending QAT techniques to a full 1-bit FQT setting. This includes the potential for error accumulation during backpropagation due to the low precision of both weights and gradients, and how the proposed method addresses these challenges. A detailed analysis of the trade-offs between the two approaches, including their respective advantages and limitations, would significantly enhance the paper's contribution.

To strengthen the discussion on per-group quantizers, the paper should delve deeper into their limitations. While per-group quantization offers a balance between accuracy and computational efficiency, it can suffer from information loss due to its coarse-grained nature. The paper should explain how the fixed quantization ranges within each group can lead to suboptimal representations, especially when the data distribution within a group is highly variable. The authors should also discuss how AGP addresses these limitations by adaptively pruning activation gradients, thereby reducing the variance of the quantizer and improving the overall training convergence. A more detailed explanation of the trade-offs between the granularity of quantization and the resulting impact on model accuracy and training efficiency would provide a more comprehensive understanding of the proposed method. This should include a discussion of how the choice of group size affects the performance of both per-group quantization and AGP.

The paper should provide a more detailed analysis of why SGD is more sensitive to gradient variance than Adam. This should include a discussion of the update rules of both optimizers and how they interact with noisy gradients. Specifically, the paper should explain how the adaptive learning rates in Adam, which are based on the first and second moments of the gradients, help to mitigate the effects of high gradient variance. In contrast, SGD uses a fixed learning rate, which can lead to unstable updates when the gradient variance is high. The paper should also discuss the implications of this difference for the choice of optimizer in low-precision training scenarios. A more detailed analysis of the convergence properties of both optimizers under different gradient variance conditions would provide valuable insights into the behavior of the proposed method.

### Questions

Please refer to the Weaknesses.

### Rating

6

### Confidence

4

**********
