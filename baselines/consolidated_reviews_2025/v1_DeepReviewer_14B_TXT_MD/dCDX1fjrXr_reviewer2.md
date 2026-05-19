### Summary

This paper proposes a new problem setting, Sparse Label Node Classification (SLNC), which aims to address the challenge of performing well with only a few labeled nodes at training time, regardless of class. The authors introduce a framework called ELI (Estimating Label Information) to tackle this problem. ELI leverages unsupervised learning to estimate label information from a pseudo space and uses this information to enhance reformulations of well-known semi-supervised learning frameworks and guide the labeled nodes selection process for training.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

1. The authors introduce a new problem setting called Sparse Labels Node Classification (SLNC), which addresses the challenge of having only a few labeled nodes at training time, regardless of class. This problem setting differs from the traditional Semi-Supervised Node Classification (SSNC) setting.
2. The authors propose a framework called ELI (Estimating Label Information) to address the SLNC problem. ELI leverages unsupervised learning techniques to estimate label information from a pseudo space and uses this information to enhance reformulations of well-known semi-supervised learning (SSL) frameworks.
3. The authors demonstrate that their approach outperforms baselines on SLNC by 10-20% when the number of labeled nodes seen at training is extremely low.

### Weaknesses

#### Some Related Works


#### comment

1. The authors assume that the number of classes c is known in advance, which may not always be the case in real-world scenarios. This assumption limits the applicability of the proposed framework in situations where the class structure is unknown or needs to be inferred from the data itself. The performance of the method could be significantly impacted if the assumed number of classes deviates from the true number of classes, leading to potential misclassification errors.
2. The authors do not provide a baseline comparison with other methods that do not require the number of classes to be known in advance. This makes it difficult to assess the relative performance of the proposed method compared to existing approaches that are more robust to unknown class numbers. Without such comparisons, it is unclear whether the proposed method offers a significant advantage over existing techniques or if it simply performs well under the specific assumption of known class numbers.
3. The authors do not provide a baseline comparison with other methods that select labeled nodes on a per-class basis. This makes it difficult to assess the effectiveness of the proposed method compared to existing approaches that are specifically designed to handle imbalanced or sparse labeling scenarios. It is important to understand how the proposed method performs in comparison to methods that explicitly address the challenge of selecting labeled nodes in a class-balanced manner, especially when some classes have very few labeled examples.

### Suggestions

The authors should investigate the sensitivity of their method to the assumed number of classes. Specifically, they should conduct experiments where the assumed number of classes differs from the true number of classes to understand how the performance degrades under such conditions. This analysis should include both cases where the assumed number of classes is higher and lower than the true number. Furthermore, the authors should explore methods to estimate the number of classes from the data itself, potentially incorporating techniques from clustering or anomaly detection. This would make the proposed framework more robust and applicable to real-world scenarios where the number of classes is not known a priori. The authors should also consider incorporating a mechanism to adaptively adjust the number of classes during the training process based on the observed data distribution.

To address the lack of comparative analysis, the authors should include a comprehensive evaluation against existing semi-supervised learning methods that do not require prior knowledge of the number of classes. This comparison should include a variety of methods, such as those based on graph convolutional networks, contrastive learning, or self-training. The evaluation should be performed on a range of datasets with varying characteristics, including different numbers of classes, nodes, and graph densities. The authors should also provide a detailed analysis of the computational complexity of their method compared to the baselines, including the time and memory requirements. This analysis should help to understand the trade-offs between performance and computational cost.

Finally, the authors should compare their method against existing techniques that explicitly select labeled nodes on a per-class basis. This comparison should include methods that use active learning strategies or other techniques to ensure a balanced representation of classes in the labeled set. The authors should also analyze the performance of their method under different levels of class imbalance in the labeled data. This analysis should help to understand the limitations of the proposed method and identify scenarios where it may not be the most appropriate choice. The authors should also consider incorporating a mechanism to dynamically adjust the labeled node selection process based on the observed performance of the model during training.

### Questions

1. How does the performance of the proposed framework change when the number of classes is not known in advance?
2. How does the proposed framework compare to other methods that do not require the number of classes to be known in advance?
3. How does the proposed framework compare to other methods that select labeled nodes on a per-class basis?

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
