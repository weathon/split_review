### Summary

This paper proposes a LUT-GEMM algorithm to accelerate GEMM with quantized weight and full precision activations. The weight is quantized with an extension of binary-coding quantization (BCQ). The authors show that BCQ is capable of representing both uniform and non-uniform weight quantization. LUT-GEMM using the BCQ format can eliminate the dequantization process and achieve low latency. The authors show that LUT-GEMM can accelerate token generation latency for LLMs.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

+ The proposed LUT-GEMM algorithm is able to use GPU-specific hardware to accelerate GEMM with quantized weights and full precision activations. 
+ The authors extend the BCQ format to support both non-uniform and uniform quantization methods. The proposed LUT-GEMM algorithm can be applied to different quantization methods.
+ The authors show that LUT-GEMM can accelerate the token generation latency for LLMs.

### Weaknesses

#### Some Related Works


#### comment

 - The authors only show the inference latency for the OPT models. It is not clear how much the inference latency can be reduced for the state-of-the-art LLMs, e.g., LLaMA-2. More experiments for the recent LLMs should be conducted.
- The authors only show the perplexity for the OPT-175B model. It is not clear how the perplexity will be affected for other LLMs. More experiments for the recent LLMs should be conducted.
- The authors only show the perplexity of the proposed LUT-GEMM for 3-bit and 4-bit quantization. It is not clear how the perplexity will be affected for lower bit quantization, e.g., 2-bit. More experiments for lower bit quantization should be conducted.
- The authors only show the perplexity of the proposed LUT-GEMM for row-wise quantization. It is not clear how the perplexity will be affected for other quantization methods, e.g., the proposed AWQ method. More experiments for lower bit quantization should be conducted.

### Suggestions

The paper would benefit significantly from a more comprehensive evaluation of the proposed LUT-GEMM algorithm across a wider range of large language models (LLMs). While the OPT model is a reasonable starting point, the field has rapidly advanced, and it is crucial to demonstrate the effectiveness of LUT-GEMM on more recent and widely adopted models such as LLaMA-2 and similar architectures. The current evaluation focuses solely on the OPT-175B model for perplexity, which limits the generalizability of the findings. It is essential to include perplexity results for other LLMs to understand how the proposed method affects model accuracy across different architectures and scales. Furthermore, the evaluation should extend beyond 3-bit and 4-bit quantization to explore the performance of LUT-GEMM at lower bit-widths, such as 2-bit quantization, which is of significant interest for reducing memory footprint and computational cost. This would provide a more complete picture of the trade-offs between latency and accuracy achievable with the proposed method. 

To further strengthen the paper, the authors should conduct a more thorough investigation into the impact of different quantization techniques on the performance of LUT-GEMM. The current evaluation is limited to row-wise quantization, and it is unclear how the proposed method interacts with other quantization strategies, such as the AWQ method. It is important to compare the performance of LUT-GEMM with different quantization methods to understand its versatility and limitations. This would involve not only reporting perplexity but also analyzing the computational overhead and memory requirements associated with each quantization technique. Such an analysis would provide valuable insights into the practical applicability of LUT-GEMM in different scenarios and help identify the most suitable quantization strategies for various LLMs. The authors should also consider exploring the impact of different group sizes on the performance of LUT-GEMM, as this parameter can significantly affect both latency and accuracy.

Finally, the paper should include a more detailed analysis of the computational complexity and memory footprint of the proposed LUT-GEMM algorithm. While the authors mention that LUT-GEMM can achieve a computational savings, a more rigorous analysis of the algorithm's complexity would be beneficial. This analysis should include a breakdown of the computational cost associated with different steps of the algorithm, such as the LUT generation and the matrix multiplication. Furthermore, the authors should provide a detailed analysis of the memory requirements of LUT-GEMM, including the size of the LUTs and the memory needed to store the quantized weights. This analysis would help to understand the scalability of the proposed method and its suitability for different hardware platforms. The authors should also discuss the potential limitations of the proposed method, such as the overhead associated with LUT generation and the impact of quantization on model accuracy.

### Questions

How much the inference latency can be reduced for the state-of-the-art LLMs, e.g., LLaMA-2?

How the perplexity will be affected for other LLMs?

How the perplexity will be affected for lower bit quantization, e.g., 2-bit?

How the perplexity will be affected for other quantization methods, e.g., the proposed AWQ method?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
