### Summary

This paper introduces FAVICOMP (Familiarity-aware Evidence Compression), a training-free method designed to enhance retrieval-augmented generation (RAG) by making retrieved evidence more familiar to the target model while integrating its parametric knowledge. The key innovation is using ensemble decoding to lower the target model’s perplexity by combining decoding probabilities from both the compression and target models, resulting in better alignment of the compressed evidence with the target model. The method balances evidence and parametric knowledge, improving performance on complex tasks where retrieved evidence may be incomplete or noisy. Experimental results show that FAVICOMP outperforms existing evidence compression baselines across multiple open-domain QA datasets, demonstrating high compression rates and significant accuracy improvements.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper is well-structured and clearly written, with a logical flow that makes it easy to follow the proposed method and its rationale. The use of figures and tables effectively illustrates the concepts and results, enhancing clarity and accessibility.
2. The proposed method is both effective and straightforward, offering a novel approach to evidence compression that leverages ensemble decoding to integrate both compression and target model knowledge. This approach is particularly useful in complex tasks where retrieved evidence may be incomplete or noisy, and it achieves impressive results across multiple datasets.
3. The paper demonstrates the effectiveness of FAVICOMP through comprehensive experiments on several open-domain QA datasets. The results show that FAVICOMP outperforms existing evidence compression baselines, achieving up to 23.91% accuracy improvement while maintaining high compression rates. This highlights the practical value of the method in real-world applications.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed analysis of the computational cost associated with FAVICOMP, which could be a concern for practical applications. Specifically, the overhead of the ensemble decoding process, including the number of forward passes required and the associated latency, is not thoroughly investigated. This lack of analysis makes it difficult to assess the method's feasibility in resource-constrained environments. Furthermore, the memory footprint of maintaining and updating the ensemble of models should also be considered.
2. While the paper demonstrates the effectiveness of FAVICOMP on open-domain QA datasets, it does not explore its performance on other types of tasks, such as summarization or dialogue generation. This limits the generalizability of the findings and raises questions about the method's applicability to different types of retrieval-augmented tasks. It is unclear whether the proposed approach would be equally effective in tasks that require different types of reasoning or information integration.
3. The paper does not provide a comprehensive comparison with other state-of-the-art methods for evidence compression, such as those based on attention mechanisms or knowledge distillation. This makes it difficult to assess the relative advantages and disadvantages of FAVICOMP compared to existing approaches. A more thorough comparison would include methods that use different strategies for compressing and integrating retrieved evidence, allowing for a more nuanced understanding of the proposed method's strengths and weaknesses.

### Suggestions

To address the lack of computational cost analysis, the authors should provide a detailed breakdown of the time and memory requirements of FAVICOMP. This should include the time taken for ensemble decoding, the memory footprint of the ensemble models, and the impact of different ensemble sizes on performance and efficiency. It would be beneficial to compare the computational cost of FAVICOMP with that of other evidence compression methods, providing a clear understanding of the trade-offs between accuracy and efficiency. Furthermore, the authors should investigate the scalability of the method with respect to the size of the retrieved evidence and the complexity of the target model. This analysis should include experiments with varying numbers of retrieved documents and different model sizes to determine the practical limits of the method.

To enhance the generalizability of the findings, the authors should evaluate FAVICOMP on a wider range of tasks beyond open-domain QA. This could include tasks such as summarization, dialogue generation, and code generation. Such evaluations would provide a more comprehensive understanding of the method's applicability and limitations. For example, in summarization tasks, the authors could assess how well FAVICOMP integrates retrieved documents with the target model's internal knowledge to generate coherent and informative summaries. In dialogue generation, the authors could evaluate how effectively FAVICOMP incorporates retrieved context to improve the coherence and relevance of the generated dialogues. These additional experiments would provide a more robust assessment of the method's versatility.

Finally, the authors should conduct a more comprehensive comparison with other state-of-the-art evidence compression methods. This comparison should include methods that use different strategies for compressing and integrating retrieved evidence, such as those based on attention mechanisms or knowledge distillation. The comparison should not only focus on accuracy but also on other relevant metrics such as computational cost, memory footprint, and robustness to noisy evidence. The authors should also discuss the specific advantages and disadvantages of FAVICOMP compared to these alternative methods, providing a clear understanding of the method's strengths and weaknesses in different scenarios. This would allow readers to better understand the relative performance of FAVICOMP and its potential for practical applications.

### Questions

See the weakness.

### Rating

5

### Confidence

3

**********
