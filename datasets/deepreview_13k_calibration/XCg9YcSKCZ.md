# Weak Supervision from Vision-Language Models to Self-Improve on Downstream Tasks

- Decision: Reject
- Avg Score: 3.50
- Scores: 5, 3, 3, 3

## Abstract
We present SelfPrompt, a novel prompt-tuning approach for vision-language models (VLMs) in a semi-supervised learning setup. Existing methods for tuning VLMs in semi-supervised setups struggle with the efficient use of the limited label-set budget, the negative impact of the miscalibrated VLMs on pseudo-labelling, and the accumulation of noisy pseudo-labels. SelfPrompt addresses these challenges by introducing (a) a weakly-supervised sampling technique that selects a diverse and representative labelled set, (b) a cluster-guided pseudo-labelling method that improves pseudo-label accuracy, and (c) a confidence-aware semi-supervised learning module that maximizes the utilization of unlabelled data by combining supervised learning and weakly-supervised learning. We conduct extensive evaluations across 13 datasets, significantly surpassing state-of-the-art performances with average improvements of 6.23\% in standard semi-supervised learning, 6.25\% in our proposed active semi-supervised learning,  and 4.9\% in base-to-novel generalization, using a 2-shot setup. Furthermore, SelfPrompt shows excellent generalization in single-shot settings, achieving an average improvement of 11.78\%.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work proposes SelfPrompt method to address the semi-supervised fine-tuning problem of CLIP. SeflPrompt contains: (1) weakly supervised sampling to select the few-shot confident examples as pseudo-labels; (2) cluster-guided pseudo-labeling to select min-centroid distance samples as cluster-wise pseudo-labels; (3) confidence aware semi-supervised learning which separately learn from confident (with supervised learning) and low-confident samples (with weakly-supervised learning). The empirical results demonstrate the significant performance gains compared with several state-of-the-art baselines on existing semi-supervised learning and few-shot learning benchmarks. The ablation results justify the contribution of each proposed component.

### Strengths
strengths:

- The performance gains of the proposed method is significant compared with previous baselines.
- The identified sampling issue of CLIP few-shot benchmark is insightful.
- The experiments are comprehensive to validate the effectiveness of the proposed method.

### Weaknesses
Limitations:

- Lack of technical novelty: The proposed method is primarily based on pseudo-label thresholding and selection, which has been well-studied by semi-supervised learning a few years ago. The identified sampling issue of existing CLIP few-shot benchmarks is somehow insightful.
- Lack of implementation details: Although the sensitivity of hyperparameters are studied, how hyperparameters are determined for various datasets is unclear. Does it involve dataset-specific tuning?
- Lack of baselines: Two recent baselines are neglected. The comparisons with them are necessary to claim the state-of-the-art performance of the proposed method.

[1] PLOT: PROMPT LEARNING WITH OPTIMAL TRANSPORT FOR VISION-LANGUAGE MODELS

[2] AWT: Transferring Vision-Language Models via Augmentation, Weighting, and Transportation

### Questions
All my concerns are listed in the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper proposes a prompt-tuning approach for VLM adaptation. Specifically, to mitigate the impact of sub-optimal VLM predictions, a quantile-based sub-sampling strategy which removes the most and least confidently predicted samples and selects candidate samples based on closeness to class-based cluster centers. These labelled samples are used in prompt-tuning the VLM.

### Strengths
The paper is well written and easy to follow throughout.

The results are promising and experimentation is comprehensive, including the ablation study.

### Weaknesses
The number of baselines is too small. There are many other baselines the authors could have implemented (as evidenced in the base-to-novel generalization results).

Please see questions section.

Line 253 says "does not rely on the VLM to generate psuedo-labels". This appears incorrect to me, as the VLM probabilities are used to determine which samples are used in clustering?

Line 249 says to "gather the labels of the selected samples". By labels, is this referring to the pseudo-labels? If not, then where are these labels taken from?

It is unclear to me what the loss function defined in line 282 is used to optimise. The prompt-tuning pipeline is not clearly and formally defined in the preliminaries as it should be.

