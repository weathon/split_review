### Summary

This paper introduces a training-free evidence compression technique called FAVICOMP (Familiarity-aware Evidence Compression) for retrieval-augmented generation. FAVICOMP aims to make retrieved evidence more familiar to the target model by integrating parametric knowledge from the model and compressing the evidence in a way that lowers the perplexity of the target model. The approach ensembles the token logits from both the compression model and the target model to generate context that is more familiar to the target model, balancing the integration of parametric and non-parametric knowledge. Experimental results show that FAVICOMP consistently outperforms recent evidence compression baselines across multiple open-domain QA datasets, improving accuracy by up to 23.91% while achieving high compression rates.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel training-free evidence compression technique called FAVICOMP (Familiarity-aware Evidence Compression) that makes retrieved evidence more familiar to the target model by integrating parametric knowledge from the model. This approach balances the integration of parametric and non-parametric knowledge, which is especially helpful in complex tasks where the retrieved evidence set may not contain all the necessary information.
2. The paper is well-written and easy to follow. The authors provide a clear explanation of the proposed method and its motivation. The experimental results are presented in a clear and concise manner, and the authors provide a thorough analysis of the results.

### Weaknesses

#### Some Related Works


#### comment

1. The authors should include a comparison with more advanced retrieval models to demonstrate the effectiveness of their approach. For example, models like [1] could provide a more challenging benchmark. Specifically, the paper lacks comparison against models that utilize more sophisticated retrieval mechanisms beyond simple term matching, such as those employing graph-based methods or learned embeddings for document representation. This limits the assessment of FAVICOMP's performance in scenarios with more complex information needs.
2. The authors should also provide an analysis of the computational cost of their method compared to other approaches. This would help to understand the trade-offs between performance and efficiency. The analysis should include a breakdown of the time spent on different stages of the pipeline, such as retrieval, compression, and generation, to pinpoint the computational bottlenecks of FAVICOMP. Furthermore, the memory footprint of the method should also be considered, especially when dealing with large-scale datasets.
3. The authors should include an analysis of the sensitivity of the method to different hyperparameter settings. This would help to understand the robustness of the approach and provide guidance for practitioners. The paper should explore the impact of key hyperparameters, such as the temperature parameter for the target model, the compression ratio, and the weighting of the parametric and non-parametric knowledge sources. A detailed sensitivity analysis would reveal the optimal operating range for these parameters and their influence on the overall performance.
4. The authors should include an analysis of the impact of the quality of the retrieved evidence on the performance of their method. This would help to understand the limitations of the approach and identify areas for future research. It is crucial to evaluate how FAVICOMP performs when the retrieved documents are noisy, irrelevant, or contain contradictory information. This analysis should also consider the impact of the number of retrieved documents on the final performance, as well as the diversity of the retrieved set.

### Suggestions

To strengthen the evaluation, the authors should include a comparison with more advanced retrieval models that go beyond simple term-based methods. Specifically, models that utilize graph-based representations of documents or learned embeddings for retrieval should be considered. This would provide a more comprehensive understanding of FAVICOMP's performance in scenarios with complex information needs and demonstrate its effectiveness against state-of-the-art retrieval techniques. For example, incorporating a comparison with models that use knowledge graph embeddings or transformer-based retrieval mechanisms would be beneficial. This would help to establish the practical applicability of FAVICOMP in real-world scenarios where the retrieval component is often a critical factor in overall performance. Furthermore, the authors should analyze the performance of FAVICOMP when the retrieval model is not perfect, simulating scenarios where the retrieval component might introduce noise or irrelevant information.

In addition to the retrieval comparison, a detailed analysis of the computational cost of FAVICOMP is essential. The authors should provide a breakdown of the time spent on different stages of the pipeline, such as retrieval, compression, and generation. This would help to identify the computational bottlenecks of the method and allow for a more informed assessment of its efficiency. Furthermore, the memory footprint of FAVICOMP should also be considered, especially when dealing with large-scale datasets. The authors should compare the computational cost of FAVICOMP with other evidence compression techniques, providing a clear understanding of the trade-offs between performance and efficiency. This analysis should also include the impact of different hyperparameter settings on the computational cost, such as the compression ratio and the number of retrieved documents.

Finally, a thorough sensitivity analysis of the hyperparameters is crucial for understanding the robustness of FAVICOMP. The authors should explore the impact of key hyperparameters, such as the temperature parameter for the target model, the compression ratio, and the weighting of the parametric and non-parametric knowledge sources. This analysis should reveal the optimal operating range for these parameters and their influence on the overall performance. The authors should also investigate the impact of the quality of the retrieved evidence on the performance of FAVICOMP. This analysis should consider scenarios where the retrieved documents are noisy, irrelevant, or contain contradictory information. Furthermore, the authors should evaluate the impact of the number of retrieved documents on the final performance, as well as the diversity of the retrieved set. This would help to identify the limitations of the approach and guide future research directions.

### Questions

Please see the weaknesses.

### Rating

6

### Confidence

4

**********
