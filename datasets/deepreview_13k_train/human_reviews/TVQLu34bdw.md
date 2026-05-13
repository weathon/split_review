# Proteina: Scaling Flow-based Protein Structure Generative Models

- Decision: Accept
- Scores: 8, 6, 5, 6, 8

## Abstract
Recently, diffusion- and flow-based generative models of protein structures have emerged as a powerful tool for de novo protein design. Here, we develop Proteina, a new large-scale flow-based protein backbone generator that utilizes hierarchical fold class labels for conditioning and relies on a tailored scalable transformer architecture with up to $5\times$ as many parameters as previous models. To meaningfully quantify performance, we introduce a new set of metrics that directly measure the distributional similarity of generated proteins with reference sets, complementing existing metrics. We further explore scaling training data to millions of synthetic protein structures and explore improved training and sampling recipes adapted to protein backbone generation. This includes fine-tuning strategies like LoRA for protein backbones, new guidance methods like classifier-free guidance and autoguidance for protein backbones, and new adjusted training objectives. Proteina achieves state-of-the-art performance on de novo protein backbone design and produces diverse and designable proteins at unprecedented length, up to 800 residues. The hierarchical conditioning offers novel control, enabling high-level secondary-structure guidance as well as low-level fold-specific generation.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces Proteína, a foundational model for generating protein backbones with innovative fold class conditioning for precise control over structure. Proteína achieves state-of-the-art results, synthesizing diverse backbones up to 800 residues long using a scalable transformer model. It leverages a 21M-sized dataset from the AFDB and, at over 400M parameters, can generate highly designable proteins even with synthetic data. The model pioneers classifier-free, autoguidance, and LoRA-based fine-tuning in protein structure generation, and introduces novel metrics for assessing generator behavior.

### Strengths
1. The paper introduces novel metrics that address previously omitted distribution-level aspects of protein generation, which is both valuable and innovative, allowing for a more comprehensive evaluation of model performance. Additionally, the scaling of both training data and model aligns with the evolution of the field of protein generation.
2. The paper proposes an innovative $t$ sampling method that effectively captures the unique characteristics of protein data. This is also the first application of classifier-free guidance (CFG) and autoguidance in protein structure generation.
3. The methodology is presented with commendable clarity and detail.

### Weaknesses
In line 119, a partial derivative seems mistakenly written as a total derivative, and the divergence is incorrectly labeled as a gradient. I believe the right form of the continuity equation should be like $\partial p_t(\boldsymbol x_t)/\partial t=-\nabla_{\boldsymbol x_t}\cdot(p_t(\boldsymbol x_t)\boldsymbol u_t(\boldsymbol x_t))$.
Additionally, the differential symbol should be formatted in upright type, as $\mathrm{d}$, to follow standard conventions.

### Questions
1. Given that the non-equivariant model still relies on random rotations as data augmentation, is the choice to adopt a non-equivariant transformer a fundamental advantage over equivariant models, or simply a practical compromise? In other words, is it reasonable to expect that, with the current dataset and model architecture, introducing equivariance into the model could further improve performance?
2. The three newly introduced metrics (FPSD, fS, fJSD) each seem to reflect certain distributional similarities between the generated data and the reference dataset. Could the authors clarify the specific focus of each metric? Additionally, is there a possibility of merging these metrics to produce a more unified and intuitive measure?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces Proteina, which is a flow-matching based protein structure generative model. The authors make efforts to explore the scalability of the new structure and the training data which results in the largest model with impressive performance. The model introduces several interesting techniques for boosting performance including the recent proposed auto-guidance. The paper proposes several new evaluation metrics with extensive baselines to demonstrate the effectiveness of the Proteina.

### Strengths
1. The paper is certainly well written and I do enjoy the reading. 

2. The paper makes several very interesting yet important explorations and observations.  For example, though AF3 already observes the Equivariant vs Non-equivariant properties, it would be nice to further explore the scalability with non-equivariant transformers; The auto guidance parts of generation also provides some new insights into the protein structure generation; Studying protein structure generation in scale is also an important research direction for the community. 

3. I appreciate the efforts of providing comprehensive and sound evaluations for the protein structure generation tasks. Specifically, apart from the previously used simple quality/diversity measurements, the introduced FPSD/FjSD/fs could provide a fresh evaluation view at the distributional level. And I believe it could make more impact in facilitating future research.

