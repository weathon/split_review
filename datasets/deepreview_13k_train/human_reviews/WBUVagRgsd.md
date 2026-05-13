# Salvage: Shapley-distribution Approximation Learning Via Attribution Guided Exploration for Explainable Image Classification

- Decision: Accept
- Scores: 6, 6, 6, 8

## Abstract
The integration of deep learning into critical vision application areas has given rise to a necessity for techniques that can explain the rationale behind predictions. In this paper, we address this need by introducing Salvage, a novel removal-based explainability method for image classification. Our approach involves training an explainer model that learns the prediction distribution of the classifier on masked images. We first introduce the concept of Shapley-distributions, which offers a more accurate approximation of classification probability distributions than existing methods. Furthermore, we address the issue of unbalanced important and unimportant features. In such settings, naive uniform sampling of feature subsets often results in a highly unbalanced ratio of samples with high and low prediction likelihoods, which can hinder effective learning. To mitigate this, we propose an informed sampling strategy that leverages approximated feature importance scores, thereby reducing imbalance and facilitating the estimation of underrepresented features. After incorporating these two principles into our method, we conducted an extensive analysis on the ImageNette, MURA, WBC, and Pet datasets. The results show that Salvage outperforms various baseline explainability methods, including attention-, gradient-, and removal-based approaches, both qualitatively and quantitatively. Furthermore, we demonstrate that our explainer model can serve as a fully explainable classifier without a major decrease in classification performance, paving the way for fully explainable image classification.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors highlight the shortcomings of existing methods for existing Shapley-based explainers and propose a method called Salvage, which effectively learns and samples based on the Shapley value distribution.

### Strengths
1) The issues identified with existing methods appear valid and relevant.
2) The authors demonstrate an improvement in explanation accuracy compared to existing methods across various datasets.

### Weaknesses
1) The explainer model is essentially an estimation model for interpreting the behavior of the target classification model; however, this paper does not clearly define what the target model is. Furthermore, there is insufficient evidence to show that the method operates effectively across different target models. The authors should specify the exact architecture and parameters of the target model used in the experiments. It is crucial to test the method's robustness across diverse model architectures, not just different datasets, to ensure its general applicability.
2) Some results seem incomplete, as suggested by Figure 1. The qualitative examples should include all baseline methods to provide a comprehensive comparison. The absence of certain methods in the main text gives the impression of a selective presentation of results.
3) The ablation study is lacking. While the proposed method focuses on effectively learning the distribution and sampling, there is no analysis of which aspect is more critical to the overall success of the method. The authors need to provide a more granular analysis of the individual contributions of the distribution learning and informative sampling components.
4) The problems identified with existing methods are described conceptually but lack empirical validation. The claims about the limitations of MSE-based approximations and the imbalance of prediction likelihood with uniform sampling should be supported by more concrete experimental evidence.

### Questions
1) What exactly does Figure 3 illustrate?
2) Since the goal is to derive an explainer model for a specific classification model, I am curious not only about the classification performance but also about how well the predictions align with those of the existing classification model (as seen in Table 2).

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
This paper introduces a novel explainability method for image classification known as Salvage. The paper employs a removal-based technique coupled with the concept of Shapley-distributions. These techniques are used to train an explainer model that learns the prediction distribution of the classifier on masked images. The authors address the imbalance between important and unimportant features by devising an informed sampling strategy. This strategy facilitates better approximation of the classifier’s distribution and helps the estimation of underrepresented features. The effectiveness of Salvage is validated through experiments on the ImageNette, MURA, and Pet datasets. The study illustrates that Salvage outdoes various baseline explainability methods and can additionally be used as a fully explainable classifier without a considerable fall in classification performance. The paper concludes by pointing out future optimizations and improvement possibilities for Salvage.

### Strengths
The paper presents "Salvage," a novel removal-based explainability method for image classification that tackles unbalanced important features via an informed sampling strategy. The invention of Shapley-distributions for a more accurate approximation of classification probability distributions is impressive. The paper's comprehensive and clear presentation, alongside robust experimental evaluation, underlines the method's potential for explainable classification, with comparable accuracy to standard classifiers.

### Weaknesses
1. Although the paper demonstrates a performance comparison with a couple of explainability methods like ViT-Shapley and RISE, more extensive comparison with a wider array of contemporary removal-based explainability methods could provide a more robust evaluation of the Salvage algorithm's efficacy. Specifically, the paper could benefit from comparisons with methods that employ different masking strategies or those that use iterative removal processes, which might reveal the limitations of the current approach under different conditions.

