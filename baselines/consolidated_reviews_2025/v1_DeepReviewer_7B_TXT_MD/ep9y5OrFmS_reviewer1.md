### Summary

The paper connects two lines of work: (1) pruning masks tend to be stable over time and (2) the top eigenspaces of the loss Hessian tend to be stable and sparse over time. The authors show that pruning masks and the top Hessian subspaces are similar early in training and that this similarity is maintained throughout training. The authors propose a method to approximate the Hessian eigenspaces using parameter pruning masks, which can be used to approximate the Hessian at a lower computational cost.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a comprehensive set of experiments to support their claims.
3. The proposed method offers a novel perspective on understanding the relationship between pruning masks and Hessian eigenspaces.

### Weaknesses

#### Some Related Works


#### comment

1. The paper's main contribution is to show that pruning masks and top Hessian subspaces are similar early in training and that this similarity is maintained throughout training. However, the paper does not provide a clear explanation of why this similarity exists. It is unclear what underlying mechanisms cause the pruning masks to align with the Hessian's top eigenspaces. The authors should delve deeper into the theoretical underpinnings of this phenomenon, perhaps by exploring connections to existing theories on feature learning or optimization dynamics in neural networks. Without a clear explanation, the observed similarity remains an empirical curiosity rather than a fundamental insight.
2. The authors propose using pruning masks to approximate the Hessian eigenspaces, which can be computationally efficient. However, the paper does not provide a thorough analysis of the approximation quality. It is unclear how accurate this approximation is and whether it introduces any bias or systematic errors. A more rigorous analysis of the approximation error, perhaps through comparisons with direct Hessian computations on smaller models, would be necessary to assess the practical utility of this approach. The authors should also discuss the limitations of this approximation and when it might fail.
3. The paper focuses on the similarity between pruning masks and top Hessian subspaces, but it does not explore the implications of this similarity for optimization or generalization. It is not clear how this observed alignment affects the training process or the performance of the trained models. The authors should investigate whether this similarity can be leveraged to improve training efficiency or model generalization. For example, can the pruning masks be used to guide the optimization process or to select better initializations?

### Suggestions

The authors should investigate the theoretical reasons behind the observed similarity between pruning masks and top Hessian subspaces. This could involve exploring connections to existing theories on feature learning, such as the Neural Tangent Kernel (NTK) theory, which provides a framework for understanding how neural networks learn and how their internal representations evolve during training. Specifically, the authors could analyze how the pruning masks interact with the NTK and whether they induce specific changes in the network's feature space that align with the Hessian's top eigenspaces. Furthermore, the authors should explore the relationship between the pruning masks and the network's loss landscape. Do the pruning masks tend to lie in regions of high curvature, which would explain why they align with the top Hessian eigenspaces? A deeper understanding of these theoretical aspects would significantly enhance the paper's contribution and provide a more fundamental insight into the observed phenomenon.

To address the concerns about the approximation quality of using pruning masks to estimate the Hessian eigenspaces, the authors should conduct a more thorough analysis. This could involve comparing the eigenvectors obtained from the pruning mask approximation with those obtained from direct Hessian computations on smaller models. The authors should quantify the approximation error using metrics such as the cosine similarity between the eigenvectors or the Frobenius norm of the difference between the eigenspaces. Furthermore, the authors should investigate how the approximation error changes during training and how it varies with different pruning strategies and network architectures. It would also be beneficial to explore the impact of the approximation error on downstream tasks, such as model generalization and transfer learning. This analysis would provide a more comprehensive understanding of the practical utility of the proposed approximation method.

Finally, the authors should explore the implications of the observed similarity between pruning masks and top Hessian subspaces for optimization and generalization. This could involve investigating whether the pruning masks can be used to guide the optimization process, for example, by using them to select better initializations or to adapt the learning rate. The authors could also explore whether the pruning masks can be used to select better subsets of the training data for training. Furthermore, the authors should investigate whether the observed alignment affects the generalization performance of the trained models. For example, do models trained with pruning masks that align with the top Hessian subspaces generalize better to unseen data? A thorough investigation of these implications would significantly enhance the paper's practical relevance and provide valuable insights for the community.

### Questions

1. Can the authors provide more insights into why pruning masks and top Hessian subspaces are similar early in training?
2. Can the authors provide a more thorough analysis of the approximation quality of using pruning masks to approximate the Hessian eigenspaces?
3. Can the authors discuss the implications of the observed similarity for optimization or generalization?

### Rating

5

### Confidence

3

**********
