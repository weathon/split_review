# Deciphering Cell Lineage Gene Regulatory Network via MTGRN

- Decision: Reject
- Scores: 6, 6, 6, 5

## Abstract
Gene regulatory network (GRN) inference is crucial for cell fate decision, as it outlines the regulations between genes, which direct cell differentiation. Although there have been some work to infer cell lineage GRN, they fail to capture the continuous nature of the differentiation process as they group cells by cell type or cluster and infer GRN in a discrete manner. In this paper, we hypothesize GRN can forecast future gene expression based on history information and transform the inference process into a multivariate time series forecasting problem, linking cells at different time to learn temporal dynamics and inferring GRN in a continuous process. We introduce MTGRN, a transformer-based model that only takes single cell data as input to infer the cell lineage GRN by forecasting gene expression. MTGRN consists of temporal blocks and spatial blocks, effectively captures the connections between cells along their developmental trajectories and leverages prior knowledge to elucidate regulatory interactions among genes. It significantly outperforms six other methods across five datasets, demonstrating superior performance even compared to multimodal approaches. Based on the inferred GRN, MTGRN pinpoints three crucial genes associated with the development of mouse embryonic stem cells and depicts the activity changes of these genes during cellular differentiation. Beyond this, MTGRN is capable of conducting perturbation experiments on key genes and accurately modeling the change of cell identity following the knockout of the Gata1 in mouse hematopoietic stem cells.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The authors propose to predict gene regulatory network connections from scRNA-seq data by learning an attention matrix that captures weighted edges between genes. Pseudotime and prior knowledge are used to help the model learn the GRN. The authors show that the model beats previously published methods on the same task.

### Strengths
The proposed deep learning architecture for learning GRNs (attention matrix) and the interpretability methods the authors implement to identify key transcription factors are very interesting.

The paper is generally well-written and easy to understand.

### Weaknesses
The methods uses prior knowledge ("a highly comprehensive gene interaction network proposed in NicheNet") in the training phase and subsequently evaluates on "the ground truth network provided in Pratapa et al. (2020)". It is possible that the prior knowledge network and the evaluation network share information and this possible circularity was not tested. The potential (and maybe likely) circularity seriously undermines the performance evaluations.

The perturbation analysis is interesting, but this could be a separate paper by itself (e.g. with comparisons to other perturbation prediction methods). I would have liked to have seen a more thorough technical analysis of the main method, such as ablation studies, instead of a small add on showing the additional perturbation use case without much technical exploration.

### Questions
Can the authors show that the performance gains are not due to circularity between the prior and evaluation data?

Assuming no circularity, what are the technical aspects of the model architecture that contribute most to the performance? i.e. what aspects should others try to build on?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a novel MTGRN model for inferring cell lineage GRNs, which employs transformer architecture to analyze single-cell data. The combination of temporal and spatial blocks effectively captures the intricate relationships between cells and their developmental trajectories. The authors provide compelling empirical evidence of MTGRN's superiority, outperforming six other methods across five datasets, including multimodal approaches. The perturbation experiments further demonstrate the model's practical utility in understanding cellular identity dynamics.

### Strengths
The paper presents a novel perspective on gene regulatory network (GRN) inference by framing it as a multivariate time series forecasting problem. This innovative approach allows for capturing the continuous dynamics of cell differentiation, which is a significant advancement over traditional methods that rely on discrete clustering.

The author describes the fundamental algorithm well, and they seem to give all relevant information to understand and reproduce their algorithm. 

The proposed method is relative better than previous methods, which is not lack of significance.

### Weaknesses
The paper mentions that the advantage of the algorithm lies in dynamic network inference; however, the experimental analysis is based on data from different cell lines rather than dynamic or developmental data, which undermines the convincingness of the experimental results.
Moreover, the authors did not compare their method with latest state-of-the-art methods.

### Questions
1. To make their results more convincing, they should compare their method with more latest state-of-the-art methods. 
2. The complexity of the MTGRN model may pose challenges for replication and application in other studies. A more thorough explanation of the model's architecture and hyperparameter settings would help researchers understand and implement the model effectively.
3. They should incorporate dynamic gene expression data to infer dynamic networks.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Genes are known to work together in specific pathways and form gene regulatory networks (GRNs). GRNs govern cell differentiation in both normal and disease conditions and identifying GRNs is crucial to understand developmental processes. This is an important area of research and the authors propose a multivariate time series forecasting problem where given single cell RNA-seq data and prior information and gene interaction, an attention based model is used comprising both temporal and spatial information to predict the gene expression in future time points. Representing [genes x cells] matrix as a [genes x times] matrix and using causal attention blocks is a smart idea to formulate a time-series prediction problem. Adding spatial attention using prior interaction networks is interesting as it tells the model to pay attention to those genes that are known to interact. The proposed approach shows that GRN prediction results is better than the benchmark methods on all except mHSC-E and mHSC-L cell types. Overall this is a promising approach and should help with generating more ideas.

