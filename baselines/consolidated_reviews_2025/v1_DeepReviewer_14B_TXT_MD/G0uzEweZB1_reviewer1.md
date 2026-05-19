### Summary

This paper proposes a frequency-domain augmentation method called FrAug, designed to address the challenge of data scarcity in time series forecasting tasks. Specifically, FrAug includes two techniques: frequency masking, which randomly sets certain frequency domain representations to zero, and frequency mixing, which combines the frequency domains of two different time series samples. By applying these techniques, the proposed method generates augmented data that helps improve the forecasting model's robustness and predictive accuracy, particularly in scenarios with limited training data or significant distribution shifts between training and test sets.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

1 poor

### Strengths

1.	The paper is well-written and easy to follow.
2.	The paper introduces FrAug, a novel data augmentation technique in the frequency domain specifically designed for time series forecasting, addressing the unique challenges of maintaining temporal relationships and semantic consistency in augmented data.
3.	The proposed method not only improves forecasting accuracy but also demonstrates effectiveness in cold-start scenarios and under distribution shifts, showing its versatility and practical value in real-world applications.

### Weaknesses

#### Some Related Works


#### comment

1.	Frequency mixing involves combining the frequency domains of two different time series samples. This operation may disrupt the temporal dependencies within the original data, potentially leading to unrealistic or inconsistent time series patterns. Specifically, the method lacks a clear mechanism to ensure that the combined frequency components maintain the original temporal relationships, which could result in augmented data that does not accurately reflect the underlying dynamics of the time series. This could be particularly problematic for time series where specific frequency components are strongly tied to particular temporal patterns.
2.	The paper primarily focuses on frequency masking and frequency mixing. It would be beneficial to explore additional frequency-domain augmentation techniques, such as frequency shifting or adding frequency-dependent noise, to further enhance the diversity of the augmented data. The current approach, while novel, may be limited in its ability to capture the full range of variations present in real-world time series data. For example, frequency shifting could introduce variations in the phase of the time series, which might be beneficial for robustness.
3.	The experimental setup in the paper lacks clarity in several areas. For example, the process for dividing the dataset into training, validation, and test sets is not described in detail. The paper should specify whether a rolling-forecast or an expanding window approach is used, and how the validation set is used for hyperparameter tuning. This lack of detail makes it difficult to reproduce the results and assess the validity of the experimental findings.
4.	The paper primarily uses the MSE metric to evaluate model performance. It would be beneficial to include additional metrics, such as MAE, RMSE, or MAPE, to provide a more comprehensive assessment of the models’ forecasting accuracy. Relying solely on MSE may not capture all aspects of forecasting performance, such as the magnitude of errors or the relative accuracy of predictions.
5.	The paper does not provide a clear explanation for why the proposed FrAug method performs poorly on the ETTm2 dataset. Further analysis is needed to understand the characteristics of this dataset that make it challenging for the proposed method. This lack of analysis limits the understanding of the method's applicability and potential limitations.
6.	The paper does not explore the application of the proposed frequency-domain augmentation method to other models. It would be beneficial to evaluate the method’s effectiveness across a wider range of models to assess its generalizability. The current evaluation is limited to a few specific models, which makes it difficult to determine whether the method's benefits are model-specific or more broadly applicable.

### Suggestions

The paper introduces a novel approach to time series augmentation in the frequency domain, which is a valuable contribution. However, several aspects of the methodology and experimental evaluation could be improved to strengthen the paper's claims and impact. First, the frequency mixing technique, while innovative, needs further justification and analysis. The paper should provide a more detailed explanation of how the mixing process preserves temporal dependencies, perhaps by visualizing the time series before and after mixing. It would also be beneficial to explore the impact of different mixing ratios and to provide a theoretical analysis of how this technique affects the spectral properties of the time series. Furthermore, the authors should consider adding a constraint to the mixing process to ensure that the augmented data remains within a realistic range, preventing the generation of potentially nonsensical time series patterns. This could involve incorporating a measure of similarity between the original and augmented time series in the frequency domain.

Second, the paper would benefit from a more comprehensive exploration of frequency-domain augmentation techniques. While frequency masking and mixing are a good start, the authors should consider incorporating other methods such as frequency shifting and frequency-dependent noise addition. Frequency shifting could be implemented by adding a random phase shift to the frequency components, which would introduce variations in the time domain without altering the amplitude spectrum. Frequency-dependent noise could be added by introducing noise that is proportional to the amplitude of the frequency components, which would simulate the effect of noise in real-world data. These additional techniques would increase the diversity of the augmented data and potentially improve the robustness of the forecasting models. The authors should also consider a systematic way to combine these different augmentation techniques, perhaps by using a weighted average or a random selection process. This would allow for a more flexible and robust augmentation strategy.

Finally, the experimental evaluation needs to be more rigorous and transparent. The paper should provide a detailed description of the data splitting process, including the specific parameters used for the rolling-forecast or expanding window approach. The authors should also justify the choice of the validation set size and explain how it is used for hyperparameter tuning. In addition to MSE, the paper should include other evaluation metrics such as MAE, RMSE, and MAPE, to provide a more comprehensive assessment of the models' forecasting accuracy. The authors should also conduct a more thorough analysis of the results on the ETTm2 dataset, exploring the reasons for the poor performance of the proposed method. This could involve visualizing the augmented data and comparing it to the original data, or analyzing the spectral properties of the augmented data. Furthermore, the authors should evaluate the proposed method on a wider range of models to assess its generalizability. This would provide a more robust assessment of the method's effectiveness and its potential for practical applications.

### Questions

1.	How does the frequency mixing ensure that the temporal dependencies within the time series data are preserved?
2.	Can the authors provide more details on the experimental setup, such as the process for dividing the dataset into training, validation, and test sets?
3.	Why does the proposed FrAug method perform poorly on the ETTm2 dataset?
4.	have you explored the application of the proposed frequency-domain augmentation method to other models?

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
