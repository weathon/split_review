### Summary

The authors study the connection between pruning masks and Hessian eigenspaces in deep learning. They show that both exhibit early crystallization and stabilization during training. They propose a method to quantify the similarity between these two subspaces using Grassmannian metrics. They find that the similarity between the subspaces induced by magnitude pruning masks and top Hessian eigenspaces is significantly larger than random chance throughout the training process. This suggests that largest parameter magnitudes tend to coincide with the directions of largest loss curvature. The authors discuss potential applications of their findings, including fast and effective low-rank Hessian approximations, and bridging the gap between first- and second-order methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper provides a novel perspective on the connection between pruning masks and Hessian eigenspaces, which is a relatively unexplored area in the field of deep learning. The use of Grassmannian metrics to quantify the similarity between these subspaces is a creative approach that allows for a more rigorous analysis of their relationship.

2. The authors conduct extensive experiments to validate their findings, including training a deep neural network and analyzing the overlap between the two subspaces throughout the entire training process. The results provide strong evidence to support the claims made in the paper.

3. The paper is well-written and easy to follow, with clear explanations of the concepts and methods used. The figures and tables are also well-designed and help to illustrate the key findings of the paper.

### Weaknesses

#### Some Related Works


#### comment

1. The paper focuses on a specific type of neural network and dataset, and it is unclear how well the findings generalize to other types of networks and datasets. Further research is needed to explore the applicability of the proposed method to different domains.

2. The paper does not provide a detailed analysis of the computational cost of the proposed method, which could be a concern for large-scale applications. It would be beneficial to include a discussion of the computational complexity and potential optimizations.

3. The paper does not address the potential limitations of the proposed method, such as its sensitivity to hyperparameters or its performance in the presence of noise or adversarial examples. A more thorough discussion of these limitations would help to provide a more balanced view of the method's strengths and weaknesses.

### Suggestions

The paper's exploration of the relationship between pruning masks and Hessian eigenspaces is novel, but its practical implications could be significantly strengthened by addressing the limitations in its current form. Specifically, the authors should investigate the sensitivity of their findings to different network architectures and datasets. For instance, the current study might be limited by the specific choice of activation functions, layer types, or the depth of the network. It would be beneficial to see experiments on convolutional networks, recurrent networks, and transformers, as well as on datasets with varying levels of complexity and dimensionality. This would help to establish the robustness and generalizability of the observed overlap between the subspaces. Furthermore, the authors should consider the impact of different optimization algorithms and learning rate schedules on the observed phenomena. Such an analysis would provide a more comprehensive understanding of the conditions under which the proposed method is effective.

Regarding the computational cost, the paper should provide a more detailed analysis of the time and memory requirements of the proposed method, especially in comparison to existing techniques for analyzing Hessian eigenspaces. The authors should discuss the scalability of their approach to larger models and datasets. For example, they could analyze the computational complexity of the SVD operation used to compute the Hessian eigenspaces and discuss potential optimizations, such as using iterative methods or low-rank approximations. Furthermore, it would be beneficial to explore the trade-off between the accuracy of the Hessian approximation and the computational cost. The authors could also investigate the possibility of using parameter inspection to approximate the top Hessian subspace, as suggested in the paper, and provide a quantitative analysis of the approximation error. This would help to make the proposed method more practical for large-scale applications.

Finally, the paper should address the potential limitations of the proposed method more thoroughly. The authors should investigate the sensitivity of their findings to hyperparameter settings, such as the learning rate, batch size, and regularization parameters. They should also explore the robustness of their method to noise and adversarial examples. For example, they could add noise to the input data or the network parameters and analyze how this affects the overlap between the pruning masks and Hessian eigenspaces. Furthermore, the authors should discuss the potential limitations of using magnitude-based pruning and explore alternative pruning techniques, such as gradient-based pruning or random pruning. This would help to provide a more balanced view of the method's strengths and weaknesses and identify potential areas for future research.

### Questions

1. How does the proposed method compare to other existing methods in terms of performance and computational cost? It would be helpful to see a more detailed comparison with other techniques in the literature.

2. What are the potential limitations of the proposed method, and how can they be addressed? It would be helpful to have a more thorough discussion of the limitations of the method and potential solutions to these limitations.

### Rating

6: marginally above the acceptance threshold

### Confidence

2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
