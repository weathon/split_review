# Towards Reliable and Efficient Backdoor Trigger Inversion via Decoupling Benign Features

- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 6, 8, 8

## Abstract
Recent studies revealed that using third-party models may lead to backdoor threats, where adversaries can maliciously manipulate model predictions based on backdoors implanted during model training. Arguably, backdoor trigger inversion (BTI), which generates trigger patterns of given benign samples for a backdoored model, is the most critical module for backdoor defenses used in these scenarios. With BTI, defenders can remove backdoors by fine-tuning based on generated poisoned samples with ground-truth labels or deactivate backdoors by removing trigger patterns during the inference process. However, we find that existing BTI methods suffer from relatively poor performance, $i.e.$, their generated triggers are significantly different from the ones used by the adversaries even in the feature space. We argue that it is mostly because existing methods require to 'extract' backdoor features at first, while this task is very difficult since defenders have no information ($e.g.$, trigger pattern or target label) about poisoned samples. In this paper, we explore BTI from another perspective where we decouple benign features instead of decoupling backdoor features directly. Specifically, our method consists of two main steps, including \textbf{(1)} decoupling benign features and \textbf{(2)} trigger inversion by minimizing the differences between benign samples and their generated poisoned version in decoupled benign features while maximizing the differences in remaining backdoor features. In particular, our method is more efficient since it doesn't need to `scan' all classes to speculate the target label, as required by existing BTI. We also exploit our BTI module to further design backdoor-removal and pre-processing-based defenses. Extensive experiments on benchmark datasets demonstrate that our defenses can reach state-of-the-art performances.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In the context of backdoor, this paper delves into the challenges in Backdoor Trigger Inversion (BTI), a critical method in defending against these threats. 

Traditional BTI methods have been hindered by their reliance on extracting backdoor features without prior knowledge about the adversaries' trigger patterns or target labels, leading to suboptimal performance. 

The authors propose a novel approach that inverts this paradigm by focusing on the decoupling of benign features (rather than backdoored features), followed by a refined trigger inversion process. This two-step method not only enhances the efficiency by obviating the need to scan all classes for potential target labels but also improves detection accuracy.

The paper's methodology encompasses minimizing the disparities between benign samples and their generated poisoned counterparts in the benign feature space, while maximizing differences in the backdoor features. 

This approach also lays the groundwork for more effective backdoor-removal and pre-processing-based defenses. 
The effectiveness of this new method is demonstrated through extensive experiments on benchmark datasets, where it achieves state-of-the-art performance in mitigating backdoor threats, showcasing a significant advancement.

### Strengths
- The paper proposes a novel approach to conduct trigger inversion, which is insightful. The approach is intuitive and appears effective.
- The paper provides a comprehensive evaluation to show the effectiveness and efficiency.

### Weaknesses
 - No discussion on the limitations.

 - Table 8 shows that the evaluation only picks 100 classes from ImageNet. This is wired. Has the method been tested on 1000 classes? What is the scalability of the proposed method? How does the method perform compared to other methods when the number of classes increases?

 - Section 2.2 misses some latest work on feature level BTI:
- SSL-Cleanse: Trojan Detection and Mitigation in Self-Supervised Learning, M. Zheng et al., 2023
- Detecting Backdoors in Pre-trained Encoders, S. Feng et al., CVPR'2023

Although these 2 works focus on self-supervised learning, they are highly related to the feature level BTI. It would be better to discuss them in Section 2.2.

### Questions
1. Table 8 shows that the evaluation only picks 100 classes from ImageNet. This is wired. Has the method been tested on 1000 classes? What is the scalability of the proposed method? How does the method perform compared to other methods when the number of classes increases?

2. Section 2.2 misses some latest work on feature level BTI:
- SSL-Cleanse: Trojan Detection and Mitigation in Self-Supervised Learning, M. Zheng et al., 2023
- Detecting Backdoors in Pre-trained Encoders, S. Feng et al., CVPR'2023

Although these 2 works focus on self-supervised learning, they are highly related to the feature level BTI. It would be better to discuss them in Section 2.2.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Existing trigger inversion techniques optimizes the trigger to find malicious
features. This paper goes the other way and tries to optimize the image so that
the benign features to be close. This is a new angle of optimizing the trigger.
The evaluation is comprehensive including a lot of datasets, models, and
baseline methods. Results are promising.

### Strengths
The inversion technique is novel and different from existing works.

The proposed method can work as different variants on different phases of the
defense.

The evaluation is comprehensive, using different datasets and baselines, etc.

### Weaknesses
An intuition of existing backdoor trigger inversion method is that backdoor
feature pattern is relatively fixed and in small size, e.g., a patch or a filter
or a generative function. However, the feature space of benign samples can be
huge, for example, for the class horse, there could be so many types of benign
feature clusters. We are not sure if there is only one cluster in the feature
space or there are actually many of them. Thus, the optimization directions can
be relatively random. Have you tried different versions of benign features
(e.g., different distance measurement)?

The adaptive settings consider blending the benign and poisoned samples in the
feature space. Have you considered triggers that naturally appear in the
training dataset, i.e., natural triggers?

