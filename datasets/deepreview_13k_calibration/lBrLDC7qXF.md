# CAB-KGC: Context-Aware BERT for Knowledge Graph Completion

- Decision: Reject
- Avg Score: 3.60
- Scores: 3, 3, 6, 3, 3

## Abstract
Knowledge graph completion (KGC) seeks to predict missing entities (e.g., heads or tails) or relationships in knowledge graphs (KGs), which often contain incomplete data. Traditional embedding-based methods, such as TransE and ComplEx, have improved tail entity prediction but struggle to generalize to unseen entities during testing. Textual-based models mitigate this issue by leveraging additional semantic context; however, their reliance on negative triplet sampling introduces high computational overhead, semantic inconsistencies, and data imbalance. Recent BERT-based approaches, like KG-BERT, show promise but depend heavily on entity descriptions, which are often unavailable in KGs. Critically, existing methods  overlook valuable structural information in the KG related to the entities and relationships. To address these challenges, we propose Context-Aware BERT for Knowledge Graph Completion (CAB-KGC), a novel model that utilizes contextual information from linked entities and relations within the graph to predict tail entities. CAB-KGC eliminates the need for entity descriptions and negative triplet sampling, significantly reducing computational complexity while enhancing performance. Additionally, we introduce the Evaluation based on Distance from Average Solution (EDAS) criterion to the KG domain, enabling a more comprehensive evaluation across diverse metrics. Our experiments on standard datasets, including FB15k-237, WN18RR, CoDEx-S, and ConceptNet100K, demonstrate that CAB-KGC outperforms state-of-the-art methods on three datasets. Notably, CAB-KGC achieves improvements in Hit@1 of 6.88\%, 14.32\%, and 17.13\% on WN18RR, CoDEx-S, and ConceptNet100K, respectively. Furthermore, EDAS rankings establish CAB-KGC as the top-performing model, highlighting its effectiveness and robustness for KGC tasks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a novel approach for Knowledge Graph Completion (KGC) named Context-Aware BERT for Knowledge Graph Completion (CAB-KGC). The goal of CAB-KGC is to predict missing entities or relationships in knowledge graphs by leveraging contextual information. Unlike traditional embedding-based methods that struggle with unseen entities and relationships, CAB-KGC utilizes the contextual data from neighboring nodes and relationships, integrating these insights with a BERT-based architecture to enhance prediction accuracy for tail entities. 
The authors also propose a new evaluation metric, Evaluation based on Distance from Average Solution (EDAS), to address potential inconsistencies in existing metrics like Mean Reciprocal Rank (MRR) and Hit@k. EDAS provides a more comprehensive assessment by considering deviations from average performance across several criteria. 
CAB-KGC is evaluated against state-of-the-art KGC methods on benchmark datasets FB15k-237 and WN18RR, showing improvements in standard metrics, particularly in Hit@1 and MRR. The experimental results demonstrate that CAB-KGC outperforms baseline methods across different datasets, indicating that incorporating both head and relationship contexts into BERT can improve KGC model accuracy. The paper also includes ablation studies to validate the contributions of each component within the CAB-KGC model, showing that combining head and relationship contexts yields the best results.
CAB-KGC addresses limitations in current KGC approaches by utilizing both structural and contextual information without relying on negative sampling or entity descriptions, and the EDAS metric offers an alternative way to rank model performance comprehensively.

### Strengths
1.	Introduction of CAB-KGC for Knowledge Graph Completion: The paper presents a novel method, CAB-KGC, which leverages context-aware information from both head entities and relationships. This is an original approach for enhancing knowledge graph completion tasks, aiming to address limitations of existing embedding-based and LLM-based models. 2.
2.	Proposal of EDAS as a New Evaluation Metric: The introduction of the EDAS (Evaluation based on Distance from Average Solution) metric is a unique contribution. EDAS aims to offer a more comprehensive assessment by incorporating both positive and negative deviations, which could provide a more nuanced evaluation of model performance, especially on ranking tasks. 
3.	Comparative Experimental Results: The paper conducts extensive experiments comparing CAB-KGC with multiple state-of-the-art methods, particularly on FB15k-237 and WN18RR datasets. The results demonstrate that CAB-KGC achieves competitive performance, with notable improvements on the Hit@1 metric.

### Weaknesses
1. Formatting and Layout Issues:

•	The paper has several formatting inconsistencies that detract from its professionalism. For instance, the template content for acknowledgments has not been removed from the end of the main text, which is distracting and unpolished.

•	In the appendix, there are large blank spaces between figures and tables, and the line thickness in tables is inconsistent, affecting visual uniformity.

