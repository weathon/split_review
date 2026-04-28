# Rethinking Out-of-Distribution Detection on Imbalanced Data Distribution

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
Detecting and rejecting unknown out-of-distribution (OOD) samples is critical for deployed neural networks to void unreliable predictions.
In real-world scenarios, however, the efficacy of existing OOD detection methods is often impeded by the inherent imbalance of in-distribution (ID) data, which causes significant performance decline.
Through statistical observations, we have identified two common challenges faced by different OOD detectors: misidentifying tail class ID samples as OOD, while erroneously predicting OOD samples as head class from ID.
To explain this phenomenon, we introduce a generalized statistical framework, termed \mmethod, to formulate the OOD detection problem on imbalanced data distribution.
Consequently, the theoretical analysis reveals that there exists a class-aware \textit{bias} item between balanced and imbalanced OOD detection, which contributes to the performance gap.
Building upon this finding, we present a unified training-time regularization technique to mitigate the bias and boost imbalanced OOD detectors across architecture designs.
Our theoretically grounded method translates into consistent improvements on the representative CIFAR10-LT, CIFAR100-LT, and ImageNet-LT benchmarks against several state-of-the-art OOD detection approaches.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The main contribution of this paper is the introduction of a generalized statistical framework called ImOOD, which addresses the problem of detecting and rejecting unknown out-of-distribution (OOD) samples in the presence of imbalanced data distributions. The paper identifies two common challenges faced by existing OOD detection methods: misclassifying tail class in-distribution (ID) samples as OOD, and incorrectly predicting OOD samples as head class ID samples. Then, the authors propose a general framework that can lead to improved detection performance.

### Strengths
The paper introduces a generalised statistical framework called ImOOD, which addresses the problem of OOD detection in the presence of imbalanced data distributions. Imbalanced data distributions widely exist in real world, and a set of fundamental works have proposed to tackle this questions to boost OOD detection. It seems that there may still exist many open questions, making the research direction in this paper promising in OOD detection. 

The paper identifies two common challenges faced by existing OOD detection methods, namely misclassifying tail class ID samples as OOD and incorrectly predicting OOD samples as head class ID samples. This identification helps in understanding the limitations of current approaches.

The proposed method  is driven by the Bayesian analysis, demonstrating the impacts of data imbalance and suggesting a general framework that can handle the distribution shift in OOD detection. The proposed framework, as claimed by the authors, can be used to handle imbalanced issue for a set of different scoring strategies, and the evaluation results further verify the power of their method against imbalance data more or less.

### Weaknesses
A direct question is that if we have used learning algorithms that can handle imbalanced data (which is often the case in reality) to train the basic model, do we need to handle imbalanced data for OOD detection thereafter. 

The authors identify two cases that make previous OOD detection methods fail, i.e., misclassifying tail class ID samples as OOD and incorrectly predicting OOD samples as head class ID samples. It is a direct conclusion and seemingly to be important, but could the authors further connect these two cases to previous works that handle imbalanced data in OOD detection and the proposed ImOOD. For example, why previous works, such as [1], will fail to discern these two cases and why ImOOD can overcome previous drawbacks. 

g should be defined in a proper position in advance. It seems that g should be the detector built upon f.

My main concern lies in the inaccurate estimation of beta, consisting of three terms that are all biased from my view. For P(i|X), a direct failure case is that when we have a detector whose g always greater than 0 (e.g., for distance based scoring), then P(i|X) will be always greater than 0.5. Thus, all data points will be taken as ID cases, making the estimation obviously a biased case. P(y|x,i) also suffers from biased estimation, due to the well known calibration failure of deep models. Such an issue, from my view, cannot be ignored in the field of OOD detection, since it is one of the main reason why MSP score is not effective in practice. The estimation of P(y) is also biased, since the training time data distribution (ID + OOD) is different from the test situation, thus n_o used for training cannot cover the real test situation. 


Detailed discussion about the hyper-parameters setting and the choice of auxiliary OOD data and the evaluation datasets should be discussed in detailed. More methods that handle OOD detection with imbalanced data should be considered here, such as [1]. More ablation studies to test the respective power of P(i|x), P(y), and P(y|x) should be tested.

### Questions
Please see the Weaknesses.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
To tackle the OOD detection under class imbalanced setting, the paper proposed the statistically guided framework called ImOOD. Through the statistical analysis, the authors have found that there exists a bias term responsible for the performance gap between balanced and imbalanced OOD detection models. Under the ImOOD framework, by leveraging the bias term, the authors then propose the post-hoc normalization and training time regularization technique to enhance the OOD performance. The experimentation conducted on multiple real-world datasets demonstrates the effectiveness of the proposed post-hoc normalization and training time regularization techniques.

### Strengths
* The motivation for proposing the ImOOD framework is clear. The authors have done a great job in terms of empirically demonstrating the limitations present in existing OOD detection techniques under imbalanced data distribution. For example,  Figure 1 demonstrates how OOD samples are incorrectly detected as head class samples and that of the in-distribution tail class samples as OOD samples. 
* The proposed post-hoc normalization and training time regularization are backed by the strong statistical analysis conducted in Section 3.1 along with empirical evidence.
* The paper is well-written and easy to follow. 
* An extensive ablation study is conducted to showcase the effectiveness of each component in their proposed framework. For example, in Table 4 the authors have shown how the estimation of the class-prior in the training-time regularization helps to improve the performance.

