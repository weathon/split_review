### Summary

This paper proposes a new method for generating SVG code that prioritizes readability, aiming to improve the logical structure and simplicity of the generated code. The authors introduce three desiderata for readable SVG code and three metrics to evaluate its readability. They also develop differentiable objectives to guide the generation process, allowing for the creation of SVGs that are both accurate and easy to understand. Experiments demonstrate that this approach improves the readability of generated SVGs compared to existing methods.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper is well-structured and clearly written, making it easy to follow the proposed methodology and findings.
2. The authors provide a comprehensive set of experiments, including both quantitative and qualitative assessments, to validate their approach. The results show that the proposed method achieves better readability and accuracy compared to baseline models.
3. The authors present a balanced trade-off between accuracy and readability, which is a significant contribution to the field of SVG generation.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed metrics and objectives are not novel, and the paper lacks a clear explanation of how they differ from existing methods. The metrics, while tailored to SVG, appear to be adaptations of existing concepts rather than fundamentally new measures. The paper does not adequately justify why these specific adaptations are necessary or how they capture aspects of SVG readability that are not already covered by standard metrics. The objectives, while differentiable, seem to be based on common loss functions, and the paper does not provide a detailed analysis of how these objectives are specifically optimized for SVG generation, beyond standard backpropagation.
2. The paper does not provide a detailed analysis of the computational complexity of the proposed method, which is important for practical applications. The lack of analysis makes it difficult to assess the scalability of the approach, especially when dealing with complex SVGs or large datasets. The paper should include a discussion of the time and memory requirements of the differentiable objectives and the metrics, as well as a comparison to existing methods.
3. The paper does not explore the limitations of the proposed method, such as potential biases in the generated SVGs or scenarios where the method may not perform well. The paper should discuss the potential for the method to generate overly simplistic or overly complex SVGs, and how these limitations might affect the usability of the generated code. It should also address the potential for the method to be biased towards certain types of SVGs or images.
4. The paper does not provide a clear explanation of how the proposed method can be integrated into existing SVG generation pipelines, which limits its practical applicability. The paper should provide a more detailed description of how the differentiable objectives can be incorporated into existing VAE architectures, and how the metrics can be used to evaluate the generated SVGs. It should also discuss the potential challenges of integrating the method into existing pipelines, such as the need for new training data or the need for modifications to the training process.

### Suggestions

The paper would benefit from a more detailed explanation of the proposed metrics and objectives, specifically highlighting how they differ from existing methods and why these differences are necessary for SVG readability. The authors should provide a more rigorous justification for the design choices, including a discussion of the theoretical underpinnings of the metrics and objectives. For example, the paper should explain how the metrics capture the specific aspects of SVG readability that are not covered by existing metrics, and how the objectives are specifically optimized for SVG generation. The authors should also provide a more detailed analysis of the computational complexity of the proposed method, including a discussion of the time and memory requirements of the differentiable objectives and the metrics. This analysis should include a comparison to existing methods, and should discuss the scalability of the approach. Furthermore, the paper should explore the limitations of the proposed method, including potential biases in the generated SVGs and scenarios where the method may not perform well. The authors should discuss the potential for the method to generate overly simplistic or overly complex SVGs, and how these limitations might affect the usability of the generated code. The paper should also address the potential for the method to be biased towards certain types of SVGs or images. Finally, the paper should provide a more detailed explanation of how the proposed method can be integrated into existing SVG generation pipelines, including a discussion of the potential challenges of integrating the method into existing pipelines, such as the need for new training data or the need for modifications to the training process. The authors should provide a more detailed description of how the differentiable objectives can be incorporated into existing VAE architectures, and how the metrics can be used to evaluate the generated SVGs.

### Questions

1. How does the proposed method compare to existing SVG generation techniques in terms of computational efficiency and scalability?
2. Can the proposed method be extended to handle more complex SVGs or images with intricate patterns?
3. What are the potential limitations or biases of the proposed method, and how can they be addressed?

### Rating

3

### Confidence

4

**********
