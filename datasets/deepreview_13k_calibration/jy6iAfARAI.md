# Reaction Graph: Toward Modeling Chemical Reactions  with 3D Molecular Structures

- Decision: Reject
- Avg Score: 6.00
- Scores: 6, 6, 6, 8, 5, 6, 8, 3

## Abstract
Accurately modeling chemical reactions using Artificial Intelligence (AI) can accelerate discovery and development, especially in fields like drug design and material science.  Although AI has made remarkable advancements in single molecule recognition, such as predicting molecular properties, the study of interactions between molecules, particularly chemical reactions, has been relatively overlooked. In this paper, we introduce Reaction Graph (RG), a unified graph representation that encapsulates the 3D molecular structures within chemical reactions.  RG integrates the molecular graphs of reactants and products into a cohesive framework, effectively capturing the interatomic relationships pertinent to the reaction process. Additionally, it incorporates the 3D structure information of molecules in a simple yet effective manner. We conduct experiments on a range of tasks, including chemical reaction classification, condition prediction,  and yield prediction. RG achieves the highest accuracy across six datasets, demonstrating the effectiveness of the proposed method. The code will be publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a new method for modelling chemical reactions. In particular the paper suggests to incorporate the 3D information of the graph.

### Strengths
- The paper is clearly written
- The technical contribution is solid

### Weaknesses
The main weakness is the baseline chosen for comparisons.

In the related work you mention [1], but you never compare against it and looking at the results from the paper they seem like they still outperform the method you propose? In fact none of the baselines in [1] are re-used as far as I can tell (why?).

The paper needs a better limitation section.

### Questions
Could the others expand on how their method differs from molecular simulation for reaction modelling? It seems that by incorporating the 3D spatial information we already quite close to molecular simulation conceptually.

What is the computation cost of your method, in particular in comparison to the other methods?

### Soundness
2

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
4

### Summary
This paper proposes a method for chemical reaction modeling that, in addition to the molecular graphs includes both a map of correspondences of atoms across the reaction (reaction edges) and the distance matrices of the 3D structures of the reactants and products.  This improved representation helps enhance the ability of the model to accurately handle chemical reactions compared to a baseline method that only uses the molecular graphs.

### Strengths
This paper introduces the 3D geometric information into reaction modeling and demonstrates a modest improvement compared to using only the molecular graphs.  Importantly, this improvement is orthogonal to the addition of the correspondence between atoms in reactants and products, which substantially improves reaction modeling compared to using only the graphs.  The paper uses several datasets and demonstrates improved results across a number of metrics and tasks compared to prior efforts.

### Weaknesses
Some of the language could benefit from greater clarity.  In the section about the implementation details, could the authors clarify what they mean with the iterative output technique to support beam search?  In page 6, line 295, the experiment results support their hypothesis but do not fully validate it, as Fig 3 only has a single example molecule.  Regarding the construction of Pistachio-Condition, how are the validation and testing splits selected?


Although the addition of 3D features appears to consistently help, the effect is somewhat unclear.  For example, why is the lack of both reaction edge and 3D structure resulting in significantly higher accuracy in Table 4 than past method in Table 3?  In particular, could the authors clarify if and how the total parameter count changes when the 3D information was excluded and whether the hyperparameters were reoptimized for that network?  In addition to ablating and optimal model with 3D, demonstrating that there is room for improvement by simply adding 3D information to a previously optimal model would strengthen the message of this work.  I wonder if the current improvement in accuracy with the addition of the 3D representation in part stems from the reduction in the total parameter count.

### Questions
Have the authors considered mixing USPTO and Pistachio (or any of the other datasets) for any of their experiments? I wonder if such mixing might yield valuable insights and lead to better model generalization.  Complementary to this point, have the authors considered separating Pistachio into folds of incremental difficulty (for example by atom count, scaffold size, or other metrics of synthetic difficulty) in order to perform a more detailed analysis of the additional contribution of 3D structure?  It would be interesting to investigate if there are classes of scaffolds where 3D helps and others where it is neutral or detrimental on average.

