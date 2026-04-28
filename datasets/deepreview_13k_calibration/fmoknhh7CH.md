# Harmonic Prior Flow Matching for Multi-Ligand Docking and Binding Site Design

- Decision: Reject
- Avg Score: 5.20
- Scores: 5, 5, 6, 5, 5

## Abstract
A significant amount of protein function requires binding small molecules, including enzymatic catalysis. As such, designing binding pockets for small molecules has several impactful applications ranging from drug synthesis to energy storage. Towards this goal, we first develop HarmonicFlow, an improved generative process over 3D protein-ligand binding structures based on our self-conditioned flow matching objective. FlowSite extends this flow model to jointly generate a protein pocket's discrete residue types and the molecule's binding 3D structure. We show that HarmonicFlow improves upon the state-of-the-art generative processes for docking in simplicity, generality, and performance. Enabled by this structure modeling, FlowSite designs binding sites substantially better than baseline approaches and provides the first general solution for binding site design.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The problem is to predict the structure of the binding pocket for a set of ligands, given the structure of the protein backbone and the 2D structure of the ligand(s). The authors introduce two flow matching models: HarmonicFlow (predicts the 3D structure of the pocket without residue types) and FlowSite (predicts both the 3D structure of the pocket and residue types).

In the main text, there are three groups of experiments:

Q1. Comparisons of HarmonicFlow with:
- DiffDock on PDBBind,
- EigenFold on MOAD.

Q2. Estimation of correctly predicted residues in the binding site on PDBBind and MOAD datasets.

Q3. Ablation studies for Flow matching design choices.

In addition, the authors introduce fake ligand data augmentation and recycling strategy for the flow model.

### Strengths
FlowSite shows better quality than the methods to which it was compared in the reported settings.

### Weaknesses
 - The paper is rather hard to follow.
- The design of most experiments is not clear to me (see questions).

- In Q1, the approach is verified on a problem of site-specific docking. Why do you think that the quality of docking tells much about the quality of side-chain prediction (DiffDock can perform this task without this information)? Moreover, for me, it is not fair to compare FlowSite with a blind docking algorithm in a site-specific setting.
- In Q2, you compare the ground truth amino acids with the predicted ones. Is it a fair surrogate metric for de novo generation, when for a given set of ligands and backbone coordinates there potentially can be many different answers? An algorithm that can generate pockets with a better binding affinity than affinity of pockets from the dataset, will have a low score.
- The output of the flow-matching model should also depend on the sampled initial conditions. In Q2 experiments, do you consider a single run of the noise sampling? Have you tried to sample many different noise vectors and compare the outputs?
- You said that it is not feasible to estimate the energy. Why? I suppose that the energy of the designed protein and the affinity of the complexes can be somehow estimated using traditional or machine learning methods. At least, it is possible to use the all-atoms confidence model from DiffDock and compare scores of complexes.
- In many experiments, you mentioned the oracle method that has access to the ground truth ligand structure. What exactly is this method?
- How much time does it take to train your model on PDBBind and MOAD?

### Questions
1. In Q1, the approach is verified on a problem of site-specific docking. Why do you think that the quality of docking tells much about the quality of side-chain prediction (DiffDock can perform this task without this information)? Moreover, for me, it is not fair to compare FlowSite with a blind docking algorithm in a site-specific setting.
2. In Q2, you compare the ground truth amino acids with the predicted ones. Is it a fair surrogate metric for de novo generation, when for a given set of ligands and backbone coordinates there potentially can be many different answers? An algorithm that can generate pockets with a better binding affinity than affinity of pockets from the dataset, will have a low score.
3. The output of the flow-matching model should also depend on the sampled initial conditions. In Q2 experiments, do you consider a single run of the noise sampling? Have you tried to sample many different noise vectors and compare the outputs?
4. You said that it is not feasible to estimate the energy. Why? I suppose that the energy of the designed protein and the affinity of the complexes can be somehow estimated using traditional or machine learning methods. At least, it is possible to use the all-atoms confidence model from DiffDock and compare scores of complexes.
5. In many experiments, you mentioned the oracle method that has access to the ground truth ligand structure. What exactly is this method?
6. How much time does it take to train your model on PDBBind and MOAD?

### Soundness
1 poor

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper propose FlowSite as a new generative model of protein pocket residue types and ligand conformations.

Methodology novelties include 1) replace diffusion with flow matching; 2) use harmonic priors; and 3) modified model architecture.

Computational results on (multiple) docking and binding site design are analyzed.

### Strengths
1. Good organization.

2. Elevation in final performances.

3. Sufficient ablation studies.

4. Fake ligand augmentation is an interesting proposal.

