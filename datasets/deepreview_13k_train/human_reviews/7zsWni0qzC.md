# Interpretable Neural ODEs for Gene Regulatory Network Discovery under Perturbations

- Decision: Reject
- Scores: 5, 5, 5, 3

## Abstract
Modern high-throughput biological datasets with thousands of perturbations provide the opportunity for large-scale discovery of causal graphs that represent the regulatory interactions between genes. Numerous methods have been proposed to infer a directed acyclic graph (DAG) corresponding to the underlying gene regulatory network (GRN) that captures causal gene relationships. However, existing models have restrictive assumptions (e.g. linearity, acyclicity), limited scalability, and/or fail to address the dynamic nature of biological processes such as cellular differentiation. We propose PerturbODE, a novel framework that incorporates biologically informative neural ordinary differential equations (neural ODEs) to model cell state trajectories under perturbations and derive the causal GRN from the neural ODE's parameters. We demonstrate PerturbODE's efficacy in trajectory prediction and GRN inference across simulated and real over-expression datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces PerturbODE, a novel framework that uses neural ordinary differential equations (ODEs) to model gene regulatory networks (GRNs) from single-cell perturbation data. PerturbODE addresses limitations of existing causal graph discovery methods by (i) incorporating biologically-informed ODEs to model cell state trajectories under perturbations, (ii) does estimation in a latent space and (iii) derive GRNs from the ODE parameters by aligning latent and input space. The method can capture non-linear and cyclic gene interactions, which is an advantage over many existing methods and maps cell states to a lower-dimensional "gene module" space, which provides high-level insights into the system. Experiments on simulated and real single-cell RNA-seq datasets show PerturbODE outperforms existing methods in GRN inference and prediction tasks. The authors demonstrate PerturbODE's ability to recover biologically meaningful network structures like negative autoregulation.

### Strengths
- allows to model cyclic GRNs, which is not addressed that much in the literature yet. The authors also provide references that this is an important aspect of biological systems
- the model is quite intuitive in its formulation

### Weaknesses
 - It's very hard to read Figure 5
- I am wondering how identifiable the model is and what number of perturbations is sufficient for this.
- there is no extension towards entropy-regularized OT
- an ablation study on the gamma parameter (scaling the sparsity effect) would be interesting to see

Typos:
- sometimes it's "non-linear" (l53) and sometimes it's "nonlinear" (e.g. l45)

### Questions
- It seems a subset of the modules is recovering relevant biological pathways. However, it only seems to be a very small amount? Can you comment on the other 95% of the modules? Does a Gene-set-enrichtment-analysis confirm your findings?
- Setting delta_j to a fixed value, here 1, would imply that all perturbations have the same strength on its gene. I guess this is not a reasonable assumption, since some perturbations won't have an effect at all?
- Can you clarify how you combine A and B exactly to get the GRNs?

I'm happy to adjust my score based on the answers to the Questions & Weaknesses subsections.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors present PerturbODE, a method based on biologically informed neural ordinary differential equations for modelling perturbation-specific cell trajectories and inferring gene regulatory networks (GRNs) from perturbational (interventional) data. They empirically validate their approach through an extensive set of experiments on both synthetic and real systems. Through their empirical experiments, the authors show that PerturbODE can achieve state-of-the-art performance in high-dimensional settings for the task of GRN inference, relative to counterpart baseline methods.

### Strengths
This work addresses the challenging problem of GRN inference and cell trajectory inference - both important problems in computational biology. The authors propose a novel method based on neural ODEs that incorporates biologically informed dynamics to address both problems. PerturbODE has three key strengths that work towards addressing these longstanding problems in the computational biology community:

1. GRN inference over high-dimensional systems is a challenging task. The authors demonstrate that their novel method, PerturbODE, is able to learn GRNs for high-dimensional systems. 
2. A challenging problem in trajectory inference of cells is predicting the response of cellular systems under unseen interventions/perturbations. The authors show that PerturbODE is able to achieve improved performance on this task relative to counterpart baselines.
3. PerturbODE is able to model and learn cyclic dependencies, pertinent to GRN inference.

