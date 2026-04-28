# Classifiers are Forgetful! Balancing the Mutual Causal Effects in Class-Incremental Learning

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 5, 3, 6

## Abstract
Class-Incremental Learning (CIL) is a practical and challenging problem for achieving general artificial intelligence. Pre-Trained Models (PTMs) have recently led to breakthroughs in both visual and natural language processing (NLP) tasks. Despite recent studies showing PTMs' potential ability to learn sequentially, a plethora of work indicates the necessity of alleviating the catastrophic forgetting of PTMs. Through a pilot study and a causal analysis of CIL, we reveal that the problem lies in the imbalance effect between new and old data, which leads to the forgetting of classifiers. To alleviate this problem, we propose BaCE, a method retrieving the causal effects from new data to the adaptation of old classes and from old data to the adaptation of new classes. By balancing the causal effect, BaCE enables the causal effects from new and old data mutually help the adaptation to each class. We conduct extensive experiments on three different tasks (Image Classification, Text Classification, and Named Entity Recognition) with various backbones (ResNet-18, ViT, BERT) in the CIL setting. Empirical results show the proposed method outperforms a series of CIL methods on different tasks and settings.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes to balance causality between old and new tasks with distillation on class incremental learning scenarios. The method uses a variation of the cross entropy loss and the KL loss adapted to whether on which data is available for rehearsal during the sequence learning. Idea is not so novel, but simple and of interest to the community. Experimental results show improvement over compared methods.

### Strengths
The proposed distillation method is similar to well-established state-of-the-art methods that tackle the relevant issues from different angles. This point of view and proposed strategy based on causality is of interest and provides good insight into balancing the stability-plasticity trade-off.

The paper is fairly easy to read, the method is well documented and supported by the causality hypotheses defined, and the results support the validity of the method.

### Weaknesses
Since the paper focuses on establishing the confrontation phenomenon, but does not provide a method that fully addresses it, the lack of more discussion of the limitations makes it weaker. The point of the paper seems to be juggling between establishing the phenomenon, but not delving as much into it as it could (e.g. more experiments that give insight into what is described in Sec. 4.2), and performing better than the state-of-the-art, but not necessarily tackling what does the proposed method solve actually, in comparison with other similar methods (e.g. where does the performance gain actually come from, is the PTM a huge effect). Some of the interesting insight is relegated to a brief description in the appendix.

IL2M is mentioned as one of the methods that does distillation with a balancing strategy (like BiC and LUCIR), but is not included in the experiments. More analysis on the comparison between these methods that balance only on the logits, and the proposed one would be insightful. 

Table 1 is split into two parts and very reduced. Needs to be fixed and more readable. Same goes for most figures, where everything is too squeezed down. Formatting needs to be readable and fixed.

Results in Table 8 of the appendix are a limitation that should be mentioned in the main manuscript. The proposed method can potentially be between 2x to 5x computationally more expensive during training.

### Questions
The compared methods for when the buffer is empty is quite limited since EWC and LwF are very classic approaches. Why not compare with more recent rehearsal-free methods? E.g. 
- Maintaining Discrimination and Fairness in Class Incremental Learning, CVPR 2020
- Prototype Augmentation and Self-Supervision for Incremental Learning, CVPR 2021
- Class-Incremental Learning via Dual Augmentation, NeurIPS 2021
- Self-Sustaining Representation Expansion for Non-Exemplar Class-Incremental Learning, CVPR 2022
- FeTrIL: Feature Translation for Exemplar-Free Class-Incremental Learning, WACV 2023

When the PTM trained on ImageNet-21k is used for the CIFAR-100 or the 5-datasets, how fair is this comparison? From the ablation in Table 2, it looks as if just freezing parts of the model with the PTM weights is rather competitive with most methods.

Overall, I think it is an interesting submission, of relevance to the field, that could be improved, although it already provides insight into the balancing of the representation biases from a causality perspective.

### Soundness
3 good

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
This paper shows the causal effect of using knowledge distillation and replay memory in class-incremental learning (CIL) setting. The authors pointed out that the main cause of performance degradation is the confrontation phenomenon between old and new samples, and try to resolve this problem with causal graphs. By analyzing the causal path from old data to logits on new classes when performing the knowledge distillation with old and new data. Furthermore, the authors also analyzed the effect of using replay buffer in the causal graph. In the experiment, the proposed method outperforms other baselines.

