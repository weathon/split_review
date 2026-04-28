# Multi-Atlas Brain Network Classification through Consistency Distillation and Complementary Information Fusion

- Decision: Reject
- Scores: 8, 5, 5, 6

## Abstract
In the realm of neuroscience, identifying distinctive patterns associated with neurological disorders via brain networks is crucial. Resting-state functional magnetic resonance imaging (fMRI) serves as a primary tool for mapping these networks by correlating blood-oxygen-level-dependent (BOLD) signals across different brain regions, defined as regions of interest (ROIs). Constructing these brain networks involves using atlases to parcellate the brain into ROIs based on various hypotheses of brain division. However, there is no standard atlas for brain network classification, leading to limitations in detecting abnormalities in disorders. Some recent methods have proposed utilizing multiple atlases, but they neglect consistency across atlases and lack ROI-level information exchange. To tackle these limitations, we propose an Atlas-Integrated Distillation and Fusion network (AIDFusion) to improve brain network classification using fMRI data. AIDFusion addresses the challenge of utilizing multiple atlases by employing a disentangle Transformer to filter out inconsistent atlas-specific information and distill distinguishable connections across atlases. It also incorporates subject- and population-level consistency constraints to enhance cross-atlas consistency. Additionally, AIDFusion employs an inter-atlas message-passing mechanism to fuse complementary information across brain regions. Experimental results on four datasets of different diseases demonstrate the effectiveness and efficiency of AIDFusion compared to state-of-the-art methods. A case study illustrates AIDFusion extract patterns that are both interpretable and consistent with established neuroscience findings.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper aims to classify brain networks from fMRI BOLD ROIs using multiple (potentially conflicting) atlases. The authors resolve conflicts with a deep neural network (specifically a "disentangle transformer") alongside external prior information related to subject and population constraints.

To evaluate the efficacy of the proposed approach, the authors compare against several classical and current methods on four disparate datasets with a classification downstream task. Their method achieves the greatest quantitative results compared to all others in nearly all cases.

### Strengths
This approach is well-motivated, as there is no consensus on the number of atlases to use. Using a single atlas conforms to the biases induced that particular atlas, and using multiple atlases involves the use of novel methods which do not regularize consistency across multiple atlases. The proposed approach aims to achieve both consistency across multiple atlases as well as providing their model ROI-level "information exchange." Accomplishing these two aims required the development and use of several techniques, including the proposed "disentangle transformer" and "identity embedding", the use of an orthogonality loss on a component of the representations, a nearly-linear learnable mapping for inter-atlas message passing, a bespoke contrastive loss for subject-level consistency, and a similarity loss for "maintain the relationship of subjects across atlases."

This paper is well-motivated and fairly comprehensive with respect to the classification experiments. The contribution of the approach as an improvement for classification of brain networks is clear. I recommend this paper be accepted.

### Weaknesses
In addition to my recommendation for acceptance, I enumerate some concerns I have below:

1. The technical claims are not fully supported. The "identity embedding" is either mis-named or its explanation is unclear. The embedding is not identity; it seems instead to simply be a learnable embedding. It is unclear whether the parameters of the MLP in Eq. 1 are learnable. If so, what is the purpose behind W_ID?
2. The efficacy of the "disentangle Transformer" is not fully supported. How well are conflicting atlases disentangled? Was the orthogonal loss actually useful towards separating shared and conflicting information across atlases? An experiment to support the authors' intuition is missing.
3. The same is true for both subject- and population-level consistencies as well as message-passing. The explanation is sensible in text, but the actual efficacy of the proposed architecture and losses is not described in the experiments and results. The reader sees that the downstream classification is improved in light of the proposed components, but it is unknown whether these components accomplish what they are intended to.
4. Some figure and table captions are too terse. Figure1, table 1, table 3 could benefit from better description to help the reader understand their contents.
5. Table 5 experiment times include training, validation, and testing across multiple cross-validation folds. This is unusual; instead, reporting training+validation time and then testing time (for a single subject) separately would be more conventional. This guides future users of the proposed method towards how much time and compute should be budgeted for training the approach as well as what hardware is necessary to use the proposed method at scale in their own work.

### Questions
These questions are adapted / copied from the weaknesses listed above:

1. It is unclear whether the parameters of the MLP in Eq. 1 are learnable. If so, what is the purpose behind W_ID?
2. The efficacy of the "disentangle Transformer" is not fully supported. How well are conflicting atlases disentangled? Was the orthogonal loss actually useful towards separating shared and conflicting information across atlases? An experiment to support the authors' intuition is missing.
3. The same is true for both subject- and population-level consistencies as well as message-passing. The explanation is sensible in text, but the actual efficacy of the proposed architecture and losses is not described in the experiments and results. The reader sees that the downstream classification is improved in light of the proposed components, but it is unknown whether these components accomplish what they are intended to. What evidence do the authors have towards these claims?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
Resting-state functional MRI is often used to predict behavioral phenotypes by measuring correlations between disparate regions/parcels of the brain. There are many different parcellation conventions (“atlases” in this context) and downstream analyses are often quite dependent on the choice of atlas.

