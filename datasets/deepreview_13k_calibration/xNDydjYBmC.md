# Enhancing PPB Affinity Prediction through Data Integration and Feature Alignment: Approaching Structural Model Performance with Sequences

- Decision: Reject
- Avg Score: 4.60
- Scores: 6, 3, 6, 5, 3

## Abstract
One key step of protein drug development is the screening of protein-protein binding (PPB) affinity. The current mainstream screening method of PPB affinity is laboratory experiments, which are costly and time-consuming, making it difficult to quickly perform high-throughput screening. Various deep learning methods have been proposed to predict PPB affinity, but they are often limited by the availability of high-quality data and the compatibility of the algorithms with that data. In this work, we developed two AI models, PPBind-3D and PPBind-1D, to predict PPB affinity. PPBind-3D leverages structural information near the protein-protein binding interface to make its predictions. By employing monotonic neural network constrained multi-task learning, we effectively utilized heterogeneous affinity data from diverse wet lab experiments to expand the development dataset to over 23,000 samples, thereby enhancing the model's generalization capabilities. Additionally, PPBind-1D was developed using sequence data to address the lack of structural data in practical applications. During the training of PPBind-1D, we aligned it with PPBind-3D by incorporating an additional 42,108 no-affinity-label samples through an alignment approach. Finally, we demonstrated three application cases of our AI models in the virtual screening of protein drugs, illustrating that our models can significantly facilitate high-throughput screening.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, PPBind-3D and PPBind-1D are developed to predict protein-protein binding affinity based on three datasets PPB-Affinity dataset, Heterogeneous Affinity Dataset and DIPS-Plus dataset. PPBind-3D used SE(3)-Invariant attention module to capture structural information near the protein-protein binding interface to make its predictions.  PPBind-1D was developed using sequence data to address the lack of structural data in practical applications.

### Strengths
The use of monotonic neural network-constrained multi-task learning (MMTL) expanded the development dataset to over 23,000 samples and helped to improve the model’s generalization abilities.

SE(3)-Invariant attention is used to get features of protein complex structures using the iDist algorithm, and then clustering the protein complex structure features based on graph partition algorithms helps to address the data leakage problem.

### Weaknesses
Currently, the code doesn’t contain a data partition process.

The paper would be better if including other methods to compare their performance with PPBind-3D.

The metrics used to estimate performance only include spearman or Pearson correlation, lack of RMSE.

### Questions
In Section 3.1, what is the reference paper for PPB-Affinity Dataset? 

In Section 4.1, you set the distance threshold for identifying protein-binding interface amino acids as 8 Å between the C-alpha atoms of two amino acids. This choice may seem somewhat arbitrary; could you elaborate further on the rationale behind selecting 8 Å as the threshold?

Could you explain more about the data partition process, and why it can help to solve the data leakage problem?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This work introduces two AI models called PPBind-3D and PPBind-1D to enhance protein-protein binding (PPB) affinity prediction, which is crucial for protein drug development. In detail, PPBind-3D leverages structural data near binding interfaces, supported by a novel monotonic neural network-based multi-task learning (MMTL) approach, which integrates diverse experimental datasets to improve generalization. Besides, PPBind-1D uses sequence-based data, aligning with structural predictions to address scenarios when structural data is limited. In the experiments, the authors demonstrate the models' potential to support high-throughput virtual screening of PPB affinities by illustrating three case studies in virtual screening applications.

### Strengths
This paper introduces a novel approach to protein-protein binding (PPB) affinity prediction, integrating both structural and sequence-based models to address the high-throughput demands of drug discovery. The models, PPBind-3D and PPBind-1D, are designed with a sequence-structure alignment strategy that allows the sequence-only model to gain structural insights indirectly. This innovation effectively bridges the gap where structural data is unavailable. Besides, the authors use a monotonic neural network-based multi-task learning (MMTL) framework to incorporate heterogeneous affinity data, enhancing the model’s robustness while handling variations in measurement types. The authors also pay attention to data partitioning to avoid data leakage. These methodological choices are evaluated by ablation studies and real-world virtual screening case studies.

The clarity of the presentation is overall good to let readers understand the proposed models and the experiments. In terms of impact, this paper addresses a critical challenge in high-throughput screening by providing a flexible solution that has both structural and sequence-based models.

### Weaknesses
The baseline models are missing in experiments, so it is unknown how well the proposed models perform when compared to existing ones.

When partitioning the data, the authors only provide the partition performance according to distances. But it is hard to understand what distance level is good or not. I feel that using the protein sequence identity ratio between different proteins can be more straightforward.

For the results of the three cases in virtual screening applications, there can be data leakage between the test set and the training set. It would be interesting to know if the well-predicted structures/sequence data exist in the training set or share high similarities with the data in the training set.

