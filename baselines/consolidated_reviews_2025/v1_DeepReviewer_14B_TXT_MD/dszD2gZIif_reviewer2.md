### Summary

This paper presents Swin4TS, a Swin Transformer-based model for long-term time series forecasting. The authors propose two variants of Swin4TS: channel-dependent (CD) and channel-independent (CI). Swin4TS/CD captures correlations in both channel and time dimensions, while Swin4TS/CI processes channels independently for improved efficiency. The model leverages window-based attention and hierarchical representation to handle long sequences and achieve linear computational complexity. The authors evaluate Swin4TS on 8 benchmark datasets and achieve state-of-the-art performance.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The Swin4TS model effectively leverages the strengths of the Swin Transformer architecture, particularly window-based attention and hierarchical representation, for time series forecasting. This allows the model to handle long sequences efficiently while capturing both local and global dependencies.
2. The proposed CI and CD strategies provide flexibility in modeling multivariate time series data. The CI strategy offers high training efficiency for large datasets, while the CD strategy captures complex inter-channel correlations. This adaptability makes Swin4TS suitable for various time series forecasting tasks and datasets.

### Weaknesses

#### Some Related Works


#### comment

1. The paper primarily focuses on long-term time series forecasting (LTSF) and does not explore the applicability of Swin4TS to other time series tasks such as anomaly detection, classification, and imputation. This limits the scope of the proposed model and its potential impact on the broader field of time series analysis. Specifically, the lack of evaluation on tasks like anomaly detection, where the model's ability to identify deviations from normal patterns is crucial, or imputation, where the model's capacity to fill in missing data points is tested, leaves a gap in understanding the model's generalizability. The absence of classification experiments also limits the assessment of the model's feature extraction capabilities for categorical prediction.
2. The authors acknowledge that the performance of Swin4TS/CD degrades on datasets with hundreds of channels, but they do not provide a detailed analysis or potential solutions to address this issue. This raises concerns about the scalability and robustness of the CD strategy for high-dimensional multivariate time series data. The paper lacks a thorough investigation into the reasons behind this performance drop, such as potential overfitting due to the increased number of parameters or the difficulty in capturing complex inter-channel dependencies with the current architecture. Furthermore, the absence of experiments with datasets having varying numbers of channels makes it difficult to pinpoint the exact threshold where the CD strategy starts to falter.
3. The paper primarily compares Swin4TS with Transformer-based and non-Transformer-based baselines. It would be beneficial to include comparisons with other CV models that have been adapted for time series analysis, such as CNN-based models or RNN-based models. This would provide a more comprehensive evaluation of Swin4TS's performance and its advantages over existing approaches. The lack of comparison with established time-series specific models, such as those utilizing temporal convolutions or recurrent mechanisms, makes it difficult to assess the true novelty and effectiveness of the proposed approach in the context of time series analysis.

### Suggestions

To strengthen the paper, the authors should extend the evaluation of Swin4TS to include anomaly detection, classification, and imputation tasks. For anomaly detection, the model could be trained on normal time series data and then used to identify anomalous patterns by measuring the reconstruction error or the likelihood of the observed sequences. For classification, the model could be adapted to extract relevant features from time series data and then fed into a classification layer to predict categorical labels. For imputation, the model could be trained to predict missing values in time series data by leveraging its understanding of temporal dependencies. These additional experiments would provide a more comprehensive understanding of the model's capabilities and limitations beyond long-term forecasting. Furthermore, it would be beneficial to explore different loss functions and training strategies tailored to each specific task.

To address the performance degradation of Swin4TS/CD on high-dimensional datasets, the authors should conduct a more detailed analysis of the model's behavior with varying numbers of channels. This could involve experiments with synthetic datasets where the number of channels can be controlled, allowing for a systematic investigation of the model's scalability. The authors should also explore potential solutions, such as incorporating channel-wise attention mechanisms or using dimensionality reduction techniques before feeding the data into the model. Additionally, regularization techniques, such as dropout or weight decay, could be explored to mitigate potential overfitting issues. A thorough analysis of the computational complexity of the CD strategy with respect to the number of channels would also be valuable.

Finally, the authors should include comparisons with other CV models that have been adapted for time series analysis, such as Temporal Convolutional Networks (TCNs) and various RNN-based architectures. This would provide a more comprehensive evaluation of Swin4TS's performance and its advantages over existing approaches. The comparison should not only focus on forecasting accuracy but also on computational efficiency and model complexity. Furthermore, the authors should consider including a discussion of the limitations of the proposed approach and potential directions for future research, such as exploring different attention mechanisms or incorporating external knowledge into the model.

### Questions

1. How does Swin4TS compare to other state-of-the-art models in terms of interpretability? Can the attention maps or other visualization techniques provide insights into the model's decision-making process?
2. How does Swin4TS handle missing values or noisy data in the time series? Are there any preprocessing steps or data augmentation techniques used to improve the model's robustness?
3. How does Swin4TS perform on datasets with varying degrees of channel dependence? Are there any guidelines for choosing between Swin4TS/CD and Swin4TS/CI based on the characteristics of the dataset?
4. What are the computational requirements for training and deploying Swin4TS? How does the training time and memory usage scale with the length of the time series and the number of channels?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
