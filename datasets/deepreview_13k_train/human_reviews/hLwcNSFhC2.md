# SAGEPhos: Sage Bio-Coupled and Augmented Fusion for Phosphorylation Site Detection

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
Phosphorylation site prediction based on kinase-substrate interaction plays a vital role in understanding cellular signaling pathways and disease mechanisms. Computational methods for this task can be categorized into kinase-family-focused and individual kinase-targeted approaches. Individual kinase-targeted methods have gained prominence for their ability to explore a broader protein space and provide more precise target information for kinase inhibitors. However, most existing individual kinase-based approaches focus solely on sequence inputs, neglecting crucial structural information. To address this limitation, we introduce SAGEPhos (Structure-aware kinAse-substrate bio-coupled and bio-auGmented nEtwork for Phosphorylation site prediction), a novel framework that modifies the semantic space of main protein inputs using auxiliary inputs at two distinct modality levels. At the inter-modality level, SAGEPhos introduces a Bio-Coupled Modal Fusion method, distilling essential kinase sequence information to refine task-oriented local substrate feature space, creating a shared semantic space that captures crucial kinase-substrate interaction patterns. Within the substrate's intra-modality domain, it focuses on Bio-Augmented Fusion, emphasizing 2D local sequence information while selectively incorporating 3D spatial information from predicted structures to complement the sequence space. Moreover, to address the lack of structural information in current datasets, we contribute a new, refined phosphorylation site prediction dataset, which incorporates crucial structural elements and will serve as a new benchmark for the field. Experimental results demonstrate that SAGEPhos significantly outperforms baseline methods, notably achieving almost 10% and 12% improvements in prediction accuracy and AUC-ROC, respectively. We further demonstrate our algorithm's robustness and generalization through stable results across varied data partitions and significant improvements in zero-shot scenarios. These results underscore the effectiveness of constructing a larger and more precise protein space in advancing the state-of-the-art in phosphorylation site prediction.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work aims at phosphorylation site prediction. While the problem of detecting phosphorylation sites is possible through high-throughput experimental techniques such as mass spectrometry, predicting phosphosites for a speicific kinase is still a relevant computational problem as detecting kinase-substrate associations is more difficult.  The work presents SAGEPhos. The contribution of this method is that as opposed to traditional methods that rely solely on sequence information, SAGEPhos  leverages both kinase sequence and structural information. SAGEPhos combines these modalities through gated fusion strategies. The inter-fusion and intra-fusion strategies aim at capturing information on different modalities for both kinase and the substrate. The paper reports a 12% improvement in AUC-ROC compared to other methods.

### Strengths
Strengths:

- The fusion strategies and the gated architecture allow for combining information such as structural or conservation scores and sequence information in a useful way.
- There is an ablation study to understand the impact of inter and intra-fusion models.
- The authors compare their methods with the most relevant work.
- The authors conduct experiments to assess the sensitivity to hyperparameter changes.
- Authors conduct experiments to understand specific cases. The case studies on GSK3B and MK01 are interesting. This work could be extended to other kinases to understand  the kinase specific motifs.

### Weaknesses
 - The main weakness of the paper is in the presentation. Many critical experimental details lack clarity which I listed in the questions:
-  The main contribution of the paper is adding structural information to the model. A comparison to a structure-aware protein language is missing. For example, how would SaProt perform on this task?
The paper claims zero-shot generalization but only demonstrates this on a single kinase. The zero-shot experiments could be more comprehensive. Additionally, a zero-shot classifier for kinases, DeepKinZero (Deznabi et al. 2020), exists, but the authors did not discuss its relevance to their work.
Authors should also discuss in the report how performance changes across different kinases. Are certain kinases easier to predict than others? Is the kinase-specific performance related to the number of substrates associated with each kinase? 

- The discussion section could be strengthened. For example, MusiteDeep's performance in cold-start cases, achieving only 6.4% AUPRC or 0.8% AUPRC, should be mentioned. Also, the authors use AlphaFold structures. Using PDB structures whenever available would make more sense, filling in only missing ones with AlphaFold predictions. Authors should at least acknowledge this and discuss the potential biases it could lead to.