The problem setting is fundamentally flawed: It is not realistic to assume we can selectively choose which samples are most helpful to somehow obtain labels for when they come from an unlabeled set.

### Questions
Line 253 says "does not rely on the VLM to generate psuedo-labels". This appears incorrect to me, as the VLM probabilities are used to determine which samples are used in clustering?

Line 249 says to "gather the labels of the selected samples". By labels, is this referring to the pseudo-labels? If not, then where are these labels taken from?

It is unclear to me what the loss function defined in line 282 is used to optimise. The prompt-tuning pipeline is not clearly and formally defined in the preliminaries as it should be.

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
The authors present SelfPrompt, a prompt-tuning approach for vision-language models (VLMs) in a semi-supervised learning setup.
SelfPrompt introduces a weakly-supervised sampling technique that selects a diverse and representative labelled set, a cluster-guided pseudo-labelling method that improves pseudo-label accuracy, and a confidence-aware semi-supervised learning module that maximizes the utilization of unlabelled data by combining supervised learning and weakly-supervised learning.

### Strengths
- The structure of this paper is well-written and easy to follow.

- The authors provide thorough ablation studies, which is helpful in understanding different design choices applying pseudo-labeling into semi-supervised learning of CLIP

- The qualitative examples as well as the failure cases effectively help the reviewer understand how the model performs on specific examples and the limitations.

### Weaknesses
 - Lack of explanation for some hyperparameters such as $\lambda$, the number of quantiles, the number of samples, etc (for example the number of quantiles, why choosing the large range as 3, 5, 20?).
- Why does CPT under 4-shot experiments fall short against SelfPrompt?
- What are the results if we set the number of samples larger than 50, as from Table 7c, the larger the better.
- If we drop different sizes of high and low confidence sets, does it improve the performance?
- The part I am most concerned about is dropping high and low confidence subsets. For example, dropping the samples with probability <= 50\% is reasonable, but dropping both high and low could remove the good information and making the model slow to converge.

### Questions
see Weaknesses

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes SelfPrompt, a prompt-tuning approach for VLMs. SelfPrompt consists of three modules: a weakly supervised sampling technique, a cluster-guided pseudo-labeling method, and a confidence-aware semi-supervised learning module. The authors conducted extensive evaluations across 13 datasets, and SelfPrompt achieves state-of-the-art performance.

### Strengths
- Tuning VLMs in the semi-supervised learning setting is an important problem as it can utilize abundant unlabeled data.

- Using a limited budget to label important samples is an important and practical problem. However, this is a new setting different from standard semi-supervised learning in [3] (refer to weaknesses). 

- The authors conducted extensive experiments and SelfPrompt achieved much better performance than existing methods (but with potential comparison problems, see weaknesses).

### Weaknesses
1. Weakly-supervised learning (WSL) is an important topic in machine learning. WSL frequently appears and seems to be an important component of this paper. Authors should discuss related WSL papers in the related work section and other parts of this paper.

2. The presentation of the problem setting is unclear. The authors define the setting as being given $M$ unlabeled data and $N = n \times c$ labeled data. However, in line 180, the authors also state, "In a few-shot learning setting with $N$ samples, the common strategy is to randomly select $n$ samples per class from the unlabeled set $U$ to form the labeled set." So, how is the labeled dataset formed? Are we given labeled data, or do we select labeled data from the unlabeled dataset and assign pseudo labels to them to form a labeled dataset? In standard semi-supervised learning, both labeled and unlabeled datasets are provided, so I am confused with the setting in this paper. Authors are suggested to write this part more clearly for understanding. Below I can only continue by guessing the setting is selecting important data ('limited budget' in paper) and then assigning ground truth labels to them as the labeled dataset. If this is true, then:

- The setting in this paper is not standard semi-supervised learning (SSL). In standard SSL, we are given both labeled and unlabeled datasets (we cannot select which data are labeled), and methods are designed to address this setup. However, in lines 38–41, the authors claim that one limitation of existing methods is that "existing methods typically select the labeled sample set randomly." However, this is not a limitation of existing methods. In standard SSL, we cannot control the selection of labeled data, so random selection is used to mimic practical scenarios, and it is not part of the method but the experiment setting. Using a limited budget to label important samples is an important problem, but it is different from the standard SSL problem in [3] and should be regarded as a new setting. So, the experimental comparison is not proper, as other methods are designed for standard SSL. It is better to make the setting more clear and show that the performance of these existing methods can be boosted using these selected labeled datasets. To show the effectiveness of the later part of pseudo-labeling for SSL, the labeled set should be the same.  

