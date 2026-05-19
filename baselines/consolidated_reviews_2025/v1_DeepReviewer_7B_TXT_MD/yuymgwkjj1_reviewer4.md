### Summary

This paper proposes a method to improve the bias of normalizing flows in OOD detection. The authors first identify the bias issue and then propose a method to address it. Experiments on image and text datasets show the effectiveness of the proposed method.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The paper addresses an important problem in OOD detection, which is critical for ensuring the reliability and robustness of deep learning models in real-world applications.
3. The authors provide a comprehensive evaluation of their method on both image and text datasets, demonstrating its effectiveness across different domains.

### Weaknesses

#### Some Related Works

[1] Out-of-distribution detection with score-based generative models

#### comment

1. The paper lacks a detailed explanation of the motivation behind the proposed method. While the authors mention the bias in normalizing flow models, they do not sufficiently explain why this bias occurs or how their method effectively addresses it. A more thorough discussion of the underlying mechanisms and the specific advantages of using synthetic outliers and the softplus function would strengthen the paper's contribution.
2. The paper lacks a comprehensive comparison with existing OOD detection methods, particularly those based on normalizing flows. While the authors compare their method to some baselines, a more detailed analysis of how their approach differs from and improves upon existing techniques would be beneficial. This should include a discussion of the specific limitations of prior methods that the proposed approach overcomes.
3. The experimental evaluation, while extensive, could be further strengthened by including a wider range of datasets and OOD scenarios. The current evaluation primarily focuses on image and text data, and it would be valuable to assess the method's performance on other data modalities, such as time series or tabular data. Additionally, the paper could benefit from a more in-depth analysis of the method's performance under different types of OOD data, including those with varying degrees of complexity and distributional shifts.
4. The paper does not provide a detailed analysis of the computational cost associated with the proposed method. While the authors mention the use of synthetic outliers, they do not discuss the computational overhead introduced by this approach. A comparison of the training and inference times with existing methods would be valuable for assessing the practical applicability of the proposed method.

### Suggestions

The paper would significantly benefit from a more in-depth discussion of the theoretical underpinnings of the proposed method. Specifically, the authors should elaborate on why normalizing flows tend to assign higher likelihoods to low-complexity OOD samples. This could involve a more detailed analysis of the model's internal representations and how they are influenced by the training data distribution. Furthermore, the authors should provide a more rigorous justification for the use of synthetic outliers and the softplus-based penalty. A theoretical analysis of how these components contribute to mitigating the bias would strengthen the paper's claims. For example, the authors could discuss the properties of the softplus function that make it suitable for this task, and how the synthetic outliers are designed to challenge the model's assumptions. This would provide a more solid foundation for the proposed method and make it more convincing.

To address the lack of comprehensive comparison with existing OOD detection methods, the authors should include a more detailed analysis of how their approach differs from and improves upon prior techniques, especially those based on normalizing flows. This should include a discussion of the specific limitations of existing methods that the proposed approach overcomes. For example, the authors could compare their method to other likelihood-based OOD detection techniques, highlighting the advantages of their approach in terms of robustness and performance. Furthermore, the authors should provide a more detailed analysis of the computational cost associated with their method. This should include a comparison of the training and inference times with existing methods, as well as an analysis of the memory requirements. This would provide a more complete picture of the practical applicability of the proposed method and allow for a more informed assessment of its strengths and weaknesses.

Finally, the experimental evaluation should be expanded to include a wider range of datasets and OOD scenarios. This should include datasets from other modalities, such as time series or tabular data, to assess the generalizability of the proposed method. Additionally, the authors should conduct a more in-depth analysis of the method's performance under different types of OOD data, including those with varying degrees of complexity and distributional shifts. This would provide a more comprehensive understanding of the method's strengths and limitations. Furthermore, the authors should provide a more detailed analysis of the impact of different hyperparameters on the performance of their method, including the number of synthetic outliers and the parameters of the softplus function. This would provide valuable insights into the practical implementation of the proposed approach.

### Questions

1. How does the proposed method compare to other OOD detection techniques, particularly those based on normalizing flows?
2. What is the computational cost of the proposed method compared to existing approaches?
3. How does the method perform on datasets other than images and text, such as time series or tabular data?
4. What is the impact of different hyperparameters on the performance of the method?

### Rating

5

### Confidence

3

**********
