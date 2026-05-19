### Summary

This paper introduces BAP, a novel runtime system designed to accelerate the inference of ASR and transformer-based models on mobile CPUs. BAP achieves this by leveraging CPU multithreading to enable parallel execution of parallelizable branches within the model's computation graph. To facilitate this parallelism, BAP employs a branch-aware memory allocation strategy that isolates memory arenas for different branches, thereby reducing memory contention and optimizing memory reuse within each branch. The authors evaluate BAP on a range of mobile devices, demonstrating significant reductions in inference latency, memory allocation requirements, and energy consumption compared to the TFLite naive memory allocation.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper introduces a novel approach to optimizing DNN inference on mobile CPUs by focusing on branch-aware memory allocation and multithreading. This is particularly relevant for dynamic models like ASR and transformers, which have not been extensively explored in the context of CPU-based parallel execution.
2. The authors provide a thorough evaluation of BAP across different mobile devices and models, showing consistent improvements in latency, memory usage, and energy consumption. The results are compelling and demonstrate the practical benefits of the proposed approach.
3. BAP's ability to optimize inference without requiring model refactoring makes it highly practical for real-world deployment, as it simplifies the integration process for existing models.
4. The paper is well-written and clearly explains the technical details of BAP, including the graph analysis pipeline, memory allocation strategy, and multithreading execution. The use of figures and tables effectively illustrates the key concepts and results.

### Weaknesses

#### Some Related Works


#### comment

1. The paper primarily focuses on CPU-based optimization, but given the prevalence of heterogeneous computing environments, exploring how BAP could be extended to leverage GPUs or NPUs would enhance its applicability. The current scope limits the potential impact of BAP, as many mobile devices have specialized accelerators that could significantly improve performance if properly utilized. The lack of discussion on how BAP's memory management and parallelization strategies would translate to these architectures is a notable gap.
2. The paper lacks a detailed discussion on the trade-offs between parallelization overhead and performance gains, particularly in scenarios with smaller models or less complex operations. It is unclear how the overhead of thread creation and management compares to the actual computation time for smaller workloads, which could negate the benefits of parallelization. A more granular analysis of the overhead costs associated with BAP's parallel execution is needed.
3. The evaluation could benefit from a more in-depth comparison with other state-of-the-art optimization techniques for mobile DNN inference, providing a clearer context for BAP's performance improvements. The paper should include a comparison with other techniques that also target branch-aware execution or memory optimization, to better position BAP's contributions within the existing landscape of mobile inference optimization.

### Suggestions

To address the limitations of BAP on lower-end devices, the authors should conduct a more detailed analysis of the performance bottlenecks. This should include profiling the execution of different operations and model architectures on a range of mobile CPUs to identify where the parallelization benefits are minimized. For example, it would be beneficial to analyze the impact of memory bandwidth limitations, cache misses, and thread management overhead on less powerful processors. The authors could also explore techniques to dynamically adjust the degree of parallelism based on the hardware capabilities, such as reducing the number of threads or using a hybrid approach that combines parallel and sequential execution. Furthermore, a more detailed breakdown of the latency improvements across different layers or operations would provide a better understanding of where BAP is most effective and where it falls short. This analysis should also consider the impact of different memory allocation strategies on performance, and how these strategies interact with the CPU's memory hierarchy.

To enhance the applicability of BAP, the authors should explore its potential for heterogeneous computing environments. This could involve investigating how BAP's branch-aware memory allocation and multithreading strategies can be adapted to leverage GPUs or NPUs. The authors should discuss the challenges of porting BAP to these architectures, such as the need for different memory management techniques and the potential for data transfer overhead between the CPU and accelerators. A detailed analysis of the performance trade-offs of using different hardware components for different parts of the model would be valuable. For example, the authors could explore the possibility of using the CPU for control flow operations and the accelerator for computationally intensive tasks. This would require a mechanism for dynamic task scheduling and load balancing across different hardware components. The authors should also consider the impact of different data formats and precision requirements on the performance of BAP on different hardware.

Finally, the authors should provide a more detailed analysis of the trade-offs between parallelization overhead and performance gains. This should include a breakdown of the time spent on thread creation, synchronization, and memory management, compared to the actual computation time. The authors should also investigate the impact of different thread pool sizes and task stealing strategies on the overall performance. A more granular analysis of the overhead costs associated with BAP's parallel execution is needed, particularly for smaller models or less complex operations. The authors should also consider the impact of different memory allocation strategies on performance, and how these strategies interact with the CPU's memory hierarchy. A comparison with other state-of-the-art optimization techniques for mobile DNN inference would also be beneficial, to better position BAP's contributions within the existing landscape of mobile inference optimization.

### Questions

1. How does BAP handle scenarios where the model structure changes dynamically during inference, and what are the potential impacts on performance and memory usage?
2. Can the authors provide more detailed insights into the energy consumption trade-offs, particularly in scenarios where the performance gains are modest?
3. How does BAP's memory management strategy compare to other advanced memory management techniques in mobile inference frameworks, and what are the specific advantages and disadvantages?
4. What are the limitations of BAP in terms of scalability to even larger or more complex models, and how might these be addressed in future work?

### Rating

6

### Confidence

4

**********
