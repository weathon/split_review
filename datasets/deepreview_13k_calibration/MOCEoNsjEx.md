# Pg-GAT: A Complete Graph Model for Cancer Detection and Subtyping in Whole Slide Images Analysis

- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 1, 3, 3, 5

## Abstract
Whole-Slide-Images (WSIs) have generated significant interests in cancer research community, owing to their availability and the rich information that they provide. Previous Multiple Instance Learning (MIL) methods often 
neglect the topological structure of tissues which is closely related to tumor evolution. Some attempts with transformer-based MIL methods take spatial relation into account with a trade-off of computational complexity. We propose Projection-gated Graph Attention Network (Pg-GAT), a lightweight model that effectively leverages graph neural network to provide structural prior, learns spatial and contextual relations through graph attention, and mitigates tissue morphology redundancy with differentiable projection-gated pooling, maintaining a data-adaptive decision boundary. In addition, Pg-GAT outputs region-of-interest (ROI) with respect to the graph-level prediction with post-hoc graph explainer, offering tumor localization and model interpretability. We evaluate our method on lymph node metastasis datasets (CAMELYON16 and CAMELYON17) and non-small cell lung cancer (TCGA-NSCLC), achieving AUCs of 97.6\% and 95.6\% and 99.6\% respectively, outperforming state-of-the-art methods.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper introduces Pg-GAT, a graph-based framework for whole-slide image (WSI) analysis, enhancing spatial and contextual awareness with in-graph hierarchical aggregation. By using an initial Euclidean grid graph and projection-gated pooling, Pg-GAT effectively adapts to imbalanced class distributions typical in WSIs. The model achieves good performance on benchmarked TCGA datasets. However, The authors seem to lack an understanding of relevant work and advancements in this field, the proposed concept/method is not novel, and I could not see their contributions to this field.

### Strengths
- **Clear Logical Flow:** The paper is structured logically, presenting each component of Pg-GAT in a clear, sequential manner that enhances readability and understanding.

- **Organized and Coherent Writing:** The writing is well-organized, with concise explanations that make mentioned concepts more accessible to the reader.

- **Comprehensive Visualizations:** The paper provides visualizations that illustrate the model’s performance and tumor localization capabilities, adding clarity and support to the claims.

### Weaknesses
This work replicates the pipeline established in MUSTANG [1] published at BMVC 2023, without proper acknowledgment or citation. The fundamental proposed architecture and application area - hierarchical GAT layers combined with pooling for WSI analysis - is identical to MUSTANG's published approach.

The only differences are the authors:

- Use a "grid-graph" defined on spatial nearest neighbors, rather than a k-NN graph defined in feature space. The use of spatial nearest neighbor graphs was established in [2], which is not cited either. 
- Use of Projection-gated topK pooling [3] instead of SAGPooling [4]. Ablation on this was also carried out in MUSTANG. 
- Apply this approach to benchmark CAMELYON and TCGA datasets, rather than the multi-stain dataset used in MUSTANG. 
- Apply pos-thoc GNNExplainer[5]

Neither of these differences represents a significant technical contribution for a conference such as ICLR. I therefore recommend rejection based on lack of novelty and proper attribution.

### Questions
- **Enhance Novelty in Graph Construction:** To distinguish Pg-GAT from existing methods, consider integrating unique graph construction techniques, such as incorporating both spatial and semantic relationships in node connectivity or exploring heterogeneous graph structures. Highlighting any specific advantages of your approach compared to H2MIL, TEA-Graph, or HEAT would also strengthen the novelty of your work.

- **Expand Experimental Comparison:** Adding comparisons with recent methods like DFTMIL could provide a clearer benchmark for Pg-GAT's performance. Evaluating Pg-GAT against a broader set of state-of-the-art approaches will help establish its competitive strengths and limitations.

- **Update or Clarify Code Link:** Ensure that the code link in the abstract is valid and accessible. If the code is not yet available, consider specifying a release timeline in the abstract or mentioning that it will be provided upon publication.

- **Clarify Interpretability Contributions:** If model interpretability is a key contribution, consider developing additional interpretability techniques beyond standard tools, or clarify the unique insights Pg-GAT offers. Explicitly discussing how your model leverages these tools in a way that adds value could address overclaim concerns.

- **Include Computational Efficiency Metrics:** To substantiate claims of computational efficiency, incorporate FLOPs or runtime comparisons with similar models. This would provide quantitative evidence of Pg-GAT’s computational advantages and validate the claim of being lightweight.

### Soundness
1

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper proposes the Projection-gated Graph Attention Network (Pg-GAT) framework, a hierarchical graph framework composed of successive GAT + Gated Projection TopK Pooling layers. After each GAT + TopK layer, max pooling is applied to obtain a readout vector. The readouts are finally averaged and input into the final MLP classification layer. This approach is applied to three benchmark datasets: CAMELYON16, CAMELYON17 and TCGA-NSCLC and compared to 4 baseline methods (CLAM, TransMIL, GTP, CAMIL). Performant results are shown across datasets. Post-hoc interpretability heatmaps were obtained using the GNNExplainer module. Ablation was carried out on the type of pooling operation (TopK, SAGPool, Mean) and graph convolution (GAT, GCN).

### Strengths
The paper is clear and well written.

### Weaknesses
1. The use of spatial graphs and graph attention networks for WSI analysis can't be viewed as contribution in 2024. Several prior graph-based methods for WSIs, such as PatchGCN [1], TEA-Graph [2], and SlideGraph+ [3], already incorporate spatial encoding and graph neural networks for WSI analysis. This prior work is notably missing from the paper’s introduction, overlooking important context for the field.

2. The paper’s critique of earlier methods lacks specificity. It is unclear which prior methods employ spectral graphs in WSI analysis, or why spatial graphs, as implemented here, would not require a large adjacency matrix. Additionally, the claim of “unleashing the potential of attention mechanisms” is vague; graph attention networks (introduced in 2017) [4] have long supported attention mechanisms, raising questions about Pg-GAT’s unique contributions beyond the projection-gated pooling.

3. Evaluating Pg-GAT on a binary cancer classification task does not fully leverage the model’s contextual learning capabilities, as the task could be solved with only one positive patch. A more suitable evaluation might involve context-dependent tasks, such as survival prediction, where broader spatial relationships are essential.

4. The baselines in Table 1 are insufficient, especially with two methods omitted due to out-of-memory errors, leaving only three comparison models (two of which are variants of CLAM). This limited comparison fails to provide a comprehensive benchmark against relevant methods.

5. The unexpectedly strong performance of Mean-GAT in TCGA-NSCLC compared to more established methods like TransMIL, CLAM, and GTP suggests potential issues in evaluation or methodology. This inconsistency should be clarified to ensure the robustness of Pg-GAT’s reported results.

6. Pg-GAT’s low detection performance in Table 2 contradicts its claim of effective tumor localization. This discrepancy undermines the model’s stated contribution of providing interpretability and detection capabilities.

### Questions
- How does the pipeline proposed in this work differ from that proposed in MUSTANG?

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces Projection-Gated Graph Attention Network (Pg-GAT) for analyzing whole-slide images (WSIs) in pathology. Pg-GAT leverages graph neural networks to capture structural, spatial, and contextual relationships while reducing redundancy in tissue morphology. The model employs a projection-gated pooling mechanism to create adaptive decision boundaries and provides both tumor detection and localization.

### Strengths
1. The projection-gated pooling mechanism is a novel contribution, adding value to the model's adaptability.
2. The paper includes comprehensive experiments at both slide and patch levels to evaluate its effectiveness.

### Weaknesses
My major concerns are about the experiments:

- The proposed method cannot achieve SOTA performance on Camelyon 16 and 17 benchmarks. Why not listing the challenge winners in table 1? For example, in Camelyon 16 challenge, the winner (Harvard & MIT) already achieves 99.4% AUC. Also, the SOTA of Camelyon 17 is from DeepBio Inc. For more recent results on the two benchmarks, you can check table 1 in PFA-Scannet [MICCAI 2019].  It is suggested to include a comparison to these top-performing methods and explain how your approach compares in terms of performance and computational efficiency.

- Why not using the challenge metrics for evaluation? For Camelyon16, FROC is a more challenging metric compared with AUC reported in this paper. Also, kappa score should be compared for Camelyon17 benchmark. Please explain why you chose AUC over FROC for Camelyon16 and to provide results using both metrics if possible. Similarly, for Camelyon17, results using the kappa score are requested, which would allow for a more direct comparison to other methods evaluated on this benchmark.

- The tumor localization performance is not satisfying. Even though the proposed method is not prioritized for this task, the gap of CAMIL, around 3% dice, is too large. Please discuss potential reasons for this performance gap in tumor localization, and suggest ways that might improve this aspect of proposed method, even if it's not the primary focus.

### Questions
1. Overall, while Pg-GAT’s projection-gated pooling is an interesting contribution, the paper requires substantial improvement in establishing its novelty, clarifying its claims, and providing comprehensive evaluations to be competitive within the field of computational pathology.
2. The provided GitLab link was inaccessible; please verify the link’s accessibility before including it in the submission.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper introduces a Projection-gated Graph Attention Network (Pg-GAT) for Whole-Slide Image (WSI) analysis, focusing on cancer detection and subtyping. Pg-GAT leverages a graph neural network (GNN) framework to model spatial and contextual relationships within tissue structures, advancing traditional Multiple Instance Learning (MIL) methods. With a differentiable pooling mechanism, it aims to reduce tissue morphology redundancy while maintaining interpretability through tumor localization.

### Strengths
- Proposes a lightweight GNN architecture that models spatial and contextual relationships within WSIs, claiming efficiency and interpretability.
- Comprehensive experimental setup that benchmarks against notable graph- and non-graph-based models.
- Demonstrates the capacity for tumor localization, with interpretability results provided through visualization and GNNExplainer analysis.

### Weaknesses
- **Novelty limitations**: The proposed use of Graph Attention Networks (GAT) for WSI-based cancer analysis has precedent in prior studies, reducing the novelty of Pg-GAT in this context[1,4]. DASMIL [1], for example, already uses a GAT layer and message passing to allow interaction along patches on different resolutions before attention pooling. 
- **Performance Concerns**: Results in Tables 1 and 2 do not consistently outperform baselines across all metrics. Specifically, Pg-GAT's tumor localization scores, evaluated by the Dice score, and classification accuracy fall short of fully distinguishing it from competing methods. More relevant confidence-based metrics, such as FROC, are related to localization and Camelyon. Since it is based on confidence, it measures the capabilities to distinguish diseases without any manual threshold.
- **Limited Scope in Model Efficiency Analysis**: Figure 4, presenting model size versus performance, is restricted to a single dataset, limiting insights into Pg-GAT’s comparative efficiency across different dataset complexities.
- **Different backbone**: Attempts to reproduce baselines such as GTP and CAMIL resulted in out-of-memory (OOM) issues, so results were drawn from prior publications. However, this approach introduces limitations, as these reported baselines utilize a different backbone (SIMCRL), which could affect comparability and undermine the experimental rigor. That comparison is vital to quantifying how the solution is better than other GNN-based solutions.
- **Interpretability Limitations**: The interpretability section would benefit from more generalized tumor examples to substantiate that Pg-GAT can adapt to varied tumor complexities.

### Minor Comments
- Clarify abbreviations as Acc and Minor typographical errors in section headers and figure captions should be corrected (e.g., "TansMIL" to "TransMIL").
- Several mentioned methods do not appear in the comparison tables as ABMIL, DSMIL, STEMIL, EGT  **(graph-based)**
- Limited Focus in Related Work: The Related Work section centers primarily on GNN-based approaches for WSI analysis rather than providing a balanced discussion that includes broader Multiple Instance Learning (MIL) solutions for WSIs. A more comprehensive review of MIL approaches used in generic WSI settings would better contextualize Pg-GAT within the landscape of WSI analysis techniques. Additionally, CAMIL and GTP are presented as primary graph-based baselines, but they are not the only approaches that employ graphs for WSI representation( EGT, DASMIL[1], H2MIL[2], GDSMIL[3]). Including a discussion on other graph-based MIL solutions would provide a clearer picture of how Pg-GAT fits among similar models and address potential limitations in novelty.
- This manuscript lacks implementation details (lr, scheduler, epochs, batch_size, etc.), which doesn't allow for reproducibility

