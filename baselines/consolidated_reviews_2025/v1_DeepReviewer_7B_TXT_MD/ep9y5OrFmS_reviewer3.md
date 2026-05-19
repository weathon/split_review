### Summary

This paper studies the relationship between pruning masks and Hessian eigenspaces. The authors find that both pruning masks and Hessian eigenspaces undergo early emergence and stabilization during training. The authors also find that the overlap between pruning masks and Hessian eigenspaces is significantly larger than random chance. The authors propose a method to approximate the Hessian eigenspaces using pruning masks, which can be used to approximate the Hessian at a lower computational cost.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The authors provide a novel perspective on the relationship between pruning masks and Hessian eigenspaces. The authors find that pruning masks and Hessian eigenspaces are similar early in training and that this similarity is maintained throughout training. This finding is interesting and provides a new way to understand the behavior of neural networks during training.
2. The authors propose a method to approximate the Hessian eigenspaces using pruning masks. This method can be used to approximate the Hessian at a lower computational cost. This is a practical contribution that can be used in real-world applications.
3. The authors provide a comprehensive set of experiments to support their claims. The experiments are well-designed and provide strong evidence for the authors' findings.

### Weaknesses

#### Some Related Works


#### comment

1. The authors do not provide a theoretical explanation for why pruning masks and Hessian eigenspaces exhibit early emergence and stabilization during training. This is a significant limitation of the paper, as it leaves open questions about the underlying mechanisms that drive these phenomena. Specifically, the paper lacks a discussion on the optimization landscape and how the training process interacts with the loss curvature, which could explain the observed early emergence and stabilization. It is unclear why certain parameters are consistently selected for pruning and why the Hessian eigenspaces converge to a stable state so quickly. A more detailed analysis of the gradient flow and its interaction with the loss landscape is needed to provide a deeper understanding of these phenomena.
2. The authors do not explore the potential applications of their method in model compression or optimization. While the authors propose a method to approximate the Hessian eigenspaces using pruning masks, they do not demonstrate how this method can be used to improve model performance or reduce computational cost. The paper lacks concrete examples of how the proposed method can be integrated into existing training pipelines or used to guide the pruning process. It is unclear how the overlap between pruning masks and Hessian eigenspaces can be leveraged to achieve better pruning or faster convergence. The authors should provide a more detailed discussion of the practical implications of their findings and how they can be used to develop more efficient training algorithms.

### Suggestions

The authors should delve deeper into the theoretical underpinnings of the observed phenomena. Specifically, they should investigate the relationship between the training dynamics, the loss landscape, and the emergence of pruning masks and Hessian eigenspaces. This could involve analyzing the gradient flow and its interaction with the loss curvature, as well as exploring the role of different optimization algorithms and hyperparameters. A theoretical framework that explains why certain parameters are consistently selected for pruning and why the Hessian eigenspaces converge to a stable state early in training would significantly strengthen the paper. Furthermore, the authors should consider exploring the connection between their findings and existing theories on feature learning and optimization dynamics in neural networks. This would help to contextualize their results and provide a more comprehensive understanding of the underlying mechanisms.

To enhance the practical impact of their work, the authors should explore the potential applications of their method in model compression and optimization. They should demonstrate how the overlap between pruning masks and Hessian eigenspaces can be leveraged to achieve better pruning or faster convergence. For example, they could investigate whether the identified pruning masks can be used to guide the pruning process in a more efficient way, or whether the Hessian eigenspaces can be used to design more effective optimization algorithms. The authors should also consider exploring the use of their method in different types of neural networks and datasets. This would help to assess the generalizability of their findings and identify potential limitations. Furthermore, the authors should provide a more detailed discussion of the computational cost of their method and compare it to existing pruning techniques. This would help to evaluate the practical feasibility of their approach.

Finally, the authors should provide a more detailed analysis of the experimental results. While the experiments are well-designed, the authors should provide a more in-depth discussion of the observed patterns and trends. For example, they should investigate the relationship between the overlap between pruning masks and Hessian eigenspaces and the performance of the pruned models. They should also explore the sensitivity of their findings to different experimental settings, such as the choice of optimizer, learning rate, and network architecture. A more thorough analysis of the experimental results would help to strengthen the paper's claims and provide a more comprehensive understanding of the phenomena under investigation.

### Questions

1. Can the authors provide a theoretical explanation for why pruning masks and Hessian eigenspaces exhibit early emergence and stabilization during training?
2. Can the authors explore the potential applications of their method in model compression or optimization?

### Rating

6

### Confidence

3

**********
