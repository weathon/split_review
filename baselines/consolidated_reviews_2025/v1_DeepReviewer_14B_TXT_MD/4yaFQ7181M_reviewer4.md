### Summary

The paper presents a new method for continuous spatio-temporal physical simulations from sparse observations. The key idea is to formulate the task as a double observation problem, with two interlinked dynamical systems defined on sparse positions and the continuous domain. The practical implementation involves recurrent GNNs and a spatio-temporal attention observer. The method is evaluated on three standard datasets in fluid dynamics and demonstrates superior performance compared to existing baselines.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a novel approach for continuous spatio-temporal simulation of physical systems, addressing the limitations of traditional numerical methods and existing data-driven approaches.
2. The proposed method leverages two interlinked dynamical systems, enabling both forecasting and interpolation of solutions. This dual approach allows for a more comprehensive understanding and prediction of physical phenomena.
3. The implementation involves recurrent GNNs and a spatio-temporal attention observer, demonstrating the effectiveness of the proposed method in capturing complex spatio-temporal dependencies.
4. The method is evaluated on three standard datasets in fluid dynamics and demonstrates superior performance compared to existing baselines, highlighting its potential for real-world applications.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the computational cost associated with the proposed method. While the authors mention the efficiency of their approach, a more thorough comparison with existing methods in terms of computational resources and time would be beneficial. Specifically, the paper should include a breakdown of the computational cost associated with each component of the model, such as the recurrent GNN and the spatio-temporal attention observer. Furthermore, the analysis should consider the scalability of the method with respect to the size of the input data and the complexity of the physical system being simulated. A comparison with the computational cost of traditional numerical methods, such as finite element or finite volume methods, would also be valuable to understand the trade-offs between accuracy and computational efficiency.

2. The paper does not provide a comprehensive discussion on the limitations of the proposed method. While the authors acknowledge the challenges of learning from sparse observations, a more detailed analysis of the scenarios where the method might fail or perform poorly would be valuable. For instance, the paper should discuss the sensitivity of the method to the choice of hyperparameters, the quality of the training data, and the complexity of the underlying physical system. It would also be beneficial to explore the limitations of the method in handling non-linear or chaotic systems, where small errors can quickly propagate and lead to inaccurate predictions. A discussion of the potential for error accumulation over long prediction horizons would also be valuable.

### Suggestions

To address the lack of detailed computational cost analysis, the authors should include a comprehensive breakdown of the computational resources required by each component of their model. This should include the time complexity of the recurrent GNN, the spatio-temporal attention observer, and the overall training and inference processes. The analysis should also consider the memory requirements of the model, particularly when dealing with large-scale simulations. Furthermore, the authors should compare the computational cost of their method with that of existing data-driven approaches and traditional numerical methods, providing a clear understanding of the trade-offs between accuracy and computational efficiency. This comparison should be performed on a standardized benchmark dataset, using consistent hardware and software configurations, to ensure a fair and objective evaluation. The authors should also investigate the scalability of their method with respect to the size of the input data and the complexity of the physical system being simulated, providing insights into the practical applicability of their approach.

To address the lack of a comprehensive discussion on the limitations of the proposed method, the authors should provide a detailed analysis of the scenarios where the method might fail or perform poorly. This should include a discussion of the sensitivity of the method to the choice of hyperparameters, such as the learning rate, the number of layers in the GNN, and the size of the attention window. The authors should also investigate the impact of the quality of the training data on the performance of the method, considering the effects of noise, outliers, and incomplete observations. Furthermore, the authors should explore the limitations of the method in handling non-linear or chaotic systems, where small errors can quickly propagate and lead to inaccurate predictions. This could involve testing the method on benchmark problems with known chaotic behavior and analyzing the long-term stability of the predictions. The authors should also discuss the potential for error accumulation over long prediction horizons, providing insights into the practical limitations of their approach.

Finally, the authors should consider including a more detailed discussion of the potential for extending their method to other types of physical systems beyond fluid dynamics. This could involve exploring the applicability of their approach to solid mechanics, heat transfer, or electromagnetism. The authors should also discuss the potential for incorporating additional physical constraints or priors into their model, such as conservation laws or symmetry properties. This could lead to more robust and accurate predictions, particularly in scenarios where the training data is limited or noisy. Furthermore, the authors should consider the potential for using their method in conjunction with traditional numerical methods, leveraging the strengths of both approaches to achieve more accurate and efficient simulations.

### Questions

1. How does the proposed method handle scenarios with highly sparse or noisy observations? Are there any specific techniques or modifications that can be employed to improve the robustness of the method in such cases?
2. Can the proposed method be extended to handle more complex physical systems with non-linear or chaotic behavior? What are the potential challenges and limitations in such scenarios?
3. How does the performance of the proposed method compare to traditional numerical methods in terms of accuracy and computational efficiency? Are there any specific scenarios where the proposed method outperforms or underperforms traditional methods?
4. What are the potential applications of the proposed method beyond fluid dynamics? Can it be applied to other areas of physics or engineering, such as solid mechanics, heat transfer, or electromagnetism?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
