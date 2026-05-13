# Hotspot-Driven Peptide Design via Multi-Fragment Autoregressive Extension

- Decision: Accept
- Scores: 6, 6, 5, 6, 8

## Abstract
Peptides, short chains of amino acids, interact with target proteins, making them a unique class of protein-based therapeutics for treating human diseases. Recently, deep generative models have shown great promise in peptide generation. However, several challenges remain in designing effective peptide binders. First, not all residues contribute equally to peptide-target interactions. Second, the generated peptides must adopt valid geometries due to the constraints of peptide bonds. Third, realistic tasks for peptide drug development are still lacking.
To address these challenges, we introduce \textbf{PepHAR}, a hot-spot-driven autoregressive generative model for designing peptides targeting specific proteins. Building on the observation that certain hot spot residues have higher interaction potentials, we first use an energy-based density model to fit and sample these key residues. Next, to ensure proper peptide geometry, we autoregressively extend peptide fragments by estimating dihedral angles between residue frames. Finally, we apply an optimization process to iteratively refine fragment assembly, ensuring correct peptide structures.
By combining hot spot sampling with fragment-based extension, our approach enables \textit{de novo} peptide design tailored to a target protein and allows the incorporation of key hot spot residues into peptide scaffolds. Extensive experiments, including peptide design and peptide scaffold generation, demonstrate the strong potential of \textbf{PepHAR} in computational peptide binder design.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces PepHAR (Hotspot-driven Autoregressive peptide design), a novel three-stage approach for designing peptides that can bind to specific target proteins. The method acknowledges the critical role of "hot spot" residues in peptide-protein binding and addresses key challenges in computational peptide design. The three stages consist of: (1) a founding stage that uses an energy-based density model to identify and sample key hot spot residues, (2) an extension stage that autoregressively builds peptide fragments from these hot spots using a dihedral angle-based approach ensuring proper geometry, and (3) a correction stage that refines the complete structure through optimization. The authors also introduce a new "scaffold generation" task that better reflects real-world peptide drug development scenarios. When compared to state-of-the-art baselines (RFDiffusion, ProteinGenerator, PepFlow), PepHAR demonstrates superior performance across multiple metrics including structural validity, geometric accuracy, binding site accuracy, and novelty/diversity of generated peptides, while maintaining competitive stability and binding affinity.

### Strengths
- Novel Problem Decomposition: The work introduces a clever way to break down peptide design into a three-stage process based on biological understanding. By focusing on hot spot residues first, then extending and refining, it makes the problem more tractable while maintaining biological relevance.


- Strong Geometric Constraints: The method explicitly handles peptide bond geometry through dihedral angles. Uses von Mises distribution (and others) to model angle distributions properly.

- Novel Energy-Based Density Model: Introduces an innovative energy-based model to identify hot spot residues. Uses noise contrastive estimation for effective training without needing explicit normalization. Employs Langevin dynamics sampling to efficiently explore the residue distribution space.

- Autoregressive Fragment Extension: Enables bidirectional growth from hot spots through Left/Right operations


- Hybrid Optimization Framework: Creates a novel joint optimization objective combining backbone and dihedral constraints. Introduces an iterative refinement strategy that can handle multiple fragments simultaneously

### Weaknesses
Overall, this work is well written with clear logic and reasonable benchmarks.

1. Many recent works of peptide binder design use AlphaFold2 for scoring (e.g., pAE or iptm). I would like to see the evaluation of designed peptides with such metrics.

2. Regarding Novelty score, can author also show separate metrics for it in supplementary as well: TM-score and sequence identity.

3. For all examples provided, I will suggest authors to also provide the peptide sequence for reference for better understanding.

4. To enhance further the evaluation and discussion, I would suggest authors to include following works for discussion and potentially use them for benchmarking as well.

[1] EvoBind: https://www.biorxiv.org/content/10.1101/2022.07.23.501214v1 (Discussed, but not benchmarked?)

[2] EvoBind2: https://www.biorxiv.org/content/10.1101/2024.06.20.599739v2

[3] PepMLM: https://arxiv.org/abs/2310.03842

[4] EvoPlay: https://www.nature.com/articles/s42256-023-00691-9

[5] AlphaProteo: https://arxiv.org/abs/2409.08022 (very recent)

[6] MASIF: https://www.nature.com/articles/s41592-019-0666-6

### Questions
Major:
1. For different sampling K values, does the binder length remain constant for the same target protein?

2. RMSD might be somewhat misleading since peptides can still bind effectively with very different geometries, which is actually desirable - valid binders that show different binding modes from native ones.

3. Regarding Novelty, especially for sequences, what is the source of this novelty? Does it primarily come from scaffold sites or contact sites? If changes are mainly in scaffold sites compared to native ones, this metric might be misleading and trivial for a designed binder.

4. In the Dataset section, the binding pocket is defined using a 10Å radius, while for BSR in the supplementary material, binding sites are defined using a 6Å radius. Why are different values used?

Minor:
1. Authors should specify that they are performing peptide binder design, not peptide design, as these are distinctly different tasks.

