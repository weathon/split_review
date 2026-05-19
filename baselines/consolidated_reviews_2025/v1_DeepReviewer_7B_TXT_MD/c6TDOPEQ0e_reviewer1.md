### Summary

This paper presents LASP-2, a novel Sequence Parallelism approach for linear attention models, designed to improve communication and computation efficiency in long-sequence language models. LASP-2 reorganizes computations to use a single all-gather collective communication, reducing latency and enabling better overlap between communication and computation. Additionally, it introduces a hybrid model, LASP-2H, that integrates LASP-2 for linear attention with standard attention modules, enhancing recall-intensive tasks. Evaluation on Linear-Llama3 demonstrates LASP-2’s 15.2% throughput improvement over LASP-1 and 36.6% over Ring Attention on a 2048K sequence.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. LASP-2’s reorganization of computations for sequence parallelism (SP) enables efficient handling of very-long input sequences, addressing a critical challenge in distributed training of long-sequence models.
2. The paper provides a detailed theoretical analysis of communication and computation costs, demonstrating LASP-2’s superiority over LASP-1 and Ring Attention.
3. The introduction of LASP-2H, which combines linear and standard attention modules, is a valuable contribution, as it allows for more flexible model architectures that can balance efficiency and performance on tasks requiring recall.

### Weaknesses

#### Some Related Works


#### comment

1. While LASP-2 shows improvements over LASP-1 and Ring Attention, the paper does not compare LASP-2 with other state-of-the-art sequence parallelism methods, such as HGRN and HGRN2. Including these comparisons would provide a clearer picture of LASP-2’s relative performance and advantages within the broader landscape of SP techniques. Specifically, the lack of comparison against methods that employ hierarchical parallelism or more sophisticated communication strategies makes it difficult to assess the true novelty and practical impact of LASP-2. The paper should include a more thorough evaluation against these methods, including a discussion of the trade-offs in terms of communication overhead, computation costs, and memory usage.
2. The paper does not provide a detailed analysis of the communication overhead associated with LASP-2, particularly in scenarios with slower interconnects. While the authors mention that LASP-2 performs best in clusters with slower interconnects, a more in-depth analysis of how communication costs scale with increasing sequence lengths and varying network bandwidths would be beneficial. This should include a breakdown of the communication patterns and their impact on overall performance, especially in cases where the all-gather operation becomes a bottleneck. The analysis should also consider the impact of network latency and bandwidth limitations on the performance of LASP-2, and how these factors affect the overall training time.
3. The evaluation is conducted on a single hardware setup, which limits the generalizability of the results. Testing LASP-2 on different hardware configurations, such as those with varying numbers of GPUs or different network architectures, would provide a more comprehensive understanding of its performance characteristics. This should include a discussion of the scalability of LASP-2 across different hardware platforms and the potential challenges in adapting it to new hardware configurations. The evaluation should also consider the impact of different GPU architectures and interconnect technologies on the performance of LASP-2.

### Suggestions

To strengthen the paper, the authors should include a more comprehensive comparison with state-of-the-art sequence parallelism methods, such as HGRN and HGRN2. This comparison should not only focus on throughput but also consider other metrics such as memory usage, communication overhead, and convergence speed. The authors should provide a detailed analysis of the trade-offs between LASP-2 and these methods, highlighting the specific scenarios where LASP-2 is expected to outperform them. This analysis should include a discussion of the communication patterns and their impact on overall performance, especially in cases where the all-gather operation becomes a bottleneck. Furthermore, the authors should provide a more detailed breakdown of the communication costs, including the time spent on different communication primitives, such as all-gather, reduce-scatter, and ring-all-reduce. This analysis should also consider the impact of network latency and bandwidth limitations on the performance of LASP-2, and how these factors affect the overall training time.

In addition to the comparison with other SP methods, the authors should provide a more detailed analysis of the communication overhead associated with LASP-2, particularly in scenarios with slower interconnects. This analysis should include a breakdown of the communication patterns and their impact on overall performance, especially in cases where the all-gather operation becomes a bottleneck. The authors should also consider the impact of different network topologies on the performance of LASP-2, and how these factors affect the overall training time. The analysis should also include a discussion of the trade-offs between the communication cost and the computation cost, and how these trade-offs affect the overall performance of LASP-2. The authors should also provide a more detailed analysis of the memory usage of LASP-2, including the memory footprint of the intermediate tensors and the memory usage of the model parameters. This analysis should also consider the impact of different memory configurations on the performance of LASP-2.

Finally, the authors should evaluate LASP-2 on a wider range of hardware configurations, including different numbers of GPUs and different network architectures. This evaluation should include a discussion of the scalability of LASP-2 across different hardware platforms and the potential challenges in adapting it to new hardware configurations. The authors should also consider the impact of different GPU architectures and interconnect technologies on the performance of LASP-2. This evaluation should also include a discussion of the limitations of LASP-2 and the potential areas for future research. The authors should also provide a more detailed analysis of the performance of LASP-2 on different sequence lengths, and how the performance of LASP-2 scales with increasing sequence lengths. This analysis should include a discussion of the trade-offs between the communication cost and the computation cost, and how these trade-offs affect the overall performance of LASP-2.

### Questions

1. How does LASP-2 perform in scenarios with varying sequence lengths, and is there a point at which the benefits of LASP-2 diminish?
2. What are the practical limitations of LASP-2 in terms of hardware requirements, and how does it perform on different hardware configurations?

### Rating

5

### Confidence

4

**********
