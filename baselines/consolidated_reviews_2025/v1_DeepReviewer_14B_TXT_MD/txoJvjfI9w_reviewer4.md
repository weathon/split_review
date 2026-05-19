### Summary

This paper introduces a novel approach to enhance the robustness of large language models (LLMs) against permutation sensitivity in in-context learning (ICL). The authors propose PEARL, a permutation-resilient learning framework, which employs distributionally robust optimization (DRO) to train LLMs against worst-case permutations. The framework includes a hard permutation mining network (P-Net) that identifies challenging permutations using optimal transport and the Sinkhorn algorithm. The paper demonstrates that PEARL significantly improves both the average and worst-case performance of LLMs across various tasks, reducing their vulnerability to permutation-based attacks.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper addresses a critical vulnerability in LLMs, providing a robust solution to the permutation sensitivity problem that has been largely overlooked.
2. The use of distributionally robust optimization (DRO) and the P-Net for identifying challenging permutations is innovative and well-integrated into the learning framework.
3. The experimental results are compelling, showing significant improvements in worst-case performance without sacrificing average performance, which is a notable achievement.

### Weaknesses

#### Some Related Works


#### comment

1. The paper could benefit from a more detailed discussion on the limitations of the proposed method, particularly in scenarios with very large numbers of demonstrations where the number of permutations grows factorially.
2. The authors should consider providing more insights into the practical implications of their method, such as the computational overhead and the potential impact on real-world applications.

### Suggestions

The paper should delve deeper into the practical limitations of the proposed PEARL framework, especially concerning its scalability with increasing numbers of demonstrations. While the authors mention the factorial growth of permutations, a more thorough analysis is needed. For instance, the paper could explore the performance of PEARL when the number of demonstrations exceeds a certain threshold (e.g., 10, 15, or 20), and how the P-Net's ability to identify challenging permutations degrades in such scenarios. It would be beneficial to include experiments that specifically test the boundaries of the method's applicability, perhaps by systematically increasing the number of demonstrations and observing the resulting impact on both average and worst-case performance. This would provide a clearer picture of the method's practical limitations and help identify the range of applications for which it is most suitable. Furthermore, the authors should discuss potential strategies for mitigating the computational burden associated with the increasing number of permutations, such as approximation techniques or sampling methods that could be integrated into the P-Net.

In addition to the scalability concerns, the paper needs to provide a more detailed analysis of the computational overhead introduced by the PEARL framework. The current discussion is somewhat vague, and it would be helpful to quantify the additional training time and memory requirements compared to standard training methods. For example, the authors could provide a breakdown of the computational cost associated with the P-Net, the Sinkhorn algorithm, and the adversarial training process. This analysis should include both training and inference time, as well as memory usage, and should be presented for different model sizes and numbers of demonstrations. Furthermore, the paper should discuss the practical implications of these computational costs for real-world applications. For instance, how would the increased training time affect the development cycle of a new model? How would the additional memory requirements impact the deployment of the model on resource-constrained devices? Addressing these questions would provide a more complete understanding of the practical trade-offs associated with the PEARL framework.

Finally, the paper should explore the potential impact of the PEARL framework on real-world applications in more detail. While the authors mention instruction tuning and many-shot ICL, they should provide concrete examples of how the method could be applied in practice. For instance, how would PEARL improve the performance of an LLM in a specific task, such as question answering or text summarization? What are the potential benefits and drawbacks of using PEARL in these scenarios? The authors should also discuss the potential for integrating PEARL with other techniques, such as retrieval-augmented generation, to further improve the robustness and performance of LLMs. This would help to demonstrate the practical relevance of the proposed method and its potential to address real-world challenges.

### Questions

1. How does the PEARL framework perform when the number of demonstrations is very large (e.g., >10)? Does the factorial growth of permutations pose a computational bottleneck?
2. Can the authors provide more details on the computational overhead introduced by PEARL, especially in terms of training time and memory requirements?
3. How does the performance of PEARL compare to other permutation-handling methods, such as those based on demonstration selection or ensembling, in terms of both effectiveness and efficiency?

### Rating

6

### Confidence

4

**********
