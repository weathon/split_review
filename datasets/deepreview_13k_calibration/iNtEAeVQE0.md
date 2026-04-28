# DISK: Domain Inference for Discovering Spurious Correlation with KL-Divergence

- Decision: Reject
- Avg Score: 3.75
- Scores: 3, 3, 6, 3

## Abstract
Existing methods utilize domain information to address the subpopulation shift issue and enhance model generalization. However, the availability of domain information is not always guaranteed. In response to this challenge, we introduce a novel end-to-end method called DISK. DISK discovers the spurious correlations present in the training and validation sets through KL-divergence and assigns spurious labels (which are also the domain labels) to classify instances based on spurious features. By combining spurious labels $y_s$ with true labels $y$, DISK effectively partitions the data into different groups with unique data distributions $\mathbb{P}(\mathbf{x}|y,y_s)$. The group partition inferred by DISK then can be seamlessly leveraged to design algorithms to further mitigate the subpopulation shift and improve generalization on test data. Unlike existing domain inference methods,  such as ZIN and DISC, DISK reliably infers domains without requiring additional information. We extensively evaluated DISK on different datasets, considering scenarios where validation labels are either available or unavailable, demonstrating its effectiveness in domain inference and mitigating subpopulation shift. Furthermore, our results also suggest that for some complex data, the neural network-based DISK may have the potential to perform more reasonable domain inferences, which highlights the potential effective integration of DISK and human decisions when the (human-defined) domain information is available. Codes of DISK are available at [https://anonymous.4open.science/r/DISK-E23A/](https://anonymous.4open.science/r/DISK-E23A/).

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents an approach called DISK for domain inference. Specifically, the DISK approach infers domains by finding a dataset partition that maximizes the predictive difference between the training set and a validation set. The spurious correlation differs between the training and validation sets.

### Strengths
This paper tried to tackle an important and extremely challenging problem: domain inference without any domain information.

### Weaknesses
1. The assumption of a validation dataset does not seem weaker than an assumption on auxiliary information. This paper assumes that the spurious correlation in the training set does not hold in the validation dataset. Without explicitly knowing the spurious correlation, the construction of such a validation set is non-trivial.

2. The motivation behind the KL maximization objective (Equation 2) is unclear. This objective aims to maximize the label distribution difference between inferred domains, but the spurious correlation does not necessarily relate to the label distribution. For example, one domain may have 50% red zero digits and 50% blue one digits, and the other domain has 50% blue zero digits and 50% red one digits. Here, the label distribution is the same for the two domains.

3. The definition of spurious label is confusing. Definition 1 states that a spurious label indicates the category of an instance. However, the abstract says that the spurious label is also the domain label. The domain label does not indicate the category of an instance.

4. The steps of the proposed approach are not described. How do we get the spurious label $y_s$ from $f_{DISK}$?

5. The experiment section seems incomplete. Is IRM inapplicable to the MNIST and CIFAR experiments?

### Questions
1. Is there any particular reason to use KL divergence in your algorithm? There are many other candidates such as Wasserstein distance.

2. What is the performance of baselines under the DISK setting? Here, we can use the training set and the validation set as two domains. No exact domain information is needed.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors study the problem of tackling spurious correlations during supervised learning, in the setting where spurious labels are not known during training. They propose a method to infer the spurious label given a validation set where spurious correlations differ, which can then be used in a second stage training to learn an unbiased model (e.g. with subsampling). Their method involves learning some spurious label that maximizes mutual information with the class label on the training set, while having the maximum divergence when conditioned on with the validation set. They evaluate their method on a variety of datasets, finding that they outperform the baselines.

### Strengths
- The paper tackles an important real-world problem.
- The proposed method is intuitive.
- The paper is well-written and easy to understand.

### Weaknesses
1. The authors should formally state some of the assumptions required for the method to learn the correct spurious label. It seems like the assumption informally is that the true spurious label is the feature that is strongly correlated with the label while giving the maximum divergence on the validation set. If this is the case, how would the method behave in the presence of multiple spurious correlations [1]? Specifically, it is unclear how the method would differentiate between multiple spurious features that each exhibit strong correlations with the label and varying divergences on the validation set. The method might latch onto a single spurious feature while ignoring others, leading to suboptimal performance.

2. The authors should empirically and theoretically characterize how different the validation dataset has to be from the training dataset in order for the method to effectively learn the spurious label. The current analysis lacks a rigorous exploration of the sensitivity of the method to the degree of distribution shift between the training and validation sets. It is crucial to understand the limitations of the method when the validation set is not sufficiently different from the training set in terms of spurious correlations. For instance, if the spurious correlations are only slightly different, will the method still be able to identify the correct spurious label?

3. The proposed method assumes access to an unlabelled validation set with different spurious correlations from the training, which is not a very strict assumption. However, the method also implicitly assumes prior knowledge of the number of possible values that the spurious correlation can take, in order to learn $w$. Prior methods like JTT [2] do not have this assumption. This assumption could limit the applicability of the method in scenarios where the number of spurious correlations is unknown or very large. The method's reliance on a predefined number of spurious labels is a potential limitation.

4. The authors should compare against more baselines which also do not require knowledge of the spurious label during training, such as JTT [2] or CnC [3]. They should also compare both performance and identified minority groups against prior group discovery method such as EIIL. The lack of comparison with these methods makes it difficult to assess the relative strengths and weaknesses of the proposed approach. It is important to demonstrate that the proposed method offers advantages over existing methods that also address spurious correlations without requiring group labels.

5. The authors should evaluate their method on additional benchmarking datasets in the NLP domain such as MultiNLI and CivilComments. The current evaluation is limited to image datasets, and it is unclear how well the method would generalize to other domains, particularly NLP, where spurious correlations can manifest differently. Evaluating on NLP datasets would provide a more comprehensive assessment of the method's robustness.

6. The proposed metric (Definition 2) seems a bit flawed, as the model could infer very few minority samples to get a high value. The authors should consider using a metric that balances precision and recall such as the intersection-over-union, and also reporting the inference accuracy. The current metric might not accurately reflect the model's ability to identify minority samples, as it could be biased towards models that predict very few samples as minority, even if those predictions are not accurate.

### Questions
Please address the weaknesses and answer the following questions:
1. What was the strategy for hyperparameter selection (i.e. to find the hyperparameters in Table 3)? Presumably, this requires access to a labelled validation set?

2. What was the validation set used in each of the datasets? How different were they from the training set?

3. How sensitive is the method to the choice of $\gamma$? The authors should consider showing the WGA when sweeping over this hyperparameter.

4. Have the authors tried additional methods for the 2nd stage other than subsampling, such as GroupDRO? Does this improve performance further?

5. In Figure 3, second row, it might be clearer to additionally report the accuracy of the classifier in distinguishing the spurious correlation, as that is what matters the most in this row.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
To address subpopulation shift without domain information, the authors propose DISK, a novel and effective end-to-end method for domain inference. The advantages are demonstrated on some datasets.

### Strengths
1. This work is relatively solid. Details of necessary proofs and experiments are attached
2. The authors focus on domain inference, providing insights on domain inference, illustrating that when spurious features contain complex information. The comparison of the neural network-based DISK and human decisions on potential to capture the essence of the data is also discussed.
3. Experiments are relatively well-designed, including the experiments on synthetic 2D data and real-world data.

### Weaknesses
1. The available and details could be discussed in more detail. The label or domain is the core of this work. When the data is labeled with this information, some carry it, and none carry it at all, is there a difference in the way the model works
2. About the formal definitions of spurious labels, technical details are ignored. Specifically, how to obtain and why consider both the spurious representation and the invariant representation. What is the advantage of such processing over other simpler method, like clusters and others?
3. Differences in data distribution may affect the effectiveness of the model. Will the discussion of discrepancy between the correlations in the training and validation set in spurious term leads to data leakage? Furthermore, data distribution seems important to the effectiveness of the model, then how to ensure the universality and wide effectiveness of DISK?
4. The representation of this paper could be optimized. For example, Related work is better to be better organized. Then naturally, the motivation and advantages of this work over previous ones could be more obvious. Furthermore, figures are lacked, especially for the ones describing the framework.
5. Some modules are lack of theorical basis. For example, why High Confidence Selection (HCS) is effective. And how to define the high-confidence and corresponding threshold when mitigating subpopulation shift with DISK.
6. The symbols used throughout this paper should be gathered, presented in the form of tables.
7. Experiments are not sufficient enough. Typically, ablation study on the strategy of determining spurious labels, the necessity of utilizing KL-Divergency and so on. 
8. Experiments do not fully demonstrate the advantages of DISK. For example, the advantages of it over baselines are not evident. Furthermore, the analysis on its performance on datasets like Celeb are not convincing. It is more like a kind of guess, and if so, DISK seems lack of universality.

### Questions
1. When the data is labeled with this information, some carry it, and none carry it at all, is there a difference in the way the model works
2. How to obtain and why consider both the spurious representation and the invariant representation. What is the advantage of such processing over other simpler method, like clusters and others?
3. Will the discussion of discrepancy between the correlations in the training and validation set in spurious term leads to data leakage? Furthermore, data distribution seems important to the effectiveness of the model, then how to ensure the universality and wide effectiveness of DISK?
4. Could you summarize the motivation and contributions of this work? And could the workflow of DISK be summarized in the form of figure?
5. Why High Confidence Selection (HCS) is effective. And how to define the high-confidence and corresponding threshold when mitigating subpopulation shift with DISK. Corresponding analysis could be more theorical and solid.
6. Why the advantages of DISK over baselines are not evident. Furthermore, the analysis on its performance on datasets like Celeb are not convincing. It is more like a kind of guess, and if so, DISK seems lack of universality. Could you demonstrate the university of DISK?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents an approach, DISK, for estimating the spurious label of a data sample to enable the use of downstream algorithms that can then use the estimated group information to address subpopulation shifts in the training data. The methodology is developed to leverage an important premise that the imbalance among subpopulations (in training data) is absent in the validation data, based on which a spurious classifier is optimized to maximize the correlation of the estimated spurious label and task label while minimizing such correlation.  To demonstrate the effective of DISK, the estimated spurious label is then used to enable a subsampling strategy to balance subgroups, with a strange of HCS to discard low-confidence predictions of spurious labels. 

Experiments were conducted on a synthetic toy case and benchmark MNIST, F-MNIST, and CIFAR datasets. Comparisons were made primarily to baselines that require actual spurious labels. Specifically, in comparison with DFR, the authors demonstrated the performance of DISK to be similar without needing the use of the true spurious label.

### Strengths
- To remove the need of actual spurious labels is an important challenge in addressing subpopulation shifts. 
- The in-depth analysis of the ability of DISK to infer spurious labels and its consistency with actual oral decision is appreciated.

### Weaknesses
Three of my major concerns are listed below:

1. The motivation of DISK is that it will remove the need of the knowledge of the data labels regarding their subgrouping based on core and spurious features. At the same time, the methodology is built on the premise that there is a training set where such spurious correlation exits, along with a validation set where such spurious correlation does not exist. It seems to me that this premise itself requires knowledge about the subgroups during data curation (in order to create validation data where subgroups are balanced) — this seems to be contradictory to the said motivation. 

2. The experiments were mostly focused on comparison with baselines that requires the label of subgroups — because DISK does not use such labels, its performance is expected to not exceed these baselines, as summarized in Table 1. While these experiments are useful to show the DISK was able to produce reasonable results without the use of spurious labels, there are however a large number of works that had proposed alternative ways of estimating the spurious labels, such as clustering based approaches ([1][2], loss based approaches ([3][4][5]  — these should be the primary baselines to demonstrate the contribution of DiSK.

[1] No Subclass Left Behind: Fine-Grained Robustness in Coarse-Grained Classification Problems
[2] Unsupervised Learning of Debiased Representations with Pseudo-Attributes
[3] Just Train Twice: Improving Group Robustness without Training Group Information
[4] Learning from Failure: Training Debiased Classifier from Biased Classifier
[5] SPREAD SPURIOUS ATTRIBUTE: IMPROVING WORST-GROUP ACCURACY WITH SPURIOUS ATTRIBUTE ESTIMATION

3. Throughout the introduction and the related work sections, the description of the problem of spurious correlation due to subpopulation distribution shifts is heavily mixed with domain adaptation and generalization problems, as if they were equivalent. This misses the important distinction between these two sets of problem despite their connection: in the former, the domain label and core label are heavily correlated due to the subpopulation distribution, versus in the general DA/DG setting, there is typically no such correlation. The authors can be more rigorous and careful in these discussion to make that distinction so as to not confuse the audience.

### Questions
I’d like to see my major comments regarding 1-2 be addressed. 

In addition, 
1. It is not clear how cross-entropy H and how the conditional density in equation (6) or (4) are calculated.
2. In (4)-(6), y^tr/^val refers to the label of core features, and y_s,w^tr/^val refers to the label of spurious features, is this true? This was not clearly defined.
3. I’d imagine that sub-sampling would see a major limitation when facing substantially underrepresented groups. The use of HCS, by further discarding low-confidence predictions, will only make it worse. Please comment on this, in particular the limit of subgroup imbalance ratio DISK can handle properly.
4. It’d be very helpful in the toy data experiments to see the estimated spurious labels.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
