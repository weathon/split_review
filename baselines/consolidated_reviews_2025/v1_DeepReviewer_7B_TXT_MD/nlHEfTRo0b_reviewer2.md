### Summary

The paper introduces PIDO, a physics-informed neural PDE solver designed to enhance generalization across different PDE configurations, including initial conditions, PDE coefficients, and training time horizons. By leveraging shared intrinsic structures among dynamical systems, PIDO projects solutions into a low-dimensional latent space and learns the dynamics within this space. The authors address challenges in physics-informed loss, such as instability during training and degradation in time extrapolation, by proposing regularization techniques—latent dynamics smoothing and latent dynamics alignment. These techniques improve training stability and extrapolation performance, as demonstrated through experiments on 1D and 2D combined equations and Navier-Stokes equations.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written, with clear explanations of the problem, methodology, and results. The motivation for addressing the limitations of existing methods is well-articulated, and the proposed solutions are presented in a logical and understandable manner.
2. The paper introduces a novel approach by combining physics-informed training with latent space dynamics modeling. The proposed regularization techniques, latent dynamics smoothing and latent dynamics alignment, are innovative and contribute to the field of neural PDE solvers.
3. The experiments are comprehensive, covering both 1D and 2D problems, and include comparisons with state-of-the-art methods. The results demonstrate the effectiveness of PIDO in generalizing across different PDE configurations and time horizons.

### Weaknesses

#### Some Related Works


#### comment

1. While the paper demonstrates the effectiveness of PIDO on the chosen benchmarks, it would be beneficial to include a more detailed analysis of the computational cost and scalability of the proposed method. Specifically, the paper should provide a breakdown of the computational complexity of each component of the model, such as the auto-decoder, neural ODE, and the physics-informed loss calculations. Furthermore, it would be valuable to see how the training time and memory requirements scale with the size of the problem, the number of training samples, and the dimensionality of the latent space. This analysis should also consider the impact of different hardware configurations on the performance of the model.
2. The paper could benefit from a more in-depth discussion of the limitations of the proposed method. For example, it would be helpful to explore scenarios where PIDO might struggle, such as highly chaotic systems or systems with discontinuities. The paper should also discuss the sensitivity of the method to hyperparameter choices, such as the learning rate, the size of the latent space, and the regularization parameters. A more thorough analysis of these limitations would provide a more balanced view of the method's capabilities and potential areas for improvement. It would also be useful to see a comparison of PIDO with other methods in terms of robustness to noise and perturbations in the input data.

### Suggestions

To address the computational cost concerns, the authors should provide a detailed analysis of the time and memory complexity of each component of the proposed model. This analysis should include a breakdown of the operations involved in the auto-decoder, the neural ODE solver, and the physics-informed loss calculation. For example, the authors could provide a table that shows the computational cost of each component as a function of the input size, the latent space dimensionality, and the number of training samples. Furthermore, the authors should provide empirical results on the training time and memory usage of the model for different problem sizes and hardware configurations. This would allow readers to better understand the scalability of the method and its suitability for different applications. It would also be beneficial to compare the computational cost of PIDO with other state-of-the-art methods for solving PDEs, such as traditional numerical solvers and other neural PDE solvers.

To address the limitations of the method, the authors should provide a more in-depth discussion of scenarios where PIDO might struggle. For example, the authors could explore the performance of the method on highly chaotic systems or systems with discontinuities. It would be useful to see experiments that specifically test the robustness of the method to these types of challenges. Additionally, the authors should provide a detailed analysis of the sensitivity of the method to hyperparameter choices. This analysis should include a systematic study of the impact of different learning rates, latent space dimensions, and regularization parameters on the performance of the model. The authors should also provide guidelines for selecting appropriate hyperparameter values for different types of problems. Furthermore, it would be valuable to compare the robustness of PIDO to other methods in terms of their sensitivity to noise and perturbations in the input data. This could be done by adding controlled amounts of noise to the input data and measuring the impact on the accuracy of the model's predictions.

Finally, the authors should consider including a discussion of the potential for extending the proposed method to more complex PDE systems. For example, the authors could discuss the challenges of applying PIDO to systems with higher-order derivatives or nonlinearities. It would also be useful to explore the potential for incorporating additional physics-based constraints into the model, such as conservation laws or boundary conditions. This would allow the model to be applied to a wider range of PDE systems and to more accurately capture the underlying physics. The authors should also discuss the potential for using the latent space representation to improve the interpretability of the model. For example, the authors could explore the possibility of visualizing the latent space and identifying patterns or structures that correspond to specific physical phenomena.

### Questions

1. How does the proposed method handle systems with higher-order derivatives or nonlinearities? Are there any specific modifications or extensions needed to apply PIDO to such systems?
2. Can the latent space representation be used to improve the interpretability of the model? For example, can the latent space be visualized or analyzed to gain insights into the underlying physics of the system?
3. How does the performance of PIDO compare to other state-of-the-art methods on more complex PDE systems, such as those with discontinuities or chaotic behavior?

### Rating

6

### Confidence

2

**********
