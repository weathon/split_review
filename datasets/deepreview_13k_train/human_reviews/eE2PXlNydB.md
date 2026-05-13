# Learning Clustering-based Prototypes for Compositional Zero-Shot Learning

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Learning primitive (i.e., attribute and object) concepts from seen compositions is the primary challenge of Compositional Zero-Shot Learning (CZSL). Existing CZSL solutions typically rely on oversimplified data assumptions, e.g., modeling each primitive with a single centroid primitive presentation, ignoring the natural diversities of the attribute (resp. object) when coupled with different objects (resp. attribute). In this work, we develop ClusPro, a robust clustering-based prototype mining framework for CZSL that defines the conceptual boundaries of primitives through a set of diversified prototypes. Specifically, ClusPro conducts within-primitive clustering on the embedding space for automatically discovering and dynamically updating prototypes. To learn high-quality embeddings for discriminative prototype construction, ClusPro repaints a well-structured and independent primitive embedding space, ensuring intra-primitive separation and inter-primitive decorrelation through prototype-based contrastive learning and decorrelation learning. Moreover, ClusPro effectively performs prototype clustering in a non-parametric fashion without the introduction of additional learnable parameters or computational budget during testing. Experiments on three benchmarks demonstrate ClusPro outperforms various top-leading CZSL solutions under both closed-world and open-world settings. Code will be released.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a clustering-based prototype mining framework namely CLUSPRO, for Compositional Zero-Shot Learning. 
Specifically, it considers within-primitive online clustering for automatically discovering and dynamically
updating prototypes. Besides, it models prototype-based primitive representation learning for promoting intra-primitive separation and inter-primitive decorrelation. Experimental results on three datasets demonstrate the superiority of the proposed method against existing methods.

### Strengths
Overall, the paper is well written and easy to follow.
The motivation behind addressing CZSL is clear and convincing.
The technical contributions are solid and novel.
The algorithm details are well provided and it should be possible to reproduce the results reported in the paper.

### Weaknesses
Figure 2 shows  the clustering-based prototype mining framework, while it is still unclear about the whole pipeline for CZSL. It is encouraged to introduce the complete network architecture in the main paper or supplementary material. It will be help to understand why the proposed method can achieve new state-of-the-art performance.

In the experiments, it is concerned about why all the compared methods including CLUSPRO employ the same ViT backbone,
to avoid the unfair comparisons between ViT-B and ViT-L. 

It is interesting to know more details about the baseline model, including network structure and training loss.

### Questions
see the weaknesses above please.

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
This paper reveals that exsiting compositional zero-shot learning (CZSL) methods only consider an isolated centroid for each primitive, ignoring rich and diverse intra-primitive patterns. To address this, the authors propose a clustering-based method CLUSPRO to learn a well-structured and independent embedding space with multiple discriminative prototypes for each primitive, thus improving CZSL. Specifically, CLUSPRO alternates between two steps: 1) performing within-primitive online clustering to automatically discover and dynamically update prototypes, and 2) using prototype-based primitive representation learning to encourage intraprimitive separation and inter-primitive decorrelation.

### Strengths
- This paper is well-motivated, highlighting that a single centroid primitive representation demonstrates limited tolerance to intraprimitive variance.
- The proposed method CLUSPRO is reasonable and has a good performance across three benchmarks under both closed-world and open-world settings.
- The authors present a comprehensive analysis of their method CLUSPRO.

### Weaknesses
 - My major concern is the number of prototype. In the experiments, the number of prototypes $K$ is empirically set to 5, which may not ne a good strategy. Additionally, using the same number of prototypes for all attributes seems unreasonable. Are there any automatic methods for discovering prototypes, thus mitigating the need for manually setting this number?
- Does performing clustering on the entire dataset will face resource limitations when dealing with very large datasets?

### Questions
Please see the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes clustering-based method for compositional zero-shot learning.
Specifically,

### Strengths
Clear presentation

### Weaknesses
Major problem:

Problem1. The definition of Compositional Zero-shot Learning (CZSL) is not correctly used.
The authors mentioned CZSL requires the model to recognize unseen compositions without additional training data, but in your method, you use pretrained CLIP trained by large-scale dataset: CLIP is trained from millions text-image pairs from web.
In other word, all your claimed unseen compositions are seen by CLIP actually.
Thus, a key question is emerged: if your visual&text encoders never meet your test compositions, can the seen and unseen compositions be seperated?
Please provide the results that using other visual&text encoders or using vision-language models whose pretrained training datasets have no overlap with the evaluted datasets.

Problem2. Besides, in the original paper of CLIP, it has clearly claimed they changed the definition of ZSL from class-level to dataset-level. "In computer vision, zero-shot learning usually refers to the study of generalizing to unseen object categories in image classification (Lampert et al., 2009). We instead use the term in a broader sense and study generalization to unseen datasets." ﻿ This excerpt is from Section 3.2 of the CLIP paper. There is a significant gap between CLIP’s definition of zero-shot learning and the CZSL task you are addressing, which still focuses on classifying unseen composition categories. This difference is substantial and cannot be overlooked.

In a short, I suggest the proposed method is a transductive classification method insteat of ZSL method actually since the pre-trained CLIP have been exposed to numerous unseen composition samples.

Problem3. 
You only compare your method to CLIP-based CZSL methods, but there are many methods that do not use CLIP.
I know those non-CLIP methods perform worsely than CLIP-based methods.
But, as I said in Problem1&2, since CLIP have been exposed to numerous unseen composition samples, the experiments are extramely unfair for other non-CLIP SOTAs.

Problem4. Why only consider the diversities of the attribute, but do not for the objects?

### Questions
See weakness

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a clustering-based prototype mining framework for CZSL which conducts within-primitive clustering on the embedding space for automatically discovering and dynamically updating prototypes. These representative prototypes are subsequently used to repaint a well-structured and independent primitive embedding space, ensuring intra-primitive separation and inter-primitive decorrelation through prototype-based contrastive learning and decorrelation learning. Experiments on three benchmarks demonstrate CLUSPRO outperforms top-leading CZSL solutions under both closed-world and open-world settings.

### Strengths
- Overall this paper is well-written and is easy to understand.
- The motivation is reasonable and the proposed framework is a little novel for CZSL.
- The CLUSPRO outperforms top-leading CZSL solutions under both closed-world and open-world settings on three benchmarks.

### Weaknesses
 - There is a lack of discussion and citation of some related works. In ZSL/CZSL fields, prototype learning is wide adopted in the works [A][B]. The Local-aware Prototype Assignment module is also similar to the previous work [C], but the necessary discussion is absent.

- The overall novelty is limited. The Local-aware Prototype Assignment technique is adopted in the work [C], and the Prototype-based Contrastive Learning have been used in previouse works (e.g., [A]).

- Writing of Chapter 3.3 could be improved. The authors do not make it clear how the K prototypes are obtained. With reference to the context, is it means k-means clustering results on visual fetaures?  In addition, when the variable notations appear for the first time, the authors should give an obvious comment (e.g., $n$ in $f_{n}$) for reducing ambiguity.

### Questions
In the Prototype-based Contrastive Learning, the strategy encourages each primitive feature $f_n$ to
be similar to its assigned prototype $P+$ and dissimilar to all other $K(M+N)−1$ irrelevant prototypes
$P-$. It means that the $K-1$ prototypes belonging to the same primitive but with different assignments are treated as negative samples in the same way as prototypes  $K(M+N-1)$ of other primitives. 
Does this have a  impact on representation learning?

### Soundness
2

### Presentation
2

### Contribution
2
