# Group Ligands Docking to Protein Pockets

- Decision: Accept
- Scores: 8, 6, 5, 8

## Abstract
Molecular docking is a key task in computational biology that has attracted increasing interest from the machine learning community. While existing methods have achieved success, they generally treat each protein-ligand pair in isolation. Inspired by the biochemical observation that ligands binding to the same target protein tend to adopt similar poses, we propose \textsc{GroupBind}, a novel molecular docking framework that simultaneously considers multiple ligands docking to a protein. This is achieved by introducing an interaction layer for the group of ligands and a triangle attention module for embedding protein-ligand and group-ligand pairs. By integrating our approach with diffusion based docking model, we set a new state-of-the-art performance on the PDBBind blind docking benchmark, demonstrating the effectiveness of our paradigm in enhancing molecular docking accuracy.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents a molecular docking framework called GROUPBIND, which enhances the binding capability of a ligand to a target protein pocket by leveraging other ligands that bind to the same pocket. 
The framework introduces message padding among groups of ligands and a triangle attention module for protein-ligand pairs. Experimental results validate that GROUPBIND improves docking performance based on diffusion models.

### Strengths
(1) The writing and organization of this paper are very clear.

(2) This paper is intriguing because it is based on the idea of enhancing the binding capability of the current ligand by considering the binding positions of other ligands that target the same protein.

### Weaknesses
 (1) Why are the results of DIFFDOCK in Table 1 worse than those in the original paper, and it seems that the bold text annotations might be inaccurate?

(2) From Figure 1, we can see that molecules binding to the same pocket indeed have similar structures, but how many pockets in the dataset exhibit this situation? Is there any statistical data on the number of pockets and the corresponding similar ligands in the PDBBind dataset? 

(3) During inference, when searching the database for ligands similar to the query ligand, how many entries in the test set can retrieve similar ligands? If similar ligands cannot be retrieved, does that mean the model becomes ineffective?

### Questions
Refer to the content in the Weaknesses.

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
5

### Summary
This paper introduces GroupBind, a blind rigid docking method predicated on the biochemical observation that ligands binding to the same target protein often adopt similar poses. GroupBind employs an interaction layer for a group of ligands and a triangle attention module to embed protein-ligand and group-ligand pairs. Performance is evaluated on the PDBbind dataset.

### Strengths
1. The idea of leveraging similar binding poses among ligands targeting the same protein is intriguing and biologically relevant.
2. The experimental results suggest that incorporating augmented ligands improves docking performance.

### Weaknesses
1. The core idea is similar  to MCS (Maximum Common Substructure) docking [1, 2], which assume that ligands with similar substructures exhibit similar docking poses. GroupBind, however, assumes all ligands share similar docking poses. Figure 1 depicts highly similar ligands with similar docking structures. Conversely, [3] (Figure 4) illustrates cases where structurally distinct ligands adopt distinct poses. A statistical comparison quantifying the difference between the MCS docking assumption and GroupBind's assumption is warranted. Specifically, it's unclear how GroupBind performs when ligands within a group have low structural similarity, and whether the method can still capture the correct binding pose in such cases. The assumption of similar binding poses for all ligands within a group needs further justification, especially when considering the diversity of chemical structures that can bind to the same protein.

2. Comparing GroupBind-Ref against blind docking methods like DiffDock is unfair. DiffDock performs blind docking, whereas GroupBind-Ref utilizes prior knowledge of the binding pocket, making it a site-specific docking method. This introduces a significant advantage for GroupBind-Ref. The manuscript should clearly distinguish between these two settings and avoid direct comparisons that do not account for the difference in input information. The performance of GroupBind in a truly blind docking scenario should be evaluated to provide a more comprehensive assessment.

3. The evaluation should include more baselines such as FABind [5] and FABind+ [6], for which source code is available. Expanding the evaluation to include datasets like PoseBuster would assess GroupBind's ability to predict physically plausible structures. The current evaluation lacks a comparison with methods that explicitly focus on generating physically realistic poses, which is crucial for practical applications. Furthermore, the evaluation should include metrics that assess the quality of the predicted binding poses beyond just success rate, such as RMSD and interaction fingerprints.

4. The reported top-1 docking success rate for DiffDock (32.4% with 40 samples in Table 1) appears considerably lower than previously 
reported results (38.2% in [4] and 36.0% in [5]). This discrepancy requires clarification. It is important to ensure that the implementation of DiffDock is consistent with the original work to ensure a fair comparison. The manuscript should provide more details about the specific parameters and settings used for DiffDock to allow for reproducibility and verification.

5. The clarity of the writing could be improved. Specific points of confusion are detailed below in the Questions section.

### Questions
1.	The definition of "ligand ground graph" needs explicit formalization. The current lack of clarity makes understanding this crucial concept challenging. For example, when referring “noisy group ligands” in line 214, it is difficult to understand this concept.
2.	The references to tables and figures are confusing. Avoid using "Section" to denote figures, tables, and section of manuscript at the same time. Use "Figure" when referring to images (e.g., Figure 1, Figure 2) and "Table" for tabular data (e.g., Table 1, Table 2). 
3.	A thorough proofread is necessary to correct spelling and grammatical errors. For instance, "beyound" on line 101 should be corrected to "beyond." A comprehensive review of the entire text is recommended.
4.	Figure 7's inclusion of Figures 3, 4, 5, and 6. For better visual organization and clarity, these figures should be presented as subfigures within a single figure (e.g., Figure 7a, 7b, 7c, and 7d). This allows for easier comparison and a more streamlined presentation.
5.	Lacking explanation of "NG" in Figure 6. While the meaning of "NG" in Figure 6 might be discernible from the main text, its meaning should be explicitly stated. This ensures clarity and avoids requiring readers to search through the text for an explanation. A concise definition or clarification of "NG" within the caption is crucial.

