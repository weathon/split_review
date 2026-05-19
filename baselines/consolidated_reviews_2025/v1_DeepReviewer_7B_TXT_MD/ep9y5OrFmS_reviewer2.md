### Summary

This paper studies the similarity between parameter pruning masks and the top-k Hessian eigenspaces. The authors propose a method to quantify the similarity between these two subspaces using Grassmannian metrics. They demonstrate that both pruning masks and top Hessian subspaces exhibit early emergence and stabilization during training. The overlap between these subspaces is significantly larger than random chance, suggesting that large parameters tend to coincide with directions of high loss curvature.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel approach to quantify the similarity between pruning masks and Hessian eigenspaces using Grassmannian metrics.
2. The paper provides empirical evidence that both pruning masks and top Hessian subspaces exhibit early emergence and stabilization during training.
3. The paper offers a new perspective on the relationship between parameter pruning and loss curvature, suggesting that large parameters are often associated with high curvature directions.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a theoretical explanation for why pruning masks and top Hessian subspaces exhibit early emergence and stabilization during training.
2. The paper does not explore the potential applications of the proposed method in model compression or optimization.

### Suggestions

The paper would benefit from a more in-depth analysis of the observed early emergence and stabilization of pruning masks and Hessian subspaces. While the empirical results are compelling, the lack of a theoretical framework leaves open questions about the underlying mechanisms. For instance, the authors could investigate whether the observed phenomena are related to the initial conditions of the training process, such as the specific initialization of network parameters, or if they are a consequence of the optimization algorithm used. A deeper exploration of these aspects would strengthen the paper's claims and provide a more comprehensive understanding of the observed behavior. Furthermore, the authors could consider exploring the relationship between the observed early emergence and the learning rate schedule or other hyperparameters of the training process. Such an analysis could provide valuable insights into the dynamics of the training process and the interplay between pruning and loss curvature.

Regarding the practical applications of the proposed method, the authors should explore the potential of using the similarity between pruning masks and Hessian eigenspaces to improve model compression or optimization. For example, the authors could investigate whether the identified pruning masks can be used to guide the selection of parameters for compression, or whether the Hessian eigenspaces can be used to design more efficient optimization algorithms. The authors could also explore the possibility of using the proposed method to identify and remove redundant parameters, which could lead to more compact and efficient models. Furthermore, the authors could investigate the potential of using the proposed method to analyze the behavior of different pruning techniques and optimization algorithms. Such an analysis could provide valuable insights into the strengths and weaknesses of different approaches and guide the development of more effective methods.

Finally, the authors should provide a more detailed discussion of the limitations of the proposed method and the potential directions for future research. For example, the authors could discuss the computational cost of computing the Grassmannian metrics and the potential for developing more efficient algorithms. The authors could also discuss the limitations of the proposed method in the context of different types of neural networks and datasets. A more thorough discussion of these aspects would provide a more balanced and comprehensive view of the proposed method and its potential impact.

### Questions

1. How does the proposed method compare to existing methods for analyzing parameter pruning and loss curvature?
2. What are the potential applications of the proposed method in model compression or optimization?
3. Can the proposed method be extended to analyze the behavior of different pruning techniques and optimization algorithms?

### Rating

6

### Confidence

3

**********
