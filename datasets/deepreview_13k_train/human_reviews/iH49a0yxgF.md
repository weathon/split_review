# DUDE: Deep Unsupervised Domain adaptation using variable nEighbors for physiological time series analysis

- Decision: Reject
- Scores: 5, 6, 6, 6

## Abstract
Deep learning for continuous physiological time series such as electrocardiography or oximetry has achieved remarkable success in supervised learning scenarios where training and testing data are drawn from the same distribution. However, when evaluating real-world applications, models often fail to generalize due to distribution shifts between the source domain on which the model was trained and the target domain where it is deployed. A common and particularly challenging shift often encountered in reality is where the source and target domain supports do not fully overlap. In this paper, we propose a novel framework, named Deep Unsupervised Domain adaptation using variable nEighbors (DUDE), to address this challenge. We introduce a new type of contrastive loss between the source and target domains using a dynamic neighbor selection strategy, in which the number of neighbors for each sample is adaptively determined based on the density observed in the latent space. This strategy allows us to deal with difficult real-world distribution shifts where there is a lack of common support between the source and the target. We evaluated the performance of DUDE on three distinct tasks, each corresponding to a different type of continuous physiological time series. In each case, we used multiple real-world datasets as source and target domains, with target domains that included demographics, ethnicities, geographies, and/or comorbidities that were not present in the source domain. The experimental results demonstrate the superior performance of DUDE compared to the baselines and a set of four benchmark methods, highlighting its effectiveness in handling a variety of realistic domain shifts. The source code is made open-source [upon acceptance of the manuscript].

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors propose a Deep Unsupervised Domain adaptation using variable nEighbors (DUDE) for physiological time series analyses. Based on Nearest-Neighbor Contrastive Learning of Visual Representations (NNCLR), the authors propose a new strategy that can adaptively select the number of neighbors. Experiments on three machine learning tasks are done to verify the effectiveness of the proposed DUDE.

### Strengths
Strength:

1.	A DUDE framework is proposed in the context of continuous physiological time series analysis.

2.	Domain shift uncertainty (DSU) layers are applied in DUDE framework.

3.	An adaptive neighbor selection strategy is proposed. 

4.	Experiments on 3 different machine learning tasks are done.

### Weaknesses
Weakness:

1.	The technical novelty of the work is quite limited. The two main parts of DUDE are either using existing techniques (DSU) or making marginal improvements on existing work NNCLR. Using threshold to adaptively select neighbors is not new, and it also brings a question on how to determine the threshold for different or new tasks. The paper claims that the best hyperparameter Δ found on the validation set was 0.95 for both experiments and thus shows the consistency for different experimental settings, which is not convincing. The authors may need to conduct a more comprehensive sensitivity analyses on this hyper-parameter or propose a valid hyper-parameter selection guideline for new tasks or unseen datasets. Specifically, the adaptive neighbor selection mechanism, while inspired by NNCLR, appears to be a rather straightforward application of a threshold on the similarity scores. The paper lacks a detailed analysis of the sensitivity of the model's performance to the choice of this threshold, and it is unclear how this threshold would generalize to new datasets or tasks with different characteristics. The claim of consistency across experiments based on a single hyperparameter value is not sufficient to demonstrate robustness.

2.	The paper highlights that DUDE is proposed for physiological time series analyses, but from the technical view, the framework can be used for general time series UDA problems. It is unclear why the context of physiological time series is necessary.

3.	Based on point 2, more general time series UDA baselines should be compared, e.g. [ref1] and [ref2], to name a few. 

4.	For DSU layer, what’s the difference between DSU and instance normalization used in [ref3]. The paper does not provide a clear explanation of the differences between the DSU layer and instance normalization, particularly in the context of domain adaptation. A more detailed explanation of the specific mechanisms of DSU and how it differs from instance normalization, especially in how it introduces uncertainty, is needed.

5.	Why different data augmentation used for different tasks? It is necessary to have an ablation study on different data augmentation techniques. The choice of data augmentation techniques seems arbitrary, with different techniques used for different tasks without clear justification. An ablation study is needed to understand the impact of these choices on the model's performance and to determine if the selected augmentations are indeed optimal for each task.

6.	The paper lacks ablation studies on the two parts (DSU and NNCLR) of DUDE. The absence of ablation studies on the individual components of DUDE, specifically the DSU layer and the modified NNCLR, makes it difficult to assess the contribution of each component to the overall performance of the framework. Such studies are crucial to understand the effectiveness of each part and to justify the design choices.

### Questions
Please refer to the weakness.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper addresses the problem of domain shifts in the case of time series data and suggests a new structured approach ('DUDE') that uses a dynamic method for neighbor selection which faces the absence of 
common support between the source and the target domain. The evaluation on real world datasets of continuous time series displays the higher f1 scores of the suggested framework versus the existing baselines.

