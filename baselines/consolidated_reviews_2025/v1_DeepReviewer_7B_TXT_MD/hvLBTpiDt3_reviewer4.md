### Summary

This paper proposes a novel pruning at initialization (PaI) method called DPaI that extends the node-path balancing principle. The proposed method is differentiable and can be directly used to optimize the pruning mask. Experiments show that DPaI outperforms existing PaI methods.

### Soundness

3

### Presentation

2

### Contribution

2

### Strengths

1. The proposed method is novel and interesting. It extends the node-path balancing principle to be differentiable and can be used to directly optimize the pruning mask.
2. Experiments show that the proposed method outperforms existing PaI methods.

### Weaknesses

#### Some Related Works


#### comment

1. The paper is not well-written and some details are not clear. For example, the authors do not provide a clear definition of the term "effective nodes" and "effective paths". The authors should provide a clear definition of these terms and explain how they are computed. Specifically, it is unclear if these terms refer to the number of active neurons or connections, and how this relates to the overall network structure. The lack of a precise definition makes it difficult to understand the core mechanism of the proposed method.
2. The authors should provide more details about the hyperparameters used in the experiments. The authors should provide the specific values of all hyperparameters used in the experiments, including learning rate, batch size, and any regularization parameters. Without these details, it is difficult to reproduce the results and assess the robustness of the method.
3. The authors should provide more details about the computational cost of the proposed method. The authors should provide a detailed analysis of the computational cost of the proposed method, including the time and memory requirements. This analysis should include a comparison with existing pruning methods to demonstrate the efficiency of the proposed method.

### Suggestions

The paper would significantly benefit from a more rigorous definition of the terms 'effective nodes' and 'effective paths.' Currently, these terms are used without a clear explanation of their relationship to the network's structure and the pruning process. For instance, are 'effective nodes' defined as the number of active neurons after pruning, or are they related to the number of connections? A precise definition, possibly with a visual aid, would greatly enhance the reader's understanding of the proposed method. Furthermore, the authors should clarify how these 'effective' measures are computed during the pruning process. This would help in understanding the core mechanism of the proposed method and its relation to the node-path balancing principle. Without this clarity, the novelty and effectiveness of the method are difficult to assess.

To improve the reproducibility of the experiments, the authors should provide a comprehensive list of all hyperparameters used in their experiments. This list should include not only the learning rate, batch size, and any regularization parameters, but also other relevant settings such as the pruning ratio, the number of iterations, and any other parameters that might affect the performance of the method. The authors should also specify the exact versions of any libraries or frameworks used in the experiments. This level of detail is crucial for other researchers to replicate the results and to assess the robustness of the proposed method. Furthermore, a sensitivity analysis of the key hyperparameters would be beneficial to understand their impact on the performance of the method. This would help in identifying the optimal settings for different tasks and datasets.

Finally, the authors should provide a detailed analysis of the computational cost of the proposed method, including the time and memory requirements. This analysis should include a comparison with existing pruning methods to demonstrate the efficiency of the proposed method. The authors should also discuss the scalability of the method to larger networks and datasets. For example, they could provide a table showing the training time and memory usage of the proposed method for different network sizes and datasets. This analysis should also include a discussion of any potential bottlenecks in the method and how they might be addressed. A thorough analysis of the computational cost would help to assess the practical applicability of the proposed method.

### Questions

See weaknesses.

### Rating

5

### Confidence

3

**********
