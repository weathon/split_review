# Candidate Label Set Pruning: A Data-centric Perspective for Deep Partial-label Learning

- Decision: Accept
- Avg Score: 8.00
- Scores: 8, 8, 8, 8

## Abstract
Partial-label learning (PLL) allows each training example to be equipped with a set of candidate labels. Existing deep PLL research focuses on a \emph{learning-centric} perspective to design various training strategies for label disambiguation i.e., identifying the concealed true label from the candidate label set, for model training. However, when the size of the candidate label set becomes excessively large, these learning-centric strategies would be unable to find the true label for model training, thereby causing performance degradation. This motivates us to think from a \emph{data-centric} perspective and pioneer a new PLL-related task called candidate label set pruning (CLSP) that aims to filter out certain potential false candidate labels in a training-free manner. To this end, we propose the first CLSP method based on the inconsistency between the representation space and the candidate label space. Specifically, for each candidate label of a training instance, if it is not a candidate label of the instance's nearest neighbors in the representation space, then it has a high probability of being a false label. Based on this intuition, we employ a per-example pruning scheme that filters out a specific proportion of high-probability false candidate labels. Theoretically, we prove an upper bound of the pruning error rate and analyze how the quality of representations affects our proposed method. Empirically, extensive experiments on both benchmark-simulated and real-world PLL datasets validate the great value of CLSP to significantly improve many state-of-the-art deep PLL methods.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper pioneers a data-centric study for the problem of partial-label learning (PLL) where each training instance is assigned with some additional false candidate labels along with its true label and proposes a new PLL related task named candidate label set pruning (CLSP) that aims to filter out false candidate labels of the training PLL data. To this end, the paper proposes the first kNN-based CLSP method that eliminates candidate labels of each training instance which have the high “down votes” from its kNN instances. Theoretically, the authors prove an upper bound of the pruning error and analyze the effect of representation quality and candidate generation against it. Empirically, after training with the pruned data, existing PLL algorithms have a significant performance improvement, which validates the effectiveness of the proposed method.

### Strengths
-	The proposed task CLSP is very significant and novel in PLL. Instead of studying learning-centric training algorithms, the authors take a different path to study filtering out false candidate labels before the training of networks, which improves the labeling quality of training PLL data and boosts the performance of existing PLL algorithms.          

-	The proposed CLSP method is simple but effective, achieving impressive empirical results on various PLL settings (random, LD, ID), benchmarks (CIFAR, Tiny-ImageNet, and VOC), and ten PLL algorithms.

-	The theoretical analysis of the pruning error is very interesting. The findings in the numerical simulation experiment achieve a good guidance for the selection of parameters k and tau in the practical employment.

### Weaknesses
- More empirical analysis in the experiment should be presented, such as which PLL algorithms are more sensitive to the pruning method. Specifically, it would be helpful to see a breakdown of performance improvement for each of the ten PLL algorithms after applying the proposed Candidate Label Set Pruning (CLSP) method. This would provide a better understanding of the method's effectiveness across different types of PLL algorithms, categorized, for instance, by whether they are considered naive or advanced approaches. Furthermore, a more detailed analysis of the relationship between the degree of pruning and the performance gain for each algorithm could illuminate potential trade-offs or limitations.

- More explanations on bad cases are needed to show the limitation of the proposed method. While the overall results are promising, a deeper dive into instances where performance degrades after pruning is crucial. For example, analyzing the characteristics of the data points or the specific settings in which these cases occur could reveal underlying factors that contribute to the negative impact. This analysis should include a discussion of whether the degradation is due to over-pruning, inherent limitations of the kNN approach in certain data distributions, or other factors. It is also important to quantify the frequency and severity of these bad cases to provide a balanced view of the method's robustness.

### Questions
-	How about pruning on noisy PLL data? I am curious about whether the proposed method could be used on noisy PLL data whose true label is outside the candidate label set.

