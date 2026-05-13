# Improving Multimodal Protein Function Prediction Using Bidirectional Interaction and Dynamic Selection Mechanisms

- Decision: Reject
- Scores: 5, 8, 3, 3

## Abstract
Protein function prediction is pivotal for uncovering the mechanisms of life processes. Protein function prediction is a multi-label classification task with numerous functional labels that exhibit hierarchical relationships. Relying solely on unimodal protein features is insufficient for computational models to capture complex protein functions adequately. Recently, several methods for protein function prediction have enhanced the performance by integrating multimodal protein features. However, since multimodal protein features describe protein functions from different perspectives, it is challenging to capture the intricate relationships among these multimodal features with different meanings and heterogeneity. Therefore, we propose a multimodal method for protein function prediction that can effectively utilize the intricate internal relationships between spatial structure features (i.e., protein-protein interaction network, subcellular location, and protein domains) and sequence features (i.e., amino acid sequence). In this work, we introduce the Bidirectional Interaction Module (BInM) to facilitate interactive learning between multimodal features by mapping spatial structure and sequence features of proteins to each other. Moreover, to deal with the difficulty of hierarchical multi-label classification in this task, a multi-branch Dynamic Selection Module (DSM) is designed to select the feature representation that is most favorable for current protein function prediction. Comprehensive experiments on human datasets demonstrate that our model outperforms state-of-the-art multimodal-based methods such as Graph2GO, DeepGraphGO, and CFAGO. Furthermore, we assess the efficacy of the features through Davies-Bouldin scores and t-SNE visualization experiments. The experimental results show that our method constructs more useful protein representations through bidirectional interaction and dynamic selection mechanisms, leading to improved accuracy in protein function prediction. The code in this work will be made public after its acceptance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors propose a connectionist approach to jointly exploit different sources of information (they term this multimodal) on proteins ranging from sequence to pairwise interactions from cellular localisation to domain composition, to tackle the problem of protein function prediction. 

The paper's contributions are: 1) differently from current multimodal approaches that primarily rely on information fusion mechanisms they consider the potential 'complementarity' between different modalities and 2) they develop an approach so that each modality not only influences the processing of other modalities but also 'obtains information' from them, thereby enhancing the overall understanding capability and 3) since protein function prediction is essentially a complex hierarchical multi-label classification problems they propose an approach to dynamically select the optimal feature combination for 'fitting more diverse' protein functions.

### Strengths
The idea of effectively iterating multiple and diverse sources of information is of interest.

### Weaknesses
1. The manuscript would benefit from enhanced clarity: the approach is made up of a large number of components, requiring careful attention to clearly explain the purpose of each part and how they relate to one another in an easy-to-follow manner.
2. each stated contribution is 1) not formally defined; 2) a formal way to measure its efficacy is not presented and 3) clear empirical experiments to show that the contribution is effective are not offered.
3. The results are presented without any measure of dispersion (e.g., standard deviation), making it difficult to determine whether the comparisons are significative.

