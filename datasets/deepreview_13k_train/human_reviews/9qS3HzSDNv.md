# Integrating Protein Dynamics into Structure-Based Drug Design via Full-Atom Stochastic Flows

- Decision: Accept
- Scores: 6, 6, 6, 8, 5

## Abstract
The dynamic nature of proteins, influenced by ligand interactions, is essential for comprehending protein function and progressing drug discovery. Traditional structure-based drug design (SBDD) approaches typically target binding sites with rigid structures, limiting their practical application in drug development. While molecular dynamics simulation can theoretically capture all the biologically relevant conformations, the transition rate is dictated by the intrinsic energy barrier between them, making the sampling process computationally expensive. To overcome the aforementioned challenges, we propose to use generative modeling for SBDD considering conformational changes of protein pockets. We curate a dataset of apo and multiple holo states of protein-ligand complexes, simulated by molecular dynamics, and propose a full-atom flow model (and a stochastic version), named DynamicFlow, that learns to transform apo pockets and noisy ligands into holo pockets and corresponding 3D ligand molecules. Our method uncovers promising ligand molecules and corresponding holo conformations of pockets. Additionally, the resultant holo-like states provide superior inputs for traditional SBDD approaches, playing a significant role in practical drug discovery.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
Summary: 
1. This paper tackles the problem of flexible proteins in small molecule structure based drug discovery to account for protein's conformational changes during binding. 
2. The authors propose a full-atom model based on continuous flow matching for pocket residues' translation, rotation, torsional angles and ligand molecule's atom position) and discrete flow matching for atom and bond types of ligand molecules. 
3. They finally present a stochastic version of their flow matching objective for increased robustness.

### Strengths
Strengths:
1. The protein flexibity problem is critical in drug discovery with no good computationally efficient insilico methods. Hence, the proposed method (if works as advertised) could be paradigm shifting. 
2. The flow matching components in the paper are generally well explained. 
3. The structural features of protein and ligands are carefully considered and appropriately modeled.

### Weaknesses
Weaknesses:
1. I have concerns about the reproducibility of this work with no code or the curated dataset (mentioned as a key contribution) not provided. Moreover access to the code would have helped understanding the complex workflow in the paper better. 
2. In table 2, where are the results for dynamic flow?
3. In figure 1, what are protein and ligand embeddings, where are they computed in the proposed workflow and how are they being used in complex graph and ligand graph respectively? Given the number of components in the workflow, I would suggest including an aggerated workflow figure with end to end pipeline starting from the apo state input to the molecule and holo state output, complete with the final flow matching loss. 
4. The overall loss for this work is unclear, while individual losses for structural features for protein and ligand are provided, how are they aggregated is not mentioned. 
5. Hyperparameter and other architectural details are also not provided.

### Questions
I found certain parts of the paper difficult to follow. Particularly in section 3.4, the details of  each of the $\phi_i$ are mising. Are they all EGNNs? I also struggled to understand how this parametrization relates to the final flow matching objective to be used. Furthermore, some parts in this section feel hand-wavy. For example, how were the hidden states used to predict atom positions and atom/bond types. Similarly in residue-level transformer, L412, final updated frames were used as predictions - for what? It was again unclear how torsion angles were predicted based on final residue level hidden states.

### Soundness
2

### Presentation
2

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
The authors propose a new dataset of apo/holo proteins and a new model to solve the mapping task between apo protein pockets and holo protein pockets/ligand complexes.

### Strengths
- A new dataset derived from the MISATO dataset and AlphaFold Protein Structure Database, which includes 5,692 complexes with 46,235 holo-ligand conformations and corresponding apo structures.
- A new task to map apo protein pockets to holo protein pockets/ligand complexes.
- A new generative model, DynamicFlow, with a stochastic variation, which is based on the combination of discrete and continuous Flow Matchings, that simultaneously generates a ligand and adjusts a protein pocket.

### Weaknesses
 - The dataset collection process is not very clear; see the questions below.
- The dataset is simulational, which makes it less representative than the PDB.
- The paper lacks the baselines for joint pocket and ligand generation or the motivation for their absence  [1, 2, 3, 4].
- The evaluation pipeline seems unfair and may be misleading: baseline models are designed to work with holo-state pockets, whereas, in the experiment, they are utilized to generate ligands for apo-state pockets.
- Unlike the baselines, DynamicFlow-generated ligands are evaluated inside the generated pockets, which also affects the comparison. From our point of view, a valid way to compare different settings for baselines and DYNAMICFLOW is to use MD trajectories-based methods, such as MMPBSA [5].
- Moreover, the fact that a ligand binds well to a generated pocket may not imply that the real affinity is good. The validity of the generated pockets is not assessed. For example, the AF PLDDT may be used. 
- Table 2. shows that the diffusion methods work better for the ligand prediction given the generated pocket than the proposed model itself, which increases the concern about the lack of comparison of the model’s architecture with the other known models