Have the authors considered alternative modern ways to incorporate 3D information, such as equivariant neural networks?

### Soundness
3

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
The authors proposed a method (i.e., Reaction Graph, RG) to learn graph representations for chemical reactions. RG conserves atom mapping information by adding edges between atoms in the reactant and product molecules. The authors also included edge distance information to capture the spatial relationship between atoms. The method was evaluated on three tasks: reaction classification, reaction condition recommendation, and reaction yield prediction. Overall, RG showed impressive performance on most dataset splits. This method can be useful for various applications in reaction modeling.

### Strengths
- Originality: The idea of conserving atom mapping information and including edge distance information is novel and significant.
- Quality: The method is well-designed, and the experiments are thorough.
- Clarity: The paper is well-written and easy to follow, and the figures are helpful.
- Significance: This method explores a new direction in chemical reaction modeling and can inspire future research in the field.

### Weaknesses
 - For each table, are the results averaged over multiple runs? It would be better to include the standard deviation or confidence interval.
- The idea of using angular edges to incorporate 3D information does not consider the torsion angle. A torsion angle is defined as the dihedral angle between four connected atoms in a molecule. Molecules with different dihedral angles can show very different properties but are represented the same using the proposed representation method. The authors might need to state this explicitly as a limitation in the current version or provide a solution to this problem in future work.
- Many tools are involved in preparing the dataset, such as MMFF for 3D coordinate generation, RXNMapper for reaction atom mapping, and NameRXN for labeling reactions. The authors might want to briefly comment on the application scope/accuracy of the methods used, as the accuracy of these methods significantly influences the data quality, and consequently, the benchmark results.



### Questions
- It might be beneficial to provide general characteristics for each task type so that future papers can informatively discuss the tasks and compare methods. For reaction classification, many methods achieved almost perfect performance. Is it because the task is too simple? For yield prediction, there is a staggering difference between small and large datasets. This is due not only to the noise level in yield records (same reaction but different yield records) but also to the non-smooth surface of the structure-yield relationship (similar reaction but very different yield records). See examples here: https://www.rsc.org/suppdata/d3/sc/d3sc03902a/d3sc03902a2.pdf. As for reaction condition prediction, label canonicalization might be a performance consideration, as there could be multiple different names for a chemical entity. See this paper for an example of canonicalizing names: Figure 2A of https://doi.org/10.1021/jacs.4c00098.
- If I understand correctly, the current reaction global representation is a linear combination of node features. For an LSTM, the last hidden state contains the information about all previous nodes, which might also be a meaningful representation for the global reaction. How did the authors decide to use the linear combination instead of the hidden state?
- Providing the definitions of CEN and MCC might be helpful for readers who are unfamiliar with these metrics. Besides, the F1 score is a common metric for binary classification tasks in science, as it considers label imbalance. Can the authors add the F1 score in Table 1?
- Why did the authors choose to compute angular edges instead of using bond angle information? The latter seems more intuitive and is readily available via RDKit/common GNN models, so there is no need to compute the angular edges.
- Writing can be more concise. For example, "computational and mathematical chemistry" could be "computational chemistry" (line 145).
- What is \( T_1 \) in equation (3)?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes the unified 3D Reaction Graph (RG), a novel graph representation for chemical reactions. By conducting various experiments on chemical reactions and comparing RG with existing models that use fingerprints and molecular graphs, the paper demonstrates that RG achieves state-of-the-art performance across multiple tasks. The findings highlight the importance of incorporating reaction edges and 3D structural information, represented as edge lengths and angular edges, rather than relying solely on molecular graphs.

### Strengths
- The Reaction Graph (RG) incorporates reaction edge and 3D information into molecular graphs, enhancing the representation of reactants and products as well as improving predictive performance on chemical reactions.
- The authors conduct experiments on a wide range of tasks and compare the proposed method with various models, demonstrating the effectiveness of RG.
- Since the proposed method is independent of the components and architectures of graph neural networks, any model can be used for chemical reaction modeling.

