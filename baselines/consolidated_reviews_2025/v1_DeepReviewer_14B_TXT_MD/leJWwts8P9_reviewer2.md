### Summary

This paper addresses the problem of model provenance in the context of large language models (LLMs). Specifically, it focuses on determining whether two models have been trained independently or if one is derived from the other (e.g., through fine-tuning or transfer learning). The authors propose a statistical test to assess the independence of two models based on the similarity of their weights and activations. The paper's main contributions are:

1) A statistical test for model independence that provides exact p-values, regardless of the training data composition. The test works by comparing the similarity of weights and activations of the original models with those of independently trained copies.

2) An evaluation of the test's power on a diverse set of 21 open-weight models (forming 210 pairs), demonstrating its ability to reliably identify pairs of fine-tuned models.

3) An analysis of transformations that can evade the proposed test without altering model outputs, highlighting potential limitations.

4) A proposed mechanism for matching hidden activations between MLP layers of different models, making the test robust to certain weight transformations and retraining scenarios.

### Soundness

3

### Presentation

2

### Contribution

2

### Strengths

1) The proposed statistical test provides a principled way to assess model independence, offering exact p-values and being applicable to models of any architecture.

2) The test demonstrates strong empirical performance, reliably identifying fine-tuned models even after substantial modifications (e.g., Llemma model fine-tuned on 750B additional tokens).

3) The authors thoroughly evaluate their method on a large-scale dataset of 21 open-weight models, providing strong empirical evidence for its effectiveness.

4) The paper addresses potential evasion attacks and proposes solutions to enhance the robustness of the test, showing a commitment to practical applicability.

### Weaknesses

#### Some Related Works


#### comment

1) The proposed method relies on access to model weights and activations, which may not be feasible in all real-world scenarios, especially with proprietary models.

2) While the test is robust to fine-tuning, the paper acknowledges that certain weight transformations can evade detection. This highlights a potential limitation in scenarios where adversaries intentionally obfuscate model provenance.

3) The paper focuses primarily on transformer-based LLMs. It's unclear how well the proposed method generalizes to other types of models (e.g., smaller language models, non-LLM architectures).

### Suggestions

The reliance on access to model weights and activations is a significant limitation that needs to be addressed more thoroughly. While the authors mention that their method does not require access to training data, the requirement for model weights severely restricts its applicability in real-world scenarios where models are often proprietary. The paper should include a more detailed discussion of alternative approaches that could be used when model weights are not available, such as methods based on analyzing model outputs or API calls. Furthermore, the authors should explore the feasibility of using their method with black-box models, where only input-output pairs are available. This would involve adapting their statistical test to work with limited information, potentially by comparing the distributions of model outputs on a shared input set. The paper should also discuss the limitations of such adaptations and the potential for reduced accuracy or increased computational cost.

Regarding the robustness of the method, the paper acknowledges that certain weight transformations can evade detection, but it does not provide a comprehensive analysis of the types of transformations that are most problematic. The authors should investigate a wider range of weight transformations, including more complex operations such as weight shuffling, low-rank approximations, and quantization. It is crucial to understand the limitations of the proposed method in the face of these transformations, as adversaries may intentionally use them to obfuscate model provenance. The paper should also explore potential defenses against these evasion techniques, such as incorporating more robust similarity metrics or using adversarial training to make the test more resilient. A more detailed analysis of the trade-offs between robustness and computational cost is also needed.

Finally, the paper's focus on transformer-based LLMs limits the generalizability of the proposed method. While the authors argue that transformers are the dominant architecture for LLMs, it is important to investigate how well the method performs on other types of models, such as smaller language models, recurrent neural networks, and convolutional neural networks. The paper should include experiments on a more diverse set of models to demonstrate the broader applicability of the proposed method. Furthermore, the authors should discuss the potential challenges of applying their method to different architectures and identify any modifications that may be necessary. This would involve analyzing the specific characteristics of each architecture and adapting the statistical test accordingly. The paper should also discuss the computational cost of applying the method to different model sizes and architectures.

### Questions

1) How does the computational cost of the proposed method scale with the size of the models being compared? Are there any optimizations that can be applied to improve efficiency?

2) The paper mentions that the test remains effective even after substantial fine-tuning. Is there a limit to the amount of fine-tuning that the test can reliably detect? How does the test perform when only a small portion of the model has been fine-tuned?

3) You mention that certain weight transformations can break the effectiveness of the test. Are there other types of transformations that could potentially evade detection? How robust is the proposed mechanism for matching hidden activations against a wider range of weight transformations?

4) How does the choice of similarity metric affect the performance of the test? Are there other similarity metrics that could be more effective in certain scenarios?

5) The paper focuses on transformer-based LLMs. How well does the proposed method generalize to other types of models (e.g., smaller language models, non-LLM architectures)?

### Rating

5

### Confidence

3

**********
