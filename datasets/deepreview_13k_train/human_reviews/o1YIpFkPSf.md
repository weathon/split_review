# Hyperbolic Visual-Semantic Alignment for Structural Visual Recognition

- Decision: Reject
- Scores: 6, 3, 6

## Abstract
Visual and semantic concepts inherently organize themselves in a hierarchy, where a higher-level textual concept, e.g., Animal, entails all images containing, e.g., Cat. Despite being intuitive, conventional visual recognition systems strive to establish single-level correspondence between images and semantic concepts, and do not explicitly capture the hierarchical relationships that exist. We present HVSA to probe multi-level semantic information, from fine-grained to fully abstracted, within the tree-shaped hierarchy to realize structural visual recognition. Our main idea is to learn shared representations of images and semantic concepts in the hyperbolic space. Hyperbolic spaces possess suitable geometric properties to embed tree-like data structures, thus will help capture the underlying hierarchy. While it is challenging to acquire structure alignment of the two modalities, we achieve the goal through a joint optimization process guided by two primary objectives. First, we propose hierarchy-agnostic visual-semantic alignment, which leverages a Gaussian mixture VAE to establish a “flat” representation space shared by both modalities. Second, we introduce hierarchy-aware semantic learning to cultivate a “hierarchical” feature space for semantic concepts solely through hyperbolic metric learning. These two distinct objectives operate on different granularity and synergistically contribute to hierarchical alignment of visual-semantic features, ultimately enhancing structural image understanding. HVSA shows high efficacy and generality, as evidenced by its notable performance improvements across six datasets, for both image-level (i.e., ImCLEF07A, ImCLEF07D and tieredImageNet-H) and pixel-level (i.e., Cityscapes, LIP, and PASCAL-Person- Part) visual recognition. Our code shall be released.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a novel approach named HVSA (Hyperbolic Visual-Semantic Alignment) for the task of structural visual recognition. HVSA consists of two key components: hierarchy-agnostic visual-semantic alignment and hierarchy-aware semantic learning. Experimental results on various tasks and datasets demonstrate the effectiveness of the proposed method.

### Strengths
1. The paper provides a compelling motivation for incorporating the hierarchical nature of features into visual recognition tasks.

2. The authors perform comprehensive experiments across various tasks and datasets, yielding convincing results.

### Weaknesses
1. The paper primarily discusses the advantages of conducting feature learning in hyperbolic space compared to Euclidean space in a theoretical manner, highlighting the inherent exponential growth characteristic of hyperbolic embeddings in capturing hierarchical structures. However, there is a lack of experimental evidence to support this design choice. A potential baseline approach could involve performing all the loss terms in Euclidean space, such as triplet loss in Euclidean space. Specifically, the paper lacks a direct comparison of the performance of the proposed method when the visual and semantic embeddings are learned in Euclidean space versus hyperbolic space, making it difficult to isolate the impact of the hyperbolic space on the overall performance. The theoretical arguments are not sufficiently backed by ablation studies that directly test the contribution of the hyperbolic space.

2. The paper does not provide explicit details on how the taxonomy of labels in different datasets is obtained. It would be beneficial to include information regarding the acquisition of label taxonomy and potentially include tree structures to visually illustrate the hierarchical relationships within the taxonomy. The absence of this information makes it difficult to assess the validity of the hierarchical structure used and its potential impact on the results. For example, are the taxonomies manually curated or automatically generated? What are the criteria for defining the hierarchical relationships?

3. The experiment section lacks a brief introduction to the metric terms CV and CMAP. This makes it difficult for readers unfamiliar with these metrics to fully understand the results and the performance of the proposed method. Without a clear definition, the significance of the reported CV and CMAP values is unclear, hindering a comprehensive evaluation of the experimental findings.

### Questions
This is not a question regarding this paper's issue, but more like a open discussion. Since the paper demonstrates the benefits of incorporating taxonomy as prior knowledge for recognition tasks in a close-vocabulary setting. It raises an intriguing question about the scalability of this approach to an open-vocabulary setting. Considering the superior performance achieved by visual-semantic alignment methods like CLIP on in-the-wild data, I am wondering whether this work can provide similar advantages in the open-vocabulary domain.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors of the paper introduced a method for visual-semantic alignment in hyperbolic space. They presented a hierarchy-agnostic approach to visual-semantic alignment, complemented by hierarchy-aware semantic learning. To demonstrate the effectiveness of their proposed model, experiments were carried out on classification and segmentation tasks across six datasets.

