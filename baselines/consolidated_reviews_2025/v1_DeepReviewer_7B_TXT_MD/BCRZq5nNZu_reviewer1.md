### Summary

The paper focuses on the continual learning (CL) setting where the data is presented in chunks instead of a full dataset. The authors refer to this as the "chunking problem" and show that it is a significant contributor to the performance drop between offline learning and CL. They analyze the chunking problem in the linear case and demonstrate that per-chunk weight averaging improves performance. They then evaluate this method on standard CL benchmarks and show that it improves the performance of several CL methods.

### Soundness

3 good

### Presentation

2 fair

### Contribution

2 fair

### Strengths

The paper identifies a new problem in CL, which is the "chunking problem". The authors show that this problem is a significant contributor to the performance drop between offline learning and CL. They also demonstrate that per-chunk weight averaging improves performance in the chunking setting and that this improvement transfers to CL.

### Weaknesses

#### Some Related Works


#### comment

1. The paper is not well written. The introduction is too short and does not provide enough background information. The related work section is also too short and does not discuss enough relevant literature. The paper also lacks a clear definition of the chunking problem and how it differs from other continual learning problems. The introduction should clearly articulate the problem being addressed, the limitations of existing approaches, and the contributions of the paper. The related work section should provide a comprehensive overview of the existing literature, highlighting the gaps that the paper aims to fill. The paper should also clearly define the chunking problem, including its characteristics and how it differs from other continual learning problems.

2. The paper does not provide a clear motivation for the chunking problem. It is not clear why this problem is important or how it affects the performance of continual learning methods. The paper should provide a clear motivation for the chunking problem, explaining why it is important and how it affects the performance of continual learning methods. The paper should also provide a clear definition of the chunking problem, including its characteristics and how it differs from other continual learning problems.

3. The paper does not provide a clear explanation of the per-chunk weight averaging method. The paper should provide a clear explanation of the per-chunk weight averaging method, including its implementation details and its theoretical properties. The paper should also provide a clear explanation of the per-chunk weight averaging method, including its implementation details and its theoretical properties. The paper should also provide a clear explanation of the per-chunk weight averaging method, including its implementation details and its theoretical properties.

4. The paper does not provide a clear evaluation of the proposed method. The paper should provide a clear evaluation of the proposed method, including its performance on standard continual learning benchmarks and its comparison to existing methods. The paper should also provide a clear evaluation of the proposed method, including its performance on standard continual learning benchmarks and its comparison to existing methods. The paper should also provide a clear evaluation of the proposed method, including its performance on standard continual learning benchmarks and its comparison to existing methods.

### Suggestions

The paper needs a more thorough introduction that clearly defines the chunking problem and its significance within the broader context of continual learning. The introduction should not only state the problem but also explain why it is challenging and how it differs from existing continual learning scenarios. For instance, the authors could discuss how the sequential nature of data presentation in the chunking setting introduces a unique form of distribution shift that is distinct from task-incremental or domain-incremental learning. Furthermore, the introduction should provide a clear motivation for why addressing the chunking problem is crucial for advancing continual learning. The authors should elaborate on the practical implications of this problem, such as its relevance to real-world applications where data is often presented in chunks or mini-batches. This would help to establish the importance of the research and justify the need for a dedicated solution.

The related work section should be expanded to include a more comprehensive overview of existing continual learning methods and their limitations in handling chunking scenarios. The authors should discuss how existing methods, such as replay-based approaches, regularization techniques, and parameter isolation methods, perform when faced with chunked data. A detailed analysis of these methods would help to highlight the novelty and importance of the proposed approach. The authors should also discuss the theoretical underpinnings of the chunking problem, such as the concept of catastrophic forgetting and how it manifests in the context of chunked data. This would provide a deeper understanding of the problem and help to position the proposed method within the existing literature. Furthermore, the authors should clearly articulate the differences between the chunking problem and other continual learning problems, such as task-incremental and domain-incremental learning. This would help to clarify the unique challenges posed by the chunking setting and justify the need for a specialized solution.

The paper should provide a more detailed explanation of the per-chunk weight averaging method, including its implementation details and its theoretical properties. The authors should explain how the weights are averaged across chunks and how this averaging process affects the learning dynamics. The theoretical properties of the method should be discussed, including its convergence behavior and its robustness to different types of data distributions. The authors should also provide a clear explanation of the per-chunk weight averaging method, including its implementation details and its theoretical properties. The paper should also include a more comprehensive evaluation of the proposed method, including its performance on standard continual learning benchmarks and its comparison to existing methods. The evaluation should include a detailed analysis of the method's performance under different chunk sizes and data distributions. The authors should also discuss the limitations of the proposed method and suggest directions for future research.

### Questions

1. What is the motivation for studying the chunking problem? How does it affect the performance of continual learning methods?

2. How does the chunking problem differ from other continual learning problems, such as task-incremental or domain-incremental learning?

3. What are the theoretical properties of the per-chunk weight averaging method?

4. How does the proposed method compare to existing continual learning methods in terms of performance and computational cost?

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
