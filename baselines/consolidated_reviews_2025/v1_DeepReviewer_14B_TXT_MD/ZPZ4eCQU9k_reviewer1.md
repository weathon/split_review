### Summary

The paper presents xLSTM-Mixer, a model for multivariate time series forecasting that combines xLSTM blocks with a mixing architecture that operates across temporal sequences and variate dimensions. The model begins with a simple linear forecast, which is then refined through complex interactions modeled by xLSTM blocks. The authors claim that xLSTM-Mixer achieves superior long-term forecasting performance compared to recent state-of-the-art methods.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

- The proposed architecture is novel, combining the strengths of xLSTM blocks with a mixing approach that allows for complex interactions between time steps and variates.
- The model achieves superior long-term forecasting performance on several benchmark datasets, which is a significant achievement.
- The paper includes a thorough ablation study that provides insights into the contribution of each component of the model.

### Weaknesses

#### Some Related Works


#### comment

 - While the paper demonstrates strong empirical results, it lacks a thorough theoretical analysis of why the proposed architecture works well. Specifically, the paper does not delve into the mathematical properties of the xLSTM-Mixer architecture that enable it to capture long-range dependencies in time series data. A more rigorous analysis, perhaps involving spectral analysis or information-theoretic measures, would be beneficial to understand the model's behavior.
- The model is complex and may be challenging to implement and train, especially for users without extensive experience in deep learning. The paper does not provide sufficient detail on the practical aspects of training the model, such as the sensitivity to hyperparameter choices and the computational resources required. This lack of practical guidance could hinder the adoption of the model by the broader research community.
- The paper does not discuss the potential limitations of the model in terms of its applicability to different types of time series data. For instance, the performance of the model on time series with high levels of noise or non-stationarity is not explored. Furthermore, the paper does not address the model's robustness to outliers or missing data, which are common in real-world time series datasets.

### Suggestions

To strengthen the theoretical foundation of the paper, the authors should consider including a more in-depth analysis of the xLSTM-Mixer architecture. This could involve examining the spectral properties of the mixing layers and how they interact with the xLSTM blocks to capture different frequency components in the time series data. Furthermore, an analysis of the information flow within the model, perhaps using information-theoretic measures, could provide insights into how the model learns to capture long-range dependencies. Such analysis would not only enhance the theoretical understanding of the model but also provide a basis for further improvements and generalizations.

To improve the practical usability of the model, the authors should provide more detailed guidance on the training process. This should include a sensitivity analysis of the model's performance with respect to different hyperparameter settings, such as the learning rate, batch size, and the number of layers. The authors should also provide recommendations for the computational resources required to train the model on different sizes of datasets. Additionally, the paper could include a discussion of techniques for mitigating overfitting, such as regularization and early stopping, and how these techniques can be applied to the xLSTM-Mixer model. Providing a well-documented implementation of the model would also greatly enhance its accessibility.

To address the limitations of the model, the authors should conduct a more comprehensive evaluation of its performance on a wider range of time series datasets. This should include datasets with different characteristics, such as high levels of noise, non-stationarity, and outliers. The paper should also explore the model's robustness to missing data and discuss techniques for handling missing values. Furthermore, the authors should investigate the model's performance on time series with different sampling rates and discuss any necessary adaptations. This more thorough evaluation would provide a better understanding of the model's applicability and limitations.

### Questions

- Can the authors provide more insights into the theoretical foundations of the proposed architecture?
- How does the model perform in terms of computational efficiency compared to other models, especially for very long time series?
- What are the limitations of the model when dealing with time series data that have missing values or are highly irregular?

### Rating

6

### Confidence

3

**********
