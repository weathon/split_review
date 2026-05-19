### Summary

The paper introduces a novel framework called Physics-Informed Coarse-grained data Learning (PICL) to address the challenges of modeling physical systems with coarse-grained data. The framework consists of an encoding module and a transition module, which are trained using a combination of data-driven and physics-informed objectives. The authors demonstrate the effectiveness of PICL on several partial differential equations, including the wave equation, linear shallow water equation, and nonlinear shallow water equation, showing superior predictive accuracy compared to baseline methods.

### Soundness

3

### Presentation

2

### Contribution

2

### Strengths

- The paper introduces a novel approach to integrating physics-based constraints with data-driven learning, which is a significant contribution to the field of machine learning for physical systems.
- The authors provide a detailed explanation of the PICL framework, including the encoding and transition modules, and the two-stage training process. The use of U-Net and FNO architectures is well-justified, and the authors provide a clear rationale for their choices.
- The paper includes extensive experiments on multiple benchmark problems, demonstrating the effectiveness of PICL in various scenarios. The results show that PICL outperforms baseline methods in terms of data efficiency and predictive accuracy.

### Weaknesses

#### Some Related Works


#### comment

 - The paper could benefit from a more detailed discussion of the limitations of the proposed approach, such as the types of physical systems or scenarios where PICL may not be applicable or may perform poorly. For example, the paper does not discuss the computational cost of training the model, or the sensitivity of the model to hyperparameter choices. It would be beneficial to understand the computational resources required for training and inference, and how these scale with the size of the problem. Additionally, the paper should discuss the potential for overfitting, especially given the use of deep learning models.
- The paper could provide more details on the implementation of the two-stage training process, including the specific optimization algorithms and hyperparameters used. The paper mentions the use of U-Net and FNO architectures, but it does not provide sufficient details on how these architectures are adapted for the specific problem. For example, the paper should discuss the specific choices of activation functions, normalization layers, and loss functions used in the encoding and transition modules. Furthermore, the paper should provide a more detailed explanation of the two-stage training process, including the specific criteria used to switch between the two stages, and the rationale behind the choice of hyperparameters.
- The paper could include a more thorough comparison with other state-of-the-art methods for modeling physical systems, such as those based on operator learning or physics-informed neural networks. The paper compares PICL to several baselines, but it does not provide a detailed analysis of the strengths and weaknesses of each method. It would be beneficial to understand how PICL compares to other methods in terms of accuracy, data efficiency, and computational cost. The paper should also discuss the potential for combining PICL with other methods to further improve performance.

### Suggestions

The paper would benefit from a more thorough discussion of the limitations of the proposed PICL framework. Specifically, the authors should address the types of physical systems where PICL is expected to perform well and where it might struggle. For example, it would be useful to discuss the applicability of PICL to systems with complex geometries, non-linearities, or time-varying boundary conditions. The authors should also discuss the potential for PICL to be applied to other types of physical systems, such as fluid dynamics, heat transfer, or electromagnetism. Furthermore, the paper should include a more detailed analysis of the computational cost of training and inference, and how these scale with the size of the problem. This analysis should include the number of parameters in the model, the training time, and the inference time. The authors should also discuss the potential for overfitting, and provide strategies for mitigating this issue, such as regularization techniques or early stopping. A more detailed discussion of these limitations would provide a more complete understanding of the capabilities and limitations of PICL.

To improve the clarity and reproducibility of the paper, the authors should provide more details on the implementation of the PICL framework. This should include a detailed description of the specific optimization algorithms and hyperparameters used in the training process. The authors should also provide a more detailed explanation of how the U-Net and FNO architectures are adapted for the specific problem. This should include a discussion of the specific choices of activation functions, normalization layers, and loss functions used in the encoding and transition modules. Furthermore, the paper should provide a more detailed explanation of the two-stage training process, including the specific criteria used to switch between the two stages, and the rationale behind the choice of hyperparameters. The authors should also provide a more detailed explanation of how the labeled and unlabeled data are used in the training process. This additional detail would make it easier for other researchers to reproduce the results and build upon the work.

The paper should include a more thorough comparison with other state-of-the-art methods for modeling physical systems. This comparison should include a detailed analysis of the strengths and weaknesses of each method, and how PICL compares to these methods in terms of accuracy, data efficiency, and computational cost. The authors should also discuss the potential for combining PICL with other methods to further improve performance. For example, the authors could explore the use of PICL as a pre-training step for other machine learning models, or the use of PICL in conjunction with other physics-informed methods. This would provide a more complete understanding of the potential of PICL and its place in the broader landscape of machine learning for physical systems. The authors should also discuss the potential for extending PICL to other types of data, such as experimental data or data from simulations.

### Questions

- How does the PICL framework handle scenarios where the coarse-grained data is noisy or incomplete? Are there any specific techniques or strategies used to mitigate the impact of data quality on the performance of the model?
- Can the PICL framework be extended to handle systems with multiple scales or multi-physics interactions? If so, what modifications would be required to the current architecture and training process?
- What are the computational costs associated with training and inference using the PICL framework? How do these costs compare to other state-of-the-art methods for modeling physical systems?
- How sensitive is the performance of PICL to the choice of hyperparameters, such as the learning rate, batch size, and network architecture? Are there any specific guidelines or best practices for tuning these hyperparameters?

### Rating

5

### Confidence

3

**********
