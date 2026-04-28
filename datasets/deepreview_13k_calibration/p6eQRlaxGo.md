# Design of Ligand-Binding Proteins with Atomic Flow Matching

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 5, 6

## Abstract
\vspace{-5pt}
Designing novel proteins that bind to small molecules is a long-standing challenge in computational biology, with applications in developing catalysts, biosensors, and more.
Current computational methods rely on the assumption that the binding pose of the target molecule is known, which is not always feasible, as conformations of novel targets are often unknown and tend to change upon binding.
In this work, we formulate proteins and molecules as unified biotokens, and present \method, a novel deep generative model under the flow-matching framework for the design of ligand-binding proteins from the 2D target molecular graph alone.
Operating on representative atoms of biotokens, \method captures the flexibility of ligands and generates ligand conformations and protein backbone structures iteratively.
We consider the multi-scale nature of biotokens and demonstrate that \method can be effectively trained on a subset of structures from the Protein Data Bank, by matching flow vector field using an SE(3) equivariant structure prediction network.
Experimental results show that our method can generate high fidelity ligand-binding proteins and achieve performance comparable to the state-of-the-art model \rfdiffusionaa, while not requiring bound ligand structures.
As a general framework, \method holds the potential to be applied to various biomolecule generation tasks in the future.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents ATOMFLOW, a novel deep generative model under the flow-matching framework for the design of ligand-binding proteins from the 2D target molecular graph alone.  It co-design the protein binder structure and the target-molecule flexibility. Experimental shows the method's effectiveness.

### Strengths
S1. This method is based on full-atom level protein and molecule generation,  with both the protein binder and the molecule pose is designed.
S2. Experiments show the effectiveness of the method.

### Weaknesses
W.1 I think the major weakness lies in its novelty. First of all, using Flow-matching with full atom generation in peptide [1] or protein [2] other bio-molecules is not a new idea. Besides, the equivariant generation process [3,4,5] and FAPE loss in AlphaFold still follow previous works. Therefore,this work appears to be a fusion of several previous studies, applied in a new task, lacking innovation in terms of the methodology. I hope the author could clarify the difference between the techniques used in this paper and the origianl ones, and the  improvements upon previous approaches. This would give the authors an opportunity to highlight any methodological innovations that may not be immediately apparent. Therefore, I have doubts about whether the level of novelty in this paper meets the standards expected for a top-tier conference like ICLR.

W.2 In the experiment, RFDiffusion based method like RFDiffusionAA is compared, but there should be more works which can fulfill such tasks, such as [6] and [7]. I am wondering that can such baselines be all included into experimental comparison? I hope the author  could discuss any technical or practical limitations that may have prevented including other baselines. Besides, I think AlphaFold3 can also fulfill this task, so what is the advantage of yours over AlphaFold3? Or there are several distinct differences between AtomFlow and AlphaFold3 in design protein binder with molecule targets? I hope the authors can clarify if AlphaFold3 is directly applicable to this specific task of designing ligand-binding proteins from 2D molecular graphs, and if so, I hope the authors to explain the key differences or advantages of their approach compared to AlphaFold3 for this particular application.

### Questions
My major question is about the novelty and insufficient experiments. I hope the author can help to address my concerns.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The authors present the ATOMFLOW architecture for the design of protein folds conditioned by the ligand SMILES description. The tool actually can be useful for the bioinformatics community, but many more validation tests are required here. I also thank the authors for providing the code, we had fun time generating different folds and assessing them.

### Strengths
It's a well written technical paper about a novel architecture that can be useful for the bioinformatics community. I am thankful to authors for providing the code. Please remove the infinite loop and the check for the clash score, it takes too much time. 

We have executed it on a couple of example, including recent L targets from CASP. I have carefully examined the generated output for L1000 ligand set. With a significant probability (about 30%), AtomFlow finds the native experimental fold (we have ~20 PDB structures with ligands different from those in CASP) and the binding site, and is also rather stable with variations of the sequence length. If I vary the design length slightly, AtomFlow seems to prefer to shorten loops even those inside the binding site, so it seems it has memorized the space of all protein folds in the PDB and simply selects the one it has seen during training. It actually can be a useful tool for fold search and classification.

