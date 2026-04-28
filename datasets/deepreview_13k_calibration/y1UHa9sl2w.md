# OntoFAR: Hierarchical Multi-Ontology Fusion Better Augments EHR Representation

- Decision: Reject
- Avg Score: 5.40
- Scores: 5, 6, 6, 5, 5

## Abstract
Medical ontology graphs, which typically organize and relate comprehensive medical concepts in a hierarchical structure, are able to map a rich set of external knowledge onto the specific medical codes observed in electronic health records (EHRs). Through the connectivity in ontologies, healthcare predictive models can utilize the ancestor, descendant, or sibling information to add supplementary contexts on medical codes, thereby augmenting expressiveness of EHR representations. However, existing approaches are limited by the heterogeneous isolation of different ontology systems (e.g., conditions vs. drugs), that different types of ontology concepts have to be learned individually, and only the homogeneous ontology relationships can be exploited. This limitation restricts the existing methods from fully leveraging the cross-ontology relationships which could substantially enhance healthcare representations. 
In this paper, we propose OntoFAR, a framework that fuse multiple ontology graphs, utilizing the collaboration across ontologies to enhance medical concept representation. Our method jointly represents medical concepts cross multiple ontology structures by performing message passing in two dimensions: (1) vertical propagation over levels of ontology hierarchy, and (2) horizontal propagation over co-occurring concepts in EHR visits. Additionally, OntoFAR leverages the large language models (LLMs) pre-trained on massive open world information to understand each target concept with its ontology relationships, providing enhanced embedding initialization for concepts. Through extensive experimental studies on two public datasets, MIMIC-III and MIMIC-IV, we validate the superior performance of OntoFAR over the state-of-the-art baselines. Beyond accuracy, our model also exhibits the add-on compatibility to boost existing healthcare prediction models, and demonstrate a good robustness in scenarios with limited data availability. The implementation code is available at [https://anonymous.4open.science/r/OntoFAR-35D4](https://anonymous.4open.science/r/OntoFAR-35D4)

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces OntoFAR, a framework designed to enhance medical concept representations by leveraging multiple ontology graphs to enrich electronic health record (EHR) data. OntoFAR aims to address limitations in existing EHR models that often treat different ontologies (e.g., conditions, drugs) in isolation, thereby missing out on potentially valuable cross-ontology relationships. 

This framework achieves improvement through a dual-directional message passing mechanism: Vertical Message Passing (VMP) within individual ontology hierarchies and Horizontal Message Passing (HMP) across co-occurring medical codes in EHR visits.

However, the proposed methodology was evaluated on a limited set of datasets and prediction tasks, showing only marginal performance gains. This raises concerns about its model generalizability. Also, the fact that it needs LLM (embeddings initialization) for training relatively small predictive models could raise the efficiency issues.

Additionally, the methodological approach lacks substantial novelty from a machine learning perspective. It primarily relies on modeling co-occurrences of codes within visits, which aligns closely with techniques already present in existing graph-based EHR predictive models, offering limited new contributions to the field.

### Strengths
1. Incorporation of Heterogeneous Ontology Motivation: The paper provides a strong motivation for utilizing heterogeneous ontologies, emphasizing the need for integrating multiple medical ontology systems to improve healthcare predictive models.

2. Demonstration of Model Strength through Comparative Experiments: Through extensive experiments comparing OntoFAR with existing methods, the paper demonstrates the model's superiority in predictive performance, particularly on tasks using real-world medical datasets like MIMIC-III and MIMIC-IV.

3. Evidence of Medical Ontology as a Key Feature in Predictive Models: The results indicate the significance of medical ontology in enhancing predictive accuracy, showing that it can serve as a critical feature in medical concept representation, effectively boosting the model's robustness and interpretability.

### Weaknesses
1. Proposed model novelty and contributions

(a) Effectiveness of LLM-based Initial Embedding: Results in Table 3 indicate that initializing embeddings with an LLM significantly improves performance. Further clarification is needed on how this initialization contributes to the overall performance of OntoFAR, as well as details on the LLM prompt design strategy. Additionally, it would be informative to assess the impact of initializing embeddings with Clinical-BERT, which is specifically trained on MIMIC medical concepts.

(b) VMP and HMP Design and Interpretation: VMP applies an established concept, and HMP seems to rely on a co-occurrence-based graph attention mechanism, which is a pre-existing technique. Although combining these two approaches appears to be a central contribution of the paper, it is unclear if HMP’s co-occurrence-based construction fully leverages inter heterogeneous medical ontologies. A more explicit discussion is needed on whether combining various ontologies in this way can genuinely contribute to model performance. (Author mentioned co-occurrence based model is utilization of "inter ontology".)

(c) Co-occurrence and Predictive Model: At the visit level, co-occurrence information may already be incorporated within the predictive model itself. If this is the case, it is unclear what additional benefits the medical concept encoder provides, even in Table 3 where HMP is highlighted. This rationale could benefit from further elaboration.

2. Limitations in Experiment Setup and Dataset Diversity

(a) Lack of Diversity in Predictive Models: Table 2 evaluates different medical concept encoders with transformer as the predictive model, yet same experiment results for RETAIN and TCN, which are shown in Table 1, are not included. Including similar results for RETAIN and TCN would provide a more comprehensive assessment of the model’s generalization capabilities.

(b) Limited Task Scope: This paper primarily focuses on a single task, sequential diagnosis prediction for the next visit. Expanding the evaluation to additional tasks would better demonstrate the generalizability and broader applicability of the proposed representations.

(c) Dataset Diversity: The experiments are conducted solely on the MIMIC dataset, which limits insights into the model’s robustness across datasets. Testing the model on additional datasets would strengthen evidence of its generalizability.

3. Model Evaluation and Performance

(a) Usage of Embeddings: Clarification is needed on whether the embeddings generated by the medical concept encoder are fixed or serve solely as initial embeddings. For example, GRAM, which serves as a baseline, uses an end-to-end approach with predictive model. Is OntoFAR primarily used to provide only initial embeddings for code representation?

(b) Marginal Improvement in Performance: The proposed model demonstrates only marginal performance gains, which makes it difficult to establish a clear advantage over existing approaches. This is especially evident when LLM embedding initialization is excluded, where the performance improvement seems negligible.

### Questions
1. Related Work: Additional discussion on how the proposed model distinctly differs from related studies would be beneficial. Clarifying the relationship between prior work and the proposed model would enhance the understanding of OntoFAR's unique contributions.

2. HGIP in Table 3: In Table 3, HGIP appears to exclude VMP. Does this mean that message passing was not applied at all, and were using the embeddings initialized by LLM used without further updates?

### Soundness
3

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
2

### Summary
The paper proposes OntoFAR, a framework that enhances EHR predictive modeling by integrating multiple medical ontologies. It introduces dual-dimensional message passing (vertical and horizontal) to enrich medical concept representations and uses LLMs for embedding initialization. The approach is validated on MIMIC-III and MIMIC-IV datasets, demonstrating superior performance over baselines and robustness in data-limited scenarios.

### Strengths
1. **Novel Idea with Cross-Ontology Integration**: 

The proposed new method is able to capture relationships between different medical code types, enhancing representation.

2. **Robust Embedding Initialization**: 

It is interesting and effective to leverage LLMs for enhanced concept embedding with external knowledge.

3. **Data Insufficiency Resilience**: 

The author also performs additional experiments to prove that the proposed method maintains strong performance even with limited data availability.

### Weaknesses
 **Substantive Assessment of Weaknesses**

1. **Insufficient Justification of Improvements and Potential Gaps in Related Work**:

While the paper proposes a multi-ontology framework to enhance EHR predictions, which is a well-explored domain, the authors' claims regarding the uniqueness and superiority of their approach are not convincingly substantiated. Integrating knowledge graphs (KGs) to improve EHR prediction is an established area with significant recent advancements. While the paper notes some limitations in current methods, it does not ensure that these criticisms translate into performance gains over state-of-the-art approaches. Notably, the comparison set lacks recent, relevant KG-based EHR prediction methods such as KerPrint [1], KAMPNet [2], and MedPath [3].

In particular, KAMPNet [2] presents a multi-source and multi-level graph framework similar in concept to the proposed OntoFAR, suggesting an overlap that should be clarified. To strengthen the paper, I recommend including these contemporary works as baselines to provide a comprehensive comparison. Additionally, a detailed discussion explaining how OntoFAR differs from and advances beyond KAMPNet’s multi-level graph strategy would be essential to highlight its distinct contributions.

### Questions
1. What is the difference between the proposed work and the KAMPNet [2]?
2. The last tested baseline is HAP (2020) and there are many following works during the last four years why they are not included.


**References**:
1. Yang K, Xu Y, Zou P, et al. *KerPrint: local-global knowledge graph enhanced diagnosis prediction for retrospective and prospective interpretations*. Proceedings of the AAAI Conference on Artificial Intelligence, 2023, 37(4): 5357-5365.
2. An Y, Tang H, Jin B, et al. *KAMPNet: multi-source medical knowledge augmented medication prediction network with multi-level graph contrastive learning*. BMC Medical Informatics and Decision Making, 2023, 23(1): 243.
3. Ye M, Cui S, Wang Y, et al. *Medpath: Augmenting health risk prediction via medical knowledge paths*. Proceedings of the Web Conference 2021. 2021: 1397-1409.

### Soundness
3

### Presentation
3

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
The authors propose a framework named OntoFAR for enhancing medical concept representation in EHRs by fusing multiple medical ontologies. It enables message passing both vertically and horizontally to capture richer cross-ontology relationships. OntoFAR constructs a unified Meta-KG initialized with embeddings from pre-trained language models, and effectively integrates medical concept information across ontologies. Evaluations on MIMIC-III and MIMIC-IV datasets demonstrate OntoFAR’s superior predictive performance and robustness, especially in data-limited scenarios, over existing EHR representation methods.

### Strengths
1. The paper addresses the crucial real-world issue of diagnosis prediction. They effectively integrate multiple ontologies to enhance predictions and resolve alignment challenges among different ontologies.
2. The authors present comprehensive experimental results from various perspectives, including many ablation studies and additional analyses that deepen the understanding of their findings.
3. The figures and tables in the paper are well-designed and contribute significantly to clarifying the framework and interpreting the results.

### Weaknesses
1. The comparison with the baselines does not seem to be fair. The proposed framework OntoFAR utilizes the GPT text embedding model for the embeddings of medical concepts, which is a much more powerful model than those used by the baselines. The ablation studies presented in Table 3 show that removing this part (w/o LLMs) results in performance on par with the baselines. This somehow suggests that OntoFAR might not truly outperform the baselines without the advantage of using this more powerful embedding model for a fair comparison.
2. The baselines used in the paper are ranging from 2017 to 2020, which are kind of outdated. It's better for the authors to consider more recent baselines, such as SeqCare [1] and other studies mentioned in the related works section (e.g., GraphCare, MedPath, RAM-EHR).
3. The notations in the method section are overly complex and could be much simplified. Many of the notations currently used are not essential.

Typos and formats:
- The referencing style throughout the paper is not correct; it should use parentheses (i.e., \citep{} instead of \cite{}).
- "Figure 3" in line 442 should be "Table 3"

### Questions
1. What's the base model in Figure 3?

### Soundness
3

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
4

### Summary
The paper proposes a new unified framework that incorporates hierarchical information from multiple ontologies to augment patient representation in electronic health records. The idea is by incorporating multiple ontologies, the model can leverage cross-ontology relationships to fully leverage existing medical knowledge bases. The framework is evaluated against various baselines on two different datasets.

### Strengths
* A unified framework for incorporating multiple ontologies where each ontology can have different hierarchical structures.
* Extensive experiments using different graph backbones (GAT and HAT), different diagnosis prediction models (transformer, RETAIN, and TCN), and 2 datasets (although there is some overlap between the two datasets).
* A case study to demonstrate how the hierarchical and co-occurrence codes can help learn a better embedding representation.

### Weaknesses
 * The paper fails to mention and benchmark against ADORE (Adaptive Integration of Categorical and Multi-relationalOntologies with EHR Data for Medical Concept Embedding by Cheong et al. 2023) which incorporates a multi-relational medical ontology, SNOMED-CT which combines medications and diagnoses into a single representation.
* There are different knowledge bases such as SNOMED-CT, CCS, and several others even for the diagnosis. Is there a reason why only one knowledge base is explored for diagnosis and/or medication (SNOMED-CT works for medication as well)? 
* Only a single downstream task is benchmarked and OntoFAR is introduced as being beneficial for a variety of tasks. How does the embedding perform on other tasks like mortality prediction or readmission prediction for either of the datasets (it does not need to be both)?
* Given MIMIC-III and MIMIC-IV share the same dataset, it would be helpful to benchmark against something that is likely to have different patients. eICU is a good example of a potential open-source dataset (there is some shared with MIMIC but there is also some outside ones). 
* The methodology section is quite dense and a bit hard to parse especially when trying to ascertain how information is shared across the different ontologies. It would be helpful to provide an example using ATC and ICD-9 hierarchy. Based on Figure 1, GAT or HAT are the mechanisms for sharing information across the same concept level across ontologies but this isn't made explicit.
* The citation style is incorrect, you should swap it to \citep as the default instead of \cite.

### Questions
* Why are OpenAI off-the-shelf LLMs used when there are many other open-source LLMs available? How sensitive is the performance to the quality of the embeddings from the LLM?
* How does your model compare against ADORE?

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
3

### Summary
The paper introduces OntoFAR, an innovative framework designed to enhance the representation of medical concepts by integrating multiple medical ontology graphs. These graphs typically structure medical knowledge hierarchically and relate it to the medical codes used in electronic health records (EHRs). Current methods are limited by their inability to cross-reference information across different ontological and are restricted to using relationships within the same ontology. OntoFAR overcomes the limitations of previous approaches by fusing multiple ontologies. This is achieved through both vertical and horizontal message passing—vertical across different levels of the ontology hierarchy and horizontal across co-occurring concepts within EHR visits.

### Strengths
Originality: The OntoFAR framework introduces a novel approach to integrating multiple medical ontology graphs, enabling both horizontal and vertical message passing across these ontologies. This method of cross-ontology relationship exploitation is innovative in its bidirectional propagation mechanism, which is distinct from existing works that typically focus on single ontology systems or unidirectional information flow.

Quality: The paper is methodologically rigorous, presenting a clear and systematic approach to the multi-ontology integration problem. The proposed framework, OntoFAR, is well-constructed with detailed descriptions of its components.

Significance: The significance of this work lies in its potential to enhance the accuracy and robustness of predictive healthcare models by leveraging a richer representation of medical concepts derived from multiple ontologies.

### Weaknesses
1) The main weakness of the paper lies in its evaluation:

- The approach is evaluated solely on the task of sequential diagnosis prediction, which restricts the assessment of OntoFAR's effectiveness. To explore the benefits of integrating multiple medical ontology graphs for different types of medical concepts, the approach should be tested on a variety of tasks that utilize diverse concepts. The current evaluation does not sufficiently demonstrate the generalizability of the learned representations to other clinically relevant tasks, such as mortality prediction or risk stratification.

- The experiments are conducted on MIMIC-III and MIMIC-IV, which originate from the same healthcare provider (Beth Israel Deaconess Medical Center in Boston). Additionally, both databases contain overlapping admissions from 2008 to 2012, which limits the diversity of the data used in the study. Evaluating the approach in other datasets, ideally from different healthcare systems and patient populations, is essential for understanding its applicability and robustness across different settings. The lack of external validation raises concerns about the potential for overfitting to the specific characteristics of the MIMIC datasets.

- When comparing the performance of OntoFAR with other existing medical ontology structure encoders, authors should also indicate the size of each model (number of trainable weights). The observed performance increase for OntoFAR may be due to an enlargement of the model relative to other methods, rather than its effectiveness in learning superior medical concept representations. Without controlling for model size, it is difficult to attribute performance gains solely to the proposed methodology.

2) In general, the writing requires significant improvements. For example, line 171: “work depicted Figure 1” should be corrected to “work depicted in Figure 1”; additionally, there are multiple typographical errors, such as the use of “massage” instead of “message” multiple times.

### Questions
- Authors need to clarify the meaning of “Pr” in equation 1.

- Additional clarification on how to aggregate clinical events embeddings from the matrix “Z” to obtain a single visit representation is needed (lines 333-335).

- In line 442, the authors likely mean “Table 3” instead of “Figure 3”. Similarly, in line 500, they might intend to refer to “Right” instead of “Left”.

- The authors should describe the elements in Fig. 6, such as the meaning of the nodes based on their color, to enhance understanding of the figure’s components.

### Soundness
3

### Presentation
2

### Contribution
2
