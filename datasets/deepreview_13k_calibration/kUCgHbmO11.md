# SF(DA)$^2$: Source-free Domain Adaptation Through the Lens of Data Augmentation

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 8, 5, 6

## Abstract
In the face of the deep learning model's vulnerability to domain shift, source-free domain adaptation (SFDA) methods have been proposed to adapt models to new, unseen target domains without requiring access to source domain data. Although the potential benefits of applying data augmentation to SFDA are attractive, several challenges arise such as the dependence on prior knowledge of class-preserving transformations and the increase in memory and computational requirements. In this paper, we propose Source-free Domain Adaptation Through the Lens of Data Augmentation (SF(DA)$^2$), a novel approach that leverages the benefits of data augmentation without suffering from these challenges. We construct an augmentation graph in the feature space of the pretrained model using the neighbor relationships between target features and propose spectral neighborhood clustering to identify partitions in the prediction space. Furthermore, we propose implicit feature augmentation and feature disentanglement as regularization loss functions that effectively utilize class semantic information within the feature space. These regularizers simulate the inclusion of an unlimited number of augmented target features into the augmentation graph while minimizing computational and memory demands. Our method shows superior adaptation performance in SFDA scenarios, including 2D image and 3D point cloud datasets and a highly imbalanced dataset.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work presents a novel approach to address the source-free domain adaptation task, which aims to adapt the pre-trained model to suit the unlabelled target domain with distribution shifts. The work looks at a novel perspective – from data augmentation in latent feature space instead of applying transformation of raw data to save computational costs while improving model robustness. The SNC loss is proposed to learn discriminative features and form tighter clusters; To augment target features, a class-wise covariance matrix is estimated in an online manner with the help of pseudo labels. IFA loss promotes the decision boundaries for each class to align with the principal direction of the variance of target features. To encourage each direction to be orthogonal, FD loss is further added. Comprehensive experiments are provided on both 2D and 3D datasets and evidence the validity of the proposed approach.

---- Post Rebuttal ----
Thanks for the detailed explanation the authors provided. I would like to maintain the original positive rating for this work.

### Strengths
+ The paper looks at an interesting way of exploring augmentation in SFDA, where the feature diversity is guaranteed while the resulting computational costs are not significantly increased compared to conventional augmentation methods. The main idea is straightforward and effective, and the authors also bring in-depth discussions and theoretical analysis to provide insights into why the idea works. This makes the proposed well-motivated and inspiring.
+ The paper presents a large number of experimental comparisons on different benchmark datasets and demonstrates a significant boost over previous methods. The running time analysis gives clear support to what is claimed in the introduction section. 
+ The paper is well structured and notations are used properly.

### Weaknesses
- As shown in Figure 3, the ablation study reveals that solely optimizing SNC performs better than with either FD or IFA loss. It remains unclear why SNC+IFA is inferior as augmented views are provided. The performance drop when using only IFA or FD loss individually suggests a potential conflict between these regularizations and the primary SNC objective. Specifically, the ablation study lacks a clear explanation of the interplay between the proposed losses. While the authors suggest that IFA and FD losses need to be applied simultaneously, the underlying mechanism behind this necessity is not thoroughly investigated. For instance, it is not evident how the disentanglement effect of FD loss directly contributes to the effectiveness of IFA loss in preserving class information during feature augmentation. More discussions can be shared to better help readers understand the proposed approach. 

- The paper mentions that the covariance matrix is estimated in an online manner. However, there is a lack of detail regarding the specific methodology used to ensure its quality and accuracy. The potential impact of an inaccurate covariance matrix on the overall performance is a significant concern, especially during the initial stages of adaptation when the feature space might be highly entangled due to domain shift.

### Questions
My question mainly lies in (1) the ablation study: why do two regularizations need to be applied simultaneously? (2) the confusion matrix is estimated in an online way. How to guarantee its quality/accuracy?

