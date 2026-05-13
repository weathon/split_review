# On the Theoretical Analysis of Dense Contrastive Learning

- Decision: Reject
- Scores: 6, 6, 6

## Abstract
Contrastive learning has achieved outstanding performance in self-supervised learning. However, the canonical image-level matching pretext is unsuitable for multi-object dense prediction tasks like segmentation and detection. Recently, numerous studies have focused on dense contrastive learning (DCL) that adopts patch-level contrast to learning representations aware of local information. Although empirical evidence has validated its superiority, to date, there has not been any theoretical work that could formally explain and guarantee the effectiveness of DCL methods, which hinders their principled development. To bridge this gap, using the language of spectral graph theory, we establish the first theoretical framework for modeling and analyzing DCL by dissecting the corresponding patch-level positive-pair graph. Specifically, by decoupling the image-level and patch-level supervision, we theoretically characterize how different positive pair selection strategies affect the performance of DCL, and verify these insights on both synthetic and real-world datasets. Furthermore, drawing inspiration from the theory, we design two unsupervised metrics to guide the selection of positive pairs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes the first theoretical framework to model and analyze dense contrastive learning (DCL) methods. This is done by constructing a patch-level positive pair graph and using concepts from spectral graph theory. By decomposing the adjacency matrix of the patch-level graph using the Kronecker product, the framework is able to decouple the image-level and patch-level supervision. Theoretical and experimental analysis shows there is a trade-off between the quantity and correctness of positive pairs selected in DCL. Matching more positive pairs reduces eigenvalues but increases labeling error rate. Two unsupervised metrics are introduced - Patch Confusion Rate (PCR) and patch-level contrastive loss - to guide positive pair selection in DCL without requiring ground truth labels. Overall, the paper provides the first theoretical understanding of DCL methods through the analysis of the patch-level positive pair graph and makes both theoretical and practical contributions.

### Strengths
1. This work first proposes a theoretical framework to model and analyze dense contrastive learning (DCL) methods.
2. Theoretical analysis is clear, and the experimental results can support the claims.
3. Two novel metrics are proposed: PCR and patch-level contrastive loss.

### Weaknesses
1. This paper does not show enough results to support the superiority of the proposed metrics. The experiment cannot support these metrics can be used to determine positive pair selection. 
2. Experiment on a real dataset is needed to validate the application of proposed theory and metrics to improve DCL models.

### Questions
The authors mentioned that the proposed metrics can determine positive pair selection strategies. The authors reckon smaller PCR and lower loss reveals a better model, however, the results in Table 3 cannot prove it. The authors need explain more for the case 5×5.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a theoretical framework for dense contrastive learning (DCL) in computer vision for downstream tasks. While contrastive learning has excelled in image-level matching, DCL explores patch-level contrast for local information. The paper dissects the patch-level positive-pair graph using spectral graph theory and highlights the impact of different positive pair selection strategies on DCL performance. The paper proposes two unsupervised metrics based on their theoretical insights to guide positive pair selection. They empirically validate their framework on synthetic datasets, providing a foundational understanding of DCL's working principles and generalization ability. This work aims at developing principled DCL methods for dense prediction tasks.

### Strengths
- The introduction of two unsupervised metrics for guiding the selection of positive pairs is a novel contribution. These metrics offer a practical way to evaluate and fine-tune dense contrastive learning systems.
- The study aligns with current trends in the field of machine learning, particularly in self-supervised and contrastive learning, which adds relevance and interest to the research.

### Weaknesses
The main problem of the method seems to be that by switching from natural images to patches, the results from HaoChen et al. (2021) cannot be carried over into DCL.

I make a few points, mainly on the positive pairs selection process and the role of the augmentations distribution {\mathcal A}:

In HaoChen et al. (2021), it is assumed that all natural images \overline{X} have the same distribution \mathcal P_{\overline X},  e.g. a mixture of manifolds, and each image is specified by a single class r. Furthermore, there is a distinction between the population distribution over \overline{X} and the distribution \mathcal A(.|\overline{x}), which is crucial to compute the weights used in the adjacency matrix. The population graph is the graph of all augmentations, including crops. \
Therefore, in HaoChen et al. (2021), wxx’ = E_{\overline{x} \in P_\overline{X}}(A( x| \overline{x}), A( x’| \overline{x})), is a marginal probability of generating a pair (x,x’)  from an image \overline{x}, sampled from P_{\overline{X}).\
If the augmentation would not include cropping, this probability is always 1, because any other augmentations, like rotation, jittering, blurring, etc., do not change the class.  

The process of selecting a positive pair is envisioned in this paper in two steps:

1. Select patches on the original image.
2. Do the augmentation, like jittering and transformations.


In equation (3) and (5) it is not clear:

1) if cropping is allowed on the views.
2) If a view includes the choice of a patch.

- If cropping is allowed on views and patches are chosen on the cropped views, then the purpose of B in (5)  is useless since it is not possible to know if the extracted patches are from the same class. As in Figure 1, right, one patch could be a leaf and another a dog head.
- If cropping is not allowed on views and patches are chosen on views, then again, positive pairs are hard in case of random rotations or random stretching since even if on the same location in the different views, they can be of different classes. Then again, B has no purpose, as patch classes cannot be determined.
- if cropping is not allowed and patches are chosen on the natural image, then \mathcal A, namely the probability, given a natural image \overline{x}, that the augmentation x and x’ form a positive pair, makes the problem trivial. In fact, on the image \overline{x}, whatever patch is chosen, the augmentation can stretch them, change colour, blur or rotate them; they will always be of the same class if they come from the same region. Therefore, B is trivial: only patches from different locations can differ. 

In this last case, which seems to be the choice of the paper, however, the probability of being a positive pair is still attributed to the views, while it is simply B, the matrix sanctioning the connections. Therefore, it seems that wxx’ is either 1 or 0.

In the proof of Theorem 2.4, it seems that it is possible to choose a patch both from the natural image and a patch from some of its views. \
Then, suppose that \overline{p} is a patch from \overline{x}, and that x is a random crop of \overline{x} that does not include \overline{p}, and p is a patch from x. Then p and \overline{p} could even be of different classes, as argued above.\ 
Therefore, what is the meaning of the sentence  “p is the corresponding patch of \overline{p}”?   Furthermore, a clear definition of the encoding f for patches is not given, as it is provided only for views (see page 12 Proof of Theorem 2.3); however, in the proof of Theorem 2.4, f(p) is used. 

Other observations:  

- F is used in many equations (e.g. in equation 1, it should be f) without being suitably introduced. 
- In Theorem 2.3, the function f does not appear, though it appears in C Proof, page 12, and it is not said that f should be an embedding function,  and here, too, F remains purposeless. Also, it seems that \psi^y cannot be defined as 2\epsilon since the similarity between augmentations (including cropping) is different from the similarity between views as stated here, where patch/cropping and other augmentations are decoupled. 
- The relation between B  as a circulant matrix and the general matrix must be discussed. I could not find an explanation in the appendix.

- In theorem 2.8, it seems that h(l) is not used. Further, the sentence “the spatial distance of a pair will simultaneously increase, which means a larger labeling error rate α” should be made precise.

- D in the appendix comes from HaoChen et al. (2021).
- In Table 2, it probably needs to be noticed that for COCO instance segmentation, Mask R-CNN is used.
  
No sensible new theory is added. Furthermore,  many statements remain unjustified. The overall writing quality needs improvement in terms of clarity and organization. The authors state that their theoretical framework can be extended to other approaches, but they only experiment on one, namely PixContrast.

### Questions
- In the paper, eigenvalue distributions are discussed about graph matrices. How were these distributions simulated, and what significance do they hold for the study?
- Why is the eigenvalue µ_(k+1) of B a good surrogate to compute error? (See Training and Evaluation section).
- What is F in Equation (1)?
- In the explanation on page 7, last paragraph, what is meant in the sentence  “positions in the original image are smaller than a given threshold”?
- Most notably, why strictly follow HaoChen et al. (2021), while the authors have written that it is hard to extend their approach to object detection and segmentation.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper uses the language of spectral graph theory to establish the first theoretical framework for modeling and analyzing DCL by dissecting the corresponding patch-level positive-pair graph. Specifically, by decoupling the image-level and patch-level supervision, the authors theoretically characterize how different positive pair selection strategies affect the performance of DCL, and verify these insights on
both synthetic and real-world datasets.

### Strengths
The paper is well-organized and easy to follow.

Using the Kronecker product to decompose the adjacency matrix of the patch-level positive-pair graph is novel and make sense.

### Weaknesses
1. Missing important references about DCL methods (iBOT, ADCLR, PQCL). 

[1] Zhou J, Wei C, Wang H, et al. ibot: Image bert pre-training with online tokenizer[J]. ICLR 2022.

[2] Zhang S, Zhu F, Zhao R, et al. Patch-level contrasting without patch correspondence for accurate and dense contrastive representation learning[J]. ICLR 2023.

[3] Zhang S, Zhou Q, Wang Z, et al. Patch-level Contrastive Learning via Positional Query for Visual Pre-training[J]. ICML 2023.

### Questions
I have no further questions.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
