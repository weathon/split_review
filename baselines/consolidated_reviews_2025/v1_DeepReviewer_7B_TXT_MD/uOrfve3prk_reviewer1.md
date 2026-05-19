### Summary

This paper proposes an encoder-decoder framework to unify various interpretability methods, including sparse autoencoders, logit lens, tuned lens, and probing. This framework maps intermediate representations to human-interpretable features, allowing interventions on these features to control model outputs. Two metrics, intervention success rate and coherence-intervention tradeoff, are introduced to evaluate the methods. The study finds that simpler methods like logit lens and tuned lens generally outperform sparse autoencoders in intervention capability, and non-interpretability-based approaches like prompting perform best overall.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

- The paper is well-organized and easy to follow.
- The proposed encoder-decoder framework is flexible and can incorporate various interpretability methods, providing a unified perspective on these methods.
- The study evaluates multiple interpretability methods across different models and intervention topics, providing a comprehensive comparison.

### Weaknesses

#### Some Related Works


#### comment

 - The paper's motivation is unclear. The introduction lacks a clear problem statement and motivation for the proposed encoder-decoder framework. The connection between the framework and the stated goals is not well-established.
- The paper lacks a strong theoretical foundation. The proposed framework and metrics are introduced without sufficient theoretical justification, making it difficult to assess their validity and generalizability.
- The evaluation is limited in scope. The study focuses on a specific set of models and intervention topics, which may not be representative of all possible scenarios. The lack of diversity in the experimental setup limits the generalizability of the findings.
- The paper does not adequately address the limitations of the proposed framework and metrics. There is no discussion of potential biases, assumptions, or edge cases that may arise in practical applications.

### Suggestions

The paper would benefit significantly from a more rigorous theoretical grounding. The authors should provide a formal definition of the encoder-decoder framework, including the mathematical properties of the mappings involved. This should include a discussion of the assumptions made about the latent space and the interpretability of the features. For example, what guarantees can be provided that the features extracted by the encoder are indeed meaningful and not just arbitrary patterns? Furthermore, the authors should explore the theoretical limitations of the proposed metrics, such as the coherence-intervention tradeoff. What are the conditions under which these metrics are reliable and how can their biases be mitigated? A more thorough theoretical analysis would greatly strengthen the paper's claims and provide a solid foundation for future research.

To address the limitations of the experimental evaluation, the authors should expand their analysis to include a wider range of models, including larger and more recent models. They should also explore a more diverse set of intervention topics, including more abstract concepts and complex relationships. For example, instead of focusing solely on simple word substitutions, they could investigate interventions that manipulate higher-level semantic concepts or causal relationships. Additionally, the authors should consider evaluating the framework's performance on tasks that require more complex reasoning and inference. This would provide a more comprehensive assessment of the framework's capabilities and limitations. The current evaluation is too narrow and does not fully demonstrate the potential of the proposed approach.

Finally, the paper needs a more thorough discussion of the limitations of the proposed framework and metrics. The authors should acknowledge the potential biases that may arise in the training data or the evaluation process. For example, how might the choice of specific interpretability methods or intervention topics influence the results? What are the potential edge cases where the framework might fail or produce misleading results? A more critical and nuanced discussion of these limitations would enhance the paper's credibility and provide a more balanced perspective on the proposed approach. The authors should also discuss the computational cost of the proposed framework and metrics, and how these might limit its practical applicability.

### Questions

- How does the encoder-decoder framework handle cases where the intermediate representations are noisy or ambiguous?
- How does the framework perform on tasks that require more complex reasoning and inference?
- What are the potential biases or limitations of the proposed metrics, and how might they affect the evaluation results?

### Rating

3

### Confidence

3

**********
