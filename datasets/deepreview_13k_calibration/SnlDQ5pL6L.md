# Spatial-Temporal Mutual Distillation for Lightweight Sleep Stage Classification

- Decision: Reject
- Avg Score: 5.50
- Scores: 3, 5, 6, 8

## Abstract
Sleep stage classification has important clinical significance for the diagnosis of sleep-related diseases. Recently, multi-channel sleep signals are widely used in deep neural networks for sleep stage classification and achieve better performance compared to single-channel sleep signals because of the rich spatial-temporal knowledge contained. However, it leads to a great increment in the size and computational costs which constrain the application of multi-channel sleep stage classification models. Knowledge distillation is an effective way to compress models. But existing knowledge distillation methods cannot fully extract and transfer the spatial-temporal knowledge in the multi-channel sleep signals. To solve the problem, we propose a spatial-temporal mutual distillation for multi-channel sleep stage classification. Spatial-temporal knowledge are key references for sleep stage classification. Spatial knowledge represents the spatial relationship of the human body while temporal knowledge means the transition rules between multiple sleep epochs. Moreover, the mutual distillation framework mutually transfer the spatial-temporal knowledge between the teacher and student to improve the knowledge transfer. The results on the ISRUC-III and MASS-SS3 datasets show that our proposed method compresses the sleep models effectively with minimal performance loss and achieves the state-of-the-art performance compared to the baseline methods.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The author proposes a distillation framework to mutually transfer both spatial and temporal knowledge from a teacher model to smaller student model.

### Strengths
The paper is easy to follow and presents the goal of the proposed method clearly.

### Weaknesses
The experimental section of the paper is very unclear. It is unclear what is meant to be the primary models compared against. Simply comparing distillation is not useful as sleep staging is not a task where it is very important. The processing is performed after completion. There is no necessity of real-time processing and complexity is not a big issue. Moreover there is no real analysis of model complexity. Simply training a smaller network can be more beneficial than performing distillation even if we want to reduce complexity. There are other papers which use spatial-temporal relationships in sleep staging such as BSTT [1] and GraphSleepNet [2]. At a minimum this process should be compared with these methods. The results presented in Table 4 also does not make sense based on the relative positions of these positions in other papers. ISRUC-III has only 10 subjects so was the evaluation performed on only one subject? That is very unreliable.

### Questions
Please address the weaknesses

### Soundness
2 fair

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
This paper investigates how to **effectively apply** knowledge distillation (KD) in the spatiotemporal sleep-stage classification task, motivated by the requirement of model efficiency. 

This paper proposes a specific KD solution **tightly combined with the characteristics of sleep signals** by mainly addressing two unique challenges in this task: 
(1) **what knowledge types** related to spatiotemporal signals are useful; and 
(2) **how to transfer** the spatial-temporal knowledge.

### Strengths
1. This paper studies an interesting and practical research topic: how to efficiently and effectively transfer knowledge for spatiotemporal signals/models?

2. This paper has its novelty--it proposes a specific KD solution tightly combined with the characteristics of sleep signals.

There are two technical contributions:
- **Novel knowledge types for sleep signal:** Channel-to-channel pairwise distances are treated as spatial knowledge type. Epoch-to-epoch pairwise similarities are treated as temporal knowledge type. 
- The paper uses a combination of Mutual Distillation [1] and Relational KD [2] to perform the teacher-student knowledge **transfer**.

[1] Zhang, Ying, et al. "Deep mutual learning." Proceedings of the IEEE conference on computer vision and pattern recognition. 2018.
[2] Park, Wonpyo, et al. "Relational knowledge distillation." Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. 2019.

3. The paper conducted comprehensive experiments to justify the effectiveness of the proposed method.

### Weaknesses
1. Despite its novelty in the sleep classification domain. The technical contributions of this paper might be relatively incremental in the ML/AI community.

For example, the second contribution ("how to transfer") is just a combination of [1] and [2].

2. The paper has missing discussions on the existing Spatiotemporal Machine Learning works that is not limited to Sleep Analysis field. Spatiotemporal Machine Learning is already a large research area, and a lot of KD-related works emerge in this field.
 
3. The paper has missing discussions on why the proposed knowledge types are reasonable.

