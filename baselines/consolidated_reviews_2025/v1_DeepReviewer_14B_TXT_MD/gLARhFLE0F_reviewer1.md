### Summary

This paper introduces LUT-GEMM, an efficient kernel for quantized matrix multiplication that eliminates the resource-intensive dequantization process and reduces computational costs. It utilizes an extended BCQ format to support both uniform and non-uniform quantization methods. The proposed method offers a flexible trade-off between compression ratio and accuracy. LUT-GEMM is implemented on GPUs and achieves significant speed-up compared to existing methods like cuBLAS, OPTQ, and AWQ.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

The authors propose LUT-GEMM, a novel quantization method that supports both uniform and non-uniform quantization methods using an extended BCQ format.

The authors demonstrate that LUT-GEMM offers a broad spectrum of latency and accuracy trade-offs.

The authors show that LUT-GEMM can considerably accelerate matrix multiplications with small quantization bits and reduce power consumption by reducing the number of GPUs needed.

### Weaknesses

#### Some Related Works


#### comment

The proposed LUT-GEMM method is not thoroughly compared to existing quantization methods. A comprehensive comparison is needed to evaluate the effectiveness of the proposed method against the state-of-the-art.

The evaluation of LUT-GEMM is primarily conducted on a single batch size, which may not be representative of real-world scenarios. Evaluating the method on various batch sizes would provide a more comprehensive understanding of its performance.

The paper lacks a detailed analysis of the impact of different quantization bits on the accuracy of the proposed method. It is important to investigate how the choice of quantization bits affects the accuracy of LUT-GEMM.

The authors should provide a more detailed explanation of the implementation details of LUT-GEMM on GPUs, including the choice of hyperparameters and their impact on performance.

### Suggestions

The paper would benefit significantly from a more rigorous comparison against existing quantization techniques, particularly those focused on reducing memory bandwidth and computational costs in large language models (LLMs). While the authors mention comparisons to cuBLAS, OPTQ, and AWQ, a deeper analysis is needed to understand the specific advantages and disadvantages of LUT-GEMM in relation to these methods. For instance, a direct comparison of memory footprint, FLOPs, and actual runtime latency against methods like GPTQ and other state-of-the-art quantization techniques for LLMs would provide a more comprehensive picture of LUT-GEMM's performance. This comparison should not only focus on overall latency but also on the breakdown of time spent in different stages of the computation, such as dequantization (if applicable), matrix multiplication, and quantization. Furthermore, the comparison should include a variety of model sizes and architectures to demonstrate the generalizability of the proposed method. A more detailed analysis of the trade-offs between compression ratio, accuracy, and computational cost is crucial for understanding the practical applicability of LUT-GEMM.

To strengthen the evaluation, the authors should conduct experiments across a wider range of batch sizes. The current evaluation on a single batch size limits the understanding of how LUT-GEMM performs under different memory and compute conditions. In real-world scenarios, batch sizes can vary significantly, and it is important to demonstrate that LUT-GEMM can maintain its performance advantages across these variations. Specifically, the authors should investigate how the memory utilization and computational efficiency of LUT-GEMM change with increasing batch sizes. This analysis should include a discussion of the limitations of the proposed method, such as the observed decrease in memory utilization with larger batch sizes. It would also be beneficial to explore the impact of different batch sizes on the accuracy of the model, as this can be a critical factor in practical applications. The authors should also consider the impact of different hardware configurations, such as the number of GPUs, on the performance of LUT-GEMM with varying batch sizes.

Finally, a more detailed analysis of the impact of different quantization bits on the accuracy of LUT-GEMM is essential. The paper should include a systematic study of how the choice of quantization bits affects the accuracy of the model across different layers and different model architectures. This analysis should not only focus on the overall accuracy but also on the per-layer accuracy and the impact on specific tasks. The authors should also investigate the trade-offs between accuracy and computational cost for different quantization bits. This analysis should include a discussion of the optimal quantization bit selection for different layers and different model architectures. Furthermore, the authors should provide a detailed explanation of the implementation details of LUT-GEMM on GPUs, including the choice of hyperparameters and their impact on performance. This should include a discussion of the thread configurations, memory access patterns, and the use of shared memory. A more detailed analysis of the computational complexity of LUT-GEMM and its dependence on the quantization bits and other hyperparameters would also be beneficial.

### Questions

In the paper, the authors mention that LUT-GEMM is primarily designed for single-batch inference. How does the method perform with larger batch sizes, and is there a potential to extend its application to multi-batch scenarios?

The paper mentions that the memory utilization of LUT-GEMM decreases as the batch size increases. Can the authors provide an explanation for this behavior and discuss its implications for practical applications?

How does the computational complexity of LUT-GEMM compare to existing quantization methods, and how does it vary with the choice of quantization bits and other hyperparameters?

The paper mentions that the optimal quantization bit selection is layer-wise. How is the optimal quantization bit determined for each layer, and what is the impact of suboptimal quantization bit selection on the performance of the proposed method?

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