### Weaknesses
 * The authors have used the auxiliary OOD training dataset and its effect on performance is not very clear. It would be interesting to see the sensitivity of the OOD performance with respect to the selection of different OOD training data. For example, what does the performance look like if we use the Cifar100 as OOD data for the model with Cifar10 as ID data? 
* The authors may need to report the performance of the wide range of OOD detection methods to demonstrate the effectiveness of their proposed post-hoc normalization and training time regularization. For example, the authors may consider the most representative OOD techniques like OpenMAX [1], CGDL [2], OLTR [3], etc.
* The performance gain using the post hoc normalization seems to be marginal on OE and BinDisc, especially in terms of AUROC and AUPR. Having a more detailed explanation for this would be useful.

### Questions
It would be interesting to see the experimental results mentioned in the weaknesses section.

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
When encountering inherent imbalance of in-distribution (ID) data, the paper identified two common challenges faced by different OOD detectors: misidentifying tail class ID samples as OOD, while erroneously predicting OOD samples as head class from ID. To explain this phenomenon, the authors introduce a generalized statistical framework, termed ImOOD, to formulate the OOD detection problem on imbalanced data distribution. Consequently, the theoretical analysis reveals that there exists a class-aware bias item between balanced and imbalanced OOD detection, which contributes to the performance gap.

### Strengths
1. The paper is written well and is easy to understand.
2. The studied problem is very important.
3. The results seem to outperform state-of-the-art.

### Weaknesses
1. I am curious about the possibility of this method being extended to distance-based OOD detection methods, such as Mahalanobios distance, etc. How well does the current method compare to the state-of-the-art distance-based methods?
2. I am curious about how well the current method performs on synthesized outliers (Tao et.al. 2023).
3. Could you elaborate more on a closely related baseline, Jiang et al. 2023, and discuss the similarities and differences w.r.t your work?

### Questions
see above

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies the problem out-of-distribution (OOD) detection when original in-distribution (ID) data suffers from class imbalance. The authors first report an experimental observation regarding two major challenges in OOD detection under the studied setting: misidentification of tail-side ID samples as OOD (False positives) and of some OOD samples as head-side ID (False negatives). They then statistically compare the learning objectives in OOD detection with class-balanced vs. -imbalanced ID data, allowing them to attribute these challenges to the auxiliary bias term that does not cancel out in the class-imbalanced scenario. Based on this analysis, they propose two unique avenues to mitigate the influence of this bias term: post-hoc normalization and train-time regularization. Together, they form a cohesive framework for OOD detection with class-imbalanced ID data, dubbed ImOOD. The authors provide substantial empirical evidence for the effectiveness of ImOOD.

### Strengths
- The statistical analysis performed in the paper is sound and written in a manner that is easy to follow. The authors include a helpful intuitive understanding of the bias term that connects it back to the empirical observations about the behavior of OOD detection models under the class-imbalanced setting.
- ImOOD is well-motivated and theoretically-grounded on the the above analysis. The general thinking behind the method is sound, and for the most part, it’s described clearly enough to understand and re-implement the design.

### Weaknesses
 - I believe the major drawback of this paper lies in the limited scope of the studied problem. It appears that the authors assume that the class-imbalance problem only exists on the original ID dataset. I am not too convinced with the practicality of the proposed scenario; it’s hard to imagine in what deployment scenarios only the ID dataset will suffer from this problem, while the OOD dataset(s) used for training/testing is void of it. Wouldn’t it be more natural to assume that the ID training dataset can be refined in advance to make it class-balanced, while the OOD data the detector must be able to identify arise in various forms, and thus is more likely to be class-imbalanced?
    - What if the auxiliary OOD dataset used for training and/or the target OOD dataset exhibits class-imbalance as well? I think it is important to study various combinations of class-balanced and -imbalanced ID/auxiliary OOD/target OOD datasets. Does the analysis performed in the paper extend to and hold in such settings? Can ImOOD still outperform other baselines?
- Please correct me if I am wrong, but it appears that the verification of post-hoc normalization (minus the train-time regularization) on larger datasets appears to be missing. Even on CIFAR10-LT, the improvement from post-hoc normalization seems marginal, but this concern could be alleviated, as long as the improvement is consistent across various datasets. If post-hoc normalization is not quite as effective on datasets, it would signify that ImOOD is heavily reliant on the train-time regularization.
- More details on how the label distribution is learned (during test-time regularization) would be appreciated. Also, do you use the same learned label distribution when performing post-hoc normalization? Or is it used only for training-time regularization? If you discard it after training, one would have to know the label distribution anyways for post-hoc normalization, so do we really need to use the learned distribution in the first place?
- The empirical validation is limited to one target OOD dataset per InD dataset. Validation on more challenging OOD datasets (e.g., near OOD data, data with spurious correlation) would be helpful to gauge the effectiveness of the proposed method.

### Questions
Please refer to the Weaknesses section.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
