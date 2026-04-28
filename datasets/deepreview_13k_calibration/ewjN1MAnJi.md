# PDDFormer: Pairwise Distance Distribution Graph Transformer for Crystal Material Property Prediction

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 6, 3, 6

## Abstract
The crystal structure can be simplified as a periodic point set repeating across the entire three-dimensional space along an underlying lattice. 
Traditionally, methods for representing crystals rely on descriptors like lattice parameters, symmetry, and space groups to characterize the structure. 
However, in reality, atoms in material always vibrate above absolute zero, causing continuous fluctuations in their positions. 
This dynamic behavior disrupts the underlying periodicity of the lattice, making crystal graphs based on static lattice parameters and conventional descriptors discontinuous under even slight perturbations. 
To this end, chemists proposed the Pairwise Distance Distribution (PDD) method, which has been used to distinguish all periodic structures in the world's largest real materials collection, the Cambridge Structural Database. 
However, achieving the completeness of PDD requires defining a large number of neighboring atoms, resulting in high computational costs. 
Moreover, it does not account for atomic information, making it challenging to directly apply PDD to crystal material property prediction tasks.
To address these challenges, we propose the atom-Weighted Pairwise Distance Distribution (WPDD) and Unit cell Pairwise Distance Distribution (UPDD) for the first time, incorporating them into the construction of multi-edge crystal graphs. 
Based on this, we further developed WPDDFormer and UPDDFormer, graph transformer architecture constructed using WPDD and UPDD crystal graphs. We demonstrate that this method maintains the continuity and completeness of crystal graphs even under slight perturbations in atomic positions. 
Moreover, by modeling PDD as global information and integrating it into matrix-based message passing, we significantly reduced computational costs. 
Comprehensive evaluation results show that WPDDFormer achieves state-of-the-art predictive accuracy across tasks on benchmark datasets such as the Materials Project and JARVIS-DFT.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces PDDFormer using the Pairwise Distance Distribution (PDD) as an invariant representation for crystal property prediction and enhances it with atom-specific weights (WPDD) and intra-unit cell structures (UPDD) to better capture atomic interactions and maintain computational efficiency. Experiments on datasets (Materials Project & JARVIS) show that WPDDFormer outperforms existing methods in predictive accuracy and computational efficiency.

### Strengths
1. The WPDDFormer model consistently outperforms other state-of-the-art methods across multiple tasks on the JARVIS and Materials Project datasets, demonstrating its effectiveness.
2. The authors provide theoretical guarantees on the continuity and completeness of the WPDD-based graphs, ensuring robust performance under minor structural perturbations.

### Weaknesses
I have no major concerns with this paper; however, an ablation study on the effect of varying the radius on WPDDFormer’s performance and efficiency would provide valuable insights into its scalability. Additionally, a time comparison between WPDDFormer and UPDDFormer would strengthen the evidence supporting UPDDFormer’s efficiency claims. The message-passing mechanism and implementation code appears to greatly overlap with ComFormer. If the message-passing approach is highly similar, the authors should focus on highlighting the key differences and consider moving the overlapping content to the background section or appendix, rather than emphasizing it in the main methodology section. A proper citation and discussion of Zeoformer (referred to as UPDD in the paper) are still necessary, as this work predates the ICLR submission. While I acknowledge the ICLR policy on concurrent submissions, the method name (UPDD) and the exact methodology are identical to those in Zeoformer, making it difficult to consider it as a contemporary work. Furthermore, Zeoformer appears to be a distinct work from this paper. If this paper is based on Zeoformer and was developed in such a short time frame, it raises concerns about the robustness of the theoretical proofs presented. Although I am not an expert on completeness proofs, I strongly encourage the authors to address the concerns raised by other reviewers on this matter.

### Questions
See weaknesses.

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
This work proposes PDDFormer, a novel framework for crystal material property prediction. The proposed PDDFormer uses insights about pairwise distance distribution impacts on crystal properties from material science community, designs a novel way to integrate pairwise distance distance distribution into crystal graph representations and a novel transformer model. PDDFormer is shown to achieve state-of-the-art performance on various crystal material property prediction benchmarks.

### Strengths
Originality:  
This work makes very significant novelty contributions in combining pairwise distance distribution with machine learning based crystal property prediction.

Quality:  
The quality of this work is evidenced by good theoretic analysis and strong experiment results.

Clarity:  
The writing of this work is overall good and clear.

Significance:  
The idea of efficiently integrating pairwise distance distribution into transformer model proposed by this work is insightful and enlightning for researchers in borad AI for science community.

### Weaknesses
(1) A remarkable motivation of this work is described in Abstract "However, in reality, atoms in material always vibrate above absolute zero, causing continuous fluctuations in their positions" (line 15-17). But it seems there is no clear discussion why the use of pairwise distance distribution resolves this atom position fluctuation issue? Authors are encouraged to give detailed clarification or discussions to this question. The connection between atomic vibrations and the proposed PDD method is not explicitly established. It's unclear how the distribution of pairwise distances inherently addresses the dynamic nature of atomic positions due to thermal vibrations. A more detailed explanation of the underlying physical principles is needed to justify this claim. Specifically, how does representing interatomic distances as a distribution, rather than a single value, account for the continuous fluctuations of atomic positions? Does the distribution capture the range of motion or the probability of finding atoms at different distances due to vibrations? These aspects require further elaboration.

