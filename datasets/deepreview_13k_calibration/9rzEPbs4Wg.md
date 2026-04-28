# Improving Generalization and Safety of Deep Neural Networks with Masked Anchoring

- Decision: Reject
- Avg Score: 6.17
- Scores: 6, 6, 5, 6, 8, 6

## Abstract
Anchoring is a recent architecture and task-agnostic technique that can produce state-of-the-art epistemic uncertainty estimates, and improve extrapolation capabilities. However, the differences between anchored models and non-anchored variants is not well studied -- as there is little insight into the kinds of functions anchoring induces and how they behave under distribution shifts. In this paper, we analyze and improve anchoring as a training protocol for deep neural networks, evaluating them on important tasks of out of distribution generalization, task adaptation, anomaly detection and calibration. We pinpoint the impact of anchoring on generalization as being inversely related to the sensitivity of the model to the distribution of residuals. We further improve this sensitivity using a new technique called Random Anchor Masking (RAM) that significantly improves the quality of anchored models. We build evidence for the superiority of RAM-training using a range of benchmarks of varying size, using neural networks of varying complexity and scale.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Authors present an overview on the benefits of anchoring for training deep models, and provide a novel technique named Random Anchor Masking (RAM) in which the anchor is masked with a given probability $\alpha$, thus only the residual $x-r$ is used for prediction. The empirical results show that with this approach better results are achieved than with standard anchoring.

### Strengths
- The proposed method does not require any changes to optimization, as it operates only in the input layer

- The experimental evaluation is performed on multiple datasets and architecture complexity 

- The paper is well written

### Weaknesses
I am not an expert on anchoring, so the main issues I encouter in this work are: 

- It is not trivial for me to understand why modelling $P(X,\Delta|Y)$ should provide better results than just $P(X|Y)$

- It is not clear to my why masking the anchor should provide better resutlts. Author say that masking "enforces an otherwise insuficient residual to make accurate prediction". If $\Delta$ is not sufficient for accurate prediction, shouldn't this lead to just overfitting the training set?

- I don't understand if the anchor is chosen always from the training set, also during test. I think it should be, as the anchor label is used as ground truth. I think this should be made clearer

- How does RAM compare to sota methods for OOD or debiasing on tasks such as ImageNet-C? Does it achieve comparable performance or is there a significant gap?

### Questions
- I don't understand if the anchor is chosen always from the training set, also during test. I think it should be, as the anchor label is used as ground truth. I think this should be made clearer

- How does RAM compare to sota methods for OOD or debiasing on tasks such as ImageNet-C? Does it achieve comparable performance or is there a significant gap?

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper extends the anchoring-based training of deep neural networks with a Random Anchor Masking (RAM) technique. The authors observed that this simple RAM strategy can significantly improve multiple metrics under domain shift setting. The empirical evaluation is conducted on CIFAR-10/100 and ImageNet datasets, which shows the positive results by considering the RAM technique in anchoring-based training. Another observation is the trade-off between OOD generalization and anomaly detection, demonstrating that models that achieved superior gains in generalization performance tend to exhibit a trade-off in their ability to detect OOD samples. The authors investigated the effect of masking ratio $\alpha$ on this trade-off.

### Strengths
1. The study of anchoring-based training and inference is interesting. Especially, there are some evidences that this training strategy can benefit some safety-aware metrics.

2. The proposed masking-based strategy is simple to implement. The empirical evaluation shows the benefits of this simple strategy.

3. The illustrative experiment in Figure 1 shows clear motivation for the proposed strategy, where models training by anchoring+RAM seem can better estimate the uncertainty for corrupted samples.

### Weaknesses
1. RAM proposed in this paper is very simple and easy to implement, which is a great advantage. However, the principle and explanation behind this simple strategy are essential. The authors have provided some motivation for this masking strategy, but further explanation of the underlying principles can further improve the quality of the article. For example, the authors mentioned that "this noisy training induced by RAM enforces the model to improve smoothness between the target and the residuals leading to better calibrated predictions". How RAM improves smoothness and how this smoothness leads to better calibration can be further explained. Specifically, the mechanism by which random anchor masking leads to smoother decision boundaries in the residual space is not clear. It would be beneficial to see a more detailed analysis of how the masking operation affects the loss landscape and the resulting model's generalization capabilities. For instance, does RAM encourage the model to rely less on specific features of the residual, and if so, how does this relate to improved calibration?

