# ShEPhERD: Diffusing shape, electrostatics, and pharmacophores for bioisosteric drug design

- Decision: Accept
- Scores: 8, 10, 6

## Abstract
Engineering molecules to exhibit precise 3D intermolecular interactions with their environment forms the basis of chemical design.
In ligand-based drug design, bioisosteric analogues of known bioactive hits are often identified by virtually screening chemical libraries with shape, electrostatic, and pharmacophore similarity scoring functions. 
We instead hypothesize that a generative model which learns the joint distribution over 3D molecular structures and their interaction profiles may facilitate 3D interaction-aware chemical design.
We specifically design \textit{ShEPhERD}\footnote{\textit{ShEPhERD}: \textbf{Sh}ape, \textbf{E}lectrostatics, and \textbf{Ph}armacophore \textbf{E}xplicit \textbf{R}epresentation \textbf{D}iffusion}, an SE(3)-equivariant diffusion model which jointly diffuses/denoises 3D molecular graphs and representations of their shapes, electrostatic potential surfaces, and (directional) pharmacophores to/from Gaussian noise. Inspired by traditional ligand discovery, we compose 3D similarity scoring functions to assess \textit{ShEPhERD}'s ability to conditionally generate novel molecules with desired interaction profiles. We demonstrate \textit{ShEPhERD}'s potential for impact via exemplary drug design tasks including natural product ligand hopping, protein-blind bioactive hit diversification, and bioisosteric fragment merging.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper introduces ShEPhERD, a generative SE(3)-equivariant diffusion model for molecular drug design that incorporates 3D structural features inspired by medicinal chemistry, namely shape, electrostatics, and pharmacophoric properties. The authors demonstrate ShEPhERD's utility for ligand-based drug design tasks, including ligand hopping, bioactive hit diversification, and bioisosteric fragment merging.

I appreciate the approach of leveraging prior target and chemical information to enhance generative models and commend the authors for advancing in this direction. While the case studies on specific targets are excellent, the general evaluation and particularly the comparative analysis with other methods could be significantly strengthened. I am inclined to give a strong score if these concerns are addressed.

### Strengths
- The paper is comprehensive and well-written, with excellent figures and molecular visualizations.
- Although conditioning on pharmacophoric features is not new in the field, this is the most thoughtful implementation of the approach to date and a very important direction more works should look into. The authors obviously have a very good understanding of drug discovery and SBDD that is not open seen at ML conferences.
- In my opinion, the field is overly obsessed with only focusing on de novo design models that cannot leverage any target specific data. Therefore, I really like the fact they were able to use experimental fragments screens to get better designed molecules.
- The inclusion of comparisons to REINVENT and random docking screens as baselines is a valuable addition, as these are seldom seen in DDPM literature. (However, I believe there is still room for improvement in the comparisons and evaluations—see below).

### Weaknesses
 **Main limitations:**

- While the method is strong, main limitation of the paper as it currently stands is the extreme lack of comparisons to related works in the experiments conducted. I kindly request the authors to benchmark against previous works in the relevant tasks. I am not looking for SOTA on all metrics, but better benchmarking is essential to understand the strengths and limitations of the work and I cannot recommend a strong accept at ICLR without more comparisons.
    - There are multiple works in a similar flavour that propose inpainting and/or conditioning on pharmacophore features of some kind. E.g.  DiffSBDD+inpainting [1], MolSnapper [2] and Diffint [3].
    - Compare to DiffHopp [4]/TurboHopp [5] in case of hit diversification. Obviously these models are only in the structure-based context.
    - Compare to ChemProjector [6]/SynFormer [7] incase of ligand hopping.
