# SSOLE: Rethinking Orthogonal Low-rank Embedding for Self-Supervised Learning

- Decision: Accept
- Scores: 5, 8, 6, 8

## Abstract
Self-supervised learning (SSL) aims to learn meaningful representations from unlabeled data. Orthogonal Low-rank Embedding (OLE) shows promise for SSL by enhancing intra-class similarity in a low-rank subspace and promoting inter-class dissimilarity in a high-rank subspace, making it particularly suitable for multi-view learning tasks. However, directly applying OLE to SSL poses significant challenges: (1) the virtually infinite number of "classes" in SSL makes achieving the OLE objective impractical, leading to representational collapse; and (2) low-rank constraints may fail to distinguish between positively and negatively correlated features, further undermining learning. To address these issues, we propose SSOLE (Self-Supervised Orthogonal Low-rank Embedding), a novel framework that integrates OLE principles into SSL by (1) decoupling the low-rank and high-rank enforcement to align with SSL objectives; and (2) applying low-rank constraints to feature deviations from their mean, ensuring better alignment of positive pairs by accounting for the signs of cosine similarities. Our theoretical analysis and empirical results demonstrate that these adaptations are crucial to SSOLE’s effectiveness. Moreover, SSOLE achieves competitive performance across SSL benchmarks without relying on large batch sizes, memory banks, or dual-encoder architectures, making it an efficient and scalable solution for self-supervised tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper presents orthogonal low-rank embedding for self-supervised learning (SSOLE) by decoupling low/high-rank enforcement on positive/negative pairs and low-rank enforcement via deviation matrices.

### Strengths
1.The paper is with a good clarity by providing a deep analysis on the problem when applied OLE in SSL. The two challenges to be solved are well discussed.
2.The authors provided a detailed theoretical analysis to illustrate the research problem as well as the developed method.
3.Sufficient experiments are performed, and the results demonstrate the work’s effectiveness.

### Weaknesses
1.The main idea of the paper of employing low/high-rank enforcement to adjust the distance between contrastive sample pairs has been proposed and discussed in several previous works of supervised learning (like LDA). As a result, the paper makes incremental contribution by extending this idea to self-supervised learning, which makes its novelty somehow limited. Besides, some related works are not discussed in this paper.
2.The relationship between the three limitations, the two challenges, and the proposed method could be further discussed. 
3.The authors consider decoupling the low-rank enforcement and high-rank enforcement with Eq. (2), which needs more explanation to analyze how Eq. (2) achieves this aim.
4.It is mentioned that achieves competitive performance across SSL benchmarks without relying on large batch sizes, memory banks, or dual-encoder architectures, which lacks detailed verification or discussion.

### Questions
1.What is the relationship between the three limitations, the two challenges, and the proposed method?

2.How does Eq. (2) decouple the low-rank enforcement and high-rank enforcement?

3.The title of the paper does not mention “multi-view learning”, but why do the authors discuss “multi-view learning” throughout the paper (especially in experiments)? Besides, since there are several multi-view self-supervised learning methods, why not compare the proposed with these works as well?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper primarily focuses on applying OLE to SSL and propose a novel method that integrates Orthogonal Low-rank Embedding into the Self-Supervised Learning paradigm. The authors mainly addresses two key challenges in applying OLE to SSL: the enforcement of orthogonality with an infinite number of classes and the limitations of the nuclear norm in distinguishing between positive and negative correlations. By decoupling low-rank and high-rank enforcement and applying constraints on feature deviations, SSOLE adapts OLE for self-supervised tasks. The paper demonstrates how SSOLE adapts OLE for self-supervised tasks and showcases its superior performance in various learning scenarios while maintaining computational efficiency.

### Strengths
1.The paper offers comprehensive experimentation, strengthening the validity of the presented approach.
2.The method is described in detail, enhancing its reproducibility and understanding.
3.In terms of experiments,  this paper evaluate the adaptability and robustness of the SSOLE framework through transfer
learning to various linear classification tasks and demonstrates its superior performances.

### Weaknesses
1.The writing of this paper needs to be improved.
2.Some experiments are not sufficiently thorough, such as when evaluating the performance of the method in semi-supervised learning, the datasets used are somewhat limited, and the experimental results are not particularly striking. If additional experiments on other datasets could be conducted to demonstrate the method's effectiveness, it would be more convincing.

