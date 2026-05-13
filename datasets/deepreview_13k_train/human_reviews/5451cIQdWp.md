# On Synthetic Data and Iterative Magnitude Pruning: a Linear Mode Connectivity Study

- Decision: Reject
- Scores: 6, 5, 3, 5

## Abstract
Recent works have shown that distilled data representations can be leveraged for accelerating the training of DNNs. However, to date, very little is understood about the effect of these synthetic data representations in the area of architectural optimization, specifically with Iterative Magnitude Pruning (IMP) and pruning at initialization. We push the boundaries of pruning with distilled data, matching the performance of traditional IMP on ResNet-18 \& CIFAR-10 while using 150x less training points to find a sparsity mask. We find that distilled data guides IMP to discard parameters contributing to the sharpness of the loss landscape, fostering smoother landscapes. These synthetic subnetworks are stable to SGD noise at initialization in settings when the dense model or subnetworks found with standard IMP are not, such as ResNet-10 on ImageNet-10. In other words, training from initialization across different shuffling of data will result in linear mode connectivity, a phenomenon which rarely happens without some pretraining. We visualize these loss landscapes and quantitatively measure sharpness through hessian approximations to understand these effects. This behavior is heavily linked to the compressed representation of the data, highlighting the importance of synthetic data in neural architectural validation. In order to find both a high performing and robust sparse architecture, a more optimal synthetic data representation is needed that can compress irrelevant noise like distilled data, yet better maintain task-specific information from the real data as dataset complexity increases.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studied the stability of synthetic subnetworks (the lottery ticket at initialization obtained by IMP after training o distilled data) with linear mode connectivity. In contrast to the usual instability observed in both the dense network and the standard IMP subnetwork, the synthetic subnetwork proves to be remarkably stable to SGD noise at initialization. To gain a better understanding of this phenomenon, the paper proceeds to visualize the loss landscape and quantitatively assess its sharpness through hessian approximation.

### Strengths
1. This paper offers a compelling insight into the impact of data distillation on the stability of lottery tickets obtained through the IMP method. This observed stability holds true across various datasets and models, strengthening the credibility of the findings.
2. The paper conducts a comprehensive analysis of the performance and stability of synthetic subnetworks. Furthermore, its impressive visual representations provide valuable insights into the study of stability and the intricacies of the loss landscape.

### Weaknesses
The analysis of the loss landscape and its sharpness for dense models, synthetic subnetworks, and IMP subnetworks is quite interesting. However, I have a couple of questions that I hope the author can clarify:

1. The loss landscape of dense models and IMP subnetworks appears to be sharper than that of synthetic subnetworks. Can the sharpness of the loss landscape be used as a criterion for determining the quality of a subnetwork? Specifically, while the paper shows that synthetic subnetworks exhibit stability, it's not clear if this smoothness directly translates to better generalization or performance compared to the sharper minima found in dense or IMP subnetworks. It would be beneficial to explore the relationship between landscape sharpness, generalization error, and robustness to perturbations in more detail.
2. In the last paragraph of Section 5.1 (on page 8), it is mentioned, 'We see the trained models fall into two separate minima in both the IMP and Dense cases, explaining the loss barrier in Figure 4.' This seems to connect stability with the loss landscape. If I understand correctly, the linear path for stability and loss landscape are different. Is this proper to explain the stability with this loss landscape? The linear interpolation for stability is performed between two independently trained models, while the loss landscape visualization is around a single trained model. It is unclear how the loss barrier observed in the landscape directly explains the stability observed during linear interpolation between different models.

Other tiny issues:

1. The axis legend in Figure 6 is almost unreadable.

### Questions
1. How is the stability of the other distilled data other than the one evaluated in the paper? 
2. How does IPC impact the stability? Can more studies are provided for ResNet18 on CIFAR10 and CIFAR100?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper follows the main idea of McDermott & Cummings (2023) that leveraging the synthetic dataset (specifically, dataset distillation) to find a sparsity mask with IMP. The difference between this paper and McDermott & Cummings (2023) is that this paper applies a better dataset distillation method. The strong part of this paper is that they found the subnetworks at initialization that are already stable to SGD noise, which is surprising.

### Strengths
1. Sec 5.'s experiments are interesting to me. The authors found that there exits subnetworks are already stable to SGD noise using distilled data.

### Weaknesses
1. The contribution is limited. The main idea of this paper actually follows McDermott & Cummings (2023) but change the dataset distillation method.
2. IB framework seems to be irrelevant to the main logic of this paper. A large part of this paper is trying to explain the connection between the IB framework and dataset distillation method, but I don't see a deep connection between this part and the main flow of this paper. Moreover, the IB framework lacks experiment or theoretical analysis which cannot convince me firmly.
3. The Sec 5.1 seems to be redundant. The LMC experiments can already give a clear conclusion over the stability of subnetworks. I don't see a large advantage to include such fancy visualizations in the main text.
4. Some figures seem to be non-informative (e.g., Fig 1 right part and Fig 2). There is no need to explain the dataset distillation and IMP with both texts and figures. This part can be put into a "background" section but no need to explain in such a detailed manner. The audience can be assumed to be people who are knowledgeable in these fields and the effect of including these figures is to lower the informativeness of this paper.
5. The writing of this paper sometimes makes me lost. There are many "therefore" in this paper, but most times when "therefore" occurs there is no clear causal relationship between the sentences before and after. Some expressions are vague, e.g., the "important" in "...What is deemed "important" for real data might not be important for distilled data; therefore, distilled pruning may attempt to remove these...." (P. 5). Also, some expressions are actually wrong, e.g., "Linear paths or Linear Mode Connectivity (LMC) is an uncommon phenomenon that only occurs in rare cases..." and LMC is not a rare phenomenon but happens with both spawning case and permutation case [cite 1].
6. Most important references are missing. Only one paper is referenced in the LMC section.

