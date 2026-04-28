# Understanding Self-supervised Learning as an Approximation of Supervised Learning

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 5, 8, 5

## Abstract
Self-supervised representation learning has mainly advanced in an empirical rather than theoretical manner. Many successful algorithms combine multiple techniques that are supported by experiments. This approach makes it difficult for the community to understand self-supervised learning fundamentally. To help settle this situation, we take a principled approach. We theoretically formulate a self-supervised learning problem as an approximation of a supervised learning problem. From the formulated problem, we derive a loss that is closely related to existing contrastive losses, thereby providing a foundation for these losses. The concepts of prototype representation bias and balanced contrastive loss are naturally introduced in the derivation, which provide insights to help understand self-supervised learning. We discuss how components of our framework align with practices of self-supervised learning algorithms, focusing on SimCLR. We also investigate the impact of balancing the attracting force between positive pairs and the repelling force between negative pairs. The proofs of our theorems are provided in the appendix, and the code to reproduce experimental results is provided in the supplementary material.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper formulates self-supervised learning (SSL) as an approximation of supervised learning (SL), deriving a loss function related to contrastive losses. The author introduce the concepts of prototype representation bias and balanced contrastive loss, providing some insights into SSL. They conduct experiments to validate their theoretical results

### Strengths
1. They proposed a novel theoretical framework that connects supervised and self-supervised learning.
2. They introduction of the concepts of prototype representation bias and balanced contrastive loss, which play important roles in the connection.
3. They offer some practical insights based on their framework.

### Weaknesses
I think the main issue with this paper is its insufficient theoretical contribution. Using the prototype representation bias, as defined by the authors, to represent the gap between SSL and SL is overly simplistic. In reality, no practical augmentation can achieve a very low prototype representation bias unless label information is available. Moreover, augmentations with the same prototype representation bias might exhibit vastly different downstream performance, depending on the finer relationship between the augmentation and the data—a topic the authors have not addressed.

### Questions
Please see the weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The submission proposes a derivation of self-supervised learning problem as an approximation of supervised learning. To this end, in supervised learning formulation the authors replace the labels with prototype representations given by an oracle. These prototype representations can then be modelled via the expected representation of objects sampled from a conditional distribution (x conditioned on label y) and across augmentations, i.e. $\mathbb{E}_{t,X|y} \ f(t(x))$. Learning under this formulation can be achieved via triplet loss, i.e. attracting positive samples (sample from one class) and repelling negative samples (samples from different classes).

In self-supervised learning, however, one has no access to labels which renders prototype representations unavailable. Instead, the authors use surrogate prototypes, i.e. expected representation of sample across its augmentations, i.e. $\mathbb{E}_t \ f(t(x))$. The authors then provide an upper bound on the loss, which yields objective called balanced contrastive loss, and show its connection to NT-Xent loss used in SimCLR. One may measure the bias introduce by the surrogate by taking the expectation of the difference between the true and surrogate representations, called prototype representation bias. The bias is shown to correlate with downstream performance.

### Strengths
It is safe to say that theoretical understanding of self-supervised learning methods is relatively lacking despite increasing interest and effort. Thus, the submission addresses an important topic and provides a clear connection to the supervised counterpart. It is generally well structured which makes it easy to follow, and provides a clear intuition of the approach. The approach covers typical components of self-supervised methods like Siamese networks, data augmentation and contrastive loss.

### Weaknesses
While the submission addresses an interesting connection to supervised learning, the connection has been addressed in previous literature [1], for example attraction/repelling and normalization has been brought up in [2]. Further, the consequences of the proposed framework seem to provide limited insight. While they provide supporting arguments for siamese architecture, data augmentation and infoNCE loss from a supervised perspective, the framework seem to conflict with the use of projection head and aggressive data augmentation. Let me elaborate on this further.

If SSL is an approximation of supervised learning, then on downstream task the use of the output of projection head should be more beneficial than the pre-projection features. However, this is not what one faces in practice. Interpreting SSL via supervised learning may inhibit understanding the use of projection head. Highlighting the mismatch between pretext and downstream tasks is important if we to gain practical consequences in designing SSL methods. The proposed interpretation, on the contrary, seem to sweep this distinction under the rug.

Furthermore, SSL methods use more aggressive augmentation strategies than those used in supervised learning, while aggressive augmentation negatively impacts supervised learning [3]. This is also something that seem to be out of tune with the proposed approach.

SimCLR-type losses are well understood from many perspectives, including spectral and information-theoretic [4,5], so it is not fair to render them as only intuitively and experimentally supported.

The authors introduce assumptions on the choice of similarity measure and use of normalization to derive the proposed loss, which is shown to generalize NT-Xent used in SimCLR. The assumptions are needed for the derivation, but I don't think one would need to additionally show their significance empirically, especially when this is already an established practice and has been ablated multiple times in the literature. Similar issue with experiments on balanced dataset. This seems to eat up space and doesn't reveal anything new about SSL methods.

Returning to the generalization of supervised learning problem from predicting labels to predicting prototype representations, this step is important but receives limited discussion in the submission. Since there are multiple target tasks for supervised training, the ideal prototype representations are as well target-specific here. How does this affect the overall framework?

### Questions
In the experimental section with balancing parameters, how are the values in the Figure 4 obtained? Is this the single run or averaged across n?

