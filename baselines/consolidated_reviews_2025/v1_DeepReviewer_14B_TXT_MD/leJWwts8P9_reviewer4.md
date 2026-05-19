### Summary

The paper proposes a statistical test to determine whether two language models are trained independently or if one is derived from the other (e.g., through fine-tuning or transfer learning). The authors introduce a novel approach that simulates independent copies of each model and compares various measures of similarity in the weights and activations of the original two models to these independent copies, yielding exact p-values with respect to the null hypothesis that the models are trained with independent randomness. They evaluate the power of these tests on pairs of 21 open-weight models and find they reliably identify all 69 pairs of fine-tuned models. Notably, their tests remain effective even after substantial fine-tuning; they accurately detect dependence between Llama 2 and Llemma, even though the latter was fine-tuned on an 750B additional tokens (37.5% of the original Llama 2 training budget). Finally, they identify transformations of model weights that break the effectiveness of their tests without altering model outputs, and—motivated by the existence of these evasion attacks—they propose a mechanism for matching hidden activations between the MLP layers of two models that is robust to these transformations.

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

1. The proposed method relies on access to model weights and activations, which may not be feasible in all real-world scenarios, especially with proprietary models.
2. While the test is robust to fine-tuning, the paper acknowledges that certain weight transformations can evade detection.

### Suggestions

The reliance on access to model weights and activations is a significant limitation that needs to be addressed more thoroughly. While the authors mention that their method does not require access to training data, the requirement for model weights severely restricts its applicability in real-world scenarios where models are often proprietary. The paper should include a more detailed discussion of alternative approaches that could be used when model weights are not available, such as methods based on analyzing model outputs or API calls. Furthermore, the authors should explore the feasibility of using their method with black-box models, where only input-output pairs are available. This would involve adapting their statistical test to work with limited information, potentially by comparing the distributions of model outputs on a shared input set. The paper should also discuss the limitations of such adaptations and the potential for reduced accuracy or increased computational cost.

Regarding the robustness of the method, the paper acknowledges that certain weight transformations can evade detection, but it does not provide a comprehensive analysis of the types of transformations that are most problematic. The authors should investigate a wider range of weight transformations, including more complex operations such as weight shuffling, low-rank approximations, and quantization. It is crucial to understand the limitations of the proposed method in the face of these transformations, as adversaries may intentionally use them to obfuscate model provenance. The paper should also explore potential defenses against these evasion techniques, such as incorporating more robust similarity metrics or using adversarial training to make the test more resilient. A more detailed analysis of the trade-offs between robustness and computational cost is also needed.

Finally, the paper should provide more detailed guidance on how to apply their method in practice. This includes specifying the required resources, such as computational power and memory, as well as the steps involved in preparing the models for testing. The authors should also discuss the limitations of their method in more detail, including the types of models and training scenarios where it may not be applicable. This would help potential users to understand the strengths and weaknesses of the method and to make informed decisions about its applicability to their specific use cases.

### Questions

1. How does the computational cost of the proposed method scale with the size of the models being compared? Are there any optimizations that can be applied to improve efficiency?
2. The paper mentions that the test remains effective even after substantial fine-tuning. Is there a limit to the amount of fine-tuning that the test can reliably detect? How does the test perform when only a small portion of the model has been fine-tuned?
3. You mention that certain weight transformations can break the effectiveness of the test. Are there other types of transformations that could potentially evade detection? How robust is the proposed mechanism for matching hidden activations against a wider range of weight transformations?
4. How does the choice of similarity metric affect the performance of the test? Are there other similarity metrics that could be more effective in certain scenarios?
5. The paper focuses on transformer-based LLMs. How well does the proposed method generalize to other types of models (e.g., smaller language models, non-LLM architectures)?

### Rating

6

### Confidence

3

**********