If the questions are properly addressed, I will consider raising my rating.

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
This work proposed a novel perspective of solving source-free domain adaptation (SFDA) problems through implicit feature augmentation on augmentation graphs. Motivated by the two assumptions, the authors naturally constructed an augmentation graph within the feature space. Initially, the augmentation graph is formed based on neighboring features. Subsequently, it is harnessed to identify clusters within the feature space using the SNC loss. With high-quality clusters, target features are implicitly augmented by an EFA loss as an upper bound of the first term of SNC loss instead of directly sampling from Gaussian distribution. Considering similar categories, feature space is further disentangled by maximizing cosine distances, leading to preserved class semantics. Experiments and analysis were conducted to prove the effectiveness of the proposed method.

### Strengths
Originality: This submission presents an innovative perspective on SFDA, introducing implicit augmentation without the need for prior knowledge. This novel approach has been thoughtfully considered and significantly broadens the scope of research in this area.

Quality: The proposed method's quality is supported by a comprehensive body of theoretical and experimental evidence.

Clarity: The definitions and mathematical terms are highly connected with the corresponding elements of the proposed method. The presentation and logical flow are well-executed.

Significance: The application of data augmentation to SFDA from a novel standpoint is of great significance. While the theoretical contributions to the SFDA field may be limited, the method holds practical and theoretical value, as it is built upon sound mathematical foundations and addresses practical issues, such as handling similar categories.

### Weaknesses
A more detailed description of the relationship between the augmentation graph and section 3.4 is warranted, as there appears to be no explicit utilization of G_hat in section 3.4.

How does equation (4) influence G_hat, and what is the impact of equation (4) and G_hat on the overall optimization process, given that equation (4) only considers cosine-similarity neighborhoods and mini-batch statistics?

Within spectral clustering methods, could the scenario wherein two groups of features belonging to the same ground truth category are erroneously assigned to separate partitions ultimately lead to a degradation in model performance, as they may be pushed apart within the feature space?

It would be much appreciated if some DA surveys and reviews are included to better show the background and related work, such as "A Comprehensive Survey on Source-free Domain Adaptation", "A Review of Single-Source Deep Unsupervised Visual Domain Adaptation".

The compared baselines are obviously insufficient. For source-free DA, some typical and latest methods are not compared, such as SHOT++. For source-available DA, the compared baselines are too old. Some more baselines published in 2022 and 2023 are required but missing.

### Questions
Please see the weaknesses above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a novel approach, namely Source-Free Domain Adaptation through the lens of Data Augmentation (SF(DA)^2), to address the challenge of source-free domain adaptation. The proposed method aims to harness the advantages of data augmentation while mitigating the drawbacks associated with relying on prior knowledge of class-preserving transformations and the increased memory and computational demands. SF(DA)^2 comprises three key components: Spectral Neighborhood Clustering (SNC) loss, Implicit Feature Augmentation (IFA) loss, and Features Disentanglement (FD) loss. The SNC loss is designed to cluster the target data in the prediction space, the IFA loss emulates the effects of augmented features without imposing additional computation and memory overhead, and the FD loss captures distinct class semantic information along diverse directions. Rigorous experimentation on various benchmarks verifies that the proposed method attains state-of-the-art performance in source-free domain adaptation.

### Strengths
(1) The writing of this paper is good.

(2) The method proposed is straightforward yet effective, and the results obtained are at the forefront of current research in the field.

### Weaknesses
(1) What are the differences between the proposed SNC loss and the loss function in the existing AaD [1]? As far as I know, the purpose of the loss in AaD is to encourage similar neighbors to be close to each other and dissimilar neighbors to be far apart within a batch. This is similar to the SNC loss proposed in this paper. The author needs to clarify the differences between these two loss functions, specifically how the spectral clustering on the augmentation graph in SNC provides a different optimization objective than the direct neighbor-based contrastive approach in AaD. It's not clear if the graph structure introduces a fundamentally different learning dynamic or if it's simply a re-parameterization of the same objective.