2. In the Dataset section (Lines 276-377), please clarify the distinction between the 158 examples and the 8,207 additional examples.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a method for peptide sequence and structure generation for peptide design with target protein. The methodology includes three parts: the hot-spot residue generation, the autoregressive generation of fragments based on the hot-spot residues to complete the chain, the correction stage that refine the peptide structure. Experiments have been performed on the peptide design and peptide scaffold generation tasks, and compared with baseline models like RFdiffusion, Pepflow, and demonstrate good performance in novelty and diversity, but not as good in the validity or quality of the generated structures.

### Strengths
- The methodology is novel, which divide-and-conquer the peptide design task into three stages: hot-spot residue generation, fragment completion and correction.
- Utilizing the information of hot-spot residues helps to improve the generation quality
- Experiments have been performed on the curated dataset and benchmarks, with comprehensive metrics, and comparison with relevant models.
- The method achieves the highest novelty and diversity compared with different baselines.

### Weaknesses
 - The quality of the generated peptide is not good, on the metrics such as validity and stability the method is significantly worse.
- In the first stage, each hotspot generation is independent and do not consider other generated hotspot, or a joint generation. And in the second stage, the completion of each fragment only depends on the target protein and the generated residues of the current fragment. Not taking other hotspots or fragments into account in the two stages could make the model ignorant of important information for the geometry and validity.

### Questions
- In the correction stage, are the terms in J_bb only non-zero in those residues that stay at the connection of two fragments? Because other residues in the middle of the fragments should be complying with the consistency constraint from construction. The authors should clarify this.
- How does the correction method proposed in this work (using models directly from the first and second stages) compare with the correction by some empirical methods (like some energy function)?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces PepHAR, a hot-spot-driven autoregressive generative model for designing peptides targeted at specific protein binding sites. The authors propose a three-stage approach: 1) hotspot residue sampling using an energy-based model, 2) fragmented autoregressive extension of peptide structure using dihedral angles, and 3) correction through gradient-based optimization to ensure overall peptide geometry validity. Through experiments, PepHAR demonstrates competitive performance in scaffold-based peptide design, showing improvements in structure and binding accuracy when compared to state-of-the-art models like RFDiffusion and PepFlow on metrics including binding site overlap, novelty, and stability.

### Strengths
The paper attempt to solve an important protein design problem with significant biomedical applications.

The hotspot-driven approach combined with an autoregressive fragment assembly model is novel within peptide design, providing a unique perspective on addressing protein-peptide design problem.

The paper offers a detailed breakdown of the approach, supported by schematics and visualizations that help clarify the generation process.

The paper uses comprehensive metrics (e.g., validity, stability, affinity, diversity, novelty), which cover structural, energetic, and novelty aspects of peptide design.

### Weaknesses
 - The autoregressive fragment extension process might introduces cumulative geometric errors, especially for longer peptides.

-  Although PepHAR outperforms some baselines, the reported improvements are incremental and may not justify the added model complexity and limitations. For a conditional generation task, the primary metric is RMSD, which quantifies the structural similarity between the generated structures and native structures. where PepHAR is worse than the baseline PepFlow.

- The claim of the paper is purely using the frame representation for peptide might break the validity of the protein structures like bond formulation. However, Table 1 shows that RFDiffusion, which is a frame-representation-based method, exhibits higher Valid %.

- I would expect open source code to support the methodology and experimental results.

- Regarding the equation, the author should add period to the end if it closes a sentence. I notice that the author missed that in most of the equations in this paper.

### Questions
- I expect the author to quantify the impact of the cumulative errors from autoregressive generation. 
- Figure 4 shows the designed peptides are all loops. Given that, I wonder if the SSR % is still meaningful if most of the native and designed peptides are just loops. Because in that case, the model can just produce all loopy structures and get a very high SSR.
- I suggest that the author further design the sequences for those generated peptide structures using for example, ProteinMPNN and report the recovery rate. This could reflect the peptide structure quality since low-quality structures would result in low sequence recovery or low-quality sequences generated such as repetitions.

### Soundness
2

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
5

### Summary
The paper introduces PepHAR, a state-of-the-art generative model for peptide design. It employs an energy-based density model to precisely sample key residues, extends peptides with an autoregressive approach based on dihedral angle estimation, and refines fragment assembly through an iterative optimization process. The paper proposes a new experimental setting, scaffold generation, to mimic practical scenarios, and demonstrate the competitive performance of PepHAR in both peptide design and scaffold generation tasks.

### Strengths
- The paper innovatively integrates hotspot residues into peptide design, a concept well-supported by biological theories, enhancing the model's relevance and novelty in the field.
- The three-stage approach, including the use of dihedral angles and the correction stage, is a robust technical framework that ensures the generation of structurally sound peptides.
- The model demonstrates excellent performance in SSR, Affinity, Novelty, and Diversity, indicating its ability to produce high-quality, functional, and diverse peptides.

