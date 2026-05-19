### Summary

This paper proposes a novel adversarial image attack framework, AdvI2I, designed to manipulate image-to-image (I2I) diffusion models to generate NSFW content. The framework extracts NSFW concept vectors from adversarial prompts and uses them to guide the generation of NSFW content in images. The authors also introduce an adaptive version of the framework, AdvI2I-Adaptive, which is designed to evade safety mechanisms and resist defenses. The paper evaluates the performance of AdvI2I and AdvI2I-Adaptive on two diffusion models, InstructPix2Pix and SDv1.5-Inpainting, and demonstrates their effectiveness in generating NSFW content.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow, with clear explanations of the proposed framework and its components.
2. The authors provide a comprehensive evaluation of the proposed framework on two diffusion models, InstructPix2Pix and SDv1.5-Inpainting, and demonstrate its effectiveness in generating NSFW content.
3. The paper introduces an adaptive version of the framework, AdvI2I-Adaptive, which is designed to evade safety mechanisms and resist defenses. This is a valuable contribution to the field of adversarial attacks on diffusion models.

### Weaknesses

#### Some Related Works

[1] Adversarial Examples Are Not Bugs, They Are Features

#### comment

1. The paper does not adequately address the potential for adversarial attacks to be detected by machine learning models. While the authors focus on generating NSFW content, they do not discuss how their approach might be detected by safety filters or other machine learning-based defenses. This is a significant oversight, as adversarial attacks are often designed to evade detection, and the paper should discuss how its approach might be detected by machine learning models. Specifically, the paper lacks discussion on the potential for feature-based detection methods that could identify adversarial perturbations, even if they are not directly targeting NSFW content. The authors should consider how their adversarial perturbations might align with features that safety classifiers are trained on, even if those features are not explicitly related to NSFW content.
2. The paper does not provide a detailed analysis of the computational cost of the proposed framework. While the authors mention that the framework is efficient, they do not provide any quantitative data on the time and resources required to generate adversarial examples. This is a significant limitation, as the computational cost of adversarial attacks can be a limiting factor in their practical application. The paper should include a detailed analysis of the computational cost of the proposed framework, including the time required for adversarial example generation, the memory requirements, and the energy consumption. This analysis should be performed on different hardware configurations to provide a comprehensive understanding of the computational cost.
3. The paper does not explore the potential for the proposed framework to be used for malicious purposes. While the authors acknowledge that adversarial attacks can be used for malicious purposes, they do not discuss the potential risks associated with their approach. This is a significant oversight, as the paper should discuss the potential for their framework to be used to generate harmful content, and how these risks can be mitigated. The paper should discuss the potential for their adversarial attacks to be used to generate content that could be used for malicious purposes, such as generating child pornography or other forms of hate speech. The authors should also discuss the potential for their attacks to be used to manipulate public opinion or to create propaganda.

### Suggestions

The paper should include a more thorough discussion of the potential for adversarial attacks to be detected by machine learning models. Specifically, the authors should explore how their adversarial perturbations might align with features that safety classifiers are trained on, even if those features are not explicitly related to NSFW content. For example, the authors could investigate whether their adversarial perturbations are detected by feature-based detection methods that identify adversarial examples based on their similarity to known adversarial patterns. The authors should also consider how their approach might be detected by ensemble methods that combine multiple detection models. This analysis should include a discussion of the limitations of current detection methods and how the proposed adversarial attacks might be designed to evade these defenses. Furthermore, the authors should discuss the potential for adversarial attacks to be detected by human inspection, and how their approach might be designed to be more easily detectable by humans.

The paper should also include a more detailed analysis of the computational cost of the proposed framework. This analysis should include the time required for adversarial example generation, the memory requirements, and the energy consumption. The analysis should be performed on different hardware configurations to provide a comprehensive understanding of the computational cost. The authors should also discuss the potential for optimizing their framework to reduce its computational cost. For example, the authors could explore the use of more efficient optimization algorithms or the use of model compression techniques. The paper should also discuss the trade-offs between computational cost and attack effectiveness, and how these trade-offs might affect the practical application of the proposed framework. The authors should also consider the impact of their framework on the computational resources of the target system, and how this might affect the deployment of their framework in real-world scenarios.

Finally, the paper should include a more thorough discussion of the potential for adversarial attacks to be used for malicious purposes. The authors should discuss the potential for their adversarial attacks to be used to generate harmful content, and how these risks can be mitigated. The paper should also discuss the potential for their attacks to be used to manipulate public opinion or to create propaganda. The authors should also consider the ethical implications of their work and how their findings might be used to develop more robust and secure generative models. The paper should also discuss the potential for their attacks to be used to generate content that could be used for malicious purposes, such as generating child pornography or other forms of hate speech. The authors should also discuss the potential for their attacks to be used to manipulate public opinion or to create propaganda.

### Questions

1. How does the proposed framework compare to other adversarial attacks on diffusion models, particularly in terms of attack success rate, computational cost, and robustness to defenses?
2. What are the potential risks associated with the proposed framework, and how can these risks be mitigated?
3. How does the proposed framework perform on different types of images and prompts, and are there any specific scenarios where it is less effective?

### Rating

6

### Confidence

3

**********
