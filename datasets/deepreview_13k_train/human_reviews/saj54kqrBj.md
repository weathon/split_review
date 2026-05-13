# Self-Tuning Self-Supervised Anomaly Detection

- Decision: Reject
- Scores: 5, 6, 6

## Abstract
Self-supervised learning (SSL) has emerged as a promising paradigm that presents supervisory signals to real-world problems, bypassing the extensive cost of manual labeling. Consequently, self-supervised anomaly detection (SSAD) has seen a recent surge of interest, since SSL is especially attractive for unsupervised tasks. However, recent works have reported that the choice of a data augmentation function has significant impact on the accuracy of SSAD, posing augmentation search as an essential but nontrivial problem with the lack of labeled validation data. In this paper, we introduce ST-SSAD (Self-Tuning Self-Supervised Anomaly Detection), the first systematic approach for rigorous augmentation tuning on SSAD. To this end, our work presents two key contributions. The first is a new unsupervised validation loss that quantifies the alignment between the augmented training data and the (unlabeled) test data. Second, we present new differentiable augmentation functions, allowing data augmentation hyperparameter(s) to be tuned end-to-end via our proposed validation loss. Experiments on two testbeds with semantic class anomalies and subtle industrial defects show that a systematic tuning of augmentation gives significant performance gains over current practices. All our code and testbeds are available at https://anonymous.4open.science/r/ST-SSAD.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces ST-SSAD, a novel approach for self-supervised anomaly detection (SSAD). It addresses the challenge of selecting proper data augmentation functions to generate pseudo-anomalies that are close to real anomalies. ST-SSAD offers two main contributions: an unsupervised validation loss using an unlabeled test dataset for tuning augmentation and differentiable augmentation functions for end-to-end hyperparameter tuning. Experimental results on two testbeds demonstrate performance improvements through the systematic augmentation tuning.

### Strengths
- The paper addresses the challenge of end-to-end augmentation tuning in SSAD. 
- The idea of employing differentiable augmentation, such as CutDiff, is interesting and demonstrates potential applicability to other domains beyond anomaly detection.  
- The paper is well organized and clearly written overall.

### Weaknesses
 - A major concern is that ST-SSAD replies on the entire test dataset during training and tuning. While the authors mention transductive learning, this approach is not quite realistic, particularly in the context of anomaly detection. The tuning result will be overly sensitive to the specific anomaly types in the test data and may not generalize well. The paper lacks clarification, experimental results, or in-depth discussion on this issue, which significantly limits the applicability and advantages of the proposed method.    

- The mean distance loss is proposed for ratio invariance with theoretical properties, but no experimental result validating this invariance is provided. 

- The method still requires prior knowledge about anomalies and heavily depends on it. For example, the augmentation functions of either local (CutDiff) or global (rotation) augmentations are considered and therefore, it works well only when anomalies closely resemble specific shapes that these functions can reflect. The method will also fail in the case where rotated samples are considered normal. 

- The authors state that 'we focus on the performance of each anomaly type rather than overall accuracy.' However, in real-world scenarios, it is common to encounter various types of anomalies. Therefore, it will be more crucial to investigate such practical scenarios. 

- It was mentioned that "there are no direct competitors on end-to-end augmentation hyperparameter tuning..."; however, it is essential to include performance comparison with the latest models that clearly distinguish train and test data. The results in Tables 1 and 2 appear to be more like an ablation study, so it is difficult to assess whether the proposed method truly outperforms the latest models in a meaningful way.

### Questions
- Can you provide results using a validation set that is disjoint from the test set? 

- I guess the proposed method may be quite sensitive to the proportion of abnormal samples in the test set. Can you provide experimental results or a discussion addressing this issue? And please provide the ratio between normal and abnormal samples in the presented results of the current manuscript. 

- Is it possible for the model to learn effectively in a scenario where abnormal samples are inherently present in the training set but remain unlabeled?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose learnable augmentations for transductive anomaly
detection.  In the transductive scenario, the test set, including
anomalies to be detected, are available for training.  They called
their method Self-Tuning Self-Supervsied Anomaly Detection (ST-SSAD).
The augmentations help simulate anomalies.  Using the proposed
validation loss, ST-SSAD tries to make the original training instances
together with their augmentations, similar to the test set.  The
validation loss is based on the distance, in the representation space,
between each test instance and the mean of training instances, as well
as the mean of augmented instances.  Instances in representation space
are transformed to have unit total pairwise squared distance.  Binary
cross entropy loss is used as the training loss.  For learnable
augmentations, they proposed differentiable CutDiff (local
augmentation) and rotation (global augmentation).

