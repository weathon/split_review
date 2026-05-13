# MeToken: Uniform Micro-environment Token Boosts Post-Translational Modification Prediction

- Decision: Accept
- Scores: 8, 5, 5, 6, 5

## Abstract
Post-translational modifications (PTMs) profoundly expand the complexity and functionality of the proteome, regulating protein attributes and interactions that are crucial for biological processes. Accurately predicting PTM sites and their specific types is therefore essential for elucidating protein function and understanding disease mechanisms. Existing computational approaches predominantly focus on protein sequences to predict PTM sites, driven by the recognition of sequence-dependent motifs. However, these approaches often overlook protein structural contexts. In this work, we first compile a large-scale sequence-structure PTM dataset, which serves as the foundation for fair comparison. We introduce the MeToken model, which tokenizes the micro-environment of each amino acid, integrating both sequence and structural information into unified discrete tokens. This model not only captures the typical sequence motifs associated with PTMs but also leverages the spatial arrangements dictated by protein tertiary structures, thus providing a holistic view of the factors influencing PTM sites. Designed to address the long-tail distribution of PTM types, MeToken employs uniform sub-codebooks that ensure even the rarest PTMs are adequately represented and distinguished. We validate the effectiveness and generalizability of MeToken across multiple datasets, demonstrating its superior performance in accurately identifying PTM types. The results underscore the importance of incorporating structural data and highlight MeToken's potential in facilitating accurate and comprehensive PTM predictions, which could significantly impact proteomics research.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The work aims at creating a structure and sequence-based representation of microenvironment  of the  residues and use this for post-translational modification (PTM) classification. They compile a large-scale sequence-structure PTM dataset featuring over 1.2 million residue-level annotated sites across multiple PTM types. The method MeToken tries to capture the context of the site using the sequential and structural neighbourhood of the modified residue. The paper learns a codebook that represents the high-dimensional data into simpler, representative tokens. The work is interesting contribution to the field.

### Strengths
- The authors use valid strategies for experimental evaluation. For example, they take into account sequence similarity to prevent leakage in the evaluation. Uses appropriately macro-avearged evaluation metrics. Many decisions are based on valid reasons or experimentation (using ESM-2 vs ESM3) and (PDB vs AlphaFold+PDB vs AlphadFold) 
- Results on two external datasets are provided. 
- The work is interesting in the sense that it uses the structural features of the modified site together with the sequence
- Authors compare against existing PTM models and wider protein language models. They have modified some of the specialized models such as DeepPhos to evaluate for the general PTM classification task.
- Authors provide an ablation study to understand the contribution of the different parts of the method

### Weaknesses
Weakness:

A simple baseline of one-hot encoded amino acid sequence representations would be useful to see if certain classes can easily be predicted based on their modification site.

The authors could compare their work to other structure-aware representations. For example, SAProt using the Foldseek structural tokens learns a sturture aware embedding.

The authors demonstrate one of the codebooks as an example but a more extensive analysis on this would be interesting. For example a very basic question would be : "Are the amino acid preferences (K for Sumoylation, S/T/Y for Phosphorylation, etc )correctly captured by the codebooks?"

Information on the hyperparameters used to train MeToken and the baseline models are needed for reproducibility of the results.

A hyperparameter sensitivity analysis would be useful. For example the codebook size, the number of neighbors in the k-nn graph etc. 

Distinguishing some PTMs from others are easier because of the distinct amino acid preferences in their modification sites. Hard evaluation sets up could have been designed to understand the weakness and the strength of the methodology. For example, does the model correctly differentiate a Lysine residue  being ubiquninated or sumoylated?

The authors do not provide results on performance across different PTM classes. Are certain PTMs are much easier because of the available training data?

### Questions
Questions 
How are the no-modification sites determined? Are these all sites in protein sequences where no modifications are reported or are they subsets based on amino acid types?

Is the quantization technique and the codebook strategy different than the cited work FoldToken? The differences and similarities should be included in the relevant literature part as it is very closely related to the work introduced here.
Of the many structures available for a protein in the PDB, which one is selected ? What criteria are applied on this selection?
Authors suggest that they introduce a sub-codebook strategy to handle the long-tail distribution but at the end of the day, all the rare classes are grouped as a single class. How does that help?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposed a pipeline to predict PTMs (mostly in residue level as opposed to other global level) by addressing the issue of lacking structural information in the modeling. Additionally they curated a new dataset for such task as added contribution. Through comparison with baselines and some ablation studies, they show the better performance of the method

### Strengths
The raised challenges in the current landscape of PTMs prediction are legit. These issues make both modeling and evaluation in the domain difficult, thus the claim for such challenge is of high relevance.

The introduction of MeToken Model, that tokenizes amino acids’ micro-environments by integrating both sequence and structural information into discrete tokens, is relevant (although it seems like most of the boost is from this innovation so it begs the questions why the latter two, see below Weakness comments)

To handle the long-tail distribution of PTM types, MeToken introduces a sub-codebook strategy which arguably serves as a regularizer for the model to learn canonical representations

### Weaknesses
The hypothesis that incorporating structural data into PTM prediction can improve accuracy is well-supported by prior research indicating that sequence-only approaches may overlook important spatial context. But from table 4 it seems like this has enough boost compared to other baselines. It's beneficial to investigate deeper (and perhaps more ablation studies on only this arm of contribution) to stress the importance of added benefit of structural information.

Additionally, ESM-2 baseline seems to be very close the proposed method and beats all other baselines so there's still arguably a lot of sequence information that's useful already, so how to showcase their method is not overfitting to structural features might help reviewers to understand the validity of their method.