### Weaknesses
Although this paper works towards addressing important and challenging problems of GRN inference and cell response prediction, there remain several shortcomings that limit the contributions of this paper (see below).

- If one of the claims is that PerturbODE can model cyclic dependencies between variables (genes), why evaluate on systems where the data generative processes adhere from directed acyclic graphs (DAGs)? If I understand correctly, SERGIO is limited to simulating systems given a DAG representation of a GRN. In this case, it may be useful to consider other biological system simulation tools in addition to SERGIO, for example, the framework in [1] could be used. At the minimum, this can be done in smaller systems (10-100 genes) to empirically validate the claims that PerturbODE can model cyclic dependencies. It is unclear if the method can truly capture cyclic dependencies if the evaluation is performed on data generated from DAGs. The authors should consider using a simulator that can generate data from cyclic GRNs to properly validate this claim.
- Likewise, for results on GRN inference on the transcription factor (TF) atlas, it is not clear if the ground truth GRNs are DAGs or contain cycles. In 4.2.2, the authors discuss that PerturbODE is able to predict negative feedback loops. However, in Appendix 6.7, the ground truth GRNs which are used for evaluation on the TF atlas (shown in Figures 15, 16, and 17), appear to be acyclic. It is not clear how the assessment of PerturbODE's ability to learn cyclic dependencies in GRNs is accomplished in this section. Further explanation and details are required to convey the significance of this result (and likewise this contribution). The authors should clarify whether the ground truth GRNs used for evaluation on the TF atlas are indeed acyclic, and if so, how the claim of modeling cyclic dependencies is supported by the experiments.
- This work focuses on the task of GRN inference from interventional data. However, only a select few baseline methods are considered and compared. There exist many methods specifically tailored for GRN inference. To give a few examples, I refer the authors to [1]. I think it is okay if other GRN inference methods are not included, but it would be beneficial to include some discussion and justification on why the baselines considered in this work are sufficient for fair evaluation. The authors should provide a more thorough justification for the choice of baseline methods, addressing why other relevant GRN inference methods were not included, and discuss the limitations of the current comparison.
- For experiments in 4.2.1 for predicting response on held-out interventions. The authors compare only to baselines that are not necessarily tailored for this task. There exist state-of-the-art methods that address this problem, for example [2, 3]. To effectively showcase the utility of PerturbODE, it would be beneficial to compare to an existing method designed for predicting response to perturbations in biological systems since the NOTEARS baselines are not designed for this task. Without a biological-specific baseline for predicting response to perturbations, it is difficult to assess how PerturbODE performs relative to state-of-the-art methods. Moreover, it would be helpful to include a baseline that does not learn a GRN and is just trained to predict the perturbational response. Such a method should not work in the setting of unseen interventions since it will never see those conditions, but can be informative of whether or not learning the GRN is actually beneficial for this task. The authors should include a baseline method specifically designed for predicting responses to perturbations, and also consider a baseline that does not learn a GRN to assess the benefit of learning the GRN for this task.

In general, there are still various details missing regarding experimental details, empirical validation of discovered GRNs, and justification of design choices of the method (see questions below). This makes the paper somewhat incomplete and hinders the presentation of the method and results. I think if these items are addressed, it would improve the overall quality of the paper.

### Questions
- Lines 245 - 246: Beyond use for benchmarking, what is the justification of classifying negative edges as non-existing edges? Why not take the absolute value over $\mathbf{W}$ and consider all edges as positive edges? 
- The authors state that the structural hamming distance (SHD) metric would strongly favour predictions of empty graphs due to sparsity of ground truth GRNs (Lines 318 - 320). Do the methods tend to return empty graphs such that this would be the case? If the methods do return empty graphs, would this not be reflected in the other metrics, while still getting a performance metric through SHD that gives some global view on how the methods perform on predicting the GRN graph.
- For the experiments in 4.1 and 4.2, why not compute other additional metrics? For instance, given that the data has intervention, the negative log-likelihood of data points under intervention (I-NLL, done in DCDFG) could be computed. Possibly area under the ROC (AUROC) could also be computed to give an additional view of the results.
- In Figures 2 and 4, what are the mean and std for box plots computed over? Different graphs? 
- For performance evaluation, the authors threshold $\mathbf{W}$ to construct a binary adjacency matrix so that the evaluation metrics can be computed. This is done by selecting some small value $\epsilon$ and setting edge weights below $\epsilon$ to $0$ and above $\epsilon$ to $1$. The determination of $\epsilon$ depends on a parameter $c$. This seems like a limiting factor in the sense that as $c$ is changed, performance may change
    - How do you decide the value of $c$? Is this value determined via SERGIO? 
    - Is this treated as a settable parameter? If so, how would the results change as the value of $c$ is changed?