Can you please elaborate more on $\nu$ used in the proposed total loss? It seems to not be available and has not analogous term in NT-Xent loss.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper theoretically models self-supervised learning as an approximation to supervised learning. The authors derive a self-supervised loss related to contrastive losses, including InfoNCE, while introducing concepts like prototype representation bias and balanced contrastive loss. They apply the framework to analyze components of self-supervised learning, notably SimCLR, and explore the effects of balancing attraction and repulsion forces.

### Strengths
1- The paper's primary strength lies in its establishment of a rigorous theoretical framework that bridges supervised and self-supervised learning, addressing a significant gap in the literature by grounding widely-used contrastive losses in theory. This approach contributes to the field by potentially enhancing the interpretability and rationale behind existing self-supervised methods.

2- The authors derive a self-supervised learning loss function from first principles, aligning it with established methods like the NT-Xent loss in SimCLR. This derivation offers the self-supervised learning community a deeper understanding of why and how particular loss functions, often implemented heuristically, are effective.

3- Introducing the concept of prototype representation bias, the paper reveals how self-supervised learning can be systematically evaluated and potentially optimized by minimizing this bias through data augmentation strategies. This is an innovative step that contextualizes the role of representation clustering within the self-supervised paradigm.

### Weaknesses
1- The authors define a surrogate prototype representation based on transformations (augmentations) of the same data point, but this choice may vary substantially across datasets and problem domains. Since many real-world applications use domain-specific augmentations (e.g., color transformations for medical images, or geometric transformations for satellite imagery), the theoretical guarantees provided may not hold uniformly. The paper lacks a rigorous investigation into how the choice of augmentations impacts the derived loss and the resulting prototype representations. A sensitivity analysis or empirical study on the effects of diverse augmentation choices, including those that introduce significant semantic changes, would strengthen the validity of the surrogate representation assumptions.

2- The paper introduces parameters (e.g., balancing factors like 
\alpha and \lambda Equation 12) that govern the relative strengths of attraction and repulsion forces in the derived loss function. However, it provides limited insights into how these parameters impact performance across diverse datasets and tasks, particularly in scenarios with varying degrees of class imbalance or data complexity. A deeper empirical analysis or sensitivity study on these parameters, including an exploration of their interaction, would make the findings more robust and practically usable. Additionally, the paper should discuss guidelines for optimal parameter selection based on dataset characteristics, such as the number of classes or the degree of intra-class variation, to improve its utility for practitioners.

3- The paper situates itself within the context of contrastive learning methods, particularly NT-Xent and InfoNCE losses. However, there are alternative frameworks in self-supervised learning, such as clustering-based approaches (e.g., DeepCluster, SwAV) and bootstrapping methods (e.g., BYOL). While the authors mention these methods briefly, they do not provide a clear comparison or discussion of how their theoretical framework might align or diverge from these alternative approaches, especially in terms of the underlying assumptions and the types of representations learned. A more comprehensive analysis, including a discussion of the limitations of the proposed framework in relation to these other methods, would position the framework more effectively within the larger self-supervised landscape.

4- The paper’s findings, especially around balancing attraction and repulsion forces, suggest potential for optimization. Yet, there is minimal exploration of how the theoretical insights could inspire specific algorithmic modifications or optimizations for contrastive learning. For example, the paper does not discuss how insights into prototype bias could be used to dynamically adjust the loss during training or how the derived loss could be adapted to online learning scenarios. Discussing these possibilities and providing concrete examples would improve the paper's impact by suggesting actionable ways to leverage its contributions.

### Questions
1- How would the assumptions, such as balanced data and the specific choice of cosine similarity, affect the generalizability of this framework to domains with significant class imbalance or non-standard data representations?

2- To what extent can prototype representation bias be quantitatively minimized through practical data augmentation strategies? Would further analysis on this bias's impact across different datasets yield consistent trends?

3- Could the theoretical framework be adapted or extended to include asymmetrical architectures, given their prominence in modern self-supervised learning algorithms? What additional assumptions might be required?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper focuses on understanding self-supervised learning, where the authors theoretically formulate the self-supervised learning problem as an approximation of a supervised learning problem.

### Strengths
1. The paper is well-organized, with clear subsections that logically flow from theoretical foundations to empirical validations.
2. The mathematical derivations and proofs in this paper seem appropriate.

### Weaknesses
1. Although the authors claim to propose a new perspective for understanding SSL, it seems to me that there is significant overlap with [a]. Unfortunately, the authors do not provide a detailed analysis of the similarities and differences between the two.
2. The correlation between theoretical analysis and insights in this article is weak: In the theoretical analysis section, only the proof of two upper bounds is provided. My question is: What is the relationship between these two upper bounds and the supervised learning paradigm? In other words, what is the significance of their insights for the paper?
3. In Section 6, the proposed new SSL format does not seem to have significant advantages. In addition, the authors also do not conduct sufficient verification experiments.
4. In fact, there are many related works (like [b-c]) on the understanding of SSL, unfortunately, this paper does not provide a detailed discussion and analysis of their differences.

### Questions
1. In the theoretical analysis section, only the proof of two upper bounds is provided. My question is: What is the relationship between these two upper bounds and the supervised learning paradigm? In other words, what is the significance of their insights for the paper?
2. What is the significance of self-supervised learning from this perspective?  At a high level, beyond some conclusions that are very similar to [a], it is difficult to capture additional information. 

Reference:
[a] Tongzhou Wang and Phillip Isola. Understanding contrastive representation learning through alignment and uniformity on the hypersphere. In International conference on machine learning, pp. 9929–9939. PMLR, 2020.

### Soundness
2

### Presentation
3

### Contribution
2