- Furthermore, the metrics could be greatly improved:
    - Heavy reliance on only Vina scores and shape/tanimoto similarity. While these are common in the field, they are insufficient to fully evaluate the quality of generated structures. The lack of metrics assessing the physical plausibility of the generated poses is a significant oversight. For instance, metrics from PoseCheck [8], such as clash scores, should be included to ensure that the generated molecules are not sterically hindered. Furthermore, the evaluation should consider the quality of hydrogen bonding networks, which are crucial for molecular recognition and binding. Simply relying on Vina scores does not provide a complete picture of the generated molecules' binding potential.
    - The work cites the PoseCheck [8] paper but does not use any of the metrics. For example, clashes are not measured. In the target conditioned cases, does ShEPhERD provide poses without clashes before relaxation? Is the model able to design hydrogen bonding networks better than previous SBDD models?
    - Strain energy is calculated in A.3 and the model appeared to perform well. However, the impact of this is greatly diminished by not comparing to other works. I would be grateful if the authors could include this to give context. Do the authors use the implentation in PoseCheck or their own? Is the strain energy calculated for poses bound inside the protein pocket?
    - PoseBusters [9] validity could also be used to access the quality of the structures. The current validity checks, while rigorous, do not fully capture the structural quality of the generated molecules. PoseBusters provides a more comprehensive assessment of structural validity by comparing generated structures to empirical distributions of bond lengths, angles, and dihedrals from the Cambridge Structural Database. This would provide a more robust evaluation of the model's ability to generate realistic molecular geometries.
