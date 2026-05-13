# Diffusion Generative Modeling for Spatially Resolved Gene Expression Inference from Histology Images

- Decision: Accept
- Scores: 8, 6, 6

## Abstract
Spatial Transcriptomics (ST) allows a high-resolution measurement of RNA sequence abundance by systematically connecting cell morphology depicted in Hematoxylin and eosin (H\&E) stained histology images to spatially resolved gene expressions. ST is a time-consuming, expensive yet powerful experimental technique that provides new opportunities to understand cancer mechanisms at a fine-grained molecular level, which is critical for uncovering new approaches for disease diagnosis and treatments. Here, we present $\textbf{Stem}$ ($\underline{\textbf{S}}$pa$\underline{\textbf{T}}$ially resolved gene $\underline{\textbf{E}}$xpression inference with diffusion $\underline{\textbf{M}}$odel), a novel computational tool that leverages a conditional diffusion generative model to enable in silico gene expression inference from H&E stained images. Through better capturing the inherent stochasticity and heterogeneity in ST data, $\textbf{Stem}$ achieves state-of-the-art performance on spatial gene expression prediction and generates biologically meaningful gene profiles for new H&E stained images at test time. We evaluate the proposed algorithm on datasets with various tissue sources and sequencing platforms, where it demonstrates clear improvement over existing approaches. $\textbf{Stem}$ generates high-fidelity gene expression predictions that share similar gene variation levels as ground truth data, suggesting that our method preserves the underlying biological heterogeneity. Our proposed pipeline opens up the possibility of analyzing existing, easily accessible H&E stained histology images from a genomics point of view without physically performing gene expression profiling and empowers potential biological discovery from H&E stained histology images.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose STEM, which is a conditional diffusion generative model-based ST prediction framework. On two public datasets, the authors show that STEM outperforms the state-of-the-art ST prediction methods. The authors also show through a series of ablation experiments what factors are contributing to good performance of their model.