### Weaknesses
1. Overall the paper is much of a summarization of known techs: harmonic priors are discussed in EigenFold; self-conditioning is applied in CV/ RFdiffusion; replacing diffusions with flow matching is well studied in CV; and model architecture improvements are somehow trivial. 

2. Three applications are proposed in this paper, while except for docking, multiple docking / binding site generation are not well investigated. The idea of multiple ligand docking itself is interesting, but not well studied. As it is mentioned in the title I'd expect some impressive case studies of multiple docking and some analysis of significance in the result. I would suggest the authors be more focused.

3. Backbone flexibility is not allowed in the entire picture. All experiments are done on PDBBind which provides accurate holo structures of proteins. This very much limited the significance of improvements on figures in this paper.

4. Baselines are weak.

### Questions
1. Are sidechains configurations by any means included as data inputs?

2. I would expect some analysis of the ODE dynamics, especially with regard to the joint dynamics of residue types and molecular conformations.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The author introduces the flow matching-based algorithm for multi-ligand docking and binding site design. The results show both FLOWSITE and HARMONICFLOW achieved the start-of-art performance. Noticeably, the FLOWSITE is the first deep-learning method for designing ligand binding pockets.

### Strengths
1. In general, the writing is great. The contribution is clearly presented, and the method is well-introduced.
2. The evaluation is fair and the improvement is significant.
3. The limitation of FLOWSITE is well introduced.

### Weaknesses
Most of the technology is just an application of the existing methods which prevents the paper from getting higher scores in machine learning conferences.

### Questions
How fast are the two methods in terms of inference speed?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes HarmonicFlow, an ODE flow model for generating pocket residue types and molecule structures.

### Strengths
- This paper studies an interesting problem.
- The writing is generally clear.

### Weaknesses
 - The problem of multi-ligand binding is interesting, but I am not sure how important this task is. The authors briefly discussed this in Sec 2, and more detailed explanations can be helpful.

 - In Sec 1 & 2, the authors highlight that HarmonicFlow is the first DL method to handle multi-ligand docking. One critical question is that how fundamentally different multi-ligand docking is from protein-ligand docking (the existing methods). 
If they are different, then one question is that the authors compared HarmonicFlow with DiffDock, but they are solving different problems: one for multi-ligand docking and the other for protein-ligand (both single- and multi-ligand) docking. Why their numbers can be compared to each other?
If they are the same in terms of the method, then HarmonicFlow is not the first DL method that can handle multi-ligand docking.

 - Does this vector field $u$ in Eq 1 have any physical meaning?

 - Can authors help summarize the essential difference between score matching / denoising diffusion with the objective (Eq 1&3) in this paper? Because score matching and denoising diffusion can be treated as ODE flow models. Also, is the proposed HarmonicFlow specific for multi-ligand docking? Now it seems that it can also fit for the general protein-ligand docking.

 - Many baselines, such as the related works mentioned in Sec 2, are missing in the experiments.

### Questions
Please see above.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on biomolecular designing problems. Two methods, HormonicFlow and FlowSite, are proposed. HarmonicFlow leverages flow matching for generating 3D binding poses of multi-ligands, and this method achieves better performance than the previous SOTA method. Furthermore, FlowSite leverages flow matching for designing binding sites for small molecules, where both discrete (residue types) and continuous (ligand pose) data are jointly generated.

### Strengths
1. HarmonicFlow applies flow matching on 3D binding pose generation for multi ligands. The corresponding experimental results are strong, surpassing the previous method, DiffDock. The method is simple yet effective. 
2. Binding site design is a novel task in machine learning community. This task is important to some real-world applications. As for novelty of methods, to design the residue types of the binding site, it generated both discrete and continuous variables under the framework of flow matching. 
3. Many reasonable tricks are used to improve the performance, such as harmonic prior and structure self-conditioning.
4. The comprehensive experiments show the ability of both HarmonicFlow and FlowSite. Almost all experiment details are clearly clarified. The results demonstrate the effectiveness of proposed methods.

### Weaknesses
There are many other tricks used for training FlowSite and HarmonicFlow, such as many auxiliary losses similar to those in Alpafold2. But there is no related ablation study.

Because no side-chains are involved in generation, binding affinity cannot be evaluated. Is there any post hoc method to generated side-chains for the designed binding site? If so, from my perspective, evaluation on binding affinity of generated binding sites and given ligands is more rationale.

### Questions
Because no side-chains are involved in generation, binding affinity cannot be evaluated. Is there any post hoc method to generated side-chains for the designed binding site? If so, from my perspective, evaluation on binding affinity of generated binding sites and given ligands is more rationale.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
