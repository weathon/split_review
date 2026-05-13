# P$^2$OT: Progressive Partial Optimal Transport for Deep Imbalanced Clustering

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
Deep clustering, which learns representation and semantic clustering without labels information, poses a great challenge for deep learning-based approaches. Despite significant progress in recent years, most existing methods focus on uniformly distributed datasets, significantly limiting the practical applicability of their methods. In this paper, we first introduce a more practical problem setting named deep imbalanced clustering, where the underlying classes exhibit an imbalance distribution. To tackle this problem, we propose a novel pseudo-labeling-based learning framework. Our framework formulates pseudo-label generation as a progressive partial optimal transport problem, which progressively transports each sample to imbalanced clusters under prior distribution constraints, thus generating imbalance-aware pseudo-labels and learning from high-confident samples.
In addition, we transform the initial formulation into an unbalanced optimal transport problem with augmented constraints, which can be solved efficiently by a fast matrix scaling algorithm. Experiments on various datasets, including a human-curated long-tailed CIFAR100, challenging ImageNet-R, and large-scale subsets of fine-grained iNaturalist2018 datasets, demonstrate the superiority of our method.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper aims to address deep clustering in an imbalanced scenario. In particular, the authors resort to partial optimal transport to gradually select imbalance-aware high-confidence samples based on pseudo-labels. The selected high-confidence samples are then considered as ground truth labelled data for supervised training. The proposed method has been evaluated in human-curated datasets and achieves superior results over baselines.

### Strengths
1.	The proposed algorithm is overall reasonable. 
2.	Sufficient empirical results are conducted. 
3.	The performance over SOTA clustering baselines are impressive.

### Weaknesses
1. Some claims in this paper are confusing and need improvement. For instance, (i) "the KL divergence-based uniform distribution constraint empowers our method to avoid degenerate solutions and generate imbalanced pseudo-labels", "demonstrating that KL constraint enables our P2OT to generate imbalanced pseudo labels." Why can the KL constraint generate imbalanced pseudo-labels, given that it is defined for a uniform distribution? The authors should clarify how the KL divergence, which encourages a distribution to be close to uniform, leads to imbalanced pseudo-labels. The mechanism behind this claim is not clearly explained and requires further elaboration. Specifically, the interaction between the KL constraint and the inherent data imbalance needs to be better articulated. 
2. I don't think Eq. 5-Eq. 6 are necessary. You can consider introducing Eq. 8 directly after Eq. 3 by introducing a virtual cluster. If I am wrong, please point it out. The authors should provide a more detailed explanation of why the intermediate steps in Eq. 5 and Eq. 6 are crucial. The role of these equations in the overall framework is not immediately obvious, and a more thorough justification is needed. It is not clear why a virtual cluster cannot be introduced directly after Eq. 3, and the authors should explain the specific technical reasons that prevent this simplification.
3. The technical contributions are overclaimed. It appears that the most important aspect of the proposed method lies in the KL constraints. If these KL constraints are added to other clustering baselines, the superiority of the proposed method will be marginal. Additionally, gradually increasing the number of high-confidence samples has been widely adopted in other clustering papers such as SPCIE. It is true that the proposed method can avoid manual selection, but it still introduces an additional hyperparameter in Eq. 7, i.e., $\rho_0$. More importantly, it does not demonstrate the superiority over the baselines. The authors need to provide more substantial evidence that the proposed method offers significant advantages beyond the use of KL constraints and gradual sample selection. The novelty of the approach should be more clearly demonstrated, and the impact of the additional hyperparameter $\rho_0$ should be thoroughly investigated, including a sensitivity analysis.

### Questions
1. A very popular real imbalanced dataset is REUTERS-10K[1], which is more challenging than the constructed dataset. How does the proposed method perform on REUTERS-10K?  
2. In Eq. 3, the KL constraint is defined for the uniform distribution. Why it can be called an unbalanced OT problem?  
3. The proposed method is defined for the whole dataset. How can it be implemented for a mini-batch scenario? In the mini-batch scenario, samples from minority clusters may not exist.  
4. Figure 2 shows that the embedding of P2OT is well-separated compared to that of other baselines. Can the authors explain why the embedding is much better than others, given that it is only slightly higher than SCAN in terms of NMI?  
5. Figure 4 shows that the performance degenerates after 10 epochs. Can you explain the reason behind this?  

[1] Xie, Junyuan, Ross Girshick, and Ali Farhadi. "Unsupervised deep embedding for clustering analysis." International conference on machine learning. PMLR, 2016

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper addresses the challenge of deep clustering under imbalanced data. The paper proposes a novel pseudo-labeling-based learning framework. This framework formulates pseudo-label generation as a progressive partial optimal transport problem, allowing it to generate imbalance-aware pseudo-labels and learn from high-confidence samples. The approach transforms the problem into an unbalanced optimal transport problem with augmented constraints, making it efficiently solvable. Experimental results on various datasets, including long-tailed CIFAR100, ImageNet-R, and iNaturalist2018 subsets, demonstrate the effectiveness of the method.