### Questions
## Questions and remarks
1. How did you transition from 19437 proteins to 16972 complexes? How are ligands selected, and why was the original number of proteins reduced?
2. What does "100-frame" mean? Every 100th frame of the MD trajectory? Or 100 frames from each MD simulation? If the second is true, how were the 100 frames selected from the MD trajectory?
3. Do you filter the protein-ligand complexes depending on the average RMSD throughout the trajectory? Please explain Figure 10 b.
4. Please add the DynamicsFlow models to Table 2 for easier comparison.
5. FREED [6] and FREED++ [7] are not cited.
6. Line 214: string repetition.
7. line 848: mistake (are can).

## Closing remarks

Overall, I find the paper important for drug design. The idea that the pocket changes upon the introduction of the ligand is well physically motivated. The generative model itself is impressive, as it combines various flow-matching modules. However, the experimental evaluation raises serious concerns about the validity of the comparison with the baselines. I would consider raising my score if the authors propose a better evaluation strategy or resolve concerns with the current evaluation.

[1] Zhang, Z., Lu, Z., Zhongkai, H., Zitnik, M., & Liu, Q. (2023). Full-atom protein pocket design via iterative refinement. Advances in Neural Information Processing Systems, 36, 16816-16836.

[2] Gao, B., Jia, Y., Mo, Y., Ni, Y., Ma, W. Y., Ma, Z. M., & Lan, Y. Self-supervised Pocket Pretraining via Protein Fragment-Surroundings Alignment. In The Twelfth International Conference on Learning Representations.

[3] Nakata, S., Mori, Y., & Tanaka, S. (2023). End-to-end protein–ligand complex structure generation with diffusion-based generative models. BMC bioinformatics, 24(1), 233.

[4] Huang, L., Xu, T., Yu, Y., Zhao, P., Chen, X., Han, J., ... & Zhang, H. (2024). A dual diffusion model enables 3D molecule generation and lead optimization based on target pockets. Nature Communications, 15(1), 2657.

[5] Wang, E., Sun, H., Wang, J., Wang, Z., Liu, H., Zhang, J. Z., & Hou, T. (2019). End-point binding free energy calculation with MM/PBSA and MM/GBSA: strategies and applications in drug design. Chemical reviews, 119(16), 9478-9508

[6] Yang, S., Hwang, D., Lee, S., Ryu, S., & Hwang, S. J. (2021). Hit and lead discovery with explorative rl and fragment-based molecule generation. Advances in Neural Information Processing Systems, 34, 7924-7936.

[7] Telepov, A., Tsypin, A., Khrabrov, K., Yakukhnov, S., Strashnov, P., Zhilyaev, P., ... & Kadurin, A. FREED++: Improving RL Agents for Fragment-Based Molecule Generation by Thorough Reproduction. Transactions on Machine Learning Research.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes Dynamic Flow, a flow-matching-based method designed for structure-based drug discovery (SBDD) with a focus on protein flexibility. Specifically, Dynamic Flow models the mappings between apo (unbound) and holo (bound) protein conformations, as well as between an ideal normal distribution and the actual ligand conformation distribution. To effectively train the model on meaningful mappings between apo and holo conformations, the authors introduce a new dataset that includes molecular dynamics (MD)-modeled apo-holo protein conformations paired with ligand conformers.

### Strengths
1) The curated dataset, where each apo protein pocket is mapped to multiple holo pockets, is novel and well-suited for the SBDD task involving protein flexibility.
2) The paper is clearly written and supported by well-designed figures, which enhance comprehension of the proposed method.

### Weaknesses
1, The curated dataset in the paper is slightly different from the commonly used benchmark dataset in SBDD which are bindingMOAD and crossdock2020 and also the datasize is smaller compared with those two, I’m curious why not start with crossdock2020 and BindingMOAD before moving into new dataset?

2, About baseline: As far as I know, there is another work on SBDD with protein flexibility via flow matching that published or submitted ahead of this work FlexSBDD[1] on Neurips 2024, I would suggest author to benchmark with their number on vina results and illustrate the novelty and improvement compare with this previous work.

3, The paper lists “atom-level SE(3)-equivariant geometrical message-passing layers and residue-level Transformer layers” as contributions; however, there is no ablation study showing the impact of these architectural changes on model performance. Providing an ablation to assess their effects on sample quality (e.g., Vina score) or computational efficiency (e.g., FLOPs) would strengthen the evidence of these improvements.

### Questions
I was wondering, how did the author select the 50 test pockets other than having no overlap with the training set? Are they uniformly sampled from the whole dataset

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Authors developed the 3D pocket conditioned generative model, named DynamicFlow, for small molecule drug discovery. Compared to existing 3D generative models that require HOLO pocket structures, the proposed model can generate protein-ligand binding HOLO structures from the APO protein structure predicted by protein structure prediction models such as AlphaFold.

