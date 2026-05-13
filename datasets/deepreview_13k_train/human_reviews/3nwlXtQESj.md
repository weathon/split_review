# Path Complex Message Passing for Molecular Property Prediction

- Decision: Reject
- Scores: 3, 6, 5, 5

## Abstract
Geometric deep learning (GDL) has demonstrated enormous power in molecular data analysis. However, GDL faces challenges in achieving high efficiency and expressivity in molecular representations when high-order terms of the atomic force fields are not sufficiently learned. In this work, we introduce message passing on path complexes, called the Path Complex Message Passing, for molecular prediction. Path complexes represent the geometry of paths and can model the chemical and non-chemical interactions of atoms in a molecule across various dimensions. Our model defines messages on path complexes and employs neural message passing to learn simplex features, enabling feature communication within and between different dimensions. Since messages on high-order and low-order path complexes reflect different aspects of molecular energy, they are updated sequentially according to their order. The higher the order of the path complex, the richer the information it contains, and the higher its priority during inference. It can thus characterize various types of molecular interactions specified in molecular dynamics (MD) force fields. Our model has been extensively validated on benchmark datasets and achieves state-of-the-art results.
The code is available at \url{https://anonymous.4open.science/r/Path-Complex-Neural-Network-32D6}

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper introduces Path Complex-based Message Passing (PCMP) and achieves promising results on molecular property prediction benchmarks. However, there are some major weakness in this paper including **lack of literature review, novelty and evaluation on current benchmarks**, and need to be further revised.

### Strengths
It proposes path complex-based message passing (PCMP) with some detailed graph theories, and achieves good results on some molecular tasks.

### Weaknesses
 - Incorporate geometric features like bond, angles, dihedrals and improper angles in the modeling is not novel, as seen in Fig.2 of [1] and Fig.2 of [2]. There are also many works already involved these many-body systems.
- Although the paper introduces the concept of a “path complex,” the actual features used, which are bond distances and angles (Table 5), are standard. Similar methods already exist, such as hierarchical message passing for updating geometric embeddings in [2]. Also, models like NequIP, Allegro, and MACE employ **many-body expansions** in message passing, leveraging **tensor products** to incorporate higher-order geometric tensors (a path fusing process [3]), which are beyond the basic features mentioned in this paper. PCMP maybe a subset of the tensor products. A more comprehensive literature review is needed for the authors [4, 5].
- The primary weakness is that the authors claim that they are inspired by MD force fields, but **no results on any standard MD benchmark, such as MD17, rMD17, MD22 are provided**. Not to mention the conduction of MD simulations further driven by this MLFF. Since the paper focuses on molecular 3D structures, **it’s a necessity to proof invariance or equivariance**, which are missing here. In contrast, this paper provides a list of the graph path theories, appears more relevant to topological graphs and is insufficient to address geometric graphs. Furthermore, despite claiming that the method “enables systematic exploration of connectivity and interaction for analyzing complex systems and networks,” **there are no experiments on these tasks supporting this claim**.
- The GEM paper is relatively old and actually we do not need to generate 3D structures using RDKit from smiles for the 2D molecule datasets. Beside the datasets mentioned in the above question, **numerous 3D molecular datasets for DFT-level property prediction, such as QM9 (with 12 targets), OC20, OE62, and PCQM4Mv2, are available**. I strongly recommend evaluating PCMP on these benchmarks for a more comprehensive assessment.

### Questions
- missing ']' in Fig. 1 dihedral term.
- If the paper aims to emphasize the Path Weisfeiler-Lehman (PWL) capacity, it should evaluate the capacities of classical models, such as DimeNet, GemNet, and MACE. For reference, see the Geometric Weisfeiler-Lehman (WL) paper.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper introduces a novel approach called Path Complex Message Passing (PCMP) for molecular property prediction using geometric deep learning. Unlike traditional graph neural networks (GNNs) that operate on molecular graphs, PCMP employs path complexes that capture multi-body interactions in molecules through paths of various orders. The model’s hierarchical message-passing mechanism updates high-order paths first, followed by lower-order paths, facilitating effective feature communication between these paths. Extensive experiments on benchmark datasets demonstrate that PCMP achieves state-of-the-art results in molecular property prediction, showcasing its potential to model complex molecular interactions comprehensively.

### Strengths
* Originality: The PCMP model presents a unique innovation in molecular property prediction by applying path complexes, which go beyond conventional graph-based representations. The incorporation of multi-order path complexes allows for capturing high-order interactions like bond angles and dihedral angles. This approach offers a fresh perspective on molecular graph representation, making PCMP stand out from other GNN-based models that primarily rely on node and edge interactions.
* Quality: The paper provides a thorough experimental validation, comparing PCMP with a diverse set of baseline models, including both pretrained and non-pretrained GNNs.

### Weaknesses
 * Clarity: I suggest the authors to hide some of the technical details in the Appendix.
* Experimental Limitations: Although the experiments are extensive, the paper could benefit from a more diverse set of benchmarks. The current datasets focus primarily on small to medium-sized molecules, while macromolecular structures, such as proteins, are absent from the evaluation. In addition, the test of efficiency, i.e. speed of training or inferences, is missing.

### Questions
Overall, I believe the authors present a good tool to predict molecular properties. However, the following questions should be addressed to clarify key aspects and improve rigor:

1. How do you compare the accuracy of your model with the more recent models, M3GNet, MACE, or EquiformerV2?

    - In addition, you only compared the accuracy, how about the speed compared with other models?

2. Is it possible to expand this framework to periodic systems, i.e. inorganic materials?

3. **Interpretability of Path Features**: Could the authors explore or comment on how path features across different orders contribute to the final prediction? Are there plans to visualize or interpret specific paths in relation to molecular properties?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper presents **Path Complex Message Passing (PCMP)**, which introduces path complexes to model intricate chemical and non-chemical interactions for molecular property prediction. The model demonstrates promising results on molecular benchmark datasets and aims to provide a more detailed molecular representation by incorporating high-order interactions in a path complex framework.

### Strengths
1. **Innovative Modeling of Molecular Interactions**: PCMP introduces path complexes, offering an approach to capture both local and global molecular features that go beyond traditional graph representations.
2. **Methodological Rigor**: The hierarchical message-passing mechanism is well-detailed, showing how path complexes of different orders contribute to the molecular representation.
3. **Thorough Ablation Studies**: The authors provide in-depth ablation studies that highlight the importance of various path orders and message-passing mechanisms, strengthening the evaluation.

### Weaknesses
1. **Unsubstantiated Claim on Force Field Mimicking**: A major claim of the paper is that PCMP mimics the molecular mechanics (MM) force field, yet no benchmarks or empirical results using MM force field datasets (e.g., MD17, MD22) are provided to substantiate this claim. Without benchmarking against MM force fields, the claim appears unsupported, and this oversight detracts from the paper's validity in this area.
  
2. **Computational Complexity**: The inclusion of path complexes, especially higher-order ones, is likely computationally demanding. However, the authors do not provide insights into potential trade-offs, such as runtime or scalability on larger datasets.

3. **Lack of Equivariance in Model Design**: Given the model’s target application in molecular property prediction, its architecture does not incorporate rotational or translational equivariance, which would enhance its ability to handle spatial molecular data more robustly. Adding equivariant layers could make the model better suited to capturing geometry-sensitive properties.

4. **Interpretability**: The model’s complex hierarchical structure might hinder interpretability, as it’s not clear which paths contribute most significantly to predictions or whether high-order interactions have consistent relevance across datasets. A comprehensive interpretability study is recommended.

### Questions
1. Can the authors provide empirical validation on MM force field datasets to substantiate their claim of mimicking MM force fields?
2. Are there specific path orders or features that consistently contribute more to accurate predictions? Could this be visualized or quantified?
3.  Can the model be used to capture the improper angle? Is it possible to implement this? 
4.  For Figure 4, does the path complex graph alleviate the over-squashing? If so, can the author provide an empirical study on this, for example, compare the effective resistance.
5.  So the current experiments contain only validation from small molecules dataset, what about for large molecules? How does the model scale to larger molecules?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces Path Complex Message Passing (PCMP), a method for molecular property prediction that represents molecules using path complexes of different orders to capture various aspects of molecular structure (bond lengths, angles, and dihedral angles). The work is heavily theoretical. The method is tested on five subsets of MoleculeNet, showing improvements over baseline models. Most of the papers content is theoretical development and proofs, with a relatively brief experimental section.

### Strengths
The paper displays technical rigor in developing its mathematical foundations, establishing formal proofs for path complex properties and their relationship to molecular structures. The proposed path complex representation is well motivated from a chemistry perspective, making explicit connections to molecular force fields and showing how different path orders correspond to physical properties (bond lengths, angles, and dihedral angles). The architecture is novel. While limited, the experimental results do show consistent improvements across multiple benchmark datasets, and the ablation studies help in distilling the contribution of different components of the model.

### Weaknesses
The paper suffers from several weaknesses. In the Introduction, the authors refer to quite 'old' papers. The experimental validation is notably thin compared to the extensive theoretical development, taking up only about 2 pages of the 10-page paper. The empirical improvements, while consistent, are relatively modest and don't seem to justify the substantial complexity introduced by the method. There's inadequate discussion of computational overhead and scalability. The path complex representation likely introduces significant computational costs, but this isn't analyzed. Even though datasets are described in the appendix, authors haven't included any brief description of the dataset, or the task at hand: for example, for QM9, one cannot know against which property the authors are regressing against from the main paper.

### Questions
1) What is the time and memory complexity of constructing and operating on path complexes compared to traditional graph-based methods?  How does the method scale with molecule size?

2) Related to above. Could you provide empirical justification for using 3-path complexes as the maximum order? What happens with higher orders?

3) Could you provide a brief description of each dataset's characteristics in the main paper?

### Soundness
2

### Presentation
2

### Contribution
2
