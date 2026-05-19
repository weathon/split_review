### Summary

This paper introduces a frequency domain augmentation technique for time series forecasting. The proposed method consists of two components: frequency masking and frequency mixing. The authors demonstrate the effectiveness of their approach through experiments on various datasets and models.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is clearly written and easy to follow.
2. The authors conducted extensive experiments to validate their method.

### Weaknesses

#### Some Related Works

[1] A K-Shaped Model for Time Series Forecasting with Non-stationary Memory Augmentation
[2] Time Series Forecasting with Informer

#### comment

1. The proposed method is not specifically designed for time series forecasting. It could also be applied to other tasks like classification and anomaly detection. Therefore, the authors should consider broadening the title and abstract to reflect the general applicability of their method.

2. The paper lacks a comparison with other data augmentation techniques specifically designed for time series forecasting, such as [1].

3. The experimental results do not include confidence intervals, making it difficult to determine whether the proposed method significantly outperforms the baselines. Additionally, the authors should consider including more recent models, such as [2], to provide a more comprehensive evaluation.

4. The authors should compare their method with traditional time series data augmentation techniques in the experiments.

### Suggestions

The authors should clarify the scope of their proposed method. While the current focus is on time series forecasting, the techniques of frequency masking and mixing could potentially be applied to other time series tasks. If the authors intend to keep the broader scope, the title and abstract should be revised to reflect this. If the focus remains on forecasting, the introduction should clearly articulate why these frequency domain augmentations are particularly well-suited for this task compared to other potential applications. Furthermore, a more detailed discussion of the theoretical underpinnings of why these augmentations work well for forecasting would be beneficial. For example, do these augmentations preserve the autocorrelation structure of the time series, or do they introduce beneficial variations that improve generalization?

To strengthen the experimental evaluation, the authors should include comparisons with other data augmentation techniques specifically designed for time series forecasting. This would provide a more comprehensive understanding of the advantages and disadvantages of the proposed method. The comparison should not only focus on performance metrics but also on computational cost and the sensitivity of the method to hyperparameter settings. Additionally, the authors should include more recent state-of-the-art time series forecasting models in their experiments to ensure that the results are relevant and up-to-date. The inclusion of confidence intervals is crucial for assessing the statistical significance of the results. Without confidence intervals, it is difficult to determine whether the observed improvements are due to the proposed method or simply due to random chance. The authors should also consider reporting additional metrics beyond MSE, such as MAE or MAPE, to provide a more complete picture of the performance.

Finally, the authors should provide a more detailed analysis of the effect of the mask rate hyperparameter on the performance of the proposed method. A systematic study of how different mask rates affect the performance of different models and datasets would be valuable. This analysis should include a discussion of the trade-offs between the mask rate and the performance of the model. The authors should also investigate whether the optimal mask rate varies across different datasets and models. This would provide practical guidance for users of the proposed method. Furthermore, the authors should consider visualizing the augmented time series in the frequency domain to provide a better understanding of the effect of the proposed augmentations.

### Questions

1. What is the effect of the mask rate hyperparameter? Could the authors conduct an ablation study to investigate its impact on performance?

2. Could the authors provide a more detailed explanation of how the proposed method differs from [3]?

[3] Frequency-domain Data Augmentation for Partially-Observed Time Series

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
