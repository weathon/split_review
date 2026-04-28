# CellPainTR: Contrastive Batch Corrected Transformer for Large Scale Cell Painting

- Decision: Reject
- Avg Score: 6.00
- Scores: 6, 5, 8, 5

## Abstract
Cell Painting, a high-content imaging-based profiling method, has emerged as a powerful tool for understanding cellular phenotypes and drug responses. However, batch effects severely constrain the integration and interpretation of data collected across different laboratories and experimental conditions. This paper introduces CellPainTR, a novel approach for unified batch correction and representation learning in Cell Painting data, addressing a critical challenge in the field of image-based profiling. Our approach employs a Transformer-like architecture with Hyena operators, positional encoding via morphological-feature-embedding, and a special source context token for batch correction,
combined with a multi-stage training process that incorporates masked token prediction and supervised contrastive learning. Experiments on the JUMP Cell Painting dataset demonstrate that CellPainTR significantly outperforms existing approaches such as Combat and Harmony across multiple evaluation metrics,while maintaining strong biological information retention as evidenced by improved clustering metrics and qualitative PCA visualizations. Moreover, our method effectively reduces the feature space from thousands of dimensions to just 256, addressing the curse of dimensionality while maintaining high performance. These advancements enable more robust integration of multi-source Cell Painting data, potentially accelerating progress in drug discovery and cellular biology research.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
A paper entitled “CELLPAINTR: CONTRASTIVE BATCH CORRECTION TRANSFORMER FOR LARGE SCALE CELL PAINTING” proposes a novel Hyena—transformer-based deep learning approach to analyse cultured cell images obtained in fluorescence high-content screening (HCS) microscopy in fluorescence staining protocol called Cell Painting. This approach involves staining (or "painting") different cellular components with fluorescent dyes, capturing detailed images of each cell, and using image analysis to extract quantitative data on various cellular features. For this, authors utilise JUMP Cell Painting dataset - a large dataset of small molecule and CRISPR perturbation-based HCS images. Notably, authors work not on images directly but on features engineered from the images using CellProfiler as a rule-based feature extractor.

### Strengths
- The paper proposes a novel architecture, suggesting it is capable of batch correction and self-supervised training

### Weaknesses
 - Authors use terminology like “biological variation”, “biological metrics” and “biological relevance” without actually explaining what they mean. I am not aware of Biology per se being a measurable quantity. Is “biological” e.g. a cell cycle effect, or a missed well while pipetting? If the authors do mean mechanistic interactions of biomolecules - this should be clarified.
- ICLR is focusing on representation learning, yet authors chose to use engineered features, rather than training the architecture end-to-end from the images. Please explain why that was not possible or viable in this case.
- I find the batch effect correction section (4.2) is presented in a very convoluted way. Images in high-content screening contain all sorts of batch effects - MTP evaporation aka “bathtub effects”, liquid handling mistakes, reagents batch issues, assay errors, imaging errors. It is not clear what is being corrected here. If everything all at once, then why is it “biological”?
- The legend of Tab 1 doesn’t clarify the mAP of what exactly was measured or what exactly the task was or the dataset was used. One cannot just say “biological relevance”, without actually explaining what that means. In the text referring to this table, authors should give examples and explain why this metric is good. I understand the limitations of the ICLR format, but these details are essential.
- CellProfiler is a well-known image analysis suite for the HTC microscopy combining rule-based and ML algorithms. It is however not SOTA in 2024. I would recommend the authors compare their results to CellPose.
- The authors claim interpretability as a key advantage of using engineered features, but do not provide any concrete examples. Many CellProfiler features, such as Zernike moments and texture features, are not directly interpretable in a biological context. The authors should demonstrate how specific changes in these features relate to observable biological phenomena, for example, by linking changes in a specific feature to a known drug mechanism of action. Despite using a high capacity head for these features, the performance on batch effect correction is marginal, raising questions about the utility of the approach.

### Questions
- I find the batch effect correction section (4.2) is presented in a very convoluted way. Images in high-content screening contain all sorts of batch effects - MTP evaporation aka “bathtub effects”, liquid handling mistakes, reagents batch issues, assay errors, imaging errors. It is not clear what is being corrected here. If everything all at once, then why is it “biological”?
- The legend of Tab 1 doesn’t clarify the mAP of what exactly was measured or what exactly the task was or the dataset was used. One cannot just say “biological relevance”, without actually explaining what that means. In the text referring to this table, authors should give examples and explain why this metric is good. I understand the limitations of the ICLR format, but these details are essential.
- CellProfiler is a well-known image analysis suite for the HTC microscopy combining rule-based and ML algorithms. It is however not SOTA in 2024. I would recommend the authors compare their results to CellPose.

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
5

