# Neural Eigenfunctions Are Structured Representation Learners

- Decision: Reject
- Scores: 6, 8, 6, 6

## Abstract
This paper introduces a structured, adaptive-length deep representation called Neural Eigenmap. Unlike prior spectral methods such as Laplacian Eigenmap that operate in a nonparametric manner, Neural Eigenmap leverages NeuralEF~\citep{deng2022neuralef} to parametrically model eigenfunctions using a neural network. We show that, when the eigenfunction is derived from positive relations in a data augmentation setup, applying NeuralEF results in an objective function that resembles those of popular self-supervised learning methods, with an additional symmetry-breaking property that leads to \emph{structured} representations where features are ordered by importance. We demonstrate using such representations as adaptive-length codes in image retrieval systems. By truncation according to feature importance, our method requires up to $16\times$ shorter representation length than leading self-supervised learning ones to achieve similar retrieval performance. We further apply our method to graph data and report strong results on a node representation learning benchmark with more than one million nodes.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a method to learn the eigenfunctions of an augmentation kernel or a given graph, by parametrizing them using deep networks, which can be used for unsupervised representation learning. Compared to previous related works the proposed approach is scalable, while it can provide ordered eigenfunctions. In the experiments, it is demonstrated the performance of the approach on downstream tasks.

### Strengths
- Unsupervised representation learning is an interesting problem, while the proposed approach extends previous works.
- The technical part of the paper seems to be correct, but I have not checked in detail all the theoretical results.
- The proposed methods perform better in some of the experiments.

### Weaknesses
 - The paper is ok written, but there are some parts that need improvement. For example, it is not entirely clear which methods the authors propose and how they differ from previous works.
- Regarding the novelty, it is unclear to me what is the difference between the proposed approaches compared to previous works, which makes hard to understand the actual contributions.
- In some of the experiments, it seems that the improvement is not significant.

### Questions
Q1. Regarding the graph-based problem (Sec. 4) it is clear that Eq. 12 is the proposed model, and due to $\hat{\psi}$ in the second term, the learned eigenfunctions are ordered. I think in Sec. 3 this is not entirely clear. As far as I understand, Eq. 8 which gives ordered representations is already proposed by Jonson et al. (2022)? While the proposed Eq. 9 does not give ordered representations but it is potentially scalable?

Q2. I think that it is not clear from the text when the $\hat{\psi}$ in the second term of Eq. 8 should be used and when not. 

Q3. I believe that the analysis of the comparison to Barlow Twins is rather limited. It seems that the approaches are very similar both in their formulation but also in the experiments. I believe the differences should be investigated in more detail.

Q4. As far as I understand, both SCL and Neural Eigenmaps learn the top-k eigenfunctions of a kernel. Why there is a difference in performance e.g. Fig 2? Neural eigenmaps approximates better the true eigenfunctions compared to SCL?

Q5. There is an example in the appendix that shows the approximation of the eigenfunctions for the RBF kernel. Similar to the spectral methods, I think that is interesting to see a comparison using 3D shapes, e.g. the Standford Bunny.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this work, the authors propose a principled theoretical motivation for eigenfunction based representation learning in the form of Neural Eigenmap and show it as providing a unifying surrogate for unsupervised representation learning. They show that this objective is close to the self-supervised learning objectives with a symmetry breaking property and present an approach to optimize it in a parametric manner, thus enabling scaling unlike many of the previous approaches-- showing that it is possible to learn eigenfunctions for a large dataset like ImageNet, along with OOD generalisation.

### Strengths
- Through this work, the authors provide additional arguments for learning the principle eigenfunctions for unsupervised representation learning by considering the integral operator of a pre-defined kernel and the data distribution, which other lines of work in this area have argued to be at the core of many machine learning problems.
- Over pre-existing work such as Johnson et al and Haochen et al, Neural Eigenmap shows better scalability with the number of eigenfunctions, and learning of an ordered structure in the representation. Also, specific to graph representation learning, the proposed method has faster forward and backward passes.
- Neural Eigenmap shows similar retrieval performance such as Barlow Twins (BT) and Spectral Contrastive Learning (SCL) on image retrieval benchmarks such as COCO etc with much fewer representation dimensions-- the authors show this is 16x fewer.

### Weaknesses
 - Maybe not a weakness, but in this kind of learning, how do we know which kernel to pre-define?

