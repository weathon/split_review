### Summary

This paper investigates the continual learning problem in the context of data chunking, where the data is presented in chunks instead of a full dataset. The authors show that the performance drop between offline and continual learning is largely due to forgetting, and that current continual learning methods do not address the chunking problem. They propose per-chunk weight averaging to improve performance in the chunking setting and demonstrate its effectiveness in standard continual learning benchmarks.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The paper provides a thorough analysis of the chunking problem in continual learning, highlighting its importance and impact on performance.
2. The proposed per-chunk weight averaging technique is simple yet effective, showing significant improvements in continual learning benchmarks.
3. The paper is well-organized and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a clear definition of the chunking problem and how it differs from other continual learning problems. The authors should provide a more rigorous definition of the chunking problem and clarify its unique characteristics compared to task-incremental or domain-incremental learning.
2. The paper does not provide a clear motivation for why the chunking problem is important or how it affects the performance of continual learning methods. The authors should elaborate on the practical implications of the chunking problem and its relevance to real-world applications.
3. The paper does not provide a comprehensive comparison of the proposed method with existing continual learning methods. The authors should compare their method with a wider range of state-of-the-art continual learning algorithms and provide a more detailed analysis of the results.
4. The paper does not discuss the limitations of the proposed method and potential future research directions. The authors should acknowledge the limitations of their approach and suggest potential avenues for future research.

### Suggestions

The paper needs to clearly define the chunking problem, specifying the exact nature of the data chunks and how they are presented to the learning algorithm. For example, are the chunks sampled randomly, or is there a specific sampling strategy? What is the size of the chunks, and how does this size affect the learning process? Furthermore, the paper should explicitly contrast the chunking problem with other continual learning scenarios, such as task-incremental or domain-incremental learning, by highlighting the unique challenges posed by the sequential presentation of data chunks. This would help to establish the novelty and importance of the problem being addressed. The authors should also provide a more detailed explanation of why the chunking problem is a significant issue in continual learning, perhaps by discussing scenarios where chunking naturally occurs and its impact on model performance. For example, in online learning settings, data might arrive in batches, and in some applications, data might be processed in fixed-size chunks due to memory constraints. 

To strengthen the paper, the authors should conduct a more comprehensive experimental evaluation of their proposed method. This should include a comparison with a wider range of state-of-the-art continual learning algorithms, such as regularization-based methods, replay-based methods, and parameter isolation techniques. The evaluation should also consider different datasets and chunk sizes to assess the robustness of the proposed method. Furthermore, the authors should provide a more detailed analysis of the experimental results, including a discussion of the strengths and weaknesses of their method compared to other approaches. For example, they could analyze the performance of their method under different forgetting metrics and compare it with the performance of other methods under the same metrics. This would provide a more comprehensive understanding of the effectiveness of the proposed method and its limitations. The authors should also consider including ablation studies to analyze the impact of different components of their method, such as the per-chunk weight averaging technique.

Finally, the paper should include a more thorough discussion of the limitations of the proposed method and potential future research directions. The authors should acknowledge the assumptions made in their analysis and discuss how these assumptions might affect the generalizability of their results. For example, they could discuss the limitations of their method in scenarios where the data chunks are highly correlated or where the chunk size is very small. They should also suggest potential avenues for future research, such as exploring alternative weight averaging techniques or developing new methods specifically designed for the chunking problem. This would help to provide a more complete picture of the contributions of the paper and its potential impact on the field of continual learning.

### Questions

1. How does the proposed method handle the case where the data chunks are highly correlated or have a large overlap between chunks?
2. What is the computational cost of the proposed method compared to other continual learning methods?
3. How does the proposed method perform when the chunk size is very small or very large?

### Rating

3: reject, not good enough

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
