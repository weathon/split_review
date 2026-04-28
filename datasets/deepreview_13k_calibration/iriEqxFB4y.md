# DOS: Diverse Outlier Sampling for Out-of-Distribution Detection

- Decision: Accept
- Avg Score: 7.33
- Scores: 8, 8, 6

## Abstract
Modern neural networks are known to give overconfident predictions for out-of-distribution inputs when deployed in the open world.
It is common practice to leverage a surrogate outlier dataset to regularize the model during training, and recent studies emphasize the role of uncertainty in designing the sampling strategy for outlier datasets.
However, the OOD samples selected solely based on predictive uncertainty can be biased towards certain types, which may fail to capture the full outlier distribution.
In this work, we empirically show that diversity is critical in sampling outliers for OOD detection performance.
Motivated by the observation, we propose a straightforward and novel sampling strategy named DOS (Diverse Outlier Sampling) to select diverse and informative outliers.
Specifically, we cluster the normalized features at each iteration, and the most informative outlier from each cluster is selected for model training with absent category loss.
With DOS, the sampled outliers efficiently shape a globally compact decision boundary between ID and OOD data.
Extensive experiments demonstrate the superiority of DOS, reducing the average FPR95 by up to 25.79\% on CIFAR-100 with TI-300K.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes Diverse Outlier Sampling (DOS), a simple sampling approach for choosing diverse and informative outliers to use as an auxiliary OOD training dataset. The basic idea is simple: use k-means on normalized features to cluster the data and then per cluster identify the most informative outlier. Diversity is achieved since the k clusters collectively explain the full possible auxiliary OOD data but per cluster, we only choose the most informative outlier, which altogether ensures that the size of the auxiliary dataset can be controlled to be small (i.e., based on the number of clusters). Experimental results show that DOS works extremely well in practice.

### Strengths
- The paper is easy to follow.
- The basic idea of the proposed approach is very simple and elegant.
- The experimental results are compelling.

### Weaknesses
 - By normalizing the feature vectors, if I understand correctly, Euclidean norm is used so that the normalized vector resides on the unit hypersphere. Is there any benefit to using specialized versions of k-means (and k-means related) algorithms for the hypersphere? For reference, there are versions of k-means and the Gaussian mixture model that are restricted to the hypersphere (technically, mixtures of von Mises-Fisher distributions). See, for instance, the papers by Banerjee et al (2005) and Kim (2021). More generally, some sort of sensitivity analysis with respect to using different clustering algorithms could be helpful.
- Figuring out how to set up experiments so that you could report error bars would be very helpful.

### Questions
See weaknesses.

### Soundness
4 excellent

### Presentation
4 excellent

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
This paper focuses on outlier sampling for out-of-distribution detection (OOD detection) tasks. To be specific, this paper follows the setting of outlier exposure that utilizes a surrogate outlier dataset to regularize the model during training, trying to make the model better recognize those OOD inputs. This work points out that previous outlier sampling methods are solely based on predictive uncertainty which may fail to capture the full outlier distribution. Motivated by the empirical evidence which shows the criticality of diversity, this work proposes Diverse Outlier Sampling (DOS) to select diverse and informative outliers via clustering the normalized features at each iteration. The proposed method achieves an efficient way to shape the decision boundary between ID and OOD data. Experiments from different perspective are conducted to demonstrate the effectiveness of DOS.

### Strengths
1. This paper focuses on an important and practical question on outlier exposure, i.e., the auxiliary outliers may fail to capture the full outlier distribution.  
2. This paper proposes a new method, namely DOS, which clusters the normalized features at each iteration and samples the informative outlier from each cluster to realize the diversified outlier selection. The technical design for clustering with normalized features is noval to the knowledge of the reviewer and shows promising empirical achievement towards the target.
3. Comprehensive experiments compared with both post-hoc OOD detection scores and also several representative sampling methods are conducted to demonstrate the effectiveness of the proposed DOS.
4. The overall presentation is clear and the method is easy to understand.