* With respect to the linear probe experiments for unsupervised representation learning, a few questions-
    * Why have the authors reproduced Barlow Twins themselves when, if I am not mistaken, the top-1 accuracy for ImageNet with a ResNet-50 pretrained encoder is available (like it is for SCL, which the authors use)?
    * Can you make any inferential comments on the link between batch size, number of epochs, projector dimensions?
    * For Barlow Twins, the authors in that paper report that the model has highest top-1 accuracy at a batch size of 1024, so like why are the results selected for a batch size of 2048 in this paper?

### questions:
 - Maybe something I am missing: while talking about the connection between PCA and the proposed method in the subsection on “Learning ordered representations”, I have a general doubt— isn’t PCA a special, linear case of spectral analysis on Euclidean space— and hence follows the observation on ordering and the principled components carrying the most information, or is there a deeper connection to talk about here?

- Something I didn’t understand: why does replacing $\hat{\psi_{X_B}}$ by $\psi_{X_B}$ not affect the optimal classifier? (when talking about the linear probe evaluation)

* What are the benchmarks that ignore, and that which do not ignore feature importance? Are they based on the task of image retrieval?

* The authors remark that the proposed method has faster forward/backward passes than graph neural networks which have a computational complexity of $O(n^3)$-- what is the computational complexity of this method?

### Questions
- Maybe something I am missing: while talking about the connection between PCA and the proposed method in the subsection on “Learning ordered representations”, I have a general doubt— isn’t PCA a special, linear case of spectral analysis on Euclidean space— and hence follows the observation on ordering and the principled components carrying the most information, or is there a deeper connection to talk about here?

- Something I didn’t understand: why does replacing $\hat{\psi_{X_B}}$ by $\psi_{X_B}$ not affect the optimal classifier? (when talking about the linear probe evaluation)

* What are the benchmarks that ignore, and that which do not ignore feature importance? Are they based on the task of image retrieval?

* The authors remark that the proposed method has faster forward/backward passes than graph neural networks which have a computational complexity of $O(n^3)$-- what is the computational complexity of this method?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes the use of NeuralEF, a neural network that aims to learn the eigenfunctions of a linear operator from large-scale data, for purposes of parametric representation learning; this is termed as a neural eigenmap. The paper provides connections between the formulation of the proposed approach and those of existing self-supervised learning methods. The paper also shows the application of the method to settings with indefinite kernels for the affinity matrix.

### Strengths
The paper leverages a recently proposed approach for eigenfunction estimation in a commonly used application of eigendecompositions for learning. The reasoning is straightforward and the results are compelling.

### Weaknesses
Some of the choices made are not clearly explained. For example, the choice of enabling/disabling stop_grad is said to allow/not allow for ordered eigenfunctions/structured representations, but there is no discussion of this (e.g., what does stop_grad do). This is also implied in the choice of elements with small indices vs. random elements being chosen when evaluating these two approaches.

The proposed method is similar in Formulation to Barlow Twins, but the numerical comparison is focused on a few experiments.

Minor comments:

* Just before eq. 3, define BN layers (as batch normalization layers?)
* Section 4: "principle eigenfunctions" should be "principal eigenfunctions".

### Questions
Can the optimization in (3) be connected to the original definition of the eigenfunction from (1)?

Can the authors elaborate on how the ordered structure arises in NeuralEF? Particularly given that the orthogonality requirement for eigenvectors in an eigendecomposition is not present in the NeuralEF formulation (8) to obtain the set of "learned" eigenvectors.

After eq. 10, should $\gamma$ be $\lambda$?

Is there intuition as to why (9) works better than (10)?

Can the authors elaborate on the scalability of the proposed approach vs. that of Johnson et al. (2022)?

Section 6.2 first sentence refers to Section 6.2 - is that a typo?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Based on NeuralEF, author(s) proposed the Neural Eigenmap that is a structured and adaptive deep presentation. Under the new formulation, an objective function can resemble those popular self-supervised learning methods. The benefits that the Neural Eigenmap can offer is that the learned representations are structures which preserve the most important information from the data. At the same time the Neural Eigenmap has been extended for graph data, building on a theoretical result.

### Strengths
1. Clearly describe the relations among Neural Eigenmap, SSL methods, and NeuralEF.  
2. Although it builds on the combination of NeuralEF and SSL Kernel, the benefits from there are clearly derived.
3. The other contribution is to generalize the Neural Eigenmap for graph data. The new formulation can be scaled up for larger graph datasets.

### Weaknesses
The paper is well presented with clear contributions in a very simple form.

### Questions
Thanks for providing the accompany code for the algorithm.   

1. I have tracked the training process over graph dataset arXiv. It seems to me that there is no special ways to take the augmented nodes. It seems to me it quite arbitrarily to construct X^+, although adjacency matrix is applied.

2. Not sure why the first term in (12) is squared in the code.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
