### Summary

This paper proposes a method to forecast which examples will be forgotten when a language model is updated to correct errors. The authors introduce two forecasting methods: a partially interpretable model based on logit changes and a black-box classifier based on example representations. They demonstrate that by replaying the forecasted forgotten examples, they can reduce catastrophic forgetting compared to random replay, improving the model's stability and performance.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The paper introduces a novel problem setup of forecasting example forgetting in model refinement, which is a significant contribution to the field of continual learning and model stability.
2. The proposed forecasting methods, especially the representation-based model, show promising results across various setups and model architectures, indicating the potential for practical applications.
3. The authors provide a thorough evaluation of their methods, including out-of-domain generalization and continual model refinement scenarios, which strengthens the validity of their findings.

### Weaknesses

#### Some Related Works


#### comment

1. The logit-change based forecasting method shows inconsistent performance across different models (BART vs. T5), which suggests that the method might not be universally applicable or requires model-specific tuning. The paper does not provide a clear explanation for why this method works well on BART but fails on T5, which raises questions about the underlying assumptions and limitations of the approach. Specifically, the method's reliance on first-order approximations of logit changes might be more suitable for models with simpler architectures or specific training regimes, and this needs to be explored further.
2. The partially interpretable model, while offering some insights, may not provide a complete understanding of the complex dynamics of example forgetting. The interpretation provided by the logit-change based model is limited to the transfer of logit changes, and it does not capture other potential factors that might contribute to forgetting, such as the interaction between examples or the specific characteristics of the model's internal representations. A more comprehensive analysis of the forgetting process is needed to fully understand the model's behavior.
3. The paper could benefit from a more detailed analysis of the computational efficiency of the forecasting methods, especially when applied to very large language models. While the authors mention the computational cost, a more thorough analysis of the time and memory requirements for each method, especially in comparison to other continual learning techniques, would be valuable. This analysis should also consider the scalability of the methods to larger datasets and model sizes.

### Suggestions

The paper should delve deeper into the reasons behind the inconsistent performance of the logit-change based forecasting method across different model architectures. A more detailed analysis of the model-specific characteristics that influence the effectiveness of this method is needed. For example, the authors could investigate how the depth of the model, the type of attention mechanisms, or the pre-training objectives affect the logit change transfer. Furthermore, exploring the impact of different fine-tuning strategies on the performance of the logit-change based method could provide valuable insights. It would also be beneficial to explore alternative methods for approximating logit changes that are less sensitive to model architecture, potentially using techniques from sensitivity analysis or adversarial training. This would help in making the method more robust and widely applicable.

To enhance the interpretability of the model, the authors should consider incorporating techniques that can provide a more comprehensive understanding of the forgetting process. For instance, they could explore methods for visualizing the internal representations of the model and how they change during the learning process. Analyzing the activation patterns of different layers could reveal which parts of the model are most affected by the fine-tuning process and contribute to forgetting. Additionally, investigating the relationship between the input examples and the model's internal representations could provide insights into why certain examples are more prone to forgetting than others. This could involve techniques such as probing, concept activation vectors, or other methods for analyzing the model's learned features. A more detailed analysis of the interaction between examples, beyond simple similarity measures, could also be beneficial.

The paper should include a more detailed analysis of the computational efficiency of the proposed forecasting methods. This analysis should include a breakdown of the time and memory requirements for each step of the methods, such as the computation of logits, the training of the forecasting models, and the replay of forgotten examples. The authors should also compare the computational cost of their methods to other continual learning techniques, such as regularization-based methods or replay-based methods. This comparison should consider both the training time and the memory requirements. Furthermore, the authors should investigate the scalability of their methods to larger datasets and model sizes. This could involve experiments with different batch sizes, model architectures, and dataset sizes. A thorough analysis of the computational efficiency would help in assessing the practical applicability of the proposed methods.

### Questions

1. How does the forecasting performance change when the model is updated on a batch of errors instead of a single error?
2. Can the forecasting methods be extended to other types of model updates beyond fine-tuning, such as pruning or quantization?
3. What are the implications of the observed logit change transfer phenomenon for understanding the internal mechanisms of language models, and how can this knowledge be used to improve model robustness?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
