# GeST: Towards Building A Generative Pretrained Transformer for Learning Cellular Spatial Context

- Decision: Reject
- Avg Score: 4.33
- Scores: 5, 5, 3

## Abstract
Learning the spatial context of cells through pre-training may enable us to systematically decipher tissue organization and cellular interactions in multicellular organisms. Yet, existing models often focus on individual cells, neglecting the intricate spatial dynamics between them. We develop GeST, a deep generative transformer model that is pre-trained on the task of using information from neighboring cells to iteratively generate cellular profiles in spatial contexts. In GeST, we propose a novel serialization strategy to convert spatial data into sequences, a robust cell quantization method to tokenize continuous gene expression profiles, and a specialized attention mechanism in the transformer to enable efficient training. We pre-trained GeST on a large-scale spatial transcriptomics dataset from the mouse brain and demonstrated its performance in unseen cell generation. Our results also show that the pre-trained model can extract spatial niche embeddings in a zero-shot way and can be further fine-tuned for spatial annotation tasks. Furthermore, GeST can simulate gene expression changes in response to spatial perturbations, closely matching experimental results. Overall, GeST offers a powerful framework for generative pre-training on spatial transcriptomics.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The authors present a generative pre-trained transformer model designed for spatial transcriptomics. The authors propose strategies to tackle common challenges in applying transformer models to ST data, including a serialization strategy, cell quantization method, and spatial attention mechanism.

### Strengths
- The authors adopted a clever strategy to tokenize continuous gene expression profiles into discrete cell states. In particular, this helps mitigate error accumulation in autoregressive generation, a common issue when dealing with continuous data in transformer models.

- The model demonstrates strong performance across multiple tasks, including unseen cell generation, niche clustering/annotation, and in-silico spatial perturbation analysis. This versatility showcases the model's potential as a foundation for various spatial transcriptomics applications.

### Weaknesses
 - The cell quantization strategy presented in the paper is not significantly different from previous strategies employed by existing methods for ST. For example, this problem of discretizing spatial data is addressed before by [1] Wen et al., [2] Yarlagadda et al, [3] Schaar et al.

- The evaluation is focused mainly on mouse brain datasets - which are known to have organized spatial structures of various distinct cell types. Evaluating model on more challenging datasets like from cancerous tissues will help solidify the work.  While spatial serialization introduces an ordinal structure, its application might overlook the full potential of irregular spatial patterns within tissues, limiting the model’s adaptability across different spatial configurations.

- The multi-level cell quantization and hierarchical loss approach are suited for well preserved mouse brain tissues. But in practice, ST data have several artifacts due to poorly preserved tissues and not very clean - transformer models for ST tend to perform relatively poorly compared to their CNN counterparts for modeling hierarchical information in the tissues.
 
- The reliance on a vocabulary to tokenize gene expression may lead to loss of subtle gene-level variations, potentially limiting the granularity of predictions, especially for rare cell subtypes.

- The model’s design does not fully account for dynamic gene-gene interactions within perturbed cells during in-silico simulations, which could lead to oversimplified, and often incorrect, biological interpretations.

-  The Spatial Attention mechanism is computationally expensive, and not optimized for long-range dependencies in large tissue sections, which may lead to biased local predictions without sufficient contextual global information. The pre-training is computationally intense and require multiple GPUs - and the authors should report how the model generalizes to non-brain tissues without sufficient available ST data.

- Authors use RMSE and Spearman correlation for evaluation, but lacks biologically relevant validation metrics, such as alignment with known cell types or tissue architectures.

- While the authors mention error accumulation in autoregressive generation, they don't provide a detailed analysis of how this affects long-range predictions or the model's stability over multiple generation steps.

### Questions
- What is the impact of tissue preparation methods and batch effects on GEST's performance? 

How does the model,
- handle rare cell types or spatially isolated cells that may not have sufficient neighboring context? 
- perform across different tissue types beyond the mouse brain?
- compare to graph-based approaches for ST data, such as spaGCN?

### Soundness
3

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
I'm initially rating this paper as "5: marginally below the acceptance threshold".

Summary: the paper proposes an auto-regressive generative model for spatial transcriptomic data. A notion of "order" is introduced thereby making use of (modified version of) pipelines for sequences with incremental updates. The method is evaluate on niche clustering, niche label annotation, unseen cell generation, and spatial perturbation prediction. To facilitate the generation of the final counts, a hierarchical clustering and meta-cell vocabulary is used.

### Strengths
- Clear writing and explanatory figures
-

### Weaknesses
 - typo (not included in score): In line 236 the sentence shouldn't spot at "$g(x)$. Instead ..."

 - My main question/concern is that there is no inherent order in cells located in spatial positions (as mentioned in the paper). Lines 150-160 explain a procedure to assign a "pseudo-order" to cells. This procedure contains cropping a square from the spatial data, selecting one of the anchors, and repeatedly selecting cells based on their spatial distance to the selected anchor. At least I do not intuitively understand why such a procedure should resemble "an order"?
- For evaluating the generative power of the model, in Figure. 4 metrics like RMSE and correlation are used. Was there a reason for not using the commonly used metrics for this purpose, like Wasserstein distance, MMD, EMD, etc?

### Questions
- My main question/concern is that there is no inherent order in cells located in spatial positions (as mentioned in the paper). Lines 150-160 explain a procedure to assign a "pseudo-order" to cells. This procedure contains cropping a square from the spatial data, selecting one of the anchors, and repeatedly selecting cells based on their spatial distance to the selected anchor. At least I do not intuitively understand why such a procedure should resemble "an order"?
- For evaluating the generative power of the model, in Figure. 4 metrics like RMSE and correlation are used. Was there a reason for not using the commonly used metrics for this purpose, like Wasserstein distance, MMD, EMD, etc?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors introduce an innovative generative pre-trained model (GeST) designed to learn the spatial context of cells within spatial transcriptomics. This model ingeniously converts two-dimensional spatial data into a serialized one-dimensional sequence to accurately capture and model the intricate spatial relationships between cells. This novel approach facilitates a deeper understanding of complex tissue organizations and provides a promising direction for further research in the field. Preliminary results demonstrate the model’s effectiveness in capturing relevant spatial patterns, although further validation is required to assess its performance across diverse datasets and potential limitations in handling varying spatial resolutions.

### Strengths
The authors creatively employ a generative pre-trained transformer for the first time to understand spatial transcriptomics at the single-cell level, introducing innovative methods to the field.

### Weaknesses
1. The introduction could be enhanced by comparing the proposed GeST model with other relevant models like GraphGT or SpaGCN, as CellPLM, which is mentioned, differs significantly in context and isn’t directly related to spatial transcriptomics.
2. The model appears to primarily apply the Vision Transformer architecture to spatial transcriptomics with minimal modifications, suggesting a lack of substantial innovation. The core mechanism of the model, which involves converting spatial data into a 1D sequence, is not novel, and the positional encoding strategy, while necessary, does not represent a significant advancement over existing methods in the transformer literature. The modifications to the attention mechanism also need further clarification to demonstrate their novelty and necessity.
3. The resolution variance among different spatial transcriptomics technologies should be more thoroughly addressed, potentially by incorporating datasets from Stereo-seq, Slide-seq v2, STARmap, and 10x Visium to provide a broader validation of the model’s utility. However, it is important to note that the resolution of 10x Visium is based on spots rather than individual cells. Does the model still perform effectively under these conditions? The model's performance at different resolutions, particularly at subcellular levels, is not sufficiently explored, and the impact of varying spot sizes on the model's ability to capture spatial context needs to be investigated.
4. In the ablation studies detailed in Table 3, it is unclear whether changes in the number of layers and heads simultaneously affect the window size. Clarification on how these architectural modifications impact the model’s spatial resolution would be valuable. Specifically, it is unclear if the window size is fixed or if it adapts to changes in the number of layers and heads. The relationship between these hyperparameters and the effective receptive field of the model is not well-defined.
5. Consider the possibility of conducting an ablation study where the neighborhood  information is removed, to assess its impact on the model’s performance and spatial understanding. This would help to quantify the contribution of spatial information to the model's predictive power, and to assess whether the model is truly learning spatial relationships or simply relying on gene expression patterns.

### Questions
1. It is advisable to try data from multiple resolutions, as different technologies offer varying levels of resolution. For example, Stereo-seq can achieve subcellular resolution, which may allow the algorithm to examine the impact of organelles on the structure.
2. When conducting biological experiments involving tissue sections, these sections are often assembled from multiple pieces. This assembly process can introduce inaccuracies that may impact the reliability of neighborhood information. How should this issue be addressed to ensure data integrity?
3. As the authors mentioned, the model is expected to perform well in predicting genes with high spatial variation. It would be beneficial to validate this conclusion using cancer datasets, which are characterized by high variability. Additionally, considering cancer datasets could be crucial for addressing key questions about the tumor microenvironment.

### Soundness
2

### Presentation
2

### Contribution
2
