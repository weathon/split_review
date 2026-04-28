# Encoding Ontologies with Holographic Reduced Representations for Transformers

- Decision: Reject
- Avg Score: 4.00
- Scores: 6, 3, 3

## Abstract
The ability to encode meaningful structure into deep learning models opens up the potential for incorporating prior knowledge, particularly in fields where domain-specific information is of great importance. However, transformer models trained on NLP tasks with medical data often have randomly initialized embeddings that are then adjusted based on training data. For terms appearing infrequently in the dataset, there is less opportunity to improve these representations and learn semantic similarity with other concepts. Medical ontologies already represent many of the biomedical concepts and define a relationship structure between these concepts, making ontologies a valuable source of domain-specific information. One of the ongoing challenges of deep learning is finding methods to incorporate this domain knowledge into models. Holographic Reduced Representations (HRR) are capable of encoding ontological structure by composing atomic vectors to create structured higher-level concept vectors. Deep learning models can further process these structured vectors without needing to learn the ontology from training data. We developed an embedding layer that generates concept vectors for clinical diagnostic codes by applying HRR operations that compose atomic vectors based on the SNOMED CT ontology. This approach still allows for learning to update the atomic vectors while maintaining structure in the concept vectors. We trained a Bidirectional Encoder Representations from Transformers (BERT) transformer model to process sequences of clinical diagnostic codes and used the resulting HRR concept vectors as the embedding matrix for the model. The model was first pre-trained on a masked-language modeling (MLM) task before being fine-tuned for mortality and disease prediction tasks. The HRR-based approach improved performance on the pre-training and fine tuning tasks compared to standard transformer embeddings. This is the first time HRRs have been used to produce structured embeddings for transformer models and we find that this approach maintains semantic similarity between medically related concept vectors and allows better representations to be learned for rare codes in the dataset, as rare codes are composed of elements that are shared with more common codes.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This  presents a novel approach for embedding medical concepts into deep learning models using Holographic Reduced Representations. This method, which leverages structured domain knowledge from medical ontologies, enhances the Transformer model's capability to handle rare medical terms and accuracy in predictive tasks. The topic matter holds potential for impactful advancements.

### Strengths
Originality:
The authors deserve commendation for their creative integration of medical concepts into deep learning, which is an absolute strength of this paper. By leveraging Holographic Reduced Representations (HRR) to embed structured medical knowledge, they have potentially enhanced the robustness and practical significance of the methodology. This novel use of HRR in the context of deep learning for medical applications sets a new benchmark and opens up avenues for more sophisticated and nuanced models that could transform medical data analysis.

Quality:
The research quality is commendably moderate, detailing the experimental procedures and significance testing methods. However, while it engages in beneficial discussions, there is room for deeper exploration and more rigorous analysis to elevate the robustness of the findings.

Clarity:
The paper is well-structured, with a clear exposition of the problem, methodology, and results. The authors articulate the limitations of current transformer models in processing rare medical terms and effectively convey how their approach addresses these issues. The use of HRR is explained with sufficient detail to be understood by readers who may not be familiar with this representation method.  Particularly noteworthy is the authors' adept use of simple, relatable examples to elucidate the more abstract concepts involved, such as the Holographic Reduced Representations (HRR). This approach significantly aids in demystifying the intricate process for readers who may not be inherently familiar with these techniques.

Significance:
The method introduced in this paper augments the capability of deep learning models to handle intricate medical data, holding promise for the creation of more precise diagnostic tools. This approach has potential implications for the progress of personalized medicine.

### Weaknesses
1. The manuscript could benefit from additional explanations of abbreviations such as "SNOMED CT." A glossary or expanded definitions on first use would aid comprehension, especially for readers unfamiliar with the terminology.

2. References to critical resources like the "MIMIC-IV dataset" are absent. Citing such resources would provide context and allow readers to assess the relevance and applicability of the data.

3. Section 2.1 lacks detailed descriptions of dataset handling procedures, which is not reader-friendly for those not acquainted with the "MIMIC-IV dataset." Providing more detail would enhance reproducibility and understanding.