-	I find some bad cases in the experiment (shown in Table 1 and Table 8) where the performance drops after pruning. How to explain this phenomenon? 

-	Could you show the values of delta_k and pho_k on the real-world dataset VOC (which are not shown in Figure 3)?

-	A unified proportion tau for each training instance is used in Eq. (2). Are there other ways to adaptively control the number of eliminated candidate labels for each training instance?

Overall, it is a good work on PLL, but there are still minor issues that can be further improved. I may consider increasing my score if the above listed weaknesses and questions can be clearly addressed.

### Soundness
3 good

### Presentation
3 good

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
The paper involves the partial label learning problems where each training example is equipped with multiple candidate labels instead of the only one ground-truth label provided in the conventional supervised learning setup. The paper proposes an innovative task to assistant partial label learning, i.e., candidate label set pruning, which targets at removing false candidate labels of each training example. The proposed pruning approach leverages the inconsistency of representation and label spaces to select certain candidate labels being abandoned beforehand.

The authors prove that the pruning error is upper bounded by the representation quality, the process of candidate label generation, and the pruning proportion. Moreover, they perform a numerical simulation experiment to empirically show how these factors affects the upper bound, which provides a practical guidance for selecting parameters k and $\tau$ in the proposed approach. 

The paper conducts comprehensive experiments on various datasets CIFAR-10, CIFAR-100, Tiny-ImageNet, and PASCAL VOC with different settings of partial label learning including uniform -, label-dependent -, and instance-dependent candidate label generation. Besides, ten state-of-the-art partial label learning algorithms are used to compare the performance improvement. The overall experiment results show that the pruning approach enables these algorithms have a great performance gain specially on more difficult settings.

### Strengths
1.	Originality. The originality of the paper lies in the proposed task candidate label set pruning and the corresponding approach for the task. For what I can tell, it is the first work to propose the task for partial label learning. Moreover, the idea of leveraging the inconsistency of representation and label spaces to filter out candidate labels is also novel.

2.	Quality. The approach proposed in the paper makes both theoretical and technical contributions. The theoretical analysis of the upper bound is very interesting. The proposed approach is technically sound, which is validated by significant performance improvements in the experiment.

3.	Clarity. The paper is well organized and easy to understand the motivation. The related work is introduced adequately. The proposed task candidate label set pruning has a formal clear definition (definition 1). 

4.	Significance. The paper brings a new data-centric view for the area of partial label learning, which is significant for the development of partial label learning. Perhaps, more attention of researchers could be shifted from designing complex training methods to studying efficient pruning methods.

### Weaknesses
1.	The numerical simulation experiment about the calculating of values and conclusions is not shown clearly enough.

2.	The PASCAL VOC dataset used in the experiment is not introduced well, as the dataset is not originally for partial label learning.

3.	Detail of trained feature extractors (ResNet-SSL, ResNet-S) is shown unclearly.

### Questions
1.	It would be appreciated if a clearer explanation for Definition 2 is provided. Why is this Definition needed?

2.	How are these values of k and $\gamma_{i}$ calculated in Figure 1? 

3.	Why does the loss curve on VOC in Figure 5 have a rise (except PRODEN algorithm)? This phenomenon is different from other cases on CIFAR and Tiny-ImageNet datasets.

4.	How is the PASCAL VOC dataset used for partial label learning algorithms?

5.	What is the potential limitation of the proposed approach? Discussing this point is also important to have a comprehensive understanding for the proposed approach.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on partial label learning, a paradigm of weakly supervised learning, and proposes a training-free method that prunes candidate label sets based on the inconsistency between the representation space and the candidate label space. In particular, when examining each potential label associated with a training instance, if it is not among the candidate labels of the instance's closest neighbors in the feature space, there is a notable likelihood of it being an erroneous label. Theoretically, it provides an upper bound of the per-example pruning error rate and analyzes how the representation quality affects the proposed algorithm.