•	The title for Figure 2 is positioned too close to the bottom margin, overlapping with the page number, which can cause readability issues. These layout errors suggest a need for a thorough review of formatting before submission.

2. Insufficient Detail in Methodology and Figures:

•	The paper’s core methodological explanation is sparse and lacks clarity, particularly in the section describing CAB-KGC. Statements such as "The CAB-KGC proposed method incorporates the importance of contextual information obtained from the head entity and the relationship and integrates with BERT" are vague and need further elaboration. It is unclear how the contextual information is extracted, what specific types of context are used (e.g., neighboring entities, relation paths), and how this information is encoded and integrated with BERT.

•	Figures intended to illustrate the model, especially Figure 1, have limited accompanying descriptions, which could hinder reader understanding. The figure lacks detailed annotations explaining the data flow and the role of each component. Additionally, some figures, particularly in the Appendix, are complex and lack explanatory text, making it challenging for readers to interpret them effectively. For example, it is not clear how the input is processed and transformed before being fed into the BERT model.

3. Weak Justification for the New Evaluation Metric (EDAS):

•	While EDAS is introduced as a novel evaluation metric, the paper does not sufficiently motivate its necessity. The limitations of current evaluation standards (such as MRR and Hit@k) are only briefly mentioned, and it is unclear why EDAS would provide a significant advantage. A more detailed comparison of EDAS with traditional metrics, highlighting specific scenarios where EDAS offers clearer insights, would strengthen this contribution. The paper needs to clarify what specific biases or shortcomings of MRR and Hit@k are addressed by EDAS and provide a more rigorous justification for its adoption.

4. Limited Innovation in CAB-KGC:

•	CAB-KGC’s novelty is unclear. The model combines context-aware techniques with BERT embeddings, which, while valuable, may not be a groundbreaking innovation within the knowledge graph completion (KGC) domain. The approach might appear as an incremental improvement over existing models rather than a fundamentally new technique. It would be beneficial for the authors to clarify CAB-KGC’s unique contributions and differentiate it from similar methods. The paper should highlight how CAB-KGC's approach to context integration differs from existing methods that use similar techniques.

5. Insufficient Experimental Validation:

•	The paper’s experiments are conducted on only two datasets, FB15k-237 and WN18RR, which limits the demonstration of the model’s generalizability. Adding results from a dataset with entity descriptions would provide a more comprehensive evaluation and demonstrate the model’s adaptability across diverse knowledge graphs. The chosen datasets are relatively small and well-studied, and the paper should demonstrate the model's performance on larger, more complex datasets.

•	The experimental setup also lacks an ablation study on a wider set of datasets or with a broader variation of components, such as testing CAB-KGC in contexts with different entity types and relationship structures. The ablation study should include more granular variations of the model components, such as different types of contextual information and different ways of integrating them with BERT.

6. Imbalance in Content Focus:

•	Although CAB-KGC is the main proposed method, much of the paper focuses on EDAS, which may dilute the impact of CAB-KGC. A better balance could be achieved by providing more detailed insights into CAB-KGC’s architecture, implementation, and performance analysis. Readers might expect the majority of the paper to focus on the core model rather than the evaluation metric. The paper should provide more details on the training process, hyperparameter tuning, and computational cost of CAB-KGC.

7. Page Length and Presentation Issues:

•	The main content is slightly shorter than the ICLR recommended 9-page limit, which might suggest a lack of comprehensive analysis or additional experimental validation. Expanding sections on methodology and experiments could provide a fuller picture of the model’s contributions.

•	In terms of presentation, the writing style sometimes lacks precision, and the images could benefit from clearer, more thorough captions and descriptions. Improved organization and clarity would enhance readability and comprehension.

### Questions
1. Formatting: There are formatting issues, such as the residual template text and inconsistent spacing. Will you address these for better readability?
2. EDAS Motivation: Can you elaborate on the limitations of traditional metrics that EDAS addresses, specifically in the context of KGC?
3. Methodology Clarity: The methodology has vague phrases like “incorporates contextual information.” Could you clarify this with more detail?
4. Broader Validation: Why were only two datasets used, and do you plan to test CAB-KGC’s generalizability on more datasets?
5. Figure Explanations: Could you add clearer captions or appendix notes to explain complex figures like Figure 1?
6. Ablation Analysis: Can you discuss the contribution of each component in CAB-KGC, specifically “head context” and “relationship context”?
7. Computational Cost: CAB-KGC is computationally intensive. Could you clarify the trade-offs between this cost and performance gains?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes Context Aware BERT for Knowledge Graph Completion (CAB-KGC), which introduces contextual information to entities and relationships in KG, eliminates the need for entity descriptions and negative sampling, and reduces computational complexity while improving performance. In addition, this paper proposes an EDAS evaluation method to more comprehensively assess the performance of model.