### Summary
The authors address the challenge of batch correction in large-scale image-based phenotypic screening experiments for drug discovery.  Specifically, they develop the CellPainTR model, which takes in engineered features from the popular CellProfiler software, and learns to embed them in a low dimensional space, with the goal of removing batch effects and preserving biological information.  The authors demonstrate their method on the JUMP-CP dataset, a multi-site Cell Painting dataset, collected across 12 partnering sites (eg, different academic institutions and Pharma companies), that is known to have extremely strong batch effects.  For example, different sites in JUMP-CP used different combinations of microscopes (confocal vs. widefield), filter sets, and biological batches of cells.

The CellpainTR model consists of a Transformer architecture with Hyena operators.  The authors include a learned positional encoding, and a source context token that learns to embed each of the multiple sites for batch correction.  Finally, the model is trained in a multi-stage process, starting from self-supervised masked token prediction, followed by supervised contrastive learning, first at the single-source level and then at the multi-source level.

Batch correction is a highly studied problem in image-based phenotypic screening. The authors compare CellpainTR against two popular batch correction methods, Combat and Harmony, that were developed and popularized by the single cell RNA sequencing community.  They also provide an ablation study of the role of multi-stage training.

* Note: I use the term source and site interchangeably to denote a single data generating center.

### Strengths
The proposed method addresses an important challenge in image-based phenotypic screening.  Notably, improvements in batch correction would have broad implications, and could greatly improve the process of drug discovery.

The authors leverage an ideal dataset for testing batch correction methods: JUMP-CP.  The JUMP-CP dataset is an important and very challenging test case, due to the multi-site data collection, and strong batch effects that have been observed.

The proposed CellPainTR method uses state-of-the-art architectures, including Hyena operators, which to my knowledge have not been tested in the setting of batch correction for Cell Painting features.

The authors conduct extensive evaluations shown in Table 1, including strong baseline methods (Combat, Harmony, Sphering), and numerous evaluation metrics measuring both residual batch effects and retention of biological information in the embeddings.

Overall, they see marginal improvements of CellPainTR over existing batch correction methods.

### Weaknesses
The authors claim three novel aspects of their batch-correction transformer architecture: (1) Hyena operators, (2) learned positioning encoding, and (3) a source context token for batch correction.  There are currently two limitations with this claim:

1) The idea to include a source context token in a transformer architecture to reduce batch effect, while a very good idea, has already been published.  See https://arxiv.org/pdf/2305.19402 and ICML SCIS 2023 workshop.

2) The authors don't perform an ablation study to demonstrate the impact of each of the above design choices.  In particular, I have not yet seen a study evaluating the use of Hyena operators in a batch correction transformer applied to Cell Profiler features.  In my opinion, including this result in the paper would increase its contribution.


Given that the problem of batch correction has been thoroughly studied in both the field of single-cell RNA sequencing and image-based profiling, a key measure of the paper's contribution is the performance comparison in Table 1.  However, I found the description of these performance metrics was very short, and in some cases missing altogether, making it difficult to understand the performance of the proposed model.  One thing that would strengthen the paper is to greatly expand the description of the evaluation metrics in section 4.2 Quantitative Evaluation Results.  

Here are a list of questions relating to Table 1:

1) The authors introduce a new Batch Correction metric, with the following description: "We also introduce a Batch Correction metric, calculated as 1 - f1 score, where f1 represents the detectability of batch effects."  This requires additional explanation.  For example, how is the detectability of batch effects measured?  Is this a K-Nearest-Neighbors model on batch ID?  Or is a supervised model trained to predict batch ID?  Alternatively, kBET (https://www.nature.com/articles/s41592-018-0254-1) is an established batch correction metric that seems highly related, and could be used for this purpose.

2) Batch Correction and Biological Metrics are provided both with and without controls.  How are the controls used in these metrics?  Does this refer to the use of negative controls in the preprocessing by Median Absolute Deviation normalization, using the negative control of each plate as the baseline (page 7)?

3) What does "no rep" refer to in the metric: mAP (no rep)?  Does this refer to "without controls", in which case it may be a typo?

4) How are the Bio Info scores calculated?  I don't see a description of this metric in the main text or appendix.

5) How are the Aggregate Scores (Batch Correction, Bio Metrics, and Overall Score) calculated?  I didn't find this explained in the main text or appendix.

6) The improvement of Overall Score between CellPainTR and the Baseline is quite small (0.63 to 0.64).  I suggest including measures of statistical significance.

I suggest including a description of each metric in the Appendix, and referencing it from the main text.

