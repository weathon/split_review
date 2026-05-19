### Summary

This paper proposes a novel method for improving out-of-distribution (OOD) detection in normalizing flow models by addressing the bias that leads to higher likelihoods for low-complexity OOD samples. The authors introduce a synthetic outlier generation technique during training to guide the model to assign lower likelihoods to OOD data and propose a specialized training objective using the softplus function for numerical stability. Extensive experiments on image and text datasets demonstrate that this approach significantly enhances OOD detection accuracy, achieving results comparable to models trained with real outliers.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel approach to bias correction in normalizing flows by generating synthetic outliers, which is an innovative solution to the OOD detection problem.
2. The use of the softplus function in the training objective is well-justified and effectively addresses numerical stability issues.
3. The experiments are comprehensive, covering both image and text data, and show significant improvements in OOD detection performance.
4. The method achieves performance comparable to models using real outliers, which highlights its practical utility and potential for real-world applications.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion of the limitations of the synthetic outlier generation method, particularly in cases where the OOD data is highly complex or multimodal. The current approach may not adequately capture the diversity of real-world OOD samples, potentially leading to suboptimal performance when faced with OOD data that deviates significantly from the synthetic outliers. For instance, if the OOD data contains novel patterns or structures not present in the training data or the generated outliers, the model's ability to detect these samples might be compromised.

2. The experiments primarily focus on image and text data; additional validation on other data types, such as time series or audio, would strengthen the generalizability claims. The current evaluation does not explore the method's performance on datasets with different characteristics, such as sequential data or data with high dimensionality and complex dependencies. This limits the understanding of the method's applicability across various domains and data modalities.

3. The complexity of the proposed method, especially the dual likelihood objective, may make it challenging to implement and tune in practice. The dual likelihood objective introduces additional hyperparameters and computational overhead, which could complicate the training process and require careful tuning to achieve optimal performance. The paper lacks a detailed analysis of the sensitivity of the method to these hyperparameters and the computational cost associated with the dual objective.

### Suggestions

To address the limitations of the synthetic outlier generation, the authors should explore methods that can generate more diverse and representative outliers. This could involve incorporating techniques such as adversarial training or generative models to create outliers that better capture the potential variations in real-world OOD data. For example, instead of simply generating outliers by perturbing in-distribution samples, the authors could train a separate generative model to produce OOD samples that are semantically different from the in-distribution data. This would allow the model to learn a more robust representation of the OOD space and improve its detection capabilities. Furthermore, the authors should investigate the impact of different outlier generation strategies on the final OOD detection performance and provide guidelines for selecting appropriate strategies based on the characteristics of the data.

To strengthen the generalizability claims, the authors should conduct experiments on a wider range of data types, including time series and audio data. This would involve adapting the proposed method to handle the specific characteristics of these data modalities, such as temporal dependencies in time series data or spectral features in audio data. For instance, the authors could explore the use of recurrent neural networks or convolutional neural networks to process time series and audio data, respectively, and integrate these architectures with the normalizing flow model. Additionally, the authors should evaluate the method's performance on datasets with varying levels of complexity and dimensionality to assess its robustness and scalability. This would provide a more comprehensive understanding of the method's applicability across different domains and data types.

To mitigate the complexity of the dual likelihood objective, the authors should investigate alternative training strategies that can simplify the optimization process. This could involve exploring techniques such as curriculum learning or adaptive weighting of the likelihood terms to stabilize the training and reduce the sensitivity to hyperparameters. Furthermore, the authors should provide a detailed analysis of the computational cost associated with the dual objective and explore methods to reduce the computational overhead. This could involve techniques such as model compression or efficient implementation of the likelihood calculations. The authors should also provide clear guidelines for tuning the hyperparameters of the dual objective to achieve optimal performance, including a sensitivity analysis of the impact of each hyperparameter on the final OOD detection performance.

### Questions

1. How does the synthetic outlier generation method perform when the OOD data is highly complex or multimodal, and are there any strategies to improve its robustness in such cases?
2. Could the authors provide more insights into the computational overhead introduced by the dual likelihood objective and any potential strategies to mitigate this?
3. How sensitive is the method to the choice of hyperparameters, particularly those related to the synthetic outlier generation and the softplus function?

### Rating

6

### Confidence

3

**********
