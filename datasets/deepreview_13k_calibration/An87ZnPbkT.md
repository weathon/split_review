# GNNAS-Dock: Budget Aware Algorithm Selection with Graph Neural Networks for Molecular Docking

- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3, 3, 3

## Abstract
Molecular docking is a major element in drug discovery and design.
It enables the prediction of ligand-protein interactions by simulating the binding of small molecules to proteins.
Despite the availability of numerous docking algorithms, there is no single algorithm consistently outperforms the others across a diverse set of docking scenarios.   
This paper introduces GNNAS-Dock, a novel Graph Neural Network (GNN)-based automated algorithm selection system for molecular docking in blind docking situations.
GNNs are accommodated to process the complex structural data of both ligands and proteins.
They benefit from the inherent graph-like properties to predict the performance of various docking algorithms under different conditions.
The present study pursues two main objectives: 
\textbf{1)} predict the performance of each candidate docking algorithm, in terms of Root Mean Square Deviation (RMSD), thereby identifying the most accurate method for specific scenarios;
and \textbf{2)} choose the best computationally efficient docking algorithm for each docking case, aiming to reduce the time required for docking while maintaining high accuracy.
We validate our approach on PDBBind 2020 refined set, which contains about 5,300 pairs of protein-ligand complexes.  
Our strategy is performed across a portfolio of 6 different state-of-the-art docking algorithms.
To be specific, the candidate algorithms are DiffDock, DSDP, TankBind, GNINA, SMINA, Qvina-W.
We additionally combine p2rank with GNINA, SMINA and Qvina-W for docking site prediction.
Therefore, there are totally 9 different algorithms for selection.
Our algorithm selection model achieves a mean RMSD of approximately 1.74 \AA, significantly improving upon the top performing docking algorithm (DiffDock), which has a mean RMSD of 2.95 \AA.
Moreover, when making selection in consideration of computational efficiency, our model demonstrates a success rate of 79.73\% in achieving an RMSD below the 2 \AA\, threshold, with a mean RMSD value of 2.75 \AA\, and an average processing time of about 29.05 seconds per instance.
In contrast, the remaining docking algorithms like TankBind, though faster with a processing time of merely 0.03 seconds per instance, only achieve an RMSD below the 2 \AA\, threshold in less than 60\% of cases.
These findings demonstrate the capability of GNN-based algorithm selection to significantly enhance docking performance while effectively reducing the computational time required, balancing efficiency with precision in molecular docking.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces GNNAS-Dock, a novel GNN-based algorithm selection system designed to enhance molecular docking in blind docking scenarios. Recognizing that no single docking algorithm consistently outperforms others across all scenarios, a statement generally supported by the no free lunch theorem. The authors propose leveraging GNNs to predict the performance of various docking algorithms based on the structural data of ligands and proteins. They aim to predict the performance (measured in RMSD) of each candidate docking algorithm to identify the most accurate method for specific scenarios. This effectively allows to choose the most computationally efficient docking algorithm for each docking case, reducing computational time while maintaining high accuracy. Approach is validated on the PDBBind 2020 refined set, comprising approximately 5300 protein-ligand complexes. The candidate algorithms include a mix of traditional and deep learning-based methods: DiffDock, DSDP, TankBind, GNINA, SMINA, Qvina-W, and their combinations with p2rank, totaling nine algorithms. Proposed algorithm selection model achieves a mean RMSD of approximately 1.74A, significantly improving upon the best performing standalone docking algorithm, DiffDock, which has a mean RMSD of 2.95A. When considering computational efficiency, the model demonstrates a success rate of 79.7% in achieving an RMSD below the 2A threshold, with an average processing time of about 29 seconds per instance.

### Strengths
This work takes the first step in addressing a prominent challenge in computational drug discovery. The implementation of a GNN using standard ligand and protein features is effective and keeps the approach straightforward.
Moreover, the combination of an accuracy model with an efficiency model is beautifully done and in line with solving the performance-accuracy trade-off often faced in DD.

### Weaknesses
1. There's no need to emphasize the use of GNN or these standard features, as they are already well-established in this field. The development details of GNN-Lig and GNN-Prot might be more suitable for an appendix, allowing the main manuscript to focus on more critical analyses.
2. An ablation study could significantly enhance the work. For instance, exploring the impact of various features on docking algorithm selection would provide valuable insights into the interpretability and relevance of specific features across different approaches. Additionally, a deeper examination of the training datasets for machine learning models, as well as the testing systems used for physics-based methods, would strengthen the study's foundation.
3. Currently, the approach appears more like a baseline than a fully developed solution. This is understandable given the limited prior work in this area, as mentioned in the introduction and related work sections. However, enhancing GNN-Lig and GNN-Prot by incorporating richer features, such as learned sequence or structural representations (e.g., ESM or GearNet embeddings as node features), could throw further insights in how current approaches to represent ligands and proteins work for this problem.
4. Perhaps the most significant concern is the reliance on PDBBind for testing. While PDBBind is a valuable addition, it does not fully capture the complexities of docking scenarios. Many docking methods are trained on PDBBind, which includes systems traditionally well-suited for docking, thus limiting the ability to assess the model’s prospective potential. A carefully curated dataset with temporal splits would provide a more realistic evaluation of the model's performance across diverse scenarios.

