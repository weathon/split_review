### Summary

This paper introduces a novel runtime model analysis pipeline designed to identify parallelizable branches within deep neural network (DNN) models, specifically targeting automatic speech recognition (ASR) and transformer-based architectures. The proposed Branch-Aware Parallel Execution (BAP) framework optimizes inference on mobile CPUs by isolating and executing parallelizable branches concurrently, while also employing a branch-aware memory allocation strategy that minimizes data conflicts and optimizes memory reuse. The multithreading implementation leverages CPU parallelism to execute these branches, further reducing latency. Evaluated on ASR models and transformer-based models, BAP demonstrates substantial improvements in latency, memory efficiency, and energy consumption, achieving up to 38.5% reduction in inference latency, 15.6x memory allocation improvements, and 20.2% energy cost savings, without requiring model refactoring or architectural modifications.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

- The paper addresses the timely challenge of optimizing complex DNN models for mobile CPU inference, a critical area given the increasing demand for real-time AI on edge devices.
- The proposed BAP framework introduces a novel runtime analysis pipeline that effectively identifies and isolates parallelizable branches within ASR and transformer-based models, enabling efficient multithreading and memory management.
- The experimental results are compelling, demonstrating significant improvements in latency, memory efficiency, and energy consumption across various mobile platforms, including Raspberry Pi 4B, Pixel 6, Google Pixel 4a, and P30 Pro.

### Weaknesses

#### Some Related Works


#### comment

 - The paper’s focus on ASR and transformer-based models limits its applicability to other types of DNNs, such as CNNs or models with different control flow structures, potentially reducing its generalizability.
- While the paper demonstrates improvements on specific mobile platforms, the evaluation could be strengthened by including a broader range of devices and edge computing scenarios to ensure robustness and generalizability.
- The paper lacks a detailed analysis of the overhead introduced by the runtime analysis pipeline, which could impact the overall efficiency of the proposed approach, especially for smaller models where overhead might be significant relative to the benefits.

### Suggestions

The authors should consider expanding the scope of their evaluation to include a more diverse set of models, particularly CNN architectures and models with control flow structures beyond the typical ASR and transformer paradigms. This would provide a more comprehensive understanding of the framework's applicability and limitations. For instance, evaluating the performance on models with conditional statements or loops, which are common in various deep learning applications, would be beneficial. Furthermore, a detailed analysis of the runtime analysis pipeline's overhead is crucial. The authors should provide a breakdown of the time spent on each step of the pipeline, including graph analysis, branch identification, and memory allocation, and compare this overhead to the actual inference time. This would help to quantify the trade-offs between the optimization benefits and the overhead introduced by the pipeline, especially for smaller models where the overhead might be more significant. 

To enhance the robustness of the evaluation, the authors should include a more comprehensive set of edge computing scenarios. This could involve testing the framework on a wider range of mobile devices with varying hardware specifications, such as different CPU architectures and memory capacities. Additionally, evaluating the performance under different network conditions, such as varying bandwidth and latency, would provide a more realistic assessment of the framework's practical applicability. The authors should also consider evaluating the framework's performance on more complex tasks, such as video or 3D point cloud processing, to demonstrate its versatility and scalability. This would involve adapting the framework to handle more complex data structures and computational patterns, which would further validate its generalizability.

Finally, the authors should provide a more detailed explanation of the branch-aware memory allocation strategy. Specifically, they should clarify how the framework handles memory allocation and deallocation for dynamic tensor operations, and how it minimizes data conflicts between parallel branches. A more detailed explanation of the memory management mechanisms, including the data structures used and the algorithms for memory allocation and deallocation, would be beneficial. Furthermore, the authors should provide a more detailed comparison of their approach with existing memory management techniques, highlighting the advantages and disadvantages of their method. This would help to better position their work within the broader context of memory management for DNN inference.

### Questions

- How does BAP handle models with conditional statements or control flow structures that are not typically found in ASR or transformer-based models?
- Can the authors provide a more detailed analysis of the runtime analysis pipeline's overhead, especially for smaller models, and how it impacts the overall inference time?
- How does BAP perform on more complex tasks, such as video or 3D point cloud processing, which involve more complex data structures and computational patterns?
- Could the authors elaborate on the branch-aware memory allocation strategy, specifically how it manages memory allocation and deallocation for dynamic tensor operations?

### Rating

3

### Confidence

3

**********
