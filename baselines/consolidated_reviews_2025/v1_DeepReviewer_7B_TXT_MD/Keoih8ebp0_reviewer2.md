### Summary

The paper introduces BAP, a runtime model analysis pipeline that identifies parallelizable branches in DNN models, particularly for ASR and transformer-based models, to optimize CPU-based inference on mobile devices. BAP enhances inference latency by isolating parallel branches, reducing memory allocation conflicts, and employs multithreading for efficient parallel execution. Evaluated on ASR models and transformer-based models, BAP achieves up to 38.5% inference latency reduction, 15.6x memory savings, and 20.2% energy cost reduction across various mobile devices without requiring model refactoring.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper addresses a relevant problem in mobile AI deployment by optimizing inference on CPUs for ASR and transformer models, which are crucial for real-time applications.
2. The proposed BAP framework shows significant improvements in latency, memory efficiency, and energy consumption across multiple mobile platforms.
3. The paper is well-structured, with clear explanations of the methodology and experimental setup.

### Weaknesses

#### Some Related Works


#### comment

1. The paper focuses on ASR and transformer-based models, which limits its generalizability to other DNN architectures. The lack of evaluation on diverse model types, such as CNNs or models with different control flow structures, makes it difficult to assess the broader applicability of the proposed approach. Specifically, the paper does not address how the branch-aware memory allocation would perform with models that have more complex conditional logic or irregular control flow, which are common in other DNN architectures.
2. The evaluation is primarily conducted on a limited set of mobile devices, which may not fully represent the diversity of real-world edge computing scenarios. The paper should include a more comprehensive evaluation across a wider range of devices with varying CPU architectures and memory capacities to demonstrate the robustness of the proposed method. The current evaluation does not sufficiently explore the performance of BAP on devices with less powerful CPUs or limited memory, which are common in many edge computing deployments.
3. While the paper highlights the benefits of branch-aware memory allocation, it lacks a detailed analysis of the overhead introduced by the runtime analysis pipeline and the multithreading implementation. The paper should provide a more thorough analysis of the computational cost of the graph analysis and branch identification steps, as well as the overhead associated with context switching and synchronization in the multithreading implementation. This analysis is crucial for understanding the practical trade-offs of the proposed approach.
4. The paper does not provide a detailed comparison with other state-of-the-art optimization techniques for mobile DNN inference. A more comprehensive comparison with existing methods, including both hardware-aware and software-based optimizations, would help to better position the contribution of BAP and highlight its advantages and limitations. The current comparison is limited to a single baseline method, which does not provide a complete picture of the performance of BAP relative to other approaches.
5. The paper does not discuss the limitations of the proposed approach, such as the potential impact of dynamic operations or irregular memory access patterns on the performance of the branch-aware memory allocation. The paper should address how the proposed method would handle dynamic operations, such as those found in recurrent neural networks, and how it would manage memory access patterns that are not strictly sequential. This discussion is important for understanding the practical limitations of the proposed approach.

### Suggestions

To address the limitations of the current study, the authors should expand their evaluation to include a more diverse set of DNN architectures beyond ASR and transformer models. Specifically, they should consider evaluating BAP on CNNs, which are widely used in image and video processing, and models with complex control flow structures, such as those found in graph neural networks or models with conditional statements. This would provide a more comprehensive understanding of the generalizability of the proposed approach. Furthermore, the authors should provide a detailed analysis of the performance of BAP on devices with varying CPU architectures and memory capacities. This analysis should include a breakdown of the performance gains achieved by BAP on each device, as well as a discussion of the factors that contribute to the observed performance differences. This would help to demonstrate the robustness of the proposed method across a wider range of real-world edge computing scenarios.

In addition to expanding the evaluation, the authors should provide a more detailed analysis of the overhead introduced by the runtime analysis pipeline and the multithreading implementation. This analysis should include a breakdown of the computational cost of each step of the pipeline, as well as the overhead associated with context switching and synchronization in the multithreading implementation. The authors should also discuss the potential impact of these overheads on the overall performance of the proposed approach, especially for smaller models where the overhead might be more significant. Furthermore, the authors should provide a more comprehensive comparison with other state-of-the-art optimization techniques for mobile DNN inference. This comparison should include a discussion of the advantages and limitations of BAP relative to other approaches, as well as a detailed analysis of the performance of BAP on a wider range of models and devices. This would help to better position the contribution of BAP and highlight its practical value.

Finally, the authors should address the limitations of the proposed approach, such as the potential impact of dynamic operations and irregular memory access patterns on the performance of the branch-aware memory allocation. They should discuss how the proposed method would handle dynamic operations, such as those found in recurrent neural networks, and how it would manage memory access patterns that are not strictly sequential. This discussion should include a detailed analysis of the potential performance degradation that could result from these factors, as well as potential strategies for mitigating these issues. The authors should also discuss the potential impact of these limitations on the practical applicability of the proposed approach in real-world edge computing scenarios.

### Questions

1. How does the branch-aware memory allocation strategy handle dynamic operations or irregular memory access patterns that may arise in other DNN architectures?
2. What are the computational costs associated with the runtime analysis pipeline, and how do they impact the overall inference time, especially for smaller models?
3. How does BAP perform on devices with less powerful CPUs or limited memory, and what are the trade-offs between latency reduction and memory savings on such devices?
4. How does BAP compare with other state-of-the-art optimization techniques for mobile DNN inference, and what are the specific advantages and limitations of the proposed approach?

### Rating

3

### Confidence

3

**********
