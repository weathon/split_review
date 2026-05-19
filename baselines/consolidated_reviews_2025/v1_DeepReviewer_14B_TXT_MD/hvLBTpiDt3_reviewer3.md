### Summary

This paper proposes a novel pruning-at-initialization method called DPaI, which is based on the Node-Path Balancing (NPB) principle. The key idea is to convert the discrete NPB principle into a differentiable form, allowing for the use of gradient-based methods for pruning. The authors demonstrate that DPaI outperforms existing state-of-the-art PaI methods on various architectures and datasets.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel differentiable formulation of the NPB principle, which is a significant advancement in the field of pruning at initialization.
2. The authors provide a comprehensive convergence analysis of the proposed method, which adds to the theoretical foundation of the work.
3. The empirical results are extensive and demonstrate the effectiveness of DPaI across different architectures and datasets.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational complexity of the proposed method compared to existing approaches. Specifically, the analysis should consider the number of operations and memory requirements for both the pruning phase and the subsequent fine-tuning (if any). A breakdown of the time spent on different parts of the algorithm, such as the calculation of effective paths, nodes, and kernels, would be beneficial.
2. The paper lacks a thorough investigation into the sensitivity of the method to different hyperparameter settings. While the authors mention using a grid search, they do not provide details on the range of values explored, the impact of each hyperparameter on the final performance, or the computational cost associated with the grid search. It would be helpful to see a sensitivity analysis showing how the performance varies with different values of α, β, and the learning rate η, and how these parameters interact with each other.
3. The paper does not explore the applicability of the proposed method to other types of neural networks, such as recurrent neural networks (RNNs) or graph neural networks (GNNs). The current evaluation is limited to CNNs and ViTs, and it is unclear how the differentiable NPB formulation would translate to other architectures with different connectivity patterns and computational flows.

### Suggestions

To address the lack of computational complexity analysis, the authors should provide a detailed breakdown of the time and space complexity of their method, comparing it to existing pruning-at-initialization techniques. This should include a theoretical analysis of the number of operations required for each step of the algorithm, as well as empirical measurements of the actual runtime and memory usage on different hardware platforms. The analysis should also consider the impact of network size and sparsity level on the computational cost. Furthermore, the authors should investigate the potential for parallelizing their method to reduce the pruning time, and provide a discussion of the trade-offs between computational cost and performance.

To improve the hyperparameter analysis, the authors should conduct a more thorough sensitivity study, systematically varying the values of α, β, and η and reporting the corresponding performance metrics. This should include not only the final accuracy but also the convergence speed and the stability of the pruning process. The authors should also explore the interaction between these hyperparameters and provide guidelines for selecting appropriate values for different network architectures and datasets. A visualization of the hyperparameter space, such as a contour plot, could be helpful to understand the sensitivity of the method to different parameter combinations. Additionally, the authors should discuss the computational cost associated with the hyperparameter search and explore more efficient optimization techniques, such as Bayesian optimization or gradient-based methods, to reduce the search time.

To broaden the applicability of the proposed method, the authors should investigate its performance on other types of neural networks, such as RNNs and GNNs. This would involve adapting the differentiable NPB formulation to handle the specific characteristics of these architectures, such as the temporal dependencies in RNNs and the graph structure in GNNs. The authors should also discuss the challenges and limitations of applying their method to these architectures and provide insights into how these challenges can be addressed. This would significantly enhance the impact of the paper and demonstrate the versatility of the proposed approach.

### Questions

1. How does the computational cost of DPaI compare to other pruning-at-initialization methods, especially in terms of pruning time and memory requirements?
2. How sensitive is the performance of DPaI to the choice of hyperparameters, and what is the computational cost of tuning these parameters?
3. Can the proposed method be applied to other types of neural networks, such as recurrent neural networks or graph neural networks?

### Rating

6

### Confidence

3

**********
