# Backdiff: a diffusion model for generalized transferable protein backmapping

- Decision: Reject
- Scores: 6, 6, 3

## Abstract
Coarse-grained (CG) models play a crucial role in the study of protein structures, protein thermodynamic 
properties, and protein conformation dynamics. Due to the information loss in the coarse-graining process, backmapping from CG to all-atom configurations is essential 
in many protein design and drug discovery applications when detailed atomic representations are needed for in-depth studies. Despite recent progress in data-driven backmapping approaches, devising a backmapping method that can be universally applied across various CG models and proteins remains unresolved. In this work, we propose BackDiff, a new generative model designed to achieve generalization and reliability in the protein backmapping problem. BackDiff leverages the conditional score-based diffusion model with geometric representations. Since different CG models can contain different coarse-grained sites which 
include selected atoms (CG atoms) and simple CG auxiliary functions of atomistic coordinates (CG auxiliary variables), 
we design a self-supervised training framework to adapt to different CG atoms, and constrain the diffusion sampling paths with arbitrary CG auxiliary variables as conditions. Our method facilitates end-to-end training and allows efficient sampling across different proteins and diverse CG models without the need for retraining. Comprehensive experiments over multiple popular CG models demonstrate BackDiff's superior performance to existing state-of-the-art approaches, and generalization and flexibility that these approaches cannot achieve. A pretrained BackDiff model can offer a convenient yet reliable plug-and-play solution for protein researchers, enabling them to investigate further from their own CG models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors developed BackDiff, a diffusion model that generates all-atom protein structures from coarse-grained models. During coarse-graining, atoms that are grouped together are represented via auxiliary variables, and the remainder are denoted CG atoms. To train the diffusion model, the authors perform an imputation task, i.e. the missing atoms are generated from a noise distribution conditioned on the remaining CG atoms. To improve generalizability to various coarse-graining methods, the missing atoms can be chosen randomly or semi-randomly from the all-atom configuration during training. In practice, the authors do not generate the coordinates of the missing atoms, instead choosing to generate their displacements from the corresponding carbon atoms in the C-alpha representation, thus necessitating the requirement that all C-alpha atom coordinates are included in the set of CG atoms. 

In order to incorporate information in the auxiliary variables, the authors constrain the reverse diffusion process. A manifold constraint is applied to each diffusion step, correcting the configuration via posterior conditions on auxiliary variables, bond lengths, and bond angles. 

The authors compare their method against two other backmapping models, GenZProt and TD, showing superior performance in terms of accuracy, diversity, and plausibility.

### Strengths
The self-supervised approach enables training for specific coarse-graining techniques as well as generalizability to data from multiple CG methods.

### Weaknesses
I am concerned about potential data leakage, based on random splitting of frames into training, test, and validation sets. 

To compute accuracy, the authors first identify a generated sample that has the lowest RMSD to the all-atom reference configuration. They then report the MSE of the center of mass of the side chain atoms compared to the reference (SCMSE). Instead, I’d prefer to see the distribution of RMSD across all generated structures, starting from different coarse-grained inputs. This would be helpful in evaluating different CG strategies.

### Questions
In Table 1, why does the BackDiff (fixed) model have significantly lower DIV scores (i.e. more diversity of generated structures) compared to BackDiff (trans)? Intuitively, I’d expect the CG-transferable model to produce more diverse structures.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a generalized transferable backmapping method that can be applied to arbitrary CG mapping without the need for retraining. The paper formulates backmapping as an imputation problem, where the model generates C alpha-atom distance vectors conditioned on CG atoms and CG auxiliary variables (aggregated properties of groups of atoms). The model can achieve generalization across different CG mappings by training with (semi)-randomly selected CG atoms and auxiliary variables. The model generates output in Cartesian coordinate space but produces well-constrained bond lengths and angles by imposing manifold constraints. The model is compared to a recent transferable generative modeling work, with experiments conducted following similar settings including the dataset and metrics, as well as a recent all atom conformer generation model.   

This paper shows clear novelty and strengths, but I still have some questions regarding the experiments.

### Strengths
1.	This is a first backmapping algorithm generalized for arbitrary CG mappings. 
2.	The idea of formulating the generalized backmapping problem as an imputation problem is novel and makes a lot of sense.

### Weaknesses
-	Have you re-implemented the baseline models (especially CGVAE) to condition them on other CG variables such as N and sidechain COM for the UNRES benchmark? If BackDiff is conditioned on C alpha, N, and side chain COM, while CGVAE is conditioned only on C alpha as in its original paper, it would be hard to tell if the performance difference is coming from the method or the difference in information given to the models. The same applies for MARTINI and Rosetta benchmarks. Alternatively, you could report the performance of BackDiff conditioned on C alpha only, with no CG auxiliary variable constraints on side chain COM. 
-	Table 1 and Table 2 report the mean RMSD across 100 sampled structures. However, a large mean RMSD of the backmapped structures could also suggest high diversity among all atom conformations, rather than high error in the structures, since one CG structure can correspond to many all atom conformations. Reporting the minimum RMSD across 100 samples should be a better metric for assessing error.
-	How did you select the PED entries for testing? The three test proteins all look pretty linear and disordered. How does the model perform on a globular protein?
-	Could you report the diversity of the generated structures conditioned on the same CG structure? For example, in the referred baseline [1], the authors reported quantitative metrics for diversity, such as the Earth Mover’s Distance for side chain torsion angles. 
-	Could you provide a speed analysis of your method, for example how much time required to backmap a frame, similar to what was done in [1]?
-	It could be interesting to see how the model performance changes as we increase the CG resolution (the number of CG atoms and CG auxiliary variables), especially in terms of the diversity of generated all atom conformations. This could provide insights into the CG system’s entropy. This is not a requirement, but just a curiosity.

### Questions
-	Yang & Bombarelli’s model is called GenZProt and not CGVAE.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The manuscript presents a method based on a diffusion model for backmapping coarse-grained MD results to full atom coordinates. By incorporating self-supervised training strategies, the proposed method can be generalized to multiple different coarse-graining (CG) methods. Experimental results indicate that the proposed method achieves better performance than state-of-the-art methods in backmapping CG configurations.

### Strengths
1. The proposed method can be applied to multiple different CG methods without the need for retraining.

2. Experimental results demonstrate that the proposed method outperforms baseline methods.

### Weaknesses
1. The Equivariance handling approach in the method constructs a reference coordinate system using the first three amino acids of each protein sequence. This implies that if the positions of the first three amino acids vary, the reference system will also differ, which may not be an ideal approach.

2. In Table 3, the Mean Absolute Error (MAE) of bond length for BackDiff (cons) can reach 0, which appears too good to be true.

3. In Table 3, the numerical values of the standard deviation (std) in the second and third rows are almost in the same range as the mean values, which is strange.

### Questions
1. Is the model used in the method SE3 equivariant?

2. Given that the model learns the displacement of omitted atoms from alpha carbons, why not directly learn displacement in the local coordinate system of each amino acid? This approach could ensure that the representation is SE3 equivariant.

3. I am not familiar with the PED dataset. Why were only 92 proteins selected out of 227 for training and testing data?

4. What do you mean by single- and multi-protein experiments? What is the primary difference? When frames are used for data partitioning, is it possible for different frames of the same protein to appear in both the training and testing sets, potentially leading to data leakage?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