### Weaknesses
1. Though with a scaled structure, it would be better to understand the training in a more systematic way, e.g. scaling laws. The trained flow matching model in general could still obtain the corresponding likelihood generally, could Proteina also conduct a likelihood evaluation over the protein structures? Is it possible to study the scaling laws based on that?

2. The notation of Table 1 for models with different configs is not very clear which makes it hard to read and analyze.  I also suggest the authors list the parameter size of the proposed models and baseline in an extra column. So considering the claimed fact that the proposed model is 5 times more params than previous models, the unconditional performance of M_{21M} is worse than previous methods in the sense of FPSD/ FS/diversity, for example, FrameFlow, etc. This raises a major concern of whether the general framework and formulation could provide benefits. I would like to suggest the authors elaborate more on this.

### Questions
refer to above

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
3

### Summary
This paper introduces Proteina, a novel flow-based model for protein backbone generation using a scalable non-equivariant transformer architecture. Proteina incorporates fold class conditioning and supports generation of diverse structures up to 800 residues long.

### Strengths
1. Very well-written paper and very easy to follow.
2. The authors show that large-scale non-equivariant flow models also succeed on unconditional protein structure generation.

### Weaknesses
1. The authors claim to significantly outperform all previous works; however, evidence supporting this assertion is not found in the experimental results table. Excluding unconditional models, there are no direct competitors, and comparisons can only be made with unconditional results. Even if the bold results are accepted as outperforming based on FPSD, FS, fJSD, and TM-score metrics, this model exhibits the lowest diversity.
2. RFdiffusion, ESM3, and Genie 2 were trained on different datasets, while the comparison in Table 1 uses PDB and AFDB, the comparison should be made against their respective training datasets. FPSD, FS, fJSD, and TM-score are uninformative metrics because they lack a defined optimum. To make metrics like FPSD, fS, fJSD, and TM-score meaningful, all competitors should be trained on the same dataset for a fair comparison. Instead of aiming for lower values (fS upper), the goal should be to achieve metrics that match the training dataset. Moreover, comparisons are made with PDB and AFDB without clarifying whether these datasets were part of the training set. If these examples were not used in training, there's no reason to expect lower (fS upper) values. The metrics also lack a clear scale. 
3. There are no direct competitors for conditional generation; however, RFdiffusion is capable of conditional generation and could potentially be used for CAT. For a proper comparison with competitors, other tasks such as motif scaffolding, inpainting, and fold conditioning should be addressed. 
4. The diversity TM-score is not a particularly informative metric because it lacks a clear optimal value. Instead of simply aiming for a lower score, we should be targeting diversity that aligns with the training dataset. Additionally, only the mean is reported without any measure of deviation, reducing its informativeness. The violin plot provides a better insight, showing the distribution and indicating that there are no identical structures (no collapse mode). When performing an unconditional comparison of the method with itself, the results appear unchanged, suggesting a lack of sensitivity in the metric.
5. The results lack statistical significance.
6. The code is not provided.

### Questions
1. The quality of a fold class predictor can be evaluated through classifier-guidance.
2. How was the multiview contrastive learning pretraining conducted for GearNet architechture? Did you initialize with GearNet's existing weights or carry out full pretraining? 
3. Can you please justify the use of the exponent in the Inception score equation if you are utilizing a variant without the exponent. Additionally, the Inception score has become less popular in recent years.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces a novel flow-based generative model for protein backbone design. The model leverages a non-equivariant transformer architecture, adding to the ongoing debate on the applications of SE(3)-equivariant architectures. The proposed model incorporates hierarchical fold class conditioning for controlled generation, and has been trained on a large dataset of 21 million protein structures, more than any of the previous approaches. The authors also introduce distribution-level metrics for evaluation of generative models of protein structures.

### Strengths
1. The paper is written exceptionally well. The authors provide a lot of auxillary information and details on nearly every aspect of the work.

2. This work pushes the frontier in terms of the training data scale and parameter count for the protein structure generation models. The authors demonstrate in detail their efficient architecture that enables scaling.

3. The extensive ablation studies and the details on the architecture and experiments are valuable for the community.

### Weaknesses
1. The main issue is the experimental design: in the fold class-conditional generation, Proteina is not compared to any other models, while the unconditional generation setting is invalid, since the baselines are trained on different data while being compared to PDB and AFDB. This renders the statements on "vastly outperforming all baselines" false. Another concern about the experimental design is self-evaluation bias: the work introduces a dataset, a model, and a set of evaluation metrics that use their own classifier without external validation.

