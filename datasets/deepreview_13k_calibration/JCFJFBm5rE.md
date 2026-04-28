# SurfDesign: Effective Protein Design on Molecular Surfaces

- Decision: Reject
- Avg Score: 6.40
- Scores: 8, 8, 5, 5, 6

## Abstract
Structure-based inverse folding has been extensively explored in recent years. In contrast, surface-conditioned protein generation is still an under-explored area. Molecular surfaces characterized by a compact and smooth composition of atoms at their boundary hold a more direct relevance to biomolecular interactions and function.
In this work, we introduce a novel framework named SurfDesign with several key improvements. Firstly, considering the theoretical fact that the molecular surface is a continuous manifold with infinite resolution, we propose surface-based equivariant message passing (SEMP) to incorporate the normal vector and curvatures and get aware of the manifold's Euclidean locality. Besides, a hybrid parameter-efficient fine-tuning (PEFT) technique is employed to combine the knowledge of protein language models (PLMs) with the surface geometric encoder. We extensively evaluate SurfDesign on the CATH, TS50, TS500, and PDB datasets, achieving an average recovery of more than 70\%.  Our work opens another road to designing functional proteins, underscoring the importance of including surface attributes in conventional inverse folding.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In this work the authors seek to address a longstanding challenge in functional protein design by augmenting inverse protein modeling with continuous surface representations. To this end, they present SurfDesign, a model trained on surface manifolds, augmented with their surface-based message passing scheme and knowledge from published PLMs. The generated sequences are evaluated on CATH 4.2 and 4.3 test sets, including short (less than 100AAs), and  single-chain ablations. Further, proteins are evaluated in a multi-chain setting using PDB structures, and on zero-shot generalization to unseen proteins on a held out test set. SurfDesign is superior on all benchmarks. The authors also evaluate the model on structure recovery, and providing scaling data, which align with prior PLMs.

### Strengths
The inverse design method proposed in this work seems to be powerful and promising. The authors perform an exhaustive set of benchmarks where they rank best against strong baselines, including another surface-based method. The formulation is intuitive and straightforward and appears to significantly improve sequence design.

### Weaknesses
 The main biological significance of this method would to be in using a surface-based method to design stronger protein-protein interacting systems, however demonstration of the model in this application (even via in-silico metrics, and an exemplary binder problem) seems to be missing.

- Line 89 What does O optionally, mean? Is it included in the backbone representation or not? 
- How is $h_i$ computed, the description reads “such as hydrophobicity, hbond, and charge”. The "such as" description is not specific. 
- It would be interesting to further explore the models performance on heterogeneous and homogeneous multi-chain complexes, examples of both are in the PDB database. 
- Line 423 I believe Figure3.3 should say Figure 4 here. 
- It would be nice to expand Figure 4 to include exposed vs buried, helical vs sheet vs loop/turn, for completeness and possibly some metrics of hydrophobicity and electrostatics. 
- Table 5 – should the row MoE-DSR be SurfDesign, based on the accompanying text? Otherwise MoE-DSR is not defined in the text anywhere 
- The section on surface isomers feels incomplete, and I couldn’t find accompanying information in the appendix.
    - What experiment was done? 
    - Were only 2 lysozyme isomers compared?
    - Do the isomers have different amino acid sequences? if so how different are they. 
    - How structurally different are the isoforms (backbone RMSD), and what are the conditions under which they were crystalized (are ligands or ions present in either crystal structure?). 
    - What is the biological significance of designing sequences that are robust to structural isomers

### Questions
- Line 89 What does O optionally, mean? Is it included in the backbone representation or not? 
- How is $h_i$ computed, the description reads “such as hydrophobicity, hbond, and charge”. The "such as" description is not specific. 
- It would be interesting to further explore the models performance on heterogeneous and homogeneous multi-chain complexes, examples of both are in the PDB database. 
- Line 423 I believe Figure3.3 should say Figure 4 here. 
- It would be nice to expand Figure 4 to include exposed vs buried, helical vs sheet vs loop/turn, for completeness and possibly some metrics of hydrophobicity and electrostatics. 
- Table 5 – should the row MoE-DSR be SurfDesign, based on the accompanying text? Otherwise MoE-DSR is not defined in the text anywhere 
- The section on surface isomers feels incomplete, and I couldn’t find accompanying information in the appendix. 
    - What experiment was done? 
    - Were only 2 lysozyme isomers compared?
    - Do the isomers have different amino acid sequences? if so how different are they. 
    - How structurally different are the isoforms (backbone RMSD), and what are the conditions under which they were crystalized (are ligands or ions present in either crystal structure?). 
    - What is the biological significance of designing sequences that are robust to structural isomers

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes a new method to generate sequence of a protein conditioned on the surface descriptors. This paper proposes improvement to the surface description by incorporating two continuous tangent vectors in addition to the normal vector at each point on the surface (Darboux frame). Moreover, the constructed frame is continuous w.r.t the point on the surface (Eq. 3-4). Additionally authors propose equivariant message passing network based on 3D Spherical Fourier-Bessel decomposition of the previously constructed Darboux frames relative positions and orientations; the rest of the message passing graph NN follows standard design. Finally, authors use fine-tuning of pretrained protein language model as a sequence decoder.
The authors extensively test their approach on CATH-4.2, CATH-4.3 benchmarks. Additionally they tested their approach to multi-chain sequence recovery using Dauparas et al dataset. SurfDesing archieves state of the art performance on CATH-4.2 and CATH-4.3 datasets, compared to the previous methods in terms of perplexity and sequence recovery. 
Authors provide evidence that each contribution (model equivariance and inclusion of PLM) contribute to the performance of their approach (Table 1, shaded rows). Additionally they show state of the art metrics in structure and surface recovery. Finally, they demonstrate that scaling PLM improves performance and that their approach is tolerant to changes in surface depending on different conditions used to crystallize the protein.

