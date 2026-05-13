# 3DMolFormer: A Dual-channel Framework for Structure-based Drug Discovery

- Decision: Accept
- Scores: 8, 6, 6, 5

## Abstract
Structure-based drug discovery, encompassing the tasks of protein-ligand docking and pocket-aware 3D drug design, represents a core challenge in drug discovery. However, no existing work can deal with both tasks to effectively leverage the duality between them, and current methods for each task are hindered by challenges in modeling 3D information and the limitations of available data. To address these issues, we propose 3DMolFormer, a unified dual-channel transformer-based framework applicable to both docking and 3D drug design tasks, which exploits their duality by utilizing docking functionalities within the drug design process. Specifically, we represent 3D pocket-ligand complexes using parallel sequences of discrete tokens and continuous numbers, and we design a corresponding dual-channel transformer model to handle this format, thereby overcoming the challenges of 3D information modeling. Additionally, we alleviate data limitations through large-scale pre-training on a mixed dataset, followed by supervised and reinforcement learning fine-tuning techniques respectively tailored for the two tasks. Experimental results demonstrate that 3DMolFormer outperforms previous approaches in both protein-ligand docking and pocket-aware 3D drug design, highlighting its promising application in structure-based drug discovery.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces 3DMolFormer, a unified transformer-based framework for SBDD, which is capable of docking prediction and pocket-aware 3D drug design. The motivations of 3DMolFormer are clearly stated: current computational docking methods lack accuracy, while current 3D pocket aware drug design methods are unable to take full advantage of 3D structural information due to factors such as difficulties in 3D information modelling and limited data regarding ground-truth protein-ligand complexes. To represent a 3D complex of a protein pocket and a small molecule ligand, 3DMolFormer uses a parallel sequence composed of the SMILES atom token sequences for the protein and small molecule, along with the numerical sequence for 3D coordinates. A GPT architecture is pretrained through autoregressive generation of the parallel sequence. Fine-tuning consists of: (1) a supervised protein-ligand binding pose prediction task, and (2) a multi-objective RL pocket-aware molecular generation task. The presented results suggest that 3DMolFormer is successful in both fine-tuning tasks; it accurately predicts binding poses of ligands to protein pockets, and is capable of generating molecules that display high binding affinity to protein targets, while being synthesizable and exhibiting drug-like qualities.

### Strengths
- The proposed GPT framework seems interesting and presents novelty in terms of representing 3D complexes.
- 3DMolFormer presents strong results compared to other models on both fine-tuning tasks.
- The presentation of this paper is clear and well-structured.

### Weaknesses
 - The multi-objective optimization of the RL seems to be overly simplistic, including a reward function that assigns a constraint-based reward for QED and SA. Literature on multi-obj DRL shows using more sophisticated reward functions and multi-objective optimization techniques greatly improve agent performance and stability. Specifically, the reward function appears to treat QED and SA as binary constraints rather than continuous objectives, which may lead to suboptimal solutions. More advanced techniques, such as Pareto-based optimization or scalarization with adaptive weights, could potentially yield better results.
- Minimal ablation studies are conducted, and all results are based on one run. More runs should be conducted to demonstrate the soundness of the model. The lack of variance analysis makes it difficult to assess the statistical significance of the results. Furthermore, the absence of ablation studies on key components of the model, such as the dual-channel transformer architecture or the specific pretraining strategy, limits the understanding of their individual contributions to the overall performance.

Minor edits:
- Line 482: the parameter σ in Eq. (4) was is to 100

### Questions
- The authors state: “... the sampling of ligand SMILES utilizes the weights of the RL agent’s model, which are continuously updated during finetuning. In contrast, the generation of atomic 3D coordinates uses the weights from the model finetuned for docking, which remains unchanged during this process.” Why don’t the authors freeze the GPT weights during the sampling of ligands? If this hinders the model’s performance, why is this not shown in the ablation studies?

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
This paper introduce 3DMolFormer, a dual-channel Transformer-based model that can process atom sequence and coordinate information parallelly, and thus this model is claimed to be the first one that could simultaneously address both protein-ligand docking and pocket-aware 3D drug design, and it outperforms previous baselines in both tasks.

