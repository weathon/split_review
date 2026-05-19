### Summary

This paper investigates the continual learning (CL) problem when the data is presented in chunks. The authors show that the performance drop between offline learning and CL from chunking is due to forgetting. They also show that current CL methods do not tackle the chunking problem at all. They propose a simple method, per-chunk weight averaging, to improve performance in the chunking setting and show that it transfers to the full CL setting.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The paper is well-organized and easy to follow.
2. The authors provide a thorough analysis of the chunking setting and demonstrate that it is a significant problem in CL.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a clear definition of the chunking problem and how it differs from other continual learning problems. The authors should provide a more rigorous definition of the chunking problem and clarify its unique characteristics compared to task-incremental or domain-incremental learning.
2. The paper does not provide a clear motivation for why the chunking problem is important or how it affects the performance of continual learning methods. The authors should elaborate on the practical implications of the chunking problem and its relevance to real-world applications.
3. The paper does not provide a comprehensive comparison of the proposed method with existing continual learning methods. The authors should compare their method with a wider range of state-of-the-art continual learning algorithms and provide a more detailed analysis of the results.
4. The paper does not discuss the limitations of the proposed method and potential future research directions. The authors should acknowledge the limitations of their approach and suggest potential avenues for future research.

### Suggestions

The paper would benefit from a more precise definition of the 'chunking problem' within the context of continual learning. Currently, the paper introduces the concept but does not clearly articulate what constitutes a 'chunk' in the data stream, how these chunks are presented to the model, and what specific challenges arise from this presentation. For instance, are the chunks sampled randomly, or is there a specific sampling strategy? What is the size of the chunks, and how does this size affect the learning process? Furthermore, the paper should explicitly contrast the chunking problem with other continual learning scenarios, such as task-incremental or domain-incremental learning, by highlighting the unique challenges posed by the sequential presentation of data chunks. This would help to establish the novelty and importance of the problem being addressed. A more rigorous definition would also help in understanding the scope of the proposed method and its potential limitations.

To strengthen the paper, the authors should provide a more compelling motivation for the importance of addressing the chunking problem in continual learning. The paper should elaborate on the practical implications of this problem and its relevance to real-world applications. For example, in online learning settings, data might arrive in batches, and in some applications, data might be processed in fixed-size chunks due to memory constraints. The authors should provide concrete examples of scenarios where the chunking problem is a significant issue and how it impacts the performance of continual learning methods. This would help to justify the need for a dedicated solution and highlight the potential benefits of the proposed method. Additionally, the authors should discuss the limitations of their approach and potential avenues for future research. This would provide a more balanced perspective on the contributions of the paper and its potential impact on the field.

Finally, the paper needs a more comprehensive experimental evaluation of the proposed method. The authors should compare their method with a wider range of state-of-the-art continual learning algorithms, including both regularization-based and replay-based methods. The evaluation should also consider different datasets and chunk sizes to assess the robustness of the proposed method. Furthermore, the authors should provide a more detailed analysis of the experimental results, including a discussion of the strengths and weaknesses of their method compared to other approaches. For example, they could analyze the performance of their method under different forgetting metrics and compare it with the performance of other methods under the same metrics. This would provide a more comprehensive understanding of the effectiveness of the proposed method and its limitations. The authors should also consider including ablation studies to analyze the impact of different components of their method.

### Questions

Please see the weakness part.

### Rating

3: reject, not good enough

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