### Weaknesses
Although the authors show the importance of 3D information and confirm a slight increase in performance for chemical reaction prediction, the 3D information's utility may depend on the computation method. Thus, performance could deteriorate if adequate computation is not applied. It may be difficult to discern which components (the features obtained from an insufficiently trained GNN or the 3D features themselves) contribute to the performance.

### Questions
- According to the ablation studies in Tables 2 and 4, the 3D information obtained from MMFF94 appears to contribute only marginally to performance. Could applying a more accurate method, such as DFT, potentially improve the performance?
- In Figure 3, DFT and other theoretical calculations provide insights into reaction sites by calculating energy potentials and activation energies. How well do the attention weights from the RG model correlate with these theoretical values? Could this correlation potentially validate the model's focus on reaction centers?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper proposes a type of graph, called Reaction Graph, to model chemical reactions that are overlooked in existing molecular graphs. Reaction graph allows GNNs to capture chemical reactions during the message passing stage and hence improves the accuracy of chemical reaction condition prediction tasks.

### Strengths
1. The paper includes chemical reactions in the graph representation.

2. The paper also includes 3D molecular information in the reaction modeling. 

3. The proposed method achieves better prediction accuracy.

### Weaknesses
1. The novelty of the paper is unclear. It's not clear why Reaction Graph is a novel graph representation. 

2. The proposed solution seems to be rather ad hoc, for example why RBF is used to embed the edge length, the way the vertex-edge integration is conducted, and why an attention-based aggregation method with an LSTM is employed. In addition, the solution also looks to be pretty straightforward and its novelty is unclear. 

3. The significance of the work is unclear to a general reader whose background is perhaps more in CS rather than in chemistry, and therefore it's hard to assess the significance of the results presented in Section 4.

### Questions
It would help readers to better appreciate the contributes of this work if the novelty of the work can be clearly justified, e.g., why Reaction Graph is a novel concept, why edge embedding, vertex-edge integration, and attention-based aggregation in the solution are reasonable and how do they compare with their alternatives, what is the novelty in the solution? 

The significance of the work might be easier for experts in chemistry to understand and hence this work might be better to be submitted to venues in chemistry, or otherwise, I suggest the authors to significantly improve the technical depth of the work.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents Reaction Graph (RG), a novel approach for representing chemical reactions using 3D molecular structures. It introduces a unified graph representation integrating reactants and products, incorporating 3D structural information. The work demonstrates applications in areas like leaving group identification.

### Strengths
- Innovative unified graph representation combining reactants and products
- Integration of 3D structural information into reaction modeling
- Promising results in leaving group identification analysis
- Clear understanding of current limitations and proposed solutions

### Weaknesses
1. Reproducibility Issues:
Code not available during review process. The statement "code will be available publicly" is insufficient for scientific reproducibility. The review process itself should include access to the code and clear instructions for reproducing the results. This is particularly important in computational chemistry where reproducibility should be more straightforward than in experimental settings.

2. Statistical Analysis Deficiencies:
The paper lacks crucial statistical analysis across all results. No uncertainty measurements (standard deviations, confidence intervals) are provided for the accuracy metrics. Without these, it's impossible to determine if the reported improvements are statistically significant or merely random variations. The authors should implement:
     - Multiple trials with different random seeds
     - Standard deviations for all metrics
     - Appropriate statistical significance tests
     - Cross-validation results
     - Confidence intervals for performance metrics


3. Limited Validation:
The authors' claim on page 6, line 295 that "The experiment results validate our hypothesis" is based on just two or three examples. This is methodologically unsound. Such limited examples cannot provide sufficient statistical power or account for the full diversity of chemical reactions. The paper needs:
     - Comprehensive testing across many reaction types
     - Analysis of edge cases and failure modes
     - Statistical validation of the hypothesis
     - Discussion of potential selection bias in examples

