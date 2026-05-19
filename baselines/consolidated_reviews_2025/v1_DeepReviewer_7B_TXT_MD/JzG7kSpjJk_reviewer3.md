### Summary

The paper proposes a method for low-bit weight-only quantization of LLMs. The main idea is to use per-channel quantization instead of per-output-channel quantization. The authors also propose an adaptive method that can automatically choose between per-channel and per-output-channel quantization for each layer. Experiments show that the proposed method can achieve better performance than previous methods.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The proposed method is simple and effective.
2. The paper is well-written and easy to follow.
3. The authors conduct extensive experiments to validate the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The main concern is the novelty of the proposed method. The idea of per-channel quantization has been proposed in previous works, e.g., LLM.int8. The main difference is that LLM.int8 uses per-group quantization, which is more complicated than per-channel quantization. It is not clear to me why per-channel quantization is better than per-group quantization in LLM.int8. Specifically, the paper does not adequately address the trade-offs between the simplicity of per-channel quantization and the potential performance gains of per-group quantization, especially given that per-group quantization in LLM.int8 is not the most complex approach available. The paper needs to clarify why a simple per-channel approach is preferable to a more sophisticated per-group method, especially considering the additional complexity it introduces.
2. The authors claim that the proposed method can adaptively choose between per-channel and per-output-channel quantization for each layer. However, it is not clear how the proposed method can adaptively choose between per-channel and per-output-channel quantization for each layer. The paper lacks a clear explanation of the adaptive mechanism. It is not sufficient to simply state that the method can adapt; the paper needs to detail the specific criteria or metrics used to determine when to switch between per-channel and per-output-channel quantization. Without this, the claim of adaptivity is unsubstantiated.
3. The proposed method seems to only support low-bit quantization, while AWQ supports higher-bit quantization. The paper should clarify the limitations of the proposed method in terms of bit-width support and justify why it is not compared against AWQ in higher bit-width settings. The lack of comparison with AWQ in higher bit-width settings is a significant oversight, as it limits the scope of the evaluation and makes it difficult to assess the true potential of the proposed method.

### Suggestions

The paper should provide a more detailed analysis of the per-channel quantization method, specifically addressing why it is superior to per-group quantization in the context of LLM.int8. A thorough comparison of the computational complexity and memory requirements of both approaches would be beneficial. Furthermore, the paper should include a discussion of the potential limitations of per-channel quantization, such as its impact on the expressiveness of the model. The authors should also explore the possibility of combining per-channel and per-group quantization techniques to leverage the strengths of both approaches. For example, they could consider using per-channel quantization for certain layers or channels and per-group quantization for others, based on a more sophisticated analysis of the model's sensitivity to quantization.

To address the lack of clarity regarding the adaptive mechanism, the paper should provide a detailed explanation of the criteria used to determine when to switch between per-channel and per-output-channel quantization. This explanation should include a clear definition of the metrics or features used to make the decision, as well as a discussion of the rationale behind these choices. The paper should also provide empirical evidence to support the effectiveness of the adaptive mechanism, such as a breakdown of the performance of the method across different layers and model sizes, showing how the choice between per-channel and per-output-channel quantization varies. It would be helpful to include a visualization of the adaptive process, showing how the method dynamically adjusts the quantization strategy during training.

Finally, the paper should address the limitation of supporting only low-bit quantization by either extending the evaluation to include higher bit-width settings or providing a clear justification for why this is not feasible. If the method is indeed limited to low-bit quantization, this should be explicitly stated in the paper, and the limitations should be discussed in detail. The authors should also compare their method with AWQ in higher bit-width settings, even if it requires some modifications to their method. This would provide a more comprehensive evaluation of the proposed method and allow for a more accurate assessment of its performance relative to existing approaches.

### Questions

Please see the weaknesses.

### Rating

3: reject, not good enough

### Confidence

5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

**********