Individual protein-ligand contacts vary in quality significantly. So I have doubts in any usefulness of further affinity prediction providing a very low quality of experimental affinity data (see below).

We have also tried to generate folds for a purine ligand, which is a part of nucleotide bases (expecting many different folds to be generated). Surprisingly, at a constant generation length, the results were extremely conservative, with zero novelty and extremely low diversity, preferring the fold that dominantly occurs in the PDB. So, I suggest the authors to run more cross-validation tests hiding some fold classes from the training and trying to reproduce them in the test. Otherwise it seems there is a significant bias towards the folds that are abandon in the PDB.

### Weaknesses
There is little technical novelty in the architecture blocks, loss function of flow matching process (but the architecture is novel and useful).

Since you are using the FAPE loss, why do you need equations 3-5, references to Riemannian Flow Matching, and fancy words? It will be much cleaner to remove this part. The justification for the specific form of the loss function, which includes time-dependent weighting, is not sufficiently clear, especially given the use of FAPE. The connection between the Riemannian Flow Matching framework and the practical implementation of the loss needs to be more explicitly explained, as the current presentation makes it seem unnecessarily complex.

Binding affinity experiments are far from complete and better to be removed. You need to split the data correctly and run multiple affinity benchmarks, for example, following CASF and DUDe protocols. It will also be useful to provide energies and folds for some well-studied proteins that have multiple structures with different ligands (they are currently coming in the PDB, you may look at the last CASP experiment). Please also provide Vina scores for native ligand poses. Vina is not the best proxy for the affinity, as it was design only to rank binding poses for the same protein-ligand complex.

Please also be aware of the quality of current affinity training sets -- e.g., https://pubs.acs.org/doi/full/10.1021/acs.jcim.4c00049.

"The scatter plot of scRMSD vs. pdbTM shown in Figure 6B reveals that ATOMFLOW has the ability to generate structures that are quite different from existing proteins with acceptable designability" - Well, all of your designs have scores > 0.5, a few are around 0.5. It means that the fold structure is the same as in the PDB, no new folds have been discovered. Please try to discover a fold with a TM score around 0.2.

### Questions
LCFM and LCFM-FAPE indeed give zero at the same point. But why their gradients will be similar? 

Can you explain more what does it mean "since the aligning object x varies upon training."? It contradicts all the theory you have just presented, no?

Can you comment on proper cross-validation experiments by removing certain fold classes from training? The same is valid for affinity experiments. Please also consider novel data with one protein and multiple ligands as validation, see four datasets from CASP16, for example.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents AtomFlow, a flow matching model for designing a protein structure to bind a small molecule ligand. The model jointly denoises the structure of the protein and ligand and thus does not require knowledge of the ligand pose, unlike RFDiffusionAA. The architecture is based on AlphaFold and predicts denoised structures from a distance map input of the input structure. The method is evaluated on (1) the set of 4 ligands studied in RFDiff-AA, and (2) an expanded set of ligands curated by the authors. AtomFlow is shown to have comparable or better designability than RFAA as well as similar Vina score.

### Strengths
* The work is solidly executed, with sensible architectural choices, strong initial evaluations, and clear and concise writing. 
* The task tackled is significant and the competitive results signify well-executed model engineering and training practices.
* The authors re-derive the quotient-space flow matching fromework from AlphaFlow with more solid theoretical justification.
* The paper is quite clearly written. The figures are well made, visually appealing, and informative.

### Weaknesses
 **Originality**
* The methodology can be described as a flow-matching version of RFDiff-AA and does not score high on originality / novelty from a ML perspective. Further, the flow model architecture and noising process are based on AlphaFlow, with different justification but no difference in practice as far as I can tell. To improve on this axis, while it's not clear that more methodological novelty is needed for its own sake, the authors could focus on novel evaluations or applications of the proposed method.

**Quality**
* The computational evaluations are well executed, but limited in scope. Most of the analysis focuses on only 4 ligands, raising concerns about sample size and statistical significance. 
* The diversity and novelty evaluations are nice, but only AtomFlow is evaluated, not RFDiff-AA or the other baselines.


