# RINGER: Conformer Ensemble Generation of Macrocyclic Peptides with Sequence-Conditioned Internal Coordinate Diffusion

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 5, 5, 8

## Abstract
Macrocyclic peptides are an emerging therapeutic modality, yet computational approaches for accurately sampling their diverse 3D ensembles remain challenging due to their conformational diversity and geometric constraints. Here, we introduce RINGER, a diffusion-based transformer model for conditional generation of macrocycle peptides based on redundant internal coordinates. RINGER provides fast backbone- and side-chain sampling while respecting key structural invariances of cyclic peptides. Through extensive benchmarking and analysis against gold-standard conformer ensembles of cyclic peptides generated with metadynamics, we demonstrate how RINGER generates both high-quality and diverse geometries at a fraction of the computational cost. Our work lays the foundation for improved sampling of cyclic geometries and the development of geometric learning methods for peptides.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the conformer generation problem in molecular machine learning. Specifically, conformer generation for ring systems is challenging for previous approaches. This paper proposes a diffusion model over internal coordinates to generate macrocycle peptide conformers. Experimental results demonstrate the effectiveness of the proposed approaches over previous methods.

### Strengths
1. This paper does capture an important problem --- sampling the conformational ensembles for structures with diverse ring systems and previous effort in this direction is relatively limited.
2. This paper proposes to use a diffusion model over internal coordinates (angles and dihedrals) is technically sound and efficient to reduce the degree of freedom (e.g. distances).
3. The empirical performance of the proposed method is excellent compared to the baseline methods.

### Weaknesses
The technical contribution of this paper is limited (to the machine learning community), the way to build a diffusion model over angle and torsion space has been widely studied in the related literature. IMHO, the most interesting part of the paper is about how to capture ring system conformational changes with angles and dihedrals, however, it is discussed only very briefly in Sec 3.3. How do you determine the 3 torsional angles and 2 bond angles for a macrocycle (how many atoms are in the cycle? How about a two-ring system?) The post-processing optimization step seems an effective and efficient solution to reconstruct the cartesian coordinates for the macrocycles, but how do you assemble them back into the structure (assuming you are only optimizing for the rings)?

Overall, I think this is an interesting application paper to establish diffusion models to sample conformational changes for molecular structures, especially ring systems. Given it's an application paper, I would expect more discussions from the problem formulation side and why it should be designed in this way with more case studies to demonstrate, e.g. it could handle multiple ring systems. The critical part missing is how to extract the angles and dihedrals from the ring.

### Questions
See weaknesses.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors present their method to generate ensembles of macrocycle conformer rings. Specifically, their model takes a 2D structure for a macrocycle peptide and generates 3D coordinates in the form of bond angle and torsional distributions. 

They test their model with and without side chains in both conditional and unconditional generation. Their method uses diffusion to generate its values and ultimately serves a purpose similar to alphafold; in that it predicts spatial characteristics of the structure from the composition of bonds and atoms in the base structure. 

In figure 2, the authors demonstrate that their method can estimate characteristics measured from test samples. In table 1, they show that their method is better able to estimate these values compared to existing methods.

### Strengths
The authors present a novel use of diffusion to generate macrocycle peptides. They show that their method can outperform existing methods by a significant margin and is able to produce estimates quite similar to test samples.

### Weaknesses
The paper doesn’t focus on its implementation details as well as it could. Most of the necessary details are there, but it also isn’t clear that their method could be definitively replicated from the details given. A system diagram or some other flowchart outlining their method could help elevate the paper.

The paper initially gave me the impression that the full structure was being generated until this was cleared up by figure 1.

While this is not a reason to reject the paper, I believe the paper could flow better if it was immediately clear exactly what are the inputs and outputs to their method. Additionally, they should, either in the abstract or in the beginning of the methods section, state in plain language what challenges their method overcomes that previous methods were insufficient to achieve. The authors do state what their method is generating, but the language could be improved to make their motivations clearer.

### Questions
The paper left me with no outstanding questions beyond certain small details which are not strictly necessary for understanding their method.

### Soundness
3 good

### Presentation
2 fair

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
This paper introduces RINGER, a novel solution for generating conformations of macrocycle peptides. RINGER is a diffusion-based model with a Transformer as its core architecture. To maintain SE(3)-invariance, RINGER operates on torsion and bond angles, and the ultimate coordinates are generated through a post hoc optimization process. RINGER is capable of performing both backbone (unconditional) generation and macrocycle (conditional) generation, and extensive experiments validate its effectiveness.

### Strengths
1. This paper delves into a relatively underexplored research area-conformation generation for macrocycle peptides. The proposed method, RINGER, has demonstrated commendable results in terms of both quality and efficiency, achieving satisfying outcomes in a mere 20 steps.
2. The paper conducted a wide array of experiments, providing robust evidence to substantiate the effectiveness of RINGER.
3. This paper takes into account the cyclic symmetry inherent to macrocycles and devises a novel relative positional encoding method that effectively incorporates this unique property.

