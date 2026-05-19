# Towards Mitigating Architecture Overfitting in Dataset Distillation

- Decision: Reject
- Scores: 6, 5, 5, 5

## Abstract
Dataset distillation methods have demonstrated remarkable performance for neural networks trained with very limited training data. However, a significant challenge arises in the form of \textit{architecture overfitting}: the distilled training data synthesized by a specific network architecture (i.e., training network) generates poor performance when trained by other network architectures (i.e., test networks). This paper addresses this issue and proposes a series of approaches in both architecture designs and training schemes which can be adopted together to boost the generalization performance across different network architectures on the distilled training data. We conduct extensive experiments to demonstrate the effectiveness and generality of our methods. Particularly, across various scenarios involving different sizes of distilled data, our approaches achieve comparable or superior performance to existing methods when training on the distilled data using networks with larger capacities.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The submission considers the problem of architecture overfitting in dataset distillation. In dataset distillation, one derives a small synthetic dataset from a given larger, real dataset (along with a “training” network) that captures the learnable properties of the real dataset and can be used to train other “test” networks more efficiently to hopefully achieve similar performance as achievable with the real dataset. An issue that has been noticed in prior work is that when the training and testing networks differ more in architecture, the distilled synthetic dataset starts being less useful, in terms of the task performance.

The submission suggests two main modifications to training the test networks. (1) Since the training networks used for distillation tend to be somewhat shallow, while the downstream test networks are intended to be larger, one heuristic is to train the test networks with a form of regularization that simulates shallower networks. In particular, dropping layers randomly can simulate a form of shallowness (with linear transforms to account for dimension matching). (2) Since it is known that performance drops upon moving to a larger network, one can further attempt to improve training of the test networks by using knowledge distillation to match the predictive distributions of the test network to the smaller training network acting as teacher.

These two tricks seem useful, illustrating significant improvements on existing benchmarks, for a choice of existing dataset distillation methods.

### Strengths
Originality: While the techniques discussed aren’t particularly original, the exploration in the context of dataset distillation seems unique, to my knowledge.

Quality: The paper seems to be of reasonable quality overall.

Clarity: The paper is reasonably clear, as long as the reader is already familiar with how dataset distillation works. (I wasn’t very familiar, and needed to skim past literature to follow the procedure and nomenclature.)

Significance: My naive understanding about the practical relevance of dataset distillation is that it has the potential to enable training very large models efficiently, by minimizing the dataset size, as well as applications where training for longer is a bottleneck (as in continual learning and neural architecture search). Modifying the training procedure of the test networks with sensible regularizations that enable this transfer can be quite significant in practice.

### Weaknesses
I sense no major weaknesses in the submission. Some minor questions remain which are listed in the following section.

### Questions
1. I’m not sure I followed the reasoning behind the scaling of the DropPath output maps. It would be nice to have a derivation in the Appendix for how this scaling matches the expectations from training to test.

2. There’s a statement that architecture overfitting occurs due to depth and not width — has this been recognized in existing work?

3. In the Three-Phase Keep Rate section on page 4, it is said that the variance increases as p increases: isn’t the variance maximal at p = 0.5?

4. There seem to be some hyper-parameters involved, such as the values shaping the shape of the three-phase cycle and the temperature in knowledge-distillation. How are these hyper-parameters tuned? The experiments suggest direct evaluation on test set performances.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a series of methods to improve the performance of models trained by synthetic datasets obtained through dataset distillation. Especially, the paper focuses on models with different architectures from those seen during dataset distillation. The proposed strategies include DropPath with a three-phase keep rate, knowledge distillation, and some other designs on learning rate, optimizer, and data augmentation. Experiments demonstrate that the proposed method improves the performance of training on different architectures using synthetic datasets in dataset distillation by a large margin.

### Strengths
1. This is the first work that explicitly focuses on the cross-architecture issue in dataset distillation. The topic itself is very meaningful since dataset distillation has been demonstrated to be easily overfitting to a single architecture used in training.
2. The writing is coherent and easy-to-follow.
3. The experiments are sufficient to demonstrate the performance of the proposed strategies and the advantages over existing baselines.

