### Summary

This paper proposes a statistical test to determine if two models are trained independently or if one is derived from the other. The authors introduce a novel approach that simulates independent copies of each model and compares various measures of similarity in the weights and activations of the original two models to these independent copies, yielding exact p-values with respect to the null hypothesis that the models are trained with independent randomness. They evaluate the power of these tests on pairs of 21 open-weight models and find they reliably identify all 69 pairs of fine-tuned models. Notably, their tests remain effective even after substantial fine-tuning, accurately detecting dependence between Llama 2 and Llemma, even though the latter was fine-tuned on an 750B additional tokens (37.5% of the original Llama 2 training budget). Finally, they identify transformations of model weights that break the effectiveness of their tests without altering model outputs, and propose a mechanism for matching hidden activations between the MLP layers of two models that is robust to these transformations.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The authors conduct extensive experiments to validate the effectiveness of the proposed method.
3. The authors also explore the limitations of the proposed method and try to address them.

### Weaknesses

#### Some Related Works


#### comment

1. The proposed method relies on access to model weights and activations, which may not be feasible in all real-world scenarios, especially with proprietary models. This dependence on internal model parameters limits the applicability of the method in situations where only input-output access is available, or where model weights are protected by intellectual property. The method's effectiveness is also contingent on the ability to extract activations from specific layers, which may not be possible with all model architectures or API access schemes.
2. While the test is robust to fine-tuning, the paper acknowledges that certain weight transformations can evade detection. This highlights a potential limitation in scenarios where adversaries intentionally obfuscate model provenance. The paper does not fully explore the implications of these transformations, particularly in the context of adversarial attacks designed to circumvent the proposed test. The robustness of the method against more sophisticated weight manipulation techniques remains unclear.

### Suggestions

The authors should investigate alternative approaches that do not rely on direct access to model weights and activations. One potential direction is to explore methods based on analyzing the input-output behavior of models. For example, the authors could investigate the use of adversarial examples or carefully crafted input sequences to probe the internal representations of models. By comparing the responses of different models to these inputs, it might be possible to infer whether they share a common origin or have been trained independently. This would require developing new techniques for analyzing input-output patterns and establishing statistical tests that can detect subtle differences in model behavior. Furthermore, the authors could explore the use of techniques such as model distillation or surrogate models to approximate the behavior of proprietary models, allowing for the application of their method in situations where direct access is not possible. This would involve training a more accessible model to mimic the behavior of the proprietary model and then applying the proposed statistical test to the surrogate model.

To address the limitations regarding weight transformations, the authors should conduct a more thorough analysis of the types of transformations that can evade detection. This could involve exploring a wider range of weight manipulation techniques, including more sophisticated methods such as weight pruning, quantization, and knowledge distillation. The authors should also investigate the impact of these transformations on the statistical properties of the model weights and activations. By understanding how these transformations affect the test's sensitivity, the authors can develop more robust methods for detecting model dependence. Furthermore, the authors should explore the use of techniques such as adversarial training to make their test more resilient to weight transformations. This would involve training the test to be robust against specific types of weight manipulations, making it more difficult for adversaries to circumvent the test. The authors should also consider incorporating additional features beyond weights and activations, such as model architecture or training data characteristics, to improve the test's robustness.

Finally, the authors should provide more detailed guidance on how to apply their method in practice. This includes specifying the required resources, such as computational power and memory, as well as the steps involved in preparing the models for testing. The authors should also discuss the limitations of their method in more detail, including the types of models and training scenarios where it may not be applicable. This would help potential users to understand the strengths and weaknesses of the method and to make informed decisions about its applicability to their specific use cases. The authors should also provide a more detailed analysis of the statistical properties of their test, including the distribution of p-values under the null hypothesis and the power of the test to detect different levels of model dependence. This would help to establish the statistical validity of the method and to provide a more rigorous basis for its interpretation.

### Questions

1. How does the proposed method perform when only a small amount of training data is available? Does the test have enough power to detect dependence in such cases?
2. How does the proposed method handle cases where the models have different architectures or have been trained on different datasets? Does the test have enough robustness to handle such scenarios?

### Rating

6

### Confidence

3

**********
