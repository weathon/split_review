### Summary

This paper proposes a magnitude-based pruning approach, WANDA, that prunes weights based on the product of their magnitude and the norm of the corresponding input activations. The method is evaluated on LLaMA and LLaMA-2 models and sparsity levels of 50% , 4:8 and 2:4. At these sparsity levels, WANDA is shown to outperform magnitude pruning and is competitive with the stronger baseline of SparseGPT.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

Pruning LLMs is an important problem and the proposed method is a strong baseline that is easy to implement and much less computationally intensive than SparseGPT. The experiments are comprehensive and provide a number of useful insights.

### Weaknesses

#### Some Related Works


#### comment

It is not clear why WANDA works better than magnitude pruning. According to the discussion in the introduction, the motivation for WANDA is that it takes into account the input activations which could play an important role as weight magnitudes in determining the neuron output. However, there is no analysis to support this claim. Further, the comparison group of weights is also a crucial component of WANDA. The fact that pruning should be done per output is surprising and also not analyzed. The paper also does not discuss the limitations of the proposed approach.

The paper is organized such that the main experiments are presented in section 4 and the analysis is presented in section 5. It would be more appropriate to present the analysis before the experiments.

### Suggestions

The paper would benefit from a more thorough investigation into why WANDA outperforms magnitude pruning. The current explanation, that WANDA considers input activations, is insufficient without supporting analysis. Specifically, the paper should include visualizations or quantitative analysis demonstrating how the product of weight magnitude and input activation norm correlates with the importance of a weight. For example, the authors could show the distribution of weights pruned by magnitude pruning versus WANDA, and analyze the impact of these pruned weights on the output of the layer. This analysis should be done across different layers and model sizes to understand the consistency of the effect. Furthermore, the paper should explore the sensitivity of WANDA to different activation functions and layer types. It is possible that the effectiveness of WANDA is dependent on these factors, and this should be investigated.

The choice of the comparison group as a crucial component of WANDA also requires more justification. The paper states that pruning should be done per output, but this is not intuitive and lacks a clear explanation. The authors should provide a detailed analysis of why per-output pruning is superior to other comparison group strategies, such as per-input or per-layer. This analysis should include experiments that compare the performance of WANDA with different comparison groups. The paper should also discuss the potential limitations of per-output pruning, such as the possibility of removing important connections that are shared across multiple outputs. A more thorough investigation into the impact of different comparison groups would strengthen the paper's claims and provide a better understanding of the method's behavior.

Finally, the paper should include a more detailed discussion of the limitations of WANDA. While the paper mentions that WANDA is not as effective as SparseGPT at very high sparsity levels, it does not explore the reasons for this. The authors should investigate why WANDA's performance degrades at higher sparsity levels and discuss the potential limitations of the method in these scenarios. For example, it is possible that the approximation of the Hessian diagonal becomes less accurate at higher sparsity levels, leading to suboptimal pruning decisions. The paper should also discuss the computational cost of WANDA compared to other pruning methods, and the potential for optimizing the implementation. A more thorough discussion of the limitations would provide a more balanced view of the method and help guide future research.

### Questions

1. Why does WANDA work better than magnitude pruning?
2. Why should the comparison group of weights be a crucial component of WANDA?
3. Is WANDA more effective for some tasks/languages than others?
4. How does WANDA perform at higher sparsity levels (> 50%)?
5. Does WANDA work for other models such as GPT,BERT etc.?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
