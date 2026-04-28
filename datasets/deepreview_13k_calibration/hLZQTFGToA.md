# Contrastive Learning is Spectral Clustering on Similarity Graph

- Decision: Accept
- Avg Score: 4.50
- Scores: 1, 6, 5, 6

## Abstract
Contrastive learning is a powerful self-supervised learning method, but we have a limited theoretical understanding of how it works and why it works. 
In this paper, we prove that contrastive learning with the standard InfoNCE loss is equivalent to spectral clustering on the similarity graph. Using this equivalence as the building block, we extend our analysis to the CLIP model and rigorously characterize how similar multi-modal objects are embedded together.}.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors present a theoretical result concerning contrastive learning. Contrastive learning is a semi-supervised task that aims to map objects into an embedding space such that similar objects are close and dissimilar objects are far apart. Their results concern the widely-used SimCLR loss, an example of an InfoNCE loss. The authors show that optimizing InfoNCE is equivalent to solving a spectral clustering problem. Based on this theoretical insight, they give an argument that exponential kernels are natural and propose a variant of InfoNCE, Kernel-InfoNCE, where they use an alternative exponential kernel in place of the usual Gaussian kernel. Doing so led them to using a Simple Sum kernel, which achieves slightly improved empirical performance on CIFAR image-text data sets. 

This paper is closely related to HaoChen et al 2021; that paper proposed a type of contrastive loss that constitutes performing spectral clustering. The authors of this paper extend this by proving that SimCLR itself constitutes performing spectral clustering. This paper is also related to Van Assel et al., 2022, which analyzes dimensionality reduction methods such as t-SNE using a Markov random field framework adopted by the authors of this paper.

### Strengths
This is an important theoretical result concerning a widely-used method. This work helps bridge the gap between theory and practice in contrastive learning. I have several comments, none of which are major.

### Weaknesses
Minor comments:

I found parts of the text difficult to follow because it lacks guideposts explaining the purpose of each section at a high level. Specifically, the transitions between the theoretical derivations and the practical implications are not always clear, making it hard to see the motivation behind certain steps. For example, the connection between the spectral clustering result and the choice of exponential kernels could be more explicitly stated.

It would help to have a definition of spectral clustering for the purposes of the paper. The paper assumes the reader has a strong background in spectral clustering, but a brief definition would make the paper more accessible and self-contained. This definition should include the key steps involved, such as graph construction, Laplacian matrix computation, and eigenvector analysis.

Eq1: I think this is meant to be a sum over different q's; the text says as much, but that's not how it's defined in Eq1. The notation in Eq1 is ambiguous and could be misinterpreted as a single term rather than a sum over multiple query samples. The use of a more explicit summation symbol or index would clarify this.

"we will flip $X_i$ to get $X_j$ with probability 1/9; it's not clear what "flip" means or why the probability is 1/9. The term "flip" is not a standard term in data augmentation and lacks a clear definition in the context of the paper. The probability of 1/9 seems arbitrary and lacks justification. It would be beneficial to clarify what kind of data augmentation is being referred to and why this specific probability is chosen.

### Questions
See above

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper applies a probabilistic graph coupling perspective to view two typical constrastive learning methods, including SimCLR and CLIP, and interpretes them as spectral clustering or generalized spectral clustering. Moreover, it also attempts to propose to use exponential kernels to replace the Gaussian kernel. Preliminary experiments show that using a mixtures of exponential kernels to replace the Gaussian kernel in the SimCLR loss yields improved classification accuracy.

### Strengths
+ It is interesting to interprete the InfoNCE loss in SimCLR and CLIP into the perspective of probablistic graph coupling and thus find the connection to spectral clustering or generalized spectral clustering.

