### Summary

This paper presents LUT-GEMM, a kernel designed to accelerate inference in large language models by utilizing quantized weights without dequantization. The authors introduce an efficient implementation of matrix multiplication that leverages binary-coded quantization (BCQ) to reduce computational overhead. The proposed kernel is claimed to achieve a 2.1x speedup over existing methods like OPTQ while maintaining low memory usage and minimal communication overhead, making it suitable for large-scale models.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper introduces an efficient binary-coded quantization (BCQ) format that supports both uniform and non-uniform quantization, offering flexibility in the compression ratio and accuracy trade-off.

2. The proposed LUT-GEMM kernel eliminates the need for dequantization, which is a common bottleneck in quantized matrix multiplication, resulting in significant speed improvements.

3. The authors provide experimental results demonstrating that LUT-GEMM can accelerate token generation latency by 2.1x compared to OPTQ, while also reducing memory usage and communication overhead.

### Weaknesses

#### Some Related Works


#### comment

1. While the paper claims that LUT-GEMM reduces memory footprint, it lacks a detailed analysis of memory usage compared to other quantization methods, such as GPTQ or AWQ. Specifically, the paper does not provide a breakdown of memory consumption for weights, activations, and other data structures, making it difficult to assess the practical benefits of the proposed approach in resource-constrained environments. A more thorough comparison, including memory usage for different model sizes and quantization levels, is needed to fully evaluate the memory efficiency of LUT-GEMM.

2. The paper does not thoroughly discuss the limitations of the proposed method, such as its applicability to different model architectures or its performance under varying hardware configurations. The evaluation is primarily focused on OPT-175B, and it is unclear how the method would perform on models with different architectural characteristics, such as those with varying layer types or activation functions. Furthermore, the paper does not explore the impact of different hardware platforms, such as GPUs with varying memory bandwidth or CPU architectures, on the performance of LUT-GEMM.

3. The paper does not provide a comprehensive comparison with other state-of-the-art quantization techniques, such as AWQ or GPTQ, in terms of both performance and efficiency. While the paper compares LUT-GEMM with OPTQ, it does not provide a detailed analysis of how LUT-GEMM compares to other advanced quantization methods in terms of accuracy, latency, and memory usage. A more comprehensive comparison, including a wider range of models and quantization levels, is needed to fully evaluate the advantages and disadvantages of LUT-GEMM.

### Suggestions

The paper would benefit significantly from a more detailed analysis of memory usage. The authors should provide a breakdown of memory consumption for different components of the model, such as weights, activations, and intermediate results, and compare these with other quantization methods like GPTQ and AWQ. This analysis should include a discussion of how memory usage scales with model size and quantization level. For example, the authors could present a table showing memory usage for different model sizes (e.g., 1B, 3B, 10B parameters) and quantization levels (e.g., 2-bit, 4-bit, 8-bit). This would allow readers to better understand the practical benefits of LUT-GEMM in resource-constrained environments. Furthermore, the authors should discuss the memory overhead of storing the lookup tables (LUTs) used in the proposed method and how this overhead compares to the memory savings achieved through quantization.

To address the limitations regarding model architecture and hardware, the authors should conduct experiments on a wider range of models and hardware platforms. This should include models with different architectural characteristics, such as those with varying layer types (e.g., attention layers, feed-forward layers) and activation functions. The authors should also evaluate the performance of LUT-GEMM on different hardware platforms, such as GPUs with varying memory bandwidth (e.g., NVIDIA A100, NVIDIA V100, AMD Radeon Instinct MI50) and CPUs with different architectures. This would provide a more comprehensive understanding of the applicability of LUT-GEMM in different scenarios. The authors should also discuss any hardware-specific optimizations that were implemented to improve the performance of LUT-GEMM.

Finally, the paper needs a more comprehensive comparison with other state-of-the-art quantization techniques. The authors should compare LUT-GEMM with other advanced quantization methods, such as AWQ and GPTQ, in terms of both performance and efficiency. This comparison should include a wider range of models and quantization levels, and should consider different evaluation metrics, such as accuracy, latency, and memory usage. The authors should also discuss the trade-offs between different quantization methods and provide guidance on when LUT-GEMM is most suitable. For example, the authors could discuss the specific scenarios where LUT-GEMM outperforms other methods and vice versa. This would allow readers to better understand the advantages and disadvantages of LUT-GEMM and make informed decisions about which quantization method to use for their specific applications.

### Questions

1. How does the proposed LUT-GEMM kernel perform on different hardware platforms, such as GPUs with varying memory bandwidth or CPUs with different architectures? Are there any specific optimizations or considerations for different hardware configurations?

2. Can the authors provide a more detailed comparison of LUT-GEMM with other state-of-the-art quantization techniques, such as AWQ or GPTQ, in terms of both performance and efficiency? Specifically, how does LUT-GEMM compare in terms of accuracy, latency, and memory usage across different model sizes and quantization levels?

3. What are the limitations of LUT-GEMM in terms of its applicability to different model architectures or its performance under varying hardware configurations? Are there any specific scenarios where LUT-GEMM might not be the most suitable choice?

### Rating

6

### Confidence

4

**********
