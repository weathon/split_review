### Summary

The paper introduces FAVICOMP, a training-free evidence compression method designed to enhance retrieval-augmented generation (RAG) by making retrieved evidence more familiar to the target model and integrating parametric knowledge. FAVICOMP uses ensemble decoding to combine token logits from both the compression model and the target model, resulting in improved downstream performance. The method is evaluated on multiple open-domain QA datasets, showing significant improvements over recent evidence compression baselines. FAVICOMP is model-agnostic and can be easily integrated into various RAG workflows.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow.
2. The proposed method is simple yet effective. The authors also conducted extensive experiments to demonstrate the effectiveness of the proposed method.
3. The proposed method is training-free and model-agnostic, making it easy to integrate into existing RAG workflows.

### Weaknesses

#### Some Related Works


#### comment

1. The authors should provide a more detailed analysis of the computational cost of FAVICOMP compared to other methods. Specifically, the paper should include a breakdown of the time spent on each stage of the FAVICOMP pipeline (retrieval, compression, and generation) and compare it to the baseline methods. This would allow for a more thorough understanding of the trade-offs between performance and computational resources.
2. The authors should provide more insights into how to choose the optimal value of $\alpha$ for different tasks and datasets. The current analysis lacks a systematic approach to determining the optimal $\alpha$ value. It would be beneficial to explore the relationship between $\alpha$ and dataset characteristics, such as the complexity of the questions or the length of the retrieved documents, and provide guidelines for selecting $\alpha$ based on these factors.

### Suggestions

To address the computational cost concerns, the authors should conduct a detailed profiling of FAVICOMP's runtime, breaking down the time spent on each stage: retrieval, compression, and generation. This analysis should be compared against the baseline methods, providing a clear picture of where FAVICOMP introduces overhead. For example, the authors could report the average time taken for each stage across different datasets and model sizes. Furthermore, it would be beneficial to analyze the memory footprint of FAVICOMP, especially during the compression phase, as this could be a limiting factor for large-scale applications. This detailed analysis would allow readers to better understand the practical implications of using FAVICOMP in resource-constrained environments and provide a more comprehensive evaluation of its efficiency.

Regarding the selection of the $\alpha$ parameter, the authors should conduct a more systematic study to understand its impact on performance across different tasks and datasets. This study should explore the relationship between $\alpha$ and various dataset characteristics, such as the complexity of the questions, the length of the retrieved documents, and the density of relevant information. For instance, the authors could analyze how the optimal $\alpha$ value changes when the questions require more complex reasoning or when the retrieved documents are longer and more verbose. Based on this analysis, the authors should provide clear guidelines for selecting the $\alpha$ value, potentially suggesting a range of values based on the characteristics of the task and dataset. This would make the method more practical and easier to use for a wider range of applications.

Finally, the authors should consider exploring adaptive methods for setting $\alpha$ dynamically based on the input query or the characteristics of the retrieved documents. For example, a higher $\alpha$ value could be used when the retrieved documents are highly relevant and contain most of the necessary information, while a lower $\alpha$ value could be used when the documents are less relevant or require more integration with the model's parametric knowledge. This adaptive approach could potentially lead to further performance improvements and make the method more robust across different scenarios. The authors could also investigate the use of a learned $\alpha$ parameter, where the value is optimized during a hyperparameter tuning process, although this would add a training component to the method.

### Questions

Please see the weaknesses.

### Rating

6

### Confidence

3

**********
