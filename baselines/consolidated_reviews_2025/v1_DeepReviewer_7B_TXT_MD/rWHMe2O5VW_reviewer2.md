### Summary

The paper presents a novel approach to modeling interacting dynamical systems, specifically focusing on out-of-distribution (OOD) scenarios and complex underlying rules. The proposed method, called Graph ODE with factorized prototypes (GOODE), integrates context discovery and system parameters to enhance generalization. The authors conduct extensive experiments in both in-distribution (ID) and OOD settings, demonstrating the superiority of GOODE over existing methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a thorough analysis of the proposed method, including theoretical guarantees and empirical validation.
3. The experiments are comprehensive and cover a wide range of scenarios, including both ID and OOD settings.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed discussion of the limitations of the proposed method. It would be beneficial to include a section that addresses the potential shortcomings of GOODE, such as its computational complexity or sensitivity to specific types of data.
2. The paper could benefit from a more thorough comparison with existing methods, particularly in terms of computational efficiency and scalability. A detailed analysis of the computational cost of GOODE compared to other approaches would be valuable.
3. The paper could be improved by providing more detailed explanations of the experimental setup and results. For example, it would be helpful to include more information about the datasets used, the evaluation metrics, and the specific parameter settings for the experiments.

### Suggestions

The paper would significantly benefit from a more in-depth discussion of the limitations of the proposed Graph ODE with factorized prototypes (GOODE) method. While the strengths of the approach are clear, a balanced perspective requires an exploration of potential weaknesses. For instance, the computational cost of training and inference, especially when dealing with large-scale dynamical systems, should be thoroughly analyzed. The authors should consider discussing the scalability of the model with respect to the number of interacting entities and the length of the time series. Furthermore, it would be valuable to investigate the sensitivity of the model to hyperparameter tuning and the potential for overfitting, particularly when the amount of training data is limited. A detailed analysis of these aspects would provide a more complete understanding of the practical applicability of GOODE and guide future research directions.

To strengthen the paper, a more rigorous comparison with existing methods is needed, focusing on computational aspects. The authors should provide a detailed breakdown of the computational complexity of GOODE, including the time and memory requirements for both training and inference. This analysis should be compared against the computational costs of other state-of-the-art methods for modeling interacting dynamical systems. Specifically, the authors should consider comparing the computational efficiency of GOODE with methods that use different graph neural network architectures or ODE solvers. It would also be beneficial to include empirical results on the runtime and memory usage of GOODE on benchmark datasets, allowing for a practical assessment of its computational performance. This would help to establish the practical advantages and limitations of the proposed approach in terms of computational efficiency.

Finally, the paper would be improved by providing more detailed explanations of the experimental setup and results. The authors should include more information about the datasets used, such as the size, characteristics, and any preprocessing steps applied. A more detailed description of the evaluation metrics used to assess the performance of GOODE is also necessary. For example, if the task involves trajectory prediction, the authors should specify the metrics used to evaluate the accuracy and stability of the predicted trajectories. Furthermore, the paper should provide more details about the specific parameter settings used in the experiments, including the learning rate, batch size, and number of training epochs. This level of detail is crucial for ensuring the reproducibility of the results and for allowing other researchers to build upon the work presented in the paper.

### Questions

1. How does the proposed method handle the case where the system parameters are unknown or partially known?
2. How does the model perform in scenarios with a large number of interacting entities?
3. How does the model perform in scenarios with noisy or incomplete data?

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
