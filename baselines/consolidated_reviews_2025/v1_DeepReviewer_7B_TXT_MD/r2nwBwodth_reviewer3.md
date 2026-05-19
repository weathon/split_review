### Summary

This paper proposes a new self-supervised learning (SSL) method for time series data called Prediction of Functionals from Masked Latents (PFML). The method aims to avoid the problem of representation collapse, where the model outputs a constant input-invariant feature representation. PFML operates by predicting statistical functionals of the input signal corresponding to masked embeddings, given a sequence of unmasked embeddings. The authors demonstrate the effectiveness of PFML through experiments on three different data modalities: infant posture and movement classification from multi-sensor IMU data, emotion recognition from speech data, and sleep stage classification from EEG data. The results show that PFML is superior to a conceptually similar SSL method, MAE, and is competitive against the current state-of-the-art data modality agnostic SSL method, data2vec.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

- The paper is well-organized and easy to follow.
- The proposed method is straightforward and conceptually simple, making it accessible for practical applications.
- The authors provide a comprehensive evaluation of PFML across three different data modalities and multiple downstream tasks, demonstrating its versatility and effectiveness.

### Weaknesses

#### Some Related Works

[1] Self-supervised contrastive representation learning for time series forecasting.
[2] Self-supervised contrastive learning for time series via time-warping augmentations.
[3] Time-llm: Time series forecasting by aligning time series with language models.
[4] Time-llm++: Harnessing the power of large language models for time series forecasting.
[5] Time-llm+: A unified framework for time series analysis with large language models.
[6] Time-llm+++: A unified framework for time series analysis with large language models.

#### comment

 - The paper lacks a detailed comparison of PFML with other SSL methods, particularly in terms of computational efficiency and scalability. It would be beneficial to include a more thorough analysis of the computational cost and memory requirements of PFML compared to existing methods, such as MAE and data2vec, especially when dealing with large datasets or high-dimensional time series. This analysis should consider both training and inference time, as well as memory usage during pre-training.
- While the paper claims that PFML avoids representation collapse, it does not provide a rigorous theoretical analysis or empirical evidence to support this claim. It would be helpful to include a more in-depth discussion of the theoretical underpinnings of PFML and how it differs from methods that suffer from representation collapse. Specifically, the paper should explore the properties of the learned representations and how they prevent the model from collapsing to a trivial solution. Furthermore, the empirical evidence should include a more diverse set of experiments, including those that specifically test the robustness of the learned representations to different types of noise and perturbations.
- The paper does not discuss the limitations of PFML or potential failure cases. It would be valuable to include a discussion of the scenarios where PFML might not perform well, such as time series with very high variability or those with complex, non-stationary patterns. The paper should also discuss the sensitivity of PFML to hyperparameter choices and provide guidelines for selecting appropriate values for different types of time series data. This discussion should include an analysis of how the choice of functionals affects the performance of the model.

### Suggestions

The paper would benefit from a more thorough analysis of the computational aspects of PFML. Specifically, the authors should provide a detailed breakdown of the time and memory requirements for both training and inference, comparing PFML against established methods like MAE and data2vec. This analysis should not only consider the theoretical complexity but also include empirical measurements on the datasets used in the paper. For instance, reporting the training time per epoch and the memory footprint during both training and inference would provide a clearer picture of the practical implications of using PFML. Furthermore, it would be beneficial to explore the scalability of PFML by evaluating its performance on larger datasets or with longer time series. This could involve experiments with synthetic datasets that vary in size and complexity, allowing for a more systematic assessment of the method's scalability. Such an analysis would help readers understand the trade-offs between performance and computational cost when choosing between different SSL methods for time series data.

To strengthen the claim that PFML avoids representation collapse, the authors should provide a more rigorous theoretical analysis of the method's behavior. This could involve examining the properties of the learned representations and demonstrating how they differ from those obtained by methods prone to collapse. For example, the authors could analyze the variance of the learned embeddings during pre-training and show that it remains non-zero, unlike what might be observed in methods that suffer from collapse. Additionally, the empirical evidence should be expanded to include a more diverse set of experiments that specifically test the robustness of the learned representations to different types of noise and perturbations. This could involve adding Gaussian noise to the input data or introducing adversarial perturbations to the embeddings. Such experiments would provide a more comprehensive understanding of the method's ability to learn meaningful representations that are not trivial or invariant to input variations. The authors should also consider visualizing the learned representations to gain insights into their structure and properties.

Finally, the paper should include a more detailed discussion of the limitations of PFML and potential failure cases. This should include an analysis of the scenarios where PFML might not perform well, such as time series with very high variability or those with complex, non-stationary patterns. For example, the authors could investigate the performance of PFML on time series with abrupt changes or sudden spikes, which might challenge the model's ability to learn stable representations. Furthermore, the sensitivity of PFML to hyperparameter choices should be explored, and guidelines for selecting appropriate values for different types of time series data should be provided. This discussion should also include an analysis of how the choice of functionals affects the performance of the model. For instance, the authors could investigate the impact of using different statistical functionals or combinations of functionals on the quality of the learned representations. This would provide a more complete understanding of the method's strengths and weaknesses and help guide its application to new datasets.

### Questions

- How does PFML compare to other SSL methods in terms of computational efficiency and scalability, especially when dealing with large datasets or high-dimensional time series?
- Can you provide a more detailed theoretical analysis or empirical evidence to support the claim that PFML avoids representation collapse?
- What are the limitations of PFML, and in what scenarios might it not perform well? How sensitive is PFML to hyperparameter choices?

### Rating

5

### Confidence

3

**********