**Significance**
* The overall significance of the contribution is unclear as it represents an incremental methodological advance over RFDiff-AA with more or less the same model capabilities. The authors argue that not needing to specify the ligand pose is a big plus, but no meaningful evidence or use case is provided for this distinction. After all, RFDiff-AA has been experimentally validated, whereas AtomFlow-generated poses have not. It is of course not expected for a ML submission to experimentally validate the proteins, but it should be made a bit clearer why the main point of difference with RFDiff-AA is important to tackle as a ML problem.

### Questions
No specific questions.

### Soundness
3

### Presentation
3

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
In this work, the authors present ATOMFLOW, a deep generative model based on a flow-matching framework for designing ligand-binding proteins from 2D target molecular graphs. ATOMFLOW operates on representative atoms of biological tokens to capture ligand flexibility, iteratively generating ligand conformations and protein backbone structures. Overall, this paper introduces an innovative model that offers a novel approach to designing proteins that bind to specific molecules.

### Strengths
-  The paper is well-structured and logically organized. Readers can easily follow the authors’ thought process, and the content is presented in a way that is easy to understand.
- Conceptualizing both proteins and molecules as biotokens with representative atoms is an interesting approach. Although similar concepts are mentioned in Umol and RoseTTAFold All-Atom, using this framework to design specific proteins without relying on the initial ligand structure demonstrates impressive performance and is commendable.
- Compared to RFDiffusionAA, ATOMFLOW shows competitive results in specific protein-molecule design tasks as well as in binding affinity prediction. The supplementary experiments in Table 8 of the appendix provide additional support for the current experimental results.

### Weaknesses
 - The intervals used in modeling the distance map for ligands and proteins are not uniformly divided. While the authors account for differing precision requirements between residues and atoms, given that the paper frames proteins and molecules as biotokens with representative atoms, could the distance partitioning criteria be standardized? Establishing a more universal distance characterization approach—without introducing additional biases—might provide a more consistent method for distance representation. Specifically, the current approach uses uneven bin sizes, which could lead to over- or under-representation of certain distance ranges, potentially skewing the model's learning process. A more rigorous justification for the chosen binning strategy, or an exploration of alternative, more uniform binning methods, would strengthen the methodology.
-  The authors mention that “the model is first trained on solely generating the protein structure for 40k steps.” In this phase, is ligand information completely omitted, or is it set as specific input information? Further details on the full training process would be beneficial. It's unclear how this initial training phase affects the subsequent conditional generation of protein-ligand complexes. Specifically, does the model learn any implicit biases towards certain protein structures during this phase that might influence its ability to generate diverse protein binders later on? A clearer explanation of the data used during this phase, and how it differs from the second phase, is needed.
- The paper indicates that, during training, the FAPE loss is divided into protein-protein interaction, protein-ligand interaction, and ligand-ligand interaction components. However, these three losses are not directly introduced or explained in detail. Could the authors elaborate on the definitions of these three loss components and how they are calculated? The lack of clarity on how these loss components are weighted and combined makes it difficult to assess the impact of each on the overall training process. A detailed breakdown of the FAPE loss, including the specific equations used for each component, is necessary for a thorough understanding of the model.
- The paper appears to lack ablation studies that could support certain design choices in the model. For instance, what impact would removing the first phase of training (the 40k steps on protein structure generation only) have on model performance? Additionally, how were the initial training and fine-tuning parameters in the second training phase determined, and what criteria guided the transition steps? Without these ablation studies, it's difficult to ascertain the necessity of each design choice and whether the model's performance is robust to changes in the training strategy. For example, the specific learning rates, batch sizes, and optimization algorithms used in each phase should be explored, and the impact of these choices on the final model performance should be quantified.

### Questions
- As I mentioned in the weakness, I hope the author can add some ablation experiments to demonstrate the effectiveness of some training strategies used in the paper.
- The author can provide a more detailed explanation of the composition of the loss in Section 4.4. I haven't seen relevant information in the appendix yet.

### Soundness
3

### Presentation
4

### Contribution
3
