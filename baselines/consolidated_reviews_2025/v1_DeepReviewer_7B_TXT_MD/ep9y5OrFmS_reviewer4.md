### Summary

This paper studies the connection between pruning masks and Hessian eigenspaces. The authors show that these two structures are similar early in training and that this similarity is maintained throughout training. They also show that the overlap between pruning masks and Hessian eigenspaces is significantly larger than random chance. The authors propose a method to approximate the Hessian eigenspaces using pruning masks, which can be used to approximate the Hessian at a lower computational cost.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The experiments are comprehensive and well-designed.
3. The proposed method is novel and has the potential to be used in real-world applications.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a theoretical explanation for why pruning masks and Hessian eigenspaces exhibit early emergence and stabilization during training.
2. The paper does not explore the potential applications of the proposed method in model compression or optimization.

### Suggestions

The paper would benefit from a more thorough investigation into the underlying mechanisms that cause the observed similarity between pruning masks and Hessian eigenspaces. While the authors demonstrate that these structures exhibit early emergence and stabilization, they do not delve into the reasons why this occurs. A deeper analysis, perhaps involving the study of the optimization landscape or the dynamics of gradient descent, could provide valuable insights. For example, the authors could explore how the loss curvature changes during training and how this relates to the selection of parameters for pruning. Furthermore, it would be beneficial to investigate whether this similarity is specific to certain types of neural networks or datasets, or if it is a more general phenomenon. Such an analysis would strengthen the theoretical foundation of the paper and provide a more comprehensive understanding of the observed behavior.

To enhance the practical impact of the work, the authors should explore the potential applications of their method in model compression and optimization. While the authors propose a method to approximate the Hessian eigenspaces using pruning masks, they do not demonstrate how this approximation can be used to improve model performance or reduce computational cost. For instance, the authors could investigate whether the identified pruning masks can be used to guide the pruning process in a more efficient way, or whether the Hessian eigenspaces can be used to design more effective optimization algorithms. Furthermore, the authors could explore the use of their method in different types of neural networks and datasets, and compare its performance to existing pruning techniques. Such an analysis would demonstrate the practical utility of the proposed method and provide a more compelling case for its adoption.

Finally, the paper could benefit from a more detailed discussion of the limitations of the proposed method and potential avenues for future research. For example, the authors could discuss the computational cost of computing the pruning masks and Hessian eigenspaces, and whether this cost is prohibitive for large-scale models. They could also explore the sensitivity of their method to different hyperparameters and training settings. Furthermore, the authors could discuss the potential impact of the choice of the pruning strategy on the observed similarity between pruning masks and Hessian eigenspaces. Such a discussion would provide a more balanced and nuanced view of the proposed method and its potential applications.

### Questions

1. Can the authors provide a theoretical explanation for why pruning masks and Hessian eigenspaces exhibit early emergence and stabilization during training?
2. Can the authors explore the potential applications of the proposed method in model compression or optimization?

### Rating

8

### Confidence

3

**********
