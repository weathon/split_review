# Global Context-aware Representation Learning for Spatially Resolved Transcriptomics

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 5, 6, 6

## Abstract
Spatially Resolved Transcriptomics (SRT) is a cutting-edge technique that captures the spatial context of cells within tissues, enabling the study of complex biological networks. Recently, graph-based deep learning has been utilized in identifying meaningful spatial domains by leveraging both gene expression and spatial information. However, these approaches fall short in obtaining qualified spot representations, particularly for those located around the boundary of cell type clusters, as they heavily emphasize spatially local spots that have minimal feature differences from an anchor node. To address this limitation, we propose a novel framework, Spotscape, which introduces the Similarity Telescope module designed to learn spot representations by capturing the global relationships among multiple spots. Additionally, to address the challenges that arise when integrating multiple slices from heterogeneous sources, we propose a similarity scaling strategy that explicitly regulates the distances between intra- and inter-slice spots to ensure they remain nearly the same. Extensive experiments demonstrate the superiority of Spotscape in various downstream tasks, including spatial domain identification, multi-slice integration, and alignment tasks, compared to baseline methods. Our code is available at the following link: https://anonymous.4open.science/r/Spotscape-E312/

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper introduces a framework called Spotscape, designed to improve spatial transcriptomics data representation for enhanced analysis of spatial domain identification, and multi-slice integration and alignment. Spotscape utilizes a graph autoencoder and incorporates various loss terms to optimize the learning of spot representations, thereby improving clustering and alignment. Applied to five datasets, the framework demonstrates its effectiveness in predicting spatial domains of brain layers and mouse embryos, aligning temporal spatial transcriptomics data, and integrating spatial data across different resolutions.

### Strengths
1. Current whole-transcriptomic spatial sequencing platforms, such as 10x Visium, face challenges with low spot resolution, where each spot may capture transcripts from tens of cells. This limits the accuracy of clustering spatial domains, like brain layers. Spotscape demonstrated notable improvements in domain prediction accuracy in the human dorsolateral prefrontal cortex and mouse embryo data. 
2. Batch effects are a common challenge in integrating and aligning multi-slice spatial data, particularly for temporal data analysis. Spotscape showed superior performance in reducing batch effects across most datasets compared to other methods. 
3. Ablation studies highlighted the importance of incorporating various loss terms in the proposed graph auto-encoder model, demonstrating their critical role in enhancing data representation quality.

### Weaknesses
1. While Spotscape demonstrated significant improvements in spatial domain identification across two Visium datasets(DLPFC and MTG), its performance on the Stereo-seq platform for mouse embryo profiling showed only modest gains compared to existing algorithms, such as domain detection with STAGATE (Fig. 3B) and batch correction with STAligner (Table 4). This difference may stem from the higher resolution of Stereo-seq (0.2 µm per spot) compared to Visium’s lower resolution (55 µm per spot). The higher resolution likely enhances cell type and spatial domain identification, potentially diminishing Spotscape's advantage. With rapid advancements in spatial transcriptomics profiling—improving resolution, gene coverage, and sensitivity—Spotscape must demonstrate strength across both low-resolution platforms like Visium and high-resolution platforms like Stereo-seq, seqFISH+, Pixel-seq, etc., to contribute significantly to spatial data analysis. Furthermore, the modest gains on Stereo-seq raise concerns about the generalizability of Spotscape's approach, particularly whether its reliance on graph-based methods is as effective when spatial resolution is not a limiting factor. The method's performance should be evaluated on a wider range of high-resolution datasets to ascertain its true utility.
2. While the inclusion of prototypical contrastive learning loss in Spotscape may improve spatial domain prediction, it could potentially impact other downstream tasks, such as trajectory prediction across cell types or states. The contrastive loss may enforce a discrete latent space representation, which could disrupt the continuous nature of biological processes needed for accurate trajectory inference. This is a critical concern, as many spatial transcriptomics studies aim to understand developmental or disease progression, which relies on accurate trajectory analysis. The paper should include an analysis of how the prototypical contrastive loss affects downstream tasks beyond clustering, particularly those that rely on a continuous latent space.
3. Several parameters, such as learning rate, number of clusters (K), and lambda values for each loss term, appear hardcoded in the provided code. It is unclear how to optimize these parameters for new datasets and whether a comprehensive search for optimal values is required. The lack of a clear parameter tuning strategy raises concerns about the practical applicability of Spotscape, especially for users who may not have the expertise or computational resources to perform extensive hyperparameter searches. The paper should provide clear guidance on how to select these parameters, and ideally, propose a more robust and less computationally intensive approach for parameter optimization. Additionally, the computational cost of this parameter search, especially for large datasets containing 40–100 spatial transcriptomics samples, needs to be addressed. The paper should provide a detailed analysis of the computational resources required for parameter optimization and the overall runtime of the method.
4. It is worth noting that single-cell embedding models like scGPT and scFoundation, which are trained on millions of cells, have demonstrated superior performance in cell type clustering and data integration. A comparison between Spotscape and these pre-trained deep learning models on spatial transcriptomics data would be valuable to determine if Spotscape can outperform these models on the proposed tasks. The lack of comparison with these powerful pre-trained models leaves a gap in the evaluation of Spotscape's performance, as it is unclear whether the proposed method offers a significant improvement over existing state-of-the-art single-cell analysis techniques when applied to spatial data.

### Questions
In addition to the main weaknesses, there are a few minor points of clarification:
1. In lines 40–42, the manuscript states, "However, they fall short in predicting accurate clustering results due to the inherent noise in SRT data." Clustering does not inherently have a predefined "accuracy." It would be clearer to specify accuracy in terms of cell type or brain layer annotation. 
2. In lines 48–49, the manuscript mentions that GNN methods have limitations, especially for spots around cell type cluster boundaries, and subsequently states that the STAGATE algorithm was developed to address this issue. However, STAGATE primarily addresses boundaries of brain layers, not cell types. Assigning cell types to Visium data is challenging, as each spot may contain multiple cells. Researchers often prefer cell type deconvolution or refer to clusters as "cell type-enriched" rather than assigning a single cell type to each spatial transcriptomics cluster for low resolution data. 
3. In lines 71–73, the manuscript states, "where cells that are spatially close often exhibit strong feature similarity even when they serve different functions." To support this general statement, it would be helpful to reference a review paper rather than a figure to clarify whether this phenomenon is specific to the dataset used or is observed across multiple datasets. This may not universally apply to all datasets, as spatial transcriptomics profiling is widely used to detect cell type and tissue structure differences in various disease contexts.

### Soundness
3

### Presentation
4

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
The authors propose a novel framework, Spotscape for spatial domain identification and SRT data integration, which achieves impressive performance. The Spotscape framework introduces a slide-level contrastive learning module to learn the spot representation, a prototypical contrastive learning loss for enhancing clustering, a reconstruction loss to stabilize the optimization procedure, and a similarity scaling strategy that maintains consistency across different tissues. 

The paper attempts to address some issues unsolved by previous studies, for example, the suboptimal result for boundary spots, the batch effect across multiple slides. The motivation is clear and sensible.

### Strengths
1. The paper studies some prominent issues, such as boundary spots, and batch effect.

2. The paper provides comprehensive experiments. The baseline models, experiment setups, and ablation studies are all carefully selected. The performance of the method is hightly competitive.

3. The paper provides source codes for reproducibility.

### Weaknesses
1. The logic of the methodology design is not very clear, some designs are very ad-hoc, which needs further clarification.

2. It is not clear how the hyperparameters lambdas are selected. In the codes provided by the authors, those hyperparameters are manually specified. It is possible that these lambdas are chosen to achieve the best test performance, which is not fair for other baseline methods. The authors need to provide additional hyperparameter-sensitive analysis to justify this.

3. It is not clear how the hyperparameters of the baseline methods are selected. The authors need to show that they made the best efforts to acquire the best performance from the baselines to ensure a fair comparison.

4. The time complexity of this method is not clear. The prototypical contrastive learning objective involves T times of k-means in each training iteration (after 500 epochs), which may dramatically impact the running speed. The author needs to provide justification for the time-performance tradeoff.



### Questions
1. The author mentions multiple times the statement that "In biological systems, cells that are spatially close often exhibit strong feature similarity, regardless of their functional characteristics." Is there any literature to justify this? From my knowledge, this statement is misleading. The similarity only appears at the spot level, while at the cell level, for example, the Xenium data, the cell types locally close to each other are actually quite heterogeneous. Tumor micro-environment is one of the few exceptions where the local cells tend to share similar characteristics. I hope the authors are rigid when making statements about biology. 

Meanwhile, statements are causing confusion like this "However, these approaches fall short in obtaining qualified spot representations, particularly for those located around the boundary of **cell type clusters**, as they heavily emphasize spatially local **spots** that have minimal feature differences from an anchor node." It mentions "cell type clusters" and "local spots" in the same time, while spots typically contain heterogeneous cell types, and they correspond to **spatial domain** instead of **cell type clusters**.

