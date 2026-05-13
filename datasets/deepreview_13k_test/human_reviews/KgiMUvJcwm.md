# IgSeek: Fast and Accurate Antibody Design via Structure Retrieval

- Decision: Reject
- Scores: 3, 3, 3, 5

## Abstract
Recent advancements in protein design have leveraged diffusion models to generate structural scaffolds, followed by a process known as protein inverse folding, which involves sequence inference on these scaffolds. However, these methodologies face significant challenges when applied to hyper-variable structures such as antibody Complementarity-Determining Regions (CDRs), where sequence inference frequently results in non-functional sequences due to hallucinations. Distinguished from prevailing protein inverse folding approaches, this paper introduces IgSeek, a novel structure-retrieval framework that infers CDR sequences by retrieving similar structures from a natural antibody database. Specifically, IgSeek employs a simple yet effective multi-channel equivariant graph neural network to generate high-quality geometric representations of CDR backbone structures. Subsequently, it aligns sequences of structurally similar CDRs and utilizes structurally conserved sequence motifs to enhance inference accuracy. Our experiments demonstrate that IgSeek not only proves to be highly efficient in structural retrieval but also outperforms state-of-the-art approaches in sequence recovery for both antibodies and T-Cell Receptors, offering a new retrieval-based perspective for therapeutic protein design.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces IgSeek, a novel structure-retrieval framework that infers CDR sequences by retrieving similar structures from a natural antibody database. Specifically, IgSeek employs a simple yet effective multi-channel equivariant graph neural network
to generate high-quality geometric representations of CDR backbone structures. Then, it aligns sequences of structurally similar CDRs and utilizes structurally conserved sequence motifs to enhance inference accuracy. The authors claim that IgSeek is highly efficient in structural
retrieval and outperforms state-of-the-art approaches in sequence recovery for both antibodies and T-Cell Receptors.

### Strengths
* This paper has fast inference speed compared to existing inverse folding models like ESM-IF.

### Weaknesses
* The train/val/test split is based on time (year) and there can be identical or highly similar sequences in the training and test set. Therefore, there can be potential data leakage. Previous work like RefineGNN or DiffAb adopt sequence-similarity split to avoid this problem.
* Retrieving CDR sequences from known antibodies can lead to low novelty / non-specific binding of designed sequences. For example, if the task is to design CDRs that bind antigen A, IgSeek may retrieves a CDR from a known antibody that binds protein B. This CDR is unlikely to be a binder because it is designed specifically for protein B. And even if it does, it shows that this CDR is non-specific and this kind of non-specific binder is unfavorable. Therefore, casting protein design as a retrieval task has limitations.

### Questions
* Can you try construct a new train/val/test split based on CDR sequence similarity?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents **IgSeek**, a framework for sequence design of the complementarity-determining regions (CDRs) of antibodies. It addresses challenges in AI-driven protein design, particularly the issue of hallucinations in hyper-variable antibody regions. Instead of direct sequence generation, IgSeek uses a multi-channel equivariant graph neural network to obtain embeddings for CDR loops and retrieves similar structures from an antibody database to infer sequences. The authors claim that IgSeek outperforms existing methods in accuracy and efficiency for both antibody and T-cell receptor sequence recovery tasks although the experimental setup is flawed.

### Strengths
- The paper is well-written and easy to follow.
- IgSeek presents a structure-retrieval approach for antibody CDR loops, enabling sequence inference based on a given CDR loop backbone structure. This method is similar to FoldSeek [1], which was developed for efficient structure search in general proteins.
- The framework shows strong performance and fast inference compared to state-of-the-art protein and antibody models. However, the experimental setup is flawed.

**References:** \
[1] Michel Van Kempen, Stephanie S Kim, Charlotte Tumescheit, Milot Mirdita, Jeongjae Lee, Cameron LM Gilchrist, Johannes Soding, and Martin Steinegger. Fast and accurate protein structure search with foldseek. Nature biotechnology, 42(2):243–246, 2024. doi: https://doi.org/10.1038/s41587-023-01773-0.