4. Section 2.2.1 does not adequately explain the rationale behind the chosen ICD mapping approach. Specifically, it is unclear why the authors did not map all ICD-10 codes directly to ICD-9 codes and subsequently to SNOMED CT, but rather employed the separate mapping method described. This decision is perplexing and warrants a thorough justification to understand the advantages or the necessity of the approach taken.

5. The choice of employing a "one-sided Dunnett’s test" in Section 3.2 is not substantiated with an explanation. It is essential for the authors to clarify this methodological decision, especially since the results in Table 1 suggest an overlap in the confidence intervals and a close proximity of mean values between the experimental and control groups. The absence of such a justification leaves readers questioning the appropriateness of the statistical test used in the analysis.

6. While Section 3.3 commendably visualizes "highly frequent codes" and "infrequent codes," the lack of separate predictive performance displays for these two categories in Table 1 is a missed opportunity. This differentiation is, after all, one of the paper's stated goals.

7. Finally, the paper does not sufficiently discuss the limitations of the proposed method. Acknowledging and addressing potential shortcomings would strengthen the paper by providing a balanced view and suggesting directions for future research.

### Questions
After a thorough review of your manuscript, I have compiled a list of questions and suggestions that I believe could enhance the clarity, completeness, and robustness of your study. Addressing these points may significantly improve the manuscript and aid readers in fully understanding your contributions.

1. The manuscript frequently uses the abbreviation "SNOMED CT" without providing a full explanation or definition for readers who may be unfamiliar with the term. Could you please provide a brief description of "SNOMED CT" and its relevance to your work in the introduction or the first instance where it is mentioned?
2. Dataset Citation:The "MIMIC-IV dataset" is a crucial element in your research, yet it lacks a proper citation or reference. Could you please add a citation for the dataset to allow readers to trace the source and potentially reproduce your study?
3. Dataset Processing Details: In Section 2.1, the description of how the dataset was processed is somewhat brief. Providing a more detailed account of the preprocessing steps would be beneficial, especially for readers who are not familiar with the dataset. Could you elaborate on this process?
4. Rationale Behind Mapping Method: Section 2.2.1 does not sufficiently explain the reasoning behind the chosen ICD mapping method. Why did you opt for the particular mapping approach used in the study instead of mapping all ICD-10 codes to ICD-9 codes, and then to "SNOMED CT"? Clarifying the rationale behind this decision would be helpful.
5. The choice of a "one-sided Dunnett’s test" in Section 3.2 requires further explanation. Could you elaborate on the reasons for selecting this test and whether your method adheres to the assumptions of the test? Additionally, if the decision to use Dunnett's test was deliberate, why opt for a one-sided test instead of a two-sided test? Do you have supporting rationale to support this test? The clarity on these points is crucial, especially in light of the overlapping confidence intervals and closely aligned mean values between the experimental and control groups as presented in Table 1.
6. While the visualization of "highly frequent codes" and "infrequent codes" in Section 3.3 is commendable, the performance metrics under these two categories are not separately displayed in Table 1. Displaying results across various scenarios could effectively showcase the effectiveness of your approach, especially since addressing the representation of infrequent codes is one of your stated objectives. Could you include these performance metrics in your results?
7. A discussion on the limitations of the proposed method is noticeably absent. An acknowledgement of potential limitations and constraints of your approach would provide a more balanced view and contribute to the paper’s integrity. Could you add a section discussing these aspects?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a neural-symbolic approach (HRRBERT) for transformers by integrating medical ontologies represented by Holographic Reduced Representations (HRR) embeddings. The methodology involves efficiently constructing vector-symbolic embeddings enabling autograd functionality in PyTorch. The experiments demonstrated that the proposed method represents ontological similarities of the codes better than the learned embeddings of the transformer model, and the method can learn similar embedding vectors for medical codes with similar medical meanings.

### Strengths
* Results show that the proposed method improves over the baselines, and the t-SNE visualizations demonstrate that codes with similar frequencies are presented close together.
* It is good to make the method compatible with PyTorch autograd.

