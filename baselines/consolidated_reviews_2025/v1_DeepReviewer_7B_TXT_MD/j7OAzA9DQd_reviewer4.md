### Summary

This paper proposes a new framework for sequential classification of multimodal longitudinal data, Longitudinal Ensemble Integration (LEI). LEI extends the Ensemble Integration (EI) framework by combining base predictors trained on individual modalities with a Long Short-Term Memory (LSTM) network for classification. The framework is evaluated on the task of early dementia detection using data from the Alzheimer’s Disease Prediction of Longitudinal Evolution (TADPOLE) Challenge. LEI outperforms existing approaches and identifies features that are consistent with known biological markers of dementia.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

The paper is well-structured and clearly written, making it easy to follow the proposed methodology and experimental setup. The authors provide a detailed description of the LEI framework, including the base predictors, LSTM network, and training procedure. The use of the TADPOLE dataset for evaluation is appropriate, as it is a challenging dataset with multiple modalities and longitudinal data. The authors also provide a thorough analysis of the identified features, which is important for understanding the underlying biological processes and for developing new treatments.

### Weaknesses

#### Some Related Works


#### comment

The paper does not provide a clear motivation for the proposed framework. The authors should explain why the proposed framework is needed and how it addresses the limitations of existing approaches. The paper does not provide a clear explanation of the base predictors used in the proposed framework. The authors should explain how the base predictors are trained and how they are combined with the LSTM network. The paper does not provide a clear explanation of the LSTM network used in the proposed framework. The authors should explain the architecture of the LSTM network and how it is trained. The paper does not provide a clear explanation of the training procedure used in the proposed framework. The authors should explain how the base predictors and the LSTM network are trained and how the training procedure is optimized. The paper does not provide a clear explanation of the evaluation metrics used in the proposed framework. The authors should explain how the evaluation metrics are calculated and how they are used to evaluate the performance of the proposed framework. The paper does not provide a clear explanation of the results obtained by the proposed framework. The authors should explain how the results are interpreted and what they mean in terms of the problem being addressed. The paper does not provide a clear explanation of the limitations of the proposed framework. The authors should discuss the limitations of the proposed framework and how they can be addressed in future work.

### Suggestions

The paper would benefit significantly from a more thorough discussion of the limitations of existing approaches and how the proposed framework addresses these shortcomings. For instance, the authors could discuss the challenges of handling multimodal data with varying time points and the difficulties in capturing temporal dependencies. They could also elaborate on the specific advantages of using an LSTM network over other sequence modeling techniques, such as recurrent neural networks or transformers, in the context of their task. Furthermore, the authors should provide a more detailed explanation of the base predictor selection process. They should discuss the criteria used for selecting the base predictors, the rationale behind choosing specific algorithms, and the potential impact of different base predictor choices on the overall performance of the LEI framework. It would be beneficial to include an ablation study to evaluate the contribution of each component of the framework, such as the base predictors and the LSTM network, to the final results. This would provide a better understanding of the framework's inner workings and the importance of each component.

To improve the clarity of the paper, the authors should provide more specific details about the implementation of the LSTM network. This includes the number of layers, the number of units in each layer, the activation functions used, and the optimization algorithm. They should also explain how the LSTM network is trained, including the loss function used, the batch size, and the number of epochs. Furthermore, the authors should provide a more detailed explanation of the training procedure for the base predictors. This includes the specific hyperparameters used, the optimization algorithm, and any regularization techniques applied. It would also be helpful to include a discussion of the computational cost of training the LEI framework and how it compares to other approaches. This would allow readers to better assess the feasibility of using the proposed framework in practice.

Finally, the paper needs a more comprehensive evaluation of the proposed framework. The authors should provide a more detailed analysis of the identified features, including their biological relevance and their potential for clinical applications. They should also compare the performance of the LEI framework with other state-of-the-art methods for multimodal longitudinal data analysis. This comparison should include a discussion of the strengths and weaknesses of each approach and the specific scenarios in which each approach is most suitable. The authors should also provide a more thorough analysis of the results, including a discussion of the statistical significance of the findings and the potential for overfitting. It would be beneficial to include a sensitivity analysis to evaluate the robustness of the results to different hyperparameter settings and data preprocessing choices.

### Questions

What is the motivation for the proposed framework? How does it address the limitations of existing approaches?
How are the base predictors selected and trained? What are the specific details of the base predictors used in the proposed framework?
What is the architecture of the LSTM network used in the proposed framework? How is the LSTM network trained?
How is the training procedure optimized? What are the specific details of the training procedure used in the proposed framework?
What are the evaluation metrics used in the proposed framework? How are they calculated and used to evaluate the performance of the proposed framework?
What are the results obtained by the proposed framework? How are they interpreted and what do they mean in terms of the problem being addressed?
What are the limitations of the proposed framework? How can they be addressed in future work?

### Rating

5

### Confidence

3

**********
