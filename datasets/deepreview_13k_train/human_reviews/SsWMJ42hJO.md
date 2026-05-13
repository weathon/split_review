# Preventing Collapse in Contrastive Learning with Orthonormal Prototypes (CLOP)

- Decision: Reject
- Scores: 5, 5, 5

## Abstract
Contrastive learning has emerged as a powerful method in deep learning, excelling at learning effective representations through contrasting samples from different distributions. However, neural collapse, where embeddings converge into a lower-dimensional space, poses a significant challenge, especially in semi-supervised and self-supervised setups. In this paper, we first theoretically analyze the effect of large learning rates on contrastive losses that solely rely on the cosine similarity metric, and derive a theoretical bound to mitigate this collapse. {Building on these insights, we propose \textbf{CLOP}, a novel semi-supervised loss function designed to prevent neural collapse by promoting the formation of orthogonal linear subspaces among class embeddings.} Unlike prior approaches that enforce a simplex ETF structure, CLOP focuses on subspace separation, leading to more distinguishable embeddings. Through extensive experiments on real and synthetic datasets, we demonstrate that CLOP enhances performance, providing greater stability across different learning rates and batch sizes.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses the dimensional collapse problems within the semi-supervised contrastive learning paradigm. This paper first provides theoretical insights into the influence of large learning rates and cosine similarities on dimensional collapse. To mitigate this issue, the authors introduce a method, termed CLOP, aimed at enhancing subspace separation.  Experimental results on CIFAR and Tiny-ImageNet demonstrate the performance improvements of the algorithm.

### Strengths
1.	The paper tackles the critical issue of dimensional collapse within semi-supervised learning scenarios.
2.	This paper provides some theoretical clues to support their claims.
3.	The paper is generally well structured and easy to follow.

### Weaknesses
1.	The paper appears to conflate two distinct concepts: dimensional collapse and neural collapse. Dimensional collapse in semi-supervised learning (SSL) typically refers to the limited dimensionality of learned SSL features, while neural collapse is associated with a desirable state in supervised training marked by several good qualities such as intra-class alignment and inter-class separation (properties NC1-NC4).
2.	The claim regarding orthogonal structures achieving the most distinguishable classes relative to the Simplex ETF structure is unclear. Simplex ETF theoretically maximizes angular separation, reaching a pairwise cosine value of -1/(k-1), whereas orthogonal structures attain pairwise cosine values of zero. The paper needs to clarify under what conditions the orthogonal structure is superior, especially given that the Simplex ETF is designed for maximal separation.
3.	The issue of dimensional collapse is primarily addressed by the SSL community; however, the paper's focus is on semi-supervised methods, yet it lacks comparison with other semi-supervised baselines. This makes it difficult to assess the true novelty and effectiveness of the proposed method within the relevant context.
4.	The proposed method should be compared with ETF-based(or uniform variants) methods[1] to adequately demonstrate its effectiveness. Moreover, to comprehensively address dimensional collapse, additional self-supervised experiments are recommended, including comparisons with ETF-based SSL methods [2] and other methods targeting dimensional collapse [3,4]. The absence of these comparisons makes it difficult to determine if the method offers a significant advantage over existing approaches.
5.	Experiments are limited to small-scale datasets, such as CIFAR and Tiny-ImageNet, which may restrict the generalizability of the findings. The performance on larger, more complex datasets should be evaluated to ensure the robustness of the method.
6.	The performance improvements are not significant on larger batch sizes. This suggests that the method's effectiveness may be limited to specific training scenarios and may not be as beneficial in more general settings.

### Questions
please refer to the weakness part.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper considers the problem of neural collapse in contrastive learning. The authors theoretically investigate the effect of large learning rate in contrastive learning with cosine similarity and provide a bound for the learning rate to avoid the collapse. The authors also propose a semi-supervised contrastive loss. Experimental results on small image datasets support the claim.

### Strengths
A theoretical upper bound of the learning rate for collapse is provided.

### Weaknesses
 - The definition of neural collapse is incorrect. Neural collapse refers to the phenomenon that within-class variance becomes zero. Although it would result in low-rank representations, "embeddings converge into a lower-dimensional space" is insufficient to properly describe neural collapse. Please refer to [Papyan et al.] that mainly discuss neural collapse, which is not cited in this paper.

[Papyan et al.] Prevalence of Neural Collapse during the terminal phase of deep learning training. PNAS 2021.

- The bound seems to be not practical. 2 is too large learning rate for contrastive learning.

- While experimental results are sensitive to the batch size, there is no discussion about the batch size throughout the theoretical analysis. 

- Experimental setting is limited to small image datasets without transfer learning, so its generalizability is questionable.

- No ablation study on the choice of the similarity function, while the authors claim that the proposed method is better than the one with consine similarity.

- Does Lemma 2 still hold when Eq. (3) is used?

### Questions
Please address concerns above.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces a contrastive learning method called CLOP, which aims to address the issue of neural collapse by leveraging orthonormal prototypes. The authors theoretically analyze the collapse phenomenon in self-supervised and semi-supervised contrastive learning setups and propose a novel loss function to mitigate collapse by enforcing orthogonal subspace constraints. Experiments on CIFAR-100 and Tiny-ImageNet suggest that the proposed method stabilizes performance under varying batch sizes and learning rates.

### Strengths
*Theoretical Analysis:* The paper provides a theoretical analysis of neural collapse, focusing on the impact of large learning rates in contrastive learning settings. The theoretical insights could offer useful guidance for practitioners concerned with collapse issues in representation learning.

*New Loss Design:* The proposal of CLOP, a loss function to enforce orthogonality among embeddings, is a potentially valuable direction for addressing neural collapse. It could add diversity to the current strategies used in self-supervised and semi-supervised learning frameworks.

### Weaknesses
 *Motivation:* The primary motivation of CLOP—to prevent neural collapse and enhance feature diversity—bears significant similarity to VICReg, which also aims to mitigate collapse by enforcing variance, invariance, and covariance constraints on representations. Although CLOP takes an orthogonal approach, it does not sufficiently differentiate itself from VICReg in either theoretical justification or practical application. The theoretical analysis mainly emphasizes the necessity for spatial separation, an objective already addressed by VICReg, leading to questions about the novelty of the approach.

*Insufficient Comparative Analysis:* While VICReg is briefly acknowledged, the paper lacks a robust empirical comparison with VICReg to establish CLOP’s superiority or complementary advantages. In particular, the experiments fail to demonstrate a distinct performance edge over VICReg, which diminishes the contribution of the proposed method. For this paper to make a convincing case for CLOP, direct comparisons, especially in scenarios prone to collapse, would be necessary.

*Experimental Design Issues:* The choice of CIFAR-100 and Tiny-ImageNet as benchmark datasets provides limited insights into the scalability and effectiveness of CLOP in larger and more complex real-world scenarios. Furthermore, while CLOP is tested under different batch sizes and learning rates, the experiments do not include variations in data augmentation or pretext tasks, which are known to impact the success of contrastive learning methods.

### Questions
Please see weaknesses

### Soundness
2

### Presentation
3

### Contribution
2
