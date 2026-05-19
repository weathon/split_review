### Summary

The paper introduces BAP, a runtime model analysis pipeline that identifies parallelizable branches in DNN models, particularly for ASR and transformer-based models, to optimize CPU-based inference on mobile devices. BAP enhances inference latency by isolating parallel branches, reducing memory allocation conflicts, and employs multithreading for efficient parallel execution. Evaluated on ASR models and transformer-based models, BAP achieves up to 38.5% reduction in inference latency, 15.6x memory savings, and 20.2% energy cost reduction across various mobile devices without requiring model refactoring.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The problem is well-motivated.
3. The proposed method is evaluated on multiple platforms, including Raspberry Pi 4B, Pixel 6, Google Pixel 4a, and P30 Pro.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a comparison with other optimization techniques, such as CoDL and NN-Stretch. Including such comparisons would provide a more comprehensive evaluation of the proposed method's effectiveness.
2. The paper does not provide a detailed explanation of how the branch-aware memory allocation strategy is implemented. A more detailed description of the memory allocation and deallocation process, especially for dynamic tensor operations, would be beneficial.
3. The paper does not discuss the limitations of the proposed method, such as its applicability to different types of DNN models or its performance on edge devices with limited resources.

### Suggestions

The paper would benefit significantly from a more thorough comparison with existing optimization techniques. Specifically, the authors should benchmark their method against CoDL and NN-Stretch, which are relevant state-of-the-art approaches for optimizing DNN inference. This comparison should not only focus on latency but also consider memory usage and energy consumption, providing a holistic view of the performance trade-offs. Furthermore, it would be valuable to analyze the performance of these methods on the same set of models and datasets used in the paper, ensuring a fair and comprehensive evaluation. This would help to establish the relative strengths and weaknesses of the proposed method and provide a clearer understanding of its practical advantages.

To enhance the clarity of the proposed method, the authors should provide a more detailed explanation of the branch-aware memory allocation strategy. This should include a step-by-step description of how memory is allocated, deallocated, and reused for different branches of the DNN model. The explanation should also address how the method handles dynamic tensor operations, which are common in many DNN architectures. A clear description of the data structures used to manage memory and the algorithms for memory allocation and deallocation would be beneficial. Additionally, the authors should discuss the potential overhead associated with the branch-aware memory allocation strategy and how it impacts the overall performance of the method. This would help readers understand the practical implications of the proposed approach.

Finally, the paper should include a more comprehensive discussion of the limitations of the proposed method. This should include an analysis of the types of DNN models for which the method is most effective, as well as the types of models for which it may not be suitable. The authors should also discuss the performance of the method on edge devices with limited resources, such as low-end GPUs or CPUs. This discussion should include an analysis of the trade-offs between performance and resource usage, as well as potential strategies for mitigating these limitations. For example, the authors could explore the use of model compression or quantization techniques to reduce the memory footprint of the models and improve their performance on resource-constrained devices.

### Questions

1. How does the proposed method compare with other optimization techniques, such as CoDL and NN-Stretch, in terms of latency, memory usage, and energy consumption?
2. Can the branch-aware memory allocation strategy be applied to other types of DNN models, such as CNNs or models with different control flow structures?
3. What are the limitations of the proposed method, and how does it perform on edge devices with limited resources?

### Rating

6

### Confidence

3

**********