Again, the latter contributions, uniform sub-codebook strategy and temperature-scaled vector quantization, seems to offer marginal benefit which IMO dilutes the core contribution brought by the Micro-env arm of contribution. In addition, the temperature adjusted approach might necessitate a huge effort for hyperparameter tunning to make it work. But the authors didn't discuss any ramification of it. Further, the uniform sub-codebook strategy might risk embedding redundancy for common PTM types, and this was not discussed either.

### Questions
They highlighted the long tail nature of the current datasets in the domain but it lacks some deeper analysis for the distribution e.g. rarity analysis, frequency statistics. It's unclear the extent to which the long tail nature is currently at play for the modeling difficulty in the domain, as what they claimed as a challenge. Additionally, reducing the class imbalance by consolidating PTM types with fewer than 100 samples into a single “rare sites” category might be exacerbate the imbalance issue? The rare classes are not modeled/studied individually then

Also, UMAP is often better at preserving global structure in the final projection. This means that the inter-cluster relations are potentially more meaningful than in t-SNE. So might want to suggest the authors to compare that visualization (see appendix c: https://arxiv.org/pdf/1802.03426)

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
4

### Summary
MeToken introduces a novel approach to PTM prediction by integrating sequence and structural data through micro-environment tokenization and a uniform codebook, enhancing model performance across diverse PTM types. The model shows good results but relies on AlphaFold data and lacks evaluation on biological interactions, suggesting areas for future refinement.

### Strengths
1. Proposes MeToken that effectively integrates sequence and structural data in PTM prediction. This foresighted approach to using micro-environment tokenization and uniform sub-codebook construction demonstrates promising results in addressing the long-tail distribution of PTM types.
2. Extensive experiments across datasets validate the model's performance, showing significant improvements in metrics such as F1-score and AUPRC over competitive baselines. The experiments reveal that MeToken captures complex biochemical contexts well, potentially setting a new benchmark for PTM prediction.

### Weaknesses
1. The reliance on AlphaFold-generated data may limit its generalizability in real-world applications where experimental structures are less available or differ significantly. The accuracy of AlphaFold predictions can vary, particularly for flexible regions or proteins with limited sequence homology to known structures, potentially introducing bias into the model's training and evaluation. This is especially concerning given that PTMs often occur in structurally dynamic regions, where AlphaFold's predictions might be less reliable.
2. Although the authors address the dimensionality reduction challenge, computational complexity remains an issue, especially given the additional steps in codebook learning and temperature-scaled quantization. The computational overhead of these steps, including the iterative codebook learning and the temperature-scaled quantization, may hinder the model's scalability to large datasets or high-throughput applications. The practical implications of this computational burden, such as increased training time and resource requirements, need to be addressed.
3. The study focuses primarily on PTM types without including interactions with enzymes or other proteins, which are crucial for PTM formation and regulation in vivo. The absence of considerations for enzyme-substrate interactions and other protein-protein interactions neglects a critical aspect of PTM regulation. This simplification may limit the model's ability to capture the complex biological context of PTMs and its applicability in real-world scenarios.

### Questions
MeToken's design, with its uniform sub-codebooks and temperature-scaled quantization, may introduce significant computational demands, especially in high-dimensional cases. Have you explored options like pruning or adaptive quantization to mitigate these costs? This could clarify MeToken’s efficiency for large-scale deployment. Another question is that as protein-protein interactions, particularly with enzymes often influence PTM sites, could you consider ways to include these relationships in MeToken’s predictions? Addressing this would potentially expand the model’s real-world applicability and accuracy in cellular contexts.

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
This paper compiles a large-scale sequence-structure PTM dataset and also propose METoken which uses sub-codebooks for each of the subtypes and temperature scaled vector quantization. On top of the the codebooks and learned tokens for micro-environment of the protein positions it then predicts PTM and its type.

### Strengths
The ablation and comparisons are done and results are reported on various useful metrics like F1, MCC and others.

### Weaknesses
It is not clear how the sequence similarity or redundancy was mitigated in the train-test-validation sets. Please report how minimal redundancy was ensured among test-train and validation sets.

In the rare modification class, how good is the predictor to discriminate the classes is not made clear. In this case authors may consider to report the different metrics for the PTM classes merged.

There are datasets and methods which are specifically learned for particular type of PTM and that has been a trend in the literature. Please report how does those methods perform comapred to METoken.

### Questions
How is the imbalance in the samples for no modification class affects the classification? Particularly the merged small PTMs and no modifications.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
PTM prediction is a very important topic in bioinformatics. This study introduces the MeToken model to consider the micro-environment of amino acids for PTM prediction. The proposed method has shown promising results in performance evaluation tests.

### Strengths
The authors incorporated the protein structural data to enhance the prediction, which is good as structural information could be better presented the functional-related information.

### Weaknesses
Some descriptions are not very accurate, and the progress of some existing studies is ignored. The model's ability to differentiate between the four PTM types (chemical groups, proteins/peptides, complex molecules, and cleavage) based on structural preferences is not clearly demonstrated. The claim that existing computational approaches predominantly focus on protein sequences is inaccurate, as many graph-based and structure-aware methods have been developed.

### Questions
1. PTMs can be summarised into four types according to the modification types: chemical groups (e.g. Phosphorylation, Acetylation), proteins/peptides (e.g. Ubiquitylation, Sumoylation), complex molecules (e.g. glycosylation), and cleavage (proteolysis). These four types could have different structural preferences. How can the proposed model capture the differences between them? Which types work well using the proposed method?
2. The description "Existing computational approaches predominantly focus on protein sequences to predict PTM sites" in the Abstract is not accurate. There are many graphs and structural-aware methods that have been developed and published.
3. The authors are suggested to provide some biological case studies to interpret the micro-environment tokenization related to the characteristics of PTMs in the biological context.
4. The source codes and datasets should be publicly available upon acceptance.

### Soundness
3

### Presentation
3

### Contribution
3