### Weaknesses
 - The reviewer was confused by the discussion before introducing problem (P1). Since that it is required that the $\mathbf \alpha$ has fewer nonzero entries, some objective of sparsity-promoting property is necessary. However, in (P1) an entropy regularization term is imposed. It is well known that the optimal solution for the maximal entropy problem in the discrete random variable is a uniform distribution. Here, the optimal solution for $\alpha_i$ should be $1/n$. It is weired to have a problem in (P2) and the solution in Theorem 5.1. Note that $\tau$ is the Lagrangian multiplier, i.e., dual variable, it is incomplete to have the dual variable inside. The motivation for using entropy regularization is unclear given the stated goal of promoting sparsity in $\alpha$. The connection between maximizing entropy and achieving sparsity is not well-established, and the paper does not provide sufficient justification for this choice. Furthermore, the role of the constraint $\psi_1 - \sum \alpha_i \psi_i \leq 0$ in the context of entropy maximization is not adequately explained. It's unclear how this constraint interacts with the entropy term to produce a non-uniform, sparse solution for $\alpha$. The introduction of the Lagrangian multiplier $\tau$ within the objective function of (P2) without a clear explanation of its role in the dual problem is confusing and makes the subsequent analysis difficult to follow.

- Moreover, there are mistakes in the formulation of (P2). It is neither the Lagrangian nor the Lagrangian dual problem. It is misleading to claim minimizing (P2) producing an upper bound of (P1). The formulation of (P2) is not a standard Lagrangian dual problem. The paper does not clearly define the primal and dual variables, and the objective function in (P2) does not correspond to the standard Lagrangian dual objective. The claim that minimizing (P2) provides an upper bound for (P1) is not rigorously justified. The relationship between the two problems is not clearly established, and the paper lacks a detailed derivation of the dual problem. The connection between the Lagrangian and the objective function in (P2) is not made clear, and the paper does not explain how the dual variable $\tau$ is used to obtain an upper bound.

- In Section 5.2, it is stated that Theorem 5.1 suggests that the loss function of that form is a natural choice for characterizing the neighborhood similarity structure. The reviewer cannot see this point. Such a form is nothing but a choice on purpose to use the maximal entropy (or due ot mistakes?). The argument that Theorem 5.1 naturally leads to the given loss function for characterizing neighborhood similarity is not convincing. The connection between the solution of (P2) and the notion of neighborhood similarity is not well-established. The paper does not provide a clear explanation of how the specific form of the loss function derived from Theorem 5.1 captures the similarity structure of the data. The claim that this form is a 'natural choice' appears arbitrary without a more detailed justification. The link between the mathematical derivation and the intuitive concept of neighborhood similarity is missing.

- In Eq. (6), it is a RBF kernel, cannot be directly yielded from the form in Theorem 5.1. Because having an exponential form does not imply to have the property of a RBF kernel. In this way, the so-called kernel-InforNCE is nothing but a heuristic form to define the similarity in the InfoNCE loss function. The paper incorrectly claims that the exponential form in Theorem 5.1 directly yields an RBF kernel. An exponential kernel does not necessarily imply the properties of an RBF kernel, which requires a squared Euclidean distance in the exponent. The use of the term 'kernel-InfoNCE' is misleading because the paper does not demonstrate that the derived form is a valid kernel. The connection between the derived exponential form and the RBF kernel is not rigorously established, and the paper does not provide a clear justification for using this form as a similarity measure.

- The related work is not good. Some remarks on the previous work are either improper or even misleading.

- The experimenal evaluation is limited.

### Questions
- The reviewer was confused by the discussion before introducing problem (P1). It is weired to have a problem in (P2) and the solution in Theorem 5.1. 

- Moreover, there are mistakes in the formulation of (P2). It is neither the Lagrangian nor the Lagrangian dual problem. It is misleading or something is missig to claim minimizing (P2) producing an upper bound of (P1). 

- The reviewer cannot see that ``Theorem 5.1 suggests that the loss function of that form is a natural choice for characterizing the neighborhood similarity structure".  

- The reviewer is not clear how to have a RBF kernel from the form in Theorem 5.1.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
- The paper proves that contrastive learning with the standard InfoNCE loss is equivalent to spectral clustering on the similarity graph, which is defined by the data augmentation process. 
- The paper extends this result to the multi-modal setting and shows that CLIP is equivalent to spectral clustering on the pair graph.