### Weaknesses
Overall, this work presents a concise and effective way to conduct diverse sampling in outlier exposure. Here are the major concerns for the current version of this paper, and hope it can help to improve the paper better.
1. Although the overall presentation is clear, some critical definitions and claims are questionable and lack of convincing support. Specifically, the notion of 'diversity' is not rigorously defined, making the motivation less compelling. The paper claims that uncertainty-based sampling fails to capture the full outlier distribution, but this is not sufficiently demonstrated with empirical evidence beyond the toy example. The claim that this leads to 'imbalanced performance' is also vague and lacks supporting data.
2. Technically, the proposed method (DOS) is based on an empirical demonstration of "diversity" with the OOD detection performance. However, the detailed definition of diversity is under-defined and the underlying mechanism of the clustering-based sampling scheme is not clearly explained. The paper does not provide a clear explanation of why clustering normalized features is an appropriate approach for achieving diversity in the context of outlier exposure. The connection between the clustering objective and the desired diversity in outlier sampling is not explicitly established.
3. Since the previous greedy strategy will continually sample those outliers that are easy to be recognized as ID data, why do we need to utilize the diverse sampling method if the newly proposed method will sample some outliers that are already recognized as OOD data by the model? This raises concerns about the potential for the proposed method to include less informative outliers, which could hinder the learning process. The paper does not adequately address this potential trade-off between diversity and informativeness.
4. The experimental part can include more results conducted in other ID datasets, as well as the large benchmark dataset (like ImageNet) to demonstrate the effectiveness and efficiency of the proposed DOS. The current experiments are limited in scope and do not fully demonstrate the generalizability of the proposed method. The lack of experiments on large-scale datasets is a significant limitation.

### Questions
Please also refer to the weakness part for the general concerns. The following questions are more specific to the clarification and the reviewer hope these question can help the authors to improve the writing and presentation of this work. 
1. As for the critical motivation ("However, the OOD samples selected solely based on uncertainty can be biased towards certain classes or
domains, which may fail to capture the full distribution of the auxiliary OOD dataset."), the intuitive illustration is based on a toy example in 2D space, it could be better to refer to some convincing results which also show the same problem with Figure 1c.
2. For the "imbalanced performance of OOD detection" pointed out in the same sentence, could the authors provide some empirical evidence?
3. The critical observation shows that "outlier subset comprising data from more clusters results in better OOD detection", but what is the relationship between the cluster with diversity? 
4. Based on the previous question, could the authors provide a more detailed or specific conceptual definition of diversity? and clearly state how to measure the diversity in the motivation part to make that part more convincing.
5. It seems that the current version of the work does not provide the corresponding experimental part for supporting the claimed "efficient" of the proposed DOS, like the sampling efficiency if I understand it correctly.
6. In addition to using the CIFAR-100 as the ID dataset, it could be better to use the ImageNet dataset as ID dataset and use a large-scale ImageNet 21k as auxiliary outliers to verify the scalability of the proposed DOS.

### Soundness
4 excellent

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes to use a diverse sampling to draw OOD samples from auxiliary datasets for training OOD models. The sampling consists of two steps. First, they apply K-means to cluster the auxiliary samples in a normalized feature space. Second, the samples close to the decision boundary of in-distribution are selected from each cluster. The clustering ensures the diversity of the selected samples. In training, the selected samples are considered OOD samples. They evaluate the proposed method on the common benchmark, i.e., CIFAR100, and show that the proposed diverse sampling improves over greedy sampling and other baselines.

### Strengths
1. The paper studies a well-motivated problem in OOD detection. Finding high-quality samples in the large auxiliary dataset improves the performance of the trained model and reduces the training cost.

2. The proposed diverse sampling is simple and effective. 

3. The proposed method achieves impressive empirical results on the common benchmark.

4. The authors provide extensive ablation studies to demonstrate the robustness of the method.

### Weaknesses
1. Diverse sampling is a well-known method in active learning [1,2]. Diverse sampling leading to superior performance is not surprising. It indeed improves the performance of OOD models. Critically speaking, the novelty in terms of the method is limited. If the authors could provide some deeper theoretical analysis, e.g., how diverse sampling improves the generalization bound, it would make the paper more solid.

2. There are typos in equation 2. I understand that the authors use a cross-entropy loss. However, equation 2 is just the entropy. $p(y)$ or $y$ is missing inside the expectation.

### Questions
How important is the clustering step in diverse sampling? [1] proposed to use a K-means++ seeding algorithm based diverse sampling for semi-supervised anomaly detection. The K-means++ seeding algorithm doesn't require to predefine the clusters and the number of clusters. I think it can be also easily combined with the absent category probability. How would the proposed diverse sampling compare to the K-means++ seeding algorithm based diverse sampling?

[1] Li, Aodong, Chen Qiu, Marius Kloft, Padhraic Smyth, Stephan Mandt, and Maja Rudolph. "Deep anomaly detection under labeling budget constraints." In International Conference on Machine Learning, pp. 19882-19910. PMLR, 2023.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