### Soundness
3

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
5

### Summary
This paper presents a deep learning model for molecular docking, which improves data utilization and model quality by docking multiple molecules to the same protein. It further enhances the connections between similar atoms across different molecules and the same protein amino acids using a triangular perceptual network. Through this multi-molecule docking approach, the model surpasses existing methods.

### Strengths
The study proposes a new molecu lar docking framework to simultaneously consider multiple ligands docking to a protein.

### Weaknesses
Overall, this paper offers a certain level of contribution, but the experimental section requires clearer descriptions and further discussion. For the figures in the paper, the authors should provide detailed captions, including explanations of the methods used.

1.	The authors should account for the effect of protein similarity on the results by performing redundancy removal on the test set proteins that are either duplicated or highly similar to those in the training or validation sets. Tools like MMseqs or other alternatives could be used for this process.
2.	The authors need to explain how the similarity between ligands in the group ligand set impacts the results.
3.	How would the results of GROUPBIND change if tested on the latest PoseBuster (version 1 and version 2)?
4.	In Figure 4 on page 8, does the success rate refer to Top 1 or Top 40? What do “SG” and “AG” specifically mean? These details should be clarified in the figure caption.
5.	What does Figure 5 on page 8 illustrate, and where is it referenced in the article?
6.	In Figure 6 on page 8, does the success rate refer to Top 1 or Top 40? The meanings of “NG”, “SG”, and “AG” should also be clarified in the figure caption.
7.	On line 457 on page 9, the percentage 36.3% is mentioned twice, which could cause confusion and should be clarified.

### Questions
1.	The authors should account for the effect of protein similarity on the results by performing redundancy removal on the test set proteins that are either duplicated or highly similar to those in the training or validation sets. Tools like MMseqs or other alternatives could be used for this process.
2.	The authors need to explain how the similarity between ligands in the group ligand set impacts the results.
3.	How would the results of GROUPBIND change if tested on the latest PoseBuster (version 1 and version 2)?
4.	In Figure 4 on page 8, does the success rate refer to Top 1 or Top 40? What do “SG” and “AG” specifically mean? These details should be clarified in the figure caption.
5.	What does Figure 5 on page 8 illustrate, and where is it referenced in the article?
6.	In Figure 6 on page 8, does the success rate refer to Top 1 or Top 40? The meanings of “NG”, “SG”, and “AG” should also be clarified in the figure caption.
7.	On line 457 on page 9, the percentage 36.3% is mentioned twice, which could cause confusion and should be clarified.

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
4

### Summary
The paper describes an approach for leveraging the insight that similar ligands that bind to the same protein target are expected to binding similarly.  A method for attending between ligands as part of a diffusion docking process is described and the results convincingly show the benefit of this approach.

### Strengths
Particularly during the lead optimization phase, it is reasonable to expect that there are a number of known ligands for the target protein and using this information to improve docking performance could help in the discovery of better ligands.

A reasonable approach for message passing across ligands with triangle attention is described.  This might provide a more general template for other tasks where output are represented as graphs and there is a known consistency bias.

This approach does not require the accessory ligands to have a known structure at inference time, which is a realistic scenario.

Informative ablation studies are performed.

### Weaknesses
The contributions are inappropriate as written.  This is not the first time the concept that multiple similar molecules can be used to enhance molecular docking has been described.  ComBind (Paggi et al, 2021; cited in the paper) does exactly that.  There are other methods that use this insight in different ways (e.g. selecting poses from ensemble docking).  The contributions should be qualified that this is the first end-to-end deep neural network approach to molecular docking that uses this insight.

The results only compare to single-ligand docking.  Comparing to ComBind (or OpenComBind if lacking a Schroedinger license) would be more relevant.  Can the diffusion model approach make better use of the similarity bias than previous methods? This question goes unanswered.

Not going beyond the PDBbind to identify alternative augmentation ligands (of which there are many, as structures aren't needed for inference) is a missed opportunity that weakens the paper as with the current evaluation framework many ligands can't be put into groups.  Replicating the ComBind evaluation would provide predefined groups of ligands while also making it possible directly compare to a conventional approach.

There are issues with using a time split to assess generalizability, but as this is the same split used with DiffDock it is appropriate to use for the comparisons performed here.

The overloading of "k" to mean two different things in Fig 2 is confusing.

I found equations (4) and (5) confusing due to the overloading of z - the text says these two separate values (presumably equivalent to AF2 incoming and outgoing triangle attention edges) will be stacked, while the equations say they are summed.

"and since the C-C bond length is about 1.5A."

Table 2 is apparently showing Top-10 results, but this fact is only stated in the main text. Why not replicate the reporting in Table 1?  "Med." isn't defined, but is presumably median RMSD.

4.4: "Section" is used when "Figure" is meant.  "ifself"

### Questions
How does your method compare to ComBind in a head-to-head comparison? Answering this would significantly increase my enthusiasm for the paper as, in addition to providing a more relevant baseline, it would involve testing using ligands without known structure as augmentation ligands (assuming the ComBind evaluation framework is used).

### Soundness
3

### Presentation
3

### Contribution
3
