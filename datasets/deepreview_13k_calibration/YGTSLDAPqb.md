# Connect Later: Improving Fine-Tuning for Robustness with Targeted Augmentations

- Decision: Reject
- Avg Score: 4.33
- Scores: 3, 5, 5

## Abstract
Models trained on a labeled source domain often generalize poorly when deployed on an out-of-distribution (OOD) target domain. In the domain adaptation setting where unlabeled target data is available, self-supervised pretraining (e.g., contrastive learning or masked autoencoding) is a promising method to mitigate this performance drop. Pretraining depends on generic data augmentations (e.g., cropping or masking) to learn representations that generalize across domains, which may not work for all distribution shifts. In this paper, we show on real-world tasks that standard fine-tuning after pretraining does not consistently improve OOD error over simply training from scratch on labeled source data. To better leverage pretraining for distribution shifts, we propose the Connect Later framework, which fine-tunes the model with \emph{targeted augmentations} designed with knowledge of the shift. Intuitively, pretraining learns good representations within the source and target domains, while fine-tuning with targeted augmentations improves generalization across domains. Connect Later achieves state-of-the-art OOD accuracy while maintaining comparable or better in-distribution accuracy on 4 real-world tasks in wildlife identification (\iwildcam), tumor detection (\camelyon), and astronomy (\classification, \redshifts).

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This manuscript deals with the domain adaptation problem, i.e., the setting in which there is a domain shift between a source and target domain and where only unlabelled data is available for the target domain. One approach to this problem is to use self-supervised learning using both the source and target domain data, followed by fine-tuning with the labelled source domain data.

The authors begin with the observation that this approach leads to inconsistent results compared to regular supervised training (ERM). They hypothesize this is because the self-supervised methods learn features that are strongly domain-specific, which means that when the model is fine-tuned the classifier from the last layer might not generalize beyond the source distribution. The authors propose a solution which involves using targeted augmentations (i.e., augmentations that are specifically designed to remove spurious domain-dependent features) during the fine-tuning phase. They show that this improves performance on three different datasets.

### Strengths
This paper looks at an interesting problem: Unsupervised domain adaptation is a very relevant problem (e.g., in many cases practitioners have labelled datasets available from a curated/lab setting, but need to generalize to actual deployment conditions). At the same time, self-supervised learning has become very popular, but its performance in the context of unsupervised domain adaptation (UDA) is still unclear.

This paper introduces a new dataset (RedShifts), and contains some encouraging results on two different domains (camera trips and astronomical observations) while performing several relevant ablations (model scale, whether to train the last layer before fine-tuning, strength of pre-training augmentations).

The paper is relatively easy to read, with good writing and a clear structure.

### Weaknesses
Overall, I find this paper lacking in a variety of areas:

The authors' refer several times to Shen et al. (2022). This paper argues that contrastive pre-training is beneficial as long as data augmentations ensure that augmented examples must be more likely to change class or domain than changing both. The authors of this manuscript seem to argue in section 3 that the bad results they observe are explained by a violation of this assumption from Shen et al. (2022). However, this isn't tested rigorously (see section 6 of Shen et al., 2022, for examples on how to evaluate connectivity on real world datasets).

A second shortcoming is that different self-supervised methods were used for the iWildCam-WILDS dataset (SWaV contrastive learning) and the astronomical time-series (masked autoencoding). This makes it hard to draw conclusions from table 1, since it is unclear which differences can be attributed to the use of different pre-training objectives.

The results on the iWildCam dataset are not very strong (given the means and standard deviations listed, there's a 20% chance that ERM + targeted augs outperforms Connect Later for any run). This leaves the improvements in the astronomical time-series datasets as the stronger proof of Connect Later's performance. But these results are a bit confusing to me: How is it that standard fine-tuning improves in-domain performance (tables 1 and 2)? This suggests to me that these datasets are possibly very small and benefit strongly from the regularization that pre-training provides. In that case, is Connect Later really addressing a domain shift issue? Or is it just addressing a regular overfitting issue? The latter seems plausible given the very small size of the dataset (6,74 objects). I would argue that in order to draw conclusions, the method should be tested on a wider variety of larger datasets.

A baseline that seems to be missing as well is the use of general augmentations during fine-tuning (my understanding is that standard fine-tuning uses no augmentations at all). This would clarify whether it is important to use targeted augmentations during fine-tuning, or whether any form of augmentations would be fine.

Overall, I find the insights that this paper provides limited: It is not surprising to me that targeted augmentations would help with fine-tuning, given that they were shown to help with regular ERM. The bigger question to me is the one raised in section 3: Why does pre-training not always lead to increased OOD performance? This question remains largely unanswered. I think this paper would be better if it provided, for example, (1) clear evidence that the assumptions from Shen et al. (2022) are routinely violated in real-world datasets and commonly used augmentations, (2) a thorough evaluation of how different pre-training techniques (MAEs, contrastive learning) perform in the UDA setting, or (3) strong evidence that targeted augmentations are particularly important compared to general augmentations.

### Questions
See weaknesses.

### Soundness
1 poor

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes Connect Later to improve robustness. It involves performing self-supervised pretraining (e.g., masked autoencoding or contrastive learning) followed by finetuning with augmentations designed with knowledge of the distribution shift. Supportive results were shown on several real-world dataset.

### Strengths
Evaluations were done on real world datasets with supportive results.

### Weaknesses
1. Generalizability of the method.
    - If target augmentations involve knowledge of the distribution shift, why pre-training is needed? If we are able to generate the target data, where other options include using powerful generative models [1], why do we need pre-training? It seems to be more a question of when is pre-training necessary. 
    - It is also not clear if pre-training in general is useful as the experimental results were only shown with one type of pre-training method and a different pre-training for different datasets. How sensitive are the results to the choice of pre-training method?
    - From Table 2, it seems like the results are sensitive to the target augmentations. For iwilds most of the gains seem to come from the targeted augmentations. But for the astro datasets the ID test acc for astroclassification is better without targeted augmentations. One a new task or dataset, how should one choose the targeted augmentations?
2. Test-time methods, like test-time augmentation/training also makes use of unlabelled data. These methods aim to adapt to the distribution shift as they occur. Furthermore, some of these pre-training objectives like masked auto-encoding have been used for test-time adaptation [2]. It may be beneficial to pose these methods wrt Connect Later.
4. Presentation
    - Sec 4 gives the technical details for creating augmentations before explaining the tasks. It may not be clear what the tasks for Astroclassification and Redshift are about and so the technical details are not easy to understand. I would suggest moving Sec 5 before 4.
    - In Fig 2, top row, what do the colors mean? Why does augmentation introduce errors?
    - It may be useful to have additional columns in the main table of results (e.g. Tab 2), that describes what the different methods are. E.g., whether finetuning augmentations are used, and with checks in the rows for the relevant methods.

### Questions
See the points raised in weaknesses for questions and suggestions.

### Soundness
2 fair

### Presentation
2 fair

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
The paper proposes Connect Later to improve model robustness in domain adaptation scenarios. The approach first leverages generic augmentations to pretrain on combined unlabeled source and target data. It then employs carefully designed targeted augmentations during fine-tuning on labeled source data to better connect the source and target domains based on knowledge of their distribution shift. The experiment shows the effectiveness of Connect Later over several baselines on three datasets.

### Strengths
The paper is clearly written in general, so the overall quality of the paper is satisfactory.

### Weaknesses
1. The proposed framework hinges on the manual design of the transformation distribution and requires knowledge about the distribution shift between source and target domains to create effective targeted augmentations. This property limits the applicability of the proposed method in scenarios where the shift is unknown or diverse. Specifically, the method relies on the ability to craft augmentations that mimic the specific types of variations seen in the target domain relative to the source. This requires a detailed understanding of the underlying causes of domain shift, which may not always be available or easily discernible. For example, if the domain shift is caused by complex, non-linear interactions of multiple factors, designing targeted augmentations becomes significantly more challenging and may require extensive trial and error.

2. On iWildCam, Connect Later only marginally outperforms ERM+targeted augmentations, which indicates that if there is diverse distribution shifts, the proposed method is not quite effective. The small performance gain suggests that the method might not be robust to complex or highly variable distribution shifts. This is a concern because real-world domain adaptation problems often involve shifts that are not easily characterized by a single type of transformation. The fact that a simpler approach (ERM + targeted augmentations) achieves nearly the same performance raises questions about the practical value of the more complex pretraining step in Connect Later, especially when the distribution shift is not well-understood.

### Questions
Could the authors test the sensitivity of the performance of Connect Later with respect to the design choice of transformation distribution?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
