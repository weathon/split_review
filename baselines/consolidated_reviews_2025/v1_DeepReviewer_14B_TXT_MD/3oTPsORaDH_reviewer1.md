### Summary

The paper introduces SEGNO (Second-order Equivariant Graph Neural Ordinary Differential Equation), a novel framework that enhances the generalization capabilities of Equivariant Graph Neural Networks (Equiv-GNNs) for modeling complex multi-object physical systems. By integrating second-order motion laws and continuous dynamics through Neural Ordinary Differential Equations (Neural ODEs), SEGNO addresses key limitations of existing Equiv-GNNs, which often rely on discrete transformations and first-order velocity information.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. SEGNO incorporates second-order continuity and equivariant properties, allowing it to learn a unique trajectory between system states while maintaining error bounds with the true trajectory. This is a significant improvement over traditional discrete models.

2. The authors provide rigorous theoretical insights, proving the uniqueness of the learned trajectory and bounding the discrepancy between the learned and actual trajectories.

3. SEGNO demonstrates substantial performance gains across various complex dynamical systems, including molecular dynamics and motion capture, outperforming state-of-the-art baselines.

### Weaknesses

#### Some Related Works


#### comment

1. The authors mention that they use the Euler integrator in the experiments, but they do not conduct a detailed analysis of the effects of different integrators on the model's performance. Specifically, the paper lacks a systematic comparison of how different numerical integration schemes, such as Runge-Kutta methods or symplectic integrators, impact the accuracy and stability of the learned dynamics, especially when dealing with varying levels of discretization. This is crucial because the choice of integrator can significantly affect the model's ability to capture the underlying physical system accurately.

2. Although the authors state that the model can adapt to different backbone GNNs, the paper does not discuss in detail how different GNN architectures affect the model's performance. The paper should explore how the choice of GNN backbone, such as EGNN, SEGNN, or other architectures with varying message-passing mechanisms, influences the model's ability to learn complex interactions and how the expressive power of the GNN affects the overall performance of SEGNO. A more detailed analysis of the interplay between the GNN backbone and the ODE solver is needed.

3. The authors do not provide a detailed explanation of the model's parameter count and computational cost compared to other baseline models. A detailed comparison of parameter counts, training time, and inference time is needed to assess the practical applicability of the proposed method. This comparison should include a breakdown of the computational cost associated with the GNN backbone and the ODE solver separately.

### Suggestions

To address the lack of analysis regarding different integrators, the authors should conduct a thorough ablation study comparing the performance of SEGNO with various numerical integration methods, such as the Euler method, Runge-Kutta methods (e.g., RK4), and symplectic integrators (e.g., Velocity Verlet). This study should evaluate the impact of these integrators on the model's accuracy and stability across different time step sizes. The results should be presented with clear metrics, such as mean squared error (MSE) or root mean squared error (RMSE), and should include a discussion on the trade-offs between computational cost and accuracy for each integrator. Furthermore, the authors should analyze how the choice of integrator affects the model's ability to capture long-term dynamics, as some integrators may be more prone to error accumulation over time. This analysis should provide clear guidelines on selecting appropriate integrators based on the specific requirements of the application.

To address the lack of analysis regarding different GNN backbones, the authors should conduct a comprehensive study comparing the performance of SEGNO with various GNN architectures, such as EGNN, SEGNN, and other relevant models. This study should evaluate how the choice of GNN backbone affects the model's ability to learn complex interactions and how the expressive power of the GNN influences the overall performance of SEGNO. The analysis should include a discussion on the strengths and weaknesses of each GNN backbone in the context of SEGNO, focusing on how the message-passing mechanisms and the equivariant properties of each GNN affect the model's ability to capture the underlying physical dynamics. The authors should also explore how the number of message-passing layers in the GNN backbone affects the model's performance and computational cost. This analysis should provide clear guidelines on selecting appropriate GNN backbones based on the specific characteristics of the physical system being modeled.

Finally, to address the lack of detailed computational cost analysis, the authors should provide a comprehensive comparison of the parameter counts, training time, and inference time of SEGNO with other baseline models. This comparison should include a breakdown of the computational cost associated with the GNN backbone and the ODE solver separately. The authors should also analyze how the number of integration steps (tau) affects the computational cost and the model's performance. This analysis should provide a clear understanding of the trade-offs between accuracy and computational cost, allowing practitioners to make informed decisions about the practical applicability of SEGNO. The authors should also discuss the memory requirements of the model, especially when dealing with large-scale systems, and provide recommendations on how to optimize the model's performance in resource-constrained environments.

### Questions

Please refer to the weaknesses.

### Rating

6

### Confidence

3

**********
