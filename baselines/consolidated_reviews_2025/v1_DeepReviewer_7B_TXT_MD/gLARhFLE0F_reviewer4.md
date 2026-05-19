### Summary

This paper proposes LUT-GEMM, a kernel for efficient matrix multiplication in large language models (LLMs) that utilizes quantized weights without dequantization. The authors introduce an efficient implementation of matrix multiplication that leverages binary-coding quantization (BCQ) to reduce computational costs. The proposed kernel is claimed to achieve a 2.1x speedup over existing methods like OPTQ while maintaining low memory usage and minimal communication overhead, making it suitable for large-scale models.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple and easy to implement.
3. The authors provide a comprehensive experimental evaluation of LUT-GEMM across various model sizes and quantization levels, demonstrating its effectiveness in accelerating inference.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed discussion of the limitations of the proposed method. For example, how does the method perform on different model architectures or under varying hardware configurations? Specifically, the paper does not explore the impact of different layer types (e.g., attention layers, feed-forward layers) or activation functions on the performance of LUT-GEMM. Furthermore, the evaluation is limited to a single GPU, and it is unclear how the method would scale to multi-GPU setups or different hardware platforms. The paper should also discuss the potential impact of the proposed method on models with varying degrees of sparsity or structured patterns in their weight matrices.
2. The authors should provide a more thorough comparison with existing quantization methods, such as GPTQ, to highlight the advantages and disadvantages of the proposed method. The comparison should not only focus on latency but also consider other factors such as memory footprint, computational overhead, and ease of implementation. A more detailed analysis of the trade-offs between LUT-GEMM and other quantization techniques is needed to fully understand its advantages and limitations. For example, the paper should discuss the impact of different quantization levels on the accuracy and efficiency of LUT-GEMM, and compare it with other methods under similar conditions.
3. The paper does not discuss the potential impact of the proposed method on the overall system performance, including memory bandwidth and inter-GPU communication. The evaluation should include a more comprehensive analysis of the memory usage and communication overhead associated with LUT-GEMM, especially when scaling to larger models or multi-GPU setups. It is unclear how the proposed method would interact with other system-level optimizations and whether it would introduce any bottlenecks. The paper should also discuss the potential impact of the proposed method on the overall system performance, including memory bandwidth and inter-GPU communication.

### Suggestions

The paper would benefit from a more thorough investigation into the limitations of the proposed LUT-GEMM method. Specifically, the authors should evaluate the performance of LUT-GEMM on a wider range of model architectures, including those with different layer types (e.g., attention layers, feed-forward layers) and activation functions. This would provide a more comprehensive understanding of the method's applicability and robustness. Furthermore, the evaluation should be extended to include multi-GPU setups and different hardware platforms to assess the scalability of the method. The authors should also discuss the potential impact of the proposed method on models with varying degrees of sparsity or structured patterns in their weight matrices, as these factors can significantly affect the performance of matrix multiplication. A detailed analysis of these limitations would provide a more complete picture of the method's strengths and weaknesses.

To strengthen the paper, the authors should provide a more detailed comparison with existing quantization methods, such as GPTQ and AWQ. This comparison should not only focus on latency but also consider other factors such as memory footprint, computational overhead, and ease of implementation. The authors should provide a quantitative analysis of the trade-offs between LUT-GEMM and other quantization techniques, highlighting the specific scenarios where LUT-GEMM is most advantageous. For example, the paper should discuss the impact of different quantization levels on the accuracy and efficiency of LUT-GEMM, and compare it with other methods under similar conditions. This would provide a more comprehensive understanding of the advantages and limitations of the proposed method. The authors should also discuss the potential impact of different quantization levels on the accuracy and efficiency of LUT-GEMM, and compare it with other methods under similar conditions.

Finally, the paper should include a more detailed analysis of the potential impact of LUT-GEMM on the overall system performance, including memory bandwidth and inter-GPU communication. The evaluation should include a more comprehensive analysis of the memory usage and communication overhead associated with LUT-GEMM, especially when scaling to larger models or multi-GPU setups. It is unclear how the proposed method would interact with other system-level optimizations and whether it would introduce any bottlenecks. The authors should also discuss the potential impact of the proposed method on the overall system performance, including memory bandwidth and inter-GPU communication. This analysis should consider the impact of the proposed method on the overall system performance, including memory bandwidth and inter-GPU communication.

### Questions

Please refer to the weaknesses.

### Rating

6

### Confidence

4

**********
