### Summary

This paper introduces a unified framework for interpreting and controlling large language models (LLMs) by mapping intermediate representations to human-interpretable features and back. The authors propose an encoder-decoder architecture that can be applied to various interpretability methods, such as sparse autoencoders, logit lens, and probing. The paper introduces two new evaluation metrics: intervention success rate and coherence-intervention tradeoff. The authors evaluate the methods across different models and intervention topics, finding that simpler methods like logit lens and tuned lens generally outperform sparse autoencoders in intervention capability, while non-interpretability-based approaches like prompting perform best overall.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

- The paper is well-written and easy to follow.
- The proposed encoder-decoder framework is flexible and can incorporate various interpretability methods, providing a unified perspective on these methods.
- The study evaluates multiple interpretability methods across different models and intervention topics, providing a comprehensive comparison.

### Weaknesses

#### Some Related Works


#### comment

 - The novelty of the encoder-decoder framework is limited. The framework primarily focuses on mapping intermediate representations to human-interpretable features and back, which is a common approach in interpretability research. The paper does not introduce a novel mapping technique or a new way of representing the latent space, which makes the contribution incremental.
- The paper lacks a thorough comparison with existing interpretability methods and frameworks. While the authors compare their framework with sparse autoencoders, logit lens, tuned lens, and probing, they do not discuss how their approach differs from other established methods like concept activation vectors (CAVs) [1] or other encoder-decoder based interpretability methods [2]. The absence of such comparisons makes it difficult to assess the unique value of the proposed framework.
- The evaluation metrics, intervention success rate and coherence-intervention tradeoff, are not sufficiently justified. The paper does not provide a strong theoretical basis for these metrics, and it is unclear how they relate to the actual utility of the interpretability methods. The intervention success rate, which measures whether increasing the activation of a feature increases the feature in the model's output, is not a strong measure of causal fidelity. The coherence-intervention tradeoff, which measures the model's coherence after intervention, is also not well-defined and lacks a clear connection to the interpretability goals.
- The paper does not provide a detailed analysis of the limitations of the proposed framework and metrics. The authors do not discuss potential biases, assumptions, or edge cases that may arise in practical applications. For example, the paper does not address how the framework would perform on models with different architectures or on tasks with more complex outputs. The lack of such analysis limits the generalizability of the findings.

[1] https://arxiv.org/abs/2406.13611
[2] https://arxiv.org/abs/2407.02077

### Suggestions

The paper would benefit significantly from a more thorough comparison with existing interpretability methods. Specifically, the authors should discuss how their encoder-decoder framework differs from concept activation vectors (CAVs) [1], which also aim to identify and manipulate high-level concepts in neural networks. A detailed comparison should include a discussion of the advantages and disadvantages of each approach, as well as a quantitative comparison on a common benchmark. Furthermore, the authors should compare their framework with other encoder-decoder based interpretability methods [2], highlighting the unique contributions of their work. This would help to establish the novelty and significance of the proposed framework within the broader landscape of interpretability research. The current lack of such comparisons makes it difficult to assess the true value of the proposed approach.

The evaluation metrics need to be more rigorously justified and connected to the interpretability goals. The intervention success rate, which measures whether increasing the activation of a feature increases the feature in the model's output, is not a strong measure of causal fidelity. A more appropriate metric would be to measure the causal effect of the intervention on the model's output, such as the change in the model's output when the feature is manipulated. The coherence-intervention tradeoff, which measures the model's coherence after intervention, is also not well-defined and lacks a clear connection to the interpretability goals. The authors should provide a clear definition of coherence and explain how it relates to the interpretability goals. A more appropriate metric would be to measure the change in the model's output when the feature is manipulated, while also considering the coherence of the output. The authors should also consider using metrics that directly measure the interpretability of the manipulated features, such as the ability to understand the relationship between the feature and the model's output.

Finally, the paper should include a more detailed analysis of the limitations of the proposed framework and metrics. The authors should discuss potential biases, assumptions, or edge cases that may arise in practical applications. For example, the paper should discuss how the framework would perform on models with different architectures or on tasks with more complex outputs. The authors should also discuss the computational cost of the proposed framework and metrics, and how these might limit its practical applicability. A thorough discussion of these limitations would help to establish the scope and limitations of the proposed approach and would provide a more balanced perspective on the findings. Without this, the generalizability of the findings is questionable.

### Questions

- How does the encoder-decoder framework handle cases where the intermediate representations are noisy or ambiguous?
- How does the framework perform on tasks that require more complex reasoning and inference?
- What are the potential biases or limitations of the proposed metrics, and how might they affect the evaluation results?

### Rating

3

### Confidence

3

**********
