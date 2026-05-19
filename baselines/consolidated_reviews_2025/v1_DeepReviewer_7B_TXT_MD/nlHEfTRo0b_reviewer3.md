### Summary

The paper introduces PIDO, a physics-informed neural PDE solver that leverages shared intrinsic structures among dynamical systems to enhance generalization across various PDE configurations, including initial conditions, PDE coefficients, and training time horizons. The authors propose a novel approach by diagnosing and addressing challenges within the latent space, specifically through latent dynamics smoothing and latent dynamics alignment regularization. These techniques improve training stability and extrapolation performance, as demonstrated through experiments on 1D and 2D combined equations and Navier-Stokes equations. The paper also explores the transferability of PIDO's learned representations to downstream tasks such as long-term integration and inverse problems, showcasing its robustness and adaptability.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and organized, making it easy to follow and understand. The authors clearly articulate the problem, methodology, and results, which enhances the overall readability and accessibility of the paper.
2. The proposed method, PIDO, is innovative and addresses a significant gap in the field of physics-informed neural PDE solvers. By leveraging shared intrinsic structures among dynamical systems, PIDO demonstrates improved generalization across various PDE configurations, including initial conditions, PDE coefficients, and training time horizons.
3. The authors provide a thorough evaluation of PIDO through extensive experiments on 1D and 2D combined equations and Navier-Stokes equations. The results demonstrate the effectiveness of the proposed method in improving training stability and extrapolation performance.
4. The paper also explores the transferability of PIDO's learned representations to downstream tasks such as long-term integration and inverse problems, showcasing its robustness and adaptability.

### Weaknesses

#### Some Related Works


#### comment

1. While the paper demonstrates the effectiveness of PIDO on the chosen benchmarks, it would be beneficial to include a more detailed analysis of the computational cost and scalability of the proposed method. Specifically, the paper should provide a breakdown of the computational complexity of each component of the model, such as the auto-decoder, neural ODE, and the physics-informed loss calculations. Furthermore, it would be valuable to see how the training time and memory requirements scale with the size of the problem, the number of training samples, and the dimensionality of the latent space. This analysis should also consider the impact of different hardware configurations on the performance of the model.
2. The paper could benefit from a more in-depth discussion of the limitations of the proposed method. For example, it would be helpful to explore scenarios where PIDO might struggle, such as highly chaotic systems or systems with discontinuities. The paper should also discuss the sensitivity of the method to hyperparameter choices, such as the learning rate, the size of the latent space, and the regularization parameters. A more thorough analysis of these limitations would provide a more balanced view of the method's capabilities and potential areas for improvement. It would also be useful to see a comparison of PIDO with other methods in terms of robustness to noise and perturbations in the input data.
3. The paper lacks a thorough discussion of the potential for extending the proposed method to more complex PDE systems. For example, the authors could discuss the challenges of applying PIDO to systems with higher-order derivatives or nonlinearities. It would also be useful to explore the potential for incorporating additional physics-based constraints into the model, such as conservation laws or boundary conditions. This would allow the model to be applied to a wider range of PDE systems and to more accurately capture the underlying physics. The authors should also discuss the potential for using the latent space representation to improve the interpretability of the model. For example, the authors could explore the possibility of visualizing the latent space and identifying patterns or structures that correspond to specific physical phenomena.

### Suggestions

The paper would significantly benefit from a more detailed analysis of the computational cost and scalability of the proposed PIDO method. The authors should provide a breakdown of the computational complexity of each component, including the auto-decoder, the neural ODE solver, and the physics-informed loss calculations. This analysis should not only consider the theoretical complexity but also include empirical measurements of training time and memory usage for different problem sizes, latent space dimensions, and hardware configurations. For instance, the authors could present a table showing how the training time scales with the number of training samples and the dimensionality of the latent space. Furthermore, it would be valuable to compare the computational cost of PIDO with other state-of-the-art methods for solving PDEs, such as traditional numerical solvers and other neural PDE solvers. This would provide a clearer understanding of the practical applicability of the proposed method and its trade-offs in terms of computational resources.

In addition to computational cost, a more in-depth discussion of the limitations of PIDO is needed. The authors should explore scenarios where the method might struggle, such as highly chaotic systems or systems with discontinuities. For example, the paper could include experiments on PDEs with known chaotic behavior or sharp transitions to assess the robustness of PIDO. Furthermore, the sensitivity of the method to hyperparameter choices should be thoroughly investigated. The authors should provide a systematic study of the impact of parameters such as the learning rate, the size of the latent space, and the regularization parameters on the performance of the model. This analysis should include guidelines for selecting appropriate hyperparameter values for different types of problems. It would also be useful to compare the robustness of PIDO to other methods in terms of their sensitivity to noise and perturbations in the input data. This could be done by adding controlled amounts of noise to the input data and measuring the impact on the accuracy of the model's predictions.

Finally, the paper should include a more thorough discussion of the potential for extending the proposed method to more complex PDE systems. The authors should discuss the challenges of applying PIDO to systems with higher-order derivatives or nonlinearities. For example, they could explore how the latent space representation can be adapted to handle these more complex systems. It would also be valuable to explore the potential for incorporating additional physics-based constraints into the model, such as conservation laws or boundary conditions. This would allow the model to be applied to a wider range of PDE systems and to more accurately capture the underlying physics. The authors should also discuss the potential for using the latent space representation to improve the interpretability of the model. For example, they could explore the possibility of visualizing the latent space and identifying patterns or structures that correspond to specific physical phenomena. This would provide a deeper understanding of the model's internal workings and its ability to capture the underlying physics.

### Questions

1. How does the proposed method handle systems with higher-order derivatives or nonlinearities? Are there any specific modifications or extensions needed to apply PIDO to such systems?
2. Can the latent space representation be used to improve the interpretability of the model? For example, can the latent space be visualized or analyzed to gain insights into the underlying physics of the system?
3. How does the performance of PIDO compare to other state-of-the-art methods on more complex PDE systems, such as those with discontinuities or chaotic behavior?

### Rating

6

### Confidence

2

**********
