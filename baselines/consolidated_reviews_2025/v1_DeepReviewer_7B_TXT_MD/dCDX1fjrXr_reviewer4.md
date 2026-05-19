### Summary

The paper introduces a novel problem called Sparse Labels Node Classification (SLNC), which aims to enhance the performance of Graph Neural Networks (GNNs) in node classification tasks with very few labeled nodes, without requiring per-class basis for labeling. To address this challenge, the authors propose a framework called ELI (Estimating Label Information), which estimates label information and enhances reformulations of well-known semi-supervised learning frameworks. The framework is evaluated on several benchmark attributed graphs and demonstrates significant improvements over baselines, particularly when the number of labeled nodes is extremely small.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a new problem called Sparse Labels Node Classification (SLNC), which is a practical and challenging task in real-world applications. The authors provide a well-motivated problem statement and clearly define the SLNC task, making it easy for readers to understand the significance of this work.
2. The paper proposes a novel framework called ELI (Estimating Label Information) to address the SLNC problem. The framework is technically sound and well-designed, with clear steps for label distribution estimation, key nodes selection, label distribution incorporation, and optimization. The authors provide a detailed explanation of each step, making it easy for readers to follow the methodology.
3. The paper presents extensive experimental results on several benchmark attributed graphs, demonstrating the effectiveness of the proposed framework. The results show significant improvements over baselines, particularly when the number of labeled nodes is extremely small. The authors also provide a thorough analysis of the results, discussing the performance of the framework under different settings.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational complexity of the proposed framework, which is an important aspect to consider for practical applications. Specifically, the paper lacks a breakdown of the time complexity for each step of the ELI framework, including the label distribution estimation, key node selection, and label distribution incorporation. This makes it difficult to assess the scalability of the method, especially for large-scale graphs. Furthermore, the memory requirements of the proposed method are not discussed, which is crucial for practical deployment.
2. The paper does not provide a comprehensive comparison with other state-of-the-art methods for semi-supervised learning on graphs. While the authors compare their method with some baselines, a more thorough comparison with other recent methods would strengthen the paper's contribution. For example, methods that explicitly model uncertainty in label predictions or those that use different forms of graph regularization could provide a more comprehensive benchmark. The current comparison is limited and does not fully demonstrate the superiority of the proposed method.
3. The paper does not discuss the limitations of the proposed framework and potential directions for future research. It is important to acknowledge the assumptions made by the framework and the scenarios where it might not perform well. For instance, the paper does not discuss the sensitivity of the framework to the choice of hyperparameters or the potential impact of noisy labels. A discussion of these limitations would provide a more balanced view of the work.

### Suggestions

The paper would benefit significantly from a more detailed analysis of the computational complexity of the proposed ELI framework. The authors should provide a breakdown of the time complexity for each step of the framework, including the label distribution estimation, key node selection, and label distribution incorporation. This analysis should consider both the theoretical complexity and the practical implications for large-scale graphs. Furthermore, the authors should discuss the memory requirements of the proposed method, as this is a crucial factor for practical deployment. A comparison of the computational cost of ELI with other state-of-the-art methods would also be beneficial, providing a more complete picture of the trade-offs involved. This analysis should include a discussion of the scalability of the method with respect to the number of nodes and edges in the graph.

To strengthen the paper's contribution, the authors should include a more comprehensive comparison with other state-of-the-art methods for semi-supervised learning on graphs. This comparison should include methods that explicitly model uncertainty in label predictions, as well as those that use different forms of graph regularization. The authors should also consider comparing their method with techniques that are specifically designed for sparse label scenarios. This would provide a more robust evaluation of the proposed method and demonstrate its superiority over existing approaches. The comparison should include a discussion of the strengths and weaknesses of each method, highlighting the specific scenarios where the proposed method performs best.

Finally, the paper should include a more thorough discussion of the limitations of the proposed framework and potential directions for future research. The authors should acknowledge the assumptions made by the framework and the scenarios where it might not perform well. For example, the paper should discuss the sensitivity of the framework to the choice of hyperparameters and the potential impact of noisy labels. A discussion of these limitations would provide a more balanced view of the work and identify areas for future improvement. The authors should also discuss potential extensions of the framework, such as incorporating uncertainty estimation or exploring different forms of graph regularization.

### Questions

1. How does the proposed framework handle noisy labels in the training data? Are there any mechanisms in place to mitigate the impact of noisy labels on the model's performance?
2. How does the proposed framework scale to very large graphs with millions of nodes and edges? Are there any optimizations or approximations that can be used to improve the scalability of the method?
3. How sensitive is the proposed framework to the choice of hyperparameters? Are there any guidelines or best practices for selecting the optimal hyperparameters for different datasets?
4. How does the proposed framework compare to other state-of-the-art methods for semi-supervised learning on graphs, particularly those that explicitly model uncertainty in label predictions?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
