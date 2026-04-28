# Fantastic Gains and Where to Find Them: On the Existence and Prospect of General Knowledge Transfer between Any Pretrained Model

- Decision: Accept
- Avg Score: 7.25
- Scores: 5, 8, 8, 8

## Abstract
Training deep networks requires various design decisions regarding for instance their architecture, data augmentation, or optimization. 
In this work, we find these training variations to result in networks learning \textbf{unique} feature sets from the data.
Using public model libraries comprising thousands of models trained on canonical datasets like ImageNet, we observe that for arbitrary pairings of pretrained models, one model extracts significant data context unavailable in the other -- independent of overall performance.
Given \textbf{any arbitrary pairing of pretrained models} and no external rankings (such as separate test sets, e.g.\ due to data privacy), 
we investigate if it is possible to transfer such "complementary" knowledge from one model to another without performance degradation -- a task made particularly difficult as additional knowledge can be contained in stronger, equiperformant or weaker models. 
Yet facilitating robust transfer in scenarios agnostic to pretrained model pairings would unlock \textbf{training guidance, auxiliary gains and knowledge fusion} from any model repository without restrictions on model \& problem specifics - including from \textbf{weaker, lower-performance models}.
This work provides a first, in-depth exploration on the viability of such \textbf{general-purpose knowledge transfer}.
Across large-scale experiments, we first reveal the shortcomings of standard knowledge distillation techniques, and then propose a general extension via data partitioning for successful transfer between nearly all pretrained models - which can also be done \textbf{unsupervised}. 
Finally, we assess both the scalability and impact of model properties on successful model-agnostic knowledge transfer.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper investigates if it is possible to transfer complementary knowledge from one model to another without performance degradation. To this end, authors propose different heuristics to design how to switch the knowledge transfer between models. Experiments with various pairs of models demonstrate the effectiveness of the model-agnostic knowledge transfer.

### Strengths
1. The writing is clear and easy to follow.

2. There are consistent performance improvements compared to different types of baselines.

### Weaknesses
1. As addressed by the authors, different models are trained with different data augmentations, architectures and optimization techniques. The performance improvements are relatively marginal (e.g., Table 1), especially considering some models are not fully trained. The reported gains, while consistent, are often less than 1% on ImageNet. Given the variance in training procedures and model architectures, it's unclear if the observed improvements are truly due to the proposed knowledge transfer method, or simply a result of these other factors. The lack of control over these variables makes it difficult to isolate the specific impact of the knowledge transfer mechanism.

2. In Table 4, do the authors train all the variations with the same number of training steps? The sequential knowledge transfer may benefit from more training steps. Specifically, it is unclear if the 20 epochs for each sequential transfer is equivalent to the 20 epochs used in the single teacher setting. If the sequential transfer involves multiple 20 epoch steps, the total training budget is significantly higher, potentially skewing the comparison.

### Questions
See the weakness.

### Soundness
2 fair

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigates the phenomenon that different models have complementary information, reflected in their different predictions on each sample. Such complementary information could be due to model architectures, training settings, etc. Then the authors study how to transfer the complementary knowledge from a teacher model to a student model. The authors formulate this as a continual learning problem, which effectively improves upon the knowledge distillation baseline  and achieves better knowledge distillation on diverse models and ImageNet.

### Strengths
1. This paper identifies the "complementary knowledge" in different neural networks with grounded evidence. I think the claims are reasonable and well-supported.

2. The authors proposed improvement to the general knowledge distillation approaches from the continual learning perspective, including constraining the weight updates and transfer data. Both of the approaches are reasonable and straightforward to apply.

3. The authors conduct experiments on a wide range of models on ImageNet and show improvement with their improved continual knowledge distillation approach.

### Weaknesses
1. Present the key terms more clearly. For example, I haven't found the definition of transfer delta $\Delta_{transf}$, which is an important evaluation metric.

2. I think the proposed regularization, including the constraining of weight updates and transfer data, are some tricks for knowledge distillation. Although I don't work directly in knowledge distillation and I will wait for other expert reviewers to justify the novelty, I think the authors need to clarify more about their motivation or form a more explicit connection with continual learning. I also raised a question in the next section, elaborating my concerns.

3. I suggest the authors add some more experiments to make the arguments more thorough. Specifically, a more detailed breakdown of the accuracy numbers would help. For instance, (a) the percentage of [teacher correct, student wrong] samples are changed to correct answers after the distillation, (b) the percentage of [teacher incorrect, student correct] samples are changed to incorrect labels, to understand if the transfer is indeed complementary.

### Questions
1. Explain more about the terms. The readers are likely to have an ambiguous understanding of them, including: transfer delta $\Delta_{transf}$, "available complementary knowledge per class," and transfer rate.

2. I am wondering if the methods have to reason from the "continual learning" perspective. In my opinion, the regularization techniques proposed by the authors seem like generally applicable tricks for knowledge distillation. If any procedure involving multiple steps has to be treated as continual learning, maybe training a neural network with SGD is also a continual learning process? I hope the authors can clarify this motivation better in the paper.

