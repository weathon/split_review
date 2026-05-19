### Summary

The paper introduces a new self-supervised learning (SSL) method called Prediction of Functionals from Masked Latents (PFML) for time-series data. PFML predicts statistical functionals of masked embeddings, which helps avoid representation collapse and is computationally simpler than previous methods. The authors demonstrate its effectiveness across three different data modalities, showing superior or competitive performance compared to existing SSL methods.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper is well-organized and clearly written, making it easy to follow and understand.
2. The proposed PFML method is straightforward and conceptually simple, making it accessible for practical applications.
3. The authors provide a comprehensive evaluation of PFML across three different data modalities and multiple downstream tasks, demonstrating its versatility and effectiveness.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed comparison of PFML with other SSL methods, particularly in terms of computational efficiency and scalability. It would be beneficial to include a more thorough analysis of the computational cost and memory requirements of PFML compared to existing methods, such as MAE and data2vec, especially when dealing with large datasets or high-dimensional time series. This analysis should consider both training and inference time, as well as memory usage during pre-training.
2. While the paper claims that PFML avoids representation collapse, it does not provide a rigorous theoretical analysis or empirical evidence to support this claim. It would be helpful to include a more in-depth discussion of the theoretical underpinnings of PFML and how it differs from methods that suffer from representation collapse. Specifically, the paper should explore the properties of the learned representations and how they prevent the model from collapsing to a trivial solution. Furthermore, the empirical evidence should include a more diverse set of experiments, including those that specifically test the robustness of the learned representations to different types of noise and perturbations.
3. The paper does not discuss the limitations of PFML or potential failure cases. It would be valuable to include a discussion of the scenarios where PFML might not perform well, such as time series with very high variability or those with complex, non-stationary patterns. The paper should also discuss the sensitivity of PFML to hyperparameter choices and provide guidelines for selecting appropriate values for different types of time series data. This discussion should include an analysis of how the choice of functionals affects the performance of the model.

### Suggestions

To strengthen the paper, the authors should provide a more detailed analysis of the computational efficiency and scalability of PFML. This should include a breakdown of the time and memory requirements for both training and inference, as well as a comparison with other SSL methods like MAE and data2vec. The analysis should consider different dataset sizes and time series lengths to demonstrate the scalability of PFML. Furthermore, the authors should investigate the impact of different hyperparameter settings on the computational cost and performance of PFML. This analysis should be presented in a clear and concise manner, possibly using tables and graphs to illustrate the results. This would allow readers to better understand the practical implications of using PFML in different scenarios.

In addition to the computational analysis, the authors should provide a more rigorous theoretical analysis of why PFML avoids representation collapse. This should include a discussion of the properties of the learned representations and how they differ from those learned by methods that suffer from representation collapse. The authors should also provide empirical evidence to support their claims, including experiments that specifically test the robustness of the learned representations to different types of noise and perturbations. This could include experiments with different types of noise, such as Gaussian noise, salt-and-pepper noise, and adversarial perturbations. The authors should also investigate how the choice of functionals affects the robustness of the learned representations. This theoretical and empirical analysis would provide a more solid foundation for the claims made in the paper.

Finally, the authors should include a more detailed discussion of the limitations of PFML and potential failure cases. This should include an analysis of the scenarios where PFML might not perform well, such as time series with very high variability or those with complex, non-stationary patterns. The authors should also discuss the sensitivity of PFML to hyperparameter choices and provide guidelines for selecting appropriate values for different types of time series data. This discussion should include an analysis of how the choice of functionals affects the performance of the model. Furthermore, the authors should explore the performance of PFML on a wider range of time series datasets, including those with different characteristics, to demonstrate the generalizability of the method. This would provide a more comprehensive understanding of the strengths and weaknesses of PFML.

### Questions

1. How does PFML compare to other SSL methods in terms of computational efficiency and scalability, especially when dealing with large datasets or high-dimensional time series?
2. Can you provide a more detailed theoretical analysis or empirical evidence to support the claim that PFML avoids representation collapse?
3. What are the limitations of PFML, and in what scenarios might it not perform well? How sensitive is PFML to hyperparameter choices?

### Rating

5

### Confidence

3

**********
