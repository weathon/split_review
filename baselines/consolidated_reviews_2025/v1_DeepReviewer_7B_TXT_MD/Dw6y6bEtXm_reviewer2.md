### Summary

The paper introduces a novel framework called Physics-Informed Coarse-grained data Learning (PICL) that integrates physics information into the training of models using coarse-grained data. The framework consists of two modules: an encoding module that generates a learnable fine-grained state from coarse-grained input, and a transition module that predicts the subsequent state. The authors propose a two-stage training process that utilizes both labeled and unlabeled data to improve the model's performance. The paper demonstrates the effectiveness of PICL on three partial differential equations, showing its superiority over existing methods in terms of data efficiency and predictive accuracy.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is well-motivated and addresses a significant challenge in modeling physical systems with coarse-grained data.
3. The authors provide a comprehensive set of experiments that demonstrate the effectiveness of PICL on three different partial differential equations.

### Weaknesses

#### Some Related Works

[1] Learning to Simulate Complex Physics with Graph Networks
[2] Learning flexible body dynamics with 3d physics-aware neural networks
[3] Learning to simulate complex physics with Lagrangian neural networks
[4] Learning flexible body dynamics with lagrangian neural networks
[5] Learning to simulate complex physics with graph network smoothers

#### comment

1. The paper lacks a thorough comparison with existing methods, particularly those that use graph neural networks (GNNs) for learning complex physical systems. The authors should provide a more detailed comparison with methods such as [1,2,3,4,5] to demonstrate the advantages of their approach. Specifically, the paper should discuss how PICL's coarse-grained approach compares to the fine-grained approaches used in GNN-based methods, and what specific advantages PICL offers in terms of computational efficiency and accuracy when dealing with coarse-grained data. A more detailed analysis of the trade-offs between these approaches is needed.
2. The paper does not provide a clear explanation of how the proposed method handles the temporal dependencies in the data. The authors should clarify how the model captures the dynamics of the physical system over time, and how it ensures that the predictions are consistent with the underlying physics. It is not clear how the model avoids accumulating errors over time, especially when dealing with long-term simulations. The paper should also discuss the limitations of the method in capturing complex temporal dynamics, and how these limitations can be addressed.
3. The paper does not provide a detailed analysis of the computational cost of the proposed method. The authors should provide a comparison of the training and inference times of PICL with other methods, and discuss the scalability of the method to larger and more complex systems. The paper should also discuss the memory requirements of the method, and how these requirements scale with the size of the system. A more thorough analysis of the computational cost is needed to assess the practical applicability of the method.
4. The paper does not provide a detailed analysis of the sensitivity of the method to the choice of hyperparameters. The authors should provide a discussion of how the performance of the method varies with different hyperparameter settings, and how these settings can be chosen to optimize the performance of the method. The paper should also discuss the robustness of the method to different choices of hyperparameters, and how these choices can be made to ensure that the method is reliable and consistent.

### Suggestions

The paper would benefit significantly from a more in-depth comparison with existing methods, particularly those employing graph neural networks (GNNs) for learning physical systems. The authors should provide a detailed analysis of how PICL's coarse-grained approach compares to the fine-grained approaches used in GNN-based methods, and what specific advantages PICL offers in terms of computational efficiency and accuracy when dealing with coarse-grained data. This comparison should not only focus on performance metrics but also on the underlying mechanisms that enable PICL to handle coarse-grained data effectively. For instance, the authors could discuss how the encoding module in PICL captures the essential information from coarse-grained data, and how this information is then used to predict the subsequent state. A more thorough discussion of the trade-offs between PICL and GNN-based methods is needed, including a discussion of the limitations of each approach and the specific scenarios where PICL is expected to perform better.

Furthermore, the paper needs to provide a more detailed explanation of how the proposed method handles temporal dependencies in the data. The authors should clarify how the model captures the dynamics of the physical system over time, and how it ensures that the predictions are consistent with the underlying physics. It is crucial to discuss the mechanisms that prevent the accumulation of errors over time, especially in long-term simulations. The authors should also discuss the limitations of the method in capturing complex temporal dynamics, and how these limitations can be addressed. For example, the authors could explore the use of recurrent neural networks or other temporal modeling techniques to improve the model's ability to capture long-term dependencies. A more detailed analysis of the model's ability to handle different types of temporal dynamics is needed to fully assess its capabilities.

Finally, the paper should include a more detailed analysis of the computational cost and sensitivity of the proposed method. The authors should provide a comparison of the training and inference times of PICL with other methods, and discuss the scalability of the method to larger and more complex systems. The paper should also discuss the memory requirements of the method, and how these requirements scale with the size of the system. A more thorough analysis of the computational cost is needed to assess the practical applicability of the method. Additionally, the authors should provide a discussion of how the performance of the method varies with different hyperparameter settings, and how these settings can be chosen to optimize the performance of the method. The paper should also discuss the robustness of the method to different choices of hyperparameters, and how these choices can be made to ensure that the method is reliable and consistent.

### Questions

1. How does the proposed method handle the temporal dependencies in the data? Specifically, how does the model capture the dynamics of the physical system over time, and how does it ensure that the predictions are consistent with the underlying physics?
2. What is the computational cost of the proposed method, and how does it compare to other methods for modeling physical systems? How does the method scale to larger and more complex systems?
3. How sensitive is the proposed method to the choice of hyperparameters? How can the hyperparameters be chosen to optimize the performance of the method, and how robust is the method to different choices of hyperparameters?

### Rating

5

### Confidence

4

**********