3. See the third weakness above.

4. I suggest the author add an oracle study to strengthen the argument. In the examples (e.g. Table 1), the final improvement seems small in scale. To argue that this is actually challenging, the authors can run several ensembles of the teacher-student model and compare it to the improvement from knowledge transfer. Of course, I welcome other variants of similar analytical studies from the authors.

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
This paper studies general knowledge distillation (KD), where, given any two models, the student can infer missing information from the teacher model and potentially improve the performance. The authors begin with a comprehensive analysis showing that such complementary knowledge generally exists in any paired models regardless of model capacity or architecture, and existing KD methods cannot leverage the information that student models already carry, i.e., trained students. To this end, the authors propose a continual learning-based extension to the existing KD methods and a data partitioning scheme that, according to the highest prediction probability., simultaneously maintains the useful knowledge of students while learning from the teacher. The extensive experiments conducted on more than 400 models sufficiently verify the effectiveness and provide many insightful analyses.

### Strengths
1. The problem studied in this paper, i.e., general knowledge distillation, is interesting and practical. It bridges the gap in the existing literature that a trained student might degrade during the knowledge distillation process.

2. The additional analysis also indicates almost every model could benefit from the other teacher models, even if the teachers are weaker than the students. The result and the evaluation methodology may motivate the community for further research.

3. The proposed method is sound yet easy to implement in practice. The authors also consider different scenarios of distillation, including a single teacher and multiple teachers distilled in different ways/orders.

4. The large-scale analysis (over 400 models) validates the claim and provides various insights, such as the properties of student models.

### Weaknesses
1. The student models considered in this paper are relatively strong. As the authors claim **general** knowledge distillation, the readers will also be interested in the weaker models or even from scratch. However, the authors only consider powerful architectures, such as transformers or ResNet, in the paper. While the paper includes some smaller models, a more systematic study of very low-capacity models, or those initialized randomly, is missing. This limits the generalizability of the findings, particularly for resource-constrained scenarios.

2. The proposed method is slightly confusing to me. My understanding is that the proposed data partition is built upon the continual learning method since Figure 4(a) clusters KL-Dist + DP Transfer into continual learning. If so, the contribution of each component is not clear enough to me. Though some experiments, e.g., Figure 4(b), present the partition improves the MCL transfer, the contribution of the partition itself is not investigated in the experiments. Specifically, the exact mechanism by which the data partitioning interacts with the KL-divergence loss and the replay mechanism is not sufficiently clear. The lack of ablation studies on the partitioning strategy makes it difficult to determine its individual impact.

3 (Minor) Consistency of italic type. Some "KL+DP" are italics in the text, while some are not.

### Questions
1. What would happen if one applies the proposed method to weaker models, e.g., randomly initialized? I guess it will be degenerated to conventional KD methods. A specific section for weaker/smaller models would be interesting to the community of edge device users/researchers.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors provide an empirical study of the ability to transfer complementary knowledge between different pretrained models without performance degradation. This paper analyzes existing approaches in knowledge distillation and find it insufficient, especially in the case of distilling specific information from weaker teacher models. They go on to propose a data partitioning-based method (into regions of desired teacher behavior and desired student behavior retention) to achieve complementary knowledge transfer between the pretrained models considered in this paper.

### Strengths
1. The paper empirically shows that complementary knowledge exists between a large suite of models defined by different architectures and sizes (and even in weaker models that are less well performant than other stronger models). This complementary knowledge is localized to particular classes (what the authors deem as relative areas of expertise)

2. The authors propose a new data-partitioning approach to transfer complementary knowledge, where data is partitioned by which model has a higher probability of the ground truth class (or chosen simply by maximum probability in an unsupervised case).

3. Extensive experimental results that demonstrate that the proposed distillation approach transfers at a higher rate and transfers complementary knowledge from weaker teacher models.

4. The paper also studies different properties of student models that better allow for knowledge transfer.

### Weaknesses
Overall, I think the paper is quite comprehensive. A few points that may be lacking:

1. The results in studying properties of student models is a bit surprising to me. This isn’t a huge weakness, but more exploration of why CNN student models improve with scale and why transformer student models seem to worsen with would strengthen these results.

2. The data partitioning heuristic is reasonable, but some ablations on this approach would be more enlightening. Perhaps in some instances, the student model may be overconfident about particular data points (that either have incorrect labels or are inherently difficult examples to classify), and this data partitioning approach would maintain this overconfidence.

### Questions
1. Do you have any intuitions as to why student models that are CNNs exhibit better transfer at scale (while other architectures do not)? (Figure 8 in Supplement)

2. In Table 3, unsupervised DP outperforms supervised DP on several tasks. This seems a bit surprising; in the cases where these methods would be different, your DP approach would be distilling information from the teacher model on instances where the model is both quite confident and incorrect. Do you have an ideas about how this would be beneficial, and does this match your intuitions as to why this method works in general?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent
