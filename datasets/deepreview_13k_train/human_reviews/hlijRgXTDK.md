# Pathologies of Out-of-Distribution Detection

- Decision: Reject
- Scores: 3, 5, 6, 5

## Abstract
There is a proliferation of out-of-distribution (OOD) detection methods in deep learning which aim to detect distribution shifts and improve model safety. These methods often rely on supervised learning to train models with in-distribution data and then use the models’ predictive uncertainty or features to identify OOD points. In this paper, we critically re-examine this popular family of OOD detection procedures, revealing deep-seated pathologies. In contrast to prior work, we argue that these procedures are fundamentally answering the wrong question for OOD detection, with no easy fix. Uncertainty-based methods incorrectly conflate high uncertainty with being OOD, and feature-based methods incorrectly conflate far feature-space distance with being OOD. Moreover, there is no reason
to expect a classifier trained only on in-distribution classes to be able to identify OOD points; for example, we should not necessarily expect a cat-dog classifier to be uncertain about the label of an airplane, which may share features with a cat that help distinguish cats from dogs, despite generally appearing nothing alike. We show how these pathologies manifest as irreducible errors in OOD detection and identify common settings where these methods are ineffective. Additionally, interventions to improve OOD detection such as feature-logit hybrid methods, scaling of model and data size, Bayesian (epistemic) uncertainty representation, and outlier exposure also fail to address the fundamental misspecification.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents a critical analysis on prior approaches for out-of-distribution (OOD) detection. The central argument of the paper is that prior approaches cannot detect certain categories of OOD samples, due to limited information regarding OOD samples at test time. The paper demonstrates failure modes for common categories of OOD detection methods such as feature-based, logit-based, and uncertainty-based methods, with concrete empirical evidence and illustrations.

### Strengths
1. The paper is overall well written with clear figures and illustrations.
2. The failure modes for different categories of OOD detection methods are clearly demonstrated with examples.

### Weaknesses
1. **Limited New Insights and Lack of Technical Depth**: The paper falls short in presenting new insights and lacks significant technical depth. For example:

- Section 4.1: The paper states that “no feature-based method can correctly detect these OOD inputs that have indistinguishable features from ID” (L217) and demonstrates this claim with examples. However, this observation is already well-established in the literature and is almost self-evident given the definition of feature-based OOD detection. Instead of demonstrating the existence of OOD samples that share features with ID (which is an expected finding), a deeper analysis of the root causes—such as the training method, model architecture, or the impact of pre-training—would provide more value. For instance, the paper could explore how different regularization techniques during training influence the feature space and the resulting overlap between ID and OOD samples. Furthermore, the analysis could investigate specific architectural choices, such as the depth and width of the network, and their impact on the separability of ID and OOD features.

- Section 4.2: The claim that “OOD examples often have low uncertainty” is supported by an experiment using only LeNet-5 to classify automobiles and trucks from CIFAR-10. The limited scope of this experiment is insufficient to support a generalized conclusion that OOD examples often exhibit low uncertainty. A more rigorous approach would involve testing a diverse set of models, including modern architectures like ResNets and Transformers, across multiple datasets with varying degrees of semantic similarity between ID and OOD samples. Additionally, the paper should analyze the calibration of uncertainty estimates for OOD samples, as low uncertainty may not always correspond to incorrect classification.

- Section 5.6: The failure mode of generative models is demonstrated solely with a simplified two-class Gaussian example and lacks accompanying experiments. The relevance of this simple demonstration to recent advancements in generative models remains unclear. A more comprehensive analysis should include experiments with modern generative models, such as diffusion models or normalizing flows, and evaluate their performance on more complex datasets. The paper should also investigate the impact of different training objectives on the generative model's ability to distinguish between ID and OOD samples.

2. **Lack of Scientific Rigor**: The paper lacks scientific rigor in most of its experimental sections. Each section follows a similar format where a failure mode is claimed (often an obvious one) and then demonstrated with a basic experiment (e.g., “To demonstrate feature overlap, we train a ResNet-18 on a subset of CIFAR-10 classes,” L247). These conclusions are drawn from experiments involving only a single model and dataset, leaving open questions about the generalizability of the findings across different training and evaluation settings. For example, the claim about feature overlap is demonstrated using a ResNet-18 trained on a subset of CIFAR-10 classes, which is not representative of the complexity of real-world datasets. A more rigorous evaluation would involve a wider range of models and datasets, including those with higher dimensionality and more complex semantic structures. The paper also lacks a systematic approach to controlling experimental variables, making it difficult to isolate the factors contributing to the observed failure modes. For example, when investigating the impact of model architecture, the paper should systematically vary parameters such as the number of layers, the width of the layers, and the type of activation functions.

### Questions
See above

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper argues that OOD detection is fundamentally misspecified. It provides a review of
existing OOD techniques and conducts mini-experiments to demonstrate that each suffers
from fundamental flaws arising from the way OOD detection is framed.

### Strengths
A substantive assessment of the strengths of the paper, touching on each of the following
dimensions: originality, quality, clarity, and significance. We
encourage reviewers to be broad in their definitions of originality and significance. For
example, originality may arise from a new definition or problem
formulation, creative combinations of existing ideas, application to a new domain, or
removing limitations from prior results. You can incorporate Markdown
and Latex into your review. See https://openreview.net/faq (https://openreview.net/faq).

The paper is well presented, easy to follow, and makes a well argued case. The authors
conduct mini-experiments to demonstrate pathologies across a wide range of OOD methods
and intend to release code publicly to reproduce examples. The topic is relevant to the
community and raises awareness of the need to clarify the framing and purpose of OOD
detection.

### Weaknesses
While the paper is well presented and provides a compelling argument, it's not clear what
the new research contribution is, and as such I cannot recommend it for acceptance in the
main research track at ICLR. I'd encourage submitting as a review article to a journal or as a
position paper to a workshop, but without a significant research contribution I can't
recommend it for the main research track.
Additional related work:
* Fahim Tajwar, Ananya Kumar, Sang Michael Xie, Percy Liang, "No True State-of-the-Art?
OOD Detection Methods are Inconsistent across Datasets" 2021
https://arxiv.org/abs/2109.05554
* Damien Teney, Yong Lin, Seong Joon Oh, Ehsan Abbasnejad "ID and OOD Performance
Are Sometimes Inversely Correlated on Real-world Datasets" NeurIPS 2023
https://arxiv.org/pdf/2209.00613
Minor:
* Figure 1 doesn't seem to be referenced in the main text
* Line 89: If taking arg max of a function with respect to K, then I'd expect K to appear
somewhere in the function. I believe the arg max should be with respect to index i ∈ {1, .., K}
and the index shown in the function as either y_i or y = i.
* line 99: features or features -> features of features?
* Line 344: OO -> OOD

### Questions
Are the authors claiming a new finding or novel contribution in relation to any specific
experiment, or are these primarily intended to demonstrate known limitations as evidence to
support the paper&#39;s main argument?

### Soundness
3

### Presentation
4

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Authors claim that current OOD detection methods, often based on supervised models and predictive uncertainty, are fundamentally misguided, as they attempt to answer the wrong questions about whether a sample truly belongs to the training distribution.

Currently, common OOD detection methods involve training a supervised model on in-distribution data and subsequently using the model’s predictive uncertainty or features to detect OOD instances. These approaches are typically divided into two main streams
(1) Feature-based methods and (2) Logit-based methods.

However, authors argue that these methods inherently answer the wrong question because they do not measure distribution membership but rather whether a sample leads to unexpected model representations. First, feature-based methods fail when features of OOD and in-distribution data overlap or are indistinguishable, leading to irreducible errors in OOD detection. Second, logit-based methods with high label uncertainty does not reliably indicate OOD samples, as in-distribution samples with high label ambiguity may appear as OOD. This conflation leads to missed detections or incorrect OOD classifications.

Also, alternative attempts to improve OOD detection through scaling, hybrid models, or outlier exposure fall short, as these interventions still rely on the flawed assumptions underlying feature- and logit-based detection.
(1) Scaling model size: Increasing model and dataset size does not fundamentally address the limitations in feature separation for OOD detection.
(2) Hybrid methods: Combining features and logits may show slight improvements but does not resolve the underlying misalignment with true OOD detection which adressed above.
(3) Outlier Exposure: Training with outlier samples to simulate OOD data may improve detection but reduces generalization performance on covariate shifts, highlighting a trade-off between detection and generalization.
(4) Methods based on epistemic (Bayesian) uncertainty, which should theoretically improve with increased data, fail as they conflate uncertainty about the model’s knowledge with uncertainty over whether a sample is OOD. 
(5) Generative models, which compute likelihoods of training data, often fail in OOD detection due to their inability to differentiate low-likelihood in-distribution data from high-likelihood OOD data.

