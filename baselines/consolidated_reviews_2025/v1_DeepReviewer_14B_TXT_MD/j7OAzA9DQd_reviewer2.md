### Summary

This paper proposes a novel framework called Longitudinal Ensemble Integration (LEI) for sequential classification using longitudinal multimodal data. The authors evaluate LEI's performance on the early detection of dementia using data from the TADPOLE challenge. LEI outperforms existing approaches by using intermediate base predictions from individual data modalities. The design of LEI also enables the identification of important features for dementia-related diagnoses.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper addresses a crucial problem in the field of sequential classification with multimodal data, which has significant implications for various application areas, particularly in biomedicine.
2. The proposed LEI framework is novel and extends the capabilities of existing methods to handle longitudinal multimodal data effectively. The use of intermediate base predictions and the integration of modality-specific information are innovative aspects of the framework.

### Weaknesses

#### Some Related Works


#### comment

1. The authors only use one dataset, which is not sufficient to validate the effectiveness of the proposed method. The TADPOLE challenge dataset, while comprehensive, may have specific biases or characteristics that could lead to overfitting or an overestimation of the model's generalizability. The lack of evaluation on other datasets limits the confidence in the robustness of the LEI framework.
2. The authors only compare their method with LSTM and PPAD, which is not enough. There are many other methods for processing longitudinal and multimodal data that should be compared, such as GRU, temporal convolutional networks, and attention-based mechanisms. The absence of these comparisons makes it difficult to assess the relative strengths and weaknesses of the proposed LEI framework.
3. The authors should provide a more detailed explanation of the proposed method, including the specific implementation details of the base predictors and the integration mechanism. The description of the base predictors is vague, lacking information on the specific algorithms used, their hyperparameter settings, and how they are trained. The integration mechanism also needs more clarification, particularly regarding the choice of the LSTM stacker and its configuration.

### Suggestions

To address the limitation of using a single dataset, the authors should evaluate the LEI framework on additional datasets that exhibit different characteristics, such as varying sample sizes, modalities, and temporal resolutions. For example, datasets from other biomedical domains, such as electronic health records or wearable sensor data, could be used to assess the generalizability of the proposed method. Furthermore, the authors should perform a more rigorous analysis of the TADPOLE dataset itself, investigating potential biases and limitations that could affect the results. This could involve examining the distribution of data across different time points and patient groups, as well as assessing the impact of missing data patterns. Such analysis would provide a more comprehensive understanding of the model's performance and its limitations.

To strengthen the comparative analysis, the authors should include a broader range of baseline methods that are commonly used for longitudinal and multimodal data processing. Specifically, they should compare the LEI framework with methods such as GRU, temporal convolutional networks (TCNs), and attention-based mechanisms. These methods represent different approaches to modeling temporal dependencies and could provide valuable insights into the relative performance of the proposed framework. Moreover, the authors should consider comparing against methods that explicitly handle multimodal data, such as those based on tensor factorization or graph neural networks. The comparison should not only focus on overall performance metrics but also on computational efficiency, parameter sensitivity, and interpretability. A detailed analysis of these aspects would provide a more comprehensive understanding of the strengths and weaknesses of the LEI framework.

To improve the clarity and reproducibility of the proposed method, the authors should provide a more detailed explanation of the base predictors and the integration mechanism. This should include a description of the specific algorithms used for the base predictors, their hyperparameter settings, and the training procedure. The authors should also clarify the choice of the LSTM stacker and its configuration, including the number of layers, the hidden size, and the activation functions. Furthermore, the authors should provide a detailed explanation of how the intermediate base predictions are integrated and how the final prediction is made. This could involve providing pseudocode or a detailed algorithm description. The authors should also discuss the computational complexity of the proposed method and its scalability to larger datasets.

### Questions

1. How does the proposed LEI framework perform on other datasets besides TADPOLE?
2. How does the proposed LEI framework compare with other methods for processing longitudinal and multimodal data, such as GRU, temporal convolutional networks, and attention-based mechanisms?
3. Can the authors provide more details on the implementation of the base predictors and the integration mechanism in the LEI framework?

### Rating

3

### Confidence

4

**********