2. "Prototypical Contrastive Learning" aims to enhance clustering and rare cell-type classification (I'm not sure how this benefits spot-level tasks). The idea is essentially similar to many previously established prototypical losses [1,2,etc]. However, I did not see any references in the paper. Should authors cite those methods or justify why they need to propose a different method?

3. The authors proudly state that "instead of relying on any predictor or stop gradient techniques, Spotscape simplifies the training procedure by employing a reconstruction loss". To me, it is not clear how the reconstruction loss provides a better solution than the other options. It seems like the authors just blindly chose a shortcut for the implementation.

[1] Prototypical Contrastive Learning of Unsupervised Representations, ICLR 2021
[2] Population-level integration of single-cell datasets enables multi-scale analysis across samples, Nature Methods

### Soundness
2

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
This paper studies the representation learning for spatial transcriptomics data. The authors argue that capturing global context is critical, especially for spots near boundaries. To address it, they propose pretraining the GNNs using contrastive learning to align the representations between inter- and intra-slice spots. Several experiments including spatial domain identification, multi-slice integration, and alignment, demonstrate the model’s effectiveness.

### Strengths
- The preliminary findings showing low clustering performance for boundary spots are interesting and can potentially motivate some future studies to address such an issue.
- The experiment is comprehensive, including multiple datasets across different sequencing technologies and patient samples. Additionally, aligning slides sequenced by Visium and Xenium is both practically significant and challenging due to batch effects.
- For methodology, the paper demonstrates the effectiveness of graph contrastive learning in spatial transcriptomics data.

### Weaknesses
 - The motivation is to capture global context through graph contrastive learning, but they haven't justified it. It’s not surprising that graph contrastive learning can improve GNN’s performance [1,2,3]. The clustering improvements for boundary spots in Figure 1 likely result from enhanced representation across all spots, as non-boundary spots also show significant improvement. Besides, aligning representations across graph augmentations doesn’t inherently enable access to information beyond local neighborhoods.
- In the methodology, several alignment loss functions are proposed, but there appears to be redundancy. For example, both L_{sc} (Equ.(1)) and L_{pcl} aim to maximize the representation similarity between two augmentations. Additionally, as shown in Figure (7), removing L_{recon} and L_{pcl} doesn’t actually impact the performance, raising the question of whether so many loss functions are necessary.
- Several experimental details are missing, including the type of graph augmentation used, the specific hyperparameters, and the tuning strategy applied.
- The explanation of Section 4.4 can be improved. The “A” is first introduced in Section 3, but it is reintroduced with a different explanation in Line 287, leading to potential confusion.

### Questions
Downstream tasks are mainly about the clustering alignment. Could the author evaluate the model on some other clinical downstream tasks?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces Spotscape, a framework designed to enhance the analysis of spatially resolved transcriptomics (SRT) data. Traditional graph-based deep learning methods in SRT have limitations in representing spots near the boundaries of cell type clusters, as they tend to focus mainly on spatially close spots with similar features. Spotscape addresses this by introducing a Similarity Telescope module, which captures global relationships among multiple spots to improve representation. Moreover, to handle the integration of multiple slices from diverse sources, the framework incorporates a similarity scaling strategy that maintains consistent distances between intra- and inter-slice spots. Experiments show that Spotscape outperforms existing methods in tasks such as spatial domain identification, multi-slice integration, and alignment.

### Strengths
1. It is quite impressive that Spotscape can handle both single-slice and multi-slice tasks, from spatial domain detection to alignment of mouse embryogenesis.
2. The experimental results show that Spotscape delivers performance boost compared to the baselines in different tasks.
3. The ablation study showcases the effects of each type of loss in different tasks, helping the readers to better understand the design of Spotscape.

### Weaknesses
1. The provided information is not enough to reproduce the experiments. For example, what kind of message passing layer is used in the GNN encoder? How many GNN layers? What are the dimensions of the layers? What are the choices for hyperparameters?
2. The proposed Spotscape looks more complicated than the baselines. I wonder if is Spotscape more resource-consuming in terms of spatial and computation complexity.
3. (minor) There are some typos in the manuscript. For example, the title of Table 2.

### Questions
1. I appreciate the authors for providing the data visualizations based on spatial coordinates. Notice that Spotscape emphasizes a lot on feature similarities, which I suppose is the key to performance improvement. It would be great to have some additional figures on the similarities regarding expression profiles. For example, a UMAP plot for the MTG data shows that the same cell types in control and AD group share similar gene expression.
2. It is great that the authors showcase some interesting alignment results with mouse embryo slices and cross-technology alignment. For the mouse embryo slices, a more general baseline is (unbalanced) optimal transport, which typically performs pretty good in temporal alignment. The results for Xenium and Visium alignment are not quite persuasive, since only a very small part of the slice is used for evaluation.

### Soundness
3

### Presentation
3

### Contribution
3
