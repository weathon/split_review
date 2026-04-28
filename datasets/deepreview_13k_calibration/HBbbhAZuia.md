# DockedAC: Empowering Deep Learning Models With 3D Protein-ligand Data For Activity Cliff Analysis

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
Artificial intelligence has become a crucial tool in drug discovery, excelling in tasks such as molecular property prediction. An activity cliff, which refers to a minor structural modification to a molecule resulting in a large change in its biological activity, poses a challenge in predictive modeling. The activity cliff depends on the interaction between the target and the ligand, which is however largely overlooked by previous ligand-centric studies. In this paper, we introduce DockedAC, a new dataset incorporating the protein target and target-ligand 3D complex structure information for studying the problem of activity cliffs. By matching protein binding information and ligand bioactivity, we employ molecular docking to generate the complex structure for each activity value. The DockedAC dataset contains 82,836 activity data on 52 protein targets with activity cliff annotations, which serves as the first step towards activity cliff research with large-scale 3D complex structures. We benchmark the dataset with traditional machine learning and deep learning approaches.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces dockedAC, a dataset that leverages molecular docking to generate complex structures associated with each activity value. The dataset incorporates 3D complex structure information, facilitating in-depth study of activity cliffs.

### Strengths
The paper is well-written and easy to understand.
The 3D structural information of molecular complexes is crucial for addressing cliff tasks, as varying interaction patterns can significantly impact affinity values. Previous methods for modeling activity cliffs typically focus on feature extraction from the ligand molecule alone, neglecting the surrounding protein environment. 
The ablation study of the paper is extensive to reflect the differences between RSME and RMSE_cliff

### Weaknesses
For ECFP, what proportion of samples have an ECFP similarity > 0.9, given that similarities > 0.5 are already quite rare?
In pairs of activity cliffs with docking conformations, what noticeable differences exist in their 3D structures? It has not been verified whether docking conformations can accurately capture the true differences in interaction patterns.
Can generated 3D docking conformations, which may differ from the crystal structures, reliably reflect the actual interaction differences between activity cliffs?
In Section 4.3, would training on bioactivity values (pKi/pEC50/pIC50 in log units) together pose any issues?
In Figure 4, although the 3D approach shows a higher RMSE difference and RMSE correlation, the performance gains from the additional 3D complex information are not very significant.
In Table 2, traditional methods (KNN, RF, SVM, etc.), even when only modeling the ligand, still achieve better results, indicating no clear advantage of using 3D complex data.
Overall, I believe that 3D complex structures are valuable for addressing activity cliffs. However, the current 3D complex methods evaluated in this paper, when compared to ligand-only approaches (such as ECFP and 2D graphs), have not shown significant improvement and still fall short of traditional ECFP-based methods. The reasons for this lack of improvement are not quantitatively analyzed, and there is also no evaluation of the quality of docking data to ensure it captures the critical information within activity cliffs.

### Questions
See weakness

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
**Summary:** The authors present DockedAC for comprehensive machine learning of molecular activity cliffs.

**Recommendation:** I am currently recommending a weak (yet optimistic) reject.

**Rationale behind Recommendation:** If the authors can clarify their dataset splitting approach and potentially benchmark one or two more recent 3D GNN/transformer architectures, I will consider raising my score.

### Strengths
- The authors' experiments and conclusions are thorough and informative. I appreciate the correlation studies for the insights they provide into the potential of 3D GNNs in this problem domain.
- The authors' benchmark is well-constructed overall.
- The authors' data and benchmarking code is thoroughly documented.

### Weaknesses
 - The authors need to clarify the splitting of their dataset to ensure proper benchmarking (see "Questions" below).
- The authors' chosen 3D GNNs (or 3D/equivariant transformers, which in my view may be most interesting to explore for this problem) are not up-to-date. For example, new models such as the Equiformer v2 architecture [1] could be included as well. The current selection of models limits the scope of the benchmark and may not reflect the state-of-the-art in 3D molecular representation learning.
- The authors should consider performing flexible docking with conventional docking algorithms rather than "fixed-protein" docking, since the amino acid side chain rotamer states in a crystal protein structure may be conducive to only the ligand against which the protein was originally bound [2]. This could introduce a bias in the benchmark, as the docked poses might not accurately reflect the true binding conformations for novel ligands. I understand this may be computationally expensive, but perhaps the authors can perform small-scale experiments at some point to see if this makes a difference in the final benchmarking results.

