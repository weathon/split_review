### Summary

This paper introduces a novel adversarial attack method, APD, which aims to improve the transferability of adversarial examples in deep neural networks. The authors argue that existing methods for enhancing adversarial transferability often spread perturbations across the entire image, which may not be effective as these perturbations may not align with the attention regions of different models. To address this, they propose a perturbation-dropping scheme that incorporates a dropout mechanism during the optimization process. The method uses class activation maps to locate the midpoint of dropped regions, ensuring that effective perturbations are generated for target models while maintaining the attack rate for the source model. Extensive experiments on the ImageNet dataset demonstrate that APD outperforms state-of-the-art methods, achieving high attack efficiency and transferability.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper presents a novel approach to enhancing the transferability of adversarial examples, which is a significant challenge in the field of deep learning security.

2. The proposed APD method is simple yet effective, and it can be integrated with other adversarial attack methods to further improve performance.

3. The paper provides extensive experimental results on the ImageNet dataset, demonstrating the effectiveness of the proposed method in improving attack success rates in black-box settings.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed APD method relies on class activation maps (CAM) to locate the midpoint of dropped regions. However, the paper does not provide a detailed analysis of the computational overhead introduced by this approach. It is unclear how the additional step of generating CAMs impacts the overall efficiency of the attack, especially when considering the iterative nature of adversarial attacks. The paper should include a more thorough discussion of the time complexity and resource requirements associated with the CAM generation and how it scales with different image resolutions and network architectures.

2. The paper claims that the proposed method outperforms state-of-the-art methods, but it is not clear if the comparison is entirely fair. The paper should explicitly state whether the baseline methods were re-implemented with the same experimental setup, including the same surrogate model, perturbation budget, and number of iterations. Without this information, it is difficult to ascertain whether the observed performance gains are due to the proposed method or to differences in the experimental setup. Furthermore, the paper should provide a more detailed analysis of the hyperparameter sensitivity of the proposed method and the baseline methods.

3. The paper focuses on improving the transferability of adversarial examples, but it does not discuss the potential implications of this research for the security of deep neural networks. While the paper mentions that the goal is to improve the transferability of adversarial examples, it does not address the potential risks associated with more transferable attacks. The paper should include a discussion of how the proposed method could be used to evaluate the robustness of deep neural networks and how it could be used to develop more effective defense mechanisms.

### Suggestions

The paper should include a more detailed analysis of the computational cost associated with the proposed method. Specifically, the authors should provide a breakdown of the time spent on generating class activation maps (CAMs) compared to the time spent on the actual adversarial perturbation generation. This analysis should be conducted for different image resolutions and network architectures to understand how the computational overhead scales. Furthermore, the authors should compare the computational cost of their method with the computational cost of the baseline methods. This would provide a more comprehensive understanding of the trade-offs between attack performance and computational efficiency. It would also be beneficial to explore alternative methods for identifying important regions in the image that may be less computationally expensive than CAM, such as using saliency maps or gradient-based methods.

To ensure a fair comparison with state-of-the-art methods, the authors should re-implement the baseline methods using the same experimental setup as their proposed method. This includes using the same surrogate model, perturbation budget, number of iterations, and any other relevant hyperparameters. The paper should also provide a detailed analysis of the hyperparameter sensitivity of both the proposed method and the baseline methods. This analysis should include a discussion of how the choice of hyperparameters affects the attack performance and the computational cost. It is important to understand the robustness of the proposed method to different hyperparameter settings and to identify the optimal hyperparameter values for different datasets and network architectures. The authors should also consider using a standardized benchmark dataset and evaluation protocol to facilitate comparison with other methods in the literature.

Finally, the paper should include a more thorough discussion of the security implications of the proposed method. The authors should discuss how the increased transferability of adversarial examples could be used to evaluate the robustness of deep neural networks and how it could be used to develop more effective defense mechanisms. The paper should also address the potential risks associated with more transferable attacks, such as the possibility of using these attacks to compromise real-world systems. The authors should also consider the ethical implications of their research and discuss how their work could be used for both beneficial and malicious purposes. It is important to consider the broader impact of this research on the field of deep learning security and to ensure that the research is conducted in a responsible and ethical manner.

### Questions

1. How does the proposed APD method perform on other datasets besides ImageNet? Are there any specific characteristics of the ImageNet dataset that make it particularly suitable for this method?

2. Can the APD method be extended to other types of adversarial attacks, such as those targeting natural language processing models or other types of machine learning models?

3. What are the potential limitations of the proposed method? Are there any specific scenarios or conditions under which the APD method may not be effective?

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
