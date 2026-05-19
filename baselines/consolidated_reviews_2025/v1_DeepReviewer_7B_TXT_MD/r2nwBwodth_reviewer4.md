### Summary

This paper presents a self-supervised learning (SSL) algorithm for time-series data called Prediction of Functionals from Masked Latents (PFML). PFML is designed to avoid representation collapse, where the model outputs a constant, input-invariant feature representation. The algorithm operates by predicting statistical functionals of the input signal corresponding to masked embeddings, given a sequence of unmasked embeddings. The authors demonstrate the effectiveness of PFML through experiments on three different data modalities: infant posture and movement classification from multi-sensor IMU data, emotion recognition from speech data, and sleep stage classification from EEG data. The results show that PFML is superior to a conceptually similar SSL method, MAE, and is competitive against the current state-of-the-art data modality agnostic SSL method, data2vec.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-organized and clearly written, making it easy to follow and understand.
2. The proposed method is straightforward and conceptually simple, making it accessible for practical applications.
3. The authors provide a comprehensive evaluation of PFML across three different data modalities and multiple downstream tasks, demonstrating its versatility and effectiveness.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed comparison of PFML with other SSL methods, particularly in terms of computational efficiency and scalability. It would be beneficial to include a more thorough analysis of the computational cost and memory requirements of PFML compared to existing methods, such as MAE and data2vec, especially when dealing with large datasets or high-dimensional time series. This analysis should consider both training and inference time, as well as memory usage during pre-training.
2. While the paper claims that PFML avoids representation collapse, it does not provide a rigorous theoretical analysis or empirical evidence to support this claim. It would be helpful to include a more in-depth discussion of the theoretical underpinnings of PFML and how it differs from methods that suffer from representation collapse. Specifically, the paper should explore the properties of the learned representations and how they prevent the model from collapsing to a trivial solution. Furthermore, the empirical evidence should include a more diverse set of experiments, including those that specifically test the robustness of the learned representations to different types of noise and perturbations.
3. The paper does not discuss the limitations of PFML or potential failure cases. It would be valuable to include a discussion of the scenarios where PFML might not perform well, such as time series with very high variability or those with complex, non-stationary patterns. The paper should also discuss the sensitivity of PFML to hyperparameter choices and provide guidelines for selecting appropriate values for different types of time series data. This discussion should include an analysis of how the choice of functionals affects the performance of the model.

### Suggestions

To strengthen the paper, the authors should provide a more detailed analysis of the computational cost and memory requirements of PFML. This should include a comparison with other SSL methods like MAE and data2vec, specifically focusing on training and inference time, as well as memory usage during pre-training. The analysis should consider different dataset sizes and time series lengths to demonstrate the scalability of PFML. For example, the authors could present a table showing the training time per epoch, inference time per sample, and memory usage for different batch sizes and sequence lengths. This would provide a clearer picture of the practical implications of using PFML compared to other methods. Furthermore, the authors should explore the impact of different model architectures on the computational cost and memory requirements of PFML. This would help readers understand the trade-offs between model complexity and computational efficiency.

To address the lack of theoretical analysis, the authors should provide a more in-depth discussion of the theoretical underpinnings of PFML and how it avoids representation collapse. This should include an analysis of the properties of the learned representations and how they differ from those obtained by methods prone to collapse. For example, the authors could analyze the variance of the learned embeddings during pre-training and show that it remains non-zero, unlike what might be observed in methods that suffer from collapse. Additionally, the authors should include a more diverse set of experiments to test the robustness of the learned representations to different types of noise and perturbations. This could involve adding Gaussian noise to the input data or introducing adversarial perturbations to the embeddings. Such experiments would provide a more comprehensive understanding of the method's ability to learn meaningful representations that are not trivial or invariant to input variations. The authors should also consider visualizing the learned representations to gain insights into their structure and properties.

Finally, the authors should include a more detailed discussion of the limitations of PFML and potential failure cases. This should include an analysis of the scenarios where PFML might not perform well, such as time series with very high variability or those with complex, non-stationary patterns. For example, the authors could investigate the performance of PFML on time series with abrupt changes or sudden spikes, which might challenge the model's ability to learn stable representations. The authors should also discuss the sensitivity of PFML to hyperparameter choices and provide guidelines for selecting appropriate values for different types of time series data. This discussion should include an analysis of how the choice of functionals affects the performance of the model. For instance, the authors could investigate the impact of using different statistical functionals or combinations of functionals on the quality of the learned representations. This would provide a more complete understanding of the method's strengths and weaknesses and help guide its application to new datasets.

### Questions

1. How does PFML compare to other SSL methods in terms of computational efficiency and scalability, especially when dealing with large datasets or high-dimensional time series?
2. Can you provide a more detailed theoretical analysis or empirical evidence to support the claim that PFML avoids representation collapse?
3. What are the limitations of PFML, and in what scenarios might it not perform well? How sensitive is PFML to hyperparameter choices?

### Rating

5

### Confidence

3

**********
