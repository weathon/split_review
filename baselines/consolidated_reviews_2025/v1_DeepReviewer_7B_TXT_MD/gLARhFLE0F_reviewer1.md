### Summary

This paper introduces LUT-GEMM, a kernel for efficient inference in large language models (LLMs). It addresses the memory wall problem by using quantized weights and a binary-coding quantization format. The proposed kernel eliminates the need for dequantization, resulting in a faster token generation latency. The authors demonstrate that LUT-GEMM can accelerate token generation latency by 2.1x compared to OPTQ.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

- The paper is well-structured and easy to follow.
- The proposed method is simple and effective, achieving a 2.1x speedup in token generation latency compared to OPTQ.

### Weaknesses

#### Some Related Works


#### comment

 - The paper lacks a comprehensive discussion of related work, particularly concerning other quantization techniques and their impact on inference speed. It would be beneficial to include a more detailed comparison with existing methods, such as AWQ, to better contextualize the contribution of LUT-GEMM.
- The paper does not adequately address the potential limitations of the proposed method. For instance, it is unclear how the method would perform with different model architectures or under varying computational constraints. The evaluation is limited to a few model sizes and does not explore the impact of different quantization levels on the final performance.
- The paper does not provide a detailed analysis of the memory footprint of the proposed method. While the authors mention reduced memory usage, a more quantitative analysis, including the memory requirements for different model sizes and quantization levels, would be beneficial. It is also unclear how the memory footprint scales with the number of GPUs used for inference.
- The paper does not provide a detailed analysis of the computational overhead of the proposed method. While the authors claim that LUT-GEMM is faster than OPTQ, it is unclear how the computational cost of the proposed method compares to other quantization techniques, such as AWQ, in terms of both latency and energy consumption. A more detailed analysis of the computational cost of the proposed method would be beneficial.

### Suggestions

The paper would benefit from a more thorough comparison with existing quantization techniques, particularly those that also aim to reduce memory footprint and improve inference speed. A detailed comparison with methods like AWQ, including a discussion of the trade-offs between different approaches, would help to better contextualize the contribution of LUT-GEMM. This comparison should not only focus on latency but also consider other factors such as memory usage, computational overhead, and the complexity of implementation. Furthermore, the authors should provide a more detailed analysis of the performance of LUT-GEMM across a wider range of model architectures and sizes. This analysis should include a discussion of how the method scales with model size and how it performs with different types of models, such as those with varying depths and widths. It would also be beneficial to explore the impact of different quantization levels on the final performance, including a discussion of the trade-offs between compression and accuracy. This would provide a more comprehensive understanding of the applicability of the proposed method in different scenarios.

To address the lack of detailed analysis on memory footprint, the authors should provide a more quantitative analysis of the memory requirements of LUT-GEMM, including the memory usage for different model sizes and quantization levels. This analysis should also consider the memory footprint when using multiple GPUs for inference. It would be beneficial to provide a breakdown of the memory usage for different components of the model, such as the weights, activations, and other data structures. This would help to identify potential bottlenecks and guide future optimization efforts. Additionally, the authors should provide a more detailed analysis of the computational overhead of LUT-GEMM, including a comparison with other quantization techniques in terms of both latency and energy consumption. This analysis should consider the computational cost of the proposed method in terms of both the number of operations and the energy consumption. A detailed analysis of the computational cost of the proposed method would be beneficial.

Finally, the paper should include a more detailed discussion of the limitations of the proposed method. This discussion should include a consideration of the potential challenges of applying LUT-GEMM to different types of models and hardware platforms. The authors should also discuss the potential impact of the proposed method on the overall system performance, including the impact on memory bandwidth and inter-GPU communication. A more thorough discussion of the limitations of the proposed method would help to provide a more balanced and realistic assessment of its applicability in different scenarios.

### Questions

- How does the proposed method compare to other quantization techniques, such as AWQ, in terms of latency, memory usage, and computational overhead?
- What are the potential limitations of the proposed method, and how might these limitations impact its applicability in different scenarios?
- How does the proposed method scale with model size and complexity? Are there any specific challenges or considerations when applying it to larger models?

### Rating

5

### Confidence

4

**********
