### Summary

This paper introduces a novel runtime model analysis pipeline designed to identify parallelizable branches in DNN models, specifically targeting ASR and transformer-based models. The proposed Branch-Aware Parallel Execution (BAP) framework optimizes inference on mobile CPUs by isolating and executing parallelizable branches concurrently, while also employing a branch-aware memory allocation strategy that minimizes data conflicts and optimizes memory reuse. Evaluated on ASR models and transformer-based models, BAP achieved significant improvements in latency, memory allocation, and energy consumption without requiring model refactoring or architectural modifications.

### Soundness

3

### Presentation

2

### Contribution

2

### Strengths

1. The paper is well-structured, with clear explanations of the methodology and experimental setup. 
2. The proposed BAP framework introduces a novel runtime model analysis pipeline that effectively identifies and isolates parallelizable branches within ASR and transformer-based models, enabling efficient multithreading and memory management. 
3. The experimental results are compelling, demonstrating significant improvements in latency, memory efficiency, and energy consumption across various mobile platforms, including Raspberry Pi 4B, Pixel 6, Google Pixel 4a, and P30 Pro.

### Weaknesses

#### Some Related Works


#### comment

1. The paper’s focus on ASR and transformer-based models limits its applicability to other types of DNNs, such as CNNs or models with different control flow structures, potentially reducing its generalizability. Specifically, the paper does not address how the proposed branch-aware memory allocation would perform with models that have more complex conditional logic or irregular control flow, which are common in other DNN architectures. This lack of evaluation on diverse model types raises concerns about the robustness of the approach.
2. While the paper demonstrates improvements on specific mobile platforms, the evaluation could be strengthened by including a broader range of devices and edge computing scenarios to ensure robustness and generalizability. The current evaluation is limited to a few specific devices, and it is unclear how the proposed method would perform on devices with different CPU architectures or varying memory capacities. This limited evaluation scope makes it difficult to assess the practical applicability of the method in diverse real-world scenarios.
3. The paper lacks a detailed analysis of the overhead introduced by the runtime analysis pipeline, which could impact the overall efficiency of the proposed approach, especially for smaller models where overhead might be significant relative to the benefits. The paper does not provide a breakdown of the time spent on each step of the pipeline, including graph analysis, branch identification, and memory allocation, and compare this overhead to the actual inference time. This lack of analysis makes it difficult to quantify the trade-offs between the optimization benefits and the overhead introduced by the pipeline, especially for smaller models where the overhead might be more significant.

### Suggestions

To address the limitations regarding model applicability, the authors should evaluate their method on a wider range of DNN architectures, including CNNs and models with different control flow structures. This would involve testing the branch-aware memory allocation strategy on models with conditional statements or loops, which are common in various deep learning applications. The evaluation should also include a detailed analysis of how the proposed approach handles dynamic operations, such as those found in recurrent neural networks, and how it manages memory access patterns that are not strictly sequential. This would provide a more comprehensive understanding of the generalizability of the proposed method and its limitations.

To strengthen the evaluation, the authors should include a more diverse set of edge computing scenarios, encompassing various devices with different CPU architectures and memory capacities. This would involve testing the proposed method on a wider range of mobile devices, including those with less powerful CPUs or limited memory. The evaluation should also consider different network conditions, such as varying bandwidth and latency, to assess the robustness of the method in real-world scenarios. Furthermore, the authors should provide a detailed analysis of the trade-offs between latency reduction and memory savings, especially for smaller models where the overhead of the runtime analysis pipeline might be more significant. This analysis should include a breakdown of the time spent on each step of the pipeline, as well as a comparison of the overall inference time with and without the optimization.

Finally, the authors should provide a more detailed analysis of the overhead introduced by the runtime analysis pipeline. This analysis should include a breakdown of the time spent on each step of the pipeline, including graph analysis, branch identification, and memory allocation. The authors should also compare the overhead of their approach with other optimization techniques, such as CoDL and NN-Stretch, to provide a more comprehensive understanding of the trade-offs between optimization benefits and overhead. This analysis should also consider the impact of the overhead on the overall inference time, especially for smaller models where the overhead might be more significant relative to the benefits.

### Questions

1. How does BAP handle models with conditional statements or control flow structures that are not typically found in ASR or transformer-based models?
2. Can the authors provide a more detailed analysis of the runtime analysis pipeline's overhead, especially for smaller models, and how it impacts the overall inference time?
3. How does BAP perform on more complex tasks, such as video or 3D point cloud processing, which involve more complex data structures and computational patterns?
4. Could the authors elaborate on the branch-aware memory allocation strategy, specifically how it manages memory allocation and deallocation for dynamic tensor operations?

### Rating

5

### Confidence

3

**********