4. Technical Clarity Issues:
- The methodology surrounding the Reaction edge introduction requires significant clarification on several fronts. First, there is a citation issue regarding RXNMapper - the authors cite a paper that merely uses RXNMapper rather than the original methodology paper (available at https://chemrxiv.org/engage/chemrxiv/article-details/60c74b2aee301c3c2cc79dac ). This should be corrected to properly credit the original work.
- More substantially, the use of force field calculations for atomic coordinates raises several crucial questions that need to be addressed. The authors mention using MMFF94 to calculate atom coordinates, but provide no details about the conformational analysis. It's essential to know whether they used the lowest energy conformation, how they handled multiple possible conformations, and what impact different conformational choices might have on their results. Given that molecular conformation can significantly affect interatomic distances and geometric parameters, this could have substantial implications for their method's reliability and reproducibility.
- The description of the edge length attribute needs elaboration. While it appears to be based on pairwise distances between selected vertices, the exact methodology isn't clear. If these are indeed simple pairwise distances, how do they account for conformational flexibility? If there's something more sophisticated at play, it needs to be explicitly described.
- A fundamental question arises about whether the reaction graph generation uses products or reactants as its basis. This has important implications for the method's practical applicability. If it uses only reactants, the authors need to explain their methodology for 3D structure generation, particularly regarding the ordering of molecules and the calculation of geometric parameters like bond angles and pairwise distances.
- The handling of molecular geometry deserves special attention. The authors should clarify their approach to calculating bond angles and whether they considered torsion angles in their analysis. The role of molecular conformation in these calculations is particularly important - did they investigate how different conformations affect their results? What criteria did they use to select specific conformations? Was any sensitivity analysis performed to assess the impact of conformational changes on their method's performance?
- Additionally, there's an inconsistency in terminology throughout the paper that needs to be addressed. The authors alternate between using "atoms" for nodes, and "bonds" and "edges" for connections. While these terms are often used interchangeably in chemical graph theory, for clarity and precision, they should establish their terminology early in the paper and maintain consistency throughout. This would help readers better understand the relationship between the chemical and mathematical aspects of their approach.
- These technical details are crucial for understanding the method's limitations and potential applications, as well as for ensuring reproducibility of the results. The authors should provide a comprehensive description of these aspects in their revision.

5. Leaving Group Analysis While the leaving group identification analysis shows promising results, it requires:
- Error analysis of misclassified cases
- Comparison with additional baseline methods
- Cross-validation results
- Discussion of systematic errors or biases
- Analysis of chemical pattern dependencies

6. Runtime Analysis The runtime discussion in section 4.2 lacks essential details
- System specifications
- Benchmark conditions
- Variability in performance
- Hardware dependencies

### Questions
- How will you ensure reproducibility by making code available and providing clear instructions?
- Can you provide comprehensive statistical analysis including standard deviations and confidence intervals?
- What was your methodology for handling multiple possible conformations in the MMFF94 calculations?
- Could you clarify whether reaction graph generation uses products or reactants as its basis?
- How do different conformations affect your results and what criteria were used for conformation selection?
- Can you expand the leaving group analysis with error analysis and comparison to additional baselines?
- Will you provide detailed runtime analysis including system specifications and benchmark conditions?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 7

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents a new method, Reaction Graph, for modeling chemical reactions. The main contributions include:

1. Constructing a reaction graph that captures interatomic relationships in both reactants and products.
2. Incorporating 3D structural information into reaction modeling.

Extensive experiments validate the effectiveness of the proposed method across various tasks related to chemical reactions.

### Strengths
1. The paper is well-written and easy to understand.
2. The motivation for introducing a reaction graph to unify reactants and products in reaction modeling is clear and reasonable.
3. The authors conducted comprehensive experiments across three different chemical reaction tasks, demonstrating the effectiveness of the proposed method.

### Weaknesses
1. The concept of unifying reactants and products seems incremental (modeling individual molecules -> unifying reactants/products (Rxn Hypergraph) -> unifying both reactants and products (Reaction Graph)).
2. The idea of utilizing 3D structures has been extensively explored in molecular modeling, and thus the novelty of extending its application to reaction modeling is limited.
3. The efficiency analysis is insufficient, both experimentally and theoretically. Experimentally, the paper compares the efficiency of the proposed method with and without 3D structure information, rather than against other baseline methods. Theoretically, the complexity analysis in Appendix E.1 focuses solely on graph size without providing a formal complexity calculation of the entire computation process. Additionally, the authors should account for the additional computational burden in preprocessing steps (such as atomic mapping prediction).

### Questions
1. Is it possible to model the interactions between reactants and products by simply adding another hypernode in the Rxn Hypergraph method (connecting to the existing hypernodes of reactants and products)?
2. In the attention-based aggregation process (Line 230), why the authors choose the LSTM-based method which is relatively old (in 2016)? Have the authors explored more recent techniques such as SetTransformer[1]?

[1] Lee et al. Set transformer: A framework for attention-based permutation-invariant neural networks. In ICML, 2019.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 8

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper is focused on the problem of modelling chemical reactions using machine learning techniques. The potential application of this work lies within the material science domain, primarily in Chemistry and drug design. 
The authors introduce the concept of Reaction Graph (RG), which is a graph representation enhanced by 3D structural information.  

One of the key objections against previous methods in the field of study is that so-called "reaction information" that is relevant to the understanding of chemical reactions is usually overlooked and not used. In previous reaction modeling works, the main focus is still molecular representation learning. With that in mind, the authors propose a novel unified graph representation that includes a reaction edge. This additional edge links the same atoms on either side of the chemical reaction - from reagents to products respectively, hence, the inductive bias about the reaction itself is preserved during the message passing. 

Experiments were conducted for a wide range of tasks, and the method shows promising results.

### Strengths
The formal requirements are met, and the overall structure of the paper is cohesive. 

 - Fig. 2 is a good example of an illustration of the overall pipeline and model architecture.
 - Novelty in terms of expansion of data representation in chemical reaction modeling.
 - Multiple experiments are performed (reaction condition prediction, reaction yield prediction, etc.), as well as the ablation study.

### Weaknesses
Figures 1 and 3 are overloaded and therefore hard to interpret.

 - Fig. 1 loses its informativity due to the number of subgraphs included. Most of it showcases the schematics of other existing methods, while only the far right is important for the reader (Reaction Graph Pipeline). Since Fig.1 is referenced many times throughout the paper, those references point to a small fraction of the data. I'd suggest thinking about another layout, either several illustrations for several disjoint figures or even removing some unrelated to the contribution of this work illustrations (e.g. Molecule Graph, Rnx Hypergraph). You can still reference these works in the text. 

 - In Fig. 3 it is not clear how to look for the "Attention weight" since the color bar has all the colors for a) different atom types; b) bromo-/amino-/other group highlights. Another question that arises, is what does "Mismatch" imply?


 I would strongly recommend proofreading the article again to correct some sentences and formulations. Examples may include:
 - poor sentence formulation: "If the edge is empty or a reaction edge, the length is set to 0."
 - "...**a** attention-based aggregation..."

### Questions
1) For additional 3D information one can utilize xyz coordinates of atoms, and therefore capture spatial information. Have you considered using coordinates? 

2) During a couple of iterations of message passing, node embedding will get a cumulative update from their second neighbor in the molecule chain. From this perspective, I don't see how angular edges are conceptually any different from the concept of additional message passing in approaches with functional groups [1] or pseudoatoms/neural atoms [2]. Can you elaborate more on this point?

3) In the section "Leaving Group Identification Analysis", could you explain what does "Overall" column have to do with the LvG identification task? 


4) In the subsection "Dataset" of section "4.3 Reaction Condition Prediction" - it isn't clear what was meant by "... construct Pistachio-Condition from the Pistachio database by thorough cleaning and filtering". What was the procedure and what was the purpose of this "filtering" of data?
_____
**References:**

[1] Hajiabolhassan, Hossein, et al. "FunQG: Molecular representation learning via quotient graphs." Journal of chemical information and modeling 63.11 (2023): 3275-3287.

[2] Li, Xuan, et al. "Neural Atoms: Propagating Long-range Interaction in Molecular Graphs through Efficient Communication Channel." The Twelfth International Conference on Learning Representations. 2024.

### Soundness
2

### Presentation
2

### Contribution
2