2. For some other findings in the experiment, such as the trade-off between generalization and OOD detection, this paper only provided some simple experimental results. The reasons behind these phenomena were not deeply analyzed. Is this phenomenon also present in other methods? It is important to understand if the observed trade-off is a fundamental limitation of the proposed approach or if it is a more general phenomenon that arises from the interaction between generalization and anomaly detection. A more thorough investigation, perhaps by comparing with other regularization techniques or OOD detection methods, would be necessary to draw more robust conclusions. The paper should also explore whether the trade-off is consistent across different datasets and architectures.

3. In inference, multiple random anchors can be used to obtain predictions and the variance can be interpreted as an estimate of the epistemic uncertainty. This is very similar with the simple deep ensemble strategy, the comparison with ensemble-based methods could be provided.

Minor issues: "was was argued" ==> "was argued", "results in 2" ==> "results in Table 2", "Figure 3a depicts" ==> "Figure 2a depicts".

### Questions
Please refer to weaknesses section.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors try to provide a high-level understanding of the advantages of the anchoring method, which is believed to offer the enhanced generalization capability of deep models. Also, the authors propose a variant of the popular anchoring method, which masks the anchor sample to achieve further improvements in generalization. Their simple yet effective method is widely evaluated on various tasks and model architectures to confirm the advantages of their strategy.

