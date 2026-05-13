# Towards Domain Adaptive Neural Contextual Bandits

- Decision: Accept
- Scores: 8, 6, 6

## Abstract
Contextual bandit algorithms are essential for solving real-world decision making problems. In practice, collecting a contextual bandit's feedback from different domains may involve different costs. For example, measuring drug reaction from mice (as a source domain) and humans (as a target domain). Unfortunately, adapting a contextual bandit algorithm from a source domain to a target domain with distribution shift still remains a major challenge and largely unexplored. In this paper, we introduce the first general domain adaptation method for contextual bandits. Our approach learns a bandit model for the target domain by collecting feedback from the source domain. Our theoretical analysis shows that our algorithm maintains a sub-linear regret bound even adapting across domains. Empirical results show that our approach outperforms the state-of-the-art contextual bandit algorithms on real-world datasets.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The manuscript introduces a domain adaption algorithm for contextual bandit. It further proves that the proposed method achieves a sub-linear regret bound. Empirical experiments conducted on real-world data shows the the proposed method outperforms existing state-of-the-art contextual bandit methods for cross domains.

### Strengths
1. The design of the new algorithm originates from an observation that leveraging data across domains leads to sub-linear regrets, which makes the whole method simple, yet elegant.

2. Theoretical proof has been provided to support the performance of the method.

3. The algorithm is extensively tested on three datasets.

### Weaknesses
It would be helpful to elaborate on why the data divergence term is sub-linear in the proof.

### Questions
See weakness.

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
The paper introduces an algorithm for domain adaptation in contextual bandits. This method aims to adapt a neural contextual bandit algorithm from a low-cost source domain to a high-cost target domain, to address the challenge of distribution shifts between the two domains. The theoretical analysis conducted demonstrates that DABand achieves a sub-linear regret bound in the target domain, which is interesting. Empirical results are presented using real-world datasets, which show that DABand outperforms existing contextual bandit methods. The proposed work has broader implications, including potential insights into reinforcement learning with human feedback algorithms.

### Strengths
(1) The proposed problem setting of contextual bandits in a domain adaptation scenario is interesting and challenging.

(2) The method utilizes unlabeled data from both source and target domains for effective representation learning and alignment across different domains.

(3) The algorithm is capable of attaining a sub-linear regret bound in the target domain by solving an online network lasso problem with time-dependent regularization.

### Weaknesses
The method leverages unlabeled data from both source and target domains to learn robust representations and aligns them effectively across different domains, enabling efficient domain adaptation. While the proposed algorithm builds upon the NeuralLinUCB framework, it introduces an adaptation in the loss function specifically tailored for updating the neural network. This loss function integrates insights from classic domain adaptation techniques, and thereby has some similarity with existing methods. The core adaptation in the loss function, while novel in the context of neural contextual bandits, appears to draw heavily from established domain adaptation techniques, potentially limiting the overall novelty of the approach. Specifically, the use of techniques to align feature representations across domains is a common theme in domain adaptation literature, and the paper could benefit from a more detailed discussion of how the specific implementation differs from or improves upon existing methods. The paper does not fully explore the sensitivity of the method to the choice of the regularization parameter in the online network lasso problem, which could significantly impact the performance of the algorithm in practice.

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies the domain transfer in (neural) contextual bandits. The authors provide a decomposition of the domain transfer in contextual bandits, and proposed an algorithm leveraging the adversarial training in domain-transfer. Theoretical results are presented understanding this decomposition and empirical evaluation are performed to validate the performance of the algorithm

### Strengths
- The authors provide a theoretical justification on the decomposition for the domain-transfer issue for contextual bandits. 
- The authors provide empirical evaluation demonstrating the performance of the algorithm.

### Weaknesses
 - (Minor) Definition 3.6 is hard to understand for me. In particular, are $\mathbf x$ and $x$ referring to the same thing? Are the authors implicitly assumes $h \in \mathcal H$ and $x \in \mathbb R^n$ in this case? It would be helpful if the authors could rephrase the mathematical formulation on this. 
- In Theorem 3.1 needs further justification. For example, I wonder why the sublinear in $R_S$ will lead to the sublinear result in $R_T$. I checked the proof for Theorem 3.1 in appendix but found nowhere explicitly discuss this part. In addition, why the data-divergence term is sublinear? 
- The adversarial training paradigm adapted in controlling the data divergence term in the proposed algorithm requires better justification: why the hypothesis class here is the same with the hypothesis class used in contextual bandits? Specifically, the original adversarial training paradigm is designed for classification tasks, while contextual bandits are essentially a regression problem. The paper needs to clarify how the hypothesis class is generalized from classification to regression and why this generalization is valid in the context of contextual bandits.
- It lacks some discussions on the performance analysis in linear contextual bandits or discussions in related literautre. The authors might want to provide more discussion on the theoretical insight of this. Specifically, it would be beneficial to discuss how the proposed method compares to linear contextual bandit algorithms, such as LinUCB, in terms of regret bounds and performance in the cross-domain setting. The paper should also discuss why simply applying linear models or neural network models without domain adaptation would fail in this setting.

- (Minor) Section 4.1 title: eq (16) -> eq (5)

### Questions
- Besides the presentation in Theorem 3.1, are there any regret scale for linear contextual bandits to help me better understand the performance of the algorithm?

### Soundness
3

### Presentation
2

### Contribution
3