### Questions
1. which is the authors contribution in the design of the individual modules is not clear: a) please provide citations for BiMamba or claim to be its authors, b) is Bidirectional Interaction Module (BINM) originally proposed for the first time in the current work? please explicitly state it if this is the case. c) is Dynamic Selection Module (DSM) the Mixture-of-Experts (MoE) from Masoudnia & Ebrahimpour, 2014, or does it introduces novelties (since <<Different from the traditional MoE system that weighted fuses all branches, our hard gating network selects one of the branches for calculation, which makes the model adapt to the prediction of the large-number and complex protein functions.>>)
2. the author offer 3 contributions:  1) not only information fusion but also a way to exploit potential 'complementarity' between different modalities: how do you show that is the complementarity that is being captured? can you design an artificial case where one can influence the level of complementarity and show that this approach can exploit it better than methods that only rely on information fusion? 2) the BINM should allow to 'obtain information' from each modality, thereby enhancing the overall understanding capability: can an artificial case be designed so that a notion of cross-talk between modalities can be manipulated and can we show that BINM can exploit that? 3) DSM should allow to dynamically select the optimal feature combination for 'fitting more diverse' protein functions: can we design an experiment to show how only some expert are used and in which contexts are they selected?
3. when comparing approaches please consider using critical difference diagrams (https://scikit-posthocs.readthedocs.io/en/latest/generated/scikit_posthocs.critical_difference_diagram.html) to report if the results are significative: a) one diagram could complement table 1 considering repeated experimental results for all performance measures and all tasks (please offer the acronym explanation for BPO MFO CCO in the text) at the same time, and could be used to answer the question: does BDGO significantly outperforms other approaches (on all task and on all measures)? b) another diagram could complement Fig. 6 and could be used to answer the question: is any ablated element contributing significantly to the performance improvement?

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper "Improving Multimodal Protein Function Prediction Using Bidirectional Interaction and Dynamic Selection Mechanisms" introduces the BDGO model, aimed at enhancing multimodal protein function prediction through a combination of spatial and sequence features. The authors propose two primary modules: the Bidirectional Interaction Module (BInM) for interactive learning between multimodal features, and the Dynamic Selection Module (DSM) for optimizing hierarchical multi-label classification. Comprehensive experiments on human datasets reveal that BDGO outperforms current multimodal-based methods, such as CFAGO, regarding F-max and m-AUPR. The paper also includes t-SNE visualization and Davies-Bouldin score analyses to validate the effectiveness of the features extracted by BDGO.

### Strengths
- Originality: The BDGO model is innovative in its approach to bidirectional interaction. It addresses challenges in multimodal protein function prediction by integrating spatial and sequence features through interactive and dynamic learning.
- Quality: The experiments are thorough, using various metrics (e.g., F-max, m-AUPR) and comparisons against state-of-the-art methods. The inclusion of ablation studies adds depth to the validation of BDGO’s components.
- Clarity: The paper clearly defines each module's role and the experimental setup. Figure 1 effectively illustrates the BDGO architecture, aiding comprehension of the methodology.
- Significance: BDGO's improvements in protein function prediction highlight its potential as a valuable tool in computational biology, particularly in handling complex, multimodal data.

### Weaknesses
 - Methodological Details: The rationale behind specific design choices, such as the number of heads in cross-attention or layer normalization parameters, could be elaborated upon to aid reproducibility. It is unclear how these parameters were selected, and what alternatives were considered. The paper lacks a discussion on the sensitivity of the model to these hyperparameters. For example, how does varying the number of attention heads or the specific layer normalization strategy impact the performance of the BInM and DSM modules? This lack of detail makes it difficult to assess the robustness of the proposed method.
- Generalizability: The paper primarily focuses on human datasets. While human datasets are important, the absence of experiments on other species raises concerns about the model's ability to generalize across different proteomes. The characteristics of protein interactions and functions can vary significantly between species, and it is not clear if the BDGO model would perform equally well on datasets with different statistical properties or evolutionary distances. The paper should include experiments on a diverse set of organisms to validate the broad applicability of the proposed approach.

### Questions
1. Could the authors clarify the parameter selection process for the BInM and DSM modules? Understanding this would improve insight into BDGO's adaptability.
2. Did the authors explore any augmentation techniques for protein features? Such techniques could potentially address overfitting in low-sample domains.
3. Would the BDGO model benefit from additional layers in the DSM, particularly when dealing with very large protein function datasets?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper presents BDGO, a novel multimodal approach for protein function prediction. The model includes a Bidirectional Interaction Module and a Dynamic Selection Module. The model incorporates the protein sequence and protein-protein interaction information. The proposed model is tested using the Gene Ontology prediction task.

### Strengths
1. The two modules (BInM and DSM) are proposed for cross-modal learning and multi-label selection. 
2. The model Integrates multiple protein features (PPI network, subcellular location, protein domains and protein sequences)

### Weaknesses
1. The motivation for using PPI data is not clear. Many works used the protein structure, which may contain more information about protein function. Comparisons should be made with methods using structural information, such as DeepFRI and SaProt.
2. The testing task is limited. It may be helpful to see if the model can make reliable predictions on unannotated proteins.
3. The sequence encoder ProtT5 is already a pre-trained model. What is the reason for pre-training it again? 
4. The effect of per-training is not clear.
5. There seem to be some hyperparameters in the model that are unclear. 
6. In line 288, how are the groups of features generated?
7. In line 195, what is the "given surface"?

### Questions
See weakness

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
4

### Summary
This paper introduced BDGO a framework for protein function prediction. It combines Mamba architecture and a interaction module for ontology prediction with pre-training on both the sequence and spatial modules. The authors show marginal performance improvement over some existing sequence based and PPI(protein-protein interaction) network based methods for protein function prediction.

### Strengths
1. The authors demonstrated the Mamba architecture combined with protein language model can improve prediction performance on existing sequence based and PPI based methods such as BLAST[1] and interaction network based methods such as Mashup[2] and NetQuilt[3].
2. Ablation studies showed the importance of the protein language models(ProtT5)[4] as a featurization tool.

### Weaknesses
1. Lack of motivation for the proposed architecture. The authors proposed the used of BiMamba as extension of the Mamba[5] architecture. However, no specific motivation was given on how the author hypothesize such architecture’s advantage on modeling protein sequences. very generic terms were used to justified such model selection. ‘’*BiMamba introduces a novel bidirectional selective scanning mechanism designed for protein information, which can take into account both the information at the beginning
and end of spatial features. This design allows BiMamba to capture details and context information in the spatial features of proteins.*” How does BOW encoding of domain and localization benefits from your “Spatial” encoding? The authors do not clearly articulate why a state space model, particularly Mamba, is suitable for encoding the bag-of-words representation of protein domains and localization. The justification lacks a clear connection to the underlying mechanisms of Mamba and how they align with the nature of the input features. The choice of Mamba seems arbitrary, given that the input is not a sequential signal but rather a set of categorical features represented as a bag-of-words.
2. In the benchmarking effort, the authors only compared with methods that used naive sequence input and PPI network information. However, the proposed method uses protein language model to featurize the input sequence and it’s widely accepted in the community that the use of protein language model and significantly improve model performance[6]. The lack of acknowledgement in the benchmarking effort either shows the authors’ lack of knowledge in the field of protein function prediction or potentially intentional misleading benchmarking setup. The authors fail to compare their method against other state-of-the-art methods that also leverage protein language models for feature extraction. This omission makes it impossible to assess the true contribution of their proposed architecture beyond the benefits of using pre-trained language models. The comparison is not comprehensive and does not provide a fair evaluation of the proposed method.
3. The failure to extend the framework to enzyme function(EC) prediction. It has been the standard for protein function prediction framework to include enzyme function prediction as part of evaluation. The authors failed to include such results. The lack of EC number prediction results is a significant oversight, as it is a standard benchmark in the field. This omission raises concerns about the completeness of the evaluation and the generalizability of the proposed method.
4. The authors directly borrowed a dataset from a previous study CFAGO[7] which is a time stamp based split. For machine learning methods, it is very important to check for sequence similarity between the training and testing set to avoid leakage and inflated results. The authors fail to address the potential for data leakage due to sequence similarity between the training and testing sets. Using a time-based split without considering sequence similarity can lead to inflated performance metrics and an inaccurate assessment of the model's generalization capabilities. This is a critical flaw in the experimental design.
5. Overall, this study showed a arbitrary deep learning architecture applied to protein function prediction. The motivation and hypothesis is not well justified for use of such model and the benchmarking effort is lacking in both comprehensiveness and rigor.

### Questions
1. What specific aspect of the proposed model contributed to the performance improvement? The use of ProtT5 against CFAGO is not a fair comparison because  CFAGO does not use protein language model as part of the featurization pipeline. 
2. How does a BOW encoding PPI matrix utilize the space state model proposed ? 
3. Why not include results for EC number prediction in your results? 
4. Why not also benchmark using a sequence similarity based split?

[1]Altschul, Stephen F., et al. "Basic local alignment search tool." *Journal of molecular biology* 215.3 (1990): 403-410.
[2]Cho, Hyunghoon, Bonnie Berger, and Jian Peng. "Compact integration of multi-network topology for functional analysis of genes." *Cell systems* 3.6 (2016): 540-548.
[3]Barot, Meet, et al. "NetQuilt: deep multispecies network-based protein function prediction using homology-informed network similarity." *Bioinformatics* 37.16 (2021): 2414-2422.
[4]Elnaggar, Ahmed, et al. "Prottrans: Toward understanding the language of life through self-supervised learning." *IEEE transactions on pattern analysis and machine intelligence* 44.10 (2021): 7112-7127.
[5]Gu, Albert, and Tri Dao. "Mamba: Linear-time sequence modeling with selective state spaces." *arXiv preprint arXiv:2312.00752* (2023).
[6] Kulmanov, Maxat, et al. "Protein function prediction as approximate semantic entailment." *Nature Machine Intelligence* 6.2 (2024): 220-228.
[7]Wu, Zhourun, et al. "CFAGO: cross-fusion of network and attributes based on attention mechanism for protein function prediction." *Bioinformatics* 39.3 (2023): btad123.

### Soundness
1

### Presentation
2

### Contribution
1
