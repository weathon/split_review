### Summary

This paper proposes a meta-learning based method to improve the generalization of foundation models. Specifically, the authors consider the scenario where a foundation model is first pretrained on a set of tasks and then fine-tuned on a downstream task. They show that the standard retraining approach cannot recover the ground-truth parameters after fine-tuning with low-rank adapters. To address this issue, the authors propose a meta-learning objective that explicitly considers the fine-tuning process and the low-rank adapters. They provide theoretical analysis to show that their proposed method can provably achieve good performance. Experiments on both synthetic data and the ConvAI2 dataset demonstrate the effectiveness of the proposed method.

### Soundness

3

### Presentation

3

### Contribution

3

### Strengths

1. The paper is well-written and easy to follow. The authors provide a clear motivation for their work and a detailed explanation of their proposed method.

2. The authors provide a thorough theoretical analysis of the proposed method, including proofs of convergence and generalization bounds. The theoretical analysis is well-supported by empirical results.

3. The authors conduct extensive experiments to validate their theoretical findings and demonstrate the effectiveness of their proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The authors only consider the linear model in their theoretical analysis. It is unclear whether the theoretical results can be extended to more complex models, such as neural networks. Specifically, the analysis relies on the properties of linear transformations and low-rank matrices, which may not directly translate to the non-linear transformations and high-dimensional parameter spaces encountered in deep learning. The theoretical guarantees provided may not hold for more complex architectures, limiting the practical applicability of the theoretical results.

2. The authors only consider the LoRA-based fine-tuning method. It is unclear whether the proposed method can be extended to other fine-tuning methods, such as adapter-based fine-tuning or prompt-based fine-tuning. The LoRA method modifies the weight matrices directly, which might have specific properties that are leveraged by the proposed meta-learning objective. It is not clear if the same performance gains can be achieved with other parameter-efficient fine-tuning techniques that operate on different parts of the model or use different parameterizations. This limits the generality of the proposed approach.

3. The authors only consider the case where the ground-truth parameters are low-rank. It is unclear how the proposed method would perform if the ground-truth parameters are not low-rank. The theoretical analysis and empirical results are based on the assumption that the underlying parameter differences are low-rank, which may not hold in many real-world scenarios. This assumption could limit the applicability of the method to tasks where the parameter differences are not well-approximated by low-rank matrices.

### Suggestions

The authors should investigate the applicability of their theoretical results to non-linear models. This could involve exploring the use of tools from non-linear functional analysis or developing new theoretical frameworks that can accommodate non-linearities. For example, they could analyze the behavior of their meta-learning objective when applied to shallow neural networks with non-linear activation functions. This would provide a more comprehensive understanding of the method's performance in realistic scenarios. Furthermore, it would be beneficial to explore the conditions under which the low-rank assumption holds for the parameter differences in non-linear models. This could involve analyzing the spectral properties of the parameter differences or developing new metrics to quantify the low-rankness of the parameter differences.

To address the limited scope of fine-tuning methods, the authors should investigate the performance of their proposed method with other parameter-efficient fine-tuning techniques. This could involve adapting their meta-learning objective to work with adapter-based fine-tuning or prompt-based fine-tuning. For example, they could explore how to incorporate the parameter updates from these methods into their meta-learning objective. This would demonstrate the generality of their approach and its potential for use with a wider range of fine-tuning techniques. It would also be useful to compare the performance of their method with other meta-learning approaches that are specifically designed for fine-tuning.

Finally, the authors should explore the performance of their method when the ground-truth parameters are not low-rank. This could involve analyzing the behavior of their method when the parameter differences are not well-approximated by low-rank matrices. They could also explore techniques for adapting their method to handle non-low-rank parameter differences. For example, they could investigate the use of more flexible parameterizations or develop new meta-learning objectives that are less sensitive to the low-rank assumption. This would make their method more robust and applicable to a wider range of tasks.

### Questions

1. Can the authors provide more details on how to extend their theoretical analysis to non-linear models?

2. Can the authors provide more details on how to extend their method to other fine-tuning methods, such as adapter-based fine-tuning or prompt-based fine-tuning?

3. Can the authors provide more details on how their method would perform if the ground-truth parameters are not low-rank?

### Rating

6

### Confidence

3

**********