(2) Generally, two novelty contributions are proposed in this work, including the use of pairwise distance distribution in graph features and a novel transformer architecture. It would make this work more solid if authors could conduct more ablation studies to study which novelty contributes better to good performance, such as applying pairwise distance distribution to other model architecture or removing it from the proposed PDDFormer model. The current evaluation does not sufficiently isolate the impact of each contribution. It is crucial to understand whether the performance gains are primarily due to the novel PDD integration or the new transformer architecture, or a combination of both. Ablation studies should include applying the PDD feature to existing crystal graph models and removing the PDD feature from the proposed PDDFormer model. Such experiments would provide a more granular understanding of the contribution of each component. Furthermore, it would be beneficial to explore different methods of integrating PDD into the graph representation and compare their performance.

### Questions
See Weaknesses part.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces PDDFormer, a model designed to construct geometrically complete and invariant representations of crystals for the task of crystal property prediction. However, the completeness claim of the proposed representation is problematic, as it relies on the assumption that "the PDD is a generally complete invariant" (citing Widdowson & Kurlin, 2022), asserting that distinct crystal structures yield distinct PDD representations. This claim is not accurate. The PDD matrix does not ensure completeness for unstable crystal structures and fails to distinguish between chiral crystal structures. Furthermore, the proposed UPDD crystal graph construction method was previously introduced in "Zeoformer: Coarse-Grained Periodic Graph Transformer for OSDA-Zeolite Affinity Prediction," and the message-passing layers draw inspiration from ComFormer. Given these issues, the paper has limited technical contributions and several potentially misleading claims.

### Strengths
1. The proposed crystal representation demonstrates continuity under small distortions and perturbations, which can be advantageous for robustness.

### Weaknesses
1. Incomplete and Potentially Misleading Claims about Completeness

The completeness proof in the paper relies on the assumption that the PDD matrix acts as a generally complete invariant for distinguishing different crystal structures. However, this is inaccurate. The PDD matrix, by its design, only considers geometric arrangements of atoms and disregards the specific atomic types. This means that it cannot distinguish between two crystal structures that have identical atomic positions but different chemical compositions. Furthermore, the PDD matrix is not guaranteed to distinguish unstable crystal structures, which may have subtle differences in atomic positions that are not captured by a fixed set of k-values, and it also cannot differentiate between chiral crystal structures, indicating fundamental limitations in the claimed theoretical foundation. Action suggested: reorganize the proof writing section or reorganize the completeness claims.

2. Limited Novelty in Crystal Graph Construction

The proposed UPDD crystal graph construction method is not novel and has been previously introduced in the work "Zeoformer: Coarse-Grained Periodic Graph Transformer for OSDA-Zeolite Affinity Prediction." This overlap with prior work limits the novelty and originality of the proposed approach. The authors have not sufficiently addressed the similarities and differences between their approach and Zeoformer, particularly regarding the use of unit cell parameters and the construction of multi-edge graphs. Action suggested: check this previous work and discuss similarity and difference with it.

3. Message Passing Layers Largely Derived from ComFormer

The architecture of the message passing layers appears to be directly inspired by ComFormer, with only minor modifications. The paper does not clearly articulate any novel aspects or improvements in their approach compared to ComFormer. The use of a node-wise transformer module, while effective, is not a significant contribution if it is largely a direct adaptation of existing work. The authors need to highlight specific innovations or modifications that go beyond a simple re-implementation of ComFormer's architecture. Could you highlight any novel aspects or improvements in your approach compared to ComFormer?

### Questions
As listed above in weaknesses.

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
3

### Summary
This paper presents atom-Weighted Pairwise Distance Distribution (WPDD) and Unit cell Pairwise Distance Distribution (UPDD) to characterize periodic crystal structure while accounting for atomic information. The continuity and geometrical completeness of these PDDs are theoretically evaluated. It then incorporates them into crystal graphs and develops graph transformer architectures for crystal property prediction. Comparative experiments show their better accuracy and efficiency over previous ML models, and ablation studies validate the importance of (W/U)PDD.

### Strengths
- The proposed (W/U)PDDs incorporate atomic information into PDD and address its high computational cost.
- The paper is overall well-written with nice flow, clarity, and illustrations.

### Weaknesses
 - The experimentation focuses on relatively simple scalar properties, some of which do not physically depend on crystal periodicity.
- Incorporating PDD into crystal graphs makes the data physics-informed, however, the proposed model does not seem to consider interpretability.
- Minor issues
  - In Definition 1, I suggest using boldface or other methods to help distinguish scalar, vector, and matrix.
  - Some languages in Definitions are vague: (1) Line 133, the range of what “crystal graph” refers to in this context should be specified. (2) Line 137, the description of geometrical completeness is unclear.
  - Typos, e.g., Line 129 “and If” and Line 512, “However”.

### Questions
- UPDD has multiple drawbacks compared to WPDD and shows inferior performance in experiments. What’s its advantage and when is it preferred over WPDD?
- The source of improvement by incorporating PDD is unclear. Is there a way to investigate whether it is because of accounting for periodicity, or because of input being more informative in other ways?
- Would the authors consider evaluating the interpretability of (W/U)PDD crystal graphs and/or the proposed transformer models?

### Soundness
3

### Presentation
4

### Contribution
3
