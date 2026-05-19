### Summary

This paper introduces a novel framework called Physics-Informed Coarse-grained data Learning (PICL), which integrates physics information into the training of models using coarse-grained data. The framework comprises two modules: an encoding module that generates a learnable fine-grained state from coarse-grained input, and a transition module that predicts the subsequent state. The authors propose a two-stage training period that utilizes both labeled and unlabeled data to improve the model's predictive ability. The framework is tested on three partial differential equations, demonstrating superior predictive accuracy and data efficiency compared to existing methods.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel framework, PICL, that integrates physics information into the training of models using coarse-grained data. This approach addresses the challenges of modeling physical systems with limited data.
2. The authors provide a comprehensive set of experiments that demonstrate the effectiveness of PICL on three different partial differential equations. The results show that PICL outperforms existing methods in terms of data efficiency and predictive accuracy.
3. The paper is well-written and easy to follow. The authors provide a clear explanation of the proposed method and its underlying principles.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a thorough comparison with existing methods, particularly those that use graph neural networks (GNNs) for learning complex physical systems. The authors should provide a more detailed comparison with methods such as "Learning to Simulate Complex Physics with Graph Networks" and other relevant works to demonstrate the advantages of their approach. Specifically, the comparison should not only focus on performance metrics but also on the underlying mechanisms that enable PICL to handle coarse-grained data effectively, and how this compares to the fine-grained approaches used in GNN-based methods.
2. The paper does not provide a clear explanation of how the proposed method handles the temporal dependencies in the data. The authors should clarify how the model captures the dynamics of the physical system over time, and how it ensures that the predictions are consistent with the underlying physics. It is not clear how the model avoids accumulating errors over time, especially when dealing with long-term simulations. The paper should also discuss the limitations of the method in capturing complex temporal dynamics, and how these limitations can be addressed.
3. The paper does not provide a detailed analysis of the computational cost of the proposed method. The authors should provide a comparison of the training and inference times of PICL with other methods, and discuss the scalability of the method to larger and more complex systems. The paper should also discuss the memory requirements of the method, and how these requirements scale with the size of the system. A more thorough analysis of the computational cost is needed to assess the practical applicability of the method.
4. The paper does not provide a detailed analysis of the sensitivity of the method to the choice of hyperparameters. The authors should provide a discussion of how the performance of the method varies with different hyperparameter settings, and how these settings can be chosen to optimize the performance of the method. The paper should also discuss the robustness of the method to different choices of hyperparameters, and how these choices can be made to ensure that the method is reliable and consistent.

### Suggestions

The paper would benefit significantly from a more in-depth comparison with existing methods, particularly those employing graph neural networks (GNNs) for learning physical systems. The authors should provide a detailed analysis of how PICL's coarse-grained approach compares to the fine-grained approaches used in GNN-based methods. This comparison should not only focus on performance metrics but also on the underlying mechanisms that enable each method to handle the specific challenges of modeling physical systems with limited data. For instance, the authors could analyze the types of physics information that PICL is able to capture and how this information is used to improve the accuracy of the model. A more thorough discussion of the trade-offs between PICL and GNN-based methods would be valuable, including a discussion of the specific scenarios where each method is expected to perform better. This would help to better position the contribution of the paper and highlight its unique advantages.

To address the lack of clarity regarding temporal dependencies, the authors should provide a more detailed explanation of how the model captures the dynamics of the physical system over time. This should include a discussion of the specific mechanisms that prevent the accumulation of errors over time, especially in long-term simulations. For example, the authors could analyze the performance of PICL on a range of PDEs with varying time scales and discuss the limitations of the method in capturing complex temporal dynamics. The authors should also discuss how the model ensures that the predictions are consistent with the underlying physics, and how this is achieved through the use of physics-informed loss functions. Furthermore, the authors should provide a more detailed analysis of the model's ability to handle different types of temporal dependencies, such as those that involve periodic or chaotic behavior. This would help to better understand the strengths and limitations of the proposed approach.

Finally, the paper needs a more detailed analysis of the computational cost and sensitivity of the method. The authors should provide a comparison of the training and inference times of PICL with other methods, and discuss the scalability of the method to larger and more complex systems. This analysis should include a discussion of the memory requirements of the method, and how these requirements scale with the size of the system. The authors should also provide a discussion of the sensitivity of the method to the choice of hyperparameters, including a discussion of how the performance of the method varies with different hyperparameter settings. The authors should also discuss the robustness of the method to different choices of hyperparameters, and how these choices can be made to ensure that the method is reliable and consistent. This analysis should be supported by experimental results and should provide a clear understanding of the trade-offs between performance and computational cost.

### Questions

1. How does the proposed method handle the temporal dependencies in the data? Specifically, how does the model capture the dynamics of the physical system over time, and how does it ensure that the predictions are consistent with the underlying physics?
2. What is the computational cost of the proposed method, and how does it compare to other methods for modeling physical systems? How does the method scale to larger and more complex systems?
3. How sensitive is the proposed method to the choice of hyperparameters? How can the hyperparameters be chosen to optimize the performance of the method, and how robust is the method to different choices of hyperparameters?

### Rating

6

### Confidence

4

**********