### Strengths
- It provides a novel theoretical analysis of contrastive learning and its connection to spectral clustering, which can help understand the underlying mechanisms and principles of this popular self-supervised learning method.
- It proposes a new Kernel-InfoNCE loss with mixture of kernel functions that is inspired by theory and achieves better performance than the standard Gaussian kernel on several benchmark vision datasets

### Weaknesses
 - I think the motivation is not good enough, such a conclusion is easy to obtain, i.e.,  InfoNCE loss is equivalent to spectral clustering. Since graph is pariwise relationship and constrastive is also pairwise relationship, both have the similar objective.
- as the first point, I think the kernel infoNCE is also not well motivated. 

#### It's important to address these concerns regarding motivation in your paper. To improve the motivation for both the InfoNCE loss and the kernel InfoNCE, you might consider the following:

> InfoNCE Loss Motivation:

- Emphasize the practical significance and real-world applications of the InfoNCE loss. How does it relate to real-world problems or datasets in a way that goes beyond spectral clustering?
- Highlight specific challenges or limitations in existing methods that the InfoNCE loss aims to address.

> Kernel InfoNCE Motivation:

- Explain how the kernel InfoNCE extends the motivation from the InfoNCE loss. What specific problems or scenarios does the kernel-InfoNCE address that are not covered by the standard InfoNCE?
- Provide examples or use cases where kernel InfoNCE can be especially valuable.
> By offering a more compelling rationale and demonstrating the practical relevance of these concepts, you can strengthen the motivation for these components in your paper.

### Questions
> see the Weaknesses
- Could you please share your reasons behind this?  it to be innovative?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proves that contrastive learning with the standard InfoNCE loss is equivalent to spectral clustering on the similarity graph. Using this equivalence as the building block, the authors extend our analysis to the CLIP model and rigorously characterize how similar multi-modal objects are embedded together. Based on the maximum entropy principle, the authors demonstrate that the exponential kernels are the natural choices for capturing the local similarity structure for contrastive learning.

### Strengths
1. The  originality, quality, and significance are well supported by the proof of the equivalence of SimCLR and spectral clustering on the similarity graph and the extension to the multi-modal setting.

2. The clarity is satisfied based on the clear illustration of the analysis in Figure 1 and the clear motivations and contributions in the Introduction part of this paper.

### Weaknesses
1. The rationality of treating K_Z and \pi as MRFs and comparing the induced probability distributions on subgraphs should be better explained. The current justification lacks a clear connection to the underlying data generation process or the specific properties of the augmentations used to construct these matrices. It's not immediately evident why comparing distributions on subgraphs is a valid proxy for comparing the full matrices, especially given that these matrices are constructed from augmentations, which may introduce complex dependencies.

2. For the definition of W, the authors are expected to further explain the mentioned unitary out-degree filter. The explanation should clarify how this filter is implemented and what its effect is on the graph structure. The term 'unitary out-degree filter' is not standard and requires a more detailed explanation for readers to fully understand its function and implications within the context of the proposed method.

3. The reason that cross-entropy loss can be converted to the combination of repulsion and attraction terms is expected to be further given after Lemma 2.4. The connection to Lemma 2.5 needs to be made more explicit. It is not clear how Lemma 2.4 leads to the decomposition of the cross-entropy loss into these two terms, and the specific role of Lemma 2.5 in this conversion is not sufficiently highlighted. The intuitive explanation is not enough; a more rigorous derivation or explanation is needed.

4. In the experiment, the improvements of the proposed method are not obvious compared with SimCLR on the given datasets. The analysis of the results at 200 epochs and 400 epochs should be more in-depth. A more detailed discussion is needed to understand why the proposed method does not show more substantial improvements over SimCLR, and the reasons for the observed convergence behavior at different epochs should be explored further.

5. The authors should repeat each experiment multiple times and list the mean and deviation to avoid the possible randomness, i.e., Table 1 and Table 4. The lack of statistical measures makes it difficult to assess the robustness of the results and the significance of the observed differences.

### Questions
1. Why choose Laplacian kernel and Simple Sum kernel for the MoCo experiment results should be further stressed, i.e., why the Gaussian kernel is not selected here.

2. Why the authors choose p=1,q=0 and p=0.75 and q=0.2 in the syntetic experiment?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
