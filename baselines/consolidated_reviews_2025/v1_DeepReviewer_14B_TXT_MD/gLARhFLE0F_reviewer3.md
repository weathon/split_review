### Summary

The paper proposes a new method for accelerating LLM inference by using quantized weights without dequantization. The method is based on a binary-coding quantization (BCQ) format, which represents weights as a sum of binary vectors with scaling factors and a bias term. The paper shows that this format can support both uniform and non-uniform quantization methods, and can be used to construct a lookup table (LUT) that avoids redundant computations and bit-level memory accesses. The paper also shows that the method can achieve a trade-off between compression ratio and accuracy by using group-wise quantization, and can reduce the number of GPUs required for inference. The paper evaluates the method on OPT-175B and LLaMA models, and shows that it can accelerate token generation latency by 2.1x compared to OPTQ.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper proposes a novel method for accelerating LLM inference by using quantized weights without dequantization. The method is based on a binary-coding quantization (BCQ) format, which represents weights as a sum of binary vectors with scaling factors and a bias term. The paper shows that this format can support both uniform and non-uniform quantization methods, and can be used to construct a lookup table (LUT) that avoids redundant computations and bit-level memory accesses.
- The paper shows that the method can achieve a trade-off between compression ratio and accuracy by using group-wise quantization, and can reduce the number of GPUs required for inference.
- The paper evaluates the method on OPT-175B and LLaMA models, and shows that it can accelerate token generation latency by 2.1x compared to OPTQ.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the impact of the bias term on the accuracy and performance of the method. It is not clear how the bias term is chosen, and how it affects the quantization error and the LUT size. A more thorough investigation of the bias term is needed to understand its role and limitations.
- The paper does not compare the method with other weight-only quantization methods, such as AWQ, which also claim to achieve high compression ratios and accuracy. A more comprehensive comparison is needed to demonstrate the advantages and disadvantages of the proposed method over existing approaches.
- The paper does not discuss the potential challenges and limitations of the method for different hardware platforms and model architectures. For example, how does the method perform on CPUs or TPUs? How does the method handle different layer types, such as attention or normalization layers? A more detailed discussion of the hardware and model dependencies of the method is needed to assess its generalizability and applicability.

### Suggestions

The paper should include a more detailed analysis of the bias term's impact on both accuracy and performance. Specifically, the authors should investigate how different bias values affect the quantization error and the resulting LUT size. It would be beneficial to provide a sensitivity analysis showing how the choice of bias affects the trade-off between compression and accuracy. Furthermore, the paper should clarify the method used to select the bias term, whether it is a fixed value, a learned parameter, or derived from some other criteria. This analysis should also include a discussion of the computational overhead associated with the bias term, such as the cost of adding it to the LUT or the impact on the LUT lookup process. Without a clear understanding of the bias term's role, it is difficult to assess the method's robustness and practical applicability.

To strengthen the paper, a more comprehensive comparison with other weight-only quantization methods is essential. The authors should compare their method against state-of-the-art techniques like AWQ, not just in terms of compression ratio, but also in terms of accuracy, latency, and memory footprint. This comparison should include a detailed analysis of the trade-offs between different quantization methods, highlighting the specific scenarios where the proposed method excels or falls short. The comparison should also consider the computational overhead of each method, including the cost of dequantization or other operations. A thorough comparison would provide a clearer understanding of the proposed method's advantages and limitations relative to existing approaches and help position the work within the broader context of model compression techniques.

Finally, the paper needs to address the hardware and model dependencies of the proposed method. The authors should discuss how the method performs on different hardware platforms, such as CPUs and TPUs, and how it scales with different model architectures. This discussion should include an analysis of the method's performance on different layer types, such as attention and normalization layers, and how the method handles the specific challenges associated with each layer type. The paper should also address the potential limitations of the method, such as the impact of LUT size on memory usage and the computational cost of LUT lookups. A more detailed discussion of these aspects would help assess the method's generalizability and applicability to a wider range of scenarios.

### Questions

- How does the bias term affect the accuracy and performance of the method? How is the bias term chosen?
- How does the method compare with other weight-only quantization methods, such as AWQ?
- How does the method perform on different hardware platforms and model architectures?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
