### Summary

This paper introduces a novel robust fine-tuning framework, AutoLoRa, which addresses the issue of divergent gradient directions in existing robust fine-tuning methods. By disentangling the optimization of natural and adversarial objectives through a low-rank branch and employing heuristic strategies for automating learning rate and scalar schedules, AutoLoRa achieves state-of-the-art adversarial robustness without requiring manual hyperparameter tuning. The framework is validated through extensive experiments on various downstream tasks, demonstrating its effectiveness and practical utility.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-structured and clearly written, making it easy to follow and understand.
2. The authors provide a thorough analysis of the limitations of existing robust fine-tuning methods, specifically the issue of divergent gradient directions. This analysis is supported by clear visualizations and quantitative results.
3. The proposed AutoLoRa framework is technically sound and demonstrates significant improvements in adversarial robustness compared to existing methods. The use of a low-rank branch for disentangling natural and adversarial objectives is an innovative approach.
4. The paper presents comprehensive experimental results across multiple downstream tasks, demonstrating the generalizability and effectiveness of the proposed method.

### Weaknesses

#### Some Related Works

[1] Robust fine-tuning of zero-shot classifiers
[2] Robust fine-tuning of vision-language models

#### comment

1. The paper lacks a comprehensive discussion of related work, particularly in the area of robust fine-tuning (RFT). For example, the paper does not discuss the differences between the proposed method and other RFT methods, such as RF-CLIP [1] and RF-ViT [2]. A more detailed comparison with these methods would help to clarify the novelty and advantages of the proposed approach.
2. The paper does not provide a clear explanation of why the proposed method is effective. While the authors claim that the disentanglement of natural and adversarial objectives leads to improved robustness, they do not provide a theoretical analysis or empirical evidence to support this claim. A more detailed analysis of the optimization landscape and the effect of the low-rank branch on the feature space would be beneficial.
3. The paper does not provide a detailed analysis of the computational cost of the proposed method. While the authors claim that the low-rank branch is parameter-efficient, they do not provide quantitative comparisons of training time, memory usage, and inference speed with other methods. This makes it difficult to assess the practical applicability of the proposed approach.

### Suggestions

The paper would benefit significantly from a more thorough comparison with existing robust fine-tuning (RFT) methods. Specifically, the authors should provide a detailed analysis of how their approach differs from methods like RF-CLIP [1] and RF-ViT [2]. This comparison should not only focus on performance metrics but also on the underlying mechanisms and assumptions of each method. For example, it would be helpful to discuss the specific types of adversarial attacks that each method is designed to defend against, and how the proposed method's disentanglement strategy compares in terms of robustness against different attack types. Furthermore, the authors should clarify whether the proposed method is applicable to different types of pre-trained models, such as those trained on different datasets or with different architectures. A more comprehensive discussion of the limitations of the proposed method would also be beneficial, including scenarios where it might not perform well or where other methods might be more suitable. This would help to provide a more balanced and nuanced view of the proposed approach.

To strengthen the claims regarding the effectiveness of the proposed method, the authors should provide a more detailed analysis of the optimization landscape and the effect of the low-rank branch on the feature space. While the authors claim that the disentanglement of natural and adversarial objectives leads to improved robustness, they do not provide a theoretical analysis or empirical evidence to support this claim. A more detailed analysis of the optimization landscape, perhaps through visualizations of the loss surface, could help to understand how the proposed method avoids the pitfalls of divergent gradient directions. Furthermore, the authors should provide a more in-depth analysis of the role of the low-rank branch in the optimization process. For example, they could investigate how the rank of the low-rank branch affects the performance and robustness of the model. Additionally, the authors should provide a more detailed explanation of the heuristic strategies for automating the scheduling of learning rates and scalars. This explanation should include a discussion of the specific parameters that are being tuned and how they affect the performance of the model. A more rigorous analysis of the sensitivity of the model to different parameter settings would also be beneficial.

Finally, the paper should include a more detailed analysis of the computational cost of the proposed method. While the authors claim that the low-rank branch is parameter-efficient, they do not provide quantitative comparisons of training time, memory usage, and inference speed with other methods. This makes it difficult to assess the practical applicability of the proposed approach. The authors should provide a more detailed breakdown of the computational cost of each component of the proposed method, including the low-rank branch and the feature extractor. This analysis should include quantitative comparisons with other methods, such as vanilla RFT and TWINS, to demonstrate the trade-offs between performance and computational cost. Furthermore, the authors should discuss the scalability of the proposed method to larger datasets and models. This analysis should include an assessment of the memory usage and training time for larger models and datasets. This would help to provide a more complete picture of the practical applicability of the proposed approach.

### Questions

1. How does the proposed method compare to other robust fine-tuning methods in terms of performance and computational cost?
2. What is the impact of the low-rank branch on the convergence and robustness of the model?
3. How does the proposed method perform on different types of pre-trained models and datasets?

### Rating

6

### Confidence

3

**********
