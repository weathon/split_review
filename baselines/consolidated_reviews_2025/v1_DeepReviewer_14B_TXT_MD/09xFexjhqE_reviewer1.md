### Summary

This paper proposes AutoLoRa to address the issue of unstable optimization directions in Robust Fine-Tuning (RFT) for pre-trained models. The method leverages LoRa as an auxiliary branch to disentangle the optimization paths for natural and adversarial objectives, enhancing parameter efficiency and reducing the need for hyperparameter tuning. AutoLoRa demonstrates state-of-the-art adversarial robustness across various downstream tasks, providing a practical solution for improving model resilience.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-structured, with clear explanations of AutoLoRa’s components and optimization strategies, making it accessible for readers.
2. The experimental design is thorough, covering multiple datasets and model architectures, which supports the generalizability of the findings.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks an in-depth theoretical analysis of why the LoRa branch effectively mitigates the issue of divergent optimization directions. Specifically, while the authors propose that the LoRa branch addresses the gradient divergence between natural and adversarial objectives, there is no formal analysis or proof to support this claim. The paper would benefit from a more rigorous exploration of the underlying mechanisms, such as an analysis of the gradient space and how the LoRa branch alters the optimization landscape. Without this, the effectiveness of the approach remains somewhat empirical and lacks a strong theoretical foundation.
2. The comparison between the proposed method and existing methods may not be entirely fair, as AutoLoRa introduces additional parameters through the LoRa branch. While the authors claim parameter efficiency, the LoRa branch still introduces new parameters that are not present in the baseline models. This difference in model capacity could contribute to the observed performance gains, making it difficult to isolate the impact of the proposed optimization strategy. A more rigorous comparison would involve controlling for the number of parameters or providing an ablation study that quantifies the contribution of the LoRa branch.
3. The paper does not provide sufficient evidence to demonstrate that the low similarity in gradient directions is the primary cause of poor robustness in existing methods. While the authors present a correlation between gradient similarity and robust accuracy, this does not establish a causal relationship. It is possible that other factors, such as the specific optimization algorithm or the choice of hyperparameters, also contribute to the observed robustness. The paper needs to provide more compelling evidence that the gradient divergence is the main bottleneck in achieving robustness.

### Suggestions

To strengthen the theoretical foundation of the paper, the authors should consider including a more detailed analysis of the gradient space. This could involve visualizing the gradient directions for both the natural and adversarial objectives, with and without the LoRa branch. Techniques such as principal component analysis (PCA) could be used to identify the dominant directions in the gradient space and quantify the degree of divergence. Furthermore, the authors could explore the use of tools from optimization theory, such as Lyapunov functions or convergence analysis, to provide a more rigorous understanding of how the LoRa branch affects the optimization process. This would help to move beyond empirical observations and provide a more solid theoretical basis for the proposed method. The analysis should also investigate the impact of the LoRa branch on the loss landscape, examining whether it leads to a smoother or more stable optimization surface.

To address the concern about fair comparisons, the authors should conduct a more thorough ablation study that controls for the number of parameters. This could involve comparing AutoLoRa with baseline methods that have a similar number of parameters, either by adding parameter-efficient modules to the baselines or by reducing the size of the LoRa branch. Additionally, the authors should provide a more detailed analysis of the training dynamics, such as the convergence rate and the sensitivity to hyperparameters. This would help to isolate the impact of the LoRa branch and determine whether the observed performance gains are solely due to the increased model capacity or the proposed optimization strategy. It would also be beneficial to compare the performance of AutoLoRa with and without the LoRa branch, while keeping the number of parameters constant, to isolate the effect of the proposed optimization strategy.

Finally, to establish a causal link between gradient similarity and robustness, the authors should conduct experiments that directly manipulate the gradient directions. For example, they could explore techniques for explicitly aligning the gradient directions during training, such as using gradient projection or regularization methods. If these techniques lead to improved robustness, it would provide stronger evidence that the gradient divergence is indeed the primary cause of poor robustness in existing methods. Furthermore, the authors should investigate whether the observed correlation between gradient similarity and robustness holds across different datasets and model architectures. This would help to determine the generalizability of their findings and provide a more comprehensive understanding of the relationship between gradient similarity and adversarial robustness.

### Questions

1. Could the authors provide a theoretical explanation for why the LoRa branch specifically addresses the issue of divergent optimization directions?
2. Have the authors considered comparing AutoLoRa with baseline methods that have similar parameter counts to ensure a fair evaluation?
3. Could the authors provide more evidence to support the claim that low gradient similarity is the primary cause of poor robustness in existing methods?

### Rating

3

### Confidence

4

**********
