# FARM: Functional Group-Aware Representations for Small Molecules

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 5, 5, 3

## Abstract
We introduce \textbf{F}unctional Group-\textbf{A}ware \textbf{R}epresentations for Small \textbf{M}olecules (FARM), a novel foundation model designed to bridge the gap between SMILES, natural language, and molecular graphs. The key innovation of FARM lies in its functional group-aware tokenization, which directly incorporates functional group information into the representations. This strategic reduction in tokenization granularity is intentionally aligned with key drivers of functional properties (i.e., functional groups), enhancing the model's understanding of chemical language. By expanding the chemical lexicon, FARM more effectively bridges SMILES and natural language, ultimately advancing the model’s capacity to predict molecular properties. FARM also represents molecules from two perspectives: by using masked language modeling to capture atom-level features and by employing graph neural networks to encode the whole molecule topology. By leveraging contrastive learning, FARM aligns these two views of representations into a unified molecular embedding. We rigorously evaluate FARM on the MoleculeNet dataset, where it achieves state-of-the-art performance on 10 out of 12 tasks. These results highlight FARM’s potential to improve molecular representation learning, with promising applications in drug discovery and pharmaceutical research.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The manuscript introduces FARM (Functional Group-Aware Representations for Small Molecules), which seeks to enhance molecular representation learning by integrating functional group (FG) information into SMILES and graph-based representations. The core innovation lies in FG-aware tokenization and the use of contrastive learning to align these sequence- and graph-based molecular representations. The paper reports that FARM outperforms existing models on the MoleculeNet dataset across 10 of 12 tasks, showcasing potential in drug discovery and cheminformatics.

### Strengths
- The model's performance on diverse tasks from the MoleculeNet benchmark and comparisons with state-of-the-art methods provide robust evidence for its efficacy.
- The paper does an excellent job explaining the FG detection, tokenization process, and integration of representations through contrastive learning. The use of a functional group knowledge graph adds depth to the model's structure-learning capabilities.
- The tables show clear improvements over existing models in both classification and regression tasks, indicating that the incorporation of functional group information yields substantial benefits.

### Weaknesses
 - The increase in tokenization granularity from 93 to 14,741 tokens could be seen as excessive, leading to training inefficiencies. While the authors acknowledge this, a deeper discussion on the trade-offs and potential mitigation strategies (e.g., pre-training optimizations) would enhance the paper.
- The absence of 3D information limits the model’s capacity to handle stereochemistry and spatial effects, which are crucial in many chemical tasks. The authors mention this as a future direction, but its exclusion remains a significant limitation.
- The paper briefly mentions augmentations for negative samples in contrastive learning, such as node deletion and swapping. A more detailed exploration of the impact of these strategies would provide clarity on their contribution to performance.
-  The paper does not sufficiently address the computational requirements of training FARM, given the added complexity from FG-aware tokenization and knowledge graph embeddings.
- The novelty is also a bit limited since similar methods based on functional groups have been well-explored in previous studies [1,2,3,4,5,6].

### Questions
I think the main issue is the experiment section is too short without any in-depth analysis and discussion. The authors should continue adding content and polishing this section.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
1

### Summary
### Summary of the Paper

This paper explores methods for enhancing small molecule representation by integrating functional group information. A rule-based approach is applied to identify significant functional groups within small molecule databases, and this information is subsequently incorporated into SMILES strings. The representation of functional groups is learned through knowledge graphs that capture relationships between functional groups and their properties. The final representation is achieved using contrastive learning, where the SMILES representation is aligned with the functional group-enhanced SMILES. The authors report that their approach yields significant improvements compared to other functional group-based methods on MoleculeNet benchmark datasets.

Overall, the paper is well-written and presents a novel approach. However, I have several concerns regarding the benchmarks used, inconsistencies in split reporting, and the generalization of rule-based methods for identifying functional groups, as well as the construction of knowledge graphs for functional group embeddings. Detailed comments for improving the paper are provided below.

### Strengths
The idea of incorporating inductive bias by using functional groups to enhance small molecule representation is intriguing. The experiments include comparisons with various existing baselines that also leverage functional groups, and the results appear promising—assuming that the splits and MoleculeNet dataset variants are consistent with those reported in prior work.

### Weaknesses
 **MAJOR Concern 1**

