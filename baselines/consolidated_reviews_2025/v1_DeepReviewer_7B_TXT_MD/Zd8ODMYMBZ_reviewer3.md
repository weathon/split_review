### Summary

The paper proposes FAVICOMP (Familiarity-aware Evidence Compression), a training-free method to improve retrieval-augmented generation (RAG) by making retrieved evidence more familiar to the target model. FAVICOMP integrates the target model's parametric knowledge with compressed evidence through ensemble decoding, which balances the integration of external and internal knowledge. The method achieves high compression rates and significant accuracy improvements, outperforming recent evidence compression baselines across multiple open-domain QA datasets.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is novel and interesting, and the experimental results are promising.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed analysis of the computational cost associated with FAVICOMP, which could be a concern for practical applications. Specifically, the overhead of the ensemble decoding process, including the number of forward passes required and the associated latency, is not thoroughly investigated. This lack of analysis makes it difficult to assess the method's feasibility in resource-constrained environments. Furthermore, the memory footprint of maintaining and updating the ensemble of models should also be considered.
2. The paper does not compare FAVICOMP with other state-of-the-art methods for evidence compression, such as those based on attention mechanisms or knowledge distillation. This makes it difficult to assess the relative advantages and disadvantages of FAVICOMP compared to existing approaches. A more thorough comparison would include methods that use different strategies for compressing and integrating retrieved evidence, allowing for a more nuanced understanding of the proposed method's strengths and weaknesses.

### Suggestions

The authors should provide a more detailed analysis of the computational cost of FAVICOMP, including a breakdown of the time and memory requirements for different components of the method. This analysis should include a comparison with other evidence compression methods to highlight the trade-offs between accuracy and efficiency. Specifically, the authors should investigate the impact of different ensemble sizes on both performance and computational cost. It would be beneficial to include experiments that measure the latency of the ensemble decoding process, as this is a critical factor for real-world applications. Furthermore, the authors should consider the impact of different decoding strategies on the computational cost and performance of FAVICOMP. For example, they could explore the use of beam search or other optimization techniques to reduce the computational overhead of the ensemble decoding process. 

To strengthen the paper, the authors should conduct a more comprehensive comparison with other state-of-the-art methods for evidence compression. This comparison should include methods that use different strategies for compressing and integrating retrieved evidence, such as those based on attention mechanisms or knowledge distillation. The comparison should not only focus on accuracy but also on other relevant metrics such as computational cost, memory footprint, and robustness to noisy evidence. The authors should also discuss the specific advantages and disadvantages of FAVICOMP compared to these alternative methods. For example, they could analyze the performance of FAVICOMP on datasets with varying levels of noise or complexity. This would provide a more nuanced understanding of the method's strengths and weaknesses and help to identify the scenarios in which it is most effective. 

Finally, the authors should provide a more detailed analysis of the impact of the ensemble coefficient on the performance of FAVICOMP. While they mention that the ensemble coefficient is set to 0.5 by default, they should investigate the sensitivity of the method to different values of this parameter. This analysis should include a discussion of the trade-offs between accuracy and efficiency when using different values of the ensemble coefficient. It would be beneficial to include experiments that explore the use of adaptive ensemble coefficients, which could be adjusted based on the characteristics of the input data. This could potentially lead to further improvements in the performance of FAVICOMP.

### Questions

1. How does FAVICOMP perform on tasks beyond open-domain QA, such as summarization or dialogue generation?
2. What is the computational cost of FAVICOMP compared to other evidence compression methods, and how does it scale with the size of the retrieved evidence and target model?
3. How does FAVICOMP compare to other state-of-the-art methods for evidence compression, such as those based on attention mechanisms or knowledge distillation?

### Rating

6

### Confidence

4

**********