### Strengths
S1. The paper focuses on knowledge graph completion, which is an important issue. The language model-based method discussed in this paper exhibit a certain novelty compared to traditional structure-based approaches.

S2. The Evaluation based on Distance from Average Solution (EDAS) criteria used in the paper is a relatively novel evaluation metric that can better evaluate model performance in the presence of multiple metrics.

### Weaknesses
W1. This work has limited technical contributions. This approach simply concatenates entities, relationships, and their contexts and inputs them into the language model, then calculates the probability of all available entities as tail entities. The idea lacks novelty, and the method appears to be a straightforward application of BERT without significant modification or innovation in the model architecture or training process. The core idea of using contextualized embeddings for knowledge graph completion is not new, and this paper does not present a novel way of using them.

W2. The description of methodology is not clear enough. The paper does not clearly specify the output of language model or how the language model output is used to compute the probability of the tail entity. Although Figure 2 suggests that the authors intend to use the embedding of CLS token for multi-class classification, this is not explicitly stated in the text. The lack of clarity makes it difficult to reproduce the results or understand the technical details of the approach. The paper should explicitly state how the CLS token embedding is processed to obtain the final probability scores for each candidate tail entity.

W3. The paper suffers from a lack of consistency in its symbolic notation, which may lead to confusion for readers. For example, in the problem formulation paragraph of the methodology section, there are three different symbol expressions for knowledge graph G. This inconsistency in notation makes the paper harder to follow and understand, and it also raises concerns about the rigor of the methodology.

W4. The paper contains numerous errors in details. For example, the Hadamard product symbol in the score function of RotatE is incorrect; there is an undefined symbol g in equation (11); the citations for ChatGPTzero-shot and ChatGPTone-shot are incorrect in Table 2. These errors indicate a lack of attention to detail and raise concerns about the overall quality of the research.

### Questions
How were the smaller datasets, such as NATION, LOCATION, COUNTRY, SPORT, and UML, constructed? Additionally, why were the ablation experiments conducted on these smaller datasets instead of on larger benchmarks like FB15k-237 and WN18RR?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces CAB-KGC, which eliminates the need for entity descriptions and negative triplet sampling, reducing computation while improving performance. It leverages contextual information from neighboring entities and relationships to predict tail entities in knowledge graphs.

### Strengths
1.The paper is clearly written and easy to follow.

2. The proposed CAB-KGC does not require negative sample training, enhancing training speed and resilience against negative sample selection, and eliminates reliance on entity descriptions, focusing solely on head and relationship contexts.

### Weaknesses
1. The article only uses two datasets in its experiments and lacks large-scale datasets. The authors should consider supplementing the datasets.

2. The creation of Figure 1 is evidently too rough, including misaligned text and meaningless graphics in the small image on the left.

3. The model section of this paper is very brief, with the model being simply a BERT that takes in information from neighboring nodes. While this approach may be effective, I question whether the paper's innovation and interpretability are sufficient for acceptance at ICLR.

4 The paper repeatedly emphasizes the advantages of the proposed model on effiency; therefore, it would be beneficial to include comparative experiments on time complexity or runtime performance between the proposed model and the baseline.

### Questions
Please refer to the "weaknesses" section.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces the CAB-KGC (Context-Aware BERT for Knowledge Graph Completion) model, which leverages contextual information from neighboring entities and relationships to predict tail entities, thus eliminating the reliance on entity descriptions. The model uses MLE to build loss, rather than contrastive training that requires negative sampling, which improves computational efficiency. 

Additionally, the paper evaluates model performance with an additional metric, the Evaluation based on Distance from Average Solution (EDAS), for more comprehensive assessment. Through experiments on the FB15k-237 and WN18RR datasets, CAB-KGC outperforms some baseline methods, showing improvements in metrics like Hit@1.

### Strengths
1. The CAB-KGC model presents a novel approach by leveraging the contextual information of neighboring entities and relationships without relying on entity descriptions or negative triplet sampling, which is a common limitation in previous KGE and LLM-based methods. This removes the dependency on external textual information, making it applicable to a wider variety of KGs, especially those that lack entity descriptions. This design leads to more efficient training and improved evaluation performance.

2. The paper demonstrates thorough experimentation and validation of the proposed CAB-KGC model on standard benchmark datasets (FB15k-237 and WN18RR).

3. The introduction of the EDAS criterion also has the potential to influence future performance evaluation practices in the knowledge graph domain.

