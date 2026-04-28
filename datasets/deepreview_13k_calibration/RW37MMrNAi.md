# Class-wise Autoencoders Measure Classification Difficulty And Detect Label Mistakes

- Decision: Reject
- Avg Score: 5.60
- Scores: 8, 3, 6, 3, 8

## Abstract
We introduce a new framework for analyzing classification
datasets based on the ratios of reconstruction errors between autoencoders trained on individual classes. This analysis framework enables efficient characterization of datasets on the sample, class, and entire dataset levels. We define reconstruction error ratios (RERs) that probe classification difficulty and allow its decomposition into (1) finite sample size and (2) Bayes error and decision-boundary complexity. Through systematic study across 19 popular visual datasets, we find that our RER-based dataset difficulty probe strongly correlates with error rate for state-of-the-art (SOTA) classification models. By interpreting sample-level classification difficulty as a label mistakenness score, we further find that RERs achieve SOTA performance on mislabel detection tasks on hard datasets under symmetric and asymmetric label noise.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work presents a method for noisy label detection, which also serves as a way to assess dataset difficulty. Using a large visual foundational model (non-feature-based, so not convolutional), the method extracts representations for each datapoint. Next, simple autoencoders with UMAP regularization are trained for each class. The ratio between reconstruction errors for the target class and the next-best autoencoder class is then used to estimate label noisiness and misclassification probabilities. From my understanding, this ratio between reconstruction errors acts as a proxy for margin. Furthermore, the authors provide numerical results to help predict the inherent difficulty of a class by interpolating reconstruction ratios at an infinite number of datapoints.

### Strengths
The paper proposes a simple yet (according to the authors) novel method to approximate dataset difficulty with minimal training required on basic autoencoder models. Furthermore, their methods for detecting misclassification are straightforward and reportedly more effective than previous ones.

### Weaknesses
Much of the issues I have with the paper lie in the presentation of the work, which may have led me to misunderstand certain concepts. For example, when explaining the different types of noise (i.e., symmetric, confidence-based, etc.), I still don’t feel I have a solid grasp of these concepts after reading the passage. Perhaps the authors could clarify further, either with mathematical notation or visuals, to help readers gain a better understanding. Another example is the appearance of the tuning parameters, such as $\gamma$, which are often introduced but not discussed in depth.

With regard to the graphs, while I understand and acknowledge the difficulty of fitting so much information into limited space, I think the visuals could be improved. Figures 1 and 5–6 are particularly cluttered due to the choices of pointers and line styles for different noise types and methods, making them difficult to interpret. Meanwhile, I think the space occupied by Figure 2 could be better used to provide additional information for the reader.

Finally, regarding the experimental setup, while I understand that details are provided in the supplementary material, I would appreciate further discussion in the main body on certain neural architecture specifics. Additionally, I find it odd that certain larger datasets, such as ImageNet, are excluded from the analysis—though I may have missed this explanation.

### Questions
1- Doesn’t Equation 9 supposedly provide a form for retrieving the threshold? Are these hyperparameters expected to work universally across any dataset? If so, what is the purpose of Section C.1?

2- Could you please provide a mathematical or visual explanation of the different noise types?

3- Are there specifics regarding whether a particular datapoint has appeared in the training set of the foundational model used? Wouldn't this have certain theoretical and practical implications if the datapoint or even the class hasn’t appeared in the source dataset of the foundational model?

4- Is the notion of the ratios of reconstruction errors effectively a reinterpretation of classification margin? Do they have a direct relationship, such as an upper or lower bound?

5- To find the extrapolated limits for class difficulty, don’t we need to train with a variety of different sample sizes, and wouldn’t this increase the algorithm’s cost significantly? If I understand correctly, this increased cost doesn’t apply to label noise detection, correct?

6- In Figure 1, this is perhaps a minor detail, but why are the higher values (brighter points) not located on the edges of the distribution in the 2D representation? Shouldn't they be more outlier-like compared to other datapoints?

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
3

### Summary
The paper propose a novel method based on the reconstruction loss of class-wise samples to analyse several datasets used in classification. In particular, the proposed method employs features extracted from some pre-trained models to train class-wise auto-encoders and use the normalised reconstruction loss, either at sample level or dataset level, to analyse different characteristics of datasets, such as classification difficulty or label noise detection. The paper also provides some post-hoc analysis that matches several observations from a wide-range of visual classification datasets.

### Strengths
The paper tackles an important problem in data-centric machine learning, which is to analyse the characteristics of datasets. The major strength is to provide an extensive empirical results and several observations on many visual datasets used in classification.

### Weaknesses
1. The paper is purely an empirical study based on many observations from a certain number of datasets. However, the claim is to provide a formal theory to analyse datasets, to me, is exagerating. This may be because there are different understanding of theory. To my understanding, theory is developed from certain axioms, then theorems built uppon those axioms coupled with further assumptions are proved. However, the ones presented in the paper are only empirical observations without any formal proofs. Some of the analysis, to me, are just curve-fitting based on what have been observed (e.g., Eq. (5)). To this end, I disagree with the claim about a new theory for dataset analysis.
2. The authors make many strong confirmations based on empirical observations on a narrow setting without any formal proof. For example, at line 262, the conclusion that the "specific features used are irrelevant". This may be true in this setting because the two feature extractors (e.g., CLIP and DINO) are pre-trained on datasets that already include or have similar images in the 18 datasets considered. If a bad feature extract is used, the empirical result may be different. In addition, if a dataset that is outside of the training data of those feature extractors, the results may also be different. For example, one can evaluate on datasets in medical, biology or space exploration.
3. In section 4.3 presenting a way to estimate symmetric label noise from the reconstruction error ratio, the proof requires further clarification, especially when simplifying the second term in Eq. (16). To make it clear, the second term of Eq. (16) is restated here:
$$
\text{second term of (16)} = \eta \mathbb{E}_{X} \left[ \frac{\Delta_{\tilde{c}} (\mathbf{x}^{c^{\prime}}) }{ \Delta_{rand} (\mathbf{x}^{c^{\prime}}) } \right],
$$
and the one defined in Eq. (6) is:
$$
\Delta_{rand} (\mathbf{x}^{\tilde{c}}) = \mathbb{E}_{c^{\prime} \in \mathcal{C} \setminus {c}} \left[ \Delta_{c^{\prime}} (\mathbf{x}^{\tilde{c}})  \right].
$$
It is hard to understand how to use the result in Eq. (6) to apply to the numerator of the second term in Eq. (16) because:
 - the two expectations are different. The one in (16) is w.r.t. $\mathbf{x}$, while the one in (6) is w.r.t. auto-encoder or class $c^{\prime}$, and
 - the expectation in (16) is applied to a ratio of two functions of $\mathbf{x}$, and note that: $\mathbb{E}[f(x) / g(x)] = \mathbb{E}[f(x)] / \mathbb{E}[g(x)]$ does not generally hold. Furthermore, the jump from Eq. (16) to Eq. (17) requires more justification. Specifically, the substitution of the expectation of a ratio with a ratio of expectations is not generally valid, and the subsequent simplification relies on this questionable step. Approximating a random variable by its expected value is not mathematically sound without further assumptions or justification.

### Questions
My main concerns have been stated in the weaknesses. Please address and provide further clarifications.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors study dataset classification difficulty via  , find strong correlation with classification error rate of SOTA models, while apply the sample-level classification difficulty as a label mistakenness score to detect noisy labels, finally via relatively sufficent empirical analysis comfirms their mitivation.

### Strengths
1. For analysing dataset classification difficulty, the authors first define a difficulty measure via RERs from AE reconstruction errors and build so-called new analysis theory and  claim the RER is model-agnostic.
2.  Based on the above measure, it can be decomposed to two parts: (1) finite sample size and (2) Bayes error and decision-boundary complexity. 
3. Via a systemic experimental study, the authors find some insightful results, such as strong correlation with classification error rate and mislabel detection.

### Weaknesses
1. the authors claim their theory is model-agnositc, however, actually, dependent on AE model since datasets with different difficulties will more likely result in the same separability, which comes from strong modeling ability of AEs, the latter makes many difficult datasets prone to linear separable, yielding possible unidentifiability! 
2. Based on the above 1, datasets may form some equivalance groups in difficulty measure, for which needing the authors to analysis.
3. From its difinition, RERs seems NOT robust, the authors do NOT clarify it!