### Strengths
1. The use of causal attention in time series problem to predict future gene expression is smart. Using spatial attention from prior gene regulatory networks also interesting. 
2. Choosing embryonic stem cells show that the GRNs can be used to study cell differentiation
3. Perturbation of gene expression results on Gata1 is very interesting and that the results correspond to the past finding that Gat1 mediates significant changes in the expression of genes throughout the erythrocytes differentiation process shows the method has promise.

### Weaknesses
1. To prove the model and the approach is robust the authors could show perturbation of other known TFs and show how does it affect the GRNs.
2. The authors focus on the GRN prediction, and did not show metrics on the gene expression prediction itself. 
3. While it is interesting to show that the model can confirm previously found important genes/transcription factors such as Gata1, it does not show any new networks or interactions between TFs and TGs even with some lower confidence. Validation of predicted GRNs that contain previously unknown genes can be done with knockout experiments and could be shown.
4. Authors could cite. Constructing the dynamic transcriptional regulatory networks to identify phenotype-specific transcription regulators which also focuses on. learning temporal representations of gene.

### Questions
1. How did the predicted gene expression metrics such as spearmanR or pearsonR look like?
2. Does the model understand genes that are co-regulated by multiple transcription factors? For e.g. https://www.nature.com/articles/s41467-019-11905-3 paper shows that EGr1 recruits Tet1 during development and upon neuronal activity. What happens to the gene expression of a target gene that is regulated by multiple TFs when the expression of just one TF is perturbed and the second TF is undisturbed?
3. Does the model show any new gene-gene interactions?

### Soundness
2

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
5

### Summary
This paper proposes MTGRN, a transformer-based model that performs GRN inference from scRNA-seq data. The method first orders cells via a trajectory inference algorithm and then treats the problem as a time series forecasting task. Two attention modules are proposed that capture connections between cells and genes. The method is compared against several baselines on 5 datasets.

### Strengths
- The paper is well-written and easy to understand. The proposed method is clear and straightforward.
- Several datasets and baselines are considered to establish the improved performance of the proposed method.

### Weaknesses
This paper has a few weaknesses which I detail below. Addressing these would strengthen the paper in my opinion.

- The proposed method incorporates prior knowledge in the form of a known GRN (NicheNet) to limit the space of possible regulatory links to those that are known. This defeats the purpose of the algorithm as the validation essentially compares two established GRNs— NicheNet and the ground truth used in the experiments—likely resulting in a significant overlap. It is unclear why this approach is considered superior against baselines which do not use such prior information but consider all GxG connections as possible (e.g., GENIE3, GRNBoost2). The substantial improvement in scores might be attributed to this unfair advantage. Furthermore, it is not clear if the edges predicted by GENIE3 and GRNBoost2 are also restricted to those present in NicheNet for a fair comparison. The overlap between the ground truth and NicheNet is also not discussed, which could further complicate the interpretation of the results, as edges present in the ground truth but absent in NicheNet would never be predicted by the method. It is also unclear what the overlap is between the ground truth and the prior information in the other baselines (NetREX, CEFCON, and Celloracle) that use such prior information.
- There is no experiment to show that the top K edges selected are not simply derived by the most expressed genes/TFs (which are likely to be the ones enriched in the corresponding cell lineages). A quantile plot of the selected TFs or targets, ranked by total counts/expression value, would be informative. If the selected genes are among the top 1% most expressed, the method's advantage over simply selecting highly expressed genes is questionable.
- Several variables such as Q, K, V are not defined in the paper nor supplement. It is not clear how the input to the TemporalAttention module $X_{\text{input}}$ of shape $G\times W\times d$ is transformed into queries, keys to give a matrix of length $W$. Furthermore, Q, K, V in the Spatial attention module seem to have different meaning and dimension than Q, K, V defined prior.
- The use of attention for GRN inference from scRNA-seq data has been explored before [1] which limits the novelty of this paper in my view.

### Questions
Authors rely on a trajectory inference method to order cells by differentiation time, which could introduce additional hyperparameters/variance. Why not use time-series scRNA-seq datasets where the time points are given rather than learned?

### Soundness
1

### Presentation
2

### Contribution
2