### Strengths
- The paper develops a model and tests it on three dissimilar settings. 
- Research on this domain has a considerable impact in real-world predictions of clinical interest and can be deployable as an indicative medical tool.
- The paper tries to face the obstacle of weak generalization of the trained models when used in an unobserved domain.
- It explores the realistic scenario of the training data distribution being  the testing data distribution. 
- The supplement explains to some extent the logic of the loss function in figure S3, which is an incremental construction if NNCLR and seems to have emerged mostly from an empirical try.
- Although the code is missing, some of the implementation details are provided. Maybe some more would make the submission stronger.

### Weaknesses
 - The improvement in the f1 scores is higher or same as in the existing baselines. However, only in two datasets (Target: MESA, Target: Asian) the difference form the baselines is more than 3%. This shows the encouraging consistent improvement of DUDE framework, but it is not making its superiority strong.

- Writing style: the citations are neither hyperlinked nor separated from the text.

### Questions
Please refer to the weaknesses.

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
The paper proposes an unsupervised domain adaptation approach for physiological time series based on a contrastive loss that leverages nearest neighbor samples from the source domain to the target domain.

### Strengths
The method is simple, which is nice, and it can be used with a variety of contrastive losses, possibly with minimal changes. The evaluation is thorough across datasets, tasks, and baselines.

### Weaknesses
The main concern is how effective the nearest neighbor strategy is. It is the main contribution, as all the other components already exist, and unsupervised domain adaptation with self-supervised losses has been extensively studied in the vision domain.

 The evaluation of the nearest neighbor strategy is not sufficiently rigorous. The paper does not explore the impact of using randomly selected source samples instead of nearest neighbors, which would serve as a strong baseline. Without this comparison, it is difficult to assess the true value of the proposed nearest neighbor approach. Furthermore, the paper lacks an ablation study to evaluate the importance of the supervised loss during adaptation, which is a critical component of the method. It is also unclear how the performance varies based on the changing number of nearest neighbors, which is a key hyperparameter for the method.

References for the augmentations used are missing. Random Switch Windows, Jitter, and Flipping were proposed in earlier work [1] on self-supervised learning for sensory data.

### Questions
What if one selects source samples randomly instead of nearest neighbors? How many samples are really needed from the source domain to be effective for adaptation?

During adaptation, how important it is to also use a supervised loss? Ablation is very important, but it is missing.

Are the baseline results (in Table 1-4) are from corresponding papers, or are the methods reimplemented and ran by the authors?

How does the performance vary based on the changing number of nearest neighbors?

References for the augmentations used are missing. Random Switch Windows, Jitter, and Flipping were proposed in earlier work [1] on self-supervised learning for sensory data.
[1] Saeed, Aaqib, Tanir Ozcelebi, and Johan Lukkien. "Multi-task self-supervised learning for human activity detection." Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies 3.2 (2019): 1-30.

### Soundness
2 fair

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
This paper proposes an unsupervised domain adaptation framework for physiological time series data. The framework extends an existing Nearest Neighbor Contrastive Learning of Visual Representations (NNCLR) algorithm by allowing multiple nearest neighbors in the support set. Extensive experiments on 8 datasets with 3 tasks suggested that the model improved over existing methods on out-of-distribution domain.

### Strengths
1. The paper studies an underexplored area: unsupervised domain adaptation for physiological time series.
2. Experiments are extensive and results are promising.
3. Paper is easy to understand.

### Weaknesses
1. Some parts of the methods need more clarification or justification. For example, what are the encoders? Why is the Domain Shift Uncertainty (DSU) layer necessary? It is unclear how the encoders are chosen for each task, and what their specific architectures are. The justification for the DSU layer is also not sufficiently explained; the paper needs to clarify the specific mechanism by which it introduces uncertainty and how this mitigates overfitting on the source domain.
2. Technical contribution is limited. The model extends existing NNCLR algorithm by incorporating more nearest neighbors in the support set. While the application to physiological time series is valuable, the core algorithmic modification seems incremental and lacks a strong theoretical underpinning. The paper does not sufficiently explore the impact of the number of neighbors on the model's performance, which would be crucial to justify the design choice.
3. Citation format is wrong, which reduces readability of the paper.

### Questions
1. What are the encoders for each task? Why is the Domain Shift Uncertainty (DSU) layer necessary? Please clarify in Methods.
2. It would be interesting to see how model performance varies across $\delta$ (i.e., number of neighbors), e.g., does model performance saturate or degrade with larger number of neighbors?
3. In ablation study (Figure S1), what’s the setup for DSU and $NNCLR_{\Delta}$? Please clarify.
4. Hidden in the supplement, the authors discuss that including a supervised loss prevents latent space collapse. Please provide an ablation study to support this claim.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
