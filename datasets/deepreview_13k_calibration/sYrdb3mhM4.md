# Predicting Spatial Transcriptomics from Histology Images via Biologically Informed Flow Matching

- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 6, 5

## Abstract
Spatial transcriptomics (ST) has emerged as a promising technology to bridge the gap between histology imaging and gene expression profiling. However, its application to medical diagnosis is limited due to its low throughput and the need for specialized experimental facilities. To address this issue, we develop STFlow, a flow-based generative model to predict spatial transcriptomics from whole-slide histology images. STFlow is trained with a biologically-informed flow matching algorithm that iteratively refines predicted gene expression values, where we choose zero-inflated negative binomial distribution as a prior distribution to incorporate the inductive bias of gene expression data. Compared to previous methods that predict the gene expression of each spot independently, STFlow models the interaction of genes across different spots to account for potential gene regulatory effects. On a recently curated HEST-1k benchmark, we demonstrate STFlow substantially outperforms all baselines including pathology foundation models, with over 18% relative improvement over current state-of-the-art.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors presented STFlow to predict ST from histology images. STFlow uses a flow matching algorithm to predict gene expression values, and achieves a performance boost over baselines on the HEST benchmark

### Strengths
- Predicting spatial transcriptomics using histology data is a relevant and important problem and has a large impact on the future of computational pathology and bioinformatics research.
- The author’s approaches uses state-of-the-art ML approaches, and seems to achieves performance boost over some baselines provided.

### Weaknesses
 - Author’s approach assembles many prior off-the-shelf methods for ST prediction, including a two-stage approach for histology, tile-level foundation models, and flow matching. Notably, the approach uses a frozen patch encoder, that does most of the heavy lifting in the representation learning, leaving it frozen inhibits the model’s ability to learn.
- The model performance boost is not substantial, and are often within error bar of the much simpler baselines. The comparison of the proposed method doesn’t have the proper slide-based baselines using the same patch encoder. For example, comparison to Hist2ST and HistToGene in table 1 does not make sense because the patch encoder is different.
- Key implementation details of the author’s approach is missing, including the model size and compute time. A comparison of the author’s model size to the baseline’s sizes provides important insight into the performance comparison.
- The authors employs leave-one-out cross validation at the patient level (which is also at the slide level for many benchmarks), except for CCRCC. Leave-one-out cross validation may lead to overfitting, and this is become more concerning here because the authors use a complex approach which can easily be overfitted on to the small number of datapoints at the slide level.

### Questions
Please address the concerns raised in weakness section, especially on the implementation/evaluation details and the comparison to the baselines.

### Soundness
3

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
This paper introduces STFlow, using history imaging to predict spatial transcriptomics (ST). STFlow is a flow-based generative model to predict ST from whole slide image. STFlow chooses a zero-inflated negative binomial distribution as prior distribution. STFlow models the interaction of of gene across different spots compared to previous methods that predict at each spot independently. On a HEST1K benchmark, STFlow outperforms all baselines.

### Strengths
This paper focus on an important steps of predicting ST from WSI. It uses an innovative flow-based generative model. By incorporating spatial attention, STFlow captures dependencies between neighboring spots, reflecting the biological reality of gene regulatory networks.

### Weaknesses
Motivation of using ZINB prior is not strong: Is there a specific reason of using this distribution? Cited literatures are single cell RNA seq which is not ST. In the Table 2, it's also clear that ZINB is not helping especially for UNI and gigapath.

Notation is not easy to follow: It's claiming that algorithm 2 has a sampling factor which is gradually decrease. However, the last step is basically, $Y_{t+1} \leftarrow Y_t + (\hat{Y} - Y_t) / (T-t)$, I don't think it's decreasing? 

Different range of t in training and inference. It's clear the t in train is from 0 ~ 1 which in inference is from 0 to T - 1. I don't know how to model account for different range of t.

Limited Generalization Under Transformations: The paper mentions that the pathology foundation models used are not E(2)-invariant, potentially restricting the model's ability to generalize under certain spatial transformations. This could limit the applicability of STFlow in diverse datasets with varying orientations and scales.

Limited Dataset Diversity: The evaluation primarily focuses on the HEST-1k benchmark. Including additional datasets like STImage-1K4M from varied sources could strengthen the claims of generalizability and robustness.

### Questions
What's the motivation of using ZINB? How does this generalize to ST? Is there any other alternative?

Could you use a more clear way of presenting algorithm 2?

Please address the issue of different range of t.

Exploring or integrating E(2)-invariant architectures for the pathology foundation models could enhance the overall invariance of STFlow, improving its robustness to spatial transformations.

Please consider more dataset like STImage-1K4M.

### Soundness
3

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
4

### Summary
The paper proposes a method 'STFlow' to predict gene expression from H&E images for the Spots in ST-Data. The proposed method uses flow matching starting from data sampled from zero-inflated negative binomial distribution to account for the sparsity in the gene data. The model is a VIT based architecture and the attention is constructed to take into account K nearest neighbors spots predicted gene expressions at time T, their relative positions, and their image encodings. The authors evaluate their  method on benchmarks from the Hest1K paper and compare with spot based and slide based approaches using different backbones. Using STFlow with different foundational models shows improved performance to other baselines. The paper also includes ablation studies for different prior distributions and E(2) representation invariance approaches.

### Strengths
- The paper is well written and easy to follow.
- The proposed method seems effective for the application and surpasses all other baselines.
- The authors provide all the hyperparameters for their experiments.

### Weaknesses
 - The novelty in the method is limited / incremental.

- The motivation for ZINB priors is not clear given the ablation study showing that using zero priors gives almost same results.
In the ablation studies, using "zero distribution, where all samples are zero". I'm not sure what it means to apply Log1p to the samples. That would mean Log 0 which is zero. This needs to be clarified. Also, the results with the zero distribution see very close to ZINB. So why go through the trouble of esimtating the parameters for ZINB? and they are better than Gaussian which sounds counterintuitive but is not explained.

- How does the proposed method compare to recent methods using diffusion models for the same task, such as: stDiff: a diffusion model for imputing spatial transcriptomics through single-cell transcriptomics, Briefings in Bioinformatics, Volume 25, Issue 3, May 2024. 

- Results with ResNet50 would be insightful as to how much power is obtained from the image encoding. Similarily, a model like BLEEP is using a ResNet50 but using embeddings from more recent foundational models would make a more fair comparison to the method.

- The qualitative results in Fig 3 (a) are not convincing, specially when we visually compare the Triplex results to STFLow on TENX95. Even though the reported numbers for STFlow show higher correlation, TRIPLEX results look better.

- In Table 2, Row 4 is a copy of row 7. Looks like it was copied by mistake.

### Questions
Please refer to the weaknesses

### Soundness
3

### Presentation
3

### Contribution
2