### Questions
1. Perform ablation studies on node features and incorporate richer representations.
2. Include temporal splits for the dataset used. Focusing on diverging from the dataset attained in training procedures and tunning of the ML models and docking scoring functions.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
In this paper, the authors propose GNNAS-Dock, a GNN-based algorithm selection model for molecular docking that combines the best-performing docking algorithms rather than relying on a single one. GNNAS-Dock consists of two submodels: the Accuracy model, which selects the docking method with the highest performance, and the Efficiency model, which prioritizes models with faster runtimes while maintaining suitable accuracy. GNNAS-Dock’s performance is compared with single-model approaches based on the percentage of ligands achieving RMSD < 2 Å and runtime efficiency.

### Strengths
- The use of multiple models with GNN-based Algorithm Selection to choose the most accurate or efficient model makes GNNAS-Dock unique.
- The efficiency model demonstrates runtime improvements.
- The accuracy model shows improvement in mean RMSD.

**Originality:** GNNAS-Dock presents an innovative approach by creating a GNN-based AS model that incorporates multiple models, aiming to select them based on accuracy and efficiency.

### Weaknesses
 - The authors highlight in the introduction and related work sections that they rely solely on the RMSD metric, which is becoming outdated in molecular docking. RMSD does not guarantee physicochemical plausibility, so I recommend they consider the PoseBuster[1] study for alternative approaches.
- Although the primary aim of the study is to select the best algorithm, the results suggest that DiffDock alone remains accurate and efficient, calling into question the effectiveness of the algorithm selection model.
- The RMSD metric used in molecular docking and Structure-Based Drug Design (SBDD) does not always yield bioactively, physically, or chemically plausible structures, as shown by studies like Posebuster[1], PoseCheck[2], PoseBench[3], and CompassDock[4]. Unfortunately, these metrics were not included in the benchmark.
- Some models may have been trained on different time splits, and if the training dataset overlaps with the validation or test sets among the chosen models, it could lead to information leakage [5]. This potential issue is insufficiently discussed.
- Details on data preparation, time-splitting, and training are inadequately explained.

**Significance:** The study does not demonstrate enough effectiveness in terms of accuracy and efficiency, which limits its applicability for scalability.

**Quality:** The paper lacks sufficient evidence and relies primarily on empirical results, without any physicochemical validation as noted above. Additionally, it is not up-to-date with the current literature, especially in the benchmarking and validation sections.

**Clarity:** The paper contains numerous grammatical errors that need revision, and the equations and annotations do not align with scientific paper standards. I recommend the authors revise the text to clarify their methods, moving away from narrative elements.

**Reproducibility:** As the code is not shared, it is currently impossible to verify whether the reported results are reproducible.

### Questions
- In the statement, 
> "Given the distinct structural complexities of proteins and ligands, it is crucial to design specific GNN architectures for each type of graph," 

  why did you choose to create separate GNNs for proteins and ligands instead of using a single GNN for protein-ligand pairs?
- Why did you limit atom types to {‘C’, ‘H’, ‘O’, ‘N’, ‘F’, ‘P’, ‘S’, ‘Cl’, ‘Br’, ‘I’, ‘B’}? Was there a reason for excluding heavier atoms?
- Did you incorporate edge features in the GNN models?
- How does this differ from a coarse-grained approach? 
> "To reduce the computational complexity of processing protein graphs, we simplify the graph representation by using amino acids, clusters of atoms with distinct functions, to represent each node $v_i \in V_P$."
- Did you also use an AS approach to select the GNN models?

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
GNNAS-DOCK processes a ligand and protein using graph neural networks to predict which docking tool will provide the best result (algorithm selection).  Both the accuracy and computational time of each algorithm is predicted so they can be simultaneously optimized.

### Strengths
This is an interesting, practical idea for exploiting/rectifying the fact that different docking tools have different performance characteristics on different systems.

### Weaknesses
The evaluation is done on a random split of PDBBind, which means there is massive information leakage between the training and test sets. Given this methodological choice, it is unlikely any reported results will generalize to realistic scenarios.

Only the redocking task is considered, which is not of much practical interest.

An unbiased assessment of Table 2 is unlikely to reach the same conclusion of the authors that their tool is a better approach than using DiffDock (unsurprising as DiffDock is being evaluated on its training set).

There is no analysis of the model's predictions - it would be very interesting to learn if there is an understandable pattern to what systems different docking tools are predicted to do better on (presumably whether the system is in the method's training set, for ML methods, is highly relevant).

There are concerning methodological choices in the neural network construction.  Raw Cartesian coordinates are used as features, and not as part of an equivariant GNN.  It does not appear data augmentation was used to learn equivariance. This means the trained models are highly brittle and unlikely to generalize.  The protein graph only connects along peptide bonds, so it is a line (so why use a graph representation?).  The graph pooling operator isn't disclosed in the text.

