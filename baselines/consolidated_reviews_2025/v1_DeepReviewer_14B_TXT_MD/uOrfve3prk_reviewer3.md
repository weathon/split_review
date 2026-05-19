### Summary

This paper introduces a unified framework for four popular interpretability methods: sparse autoencoders, logit lens, tuned lens, and probing. The framework allows for structured interventions on human-interpretable features, mapping them back to model latent representations to directly control outputs. The authors introduce two evaluation metrics: intervention success rate and the coherence-intervention tradeoff, to assess the causal fidelity and utility of interpretability methods. The findings reveal inconsistencies in intervention capabilities across different methods and models, with simpler lens-based approaches generally outperforming more complex methods for simple interventions. However, non-interpretability-based approaches like prompting often perform best, highlighting gaps in current interpretability approaches.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper proposes a unified framework that integrates four popular interpretability methods, providing a structured approach to both interpret and control model behavior through interventions.
2. The introduction of two standardized metrics, intervention success rate and coherence-intervention tradeoff, offers a rigorous basis for evaluating the causal fidelity and utility of interpretability methods.
3. The paper conducts extensive experiments across multiple models (GPT2-small, Gemma2-2b, and Llama2-7b) and methods, providing a comprehensive evaluation of intervention capabilities.

### Weaknesses

#### Some Related Works


#### comment

1. The paper primarily focuses on simple, low-level features for intervention, which may not fully capture the complexities of real-world applications requiring abstract or high-level feature control. Specifically, the interventions are limited to token-level manipulations, neglecting the potential for more nuanced interventions at the level of concepts or relationships. This limits the applicability of the findings to scenarios requiring more sophisticated control over model behavior.
2. The effectiveness of interventions varies significantly across different models, with some methods showing limited impact or even negative effects on output coherence. The paper lacks a detailed analysis of why certain methods fail or degrade performance in specific models. For instance, it is unclear why sparse autoencoders perform poorly on GPT2-small, or why interventions using steering vectors and probes have minimal effect on Gemma2-2b. This variability makes it difficult to draw general conclusions about the reliability of these methods.
3. The paper notes that interventions often lead to a decline in text coherence, especially with stronger intervention strengths, which could limit the practical application of these methods in scenarios requiring high model performance. The trade-off between intervention success and coherence is not sufficiently explored, and the paper does not provide clear guidelines on how to balance these two factors. The lack of a systematic approach to managing this trade-off is a significant limitation.

### Suggestions

The paper would benefit from a more in-depth exploration of high-level feature interventions. Instead of focusing solely on token-level manipulations, the authors should investigate methods for intervening on more abstract concepts or relationships within the model's representation space. This could involve techniques such as identifying and manipulating latent vectors corresponding to specific concepts, or using more sophisticated methods for disentangling the model's representation space. For example, the authors could explore the use of contrastive learning to identify latent vectors that correspond to specific high-level features, and then use these vectors to guide interventions. This would allow for a more nuanced understanding of the model's behavior and enable more targeted control over its outputs. Furthermore, the paper should include a more detailed analysis of the failure cases of different intervention methods. The authors should investigate why certain methods perform poorly on specific models, and provide insights into the underlying causes of these failures. This could involve analyzing the model's internal representations, identifying potential bottlenecks or limitations of the intervention methods, and exploring alternative approaches. For instance, the authors could examine the activation patterns of different layers in the model to understand how interventions propagate through the network, and identify potential sources of interference or degradation. Finally, the paper should provide a more systematic approach to managing the trade-off between intervention success and coherence. The authors should explore methods for optimizing interventions to achieve a better balance between these two factors. This could involve using techniques such as regularization or adaptive intervention strengths, or developing new metrics that capture both intervention success and coherence. For example, the authors could explore the use of a coherence-preserving loss function that penalizes interventions that lead to incoherent outputs, or develop a method for dynamically adjusting the intervention strength based on the model's current state.

### Questions

1. How do the proposed methods perform when intervening on more complex or abstract concepts beyond specific words or phrases?
2. Can the proposed framework and evaluation metrics be adapted to other types of models or tasks beyond language generation?
3. How do the different methods compare in terms of computational cost and scalability for large language models?
4. How sensitive are the results to the choice of hyperparameters, such as the intervention strength α?

### Rating

6

### Confidence

3

**********