### Strengths
1. The authors extend the 3D structure-based ligand binder design problem to an Apo pocket structure setting.
2. They demonstrate that the predicted protein Holo structures can be utilized as input structures for existing 3D molecular generation models.
3. The authors perform not only docking but also non-covalent interaction analysis. This will likely serve as a desirable experimental analysis design for future 3D molecular generation model works.

### Weaknesses
 **Overall comment.**

The authors effectively address protein flexibility relative to small molecules using state-of-the-art flow matching techniques.
I'm not very interested in the 3D molecular generative models due to its unproven practicality; however, setting this bias aside, I consider this paper an important milestone in this field. However, questions remain regarding the quality of generated samples and the real-world applicability of the proposed methodology.

* The issues are sorted in the order they appeared in the manuscript.*

**Issue 1: Bias in the training data.** Page 8. Section 4. Data curation.

This work relies on training datasets constructed from MD simulations, which may lead the model to learn the simulated physics of MD rather than capturing real-world structural distributions. While various 3D generative models [1-2] utilized simulation datasets (e.g., CrossDocked2020), I think it would be a minor issue. For future work, authors might consider leveraging true experimental datasets PDBbind [3] to enhance reliability [4].

**Issue 2: Bias in the predicted pocket structure selection for analysis.** Page 9. Table 2, Page 10 Figure 6.

In the paper, authors selected the pocket structure ("our pocket") among the predicted pocket conformations based on Vina score, so the distribution of selected structures is biased from the training dataset. I suggest adding the analysis about randomly selected conformations, too. If the performance of SBDD methods (Table 2) or Volume distribution (Figure 6) are similar when using true holo structure and randomly selected structure, this would be strong evidence that the model has learned the distribution of holo structures.

**Issue 3: Questions about applicability in real-world applications.** Page 16. Line 835. "we locate residues within a cutoff distance of 7Å around each ligand and extract them from the 100-frame MD results."

As I understand it, this study define the pocket using the atom coordinate informations of known active binders in holo structures.
However, I wonder whether these pocket definitions are directly applicable to Apo protein structures generated in AlphaFold.
For high usability, the pockets should be easily defined, e.g., defining pocket using the center and radius (or box length) in an Apo structure.
This process has been used in existing 3D generative models [1-2], but this is because they do not account for the flexibility of the pockets.
If I misunderstood the process, let me know.

### Questions
1. **Page 8, Table 1.** The proposed models and baselines are distribution learning-based models. Therefore, QED, SA, Lipinski, logP should be similar to Reference ligands. (No $\uparrow$ or $\downarrow$.)
2. What is the generation time scale?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper curate a dataset of apo and multiple holo states of protein-ligand complexes, simulated by molecular dynamics, and propose a full-atom flow model (and a stochastic version), named DynamicFlow, that learns to transform apo pockets and noisy ligands into holo pockets and corresponding 3D ligand molecules. The experimental results seem to demonstrate that the model significantly improves the inputs for SBDD methods and enables the generation of ligand molecules with high binding affinity.

### Strengths
1. The results indicate that the proposed method is effective in enhancing the binding ability between ligands and proteins, with the Vina score reflecting a strong binding affinity.​
2. The concept of incorporating dynamic adaptability into drug design is uncommon in the existing literature and demonstrates a high level of originality.

### Weaknesses
1. The results pertaining to the main proposed evaluation algorithm appear to align with previous studies. Several algorithms referenced are well established in the literature. The authors should:

- Clearly specify which algorithms are original and unique to this study.

- Explicitly indicate which algorithms are derived from existing works, rather than from the authors' own proofs.

2. The paper employs various professional terms and abbreviations; however, the backgrounds and specific definitions for these terms are not adequately clarified. For example, the term "stochastic full-atom flow" within the model lacks a clear explanation of its exact meaning and implementation methods.
  
3. Regarding the dynamic adaptation of ligands and proteins, although relevant mathematical models are provided, there is a lack of essential intuitive explanations. Additionally, the logical relationships and technical details of certain steps are not distinctly articulated.

4. The analysis and treatment of different states (apo and holo) in the dataset are not sufficiently explored. Moreover, the specific reasoning behind the ratio of the various states (apo to holo) remains unclear.

5. There is a notable absence of baseline methods presented. It would be beneficial to consider comparing a broader range of graph-based generative models to conduct a thorough evaluation of the model's performance.
  
6. Reviews of computer science papers typically encourage the inclusion of anonymous code, accompanied by straightforward and easily testable data. Furthermore, it is recommended to incorporate a Jupyter Notebook, facilitating readers' understanding of the method presented.

### Questions
What challenges does this method have in dealing with protein flexibility? How can we learn from the direction of the solution?

### Soundness
3

### Presentation
3

### Contribution
3
