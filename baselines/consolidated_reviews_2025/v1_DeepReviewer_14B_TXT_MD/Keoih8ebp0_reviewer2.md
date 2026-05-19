### Summary

This paper proposes a branch-aware parallel execution framework for DNN inference on mobile CPUs. The proposed framework consists of three main components: graph analysis, branch-aware memory allocation, and multithreading execution. The authors evaluate the proposed framework using ASR and transformer-based models and compare it with the TFLite runtime on various mobile devices. The results show that the proposed framework can reduce inference latency by up to 38.5% and energy cost by up to 20.2% compared to the TFLite runtime.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The authors provide a comprehensive evaluation of the proposed framework on various mobile devices and models, demonstrating its effectiveness in reducing inference latency and energy consumption.

### Weaknesses

#### Some Related Works


#### comment

1. The authors only evaluate the proposed framework on ASR and transformer-based models. It would be beneficial to evaluate the framework on other types of models to demonstrate its generalizability.
2. The authors compare the proposed framework with the TFLite runtime but do not compare it with other state-of-the-art frameworks or libraries for DNN inference on mobile CPUs, such as TensorFlow Lite Delegated Execution and MNN. It is unclear how the proposed framework compares to these other solutions in terms of performance and energy efficiency.
3. The authors mention that the proposed framework can reduce memory allocation requirements by up to 15.6x compared to the TFLite naive memory allocation. However, it is not clear how the proposed framework achieves this reduction and what the trade-offs are in terms of performance and energy consumption.

### Suggestions

The paper would benefit from a more thorough evaluation of the proposed framework's generalizability. While the current evaluation focuses on ASR and transformer-based models, it is crucial to demonstrate its effectiveness across a broader range of model architectures. Specifically, the authors should consider evaluating the framework on models with different computational characteristics, such as CNNs for image classification or other sequence-based models beyond transformers. This would provide a more comprehensive understanding of the framework's strengths and limitations and its applicability to diverse workloads. Furthermore, it would be beneficial to analyze the performance of the framework on models with varying levels of sparsity, as this could reveal potential areas for optimization or limitations of the proposed approach. Such an analysis would strengthen the claims of the paper and provide a more robust assessment of the framework's practical utility.

To better contextualize the performance of the proposed framework, a comparison with other state-of-the-art solutions for DNN inference on mobile CPUs is necessary. While the comparison with TFLite runtime is a good starting point, it is important to benchmark against other prominent frameworks such as TensorFlow Lite Delegated Execution and MNN. This comparison should not only focus on inference latency but also consider other critical factors such as energy consumption, memory footprint, and model compatibility. A detailed analysis of these aspects would provide a more comprehensive understanding of the proposed framework's advantages and disadvantages compared to existing solutions. Furthermore, it would be valuable to investigate how the proposed framework interacts with different hardware architectures and instruction sets, as this could reveal potential bottlenecks or opportunities for further optimization. Such a comparison would help to position the proposed framework within the broader landscape of mobile DNN inference solutions.

Finally, the paper should provide a more detailed explanation of the memory allocation reduction achieved by the proposed framework. While the authors mention a 15.6x reduction compared to TFLite's naive allocation, the underlying mechanisms and trade-offs are not clearly explained. It is important to elaborate on the specific techniques used to achieve this reduction, such as memory pooling, reuse strategies, or custom allocators. Furthermore, it is crucial to analyze the impact of these techniques on performance and energy consumption. For example, while reducing memory allocation can decrease memory usage, it may also introduce overhead in terms of memory management or data movement. A detailed analysis of these trade-offs would provide a more complete understanding of the proposed framework's memory management strategy and its implications for overall performance and energy efficiency.

### Questions

1. How does the proposed framework compare to other state-of-the-art frameworks or libraries for DNN inference on mobile CPUs, such as TensorFlow Lite Delegated Execution and MNN?
2. How does the proposed framework achieve memory allocation reduction, and what are the trade-offs in terms of performance and energy consumption?
3. How does the proposed framework handle dynamic control flows and tensor operations in DNN models, and what are the limitations of the proposed approach?

### Rating

5

### Confidence

3

**********
