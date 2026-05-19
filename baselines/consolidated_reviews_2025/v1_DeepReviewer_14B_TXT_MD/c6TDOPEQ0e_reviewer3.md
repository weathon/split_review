### Summary

This paper proposes LASP-2, an improved version of LASP, to enhance the communication and computation efficiency of linear attention models. LASP-2 reduces the communication overhead by using a single all-gather operation, which is independent of the sequence length. The authors also extend LASP-2 to LASP-2H, which supports hybrid models with both linear and standard attention layers. The experiments show that LASP-2 achieves better throughput and scalability than existing methods on very long sequences.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow. The authors provide a clear motivation and a detailed description of the proposed method.
2. The paper addresses an important problem of training linear attention models on very long sequences, which is challenging for existing methods due to the high communication cost.
3. The paper proposes a novel and effective solution of using a single all-gather operation to reduce the communication overhead, which is independent of the sequence length.
4. The paper extends the proposed method to support hybrid models with both linear and standard attention layers, which increases the applicability of the method.
5. The paper provides a comprehensive evaluation of the proposed method on various linear attention models and sequence lengths, and shows that it outperforms existing methods in terms of throughput and scalability.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a theoretical analysis of the communication and computation complexity of the proposed method, which is important for understanding the scalability and efficiency of the method. Specifically, a formal analysis of how the all-gather operation scales with the number of devices and sequence length is missing. This makes it difficult to predict the performance of LASP-2 on different hardware configurations and model sizes.
2. The paper does not compare the proposed method with other state-of-the-art methods for training linear attention models, such as RetNet and GLA, which are also designed for efficient training on long sequences. A direct comparison with these methods, including a breakdown of the performance differences, would be beneficial to understand the relative advantages and disadvantages of LASP-2.
3. The paper does not evaluate the proposed method on downstream tasks, such as language modeling or image classification, which is important for verifying the effectiveness of the method in real-world applications. The paper only focuses on training efficiency and does not demonstrate the practical impact of the proposed method on the quality of the trained models.

### Suggestions

The paper would benefit from a more detailed theoretical analysis of the communication and computation complexity of LASP-2. This analysis should include a formal derivation of the communication cost as a function of the number of devices, sequence length, and model dimensionality. Furthermore, the analysis should consider the impact of different communication topologies on the overall performance. For example, the analysis could explore how the all-gather operation's latency and bandwidth requirements affect the scalability of the method. This theoretical analysis would provide a more solid foundation for the proposed method and allow for better prediction of its performance on different hardware configurations. Additionally, it would be beneficial to include a comparison of the theoretical complexity of LASP-2 with existing methods, such as Ring Attention, to highlight the advantages of the proposed approach.

To strengthen the empirical evaluation, the paper should include a direct comparison with other state-of-the-art methods for training linear attention models, such as RetNet and GLA. This comparison should not only focus on training throughput but also on the convergence speed and the final performance of the trained models. The authors should provide a detailed breakdown of the performance differences, including the impact of different hyperparameters and model configurations. This would allow for a more comprehensive understanding of the relative advantages and disadvantages of LASP-2 compared to existing methods. Furthermore, the evaluation should include a comparison of the memory usage of LASP-2 with other methods, as memory efficiency is also a critical factor for training large models on long sequences.

Finally, the paper should include an evaluation of the proposed method on downstream tasks to demonstrate its practical impact. This evaluation should include a variety of tasks, such as language modeling, image classification, and other relevant applications. The authors should compare the performance of models trained with LASP-2 with models trained with other methods, including standard attention and other linear attention variants. This would provide a more complete picture of the effectiveness of the proposed method and its potential for real-world applications. The evaluation should also consider the impact of different sequence lengths on the downstream task performance, as this is a key aspect of the proposed method.

### Questions

1. How does the proposed method compare with other state-of-the-art methods for training linear attention models, such as RetNet and GLA, in terms of throughput and scalability?
2. How does the proposed method affect the convergence speed and the final performance of the trained models on downstream tasks?
3. How does the proposed method handle the numerical instability of linear attention, especially when the sequence length is very long?

### Rating

6

### Confidence

3

**********