### Questions
- On line 198, how is a canonical SMILES string determined for each pair of ligands?
- On line 213, when are two binding sites considered the same? Do you use a distance-based metric here? Please explain in more detail.
- On line 227, what does "docking results are reviewed" mean? Do you simply mean that you reject ligands that achieved a docking score greater than or equal to zero? Or did you manually apply some other heuristic to reject ligands at this stage?
- Regarding line 234, could the authors provide more detail about why they split the dataset this way? I ask because it's not clear to me how this splitting strategy would prevent models from overfitting to popular protein targets such as GPCRs if they are widely represented in the dataset. Perhaps I'm misunderstanding how the authors trained their baseline methods on this dataset (e.g., maybe they only trained on one protein at a time, an approach which seems difficult to scale), but it's important for the authors to more clearly explain their design and rationale for this proposed dataset splitting strategy (since their results suggest 3D GNNs perform well in certain contexts, where they might be overfitting to the crystal protein structures in the dataset).
- More of a suggestion: Drawing a downward arrow next to 5.4 nM in Figure 1 could inform readers unfamiliar with bioactivity measurements that a lower quantity is better in this context.

### Soundness
2

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work introduces the new benchmark dataset including Activity Cliffs (AC), which holds significant importance in quantitative structure-activity relationship (QSAR) analysis.
Authors collect the bioactivity data from ChEMBL, refine the collected molecules, find the AC relationships in the dataset, and construct 3D conformer dataset using docking.
Finally, authors investigate the regression performance of various ML and DL methods and demonstrate that the 3D spatial information helps to distinguish ACs.

### Strengths
1. Authors include various ML, DL methods for benchmarking.
2. The curation process is clear and well-organized to understand.
3. Unlike previous datasets, DockedAC includes 3D conformers which play crucial roles in protein-ligand interaction.
4. They perform an ablation study to investigate the 3D conformational information. (Appendix B)

### Weaknesses
 **Issue 1.**
I believe that a benchmark set like DockedAC, which focuses on metrics relevant to the application domain, its value is evaluated by how effectively it can assess the performance of different methodologies used in the field (e.g., PoseCheck [1], DUD-E [2]).
In this light, I think this AC-focused benchmark can be used as a rigorous and meaningful test set for various 3D protein-ligand interaction prediction model, which have been in development for a long time.

Therefore, I wonder why authors do not include evaluations for popular 3D binding affinity prediction models (e.g., PIGNet [3], RTMScore [4], TANKBind [5], DSMBind [6], KarmaDock [7]).
Similar to how DUD-E serves as a virtual screening benchmark, the authors could evaluate these models by using the entire collected dataset as a test set.
Although the authors included IGN and SS-GNN, which are 3D binding affinity prediction models, they trained these neural networks on their own training set.
I suggest evaluating the activity cliff prediction performance of some of state-of-the-art models [3-7] trained on general binding affinity dataset (e.g., PDBbind) using the DockedAC benchmark set.

**Issue 2.**
The 3D conformer sets are generated through a single GPU-accelerated docking using AutoDock Vina scoring. Since the binding conformations are crucial for identifying protein-ligand interactions, and I concerned that the performance of the 3D DL model may be constrained by the quality of the conformers. It would be beneficial to include the diverse conformers computed by various docking tools employing different scoring functions, such as conventional docking (Smina, AutoDock Vina, Quick Vina, GLIDE) or deep learning-based docking (KarmaDock, DiffDock).

### Questions
1. Could you please clarify whether the 3D DL methods are trained on the entire training set using a single model that is generalized to pockets (target-conditioned) or are they trained for each target pocket (target-specific)? Additionally, what are the target DL methods of this benchmark? Neural network architecture (e.g., EGNN or MPNN) or trained 3D DL models which is generalized to different proteins? (e.g., PIGNet, KarmaDock.)
3. I wonder why empirical scoring function of AutoDock Vina is not included as the baseline.
4. As I understand it, the ligands are docked to the single rigid protein binding site structure. To reflect the protein’s flexibility, it would be helpful to consider multiple protein structures, i.e., run docking with multiple protein structures for each ligand.

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
4

