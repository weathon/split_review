### Summary

This paper introduces FAVICOMP (Familiarity-aware Evidence Compression), a novel training-free method designed to improve retrieval-augmented generation (RAG) by making retrieved evidence more familiar to the target model. FAVICOMP integrates the target model's parametric knowledge with compressed evidence through ensemble decoding, which balances the integration of external and internal knowledge. The method achieves high compression rates and significant accuracy improvements, outperforming recent evidence compression baselines across multiple open-domain QA datasets.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. FAVICOMP is a training-free method that effectively integrates the target model’s parametric knowledge with compressed evidence, enhancing the model's ability to handle complex tasks where retrieved evidence may be incomplete or noisy.
2. The paper presents a comprehensive experimental evaluation of FAVICOMP across multiple open-domain QA datasets, demonstrating its effectiveness and robustness in various scenarios.
3. FAVICOMP achieves high compression rates, making it a practical solution for reducing the computational cost of RAG systems without sacrificing accuracy.

### Weaknesses

#### Some Related Works


#### comment

1. While the paper demonstrates the effectiveness of FAVICOMP on open-domain QA datasets, it does not explore its performance on other types of tasks, such as summarization or dialogue generation. This limits the generalizability of the findings and raises questions about the method's applicability to different types of retrieval-augmented tasks.
2. The paper does not provide a detailed analysis of the computational cost associated with FAVICOMP, which could be a concern for practical applications. Specifically, the overhead of the ensemble decoding process, including the number of forward passes required and the associated latency, is not thoroughly investigated. This lack of analysis makes it difficult to assess the method's feasibility in resource-constrained environments. Furthermore, the memory footprint of maintaining and updating the ensemble of models should also be considered.
3. The paper does not compare FAVICOMP with other state-of-the-art methods for evidence compression, such as those based on attention mechanisms or knowledge distillation. This makes it difficult to assess the relative advantages and disadvantages of FAVICOMP compared to existing approaches. A more thorough comparison would include methods that use different strategies for compressing and integrating retrieved evidence, allowing for a more nuanced understanding of the proposed method's strengths and weaknesses.

### Suggestions

The authors should consider expanding their experimental evaluation to include tasks beyond open-domain question answering. Specifically, exploring the performance of FAVICOMP on tasks such as summarization, dialogue generation, or code generation would provide a more comprehensive understanding of its generalizability. For summarization, the method could be evaluated on datasets like CNN/DailyMail or XSum, assessing how well FAVICOMP integrates retrieved documents with the target model's internal knowledge to generate coherent and informative summaries. In dialogue generation, the authors could test the method's ability to incorporate retrieved context to improve the coherence and relevance of the generated dialogues. These additional experiments would help to establish the broader applicability of FAVICOMP and highlight its potential for use in a wider range of RAG applications. Furthermore, it would be beneficial to analyze the performance of FAVICOMP on tasks with varying levels of complexity and information density to understand its limitations and strengths in different scenarios.

To address the lack of computational cost analysis, the authors should provide a detailed breakdown of the time and memory requirements of FAVICOMP. This analysis should include the time taken for ensemble decoding, the memory footprint of the ensemble models, and the impact of different ensemble sizes on performance and efficiency. It would be beneficial to compare the computational cost of FAVICOMP with that of other evidence compression methods, providing a clear understanding of the trade-offs between accuracy and efficiency. The authors should also investigate the scalability of the method with respect to the size of the retrieved evidence and the complexity of the target model. This analysis should include experiments with varying numbers of retrieved documents and different model sizes to determine the practical limits of the method. Additionally, the authors should consider the impact of different decoding strategies on the computational cost and performance of FAVICOMP.

Finally, the authors should conduct a more comprehensive comparison with other state-of-the-art methods for evidence compression. This comparison should include methods that use different strategies for compressing and integrating retrieved evidence, such as those based on attention mechanisms or knowledge distillation. The comparison should not only focus on accuracy but also on other relevant metrics such as computational cost, memory footprint, and robustness to noisy evidence. The authors should also discuss the specific advantages and disadvantages of FAVICOMP compared to these alternative methods, providing a clear understanding of the method's strengths and weaknesses in different scenarios. This would allow readers to better understand the relative performance of FAVICOMP and its potential for practical applications. The authors should also consider including a discussion of the limitations of their approach and potential avenues for future research.

### Questions

1. How does FAVICOMP perform on tasks beyond open-domain QA, such as summarization or dialogue generation?
2. What is the computational cost of FAVICOMP compared to other evidence compression methods, and how does it scale with the size of the retrieved evidence and target model?
3. How does FAVICOMP compare to other state-of-the-art methods for evidence compression, such as those based on attention mechanisms or knowledge distillation?

### Rating

6

### Confidence

3

**********
