### Summary

This paper studies the variable subset forecasting problem, where the forecasting model is trained on complete time series while testing on time series with only a subset of variables available. The authors propose a Shift-Resilient Diffusive Imputation (SRDI) framework to address distribution shifts caused by inter-series and intra-series shifts. The framework integrates divide-and-conquer strategies with the denoising process, decomposing the input time series into invariant and variant patterns. A meta-learning paradigm is introduced to handle intra-series shifts by treating time windows as tasks. The authors conduct experiments on four datasets, demonstrating that SRDI outperforms state-of-the-art methods in handling distribution shifts.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper addresses a practical and challenging problem in time series forecasting, where only a subset of variables is available during testing. This scenario is common in real-world applications, such as sensor failures or data collection issues.
2. The authors propose a novel approach that combines divide-and-conquer strategies with diffusion models to handle distribution shifts. The use of invariant and variant patterns is an interesting idea that could potentially be applied to other time series analysis tasks.
3. The paper includes extensive experiments on four datasets, demonstrating the effectiveness of SRDI compared to state-of-the-art methods.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a clear and concise introduction to the problem of variable subset forecasting (VSF). The authors should provide a more detailed explanation of the problem setting, including the types of time series data, the nature of the variables, and the specific challenges associated with VSF. For example, are the variables independent or correlated? What are the typical characteristics of the missing data patterns? A more thorough discussion of these aspects would help readers better understand the significance of the problem and the proposed solution.
2. The motivation for using diffusion models for imputation in the context of VSF is not well-justified. While diffusion models have shown promise in other imputation tasks, the authors need to explain why they are particularly suitable for handling distribution shifts in VSF. What specific properties of diffusion models make them advantageous compared to other imputation techniques? For instance, do they better capture complex dependencies or are they more robust to noisy data? The paper should provide a more detailed analysis of the theoretical and empirical benefits of using diffusion models for this specific problem.
3. The paper does not provide a clear explanation of how the proposed framework addresses intra-series shifts. The authors mention that a meta-learning paradigm is used, but the details of this approach are vague. What specific meta-learning algorithm is used? How are the time windows defined and treated as tasks? What is the loss function used for training? A more detailed description of the meta-learning framework, including the mathematical formulation and implementation details, is needed to fully understand how intra-series shifts are handled.
4. The paper lacks a detailed discussion of the limitations of the proposed approach. What are the potential drawbacks or scenarios where SRDI might not perform well? For example, how does the performance of SRDI vary with different types of distribution shifts? What are the computational costs associated with the proposed method? A thorough discussion of these limitations would provide a more balanced and realistic assessment of the proposed approach.

### Suggestions

The paper would significantly benefit from a more detailed explanation of the variable subset forecasting (VSF) problem. The authors should elaborate on the characteristics of the time series data they are working with, including whether the variables are independent or correlated. They should also provide concrete examples of real-world scenarios where VSF is encountered, such as sensor failures in a smart grid or data loss in a sensor network. Furthermore, a more in-depth discussion of the specific challenges associated with VSF, such as the impact of missing data on model performance and the need for robust imputation techniques, would help to contextualize the proposed approach. This would allow readers to better understand the significance of the problem and the potential impact of the proposed solution. The authors should also clarify the nature of the missing data patterns, such as whether they are random or follow a specific distribution, as this can significantly affect the choice of imputation method.

To strengthen the justification for using diffusion models, the authors should provide a more detailed analysis of their properties that make them suitable for handling distribution shifts in VSF. They should discuss how diffusion models capture complex dependencies and why they are more robust to noisy data compared to other imputation techniques. For example, they could explain how the denoising process in diffusion models allows them to learn the underlying data distribution more effectively, especially when dealing with incomplete data. They should also provide a theoretical analysis of the convergence properties of the diffusion model in the context of VSF. Furthermore, a comparison with other generative models, such as variational autoencoders, would help to highlight the advantages of diffusion models for this specific problem. The authors should also discuss the computational cost of training and using diffusion models, and how this compares to other imputation techniques.

The paper needs a more detailed explanation of the meta-learning framework used to address intra-series shifts. The authors should provide a clear description of the specific meta-learning algorithm used, including the mathematical formulation and implementation details. They should explain how the time windows are defined and treated as tasks, and what the loss function is used for training. A detailed description of the meta-learning framework would allow readers to better understand how intra-series shifts are handled. The authors should also provide a discussion of the limitations of the meta-learning approach, such as the potential for overfitting to specific time windows or the computational cost of training the meta-learning model. Furthermore, they should provide a more detailed analysis of the performance of SRDI under different types of distribution shifts, including both inter-series and intra-series shifts. This would help to demonstrate the robustness of the proposed approach.

### Questions

1. Could you provide a more detailed explanation of the variable subset forecasting (VSF) problem, including the types of time series data, the nature of the variables, and the specific challenges associated with VSF?
2. What is the motivation for using diffusion models for imputation in the context of VSF? How do diffusion models specifically address the challenges of distribution shifts in VSF compared to other imputation techniques?
3. How does the proposed framework address intra-series shifts? Could you provide a more detailed explanation of the meta-learning paradigm used, including the specific meta-learning algorithm, the definition of time windows as tasks, and the loss function used for training?
4. What are the limitations of the proposed approach? How does the performance of SRDI vary with different types of distribution shifts? What are the computational costs associated with the proposed method?

### Rating

5

### Confidence

3

**********