- I think the cold-start kinase or substrate experiments are not truly cold. Some kinases are very similar for example keeping AKT1 in the training set and putting AKT2 in the test set, the test cases for AKT2 would be easy. Same for the substrate. Thus the cold start experiments could have taken the similarity of the sequences.

-Authors learn the conservation scores. A natural question to ask is would the pre-calculated conservation scores from the MSAs would better than that. And how is it different than an attention score.

- The comment on "The zero-shot experiments could have been more comprehensive. " is not handled.

- What was the similarity metric? Identity? And for the kinases, the similarity should be calculated over the kinase domains I think. Otherwise the unrelated domains in the protein would reduce the similarity.

- One last question, what guarantees that the learned scores reflect conservation scores?  I think the authors should showcase that the learned scores are in the conservation scores in the evolution - which is the  common term that the field has been using.

### Questions
- It is unclear how the cold-start and warm-start experiments are designed. The cited reference does not include this information either, which is critical to assessing the results.

- The negative example selection procedure is not clearly described. The authors state: “For each kinase, we selected an equal number of negative samples from substrate sequences lacking explicit evidence of catalysis by that kinase, resulting in a balanced 1:1 ratio of positive to negative “ Are negative sequences chosen from other positions within the same substrate of the kinase, or the entire substrate set across all kinases? Are these positions known phosphosite locations on other substrates, or are they potential sites that could accept a phosphate group without a reported kinase association? Clarifying this distinction is important, as each case poses a different level of classification difficulty.

- The paper combines three different datasets, removing redundant information. When splitting the train/test folds, is substrate similarity or kinase similarity taken into account?

Some other  technical details are missing, which will make it difficult to reproduce the work:


-ESM2 is used for feature extraction, but the specific ESM2 model size is not specified.
- How are the conservation scores computed? 
- Which physicochemical properties are used and with what kind of representation? Continuous scale, binarized categories? Figure A1 needs a legend for the color scale.					
“We used this data to create a new test set, where substrate-kinase pairs ranked first for CDK17 were treated as positive samples, and those ranked the bottom two were designated as negative samples.” How many substrates are taken from the bottom and the top?

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
2

### Summary
The paper discusses SAGEPhos, a model developed for predicting phosphorylation sites in proteins by using both kinase sequence information and the 3D structural information of substrates. It employs a multi-modal fusion framework called MERGE, which integrates structural and sequence data through two main techniques: Bio-Coupled Fusion and Bio-Augmented Fusion. This approach aims to highlight critical phosphorylation regions by combining sequence-based and structure-based insights. The model demonstrates enhanced accuracy and AUC metrics compared to traditional methods, showing potential applications in kinase signaling pathways relevant to diseases such as cancer and neurodegenerative disorders.

### Strengths
1. Innovative Fusion Strategy: The paper introduces Bio-Coupled and Bio-Augmented fusion mechanisms, which enhance phosphorylation site prediction by effectively merging structural and sequence data.
2. Integration of Structural Data: Utilizing structural data (such as from AlphaFold2) to predict phosphorylation sites addresses a notable gap in traditional models that rely solely on sequence information, potentially providing more biologically relevant insights.
3. Zero-shot prediction: SAGEPhos is evaluated in different contexts, which test its ability to generalize to unseen kinases, demonstrating versatility.

### Weaknesses
1. Limited Justification for Method Choices: The choice of certain architectural elements, like GCN for structural data and gated/residual features, lacks thorough justification. Without clear reasoning, it’s difficult to determine if these choices genuinely improve the model’s performance or if simpler alternatives could suffice. For instance, the specific type of GCN (e.g., spectral vs. spatial) and the number of layers are not justified. Furthermore, the necessity of gated and residual connections within the fusion modules should be supported by ablation studies or comparative analysis against simpler fusion techniques.
2. Complex Model Architecture: The use of multi-modal fusion (Bio-Coupled and Bio-Augmented), along with gated and residual features, adds considerable complexity. This complexity may reduce the model’s accessibility and reproducibility for researchers without advanced computational resources or expertise in deep learning. The authors should consider providing a more modular design or open-source implementation to facilitate broader adoption and validation by the community.
3. Dependence on AlphaFold Structures: The model relies heavily on AlphaFold’s structural predictions, which may not be entirely accurate for all proteins, especially those without known homologs. The paper does not discuss how the model handles low-confidence regions or potential errors in the predicted structures, which could significantly impact the prediction accuracy. A sensitivity analysis on the impact of varying pLDDT scores would be beneficial.

