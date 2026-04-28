# Concept Bottleneck Models under Label Noise

- Decision: Reject
- Avg Score: 3.75
- Scores: 3, 6, 3, 3

## Abstract
Concept bottleneck models (CBMs) are a class of interpretable neural network models that make the final predictions based on intermediate representations known as concepts. With these concepts being human-interpretable, CBMs enable one to better understand the decisions made by neural networks. Despite this advantage, we find that CBMs face a critical limitation: they require additional labeling efforts for concept annotation, which can easily increase the risk of mislabeling, i.e., CBMs need to be trained with noisy labels. In this work, we systematically investigate the impact of label noise on CBMs, demonstrating that it can significantly compromise both model performance and interpretability. Specifically, we measure the impact of varying levels of label noise across different training schemes, through diverse lenses including extensive numerical evaluations, feature visualizations, and in-depth analysis of individual concepts, identifying key factors contributing to the breakdowns and establishing a better understanding of underlying challenges. To mitigate these issues, we propose leveraging a robust optimization technique called sharpness-aware minimization (SAM). By improving the quality of intermediate concept predictions, SAM enhances both the subsequent concept-level interpretability and final target prediction performance.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The submission empirically investigates the effect of injecting label noise in concept bottleneck models for image classification. These models require two types of labels: class labels and concept labels. The effect is evaluated in three training regimes: training the concept predictor and the classifier separately, training them in sequence, and training them jointly. The results on two image classification datasets show that increasing label noise decreases classification accuracy. The effect is smallest for joint training. However, concept prediction accuracy is severely affected in joint training. The submission also shows that sharpness-aware minimization can be used to ameliorate accuracy. Auxiliary results are given for two variants of concept bottleneck models, structured noise, and different network architectures. These support the findings regarding the effects on classification accuracy.

### Strengths
The submission provides an extensive set of results investigating the effect of label noise on concept bottleneck models.

Prior literature does not appear to have investigated the effect of label noise on the accuracy of concept prediction.

The finding that joint training maintains classification accuracy best while incurring a large drop in concept prediction accuracy is interesting.

### Weaknesses
It is unsurprising that injecting label noise reduces predictive performance, and it is known that sharpness-aware minimization improves performance when label noise is present. 

The findings are purely empirical, and it is unclear how representative the noise models used in the paper are for the types of noise that occur in real-world settings. Specifically, the symmetric noise model, while common, may not capture the nuanced correlations present in real-world label errors. The pairwise noise model is a step in the right direction, but it's unclear if the specific dependencies it introduces are realistic or if they are simply a convenient way to generate asymmetric noise. Further, the magnitude of noise applied in the experiments might not reflect real-world scenarios, where noise levels can vary significantly and may not be uniformly distributed across classes.

The classifier considered in the submission is a linear one, and it is unclear how the results are affected by the fact that this classifier is relatively insensitive to noise. This choice of a linear classifier might mask the true impact of label noise on the learned representations, as non-linear classifiers are known to be more susceptible to overfitting noisy data. It is possible that the observed robustness to target noise is an artifact of the linear classifier's simplicity, rather than an inherent property of the concept bottleneck model itself. The paper should investigate the sensitivity of the results to the choice of classifier, especially given that the goal is to understand the effect of noise on the learned representations.

There is a section on label smoothing in the appendix. Label smoothing is not referred to in the main text.

A couple of other small issues:

"need to be trained with noisy labels" - rephrase

Multiple duplicate references in the bibliography.

### Questions
N/A

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
The paper is concerned with inherently interpretable models called Concept Bottleneck Models (CBMs). These models require extensive concept labeling; however, these labels are usually assumed to be perfect. The paper explores how noise in these concept labels affects the final target prediction. The authors perform extensive experiments across all three variants of CBMs to show the detrimental effects of concept labels. The authors then proposed SAM training to improve concept and target accuracy.

### Strengths
- Label noise and mislabeling are well-motivated problems, especially from a CBM perspective. No work has explicitly examined this problem.

- The paper structure is very intuitive and easy to read.

- The authors showed the degradation due to label noise well with comprehensive experiments.

### Weaknesses
 - While the experiments are comprehensive for Section 3 and 4. Some of the results are pushed to the appendix (which is fine), however it would have been nice to summarise them in brief in the text.

- I enjoyed reading up to Section 4. Thank you. However, I would have appreciated some theoretical intuition on why SAM works better (unless I missed it).

- The paper performs experiments with CUB and AwA2 datasets, popular benchmark datasets for CBMs. These datasets however have a strong correlation between concept labels and the target label. I can imagine label noise to be very detrimental (as observed from Figure 2).  The potential observed effect due to label noise might be weaker in the case of diverse concepts for each target.