### Questions
Do you augment with random translations/rotations to compensate for using Cartesian coordinates as features (or apply some other approach to induce equivariance)?

If the protein graph is only connected along peptide bonds, why not treat as sequence data?

Can you say anything about what systems different docking tools are predicted to perform well at?  What percentage of the time are different tools predicted? Is there any correlation to protein families?

How well does the method work with a more meaningful train/test split, such as provided with PLINDER?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces GNNAS-Dock, a novel Graph Neural Network-based algorithm selection system for molecular docking. The system aims to address two key challenges: (1) selecting the most accurate docking algorithm in terms of RMSD, and (2) maintaining computationally efficiency and acceptable accuracy. The approach was validated on the PDBBind 2020 refined dataset across 9 different docking algorithms, demonstrating improvements accuracy compared to individual algorithms while maintaining efficiency.

### Strengths
1. The authors conducted a comprehensive comparison experiment with the individual method, demonstrating potential improvements in accuracy while maintaining computational efficiency.
2. The authors innovatively address an important problem by applying stacking learning to molecular docking, where ensemble learning and algorithm selection approaches have been previously overlooked.

### Weaknesses
1. Some recently published SOTA works are missing (according to the ICLR reviewer guide, these works do not qualify as concurrent work), e.g. DiffDock-L. The absence of comparison with such methods, particularly those demonstrating advancements in blind docking scenarios, limits the assessment of the proposed method's relative performance in the current state of the art.
2. The paper lacks comparison with other algorithm selection methods. While the comparison with individual algorithms demonstrates the effectiveness of ensemble learning or algorithm selection (which is an expected outcome), it does not sufficiently validate the merits of the authors' proposed core methodology. The evaluation does not isolate the specific contributions of the GNN architecture compared to other established algorithm selection techniques, making it difficult to assess the novelty and advantage of the proposed approach.
3. The results presented in Table 2 appear to be inconsistent with previously reported results in the literature, particularly for DiffDock. Notably, the success rate for RMSD<2Å is significantly higher than previously reported values. This discrepancy raises concerns about the experimental setup and the dataset used for validation, requiring further clarification to ensure the reproducibility and reliability of the findings.

### Questions
1. Given the recent advances in molecular docking, particularly the emergence of improved variants like DiffDock-L (which has shown promising results in blind docking scenarios), would the authors consider expanding their comparative analysis to include such state-of-the-art methods? 
2. Would you consider adding comparative experiments with other algorithm selection methods cited in your related work? This could help better demonstrate the specific advantages of your proposed approach beyond the expected benefits of ensemble learning.
3. The results presented in Table 2 appear to be inconsistent with previously reported results in the literature, particularly for DiffDock. Notably, the success rate for RMSD<2Å is significantly higher than previously reported values. Could the authors provide more detailed information about their experimental settings to clarify these discrepancies?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces GNNAS-Dock, an algorithm selection method tailored for molecular docking. GNNAS-Dock first generates molecular representations for both ligand and protein by combining GCN, GAT, and GIN models. These representations are concatenated and then passed through two separate models—an accuracy model and an efficiency model—that predict the performance of each algorithm. Experimental results demonstrate GNNAS-Dock’s performance compared to previous molecular docking approaches.

### Strengths
- The paper is easy to follow.
- The use of two criteria, accuracy and efficiency, for algorithm selection is a reasonable approach that adds value.

### Weaknesses
 - Is the Accuracy Model and Efficiency Model trained using supervised learning with a labeled dataset that includes labels for both accuracy and efficiency?
- When a new molecular docking algorithm is released, does GNNAS-Dock need to be retrained from scratch? Would this require a new labeled dataset for the accuracy and efficiency of the new docking algorithms? Could transfer learning be applied to GNNAS-Dock in this scenario? If transfer learning is not feasible, this would represent a significant weakness.
- Table 2 shows that DiffDock achieves comparable or even superior performance to GNNAS-Dock. Given that GNNAS-Dock requires additional overhead compared to DiffDock, it raises the question: why would practitioners choose GNNAS-Dock over DiffDock? Would DiffDock be a preferable choice for practical applications?
- Is there any baseline in the literature for algorithm selection that could be used as a comparison, rather than individual molecular docking algorithms?
- I suggest moving the explanations of GCN, GAT, and GIN from the Methods section to a Preliminary section. This would allow the Methods section to focus solely on the novel methodological contributions, which would better clarify the paper’s contributions.
- Typo: Line 221 "From"
- The evaluation of GNNAS-Dock on the DUDE dataset using AA-score is inappropriate. AA-score is designed to evaluate binding poses, not virtual screening performance, which is the typical use case for the DUDE dataset. Virtual screening metrics, such as AUC, enrichment factor, or BEDROC, should be used to evaluate performance on DUDE.
- The lack of comparison to algorithm selection baselines is a significant weakness. Simple baselines like min-rank or average-rank should be included to demonstrate the added value of the proposed method. More sophisticated baselines, such as those based on belief theory, should also be considered.

### Questions
See Weaknesses Section.

### Soundness
2

### Presentation
3

### Contribution
2
