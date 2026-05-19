### Summary

This paper addresses the gap between interpretability and control in large language models (LLMs). The authors propose an intervention-based framework to unify and evaluate four popular interpretability methods: sparse autoencoders, logit lens, tuned lens, and probing. By mapping latent representations to human-interpretable features, they enable controlled interventions to assess each method's effectiveness in modifying model behavior. They introduce two evaluation metrics: intervention success rate and coherence-intervention tradeoff. The results show that while current methods allow for intervention, they are inconsistent across models and features, with lens-based methods performing better for simple interventions. However, interventions often compromise model coherence, underperforming simpler methods like prompting.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper provides a unified framework for interpretability and control, addressing a critical gap in the field. The intervention-based approach offers a practical way to evaluate interpretability methods by their ability to control model behavior.

2. The paper introduces two new evaluation metrics, intervention success rate and coherence-intervention tradeoff, which provide a quantitative way to assess the effectiveness and utility of interpretability methods.

3. The authors conduct extensive experiments across multiple models (GPT2-small, Gemma2-2b, and Llama2-7b) and various intervention topics, providing a comprehensive evaluation of the proposed framework and methods.

### Weaknesses

#### Some Related Works


#### comment

1. The paper focuses primarily on simple intervention topics (e.g., specific words or phrases), which may not generalize to more complex or abstract intervention topics relevant to real-world applications. The evaluation of intervention success is limited to surface-level text changes, and does not assess whether the model's internal understanding or reasoning is actually being modified in a meaningful way. For example, intervening on a concept like 'fairness' or 'bias' would require a more nuanced approach than simply inserting or deleting keywords.

2. The proposed framework and evaluation metrics may not be applicable to other types of models or tasks beyond language generation. The reliance on token-level manipulations and text-based coherence metrics limits the generalizability of the approach to other modalities or tasks where such manipulations are not directly applicable. For instance, it is unclear how this framework would apply to models performing image classification or reinforcement learning tasks.

3. The paper acknowledges that the learned features of sparse autoencoders are frequently not human-interpretable, which can limit their practical utility. The lack of clear semantic meaning for the learned features makes it difficult to design targeted interventions and to understand the underlying mechanisms of the model. This limitation undermines the goal of using interpretability methods to gain deeper insights into model behavior.

4. The paper does not provide a clear comparison of the computational cost and scalability of different methods, which can be an important factor for practical applications. Without a detailed analysis of the computational resources required for each method, it is difficult to assess their feasibility for large-scale models or real-time applications. The lack of such analysis makes it hard to choose the most appropriate method for a given use case.

### Suggestions

The authors should consider expanding their evaluation to include more complex and abstract intervention topics that are relevant to real-world applications. This could involve designing interventions that target higher-level concepts such as reasoning, bias, or ethical considerations. For example, instead of simply inserting the word 'democracy', the authors could attempt to intervene on the model's understanding of democratic principles and assess how this intervention affects its responses to related questions. This would require developing new metrics that can capture the impact of interventions on the model's internal representations and reasoning processes, rather than just surface-level text changes. Furthermore, the authors should explore methods for evaluating the long-term effects of interventions, as a single intervention may not be sufficient to induce a lasting change in the model's behavior. This could involve tracking the model's responses over multiple interactions or evaluating its performance on downstream tasks after the intervention.

To address the limited generalizability of the proposed framework, the authors should investigate how their methods can be adapted to other types of models and tasks beyond language generation. This could involve exploring alternative manipulation techniques that are not reliant on token-level operations, as well as developing new metrics that are suitable for different modalities and tasks. For example, in the context of image classification, the authors could investigate how interventions on feature maps affect the model's predictions. In reinforcement learning, they could explore how interventions on the agent's policy or value function impact its behavior. This would require a significant effort to develop new tools and techniques, but it would greatly enhance the applicability of the proposed framework. The authors should also consider the limitations of their approach in scenarios where the model's behavior is highly non-linear or where the relationship between the intervention and the outcome is not straightforward.

Finally, the authors should provide a more detailed analysis of the computational cost and scalability of the different methods they evaluate. This should include a breakdown of the time and memory requirements for each method, as well as an analysis of how these requirements scale with the size of the model and the complexity of the intervention. The authors should also investigate techniques for improving the efficiency of the more computationally expensive methods, such as sparse autoencoders. This could involve exploring methods for pruning the dictionary or using more efficient optimization algorithms. A thorough analysis of the computational aspects of these methods is crucial for their practical application, and it would greatly enhance the value of the paper.

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
