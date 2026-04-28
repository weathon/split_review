# Redefining the task of Bioactivity Prediction

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 6, 8

## Abstract
Small molecules are vital to modern medicine, and accurately predicting their bioactivity against protein targets is crucial for therapeutic discovery and development. However, current machine learning models often rely on spurious features, leading to biased outcomes. Notably, a simple pocket-only baseline can achieve results comparable to, and sometimes better than, more complex models that incorporate both the protein pockets and the small molecules. Our analysis reveals that this phenomenon arises from insufficient training data and an improper evaluation process, which is typically conducted at the pocket level rather than the small molecule level. To address these issues, we redefine the bioactivity prediction task by introducing the SIU dataset-a million-scale Structural small molecule-protein Interaction dataset for Unbiased bioactivity prediction task, which is 50 times larger than the widely used PDBbind. The bioactivity labels in SIU are derived from wet experiments and organized by label types, ensuring greater accuracy and comparability. The complexes in SIU are constructed using a majority vote from three commonly used docking software programs, enhancing their reliability. Additionally, the structure of SIU allows for multiple small molecules to be associated with each protein pocket, enabling the redefinition of evaluation metrics like Pearson and Spearman correlations across different small molecules targeting the same protein pocket. Experimental results demonstrate that this new task provides a more challenging and meaningful benchmark for training and evaluating bioactivity prediction models, ultimately offering a more robust assessment of model performance.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper addresses significant issues in current evaluation strategies for bioactivity prediction, identifying problems with data preparation and evaluation metrics that result in inadequate benchmarking. For instance, approaches that only consider protein features in protein-small molecule interaction predictions may outperform methods that consider both due to overfitting. To tackle these challenges, the authors propose a new large dataset SIU based on mining wet lab bioactivity data and software-based docking to obtain structures, along with new evaluation metrics. The evaluations demonstrate the superiority of SIU over existing datasets and support the adoption of the new metrics.

### Strengths
**Originality**. The paper presents original research with novel isights into the issues in bioactivity predictions and novel methodology for constructing bioactivity data for machine learning.

**Quality**. The experiments are sound and convincing, clearly demonstrating the inadequacies of prior evaluation methods and the value of the new dataset and metrics.

**Clarity**. The paper is easy to follow.

**Significance**. The paper addresses a highly important issue of inadequate benchmarking in bioactivity prediction. The new SIU dataset is substantially larger than existing alternatives.

### Weaknesses
 
**Major Comments**