### Questions
1.In the case of weakly supervised datasets, such as when the dataset contains noisy labels, does this method have adaptability?
2.Regarding the description in the appendix A.4 that the product of diagonal matrix P and its transpose is the identity matrix, why are all the diagonal elements of the resulting matrix either 1 or -1? Could you provide a more detailed explanation?

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
The paper points out that traditional Orthogonal Low-Rank Embedding (OLE) methods face significant challenges in self-supervised learning (SSL), mainly due to representational collapse caused by an excessively large number of classes, and the difficulty of distinguishing between positively and negatively correlated features under low-rank constraints. To address these issues, SSOLE decouples the low-rank and high-rank constraints and applies low-rank constraints to the deviation matrix of features. This approach effectively prevents representational collapse and enhances the ability to differentiate between positive and negative sample pairs. Experimental results demonstrate that SSOLE achieves excellent performance across various SSL benchmarks, showing good scalability and efficiency, especially without requiring large batch sizes and complex architectures.

### Strengths
1. Methodological Innovation: The paper introduces a low-rank bias matrix and a decoupled constraint mechanism based on the integration of OLE and SSL, addressing the issue of representation collapse that traditional methods struggle to resolve in unsupervised scenarios.

2. Theoretical and Experimental Support: The effectiveness of the SSOLE framework is supported by both theoretical analysis and experimental validation, demonstrating strong performance across various datasets, particularly in settings with limited computational resources.

3. Broad Applicability: In image classification tasks, SSOLE shows good generalization ability, adapting to different datasets and further enhancing the robustness of feature representation.

### Weaknesses
1. Some proofs are omitted and not specific enough, such as

i) Why is the probability of $|cos(\theta_{ij})|>1/d$ is larger than $1/d$? By what, Chebyshev inequality? The current explanation lacks a clear derivation showing how the probability bound is obtained. It's not immediately obvious how the properties of random vectors on a unit sphere translate to this specific probability bound using Chebyshev's inequality, and the paper needs to explicitly show the intermediate steps, including the variance calculation of the cosine similarity.

ii) Some statements are as follows: "Since the rows of  $\tilde{V}$ are nearly orthogonal, the nuclear norm is dominated by the sum of the row norms." Why can it hold? The readers need more detailed explanations. The justification for this claim is insufficient. The paper needs to provide a more rigorous argument, potentially by showing how the singular values of a nearly orthogonal matrix relate to its row norms. A more detailed analysis of the perturbation bounds on the singular values due to the non-orthogonality would be beneficial.

2. Some proofs are unnecessary. THEOREM 3.3 states that the nuclear norm is unitarily invariant, a property that is very common in linear algebra textbooks. While this property is true, its inclusion without a clear explanation of its specific relevance to the core contribution of the paper makes it seem out of place. The paper should clarify why this property is crucial for the proposed method and how it directly impacts the results.

3. What does $\approx$ mean? Does it mean that the equation holds with high probability, or that the values are close? If so, how close are the values? The paper needs to give a clear definition. The lack of a precise definition for the approximation symbol creates ambiguity. The paper needs to specify if it is a high-probability approximation, a numerical approximation, or something else, and provide the error bounds or concentration inequalities that justify it.

### Questions
See "Weaknesses".

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a self-supervised orthogonal low-rank embedding (SSOLE), which integrates OLE into the SSL paradigm. It addresses two challenges in applying OLE to SSL: the difficulty of enforcing orthogonality in the presence of an infinite number of classes, and the nuclear norm’s inability to distinguish between positive and negative correlations. By decoupling low-rank and high-rank enforcement and applying low-rank constraints to feature deviations, SSOL adapts OLE for self-supervised and other tasks.

### Strengths
1.	This paper is well-written with clear motivations.
2.	It is technically sound with comprehensive theoretical analysis.
3.	Experimental results demonstrate the effectiveness of the method.

### Weaknesses
1.	The parameter $\lambda$ controls the balance between intra-class compactness and inter-class separability enforcement. It will be better to analyze its influence to the final performance.

2.	The authors enforce intra-class low-rank property via deviation matrix instead of original feature matrix, it is also suggested to investigate its effectiveness by ablation study.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
