# Continual Learning in Open-vocabulary Classification with Complementary Memory Systems

- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 5, 8

## Abstract
We introduce a method for flexible and efficient continual learning in open-vocabulary image classification, drawing inspiration from the complementary learning systems observed in human cognition. Specifically, we propose to combine predictions from a CLIP zero-shot model and the exemplar-based model, using the zero-shot estimated probability that a sample's class is within the exemplar classes. We also propose a ``tree probe'' method, an adaption of lazy learning principles, which enables fast learning from new examples with competitive accuracy to batch-trained linear models. We test in data incremental, class incremental, and task incremental settings, as well as ability to perform flexible inference on varying subsets of zero-shot and learned categories. Our proposed method achieves a good balance of learning speed, target task effectiveness, and zero-shot effectiveness.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper tackles a new problem of continual learning in open-vocabulary classification where the model can update its knowledge based on incoming new samples while preserving zero-shot learning capability.
To achieve this, this works proposes to combine CLIP model, having zero-shot ability, with examplar-based learning, which stores additional training samples as exemplar for continual learning.
For exemplar-based learning, the author introduces a tree-probed algorithm which improves upon KNN to increase accuracy.
The paper provides an interesting analogy between CLIP & instance-based learning and fast & slow learning system in human development.
To combine between these two different learning paradigms, the proposed work designs a fusing prediction formula that averages the probability or embedding predictions of the two models. Finally, Adaptive Instance Marginalization module is trained to estimate the probability of a test sample belong to the exemplar set to further boost the performance.
The paper conducts experiments on CIFAR100, SUN397, FGVCAircraft, EuroSAT, OxfordIIITPets, StanfordCars, Food101 and Flowers102, ImageNet, UCF101, and DTD.

### Strengths
+ Using fast & slow learning system from human learning to describe the combination of zero-shot and exemplar-based learning is inspiring.
+ The problem of continual learning in open-vocabulary classification is interesting and can have practical applications.
+ The paper provides details experiments on multiple datasets.

### Weaknesses
 + The paper is hard to follow. Specifically the proposed setup is vaguely describe in the paper. For example, in the literature of open-vocabulary learning, there are only base and target classes [A,B]. However, the paper keeps mentioning about zero-shot and target tasks without clear explanation on what is zero-shot class (in open-vocabulary learning).

+ The proposed idea is highly similar to continual zero-shot learning work where the goal is also to update model with new samples while maintaining the zero-shot performance [B]. It seems that the main difference is the use of CLIP encoder which boosts the model zero-shot capability but the core idea of continuously update the zero-shot model is similar. However, there is no discussion or comparison with these prior works.

+ The reviewer also has doubted on the effectiveness of the proposed method as on average task performance the model only improve 0.5% compared the strong baseline ZSCL (as reported in table 1 in the main paper). Moreover, based on table 4, it appears that the proposed method doesn't perform well on fine-grained classification tasks of Flowers, Cars and EuroSat. Thus, the reviewer is not confident on whether the proposed method advances the continual open-vocabulary classification task.

### Questions
+ Can the author verify the continual learning setup as well as the terminology (zero-shot tasks) clearly in the manuscript? This would significantly improves the paper readability.
+ Sufficient discussion should be make between the proposed work and continual zero-shot learning literature.
+ Can the author justify the modest improvement of 0.5% compared to SOTA?

### Soundness
3 good

### Presentation
2 fair

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
The approach enables adaptable and efficient continual learning in open-vocabulary image classification. It draws inspiration from human cognition’s complementary learning systems. In this work, the author merges predictions from a CLIP zero-shot model and an exemplar-based model. it is based on using the zero-shot estimated probability that a sample’s class is within the exemplar classes. Inspired by lazy learning principles, the author introduces a “tree probe” method, which facilitating rapid learning from new examples with comparable accuracy to batch-trained linear models.

### Strengths
[1] The problem is interesting, which predicts the open set vocabulary while following the setting of continual learning.

[2] Results are evaluated over the various datasets in the diverse setting.

[3] “Tree-probe” is interesting, which balance the rapid learning and performance.

### Weaknesses
[1] There are various setting in the continual learning (task incremental, class incremental, data incremental etc.) and zero-shot learning (generalized/non-generalised setting). The exact experimental setting, evaluation strategy, and the motivation of each setting are not clear. It’s difficult to follow the section 4.2, there should me better illustration and discrimination between the various evaluation scenarios.

[2] There are few recent works [1,2] follow the similar setting. These works can be considered as baseline along with the CLIP zero-shot.

[3] I believe that adding the problem setting before the section-3 (Method) with the proper notation will increase the readability. 

[4] The recent prompting based continual learning approach [3,4] leverages the strong pretrained model and shows the promising result for the continual learning without complementary memory system. Instead of examplar storage, if model leverages promoting based approach, how the model behaves?

### Questions
Please refer to the weakness section.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a continual learning method for image classification. It addresses quite challenging setups as data incremental, class incremental and task incremental settings. The core of their method is a combination CLIP embedding for zero-shot prediction and tree-based kNN exemplar-based model (TreeProbe). The paper presents results a large variety of datasets and compares with a few well-cited continual learning methods from the past decade. CLIP enables open-vocabulary learning (within CLIP training set, of course) and their suggested TreeProbe shows quick training and inference. The two-model combination is inspired by a famous work in continual learning "complimentary learning system" that suggests that human brain has two types of memories: fast episodic memory (hippocampus) and slow consolidating memory (neocortex). It's been exploited in continual learning approaches before with limited success.

### Strengths
I find this paper quite strong. It tackles a very very difficult problem of open-world image classification in incremental learning. Typically neural nets suffer from catastrophic forgetting that makes incremental training pointless pretty much. Many attempts were made on solving this problem. 

Overall results look very promising. I am happy to not see permuted MNIST in benchmarks.

The paper is well-written and easy to read. The paper achieves SOTA results although the gap with the other CLIP-based model is pretty small. I found it convincing enough and sufficiently novel.

### Weaknesses
Using CLIP for incremental learning isn't novel. TreeProbe seems like a quite simple approach, I can't believe it wasn't described before. I couldn't however find a reference.

The main drawback is that it still relies on CLIP. While we don't know exactly what CLIP was trained on, I find it easy to believe that 400M dataset contains everything that the authors used for evaluation so in a way it is not really continual learning as we would like it to be.

### Questions
The method contains a lot of moving parts around merging CLIP and exemplar model and TreeProbe implementation. I encourage the authors to release their code to facilitate future research.

I also suggest to clearly present accuracy of supervised baselines for every dataset they used. While it is certainly not to compare their method against, it is useful to know "are we there yet?" in terms of how practical continual learning has become. It is also useful to know total number of classes that was obtained after merging all datasets.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
