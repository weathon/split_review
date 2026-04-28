# Cross-Domain Offline Policy Adaptation with Optimal Transport and Dataset Constraint

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 6, 8

## Abstract
Offline reinforcement learning (RL) often struggles with limited data. This work explores cross-domain offline RL where offline datasets (with possibly sufficient data) from another domain can be accessed to facilitate policy learning. However, the underlying environments of the two datasets may have dynamics mismatches, incurring inferior performance when simply merging the data of two domains. Existing methods mitigate this issue by training domain classifiers, using contrastive learning methods, etc. Nevertheless, they still rely on a large amount of target domain data to function well. Instead, we address this problem by establishing a concrete performance bound of a policy given datasets from two domains. Motivated by the theoretical insights, we propose to align transitions in the two datasets using optimal transport and selectively share source domain samples, without training any neural networks. This enables reliable data filtering even given a few target domain data. Additionally, we introduce a dataset regularization term that ensures the learned policy remains within the scope of the target domain dataset, preventing it from being biased towards the source domain data. Consequently, we propose the Optimal Transport Data Filtering (dubbed OTDF) method and examine its effectiveness by conducting extensive experiments across various dynamics shift conditions (e.g., gravity shift, morphology shift), given limited target domain data. It turns out that OTDF exhibits superior performance on many tasks and dataset qualities, often surpassing prior strong baselines by a large margin.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a novel method named Optimal Transport Data Filtering (OTDF) for cross-domain offline policy adaptation. Previous works still need a comparatively large target domain dataset to learn domain classifiers or filtering via mutual information. In this paper, the authors provide a performance bound to identify the factors of the performance deviation. This paper proposes to use optimal transport to align data distributions and a regularization term to ensure the learned policy remains within the target domain’s span. The empirical study shows that OTDF outperforms existing methods in cross-domain offline policy adaptation.

### Strengths
- The paper introduces a theoretical analysis of the performance bound in cross-domain offline policy adaptation, providing a clear foundation for the proposed method.
- The optimal transport-based data filtering method is motivated and efficient to compute the Wasserstein distance between source and target domains and filter the source data accordingly.
- The empirical results across various environments and types of dynamics shifts demonstrate that OTDF significantly outperforms baseline methods based on the IQL.

### Weaknesses
 - The proposed practical implementation of OTDF still needs to learn a conditional variational auto-encoder to estimate the behavior polic which may introduce additional computational overhead.
- The paper argues that the proposed method can use a small target domain dataset however the detailed explanation of theoretical and empirical analysis is still limited.
- Ablation study on the proposed method is limited and the comparison with other dynamic model-based methods or adaptive transfer learning approaches is not comprehensive.

### Questions
- Can you provide more insights on using the small amount of target domain data in the proposed method? Can you provide a more detailed explanation from the theoretical and empirical sides?
- Can you explain more about the CVAE you used in the proposed method? Why use the CVAE to estimate the behavior policy? How does the CVAE affect the performance of the proposed method?
- Can you discuss and cite more related works on cross-domain policy adaptation such as [1], [2], and [3], and how the proposed method compares to these methods?
- Can you explain why use the different performance level target domain dataset from the source domain dataset in the empirical study? For example, why use the medium dataset in the source domain combined with the expert dataset in the target domain? Is it a reasonable setting for cross-domain policy adaptation?
- Do you have any results for other offline RL backbones like CQL, BCQ, or BEAR? How does the proposed method compare to these methods in cross-domain offline policy adaptation?

[1] When to trust your simulator: Dynamics-aware hybrid offline-and-online reinforcement learning

[2] Off-Dynamics Reinforcement Learning via Domain Adaptation and Reward Augmented Imitation

[3] Return Augmented Decision Transformer for Off-Dynamics Reinforcement Learning

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the challenge of cross-domain offline reinforcement learning (RL) where the goal is to leverage a source domain dataset to improve policy learning in a target domain with limited data. This paper identifies that directly merging data from different domains can lead to performance degradation due to dynamics mismatches. To mitigate this, they propose a method called Optimal Transport Data Filtering (OTDF), which aligns transitions from source and target domains using optimal transport, selectively shares source domain samples, and introduces a dataset regularization term to keep the learned policy within the scope of the target domain dataset. The effectiveness of OTDF is evaluated across various dynamics shift conditions with limited target domain data, demonstrating superior performance over strong baselines.

### Strengths
1. This paper introduces a novel approach to cross-domain offline RL by combining optimal transport with dataset regularization, which is a unique combination not commonly seen in the literature.
2. The authors provide a solid theoretical foundation for their method, characterizing the performance bound of a policy and motivating their approach with theoretical insights

### Weaknesses
1. In previous studies, DARA, BOSA, and IGDF all utilize source and target domain data of similar quality, implying that the state space distributions of the datasets were closely aligned. This alignment ensures, to some extent, that there is a certain overlap between the source and target domain data. Your setting differs from theirs, which naturally raises the question of whether data filtering or policy regularization played the critical role. As the results in Figure 3 indicate, the introduction of policy regularization has a highly significant impact on the performance of the algorithm. However, in previous methods such as SRPO and IGDF, constraints related to this were not designed, which may account for the significant performance improvement observed in OTDF.

2. In the paper "Cross-domain imitation learning via optimal transport, ICLR 2022," some methods for cross-domain transfer based on optimal transport have already been adopted. What do you think are the differences between your method and the previous methods in terms of implementation?

### Questions
1. Table 1 is too wide and not pleasing enough. Recommend using \resizebox {\linewidth} {!} to fix it.
2. Why is the performance of IQL not assessed when using only source domain data?
3. The paper does not provide the impact of using OT for data filtering or subsequent policy regularization on the performance bound of OTDF. A sub-optimal gap is expected to be given.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This work proposes a new cross-domain offline RL method OTDF, which can leverage data from source domain to help the learning of the target domain. This work proposes that the core of the cross-domain offline RL is the dynamics mismatch between source and target domain, and introduces a threshold and a weight to only leverage those data close to the target domain in the source domain.

### Strengths
- This work proposes an informative proof and well-designed method. Also, this work can be a well baseline for follow-up works.

### Weaknesses
The $\mu_{t,t'}$ is not defined in Eq. 1.

### Questions
Can a more complex kinematic shift be proposed?

### Soundness
4

### Presentation
3

### Contribution
3