### Weaknesses
1. I do not think the cross-architecture generalization problem should be addressed this way. The authors do not modify the process of obtaining synthetic datasets during dataset distillation. Instead, they modify the training strategies **given** synthetic datasets. In dataset distillation, we should definitely focus on the former and should not make any assumptions on how users should use provided synthetic datasets for **downstream** training. What I want to see is actually a thorough algorithm for the process of dataset distillation that can improve the cross-architecture performance following the original evaluation protocols. The current form does not really enhance dataset distillation. The improvement is from the strategies of using distilled datasets.
2. If the paper focuses on how to use distilled datasets, the problem can be cast to some more classical problems, like how to avoid overfitting, synthetic-to-real generalization, few-shot learning, etc. The authors fail to make a broader discussion.
3. The technical novelty is limited because the authors only provide strategies with minor designs that can empirically improve the performance. Without sufficient analysis, the principles of how the proposed methods work are unclear, which results in limited scientific value.
4. The proposed methods are somewhat complicated. For example, they assume users would apply a three-phase keep rate during training with DropPath, which introduces lots of hyper-parameters and makes the pipeline complex and less robust.

### Questions
Please refer to Weaknesses for details.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper presents a set of techniques for training networks on distilled datasets given a fixed (usually small) backbone. The networks for training are not constrained to be the same as those used in the distillation process. The authors argue that the "architecture overfitting" will happen in the distillation process.  To mitigate this, the authors propose a set of techniques to improve the evaluation process and obtain better performance. The authors conduct experiments on two baseline methods and show improved test accuracy.

### Strengths
1. The paper is generally written in good quality and easy to follow. 
2. The idea is straight-forward and seem to be effective. 
3. The topic is timely and important.

### Weaknesses
Questions: 

1.  I am not sure whether it is really the "overfitting". Why this is an overfitting? Is there any evidence to show that the performance already saturate on one backbone, but decrease on the other backbones? It could be the case that the distillation process is even "underfit" on a given architecture - and the performance drop during "transferring" (i.e., distill with one backbone and then evaluate on the others) could be just some normal "generalization error". I would suggest to use the terminology more carefully to avoid such an confusion, or provide evidence to support the terminology. 

2. From what I am understanding, this work actually alters the evaluation process (the process of training a model on the distilled image set). Augmenting the training process is not novel at the high level as many previous works have already done so. A lot of augmentation to architectures (like DropOut and DropPath etc. ) and data (MixUp, CutMix, AutoAugment, etc. ) could be applied here and I think that can serve as potential baselines. 

3. Table 2 provides lower results for MTT baselines. From the original paper, MTT reaches 65.3/71.6 accuracy on CIFAR-10, while in Table 2 the authors reported 63.6 and 70.2. I am curious why there is a performance gap since it may create invalid performance advantages for the proposed techniques. 
 

4. Section 4.2 is interesting, but I think it is off-topic. The paper is trying to solve the so-called "architectural overfitting" but it will not happen when there is no actual "fitting" process. Therefore, I think Contribution 3 is do not count and the contribution bullets should be adjusted.

### Questions
See the above section. My score will be updated accordingly after the rebuttal.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed a series of methods to address the cross-architecture generalization problem of dataset distillation. In detail, combining the DropPath and knowledge distillation, this paper proposed two adapted methods to use a new model design and loss objective to alleviate the overfitting problem. Besides, other tricks like LR and augmentation policy are also used. In experiments, the proposed method performed decently on the cross-architecture tests.

### Strengths
+ The proposed method achieved good results on the claimed cross-architecture test.

+ The presentation is easy to follow. The code is provided.

+ The experiments on multiple datasets, models, and settings provide a solid validation for the contribution.

### Weaknesses
- The results are impressive, however, the method contributions seem relatively marginal. Though the adapted method absorbed from previous works is non-trivial, the discussion lacks enough insight but is empirical.

- The three-phase Keep Rate looks quite complex for tuning. How is the tuning complexity and robustness if we use the proposed method for many different models?

- Though the bag of methods works well, the whole paper gives the readers a feeling of separation.

- typo: in the abs, performance across different network architectures {

### Questions
1. There were only discussions on the residual architecture, why? There are also other multi-branch architectures.

2. "As a result, we can also expect DropPath to mitigate the architecture overfitting issue in dataset distillation. " --- any more detailed analysis?

3. "Architecture overfitting arises from deeper test networks" --- any citation or discussion?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
