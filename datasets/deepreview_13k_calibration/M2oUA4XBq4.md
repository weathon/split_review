# Learning to ignore: Single Source Domain Generalization via Oracle Regularization

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 5, 3, 3

## Abstract
Machine learning frequently suffers from the discrepancy in data distribution, commonly known as domain shift. Single-source Domain Generalization (sDG) is a task designed to simulate domain shift artificially, in order to train a model that can generalize well to multiple unseen target domains from a single source domain. A popular approach is to learn robustness via the alignment of augmented samples. However, prior works frequently overlooked what is learned from such alignment. In this paper, we study the effectiveness of augmentation-based sDG methods by analyzing the data generating process. We highlight issues in using augmentation for OOD generalization, namely, the distinction between domain invariance and augmentation invariance. To alleviate these issues, we introduce a novel regularization method that leverages pretrained models to guide the learning process via a feature-level regularization of mutual information, which we name PROF (Progressive mutual information Regularization for Online distillation of Frozen oracles). PROF can be applied to conventional augmentation-based methods to moderate the stochasticity of models repeatedly trained on augmented data. We show that PROF stabilizes the learning process for sDG.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies Single Source Domain Generalization where the models are only allowed to train on images from a single source and should generalize to other domains. The authors highlight some issues and failure modes with prior works based on augment-and-align, and introduce a feature-level regularization method via distillation to improve outcomes.

### Strengths
The paper attempts to improve performance on a relevant problem – single-domain generalization. Presumably, methods that work well here will give deeper insight into feature learning & generalization.

### Weaknesses
The paper studies Single Source Domain Generalization where the models are only allowed to train on images from a single source and should generalize to other domains. The authors highlight some issues and failure modes with prior works based on augment-and-align, and introduce a feature-level regularization method via distillation to improve outcomes.

 2 fair

 1 poor

 1 poor

The paper attempts to improve performance on a relevant problem – single-domain generalization. Presumably, methods that work well here will give deeper insight into feature learning & generalization.

The combination of a) a complex, not clearly motivated solution, b) lack of clarity on key contributions and empirical evidence to back this up (lesion analysis), c) overall weak results make this paper fall a bit short of the mark.

