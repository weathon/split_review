### Summary

This paper proposes a novel adversarial attack framework, AdvI2I, designed to manipulate image-to-image diffusion models to produce NSFW content. The framework leverages adversarial image generators to create perturbations that induce the generation of inappropriate images, even when using safety filters. The authors also introduce an adaptive version of the framework that enhances its robustness against existing defense mechanisms. The paper highlights the urgent need for stronger security measures in generative models to address the misuse of these technologies.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper introduces a new adversarial attack framework, AdvI2I, specifically designed for image-to-image diffusion models, which is a novel contribution to the field.
2. The authors conduct extensive experiments to evaluate the performance of the proposed framework and its adaptive version, AdvI2I-Adaptive, under various defense mechanisms.
3. The paper is well-structured and clearly presents the proposed methods, experimental setup, and results.

### Weaknesses

#### Some Related Works


#### comment

1. The paper primarily focuses on the technical aspects of the adversarial attack framework and does not delve deeply into the ethical implications of such attacks on image-to-image diffusion models. A more comprehensive discussion of the ethical considerations and potential misuse of the proposed framework would strengthen the paper's contribution.
2. The paper could benefit from a more detailed analysis of the limitations of the proposed framework and potential future research directions. This would provide a more balanced perspective on the contributions and suggest avenues for further exploration.
3. The paper could provide a more thorough comparison with existing adversarial attack methods for diffusion models, highlighting the unique aspects and advantages of the proposed framework. This would help to better position the contributions of the paper within the broader context of adversarial attacks on generative models.

### Suggestions

The paper would benefit from a more in-depth discussion of the ethical dimensions of adversarial attacks on image-to-image diffusion models. While the technical aspects are well-presented, the potential for misuse, such as the generation of harmful or inappropriate content, needs to be addressed more thoroughly. For instance, the authors could explore scenarios where an attacker might manipulate an image-to-image model to create NSFW content, and discuss the implications for users and society. This could include a discussion of potential mitigation strategies, such as input sanitization or output filtering, and how these might be integrated with existing defense mechanisms. Furthermore, the authors should consider the impact of their work on different user groups and the potential for bias in the generated content. A more nuanced discussion of these ethical considerations would significantly enhance the paper's contribution and relevance.

To strengthen the paper's analysis, a more detailed discussion of the limitations of the proposed AdvI2I framework is necessary. The authors should explore scenarios where the framework might fail or be less effective, such as when the input image is significantly altered or when the diffusion model is trained on a different dataset. For example, how does the framework perform when the input image contains artifacts or is of very low resolution? Additionally, the authors should discuss the computational cost of the attack and its scalability to larger datasets or more complex models. A thorough analysis of these limitations would provide a more balanced view of the framework's capabilities and suggest avenues for future research, such as exploring more robust optimization techniques or adaptive perturbation strategies. Furthermore, the authors should consider the impact of different hyperparameter settings on the attack's performance and provide guidelines for selecting appropriate values.

Finally, the paper would be significantly improved by a more comprehensive comparison with existing adversarial attack methods for diffusion models. The authors should not only compare the performance of their framework but also discuss the underlying differences in methodology and the specific advantages and disadvantages of each approach. For example, how does AdvI2I compare to other gradient-based attacks in terms of attack success rate, computational cost, and robustness to defenses? A detailed comparison should also consider the specific types of adversarial perturbations used by different methods and their impact on the generated content. This would help to better position the contributions of the paper within the broader context of adversarial attacks on generative models and highlight the unique aspects of the proposed framework. Furthermore, the authors should discuss the potential for combining their approach with other attack methods to achieve even more effective results.

### Questions

1. Could the authors elaborate on the ethical implications of the proposed adversarial attack framework for image-to-image diffusion models? How might this framework be misused, and what steps can be taken to mitigate these risks?
2. What are the limitations of the proposed AdvI2I framework, and how might these limitations be addressed in future research?
3. How does the proposed framework compare to other adversarial attack methods for diffusion models, particularly in terms of attack success rate, computational cost, and robustness to defenses?

### Rating

5

### Confidence

4

**********