- The paper claims to be first the paper to looking at label noise in CBMs, while I would not refute this, I would like to point out the authors to some very relevant papers - [1] (noise added to concept labels, similar to some of the exps in Sec3) [2]-(concept robustness and adv attacks)

[1] - Sheth, Ivaxi, and Samira Ebrahimi Kahou. "Auxiliary losses for learning generalizable concept-based models." Advances in Neural Information Processing Systems 36 (2024).

[2] - Sinha, Sanchit, et al. "Understanding and enhancing robustness of concept-based models." Proceedings of the AAAI Conference on Artificial Intelligence. Vol. 37. No. 12. 2023.

### Questions
- In Sec 6.1 authors show that other CBM variants are also susceptible to label noise. This alings with CBMs, however the obvious question for me is, does SAM training improve the robustness? Why or Why not?

- Concept labeling CBMs is very difficult, there is an increasing interest in using LLMs for concept annotation. Can the authors kindly comment (maybe in Limitations section of the paper), on whether label noise will impact such concept labels. 

- Interventions are useful aspect of CBMs. What is the impact of interventions to reduce label noise? I assume interventions may be less effective. Does SAM improve it? 


Minor:

- Line 101, now caps for "We".

- Figure 3, which model is used not specified? Joint/Ind/Seq?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper has a clear motivation to investigate and demonstrate the severity of detrimental effects caused by label noise of different levels, specifically examining how label noise compromises the performance of CBM. Specifically, the paper utilizes SAM to mitigate these impacts. Empirical results show that SAM has the potential to significantly enhance the robustness of CBM, compared to SGD.

### Strengths
- This paper has a clear motivation focused on the robustness under conditions with label noise.
- From an overall view, this paper is easy to follow and the idea of using SAM is reasonable.
- It provides detailed insights into the underlying causes of decreased prediction accuracy, both for intermediate concepts and final targets, contributing to a deeper understanding of the effects of label noise.

### Weaknesses
 - Although the paper details the impact and offers an in-depth analysis of label noise, the methodology could be strengthened. The use of SAM, which is borrowed from prior works, is the sole approach for enhancing robustness.
- The emphasis on label noise impact might be overstated, especially as noise levels are extended to 40%, which is unconventional for real-world scenarios. Natural label noise is already present in datasets like CUB and AWA2.
- The proposed method's improvement over joint CBM is relatively incremental, even under high noise levels, which may limit the perceived effectiveness of SAM.
- In Table 1, the concept prediction accuracy is only 92.4% for joint CBM when the noise level is 0%, which does not correspond to 96.9% reported in the vanilla CBM literature, despite using the same Inception-V3 backbone. What might account for this discrepancy?
- This paper lacks an alternative type of literature such as [1] that generates concepts using LLM/VLM. This category is highly relevant to the label noise setting.
- The vanilla CBM is the only baseline and more baselines should be considered to validate the effectiveness.
- The authors discuss the impacts on interpretability by evaluating concept prediction accuracy. However, these two definitions are not strictly synonymous.

### Questions
- In Fig. 7, I noticed a sharp drop in target validation accuracy for the SGD training methods after a certain number of iterations, yet the target validation accuracy appears to stabilize overall. Could you provide an explanation for this observation?
- Also, for figure-7-b, why are the performance of SGD and SAM almost the same?

### Soundness
2

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
4

### Summary
The article investigates concept bottleneck models as regards their brittleness to label noise in the involved concepts. The article shows that this is indeed the case, using different amount of noise and benchmark data sets. It investigates the impact on both, meaningfulness of concepts and accuracy, as well as visualizes this. Then it shows that a technology proposed for mitigating sensitivity to label noise helps (somewhat).

### Strengths
The article investigates a novel and relevant problem which, to my knowledge, has not been targeted yet. The article is extensive w.r.t. evaluation. It proposes a first mitigation.

### Weaknesses
The article is merely experimental and does not provide theoretical insights. It widely ignores previous work on dealing with label noise such as probabilistic treatments, differences of sensitivity based on the cost function etc. (see eg overviews by Ata Kaban and Benoit Frenay). The expertiments are somewhat lengthy with not so much insight. The mediation procedure is only mildly successful.

### Questions
What is the effect of asymmetries of label noise?
Can you investigate different cost functions for training and different other methods?
How does this relate to technologies which do not assume availability of information w.r.t. concepts for all data?
How does the effect relate to aspects of the suitability of concepts?

### Soundness
2

### Presentation
3

### Contribution
2