### Weaknesses
1. Lack of novelty: The innovation in this work seems incremental, as it mainly builds on the SimKGC framework. The only major difference in the CAB-KGC model is that it does not require head entity descriptions and employs a classification loss (cross-entropy) instead of contrastive loss for training.
2. Presentation issues:

    2.1. Unclear figures: Figures are often unclear or poorly labeled, making it hard for readers to interpret their meaning. For instance, Figure 1 lacks detailed labeling and a proper explanation of how its components relate to the proposed methodology.

    2.2. Inconsistent mathematical notation: Symbols are used inconsistently. In the Introduction, the sets of entities and relations are referred to as $\mathcal{E}$ and $\mathcal{R}$, but in the Methodology section, they are denoted as $E$ and $R$. Additionally, the formulas presented lack rigor and are not sufficiently academic.

    2.3. Grammatical and typographical errors: The paper contains several issues with grammar and typos.

    2.4. Missing ablation studies: Ablation results and analyses are absent from the main text, and since reviewers are not required to consult the appendix, this omission is problematic. The authors should revise the structure of the paper.

3. Experimental design shortcomings:

    3.1. Small datasets: The experiments are conducted primarily on small datasets like WN18RR and FB15k-237. While these are common, evaluating the model on larger datasets, such as Wikidata5M, would better demonstrate the method’s generalizability.

    3.2. Training epoch limitations: The authors note that “The number of epochs was set to 30 for CAB-KGC and other models,” which may result in unfair comparisons since different models might require different numbers of training epochs.

    3.3. Lack of metric comparison: There is insufficient comparison between EDAS and traditional metrics like MRR, and the paper does not thoroughly explain the advantages of EDAS.

    3.4. No explanation of ablation results: The ablation results are not properly explained, making it difficult to assess their relevance or impact.

### Questions
The authors can focus on addressing the third concern of the weaknesses (Experimental design shortcomings), providing additional results, clarifications, etc.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes a text-based KGC method named CAB-KGC. CAB-KGC finetunes a BERT model to complete the missing entity of a triple with the help of neighboring contexts, instead of entity descriptions. The proposed method gets rid of the high computational complexity imposed by negative sampling.

### Strengths
1) The problem is clearly defined. 
2) The limitation of text-based methods, namely encoding negative samples, is clearly pointed out. 
3) The proposed method can alleviate the high computational overhead imposed by negative sampling.

### Weaknesses
1) On page 2, line 2-7, The authors classify related works using BERT-based pre-trained language models, such as KG-BERT. This reviewer does not agree with such a claim to some extent. Given the limited number of parameters, BERT, especially BERT-base, cannot be considered as an LLM. In this case, this reviewer suggests the authors use "text-based" methods instead.
2) There are several non-concurrent state-of-the-art works that are not discussed or compared with the proposed method.

a. For instance, the SOTA GNN-based method, NBF-Net [1], accepted to NeurIPS 2021, achieves Hits@1 performance of 0.321 and 0.497 on the FB15k237 and WN18RR datasets, respectively.

b. In addition, the authors did not completely report the performance of KICGPT [2] (Wei et al. 2024) referred in their paper. KICGPT is accepted to EMNLP2023 Findings, which achieves a Hits@1 of 0.327 and an MRR of 0.412 on the FB15k237 dataset, which outperforms the proposed method.

Given the reasons above, it is inappropriate to claim that the proposed method is SOTA.

3) This reviewer acknowledges that text-based methods underperform SOTA also have their merits. However, the performance of baseline methods should be completely referred and duly acknowledged.

4) Moreover, there is another SOTA method DIFT [3], which the authors claimed that the paper is accepted to 2024, achieves a Hits@1 of 0.364 and a Hits@3 of 0.439 on the FB15k237 dataset. Nevertheless, The decision made by this reviewer is not based on the existence of [3] since it is a concurrent work of this submission.

5) This paper does not report the Hits@10 performance of the proposed method and its baselines. Hits@10 is also a commonly used evaluation metric. It is acceptable if the proposed method cannot achieve desirable Hits@10 performance, as long as the issue is discussed and analysed.

6) There are many duplicated references included in the reference list. Papers including but not limited to "Convolutional 2d knowledge graph embeddings" and KICGPT appear twice or even three times on pages 9-11.

7) There are several minor Latex formatting issues. E.g. “Equations 1-??” on page 4. The correct symbol to represent membership is \in, not \epsilon (the misuses are shown in the 2nd paragraph, section 3, page 4).

### Questions
This reviewer sincerely requests the authors to revise the manuscript carefully. 

For details, please see the weakness part above.

### Soundness
1

### Presentation
2

### Contribution
1
