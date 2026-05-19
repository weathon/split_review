### Summary

This paper proposes a gradient regularization-based cross-prompt attack method to improve the transferability of adversarial attacks on visual language models (VLMs) across different prompts. The authors identify the issue of non-stationarity during adversarial example generation and address it by reducing the variance of back-propagated gradients in the attention and MLP components of the model. Experiments on models such as Flamingo, BLIP-2, LLaVA, and InstructBLIP demonstrate the effectiveness of the proposed method.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper introduces a gradient regularization method that enhances the transferability of adversarial examples across different prompts, which is a novel contribution to the field of adversarial attacks on VLMs.
2. The authors provide extensive experimental results on multiple state-of-the-art VLMs, demonstrating the effectiveness of their proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the computational complexity and scalability of the proposed method, especially when applied to larger models and datasets.
2. The paper could benefit from a more comprehensive discussion of the potential ethical implications of adversarial attacks on VLMs, particularly in real-world applications.
3. The paper could provide more insights into the limitations of the proposed method and potential directions for future research.
4. The paper does not provide sufficient evidence to support the claim that the proposed method can effectively alleviate overfitting issues in the deep Transformer blocks of visual and textual features.

### Suggestions

The paper should include a more rigorous analysis of the computational demands of the proposed gradient regularization method. Specifically, the authors should provide a breakdown of the time and memory complexity of their approach, considering the number of parameters in the VLM, the size of the input data, and the number of iterations required for convergence. This analysis should also compare the computational cost of the proposed method with existing adversarial attack techniques, highlighting any trade-offs between performance and computational efficiency. Furthermore, the authors should discuss the scalability of their method to larger models and datasets, providing empirical evidence of its performance on models with varying numbers of parameters and datasets of different sizes. This would help to establish the practical applicability of the proposed method in real-world scenarios.

To address the ethical concerns, the paper should include a more in-depth discussion of the potential misuse of adversarial attacks on VLMs. This discussion should consider the possible negative consequences of these attacks, such as the generation of misleading or harmful content, and the potential for these attacks to be used in malicious ways. The authors should also discuss the potential for these attacks to be used to evade detection by security systems, and the implications of this for the security of VLM-based applications. Furthermore, the paper should discuss the potential for these attacks to be used to manipulate the behavior of VLMs, and the ethical implications of this. The authors should also consider the potential for these attacks to be used to discriminate against certain groups of people, and the ethical implications of this. Finally, the paper should discuss the potential for these attacks to be used to undermine trust in VLM-based systems, and the ethical implications of this.

Finally, the paper should provide a more detailed analysis of the limitations of the proposed method. This analysis should consider the potential for the method to fail in certain scenarios, such as when the adversarial examples are not transferable across different prompts, or when the method is applied to models with different architectures. The authors should also discuss the potential for the method to be vulnerable to defenses, such as adversarial training, and the implications of this for the robustness of the method. Furthermore, the paper should discuss the potential for the method to be used to generate adversarial examples that are not perceptible to humans, and the ethical implications of this. The authors should also consider the potential for the method to be used to generate adversarial examples that are not effective in real-world scenarios, and the implications of this for the practical applicability of the method. The paper should also provide more insights into the potential directions for future research, such as exploring alternative regularization techniques, or investigating the use of the proposed method in other domains.

### Questions

1. Can the authors provide more insights into the potential defenses against the proposed attack method?
2. How does the performance of the proposed method vary across different types of visual and textual data?
3. Can the authors discuss the potential for extending their method to other types of multimodal models beyond VLMs?

### Rating

5

### Confidence

3

**********
