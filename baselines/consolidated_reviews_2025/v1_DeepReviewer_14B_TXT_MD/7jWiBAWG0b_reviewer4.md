### Summary

This paper investigates the generalization and optimization properties of non-convex pairwise SGD with heavy-tailed gradient noise. The authors establish stability-based learning guarantees for non-convex pairwise SGD by investigating its generalization and optimization jointly. They first bound the generalization error of pairwise SGD in the general non-convex setting, after bridging the quantitative relationships between $\ell_1$ on-average model stability and generalization error. Then, a refined generalization bound is established for non-convex pairwise SGD by introducing the heavy-tailed gradient noise to remove the bounded gradient assumption. Finally, the sharper error bounds for generalization and optimization are provided under the gradient dominance condition. In addition, they extend their analysis to the corresponding pairwise minibatch SGD and derive the first stability-based near-optimal generalization and optimization bounds which are consistent with many empirical observations.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow. 
2. The paper provides a comprehensive theoretical analysis of non-convex pairwise SGD with heavy-tailed gradient noise, filling a gap in the learning theory for this setting. 
3. The theoretical results are solid and novel.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks experimental results to validate the theoretical findings. It would be beneficial to include some experiments to demonstrate the practical implications of the theoretical results. Specifically, the paper should include experiments that compare the performance of the proposed pairwise SGD with existing methods on benchmark datasets. The absence of such empirical validation makes it difficult to assess the practical relevance of the theoretical bounds derived in the paper. Furthermore, it is unclear how the theoretical results translate into practical algorithm design choices, such as the selection of step sizes and batch sizes. 
2. Some assumptions, such as the PL condition, may be restrictive in practice. The paper relies on the Polyak-Łojasiewicz (PL) condition, which is a strong assumption that may not hold for many non-convex loss functions encountered in practice. This limitation restricts the applicability of the theoretical results to a specific class of problems. It would be beneficial to discuss the implications of this assumption and explore potential relaxations or alternative conditions that could broaden the scope of the analysis.

### Suggestions

To enhance the practical impact of the paper, it is crucial to include a comprehensive experimental section. This section should include experiments on benchmark datasets relevant to pairwise learning tasks, such as metric learning or ranking problems. The experiments should compare the performance of the proposed pairwise SGD algorithm with existing state-of-the-art methods, demonstrating the advantages and limitations of the proposed approach. Furthermore, the experimental results should be used to validate the theoretical bounds derived in the paper, showing how the theoretical predictions align with the empirical observations. For example, the experiments could investigate the effect of different step sizes and batch sizes on the convergence rate and generalization performance, providing practical guidance for algorithm design. The experiments should also explore the sensitivity of the algorithm to the heavy-tailed nature of the gradient noise, verifying the theoretical analysis under different noise conditions. This would provide a more complete picture of the practical behavior of the proposed algorithm and its robustness to real-world data.

To address the limitations imposed by the PL condition, the authors should explore potential relaxations or alternative conditions that could broaden the applicability of the theoretical results. For instance, the authors could investigate the possibility of using weaker conditions, such as the Łojasiewicz inequality with a variable exponent, or explore the use of gradient dominance conditions. Furthermore, the authors should provide a more detailed discussion of the implications of the PL condition, including examples of loss functions that satisfy or violate this condition. This would help the reader to better understand the scope and limitations of the theoretical analysis. It would also be beneficial to discuss the potential impact of violating the PL condition on the convergence rate and generalization performance of the proposed algorithm. This discussion should include a theoretical analysis of the behavior of the algorithm under more general conditions, providing a more robust and comprehensive understanding of the proposed method.

Finally, the paper should provide more concrete guidance on how to choose the step size and batch size in practice. The theoretical results provide bounds on the convergence rate and generalization error, but they do not provide explicit formulas for selecting these parameters. The authors should provide practical recommendations for choosing these parameters based on the theoretical analysis and empirical observations. For example, the authors could provide a rule of thumb for selecting the step size based on the smoothness of the loss function and the heavy-tailed parameter of the gradient noise. Similarly, the authors could provide guidance on how to choose the batch size based on the size of the dataset and the computational resources available. This practical guidance would make the paper more accessible to practitioners and facilitate the adoption of the proposed algorithm in real-world applications.

### Questions

1. Can the authors provide experimental results to validate their theoretical findings? 
2. Are there any potential relaxations or alternative conditions that could be more realistic in practice?

### Rating

6

### Confidence

4

**********
