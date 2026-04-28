# UniMatch: Universal Matching from Atom to Task for Few-Shot Drug Discovery

- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 8, 8, 6

## Abstract
Drug discovery is crucial for identifying candidate drugs for various diseases. However, its low success rate often results in a scarcity of annotations, posing a few-shot learning problem. Existing methods primarily focus on single-scale features, overlooking the hierarchical molecular structures that determine different molecular properties. To address these issues, we introduce Universal Matching Networks (UniMatch), a dual matching framework that integrates explicit hierarchical molecular matching with implicit task-level matching via meta-
learning, bridging multi-level molecular representations and task-level generalization. Specifically, our approach explicitly captures structural features across multiple levels—atoms, substructures, and molecules—via hierarchical pooling and matching, facilitating precise molecular representation and comparison. Additionally, we employ a meta-learning strategy for implicit task-level matching, allowing the model to capture shared patterns across tasks and quickly adapt to new ones. This unified matching framework ensures effective molecular alignment while leveraging shared meta-knowledge for fast adaptation. Our experimental results demonstrate that UniMatch outperforms state-of-the-art methods on the MoleculeNet and FS-Mol benchmarks, achieving improvements of 2.87% in AUROC and 6.52% in ∆AUPRC. UniMatch also shows excellent generalization ability on the Meta-MolNet benchmark

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors propose UniMatch, a dual matching framework that integrates hierarchical molecular matching with meta-learning, significantly improves the performance and generalization in molecular property prediction tasks.

### Strengths
1.  UniMatch is the first method that integrates multiple levels of molecular structures, demonstrating outstanding performance across various tasks and sigificantly contributes to the filed of drug discovery.
2. This paper is clearly-written and accompanied supported by well-designed figures, well done!

### Weaknesses
1. I suggest further investigating the interpretability of the model, particularly with respect to the multi-level representations. Some gradient-based methods (e.g. DeepLIFT) could be used to reveal the importance of these features.

### Questions
1. Do AUCPR and AUPRC refer to the same metric? If so, I sugget using a consistent abbreviation throughout the paper.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents UniMatch, a framework designed to address data scarcity in few-shot drug discovery. It uses a dual matching approach: explicit hierarchical molecular matching, which captures information from the atomic level to full molecular structures, and implicit task-level matching via meta-learning to enable effective generalization across tasks.

### Strengths
1. The concept of modeling molecular structures across multiple levels is promising.
2. The manuscript is well-written and easy to read.
3. Extensive experiments across diverse datasets demonstrate that the model consistently outperforms baselines.

### Weaknesses
1. The related work section is somewhat lengthy. It might be more effective to move it to the end of the manuscript or condense it.
2. While the rationale for modeling hierarchical structures is solid, I have concerns about the use of mean pooling. This approach may lead to a predominantly molecule-level representation, potentially losing crucial atomic and substructural details. What do the authors think?

### Questions
see weaknesses

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This study introduces a new framework for molecular representation specially aimed at multi-task few-shot learning. In this context for each task there is a small support subset of molecules with known labels ($S_T$) and a query subset ($Q_T$) with unknown labels.

The contributions of the study can be broken down into the following components:

1. Matching at different levels of the molecular graph. This is achieved by an attention mechanism where the keys are the molecular features of the $S_T$, the molecular representations of $Q_T$ are used as query, and as value, the labels of the $S_T$. This matching attention mechanism is not novel. The novelty resides on repeating this matching with the representations at each layer of the GNN (thus effectively capturing information at different structural levels of any given molecule) and concatenating the resulting values that are then passed through an MLP to predict the final target value.
2. Meta-learning. An additional implicit matching mechanism is used to learn the similarity between different tasks and how to leverage the multi-scale representations from one task to another. This is achieved by an inner loop where the task-specific adaption parameters are updated using the matrix that captures the similarity between tasks and an outer loop where this similarity matrix is updated.

The results obtained in benchmark datasets clearly show that the benefits of this approach when compared to current state-of-the-art alternatives. The ablation study also clearly supports the contribution of all the components of the method.

### Strengths
1. The paper tackles a valuable domain-specific problem, which high societal value, with a method that can be reasonably adapted to different domains.
2. The evaluation is extensive and clearly demonstrates the advantages of the method.
3. The ablation study is complete and clearly demonstrates the contribution of every component in the method.

