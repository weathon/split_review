### Summary

The paper proposes a novel adaptive retrieval augmented generation (RAG) model, called SeaKR, which leverages the self-aware uncertainty of large language models (LLMs) to dynamically determine when to retrieve external knowledge and how to integrate it. SeaKR activates retrieval when LLMs exhibit high self-aware uncertainty and re-ranks retrieved knowledge snippets based on their ability to reduce this uncertainty. The authors demonstrate the effectiveness of SeaKR through extensive experiments on both complex and simple question-answering tasks, showing that it outperforms existing adaptive RAG methods.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel approach to adaptive RAG by leveraging the self-aware uncertainty of LLMs, which is a significant advancement in the field.
2. The authors provide a thorough experimental evaluation, including ablation studies and case studies, to validate the effectiveness of SeaKR.
3. The paper is well-organized and clearly written, making it easy to follow the proposed methodology and results.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not extensively discuss the potential limitations of SeaKR, such as its performance on different types of tasks or with different LLMs. Specifically, the evaluation lacks a detailed analysis of how the method performs on tasks requiring complex reasoning beyond simple fact retrieval, and how the choice of LLM impacts the overall performance, particularly in terms of the quality of the self-aware uncertainty estimates.
2. The computational cost of SeaKR is not thoroughly analyzed, which is crucial for practical applications. The paper does not provide a detailed breakdown of the time complexity associated with the self-aware uncertainty estimation, nor does it compare the computational overhead of SeaKR with other adaptive RAG methods. This makes it difficult to assess the practical feasibility of the approach, especially for resource-constrained environments.
3. The paper could benefit from a more detailed comparison with other state-of-the-art adaptive RAG methods, highlighting the specific advantages and disadvantages of SeaKR. While the paper mentions existing methods, it lacks a rigorous comparison that would clearly delineate the scenarios where SeaKR excels or falls short, particularly in terms of retrieval latency, knowledge integration, and overall accuracy.

### Suggestions

The paper would benefit from a more thorough investigation into the limitations of SeaKR, particularly concerning its applicability to diverse tasks and its sensitivity to the choice of the underlying LLM. The authors should include experiments on tasks that require more complex reasoning, such as multi-hop question answering or tasks involving logical inference, to better understand the boundaries of SeaKR's effectiveness. Furthermore, a detailed analysis of how the self-aware uncertainty estimates vary across different LLMs, including variations in model size and architecture, would provide valuable insights into the robustness of the proposed approach. This analysis should also explore the impact of different uncertainty estimation techniques on the overall performance of SeaKR, potentially identifying more efficient or accurate methods for uncertainty quantification.

To address the lack of computational analysis, the authors should provide a detailed breakdown of the time complexity associated with each step of the SeaKR pipeline, including the self-aware uncertainty estimation, retrieval, and knowledge integration. This analysis should include a comparison of the computational overhead of SeaKR with other adaptive RAG methods, considering both the number of parameters and the number of forward passes required. The authors should also explore potential optimizations to reduce the computational cost of SeaKR, such as using more efficient uncertainty estimation techniques or implementing parallel processing for retrieval and integration. A practical evaluation of the method's performance on different hardware configurations would also be beneficial, providing a more realistic assessment of its feasibility for real-world applications.

Finally, the paper should include a more rigorous comparison with other state-of-the-art adaptive RAG methods, focusing on specific aspects such as retrieval latency, knowledge integration, and overall accuracy. This comparison should not only highlight the advantages of SeaKR but also identify its limitations and potential areas for improvement. The authors should consider including a wider range of baselines, including both non-adaptive and adaptive RAG methods, to provide a more comprehensive evaluation of the proposed approach. A detailed analysis of the trade-offs between different methods would help readers better understand the strengths and weaknesses of SeaKR and its suitability for various applications.

### Questions

1. How does SeaKR perform on tasks that require more complex reasoning or multi-step inference?
2. What is the computational overhead of SeaKR compared to other RAG methods, and how does it scale with the size of the knowledge base and the length of the input queries?
3. How sensitive is SeaKR to the choice of the underlying LLM, and are there any specific LLMs for which it performs particularly well or poorly?

### Rating

6

### Confidence

3

**********