- On the SERGIO simulated data the authors claim that PeturbODE gives significantly higher precision, recall, and F1 scores compared to DCDFG, NOTEARS, and NOTEARS-LR, while comparable scores DCDI, especially in the high dimensional case (400 genes). Compared to DCDI, it appears PerturbODE also yields a significantly higher variance on Recall and F1 score, while performing overall worse on precision. Is there intuition as to why PerturbODE yields such a high variance on Recall? I assume since there is variance on recall, this leads to variance on F1 score as well.
- For the task of predicting the response of unseen interventions (In Table 1) is there intuition as to why PerturbODE performs worse on the 2-Wasserstein metric, but significantly better on Pearson correlation? In general, this is a very difficult task. It could help to observe how the numbers for these metrics look for seen interventions (see earlier question regarding Interventional-NLL).
- For the result presented In Figure 4, the authors state GRN inference is done for a system of 817 genes. But the ground truth GRNs shown in Appendix 6.7 have far less genes. Are the GRNs shown in Appendix 6.7 Figures 15, 16, and 17 only the non-zero edges in the ground truth GRNs? 
- If the objective is to learn a flow map for pushing initial samples over time (eq 3), why not use the recent advances in flow matching [4], which can achieve the same result in a significantly more efficient manner using simulation-free training, compared to Neural ODEs? This could potentially enable further scaling. 

References:

[1] Pratapa, Aditya, et al. "Benchmarking algorithms for gene regulatory network inference from single-cell transcriptomic data." Nature methods 17.2 (2020): 147-154.

[2] Lotfollahi, Mohammad, et al. "Predicting cellular responses to complex perturbations in high‐throughput screens." Molecular systems biology 19.6 (2023): e11517.

[3] Roohani, Yusuf, Kexin Huang, and Jure Leskovec. "Predicting transcriptional outcomes of novel multigene perturbations with GEARS." Nature Biotechnology 42.6 (2024): 927-935.

[4] Lipman, Yaron, et al. "Flow Matching for Generative Modeling." International Conference on Learning Representations. (2023)

### Soundness
2

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
3

### Summary
The paper titled “Interpretable Neural ODEs for Gene Regulatory Network Discovery under Perturbations” presents PerturbODE, a neural network designed to model cell state trajectories and derive causal gene regulatory networks (GRNs) from its parameters. The authors propose a model that utilizes neural networks to infer changes in gene expression levels based on their current states. A notable contribution of this work is its ability to model GRNs with negative edges and explicitly specify perturbed genes. The study demonstrates PerturbODE’s effectiveness in deriving the ground truth GRN and highlights its potential to predict cellular responses to novel perturbations.

### Strengths
1.PerturbODE offers excellent interpretability, with parameters that reveal clear relationships between genes and the inferred gene modules.

2.The innovative approach of PerturbODE effectively captures key biological processes, such as cellular differentiation and negative feedback regulation.

3.The authors have conducted comprehensive experiments, comparing PerturbODE with other methods on both simulated and large-scale perturbational scRNA-seq datasets. They also explore its capability to identify negative autoregulation and infer gene modules.
4.The paper is well-organized, featuring clear explanations of the methodology.

### Weaknesses
1.It would be beneficial to include more discussions and experiments addressing instances where PerturbODE does not outperform other models.

2.In Section 4.2.1, a more detailed discussion about performance variations could enhance clarity and understanding.

### Questions
1.Have you considered using a more complex or simpler model? How might this impact performance?

2.Could you elaborate on how this work contributes to our understanding and discovery of gene modules?