### Strengths
1. This paper introduce a novel transformer-based model that can handle docking and structure-based drug design simultaneously

### Weaknesses
1. This paper introduce a novel transformer-based model that can handle docking and structure-based drug design simultaneously

 1. This paper mention figure 1 multiple times when introducing model structure, however there is no figure 1 in the preprint.

### Questions
1. For the pose evaluation, the model only check for RMSD. Could you also report other pose-relate metrics like steric clashes and strain-energy?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a novel dual-channel transformer-based framework that effectively handles both protein-ligand docking and structure-based drug design (SBDD) tasks.

### Strengths
1. Docking and structure-based drug design (SBDD) are indeed dual tasks. The method presented in this paper, which models both tasks simultaneously within a single framework, represents a promising and logical approach.
2. By leveraging the similar architecture of GPT, the proposed method demonstrates significant scalability, including both model parameters and data volume, allowing for the effective utilization of large-scale datasets for pre-training.

### Weaknesses
As discussed in Section 5, the proposed method does not consider SE(3) symmetry explicitly but instead relies on data augmentation techniques. I think this aspect warrants further discussion and consideration. Although the experiments validate the method's effectiveness to some extent, I believe the persuasive power of these findings is limited when considering the following points:
1. For docking task, as far as I know, the more advanced approach Uimol-docking v2 is not included in the baslines.
2. For sbdd task, I noticed that the article directly employs evaluation metrics (Vina QED SA) as the reward function and utilizes reinforcement learning for fine-tuning. This approach may be considered unfair to other methods.  It may be necessary to incorporate abalation study as well as additional evaluation methods to comprehensively validate the effectiveness of the approach, for example, the delta score proposed in paper [1] may serve as a metric for assessing whether the method is overfitting to the Vina evaluation.

### Questions
Refer to the weaknesses.

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
4

### Summary
The paper presents 3DMolFormer, a dual-channel transformer framework designed for protein-ligand docking and pocket-aware 3D drug design. It utilizes a parallel sequence format to represent 3D pocket-ligand complexes and employs a "pre-training + fine-tuning" approach on a large dataset to model 3D information effectively.

### Strengths
Unified Framework: 3DMolFormer integrates protein-ligand docking and pocket-aware 3D drug design into a single model.
Parallel Sequence Format: Represents 3D pocket-ligand complexes, facilitating effective modeling of both discrete and continuous information.
Large-Scale Pre-training: Utilizes a pre-training.
Enhanced 3D Information Modeling: Effectively addresses challenges in modeling complex 3D interactions.
Novel dual generative+docking : Applicable to multiple tasks within structure-based drug discovery with 3D information, improving efficiency in drug design processes.

### Weaknesses
Docking. The model should be benchmarked against PoseBusters. The state of the art here includes AF3 and Chai-1, which achieve an accuracy of 76–77%. These models are only trained on PDB data. I understand that cofolding is not part of this approach, but we still need to assess the trade-offs on a widely recognized benchmark.

Synthetic Accessibility Score. It's stated that a score above 0.59 is given a value of 1. Why is this the case? Typically, a lower score indicates better synthetic accessibility. Is there a mistake, or are they using a different metric? I noticed that further clarification is provided in the Appendix.

Multi-score Thresholds. The thresholds for multi-score criteria appear to be chosen arbitrarily. For example, a value of 1 is assigned to QED and SA scores that surpass a certain threshold. Could you clarify how these cutoffs were selected?

Docking Formula. They provide a formula for redocking, but typically, a different target would require a distinct reference score, standardized by weight. There doesn’t seem to be a standard docking energy applied here.

Molecule Distribution. The paper does not specify the distribution of generated molecules in terms of size. Is there variation in logP values? How about the number of rotatable bonds?

Benchmarks for 3D Generation. I suggest using established benchmarks, such as CheckPose or DrugPose, for 3D generation.

### Questions
-Could you clarify how well you perform on PoseBusters?
-What are speed accuracy trade-offs in comparison to AlphaFold3 or Chai-1?
-How the thresholds where chosen for the addition. By calculating using the formula. It seems that it was chosen to use QED 4.39?
-What are the proteins in which you generated the molecules? How did you choose them? Are they diverse?

### Soundness
2

### Presentation
2

### Contribution
2