### Strengths
The main strength of the work is that authors archive state of the art performance on a variety of benchmarks with extensive validation of their claims. The contribution to the surface description of a protein is novel and relevant to the field. Their design of equivariant surface message passing algorithm is also novel because it integrates curvature information due to use of surface-continuous Darboux frames instead of point clouds. These two contributions coupled with extensive validation already warrant the publication of this work.

### Weaknesses
The main weakness of this work is the possibility of data leakage between training and test sets. The authors use PLM as the sequence decoder, which training dataset contains sequences from CATH database.  Although the no-PLM ablation experiment shows performance on par with SurfPro (similar sized model), we suggest showing that generated sequences do not have 100% identity to any sequence from the PLM training datasets. The second possible data leakage pathway is that exact curvatures of the surface may perfectly encode the identities of surface residues, therefore is may be useful to show sequence recovery, however the Figure 4 seems to disprove this possibility, due to core residues having higher recovery rates than the surface residues. Altogether we think that this possible weakness of this work is inconsequential.
Another weakness is that this approach to surface description is not differentiable w.r.t atomic coordinates, but it falls outside of the scope of this work.

### Questions
1. Minor errors in text:
- line 134: "discover ignorable differences". The line is unclear; are the differences insignificant? Could you state why you chose cumbersome method of using pymol for surface extraction instead of convenient biopython package is the differences are minor?
- line 457: studies -> studied
- lines 315, 317, 322: please use different delimiters between decimals and numbers in the dataset splits

### Soundness
4

### Presentation
4

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
The authors propose a new inverse folding model called SurfDesign that combines surface-based protein structure representations with protein language models to achieve higher sequence recovery rates on datasets like CATH. For the surface-based model they propose a new message passing scheme called SEMP (surface-based equivariant message passing) that allows the model to incorporate curvature and other geometrical quantities of the protein surface into the design process. The authors showcase their approach on CATH and other datasets and demonstrate lower perplexity and higher sequence recovery values compared to the baseline methods.

### Strengths
1. **Principled modelling methodology**: The paper described their new message passing scheme and the involved considerations in detail and highlight why different geometrical features may be useful to include.
2. **Extensive benchmarks and ablation studies**: The authors benchmark their model and several baselines on several datasets and demonstrate that they achieve lower perplexities and higher sequence recovery rates. They also present extensive ablation studies to highlight the important components in their modelling framework.

