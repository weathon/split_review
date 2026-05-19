### Summary

This paper introduces LASP-2, a new sequence parallelism (SP) approach designed to enhance both communication and computation efficiency in linear attention transformer models with very-long input sequences. LASP-2 rethinks the minimal communication requirement for SP on linear attention and reorganizes the whole communication-computation order of LASP-1. It only needs one single all-gather collective communication on intermediate memory states, whose sizes are independent of the sequence length. Additionally, the paper extends LASP-2 to LASP-2H by applying similar communication redesign to standard attention modules, offering an efficient SP solution for hybrid models that combine linear and standard attention layers. The evaluation demonstrates the effectiveness of LASP-2 and LASP-2H on a Linear-Llama3 model.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. This paper proposes LASP-2, which improves both communication and computation parallelism, as well as their overlap, by rethinking the minimal communication requirement for SP on linear attention and reorganizes the whole communication-computation order of LASP-1. 
2. The evaluation shows that LASP-2 achieves throughput improvements of 15.2% over LASP-1 and 36.6% over Ring Attention, with a sequence length of 2048K across 64 GPUs.

### Weaknesses

#### Some Related Works


#### comment

1. The evaluation only compares LASP-2 with LASP-1 and Ring Attention. It would be better to include more baselines, such as other SP methods for linear attention or hybrid models. Specifically, comparisons with other state-of-the-art sequence parallelism techniques, especially those designed for long sequences, would provide a more comprehensive understanding of LASP-2's performance relative to the broader landscape of solutions. The absence of such comparisons makes it difficult to ascertain the true novelty and effectiveness of the proposed approach.
2. The paper only evaluates LASP-2 on the Linear-Llama3 model. It would be better to evaluate LASP-2 on more models and datasets to show the generalization ability. The current evaluation is limited to a single model architecture, which raises concerns about the general applicability of LASP-2. Evaluating on diverse models, including those with different attention mechanisms and layer configurations, would be necessary to demonstrate the robustness and generalizability of the proposed method. Furthermore, the evaluation should include a variety of datasets with different characteristics to ensure the method's effectiveness across different data distributions.

### Suggestions

To strengthen the evaluation, the authors should include comparisons with additional state-of-the-art sequence parallelism methods, particularly those designed for long sequences. This should include methods that employ different communication strategies and parallelization techniques. For instance, comparing against methods that utilize pipelining or tensor partitioning would provide a more complete picture of LASP-2's performance. Furthermore, the evaluation should not only focus on throughput but also consider metrics such as scalability, memory usage, and communication overhead. A detailed analysis of these metrics would provide a more nuanced understanding of the strengths and weaknesses of LASP-2 compared to other approaches. The authors should also provide a more detailed explanation of the implementation details of the baselines, including any specific optimizations or configurations used, to ensure a fair comparison.

To address the concern about the limited evaluation scope, the authors should evaluate LASP-2 on a wider range of models and datasets. This should include models with different attention mechanisms, such as standard attention and other variants of linear attention, as well as models with varying layer configurations. Evaluating on diverse datasets with different characteristics, such as different sequence lengths and data distributions, would also be crucial to demonstrate the generalizability of LASP-2. The authors should also consider evaluating on tasks beyond pretraining, such as finetuning and inference, to provide a more comprehensive assessment of the method's practical utility. This would help to demonstrate the method's effectiveness in real-world scenarios.

Finally, the authors should provide a more detailed analysis of the communication and computation costs of LASP-2, including a breakdown of the time spent on different operations. This analysis should consider the impact of different sequence lengths, model sizes, and hardware configurations on the performance of LASP-2. The authors should also discuss the limitations of LASP-2 and identify potential areas for future research. This would provide a more complete understanding of the method's strengths and weaknesses and help to guide future work in this area.

### Questions

1. How does LASP-2 compare to other SP methods for linear attention, such as [a] [b]?
2. Can the authors evaluate LASP-2 on other models and datasets? This would help to demonstrate the generalization ability of LASP-2.
3. What is the communication overhead of LASP-2 on different network topologies and sequence lengths? The authors should provide a detailed analysis of the communication cost of LASP-2.

### Rating

6

### Confidence

3

**********
