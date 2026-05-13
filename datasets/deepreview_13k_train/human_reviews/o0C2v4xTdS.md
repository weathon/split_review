# CoarsenConf: Equivariant Coarsening with Aggregated Attention for Molecular Conformer Generation

- Decision: Reject
- Scores: 8, 5, 6, 5

## Abstract
\normalsize
\noindent Molecular conformer generation (MCG) is an important task in cheminformatics and drug discovery. 
The ability to efficiently generate low-energy 3D structures can avoid expensive quantum mechanical simulations, leading to accelerated virtual screenings and enhanced structural exploration.
Several generative models have been developed for MCG, but many struggle to consistently produce high-quality conformers.
To address these issues, we introduce \modelns, which coarse-grains molecular graphs based on torsional angles and integrates them into an SE(3)-equivariant hierarchical variational autoencoder.
Through equivariant coarse-graining, we aggregate the fine-grained atomic coordinates of subgraphs connected via rotatable bonds, creating a variable-length coarse-grained latent representation.
Our model uses a novel aggregated attention mechanism to restore fine-grained coordinates from the coarse-grained latent representation, enabling efficient generation of accurate conformers.
Furthermore, we evaluate the chemical and biochemical quality of our generated conformers on multiple downstream applications, including property prediction and oracle-based protein docking.
Overall, \model generates more accurate conformer ensembles compared to prior generative models.            % and traditional cheminformatics methods.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies molecular conformer generation (MCG). The proposed method is a new SE(3)-equivariant hierarchical variational autoencoder that leverages coarse-grains molecular graphs with torsional angels. The proposed attention mechanism enables variable-length coarse-to-fine generation that restores high-quality conformers from coarse-grain graphs in an autoregressive way. This framework more efficiently generates more accurate conformer ensembles.

### Strengths
1. **Novelty.** As the authors claimed, this paper proposed a novel pipeline to generate conformers using a SE3-equivariant hierarchical VAE and aggregated attention.
2. **One stone three birds:** **efficiency, flexibilty and quality.** In contrary to prior works, the proposed method can generate all size of conformers by a single model whereas some existing approaches require a model for one length resulting in 100+ models to learn a dataset. This unified model learns more parameter-efficiently and more effectively with virtually more samples per model.
3. **Competitive performance.** Experimental results in Table 3 and 4 show that the proposed method achieve competitive performance on Protein Docking and Binding Affinity compared to two or three baselines.

### Weaknesses
1. Weak performance on GEOM-DRUGS compared to Torsional Diffusion. In addition, the performances of baselines are different from the literature. Also, Recall should be reported as well. Please explain what causes the discrepancy.
2. Only few baselines are provided. If more baselines are provided, then it will be better to evaluate the effectiveness of the proposed method compared to recent techniques.

### Questions
1. QM9 and ZINC250 have been used for learning molecular distributions. Also, several representations have been used for generation such as string (SMILES, SELFIES) and (2D) graphs. Is it possible to compare MCG with other graphs or string based methods? Often papers provide other groups of approaches in tables as references with dim fonts. 
2. Coarse-to-fine is a popular strategy in many applications. The conditional generation idea can be generalized in other directions. 2D to 3D generation is quite popular in the computer vision domain. Have you ever considered other coarse representations? and how robust/sensitive is the proposed pipeline to the quality of coarse-grain generation?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes CoarsenConf, a novel conditional hierarchical VAE for molecular conformer generation. In particular, CoarsenConf aggregates the fine-grained atomic coordinates of subgraphs connected via rotatable bonds to create a variable-length coarse-grained latent representation, and uses a novel aggregated attention mechanism to restore fine-grained coordinates from the coarse-grained latent representation.

### Strengths
1. The idea of this work is straightforward and novel.
2. The entire model can be trained end-to-end, and generate more accurate conformer ensembles compared to prior generative models. Besides, it shows very good performance on multiple downstream applications.

### Weaknesses
1. Authors say that they are the first model to employ variable-length coarse-graining. As far as I know, it has already been used in the molecular field (e.g., Qiang B, Song Y, Xu M, et al. Coarse-to-fine: a hierarchical diffusion model for molecule generation in 3D, ICML2023).
2. The model architecture needs further explanations. For example, the description of encoder architecture in your appendix is unclear. What are the inputs and outputs of the three modules? How to get outputs based on inputs? Please reorganize this section.
3. The presentation needs further improvement. This paper does not provide any algorithm for the proposed method, making me very confused about a lot of training and inference details.
4. As shown in Table 1, Table 5 and Table 6, the performance of this work seems to be suboptimal, especially for Recall.

### Questions
1. Compared with current ML methods, how efficient is this method?
2. Why is there a lack of comparison with Geodiff in many experiments? They have already released their code.

### Soundness
3 good

### Presentation
2 fair

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
This paper proposes a molecular conformer generation framework based on the coarse-graining of molecular graphs. Its main idea is to learn a coarse-grained latent representation based on an encoder with a "multi-resolution" message passing structure and autoregressive ly decode the conformer from coarse latent representations. Experiments demonstrate performance improvement over existing works such as torsional diffusion for applications like property prediction and oracle-based protein docking.

### Strengths
Overall, I think this work provides a solid and incremental contribution to molecular conformer generation.

- To my knowledge, this work is the first to apply coarse-graining for molecular conformed generation. 
- It is interesting to see that autoregressive decoding is still useful for molecular conformer generation (compared to existing diffusion-based techniques).
- The proposed idea can be extended to other tasks like generating molecules from scratch.
- The experiments seem solid enough to verify the usefulness of the proposed method.

### Weaknesses
Since the proposed architecture is a bit complex, it is hard to identify the main source of performance improvement in the architecture. For example, one might argue that most of the improvement comes from (a) using substructures with fixed 3D coordinates and (b) using an encoder with a pooling layer. However, (a) has been proposed by torsional diffusion paper, and (b) has been investigated by the GNN community. It would be nice if the authors could design an ablation study on the effectiveness of each architectural component. Specifically, it is unclear if the performance gains are primarily due to the multi-resolution message passing, the specific choice of coarse-graining, or the autoregressive decoding process. The use of substructures with fixed 3D coordinates, while potentially beneficial, also introduces a potential bias that needs to be carefully evaluated. Furthermore, the impact of the distance-based auxiliary loss on the overall performance should be investigated, as it is not clear if this loss is essential or if it is simply a regularization term. The interaction between the different geometric modalities (angles, coordinates, distances) and how they are optimized could also be better understood with more detailed ablation studies.

### Questions
I have the impression that this paper is in fact quite related to the torsional diffusion paper, e.g., both paper uses molecular substructures as fixed building blocks for molecular conformed generation. 

Could the authors elaborate more specifically on the difference and the benefits of using the coarse-graining procedure?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors proposed a coarse-grained method for molecule conformer generation, through an SE(3)-equivariant hierarchical VAE. The method is able to do coarse-graining generation with variable length via an aggregated attention strategy. The proposed method achieved state-of-the-art performance across a set of downstream tasks, including structural precision, property prediction, and docking binding affinity.

### Strengths
The performance is promising.

### Weaknesses
1. Problem Significance: The authors may need to demonstrate the problem of conformation generation remains significant, in the context of the rapid development of 3D molecule generation from scratch.
2. Novelty: There has been a line of work studying coarse-grained molecule generation in the community [1, 2]. The authors may need to further discuss the novelty of their methods in comparison to these existing methods.
3. Novelty Again: There has been another work proposing its information fusion attention that is similar to the aggregated attention strategy [3].

### Questions
N/A

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
