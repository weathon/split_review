### Summary

This paper introduces LUT-GEMM, a kernel designed to accelerate inference in large language models (LLMs) by utilizing quantized weights without the need for dequantization. The authors propose a binary-coding quantization (BCQ) format to represent both uniform and non-uniform weight quantization, enabling a flexible trade-off between compression ratio and accuracy. LUT-GEMM leverages the BCQ format to construct lookup tables that accelerate matrix multiplication, reducing computational costs compared to traditional methods. The authors demonstrate that LUT-GEMM achieves a 2.1× speedup over OPTQ on a single GPU while maintaining comparable accuracy.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

- The paper is well-written and easy to follow.
- The proposed method is simple and easy to implement.
- The authors provide a comprehensive experimental evaluation of LUT-GEMM across various model sizes and quantization levels, demonstrating its effectiveness in accelerating inference.

### Weaknesses

#### Some Related Works


#### comment

 - The paper lacks a detailed discussion of the limitations of the proposed method. For example, how does the method perform on different model architectures or under varying hardware configurations? Specifically, the paper does not address the impact of the proposed method on models with different layer types (e.g., attention layers, feed-forward layers) or activation functions. Furthermore, the evaluation is limited to a single GPU, and it is unclear how the method would scale to multi-GPU setups or different hardware platforms.
- The authors should provide a more thorough comparison with existing quantization methods, such as GPTQ, to highlight the advantages and disadvantages of the proposed method. The comparison should not only focus on latency but also consider other factors such as memory footprint, computational overhead, and ease of implementation. A more detailed analysis of the trade-offs between LUT-GEMM and other quantization techniques is needed to fully understand its advantages and limitations.
- The paper does not discuss the potential impact of the proposed method on the overall system performance, including memory bandwidth and inter-GPU communication. The evaluation should include a more comprehensive analysis of the memory usage and communication overhead associated with LUT-GEMM, especially when scaling to larger models or multi-GPU setups. It is unclear how the proposed method would interact with other system-level optimizations and whether it would introduce any bottlenecks.

### Suggestions

The paper would benefit from a more thorough investigation into the limitations of the proposed LUT-GEMM method. Specifically, the authors should evaluate the performance of LUT-GEMM on a wider range of model architectures, including those with different layer types and activation functions. For example, it would be valuable to see how LUT-GEMM performs on models with complex layer structures, such as those found in Vision Transformers or other specialized architectures. Additionally, the authors should explore the impact of different hardware configurations, such as multi-GPU setups or different CPU architectures, on the performance of LUT-GEMM. This would provide a more comprehensive understanding of the method's applicability and scalability. Furthermore, the authors should investigate the sensitivity of LUT-GEMM to different quantization levels and provide guidelines for selecting the optimal quantization parameters for different model sizes and hardware platforms. This would help practitioners to effectively utilize LUT-GEMM in their applications.

To strengthen the paper, the authors should provide a more detailed comparison with existing quantization methods, such as GPTQ, AWQ, and others. This comparison should not only focus on latency but also consider other factors such as memory footprint, computational overhead, and ease of implementation. The authors should provide a quantitative analysis of the trade-offs between LUT-GEMM and other quantization techniques, highlighting the specific scenarios where LUT-GEMM is most advantageous. For example, it would be valuable to see how LUT-GEMM compares to other methods in terms of memory usage for storing lookup tables and intermediate results, as well as the computational cost of constructing and accessing these tables. The authors should also discuss the potential challenges of implementing LUT-GEMM in real-world applications, such as the overhead of constructing and accessing lookup tables, and provide recommendations for mitigating these challenges. A more comprehensive comparison would help readers understand the advantages and limitations of LUT-GEMM in the context of existing quantization techniques.

Finally, the paper should include a more detailed analysis of the potential impact of LUT-GEMM on the overall system performance. This should include a quantitative evaluation of the memory bandwidth and inter-GPU communication overhead associated with LUT-GEMM, especially when scaling to larger models or multi-GPU setups. The authors should also discuss how LUT-GEMM interacts with other system-level optimizations, such as memory management and data transfer, and whether it introduces any bottlenecks. For example, the authors should analyze the impact of LUT-GEMM on the memory access patterns and how this affects the overall performance of the system. Furthermore, the authors should provide recommendations for optimizing the implementation of LUT-GEMM to minimize its impact on system performance. This would help practitioners to effectively utilize LUT-GEMM in their applications and understand its potential limitations.

### Questions

- How does the proposed method perform on different model architectures or under varying hardware configurations?
- How does LUT-GEMM compare with other quantization methods in terms of memory footprint, computational overhead, and ease of implementation?
- What is the potential impact of LUT-GEMM on the overall system performance, including memory bandwidth and inter-GPU communication?

### Rating

6

### Confidence

4

**********