### Questions
1. What steps did you take to ensure the model’s generalizability, given that it was only evaluated on a limited set of datasets?
2. Could you clarify why you chose complex models like R-GCN for structural representation over simpler alternatives, and what benefits they provide?
3. How does SAGEPhos handle incomplete or low-confidence structural data, given its reliance on AlphaFold2 predictions?
4. Why does the model only use both sequence and structure data for substrates, while only sequence data is used for kinases?
5. Why was a GCN applied to the AlphaFold structures instead of directly using AlphaFold’s embeddings?

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
3

### Summary
The paper introduces SAGEPhos, a novel structure-aware framework designed to enhance phosphorylation site prediction by integrating sequence and structural information in a multi-modal fusion approach. To address the limitations of current kinase-specific prediction methods that primarily focus on sequence data, SAGEPhos employs two complementary fusion strategies: Bio-Coupled Fusion, which refines substrate feature spaces using kinase sequence data for inter-modality integration, and Bio-Augmented Fusion. And these methods also provide a shared semantic space that captures crucial kinase-substrate interaction patterns. Besides, the authors contribute a new phosphorylation site prediction dataset enriched with structural information, establishing a more comprehensive benchmark for this domain. Experimental results show that SAGEPhos achieves significant improvements over existing approaches in both warm-start and zero-shot scenarios.

### Strengths
1) The paper is well-written.

2) The proposed method achieves state-of-the-art performance on new phosphorylation site prediction dataset  compared to baselines.

3) The paper introduces a novel method to phosphorylation site prediction by integrating both sequence and structural data through Bio-Coupled and Bio-Augmented Fusion modules. This dual fusion approach is particularly innovative, allowing SAGEPhos to capture additional information of kinase-substrate interactions, addressing an limitation in existing models that focus on sequence data.

4) The new dataset with added structural information is a valuable addition, offering a benchmark supports future work in this field.

### Weaknesses
1) The paper uses structural information as an auxiliary modality fused with sequence data; however, it lacks an in-depth discussion on the mechanisms of multi-modal interaction. Specifically, after R-GCN extracts structural features, the paper does not clarify how these features are effectively leveraged sequence information in specific task, such as complex kinase-substrate interactions. The paper should elaborate on how the structural embeddings, derived from R-GCN, are integrated with the sequence embeddings. For instance, does the model use attention mechanisms to weigh different structural features based on the sequence context, or are the features simply concatenated? A more detailed explanation of the fusion process is needed to understand the model's inner workings.

2) The addition of new structural data as a modality increases the complexity of the SAGEPhos model. However, the paper omits discussion of the additional computational costs introduced by this additional complexity. The paper should provide a detailed analysis of the computational resources required by SAGEPhos, including training time, memory usage, and inference speed. This analysis should compare SAGEPhos with baseline models to demonstrate the trade-offs between performance gains and computational overhead. Without this information, it is difficult to assess the practical applicability of the proposed method.

3) Though the new dataset with structural information is a valuable contribution, it remains relatively small and limited in diversity, especially in terms of kinase families and phosphorylation patterns. The dataset's limited size and diversity may restrict the generalizability of the findings. The paper should discuss the potential biases introduced by the dataset's composition and acknowledge the need for larger, more diverse datasets to validate the model's performance across a wider range of kinase-substrate interactions. Specifically, the distribution of kinases and substrates should be analyzed to identify potential gaps in the training data.

### Questions
1) Do you consider directly comparing SAGEPhos with a model that simply combines sequence and structure data? It seems  the improvements in SAGEPhos may result more from the utilization of structural information itself rather than from the hierarchical fusion strategy. A direct fusion comparison would clarify the benefits of the selective approach.

2) Do you consider other structure encoders besides R-GCN, there are multiple encoding models available for protein structure.

3) How to explain the performance differences in FPR across models in Table 2? The substantial FPR variance raises questions about the stability and consistency of SAGEPhos compared to other baselines. A more detailed discussion of the factors behind these differences would be helpful.

### Soundness
3

### Presentation
3

### Contribution
3