### Weaknesses
1. **Performance in Specific Metrics**: As shown in Section 5.1, Table 1, PepHAR underperforms RFDiffusion in the Valid metric by a significant margin (10%). This suggests that PepHAR may not always generate peptides with geometries that are fully consistent with the formation of peptide bonds, indicating potential issues with the model's ability to accurately represent the constraints of peptide bond geometry. Additionally, PepHAR's Affinity metric indicates room for improvement, potentially due to the density model's limitations in sufficiently approximating the complex energy landscapes involved in peptide-target interactions, particularly in capturing the subtle non-covalent interactions that contribute to binding affinity. The model's performance on the Stability metric also warrants further investigation, as it is crucial for practical applications.
2. **Limited Exploration in Scaffold Generation**: The scaffold generation scenario only considers a small number of hotspots (K=1, 2, 3), with baseline comparisons limited to K=3. This narrow exploration may not capture the full spectrum of possible hotspot configurations, potentially limiting the generalizability of the findings to more complex scenarios where the number and spatial arrangement of hotspots can vary significantly. The lack of a systematic study of how different hotspot configurations impact the performance of both PepHAR and baseline models makes it difficult to fully assess the method's robustness and adaptability.
3. **Density Model Limitations**: The energy-based density model used in PepHAR might not fully approximate the intricate energy landscapes of peptide interactions, which could impact the model's ability to generate peptides with optimal binding affinities. The current implementation may struggle with the high dimensionality and complex multi-modal nature of these energy landscapes, potentially leading to suboptimal sampling of peptide conformations and sequences. This limitation could be further exacerbated by the choice of energy function and training procedure, which may not be sufficiently expressive to capture the nuances of peptide-target interactions.

### Questions
1. In Section 5.2, Table 2, it would be insightful to see the performance of the baseline models under different conditions, specifically for K=1 and K=2, which are currently not included. Additionally, to thoroughly understand the influence of hotspot count on peptide design and the tradeoff with diversity mentioned in Section 5.3, it would be valuable to conduct experiments with a broader range of K values, or explain the insights behind the choice of these values.
2. The current study employs RFDiffusion and PepFlow as baseline models. Given the recent advancements in diffusion or flow-based peptide design, it would be valuable to include additional baseline models such as PepGLAD
3. Why does PepHAR underperform RFDiffusion and PepFlow in metrics such as valid% and RMSD, and what is the tradeoff involved?
4. The paper mentions tasks such as HIV-1+CD4 and p53+MDM2 interactions, which are known for their hotspot-mediated binding. It would be beneficial to see PepHAR's performance demonstrated on these specific systems.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors present a novel de-novo peptide design method, PepHAR, aimed at generating binders for specific sites on a target protein. The method leverages the concept of "hotspots", a small number of residues at protein-protein interfaces that contribute most of the binding energy, with other residues acting as "scaffolds" to stabilize the interface. PepHAR’s peptide prediction process is based on three main components: (1) A neural network trained using a noise contrastive estimation (NCE) loss to differentiate between real interface residues (ground truth) and noisy counterparts altered with spatial perturbations. The authors use Langevin dynamics to sample from this energy-based model. (2) A second neural network that builds a polypeptide chain autoregressively by predicting the phi-psi dihedral angles for each subsequent residue. This model, trained using maximum likelihood estimation (MLE), predicts angles for residues extending either direction along the chain. (3) A final correction step to refine the predicted peptide structures, addressing minor inaccuracies like dihedral angle errors, steric clashes, or chain breaks. This stage optimizes dihedrals based on neighboring residues and rebuilds the peptide, comparing it to the initial prediction. An objective function minimizes the distance between the rebuilt and predicted structures while ensuring angles align with the learned dihedral distribution.
PepHAR was evaluated for de-novo peptide generation with up to three hotspots, comparing favorably to other leading methods like RFdiffusion, PepFlow, and ProteinGenerator. An ablation study also confirmed the significance of each method component. Overall, PepHAR generated peptides with lower RMSD to the native structure than other methods, showing its effectiveness in autoregressively designing peptides for target protein interfaces.

### Strengths
The paper is well-written, with ideas and concepts clearly explained. Given the ongoing challenges in de-novo peptide binder design, this novel and original approach is both relevant and significant. I especially appreciated the clear presentation of the derivations and fundamental principles underlying the neural network design and training.

### Weaknesses
The paper is well-written, with few notable weaknesses.

### Questions
I have two minor questions, primarily out of curiosity:

(1) In the benchmarks where PepHAR was tested, could you provide more insights into the nature of the predicted structures? For instance, do the predictions tend to cluster around helical bundles, or is there a broader range of conformations? Additionally, are the k=3 hotspots located within disordered regions, or are they typically in helices, where the backbone might be easier to infill? I would suggest to include a brief analysis of the secondary structure composition of the generated peptides and compare it to native structures (or a representative set of native structures), as well as an examination of where the hotspots tend to be located in terms of secondary structure elements.

(2) When multiple hotspots are specified, fragments are grown from each hotspot. How does the network ensure that these initially disconnected fragments will eventually fit together? Is this addressed during the extension phase or in the polishing stage? Furthermore, is there a risk that extended chains from different fragments might fail to converge into a closed structure? It could be useful to elaborate on the fragment assembly method, and add statistics on how often fragments successfully connect and if there are any strategies used to ensure proper assembly or safeguard this process.

### Soundness
4

### Presentation
3

### Contribution
4