### Weaknesses
Major weaknesses
---
1. The technical description of the dual matching mechanism is hard to follow and it is a disservice to an otherwise solid work.


Minor weaknesses
---
_(These are minor points that do not have a direct bearing in my evaluation of the paper, but I think would improve its quality)_

1. In line 075-077 and Figure 1, one of the examples provided of the importance of the multi-level representation of molecules from atomic, to whole molecule serve their purpose as an illustration, but it is not chemically correct. Hydrogen ions do not exist within the molecule, they would be referred to as hydrogen atoms. Though it is true that Hydrogens ions in a solution determine its acidity. In a molecule, the hydrogen atoms are not the determinants of acidity, but rather the atoms they are attached to. So in the first examples, the acidity of those molecules is not determined by the Hydrogen atoms but by the chlorine and oxygen atoms; and their electronegativity (or ability to hold onto the Hydrogen). Still the illustration is accurate, but the atom that should be highlighted is not the Hydrogen. In the case of the right example, it is arguable that the acidity is not only caused by the oxygen, but rather the whole substructure of H-O-S.
2. In line 409, when describing the FS-Mol dataset, it is described as "[a benchmark] for macromolecules (i.e., proteins)". This is not accurate, the benchmark measures the ability of small molecules (the one that serve as input for this system) to bind to proteins. In other words, the tasks are whether the molecules can bind to specific proteins. This is an important distinction because due to their size, modelling proteins with the approach presented in this paper would be computationally infeasible.

### Questions
1. When evaluating against MoleculeNet tasks, is there a reason why the QM tasks were not considered and only the biophysical properties are included?
2. Do you have any ideas as to whether more explicitly introducing an inductive bias to the different levels of attention could be helpful?

### Soundness
4

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This work presents UniMatch for molecular property prediction in the few-shot learning scenario. It combines explicit hierarchical molecular matching with implicit task-level matching via meta-learning. The effectiveness of the few-shot learning and multi-task generalization is validated on the MoleculeNet, FS-Mol, and Meta-MolNet benchmarks. An ablation study and visualizations are provided to demonstrate the importance of hierarchical molecular matching and task-level matching.

### Strengths
1. The writing is clear, with well-crafted figures that enhance understanding. It also offers a discussion of limitations and detailed supplementary explanations.

2. The experiments are quite extensive. The research examines the universality of the method across different network structures. It also conducts evaluations on three benchmarks. The results are convincing.

### Weaknesses
1. **Timeliness**:
 - The baselines and related work employed in the paper lack more recent works, especially those of recent 1 or 2 years. 

- The pretraining model, Pre-GNN (Hu et al., 2020), is relatively old in the context of molecular pretraining. Recent years have seen the emergence of far more powerful models. I encourage authors to consider integrating more up-to-date pretraining models to showcase the significance and practical usage of their approach. 

By simple searching, I find more recent related works on Hierarchical molecular representation learning methods like "UniCorn: A Unified Contrastive Learning Approach for Multi-view Molecular Representation Learning" (ICML 2024) and "Adapting Differential Molecular Representation with Hierarchical Prompts for Multi-label Property Prediction" (Briefings in Bioinformatics, 2024).



2. **Novelty**:

The hierarchical molecular representation extraction concept is commonly seen in the literature. Additionally, the paper employs standard attention and meta-learning methods. I'm concerned that this may not meet the novelty standards of top conferences.

### Questions
1. **Generalization to different molecular structures**:
It would be beneficial to understand how well the method generalizes to diverse molecular structures, as this is crucial for practical applications. For example, testing under a scaffold split for support and query sets could provide insights. The paper mentions the method's failure on MUV. Is this due to a lack of structure generalization? The phrase "severe distribution imbalance" is not clearly explained. What does it refer to specifically? And why are other baselines able to overcome this issue?

2. In Figure 2, the query molecule appears identical to one in the support set. In your implementation, can the query molecule overlap with the support set? 

3. The numbers in parentheses following the datasets in Table 1, which appear to represent the number of tasks, do not seem to be explained in the main text.

### Soundness
2

### Presentation
3

### Contribution
3
