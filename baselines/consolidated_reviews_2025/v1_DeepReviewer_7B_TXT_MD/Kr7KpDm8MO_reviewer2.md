### Summary

This paper studies the update dynamics of individual neurons in neural networks through the lens of weight decay. The authors analyze the equilibrium norm and angular update of a neuron's weight vector under a simplified random walk model, and show how weight decay interacts with gradient descent to balance the rotation of weight vectors across neurons. They also propose a rotational variant of AdamW (AdamW-RV) that constrains the angular updates, and validate their findings through experiments.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper provides a detailed analysis of the update dynamics of individual neurons in neural networks through the lens of weight decay.
2. The authors derive the equilibrium norm and angular update of a neuron's weight vector under a simplified random walk model, and show how weight decay interacts with gradient descent to balance the rotation of weight vectors across neurons.
3. The paper proposes a rotational variant of AdamW (AdamW-RV) that constrains the angular updates, and validate their findings through experiments.

### Weaknesses

#### Some Related Works


#### comment

1. The theoretical analysis relies on a simplified random walk model, which may not accurately reflect the complex dynamics of neural network training. The assumption of a random walk, while simplifying the analysis, neglects the fact that weight updates are highly structured and influenced by the specific loss landscape and data distribution. This simplification may lead to a theoretical framework that is not directly applicable to real-world scenarios, where the interaction between weight decay and gradient descent is likely more intricate than a simple random walk.
2. The experiments are limited to a few datasets and models, which may not be sufficient to generalize the findings. The choice of datasets and models, while relevant, might not cover the full spectrum of neural network architectures and training scenarios. For instance, the absence of experiments on larger, more complex models and datasets could limit the generalizability of the conclusions. Furthermore, the paper does not explore the sensitivity of the results to different hyperparameter settings, which is crucial for practical applications.

### Suggestions

To strengthen the theoretical analysis, the authors should consider exploring more realistic models of weight update dynamics. Instead of relying solely on a random walk model, they could investigate models that incorporate aspects of the loss landscape, such as curvature or the presence of saddle points. This could involve analyzing the Hessian of the loss function or using techniques from dynamical systems theory to model the evolution of weight vectors. Furthermore, the authors could explore the impact of different regularization techniques beyond weight decay, such as dropout or batch normalization, on the derived equilibrium norms and angular updates. This would provide a more comprehensive understanding of how various regularization methods interact with the optimization process. The theoretical analysis should also consider the impact of different activation functions and network architectures on the update dynamics.

To address the limitations of the experimental evaluation, the authors should conduct experiments on a wider range of datasets and models. This should include experiments on larger, more complex datasets, such as ImageNet or COCO, and on more diverse model architectures, such as transformers or graph neural networks. This would help to assess the generalizability of the findings and identify potential limitations of the proposed approach. Additionally, the authors should perform a thorough hyperparameter sensitivity analysis to determine the robustness of their results to different settings. This should include varying the learning rate, weight decay, and other relevant hyperparameters and analyzing their impact on the observed equilibrium norms and angular updates. Such an analysis would provide valuable insights into the practical implications of the theoretical findings. The experimental section should also include a more detailed analysis of the convergence behavior of the proposed method, including the number of epochs required for convergence and the sensitivity of the results to the choice of hyperparameters.

Finally, the authors should provide a more detailed discussion of the practical implications of their findings. While the theoretical analysis provides valuable insights into the update dynamics of neural networks, it is important to translate these insights into actionable recommendations for practitioners. This could involve proposing specific strategies for tuning hyperparameters, designing new regularization techniques, or developing more efficient optimization algorithms. The authors should also discuss the limitations of their approach and identify areas for future research. This would help to contextualize their work and highlight its potential impact on the field.

### Questions

1. How does the simplified random walk model capture the complex dynamics of neural network training?
2. How do the findings generalize to other neural network architectures and datasets?

### Rating

6

### Confidence

2

**********