### Strengths
I think STEM adds a valid contribution to a large suite of ST-prediction methods, which are predominantly regression-based approaches (except for BLEEP, which relies on the embedding neighborhood in the training set). The application of generative model is novel, the strength of which is clearly shown in the great performance. I also appreciate that the authors invested efforts into several ablation study factors and carefully designed the experiments to mitigate potential bias (which I don't think BLEEP did well at all). Assuming that the codebase is provided, I think this can be integrated into pratictioner's toolbox.

### Weaknesses
I think there are several weaknesses that the authors can address to make it an even better contribution to the field.

- For reproducibility, the authors NEED to be more specific about hyperparameters used in STEM - I don't think any information was provided.
- This is a generative model, meaning multiple gene predictions are generated from the given histology image. While the authors say that these are averaged to yield the final expression, I would like to see an ablation or example of what each sample looks like and how they would affect all the performance metrics that we observe.
- While not required, I would like to see the authors also try with different histopatholgy foundation models, such as Virchow or H-Optimus, just for robustness
- I am slightly confused as to why TRIPLEX performance is really low. In their CVPR 2024 paper, they show that TRIPLEX outperforms HisToGene and BLEEP significantly. But it is really bad. Have authors used their model properly?
- To really show that it is indeed the *conditional generative model* part of STEM contributing to the increase PCC performance, the authors need to be careful in comparing to other SOTA baselines. BLEEP uses ResNet50, TRIPLEX uses Resnet18, whereas STEM uses UNI or CONCH. Could the difference simply be coming from difference in patch encoders?
- The authors (in line 78~80) argue that even same cell type might be in different cell types of differ in spatial locations causing different gene expression outcomes and that previous models cannot 'capture them. However, I am not sure if STEM can also address this shortcoming of the previous models, since it is also simply using patch encoder (albeit a powerful one) to summarize the image patch.
- When encoding gene count, the input is a scalar, passed through MLP? The authors need to elaborate more on what this MLP structure is, since it is confusing.
- In encoder ablation study, what does CONCH+UNI mean? Simple concatenation of both features?

### Questions
See weakness

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
3

### Summary
**Motivation:** Infer spatial resolved gene expression only from histology images
**Technical contribution:** A diffusion model based approach is proposed to predict spatial gene expression from histology images
**Strengths:** The paper is clearly written and the results support the story. The method is easy to understand and effective.
**Weakness:** The novelty of proposed method (clever application vs. novel technical contribution) is not very clear. Analysis can be expanded to more datasets.  

**Justification of score:** Overall, the paper proposes a simple and effective method, which is above acceptance threshold. I would be happy to revise my score pending clarifications on my questions from the authors.

### Strengths
**Clear grounding of literature:** The introduction and related works sections are comprehensive and ground the problem well. In addition to working on better predicting gene expression, the authors also highlight problems with current simplistic evaluation framework based on Pearson correlation. They also propose new measures of correctness. Overall, the paper is clearly written.

**Comparison with recent baselines:** The authors benchmarked their model against recent baselines, such as BLEEP.

### Weaknesses
 **Additional evaluation**
While the authors do demonstrate their method on two datasets and organs, there is a large amount of spatial transcriptomics data available publicly. I encourage the authors to try it out and see if their method works equally well for different organs, cancer vs. non-cancer, and/ or different species. Specifically, the performance of the method should be evaluated on more complex datasets with higher levels of heterogeneity and more diverse tissue structures. The current datasets may not fully capture the challenges of real-world spatial transcriptomics data, which often includes significant variations in cell types and tissue architecture.

**Using pre-trained encoders for gene expression**
The authors seem to train from scratch their gene value encoder. Can they comment on why do they do this when numerous gene expression encoder foundation models are available, such as scGPT? While these encoders have been trained on single cell data, they have shown promising results for bulk expression, hence showing their versatility. It is unclear why the authors did not explore the use of these readily available pre-trained models, which could potentially improve performance and reduce training time. The decision to train from scratch needs further justification, especially given the potential benefits of transfer learning from existing models.

**Limited novelty**
The proposed method seems like a clever application of conditional diffusion models to the problem. Can the authors further comment on the novelty of their method and how is it different compared to the existing literature? The paper needs to clearly articulate the specific technical contributions beyond a straightforward application of existing techniques. The novelty should be more clearly defined in terms of the specific modifications or innovations made to the diffusion model framework to address the spatial transcriptomics problem.

### Questions
- Was any batch correction applied to the spatial transcriptomics data?
- Since many metrics are presented in the table, it might be easier to interpret them if authors have conventional up and down arrows next to the metric name.
- What was the rationale behind trying only UNI and CONCH, when larger models exist, such as Virchow [1]?

---
References
[1] Vorontsov, Eugene, et al. "A foundation model for clinical-grade computational pathology and rare cancers detection." Nature medicine (2024): 1-12.

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
5

### Summary
The authors proposed a novel computational tool that leverages a conditional diffusion generative model to enable in silico gene expression inference from H&E stained images. This tool can capture better heterogeneity and stochasticity of ST data and achieve SOTA on the gene expression prediction across various datasets with different metrics.

### Strengths
The authors considered a limitation I fully agreed with: gene expression cannot be gained from cellular morphology only. To solve this, proposed model learns a conditional distribution over the potentially associated gene expression profiles given the histology images, facilitating a one-to-many correspondence between the image and ST data.

### Weaknesses
I think the model should be tested with larger gene panel (maybe thousands of genes) to evaluate the performance limits compared with other methods. I also want to see the evaluation other than the datasets with super-resolution spots (for example, how about the performance under Slide-seq? Stereo-seq? or Even in situ technologies?). Does the image patch size change to match the size of the spots?

For Figure 3, it is not enough to choose one sample with two marker gene. I would like to see more visualization results with more marker genes across different cell types. More importantly, compare these visualization results with existing methods. I would like to see the difference about cell type identification.

Since the authors used a transformed version of original histology images, I want to know how they transformed images.

How many genes did authors used for calculating MSE and MAE?

### Questions
1. I suggest testing the model with a larger gene panel (>1000) and compare with other methods.
2. I suggest testing on datasets generated by other platforms (Slide-seq, Stereo-seq, or in situ technologies).
3. For Figure 3, it is not enough to choose one sample with two marker gene. I would like to see more visualization results with more marker genes across different cell types. More importantly, compare these visualization results with existing methods. I would like to see the difference about cell type identification.
4. Since the authors used a transformed version of original histology images, I want to know how they transformed images.
5. How many genes did authors used for calculating MSE and MAE?

### Soundness
3

### Presentation
4

### Contribution
3
