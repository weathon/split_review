# BrainOOD: Out-of-distribution Generalizable Brain Network Analysis

- Decision: Accept
- Scores: 6, 5, 5

## Abstract
In neuroscience, identifying distinct patterns linked to neurological disorders, such as Alzheimer’s and Autism, is critical for early diagnosis and effective intervention. Graph Neural Networks (GNNs) have shown promising in analyzing brain networks, but there are two major challenges in using GNNs: (1) distribution shifts in multi-site brain network data, leading to poor Out-of-Distribution (OOD) generalization, and (2) limited interpretability in identifying key brain regions critical to neurological disorders. Existing graph OOD methods, while effective in other domains, struggle with the unique characteristics of brain networks. To bridge these gaps, we introduce \textit{BrainOOD},  a novel framework tailored for brain networks that enhances GNNs’ OOD generalization and interpretability. BrainOOD framework consists of a feature selector and a structure extractor, which incorporates various auxiliary losses including an improved Graph Information Bottleneck (GIB) objective to recover causal subgraphs. By aligning structure selection across brain networks and filtering noisy features, BrainOOD offers reliable interpretations of critical brain regions. Our approach outperforms 16 existing methods and improves generalization to OOD subjects by up to 8.5\%. Case studies highlight the scientific validity of the patterns extracted, which aligns with the findings in known neuroscience literature. We also propose the first OOD brain network benchmark, which provides a foundation for future research in this field.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work addresses the out-of-distribution (OOD) problem in brain network analysis. It introduces a framework called BrainOOD, which consists of a feature selector and a structure extractor. By filtering out noisy nodes and edges and enforcing the model to consistently select the same connections across all brain networks within each batch, the proposed method achieves strong performance on the ABIDE and ADNI datasets. Additionally, visualization results are provided to illustrate the method’s effectiveness.

### Strengths
- **Originality**: This paper demonstrates a notable level of novelty, particularly in its combined approach of selecting critical node features and graph structures, along with the batch-level loss designed to identify key discriminative connections.
- **Quality**: The methodology is thoroughly evaluated through comparisons with 16 existing methods across two datasets (ABIDE and ADNI), effectively highlighting its effectiveness and efficiency.
- **Significance**: This research provides valuable insights into addressing the OOD problem in brain network analysis, contributing meaningfully to advancements in neuroscience.

### Weaknesses
 - **Contribution of the Benchmark**

**The claim of introducing the first benchmark seems somewhat overstated.** The ABIDE and ADNI datasets have been long established in brain network analysis and are widely used for evaluating brain disorder diagnosis models. Simply partitioning these datasets to create an OOD scenario may not constitute a significant contribution. The partitioning strategy, while creating a site-specific split, does not inherently introduce a novel challenge beyond what is already considered in multi-site studies. The lack of a clear justification for why this specific OOD split is more challenging or representative of real-world OOD scenarios compared to existing multi-site evaluations is a notable weakness. A more rigorous argument is needed to demonstrate the novelty and significance of this benchmark.

- **Alignment of Motivation, Method, and Analysis**

The motivation of this work is to address the OOD generalization problem. However, **it is not clearly explained how the proposed method specifically tackles this issue**. While reducing noisy nodes and structures could indeed improve brain disorder diagnosis performance, the methodology and interpretive analysis lack clarity on how this approach mitigates the OOD generalization problem. For instance, visualizing the top 10 connections with the highest scores on both the ABIDE ID and ABIDE OOD sets could help demonstrate the method’s generalizability more effectively. The paper needs to explicitly link the proposed feature selection and structure extraction mechanisms to the theoretical underpinnings of OOD generalization, such as invariant feature learning or domain adaptation. Without this explicit connection, the method's effectiveness in addressing OOD generalization remains unclear.

- **Paper Organization**

The organization of the paper could be improved for clarity. **It may not be necessary to dedicate extensive sections to GNN and brain network fundamentals.** Additionally, placing the related work section directly after the introduction or immediately before the conclusion could improve the flow and readability.

### Questions
1. How do you balance the four losses in the proposed method? Given the numerous modules and hyperparameters involved, does training the model from scratch carry a high risk of overfitting?
2. Considering the frequent occurrence of the OOD generalization problem in brain network analysis, how could the proposed method be adapted or transferred to other models?
3. Since the performance of fMRI-derived brain networks on the ADNI dataset is lower than that of structural MRI, do you believe it is appropriate or necessary to use it as a benchmark for the OOD generalization problem?

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
The paper presents BrainOOD, a framework designed to address the challenges of Out-of-Distribution (OOD) generalization in brain network analysis. Specifically, BrainOOD aims to enhance the performance and interpretability of Graph Neural Networks (GNNs) in diagnosing Alzheimer’s Disease (AD) and Autism Spectrum Disorder (ASD). The method incorporates a feature selector, structure extractor, and auxiliary losses, leveraging the Graph Information Bottleneck (GIB) framework to recover causal subgraphs. Through extensive experiments on those datasets, the framework demonstrates competitive performance, outperforming baseline models in OOD settings.