### Strengths
This paper tried to adress its critical examination of the conceptual limitations of widely used OOD detection methods. By challenging the assumptions underlying feature- and logit-based OOD techniques, the authors reveal fundamental pathologies—such as the conflation of high uncertainty with out-of-distribution status. This critique goes beyond incremental improvements and instead questions the foundational approach, which could reshape the field’s direction. Overall the paper is well written in clear presentations with a topic should be high interest in the field.

### Weaknesses
Although, I agree that there is a fundamental pathologies in OOD detection which mentioned in the strength of the paper, I still have some concerns regarding the paper.

1. OOD features that are indistinguishable from ID features may due to the small model representation space. Larger models with various classes may learn detailed representation that can distinguish.

2. Recent OOD methods have devided definition of OOD score and uncertainty. It might seem simmilar, but OOD scores are for detecting whether the input is OOD or ID, not serving as the label is certain or not. This refers there can be a sample with low label uncertainty with high OOD scores (and this is the reason that most SOTA ood detection methods outperform MSP in tables).

### Questions
Interesting paper with nice contributions. You may want to address the weaknesses I listed.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper critically re-examines the popular family of OOD detection procedures, which rely on supervised learning to train models with in-distribution data and then use the models’ predictive uncertainty or features to identify OOD points. The analysis reveals deep-seated pathologies. It argues that these procedures are fundamentally answering the wrong question for OOD detection, with no easy fix. Uncertainty-based methods incorrectly conflate high uncertainty with being OOD, and feature-based methods incorrectly conflate far feature-space distance with being OOD. Moreover, there is no reason to expect a classifier trained only on in-distribution classes to be able to identify OOD points. It shows how these pathologies manifest as irreducible errors in OOD detection and identifies common settings where these methods are ineffective. Additionally, it shows that interventions to improve OOD detection such as feature-logit hybrid methods, scaling of model and data size, Bayesian uncertainty representation, and outlier exposure also fail to address the fundamental misspecification.

### Strengths
1. This paper introduces a fresh perspective by highlighting that many popular OOD detection methods – whether supervised or generative – are not effectively addressing the core question: Is this unlabeled point from a different distribution? 

2. This paper provides concrete examples illustrating how widely-used OOD detection techniques fundamentally miss the mark for true OOD detection. The paper further demonstrates that both feature-based and logit-based methods inherently suffer from irreducible errors, limiting their effectiveness in this context.

3. This paper is well-structured, with clear explanations, making it easy to follow.

### Weaknesses
1. While the paper argues that popular OOD detection methods do not directly address the question of whether an unlabeled point is from a different distribution, these methods have demonstrated strong performance across established benchmarks. It remains unclear whether adopting the approach suggested in the paper would lead to meaningful improvements in performance, raising questions about the practical utility of the findings.

2. The experiments are relatively simple and may not sufficiently support the claims. For instance, the study relies on a small-scale experiment using a LeNet-5 model trained to classify automobiles and trucks from CIFAR-10 to argue that OOD examples often exhibit low uncertainty. However, it is unclear whether these findings generalize to more complex architectures, such as ResNet, or to larger, real-world datasets.

3. While the paper provides a critical analysis of existing OOD detection methods, it does not propose new approaches to address the identified limitations or offer concrete suggestions for overcoming the challenges it highlights. This limits the practical contribution and leaves open questions about how to improve OOD detection in light of the paper’s critiques.

### Questions
1. Given that existing OOD detection methods perform well on benchmarks, how do the authors envision a method that directly addresses the question “Is this unlabeled point from a different distribution?” improving current performance? Could the authors provide further theoretical insights or experimental scenarios to clarify when and why their proposed perspective might offer an advantage?

2. Have the authors considered evaluating their findings with more advanced architectures, such as ResNet, and on larger or more diverse datasets beyond CIFAR-10? Doing so could help demonstrate the generalizability of the claims. 

3. While the paper offers a valuable critique of existing methods, have the authors considered proposing potential approaches or heuristics to address the identified limitations? Even if speculative, some guidance or future directions could make the paper’s contributions more actionable for researchers looking to build on the work.

### Soundness
2

### Presentation
2

### Contribution
2