3. One motivation for filtering is: "Highly confident samples offer minimal information gain, as the model is already certain of their classification." However, is this claim really correct? Are there any references to support this? In my view, in many semi-supervised learning works [1, 2], authors have proposed using thresholds to select highly confident samples for training and filter out unconfident, noisy data. This suggests that highly confident samples are important for training. I am not sure whether the motivation in this paper is correct and appropriate. Moreover, "Highly confident samples" is very vague. Can the authors use something like probability to describe it?

4. It is unclear why the authors perform k-means with $N$ clusters instead of $C$. $N = n \times C$ is the number of labeled data with no semantic meaning (In my view). To me, k-means with $C$ clusters makes more sense, since $C$ is the number of classes, and clustering with respect to classes seems appropriate. However, it seems that there is no semantic meaning for $N$, so why are we clustering samples into $N$ clusters?
Could the authors further clarify the motivation of this part?

5. The authors claim that "Cluster-guided pseudo-labeling" does not rely on VLM predictions for pseudo-labeling. However, this claim is not entirely convincing. As stated in line 256, "the clusters are formed based on embedding similarity," and the embedding similarity is derived from VLM pretraining knowledge. So, if there is bias in the VLM-generated pseudo-labels, the embedding generated by VLMs is likely to contain similar bias.

6. The module "Confidence-aware semi-supervised learning" contradicts the earlier claim that "Highly confident samples offer minimal information gain, as the model is already certain of their classification." If the authors claim that highly confident samples are not important and exclude them from the pseudo-labeled dataset, why do they now claim that confident samples are important and use them here? Moreover, this module seems similar to [3], could authors discuss the difference?


7. Reproducibility: The authors did not report the values of the hyperparameters$p$, $q$, $\tau$, and $\lambda$ in the experiment section. For reproducibility, the authors should report these values and discuss how to select them in the implementation details section.

8. Undefined and unclear variables:
- In line 264, $(x_{j1},y_j)$, what is j?

- The definition of $X_{\text{weak}}$ is unclear. The authors only define $x_i \notin X^+$, but where does $x_i$ come from?

- $L_{\text{weak}}$ is not defined.

- How the function top$_t(\cdot)$ defined? 

- $f$ is not defined. Is it $\theta$? Moreover, the authors should define $\lambda$ as a hyperparameter in the paper.

- Subscripts are very confusing: the authors use subscripts to distinguish different vectors but also use subscripts to represent the corresponding elements of the vector.  For example, authors use $s_{i}$ to represent the corresponding vector for $x_i$, but in Eq. 6, the authors seem to use $s_c$ to represent the c-th element. 

Minor problems:

The presentation of this paper is not very polished. The authors should pay attention to the math formulas and variable definitions. The form of variables should be consistent. Some of the issues with the math formulas are listed below:
- The input $x_i$ is a vector and it should be represented in bold.
- In Eq. 2, $p_{ic}$ is not defined. Maybe it should be $p_i^c$?
- In line 238, the form of $Q_k$ is different from line 236.
- In line 262, $\mathbf{z}^*_j$ is not defined, and $|| \cdot ||^2$ is not defined.
- The form of $P_j$ is different from how it is defined in line 260.
- The form of $X_p$ in Eq. 4 is different from how it is defined in line 264.
- $s_i$ is a vector but is not represented in bold.
- In Eq. 5, the $X_L$ is not in a consistent form. 
- SOTA is not defined. The authors should introduce it as "state-of-the-art (SOTA)" and then use the abbreviation.

### Questions
How do the three datasets ($X_L$, $X_+$, and X_{weak}) change during the tuning process? Could authors provide a pseudo-code to better understand how the method is implemented?

### Soundness
3

### Presentation
1

### Contribution
2