### Strengths
- The paper addresses a critical gap in brain network analysis by focusing on OOD generalization and interpretability, which are essential for deploying models in real-world settings. The work has high significance for the medical and neuroscience community. 
- It presents a framework that improves diagnostic tools for neurological disorders like AD and ASD, potentially leading to earlier and more accurate diagnoses. 
- The authors evaluate their method across two major datasets (ABIDE and ADNI) and compare it with 16 baselines including brain-specific networks, which adds credibility to their results. 
- The alignment of identified brain patterns with known neuroscience findings lends additional weight to the framework's interpretability. Also, ablation study demonstrates the needs of each loss types.

### Weaknesses
1) The technical contribution of this paper appears to be marginal despite addressing the OOD generalization problem and enhancing interpretability in brain network analysis. While the introduction of an OOD benchmark for brain networks is appreciated, it is unclear if this benchmark adds novel challenges beyond those already present in multi-site datasets like ABIDE and ADNI. Specifically, the site-specific variations in these datasets already introduce a form of distribution shift, and the paper does not adequately demonstrate that the proposed OOD split creates a fundamentally different or more difficult challenge. Furthermore, many of the technical components, such as the auxiliary losses and discrete sampling strategy, are borrowed from existing work. Although the paper effectively motivates the need for the Graph Information Bottleneck (GIB) framework, the core technical innovations do not extend significantly beyond prior work, and the specific adaptation to brain networks lacks substantial novelty.

2) One of the primary technical contributions --- feature selection mechanism --- lacks clarity in its formulation. Specifically, the intuition behind $\hat{X}$ derived from the covariance of $\hat{H}$ and the use of the $tanh()$ as activation function is not well explained, leaving readers uncertain about the necessity of these design choices. The paper does not provide a clear justification for why the covariance of the latent representation $\hat{H}$ is a suitable proxy for feature importance in the context of brain network analysis. Moreover, the use of $tanh()$ to scale the reconstructed features to the range [-1, 1] is not sufficiently motivated; other scaling methods could potentially be more appropriate or have different effects on the model's performance.

3) The definition of the OOD problem itself also raises concerns. Table 2 indicates insignificant performance differences between in-distribution (ID) and OOD scenarios, even with the Empirical Risk Minimization (ERM) baseline, suggesting that the OOD scenario may not be as challenging as claimed. This raises the possibility that the proposed framework performs effectively only under moderate distribution shifts. Additionally, the paper would benefit from comparing the performance of other brain-specific models, such as BrainNetCNN or BrainGNN, under the same OOD conditions to better contextualize the reported improvements. The lack of a more rigorous comparison makes it difficult to assess the true impact of the proposed method in the context of existing approaches.

4) Grammar should be double checked.

### Questions
- Please see the weakness above. 

- In addition, can you provide an ablation study on the feature selector and structure extractor by evaluating configurations such as $(X', A)$ and $(X, A')$? These results would help to clearly demonstrate the contribution of each module. Additionally, similar to the discussion on edge scores, the node mask should also be examined to strengthen the claim that the proposed method yields clinically relevant results.

- While several GNNs and HPGNN are incorporated into the framework, certain aspects remain unclear. Specifically, what advantage does using HPGNN with multiple layers (hops) offer over simply multiplying the graph Laplacian matrix, especially if the goal is to capture deviations from local patterns? Furthermore, given your assertion that the brain structure matrix A contains noise, why did you choose to retain A rather than use A’ during feature selection?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents BrainOOD, a novel GNN framework tailored for brain functional network analysis, which consists of feature selector and causal subgraph extractor for brain functional network to enhance the generalization to out-of-distribution dataset. The proposed framework has been evaluated on two multi-site datasets and demonstrated improved classification performance.

### Strengths
It is novel to simultaneously identify informative features and extract causal subgraph for brain functional network based prediction.

### Weaknesses
1. Several descriptions are not clear. Please refer to the Questions section for details.
2. The classification setting (6-class) on the ADNI dataset. It is confusing to have three classes related to MCI (MCI, EMCI, and LMCI), which affects the evaluation results. EMCI and LMCI are used in ANDI GO/2, while MCI used in ADNI 1 is deemed LMCI. A 5-class (CN, SMC, EMCI, LMCI, AD) setting is more reasonable.

### Questions
1. For the adjacency matrix, were the top 20% connections identified based on correlation magnitude (including both positive and negative correlation)?
2. The classification setting (6-class) on the ADNI dataset. It is confusing to have three classes related to MCI (MCI, EMCI, and LMCI), which may affect the evaluation results. EMCI and LMCI are used in ANDI GO/2, while MCI used in ADNI 1 is deemed LMCI. A 5-class (CN, SMC, EMCI, LMCI, AD) setting is more reasonable.
3. It would be helpful to add more description about how the reconstruction loss can help select informative features.
4. It is not clear how in-domain testing was performed. 
5. What are the differences between the 10-fold-CV and the overall test in Tabel 2 and 3?
6. For evaluation, it is better to add some conventional ML methods (e.g., SVM) as baseline.
7. What does the ID and OOD checkpoints mean in Fig.3? The edge score seems quite low (max value around 0.08, Fig.3 top left), how many edges were generally included in the extracted sub-graph?
8. There are several other parameters in the framework (e.g., temperature in eq.11, number of sampling k for the final prediction). How do they affect the performance?

### Soundness
3

### Presentation
2

### Contribution
2