3. In the experimental phase, the paper primarily presents metric-based results, showing that the method outperforms others. However, in solving a specific GRN problem, the focus should be on whether the inferred GRN can identify key genes or transcription factors (TFs) that can then undergo downstream analysis. For a biological application, simply comparing metrics does not sufficiently demonstrate the model’s effectiveness.

4. In GRN inference problems, perturbation experiments for some key genes are also an important downstream analysis. Including some perturbation experiments could help validate the accuracy of the inferred GRN.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors propose PerturbODE, a framework based on neural ODEs to infer causal GRNs from scRNA-seq data. PerturbODE aims to address limitations of prior methods regarding scalability, and modeling capacity. Two simulated experiments are performed as well as an experiment using real-life perturbation data (TF atlas).

### Strengths
- The study is well-motivated and the writing is clear. Addressing causality in GRN inference is important as most methods rely on gene co-expression networks.
- The proposed method scales well to large datasets, which is essential in an era where large-scale omics datasets are increasingly common.
- The model can handle both perfect and imperfect interventions, which can model a wide range of experimental conditions.

### Weaknesses
My main concerns with this paper relate to experiments. It is not evident from the validation analysis that the proposed method is superior. Furthermore, the study would benefit from incorporating a larger number of real life datasets and baselines. See detailed comments below.

- There is a large discrepancy in the number of selected edges between PerturbODE and the baselines for the atlas TF dataset (103,941 for PerturbODE and fewer than 500 for NO-TEARS and NO-TEARS-LR). It is not clear how meaningful the reported recall scores are given such discrepancy. Tuning parameters to select more edges in the baselines or including other baselines from causality literature [1-2] is necessary to provide a more accurate comparison. The reported recall scores are difficult to interpret without a more thorough analysis of the edge selection process for the baselines, including a sensitivity analysis of the parameters that control edge selection.
- The total number of genes used in the TF atlas is 817, for a total of 667,489 possible edges. Selecting 100k from these (around 1/6) will likely inflate recall scores and, furthermore, is not very biologically plausible (you would expect around 3 interactions per gene on average [3]). The high number of predicted edges, without a clear justification or biological validation, raises concerns about the method's specificity and potential for false positives. A more detailed analysis of the distribution of the predicted edges, and comparison with known biological networks, would be necessary to assess the plausibility of the results.
- Only one real experimental dataset is used (TF atlas) in the benchmark. Incorporating other datasets (e.g., from drug treatment, environmental stress) is necessary to support the claims made in this paper. The lack of diversity in the real-world datasets limits the generalizability of the findings. Datasets with different types of perturbations and experimental designs would provide a more robust evaluation of the method.
- The analysis is largely performed on edges and gene modules. More biological validation, e.g., gene enrichment analysis of top regulated genes, would enhance the biological validity of the model. The current analysis lacks a deeper biological interpretation of the predicted networks. Functional enrichment analysis of the genes within the predicted modules, and comparison with known biological pathways, would provide a more meaningful evaluation of the method.
- Comparing against established methods for (non-causal) GRN inference (e.g., from the BEELINE benchmark [4]) would help the reader determine the utility of such causal models. The absence of comparisons with well-established GRN inference methods makes it difficult to assess the added value of the proposed causal approach. A comparison with methods that do not explicitly model causality would help to determine if the added complexity of the causal model is justified by improved performance.
- Other methods have proposed neural ODEs for GRN inference [5]. A comparison with these or explanation why they are not applicable may be necessary. The lack of comparison with other neural ODE-based methods for GRN inference makes it difficult to assess the novelty and advantages of the proposed approach. A detailed discussion of the differences and similarities with existing neural ODE-based methods, and a justification for the chosen architecture, would be necessary.

### Questions
- Would help to show $-\log_{10}$(p-values) rather than p-values in plots.
- How important is the decay component in (1)? RNA decay may or may not be plausible for cells 7 days after perturbation.
- As I understand it, the TF atlas consists of 2 time points. Can the method work with scRNA-seq datasets with multiple time points?

### Soundness
2

### Presentation
3

### Contribution
2