### Summary
An activity cliff (AC) refers to cases where structurally similar ligands exhibit significantly different activity values due to interactions between protein targets and ligands. Benchmark datasets for ACs have been limited. While existing large datasets consist only of 2D information, they fail to consider 3D interactions. In this context, this work creates a new dataset that adds 3D information which previous AC data could not cover. The purpose and methodology are sound, but there’s a lack of analysis on whether the data classified as activity cliffs genuinely represent real AC relationships. Additionally, there’s no mention of the diversity of conformations generated by docking, and some analyses are not straightforward.

### Strengths
**S1**: The authors collected significantly more AC data than previously available high-quality AC datasets[1,2,3] through binding affinity data curation for various protein targets and species.

**S2**: Based on the importance of considering 3D information in target-specific AC prediction, the authors generated pseudo-binding structures using molecular docking, overcoming limitations of 2D-only AC data.

**S3**: The authors benchmarked their dataset using various models, providing many baselines.

## References
[1] Wang, Lingle, et al. "Accurate and reliable prediction of relative ligand binding potency in prospective drug discovery by way of a modern free-energy calculation protocol and force field." Journal of the American Chemical Society 137.7 (2015): 2695-2703.

[2] Schindler, Christina EM, et al. "Large-scale assessment of binding free energy calculations in active drug discovery projects." Journal of Chemical Information and Modeling 60.11 (2020): 5457-5474.

[3] Pecina, A., Fanfrlík, J., Lepšík, M. et al. SQM2.20: Semiempirical quantum-mechanical scoring function yields DFT-quality protein–ligand binding affinity predictions in minutes. Nat Commun 15, 1127 (2024).

### Weaknesses
 **W1**: It appears that the authors directly followed the definition from existing work. In the definition of activity cliff in Section 3.2, all criteria seem to *implicitly* consider the structural similarity of molecules. Is there any reason not to consider explicit structures such as Maximum Common Substructure (MCS)? If computational complexity is a concern, it would be more impactful to check the distributions of number of shared and different atoms between newly created AC data pairs with MCS.

**W2**: Since the structures are generated through docking, it’s challenging to obtain the correct global minimum structures (as mentioned in the limitations). Providing multiple local minimum structures might be beneficial, but those information are not exist in the current manuscript.

**W3**: Some analyses about dataset is not straightforward. (see Q2-5)

**W4**: Several recent models[1,2,3] aiming versatile predictions for protein-ligand interaction (doing both virtual screening and scoring on acitivity-cliff data) also used well-curated activity cliff data[3,4]. The authors might include these works in related works or further do benchmarks on these models to enlarge the impact of this work.

### Questions
**Q1**: Sections 3.2 and 3.5 seem identical to previous work[1]. Shouldn’t this be acknowledged or cited appropriately?

**Q2**: In Section 5.1, when correlating RMSE with RMSE-cliff, is there a potential for bias introduced by comparing AC data with the entire dataset (which includes both AC and non-AC data)?

**Q3**: Conceptually, using 3D information should improve AC prediction. However, deriving this conclusion in section 5.1 from the results comparing IGN[2] and other 2D models seems to lack depth in interpretation. It would be better to compare IGN with a 2D version of IGN to minimize bias.

**Q4**: In Section 5.3, is the sample size too small for calculating the p-value? Additionally, in Table 3, the percentage of AC is at most 0.6%. Why did the authors choose to show the correlation with a maximum AC data percentage of only 0.6%?

**Q5**: In Section 5.4, ECFP shows the best performance. Could this be because ECFP was used in the criteria when dividing the data? Is there a potential ECFP bias? How do the results look if the authors use the other fingerprints for dividing data instead of ECFP?

## References
[1] Van Tilborg, Derek, Alisa Alenicheva, and Francesca Grisoni. "Exposing the limitations of molecular machine learning with activity cliffs." Journal of chemical information and modeling 62.23 (2022): 5938-5951.

[2] Jiang, Dejun, et al. "Interactiongraphnet: A novel and efficient deep graph representation learning framework for accurate protein–ligand interaction predictions." Journal of medicinal chemistry 64.24 (2021): 18209-18232.

### Soundness
3

### Presentation
3

### Contribution
3
