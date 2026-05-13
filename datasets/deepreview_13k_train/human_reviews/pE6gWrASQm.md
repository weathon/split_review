# On Adversarial Training without Perturbing all Examples

- Decision: Accept
- Scores: 6, 8, 6, 6

## Abstract
Adversarial training is the de-facto standard for improving robustness against adversarial examples. This usually involves a multi-step adversarial attack applied on each example during training. In this paper, we explore only constructing adversarial examples (AE) on a subset of the training examples. That is, we split the training set in two subsets $A$ and $B$, train models on both ($A\cup B$) but construct AEs only for examples in $A$. Starting with $A$ containing only a single class, we systematically increase the size of $A$ and consider splitting by class and by examples. We observe that: (i) adv. robustness transfers by difficulty and to classes in $B$ that have never been adv. attacked during training, (ii) we observe a tendency for hard examples to provide better robustness transfer than easy examples, yet find this tendency to diminish with increasing complexity of datasets (iii) generating AEs on only $50$% of training data is sufficient to recover most of the baseline AT performance even on ImageNet. We observe similar transfer properties across tasks, where generating AEs on only $30$% of data can recover baseline robustness on the target task. We evaluate our subset analysis on a wide variety of image datasets like CIFAR-10, CIFAR-100, ImageNet-200 and show transfer to SVHN, Oxford-Flowers-102 and Caltech-256. In contrast to conventional practice, our experiments indicate that the utility of computing AEs varies by class and examples and that weighting examples from $A$ higher than $B$ provides high transfer performance. Code is available at [http://github.com/mlosch/SAT](http://github.com/mlosch/SAT).

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies the impact of adversarial training with a limited subset of data on the robust accuracy of computer vision models. The empirical study shows that a limited amount (30%) of carefully selected data is sufficient to achieve 90% of the robustness of the models. Additionally, the paper explores the transferability to other models of the robustness acquired with their method. Empirically, the paper shows that model robustness is best preserved with a custom-balanced loss and with hard-to-classify examples.

### Strengths
- The paper addresses the relevant problem of the generalization of the acquired robustness to unseen classes, examples, and tasks.
- The paper is well-written and easy to grasp.
- The experimental protocol is well described and allows to reproduce the study.
- The paper provides an in-depth empirical study to support its claim.
- The paper proposes a method to estimate the transferability of the acquired robustness which can be useful for testing ML models, as new classes and examples can appear after adversarial training in real-world systems.

### Weaknesses
I have a single but potentially critical concern regarding the significance of this work. In particular, I am unsure what are the benefits of considering a subset of the adversarial examples during adversarial training to improve the efficiency of the process.

As I understand, the key objective of this paper is to limit the size of the set of examples used for adversarial training, to achieve a similar robust accuracy than with full adversarial training. The reason is that full adversarial training is computationally expensive. Considering the settings described in the experimental protocol, I fail to understand why the proposed process is more efficient than full adversarial training. In both cases, the full datasets need to be labeled and the same amount of computational resources is needed, as only the set of available examples for adversarial training differs, not the total number of examples used during adversarial training (since the subset of adversarial examples is completed with the clean examples not used for generating adversarial examples. One could argue that we save 70% of the time to generate the adversarial examples, but the largest cost still come from model training. Considering the empirical results that demonstrate that the proposed method does not lead to better robust accuracy than full adversarial training, I do not see the added value for model robustness efficiency/effectiveness. It would be good if the authors could clarify the benefits of using only a subset of examples in the adversarial training process.

### Questions
- What is the exact process of adversarial training used in the experiments? Are all examples adversarially perturbed? Are some examples perturbed and others clean? In what proportion? In total is the number of perturbation executions the same for adversarial training as subset adversarial training? 

- What is the objective of transferring the robustness across classes and tasks? We need to retrain models to adapt to these new classes and tasks, isn’t it simpler to adversarial train them at retraining, therefore empirically obtaining a more robust model ?

Other comments:

- On page 6,  lines 6 and 11, of the paragraph left to fig 3, describe the results for the class “car” while the numerical value corresponds to the line “plane” on fig 2.
- Figures are not readable when printed.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper conducts extensive experiments to see how only perturbing a subset of adversarial examples in training impacts adversarial robustness.  The authors find that using adversarial examples from certain classes can lead to nontrivial gains in robustness in other classes (despite not training with those classes).  The authors find that the most useful examples/classes to train with are correlated with their difficulty which they measure using entropy.

### Strengths
- paper is very clear
- great scope in experiments which encompass multiple datasets and model architectures
- experiments clearly demonstrate correlation between entropy and robust accuracy on the subset
- experiments suggest that in certain settings, we can train with a smaller subset of adversarial examples instead of all adversarial examples which can reduce the runtime of adversarial training, making it more feasible in practice.  Robustness also transfers to other datasets as well suggesting that this approach can be used with pretraining models.

### Weaknesses
 - while it's clear that training with smaller subsets of adversarial examples can be beneficial, are there guidelines for how to determine the size of this subset to use SAT in practice?

### Questions
See weaknesses

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
To investigate the transferability of adversarial robustness across different classes and tasks, the authors proposed Subset Adversarial Training (SAT), which splits the training data into A and B and constructs adversarial examples (AEs) on A only.  Using SAT, this paper shows that training on AEs of just one class (e.g., cars in CIFAR-10) can transfer a certain level of robustness to other classes. Hard-to-classify classes (like cats) tend to provide greater robustness transfer compared to easier ones. Moreover, using AEs generated from half of the training data can match the performance of full AT. These findings also apply to downstream tasks. This paper distinguishes itself from others by only creating AEs on a pre-defined subset of the training set, independent of the model's architecture or the specifics of the training process.

### Strengths
1. The paper provides valuable insights into the transfer properties of adversarial robustness. The observation that adversarial robustness can transfer to classes that have never been adversarially attacked during training is intriguing.
2. The finding that generating AEs on merely 50% of the data can recover most of the baseline AT performance, especially on large datasets like ImageNet is insightful. This could potentially lead to significant computational savings without compromising the robustness of the model.
3. The paper's findings are not limited to a single task or dataset. The authors have undertaken a thorough experimental evaluation across multiple datasets.

### Weaknesses
1. While this paper presents intriguing empirical results on the SAT approach, it falls short of providing a clear explanation for the observed transferability of adversarial robustness from subset A to subset B. The lack of a theoretical grounding makes it difficult to understand why certain classes transfer robustness better than others, or why a subset of the data is sufficient for training. The paper would benefit from an analysis of the feature space learned by the model to better understand the underlying mechanism behind the observed transfer.

2.  The finding that harder examples provide better robustness transfer is interesting, but the paper does not delve into the specific properties of these 'hard' examples that make them more effective for transfer. For instance, are these examples located closer to the decision boundary, or do they activate a broader range of feature maps within the network? Without a more detailed analysis, it's hard to generalize these findings beyond the specific datasets used in this study.

3. The paper mentions that the trend of harder examples providing better robustness transfer diminishes as dataset complexity increases, but does not provide a sufficient explanation. It is unclear if this is due to the increased dimensionality of the input space, a greater diversity of features, or some other factor. A more detailed analysis of the feature representations in complex datasets is needed to understand this phenomenon.

### Questions
1. Can you provide more theoretical justification or intuitive explanations for the observed efficacy of constructing AEs on only a subset of the training data? Specifically, what underpins the phenomenon where harder examples offer better robustness transfer?
2. You mentioned that as dataset complexity increases, the trend of harder examples providing better robustness transfer diminishes. Can you explain the reasons behind this observation? Are there specific characteristics or properties of complex datasets that might be influencing this behavior?
3. Could you explain more on why the robustness transfer notably increases for smaller $\epsilon$ and decreases for larger $\epsilon$?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors study the generalization of adversarial robustness from class-wise and sample-wise aspects.

### Strengths
1. There are two different settings, i.e., CSAT and ESAT. For each of them, there are comprehensive experiments based on the proposed entropy metrics. On the other hand, the authors consider both $L_2$ and $L_\infty$ attacks. All settings are studied on multiple datasets, which makes the results more convincing.

2. Downstream task transferability is an interesting topic. The results indicate that the learned features can be transferred to other classes, which is aligned with the observation from CSAT.

3. This paper is easy to follow. The writing is clear.

### Weaknesses
1. This paper mainly contains various experiments and their results, but lack the important analysis. Specifically, there are no analysis of the transferability observed from CSAT and ESAT. I cannot get any insightful information after reading this paper, although the results are informative. The paper does not delve into why certain classes, like 'cat', seem to provide better robustness transfer than others, or why robustness from 'cat' transfers to 'car'. This lack of mechanistic understanding limits the impact of the empirical findings.

2. There is no theoretical analysis to rethink the observation as a special property of adversarial training. Additionally, from Figure 4, we can find that the clean accuracy has a similar tendency as the robust accuracy, therefore, it is possible that CSAT and ESAT are just because of the generalizability of the deep learning models. The paper needs to disentangle the effects of general model capacity from the specific properties of adversarial training. It is unclear if the observed robustness transfer is a unique characteristic of adversarial training or simply a consequence of improved generalization due to the training procedure.

3. Only PGD-AT is considered. More advanced methods, like TRADES and AWP, should be evaluated under the same settings. The absence of these comparisons makes it difficult to assess the practical relevance of the proposed method in the context of state-of-the-art adversarial training techniques. The paper should demonstrate the effectiveness of the proposed approach in conjunction with other advanced adversarial training methods.

4. For downstream task transferability, it is similar, but not exactly the same, as contrastive adversarial training. The authors should discuss the similarity and difference between these two methods in this case. A more detailed discussion is needed to clarify the novelty of the proposed method compared to existing contrastive adversarial training approaches, especially regarding the data selection process and its impact on robustness transfer.

### Questions
1. I notice that the authors use stronger data augmentation than usual. For example, when training on CIFAR-10, we usually only use random crop and flip. I hope the authors can provide ablation studies on these data augmentation methods.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
