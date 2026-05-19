### Summary

This paper proposes a new training method that modifies the empirical risk minimization (ERM) framework by adding two additional terms to the loss function, aiming to reduce the generalization error. The authors decompose the generalization error into three components: the expectation of conditional testing variance, the expectation of conditional training variance, and the expectation of bias between training and testing. They then approximate the generalization error using analytical proxies. By jointly minimizing the conventional training loss and the proxy for the conditional generalization error, the proposed method achieves improved performance on CIFAR100 and ImageNet compared to ERM and another baseline, DOM.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper provides a decomposition of the generalization error, offering an interesting perspective on the sources of generalization error in deep learning.

2. The proposed method demonstrates improved performance on CIFAR100 and ImageNet compared to ERM and DOM.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks details on how the hyperparameters $\lambda$ and $\beta$ in Equation (19) are chosen. The performance of the method depends on these hyperparameters, and their selection may involve expensive search costs. Specifically, the paper does not provide a clear methodology for selecting these values, such as a grid search or a more principled approach. The absence of this information makes it difficult to assess the practical applicability of the method, as the optimal hyperparameter values may vary significantly across different datasets and model architectures. Furthermore, the computational cost associated with tuning these hyperparameters is not discussed, which is a crucial factor for real-world applications.

2. The paper lacks a theoretical analysis of the relationship between the proposed loss function (Equation (19)) and the generalization error. While the authors provide an intuitive explanation for the improved performance, a more rigorous theoretical justification is needed to understand why minimizing the proposed loss function leads to better generalization. The connection between the added terms in the loss function and the three components of the generalization error decomposition is not clearly established. A theoretical analysis could provide insights into the convergence properties of the proposed method and its robustness to different datasets and model architectures.

3. The paper lacks a comparison with important baselines, such as sharpness-aware minimization (SAM). The absence of a comparison with SAM, a well-established method for improving generalization, makes it difficult to assess the relative performance of the proposed method. It is important to compare the proposed method with other state-of-the-art techniques to demonstrate its advantages and limitations. The lack of such a comparison limits the impact of the paper and raises questions about the novelty and effectiveness of the proposed approach.

### Suggestions

The paper would significantly benefit from a more detailed explanation of the hyperparameter selection process for $\lambda$ and $\beta$. The authors should provide a clear methodology for choosing these values, such as a grid search or a more principled approach. It is important to discuss the sensitivity of the method to different hyperparameter values and provide guidelines for selecting appropriate values for new datasets and model architectures. Furthermore, the computational cost associated with tuning these hyperparameters should be discussed. For example, the authors could explore techniques like Bayesian optimization or random search to efficiently find optimal hyperparameter values. This would make the method more practical and accessible to a wider audience.

To strengthen the theoretical foundation of the paper, the authors should provide a more rigorous analysis of the relationship between the proposed loss function and the generalization error. This analysis should include a discussion of the convergence properties of the proposed method and its robustness to different datasets and model architectures. The authors should also provide a more detailed explanation of how the added terms in the loss function relate to the three components of the generalization error decomposition. A theoretical analysis could provide insights into why minimizing the proposed loss function leads to better generalization. This would enhance the credibility of the proposed method and provide a deeper understanding of its underlying mechanisms.

Finally, the paper should include a comparison with important baselines, such as sharpness-aware minimization (SAM). This comparison would allow the authors to demonstrate the advantages and limitations of the proposed method relative to other state-of-the-art techniques. The authors should also consider comparing their method with other regularization techniques that aim to improve generalization. This would provide a more comprehensive evaluation of the proposed method and help to establish its contribution to the field. The experimental section should be expanded to include these comparisons, and the results should be discussed in detail.

### Questions

1. How are the hyperparameters $\lambda$ and $\beta$ in Equation (19) chosen? Does the method's performance heavily depend on these hyperparameters?

2. Could the authors provide a theoretical analysis of the relationship between the proposed loss function (Equation (19)) and the generalization error?

3. Could the authors compare the proposed method with important baselines, such as sharpness-aware minimization (SAM)?

### Rating

3

### Confidence

4

**********
