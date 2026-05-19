### Summary

This paper proposes a new framework for sequential classification of multimodal longitudinal data, called Longitudinal Ensemble Integration (LEI). The proposed framework extends the Ensemble Integration (EI) framework to handle longitudinal data by combining base predictors trained on individual modalities with a Long Short-Term Memory (LSTM) network for classification. The authors evaluate LEI on the task of early dementia detection using data from the Alzheimer’s Disease Prediction of Longitudinal Evolution (TADPOLE) Challenge. The results show that LEI outperforms existing approaches and identifies features that are consistent with known biological markers of dementia.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

- The proposed framework, LEI, is a novel extension of the Ensemble Integration (EI) framework to handle multimodal longitudinal data, which is a challenging and important problem in many fields, including healthcare.
- The authors provide a clear and detailed description of the proposed framework, including the base predictors, the LSTM network, and the training procedure.
- The authors evaluate LEI on a real-world dataset, the TADPOLE dataset, which is a challenging dataset with multiple modalities and longitudinal data.
- The authors provide a detailed analysis of the identified features, which is important for understanding the underlying biological processes and for developing new treatments.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a clear motivation for the proposed framework. The authors should explain why the proposed framework is needed and how it addresses the limitations of existing approaches.
- The paper does not provide a clear explanation of the base predictors used in the proposed framework. The authors should explain how the base predictors are trained and how they are combined with the LSTM network.
- The paper does not provide a clear explanation of the LSTM network used in the proposed framework. The authors should explain the architecture of the LSTM network and how it is trained.
- The paper does not provide a clear explanation of the training procedure used in the proposed framework. The authors should explain how the base predictors and the LSTM network are trained and how the training procedure is optimized.
- The paper does not provide a clear explanation of the evaluation metrics used in the proposed framework. The authors should explain how the evaluation metrics are calculated and how they are used to evaluate the performance of the proposed framework.
- The paper does not provide a clear explanation of the results obtained by the proposed framework. The authors should explain how the results are interpreted and what they mean in terms of the problem being addressed.
- The paper does not provide a clear explanation of the limitations of the proposed framework. The authors should discuss the limitations of the proposed framework and how they can be addressed in future work.

### Suggestions

The paper would benefit significantly from a more detailed explanation of the base predictor selection process. The authors mention using KNNImpute for missing data, but they do not specify the features used as input to the KNNImputer. It is crucial to understand which features (e.g., demographic, cognitive test scores, imaging biomarkers) are used to generate the base predictions for each modality. Furthermore, the authors should clarify how the base predictors are trained, including the specific hyperparameters used and the optimization algorithm. For example, if logistic regression is used, what regularization technique is applied, and what is the value of the regularization parameter? A more detailed description of the base predictor training process would allow for better reproducibility and a deeper understanding of the framework's behavior. The authors should also discuss the rationale behind choosing specific base predictors over others and how these choices impact the overall performance of the LEI framework.

Regarding the LSTM network, the paper lacks specific details about its architecture. The authors should specify the number of LSTM layers, the number of units in each layer, and the activation functions used. It is also important to explain how the outputs of the base predictors are fed into the LSTM network. Are the outputs concatenated, or is there a more complex integration mechanism? The authors should also describe the training procedure for the LSTM network, including the loss function used, the optimizer, and the number of epochs. Furthermore, the authors should discuss the rationale behind choosing an LSTM network over other sequence models, such as GRUs or Transformers. A more detailed explanation of the LSTM architecture and training procedure would allow for a better understanding of how the framework captures temporal dependencies in the data. The authors should also discuss the computational cost of training the LSTM network and how it scales with the length of the input sequences.

Finally, the paper needs a more thorough explanation of the evaluation metrics and the results. The authors should clearly define each metric used (e.g., F1-score, precision, recall) and explain how it is calculated. They should also discuss the limitations of each metric and why they are appropriate for evaluating the performance of the proposed framework. For example, if the classes are imbalanced, the authors should discuss the limitations of accuracy and why F1-score is a more appropriate metric. The authors should also provide a more detailed analysis of the results, including a comparison of the performance of the LEI framework with other state-of-the-art methods. They should also discuss the statistical significance of the results and provide confidence intervals for the performance metrics. A more thorough explanation of the evaluation metrics and results would allow for a better understanding of the strengths and weaknesses of the proposed framework.

### Questions

- What is the motivation for the proposed framework? How does it address the limitations of existing approaches?
- How are the base predictors selected and trained? What are the specific details of the base predictors used in the proposed framework?
- What is the architecture of the LSTM network used in the proposed framework? How is the LSTM network trained?
- How is the training procedure optimized? What are the specific details of the training procedure used in the proposed framework?
- What are the evaluation metrics used in the proposed framework? How are they calculated and used to evaluate the performance of the proposed framework?
- What are the results obtained by the proposed framework? How are they interpreted and what do they mean in terms of the problem being addressed?
- What are the limitations of the proposed framework? How can they be addressed in future work?

### Rating

3

### Confidence

3

**********
