### Summary

The paper proposes a method to train Differentially Private (DP) Deep Neural Networks (DNN) without the need for per-sample gradient clipping, a process that biases gradient directions and is computationally expensive. The authors suggest using Lipschitz constrained networks to provide sensitivity bounds. They establish a link between the Lipschitz constant with respect to network inputs and parameters, proving that bounding the Lipschitz constant of each layer allows for DP training with privacy guarantees. This approach enables scalable computation of sensitivities and optimizes the gradient-to-noise ratio for fixed privacy guarantees.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a novel approach to train Differentially Private Deep Neural Networks without per-sample gradient clipping, which is a significant advancement in the field.
2. The authors provide a theoretical analysis that establishes a link between the Lipschitz constant with respect to network inputs and parameters. This is a valuable contribution to the understanding of Lipschitz networks.
3. The proposed method allows for scalable computation of sensitivities and provides guidance on optimizing the gradient-to-noise ratio for fixed privacy guarantees, which is practically useful.

### Weaknesses

#### Some Related Works


#### comment

1. The paper mentions that the proposed method is based on Gradient Norm Preserving (GNP) networks, which enforce orthogonality in the Jacobian of layers. However, enforcing strict orthogonality, especially for convolutions, is challenging and remains an active research area. The paper acknowledges this limitation but could provide more details on the practical implications and potential workarounds. Specifically, the paper does not discuss the numerical instability that can arise from attempting to enforce orthogonality with floating-point precision, which can lead to oscillations or divergence during training. Furthermore, the paper does not address how the proposed method handles non-linearities within the convolutional layers, which can further complicate the enforcement of GNP constraints.
2. The paper does not provide a detailed comparison of the proposed method with other existing approaches for differentially private training of deep neural networks, such as those based on regularization. It is unclear how the proposed method compares in terms of computational cost, memory requirements, and convergence speed. A more thorough comparison, including quantitative results, would be beneficial. For instance, the paper should compare the proposed method against DP-SGD with various clipping norms, and also against methods that use explicit regularization terms to enforce Lipschitz constraints, providing a clear picture of the trade-offs involved.

### Suggestions

The paper should delve deeper into the practical challenges of enforcing Gradient Norm Preserving (GNP) constraints, particularly within convolutional neural networks. While the paper acknowledges the difficulty of achieving strict orthogonality, it should provide a more detailed discussion of the numerical issues that arise during training. For example, the authors could explore the use of proximal operators or other numerical techniques to stabilize the enforcement of GNP constraints. Furthermore, the paper should investigate the impact of different non-linearities on the GNP property and propose specific strategies to mitigate any adverse effects. A more thorough analysis of the trade-offs between the strictness of the GNP constraint and the training stability would also be valuable. This could involve exploring different levels of approximation to orthogonality and analyzing their impact on both privacy and utility.

To strengthen the paper, a more comprehensive experimental evaluation is needed. The authors should compare their method against a wider range of baselines, including DP-SGD with various clipping norms and methods that use explicit regularization to enforce Lipschitz constraints. The comparison should not only focus on the final accuracy but also on the convergence speed, computational cost, and memory requirements. It would be beneficial to include a detailed analysis of the sensitivity of the proposed method to different hyperparameter settings, such as the learning rate and the noise multiplier. Furthermore, the paper should provide a more detailed explanation of the experimental setup, including the specific architectures used and the datasets used for evaluation. This would allow for a more thorough assessment of the method's performance and generalizability.

Finally, the paper should provide more practical guidance on how to implement the proposed method. This could include a discussion of the specific software libraries or tools that can be used to enforce GNP constraints and compute the Lipschitz constants. The authors should also provide a detailed explanation of the backpropagation process for bound computation, including any specific optimizations or techniques that can be used to improve efficiency. A step-by-step guide on how to train a neural network using the proposed method, including the selection of appropriate hyperparameters, would also be beneficial for practitioners. This would make the paper more accessible and increase its impact on the field.

### Questions

1. Can the authors provide more details on how the Lipschitz constant of each layer is bounded in practice? What are the computational costs associated with this process?
2. How does the proposed method compare to other existing approaches for differentially private training of deep neural networks in terms of performance and efficiency?
3. What are the potential limitations or challenges of the proposed method, and how can they be addressed in future work?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
