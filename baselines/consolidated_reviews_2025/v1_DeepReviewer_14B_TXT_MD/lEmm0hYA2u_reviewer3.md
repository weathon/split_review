### Summary

This paper proposes a novel zero-shot quantization (ZSQ) framework, named ZeroP, that leverages publicly available data - proxy data (PD) - as a substitute for the OD. The authors first explore the impact of PD on the performance of current ZSQ methods over 16 different computer vision datasets and introduce a simple and effective PD selection method based on batch-normalization statistics(BNS) to select the optimal PD. The authors then apply ZeroP to three state-of-the-art pure-SD (using only SD) methods, achieving 7% to 16% improvements in accuracy for MobileNetV1 on ImageNet-1K in a 4-bit setting. Furthermore, the authors demonstrate the effectiveness of ZeroP on extensive models and datasets.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow.
2. The motivation of this paper is clear and reasonable.
3. The performance seems to outperform the SOTA methods.

### Weaknesses

#### Some Related Works


#### comment

1. The novelty of this paper seems to be limited. The proxy data has been used in the ZSQ, which reduces the contribution of this paper.
2. The authors should provide the comparison of the inference latency between the proposed method and other competitors.
3. The authors should provide the comparison of the model size between the proposed method and other competitors.
4. The authors should provide the comparison of the FLOPs between the proposed method and other competitors.
5. The authors should provide the comparison of the energy consumption between the proposed method and other competitors.

### Suggestions

The paper's primary weakness lies in its limited novelty. While the use of proxy data in zero-shot quantization (ZSQ) is not entirely new, the authors should more clearly articulate the specific differences and advantages of their approach compared to existing methods. A more thorough discussion of how their method differs from prior work, particularly in the context of proxy data selection and utilization, is needed. For example, the authors could elaborate on the specific types of proxy data they use, how they select it, and why this selection is superior to other approaches. Furthermore, a more detailed analysis of the limitations of existing ZSQ methods that rely solely on synthetic data would strengthen the motivation for their work. The authors should also consider a more rigorous ablation study to demonstrate the impact of each component of their proposed framework, particularly the proxy data selection method based on batch-normalization statistics (BNS). This would help to isolate the contribution of each element and provide a more comprehensive understanding of the method's effectiveness.

In addition to the novelty concerns, the paper lacks a comprehensive evaluation of the practical implications of the proposed method. The authors should provide a more detailed analysis of the inference latency, model size, FLOPs, and energy consumption of their method compared to other state-of-the-art techniques. This is crucial for assessing the real-world applicability of the proposed approach. For instance, while the authors demonstrate accuracy improvements, it is important to understand the trade-offs in terms of computational cost and energy efficiency. A comparison of these metrics across different hardware platforms would also be beneficial. The authors should also consider providing a more detailed analysis of the method's performance across different network architectures and datasets. This would help to establish the generalizability of the proposed approach and identify potential limitations. Furthermore, a discussion of the sensitivity of the method to different hyperparameter settings would be valuable.

Finally, the authors should provide a more in-depth analysis of the batch-normalization statistics (BNS) based proxy data selection method. While the paper introduces this method, a more detailed explanation of the underlying theory and the specific advantages of using BNS for proxy data selection is needed. For example, the authors could discuss how BNS captures the distribution of the data and why this is a suitable metric for selecting proxy data. A comparison of BNS with other potential metrics for proxy data selection would also be beneficial. Furthermore, the authors should provide a more detailed analysis of the impact of the proxy data size on the performance of the proposed method. This would help to understand the trade-offs between proxy data size and computational cost. The authors should also consider exploring the use of different types of proxy data and their impact on the performance of the proposed method.

### Questions

Please see the Weaknesses.

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
