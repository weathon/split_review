### Summary

This paper investigates the effects of weight decay on the update behavior of individual neurons in deep neural networks. The authors propose that weight decay leads to a state of rotational equilibrium, where neurons achieve a balanced average rotation across layers and components. They analyze this phenomenon across various optimizers, including AdamW, Adam with L2-regularization, Lion, and SGD with momentum, and validate their findings through experiments. The study also introduces "Rotational Variants" (RVs) of optimizers, which directly control angular updates, offering an alternative to weight decay and normalization techniques.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-organized and clearly written, making complex concepts accessible to readers. The use of visual aids, such as figures and tables, effectively illustrates key points and supports the theoretical analysis.
2. The authors provide a thorough and rigorous analysis of the neuronal update dynamics, particularly in the context of scale-invariant weights. The derivation of equilibrium states and the examination of both transient and steady-state behaviors contribute to a deeper understanding of optimizer performance.
3. The paper's exploration of rotational equilibrium and its impact on optimizer behavior is a valuable contribution to the field. The authors' analysis sheds light on the mechanisms by which weight decay influences learning rates and provides a new perspective on widely used regularization techniques.

### Weaknesses

#### Some Related Works


#### comment

1. The paper's analysis relies heavily on the assumption of a random walk for parameter updates, which may not fully capture the complexities of real-world neural network training. While the authors acknowledge this limitation, further investigation into how the findings generalize to more realistic scenarios would strengthen the paper's conclusions. Specifically, the assumption that gradients are uncorrelated and have constant variance, which is implicit in the random walk model, is unlikely to hold true during the course of training. The paper does not address how the changing loss landscape and the adaptive nature of optimizers might affect the observed rotational equilibrium.
2. The paper's focus on scale-invariant weights, while insightful, may limit the generalizability of the findings to other types of neural network architectures and settings. The analysis does not consider the impact of different activation functions, which can introduce scale dependencies, or the effects of batch normalization, which can alter the effective learning rate of different layers. The paper should discuss how these factors might affect the rotational equilibrium and the applicability of the proposed Rotational Variants.
3. The paper could benefit from a more detailed exploration of the limitations of the proposed Rotational Variants (RVs) of optimizers. While the authors demonstrate that RVs can achieve similar performance to standard optimizers, they do not fully address the potential drawbacks of these methods. For example, the paper does not discuss the computational overhead of calculating the angular updates, or whether the RVs are as robust to noisy gradients as standard optimizers. A more thorough analysis of these limitations would provide a more balanced view of the proposed methods.

### Suggestions

To strengthen the paper, the authors should investigate the validity of the random walk assumption more thoroughly. This could involve analyzing the autocorrelation of gradients during training to assess the degree of correlation between successive updates. Furthermore, the authors could explore how the variance of the gradients changes over time and how this affects the rotational equilibrium. It would be beneficial to conduct experiments on a wider range of architectures and datasets to assess the generalizability of the findings. Specifically, the authors should consider including experiments with different activation functions, batch normalization, and other common architectural components. This would help to determine the extent to which the observed rotational equilibrium is a general phenomenon or specific to certain types of networks. Additionally, the authors should explore the impact of different learning rate schedules on the rotational equilibrium, as the current analysis assumes a fixed learning rate. This would provide a more complete picture of the dynamics of the proposed Rotational Variants.

In addition, the authors should provide a more detailed analysis of the computational cost and robustness of the proposed Rotational Variants. This could involve comparing the training time and memory usage of the RVs with standard optimizers. The authors should also investigate the sensitivity of the RVs to noisy gradients and different initialization schemes. It would be useful to explore whether the RVs require any specific hyperparameter tuning or whether they can be used with default settings. A more thorough analysis of these practical aspects would make the proposed methods more accessible and useful to the broader research community. Furthermore, the authors should consider the potential for adaptive angular update strategies, where the magnitude of the angular update is adjusted based on the current state of the network. This could potentially lead to more efficient and robust training.

Finally, the authors should discuss the potential limitations of the proposed approach in more detail. For example, the paper could explore whether the rotational equilibrium is always desirable or whether there are situations where it might be beneficial to deviate from this state. The authors should also consider the potential impact of the rotational equilibrium on the generalization performance of the network. It would be valuable to investigate whether the RVs lead to better or worse generalization compared to standard optimizers. Addressing these limitations would provide a more balanced and nuanced view of the proposed methods and their potential impact on the field. The authors should also discuss the potential for combining the Rotational Variants with other regularization techniques, such as dropout or batch normalization, to further improve the performance and robustness of the network.

### Questions

1. Could the authors elaborate on how the random walk assumption affects the generalizability of their findings to real-world neural network training? Are there specific scenarios where this assumption might break down?
2. How do the proposed Rotational Variants (RVs) compare to standard optimizers in terms of computational efficiency and robustness to noisy gradients? Are there any practical limitations or trade-offs associated with using RVs?
3. The paper focuses on scale-invariant weights. How might the findings differ for other types of weights or neural network architectures? Are there any specific architectural components or settings where the concept of rotational equilibrium might not apply?

### Rating

6

### Confidence

2

**********