### Questions
How is the performance on natural triggers?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new backdoor trigger inversion method. Existing inversion
methods optimize the backdoor features, but this paper takes a different
approach that minimizes the feature differences between a benign image and its
triggered version. The method is efficient as it no longer requires scanning
of all classes of a model.

### Strengths
This is an interesting paper. Its main contribution is a trigger inversion
method for backdoor attacks. The main method is quite different from existing
ones, as it works as the "opposite" to existing ones by leveraging the benign
features rather than focusing on the trigger-related ones.

The method also overcomes the limitation of existing method that requires
scanning all output classes to select the most likely target label and class.

The paper has compared the proposed method with state-of-the-art baselines and achieved remarkable results.

The paper also discussed potential adaptive attacks, which is based on blending
the adverbial features into benign ones.

### Weaknesses
Besides the discussed adaptive attack that blend features, some attacks, e.g.,
the composite attack, "Composite Backdoor Attack for Deep Neural Network by
Mixing Existing Benign Features" from CCS 2020, also heavily mix benign and
malicious features. Similarly, the paper can benefit from evaluating on other baselines, e.g., NONE (NeurIPS'22). The evaluation of the method should also consider the trigger size. It is unclear how the proposed method performs against backdoors with larger trigger sizes, which can be more challenging to detect and mitigate. The current evaluation seems to focus on relatively small triggers, and it would be beneficial to see results with a wider range of trigger sizes to better understand the robustness of the approach. Furthermore, the paper should discuss the computational cost of the proposed method. While the paper mentions efficiency gains by not scanning all classes, it does not provide a concrete analysis of the computational overhead of the proposed trigger inversion process, which is crucial for practical applications.

### Questions
See detailed comments.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In this paper, a trigger inversion approach is proposed by first decoupling the benign features from the backdoor features. Then the trigger is inverted on the backdoor features. The proposed method is evaluated on several datasets compared with several baseline approaches against several popular backdoor attacks.

### Strengths
* The paper is generally well-organized.

### Weaknesses
 * (Claimed contribution 3) The proposed BTI-DBF is almost the same as the backdoor mitigation approach in Neural Cleanse [1]! While the authors use a UNet generator, the core idea of inverting a trigger is present in both. The claim that their method generates 'higher-quality' triggers needs more rigorous justification, as the evaluation primarily focuses on defense success rather than trigger fidelity.

I didn't flag for ethics review for this one since I tend to believe that the authors just omitted this existing approach.

[1] Wang et al,  Neural cleanse: Identifying and mitigating backdoor attacks in neural networks. In IEEE S&P, 2019.

* (Claimed contribution 2) The general idea of first decoupling backdoor features from benign ones and then performing trigger inversion on backdoor features is the same as in [2] (though the formulation of the optimization problem is different). The argument that ABS assumes complete separation at the neuron level is not a sufficient distinction, as many methods make similar simplifying assumptions for tractability. The use of a soft mask does not fundamentally alter the core concept of feature decoupling.

[2] Liu et al, ABS: Scanning Neural Networks for Back-doors by Artificial Brain Stimulation. CCS, 2019.

* (Claimed contribution 1) "Revealing the low efficiency and low similarity nature of existing backdoor trigger inversion (BTI) methods and their intrinsic reason" cannot be regarded as a contribution even though you show your method performs better. Besides, there is no adequate discussion about the "intrinsic reason" in this paper. The authors point to scanning all potential classes as the reason for inefficiency, but this is a common requirement for many backdoor detection methods and not unique to BTI.

* The motivation of this work is weak.

What is the motivation for proposing this trigger inversion approach? If the purpose is for better backdoor detection, there is no detection performance demonstrated in the paper. If it is for better backdoor mitigation, there is no evidence that the trigger inverted by other baselines cannot mitigate the backdoor. Moreover, intuitively, inaccurately estimated triggers will introduce more robustness to backdoor unlearning. For example, if the trigger is a 3 by 3 yellow square, unlearning using yellow squares with different shapes and sizes will be more effective than unlearning the backdoor using the exact 3 by 3 square only.

* The results in Table 1 need to be double-checked.

For example, the DSR for Unicorn is much lower than the original paper [3].

[3] Wang et al, Unicorn: A unified backdoor trigger inversion framework. In ICLR, 2023.

* The intuition behind the proposed method does not always hold.

The proposed trigger inversion method can be defeated when there is no decoupling between benign and backdoor features. This happens when the model is compact and when the trigger is globally wide. For example, the "chessboard" trigger that cannot be mitigated by the method in [4] does not satisfy the decoupling assumption.

[4] Wang et al, MM-BD: Post-Training Detection of Backdoor Attacks with Arbitrary Backdoor Pattern Types Using a Maximum Margin Statistic, In IEEE S&P, 2024.

* Insufficient evaluation of the decoupling method.

If the decoupling method works for the proposed formulation for trigger inversion, it should also work for other formulations such as Unicorn. It is important to show that such decoupling is generalizable.

* No evaluation of efficiency in the main paper.

To show that the proposed method is reliable and efficient, it is necessary to include a quantitative comparison of computational overhead in the main paper.

### Questions
Please see the weakness part.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