The paper explains that the masking ratio for each training batch is chosen from a range of [0.05, 0.4], applied uniformly across all five channels in the Cell Painting data.  It is known that many Cell Profiler features are highly correlated, such as features arising from the same filter with different parameter settings.  It would be informative if the authors could provide additional information regarding the choice of masking ratio, and whether it benefits from first removing very highly correlated features.

It wasn't clear to me what the colors of each feature refer to in Figure 3.  For example, in Figure 3a the first (input) Cell Profiler feature is blue with pink lines, and the first feature in the learned Channel Wise Masked Morphology embedding is blue with pink lines that are rotated 90 degrees.  Does this imply that the learned features correspond to the same channel?  If the color scheme encodes information relative to the algorithm design, it should be described in a legend or figure caption.

The UMAP in Figure 4 is difficult to interpret.  In particular, there are no legends describing the color scheme.  In the case of coloring by Compound, there will certainly be too many different compounds to color uniquely.  I suggest including an embedding (PCA, tSNE or UMAP) showing coloring at the MOA level, to demonstrate if compounds with the same MOA tend to cluster together.  This may require subsetting to a small number of compounds and MOAs.


Formatting issues:

1) Missing "space" in intro to section 3.2 Training

2) "vari- ation" in section 4.1 Qualitative Evaluation Results

3) Comma instead of decimal point in Table 1 (Sphering, Sil. batch)

### Questions
It was unclear to me how the InChIKey is used in the supervised contrastive objective (Equation 8).  Is it true that positive samples are chosen from technical replicates that received the same compound treatment (ie, same InChIKey)?  If so, I suggest making this statement more explicit in the text.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces CellPaintTR, a novel transformer-based model designed to enhance the analysis of cellular image data by encoding CellProfiler features into a reduced-dimensionality space while minimizing batch effects. This method is particularly relevant for large-scale cellular datasets, where high-dimensional data and batch variability can hinder downstream analysis.

To validate the model's effectiveness, the authors conduct extensive experiments on the JUMP-CP dataset, a large and diverse collection of cellular images commonly used for benchmarking in this field. 

A key technical advancement of CellPaintTR lies in its architecture, particularly its innovative use of the Hyena operator and a specialized source token within the transformer framework.

### Strengths
The research presented addresses a critical challenge in the field of computational biology and bioinformatics: the effective encoding and analysis of high-dimensional cellular image data while controlling for batch effects. 

The results presented are thorough and compelling, illustrating the method's strong performance across various metrics and experimental conditions. The authors carefully validate CellPaintTR on the well-regarded JUMP-CP dataset, showing its capacity to generalize across different cellular contexts and experimental setups.

From an architectural and methodological standpoint, the approach is highly novel. CellPaintTR leverages a unique combination of architectural choices, including the Hyena operator and a tailored source token mechanism within the transformer model. Additionally, the training strategy is specifically designed to optimize performance.

An added strength of this work is its commitment to open science. The authors have made their code publicly available, allowing other researchers to reproduce and build upon their findings. Moreover, by using public databases such as JUMP-CP, the authors ensure that their results are accessible and verifiable.

### Weaknesses
Firstly, while the results are promising, a more comprehensive benchmarking discussion would strengthen the work’s impact and contextualize its contributions within the existing literature. In particular, I recommend that the authors provide a thorough comparison of their batch correction method within a protocol outlined in [1]. Furthermore, it would be beneficial to explore how the model would handle data from a novel source not seen during the initial training process. For example, how resilient is the CellPaintTR architecture to batch effects that may emerge from new experimental or imaging conditions? Specifically, the authors should consider evaluating their method on a dataset with different imaging modalities, staining protocols, and cell types, to rigorously assess its generalizability. The lack of such an evaluation limits the conclusions that can be drawn about the method's robustness in real-world scenarios.

In terms of presentation, the paper could benefit from a clearer and more intuitive description of certain technical aspects, particularly for readers less familiar with transformer models or batch correction techniques. Figure 2, for instance, could be refined to include a visualization of the Hyena operator, which is a key component of the model architecture. Adding a clear, visual representation of the Hyena operator’s role and function, including its specific mathematical operations and how it differs from standard attention mechanisms, would greatly aid readers in understanding the intuition and value behind this design choice. Additionally, enhancing the color scheme and increasing the font sizes across all figures would improve their readability and make the data more accessible. Minor typos, such as updating "bidrectional" to "bidirectional" in Fig. 2,  would also enhance the overall polish of the paper.