### Questions
Since the proposed methods are meant to be applied to virtual screening, what is the efficiency of them? For example, the inference speed and memory consumption.

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
This paper presents a new approach for predicting protein-protein binding (PPB) affinity, which is essential in drug discovery. The authors developed two models, PPBind-3D and PPBind-1D. 

PPBind-3D leverages structural data to predict affinity using advanced data integration and a multi-task learning approach, which enables it to generalize well despite data variability. PPBind-1D, on the other hand, relies on sequence data alone, making it more applicable when structural data is unavailable. 

To align PPBind-1D's performance with that of PPBind-3D, the authors introduced an alignment technique using additional unlabeled data, helping the sequence-based model approximate structural model performance. Evaluations show that these models, particularly PPBind-1D, can support high-throughput screening by predicting PPB affinity accurately, even under strict data partitioning to avoid leakage. The work’s impact lies in enhancing drug discovery workflows with a method that bridges data gaps while maintaining predictive accuracy.

### Strengths
The methodology is strong, incorporating strict data partitioning and monotonic multi-task learning to enhance model generalization. While the technical explanations are clear, some sections could benefit from simplification for accessibility. This work’s flexible, scalable model has significant implications for drug discovery, offering a valuable tool for high-throughput screening relevant to both computational biology and AI communities.

### Weaknesses
The alignment method for integrating sequence-based features with structure-based predictions is intriguing but not fully detailed. Providing more in-depth explanations and visualizations, especially of how alignment influences the latent spaces between PPBind-1D and PPBind-3D, would strengthen understanding and reproducibility.

While the paper includes ablation studies, adding more direct comparisons with existing models (e.g., CSM-AB, AREA-AFFINITY) using standard benchmarks would clarify the novelty and effectiveness of the proposed approach. Highlighting quantitative gains over established models would emphasize the advantages of PPBind-1D and PPBind-3D.

A brief analysis of feature importance or interpretability of predictions, particularly around how sequence and structural features affect affinity, would make the work more useful for practical applications and provide valuable insights into model behavior.

### Questions
Can the authors elaborate on the performance of PPBind-1D and PPBind-3D across additional external datasets? It would be helpful to understand how well these models generalize to datasets beyond PPB-Affinity and DMS-Het, especially for applications with different data types or measurement techniques.


Adding an analysis on which structural or sequence features most impact the predictions would provide valuable insights. Are there any interpretability tools (e.g., SHAP values or feature importance rankings) applied to understand how features contribute to binding affinity predictions? This could increase the model’s practical applicability and user trust.

Can the authors provide more details on the computational resources required for PPBind-3D versus PPBind-1D? A comparison in training and inference time, along with any scalability insights, would help evaluate the model’s applicability in real-world, high-throughput scenarios.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work addresses the task of predicting protein-protein binding (PPB) affinity to improve the efficiency of high-throughput screening in protein drug development. The motivation behind this work is to overcome limitations associated with traditional laboratory screening methods for PPB affinity, which are costly, time-consuming, and not well-suited for high-throughput applications. Additionally, existing deep learning models often lack sufficient high-quality data or generalization capability due to limited compatibility with diverse affinity data. To accomplish this, the authors developed two AI models, PPBind-3D and PPBind-1D. In this process, they focused on (1) utilizing a novel and large dataset, (2) strictly partitioning data for performance testing, and (3) introducing a "feature alignment" mechanism. The authors demonstrated the performance of their models using the PPB-Affinity dataset and three virtual screening cases.

### Strengths
The structure of the article is clear and easy to follow. The figures are well-designed. The authors use biological measurement terminology correctly, such as subscripting characters where appropriate.

### Weaknesses
1. Lack of Baselines: Section 2, "Related Work," mentions several existing studies on this task. However, **there is no comparison between the proposed models and previous models**, aside from the comparisons within the authors' own models (1D, 3D, and aligned).
2. Missing Important Figure: **Figure 5 is an exact copy of Figure 4**. While this is likely unintentional, the absence of additional descriptions or tables showing the performance of the 1D model is a significant issue, as the case studies alone cannot demonstrate the model's general performance.
3. Presentation Weaknesses: Tables would be more suitable for displaying model performance, especially for conference papers. Additionally, the title is overly long and lacks focus. For readers unfamiliar with the subject, the abbreviation "PPB" may be confusing; using it in an already lengthy title is somewhat counterintuitive. In Figures 7 and 8, the x-axis ranges in panels A, B, and C are inconsistent, making it difficult to identify trends. There is also a typo in line 413: "affiity."

