# CARPRT: Class-Aware Prompt Reweighting for Pre-Trained Vision-Language Models

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
When using a pre-trained vision-language model (VLM) to classify an image, we often need to use the pre-trained VLM to compute a similarity score between the image and texts containing a semantic label, e.g., “a photo of a cat”, where “a photo of a” is called a prompt and “cat” is the semantic label (a.k.a. a class in classification tasks). The existing studies have shown that the selection of prompts can significantly affect the scoring scheme between a given image and a semantic label, and they proposed a new score via using a weighting vector to reassemble scores regarding different prompts. However, these studies assume that all classes should share the same weighting vector. In this paper, we first empirically show that the existing approach is sub-optimal. We subsequently revisit the existing reweighting strategy from a probabilistic view and find an implicit assumption in prior work: the conditional independence of classes and weights, which often does not hold in practice. To cope with this problem, we propose class-aware prompt reweighting (CARPRT), a strategy designed to adjust the weighting vector for each class. CARPRT calculates the relevance scores for prompt-class pairs with respect to all images, and identifies the maximum score for each prompt-class pair. These maximum scores are then averaged across prompts for each class to estimate the class-specific weighting vectors, ensuring that prompts are optimally reweighted based on class-specific information. Our experiments demonstrate that CARPRT outperforms the existing reweighting strategy under the image classification tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies how to improve the prompting for the CLIP model. The motivation lies in the fact that existing prompting methods ignore the dependence of prompt weights on different classes. The authors first conduct experiments to demonstrate the positive influence of class-specific weights on prediction performance. Then, a class-aware prompt reweighting method CARPRT is proposed. CARPRT calculates the weight matrix based on the relevance scores between images and prompt-class pairs. Experimental results show that CARPRT surpasses ZPE in most cases.

### Strengths
- The motivation is intuitive while reasonable. As far as I know, it is the first work applying the class-aware weighted prompt ensemble.
- The paper is well-written and easy to follow. The authors revisit the existing works, present detailed analyses and explanations, and give clear formulations and an algorithm procedure for the proposed method.
- Extensive experimental results are reported.

### Weaknesses
 - One concern is regarding the computational complexity. Unlike class-wise or prompt-wise reweighting, the proposed method calculates the weight matrix based on two dimensions. Is there any complexity analysis?
- Another concern is regarding the performance gains. It seems that the results in Table 2 showcase marginal improvement compared to ZPE. The performance gains of some datasets in Table 1 are also limited. This may raise concerns regarding the limited contributions to the community.
- I am also concerned with the hyper-parameter sensitivity across different datasets. It seems that the results in Figure 3 are the overall results. However, I am still concerned with the results for each dataset. Are the hyper-parameter settings (e.g. $\tau=3.0$) suitable for all datasets? Considering the generality of the proposed method, I suggest the authors report more detailed results and analyses.

### Questions
See weaknesses.

### Soundness
2

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
3

### Summary
The paper presents CARPRT, a method to automatically choose and assign weights to a given set of standard prompts when used for zero shot image classification. CARPRT specifically addresses the limitation of the current zero-shot method that uses a fixed weighting vector for the given set of prompts for all classes. Instead, it adjusts prompt weights for each class based on image-prompt relevance by leveraging pseudo-labeling. Experiments on multiple benchmarks show that CARPRT improves zero-shot classification accuracy, especially in fine-grained classification tasks.

### Strengths
**Well motivated**: CARPRT effectively demonstrates the need for class-aware weights, showing that a shared weight for prompts for all classescan hinder zero-shot VLM performance.

**Simple, mathematically sound probabilistic framework**: The paper uses an energy-based probabilistic framework to model underlying class distributions for prompt reweighting, enhancing the interpretability of CARPRT’s approach.

**Improvements on Fine-grained datasets**: The method achieves state-of-the-art results on multiple datasets, notably improving accuracy on some fine-grained datasets like EuroSAT and Flowers102.

### Weaknesses
 **W1 Limited Improvement on ImageNet Variants**: The performance gains on datasets like ImageNet-A and ImageNet-R are modest, suggesting that CARPRT’s advantages may be less pronounced on general image datasets compared to fine-grained datasets. The paper lacks a thorough analysis of why the method struggles on these datasets. It would be beneficial to explore whether the limited gains are due to the nature of the ImageNet dataset itself, the quality of the prompts used, or the inherent limitations of the energy-based model for such a broad range of classes. Further testing on other large datasets (e.g. Places 365) would help better evaluate the methods significance for large datasets.