### Strengths
1. The visual-semantic alignment from a probabilistic perspective in hyperbolic space is novel. 
2. The hierarchy-agnostic idea is innovative. 
3. Extensive experiments were conducted, covering multiple tasks.

### Weaknesses
1. The logic flow is broken, one can hardly see the connection between 3.1, 3.2. It will be very difficult (even for a hyperbolic learning researcher) to reproduce the method by reading the ``Method'' section. 

2. Many important descriptions are missing or even incorrect, e. g. ,

>  " ... the mean of the wrapped normal mixture distribution is calculated by Möbius addition. " is not logically correct.

>  " ... resulting in $y_{l,i} = \mathbf{\mu}_l + \mathbf{\Sigma}_l$ ...", you cannot add a mean vector to a covariance matrix.

>  The reconstruction loss is neither explained nor linked to a reference

3. The tables basically show "we have better numbers", but the analysis lacks in-depth understanding of why each part works.

- In the submission, eq. (9) is in essence the same as eq. (32) in (Ganea et al., 2018), eq. (10) is in essence the same as eq. (33) in (Ganea et al., 2018). The only notation difference is that
1. The authors use $(z_a, z_p) \in P$ for positive pairs and $(z_a, z_n)\in N$ for negative pairs
2. (Ganea et al., 2018) uses $(u, v) \in P$ for positive pairs and $(u', v') \in N$ for negative pairs.

In the submission, eq. (11) is in **EXACTLY the same** as eq.(28) in (Ganea et al., 2018).

However, in (Ganea et al., 2018), eq. (28) and eq. (33) is used for defining the cone, which is the **core contribution, such that the word "cone" is in the title of   (Ganea et al., 2018)**.

In this submission, those cone definitions are neither related to "visual-semantic alignment from a probabilistic perspective" nor "hierarchy-agnostic perspective", which I found conceptually novel.

- In the authors' last comments, they defined the compositional label with an example: ``a bus might have three labels "vehicle, large-vehicle, bus" in Cityscapes taxonomy``, which is the ``grantparent_class`` to ``parent_class`` to ``children_class`` relationship on the hierarchy.  (Liu et al., 2020) did the same, but on the WordNet hierarchy, I didn't see the authors fundamental differences.

- I would like to reiterate that ``"we have better numbers" is NOT in-depth analysis``. One of the authors' core contributions, ``Probabilistic Label Embedding``'s effectiveness against non-probabilistic embeddings, is NOT supported by any of those 10 Tables. Furthermore, the term 'compositional labels' is not explicitly used or explored in Section 4.1, despite the claim that Section 4.1 addresses the compositional properties of semantic concepts. This lack of explicit modeling and analysis of compositional labels undermines the novelty of the approach.

### Questions
Please see the weaknesses. besides, I have one more question regarding the motivation

> What is the aim of hierarchy-agnostic alignment when we already have the hierarchy information? Why is the ``agnostic'' part important?

### Soundness
2 fair

### Presentation
3 good

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
This paper introduces a method named HvsA for structural visual recognition. HvsA consists of two stages. In “hierarchy-agnostic visual-semantic alignment”, it first encodes images and semantic labels in the hyperbolic space. Then it utilizes a Gaussian mixture VAE to align visual embedding with label embedding to yield a shared representation space. While in “hierarchy-aware semantic learning”, it leverages triplet metric learning over label space to push the label embeddings away for those without hierarchical relationships while pull close those with similar semantics. Experiments are conducted over six datasets, showing the effectiveness of the method.

### Strengths
1. The paper is well-written and easy to follow.
2. The concept of encoding hierarchical label embeddings and aligning visual embeddings is reasonable. Furthermore, the introduction of a triplet loss designed to operate within the label space, thereby facilitating the alignment of visual embeddings in a more hierarchical manner, is sound.
3. The experimental results are competitive.

### Weaknesses
1. The definition of q_θ in Eq 7 and 8 are missing.
2. The training and inference computation efficiency is not presented.
3. Minor issue:  
  3.1. Typo: Section 3.2, Task Setting: “An undirected edges (vi, vj) ∈ E indicates that the class i is a superclass of label i” It should be “label j” instead of “label i”.  
  3.2. Typo: Section 3.2.1 Hyperbolic Gaussian Mixture VAE: “we seek to align visual embedding with visual embedding to yield a shared representation space.” Is it “align visual embedding with LABEL embedding”?

### Questions
Are the authors planning to release the source code for this work?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