This paper encodes spatial & temporal knowledge in a separate manner. However, is it not true that spatiotemporal knowledge should be jointly modeled as they are hight entangled?

Given this awareness, the proposed knowledge types ("Channel-to-channel distances" and "Epoch-to-epoch similarities") might be outdated, unless the authors can provide the evidence why the separate knowledge types are better than the jointly encoded knowledge.

### Questions
In Eq.(11-12), shouldn't the Loss terms are gradient? 

Also, Eq.(13-14) never appear in objectives. Where should they belong to?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Taking into account spatial knowledge in sleep staging can help improve the model prediction's accuracy. Yet increasing the number of channels can also lead to high computational costs. The authors propose a method to reduce the size of the trained model using knowledge distillation. The paper proposes a new way of extracting spatial and temporal knowledge and an effective knowledge transfer. This new approach is tested over sleep data from two different datasets: MASS-SS3 and ISRUC-III.

### Strengths
The paper explained the relative work and their method very clearly thanks to good writing and very readable plots.

The authors propose a new way to deal with spatial information and a new transfer strategy between teacher and student called mutual distillation. This new way of transfer allows for a proper exchange of spatial-temporal knowledge between the two models. This new distillation's importance is proved in complete experimental results comprising a comparison between SOTA knowledge distillation methods and ablation study.

### Weaknesses
The new mutual distillation needs weight setting. The authors only say that they fixed the weight to 1:5:1 without explaining why this choice was made. The results should be sensitive to the variation of these parameters. Did you try to see the sensitivity of the model to this parameter? How do you select them?

The authors choose only to use six channels comprising EEG and EOG. In classical sleep staging papers, one usually uses 2 EEGs (like Fpz-Cz and Pz-Cz) and possibly EOG (helping to predict the REM stage) and even EMG (helping to predict the wake stage). How was the number of channels chosen? Why six and not all the available channels? The paper shows in the appendix that using the six available EEG channels in ISTUC-III gives better results.

Recent paper, such as Usleep or RobustSleepNet

There is no access to the authors' code for reproducibility; maybe it will be available for the potential final version.



### Questions
To characterize the divergence between the two graphs, you chose to use KL divergence. Do you try other divergences such as TV, MMD, or Wasserstein distance?

Do you try to visualize the graph you obtain at the end of the training or even during training? Do we retrieve a graph base of the Euclidean distance between the channels?

Recent architectures, such as Usleep (https://www.nature.com/articles/s41746-021-00440-5) or RobustSleepNet (https://arxiv.org/abs/2101.02452), train their model on several datasets and give good results on an unseen dataset. Distillation learning proposes to have a smaller model for inference, but I am afraid that your student model will be dataset-specific. It will be interesting to see if such a model can be generalized over a new dataset. With maybe more variability in training set (several dataset)

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a knowledge distillation mechanism for sleep staging. The authors extract the temporal and spatial features based on multi-channel signals.

Meanwhile, a mutual distillation framework is proposed to update teacher and student model. The method was evaluated on two public datasets.

### Strengths
1)The question is interesting. The paper adopts Sleep Knowledge Distillation to decrease the size and computational costs of the existing multi-channel sleep stage
classification models;
2)The paper proposes a spatial-temporal relationship knowledge module to fully extract spatial-temporal knowledge from multi-channel sleep signals
3) This seems to be the first time that spatiotemporal knowledge distillation has been applied to the classification of sleep stages.

### Weaknesses
The experiments are not sufficient enough. The authors should compare their KD method with more popular sleep models. In fact, there are some sleep staging model consisting of a less number of model parameters, e.g. TinySleepNet. 3. “As a result, based on the inspiration of classical sleep models such as DeepSleepNet, we design a CNN and RNN based teacher-student model ” . When compared to DeepSleepNet which is a CNN-LSTM based model, TinySleepNet is both more Reviewer #3 lightweight and shares the same structure, so why not design the teacher-student model based on TinySleepNet.

The main purpose of this paper is to achieve student model lightweighting through knowledge distillation. However, as shown in Tab.2, only the computational costs of teacher and student models are listed. It lacks the comparison with other classical sleep staging models.

It lacks the comparison with other multi-channel sleep staging model, such as SalientSleepNet

### Questions
See Weaknesses

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
