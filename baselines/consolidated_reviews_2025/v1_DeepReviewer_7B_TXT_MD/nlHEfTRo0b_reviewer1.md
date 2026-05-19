### Summary

This paper proposes PIDO, a physics-informed dynamics representation learner that learns shared latent representations of dynamical systems with varying properties. The proposed method is evaluated on several benchmark problems and shows improved performance compared to existing methods.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

- The paper is well-structured and easy to follow.
- The paper provides a comprehensive review of related work and clearly positions the proposed method within the existing literature.
- The proposed method is evaluated on several benchmark problems and shows improved performance compared to existing methods.
- The paper includes ablation studies to demonstrate the effectiveness of the proposed regularization techniques.

### Weaknesses

#### Some Related Works


#### comment

 - The paper lacks a detailed discussion of the limitations of the proposed method and potential directions for future work.
- The paper does not provide a thorough analysis of the computational cost of the proposed method, especially in comparison to other methods.
- The paper does not provide a clear explanation of how the proposed method handles complex or chaotic systems.
- The paper does not provide a clear explanation of how the proposed method handles systems with multiple time scales.

### Suggestions

The paper should include a more detailed discussion of the limitations of the proposed method. For example, the authors should discuss the sensitivity of the method to the choice of hyperparameters, such as the latent space dimensionality and the regularization parameters. It would also be beneficial to discuss the potential failure modes of the method, such as when the underlying dynamical system is highly nonlinear or chaotic. Furthermore, the authors should provide a more thorough analysis of the computational cost of the proposed method, especially in comparison to other methods. This analysis should include a discussion of the time and memory requirements of the method, as well as how these requirements scale with the size of the problem. It would also be helpful to provide a comparison of the training and inference times of the proposed method with other methods. The paper should also provide a more detailed explanation of how the proposed method handles complex or chaotic systems. For example, the authors should discuss how the latent space representation captures the underlying dynamics of the system, and how this representation can be used to make predictions over long time horizons. It would also be beneficial to provide a comparison of the performance of the proposed method on different types of dynamical systems, such as those with different levels of chaos or complexity. Finally, the paper should provide a more detailed explanation of how the proposed method handles systems with multiple time scales. For example, the authors should discuss how the latent space representation captures the different time scales of the system, and how this representation can be used to make predictions over long time horizons. It would also be beneficial to provide a comparison of the performance of the proposed method on different types of dynamical systems, such as those with different levels of multiple time scales.

### Questions

- How does the proposed method handle complex or chaotic systems?
- How does the proposed method handle systems with multiple time scales?
- How does the computational cost of the proposed method compare to other methods?

### Rating

6

### Confidence

2

**********