- The availability of the dataset is not discussed. Will it be publicly accessible, and if so, in what form?
- Data deduplication and diversity measurement methods are only briefly mentioned and not described anywhere in the text. Specifically, please elaborate on the ECFP and FLAPP methods used for deduplication of small molecules and pockets, respectively, and analyze the diversity and statistics after deduplication. The description should include specific parameters used for ECFP (e.g., radius, number of bits) and FLAPP (e.g., alignment parameters, scoring function).
- Although the paper proposes a large dataset, further analysis of the data splitting approach would be beneficial. The meanings of 0.6 and 0.9 non-homology levels are unclear (Does 0.6 signify 60% sequence identity upon alignment? How are sequences aligned?). Furthermore, is sequence similarity-based splitting sufficient with respect to data leakage? Recent work suggests that structure-based splitting may be a better choice [[1](https://arxiv.org/abs/2402.18396), [2](https://www.biorxiv.org/content/10.1101/2024.07.17.603955v1)]. The authors should clarify the alignment method used to calculate sequence identity and justify the choice of sequence-based splitting over structure-based approaches, especially given the availability of structural data.
- The related work section is brief, only covering a few related datasets. Including related work on bioactivity prediction baselines to justify the selected methods for experiments and discussing prior evaluation metrics would strengthen the paper. Specifically, a discussion of the limitations of existing metrics (e.g., RMSE, MAE) in the context of bioactivity prediction would be beneficial.
- A table summarizing the statistics (for example, number of proteins, ligands, pairs, unique pockets, unique ligands, etc.) for the training and test sets of SIU and other datasets like PDBbind would be beneficial. This table should also include the number of unique protein sequences and structural folds to assess the diversity of the dataset.

**Minor Comments**

- Abstract: please clarify what SIU stands for. From the abstract it is not clear that SIU is a dataset.
- Figure 1: What is the GNN architecture? Please provide details on the number of layers, hidden units, and activation functions used.
- Figure 1C: the meaning of the red line and the target are not clear. It's unclear how the target values are distributed and what the red line represents in relation to the predicted values.
- Line 153: please specify the cutoffs being referenced. What specific values were used for filtering or thresholding?
- Figure 2: Poses are visualized in the same way as ligands, which is confusing. The visualization should clearly distinguish between the original ligand structure and the docked poses.
- Line 209: “identified by PDB IDs” contradicts earlier text, which states that multiple pockets may arise from the same PDB ID. The text should clarify whether pockets are identified by PDB IDs or UniProt IDs.
- Figure 3: clarify the meaning of RMSD—is it the RMSD between a docking pose and the ground truth from PDB, or between docking poses obtained with different methods to quantify consensus? The text should specify which structures are being compared when calculating RMSD.
- Section: “Structural data construction via multi-software docking”: Same as above, RMSD is used in two different senses, which is not always clear. The text should clearly differentiate between RMSD calculations for pose consensus and RMSD calculations against experimental structures.
- Section: “Structural data construction via multi-software docking”: Are the three chosen docking methods independent? Why were these specific methods selected? The rationale for choosing these specific docking methods should be provided, including a discussion of their strengths and weaknesses.
- Line 280: the claim “diverse small molecules” is unsupported by experiments. The authors should provide quantitative evidence to support this claim, such as diversity metrics or property distributions.
- Line 346: “for each target” is slightly confusing—are there only 10 targets in the dataset? The text should clarify the number of targets used in the analysis.
- Line 392: clarify the statement, “We conducted non-homology analyses at two levels, 0.6 and 0.9”—does this imply a maximum of 60% and 90% sequence identity between training and test proteins? The text should explicitly state the meaning of these non-homology levels.
- Line 424: UniMol reference appears to be missing.
- Tables 1 and 2: highlighting the highest values in bold would improve clarity.
- Line 496: “pdb” should be in uppercase (PDB).

### Questions
- Would a complementary analysis focused solely on small molecules, rather than only proteins, lead to the same conclusions? For example, could training a small-molecule-only baseline on PDBbind yield similar insights?

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
The paper has two main contributions. First, it presents a new large-scale dataset of small molecule-protein interactions for unbiased bioactivity prediction, named SIU. Second, the authors redefine evaluation metrics for bioactivity prediction by proposing to average correlation coefficients per protein before calculating the overal coefficients, and by stratifying performance evaluation across four key types of bioactivity labels. The benefits of the proposed dataset and metrics are demonstrated empirically through the evaluation of several standard models.

### Strengths
Originality

The work’s originality lies primarily in its focus: rather than routinely proposing new models using existing datasets without analyzing their limitations, it critically examines the dataset and evaluation metrics themselves.

Quality

The technical quality of the work is high. The methods employed are appropriate and well-justified.

Clarity

The paper includes a thorough introduction that provides clear context and a strong foundation for the study.

Significance

This work is highly significant for the machine learning community, as it introduces both a new dataset and an updated evaluation protocol for the important task of bioactivity prediction, while effectively demonstrating limitations in previous datasets and evaluation methods.

### Weaknesses
Major Concerns:

- Data and Code Availability: A primary contribution of this work is the benchmark for bioactivity prediction, which includes a new dataset, evaluation metrics, and a specific data split. However, without readily accessible resources, the value of the work may be limited, as reproducing the benchmark independently could be challenging (e.g., requiring extensive runs across multiple docking software tools). It would be helpful if the authors addressed data availability, perhaps by providing a link to an anonymous GitHub repository.

- Simulated Poses vs. Crystal Structures: The dataset consists exclusively of simulated poses rather than crystal structures. Since the dataset is described as high-quality, a discussion of the tradeoffs between experimental crystal structures and generated poses would add valuable context. For example, the dataset is constructed based on a consensus from two out of three docking tools. Additional information on whether this approach assures high quality—especially if one tool generates a different pose—could be beneficial. The authors might also consider presenting results from training on SIU and evaluating on PDBbind to explore any potential distribution shifts.

- Sequence Identity-Based Data Splitting: The paper uses sequence identity-based data splitting; however, since the task is defined in terms of 3D structures, a structure-based split may offer a more appropriate approach, especially considering that similar structures may arise from different sequences.

- Validation Fold Construction: Details on the construction of the validation fold would clarify this important aspect, as it affects both model training outcomes and the usability of the dataset in future work.

- Test Fold Curation: While the manual curation of the test fold is appreciated, it would be helpful to understand the choice of focusing on only 10 protein targets, as this might affect the generalizability of the evaluation. Could the authors expand it to more proteins?

- Redefining the Bioactivity Prediction Task: Since the paper redefines the bioactivity prediction task, a clearer description of the specific inputs and outputs considered would be helpful. For instance, it is unclear which ligand pose is used as input when three docking tools are involved. Additionally, Section 3.3, "Reframing the Bioactivity Prediction Task," does not discuss the RMSE and MAE metrics used for evaluation.

- Figure 3 Interpretation: Interpreting Figure 3 is challenging without a more precise definition of the evaluation using co-crystal poses from PDB complexes. The text does not clarify which PDB complexes were included and does not clearly define Success Ratio and Remaining Ratio.

Minor Concerns:

- The abstract does not define what SIU stands for.
- The process for filtering based on extended-connectivity fingerprints could be elaborated. Is it based on pairwise Tanimoto similarities between fingerprints?
- Line 330: The statement, "Our structured approach facilitates nuanced assessments, such as evaluating the impact of specific small molecule modifications on protein interactions or comparing the efficacy of different compounds within the same protein pocket context," is not clear, especially as some filtering of ligands was involved based on extended-connectivity fingerprints.
- Line 282: The acronym "AIDD" could be defined for clarity.
- Line 346: It appears that Figure 4(D) should be replaced with Figure 4(B).

### Questions
- Could the authors clarify how the RMSE and MAE metrics are averaged? It would also be helpful to understand why RMSE* and MAE* are not defined using the same approach as Pearson* and Spearman* from Pearson and Spearman, respectively.
- Could the authors explain why grouping by pockets is considered equivalent to grouping by PDB IDs? Is not it possible for a single protein to have multiple pockets?

### Soundness
2

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
4

### Summary
The paper proposes a new benchmark for training and testing of bioactivity prediction models, a critical task in computational biology. The curation of the training data involves filtering a set of more than one million bioactivities, cluster them into predictions around specific pockets and predict approximate structures for each of them. The curation of the test set the selection of a small subset of test complexes and the definition of the task as correlations within each target. Finally, the authors train a number of models on this new benchmark and highlight how the poor results on this assessment suggests more work needs to be done.

### Strengths
I believe that the curation of a dataset for protein small molecule activity prediction is very important. Current datasets are too small and used in the incorrect way as the authors also represent. In this work, the authors do a very extensive and carefully thought out job towards building such dataset.

### Weaknesses
Building and proposing a new benchmark constitutes a significant responsibility: once the benchmark is released and, as I hope, the community adopts it, it will become very hard to correct any wrong choice made at this stage and these may lead to a lot of work being largely wasted (as I believe it is happening with current benchmarks for this task). Therefore, my bar is not just having an improvement over what is public but making sure that researchers in the field would not have concerns about adopting such a dataset.

Based on this premise below I’m presenting a list of concerns that I would appreciate the authors responding to or addressing:

1. The authors only retained datapoints for which the docking methods were consistent in their majority. While this appears sensible, it also creates a bias in the kind of molecules that the model considers (intuitively only “easier” complexes). It could be interesting to ablate the addition of non-consensus poses in the training set or in the test set for some of the baselines.

2. The success proportion presented appears somewhat misleading. It is well known that redocking or holo-structure docking (that the authors use to validate the structure generation) is significantly easier than cross-docking (docking to the protein structure resolved when binding to a different protein, which the authors have to use when generating new structures). Therefore the experiments on the success should be performed on the cross docking task. This can be performed by taking from PDB structures of ligands bound to the same pocket.

3. Saying that structures generated with the docking programs are of high quality seems a bit exaggerated or at least lacking experimental backing (see comment above on the difference between redocking and cross-docking). Multiple works in the molecular docking community have shown significant issues with the apo or cross docked performance of the methods applied for docking in this work.

4. Assay types might be a bit misleading as the name of the “label type” as there are many different types of assays producing for example Kd values.

5. The definition of different pockets from PDB IDs of co-crystal ligands and the subsequent deduplication are very unclear. While this seems a relatively non-important detail it becomes critical once the authors decide to use this assignment to compute correlation over.

6. For protein ligand complexes from the bioactivity assays the way that these are assigned to a specific PDB ID / pocket is not clear to me. The available information is the Uniprot but then how does one go from having a specific Uniprot to deciding which of the PDB IDs corresponding to the different pockets to assign a complex to.

7. Basing the benchmark of the output of the docking models e.g. by filtering out complexes with non-consensus poses and grouping by predicted pocket, will not allow fair comparisons for non-structure based methods or methods based on a different docking algorithm. I would recommend the authors remove such filtering steps for the test set to avoid the applicability of the benchmark being limited.

8. Line 326 the authors say that the dataset is unbiased. Could they specify clearly what they mean by this term? Once again the claim does not seem fully justified.

9. In paragraph 3.3, the authors discuss the value of dividing the prediction for different assay types. To motivate this they apply statistical significance test to the mean of the distribution of different assay types. However, it is unclear to me why this would be a good motivation for that. Differences in averages might just mean that these assays were applied to different types of proteins, while what the authors would need to show to motivate this point is that if they were applied to the same complex the results would be different depending on the assay. This work was actually performed by a recent paper [1] which however showed no very clear outcomes when it comes to the differentiation between different assay types. An alternative way to try to demonstrate this point would be to put all datapoints in the same “task” and then train and evaluate a single task model.

10. I believe that saying that “In the traditional approach” or “conventional approach” people would look for pearson across different targets is misleading. This has been indeed unfortunately done recently in a number of ML papers, however, more established benchmarks in the field such as FEP+ do look at correlations computed per target.

### Questions
1. Figure 3: how is success ratio defined?

2. What type of assay does the test set contain? I assume it does not contain measurements across all different assay types. In this case how are spearman and person correlations computed for al assay types in the test set?

3. How will the dataset be released? What format and what license?

4. Is Pearson computed also on inactives? What proportion of the test and training set are inactive?

5. Do I understand correctly that the test set only has 10 targets? 

6. In line 365 I assume the assay type is also used for the grouping, could the authors confirm?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors present a new dataset for bioactivity prediction together with a more fair metric for evaluation of ML models for bioactivity prediction. The authors present valuable insights regarding the weaknesses of current state of the art which convincingly motivates their work. The new carefully curated dataset together with the new metric tackles the identified weaknesses of current SOTA.

### Strengths
1. Identification of the issues with current SOTA: overfitting to protein pockets due to small diversity of current datasets in terms of containing different small molecules docked to a single protein pocket; issues in reporting the overall correlation instead of computing the partial correlations per target and pooling the partial correlations which can help hide the problem of overfitting to protein pockets

2. Introduction of a new large dataset for bioactivity prediction

3. Careful curation of the dataset using a custom method of majority vore over different docking tools used for generation of the docked pose. Separation by different essay types is also useful.

### Weaknesses
1. There are few smaller unclarities in the text:
- On line 174, I did not understand what it is meant by "anti-logged"
- I did not find what method was used for generation of the small molecule conformers, it would be good to clarify this near the statement "Initial 3D conformations for the small molecules were generated prior to docking."
- Figure 4 is discussed in the text, but the caption could use more detailed description. Just by looking at the figure it is not clear what we are looking at.
- The statement “We conducted non-homology analyses at two levels, 0.6 and 0.9,” is not clear. Did the authors check for sequence identity less than 60/90 pct. between test and train set? Or the complement of 40/10 pct.? Please clarify.

2. No mention of the Papyrus dataset ( https://jcheminf.biomedcentral.com/articles/10.1186/s13321-022-00672-x ). It should be discussed in related work and authors should compare SIU to Papyrus in all relevant aspects, such as size, data origin and level of curation.

3. Detailed, practical description of the dataset, which would facilitate its usage by developers of ML models is missing. I suggest putting to supplementary material more detailed and practical description of what is provided in the dataset. PDB files containing the structure of the protein-ligand complexes as docked by some of the docking software? And the labels are just a single scalar value per datapoint? Please explain in detail.

4. The sequence similarity thresholds of 0.6 and 0.9 for splitting the data seem high. It is common to observe structural homologs with sequence identities lower than 0.6. Using thresholds such as 0.3 or 0.4, as is common practice in methods like AF2, would be more appropriate to avoid data leakage and ensure a more robust benchmark. The current thresholds might allow for significant information overlap between training and test sets, potentially inflating performance metrics.

### Questions
1. The presented majority vote system over the 3 docking system is interesting even from the point of view of docking. What percentage of poses passed this filter? Did you notice some 2 of the 3 tools to tend to agree more with each other? It would be interesting to benchmark this method against the individual tools on some docking dataset (e.g. PDBBind) - for example take the performance of the 3 individual tools evaluated on PDBBind and compare it to the performance of the best of the 3 tools evaluated just over the datapoints which passed the majority vote filter. This benchmarking is not a strict requirement for the rebuttal period from me, but I would be really interested to see it.

2. Could you please describe in more detail how were the models trained for the bioactivity prediction? E.g. the docking model UniMol is described in SuppMat to have an MLP on top of it. What is the input and what is the output of such model. Is the MLP trained to predict a single scalar value for a protein-ligand pair? Please explain.

### Soundness
4

### Presentation
3

### Contribution
3