* Clarity: Although the authors seems to have put a lot of effort in explaining different components being used in the method, I believe there is a lot of scope of improvement.
    * Currently, it’s very difficult to follow and understand what, precisely, is the problem being solved, why we should care, and what is the exact novel idea being contributed. Sections 2 & 3 introduce a number of concepts (causal graphs, augmentation, training dynamics, distillation, etc., all from previous work, but do not really help clarify e.g., why these observations should form the logical starting point of a system for single source domain generalization.
    * Figure 2 illustrates the system which has a surprisingly large number of components – ensembling of generators, augmentation schemes, distillation from an oracle, an oracle regularizer, again many being adapted from previous works. There’s also the use of a Multi-domain alignment loss. It’s not clear why this specific combination of components is useful, which ones are new, and how/why these pieces work together. 

* Results: 

    * The results are mixed at best, with e.g., table 2 “Ours” not being any better than metaCNN on any column (but bolded in multiple places incorrectly), table 3 being quite variable too, and table4 having no baseline comparisons.
    * Lacking explanations: Although authors motivate the paper by claiming that PROF is better than augment-and-align as it reduces mid-training OOD fluctuations, they fail to explain the failure modes (eg training domain: Cartoon, Target Domain Sketch: 0.70 -> 3.91). More study is required to properly understand when the proposed method becomes unstable.
    * As mentioned in the paper, the proposal of using oracle model to minimize mutual information with it is not novel and is already proposed in MIRO[1], so it would make sense to directly compare against it.

### Questions
please see above.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors suggest that conventional augmentation-based single source domain generalization methods cannot effectively handle large domain shift scenarios. They study this phenomenon from the point of view of S-C disentanglement and propose a novel augmentation-based sDG baseline, MDAR. Besides, they introduce an oracle regularizer, PROF, which utilizes an oracle model and knowledge distillation method to solve this problem. Experiments on several DG benchmarks verified the severe OOD performance fluctuations.

### Strengths
- The paper is well-organized.
    
- The related work and the background knowledge are comprehensive and overall complete.
    
- Discussions and questions about the quality of data augmentation and the effects of alignment are insightful.

### Weaknesses
 - There are some presentations that could be more precise. Please refer to the Questions.
    
- The novelty of this article is limited. The proposed network components and corresponding losses are a little redundant. Lack of discussion of the necessity for each component.
    
- The experimental results, compared with some SOTA performances, are not very convincing.

### Questions
- Presentations:
    
    - In the abstract, it is mentioned “analyzing the data generating process“. But, I did not find any explicit explanations in the main paper.
        
    - Is there any formal explanation or computational and mathematical definition of mid-train fluctuations?
        
    - For “Learning to ignore” under section 3, there are some incomplete phrases. Besides, a clearer explanation of why a less severe mid-train fluctuation means a better capture of domain invariant features should be added.
        
- Experiments:
    
    - The experimental results and the analysis mention that the proposed PROF regularizer only performs well under some large domain shift scenarios. Will this limit the application and the contribution of the proposed method?
        
    - What is the difference or the benefit of the proposed baseline MDAR, compared with other augment and align methods?
        
    - As the PROF aims to guide the task model to learn more domain-invariant knowledge from the oracle model, I think a study of different oracle models’ influence is necessary.
        
    - While measuring the mid-train fluctuations, are the results an average of multiple experiments or a single experiment? Is it statistically significant?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper critiques augmentation-based Single-source Domain Generalization (sDG) methods, emphasizing the distinction between domain and augmentation invariance. To tackle this, this work leverages pre-trained models for mutual information regularization.

### Strengths
- The paper takes a deep dive into augmentation-based sDG methods and highlights existing challenges. Analyzing the data-generating process and the distinction between domain invariance and augmentation invariance provides insights.
-  The introduction of the PROF method for feature-level regularization of mutual information leads to improvements over several benchmark datasets.

### Weaknesses
 - The use of pre-trained models for "oracle" regularization in the domain generalization context is not entirely novel, as evidenced by prior works such as [1]. From a technical standpoint, the advancements proposed here appear to be incremental.

- While the critique of sDG methods and the subsequent motivation for the proposed method is commendable, mere verbal analysis falls short of expectations. There appears to be a void in terms of rigorous theoretical groundwork. Specifically, the paper lacks a deep theoretical analysis, such as the provision of a generalization bound, that sheds light on the functioning and merits of PROF.

### Questions
See weakness.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper presents a method called Progressive mutual information Regularization for Online distillation of Frozen oracles (PROF) for addressing single-source Domain Generalization (sDG) under large style domain shifts. A popular approach is to learn robustness via the alignment of augmented samples. However, prior works frequently overlooked what is learned from such alignment. To address this, the authors introduce PROF, a novel regularization method that leverages pretrained models (oracles) to guide the learning process via a feature-level regularization of mutual information. The authors also present an alignment objective, Multi-Domain Alignment with Redundancy Reduction (MDAR), that serves as a strong sDG baseline. The paper is focusing on style domain shifts (but not others).

### Strengths
1. The paper tackles an essential research problem of single-source Domain Generalization for style domain shift, a topic still awaiting further exploration.

2. The overall organization of the paper is relatively clear. However, the method description section is not well-organized (see weaknesses).

### Weaknesses
1. Organization and Clarity in Section 4.

The method description in Section 4 is not reader-friendly. Generally, when a final loss function consists of multiple loss terms, it's more intuitive to first introduce each term separately, explaining their purpose and how they interact, before presenting them as a sum. However, in this section, the authors introduce the summation of loss items before elaborating on each term, which may confuse readers. In particular, The term L_{cls} in equation (2) is not introduced anywhere either in words or in maths before equation (2), and only clarified in Section 4.3. This organization makes understanding the method unnecessarily difficult and time-consuming, even for readers familiar with single-source DG methods like me. Additionally, the symbol "D" is used to represent different concepts in Sections 3 and 4.

2. Incomplete Reference to Related Works and Baselines.

 There are numerous regularization-based strategies for DG in the literature that haven't been addressed in this paper. For example, Probability matching is employed in ReLIC [1] and AugMix [2]; logit matching is used in CoRE [3]; and feature matching is deployed in MatchDG [4]. However, these works are neither discussed nor evaluated in the paper.

[1] Jovana Mitrovic, Brian McWilliams, Jacob C Walker, Lars Holger Buesing, and Charles Blundell. Representation learning via invariant causal mechanisms. In ICLR, 2021.

[2] Dan Hendrycks, Norman Mu, Ekin D. Cubuk, Barret Zoph, Justin Gilmer, and Balaji Lakshminarayanan. AugMix: A simple data processing method to improve robustness and uncertainty. Proceedings of the International Conference on Learning Representations (ICLR), 2020.

[3] Christina Heinze-Deml and Nicolai Meinshausen. Conditional variance penalties and domain shift robustness. Machine Learning, 110(2):303–348, 2021.

[4] Divyat Mahajan, Shruti Tople, and Amit Sharma. Domain generalization using causal matching. In International Conference on Machine Learning, pp. 7313–7324. PMLR, 2021.

3. Lack of Comprehensive Ablation Study.

The loss function of the task model, as presented in equation (2), comprises several loss terms, each containing multiple sub-components. Without a thorough ablation study, it's challenging to understand the contribution of each sub-component towards the overall DG performance or to verify that the combination proposed by the authors is indeed the most effective.

Specific questions that arise from this include, but are not limited to:

- What would the results be if the last two terms in equation (2) were removed, i.e., simply using the examples generated by the generator alongside the original examples in ERM training?
- How does the oracle model alone perform on the DG task? Given that the oracle model is trained on a much larger dataset, it may already see images in varying styles. Is the DG performance improvement in PROF mainly due to domain leakage from the oracle model?
- How crucial are D and P, and the Barlow Twins in equations (3) and (5)? What would the results look like if simple feature matching/logit matching/probability matching were used instead?
- What would be the impact of using a different number of augmented views in equation (5)?
- Could the authors provide more rationale behind the current generator's design? Is there a specific reason it must be designed this way? How would the results be affected if a different generator was used?

These questions highlight the need for a more detailed ablation study to fully understand and validate the proposed method. Without such an analysis, it's reasonable to question the necessity of each component and specific design. 

4. The performance of the proposed method in the dataset with style shift in the more real-world scenario, such as the FMoW-WILDS and Camelyon-WILDS (https://wilds.stanford.edu/) is unknown. 

In summary, the unclear method description, the absence of several related works and baselines, and the lack of a comprehensive ablation study led me to lean toward rejecting this paper. However, I am open to further discussion and may reconsider my decision based on the authors' responses.

### Questions
See weaknesses above.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