### Strengths
1. By carefully analyzing the causal path in the causal graph, it is clear to see the main cause of confrontation phenomenon between old and new samples. 

2. In all experiments, the proposed algorithm achieves higher accuracy than other baselines.

### Weaknesses
1. First, the motivation behind constructing the causal graph is similar to [1]. [1] also point out that the path from old samples to intermediate feature can occur the interference, and they also try to resolve this issue. Though figuring out the confrontation phenomenon in CIL may be novel, constructing the causal graph as [1] is quite similar.

2. It would be better to carry out the experiments on large-scale dataset. Since utilizing the pre-training network can also be practical in large-scale dataset setting, showing the effectiveness of BaCE in large scale dataset experiment can strengthen the results.

### Questions
1. Why the prediction bias from class imbalance and the confrontation phenomenon are different? Is it wrong that both problem come from imbalanced dataset?

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposed a new method to deal with old and new data imbalance in continual learning based on causal graph. But the experiment settings have several issues.

### Strengths
The paper proposed a new method to deal with data imbalance in class-incremental learning. The method is based on a causal graph, which is new. 

The proposed method uses a pre-trained model, which is good. In this day and age, many papers still do not use a pre-trained model, which is not understandable.

### Weaknesses
1. The data imbalance problem in continual learning is not new. It is weird that the related work on dealing with data imbalance is put in the appendix. Your method of using KD to prevent forgetting is not new.

2. My complaints are about the experiments. First of all, the pre-training data ImageNet 21k already contains most of the classes in cifar100 and 5-datasets, which means that those classes have been learned during pre-training, which is information leak. In continual learning, they aren’t new anymore. That is why less forgetting occurs. The proper way of conducting the experiments is to pre-train using only the data in ImageNet21k with those intersecting classes removed, like this paper: Kim et al. Learnability and Algorithm for Continual Learning. Proceedings of ICML, 2023.

3. It is unfair to compare your model employing a strong pre-trained network with many baselines that don’t use pre-trained network. 

4. When comparing your Table 1 and Table 1 in the L2P paper, I found that when L2P performs poorer in a setting than your system, you copied the result from L2P using it as a baseline, but when L2P performs better than your system, you didn't. 

5. What does average accuracy mean, average incremental accuracy or average final/last accuracy computed after the last task is learned?

6. Too few datasets are used in the experiments. 

7. Many parts of the paper are hard to read.

### Questions
See points 1, 4 and 5 in the weakness section.

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a unique method to address catastrophic forgetting, drawing inspiration from Causal Effects. Through empirical studies, it highlights the imbalanced causal effect between new and old task data. To address the bias due to the imbalance problem in data between old and new classes, the proposed method strives to equalize the causal impacts of both tasks. Experimental results on CIFAR100 and 5-datasets show that their proposed method outperforms the selected baselines.

### Strengths
1. This paper provides a new view on the underlying problem of catastrophic forgetting, drawing attention to the imbalanced causal relationship between data of old and new tasks.
2. The article presents new method named BaCE, utilizing rebalancing methods to alleviate the bias resulting from the imbalanced causal impact between data from both old and new tasks
3. Experimental results on CIFAR100 and 5-datasets are good.

### Weaknesses
1. Utilizing a supervised pre-trained model for continual learning may not be an optimal setup, especially when there's an overlap between the pre-training dataset and the continual learning dataset. While it's not strictly prohibited to use a pre-trained model for continual learning, it's preferable to use self-supervised pre-trained models. These models ensure that no label information from the downstream continual learning tasks is leaked. Specifically, using a supervised pre-trained model risks introducing a bias where the model has already seen similar classes, potentially inflating performance metrics and not truly reflecting the model's ability to learn new classes in a continual learning setting. This is particularly concerning when the pre-training dataset shares classes or visual features with the continual learning datasets.
2. The selected datasets contain a limited number of classes. For class-incremental learning, it's recommended to utilize datasets with a broader range of classes, such as ImageNet. The limited number of classes in CIFAR100 and the 5-datasets may not fully capture the challenges of catastrophic forgetting in more complex scenarios. Datasets with a larger number of classes, and more diverse visual features, would provide a more robust evaluation of the proposed method's ability to mitigate forgetting and maintain performance as new classes are introduced.

### Questions
See above.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
