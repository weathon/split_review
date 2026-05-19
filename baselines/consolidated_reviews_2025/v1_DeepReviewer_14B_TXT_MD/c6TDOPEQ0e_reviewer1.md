### Summary

This paper proposes a sequence parallelism (SP) approach, LASP-2, to improve the training efficiency of linear attention transformer models with very-long input sequences. LASP-2 redesigns the communication protocol to use an all-gather operation, which reduces the communication overhead and allows for better overlap of communication and computation. The authors also extend LASP-2 to LASP-2H, which is applicable to hybrid models that combine linear and standard attention. The experiments show that LASP-2 achieves significant throughput improvements over existing methods on a 64-GPU system.

### Soundness

3

### Presentation

3

### Contribution

2

### Strengths

1. LASP-2 is well-motivated and effectively addresses the communication bottleneck of existing SP methods for linear attention. The use of all-gather is a simple but effective solution that reduces the communication cost and improves the parallelism.

2. The paper is clearly written and easy to follow. The authors provide a comprehensive analysis of the communication and computation costs of LASP-2 and LASP-1, which demonstrates the advantage of the proposed method.

3. The experimental results are promising and demonstrate the scalability of LASP-2 on long sequences and large models. The authors also validate the effectiveness of LASP-2H for hybrid models.

### Weaknesses

#### Some Related Works


#### comment

1. The novelty of LASP-2 is somewhat limited. The core idea of using all-gather is not new and has been used in other contexts. The authors should clearly differentiate LASP-2 from existing SP methods for standard attention. Specifically, while the application to linear attention is presented as a key contribution, the core communication strategy appears to be a direct adaptation of existing techniques. The paper needs to more clearly articulate the specific challenges in linear attention that necessitate this particular all-gather approach, beyond simply stating it improves communication efficiency. A more detailed comparison to existing SP methods, highlighting the specific differences in implementation and challenges addressed by LASP-2, would be beneficial.

2. The experiments only compare LASP-2 with LASP-1, Ring Attention, and Megatron-SP. It would be better to include more baselines, such as other SP methods for linear attention or hybrid models. The current comparison is insufficient to fully demonstrate the superiority of LASP-2. The lack of comparison against other state-of-the-art sequence parallelism techniques, especially those tailored for linear attention or similar architectures, makes it difficult to assess the true impact of the proposed method. The paper should include a more comprehensive set of baselines to provide a more robust evaluation.

3. The authors only evaluate LASP-2 on the Linear-Llama3 model. It would be better to evaluate LASP-2 on more models and datasets to show the generalization ability. The exclusive focus on the Linear-Llama3 model raises concerns about the general applicability of LASP-2. The paper needs to demonstrate that the method is not specific to this particular architecture and can be effectively applied to other models and datasets. The lack of experiments on diverse models and datasets limits the confidence in the generalizability of the proposed approach.

### Suggestions

To address the limited novelty concern, the authors should provide a more detailed explanation of the specific challenges that arise when applying sequence parallelism to linear attention, and how LASP-2's all-gather approach uniquely addresses these challenges. This should go beyond simply stating that it improves communication efficiency. For example, the authors could discuss the specific memory access patterns and computational dependencies in linear attention that make existing SP methods less efficient, and how the all-gather approach mitigates these issues. A more in-depth analysis of the differences between LASP-2 and existing SP methods for standard attention, highlighting the specific adaptations made for linear attention, would strengthen the contribution. This could include a discussion of the specific communication patterns and memory layouts that are unique to linear attention and how LASP-2 leverages these to achieve better performance.

To improve the experimental evaluation, the authors should include a broader range of baselines, specifically other sequence parallelism methods that are applicable to linear attention or similar architectures. This could include methods that use different communication strategies or hybrid parallelism approaches. The comparison should not only focus on throughput but also consider other metrics such as scalability and memory usage. Furthermore, the authors should provide a more detailed analysis of the performance bottlenecks of each method, highlighting the specific advantages of LASP-2. This would provide a more comprehensive understanding of the method's strengths and weaknesses. The inclusion of more diverse models and datasets is also crucial to demonstrate the generalizability of LASP-2. The authors should consider evaluating the method on other transformer models that use linear attention, as well as different datasets to show that the method is not specific to the Linear-Llama3 model. This would significantly increase the impact and relevance of the work.

Finally, the authors should provide a more detailed analysis of the limitations of LASP-2. This could include a discussion of the scenarios where the method might not be as effective, such as very short sequences or specific hardware configurations. A thorough discussion of the limitations would provide a more balanced view of the method and help guide future research in this area. The authors should also consider providing an ablation study to analyze the impact of different components of LASP-2, such as the all-gather operation and the communication-computation overlap. This would provide a more detailed understanding of the method's inner workings and help identify areas for further improvement.

### Questions

1. How does LASP-2 compare to other SP methods for linear attention, such as [a][b]? The authors should provide a detailed comparison to show the advantage of LASP-2.

2. Can the authors evaluate LASP-2 on other models and datasets? This would help to demonstrate the generalization ability of LASP-2.

3. What is the communication overhead of LASP-2 on different network topologies and sequence lengths? The authors should provide a detailed analysis of the communication cost of LASP-2.

### Rating

6

### Confidence

4

**********
