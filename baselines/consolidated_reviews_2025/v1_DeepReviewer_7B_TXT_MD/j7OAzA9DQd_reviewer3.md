### Summary

This paper proposes a new framework for sequential classification of multimodal longitudinal data, called Longitudinal Ensemble Integration (LEI). The proposed framework extends the Ensemble Integration (EI) framework to handle longitudinal data by combining base predictors trained on individual modalities with a Long Short-Term Memory (LSTM) network for classification. The authors evaluate LEI on the task of early dementia detection using data from the Alzheimer’s Disease Prediction of Longitudinal Evolution (TADPOLE) Challenge. The results show that LEI outperforms existing approaches and identifies features that are consistent with known biological markers of dementia.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The proposed framework, LEI, is a novel extension of the Ensemble Integration (EI) framework to handle multimodal longitudinal data, which is a challenging and important problem in many fields, including healthcare.
2. The authors provide a clear and detailed description of the proposed framework, including the base predictors, the LSTM network, and the training procedure.
3. The authors evaluate LEI on a real-world dataset, the TADPOLE dataset, which is a challenging dataset with multiple modalities and longitudinal data.
4. The authors provide a detailed analysis of the identified features, which is important for understanding the underlying biological processes and for developing new treatments.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a clear motivation for the proposed framework. The authors should explain why the proposed framework is needed and how it addresses the limitations of existing approaches.
2. The paper does not provide a clear explanation of the base predictors used in the proposed framework. The authors should explain how the base predictors are trained and how they are combined with the LSTM network.
3. The paper does not provide a clear explanation of the LSTM network used in the proposed framework. The authors should explain the architecture of the LSTM network and how it is trained.
4. The paper does not provide a clear explanation of the training procedure used in the proposed framework. The authors should explain how the base predictors and the LSTM network are trained and how the training procedure is optimized.
5. The paper does not provide a clear explanation of the evaluation metrics used in the proposed framework. The authors should explain how the evaluation metrics are calculated and how they are used to evaluate the performance of the proposed framework.
6. The paper does not provide a clear explanation of the results obtained by the proposed framework. The authors should explain how the results are interpreted and what they mean in terms of the problem being addressed.
7. The paper does not provide a clear explanation of the limitations of the proposed framework. The authors should discuss the limitations of the proposed framework and how they can be addressed in future work.

### Suggestions

The paper would benefit from a more thorough discussion of the motivation behind the proposed Longitudinal Ensemble Integration (LEI) framework. While the authors mention addressing the limitations of existing approaches, they do not clearly articulate what these limitations are or why the EI framework, which is not specifically designed for longitudinal data, is a suitable starting point. A more detailed explanation of the shortcomings of current methods for multimodal longitudinal data analysis would help to justify the need for LEI. Furthermore, the authors should elaborate on the specific challenges posed by the TADPOLE dataset and how LEI is uniquely positioned to overcome these challenges. For example, are there specific temporal dependencies or modality-specific noise issues that LEI is designed to handle? Without a clear articulation of these points, the reader is left to wonder why LEI is a necessary advancement over existing techniques.

To improve the clarity of the paper, the authors should provide more specific details about the implementation of the base predictors and the LSTM network. For the base predictors, the authors should specify the exact algorithms used, including any hyperparameter settings. For example, if logistic regression is used, what regularization method is applied, and what is the value of the regularization parameter? Similarly, for the LSTM network, the authors should specify the number of layers, the number of units in each layer, the activation functions used, and the optimization algorithm. The authors should also explain how the outputs of the base predictors are fed into the LSTM network. Are they concatenated, or is there a more complex integration mechanism? These details are crucial for reproducibility and for understanding the inner workings of the LEI framework. Without these specifics, it is difficult to assess the technical soundness of the proposed method.

Finally, the paper needs a more detailed explanation of the training procedure. The authors should clarify how the base predictors and the LSTM network are trained, including the loss functions used, the optimization algorithms, and the number of epochs. It is also important to discuss how the training procedure is optimized. For example, are there any techniques used to prevent overfitting, such as dropout or early stopping? The authors should also explain how the hyperparameters of the base predictors and the LSTM network are selected. Were they tuned using a validation set? Without a clear explanation of the training procedure, it is difficult to assess the validity of the experimental results. Furthermore, the authors should provide a more detailed explanation of the evaluation metrics used. They should explain how each metric is calculated and how it is used to evaluate the performance of the proposed framework. For example, what is the rationale for using F1-score instead of accuracy? Why is the weighted ordinal cost function used for the LSTM? These details are important for understanding the experimental results and for comparing the performance of LEI with other methods.

### Questions

1. What is the motivation for the proposed framework? How does it address the limitations of existing approaches?
2. How are the base predictors selected and trained? What are the specific details of the base predictors used in the proposed framework?
3. What is the architecture of the LSTM network used in the proposed framework? How is the LSTM network trained?
4. How is the training procedure optimized? What are the specific details of the training procedure used in the proposed framework?
5. What are the evaluation metrics used in the proposed framework? How are they calculated and used to evaluate the performance of the proposed framework?
6. What are the results obtained by the proposed framework? How are they interpreted and what do they mean in terms of the problem being addressed?
7. What are the limitations of the proposed framework? How can they be addressed in future work?

### Rating

3

### Confidence

3

**********
