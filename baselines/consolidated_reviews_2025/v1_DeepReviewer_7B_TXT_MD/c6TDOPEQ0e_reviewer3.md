### Summary

This paper proposes LASP-2, a sequence parallelism (SP) approach designed to enhance the efficiency of linear attention models, particularly for handling long sequences. LASP-2 reorganizes the computation and communication process to minimize the communication overhead, achieving better performance compared to previous methods like LASP-1 and Ring Attention. Additionally, the authors introduce LASP-2H, an extension that integrates LASP-2 with standard attention modules, enabling the model to handle both linear and standard attention layers. Experimental results demonstrate that LASP-2 and LASP-2H significantly improve throughput and scalability when dealing with very long sequences.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-structured, with a clear presentation of the proposed LASP-2 method and its integration with standard attention modules in LASP-2H. The authors provide a detailed explanation of the communication and computation processes, making it easy to follow the technical contributions.
2. The authors provide a theoretical analysis of the communication and computation costs of LASP-2, demonstrating its efficiency compared to LASP-1 and Ring Attention. This analysis helps to validate the effectiveness of the proposed method.
3. The experimental results show that LASP-2 achieves a throughput improvement of 15.2% over LASP-1 and 36.6% over Ring Attention on a 2048K sequence length. These results demonstrate the practical benefits of the proposed method in handling very long sequences.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a detailed comparison of the communication overhead between LASP-2 and LASP-1, particularly in scenarios with slower interconnects. While the authors mention that LASP-2 performs best in clusters with slower interconnects, a more in-depth analysis of the communication patterns and their impact on overall performance would be beneficial. Specifically, the paper lacks a breakdown of the communication costs associated with different components of the LASP-2 algorithm, such as the all-gather and reduce-scatter operations, and how these costs scale with increasing sequence lengths and network bandwidth limitations. This makes it difficult to fully assess the practical advantages of LASP-2 in various network environments.
2. The evaluation is conducted on a single hardware setup, which limits the generalizability of the results. Testing LASP-2 on different hardware configurations, such as those with varying numbers of GPUs or different network architectures, would provide a more comprehensive understanding of its performance characteristics. The paper does not discuss the potential challenges in adapting LASP-2 to new hardware configurations, such as the impact of different GPU architectures or interconnect technologies on the performance of the proposed method. This lack of hardware diversity makes it difficult to assess the robustness and portability of LASP-2 across different computing environments.
3. The paper does not provide a detailed analysis of the memory usage of LASP-2, including the memory footprint of the intermediate tensors and the memory usage of the model parameters. This analysis should also consider the impact of different memory configurations on the performance of LASP-2. The paper should also discuss the potential memory bottlenecks that may arise when using LASP-2 with very long sequences, and how these bottlenecks can be mitigated. A more detailed analysis of memory usage would provide a more complete picture of the resource requirements of the proposed method.

### Suggestions

To address the lack of detailed communication overhead analysis, the authors should provide a more granular breakdown of the communication costs associated with LASP-2. This should include a quantitative analysis of the time spent on all-gather and reduce-scatter operations, and how these costs scale with increasing sequence lengths and network bandwidth limitations. The analysis should also consider the impact of different network topologies on the performance of LASP-2, and how these topologies affect the communication overhead. Furthermore, the authors should provide a comparison of the communication overhead of LASP-2 with LASP-1, specifically focusing on scenarios with varying network conditions. This would help to clarify the practical advantages of LASP-2 in different network environments and provide a more comprehensive understanding of its performance characteristics. The authors should also discuss the potential limitations of LASP-2 in scenarios with very high network latency or low bandwidth, and how these limitations can be mitigated.

To improve the generalizability of the results, the authors should evaluate LASP-2 on a wider range of hardware configurations, including different numbers of GPUs and different network architectures. This should include a discussion of the potential challenges in adapting LASP-2 to new hardware configurations, such as the impact of different GPU architectures or interconnect technologies on the performance of the proposed method. The authors should also provide a detailed analysis of the performance of LASP-2 on different hardware platforms, including the impact of memory bandwidth and interconnect latency on the overall performance. This would help to assess the robustness and portability of LASP-2 across different computing environments. The authors should also discuss the potential limitations of LASP-2 in scenarios with very limited memory resources, and how these limitations can be mitigated.

Finally, the authors should provide a more detailed analysis of the memory usage of LASP-2, including the memory footprint of the intermediate tensors and the memory usage of the model parameters. This analysis should also consider the impact of different memory configurations on the performance of LASP-2. The authors should also discuss the potential memory bottlenecks that may arise when using LASP-2 with very long sequences, and how these bottlenecks can be mitigated. A more detailed analysis of memory usage would provide a more complete picture of the resource requirements of the proposed method. The authors should also discuss the potential limitations of LASP-2 in scenarios with very limited memory resources, and how these limitations can be mitigated. This analysis should include a discussion of the trade-offs between memory usage and performance, and how these trade-offs can be managed in practice.

### Questions

1. How does the communication overhead of LASP-2 compare to LASP-1, particularly in scenarios with slower interconnects? A more detailed analysis of the communication patterns and their impact on overall performance would be beneficial.
2. How does LASP-2 perform on different hardware configurations, such as those with varying numbers of GPUs or different network architectures? Testing on a wider range of hardware setups would provide a more comprehensive understanding of its performance characteristics.
3. What is the memory usage of LASP-2, and how does it scale with increasing sequence lengths? A detailed analysis of the memory footprint of the intermediate tensors and the memory usage of the model parameters would be helpful.

### Rating

6

### Confidence

3

**********