### Strengths
This paper studies an interesting problem, deep clustering under imbalanced data. It proposed a progressive partial optimal transport algorithm to address this problem, and extensive experiments have been conducted to evaluate its effectiveness.

### Weaknesses
1. Great computational cost. In Figure 5, it takes 1 second to estimate the pseudo-labels when K=40. It is impossible in practice with a larger number of clusters, eg, imagenet, and mini-batch training.
2. Missing comparisons on balanced datasets. The true data distribution is unknown in real-world applications. This paper only investigates the settings of imbalanced data or tests on balanced data. It is not well aligned with most literature of deep clustering.
3. This paper does not learn representations, which may be confusing and needs to be clarified. In addition, this paper uses a large pre-trained model and lacks a simple baseline with representation learning models. For example, BYOL or DNIO pre-trained on ImageNet can be used to extract the representations for subsequent K-means clustering. In such settings, we do not need to determine whether the data is imbalanced, as each sample belongs to a single class or a large number of clusters can be pre-defined.
4. A good evaluation metric should be important for imbalanced deep clustering. Under the imbalanced setting, no samples may be assigned to tail classes during Hungarian matching. As we can see in Figure S7, the predictions of the proposed method are more uniform than baselines. There are more samples assigned to tail classes, though this is not true in training data. It confirms that a uniform clustering result is beneficial for evaluation. I suggest that kNN evaluation in representation learning can be adopted for imbalanced clustering, without the need of Hungarian matching. Due to the uniform constraints, more discussion should be paid to Huang et al., 2022.

### Questions
1. Change 'confidence sample selection' to 'confident sample selection'
2. Which dataset is used for DINO pretraining? Is the backbone fixed during training?
3. It is unclear about the use of historical predictions.
4. What is visualized in Figure 2? We usually visualize the features before the classifier instead of class predictions. If the results are consistent for the features, we can conclude: more distinct clusters.

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
This paper studied a more general clustering problem, deep imbalanced clustering. From the perspective of pseudo label generation, the authors propose a progressive partial optimal transport method to combat the imbalanced challenges in data. The technical way to incorporate the imbalanced distribution into the optimal-transport framework and align with the classical solver is appealing, and a range of experiments demonstrate the performance of the proposed method.

### Strengths
1) The technical point is good, which leverages a virtual cluster to incorporate the spirit of sample selection in optimal transport is novel. The authors applied a mass increasing process in the constraint of unbalanced OT to progressively leverage more confident samples for representation learning and avoids the degeneration due to the skew distribution.

2) The reformulation with entropy regularization and the weighted the KL divergence makes the classical Sinkhorn-knop algorithm appliable and stably optimize the target towards the progressive imbalance constraint. The authors carefully deal with the reformulation to make the algorithm can sufficiently incorporate the desire for sample selection.

3) The authors conduct a range of experiments on the representative datasets like small dataset CIFAR100-LT, the mid-scale ImageNet-R, and large-scale iNaturalist. The experimental results and the visualization consistently support the author's claim, and the ablation study provided the insight on how the components work and how useful they are.

### Weaknesses
Although the proposed method is overall novel, there are still some concerns that should be considered.
1) The technical choice about Eq.(13) is unique. The other choice like introducing a hard equality constraint about the mass of the virtual cluster and applying the lagrange multiplier can be also possible. The main concern here is that the authors introduce two hyperparameters for weighted KL: one is for the target clusters, i.e., \lambda, and the other is the large value for the virtual cluster.  How is the performance of directly constraining the equality about 1-\rou with lagrange multiplier compared with Eq.(13).

2) It is not clear why the authors have not compared with the clustering with self-labeling by Asano from the perspective of OT. For SPICE, the performance reported in the appendix is also not convincing. How is the performance comparison of SPICE and P^2OT on the balanced datasets. It will be provide more comprehensive comparison here on both imbalanced datasets and balanced datasets to show their pros and cons.

3) In the perspective of representation learning, some related works should be included with the proper discussion, e.g., about the self-supervised long-tailed learning, like SDCLR [1], BCL [2] and re-weighted regularization, as they also target to representation learning of imbalanced data without label information. Some proper comparison will be better.

### Questions
1) The performance of P^2OT and SPICE on the balanced datasets.

2) How is the performance comparison between the proposed deep imbalanced clustering and some self-supervised long-tailed learning methods in terms of the representation quality?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
