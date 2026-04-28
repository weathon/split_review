# Learning with Temporal Label Noise

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 3, 5, 8

## Abstract
Many sequential classification tasks are affected by label noise that changes over time. Such noise might arise from label quality improving, worsening, or periodically changing over time. In this work, we formalize the problem of label noise in sequential classification, where the labels are corrupted by a temporal, or time-dependent, noise function. We call this novel problem setting temporal label noise and develop a method to learn a sequential classifier that is robust to such noise. Our method can estimate the temporal label noise function directly from data, without a priori knowledge of the noise function. We first demonstrate the importance of modelling the temporal label noise function and how existing methods will consistently underperform. In experiments on both synthetic and real-world sequential classification tasks, we show that our algorithm leads to state-of-the-art performance in the presence of diverse temporal label noise functions.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The manuscript studies the problem of learning (multi-class) classifiers for sequential data in the presence of temporal label noise, i.e., label flip probabilities (from class i to class j) varies with time. The paper models such temporal label noise via a matrix function (num classes x num classes), as is standard in the literature, but parameterized by time, which is new. The authors propose extensions of the so-called 'forward' and 'backward' loss correction mechanisms for empirical risk minimization on training data with temporal noise, and show that ERM using the proposed losses under noisy labels is equivalent to ERM on the clean data, i.e., their Bayes optimal classifiers coincide. The noise function however also needs to be estimated from the data -- so the authors propose a joint training objective to learn the noise function and the classifier, by parameterizing the noise function via a neural network. Empirical results and various ablations show the effectiveness of the proposed formulation and the learning algorithms. 

Overall I think the paper has enough merits but there're some missing details that need to be resolved so that I can better evaluate the contributions. I've some questions below which I'd like the authors respond to in their rebuttal.

### Strengths
- Interesting and relevant ML problem and formulation; sequential data arise fairly regularly in many domains, and label noise changing with time also seems well-motivated to warrant a rigorous study.
- Forward and backward sequential loss formulations for temporal noise and theoretical justifications.
- Fairly elaborate and supportive empirical validation, and detailed analysis of various aspects in the proposed approach.

### Weaknesses
 - Learning a matrix function that changes with time seems very challenging even independently, but learning it together with the classifier is even more so. The paper lacks clarity on why this approach works. If even if there are not any theoretical guarantees for TENOR method, it would be good to discuss why the optimization works and is not derailed by too much label noise (in the experiments, I see even for about 30% noise, the learning is pretty robust).
- More importantly, it's unclear how the TENOR objective imposes regularity across time 't', e.g. if we know the label noise say increases with time in the instances, or varies sinusoidally, etc., it's surprising that the model can learn such Q(t) functions, without any additional regularization or at least a good initial point. The Frobenius norm reg. can't do this. Part of this confusion arises because of my lack of clarity in how Q_w(t) is modeled via a neural network -- are there just one set of weights and an additional 't' parameter (integer) that gives the noise matrix estimates across 't'?
- Theorems 1 and 2 are about equivalences, but there are no forms of estimation/finite sample guarantees in the paper.

### Questions
Please respond to the questions in the 'weaknesses' section.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the problem of learning with label noise under temporal classification, specifically when label noise could be generated from a non-i.i.d function, and existing works could easily fail. To tackle the problem of temporal label noise, the authors first demonstrate that under certain settings, applying loss correction to temporal label noise can obtain a risk-consistent classifier defined over a noise-free distribution. Based on this principle, the authors further proposed TENOR, a noise transition estimation method for temporal classification.

### Strengths
1. This paper proposed a meaningful and relatively under-studied question - how to tackle sequentially correlated label noise.

2. The authors attempt to address this issue from a theoretical prospective, by proving that the loss correction framework under the i.i.d setting can be applied to temporal classification.

3. In addition to the end-to-end learning framework and volume-minimization from existing work [1], authors further proposed a regularization term that enforces the off-diagonal value of the transition matrix to not vanish, which could be useful when the noise rate is high.

[1] Li, Xuefeng, et al. "Provably end-to-end label-noise learning without anchor points." International conference on machine learning. PMLR, 2021.

### Weaknesses
$	extbf{Major issues:}$

1. Simply assuming Assumption 2-4 ignores the main technical challenge in applying loss correction to sequential data - this bypasses the significant challenges such as how the corrected loss at each time step correlates with other time steps. Specifically, the paper does not address how the error in estimating the noise transition matrix at one time step might propagate and affect the corrected loss at subsequent time steps. The assumption of conditional independence, while simplifying the analysis, may not hold in real-world scenarios where temporal dependencies in noise are likely. This lack of consideration for error propagation and temporal correlations in the noise process is a critical oversight.

2. The noise transition estimator is directly borrowed from existing works, however, there is an in-depth discussion on how these methods are suitable for sequential scenarios. The authors do not provide any justification for why a method designed for i.i.d. data would be appropriate for time-series data with potentially complex temporal dependencies. The paper lacks a discussion of the potential limitations and biases that could arise from applying such a method to sequential data, especially when the underlying noise process is non-stationary or has long-range dependencies.