To further improve readability and organization, I recommend restructuring the experimental sections by dividing them into two distinct parts: one dedicated to the experimental setup and the other to results and discussion. Clearly separating these sections would make it easier for readers to follow the methodology and interpret the findings. This separation should include detailed descriptions of the specific experimental conditions, including the number of replicates, the specific cell lines used, and any other relevant parameters that could affect the results. The results section should then focus on the quantitative outcomes and their statistical significance, followed by a discussion of the implications of these results.

### Questions
Could the authors provide a more comprehensive benchmarking discussion comparing their batch correction method in a setup described in [1]?

How would CellPaintTR handle data from a new source that was not present in the training dataset? Could the authors discuss the model's robustness and adaptability to previously unseen batches?

In Figure 2, could the authors include a visualization of the Hyena operator to clarify its role and function within the model architecture?

Would the authors consider enhancing the color scheme and increasing font sizes in all figures to improve readability?

Could minor typographical errors, such as "bidrectional" instead of "bidirectional," be corrected to improve the overall presentation?

To improve organization, would the authors consider separating the experimental section into two distinct parts: one for experimental setup and another for results and discussion?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors present CellPainTR, an approach designed to address batch effects in CellProfiler features from Cell Painting data. CellPainTR performs batch correction and representation learning simultaneously while maintaining biologically relevant information. The model is trained progressively, starting with channel-wise masked morphology and followed by intra-source and inter-source supervised learning. Qualitative and quantitative results show that CellPainTR outperforms other batch correction techniques on various metrics.

### Strengths
1. Innovative Approach: 

The introduction of CellPainTR provides a novel approach to unified batch correction and representation learning specifically designed for CellProfiler data from Cell Painting images, addressing batch effect challenges. This focus is innovative and well-suited for high-dimensional biological data, which has traditionally struggled with batch effects.

### Weaknesses
1. There is no discussion of the related work:

   - Given that the main contribution is a method for batch correction in biological data, there are several works that need to be discussed, including but not limited to [1, 2].

2. The methods section (Section 3) is minimal, with a lack of equations for the key components of CellPainTR.

   - More information is needed for the "linear adapter," "feature context embedding," and "source context token."

3. CellPainTR was only evaluated on CellProfiler features:

   - This is insufficient. Why were no other feature extraction methods evaluated? For example, those presented in [3].

4. Computationally inefficient:

   - The pretraining took two weeks to train three epochs. How would it affect the performance if this pretraining was not done? Am I correct in saying that this ablation study was not part of CellPainTR(1) or CellPainTR(2)?
   - This process is extremely inefficient, taking approximately five weeks to train.

5. Subjective qualitative evaluations:

   - Figure 4 is subjective and does not demonstrate a “clear separation of compounds” for the final model in the Compound row. One might argue the opposite.

6. Final model performance gain over intermediate models is minimal:

   - Overall, the final model is not better than the intermediate models. Therefore, there is no reason to train in the final stage, which takes an extra week. 

7. The metrics are not sufficiently explained:

- mAP is explained in the Appendix, however there should be something in the main.

Minor:

   - The authors appear to be confused by Cell Painting and Cell Profiler features. Cell Painting is the imaging technique, and CellProfiler is the tool that obtains morphological features from images. Therefore, “Cell Painting features” should be replaced with CellProfiler features.
   - Cite transformer and Hyena in the introduction in line 52.
   - Cite combat and harmony in lines 92-93.
   - Cite: “The challenge of batch effects in high-dimensional biological data, particularly in the field of image-based profiling like CellPainting, has been a significant focus of research in recent years.”
   - Cite: “Several algorithms have been developed to address batch effects in biological data.”
   - Citations out of place:  
     - The Cell painting dataset is cited in the sentence in line 221-222:
     - “This method allows us to provide the CellPainTR model with explicit feature context information (Wayetal.,2021).” The cell painting dataset is also cited in line 228, which is out of place.
     - Hinton et al. 2006 cited after “while still capturing biologically meaningful information.” in line 327.
     - Goodfellow et al. 2016 is out of place in line 373.
- Since the value of $\lambda$ in equation 7 is always set to 1, this is redundant unless there is an ablation when changing this value.
- Nyffler et al. 2020 does not exist. If I am missing it, could the authors please point to this paper?

### Questions
- What is a “Linear Adapter?”
- Am I correct that training the model for 3 epochs took two weeks? This raises questions about the usefulness and scalability of the method.
- What is Biological Information, and how is it calculated?
- The Silhouette batch score “measures the degree of separation between batches.” Am I correct in assuming that a lower value means that the batches are not separable which is better for batch correction? If so, why is the highest value highlighted in the table? Overall, these metrics need to be explained in more detail including whether higher or lower is better and how they are calculated.
- What methods did the authors use to analyse downstream prediction tasks? This needs to be explained further.

### Soundness
2

### Presentation
3

### Contribution
2
