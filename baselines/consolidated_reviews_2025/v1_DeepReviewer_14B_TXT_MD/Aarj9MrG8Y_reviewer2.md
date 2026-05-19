### Summary

The paper proposes a learning principle for designing graph filters that can be applied to construct infinite-depth Graph Neural Networks (GNNs). The authors provide a theoretical analysis of the convergence and stability of the proposed graph filter and develop a practical model called Adaptive Power GNN (APGNN) based on this principle. The paper also presents a generalization analysis of the proposed learning framework and provides an upper bound for the generalization error. The authors conduct experiments on various benchmark datasets and demonstrate that APGNN outperforms state-of-the-art GNNs in node classification tasks.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper proposes a novel learning principle for designing graph filters that can be applied to construct infinite-depth GNNs. The proposed principle provides a theoretical guidance for designing deeper GNNs and addresses the limitations of existing methods that cannot be extended to infinite depth.

2. The authors provide a theoretical analysis of the convergence and stability of the proposed graph filter and present a generalization analysis of the proposed learning framework. The theoretical results provide a solid foundation for the proposed method and demonstrate its effectiveness.

3. The authors develop a practical model called APGNN based on the proposed learning principle. The model employs exponentially decaying weights to aggregate graph information of different orders and can be seamlessly extended to an infinite-depth network.

4. The paper is well-written and easy to follow. The authors provide a clear explanation of the proposed method and its theoretical analysis. The experimental results are presented in a clear and concise manner.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a comprehensive comparison with existing methods. While the authors compare APGNN with several state-of-the-art GNNs, they do not provide a detailed comparison with other methods that can be extended to infinite depth. Specifically, the comparison lacks methods that utilize iterative approaches or spectral techniques that could potentially be extended to infinite depth. A more thorough comparison should include methods that, while not explicitly designed for infinite depth, share similar theoretical underpinnings or practical goals.
2. The paper does not provide a detailed analysis of the computational complexity of APGNN. It is important to understand how the computational cost of APGNN scales with the size of the graph and the number of layers. The analysis should include a breakdown of the time and space complexity, considering the exponential decay of weights and the aggregation of multi-order graph information. It should also discuss the practical implications of this complexity on large-scale graphs.
3. The paper does not provide a detailed analysis of the sensitivity of APGNN to the choice of hyperparameters. It is important to understand how the performance of APGNN is affected by the choice of hyperparameters, such as the decay rate and the number of layers. The analysis should include a systematic exploration of the hyperparameter space, potentially using techniques like grid search or Bayesian optimization, and should discuss the impact of different hyperparameter settings on the model's performance and stability.

### Suggestions

To address the lack of comprehensive comparison, the authors should include a more detailed analysis of methods that, while not explicitly designed for infinite depth, share similar theoretical underpinnings or practical goals. This could include methods that utilize iterative approaches, such as power iteration methods, or spectral techniques that could be extended to infinite depth. The comparison should not only focus on performance metrics but also on the theoretical properties of these methods, such as their convergence rates and stability. Furthermore, the authors should provide a clear rationale for why the chosen baselines are the most relevant for comparison, and discuss the limitations of the proposed method in relation to these baselines. This would provide a more complete picture of the strengths and weaknesses of APGNN in the context of existing literature.

Regarding the computational complexity, the authors should provide a detailed analysis of the time and space complexity of APGNN, considering the exponential decay of weights and the aggregation of multi-order graph information. This analysis should include a breakdown of the computational cost of each step in the algorithm, and should discuss how this cost scales with the size of the graph and the number of layers. The authors should also provide empirical evidence to support their theoretical analysis, by reporting the running time of APGNN on different datasets and comparing it with other methods. Furthermore, the authors should discuss the practical implications of this complexity on large-scale graphs, and suggest potential strategies for improving the scalability of APGNN, such as using sparse matrix representations or approximation techniques.

Finally, to address the sensitivity to hyperparameters, the authors should conduct a more systematic exploration of the hyperparameter space, potentially using techniques like grid search or Bayesian optimization. This exploration should include a detailed analysis of the impact of different hyperparameter settings on the model's performance and stability. The authors should also provide guidelines for selecting appropriate hyperparameter values for different datasets, and discuss the potential trade-offs between performance and computational cost. Furthermore, the authors should investigate the robustness of APGNN to different initialization strategies and optimization algorithms, and discuss how these factors can affect the model's performance.

### Questions

Please see the weaknesses.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