### Weaknesses
 * The performance improvements in the fine-tuning task are not very large.
* The authors claim in their paper that the proposed method is efficient. However, there is no direct comparison with the baselines regarding efficiency, thus making the authors' claims that their method is efficient seem a bit unsupported.
* Evaluation is only performed on the MIMIC-IV dataset collected from a single medical center. Further evaluation of multi-center datasets such as eICU could present further information on the method's usefulness.
* The presentation of the paper needs to be significantly improved. The abstract is too long, and while the details described in the main paper are meaningful, they sometimes break the flow of the paper, making the contents difficult to read. I believe the paper needs a significant overhaul to reach a publishable quality for ICLR.
* (minor) Grammar mistakes and typos can be seen in the paper.

### Questions
Given the small performance boosts demonstrated in Table 1, I wonder under what circumstances we need to adopt the proposed method.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This article addresses the limitations observed in pre-trained language models (PLMs) when generating high-quality embeddings for seldom-encountered terms, especially within the training dataset. With a particular emphasis on the medical realm, the researchers enrich PLMs by integrating medical ontologies and their associated embeddings.

A central feature of this study is the application of Holographic Reduced Representations (HRR) to encode medical ontologies like SNOMED CT into distinct concept vectors. This is achieved by adding an HRR layer to the transformers found in BERT, allowing for the efficient processing of clinical diagnosis codes.

Empirical results indicate that the enhanced HRR-integrated BERT model delivers superior performance compared to its standard counterpart, particularly in the context of rare diseases.

### Strengths
This study delves into the intriguing concept of integrating ontological knowledge with pre-trained language models built on transformer layers. Such an approach holds significant promise and will likely captivate those looking to modify or enrich Large Language Models (LLMs) with additional knowledge in future research.

### Weaknesses
 - **Methodological Novelty**: While the paper introduces Holographic Reduced Representations (HRRs) into the training of transformer layers, it doesn't clearly articulate innovative techniques or strategies for their integration with transformers and the special challenges into dealing with medical ontologies. The description lacks detail on how the HRR vectors are incorporated into the transformer architecture, specifically how the HRR concept vectors interact with the attention mechanism and the feed-forward networks within the transformer layers. It is unclear if the HRR vectors are simply concatenated, added, or if a more complex interaction is employed. Furthermore, the paper does not discuss the computational challenges of using HRRs, such as the potential for increased memory usage or the need for specialized operations, and how these challenges are addressed.

- **Experimentation**: The presented experiments seem insufficient to conclusively establish the superiority of the proposed methods. As evidenced by Table 1 and Fig. 1, the various BERT adaptations demonstrate comparable performances. Furthermore, there's a noticeable absence of comparisons with other foundational benchmarks within the disease diagnosis domain. The experiments do not explore the sensitivity of the model to different hyperparameters, such as the dimensionality of the HRR vectors or the learning rate of the HRR layer. The lack of ablation studies makes it difficult to understand the contribution of each component of the proposed model. Additionally, the paper does not provide a clear rationale for the choice of evaluation metrics, and it is unclear if these metrics are appropriate for the specific task of disease diagnosis.

- **Reproducibility**: To faithfully replicate the study's findings, more detailed information is necessary. Specifically, clarity on the dataset employed, the design of the architectural models, and the implementation specifics of all the variant baselines would be indispensable. The paper lacks details on the preprocessing steps applied to the medical ontologies and the clinical data. The specific versions of the libraries used, such as PyTorch and Transformers, are not mentioned, making it difficult to reproduce the results. Furthermore, the paper does not provide information on the hardware used for training and evaluation, which can significantly impact the performance of deep learning models.

### Questions
- Fig. 1: Why does the HRRBase have such a noticeably lower score compared to the other methods? Does this suggest that HRRBase is the least effective?

- Table 1: While the performances of all methods seem to be on par, what distinguishes HRR from the unstructured approach in terms of advantages?

- Figure 2: Why is there no visualization for the control method, 'Unstructured'? Given that the embedding spaces in the current Figure 2 appear quite analogous, what's the primary takeaway or message from this representation?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
