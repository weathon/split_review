# Temporal Test-Time Adaptation with State-Space Models

- Decision: Reject
- Avg Score: 4.50
- Scores: 6, 3, 3, 6

## Abstract
Distribution shifts between training and test data are inevitable over the lifecycle of a deployed model, leading to performance decay. Adapting a model on test samples can help mitigate this drop in performance. However, most test-time adaptation methods have focused on synthetic corruption shifts, leaving a variety of distribution shifts underexplored. In this paper, we focus on distribution shifts that evolve gradually over time, which are common in the wild but challenging for existing methods, as we show. To address this, we propose STAD, a probabilistic state-space model that adapts a deployed model to temporal distribution shifts by learning the time-varying dynamics in the last set of hidden features. Without requiring labels, our model infers time-evolving class prototypes that act as a dynamic classification head. Through experiments on real-world temporal distribution shifts, we show that our method excels in handling small batch sizes and label shift.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper studied test-time adaptation, a setting where model parameters are updated based on incoming test features. It proposes STAD, a method to track gradual distribution shifts which only updates the last layer in a given network, based on the EM algorithm. The authors report results on several tasks.

### Strengths
The paper is well-written and gives a principled justification for the proposed method. It considers real-world shifts and the proposed method seems to outperform the baselines generally.

### Weaknesses
The paper does not appear to have any major weaknesses, but I am curious about the importance of the subfield (temporal test-time adaptation). Why is this the right setting to study (as opposed to others for distribution shift) and how does it compare to methods involving periodic retraining and unsupervised domain adaptation?

LIne 37 - why can't test-time training operate in this paradigm? what is the precise difference between TTA and TTT?
46 - Doesn't FMoW have labels? Why is this dataset suitable for the proposed setting, which claims that one of its benefits is not needing labels?
192 - missing a comma inside the parentheses?

How important is the linear Gaussian transition model assumption? Could your method make use of labels if they were made available?

### Questions
LIne 37 - why can't test-time training operate in this paradigm? what is the precise difference between TTA and TTT?
46 - Doesn't FMoW have labels? Why is this dataset suitable for the proposed setting, which claims that one of its benefits is not needing labels?
192 - missing a comma inside the parentheses?

How important is the linear Gaussian transition model assumption? Could your method make use of labels if they were made available?

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
4

### Summary
This paper introduces a novel Test-Time Adaptation (TTA) method, STAD, which leverages a state-space model to learn time-evolving feature distributions. It also proposes a new TTA setting that is more reflective of real-world scenarios.

### Strengths
1. The authors propose a realistic TTA setting and conduct extensive experiments across multiple datasets to validate the method's effectiveness.
2. A new TTA method, STAD, is introduced, combining state-space models with a solid theoretical foundation.

### Weaknesses
1. The method modifies and updates only the linear classifier, raising concerns about effectively handling covariate shifts. As shown in Table 4, adapting only the classifier on CIFAR-10C performs significantly worse than adapting the feature extractor. 

2. Experimentally, while a realistic TTA setting is proposed, comparisons with other similar settings and related methods are lacking. For instance, the following related works are not adequately compared:

   1. UniTTA: Unified Benchmark and Versatile Framework Towards Realistic Test-Time Adaptation. arXiv 2024.
   2. Towards real-world test-time adaptation: Tri-net self-training with balanced normalization. AAAI 2024.
   3. Robust test-time adaptation in dynamic scenarios. CVPR 2023.
   4. Universal Test-Time Adaptation Through Weight Ensembling, Diversity Weighting, and Prior Correction. WACV 2024.

   Additionally, only a small portion of common TTA datasets (CIFAR-C, ImageNet-C) are addressed, with limited focus on CIFAR-10C.

### Questions
See the weaknesses section.

### Soundness
1

### Presentation
2

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
This paper addresses the test-time adaptation problem under gradual distribution shifts. The proposed method models the gradual distribution shift in the representation space using linear state-space models, implemented through the von Mises-Fisher distribution. Experimental results on multiple real-world datasets demonstrate the effectiveness of the proposed algorithm.

### Strengths
This work conducts experiments on several real-world datasets, enhancing the practical applicability of TTA algorithms in real-world settings.

By modeling gradual distribution shifts using linear state-space models, this work provides fresh insights in the field of TTA.

### Weaknesses
The paper lacks discussion and empirical comparisons with related work, particularly in the field of gradual unsupervised domain adaptation, which addresses very similar problems (e.g., [1, 2]). As a result, the contribution of this paper may be overstated.

The gradual shift assumption represents a relatively simple form of distribution shift in dynamic environments, as its total variation is small. This simplicity limits the contribution of the work.

The proposed method appears to combine existing approaches, which limits its technical novelty.

### Questions
How does the proposed method compare to self-training algorithms, e.g., Ref [1], on real-world tasks?

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
4

### Summary
This paper proposes a method STAD designed to adapt a model’s classification head during inference to handle temporal distribution shifts, which are underexplored. The paper focuses on test-time adaptation, proposing to track the evolution of hidden features using SSMs. STAD dynamically updates class prototypes to reflect the evolving data distribution. Extensive experiments demonstrate that STAD performs well in temporal distribution shifts, label shifts, and small batch size settings. The paper evaluates its approach on several real-world datasets, showing robustness and performance gains compared to baseline methods.

### Strengths
1. The paper is generally well-written with clear explanations of both the problem and the proposed solution.
2. The authors provide a strong theoretical foundation for the use of probabilistic SSMs to address temporal test-time adaptation, with detailed mathematical formulations of the dynamics model.
3. The empirical analysis is comprehensive, with evaluations on multiple datasets, including both real-world temporal shifts and synthetic corruption shifts.

### Weaknesses
1. The paper does not clearly describe the sensitivity of STAD to hyperparameters which could impact the method’s robustness.
2. While STAD adapts the last layer to changing distributions, the reliance on class prototypes could be problematic when distributions are overfitted to the target domains and cause catastrophic forgetting. The method's reliance on updating class prototypes based on potentially noisy or biased target data could lead to the model drifting away from the source domain's knowledge, especially if the target data distribution is significantly different or contains outliers. This could result in a form of catastrophic forgetting where the model's performance on the original source domain degrades after adaptation.
3. The gradual distribution shift assumption is pretty strong especially during test time, which undermines the significance of the method. For example, ATTA [1] also targets distribution shifts during test time, which also includes some similar distribution shifts constrains. Given these constrains, they reason that a few labeled data is necessary to make the setting reasonable in real world scenarios. As what I believe, the gradual distribution shift assumption is a major limitation of this work. While it may be hard to make this method work perfectly on non-trivial domain shift datasets such as PACS and VLCS, there are two important experiments to do. (1)  Building boundaries on the ability limitations and applicability of this work on non-trivial domain shift datasets. (2) Validating that it is **not necessary** to use labels in the gradual shift setting by showing that STAD's performance is similar to the methods using labels (as Oracle), such as active online learning and ATTA.

### Questions
How can we quantify the gradual distribution shifts?

### Soundness
3

### Presentation
3

### Contribution
2
