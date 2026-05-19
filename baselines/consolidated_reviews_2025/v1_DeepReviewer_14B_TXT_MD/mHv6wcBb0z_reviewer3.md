### Summary

This paper addresses the problem of model collapse in Deep Canonical Correlation Analysis (DCCA) for multi-view representation learning. The authors propose a novel noise regularization approach to prevent model collapse in DCCA. The key idea is to enforce the Correlation Invariant Property (CIP) in DNNs by adding random data to constrain the weight matrices. The authors provide theoretical analysis showing that CIP is equivalent to the full-rank property of weight matrices, which is crucial for preventing model collapse. They also develop a framework to construct synthetic data with different common and complementary information for evaluating multi-view representation learning methods. The proposed NR-DCCA method is shown to outperform baselines stably and consistently in both synthetic and real-world datasets.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper identifies and addresses a significant problem in DCCA-based methods for multi-view representation learning, which is the model collapse issue.
- The proposed noise regularization approach is simple yet effective, and it can be generalized to other DCCA-based methods.
- The paper provides rigorous theoretical analysis to justify the proposed approach, showing that CIP is equivalent to the full-rank property of weight matrices.
- The authors develop a framework to construct synthetic data with different common and complementary information for evaluating multi-view representation learning methods.
- The proposed NR-DCCA method is shown to outperform baselines stably and consistently in both synthetic and real-world datasets.

### Weaknesses

#### Some Related Works


#### comment

 - The paper could provide more details on the implementation of the proposed method, such as the specific architecture of the neural networks used and the hyperparameter settings.
- The paper could also discuss the limitations of the proposed method and potential directions for future research.

### Suggestions

The paper would benefit from a more detailed explanation of the neural network architectures employed in the NR-DCCA method. Specifically, the number of layers, the type of activation functions, and the dimensionality of the hidden layers should be explicitly stated. Furthermore, the optimization algorithm used, along with its specific parameters (e.g., learning rate, batch size, number of epochs), should be clearly outlined. This level of detail is crucial for reproducibility and for other researchers to build upon this work. For instance, if the authors used a specific type of recurrent neural network, they should specify the number of recurrent units and the type of recurrent cell (e.g., LSTM, GRU). Without these details, it is difficult to assess the practical applicability of the proposed method and to compare it with other existing approaches.

Additionally, the paper should delve deeper into the limitations of the proposed NR-DCCA method. While the authors mention that the method is effective in preventing model collapse, they should also discuss scenarios where it might fail or underperform. For example, it would be beneficial to analyze the sensitivity of the method to different levels of noise in the input data. Does the regularization parameter need to be tuned differently for different datasets? What are the computational costs associated with the proposed method, and how do they scale with the size of the input data? Addressing these questions would provide a more comprehensive understanding of the method's strengths and weaknesses. Furthermore, the authors should explore the potential impact of the choice of noise distribution on the performance of the method. Are there specific types of noise that are more effective in preventing model collapse, and why?

Finally, the paper should provide more concrete directions for future research. While the authors mention that the proposed noise regularization approach can be generalized to other DCCA-based methods, they should provide specific examples of how this generalization can be achieved. For instance, how would the method be adapted to handle different types of input data, such as images or text? What are the potential challenges in applying the method to large-scale datasets, and how can these challenges be addressed? Furthermore, the authors could explore the possibility of combining the proposed method with other regularization techniques, such as dropout or weight decay, to further improve the robustness of the model. These suggestions would help to guide future research in this area and to further advance the field of multi-view representation learning.

### Questions

- Can the authors provide more details on the implementation of the proposed method, such as the specific architecture of the neural networks used and the hyperparameter settings?
- What are the limitations of the proposed method, and what are the potential directions for future research?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