2. The proposed metrics (FPSD and fJSD) are highly correlated and redundant. Calculation of Frechet distances to PDB and AFDB datasets does not make sense until the models are trained on those datasets. Generative models should generate samples resembling their respective training data, not PDB or AFDB. Either all the baselines should be trained on the same dataset and FPSD and fJSD calculated for this dataset, or another set of metrics should be chosen to evaluate unconditional generation. When using distributional distance metrics, it is a good idea to provide a sense of scale by measuring such distance between random samples in the dataset itself.

3. I agree with the Authors' critique of the existing metrics like diversity and novelty. But there is more to it. The TM-score diversity metric is not informative and lacks an optimal reference point. Providing distributions over TM-scores (e.g., violin plots) would be much more informative than the provided mean over different means over different length ranges. The TM-score expected from the generative model depends on the dataset it is trained on, so providing such value for a subset of a dataset is a good idea. Another issue with metrics is that a single threshold for cluster diversity is not enough as a 50% level cannot detect mode collapse inside the clusters. For example, when each cluster consists of identical structures memorized by the model.

4. The use of a classifier is justified in the experiments that include predictions on the noised data, however, the classifier has not been trained on the noisy data which makes the claim that it can evaluate protein realism weak. If the classifier was trained on the noisy structures, it could be used for classifier guidance.

5. The task scope is limited, which hinders our ability to assess the model. The Authors show unconditional generation and fold class-conditional generation. However, the comparison with other models is poorly set up in the case of unconditional generation and is not performed at all in the case of fold conditioning. The remedy could come from solving other tasks where several baselines exist, for example, motif-scaffolding/inpainting.

### Questions
Could you please provide the details on how the GearNet-based classifier was trained? From scratch with contrastive objective as in the original paper, or from the pretrained model, if so, how exactly?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents Proteina, a new large-scale flow-based protein backbone generator that utilizes hierarchical fold class labels for conditioning and relies on a tailored scalable transformer architecture. The model is trained on up to 21 million protein structures, a significant increase compared to previous work. Proteina achieves state-of-the-art performance on de novo protein backbone design and produces diverse and designable proteins at unprecedented length, up to 800 residues. The hierarchical conditioning offers novel control, enabling high-level secondary-structure guidance as well as low-level fold-specific generation. In addition, the paper also offers numerous practical insights that can serve as valuable references, such as LoRA fine-tuning, autoguidance, and new evaluation metrics.

### Strengths
- The paper demonstrates the current state-of-the-art capabilities in protein backbone design.
- The paper addresses the longstanding issue of insufficient $\beta$-sheets in this field by introducing the CAT lable.
- The paper introduces new evaluation metrics that offer a fresh perspective for examining the model.
- The paper provides valuable insights by exploring numerous practical techniques, e.g., LoRA fine-tuning and autoguidance, in the field of protein design.

### Weaknesses
 - Although the article provides detailed implementation details, Proteina, as a complex system engineering project, requires open-source code and data as essential resources for reproducibility.
- The paper does not provide a discussion on the scaling trends of the data and model, meaning we cannot determine whether the 21 million protein structure data points and 400 million model parameters are necessary conditions for achieving the current performance of Proteina. Specifically, the absence of ablation studies on the training data size makes it difficult to assess the contribution of the large dataset. It is unclear if a smaller, more curated dataset could achieve comparable results, or if the performance gains are solely due to the scale of the data. Furthermore, the lack of analysis on the model size scaling makes it difficult to understand the trade-offs between model complexity and performance. It is not clear if the current model size is optimal or if a smaller model could achieve similar results with less computational cost.


### Questions
- As a method for backbone design, is the input sequence representation in the model composed entirely of a sequence made up of the same special symbol?
- Will the newly proposed metrics, which are based on the fold classifier, create an unfair competitive advantage for Proteina, as it uses CAT as an input? Could a more general classifier be used to improve the design of these metrics?
- For a single protein design, are all amino acids input using the same CAT label (e.g., amino acids A and B both use the label X), or is the CAT label adjusted specifically for each amino acid (e.g., amino acid A uses Xa and amino acid B uses Xb)?

### Soundness
4

### Presentation
4

### Contribution
4
