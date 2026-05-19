### Summary

This paper proposes a new approach to accelerate the inference of large language models (LLMs) by using a lookup table (LUT) based GEMM kernel. The key idea is to represent the quantized weights as a sum of binary vectors with scaling factors and a bias term, and then use a LUT to precompute the partial products of the GEMM operation. This way, the LUT-GEMM kernel can avoid the costly dequantization step and reduce the computational complexity. The authors show that the LUT-GEMM kernel can achieve a 2.1x speedup over OPTQ on the OPT-175B model with 3-bit quantization, while maintaining a similar perplexity. The authors also demonstrate the flexibility of the LUT-GEMM kernel by showing that it can support both uniform and non-uniform quantization methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper proposes a novel approach to accelerate the inference of LLMs by using a LUT based GEMM kernel. The LUT-GEMM kernel can avoid the costly dequantization step and reduce the computational complexity, which can lead to significant speedups and energy savings.
- The paper shows that the LUT-GEMM kernel can achieve a 2.1x speedup over OPTQ on the OPT-175B model with 3-bit quantization, while maintaining a similar perplexity. This demonstrates the effectiveness of the proposed approach in practice.
- The paper demonstrates the flexibility of the LUT-GEMM kernel by showing that it can support both uniform and non-uniform quantization methods. This allows the LUT-GEMM kernel to be applied to various quantization techniques and achieve optimal trade-offs between accuracy and efficiency.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a detailed analysis of the memory overhead of the LUT-GEMM kernel. The LUT-GEMM kernel requires storing the LUT in the GPU memory, which can increase the memory footprint and limit the scalability of the approach. The paper should provide a quantitative analysis of the LUT size and its impact on the overall memory usage, especially for larger models and different quantization levels. It is unclear how the LUT size scales with the number of quantization bits and the size of the weight matrices, and this needs to be addressed.
- The paper does not compare the LUT-GEMM kernel with other state-of-the-art GEMM kernels for LLM inference, such as cuBLAS or other optimized libraries. The paper should provide a more comprehensive comparison of the LUT-GEMM kernel with other existing solutions to demonstrate its advantages and disadvantages. This comparison should include not only latency but also memory usage and energy consumption, and should be performed across a range of model sizes and quantization levels.

### Suggestions

The paper should include a detailed analysis of the memory overhead associated with the LUT-GEMM kernel. Specifically, the authors should provide a breakdown of the LUT size for different quantization levels (e.g., 2-bit, 3-bit, 4-bit) and different weight matrix sizes. This analysis should also consider the impact of the LUT size on the overall memory footprint of the model, especially when considering large language models. It would be beneficial to include a graph showing how the LUT size scales with the number of quantization bits and the size of the weight matrices. Furthermore, the authors should discuss the trade-offs between LUT size, memory usage, and performance, and provide guidelines on how to choose the optimal LUT size for different scenarios. This analysis should also consider the impact of the LUT on the cache performance of the GPU, as a large LUT may lead to cache misses and reduce the overall performance.

To strengthen the paper, a more comprehensive comparison with existing GEMM kernels is needed. The authors should compare the LUT-GEMM kernel with other state-of-the-art GEMM kernels, such as cuBLAS, and other optimized libraries for LLM inference. This comparison should include not only latency but also memory usage and energy consumption. The comparison should be performed across a range of model sizes and quantization levels. It would be beneficial to include a table summarizing the performance of different GEMM kernels across different model sizes and quantization levels. The authors should also discuss the limitations of the LUT-GEMM kernel compared to other existing solutions, and provide guidelines on when to use the LUT-GEMM kernel and when to use other existing solutions. This comparison should also consider the impact of different hardware architectures on the performance of different GEMM kernels.

Finally, the paper should provide more details on the implementation of the LUT-GEMM kernel. Specifically, the authors should discuss the data structures used to store the LUT, and the algorithms used to access the LUT. The authors should also discuss the optimization techniques used to improve the performance of the LUT-GEMM kernel, such as memory access patterns and loop unrolling. It would be beneficial to include a pseudocode of the LUT-GEMM kernel to help the reader understand the implementation details. The authors should also discuss the limitations of the current implementation and suggest potential future directions for improving the performance of the LUT-GEMM kernel.

### Questions

- How does the memory overhead of the LUT-GEMM kernel compare to other GEMM kernels for LLM inference?
- How does the LUT-GEMM kernel perform on different hardware platforms, such as CPUs or TPUs?
- How does the LUT-GEMM kernel handle the non-linear operations in LLMs, such as softmax and normalization?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