### Strengths
**Strength 1**: The authors try to provide a comprehensive benefit of anchoring by evaluating the set of related tasks, which have been done separately but are commonly related to the generalization capability of models. Specifically, the corruption robustness benchmarks, including a set of `-C' tasks, the anomaly detection benchmarks, and the various kinds of downstream transfer learning tasks, are largely considered. I believe that the extensive and collective evaluations can provide a comprehensive understanding of the strength of the anchoring methods.

### Weaknesses
 **Weakness 1:** The main motivation of this work seems to offer a 'clear' understanding of the benefits of anchoring, but I feel that the provided explanation is not sufficient to understand anchoring thoroughly. The main reason for this critique is that the analysis remains empirical observations rather than trying to provide theoretical analysis. Most of the researchers conjecture that random perturbations on inputs, e.g., data augmentations with noise or corruptions, or the interpolations between samples, e.g., a family of methods with Mixup such as Mixup, Manifold mixup, CutMix, etc, are linked to the improved generalization of models by letting models face the diversity beyond clean data sample-wise training. However, pushing the 'high-level conjecture' forward 'theoretical proofs' is crucial. I feel that this work has tried to do that, but is quite limited in providing the empirical observations and conjectures, without theoretical proofs.

**Weakness 2:** It is hard to find an explicit logical link between the proposed strategy (i.e., Random Anchoring Masking) and the understanding of anchoring. Why do we have to randomly mask the anchor in order to improve the generalization? Are there any further insights into the proposed strategy beyond the simple objective of imposing higher diversity on models?

**Weakness 3:** The paper is not well organized. For example, it would have been better to organize Related Work to clearly analyze the previous works on both technical and theoretical sides. I know that the author's analyses of the prior works are spread into multiple sections in this version of the article. However, it is better to show a designated section to emphasize the uniqueness of this work beyond prior efforts is strongly required. Also, I guess that the Conclusion section is missing.

There are some minor corrections, including typos.
- In '2.1 Preliminaries', at the 'Notations' part: "of distinct classes.." -> "of distinct classes."
- In the third sentence of '3. An Anchoring Perspective to Generalization': "it was was" -> "it was"

### Questions
**Q1:** As pointed out in 'Weakness 1', would you provide any theoretical support to clearly understand the advantages of anchoring and the proposed masked anchoring method?

**Q2:** As aforementioned in 'Weakness 2', would you provide the logical reasoning of the masking-based approach for anchoring?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper investigates a recent architecture named anchoring.  By evaluating important tasks of out-of-distribution generalization, task adaptation, anomaly detection, and calibration, the authors give a comprehensive study of anchoring for the safety and generalization of deep neural networks. Based on this, a simple modification called Random Anchor Masking (RAM) is proposed and it shows significant performance gains over both standard anchoring and non-anchored models. Extensive experiments across datasets of varying size and complexity (CIFAR10- 100/ImageNet) as well as architectures of varying scales (RegNet/ResNet/WRN/ViT) are conducted, which verify the effectiveness of the proposed RAM methods.

### Strengths
1. This paper investigates a new and novel topic named anchoring, from the perspective of improving the generalization and safety of deep neural networks.
2. This paper is well-written and easy to follow.
3. The proposed method is simple but effective, and it gives some insight by linking the improved generalization behavior of anchored models to their sensitivity to the space of residuals.
4. Extensive experiments across datasets of varying size and complexity (CIFAR10- 100/ImageNet) as well as architectures of varying scales (RegNet/ResNet/WRN/ViT) are conducted, which verify the effectiveness of the proposed RAM methods.

### Weaknesses
1. The proposed RAM method aims at improving the smoothness of the relationship between residual and target labels. However, why does such an easy strategy work on so many datasets and applications? It seems that more analysis and explanations should be given, apart from the extensive experiments showing that it works. Specifically, the paper lacks a deeper dive into the mechanism by which random anchor masking (RAM) achieves its effects. While the empirical results are compelling, the paper would benefit from a more detailed investigation into why perturbing the residuals in this manner leads to the observed improvements in generalization and safety. For instance, is it primarily due to a change in the loss landscape, or is it related to the model's ability to learn more robust features? A more thorough exploration of these underlying factors is needed.
2. According to the impact of masking probability alpha on generalization and safety metrics, it shows a direct correlation between alpha and corruption accuracy. However, why such a correlation is held? Will this correlation be held for more datasets or applications? The paper does not provide a clear explanation for this correlation. It is unclear whether this relationship is a general property of the method or if it is specific to the datasets and architectures used in the experiments. Further analysis is needed to understand the theoretical basis for this correlation and to determine its robustness across different scenarios. It would be beneficial to see if this correlation holds for other types of corruptions or if it is limited to the specific corruptions used in the study.

### Questions
Please see the weaknesses section.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose an extension to the method of anchoring, Random Anchor Masking (RAM), based on their empirical evaluation of anchoring on more typical Deep Neural Networks (DNNs) and tasks than it has been evaluated on in the past. 

Anchoring is a recently proposed methodology designed to improve uncertainty estimation of DNNs by representing input samples as the difference (i.e. residuals) from a different randomly chosen sample within the training set (the anchor). As such, when used at inference time, anchored models are better able to estimate uncertainty since the residuals of an input not within distribuition are likely to be quite large. While anchoring has shown some success in uncertainty estimation on small scale benchmarks, the authors highlight that it has not been evaluated as much on more typical DNN architectures/problems, nor has it been evaluated in the context of other problems where distribution shifts occour, such as outliers, generalization under distribution shift and linear probing, calibration, robustness and outlier rejection. The authors proceed to evaluate standard anchoring on these problems with CIFAR-10/CIFAR-100 and ImageNet dataset variants relevant to the problem and on ResNet/WideResNet CNNs and Vision Transformers.

Despite the relatively good performance of anchoring on these problems, the authors are concerned that when the residual is large, such as would be expected in distribution shift, an anchored model may suffer significantly decreased generalization because it overfits the anchor. The authors propose to extend anchoring by simply masking (i.e. zeroing) the anchor (after residual calculation) with a probability $\alpha$. In other words, they dropout the anchor with probability $\alpha$, introducing noise in the anchored training process. For a small $\alpha$ this might be expected to reduce any dependence the model might learn on the anchors themselves and improve generalization on slightly OOD samples. The authors demonstrate results in a similar empirical analysis as used for standard anchoring and compare results with anchored and non-anchored models. Finally, the authors highlight that their results often show a trade-off for RAM/anchoring with generalization and each problem they evaluated, e.g. calibration. They describe how the hyper parameter $\alpha$ affects this tradeoff, and propose some methodology to mitigate it.

### Strengths
* Overall a very well-written and presented paper (with the notable exception of figure captions/labels).
* Clear motivation and clear method, although some of the design decisions for the method could be explained better.
* Very good background on explaining anchoring and why it might be interesting for other problems with distribution shift as an underlying cause/factor.
* Results are overall presented well in tables, and clear, again with the exception that some aspects are never explained (i.e. +/- is what exactly).
* The paper doesn't just propose a new anchoring method, but also evaluates the existing anchoring methodology on a wide range of problems within the deep learning literature, including robustness, calibration, OOD samples, corruption and linear probing/adaption.
* Reasonable evaluation of the proposed method, and existing anchoring methodology, using appropriate datasets (CIFAR-10/CIFAR-100/ImageNet, and the task variants of these) and a wide range of DNN models, including ResNet/WideResNet CNNs and a Vision Transformer.
* Almost all of the presented results for RAM beat the baselines models modestly with and without anchoring, with perhaps the exception of calibration which is much closer. Overall the results across a wide range of problems are quite impressive, again compared to the baselines.
* The analysis on the trade-off for generalization v.s. each task, e.g. calibration, is welcome and in particular Figure 2 is great to give a high-level overview of what this tradeoff is for some variants of the hyper parameter $\alpha$.

### Weaknesses
 * Why this type of added noise during training v.s. say residual noise, or other noise applied to the mask? While the intuition of noisy training reducing the model overfitting on anchors makes sense, the intuition as to why the authors believe anchor overfitting is a problem isn't completely obvious to me.
* RAM is a very unfortunate acronym to be using in computer circles, while I appreciate the acronym isn't made up and is meaningful, it would probably be best to come up with another one.
* Not clear to me if the same $\alpha$ is applied to the whole batch, or is per-sample. The text in section 3.1 makes it sounds like the former, but that doesn't make sense to me, it seems very strange to mask out a whole batch's anchors instead of a random subset, e.g. like dropout. The lack of clarity here makes it difficult to assess the method's practical implementation and potential impact on training dynamics.
* Calibration results appear to be relatively weak, with many of the results presented being within the variance(?) of baselines. The lack of a clear explanation of the error bars makes it difficult to interpret the significance of these results.
* The captions of figures/tables and labelling of figures is weak, with little explanation to be found within a figure's caption, and labels missing from elements of figures - e.g. missing $\alpha$ on the legend of Figure 2(a). Ideally figures and tables should almost be self-contained, but I found myself having to read the text quite a bit to figure out each one. This lack of self-contained figures and tables hinders the reader's ability to quickly grasp the key findings.
* While the authors compare the performance of RAM w.r.t. the models with and without anchoring on standard task-specific datasets (here I use task to loosely mean problems such as calibration, corruption, robustness, etc). For example while using corrupted ImageNet-C, they do not compare with state-of-the-art methods on that dataset. I personally am willing to forgive this, as the authors do not claim state-of-the-art results on these tasks, and appear to be the first to evaluate anchoring on these tasks at all. However, it would be beneficial to see a comparison with SOTA methods to better understand the relative performance of the proposed approach.
* Little discussion apparently on the effect of adding noise to training on the training time of the model, typically when we add noise to training and make it more difficult, it might be expected that training would take longer to reach the same generalization. The absence of this discussion leaves a gap in understanding the practical implications of the proposed method.
* Not clear how the $\alpha$ hyperparameter values found throughout the paper are decided on. The lack of a clear hyperparameter selection process makes it difficult to reproduce the results and assess the robustness of the method.

### Questions
* Is $\alpha$ is applied to the whole batch, or is it per-sample? In 3.1 "...RAM completely masks the anchors in the tuple for a given batch during training...". If it is for the whole batch, why would you do it this way instead of per-sample, which aligns more with the objective of adding some noise to training (i.e. dropout).
* What is the +/- shown in results, as I don't see it explained anywhere in the paper, i.e. is it variance, stddev, ...? Ideally this should be explained in the captions of the figures themselves.
* Is RAM close to state-of-the-art on any of the datasets it is evaluated with, e.g. ImageNet-C, etc? If not, how far away from SOTA is it, and what do you think it would take to bring anchoring closer to SOTA in these tasks?
* You claim no computational overhead in section 4.2 for RAM w.r.t. anchoring, which I believe given the method. However, anchoring itself does have a computational overhead over standard methods of training since the first (and most computationally expensive) layer of e.g. a CNN is effectively doubled in size. What is the trade-off on this front? Is the tradeoff reasonable for large models still, i.e. ViT?
* Furthermore, since we are making training harder vis-a-vis dropout, what is the increase in training time to reach the same generalization as anchored models? What about compared to models without anchoring?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors explore the anchoring’s role in the generalization and safety properties of models. Based on this insight, the authors uncover that anchoring can be a training mechanism to improve generalization and safety.

### Strengths
The authors show the relationship between generalization ability and residual sensitivity.

This paper is well-written and easy to follow, and the method is simple and implementable.

The experimental results are extensive.

### Weaknesses
Masking probability $\alpha$ is a hyperparameter in the algorithm, which is difficult to estimate in practice.

Masking can reduce the sensitivity of the model to residual, but why can masking promote the smoothness of the model?

### Questions
Please refer to the questions in the Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