$	extbf{Minor issues:}$

1. Some strong assumptions are assumed, namely, Assumptions 2-4. The authors did not discuss how those assumptions are valid in a real-world setting, and intuitively speaking, those assumptions can easily be violated. For example, Assumption 3 assumes that the noise transition matrix is time-invariant, which is often not the case in practice. The authors should provide more discussion on the practical implications of these assumptions and how their method would behave if these assumptions are violated. A sensitivity analysis of the method's performance under different degrees of assumption violations would be valuable.

2. If we penalize the estimated transition matrix from the identity matrix, in a low noise setting, the transition matrix will tend to produce underconfident loss, hence impairing the training of TENOR, which can be observed in Figure 3.

### Questions
1. Named entity recognition (NER) with label noise is a highly related domain (both dealing with sequentially correlated label noise), some existing works have already been proposed in this area [1,2], and authors should discuss the similarities and differences between those domains, and if possible, apply TENOR to NER to better showcase the performance superiority.

$\textbf{General improvement advises for authors:}$

1. Authors should consider more mild assumptions that enable loss correction to be applied to temporal classification.

2. The proposed TENOR framework is significantly overlapped with the existing method, authors should devise new methods that are specifically designed for temporal classification (orientated to more specific technical challenges). 

[1] Liu, Kun, et al. "Noisy-Labeled NER with Confidence Estimation." Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies. 2021.

[2] Huang, Xiusheng, et al. "Named entity recognition via noise aware training mechanism with data filter." Findings of the Association for Computational Linguistics: ACL-IJCNLP 2021. 2021.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces the concept of a new label noise setting: temporal label noise, where labels are affected by a time-dependent noise function. It presents a method to train a sequential classifier resilient to such noise, directly estimating the temporal label noise function from data. Its main contributions lie in formalizing the temporal label noise problem and devising a novel algorithm to tackle it. Extensive experiments conducted on both synthetic and real-world sequential classification tasks, demonstrate the effectiveness of the proposed method in addressing the temporal label noise.

### Strengths
(1) A new label noise setting is introduced which is unexplored before.

(2) A new method named TENOR is proposed to model the temporal label noise.

(3) Extensive experimental results demonstrated the effectiveness of the proposed method in addressing the temporal label noise.

### Weaknesses
The paper delves into an interesting temporal label noise learning problem, yet it contains several aspects that could benefit from improvement. While the proposed method introduces a fresh label noise setting, it lacks clarity regarding the motivation behind formalizing this new paradigm. Could the temporal label noise setting serve as a replacement for existing label noise settings? Offering reasonable explanations for these concerns can enhance the significance of the new settings.

The authors assume that ‘the sequence of noisy labels is independent of the features given the true labels’ can be strong, since the label noise in the real-world can be instance depended and class depended. This assumption, while simplifying the analysis, may not hold in many real-world scenarios where the noise is correlated with specific features or classes, potentially limiting the applicability of the proposed method.

The comparison methods can be outdated. It is better to consider more SOTA methods as baseline. Furthermore, how you adaptive the baseline to fit your specific setting. The paper would benefit from a more thorough comparison against state-of-the-art methods in label noise learning, especially those that address non-static noise patterns. The current baselines, while relevant, do not fully capture the advancements in the field, making it difficult to assess the true novelty and performance of the proposed method.

Is the proposed method only applicable to binary classification? It is advisable to adapt the real-world noisy label learning dataset Clothing1M to your framework to validate the efficacy of the proposed method. The lack of validation on multiclass datasets and real-world noisy datasets like Clothing1M raises concerns about the generalizability of the proposed method. It is crucial to demonstrate the method's effectiveness beyond the specific binary classification tasks used in the paper.

### Questions
(1) What motivate you introduce this new label noise setting? Does the temporal label noise exist in the real-world application?

(2) The authors assume that ‘the sequence of noisy labels is independent of the features given the true labels’ can be strong, since the label noise in the real-world can be instance depended and class depended.

(3) The comparison methods can be outdated. It is better to consider more SOTA methods as baseline. Furthermore, how you adaptive the baseline to fit your specific setting.

(4) Is the proposed method only applicable to binary classification? It is advisable to adapt the real-world noisy label learning dataset Clothing1M to your framework to validate the efficacy of the proposed method.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Learning from label noise has been widely studied. This paper focuses particularly on the case where noise is introduced over time under specific conditions. This paper introduces the case where noise is time-dependent. Then the authors propose methods that can estimate the temporal label noise function directly from data. The proposed methods improve the performance against existing methods on synthetic and real-world datasets.

### Strengths
The paper formally defines a non-trivial noise label setting whose assumption is more realistic than the earlier approach.

The paper addresses empirical improvement on multiple datasets against existing
state-of-the-art algorithms.

The paper is well written and it is easy to follow.

### Weaknesses
The paper does not discuss the computational complexity

How about the training time compared to other methods?

Is it possible to show that the datasets satisfy the assumption?

Fix the references. The name of some conferences and journals appears with uppercase letters and others with lowercase letters.

### Questions
See Weaknesses Section.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