2. It would be beneficial to see Salvage's performance with other types of data or in other domains, beyond the ones mentioned in the paper (ImageNette, MURA, and Pet datasets). This would help in evaluating the broad applicability and versatility of the approach. For instance, evaluating performance on datasets with higher image complexity or different modalities (e.g., medical imaging with different contrasts, satellite imagery, or even non-image data) would provide a more comprehensive understanding of the method's strengths and weaknesses.

3. The impacts of temperature parameter changes in the softmax or sigmoid functions during the approximation of the classifier’s distribution could have been explored in more depth. More extensive experimental study in this aspect could enhance the robustness of Salvage. The paper should investigate how different temperature values affect the sharpness of the probability distributions and, consequently, the quality of the explanations. This analysis should also consider the computational cost associated with tuning these parameters.

### Questions
1. Could you please elaborate more on why the informative sampling's improvement in performance is less noticeable in the Pet dataset compared to the other datasets?
2. How would different neural architecture designs for the explainer model impact the performance of Salvage?
3. Given that the model has been tested on a limited number of datasets, have you considered testing Salvage on a wider array of datasets, particularly more complex or diverse ones, to evaluate its broad applicability?

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
This paper introduces Salvage,a removal-based explainability method for image classification. It includes a concept of Shapley-distributions,which offers a more accurate approximation of classification probability distributions and an informed sampling strategy that leverages approximated feature importance scores to reduce imbalance and facilitate the estimation of underrepresented features.

### Strengths
1. A  new concept of Shapley-distributions,which offers a
 more accurate approximation of classification probability distributions, is introduced.
2. The comparison methods, datasets, and metrics are quite comprehensive. On some metrics, it has a clear advantage.

### Weaknesses
 **The presentation should be improved a lot.**

1. The explanation of symbols in the formulas is not clear enough, causing difficulty in understanding, such as Eq.2. Specifically, the meaning of  'p_w(S) ∝ w_S' is not immediately obvious and requires a more detailed explanation. The relationship between the weighting factor 'w_S' and the sampling distribution 'p_w(S)' needs to be explicitly defined. It's unclear how this proportional relationship translates into a concrete sampling procedure. A more rigorous definition of the sampling process is needed to ensure reproducibility and understanding.
2. In Table 1, there are several obvious typographical errors of the experimental results, for example “68,56”. It should be “68.56”. These errors undermine the credibility of the presented results and suggest a lack of attention to detail in the experimental reporting.
3. The bottom line of the Table 2 is not drawn!

**Soundness**
1. There is no theoretical  proof or experimental results can demonstrate that the INFORMATIVE SAMPLING has improved efficiency. The claim that informative sampling improves efficiency is not substantiated by any empirical evidence or theoretical analysis. It is unclear how the proposed sampling strategy leads to faster convergence or better performance compared to a uniform sampling strategy. A quantitative comparison of the performance with and without informative sampling is necessary to support this claim.
2. In Table 2, on PET, in terms of RRA, Salvage underperforms about 3 point compared with SOTA. There should be appropriate analysis and discussion regarding this. The paper lacks a thorough discussion of why Salvage underperforms on the RRA metric for the PET dataset. A detailed analysis of the potential reasons for this discrepancy is needed, including a comparison of the attribution maps generated by Salvage and the SOTA method. This analysis should consider the specific characteristics of the PET dataset that might contribute to this performance difference.
3. Only make ablation study on INFORMATIVE SAMPLING.

### Questions
1.How is the experimental performance when using SHAPLEY DISTRIBUTION ESTIMATION alone?

2. Is this method applicable to other types of tasks (such as object detection or segmentation)?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This article proposes a new explainability method for image classification. Most of the explainability methods target CNNs; instead, Salvage, the proposed method is architecture agnostic. Salvage is a removal-based approach based on ViT-Shapely with further improvements. The method surpasses the current SOTA.

### Strengths
The paper is clear and well-explained. The methodology is adequate. The method is well evaluated. The method, despite not being completely novel, builds on SOTA methods (ViT Shapely) and improves their shortcomings.

### Weaknesses
The method is incremental with respect to ViT-Shapely but better. So no much concern.

### Questions
I find the paper good as is.

### Soundness
4

### Presentation
3

### Contribution
3
