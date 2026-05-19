### Summary

This paper introduces a novel framework for unsupervised domain adaptation in time series classification. The proposed method, LOLO, leverages both global and local features to enhance domain-invariant feature alignment. It employs a multi-scale local encoder and a fusion module to capture complex patterns in time series data. Additionally, the authors propose a new metric learning method based on Dynamic Time Warping (DTW) to improve the robustness of feature alignment across domains. The framework also incorporates adversarial learning and center alignment to further enhance the transferability of learned features. Extensive empirical results demonstrate that LOLO outperforms state-of-the-art baselines by up to 12.52% on four time series datasets.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow. The authors provide a clear and concise explanation of the proposed method, including the motivation, methodology, and experimental setup.
2. The authors conduct extensive experiments on four benchmark datasets, demonstrating the effectiveness of LOLO over state-of-the-art baselines. The results are presented in a clear and organized manner, with tables and figures that effectively illustrate the performance improvements.
3. The authors provide a detailed ablation study, which analyzes the impact of different components and loss functions on the performance of LOLO. This study helps to understand the contribution of each component to the overall performance of the framework.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational complexity of the proposed method. It would be beneficial to include a discussion of the time and memory requirements of LOLO, especially in comparison to other state-of-the-art methods. This analysis should consider the impact of different hyperparameters, such as the number of local encoders and the size of the patches.
2. The paper does not discuss the limitations of the proposed method. It would be helpful to acknowledge the potential challenges and drawbacks of LOLO, such as its sensitivity to hyperparameter settings or its performance on specific types of time series data. For example, the paper does not address how the method would perform on time series with high levels of noise or non-stationarity.
3. The paper does not provide a detailed explanation of the choice of the specific loss functions used in the framework. While the authors mention that they are based on existing loss functions, it would be helpful to provide a more detailed justification for their selection and to discuss any potential alternatives. For example, the paper does not explain why the specific combination of triplet loss, margin alignment loss, and center alignment loss was chosen over other possible combinations.

### Suggestions

The paper would benefit from a more thorough analysis of the computational complexity of the proposed LOLO framework. Specifically, the authors should provide a breakdown of the time and memory requirements for each component of the model, including the multi-scale local encoder, the patching transformer, and the fusion module. This analysis should not only consider the theoretical complexity but also provide empirical measurements on the datasets used in the experiments. Furthermore, the authors should discuss how the computational cost scales with the input sequence length, the number of local encoders, and the size of the patches. This would help readers understand the practical limitations of the method and its suitability for different applications. For example, a discussion of the impact of the number of local encoders on both performance and computational cost would be valuable. It would also be beneficial to compare the computational cost of LOLO with other state-of-the-art methods for time series classification, providing a clear picture of its efficiency relative to existing approaches.

In addition to the computational analysis, the paper should also include a more detailed discussion of the limitations of the proposed method. The authors should acknowledge potential challenges and drawbacks, such as the sensitivity of the method to hyperparameter settings and its performance on specific types of time series data. For instance, the paper should address how the method would perform on time series with high levels of noise or non-stationarity. It would be useful to include experiments that specifically test the robustness of LOLO under these conditions. Furthermore, the authors should discuss the potential impact of the choice of local encoders and the patching strategy on the overall performance of the method. A sensitivity analysis of these parameters would provide valuable insights into the method's behavior and help users choose appropriate settings for their specific applications. The authors should also discuss the potential limitations of the metric learning approach based on Dynamic Time Warping (DTW) and how it might affect the alignment of features across domains.

Finally, the paper needs a more detailed explanation of the choice of loss functions. While the authors mention that they are based on existing loss functions, a more thorough justification for their selection is needed. The authors should explain why the specific combination of triplet loss, margin alignment loss, and center alignment loss was chosen over other possible combinations. A discussion of the potential alternatives and the reasons for their exclusion would be valuable. For example, the authors could discuss the specific properties of each loss function and how they contribute to the overall performance of the framework. Furthermore, the authors should provide a more detailed explanation of how the hyperparameters of these loss functions are tuned and how they affect the training process. This would help readers understand the impact of the loss functions on the final results and provide guidance on how to use the framework effectively.

### Questions

1. How does the proposed method handle time series with high levels of noise or non-stationarity? Are there any specific strategies or modifications that can be applied to improve performance in these scenarios?
2. How does the choice of local encoders and patching strategy affect the overall performance of LOLO? Are there any guidelines or best practices for selecting these parameters?
3. How does the proposed method compare to other unsupervised domain adaptation methods for time series classification? Are there any specific advantages or disadvantages of LOLO compared to these methods?

### Rating

6

### Confidence

4

**********
