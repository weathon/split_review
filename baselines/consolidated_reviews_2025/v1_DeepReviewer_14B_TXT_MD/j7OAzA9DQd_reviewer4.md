### Summary

The authors propose a method for sequential classification of longitudinal data. The method is based on ensemble integration (EI) of predictions from multiple modalities. The authors propose a longitudinal version of EI, where the ensemble integration is performed by a LSTM. The authors evaluate their method on a dataset from the Alzheimer's Disease Neuroimaging Initiative (ADNI), where they consider the task of predicting the diagnosis of a patient at the next visit.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

The paper is generally well written and easy to follow. The authors propose a longitudinal version of ensemble integration, which is an interesting idea.

### Weaknesses

#### Some Related Works


#### comment

1. The authors do not discuss the related work in detail. In particular, the authors do not compare their method to other methods for longitudinal multimodal data. The authors should discuss and compare their method to other methods, such as those mentioned in the introduction. Specifically, a more thorough comparison with methods that explicitly model temporal dependencies within each modality, rather than just ensembling final predictions, is needed. The current discussion lacks a detailed analysis of how the proposed method handles multimodal data compared to existing approaches that might use attention mechanisms or other fusion techniques.
2. The authors do not compare their method to other methods in the experiments. The authors should compare their method to other methods for longitudinal multimodal data. The experimental section is limited by the lack of comparison to established longitudinal multimodal classification techniques. The absence of a comparison to methods that jointly model temporal and multimodal aspects makes it difficult to assess the true contribution of the proposed approach.
3. The authors do not provide code for their method, which makes it difficult to reproduce their results. The lack of publicly available code hinders the reproducibility of the results and makes it difficult for other researchers to build upon this work. This is a significant drawback for a method that aims to contribute to the field.
4. The authors do not provide a detailed description of their method. In particular, the authors do not describe the ensemble integration (EI) method in detail. The description of the EI method is too high-level, lacking crucial details about the specific base predictors used, their training procedure, and how their outputs are combined. This lack of detail makes it difficult to understand the inner workings of the proposed method and to assess its potential limitations.

### Suggestions

The authors should significantly expand the related work section to include a more detailed discussion of existing methods for longitudinal multimodal data analysis. This should include a comparison of the proposed method with techniques that explicitly model temporal dependencies within each modality, such as recurrent neural networks or temporal convolutional networks, and methods that use attention mechanisms for multimodal fusion. The discussion should also address how the proposed method handles potential issues such as missing data or varying sampling rates across modalities, and how it compares to other methods in terms of computational complexity and interpretability. A more thorough literature review would help to position the proposed method within the broader context of longitudinal multimodal data analysis and highlight its unique contributions.

In the experimental section, the authors should include a comparison with established longitudinal multimodal classification techniques. This should include a selection of state-of-the-art methods that are relevant to the specific task and dataset used in the paper. The comparison should not only focus on overall performance metrics but also on other aspects such as the ability to handle missing data, the interpretability of the results, and the computational efficiency of the methods. The authors should also provide a detailed analysis of the results, including a discussion of the strengths and weaknesses of the proposed method compared to the other methods. This would provide a more comprehensive evaluation of the proposed method and help to assess its true contribution to the field.

The authors should provide a detailed description of their method, including the specific base predictors used, their training procedure, and how their outputs are combined. This should include a clear explanation of the EI method, with details about the specific algorithms used for base prediction and how the LSTM is used for integration. The authors should also provide a detailed description of the hyperparameter settings used for the experiments, and how these settings were chosen. The code for the method should be made publicly available to ensure reproducibility and to allow other researchers to build upon this work. This would significantly improve the quality and impact of the paper.

### Questions

1. How does your method compare to other methods for longitudinal multimodal data?
2. Can you provide code for your method?
3. Can you provide a more detailed description of your method?

### Rating

3

### Confidence

4

**********
