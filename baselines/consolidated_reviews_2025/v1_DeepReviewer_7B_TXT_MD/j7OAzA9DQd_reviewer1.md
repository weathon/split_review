### Summary

The paper proposes a framework for sequential classification of multimodal data, Longitudinal Ensemble Integration (LEI), which extends the capabilities of the Ensemble Integration (EI) framework to handle longitudinal data. The framework is evaluated on the task of early dementia detection using data from the Alzheimer’s Disease Prediction of Longitudinal Evolution (TADPOLE) Challenge. The authors compare the performance of LEI with existing approaches and analyze the identified features.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

The paper addresses the important problem of multimodal data classification, which is relevant in many fields, including healthcare. The proposed framework is well-motivated, and the authors provide a clear description of the method and its components. The experimental results demonstrate the effectiveness of the proposed approach in the context of early dementia detection.

### Weaknesses

#### Some Related Works


#### comment

The paper lacks a thorough comparison with existing state-of-the-art methods for multimodal data classification, particularly those designed for longitudinal data. The experimental evaluation is limited to a single dataset, which raises concerns about the generalizability of the results. The paper also does not provide a detailed analysis of the computational complexity of the proposed framework, which is important for practical applications. Furthermore, the paper does not discuss the limitations of the proposed approach and potential directions for future research. The analysis of the identified features is also not very detailed, and it is not clear how these features relate to the underlying biological processes.

### Suggestions

The authors should conduct a more comprehensive comparison with existing state-of-the-art methods for multimodal data classification, especially those that are designed for longitudinal data. This comparison should include a wider range of methods, such as those based on recurrent neural networks or attention mechanisms, to provide a more robust evaluation of the proposed approach. The experimental evaluation should also be expanded to include multiple datasets to demonstrate the generalizability of the proposed framework. This would involve selecting datasets with different characteristics, such as different numbers of modalities, different sample sizes, and different types of longitudinal trajectories. The authors should also provide a detailed analysis of the computational complexity of the proposed framework, including the time and memory requirements for training and inference. This analysis should consider the impact of different parameters, such as the number of base predictors, the size of the LSTM network, and the length of the input sequences. Furthermore, the authors should discuss the limitations of the proposed approach, such as its sensitivity to hyperparameter tuning and its potential for overfitting. They should also suggest potential directions for future research, such as exploring different architectures for the base predictors or developing more sophisticated methods for feature selection and integration.

The authors should provide a more detailed analysis of the identified features, including their biological relevance and their relationship to the underlying disease progression. This analysis should go beyond simply identifying the most predictive features and should aim to understand what these features represent in terms of the underlying biological processes. For example, the authors could investigate whether the identified features are related to specific brain regions or cognitive functions. They could also explore the temporal dynamics of these features and how they change over time. This analysis could involve using techniques from computational neuroscience or bioinformatics to interpret the identified features. The authors should also discuss the limitations of the feature interpretation, such as the potential for spurious correlations and the difficulty of interpreting complex, high-dimensional data.

Finally, the authors should consider the impact of missing data on the performance of the proposed framework. In longitudinal studies, it is common to have missing data due to various reasons, such as participant dropout or technical issues. The authors should investigate how the proposed framework handles missing data and whether it is robust to different missingness patterns. They should also consider developing methods for imputing missing data or for handling missing data directly within the framework. This would make the proposed framework more practical and applicable to real-world datasets. The authors should also discuss the potential impact of missing data on the interpretation of the identified features and the generalizability of the results.

### Questions

How does the proposed framework compare to other state-of-the-art methods for multimodal data classification, particularly those designed for longitudinal data?
What are the limitations of the proposed approach, and what are the potential directions for future research?
How does the framework handle missing data, and what is its robustness to different missingness patterns?
Can the identified features be interpreted in terms of their biological relevance?

### Rating

3

### Confidence

3

**********
