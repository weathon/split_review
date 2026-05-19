### Summary

This paper presents a parallel execution framework for dynamic neural networks on mobile devices. It introduces a runtime analysis pipeline that identifies parallelizable branches within the model’s computational graph, allowing for branch-aware memory allocation and optimized multithreading execution. The proposed method reduces inference latency and memory allocation requirements, with minimal impact on energy consumption.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-structured and easy to follow, making the methodology and results accessible to readers.
2. The proposed approach demonstrates significant reductions in inference latency and memory usage, which are critical for real-time applications on resource-constrained mobile devices.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a detailed explanation of how the runtime analysis pipeline identifies parallelizable branches. Specific criteria and algorithms used for this process are not clearly described, making it difficult to assess the robustness and generalizability of the approach. For instance, the paper does not specify how it handles different types of control flow operations (e.g., loops, conditionals) within the computational graph, which are common in dynamic neural networks. The absence of a clear algorithm or pseudocode makes it hard to understand the practical implementation of the analysis pipeline.
2. While the paper claims compatibility with existing optimization techniques, it does not provide empirical evidence or detailed explanations of how these techniques can be integrated with the proposed method. This lack of clarity raises questions about the practical applicability and potential benefits of such integration. For example, it is unclear how the proposed branch-aware memory allocation would interact with techniques like quantization or pruning, and whether these techniques would require re-tuning or modification to be compatible.
3. The evaluation lacks a detailed breakdown of performance improvements across different model architectures and layers. This makes it challenging to understand where the proposed method achieves its best performance and where it might have limitations. For example, it would be beneficial to see the performance gains for different types of layers (e.g., convolutional, recurrent, attention) and how these gains vary across different network architectures. The current evaluation does not provide sufficient granularity to identify the specific scenarios where the proposed method is most effective.
4. The paper does not provide a thorough comparison with existing parallel execution frameworks or libraries for mobile devices. This makes it difficult to assess the novelty and advantages of the proposed method over existing solutions. Specifically, the paper should compare against other methods that also target dynamic neural networks on mobile devices, and it should clearly articulate what makes the proposed approach unique and superior.
4. The energy consumption analysis is somewhat limited, as it only provides estimated energy savings. Including actual energy consumption measurements would strengthen the evaluation and provide more concrete evidence of the method’s efficiency. The paper should include measurements of actual power draw during inference, rather than relying on estimations, to provide a more accurate assessment of the method's energy efficiency.

### Suggestions

To address the lack of detail regarding the runtime analysis pipeline, the authors should provide a more thorough explanation of the algorithms and criteria used to identify parallelizable branches. This should include a discussion of how different types of control flow operations, such as loops and conditionals, are handled. The paper should also include pseudocode or a detailed example to illustrate the practical implementation of the analysis pipeline. Furthermore, the authors should specify how the analysis handles data dependencies between operations within the graph, and how it ensures that parallel execution does not lead to race conditions or other errors. A clear explanation of the limitations of the analysis pipeline, such as types of models or operations that it cannot handle, would also be beneficial.

To strengthen the claims about compatibility with existing optimization techniques, the authors should provide empirical evidence demonstrating the integration of their method with techniques like quantization and pruning. This could include experiments showing the performance gains when these techniques are combined, and a discussion of any modifications or re-tuning that may be required. The paper should also address how the proposed branch-aware memory allocation interacts with other memory optimization techniques, and whether it introduces any overhead or limitations. A detailed analysis of the trade-offs between different optimization techniques and the proposed method would be valuable. The authors should also clarify whether the proposed method can be applied to models that have already been optimized using other techniques, or if it requires a specific model format or structure.

To improve the evaluation, the authors should provide a more detailed breakdown of performance improvements across different model architectures and layers. This should include a comparison of the performance gains for different types of layers, such as convolutional, recurrent, and attention layers, and how these gains vary across different network architectures. The evaluation should also include a more thorough comparison with existing parallel execution frameworks or libraries for mobile devices, including a discussion of the advantages and disadvantages of the proposed method compared to these alternatives. The authors should also include actual energy consumption measurements, rather than estimations, to provide a more accurate assessment of the method's energy efficiency. This could involve using a power meter to measure the power draw during inference, and reporting the results for different models and devices.

### Questions

1. Can the authors provide more detailed explanations and algorithms for the runtime analysis pipeline used to identify parallelizable branches?
2. How does the proposed method integrate with existing optimization techniques, and what are the empirical benefits of such integration?
3. Could the authors provide a more detailed breakdown of performance improvements across different model architectures and layers?
4. How does the proposed method compare with existing parallel execution frameworks or libraries for mobile devices?
5. Can the authors provide actual energy consumption measurements to complement the estimated energy savings?

### Rating

3

### Confidence

3

**********
