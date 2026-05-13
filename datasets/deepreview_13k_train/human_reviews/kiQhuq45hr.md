# MPHIL: Multi-Prototype Hyperspherical Invariant Learning for Graph Out-of-Distribution Generalization

- Decision: Reject
- Scores: 5, 5, 5, 6

## Abstract
Out-of-distribution (OOD) generalization has emerged as a critical challenge in graph learning, as real-world graph data often exhibit diverse and shifting environments that traditional models fail to generalize across. A promising solution to address this issue is graph invariant learning (GIL), which aims to learn invariant representations by disentangling label-correlated invariant subgraphs from environment-specific subgraphs. However, existing GIL methods face two major challenges: (1) the difficulty of capturing and modeling diverse environments in graph data, and (2) the semantic cliff, where invariant subgraphs from different classes are difficult to distinguish, leading to poor class separability and increased misclassifications. To tackle these challenges, we propose a novel method termed Multi-Prototype Hyperspherical Invariant Learning (MPHIL), which introduces two key innovations: (1) invariant learning in hyperspherical space, enabling robust invariant feature extraction and prototypical learning in a highly discriminative space, and (2) class prototypes as intermediate variables, which eliminate the need for explicit environment modeling in GIL and mitigate the semantic cliff issue through multi-prototype-based classification. Derived from the theoretical framework of GIL, we introduce two novel objective functions: the invariant prototype matching loss to ensure samples are matched to the correct class prototypes, and the prototype separation loss to increase the distinction between prototypes of different classes in the hyperspherical space. Extensive experiments on 11 OOD generalization benchmark datasets demonstrate that MPHIL achieves state-of-the-art performance, significantly outperforming existing methods across graph data from various domains and with different distribution shifts. The source code of MPHIL is available at https://anonymous.4open.science/r/MPHIL-23C0/.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents a novel method MPHIL to address two challenges in existing graph invariant learning methods: the difficulty of capturing environmental information and the semantic cliff  across different classes. MPHIL operates in hyperspherical space with class prototype as intermediate variable to improve representation separability and robustnes without explicit environment modeling. 
Two innovative loss functions are derives to enhance intra-class invariance and inter-class separability. Extensive experiments show that MPHIL outperforms state-of-the-art methods on various benchmark datasets, demonstrating its effectiveness for OOD generalization.

### Strengths
This paper propose a new method for graph invariant learning. 
- The paper is well-organized.

### Weaknesses
 -  Intuitively, the accuracy the class prediction relies on the fastest prototype point in the same class prototype set.  What if use the mean/sum/min for predicting the class? More ablation study can make your work more convincing.
- The novelty of this proposed method is limited. I don't think the projection to the hypersphere here is novel. Actually, it is a simple cosine distance. How about using other distances like L2, L1, more analysis should be included.
- I wonder the performance when only using one protype. 
- The prototype updating mechanism is complicated, what if directly use the representation of the sample from training set after training.
- The explaination of some symbols is missing, e.g. the $\omega_k^{(c)}$ in Eq (12).

### Questions
See weakness.

### Soundness
2

### Presentation
2

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
The authors address the challenges of out-of-distribution (OOD) generalization on graphs and propose a model named MPHIL in this paper. MPHIL builds on graph invariant learning (GIL) by disentangling label-correlated invariant subgraphs from environment-specific subgraphs, which helps overcome difficulties in capturing diverse environments and the semantic cliff. For more details, MPHIL first introduces invariant learning within a hyperspherical space using multiple class prototypes to enhance classification without explicit environment modeling. Then, two loss functions ( invariant prototype matching loss and prototype separation loss ) are proposed to ensure accurate class association and inter-class distinction within the hyperspherical space. Extensive experiments conducted across 11 OOD generalization benchmark datasets demonstrate the effectiveness of MPHIL.

### Strengths
Different from traditional methods, this paper introduces a novel approach by applying invariant learning in a hyperspherical space to enhance out-of-distribution (OOD) generalization in graph-based tasks. Specially, the invariant prototype matching loss and prototype separation loss proposed in Section 3.4 are well-designed to ensure both accurate class association and inter-class distinction, improving model robustness in hyperspherical space.

### Weaknesses
- The novelty of this paper is limited. This paper introduce invariant learning into a hyperspherical space and introduces multiple prototypes to improve class separability, these ideas extend previously established techniques in a relatively straightforward manner. However, the use of hyperspherical embeddings for enhancing model performance of OOD has been explored [1], [2] and [3]. Specifically, the paper does not adequately address how its approach differs fundamentally from existing methods that also leverage hyperspherical embeddings for representation learning, particularly in the context of graph data. The motivation for using multiple prototypes is not clearly justified beyond a general desire for improved class separability, and the specific design choices for the invariant prototype matching loss and prototype separation loss lack a strong theoretical grounding, making them appear somewhat ad-hoc.

