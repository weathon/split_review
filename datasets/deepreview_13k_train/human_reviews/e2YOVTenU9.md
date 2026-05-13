# ArchLock: Locking DNN Transferability at the Architecture Level with a Zero-Cost Binary Predictor

- Decision: Accept
- Scores: 6, 8, 3

## Abstract
Deep neural network (DNN) models, despite their impressive performance, are vulnerable to exploitation by attackers who attempt to transfer them to other tasks for their own benefit. Current defense strategies mainly address this vulnerability at the model parameter level, leaving the potential of architectural-level defense largely unexplored. This paper, for the first time, addresses the issue of model protection by reducing transferability at the architecture level. Specifically, we present a novel neural architecture search (NAS)-enabled algorithm that employs zero-cost proxies and evolutionary search, to explore model architectures with low transferability. Our method, namely ArchLock, aims to achieve high performance on the source task, while degrading the performance on potential target tasks, i.e., locking the transferability of a DNN model. To achieve efficient cross-task search without accurately knowing the training data owned by the attackers, we utilize zero-cost proxies to speed up architecture evaluation and simulate potential target task embeddings to assist cross-task search with a binary performance predictor. Extensive experiments on NAS-Bench-201 and TransNAS-Bench-101 demonstrate that ArchLock reduces transferability by up to 30% and 50%, respectively, with negligible performance degradation on source tasks (<2%). The code is available at https://github.com/Tongzhou0101/ArchLock.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper prposes ArchLok to mitigate unauthorizaed DNN transfer. ArchLock first encodes the NN architecture to evaluate rank two architectures with task embeddings, then perform neural architecture search to find archs that are good on source tasks but bad on target tasks. Evaluation on NAS-Bench-201 and Trans-Bench-101 demonstrate that ARchLock significantly reduces the transferbility.

### Strengths
By addressing security at the architecture level, ArchLock potentially fills a gap left by other security measures that focus on the model parameter level. This provides a more holistic defense strategy for DNN models.

ArchLock focuses more on the architecture rankings rather than the actual performance numbers, and utilize efficient zero-cost proxies as supervision. This approach can be scaled to any size of architecture pool and reduces the cost of training several architectures from scratch.

Experiments on NAS-Bench-201 and TransNAS-Bench-101 demonstrate the effectiveness of ArchLock. It can effectively degrade the performance on target tasks by up to 30% while preserving the performance on source tasks.

### Weaknesses
The details of S / TU / TK are not clearly described. Algorithm 1 shows the cross-task search when the target task is known, but it does not discuss how the other two baselines are performed. Additionally, it is still unclear how the GraphEncoder (Figure.1) is executed and how task embedding is extracted. How much overhead does  task embedding take for each new task?

Are the numbers in Tab 1 and 2 real measurements, or are they directly taken from NAS-Bench/TransNAS-Bench? The zero-cost proxies/predictors are trained on the same set of datasets, which may lead to potential overfitting. Evaluating on unseen and large-scale datasets (e.g., ImageNet [can be a subset with ful 224x224 resolution], Miniplaces) is necessary to demonstrate effectiveness.

ArchLock aims to design architectures that show less transferability on new tasks, but it does not discuss what kind of architecture leads to poor transferability. For example, do different datasets dislike different architecture designs, or there is an type of architecture that transfers bad generally on all tasks? It would be beneficial to provide visualizations and discussions of general un-transferable architectures so that further work can gain inspiration and insights.

### Questions
See weakness above

### Soundness
4 excellent

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a cross-task NAS framework to find an architecture to mitigate unauthorized DNN transferability.  A binary predictor using multiple zero-cost proxies is proposed to accelerate the NAS procedure. The results and the ablations demonstrate the effectiveness of the proposed method.

### Strengths
1. The whole formulation of reducing transferability at the architecture level involved with architecture search is solid.
2. The proposed nas method based on binary predictor is efficient and effective in designing model architectures with low transferability.

### Weaknesses
1. Since the proposed method is based on a predictor, maybe it is better to cite a series of predictor-based NAS work. For example, PINAT: A Permutation INvariance Augmented Transformer for NAS Predictor AAAI 2023 TNASP: A Transformer-based NAS Predictor with a Self-evolution Framework NeurIPS 2021 and so on.
2. It seems that there is no training details about the binary predictor, What is the training cost for this predictor? Is one pre-trained predictor suitable for processing the architectures from different search spaces?

### Questions
NA

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper presents a methodology to degrade NN performance on new tasks. Specifically, the paper mentions that adversaries may want to adapt a pretrained NN to a new task while violating its terms of use. To mitigate this issue, the presented methods performs a form of neural architecture search to find NN architectures that degrade performance on the tasks for which the NN was not trained.

### Strengths
- Demonstrates results on transnasbench.
- Leverages zero-cost proxies in a new way.

### Weaknesses
While this paper is interesting, I am not quite convinced of the motivation behind it. If you want to prevent others from fine-tuning a NN, why even release its parameters to begin with? perhaps in this use-case, the model should not even be released? Also, the definition of "task" is very broad. Would additional data be considered a new task? for example, more 32x32 images to be classified into cifar 10 classes for a cifar-10 NN? Or is it just when the classification head is modified?

Other weaknesses include:
- a limited evaluation on NAS benchmarks, making it harder to appreciate the motivation of the paper. If evaluation was done on some NN that someone wants to protect, then it would've helped.
- 2% performance degradation on CIFAR-leve NNs is actually quite large.
- Zero-cost proxies are meant to guage accuracy in general and have not been verified to work for this  task of minimizing out-of-training-distribution accuracy.

### Questions
Can you please provide responses to the weaknesses above. The work is interesting but not fully convincing in its current form.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