- An expanded related work section covering models that perform ligand hopping, scaffold hopping and fragment merging would base the work in the literature much better.
- Would be nice to see anonymous code in the review stage.
- In the hit diversiation section, the authors claim that ShephERD produces enriched sampled “Despite having no knowledge of the protein targets”. While it is technically true the model has never directly see the receptor coordinates, a large amount of structural information is leaked/provided based on the complimentarity of the 7 experimental ligands. This is not a weakness of the method but I believe the language to be misleading. A simple rewording should do.
- The joint model/inpainting method used to condition on the target profile is not novel, as this was done in DiffSBDD 2 years ago [1]. A citation to that work and the original RePaint paper reproducing the ‘replacement’ method of inpainting in the main text would suffice.
- In the interaction-conditioned generation section you only generate 20 samples per target and filter based on interaction similarity. How many samples are left after filtering? How can you ensure statistical significance?
- It is not clear to me if any attempt was made to reduce data leakage between train and test sets (except for size) as the splits seem random. How can you be sure that the target interaction profile on the test samples are not the same/similar to those seem during training?
- Comparison to REINVENT.
    - Was REINVENT trained to convergence? 10,000 oracle calls seems quite low in my experience? (Happy to be proved wrong)
    - Can the authors clarify exactly which version of REINVENT they use? They seem to use an old version from the PMO benchmark. This is the 2017 implementation I believe? I would encourage them to use the largest REINVENT4, this is easy to use and a strong baseline in my experience (https://github.com/MolecularAI/REINVENT4).
    - Little measure of synthetic accessibility in the work. REINVENT does surprisingly well on SA score in my experience. Can this be benchmarks quantitively?

**Minor points:**

- Some background on various inpainting/conditioning strategies for DDPMs would be nice (i.e. replacement method [what is used here], classifier guidance, reconstruction guidance, Doobs-H transform)
- The generated samples in Appendix A.10 are quite small. It would be nice to include some larger samples as well to see how the model handles larger structures.
- The neural network architecture is described in great detail. In my opinion taking too much space. I would prefer to see this in the appendix with more discussion on experiments in the main text.
- What was the intuition for scaling the pharmacophore feature vector by 2.0?
- Can the target profile guidance be more or less ‘weakly’ enforced?
- It would be nice to see the fragment merging work replicated on more than one target. I would recommend the Mpro screen (on Fragalysis already) for example. You can then compare for novelty against the molecules derived from than screen in the COVID moonshot- To what extent does conditioning with the ShEPhERD method limit diversity of new samples? Could be that previous DDPMs produce on average worse samples but allow for the exploration of novel chemotypes? (My guess is this method is still very useful but I would like to see this discussed/measured)
- Have you tried an ablation of the joint noising regime? I believe in DiffSBDD its benefits was found to be marginal. [1]
- Could your pharmacophore similarity metric be seen as related to interaction fingerprint similarity? 
- Is it possible to use ShEPhERD completely de novo? I.e. for a new target without example molecules in the PDB? Could pharmacophore features be constructed from hotspot maps/manual feature engineering?
- The fragment merging protocol is nice, can a semi-automated pipeline be provided in the code?
- Section A.9 correctly points out the disparity between the size of ligand seen during training and those seen during evaluation. Why not include larger ligands in the training set?
- Given the large training set size, it would be nice to see some scaling law experiments in terms of dataset and model size. (Given that I am not aware of the resources available to the authors this will not impact my review score - I am just interested if its possible)..
    - Can you provide a list of the 7 PDBs used to perform these experiments?
- Figure 1 + 2:
    - Are both very good: I would consider merging to safe space and add more analysis/discussion.
- Figure 3:
    - Can ‘dataset samples’ be added to the histograms in the right of the figure?
- Figure 4:
    - The PyMol in this paper is generally very good but the overlapping molecules in this figure is highly confusing. A key/color map would be very helpful. (Especially for hit diversification section).
    - REINVENT molecules seem to consistently outperform ShEPhERD on SA scores. I would be good to include an example structure instead of just listing the metrics.
    - The PDB targets are quite well chosen (Kinases/COVID MPro etc), adding target names in brackets next to PDBs would be helpful.

### Questions
- To what extent does conditioning with the ShEPhERD method limit diversity of new samples? Could be that previous DDPMs produce on average worse samples but allow for the exploration of more novel chemotypes? (My guess is this method is still very useful but I would like to see this discussed/measured)
- Have you tried an ablation of the joint noising regime? I believe in DiffSBDD its benefits was found to be marginal.
- Could your pharmacophore similarity metric be seen as related to interaction fingerprint similarity? 
- Is it possible to use ShEPhERD completely de novo? I.e. for a new target without example molecules in the PDB? Could pharmacophore features be constructed from hotspot maps/manual feature engineering?
- The fragment merging protocol is nice, can a semi-automated pipeline be provided in the code?
- Section A.9 correctly points out the disparity between the size of ligand seen during training and those seen during evaluation. Why not include larger ligands in the training set?
- Given the large training set size, it would be nice to see some scaling law experiments in terms of dataset and model size. (Given that I am not aware of the resources available to the authors this will not impact my review score - I am just interested if its possible).

### Soundness
2

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
10

### Rating Number
10

### Confidence
5

### Summary
This paper presents a new method for the generation of small molecules conditioned on shape, electrostatic potential surface, or pharmacophores.  This development provides a useful and practical tool that can complement multiple conventional tasks during various stages in drug design projects.  The method is a joint diffusion model that predicts molecules in terms of graphs plus coordinates, surfaces sampled on a modest number of points (with or without an electrostatic potential), and pharmacophores (types and coordinates).  The conditional generation uses inpainting to sample the molecule graphs and coordinates conditioned on one or more other properties of the molecule, which can mimic a known target molecule.

### Strengths
The paper presents a substantial advance compared to previous related methods; it has a strong logical foundation with clear exposition of the method and its parameters, and a diverse set of demonstrations.  The conditional generation of molecules based on ligand-only properties is important in applied drug discovery and the method offers both a practical way for thinking about some of the concepts and a tool that can be readily applied.  In addition, it introduces useful and practical datasets, and it defines a simple but clear metric for comparing surface shapes.  I think that the work opens up a logical framework for building practical tools in drug discovery and will influence followup research.

### Weaknesses
Most of the weaknesses of the paper are somewhat superficial and do not limit the importance of this contribution.

All the conditional generation requires providing n1 a priori for each sample, and the pharmacophore application, which is particularly interesting and useful, requires providing both n1 and n4.  In addition to sampling n4 based on the chosen n1 and the training data distribution, have the authors considered exploring ways to automate or predict values for parameters like n1 and n4?  It would be very interesting to explore the regime where compute limitations are of no concern.

The demonstration of conditional generation in Fig 3 is performed on a random subsample of the training molecules.  I understand that there is no perfect split of molecules, however, the jump from a random subset, which work rather well, to natural products, which are completely out of distribution and don't appear to work well (albeit better than reinvent), appears a bit too dramatic.  To enhance the robustness of the evaluation and to gain additional insights, the authors could create additional, harder, splits by molecular properties such as numbers of atoms or rings, splits by scaffold, or splits by similarity clustering of the training data. Because the authors provide two new training datasets, it is perhaps more important than it would otherwise have been to provide and characterize a number of distinct, increasing difficulty splits.

The surfaces were fit on modest numbers of points and the graph embedding networks are surprisingly small, which are all probably a result of trying to keep the graph neural nets from collapsing.  It is possible that these shortcuts (and the usual problems of graph neural nets and scaling to larger systems) lead to the size-dependent effects demonstrated in the supplemental materials; these limitations might also underpin the examples of natural products.  It may be worth adding a brief note in the main text of the paper to discuss the scaling of the method with the size of the small molecules, even if the detailed analysis is reserved for the supplemental materials due to space limitations.

### Questions
Although it is not unreasonable, what is the logic for fitting the surfaces onto the volumes in order to obtain the parameters required for the method?  Also, why only fitting the particular set of discrete numbers of points (50, 100, 150, 200, 300, 400) and not, say, a function of the number of atoms, or of the total surface size?  Would there be a problem with scaling the method to a large number of points, or is it simply deemed unnecessary?  As a minor related question, what is the purpose of a separate set of surface points for x2 compared to x3?  Wouldn't the coordinates of x3 suffice for both tasks?

Other than following prior work, do the authors have a high level rationale for selecting the particular subset of targets from the PDB in Zheng et al (2024)?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces the ShEPhERD method for generating 3D molecules that satisfy specific shape, electrostatic surface, and pharmacophore constraints. The method represents molecular shapes, electrostatic surfaces, and pharmacophores as point clouds and jointly models these properties with the 3D molecular structure. During sampling, inpainting techniques are used to generate molecules that meet the specified properties. This method enriches ligand-based drug design approaches and shows significant innovation in its application areas. However, it lacks substantial innovation in the basic structure of the generative algorithm.

### Strengths
1. The method provides a comprehensive summary of related work. To my knowledge, it is currently the only 3D generative model that simultaneously incorporates shape and pharmacophore constraints.
2. The authors achieved credible results in three specific tasks, partially demonstrating the method’s effectiveness.

### Weaknesses
1. The method represents shapes and electrostatic surfaces as point clouds and generates them together with the molecular structure using 3D graph neural networks, which may significantly impact computational efficiency. The generative model based on DDPM may also have efficiency drawbacks. The authors should provide relevant statistical results, including the average time for generating a single molecule and the computational resources required for training and inference. Furthermore, the memory footprint of the point cloud representation should be quantified, as this could limit the size of molecules that can be effectively handled.
2. The method lacks comparisons with other methods, casting doubt on the superiority of the results.
    (1). For shape-based molecular generation, methods like ShapeMol and SQUID can achieve similar effects and should be compared. Specifically, the authors should compare not only the shape similarity scores but also the chemical diversity of the generated molecules. A comparison of the distribution of Tanimoto coefficients for generated molecules against a reference set would be informative. (2) For pharmacophore-based molecular generation, both pharmacophore type matching and structural matching should be considered and evaluated separately. If combined comparison is necessary, reference to 2D pharmacophore works such as the Match Score (Nature Communications | (2023)14:6234) is suggested. The evaluation should include a breakdown of the contribution of each pharmacophore feature to the overall score. (3) The authors should provide the similarity of generated molecules to reference molecules for each specific task to ensure that the generated molecules are not simple variations of the reference molecules. This should include a quantitative analysis of molecular similarity metrics, such as Tanimoto coefficient based on Morgan fingerprints, and should be presented as a distribution rather than a single average value.

### Questions
My questions are the same as mentioned in Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
