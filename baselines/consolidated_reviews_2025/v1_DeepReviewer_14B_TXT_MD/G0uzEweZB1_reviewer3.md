### Summary

This paper proposes a data augmentation method in the frequency domain for time series forecasting. The method includes two strategies: frequency masking and frequency mixing. The authors show that the proposed method can improve the performance of time series forecasting models, especially in scenarios with limited training data or significant distribution shifts. The paper also demonstrates that the proposed method can be applied to various state-of-the-art time series forecasting models and datasets.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The paper proposes a novel data augmentation method in the frequency domain for time series forecasting, which is a relatively unexplored area in the literature.
2. The proposed method is simple yet effective, and can be easily integrated into existing time series forecasting models.
3. The paper provides extensive experimental results on various datasets and models, demonstrating the effectiveness of the proposed method in different scenarios.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a theoretical analysis of why the proposed method works. It is unclear how manipulating the frequency components of a time series can improve the forecasting performance. Specifically, the paper lacks a discussion on how the proposed frequency masking and mixing strategies affect the spectral properties of the time series and how these changes relate to improved forecasting accuracy. A more rigorous analysis, perhaps using concepts from signal processing or time series analysis, would be beneficial.
2. The paper only considers two simple strategies for frequency domain augmentation. It would be interesting to explore other potential strategies, such as frequency shifting or frequency scaling. The current approach seems limited in its ability to capture the full range of possible frequency domain manipulations. For instance, the paper does not discuss the potential benefits of phase manipulation or more complex transformations that could be applied in the frequency domain.
3. The paper does not compare the proposed method with other data augmentation techniques for time series forecasting. It would be useful to compare the proposed method with other state-of-the-art data augmentation techniques, such as time warping or generative adversarial networks (GANs). Without such comparisons, it is difficult to assess the relative merits of the proposed method. The lack of comparison with methods that operate in the time domain makes it hard to understand the specific advantages of the frequency domain approach.
4. The paper does not provide a detailed analysis of the computational complexity of the proposed method. It would be useful to know how the computational cost of the proposed method scales with the size of the time series and the number of frequency components. The paper should include a discussion of the time and memory requirements of the proposed method, especially when applied to large datasets or long time series.

### Suggestions

The paper would benefit from a more in-depth theoretical analysis of the proposed frequency domain augmentation method. Specifically, the authors should explore how the frequency masking and mixing strategies affect the spectral characteristics of the time series. For instance, they could analyze how these operations alter the power spectral density and how these changes relate to the forecasting performance. A theoretical framework, perhaps based on concepts from signal processing or time series analysis, could provide a deeper understanding of why the proposed method works. This analysis should also consider the potential impact of these manipulations on the autocorrelation structure of the time series, which is crucial for forecasting. Furthermore, the authors should investigate the relationship between the frequency components and the underlying dynamics of the time series, providing a more solid justification for their approach. This would strengthen the paper's contribution and provide a more rigorous foundation for the proposed method.

To enhance the practical impact of the work, the authors should explore a wider range of frequency domain augmentation strategies. Beyond simple masking and mixing, they could investigate the effects of frequency shifting, scaling, and phase manipulation. These more complex transformations could potentially capture a broader range of variations in the time series data. For example, frequency shifting could simulate changes in the underlying periodic behavior of the time series, while phase manipulation could introduce more subtle variations. The authors should also consider adaptive augmentation strategies that adjust the frequency domain manipulations based on the characteristics of the time series. This could involve using techniques from signal processing to identify the most relevant frequency components and applying augmentations that are tailored to these components. Such an approach could lead to more effective data augmentation and improved forecasting performance.

Finally, the paper needs a more comprehensive experimental evaluation that includes comparisons with other state-of-the-art data augmentation techniques for time series forecasting. The authors should compare their method with techniques that operate in both the time and frequency domains, such as time warping, GANs, and variational autoencoders (VAEs). This would provide a more complete picture of the relative strengths and weaknesses of the proposed method. The experimental evaluation should also include a detailed analysis of the computational complexity of the proposed method, including the time and memory requirements for different dataset sizes and time series lengths. This analysis should consider the impact of the number of frequency components on the computational cost. Furthermore, the authors should investigate the sensitivity of the proposed method to the choice of hyperparameters, such as the masking rate and the mixing ratio. This would provide valuable insights into the practical application of the method and help users to tune the method for their specific needs.

### Questions

1. How does the proposed method compare with other data augmentation techniques for time series forecasting, such as time warping or generative adversarial networks (GANs)?
2. What is the computational complexity of the proposed method, and how does it scale with the size of the time series and the number of frequency components?
3. How does the proposed method handle time series with complex patterns or multiple frequencies? Are there any limitations to the proposed method in these scenarios?
4. Can the proposed method be extended to other time series analysis tasks, such as classification or anomaly detection?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
