### Summary

The paper introduces a new concept bottleneck model that uses energy-based models to represent the joint distribution of input, concepts, and class labels. The proposed method is shown to outperform existing concept bottleneck models on several benchmark datasets. The paper also provides a theoretical analysis of the proposed method and shows that it can be used to perform concept correction and conditional interpretation.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper proposes a new concept bottleneck model that uses energy-based models to represent the joint distribution of input, concepts, and class labels. This is a novel approach that has not been explored in previous work.
- The proposed method is shown to outperform existing concept bottleneck models on several benchmark datasets. This demonstrates the effectiveness of the proposed approach.
- The paper provides a theoretical analysis of the proposed method and shows that it can be used to perform concept correction and conditional interpretation. This is a valuable contribution that can help to improve the interpretability of concept bottleneck models.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the computational complexity of the proposed method. It is not clear how the computational cost of the proposed method compares to existing concept bottleneck models.
- The paper does not provide a detailed analysis of the sensitivity of the proposed method to the choice of hyperparameters. It is not clear how the performance of the proposed method varies with different choices of hyperparameters.

### Suggestions

The paper should include a more thorough analysis of the computational complexity of the proposed energy-based concept bottleneck model (ECBM). Specifically, the authors should provide a breakdown of the time and space complexity for each step of the training and inference process, including the computation of the energy function, the optimization procedure, and the calculation of conditional probabilities. This analysis should compare the computational cost of ECBM with existing concept bottleneck models (CBMs) and other relevant baselines. For example, the authors could analyze the number of floating-point operations (FLOPs) required for each method and discuss how the computational cost scales with the number of concepts, input dimensions, and training data size. Furthermore, the authors should provide empirical results on the training and inference time of ECBM and compare them with other CBMs on the same hardware. This would provide a more concrete understanding of the practical computational overhead of the proposed method.

In addition to computational complexity, the paper should also include a more detailed analysis of the sensitivity of the proposed method to the choice of hyperparameters. The authors should conduct a systematic study of how the performance of ECBM varies with different choices of hyperparameters, such as the learning rate, batch size, regularization parameters, and the architecture of the energy function. This analysis should include both quantitative results (e.g., accuracy, concept accuracy) and qualitative results (e.g., the interpretability of the learned concepts). The authors should also discuss the optimal range of values for each hyperparameter and provide guidelines for selecting appropriate values for different datasets. For example, the authors could perform a grid search over a range of hyperparameter values and plot the performance of ECBM as a function of each hyperparameter. This would help to identify the most critical hyperparameters and provide a better understanding of the robustness of the proposed method.

Finally, the paper should provide more details on the implementation of the proposed method. For example, the authors should specify the exact architecture of the energy function, the optimization algorithm used for training, and the details of the inference procedure. The authors should also provide the source code of the proposed method to ensure reproducibility of the results. This would allow other researchers to easily implement and evaluate the proposed method and compare it with other CBMs. Furthermore, the authors should provide more details on the datasets used in the experiments, including the number of training examples, the number of concepts, and the dimensionality of the input data. This would help to better understand the experimental results and compare them with other studies.

### Questions

- How does the computational cost of the proposed method compare to existing concept bottleneck models?
- How sensitive is the proposed method to the choice of hyperparameters?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