ST-SSAD was compared with multiple baseline algorithms on two datasets
with different types of anomalies. Empirical results indicate ST-SSAD
generally outperforms the baselines.  Ablation studies indicate the
proposed components of ST-SSAD contribute to higher performance.

### Strengths
Allowing augmentations to be learnable/differentiable is interesting.
Examples were presented to show augmentations can match anomalies.
Empirical results indicate ST-SSAD generally outperforms the
baselines.  The paper is generally well written.

### Weaknesses
During evaluation, each anomaly type is separated.  The proposed
ST-SSAD seems to assume only one anomaly type exists in the test set.
That is, the user might need to use ST-SSAD for each anomaly type.
How to handle multiple anomaly types in the same test set is not
clear.

Details are in questions below.

### Questions
1.  In the experiments, anomaly types are separately evaluated.  That
seems to mean that the anomaly type is known, and the augmentation
parameters are learned to match the anomaly type.  This seems to be
assumed in Equation 3 because the second term calculates the mean of
the augmented instances.  That is, Eq. 3 seems to be finding an
augmentation and its parameters to match the anomaly type.  If that is
correct, how can multiple types of anomalies in the same test set be
handled?

2.  While the augmentation parameters are learnable, the augmentation
types such as cut and rotation need to be specified.  Also, to be
detected, seemingly an anomaly type in the test set needs to match one
of the augmentation types.  Could the matching be relaxed?  That is,
the user potentially does not need to know what the anomaly types are.

3.  What is the size of $D_{aug}$?

4.  Eq 2, equation on the right for $z_i^c$: should $z$ be $z_i$ and
the summation is over another index such as $j$ to not confuse with
$i$?

5.  Eq 3: mean(.) seems to be similar to $1/N\sum_{i=1}^{N}z_{i}$ in
Eq 2.  If so, using mean(.) in Eq 2 would make the presentation
consistent.  If not, what is the difference?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper mainly studies an adaptive method to search the optimal data augmentation function for self-supervised anomaly detection task. It formulates the learning of potential abnormal distribution (i.e. true anomaly-generating mechanism) as a second-order optimization problem. To this end, two aspects are mainly studied: (1) a new validation loss for differentiable distribution matching of augmented training data and the unlabeled testing anomalies; (2) some differentiable augmentation functions for optimizing their learnable control factors and detector parameters alternatively. Experiments on both semantic and non-semantic anomalies demonstrates the effectiveness.

### Strengths
- This paper is well-motivated and clearly presented. Researchers could gain a lot of insight into this paradigm and the potential impact on discriminative learning with synthetic anomaly is significant. Besides, the authors provide theoretical evidence and clear illustrations for better understanding, including their idea, method and some demonstrative examples.

- The optimal augmentation function seems to alleviate the limitation and difficulty of artificially synthesized pseudo anomalies, due to the better consistency with real anomalies. 

- The parameters are optimized during end-to-end training, which is feasible and ideal.

### Weaknesses
 - My major concern of this paper lies in the strong assumption, here are a couple of aspects:

1.	The authors evaluate MV Tech AD with the data being collected according to given abnormal patterns. I wonder if the proposed framework can simultaneously deal with multiple different augmentations, since this case is more general in real-world anomaly detection scenarios and is more likely to avoid overfitting to the optimal **a**. It will be helpful to show the results with **UN**split original classes in MV Tech AD.

2.	The assumption that the validation and test distributions are consistent may be too strong for the setting of anomaly detection task (*e.g.* new anomaly pattern or even mixing anomalies makes **a** not optimal). It may not be reasonable to omit test images drawn from unseen distributions in real scenarios.

- The author believes that the heuristic function $S$ will be high (higher variance of anomaly scores) *only if* augmentation parameters are initialized better (more separable distributions). However, this may not always hold, as the optimization of a mismatched *strong/hard* augmentation (as long as the decision boundary divides testing distribution into any two parts) may also lead to high variance of anomaly scores. I wonder if there are any theoretical or intuitive explanations about this issue.

- The authors use CutDiff and Rot for non-semantic and semantic shift detection respectively. But I would like to know could ST-SSAD learn zero-angle Rot for non-semantic defects and zero-size CutDiff for semantic shifts in end-to-end optimization when using both augmentations together.

- The term ``Ratio invariance’’ may be imprecise. With the augmentation quantity changed, $L_{val}$ could be changed together because the included $\frac{\sqrt{N}}{{\Vert {Z}^{c}\Vert}_{F}}$ is different (I notice that this have no negative impact on optimization target).

- There are some writing issues, *e.g.* superscript $^{n}$ should be $^{a}$ in **Lemma 2**.

### Questions
Please refer to the "weaknesses" part for details.

### Soundness
1 poor

### Presentation
3 good

### Contribution
3 good
