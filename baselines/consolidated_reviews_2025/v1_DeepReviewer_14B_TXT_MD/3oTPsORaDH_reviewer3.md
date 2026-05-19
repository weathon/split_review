### Summary

The authors propose a new equivariant graph neural network architecture, SEGNO, that is based on Neural ODEs. The authors show that SEGNO is able to learn the underlying dynamics of the system better than other baselines. The authors also show that SEGNO is able to maintain equivariance properties identical to the backbone Equiv-GNNs.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

- The paper is well written and easy to follow.
- The authors provide a theoretical analysis of the SEGNO model, which is a nice addition to the paper.
- The authors provide a thorough experimental evaluation of the SEGNO model on both synthetic and real-world datasets.

### Weaknesses

#### Some Related Works


#### comment

 - The authors do not provide a detailed analysis of the computational cost of the SEGNO model compared to other baselines. This is an important consideration for practical applications, as the SEGNO model may be more computationally expensive than other models.
- The authors do not provide a detailed analysis of the sensitivity of the SEGNO model to the choice of hyperparameters. This is an important consideration for practical applications, as the performance of the SEGNO model may be sensitive to the choice of hyperparameters.
- The authors do not provide a detailed analysis of the generalization performance of the SEGNO model to out-of-distribution data. This is an important consideration for practical applications, as the SEGNO model may not generalize well to data that is different from the training data.

### Suggestions

The paper would benefit from a more thorough investigation into the computational demands of the SEGNO model. While the authors mention the use of Neural ODEs, they do not delve into the specific computational bottlenecks associated with solving these ODEs, especially in the context of graph neural networks. For instance, the number of ODE solver steps required for convergence, and how this scales with the size of the graph, should be analyzed. Furthermore, a comparison of the wall-clock time for training and inference, not just the number of parameters, would provide a more practical understanding of the model's efficiency. The authors should also consider the memory footprint of the SEGNO model, as this can be a limiting factor for large-scale graph datasets. A detailed breakdown of the computational cost associated with each component of the model, such as the message passing and the ODE solver, would be beneficial.

In addition to computational cost, a more rigorous analysis of the hyperparameter sensitivity of the SEGNO model is needed. The authors should explore the impact of key hyperparameters, such as the learning rate, the number of layers in the GNN backbone, and the ODE solver tolerance, on the model's performance. It is important to understand how these hyperparameters interact with each other and how they affect the convergence and generalization of the model. A sensitivity analysis, perhaps using techniques like Sobol indices, could provide valuable insights into the robustness of the model. The authors should also investigate the effect of different initialization strategies on the model's performance, as this can be a critical factor in training deep learning models. Furthermore, the authors should provide guidelines for selecting appropriate hyperparameter values for different datasets and tasks.

Finally, the paper should include a more comprehensive evaluation of the model's generalization capabilities, particularly on out-of-distribution data. The authors should consider evaluating the model on datasets that exhibit different characteristics from the training data, such as different graph sizes, node features, or edge attributes. This would provide a more realistic assessment of the model's ability to generalize to unseen scenarios. The authors should also investigate the model's robustness to adversarial attacks or noisy data, as this is an important consideration for practical applications. Furthermore, the authors should explore the model's ability to extrapolate beyond the training data, as this is a key requirement for many real-world applications. A detailed analysis of the model's failure modes would also be beneficial, as this can provide insights into the model's limitations and potential areas for improvement.

### Questions

- How does the computational cost of the SEGNO model compare to other baselines?
- How sensitive is the SEGNO model to the choice of hyperparameters?
- How well does the SEGNO model generalize to out-of-distribution data?

### Rating

6

### Confidence

3

**********
