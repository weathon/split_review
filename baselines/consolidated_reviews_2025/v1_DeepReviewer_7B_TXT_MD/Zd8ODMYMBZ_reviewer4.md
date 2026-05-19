### Summary

The paper introduces FAVICOMP (Familiarity-aware Evidence Compression), a novel training-free approach to improve retrieval-augmented generation (RAG) systems. FAVICOMP addresses the challenge of integrating retrieved evidence with target model knowledge by making the retrieved evidence more "familiar" to the target model. This is achieved through ensemble decoding, which combines the target model's decoding probabilities with those from a compression model, lower perplexity is achieved when the target model is more familiar with the compressed evidence. The method is evaluated on multiple open-domain QA datasets and demonstrates significant improvements over existing evidence compression baselines.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow. The motivation and methodology are clearly explained, making the paper accessible to a broad audience.
2. The proposed FAVICOMP method is novel and addresses a key challenge in RAG systems. The use of ensemble decoding to make retrieved evidence more "familiar" to the target model is a creative approach that shows promise for improving RAG performance.
3. The experimental results are compelling. FAVICOMP consistently outperforms existing baselines across multiple datasets, demonstrating its effectiveness in improving RAG accuracy.

### Weaknesses

#### Some Related Works


#### comment

1. While FAVICOMP shows strong performance on open-domain QA datasets, its generalizability to other types of tasks remains unclear. The paper would benefit from a discussion on potential limitations and future work to extend its applicability.
2. The paper does not provide a detailed analysis of the computational cost associated with FAVICOMP. While the method is effective, understanding its efficiency is crucial for practical applications.

### Suggestions

The paper should include a more thorough discussion of the limitations of FAVICOMP, particularly regarding its applicability to tasks beyond open-domain question answering. While the current experiments demonstrate strong performance on QA datasets, it is important to acknowledge that these tasks often involve relatively structured and well-defined queries. The paper should explore how FAVICOMP might perform on tasks with more complex or ambiguous queries, such as those found in creative writing or summarization. Furthermore, the paper should discuss the potential challenges of applying FAVICOMP to tasks that require multi-hop reasoning or involve external knowledge sources. A more detailed analysis of these limitations would provide a more balanced view of the method's capabilities and guide future research directions. For example, the authors could consider evaluating FAVICOMP on datasets that include tasks with varying levels of complexity, such as those found in the Natural Questions benchmark or the MultiFieldQA dataset. This would provide a more comprehensive understanding of the method's strengths and weaknesses.

To address the lack of computational cost analysis, the paper should include a detailed breakdown of the time and memory requirements of FAVICOMP. This analysis should consider the overhead introduced by the ensemble decoding process and the size of the compressed evidence. The paper should also compare the computational cost of FAVICOMP with that of the baseline methods. This comparison should include metrics such as the number of forward passes, the memory footprint, and the inference time. Furthermore, the paper should discuss the scalability of FAVICOMP with respect to the size of the retrieved evidence and the complexity of the target model. This analysis would provide a more complete picture of the method's practical feasibility and help readers understand its trade-offs between accuracy and efficiency. For instance, the authors could provide a table showing the inference time and memory usage for different datasets and model sizes. This would allow readers to assess the method's suitability for different applications.

Finally, the paper should explore potential avenues for optimizing the computational cost of FAVICOMP. This could include techniques such as model pruning, quantization, or knowledge distillation. The paper should also investigate the use of more efficient ensemble decoding strategies, such as those that selectively combine the outputs of the target and compression models. By addressing these optimization challenges, the paper could make FAVICOMP more practical for real-world applications. For example, the authors could explore the use of knowledge distillation to transfer the knowledge from the ensemble model to a smaller, more efficient model. This would reduce the computational cost of inference while maintaining the accuracy of the method. Additionally, the authors could investigate the use of techniques such as caching or parallel processing to further improve the efficiency of the method.

### Questions

1. How does FAVICOMP handle cases where the retrieved evidence is noisy or contains irrelevant information?
2. What are the potential limitations of FAVICOMP in scenarios where the target model has significantly different knowledge or capabilities compared to the compression model?

### Rating

6

### Confidence

3

**********