[1]: A Graph-Based Multi-Scale Approach With Knowledge Distillation for WSI Classification, TMI 
[2] H^2-MIL: Exploring Hierarchical Representation with Heterogeneous Multiple Instance Learning for Whole Slide Image Analysis
[3] Enhancing PFI Prediction with GDS-MIL: A Graph-Based Dual Stream MIL Approach.
[4] Whole Slide Cervical Cancer Screening Using Graph Attention Network and Supervised Contrastive Learning

### Questions
Why do you have OOM with other baselines? Are you working with batch_size=1? Is the issue related to training or inference? Consider exploring subgraph sampling during training to address the OOM issues with baselines. This approach might allow for dropping patches while augmenting the number of slides, potentially improving efficiency and performance.  What is the contribution of the work to other GAT-based solutions?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper propose a lightweight graph network for whole-slide images analysis, in which the nodes are grid patches and edges are initialized as the Euclidean distances. Compared with previous methods, the proposed GAT can efficiently learn both the local context information and global structure that are hard to extract from whole-slide images. More specifically, the projection-gated pooling technique can introduce sparsity and hierarchy among graph nodes, making it effective to remove morphological redundancy and aggregate global information. In overall, the graph formulation for whole-slide images is interesting and straightforward. However, part of the experiment results are not solid enough and do not achieve the SOTA performance. If my concerns can be addressed, I would like to raise my ratings to borderline above.

### Strengths
- The graph formulation for whole slide images are straightforward and interesting, and more importantly, it is costly efficient.

- The global structure learning is inspiring. The ways of how to remove morphological redundancy and perform in-graph hierarchical aggregation are effective and non-trivial. 

- The paper is well-written, and the method can be easily followed by readers.

### Weaknesses
My major concerns are about the experiments:

- The proposed method cannot achieve SOTA performance on Camelyon 16 and 17 benchmarks. Why not listing the challenge winners in table 1? For example, in Camelyon 16 challenge, the winner (Harvard & MIT) already achieves 99.4% AUC. Also, the SOTA of Camelyon 17 is from DeepBio Inc. For more recent results on the two benchmarks, you can check table 1 in PFA-Scannet [MICCAI 2019].  It is suggested to include a comparison to these top-performing methods and explain how your approach compares in terms of performance and computational efficiency.

- Why not using the challenge metrics for evaluation? For Camelyon16, FROC is a more challenging metric compared with AUC reported in this paper. Also, kappa score should be compared for Camelyon17 benchmark. Please explain why you chose AUC over FROC for Camelyon16 and to provide results using both metrics if possible. Similarly, for Camelyon17, results using the kappa score are requested, which would allow for a more direct comparison to other methods evaluated on this benchmark.

- The tumor localization performance is not satisfying. Even though the proposed method is not prioritized for this task, the gap of CAMIL, around 3% dice, is too large. Please discuss potential reasons for this performance gap in tumor localization, and suggest ways that might improve this aspect of proposed method, even if it's not the primary focus.

### Questions
- Any justification of using DINOv2 as the pretraining image feature? The recent pretrained RADIO feature can be a better design choice, since it is distilled from CLIP, DINOv2 and SAM, containing richer information (both low-level correspondence and high-level semantics) in the features. Please compare the performance of your method using DINOv2 versus RADIO features, or to explain why you believe DINOv2 is more suitable for your task.

- How much morphological redundancy can be removed after performing top-k ranking? Please. provide quantitative results showing the reduction in node count (from N to M), and to discuss how this affects the model's performance and efficiency.

- The effectiveness of GAT is questionable, compared with GCN. As shown in table 4, the improvement of GAT over GCN is very marginal. Please provide a more detailed analysis of why GAT was chosen over GCN.

### Soundness
3

### Presentation
3

### Contribution
2
