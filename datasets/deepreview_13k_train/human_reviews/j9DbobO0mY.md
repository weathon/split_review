# Sparse MoE as a New Retriever: Addressing Missing Modality Problem in Incomplete Multimodal Data

- Decision: Reject
- Scores: 3, 5, 6, 8

## Abstract
In multimodal machine learning, effectively addressing the missing modality scenario is crucial for improving performance in downstream tasks such as in medical contexts where data may be incomplete. Although some attempts have been made to effectively retrieve embeddings for missing modalities, two main bottlenecks remain: the consideration of both intra- and inter-modal context, and the cost of embedding selection, where embeddings often lack modality-specific knowledge. In response, we propose MoE-Retriever, a novel framework inspired by the design principles of Sparse Mixture of Experts (SMoE). First, MoE-Retriever samples the relevant data from modality combinations, using a so-called supporting group to construct intra-modal inputs while incorporating inter-modal inputs. These inputs are then processed by Multi-Head Attention, after which the SMoE Router automatically selects the most relevant expert, i.e., the embedding candidate to be retrieved. Comprehensive experiments on both medical and general multimodal datasets demonstrate the robustness and generalizability of MoE-Retriever, marking a significant step forward in embedding retrieval methods for incomplete multimodal data.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a model called MoE-Retriever to retrieve embeddings for missing modalities in multimodal machine learning. Both intra-modal and inter-modal contexts are considered in the embedding retrieval process. The former considers other data samples with the target modality to be retrieved by proposing a supporting group and the later considers the available modalities from the same data sample. Empirical evaluation shows improvement over existing methods on several public datasets.

### Strengths
- The problem of missing modality in the context of multimodal machine learning is significant and worth investigating.
- The idea of considering intra-modal and inter-modal contexts for embedding retrieval is interesting and important.
- The empirical evaluation shows improvement over existing methods.

### Weaknesses
The major weaknesses are the limited novelty and unclear presentation. Detailed comments are as follows.

1. The novelty seems limited. The proposed MoE is largely developed based on FuseMoE with the same router design. The added value on top of FuseMoE is mainly the intra- and inter-modal contexts.
2. The intra-modal context section, especially Eq. (2), looks very confusing to me. $\mathcal{M}$ is a set of all modalities, $\mathcal{X}(\mathcal{T}|mc)$ is a set of subsets of $\mathcal{M}$, why the integer $j$ is an element of it? What does $S\wedge \mathcal{T}$ mean? Or is it supposed to be $S\cap \mathcal{T}$? Is $S$ a set? why $S$ is a subset of $\mathcal{M}$ and at the same time $S\wedge\mathcal{T}$ is an element of $S$? After carefully reading Eq. (2) and the descriptions below it, I still find it difficult to understand how the intra-modal context is extracted and used.
3. The inter-modal context is not described in detail. Particularly, it is argued that the missing modality of imaging may indicate an early stage of AD, but it is not clear how the proposed inter-modal context can help address this issue. The explanation lacks a clear connection between the inter-modal context and the specific problem of early AD detection. It is unclear how the model leverages the presence of genetic and clinical data, and the absence of imaging, to infer early AD. The mechanism by which the model learns this relationship is not well-defined.
4. In Eq. (3), are $\mathbf{P}^\prime$, predicted retrieved embedding, matrices? What does it mean to take the union between two matrices? The notation is ambiguous and needs clarification. It is unclear how the intra-modal and inter-modal embeddings are combined and what the resulting structure represents.
5. It is not clear how each expert is parameterized. What is the model used for each expert? The description lacks detail on the architecture of the experts, making it difficult to assess the complexity and capacity of the model.
6. What does "input token" mean? Is it one data sample or one particular feature from a data sample? The terminology is not precise, leading to confusion about the input representation.
7. For implementation, using optimal hyperparameter settings in the original paper does not necessarily guarantee a fair comparison since the baselines may not be tuned in the datasets used in this work. Careful tuning of hyperparameters of each baseline model is needed to ensure a fair comparison. The lack of hyperparameter tuning for baselines raises concerns about the validity of the comparison.
8. The "Details on ADNI dataset preprocessing" paragraph in Appendix A.1.1 duplicates the reprocessing steps for the MIMIC dataset. In addition, it should be explicitly clarified in A.1.2 that the MIMIC dataset has a linkage with the Massachusetts State Registry of Vital Records and Statistics to allow analysis regarding out-of-hospital mortality up to one year after hospital discharge.

### Questions
Please see my comments above.

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper aims to address the missing modality problem by retrieving the most relevant embedding for the target(missing) modality. To obtain the relevant embedding, both intra- and inter-modal contexts are employed along with a router. The experimental results on medical datasets and general multimodal datasets demonstrate the effectiveness of the approach.

