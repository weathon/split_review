### Summary

This paper addresses the challenge of architecture overfitting in dataset distillation, where distilled data created by one network architecture performs poorly on others. The authors propose several methods to improve generalization across architectures, including a modified DropPath technique, knowledge distillation from smaller networks, and stronger data augmentation. Through extensive experiments, they show their approaches achieve comparable or superior results to existing methods, especially with larger networks trained on distilled data.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to understand.
2. The issue of dataset distillation is important for the dataset distillation community.
3. The experiments are extensive.

### Weaknesses

#### Some Related Works

[1] Gradient-based optimization for dataset distillation
[2] Dataset distillation by matching training and test loss trajectories

#### comment

1. The proposed methods are not novel, e.g., DropPath and knowledge distillation are existing methods.
2. The authors only compare their methods with MTT and MTT+DP, while neglecting the comparison with other dataset distillation methods such as [1] and [2].
3. The authors only conduct experiments on CIFAR-10 and CIFAR-100, while neglecting the comparison on larger datasets such as ImageNet-1K.

### Suggestions

The paper's primary weakness lies in its incremental contribution. While the combination of DropPath and knowledge distillation is presented as a solution to architecture overfitting in distilled datasets, the individual components are well-established techniques. The paper lacks a thorough analysis of why this specific combination is particularly effective for this problem, beyond empirical results. A deeper investigation into the interaction between DropPath's stochastic depth and the regularization effect of knowledge distillation would strengthen the novelty claim. For example, the authors could analyze how DropPath affects the feature space of the distilled data and how this interacts with the knowledge distillation process. Furthermore, the paper should explore alternative regularization techniques or architectural modifications that could achieve similar or better results, providing a more comprehensive understanding of the problem space.

Another significant limitation is the narrow scope of the experimental evaluation. The comparison is primarily limited to MTT and its variant, neglecting other prominent dataset distillation methods. This makes it difficult to assess the true effectiveness of the proposed approach relative to the state-of-the-art. The authors should include a wider range of dataset distillation techniques, such as those based on gradient matching or trajectory matching, to provide a more robust evaluation. Moreover, the experiments are confined to CIFAR-10 and CIFAR-100, which are relatively small datasets. The performance of the proposed method on larger and more complex datasets, such as ImageNet-1K, remains unclear. The authors should extend their experiments to include such datasets to demonstrate the scalability and generalizability of their approach. This would also help to identify potential limitations of the method when applied to more challenging scenarios.

Finally, the paper would benefit from a more detailed analysis of the computational overhead introduced by the proposed methods. While DropPath is generally efficient, the knowledge distillation process can be computationally expensive, especially when using larger teacher networks. The authors should provide a quantitative analysis of the training time and memory requirements of their approach, comparing it to the baseline methods. This would allow readers to better understand the trade-offs between performance and computational cost. Additionally, the authors should explore techniques to mitigate the computational burden of knowledge distillation, such as using smaller teacher networks or more efficient distillation strategies. This would make the proposed method more practical for real-world applications.

### Questions

Please refer to the weaknesses.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