### Questions
1. the setting discussed is NOT that practical, the authors assume classes in training are balanced, however, often assuming long-tailed character. while from their discussion, it seems the inputs are clean though labels are noisy, which is too ideal, noisy labels are exactly more likely from unclean inputs such as images.
2. Insufficient analyses for RERs, such as scaling invariance and robustness to noise.
3. Do those representations from different foundation models such as CLIP and DINOv2 you use here have different "difficulty" scores or correlation?  Or are their "difficulties" consistent? for example, samples' or classes's difficulties are order-preserving?
4. At lines 149-150, "decompose the dataset by class and use shallow autoencoders to learn robust representations of these class manifolds" appears NOT to using classification, however, essentially, using class-wise autoencoders to learn representaions corresponding to individual classes has infused class information!  whether could you try to re-determine the difficulty by artificially merging two-classes to one meta-class?
5. when training the c-th encoder using mislabeled x^c (in fact, x^c has ground-truth class c'), the encoder will be brittle to the noisy sample!, but the mislabeled x^c  may still have small reconstructed error, naturally yielding misleading error!

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces a dataset classification difficulty analyzing approach using reconstruction error ratios (RERs) derived from autoencoders trained on individual classes. The study shows that RER-based difficulty metrics strongly correlate with state-of-the-art (SOTA) classification model error rates, which could be regarded as a probe for mislabeled detection tasks.

### Strengths
This paper starts an early attempt to leverage the prior knowledge of foundation models for classification difficulty analysis.

### Weaknesses
One major concern is that the writing and structure of this paper require careful improvement and reorganization. In the current version, numerous details are insufficiently introduced, which may impede understanding of the motivations and methods. For instance, in Fig. 1, the authors do not clearly define 'in-class' and 'out-of-class,' explain how $R^2$ is calculated, or discuss its implications. Additionally, the definitions of 'easiest,' 'median,' and 'hardest' class are unclear.

Another critical weakness is the limited contribution of this paper. It appears to mainly propose a new metric (Eq. 3) without designing a novel algorithm. As illustrated in Fig. 6 and Fig. 10, the performance of the proposed RER-based method is not particularly promising.

### Questions
Please refer to the Weakness.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a novel approach for analyzing existing datasets by breaking down complex multi-class classification problems into class-wise reconstruction tasks. The proposed method shows strong performance in terms of interpretability, generality, and efficiency with some interesting observations.

### Strengths
1. The research topic is highly important and intriguing, especially in this data-centric era where data quality is more crucial than ever.
2. All the experiments and observations are fundamentally new and interesting.
3. The proposed method is simple but very intuitive. To borrow idea from ood detection is interesting.

### Weaknesses
#### Major problems
1. Although the observation and estimated rational function in Section 4.2 are informative, no further analysis of the dataset is provided. I'm curious whether the results in Figure 4 are based on a simple simulation or if there is some underlying rationale. Specifically, the paper lacks a discussion on how the number of samples per class affects the reconstruction error ratio and the fitted curve. It's unclear if the observed relationship holds across different dataset characteristics such as class imbalance, feature dimensionality, and data complexity. The paper should also explore the sensitivity of the fitted parameters to these factors.
2. More detailed comparisons with existing method on quality assessment method should be included. The paper should provide a more thorough comparison with existing dataset quality assessment methods, detailing their computational complexity, sensitivity to different types of data corruption, and performance on a wider range of datasets. The current comparison is insufficient to demonstrate the superiority or even the competitiveness of the proposed method.
3. Some minor issues like grammar mistakes, spelling problems and wrong word order in the sentence make the reading a bit difficult.
4. Further discussions on applying the proposed method are needed. While classification is important, dataset quality assessment should encompass a wider range of research areas. The paper should discuss how the proposed method could be adapted or extended to other tasks such as object detection, segmentation, or even non-visual data analysis. The current focus on classification limits the impact and applicability of the method.

#### Minor issues
1. Missing word in line 85-86: "has long been challenge a in machine learning"
2. Grammar mistakes in line 46: "how well a new sample is reconstructed the shallow model"
3. Confusing expression in line 157-158: "which helps the very compact models learn the local and global structure of each class manifold"

### Questions
Some vague notations or conclusions: In lines 263-266, the authors claim that ViT-based features strongly predict classification dataset difficulty, whereas pretrained ResNet-style models are only weakly correlated. Further analysis would be interesting and important, as the choice of pretrained models is crucial for subsequent data assessment.

### Soundness
4

### Presentation
2

### Contribution
4