(2) Are the estimated covariance matrices accurate in the IFA and FD losses, given the domain shift between the source and target domains? The estimation of these matrices relies on the output probabilities of the target data. However, this estimation process may introduce biases, especially when there are significant dissimilarities between the classes in the target domain and those in the source domain. As a result, the probabilities associated with these classes in the target domain, as generated by the source domain model, may be greatly reduced. Consequently, there is a potential risk of losing the capability to effectively learn these specific classes during the subsequent learning process, presenting a challenge to rectify the situation. The paper needs to address how the method handles the potential for biased covariance estimates, especially in the early stages of training when the target domain predictions are likely to be unreliable. Furthermore, the method should discuss the potential impact of these inaccurate covariance matrices on the disentanglement process.

(3) IFA operations have shown promise as a universally applicable data augmentation technique in unsupervised tasks. Can IFA be applied to other existing unsupervised tasks? Can you provide examples to validate its effectiveness? The paper should elaborate on the generalizability of IFA and discuss any modifications or considerations needed to apply it to different unsupervised learning scenarios beyond domain adaptation. It would be beneficial to see a discussion of the limitations of IFA and the types of tasks where it might not be suitable.

(4) Two questions regarding the experiment:
(a) In VisDA, Domain-Net, and PointDA-10 datasets, IFA loss has a weight of 1e-4, while FD loss has a weight of 10, resulting in a limited impact of IFA loss on the training process compared to FD loss. Can the inclusion of the other two datasets, apart from the VisDA-Rust task, demonstrate the significance of this new data augmentation technique? The paper needs to provide a more detailed analysis of the impact of the IFA loss, perhaps through ablation studies with varying weights or by showing its contribution to the overall performance in a more isolated manner. The current weight configuration makes it difficult to assess the true effectiveness of IFA.
(b) Why are there no comparisons of NRC and AaD methods on the DomainNet dataset? Similarly, why are the results of AaD not compared on the PointDA-10 dataset? The absence of these comparisons makes it difficult to fully contextualize the performance of the proposed method relative to existing state-of-the-art techniques. The paper should include these comparisons to provide a more comprehensive evaluation.

(5) In the Introduction, the authors mention that recent studies have used data augmentation techniques to improve adaptation performance. However, there is a lack of more relevant work cited, such as [2] and [3].

### Questions
Please see the weaknesses.

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
This paper addresses source-free domain adaptation task. The submission investigates the problem from the view of data augmentation, along with neighborhood clustering.

### Strengths
- The motivation is clear and sound, by using neighborhood (spectral) clustering to address SFDA, which is already proved by the previous related works.

- Instead of utilizing heavy explicit data augmentation, the submission resorts to implicit augmentation via local neighbors. It decreases the complexity.

- Experimental results on several methods are better compared to existing methods.

### Weaknesses
 - The proposal of SNC is not new. SFDA method AaD already introduced quite similar method (in both motivation and final objective form). More specifically, the proposed SNC just takes [1] into the SFDA task.

- Several results for other methods in the main tables are not identical to the results in their original papers. It is not good to report the reproduced results of own without mentioning it in the paper (though there are always software environment difference).




### Questions
- The introductions of IFA and FD are the main contribution of the paper. In my understanding, IFA loss plays similar role as the first term in SNC loss, while FD loss plays the similar role as the second term of SNC loss (here FD loss may be better as it quantifies the similarity degrees between different categories). I am just wondering what if only using FD and IFA losses for adaptation.



- In Fig. 2, the results show that the proposed method can not improve SHOT, while in AaD it indicates that SHOT is actually conducting similar operation as NRC and AaD. Do authors have clear explanation about the phenomenon, is it due to the pseudo labeling used in SHOT?

- In Fig. 3, with only FD or IFA on SNC will deteriorate the performance. The authors posit some hypothesis for explanation, while I think there may need more results on several other datasets to prove the assumption. By the way, I think there is no information we could get from Fig. 3(b), since it is neither not consistent with the corresponding accuracy, nor cable to guide the hyperparameter tuning.

- There are two extra hyperparameters for FD and IFA losses, and there seems no ablation study for those hyperparameters. In the paper, it mentioned that $\alpha_1$ and $\alpha_2$ are set to different values for different dataset. I conjecture they may be sensitive on some datasets and hard to tune in the unsupervised way.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