**W2 - Pseudo-Label Accuracy Dependency**: The method depends on accurate pseudo-labels to derive class-specific weights, which can be problematic in scenarios where pseudo-labeling quality is low. The paper does not provide a clear definition of pseudo-label accuracy in the context of multiple prompts predicting different labels for the same image. A more detailed study on how this affects performance, including the impact of noisy pseudo-labels on the final classification accuracy, is needed. It would be beneficial to understand how the method behaves when the pseudo-labels are significantly incorrect, and what are the failure modes of the method in such situations.

### Questions
1. Did you try using models other than Energy based ones to model the underlying class distributions (e.g. GMMs, Local Manifold models) ? It would be interesting to see how/ if the choice makes a difference. 
2. How well does CARPRT work on fine-grained datasets that have class imbalances ? Does using a different weights for each class improve performance here too ?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a category-aware prompt re-weighting (CARPRT) method to improve the performance of pre-trained visual language models (VLMs) on zero-shot image classification tasks. It first finds the limitations of existing prompt re-weighting methods, and explains the root cause from a probabilistic analysis perspective. The proposed CARPRT calculates the relevance scores of prompt-class pairs and determines the optimal prompt weight vector for each class based on these scores. The experimental results show that CARPRT outperforms existing re-weighting strategies on various image classification benchmarks.

### Strengths
1. The proposed CARPRT introduces a class-specific weighting mechanism, significantly improving the alignment of prompts with class-specific information.
2. The paper provides a solid theoretical foundation, addressing the conditional independence limitations in previous methods.
3. By automating the prompt reweighting process, the method reduces dependency on manually crafted prompts.

### Weaknesses
1. The approach introduces additional computational complexity while the improvement is extremely limited (less than 1%) on part of situations. Moreover, only the weighted baselines are compared, I doubt that whether it can enhance existing prompt engineer methods.
2. The effectiveness of CARPRT is tied to the quality and diversity of the prompt template pool, is it effective for learned prompts?

### Questions
see weaknesses

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies class-aware prompt reweighting strategy for vision-langauge models. The idea is that when doing prompt ensembling, using the same weighting vector for all classes overlooks the diverse characteristics of different classes, and may yield suboptimal results. Further, the authors present a probabilistic viewpoint based on Bayes' Theorem to show the conditional independence assumption between the class and weights in the class-shared weighting method. CARPRT is proposed that obtains weight vectors based on the relevance score to prioritize the most relevant prompts for each class. The efficacy of CARPRT is verified using CLIP model over multiple benchmarks.

### Strengths
- This paper studies the important prompt ensembling task. With the popularity of zero-shot image classification with multimodal models such as CLIP, the proposed method/idea can be useful to a wide audience.

- The idea of class-aware prompt weighting is simple, but the authors present a probabilistic viewpoint based on Bayes' theorem to show its advantage over class-independent prompt weighting.

- The final CARPRT method is a simple implementation that adheres to the key principles established in the probabilistic analyses. Over 10 fine-grained datasets and 3 ImageNet variants, it shows an improvement in accuracy over ZPE. Both ViT and ResNet backbones are considered. Hyper-parameter studies are adequate.

- The paper is well-written and easy to follow.

### Weaknesses
- The proposed CARPRT adheres to the key principles established in Section 3, but the detailed correspondences are not explicitly presented. The marginalization in Eq.(6) over $W$ appears to reduce to a point estimation of $W$ for the following analysis. $Pr(W|P)$ is not reflected in the implementation. $Pr(y_c|W,P)$ is approximated by Eq.(9). The final weights $w$ in Eq.(16) seem to be the posterior approximation of Eq.(7), but how to derive these formulations (from Eq.(13) to Eq.(16)) are omitted in the paper. A more rigorous derivation connecting the probabilistic formulations to the practical implementation would strengthen the paper significantly.

- Using class-aware prompt weighting theoretically is better than class-independant prompt weighting, but its robustness is also a practical concern. The authors also mention the influences of pseudo-labels and prompt template pool, but relevant empirical analyses are not provided. For example, how does the accuracy of the pseudo-labels affect the performance of CARPRT compared to ZPE? What is the impact of the diversity and size of the prompt template pool on the performance, especially when dealing with fine-grained datasets? It is stated that templates are combined from different datasets for a particular test dataset, but is this really necessary, and what are the criteria for selecting and combining these templates?

### Questions
- Please clarify the correspondances between CARPRT formulations and probabilistic derivation.

- In Appendix D, the authors discuss several forms of $Pr(W|P)$. Could the authors explain how these priors can be obtained and used, for example, in the Test-Time Adaptation situation mentioned in the paper?

- I am confused about the toy example in Proposition 3. Why all the three (Ln 880-883) have $y_1$ as their variates? How Ln 886-889 are derived?

- In Ln 431, a typo in 'iaccuracy'.

### Soundness
3

### Presentation
3

### Contribution
3
