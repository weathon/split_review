### Summary

This paper introduces a novel approach to pruning neural networks at initialization using a differentiable mask optimization technique. The method, called DPaI, leverages the Node-Path Balancing Principle to optimize the network topology, ensuring a balance between the number of effective nodes and paths. The authors demonstrate that DPaI outperforms existing state-of-the-art pruning methods across various architectures and datasets, particularly in scenarios with high sparsity levels.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel differentiable pruning method that addresses the limitations of existing pruning techniques.
2. The method is shown to outperform state-of-the-art pruning methods across multiple architectures and datasets.
3. The paper provides a thorough analysis of the method's performance, including ablation studies and comparisons with other techniques.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed discussion of the computational cost associated with the proposed method. While the authors mention that DPaI is efficient, they do not provide a comprehensive analysis of the time and memory requirements, especially in comparison to other pruning techniques. The analysis should include a breakdown of the time spent on different stages of the pruning process, such as mask optimization and network evaluation, and how these scale with network size and sparsity levels. Furthermore, the memory footprint of the method, including the storage of masks and intermediate variables, should be quantified and compared to other methods.
2. The paper does not explore the sensitivity of the method to different hyperparameters, such as the learning rate and the number of iterations. A more thorough analysis of how these parameters affect the performance of the method would be beneficial. Specifically, the paper should investigate the impact of different learning rates on the convergence of the mask optimization process and the final sparsity achieved. The number of iterations should also be analyzed to determine the trade-off between computational cost and performance. It is also important to analyze the sensitivity of the method to the choice of the balancing parameter in the Node-Path Balancing Principle, as this parameter could significantly impact the final network structure.
3. The paper could benefit from a more detailed comparison with other pruning methods, particularly in terms of the trade-offs between accuracy and sparsity. The comparison should not only focus on the final accuracy achieved but also on the sparsity levels attained and the computational cost associated with each method. It would be beneficial to include a Pareto front analysis to visualize the trade-offs between accuracy and sparsity for different methods. Additionally, the paper should discuss the limitations of the proposed method in scenarios where high accuracy is more critical than sparsity, and vice versa.

### Suggestions

To address the lack of detailed computational cost analysis, the authors should include a comprehensive breakdown of the time and memory requirements of their method. This should include a comparison with other pruning techniques, detailing the time spent on mask optimization, network evaluation, and any other relevant stages. The analysis should also consider how these costs scale with network size and sparsity levels. For example, the authors could provide a table showing the pruning time for different network architectures (e.g., ResNet-18, VGG-19) and sparsity levels (e.g., 90%, 95%, 99%). Furthermore, the memory footprint of the method should be quantified, including the storage of masks and intermediate variables, and compared to other methods. This would provide a more complete picture of the method's efficiency and practicality.

To address the sensitivity to hyperparameters, the authors should conduct a more thorough analysis of how different learning rates and iteration numbers affect the performance of their method. This should include experiments with a range of learning rates and iteration numbers, and the results should be presented in a clear and concise manner, such as through plots or tables. The analysis should also investigate the impact of the balancing parameter in the Node-Path Balancing Principle. The authors should provide guidelines for selecting appropriate hyperparameter values based on the specific network architecture and dataset. This would make the method more robust and easier to use in practice. For example, the authors could show how the final accuracy and sparsity change as the learning rate is varied, and how the convergence of the mask optimization process is affected by the number of iterations.

To improve the comparison with other pruning methods, the authors should include a more detailed analysis of the trade-offs between accuracy and sparsity. This should include a Pareto front analysis to visualize the trade-offs between accuracy and sparsity for different methods. The authors should also discuss the limitations of their method in scenarios where high accuracy is more critical than sparsity, and vice versa. For example, the authors could compare their method with other pruning techniques in terms of the accuracy achieved at different sparsity levels, and discuss the scenarios where their method is most suitable. This would provide a more complete understanding of the strengths and weaknesses of the proposed method and its applicability to different scenarios.

### Questions

1. How does the computational cost of DPaI compare to other pruning methods, especially in terms of pruning time and memory requirements?
2. How sensitive is the method to the choice of hyperparameters, such as the learning rate and the number of iterations?
3. How does the method perform on larger and more complex datasets, such as ImageNet?
4. What are the limitations of the method in scenarios where high accuracy is more critical than sparsity, and vice versa?

### Rating

6

### Confidence

3

**********
