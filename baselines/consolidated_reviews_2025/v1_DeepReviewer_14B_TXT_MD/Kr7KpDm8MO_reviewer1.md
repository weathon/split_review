### Summary

This paper studies the impact of weight decay on the rotational movement of neuron weights in deep neural networks. The authors argue that weight decay leads to a state of "rotational equilibrium" where neurons achieve a balanced learning rate across layers. They provide theoretical analysis and experiments to demonstrate this effect across optimizers like Adam, Lion, and SGD with momentum.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper provides a novel perspective on weight decay, moving beyond traditional regularization views.

2. The analysis covers multiple optimizers, increasing the generalizability of the findings.

### Weaknesses

#### Some Related Works


#### comment

1. The theoretical analysis relies on simplifying assumptions about noise and equilibrium states, which may not fully capture real-world complexities. Specifically, the assumption that noise dominates gradient updates, leading to a random walk behavior, is a strong simplification. While this might hold in the initial stages of training, it's unclear how well it applies when the loss landscape becomes more complex and the gradients are no longer purely noise-driven. The analysis also assumes a steady-state equilibrium, which might not be reached in practice, especially with non-convex loss functions and varying learning rate schedules.

2. The practical implications of rotational equilibrium for hyperparameter tuning are not fully explored. While the paper introduces the concept of rotational equilibrium, it doesn't provide concrete guidance on how to leverage this understanding to improve hyperparameter selection. For example, how should one choose the learning rate, weight decay, and momentum parameters to achieve or maintain rotational equilibrium? The paper lacks a clear connection between the theoretical findings and practical hyperparameter optimization strategies.

3. The paper lacks a systematic study of how different initialization methods affect rotational equilibrium. The initialization of neural network weights can significantly impact the training dynamics, and it's crucial to understand how different initialization schemes interact with the proposed rotational equilibrium. For instance, do initializations that promote orthogonality or specific variance properties lead to faster convergence to rotational equilibrium? This aspect is not addressed, leaving a gap in the analysis.

4. The computational overhead of measuring and controlling rotational dynamics is not discussed. Implementing and monitoring rotational dynamics could introduce additional computational costs, especially for large-scale models. The paper does not quantify these costs or discuss their implications for practical applications. It's important to understand the trade-offs between the potential benefits of controlling rotational dynamics and the associated computational burden.

### Suggestions

To strengthen the theoretical analysis, the authors should consider relaxing the simplifying assumptions about noise and equilibrium states. Instead of assuming a random walk, they could explore models that incorporate more realistic gradient behaviors, such as those that account for the structure of the loss landscape and the correlation between gradients at different time steps. Furthermore, the analysis should be extended to investigate the transient behavior before equilibrium is reached, as this period can be critical for the overall training process. Techniques from stochastic differential equations or dynamical systems could be employed to model the evolution of weights more accurately. It would also be beneficial to provide a more rigorous definition of rotational equilibrium, perhaps using concepts from differential geometry or manifold learning, to better characterize the state and its properties.

To enhance the practical impact of the work, the authors should provide more concrete guidance on how to leverage the concept of rotational equilibrium for hyperparameter tuning. This could involve developing adaptive optimization algorithms that dynamically adjust hyperparameters based on the observed rotational dynamics. For example, the learning rate could be modulated to maintain a desired level of rotational equilibrium, or the weight decay could be adjusted to promote balanced rotation across layers. The authors could also explore the use of metrics derived from rotational dynamics, such as the variance of angular updates, to guide hyperparameter selection. Furthermore, it would be valuable to conduct experiments on a wider range of architectures and datasets to validate the generalizability of the findings and identify potential limitations.

Finally, the authors should investigate the impact of different initialization methods on rotational equilibrium. This could involve comparing the convergence behavior of different initializations, such as Xavier, He, or orthogonal initialization, in terms of their ability to achieve and maintain rotational equilibrium. The analysis should also consider the interplay between initialization and other hyperparameters, such as learning rate and weight decay. Additionally, the computational overhead of measuring and controlling rotational dynamics should be quantified and discussed. This could involve analyzing the time and memory requirements of the proposed methods and comparing them to standard optimization techniques. The authors should also explore potential optimizations to reduce the computational burden and make the approach more practical for large-scale applications.

### Questions

1. How does the concept of rotational equilibrium apply to architectures without normalization layers?

2. Can the authors provide more empirical evidence for the benefits of balanced rotation in other tasks?

3. How sensitive are the results to different learning rate schedules?

4. What are the trade-offs between controlling rotational dynamics and other regularization methods?

### Rating

3

### Confidence

3

**********