### Questions
1. What is the SOTA performance on the PPB task and on the datasets used, such as PPB-Affinity?
2. Why specifically choose iDist and K-nearest neighbors methods? Although PDB code-based and time-based splitting methods are insufficient, why not consider sequence similarity-based splitting methods, for example? 
3. As the authors mentioned in Section 3, the lack of strict data splitting is problematic for validating models. Why do the authors use models trained on randomly split data in Section 5.2? How can model performance be validated when the data splitting process is not strict? Will there be a significant drop in model performance in the virtual screening scenario introduced in Section 5.2 when using strictly split datasets?
4. Why was contrastive learning not selected for feature alignment?
5. I'm unsure whether the log₂ enrichment ratio qualifies as an affinity measurement.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces two new models for the prediction of protein-protein binding affinity (dG) based on protein sequence or protein structure respectively. The data leakage issue for protein-protein interaction datasets is discussed.

### Strengths
1. The idea with the alignment of the structure-based and the sequence-based model is interesting.

2. The focus on dealing with the data leakage issue in PPI datasets is appreciated. Figure 4 illustrates the problem with data splitting well.

### Weaknesses
1. No benchmarking against other methods. In Related work, there is paragraph listing several methods for dG prediction such as dG-Affinity, PPI-Affinity and AREA-Affinity but none of the tools is benchmarked against in the paper. The authors should (i) make sure the related work is up to date and there are no more recent methods for the PPB affinity prediction task and (ii) authors should compare their methods against SOTA. The lack of comparison to existing methods makes it impossible to assess the true performance and novelty of the proposed approach. Specifically, the absence of a comparison to methods like PRODIGY, which is widely used for binding affinity prediction, is a significant oversight. The authors should include a comparison to at least a few well-established methods to properly contextualize their results.

2. The "monotonic neural network-constrained multi-task learning (MMRL)" method is not clear at all. What is the operator $M_{	heta_t}$? It just says it as a monotonic neural network. What is the architecture? What are its parameters trained on? Is it trained together with the task for which equation (6) is used as the objective? Can the authors comment on what are the implications of cooptimizing the task and its learning objective? The description of the monotonic neural network is insufficient. The authors need to provide details on the specific architecture used (e.g., number of layers, activation functions, etc.), how the monotonicity constraint is enforced, and how the parameters are optimized. The lack of clarity makes it difficult to reproduce the results and understand the method's inner workings. Furthermore, the implications of jointly training the monotonic network with the main task are not discussed, and it is unclear how this affects the overall performance.


3. The claimed novelty in partitioning the dataset with iDist is not novel, it has already been done by the authors of iDist [1]. If the authors want to claim novelty, they should explain what is the novelty with respect to [1]. The authors need to clearly articulate how their use of iDist for partitioning differs from the original iDist paper. Simply stating that they use iDist is not sufficient; they need to highlight any modifications or novel applications of the method. Without a clear explanation of the differences, the claim of novelty is unsubstantiated.

4. Significant part of results for PPBind-1D is missing because the Figure 5 is a duplicate of Figure 4. Please fix.

### Questions
1. Did the authors check for potential overlap (e.g. with iDist) between DIPS-plus and PPBAffinity dataset? If there is some overlap, this might explain the success of the alignment procedure.

2. The authors are using DIPS-Plus dataset, which has already been shown to contain many near-duplicates [1]. I suggest using datasets which improved on this issue, are bigger and of higher quality, such as PPIRef [1] or PINDER [2].

3. What is the purpose of Figure 2? It is not well described and it is not sure whether it conveys some important information. Consider removing the figure or explaining its purpose.

4. Line 178-179 "Euclidean distances between each fold of data were calculated as shown." Where is it shown? Please explain in detail (SuppMat can be used).

5. Is the geometric encoder (equations 1-5) completely novel? Did the authors draw inspiration from some existing work? Relevant work should be cited in case inspiration was taken from the literature. If the method is novel, it deserves more attention and it should be discussed in more detail to provide intuition for the equations.

6. I am not sure how advanced is the benchmarking for the dG prediction task, if it is hard to benchmark on that task, the authors could consider using PPI datasets such as PPIRef or PINDER and use the number of contacts between proteins as a proxy for binding affinity [3].

References:

[1] Bushuiev, A., et al. (2024). Learning to design protein-protein interactions with enhanced generalization, ICLR 2024

[2] Kovtun et al. (2024) PINDER: The protein interaction dataset and evaluation resource, bioRxiv 2024.07.17.603980; doi: https://doi.org/10.1101/2024.07.17.603980

[3] Anna Vangone Alexandre MJJ Bonvin (2015) Contacts-based prediction of binding affinity in protein–protein complexes eLife 4:e07454.
https://doi.org/10.7554/eLife.07454

### Soundness
2

### Presentation
2

### Contribution
2
