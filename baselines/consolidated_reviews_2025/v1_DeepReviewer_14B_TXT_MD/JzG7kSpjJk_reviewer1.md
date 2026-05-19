### Summary

This paper presents a method for LLM weight-only quantization. The authors begin by observing that activation outliers correspond to sensitive weights, where large activations can amplify rounding errors. This insight motivates the introduction of per-input-channel (per-IC) quantization, which aims to isolate these outlier effects by selecting quantization ranges within each input channel. Building on this, the authors further propose an adaptive per-channel quantization scheme, AdaDim, which selects between per-IC and per-output-channel (per-OC) quantization based on a reconstruction error objective. Experimental results demonstrate that AdaDim improves the performance of both round-to-nearest and GPTQ quantization methods. While the paper offers valuable insights into the connection between activation outliers and weight sensitivity, several limitations remain, which I will discuss in the following sections.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

* The paper provides valuable insights by demonstrating that activation outliers tend to occur in specific weight channels, thereby establishing a connection between activation outliers and weight sensitivity. 
* The authors show that per-IC quantization can help mitigate the impact of outlier effects, which is an interesting observation that can inspire future work. 
* The experiments are thorough and well-presented, offering a clear understanding of the method's effectiveness.

### Weaknesses

#### Some Related Works


#### comment

 * The paper's motivation could be strengthened. While it demonstrates that activation outliers correlate with sensitive weights, it does not fully establish that these outliers are the direct cause of weight sensitivity. More analysis is needed to clarify their relationship and to justify the assumption that outliers are the primary cause of sensitivity. For instance, the paper does not explore other potential causes of weight sensitivity, such as the distribution of weights themselves or the specific operations performed in the network. A more rigorous analysis, perhaps involving controlled experiments where outlier effects are selectively removed or amplified, would be beneficial to isolate the impact of outliers on weight sensitivity.
* The novelty of the per-IC quantization approach is somewhat limited, as it resembles the per-data-sample quantization method described in the GPTQ paper. The paper does not adequately address the practical implications of per-IC quantization, particularly regarding its hardware efficiency. The claim that per-IC quantization is more hardware-efficient than per-OC requires more detailed justification, especially considering the potential for increased memory access overhead due to the finer granularity of quantization ranges. A more thorough discussion of the trade-offs between accuracy and hardware efficiency is needed.
* The paper's main contribution, AdaDim, is presented as a method that dynamically selects the optimal quantization dimension. However, this selection process introduces additional computational overhead, which the paper does not adequately address. The lack of a detailed analysis of the computational cost of this search, including the time required for the reconstruction error calculation, makes it difficult to assess the practical viability of AdaDim. Furthermore, the paper does not discuss the potential for this search to become a bottleneck in the quantization process, especially for very large models.

### Suggestions

To strengthen the paper, the authors should provide a more detailed analysis of the relationship between activation outliers and weight sensitivity. This could involve conducting experiments where the activation outliers are selectively removed or amplified, and then observing the impact on weight sensitivity. For example, the authors could apply techniques such as clipping or smoothing to the activations and then measure the resulting changes in weight sensitivity. This would help to isolate the specific contribution of outliers and provide a more robust justification for the proposed method. Furthermore, the authors should explore other potential causes of weight sensitivity, such as the distribution of weights themselves or the specific operations performed in the network, to provide a more comprehensive understanding of the phenomenon.

The authors should also provide a more thorough discussion of the practical implications of per-IC quantization, particularly regarding its hardware efficiency. This should include a detailed analysis of the memory access patterns and computational overhead associated with per-IC quantization, compared to per-OC quantization. The authors should also discuss the potential for increased memory access overhead due to the finer granularity of quantization ranges. A more detailed comparison of the hardware requirements of per-IC and per-OC quantization, including memory bandwidth and computational complexity, would be beneficial. Additionally, the authors should clarify the specific hardware platforms for which per-IC quantization is most suitable and discuss the potential limitations of the approach on different architectures.

Finally, the authors should provide a more detailed analysis of the computational cost of the AdaDim search process. This should include a breakdown of the time required for each step of the search, as well as a discussion of the potential for this search to become a bottleneck in the quantization process. The authors should also explore alternative search strategies that could reduce the computational overhead of AdaDim. For example, they could consider using a heuristic approach to guide the search or using a simplified model to estimate the reconstruction error. A more thorough analysis of the trade-offs between accuracy and computational cost would be beneficial in assessing the practical viability of AdaDim.

### Questions

* Could the authors provide more analysis to demonstrate that activation outliers are a primary cause of weight sensitivity, rather than just correlated with it?
* Could the authors clarify the difference between per-IC quantization and per-data-sample quantization from the GPTQ paper, and provide a more detailed justification for the hardware efficiency claims?
* Could the authors discuss the computational overhead introduced by the dimension search in AdaDim and its impact on the overall quantization process?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
