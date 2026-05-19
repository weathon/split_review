### Summary

This paper proposes a new approach to low-bit weight-only quantization of LLMs. The key idea is to perform per-channel quantization instead of per-output-channel quantization, which can effectively reduce the outlier issue. The authors further propose a method to adaptively choose between per-channel and per-output-channel quantization for each layer. Experiments show that the proposed method can achieve better performance than previous methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and effective.
3. The authors conduct extensive experiments to validate the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The main concern is the novelty of the proposed method. The idea of per-channel quantization has been proposed in previous works, e.g., LLM.int8. The main difference is that LLM.int8 uses per-group quantization, which is more complicated than per-channel quantization. It is not clear to me why per-channel quantization is better than per-group quantization in LLM.int8. Specifically, the paper does not adequately explain the trade-offs between the simplicity of per-channel quantization and the potential performance gains of per-group quantization, especially given that per-group quantization in LLM.int8 is not the most complex approach available. The paper needs to clarify why a simple per-channel approach is preferable to a more sophisticated per-group method, especially considering the additional complexity it introduces.
2. The authors claim that the proposed method can adaptively choose between per-channel and per-output-channel quantization for each layer. However, it is not clear how the proposed method can adaptively choose between per-channel and per-output-channel quantization for each layer. The paper lacks a clear explanation of the adaptive mechanism. It is not sufficient to simply state that the method can adapt; the paper needs to detail the specific criteria or metrics used to determine when to switch between per-channel and per-output-channel quantization. Without this, the claim of adaptivity is unsubstantiated.
3. The proposed method seems to only support low-bit quantization, while AWQ supports higher-bit quantization. The paper should clarify the limitations of the proposed method in terms of bit-width support and justify why it is not compared against AWQ in higher bit-width settings. The lack of comparison with AWQ in higher bit-width settings is a significant oversight, as it limits the scope of the evaluation and makes it difficult to assess the true potential of the proposed method.

### Suggestions

The paper needs to provide a more thorough justification for its choice of per-channel quantization over per-group quantization, especially given the existence of more complex methods like those used in LLM.int8. A detailed analysis of the trade-offs between simplicity and performance is needed. This analysis should include a discussion of the specific scenarios where per-channel quantization is expected to outperform per-group quantization, and why the added complexity of per-group quantization in LLM.int8 is not always beneficial. The authors should also consider providing a more in-depth comparison of the computational overhead of per-channel versus per-group quantization, as this could be a significant factor in practical applications. Furthermore, the paper should explore the potential for hybrid approaches that combine the simplicity of per-channel quantization with the performance benefits of per-group quantization, rather than simply stating that per-channel is sufficient.

To address the lack of clarity regarding the adaptive mechanism, the paper should provide a detailed explanation of the criteria used to determine when to switch between per-channel and per-output-channel quantization. This explanation should include a clear definition of the metrics or features used to make the decision, as well as a discussion of the rationale behind these choices. The paper should also provide empirical evidence to support the effectiveness of the adaptive mechanism, such as a breakdown of the performance of the method across different layers and model sizes, showing how the choice between per-channel and per-output-channel quantization varies. This would help to demonstrate the adaptivity of the method and justify the claim that it can dynamically adjust to different model characteristics. The authors should also consider providing a more detailed analysis of the impact of the adaptive mechanism on the overall performance of the model, including a comparison of the performance with and without the adaptive mechanism.

Finally, the paper needs to address the limitation of supporting only low-bit quantization and clarify why it is not compared against AWQ in higher bit-width settings. The authors should either extend the evaluation to include higher bit-width settings or provide a clear justification for why this is not feasible. If the method is indeed limited to low-bit quantization, this should be explicitly stated in the paper, and the limitations should be discussed in detail. The paper should also provide a more comprehensive comparison with other state-of-the-art methods, including those that support higher bit-width quantization, to better contextualize the contribution of the proposed method. This would help to demonstrate the strengths and weaknesses of the proposed method and provide a more complete picture of its performance relative to existing approaches.

### Questions

1. What is the difference between the proposed method and LLM.int8?
2. How can the proposed method adaptively choose between per-channel and per-output-channel quantization for each layer?

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
