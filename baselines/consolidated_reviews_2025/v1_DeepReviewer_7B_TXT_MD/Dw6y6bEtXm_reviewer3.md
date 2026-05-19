### Summary

This paper proposes a new framework called PICL that integrates physics information into the training of models using coarse-grained data. The framework consists of an encoding module and a transition module. The encoding module generates a learnable fine-grained state from coarse-grained input, and the transition module predicts the subsequent state. The framework employs a two-stage training period, utilizing both labeled and unlabeled data to improve the model's performance. The authors demonstrate that PICL outperforms existing methods in terms of data efficiency and predictive accuracy across various PDEs.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-structured and clearly written, making it easy to follow and understand the proposed method and its contributions.
2. The authors provide a thorough explanation of the proposed method, including the encoding module, transition module, and the two-stage training process. The use of U-Net and FNO architectures is well-justified, and the authors provide a clear rationale for their choices.
3. The paper includes extensive experiments on multiple benchmark problems, demonstrating the effectiveness of PICL in various scenarios. The results show that PICL outperforms baseline methods in terms of data efficiency and predictive accuracy.
4. The authors provide a detailed ablation study, which helps to understand the impact of different components and hyperparameters on the performance of PICL. This study provides valuable insights into the design choices and their contributions to the overall performance of the framework.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a thorough comparison with existing methods, particularly those that use graph neural networks (GNNs) for learning complex physical systems. The authors should provide a more detailed comparison with methods such as "Learning to Simulate Complex Physics with Graph Networks" and other relevant works to demonstrate the advantages of their approach. Specifically, the comparison should not only focus on performance metrics but also on the underlying mechanisms that enable PICL to handle coarse-grained data effectively, and how this compares to the fine-grained approaches used in GNN-based methods.
2. The paper does not provide a clear explanation of how the proposed method handles the temporal dependencies in the data. The authors should clarify how the model captures the dynamics of the physical system over time, and how it ensures that the predictions are consistent with the underlying physics. It is not clear how the model avoids accumulating errors over time, especially when dealing with long-term simulations. The paper should also discuss the limitations of the method in capturing complex temporal dynamics, and how these limitations can be addressed.
3. The paper does not provide a detailed analysis of the computational cost of the proposed method. The authors should provide a comparison of the training and inference times of PICL with other methods, and discuss the scalability of the method to larger and more complex systems. The paper should also discuss the memory requirements of the method, and how these requirements scale with the size of the system. A more thorough analysis of the computational cost is needed to assess the practical applicability of the method.
4. The paper does not provide a detailed analysis of the sensitivity of the method to the choice of hyperparameters. The authors should provide a discussion of how the performance of the method varies with different hyperparameter settings, and how these settings can be chosen to optimize the performance of the method. The paper should also discuss the robustness of the method to different choices of hyperparameters, and how these choices can be made to ensure that the method is reliable and consistent.

### Suggestions

The paper would significantly benefit from a more thorough comparison with existing methods, particularly those employing graph neural networks (GNNs) for learning physical systems. The current comparison is insufficient, and the authors should delve deeper into the specific advantages and disadvantages of PICL compared to GNN-based approaches. This should include a detailed analysis of how PICL's coarse-grained approach compares to the fine-grained approaches used in GNNs, and what specific advantages PICL offers in terms of computational efficiency and accuracy when dealing with coarse-grained data. For example, the authors could analyze the performance of PICL and GNN-based methods on a range of PDEs with varying levels of complexity and data sparsity, and discuss the trade-offs between the two approaches. Furthermore, the authors should provide a more detailed explanation of the specific mechanisms that enable PICL to handle coarse-grained data effectively, and how this compares to the fine-grained approaches used in GNN-based methods. This could include a discussion of the specific types of physics information that PICL is able to capture, and how this information is used to improve the accuracy of the model.

To address the lack of clarity regarding temporal dependencies, the authors should provide a more detailed explanation of how the model captures the dynamics of the physical system over time. This should include a discussion of the specific mechanisms that prevent the accumulation of errors over time, especially in long-term simulations. For example, the authors could analyze the performance of PICL on a range of PDEs with varying time scales, and discuss the limitations of the method in capturing complex temporal dynamics. The authors should also discuss how the model ensures that the predictions are consistent with the underlying physics, and how this is achieved through the use of physics-informed loss functions. Furthermore, the authors should provide a more detailed analysis of the computational cost of the proposed method, including a comparison of the training and inference times of PICL with other methods. This analysis should also include a discussion of the memory requirements of the method, and how these requirements scale with the size of the system. The authors should also discuss the scalability of the method to larger and more complex systems, and provide insights into how the method can be optimized for practical applications.

Finally, the paper needs a more detailed analysis of the sensitivity of the method to the choice of hyperparameters. The authors should provide a discussion of how the performance of the method varies with different hyperparameter settings, and how these settings can be chosen to optimize the performance of the method. This should include a discussion of the robustness of the method to different choices of hyperparameters, and how these choices can be made to ensure that the method is reliable and consistent. For example, the authors could perform a sensitivity analysis of the key hyperparameters, such as the learning rate, the number of layers in the neural network, and the size of the training data. The authors should also discuss the impact of different hyperparameter settings on the convergence of the training process, and provide guidance on how to choose the optimal hyperparameter settings for different applications. This analysis should be supported by experimental results, and should provide a clear understanding of the trade-offs between different hyperparameter settings.

### Questions

1. How does the proposed method handle the temporal dependencies in the data? Specifically, how does the model capture the dynamics of the physical system over time, and how does it ensure that the predictions are consistent with the underlying physics?
2. What is the computational cost of the proposed method, and how does it compare to other methods for modeling physical systems? How does the method scale to larger and more complex systems?
3. How sensitive is the proposed method to the choice of hyperparameters? How can the hyperparameters be chosen to optimize the performance of the method, and how robust is the method to different choices of hyperparameters?

### Rating

6

### Confidence

4

**********