### Weaknesses
1. **Metrics**: The only metrics used in the paper are sequence recovery and perplexity. These metrics do not provide any insight into how good the model is for actual protein design tasks. They provided insight in the past when the values for e.g. sequence recovery were a lot worse; however, at the 60-70% levels that are presented in this paper there is no evidence that this leads to better designs or is just overfitting to the training distribution. In fact, a "perfect" sequence recovery of 100% would render the model completely useless since it would have just memorised the training dataset. These problems have been discussed in the past in papers like [PDB-Struct](https://arxiv.org/abs/2312.00080), and the authors should adopt some of the metrics proposed there to validate the claims of an improved model. Alternatively, other ways to evaluate the performance of a model would include wet-lab experiments in which the method is compared to other methods as well as an evalution to what the sequence variability between similar structures is to determine a potential "upper limit" on sequence recovery beyond which improvements just lead to overfitting.
2. **Features used in model**: The authors describe that similar to MaSIF they calculate hydrophobicity, charge and electrostatics and leverage hydrophobicity and charge in the end. However, while this is a valid thing to do for MaSIF since they consider tasks like PPI prediction and interface site prediction for which full-atom structures are available, SurfDesign is used for inverse folding where this information is not available. Making that information available to the model leads to full data leakage and makes it easy for the model to just predict the ground truth data. In the code that the authors link fro MaSif in lines 751-755, the full structure including residue identities is leveraged for calculating these properties, resulting in data leakage. For a proper validation of their model, the authors should consider tasks similar to the MaSi paper in which this information is actually available for the task at hand.
3. **Mistakes**: There are a few typos/mistakes in the paper that sometimes cause confusion for readers:
   1. L 104: Heading should be "Preliminary" and not "Priliminary"
   2. L 365: "This makes LM-DESIGN more versatile..." should be "This makes SurfDesign more versatile..." I assume since the method described in this paper is SurfDesign not LM-Design.

### Questions
1. L 132: The surface graph is built via k-NN construction, but which k is used and for what reason? There seems to be no description about this in the paper.
2. L 187: "It can be proved that this curvature feature ψ is roto-translation invariant". Can a proof for this or a reference to the proof be added?
3. In this paper only inverse folding is considered as a task, but can the surface-based design framework proposed here easily be adapted to backbone or all-atom generation?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces SurfDesign, a protein design approach utilizing protein surface geometry and the corresponding biochemical properties, such as hydrophobicity and charge. The authors present an equivariant surface encoder that captures directional and curvature information using 3D spherical Fourier-Bessel bases, serving as a structural adaptor within a protein language model to generate amino acid sequences. The method is evaluated on multiple inverse folding benchmarks and the results show that the proposed method outperforms the state-of-the-art baseline models.

### Strengths
- The designed equivariant model leverages the inductive bias of molecular surfaces, which is relational and can benefit surface-related applications.
- The combination of surface geometry and protein language model is interesting and novel.
- The paper is well-written, presenting a well-motivated problem formulation and clear illustrations.

### Weaknesses
 - In terms of practical application, the method depends on the protein surface generated from all-atom structures, including both backbone and side-chain information. This raises the concern that the performance improvement may be due to this additional structural information. A key issue with protein surface-based design is the source of these surfaces—specifically, how to obtain a protein surface without first having the all-atom structures. Please correct me if I’ve misunderstood.
- Efficiency analysis of the proposed architecture is missing, which is crucial given that modeling the protein surface involves encoding significantly more points than just the backbone.
- Given that the motivation is functional protein design, it would be great to have some corresponding experiments besides inverse folding, such as protein optimization.

### Questions
Could you show some statistics on the generated protein surfaces?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes a function-focusing inverse-folding approach utilizing surface features, advancing beyond the traditional structure-focusing inverse-folding methods that primarily emphasize structure consistency. The authors introduce an equivariant message passing technique designed to effectively process surface features, demonstrating improved sequence recovery compared to existing models.

### Strengths
The paper presents an innovative equivariant message passing approach capable of effectively representing surface features.

### Weaknesses
### Insufficient Metrics for Functionality Preservation

1. The improved sequence recovery observed in this model compared to existing approaches like PiFold or ProteinMPNN is an expected outcome, given the inclusion of surface features closely related to side-chains that determine residues, unlike previous models that only consider backbone atoms. This is a fundamental difference in input data, not necessarily an advance in methodology.
2. Relying solely on global accuracy metrics such as recovery (accuracy) is insufficient to claim the model's novelty. The model needs to demonstrate that it is not simply memorizing sequences but is capable of generating novel sequences with preserved functionality.
3. Given that surface functionality, the focus of this paper, is primarily local information, it is crucial to evaluate recovery specifically for local functional sites. Global metrics can mask poor performance in critical regions.
4. The metrics presented in Table 5 are geometrical and do not adequately represent physically and chemically meaningful insights. Metrics like RMSD and TM-score do not capture the nuances of functional site conservation.
5. Additional experiments are necessary to demonstrate that newly designed sequences maintain similar functionality:
   - For instance, when designing surface-specific sequences for hydrophobic sites, the new sequences should maintain hydrophobic properties while exhibiting sequence diversity. This requires metrics that assess the preservation of physicochemical properties.
   - Failure to achieve this would indicate that the model has not fulfilled its motivation of function-specific design. The model should be able to generate sequences that not only fold correctly but also maintain the desired surface properties.
   - Case studies or novel metrics demonstrating successful design for specific functional sites are needed like [1] or [2].

### Limited Analysis of Multi-chain Complex Dataset
1. For complex design, a more detailed analysis specific to interaction sites is required. The current analysis lacks granularity in assessing interface-specific sequence design.
2. A comprehensive examination of how well the new sequences preserve the functionality of the initial complex surface while proposing diverse sequences is necessary. It is not enough to show that the complex is still formed; the specific interactions must be maintained.

### Lack of Computational Efficiency Comparison
1. The paper does not provide a comparison of overall processing times between methods. This makes it difficult to assess the practical applicability of the method.
2. Surface feature calculation may introduce significant computational overhead not present in other models. A time comparison would better illustrate the trade-offs between the proposed approach and existing methods. The authors should quantify the computational cost of surface feature extraction.

### Questions
### Insufficient Metrics for Functional Preservation
1. Can you provide case study or suggest a new metric on local functionality design using your model? and compare with other models?

### Limited Analysis of Multi-chain Complex Dataset
1. Can you analyze how your surface-based inverse-folding model outperforms other models on the interface design of protein complexs?

### Lack of Computational Efficiency Comparison
1. Can you provide the comparison on the speed of whole sequence design protocol including data processing and inference?

### Soundness
3

### Presentation
3

### Contribution
2