### Strengths
- The motivation of the paper is clear and convincing. 
- The method used is reasonable and interesting.

### Weaknesses
 - As the target of the paper is to address missing modality, it would be more convincing if results regarding different missing ratios could be given for robustness illustration. 
- Are there any data statistics regarding the missing modalities for MIMIC?



### Questions
- As stated in the paper, baseline models with MIMIC dataset suffer from label imbalance problems. Is there any results using PRAUC?
- For results CMU-MOSI, the results using three modalities (V+A+T) across all models are worse than those with two modalities (A+T). What caused the performance drop?
- For results on CMU-MOSI and ENRICO, the dropping rate is 0.3. Is there an ablation study regarding the robustness against different dropping ratios? 
- In Figure 4, MoE-Retriever demonstrated better computational efficiency. However, when the number of modalities scales up, other methods remain similar while MoE-Retriever scales up a bit. Can authors provide more insights or further explanations?
- One additional concerning issue is the resembling of figures and experiment results with the paper [1], which is not cited, mentioned, or discussed at all in the submission. Particularly, experiment results of the FuseMoE baseline reported in Table 1 are exactly the same as that reported in Table 1 and 2 of [1]. Please clarify if the results reported are obtained by the own experiments of the authors, or taken from any other papers. Fig. 3(a) is a modified version of Fig. 2(c) of [1] without any acknowledgment of the sources. Please clarify the source of the figure.

[1] Yun, Sukwon, et al. "Flex-MoE: Modeling Arbitrary Modality Combination via the Flexible Mixture-of-Experts." arXiv preprint arXiv:2410.08245 (2024).

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
This paper introduces MoE-Retriever to address the missing modality problem in medical data. MoE-Retriever leverages intra-modal context by using other samples with the same missing patterns and inter-modal context from available modalities. These contexts are processed through a multi-head attention layer and then aggregated using a sparse mixture-of-experts architecture. Experimental results show that MoE-Retriever improves performance across multiple datasets.

### Strengths
1. The approach of leveraging other samples to “impute” missing modalities is intuitive and well-motivated.
2. The use of a sparse mixture-of-experts architecture is reasonable.
3. The experiments are extensive, and the proposed method demonstrates improved performance over existing methods on multiple datasets.

### Weaknesses
1. Novelty: The model primarily applies existing techniques, which may limit its novelty.
2. Architecture: MoE-Retriever appears to select support samples randomly. This could lead to inconsistencies if selected samples differ significantly from the input sample. Incorporating a similarity measure might enhance retrieval accuracy.
3. Presentation: The paper’s clarity could be improved, especially in notation, as the numerous superscripts and subscripts can be difficult to follow. Additionally, there is an unusually large margin on page 6.

### Questions
See weakness 2.

### Soundness
2

### Presentation
2

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
This work attempts to tackle the missing modality problem in multimodal learning. Observing that existing methods do not balance the intra- and inter-modal information when retrieving the representations for missing modalities and the costly computations, the authors tackle these issues by using Sparse MoE. Experiments on general and medical multimodal datasets demonstrate satisfactory performance and thorough ablation studies were performed.

### Strengths
•	This work tackles the challenging problem of missing modality, which is one of the most important concerns of multimodal learning. 

•	Extensive experiments have been performed on various datasets and recent baseline methods and satisfactory performance is obtained. Ablation study is well-performed.

•	The paper is overall clearly written.

•	Codes and algorithms are available for reproducibility

### Weaknesses
· The notion of using MoE to tackle the missing modality problem seems to be well studied by FuseMoE, and the SMoE is also proposed by existing works and extensively applied. More contributions are expected in addition to addressing the balance between intra- and inter-modal information. For instance, there could be more designs on adapting the some into the framework (e.g., how to select the experts based on intra- and inter-modality groupings), given that currently the frameworks just use some with little elaborations on the motivations and modifications. In this sense, I am less convinced that the contribution is enough to meet the bar.

**Minor:**

•	The authors only report the accuracy and F1 scores for primary results, which are highly sensitive to thresholds. Authors are suggested to present the results in AUROC (which is also adapted by MUSE, one of the baselines) in addition to current metrics, to more comprehensively evaluate the performance.

•	The use of English has space of improvement. Some sentences are difficult to follow / less clear. For instance, "lack of specialized knowledge in embedding candidates”"in the abstract is vague and hard for me to follow (i.e., more precise words need to be used for “specialized knowledge”, which is a quite subjective word).

### Questions
* Is there any particular advantage on applying the proposed method to medical datasets than general multimodal datasets?
* Is there any specific case from MIMIC (e.g., for a specific diagnosis) to interpret the feature retrieval process of the MoE?
* The CMU-MOSI experiments look interesting. Could the authors also open-source the codes for more information on the implementation?

### Soundness
3

### Presentation
3

### Contribution
2