- The experimental results are not convincing, and the baseline methods are not strong enough. Although the authors compare MPHIL with some widely used baseline methods like ERM, CIGA and GSAT, these are neither the latest nor the most competitive, which undermines the significance of the reported performance. More recent OOD methods for graphs should be introduced in the experimental part for fair comparisons, such as OOD-GCL [4], GALA [5] and LECI [6]. The paper lacks a thorough ablation study to demonstrate the contribution of each component of the proposed method. For example, it is unclear how much performance gain is due to the hyperspherical embedding versus the multi-prototype approach, or the specific design of the loss functions. Furthermore, the experimental setup does not include a detailed analysis of the computational cost of the proposed method compared to baselines, which is important for practical applications.

### Questions
see weakness

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies the problem of graph Out-of-distribution (OOD) generalization and then proposes two objective functions: the invariant prototype matching loss to ensure samples are matched to the correct class prototypes, and the prototype separation loss to increase the distinction between prototypes of different classes in the hyperspherical space. Extensive experiments on 11 OOD generalization benchmark datasets demonstrate the effectiveness of the proposed method.

### Strengths
- The paper studies an important research question.
- The experimental results are extensive.

### Weaknesses
 - This paper seems to closely follow the recent research "HYPO: Hyperspherical Out-Of-Distribution Generalization", e.g., "intra-class variation and inter-class separation principles". The novelty of the paper seems to be limited.
-  The visualization results do not seem clear (fig 3). Why the proposed method is better than the compared method
- Some SOTA methods seem to be missing.

### Questions
See above.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces MPHIL, a novel method for graph out-of-distribution (OOD) generalization. Key features include: 1）Invariant learning in hyperspherical space. 2) Multi-prototype classification approach. MPHIL eliminates the need for explicit environment modeling and addresses the semantic cliff issue. It outperforms existing methods on 11 OOD benchmark datasets across various domains. The approach offers a more robust solution for real-world graph learning applications where data distributions often shift.

### Strengths
1. Originality: The idea is relatively novel, using Hyperspherical Learning to deal with OOD generalization on graphs, and achieving promising experimental results.

2. Clarity & Significance: The logic of the manuscript is clear. In particular, the example of molecular graphs given in the introduction is very helpful for contextualization, and does a good job of describing the problem the authors were trying to solve and the significance of the study.

3. The manuscript is substantial and essentially encompasses all of the research that should be discussed.

### Weaknesses
1. There are some terms and formulas that are not presented accordingly, such as I(z;y) in Eq. 2, which I understand to mean mutual information. However, to increase readability I would suggest that these symbols should be explained the first time they appear. Apart from this, there is no explanation of the significance of some of the designed variables, such as separation score S. Why add it additionally to H? What is the benefit of doing so? It is unclear how this separation score directly contributes to invariant feature extraction, especially since the method encodes the entire graph initially. The connection between the separation score and the final invariant representation is not sufficiently justified.

2. Figure 3 does not significantly show the advantage of your proposed method over baseline, can you consider a different visualization example that more intuitively reflects the difference between the two? The current visualization makes it difficult to discern the clustering and separation of different classes, which is crucial for demonstrating the effectiveness of the proposed method. The lack of clear visual separation undermines the claim of improved OOD generalization.

3.  You included a link to the code in your manuscript, but I found that many of the modules are called, but the relevant code doesn't exist and doesn't work. This makes it difficult to reproduce the results and verify the claims made in the paper. The absence of necessary modules and the lack of clear instructions for setting up the environment significantly hinder the reproducibility of the work.

### Questions
1. Is graph invariant learning only applicable to graph classification task? Can it be processed if it is a node classification task?

2. In Section 3.3, it is mentioned that K prototypes are assigned to each category, so what is the basis for the final categorization? Further, since invariant representation can correspond to a set of prototypes, does it happen that these prototypes do not belong to the same class at the test phase? (after softmax operation, although one of the prototypes has the highest probability, but the other classes contain multiple prototypes with relatively high probability, can it be considered that the confidence of the classification result is lower?) I'm a bit confused here, can you explain the rationale for designing prototypes? Is it relying exclusively on the several losses that have been subsequently proposed to be corrected to avoid the situation I have described?  (I completely agree with your statement at the beginning of section 3.3 about the risk of overfitting caused by a single prototype in the previous approach)

### Soundness
3

### Presentation
3

### Contribution
3