### Questions
No question.

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper investigates the effect of using distilled datasets for training deep neural networks in terms of the linear mode connectivity of pruned models (analogously to experiments by Frankle et al. with iterative pruning). Empirical investigation shows that sparsity masks found with distilled (synthetic) data are approximately as good as the ones found with standard IMP, but at the same moment they demonstrate more stability to SGD noise in terms of linear mode connectivity, i.e., the barrier between "synthetic" subnetworks is smaller than one between standard IMP subnetworks.

### Strengths
The idea to understand the effect of the synthetic data on the training loss surface is interesting. It can shed light on the ways data affects the optimization landscape. It also has a benefit of a faster pruning process, since training on less data is (hopefully) faster.

### Weaknesses
While the core idea of the investigation is interesting, the overall contribution of the paper is questionable. The largest part of the paper is dedicated to the description of the process of data distillation, while that is not the contribution of the paper (existing distilled datasets are used for the experiments).

The discussion about information bottleneck is largely misplaced in this work. The initial idea of IB is that a deep learning model implicitly tries to learn a representation that keeps maximal possible information about targets and minimal possible information about inputs, thus forming a bottleneck. It is still not proven that such compression is needed for generalization and that deep neural networks indeed perform it. Moreover, a natural conjecture about using a data that is already optimized in terms of information is that the model (neural network in this case) does not have to learn it anymore. Meaning, that from the initialization its task is simplified significantly, it basically does not have to form a bottleneck in itself. The empirical evidence in this paper is supporting this conjecture directly (especially with the observation that for more complex datasets there is no effect of smoothing barriers). I see the analysis of direct differences between sparsity masks induced by distilled data and natural data and analysis of them as an important experiment not performed in this paper. As well as the exhaustive comparison between the performance of synthetic masks should be one of the central and most discussed results, but it is reduced to one diagram in the paper.

Minor:

- please make use of \citep and \citet to distinguish citations that are not part of the sentence and part of it correspondingly

- in section4 there is a mention of "architectural relationship of the data" - it is completely unclear what does this term mean

- diagram in Fig.7 is very hard to understand. Why only 60 and 87 sparsity are chosen? Why the barrier is always same for IMP setup? What is performance ratio? Why IMP baseline is only one no matter that there are several setups?

- I think the first sentence of Discussion does not belong to the text

- the flatness investigation is left out to the appendix, nevertheless it is mentioned as one of the conclusions for the paper. There is no clear connection in general in the existing research between LMC and flatness, so the conclusions are inaccurate.

### Questions
1 - What is the core goal of the research performed in the paper?

2 - How easy it is to produce distilled datasets analogous to ones used for experiments? Why they are tightly bound to a particular architecture?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the effects of pruning on distilled datasets (the synthetic data created by dataset distillation) and compares it with Iterative Magnitude Pruning (IMP). The authors find that pruning on distilled datasets has a higher efficiency, causes flatter landscapes, and has better linear mode connectivity. They also interpret the phenomena via the information bottleneck perspective.

### Strengths
* The information bottleneck perspective on the distilled dataset is interesting and novel.
* The findings that the pruned networks on the distilled dataset have flatter landscapes and better linear mode connectivity are new and insightful.
* The experiments are somewhat solid.

### Weaknesses
 * **Presentation and structure.** I think this paper may have poor presentation and language. I recommend the authors to polish the paper and reorganize the structure. For example, the information bottleneck part seems strange to me at first glance. Maybe the authors can elaborate more on how information bottleneck is related to the main findings and claims and conduct a more fluent transition between (sub)sections.
* **Novelty.** Using the distilled dataset for better efficiency in pruning has already been proposed in previous literature [1], which weakens the novelty and contribution of the proposed method. Therefore, the efficiency cannot be a main claim. And I think the whole novelty of this paper is weak.
* **Lack of further evidence.** Information bottleneck is a good perspective to understand the distilled datasets, but I think the paper lacks further evidence on how information bottleneck is related to the findings. Concretely, how the information bottleneck is quantized? I think the loss landscape is not a direct aspect to show the point. More direct and intuitive evidence is needed.
* **Lack of implications to practices.** Knowing the fact that pruning on distilled data is not new in this paper, the author should provide more insights on how the findings can guide applications and practices.

### Questions
* The used models are only ResNets and ConvNets. I am interested in the results regarding more model architectures, specifically, Transformer is of particular interest, and other architectures, such as MLPs, VGGs, and MobileNets, are also needed.

### Soundness
3 good

### Presentation
1 poor

### Contribution
2 fair
