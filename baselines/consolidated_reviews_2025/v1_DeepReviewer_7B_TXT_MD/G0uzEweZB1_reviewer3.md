### Summary

This paper proposes FrAug, a novel frequency domain augmentation technique for time series forecasting. The authors claim that existing data augmentation methods in time series analysis are not suitable for forecasting tasks due to their disruption of fine-grained temporal relationships. To address this issue, FrAug introduces two methods: frequency masking and frequency mixing, which aim to preserve the semantic consistency of augmented data-label pairs in forecasting. The authors evaluate FrAug on eight widely-used benchmarks with several state-of-the-art forecasting models and demonstrate that FrAug can improve forecasting accuracy, especially when the training dataset is small.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a comprehensive review of existing data augmentation methods in time series analysis and forecasting.
3. The proposed FrAug is simple and easy to implement.

### Weaknesses

#### Some Related Works


#### comment

1. The authors claim that existing data augmentation methods in time series analysis are not suitable for forecasting tasks due to their disruption of fine-grained temporal relationships. However, the authors do not provide a detailed analysis of why these methods are not suitable for forecasting tasks. Specifically, the paper lacks a rigorous explanation of how methods like cropping, warping, and noise injection, which are common in time series analysis, fundamentally violate the temporal dependencies crucial for forecasting. A more in-depth discussion of the underlying assumptions of forecasting models and how these augmentation techniques disrupt those assumptions is needed.
2. The authors argue that FrAug can alleviate overfitting problems of state-of-the-art TSF models. However, the authors do not provide a detailed analysis of why FrAug can alleviate overfitting problems. It would be better if the authors could provide some theoretical analysis or empirical evidence to support this claim. For instance, how does the frequency masking and mixing specifically prevent the model from learning spurious correlations that lead to overfitting? A more detailed explanation of the mechanism by which FrAug reduces the effective capacity of the model or forces it to learn more generalizable features is necessary.
3. The authors claim that FrAug can improve forecasting accuracy, especially when the training dataset is small. However, the authors do not provide a detailed analysis of why FrAug can improve forecasting accuracy in low-data regimes. It would be better if the authors could provide some theoretical analysis or empirical evidence to support this claim. For example, how does FrAug help the model generalize better from limited data? Is it because FrAug creates more diverse training examples, or does it help the model learn more robust features? A more detailed explanation of the underlying mechanisms that lead to improved performance in low-data settings is needed.

### Suggestions

The paper would benefit from a more thorough investigation into the limitations of existing time series augmentation techniques for forecasting. While the authors correctly point out that methods like cropping, warping, and noise injection can disrupt fine-grained temporal relationships, they do not delve into the specific mechanisms through which these disruptions occur in forecasting models. For example, a detailed analysis of how these methods affect the model's ability to capture long-range dependencies or how they introduce artificial noise that hinders the learning of underlying patterns would be valuable. Furthermore, the authors should consider exploring the impact of these augmentations on the spectral properties of the time series, as many forecasting models rely on frequency-domain representations. A more rigorous analysis of these aspects would strengthen the paper's argument and provide a more solid foundation for the proposed FrAug method. Specifically, the authors could analyze the effect of these augmentations on the model's ability to capture long-range dependencies or how they introduce artificial noise that hinders the learning of underlying patterns. A more detailed explanation of the underlying assumptions of forecasting models and how these augmentation techniques disrupt those assumptions is needed.

To address the lack of clarity regarding the overfitting alleviation, the authors should provide a more detailed explanation of how frequency masking and mixing prevent the model from learning spurious correlations. One approach could be to analyze the effect of FrAug on the model's loss landscape, showing how it leads to flatter minima that are less prone to overfitting. Another approach could be to investigate the spectral properties of the augmented time series and demonstrate how FrAug forces the model to learn more robust and generalizable features. For example, the authors could show that FrAug increases the diversity of the training data in the frequency domain, which could lead to better generalization. Additionally, the authors could consider comparing FrAug with other regularization techniques, such as dropout or weight decay, to demonstrate its unique advantages in preventing overfitting. A more detailed explanation of the mechanism by which FrAug reduces the effective capacity of the model or forces it to learn more generalizable features is necessary.

Finally, the paper needs a more detailed explanation of why FrAug improves forecasting accuracy in low-data regimes. The authors should investigate whether FrAug helps the model generalize better from limited data by creating more diverse training examples or by learning more robust features. For example, the authors could analyze the feature space of the model trained with and without FrAug and show that FrAug leads to a more compact and well-separated feature space, which could explain the improved generalization performance. Furthermore, the authors could consider comparing FrAug with other data augmentation techniques that are specifically designed for low-data regimes, such as synthetic data generation or transfer learning, to demonstrate its unique advantages in this setting. A more thorough analysis of the underlying mechanisms that lead to improved performance in low-data settings is needed. Additionally, the authors should provide a more detailed analysis of the computational cost of FrAug, especially when dealing with large-scale time series datasets. It would be beneficial to discuss the trade-offs between the computational cost and the performance gains achieved by FrAug.

### Questions

Please see the weaknesses.

### Rating

5: marginally below the acceptance threshold

### Confidence

5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

**********