The use of splits in the MoleculeNet datasets is inconsistent with the original MoleculeNet recommendations. Specifically, random splits are recommended for regression tasks such as ESOL, Lipophilicity, and FreeSolv. In this paper, the authors do not consistently clarify the splits used; for example, scaffold splits are mentioned in the appendix, but captions for Tables 7 and 8 indicate random splits. The lack of clarity regarding the precise method used to generate these splits, specifically whether standard functions from MoleculeNet were employed, raises concerns about the validity of the reported results. For instance, the BBBP dataset, when using a scaffold split, typically yields results around 0.75, as reported in recent studies, which is significantly lower than the 0.93 reported in this paper. This discrepancy suggests a potential issue with the splitting methodology, which needs to be addressed. Furthermore, the GROVER results reported in this paper are also higher than those reported in other works, further highlighting the need for clarification on the splitting method.

A significant challenge with MoleculeNet is the absence of a leaderboard with predefined splits, leading researchers to create custom splits, and sometimes even modify the original datasets, as seen in modifications to ESOL and FreeSolv in cases like [this issue](https://github.com/IBM/molformer/issues/9). This issue may reflect the use of dataset variants such as those described in [this study](https://www.nature.com/articles/s42256-022-00580-7.epdf?sharing_token=p5m9Z0797IQeBDOiMGn71dRgN0jAjWel9jnR3ZoTv0MeIJPs9pbG9QLaEN_McFTR3KHv1tHh1FDNJB4ZuILdAmRtINVn6KqXrLkPhEiAZW5mM0dWWKSmPk82eibEUBx01sLTSHx6w903cDaUoXg9lAGzcHY_ifmakrBcIzUUDwI%3D).

The existence of multiple dataset versions and split schemes makes it difficult to accurately assess improvements toward state-of-the-art (SOTA) results, as subsequent studies often cite results without clarity on splits used. For instance, in *"SELF-BART: A Transformer-based Molecular Representation Model using SELFIES"* (NeurIPS 2024, AI4Mat, [link](https://arxiv.org/abs/2410.12348)), the reported MoleculeNet performance is challenging to compare with this paper due to inconsistent dataset versions and splits.

I recommend the authors:
1. Provide consistent results using the original splits recommended by MoleculeNet.
2. Conduct additional experiments on the TDC ADMET groups (https://tdcommons.ai/benchmark/admet_group/overview), which offer leaderboards and fingerprint-based baselines. TDC ADMET provides consistent splits, making future comparisons easier.



**MAJOR Concern 2**

In the paper, the authors propose methods for FG-aware tokenization and fragmentation. Functional groups are identified based on known conventional groups or potentially using domain knowledge to define new groups. However, the set of rules for identifying new functional groups appears limited, raising questions about their generalizability. How do these rules compare to frequent subgraph mining, a widely-used technique in graph mining, where common subgraphs are often predictive features for small molecules?


**MAJOR Concern 3**

The use of a functional group knowledge graph to learn functional group embeddings is innovative, but some relationship types might provide an unfair advantage over other methods. For example, including properties like water solubility or lipophilicity (logP) could yield better results on downstream tasks related to those specific properties. It would be beneficial to assess the impact of removing such information from the knowledge graph to determine if the observed improvements are primarily due to these additional properties, which are not considered in other methods. Regardless of whether this information is utilized at the molecular level or functional group level, its inclusion in the learning process could still lead to data leakage. I strongly recommend that the authors exclude this information from the learning process and re-evaluate the results to assess the potential impact of leakage.

### Questions
Please see the questions in the Weakness section of the review.

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
4

### Summary
This paper presents Functional Group Aware Representations for Small Molecules (FARM), pre-trained foundation model that incorporates functional group tokenization, fragmentation, and knowledge graph-based structural representation learning. Moreover, this work integrates the atom-feature and structural representation by contrastive learning, which results in achieving the SOTA results in MoleculeNet dataset.

### Strengths
- The figures are neat, and the clear writing enhances the comprehensibility of the paper, making it easy to follow.
- This paper highlights the importance of functional groups, which are often overlooked in many molecular foundation models, and effectively integrates these functional groups into the molecular foundation model.
- The analysis presented in the paper, including the knowledge graph embedding space, substitution of functional groups, and visualization of attention maps, enriches the understanding of the method’s contributions.

### Weaknesses
 - The approach is quite similar to existing motif-based tokenization and fragmentation methods. While the authors define functional groups in terms of functional groups and fused ring systems, these could typically be identified through standard fragmentation tasks. An ablation study comparing FARM with other fragmentation methods would clarify its advantages. If applied under the same training conditions, does FARM demonstrate superiority?
- This work heavily relies on fused ring systems, which constitute over 99% of the identified functional groups. This raises concerns, as ring systems are generally not classified as functional groups. The paper emphasizes functional groups as the main contribution, as suggested by the method’s name. If ring systems are excluded, does the method still show superior performance?
- The naming process for fused ring systems seems to overlook bond types, considering only ring indices and sizes. However, bond types, including single and aromatic bonds, are crucial for understanding the ring system. How are these bond types accounted for in the analysis?
- The limitations of related works that address functional groups are unclear. The authors state that previous works “do not extend to detecting more complex functional groups, such as ring systems.” However, RDKit can identify ring systems, and simple IUPAC transformations could be applied to adapt this information for earlier works.
- Which functional group detection algorithm is employed? The paper lacks a description of the algorithm that traverses the graph to identify functional groups, which is critical for the method. For instance, there should be clear priorities among functional groups to consistently identify intersected atoms across different functional groups.
- In functional graph generation, what happens if the graph cannot be represented as a linear graph? Specifically, the node perturbation process in augmentation may be unclear. For example, if a functional group graph forms a triangle (a-b-c), the node perturbation could result in the same functional group graph, potentially generating incorrect negative samples.
- In Figure 5, how do the removals of multiple functional groups and single functional groups yield parallel results? For instance, the orange molecule has three functional groups removed, while the green molecule has only one removed, yet both show similar results.
- In the knowledge graph construction, how are continuous values such as LogP discretized? The original continuous values may not correlate with other functional groups.
- Will this approach be effective for generation tasks? A simpler generation task compared to SMILESLSTM could strengthen the contribution.
- Why does Figure 5(b) depict the link prediction performance?

### Questions
- Which functional group detection algorithm is employed? The paper lacks a description of the algorithm that traverses the graph to identify functional groups, which is critical for the method. For instance, there should be clear priorities among functional groups to consistently identify intersected atoms across different functional groups.
- In functional graph generation, what happens if the graph cannot be represented as a linear graph? Specifically, the node perturbation process in augmentation may be unclear. For example, if a functional group graph forms a triangle (a-b-c), the node perturbation could result in the same functional group graph, potentially generating incorrect negative samples.
- In Figure 5, how do the removals of multiple functional groups and single functional groups yield parallel results? For instance, the orange molecule has three functional groups removed, while the green molecule has only one removed, yet both show similar results.
- In the knowledge graph construction, how are continuous values such as LogP discretized? The original continuous values may not correlate with other functional groups.
- Will this approach be effective for generation tasks? A simpler generation task compared to SMILESLSTM could strengthen the contribution.
- Why does Figure 5(b) depict the link prediction performance?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes FARM, a functional group-aware representations for small molecules. The authors suggest to learn molecular representations via contrastive learning based on SMILES and graph information of molecules. Firstly, a string-based model and a graph-based model learn molecular representations with MLM objective and KG-graph/link prediction objectives, respectively. Then, contrastive objective is applied between two models.

### Strengths
- The problem of interest, molecular property prediction, is important for real-world applications, e.g., drug discovery.

- Utilizing functional groups is chemically reasonable, since molecular properties are highly related to functional groups.

### Weaknesses
 - Lack of novelty.

Using functional groups in molecular representation learning has already been investigated by many works. Also each component of the framework, e.g., MLM, link prediction, and contrastive loss, has also been widely investigated. I could not find new (or novel) components in the overall framework.

---
- Imprecise motivation on contrasive learning.

The motivation of this work is vague. SMILES and graph of molecules contain the same information of molecule, i.e., a molecule can be reconstructed from both SMILES and graph. Why should we deal with them both instead of focusing on a single representation (SMILES or graph)? Since this paper strongly insist that they learn "chemically plausible" representation, this choice should be "chemically" justified (I know that the language model and the graph model may learn different features of molecules, but it is not a "chemical" motivation).

---
- Misclaim "L71: Our approach overcomes these limitation ..."

The proposed approach cannot overcome "3D coordinates" (L66) and "long-range dependencies" (L68). This method does not deal with 3D coordinates nor long-range dependencies.

---
- Complexity of method.

This work combines several objectives, e.g., link prediction, contrastive and MLM loss. However, the impact of each component is not thoroughly investigated. Furthermore, such complex objective introduces several hyper parameters and makes the training unstable.

### Questions
1. Why ToxCast is excluded in MoleculeNet experiments?

2. In my previous experiences, 3 seeds in MoleculeNet experiments are not enough due to very high variance. I suggest to report the results based on (at least) 10 seeds.

3. The authors train two models (language and graph). Which model is used in the fine-tuning phase?

### Soundness
1

### Presentation
2

### Contribution
1
