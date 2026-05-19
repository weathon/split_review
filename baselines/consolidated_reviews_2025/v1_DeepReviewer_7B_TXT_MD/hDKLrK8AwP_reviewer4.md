### Summary

This paper proposes a new method to generate readable SVG code. The authors first propose three desiderata for readable SVG code, and then introduce three metrics to evaluate the readability of SVG code. Differentiable objectives are designed to optimize SVG generation models to produce more readable SVG code. Experiments are conducted to demonstrate the effectiveness of the proposed method.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed metrics and objectives are reasonable and well-motivated.
3. Experiments are conducted to demonstrate the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The novelty of the proposed method is limited. The proposed method is a combination of existing techniques, including VAE, differentiable proxy loss, and existing SVG generation methods. The core idea of using a VAE to generate SVGs, while effective, is not new, and the application of differentiable losses to guide the generation process is also a common approach in generative modeling. The specific combination of these techniques, while potentially effective, does not represent a significant conceptual leap. The paper does not sufficiently articulate how the specific combination and application of these techniques leads to a novel approach beyond existing methods.
2. The proposed metrics are not well-motivated. The authors claim that the proposed metrics are based on "desiderata" for readable SVG code, but the connection between these desiderata and the specific mathematical formulations of the metrics is not clearly established. For example, the "Structural Proximity Index" (SPI) is based on the assumption that elements should be generated in the correct order, but this assumption is not rigorously justified. The metrics also lack a clear connection to actual human readability, making it difficult to assess their practical relevance. The paper needs to provide a more detailed explanation of how each metric is derived from the desiderata and how it relates to human perception of readability.

### Suggestions

The paper would benefit from a more thorough discussion of the novelty of the proposed method. The authors should clearly articulate the specific contributions of their approach beyond the combination of existing techniques. This could involve highlighting unique aspects of their method, such as specific architectural choices, loss function designs, or optimization strategies that differentiate it from prior work. For example, if the method introduces a novel way of integrating differentiable losses with the VAE framework, or a unique approach to SVG generation, this should be explicitly stated and justified. Furthermore, the authors should provide a more detailed analysis of the limitations of existing methods and how their approach addresses these limitations in a novel way. This would help to establish the significance of their contribution and justify the need for their proposed method.

To address the lack of motivation for the proposed metrics, the authors should provide a more rigorous justification for each metric. This should include a clear explanation of how each metric is derived from the desiderata for readable SVG code and how it relates to human perception of readability. For example, the authors should explain why the Structural Proximity Index (SPI) is a good measure of logical structure and how it captures the desired properties of readable SVG code. They should also provide empirical evidence to support the validity of each metric, such as correlations with human ratings of readability. Furthermore, the authors should discuss the limitations of each metric and how they might be improved in future work. This would help to establish the practical relevance of the metrics and provide a more solid foundation for their use in evaluating SVG code.

Finally, the paper should include a more detailed analysis of the experimental results. The authors should provide a more thorough comparison of their method with existing approaches, including a discussion of the strengths and weaknesses of each method. They should also provide a more detailed analysis of the impact of different parameters and settings on the performance of their method. This would help to establish the robustness and generalizability of their approach. Furthermore, the authors should discuss the limitations of their experimental setup and how these limitations might affect the results. This would help to provide a more balanced and comprehensive evaluation of their method.

### Questions

1. What is the motivation for proposing the metrics in Section 2.2.1 and 2.2.2?
2. What is the motivation for proposing the losses in Section 3.2.1, 3.2.2, and 3.2.3?
3. What is the performance of the proposed method on real-world images?

### Rating

6

### Confidence

3

**********