### Weaknesses
- The method lacks novelty, as the clustering of canonical CDR loops has been previously established ([1]) and used for antibody sequence design in frameworks such as Rosetta ([2]).

- The comparison with FoldSeek in Figure-2 is problematic; FoldSeek is designed for conserved regions of general proteins and is not suited for flexible loops such as antibody CDRs. Despite that, it’s surprising to me that FoldSeek outperformed IgSeek in CDR-H3. 

- In Figure-3, the comparisons with Antifold and AbMPNN for amino acid recovery tasks are unfair, as these models are not specifically trained for CDR loops alone. As acknowledged by the authors, this biases the results in favour of IgSeek, potentially exaggerating its performance.

- Figure-3 indicates that sorting by RMSD is more effective than using embeddings from IgSeek. Showing results based solely on RMSD (Kabsch) would provide a clearer performance baseline.

- Figure-4 omits the inference time of the IgSeek+Kabsch method, although the authors use this method to argue that their approach outperforms others in Figure-3a/b. The added time from Kabsch alignment likely impacts overall inference speed, and a consistent comparison across methods is important.

- In the CDR sequence recovery tasks, the authors sample two sequences per query and select the one that best aligns with the ground truth, which is biased. In practical applications, such as library design for real experiments, the ground truth is unknown.

- IgSeek’s effectiveness heavily relies on the quality and diversity of the antibody structure database, which may restrict its applicability. This dependency also limits its ability to generate novel, diverse sequences, reducing its utility for de novo design.

- The paper does not specify how CDR regions are defined  (what numbering scheme is used?)

- Generated sequences for a given CDR loop are constrained to a fixed length, limiting flexibility for generating variable-length sequences, although similar limitations apply to existing methods.


**References:** \
[1] North B, Lehmann A, Dunbrack RL Jr. (2011). A new clustering of antibody CDR loop conformations. J Mol Biol 406: 228–256. pmid:21035459 \
[2] Jared Adolf-Bryfogle, Qifang Xu, Benjamin North, Andreas Lehmann, and Roland L Dunbrack Jr. Pyigclassify: a database of antibody cdr structural classifications. Nucleic acids research, 43(D1): D432–D438, 2015. doi: https://doi.org/10.1093/nar/gku1106.

### Questions
No questions.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents IgSeek, a novel structure-retrieval framework for antibody design. The framework leverages neural retrieval in an antibody database to retrieve structurally similar sequence templates of Complementarity-Determining Regions (CDRs) and ensembles these templates for sequence prediction. The paper demonstrates the effectiveness of IgSeek in predicting CDR sequences, particularly for relatively conserved residues, and shows its superiority in terms of speed and accuracy compared to existing baseline models.

### Strengths
1. IgSeek introduces a novel structure-retrieval framework for antibody design, which leverages neural retrieval and ensembling techniques.
2. The experimental setup is rigorous, and the results are thoroughly analyzed and visualized.

### Weaknesses
1. What is definition of the "hallucinations" problem in antibody design? How this problem generated?
2.  The authors said that the "IgSeek leverages neural retrieval in an antibody database to retrieve structurally similar sequence templates of CDR". I guess the performance is dependent on the accuracy of the antibody structures, How to get accurate antibody structures, how to ensure that the antibody database is large, and what if no structurally similar samples can be retrieved for some antibodies?
3. Other than the structure retrieval, what are the differences of your GNN method with other similar GNN-based antibody design methods?
4.  Some notations should be specified,  what does the $x_{ij}$ mean in Eq.4, the K value in Line 99, why k is 10 as shown in Table 2, how to determine it?
5. IgSeek needs the CDR structures as input, this may limit the application of this method, how to design the antibodies when the CDR structures are not known?  The effectiveness of IgSeek is heavily dependent on the quality and diversity of the antibody database. How sensitive is IgSeek to variations in the antibody database, and what strategies can be employed to mitigate this sensitivity? 
6. it seems that there is no specific design for antibody, this method is very general, i.e., it is can be used in common protein design. Structure retrieval method can be used in other structure to sequence tasks.
7. Lack of comparison baselines in Figure 3, like MEAN (Kongetal.,2023b), dyMEAN(Kongetal., 2023a) and ADesigner (tan, 2023).


