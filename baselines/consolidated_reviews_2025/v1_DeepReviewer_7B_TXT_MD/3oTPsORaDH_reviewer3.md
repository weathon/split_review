### Summary

This paper introduces SEGNO, a model that integrates equivariant GNNs with Neural ODEs to learn continuous trajectories in multi-object physical systems. The authors propose a method to model second-order dynamics by using Neural ODEs to approximate the continuous trajectory between two observed states. The paper provides theoretical analysis of SEGNO, including a uniqueness theorem and error bounds. Empirical results on simulated N-body systems, MD22, and CMU motion capture datasets demonstrate that SEGNO outperforms state-of-the-art baselines in terms of prediction accuracy and generalization ability.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper addresses a significant gap in the literature by focusing on continuous dynamics in equivariant GNNs, which is important for modeling physical systems.
- The theoretical analysis is rigorous, providing a solid foundation for the proposed method.
- The empirical results are comprehensive and demonstrate the effectiveness of SEGNO on multiple datasets.

### Weaknesses

#### Some Related Works


#### comment

 - The paper could benefit from more detailed ablation studies to understand the contribution of each component of the proposed method. Specifically, it is unclear how much of the performance gain is due to the Neural ODE component versus the equivariant GNN backbone. A more thorough analysis of the impact of different GNN architectures and the Neural ODE solver would be beneficial.
- The paper could discuss the limitations of the proposed method in more detail, such as potential failure cases or scenarios where the method might not perform well. For example, how does the method handle systems with highly chaotic or turbulent dynamics? Are there specific types of interactions or physical phenomena that the model struggles with? A discussion of these limitations would provide a more balanced view of the method's applicability.

### Suggestions

To strengthen the paper, the authors should conduct a more comprehensive ablation study. This should include varying the architecture of the equivariant GNN backbone, such as using different message-passing layers or activation functions. Furthermore, the impact of different Neural ODE solvers, such as Euler, Runge-Kutta, or adaptive step-size solvers, should be investigated. It would also be valuable to analyze the sensitivity of the model to the choice of the Neural ODE solver's parameters, such as the tolerance and maximum step size. These ablation studies would provide a clearer understanding of the contribution of each component of the proposed method and help identify potential areas for improvement. For example, if the performance is highly sensitive to the choice of the Neural ODE solver, it would suggest that the model is not robust to changes in the solver parameters.

In addition to the ablation studies, the authors should provide a more detailed discussion of the limitations of the proposed method. This discussion should include specific examples of scenarios where the method might fail or perform poorly. For instance, the authors could explore the performance of the model on systems with highly non-linear dynamics or systems with a large number of interacting objects. It would also be beneficial to analyze the model's performance on systems with external forces or constraints that are not captured by the GNN backbone. A more thorough analysis of these limitations would provide a more balanced view of the method's applicability and help guide future research in this area. For example, the authors could investigate how the model performs on systems with time-varying parameters or systems with stochastic dynamics.

Finally, the authors should consider including a discussion of the computational cost of the proposed method. This discussion should include an analysis of the time and memory requirements of the model, as well as a comparison to the computational cost of other state-of-the-art methods. This would help readers understand the practical trade-offs associated with using the proposed method. Furthermore, the authors should discuss potential strategies for reducing the computational cost of the model, such as using more efficient Neural ODE solvers or employing model compression techniques. This would make the method more accessible to a wider range of researchers and practitioners.

### Questions

- How does the proposed method handle systems with non-Euclidean geometries or non-Euclidean spaces?
- How does the method perform on systems with non-constant acceleration or external forces that are not captured by the GNN backbone?

### Rating

6

### Confidence

4

**********
