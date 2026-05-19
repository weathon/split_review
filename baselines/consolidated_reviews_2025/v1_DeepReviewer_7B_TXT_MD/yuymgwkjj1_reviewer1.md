### Summary

This paper addresses the challenge of Out-of-Distribution (OOD) detection, particularly focusing on the bias in normalizing flow models. These models tend to assign higher likelihoods to OOD samples with low complexity, which reduces their effectiveness in OOD detection. To tackle this issue, the authors propose a novel method that incorporates synthetic outliers during training and employs a specialized training objective that leverages the softplus function for OOD data. This approach enhances the model's ability to distinguish between in-distribution (ID) and OOD data. The method is validated through extensive experiments on benchmark and high-dimensional real-world datasets, demonstrating superior OOD detection performance, achieving results comparable to models trained with limited real outliers. Additionally, the approach increases the Lipschitz constant, supporting the hypothesis that a higher Lipschitz constant enhances model stability and OOD detection performance.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

- The paper is well-organized and clearly presented, making it easy to follow and understand.
- The paper addresses an important problem in OOD detection, which is critical for ensuring the reliability and robustness of deep learning models in real-world applications.

### Weaknesses

#### Some Related Works

[1] Serra et al. Out-of-distribution detection with score-based generative models. ICLR 2021.

#### comment

 - The paper does not provide a clear and detailed explanation of the motivation behind the proposed method. While the authors mention the bias in normalizing flow models, they do not sufficiently explain why this bias occurs or how their method effectively addresses it. A more thorough discussion of the underlying mechanisms and the specific advantages of using synthetic outliers and the softplus function would strengthen the paper's contribution.
- The paper lacks a comprehensive comparison with existing OOD detection methods, particularly those based on normalizing flows. While the authors compare their method to some baselines, a more detailed analysis of how their approach differs from and improves upon existing techniques would be beneficial. This should include a discussion of the specific limitations of prior methods that the proposed approach overcomes.
- The experimental evaluation, while extensive, could be further strengthened by including a wider range of datasets and OOD scenarios. The current evaluation primarily focuses on image and text data, and it would be valuable to assess the method's performance on other data modalities, such as time series or tabular data. Additionally, the paper could benefit from a more in-depth analysis of the method's performance under different types of OOD data, including those with varying degrees of complexity and distributional shifts.
- The paper does not provide a detailed analysis of the computational cost associated with the proposed method. While the authors mention the use of synthetic outliers, they do not discuss the computational overhead introduced by this approach. A comparison of the training and inference times with existing methods would be valuable for assessing the practical applicability of the proposed method.

### Suggestions

The paper would significantly benefit from a more detailed explanation of the motivation behind the proposed method. The authors should elaborate on the specific mechanisms within normalizing flow models that lead to the bias towards assigning higher likelihoods to low-complexity OOD samples. This could involve a discussion of the model's internal representations and how they might be influenced by the training data distribution. Furthermore, the authors should provide a more in-depth explanation of how the proposed synthetic outliers and softplus-based training objective specifically address this bias. For example, they could discuss how the synthetic outliers are designed to challenge the model's assumptions and how the softplus function contributes to a smoother and more effective training process. A more thorough theoretical justification for the proposed approach would greatly enhance the paper's contribution.

To strengthen the paper's comparison with existing methods, the authors should include a more comprehensive analysis of the differences between their approach and other OOD detection techniques, particularly those based on normalizing flows. This should include a discussion of the specific limitations of prior methods that the proposed approach overcomes. For example, the authors could compare their method to other likelihood-based OOD detection techniques, highlighting the advantages of their approach in terms of robustness and performance. Additionally, the authors should provide a more detailed analysis of the computational cost associated with their method, including a comparison of training and inference times with existing methods. This would provide a more complete picture of the practical applicability of the proposed approach.

Finally, the experimental evaluation could be further strengthened by including a wider range of datasets and OOD scenarios. The authors should consider evaluating their method on other data modalities, such as time series or tabular data, to assess its generalizability. Additionally, the paper could benefit from a more in-depth analysis of the method's performance under different types of OOD data, including those with varying degrees of complexity and distributional shifts. This would provide a more comprehensive understanding of the method's strengths and limitations. Furthermore, the authors should provide a more detailed analysis of the impact of different hyperparameters on the performance of their method, including the number of synthetic outliers and the parameters of the softplus function. This would provide valuable insights into the practical implementation of the proposed approach.

### Questions

- How does the proposed method compare to other OOD detection techniques, particularly those based on normalizing flows?
- What is the computational cost of the proposed method compared to existing approaches?
- How does the method perform on datasets other than images and text, such as time series or tabular data?
- What is the impact of different hyperparameters on the performance of the method?

### Rating

5

### Confidence

3

**********