Submission 4706 presents a classification framework that integrates multiple different atlas conventions for a given subject. They propose a transformer that extracts complementary information and gain modest accuracy increases across four different datasets.

### Strengths
- The use of [transformer registers](https://arxiv.org/abs/2309.16588) (herein called “incompatible nodes”) for potentially filtering out incompatible information across atlases is a novel and interesting application.
- The use of spatial distances between regions of interest in the brain when constructing the message-passing framework is interesting and, to my limited knowledge, not commonly done.
- Generally clearly and straightforwardly presented.

### Weaknesses
I do not work in this specific subfield and would be happy to revisit my score and look forward to the discussion phase. I also did not read the appendix so please correct me if I missed something.

### 1. Unclear motivation for transformer-based approach on processed connectomes

The datasets in fMRI connectomics are (understandably) limited in sample size, ranging here from N=60 to N=1300. 

However, it is unclear how the submission can adequately train transformers on 60 data samples. Without inductive bias (beyond permutation equivariance), transformers require several orders of magnitude higher training sets across the literature. I do not see any mention of pretraining either on larger datasets (e.g. UKBiobank) that would potentially enable few-shot finetuning.

Further, could the authors please elaborate on why they chose to work only with the processed connectomes instead of the high-dimensional raw data where there may be more potential for self-supervised pretraining?

### 2. Using only two atlases in experiments

The submission motivates itself by claiming that multiple atlases provide complementary information (which is a reasonable hypothesis) but its experiments only use two atlases (Schaefer100 and AAL116). Given that there is a wide range of potential atlasing procedures and many other atlases are often used, could the authors please clarify why two atlases were used in the experiments?

### 3. Unclear significance

The main comparative results (presented in Table 2) are largely well within each others’ error bars without clear significance.

Is there high inter-subject or inter-site variability s.t. standard deviations are inflated? Plotting per-subject performance as a supplemental figure should clarify this.

Further, could the authors please perform significance tests with corrections for multiple comparisons s.t. readers can assess whether these gains are meaningful?

### 4. Baseline choices and clarifications

#### 4.1. Iterative/conventional baselines

The only iterative baselines included for comparison are logistic regression and SVMs. It is not mentioned whether these methods were regularized in any form (e.g. LASSO) and, if so, whether the regularization hyperparameters were tuned at all. As far as I’m aware, practitioners [largely use LASSO-style methods for behavior prediction](https://db.humanconnectome.org/megatrawl/HCP820_MegaTrawl_April2016.pdf) and find that the regularization weight strongly affects the results.

Further, to my knowledge, deep nets and methods such as kernel regression are largely equivalent on this task when tested on much larger sample sizes ( [reference](https://pubmed.ncbi.nlm.nih.gov/31610298/) ).

As all results are well within each other's error bars (see point 3 above), could the authors please detail why only two non-DL methods were benchmarked and whether these methods were regularized and tuned?

#### 4.2 Transformer baselines

Several transformer-based approaches to fMRI classification are neither cited nor benchmarked against. For example,
- https://link.springer.com/chapter/10.1007/978-3-031-43993-3_28 (MICCAI’23)
- https://link.springer.com/chapter/10.1007/978-3-031-72390-2_14 (MICCAI’24)

Additionally, while not a one-to-one comparison to these papers use of static splits vs. the submission using 10-fold CV, these papers report much higher performance on ABIDE (high-70s vs the paper’s mid-60s accuracy). 

Could the authors please address differences relative to these works, whether they could be used as baselines, and what could explain the major performance differences?

### 5. Missing ablations for key contributions

The paper has several moving parts, all of which are claimed as novel contributions. However, the core parts of Section 4.1 (the identity embedding, the “disentangle Transformer”, and the orthogonal loss) are not ablated. Please do so in the rebuttal or future versions.

### 6. Minor
These aspects do not affect my score.

- The paper claims that not all regions of the brain are covered by all atlases and thus integrating multiple atlases may have benefits. Please correct me if I’m wrong but don’t atlases such as Shen and Craddock cover most of the brain? 
- Somewhat orthogonally, multiple atlas _harmonization_ can also be performed as with iterative methods like [CAROT](https://www.sciencedirect.com/science/article/am/pii/S136184152300124X). Could the authors please clarify the differences in motivation for their approach vs. atlas harmonization? I ask as much of the paper is motivated by the goal of integrating information across atlases and there are existing methods to do so.

### Questions
- How is transformer training feasible on tiny datasets with sample sizes of N=60 and N=1300 without any self supervised pretraining?
- Why work with processed connectomes instead of raw data for transformer training?
- Please perform significance testing with multiple comparisons adjustments.
- Please describe how the conventional baselines were tuned and whether they were regularized
- Please add ablations for the key contributions in 4.1

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
In this paper, a novel method named AIDFusion is proposed to learn unified and informative representations of brain functional networks derived from multiple brain atlases, which are expected to facilitate the brain network based classification. The method consists of several modules including disentangle transformer, inter-atlas message-passing, subject-level and population-level consistency to learn atlas-consistent information. The proposed method has been evaluated on multiple datasets to demonstrate its effectiveness.

### Strengths
1. The idea of learning unified representation from multiple brain networks is promising to improve classification performance.
2. Multiple techniques are proposed to facilitate the unified representation learning, e.g., disentangle transformer, inter-atlas message-passing, and multi-level consistency.

### Weaknesses
1. The brain networks from different atlases will contain atlas-consistent information and atlas-specific information, both types of information may be informative for classification. While the proposed method adopts several techniques to get enhanced atlas-consistent information, the atlas-specific information may not be effectively captured. Not sure if the proposed disentangle transformer may discard atlas-specific information that are useful for classification.
2. As demonstrate in the experimental results, the fusion of multiple arbitrary atlases may not improve classification performance. It is not clear and not verified what atlases should be fused.

### Questions
1. For the identity embedding in the disentangle transformer. It is not clear how the identity embedding was implemented. "... a parameter matrix W_ID to encode nodes within the same ROI", but it looks like one node corresponds to one brain ROI in the proposed method.
2. The brain networks from different atlases will contain atlas-consistent information shared across atlases and atlas-specific information, both types of information may be informative for classification. While the proposed method adopts several techniques to get enhanced atlas-consistent information, the atlas-specific information may not be effectively captured. Not sure if the proposed disentangle transformer may discard atlas-specific information that are useful for classification.
3. The Eq.(9) is not correct. I think i refers to ROI in atlas a or b, not cluster.
4. The AAL atlas contains both cerebral cortex, subcortical structures, and cerebellum regions, while the Schaefer atlas only covers cerebral cortex regions. Not sure if it is proper to learn consistent representations from brain networks with different brain coverages.
5. As demonstrate in the experimental results, the fusion of multiple arbitrary atlases may not improve classification performance. A principled way to identify what atlases should be fused is needed.
6. When applied to more than 2 atlases, will the orthogonal loss, inter-atlas message passing, and subject/population-level consistency be computed for each pair of atlases?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes a method called AIDFusion, designed to improve brain network classification using rs-fMRI data. 

The authors note that existing methods often rely on single atlases for classification, while approaches that utilize multiple atlases tend to overlook cross-atlas consistency and fail to facilitate information exchange at the ROI level. To address these issues, the authors first introduce a disentangled Transformer to learn atlas-level embeddings. They then propose an inter-atlas message-passing mechanism to fuse complementary information across brain regions. Additionally, subject-level and population-level consistency losses are employed to enhance cross-atlas coherence.

### Strengths
- Originality: This paper demonstrates some novelty. For instance, the concept of inter-atlas message-passing is interesting.
- Quality: The methodology is validated across four datasets representing different diseases, effectively showcasing its effectiveness and efficiency.
- Clarity: The paper is well-structured and easy to follow, enhancing comprehension for readers.
- Significance: This research offers new insights into brain network analysis within the field of neuroscience.

### Weaknesses
**1. There are too many hyperparameters to tune, which undermines the credibility of the results.**

For example, the training loss comprises five components, with four parameters requiring tuning. Additionally, hyperparameters from other modules of the method, such as the k value in KNN (lines 258-259), the keeping ratio (lines 278-279), and the temperature parameter (lines 302-303), also need to be set appropriately.

**2. The presence of numerous networks to learn complicates the training process, potentially leading to instability.**

This includes the transformers in lines 216-240 and three GCNs in lines 263-267 and 280-285.

**3. The motivations for some modules are unconvincing.**

For example, in lines 216-221 and 242-245, the authors mention introducing incompatible nodes and using orthogonal loss to filter out inconsistent atlas-specific information, citing the [CLS] token in NLP as motivation. However, the relationship is not adequately established, and the effect of these incompatible nodes is not clearly illustrated or justified.

**4. The comparisons are insufficient.**

Given that the atlas embedding learning is a transformer-based method, comparisons with additional transformer-based methods, such as [1], should be included. Additionally, other multi-atlas methods, like [2], should be considered. the manuscript may lack ablation studies that directly concatenate embeddings from single-atlas methods across different atlases similar in [2][3].

*[1] Kan, X., Dai, W., Cui, H., Zhang, Z., Guo, Y., & Yang, C. (2022). Brain network transformer. Advances in Neural Information Processing Systems, 35, 25586-25599.*

*[2] Wang, W., Xiao, L., Qu, G., Calhoun, V. D., Wang, Y. P., & Sun, X. (2024). Multiview hyperedge-aware hypergraph embedding learning for multisite, multiatlas fMRI based functional connectivity network analysis. Medical Image Analysis, 94, 103144.*

*[3] Zhao, B. W., You, Z. H., Wong, L., Zhang, P., Li, H. Y., & Wang, L. (2021). MGRL: Predicting Drug-Disease Associations Based on Multi-Graph Representation Learning. Frontiers in genetics, 12, 657182. https://doi.org/10.3389/fgene.2021.657182*

### Questions
Given the small sample sizes of rs-fMRI datasets, as stated in lines 325-330, how did you overcome the risk of overfitting during the training process and determine hyperparameters?

### Soundness
2

### Presentation
3

### Contribution
2