### Weaknesses
1. I do not think novelty is enough. RINGER shares similarities with FoldingDiff [1]. The differentiating factor lies in RINGER's introduction of a unique relative positional encoding, specifically designed to account for cyclic symmetry. It's important to note that there appears to be a lack of an ablation study on this proposed positional encoding, which could provide valuable insights. The core architecture, a diffusion-based Transformer, is not novel, and the use of torsion and bond angles to maintain SE(3)-invariance is also a common practice. The primary novelty seems to stem from the cyclic positional encoding, but without a thorough ablation study, it's difficult to assess its true contribution. Specifically, it is unclear how much performance gain is attributable to this encoding versus other design choices.
2. Additionally, from a machine learning perspective, one may question the inherent challenges of conformation generation for macrocyclic peptides. It might be worthwhile to explore whether adapting methods from other molecule types is a feasible approach, as machine learning methods may not be strongly influenced by molecular variations. The paper does not sufficiently justify why existing methods for small molecule conformation generation cannot be applied or adapted to macrocyclic peptides. A more detailed discussion of the specific challenges posed by macrocycles, such as their unique conformational space and cyclic constraints, is needed to justify the development of a specialized method.
3. In the context of unconditional generation tasks, a comparison with other existing methods would be highly valuable in order to assess RINGER's performance and capabilities more comprehensively. Additionally, in the comparison of conditional generation, where rRMSD and rTFD metrics are employed, it appears that there is a absence of a method focused on backbone generation. It is unclear why a comparison to existing backbone-focused methods was not included, especially since the paper emphasizes the importance of backbone conformation in macrocycle design. The lack of this comparison makes it difficult to assess the method's performance in this specific context.

### Questions
1. Why the baseline excludes Torsional Diffusion [2]? I can understand that ‘Methods such as torsional diffusion only alter freely rotatable bonds and cannot sample macrocycle backbones by design.’, but I think Torsional Diffusion can be compared ‘in the context of all-atom geometries (RMSD)’ in section 4.3 if I do not misunderstand.
2. Why GeoDiff-Macro performs so poor? Can you provide experiment details of GeoDiff-Macro?

[2] Jing B, Corso G, Chang J, et al. Torsional diffusion for molecular conformer generation. Advances in Neural Information Processing Systems, 2022, 35: 24240-24253.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses the challenge of generating macrocyclic peptides. The approach involves training a discrete-time diffusion model on the internal coordinates, which is implemented using a transformer equipped with its specific invariant cyclic positional encoding tailored for this generation task. During inference, the set of angles and torsions generated undergoes a refinement phase through constrained optimization.

The primary contribution of this work is the innovative architectural design tailored to tackle conformer generation for this particular class of molecules. Additionally, the paper provides comprehensive experimental evidence to establish the suitability of their approach for the problem.

### Strengths
Significance:
Macrocyclic peptides represent a crucial category in therapeutics, and enhancing the precision and efficiency of conformer generation can profoundly impact drug discovery. Thus, this paper addresses a highly significant problem in the field.

Originality:
The paper introduces two key technical innovations. First, it adapts the positional encoding of the transformer architecture to better suit cyclic peptides, showcasing the authors' domain-specific knowledge in their modeling approach. Second, the paper presents a straightforward yet effective ring-closing procedure based on constraint optimization. Both solutions highlight that the authors intelligently use their task-specific insights. Moreover, the paper goes beyond traditional metrics for conformer generation, introducing novel evaluation criteria better aligned with the task.

Clarity and Quality:
The text is well-crafted, effectively motivating the problem, and the literature review is well-structured and relevant to the context.

### Weaknesses
An ablation study is essential to elucidate the respective contributions of the positional encoder and the ring closing algorithm to the overall performance. Specifically, it's unclear how much performance gain is attributable to the novel cyclic positional encoding versus the constrained optimization procedure. Disentangling these effects is crucial for understanding the method's strengths and limitations. For example, the performance of the model with a standard positional encoding and the proposed ring closing algorithm should be compared to the full model. Furthermore, the impact of different optimization constraints on the final conformer quality should be explored.

The benchmarking falls short in including some of the most recent diffusion models for small molecule conformer generation. While the authors acknowledge their limitations, substantiating these claims with experimental evidence is crucial. It would be valuable to include models such as TorsionDiff and a non-diffusion model like GFlowNets for a more comprehensive evaluation. The absence of these comparisons makes it difficult to assess the relative performance of the proposed method against the current state-of-the-art. Moreover, the evaluation should include a more diverse set of macrocycles, including those with varying ring sizes and chemical functionalities, to ensure the generalizability of the results.

### Questions
- why macrocycles with fixed bond distances contain three redundant torsional angles and two redundant bond angles ?

- What is the information regarding the rejection rate for samples where the ring torsion fingerprint deviation exceeds 0.01 before and after optimization using Equation 3?

- What's the rationale for not directly modeling non-rotatable side-chain groups like phenyl rings and instead generating them using RDKit?

- Why was the training set restricted to 30 conformers per molecule with the lowest energy as opposed to a threshold based on the lowest energy?

- I'm seeking clarification on why, in section 4.4, you claim that the additional xTB optimization demonstrates the efficacy of the diffusion scheme in achieving diverse sampling. Could you elaborate on this point?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