[1] Xiangzhe Kong,et al. End-to-end full-atom antibody design. In ICML, pp.17409–17429,2023a.
[2] Xiangzhe Kong,et al. Conditional antibody design as 3d equivariant graph translation. In ICLR,2023b.
[3] Tan, C., et al. Cross-gate mlp with protein complex invariant embedding is a one-shot antibody designer. In AAAI.

### Questions
1. Can IgSeek be adapted to design antibodies for specific targets or diseases? If so, what modifications would be required?
2. Why diffusion models can be used to design antibodies?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The design of synthetic antibodies is an important challenge in AI for computational biology. This paper notices the occurrence of hallucinations during sequence inference, where sequences may not fold into desired structures in real applications. To overcome this obstacle, IgSeek proposes to retrieve similar structures from a natural antibody database. Experiments demonstrate its high efficiency by achieving the state-of-the-art performance in sequence recovery. Despite the performance, there are several issues remained to be explained more clearly.

### Strengths
(1) The idea of searching and matching substructures from a given candidate database is novel and interesting. I believe sometimes, instead of completely de novo generation, retrieval-based algorithm is a promising direction and can be incorporated into de novo design. 

(2) The inference speed of IgSeek is outstanding, which may enable the large-scale antibody retrieval-based design.

### Weaknesses
(1) The multi-channel equivariant message passing (MEGNN) has already been introduced in MEAN [i]. What is the difference between this paper's MEGNN and MEAN's version? They look very similar, just extending the single-channel EGNN layer to process residues with several atom coordinates. 


[i] CONDITIONAL ANTIBODY DESIGN AS 3D EQUIVARIANT GRAPH TRANSLATION. ICLR 2023. 

(2) Some important baselines are missing, for instance, DiffAB, MEAN, dyMEAN, etc.  

(3) A key motivation for IgSeek is that prior DL methods such as ProteinMPNN and IF can trigger hallucinations, namely, inferred sequences fail to fold into expected structures. *Therefore, it can be biased if we only adopt the sequence recovery rate to evaluate the model performance.*   

However, in the experiments, the author still regarded AAR as the most crucial factors to assess the performance of different approaches. From my point of view, they should compare the designed CDR structures (via some antibody-antigen folding prediction models such as Ab-Fold, AF3, etc.) with the ground truth structures. Besides, it is also necessary to evaluate the binding affinity or energy change between designed CDR and the original one, which can be difficult and can be implemented using some simulation tools such as Rosetta. My major concern is that you can not take the retrieved CDR struture for granted as the real one for designed CDR. Even if with the same sequences, these substructures can be significantly different in different antibody contexts. However, if the author have literactures or theories to support their point, I would be happy to discuss further.

### Questions
(1) Unlike previous co-design methods, IgSeek only focus on the CDR, ignoring the other parts of the antibody and even antigens. The current task in this paper is more like a toy task, without considering all essential contexts and ultimate goals: given an antigen, we hope to design an optimal antibody that binds well with it. So from both sides of model design and evaluation, we should all take this factor into account. Can the author explain why they only care about CDR and believe a successful CDR match is adequate for antibody design? 


(2) The experimental results are heavily dependent on your split and curation of the dataset. In other words, if there are no similar CDRs in your CDR candidate databse, you can never find or retrieve a suitable CDR for test samples. Unfortunately, the author failed to explore this severe drawbacks and proposed any potential solutions.

### Soundness
2

### Presentation
3

### Contribution
2