### Strengths
Strengths:
1. Different from the previous learning-centric PLL methods, the method of this paper is proposed from a data-centric perspective, which is novel. 
2. The paper theoretically provides an upper bound of the per-example pruning error rate and analyzes how the representation quality affects the proposed algorithm, which is solid.
3. The proposed method is easy to understand and implement.
4. The paper conducts extensive experiments on various settings of PLL.

### Weaknesses
Weaknesses:
1. My major concern is that the proposed method will transform a PLL problem into an UPLL problem, which is more challenging due to the existence of the correct label may not be guaranteed in the candidate label set. Although it provides an upper bound of the per-example pruning error rate, the negative impact of eliminating the correct label from the candidate label set is still unknown. Specifically, the paper does not explore the trade-off between reducing noisy labels and the risk of removing the true label, which is critical for the practical application of the method.
2. The proposed method is dependent on the KNN algorithm, which should be given more details in the main body of the paper. For example, it could be found in the appendix that the KNN algorithm are implemented on the output of a feature extractor. However, what the feature extractor comes from is unknown. The paper should clarify whether this feature extractor is pre-trained or trained on the target dataset, as this has a significant impact on the training-free claim of the method. Furthermore, the choice of distance metric in KNN and its impact on the pruning performance should be discussed.
3. [1] also attempts to filter out the incorrect candidate labels, which is suggested to be considered in related works, and even experiments.

### Questions
1.What is the main difference between a data-centric method and a pre-processing method?

2.Does the feature extractor in the KNN algorithm come from the classifier during the training process? If yes, it seems unreasonable to say that the method is training-free. If not, a pre-trained model should be introduced.

### Soundness
3 good

### Presentation
3 good

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
This paper present a novel insight into PLL from the perspective of candidate label set pruning (CLSP), and propose the first CLSP method based on a "down-vote" kNN. The authors also theoretically analyze the effects of the feature quality and label ambiguity against the pruning error. Extensive experiments are conducted on various datasets to validate the superiority of CLSP.

### Strengths
This paper is fresh to PLL community from a data prunning perspective, and propose the first candidate label set pruning (CLSP) method based on kNN. The theorectical analysis of the prunning error is reasonable and the comprehensive experimental results validate the effectiveness of the proposed method. The paper is well organized and the expressions are clear. This work is excellent, and will inspire many researchers in PLL community.

### Weaknesses
No big problem, only some minor issues, such as, typo, vague expression, and missing reference.

1. A small typo? I guess the author may forget to divide n in the formulation of \beta in Definition 1, as \beta does not equal to 1 but n in the optimal pruning case. Can author clarify that?
2. It is vague to describe PLL in the abstract that "Partial-label learning (PLL) allows each training example to be equipped with a
set of candidate labels." Does the author intentionally ignore the assumption that "only one is the ground-truth label"? It is better to clarify as some PLL research wave the limitation to investigate a new PLL task (called Unreliable or Noisy PLL).
3. Some state-of-art PLL methods are missing in the reference, such as, A Unifying Probabilistic Framework
for Partially Labeled Data Learning; Mutual Partial Label Learning with Competitive Label Noise.

### Questions
1. A small typo? I guess the author may forget to divide n in the formulation of \beta in Definition 1, as \beta does not equal to 1 but n in the optimal pruning case. Can author clarify that?
2. It is vague to describe PLL in the abstract that "Partial-label learning (PLL) allows each training example to be equipped with a
set of candidate labels." Does the author intentionally ignore the assumption that "only one is the ground-truth label"? It is better to clarify as some PLL research wave the limitation to investigate a new PLL task (called Unreliable or Noisy PLL). 
3. Some state-of-art PLL methods are missing in the reference, such as, A Unifying Probabilistic Framework
for Partially Labeled Data Learning; Mutual Partial Label Learning with Competitive Label Noise.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent
