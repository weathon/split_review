# Multimodal Molecular Pretraining via Modality Blending

- Decision: Accept
- Avg Score: 6.00
- Scores: 5, 8, 5, 6

## Abstract
Self-supervised learning has recently gained growing interest in molecular modeling for scientific tasks such as AI-assisted drug discovery. Current studies consider leveraging both 2D and 3D molecular structures for representation learning. However, relying on straightforward alignment strategies that treat each modality separately, these methods fail to exploit the intrinsic correlation between 2D and 3D representations that reflect the underlying structural characteristics of molecules, and only perform coarse-grained molecule-level alignment. To derive fine-grained alignment and promote structural molecule understanding, we introduce an atomic-relation level "blend-then-predict" self-supervised learning approach, \name{}, which first blends atom relations represented by different modalities into one unified relation matrix for joint encoding, then recovers modality-specific information for 2D and 3D structures individually. By treating atom relationships as anchors, \name{} organically aligns and integrates visually dissimilar 2D and 3D modalities of the same molecule at fine-grained atomic level, painting a more comprehensive depiction of each molecule.
Extensive experiments show that \name{} achieves state-of-the-art performance across major 2D/3D molecular benchmarks. We further provide theoretical insights from the perspective of mutual-information maximization, demonstrating that our method unifies contrastive, generative (cross-modality prediction) and mask-then-predict (single-modality prediction) objectives into one single cohesive framework.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a molecular representation learning method that fusing the information from both 2D and 3D molecule structures. A unified relation matrix is constructed to describe the relationships between each pair of atoms, so that both 2D and 3D information can be injected into the matrix for fusion. For the 2D structure, based the bonds between atoms, shortest path and edge type information can be calculated for each entry of the relation matrix, and for the 3D structure, the entry can records the 3D Euclidean distance between atoms. The 2D and 3D information are blended in one relation matrix and a Transformer backbone is trained to recover the full information.

### Strengths
1. The idea of using a relation matrix to unify the 2D and 3D information for molecular representation learning is novel.
2. Theoretical analysis provide more insights to the proposed method.
3. The paper is well writen and structured and easy to follow.

### Weaknesses
1. The information gathered in the relation matrix is quite limited and much information in the original structure is lost, especially those in the 3D structure. The matrix construction is quite similar to the work of  "One transformer can understand both 2d & 3d molecular data" published in ICLR 2023.
2. Ablation studies on blending two masks should be provided.
3. Some details of the experimental setup is missing.

### Questions
1. Does the author run all baseline methods on the experimented splits or cite some results from other papers? For the results in Table 4, does the  single-modality mask-then-predict strategies use the same network as the proposed blending strategy?

2. In Table 4, I think the author compares blending three mask to using only one mask. What's the effect of blending two masks?

3. The conclusion in section D.1 is not well supported, since different 3D networks may perform differently and may have different speed of convergence. It's not enough to draw the conclusion by comparing the proposed method to only one 3D model.

4. Why run ablation studies on different datasets and different tasks?

### Soundness
3 good

### Presentation
3 good

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
This paper proposes MolBlend, a method that explores the intrinsic alignment between 2D and 3D for molecule pretraining. MolBlend aims to conduct the 2D-3D pretraining based on the atom relations, which is finer-grained than previous works.

### Strengths
- The key idea is clear and straightforward: to use the attention module to help augment the 2D-3D atom-relation for molecule pretraining.
- The theoretical proof is interesting.

### Weaknesses
 - The motivations are not clearly claimed or supported.
    - For instance, on Page 2, the authors say that they “observe that although appearing visually distinct … are intrinsically equivalent as they are essentially different manifestations of the same atoms and their relationships”. What does “equivalent” mean here? A lot of 2D-3D pretraining methods start by saying such two modalities are complementary to each other. It is unclear what specific advantage is gained by reframing them as equivalent rather than complementary.
    - Additionally, on Page 2, what is the motivation to feed both modalities as one unified data structure to one single model in MoleBlend? Why not use separate models or a model with distinct branches for each modality, as is common in multimodal learning?

- Notations are misleading in Sec 3.1.
    - Why is $R_{spd}$ required? Because they can be derived from $R_{edge}$? The relationship between these different relation matrices needs to be clarified. It's not clear if they are redundant or if each provides unique information. Specifically, what information is captured in $R_{spd}$ that is not already present in $R_{edge}$ or $R_{distance}$?
    - For Eq 1, the notation should be $R_{2D3D,S}$ (with S in the subscript).
    - Is $R_{2D3D}$ the masked version of $R_{spd}, R_{edge}, and R_{distance}$? The masking process is not clearly described. What specific masking strategy is used, and how does it affect the learning process?

- Other minor comments:
    - The title can be further improved, especially that what modalities are considered is not explicit. A more descriptive title would improve clarity.
    - The distance modeling is invariant. A more advanced equivariant model is preferred here. The current model does not explicitly account for the geometric properties of 3D space, which could limit its ability to generalize to different orientations of the same molecule.
    - It would be better to explicitly add a column in the result tables on what backbone models are pretrained/comparing. This is crucial for comparing the results with existing methods.
    - The citation of 3D InfoGraph is wrong. Please fix it.

### Questions
- I am confused about the Fig 1.b. Does this mean the input can be either 2D or 3D, and the output can be both 2D and 3D?

### Soundness
3 good

### Presentation
3 good

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
The authors proposed to align molecule 2D and 3D modalities at the atomic-relation level and introduce MOLEBLEND. This multimodal molecular pretraining method explicitly utilizes the intrinsic correlations between 2D and 3D representations in pertaining. Extensive evaluation demonstrates that MOLEBLEND achieves state-of-the-art performance over diverse 2D and 3D tasks, verifying the effectiveness of relation-level alignment.

### Strengths
1. The paper is well-written and easy to understand.
2. The authors conducted extensive experiments on both 2D and 3D molecule tasks and showed their good performance.

### Weaknesses
1. The authors did not discuss the training time cost of different pretraining methods.
2. A series of pertaining baselines are missed in related works and comparisons. For example:

[1] Xu M, Wang H, Ni B, et al. Self-supervised graph-level representation learning with local and global structure. ICML 21.  
[2] Zhang Z, Liu Q, Wang H, et al. Motif-based graph self-supervised learning for molecular property prediction. NeurIPS 21.  
[3] Zaidi S, Schaarschmidt M, Martens J, et al. Pre-training via denoising for molecular property prediction. ICLR 23.  

3. The theoretical analysis is good. However, could the authors provide more insights into why MOLBLEND overperforms existing methods theoretically?

4. How does the different choice of encodings for 2D/3D modalities influence the pretaining?

### Questions
Please see the weakness.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper seeks to understand the inherent connection between 2D and 3D representations, capturing the essential structural attributes of molecules through atomic-relation level multimodal pretraining techniques. 
In this process, the authors initially combine atom relations from various modalities into a single cohesive matrix for combined encoding, and subsequently retrieve specific information for both 2D and 3D structures separately.

### Strengths
1. Learning the qualified representation of molecules is important for various downstream tasks.
2. To the best of my knowledge, this is the first work that aligns atom-level representation for 2D and 3D representations of molecules.

### Weaknesses
1. As highlighted by the authors, earlier studies typically aligned different modalities at a broader molecule level, potentially hindering the capture of detailed molecular structures. Initially, when considering atom-level depictions of a molecule, our focus might be on the atom-level rather than the atomic-relation level. For instance, we might design a model that determines 3D atom coordinates based on a 2D molecular graph. What's the rationale behind emphasizing atomic-relation level multi-modal pretraining? It would be beneficial to provide a thorough reasoning in the methodology section and draw empirical comparisons in the experiments.

2. The experimental findings appear to be underwhelming. MoleBlend's performance, as shown in Tables 1 and 2, doesn't seem to fare well against prior studies.

### Questions
Provided above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
