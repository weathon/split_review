### Summary

This paper proposes a new method for LLM weight-only quantization. The authors first observe that activation outliers correspond to sensitive weights, where large activations can amplify rounding errors. This insight motivates the introduction of per-input-channel (per-IC) quantization, which aims to isolate these outlier effects by selecting quantization ranges within each input channel. Building on this, the authors further propose an adaptive per-channel quantization scheme, AdaDim, which selects between per-IC and per-output-channel (per-OC) quantization based on a reconstruction error objective. Experimental results demonstrate that AdaDim improves the performance of both round-to-nearest and GPTQ quantization methods.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

* The paper provides valuable insights by demonstrating that activation outliers tend to occur in specific weight channels, thereby establishing a connection between activation outliers and weight sensitivity. 
* The authors show that per-IC quantization can help mitigate the impact of outlier effects, which is an interesting observation that can inspire future work. 
* The experiments are thorough and well-presented, offering a clear understanding of the method's effectiveness.

### Weaknesses

#### Some Related Works


#### comment

 * The paper's motivation could be strengthened. While it demonstrates that activation outliers correlate with sensitive weights, it does not fully establish that these outliers are the direct cause of weight sensitivity. More analysis is needed to clarify their relationship and to justify the assumption that outliers are the primary cause of sensitivity.
* The novelty of the per-IC quantization approach is somewhat limited, as it resembles the per-data-sample quantization method described in the GPTQ paper. Additionally, the paper lacks a clear explanation of why per-IC quantization is more hardware-efficient than per-OC.
* The paper's main contribution, AdaDim, is presented as a method that dynamically selects the optimal quantization dimension. However, this selection process introduces additional computational overhead, which the paper does not adequately address.

### Suggestions

To strengthen the paper, the authors should provide a more detailed analysis of the relationship between activation outliers and weight sensitivity. This could involve conducting experiments where the activation outliers are selectively removed or amplified, and then observing the impact on weight sensitivity. For example, the authors could apply techniques such as clipping or smoothing to the activations and then measure the resulting changes in weight sensitivity. This would help to isolate the specific contribution of outliers and provide a more robust justification for the proposed method. Furthermore, the authors should explore other potential causes of weight sensitivity, such as the distribution of weights themselves or the specific operations performed in the network. A more comprehensive analysis would help to establish the novelty and significance of the proposed approach.

Regarding the per-IC quantization, the authors should provide a more detailed comparison with per-data-sample quantization, highlighting the specific differences and advantages of their approach. A more thorough discussion of the hardware efficiency claims is also needed. The authors should provide a quantitative analysis of the memory access patterns and computational costs associated with both per-IC and per-OC quantization, as well as a comparison with per-data-sample quantization. This analysis should include a discussion of the potential for parallelization and the impact of different group sizes on performance. Furthermore, the authors should clarify the specific hardware platforms for which per-IC quantization is most suitable and discuss the potential limitations of the approach on different architectures. This would help to establish the practical relevance of the proposed method.

Finally, the authors should provide a more detailed analysis of the computational cost of the AdaDim search process. This should include a breakdown of the time required for each step of the search, as well as a discussion of the potential for this search to become a bottleneck in the quantization process. The authors should also explore alternative search strategies that could reduce the computational overhead of AdaDim. For example, they could consider using a heuristic approach to guide the search or using a simplified model to estimate the reconstruction error. A more thorough analysis of the trade-offs between accuracy and computational cost would be beneficial in assessing the practical viability of AdaDim.

### Questions

1. Could the authors provide more analysis to demonstrate that activation outliers are a primary cause of weight sensitivity, rather than just correlated with it?
2. Could the authors clarify the difference between per-IC quantization and per-data-sample quantization from the GPTQ paper, and provide a more detailed justification for the hardware efficiency claims?
3. Could the authors discuss the computational overhead introduced by the dimension search in AdaDim and its impact on the overall quantization process?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
