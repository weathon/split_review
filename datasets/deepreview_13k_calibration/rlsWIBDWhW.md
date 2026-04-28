# Cluster-Driven Adversarial Perturbations for Robust Contrastive Learning

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 5, 6, 6

## Abstract
Adversarial contrastive learning aims to learn a representation space robust to adversarial inputs using only unlabeled data. Existing methods typically generate adversarial perturbations by maximizing the contrastive loss during adversarial training. However, we find that the effectiveness of this approach is influenced by the composition of positive and negative examples in a minibatch, which is not explicitly controllable. To address this limitation, we propose a novel approach to adversarial contrastive learning, where adversarial perturbations are generated based on the clustering structure of the representation space learned through contrastive learning. Our method is motivated by the observation that contrastive learning produces a well-separated representation space, where similar data points cluster together in space, while dissimilar ones are positioned farther apart. We hypothesize that perturbations directed toward neighboring (the second nearest to be specific) clusters are likely to cross the decision boundary of a downstream classifier built upon contrastive learning, effectively acting as adversarial examples. A key challenge in our approach is to determine a sufficiently large number of clusters, for which the number of classes in the downstream task would serve the purpose but is typically unknown during adversarial contrastive learning. Therefore, we employ the silhouette score to identify the optimal number of clusters, ensuring high-quality clustering in the representation space. Compared to the existing approaches, our method achieved up to $2.25$\% and $5.05$\% improvements in robust accuracy against PGD and Auto-Attack, respectively, showing slight improvement in standard accuracy as well in most cases.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents a novel method for adversarial contrastive learning that aims to improve the robustness of learned representations by leveraging the clustering structure inherent in the representation space formed during contrastive learning. NCP-ACL directs perturbations toward neighboring clusters (specifically the second nearest), hypothesizing that such perturbations are more likely to cross the decision boundary of a downstream classifier.

### Strengths
- The paper clearly explains the stages of NCP-ACL, from pre-training with SimCLR to the specific perturbation generation technique.
- The paper provides an extensive experimental analysis comparing NCP-ACL with existing state-of-the-art adversarial contrastive learning methods.
- The reported improvements in robust accuracy against strong adversarial attacks (e.g., PGD, Auto-Attack) are promising.
- The paper includes detailed ablation studies that examine the effects of different components, the number of clusters K, the balance parameter λ, and perturbation strategies.

### Weaknesses
 - The relationship between the clustering in the representation space and the downstream classifier's decision boundary could be more clearly explained. The paper states that perturbations are likely to cross the boundary when directed toward neighboring clusters, but does this generalize across different downstream tasks? The assumption is not well motivated throughout the paper. Fig. 1 (b) for example shows that there exist clusters that are neighboring but not close to the decision boundary. The gray arrow case that is expected to "act as a positive sample in regular contrastive" needs further elaboration. Specifically, the paper lacks a rigorous justification for why moving towards the second-nearest cluster is more effective at generating adversarial examples than moving towards other neighboring clusters or even random directions within the representation space. The claim that such perturbations are more likely to cross decision boundaries needs more theoretical backing, particularly given that the decision boundary of a downstream classifier is not explicitly considered during the contrastive learning phase.
- The motivation for why targeting the second nearest cluster is particularly effective could be further elaborated. While the appendix empirically shows that perturbations directed toward this cluster lead to effective adversarial examples, the analysis is for the top-5 clusters and lacks a deeper theoretical or conceptual explanation that would strengthen the argument and provide more insight into the underlying mechanism. The empirical analysis does not sufficiently explain why the second nearest neighbor is optimal, and not the third, fourth, or even a combination of multiple neighbors. The lack of a theoretical basis makes the choice seem somewhat arbitrary.
- From a technical contribution, this work integrates clustering into the existing DeACL method. The novelty seems limited, and the method relies heavily on the quality of the clustering in the representation space. If the clusters are not well-formed, the perturbations generated may not be as effective in enhancing adversarial robustness. The paper does not sufficiently address the potential for poor clustering to negatively impact the performance of the method. The clustering step introduces a dependency that could be a point of failure if the representation space is not well-structured. This dependency on clustering quality is a significant limitation that needs more discussion and analysis.
- Decoupled adversarial contrastive learning for self-supervised adversarial robustness. In the related works section, the paper could better position itself within the adversarial CL literature. The paper needs to more clearly differentiate itself from existing adversarial contrastive learning methods, particularly those that also use some form of perturbation in the latent space. A more thorough comparison with existing methods is needed to highlight the unique contributions of this work.
- The experiments are conducted on CIFAR-10, CIFAR-100, and STL-10, which are relatively small-scale datasets. Including results from larger and more diverse datasets (e.g., ImageNet) would better showcase how the method performance scales. The lack of experiments on larger datasets limits the generalizability of the findings. It is unclear how the method would perform on more complex datasets with a larger number of classes and more diverse data distributions.
- The paper discusses that the perturbed anchor sample $x + \delta$ may move closer to the perturbed negative set and further from the perturbed positive set when a sufficiently large number of negative samples is present. However, the statement does not seem to hold for recent works that adjust the direction of perturbations [1-3]. For example, targeted adversarial strategies, like TARO [1], demonstrate that simply perturbing samples without considering specific target directions or entropy measures can lead to suboptimal adversarial effects. The paper does not adequately address how the proposed method compares to targeted adversarial attacks that consider specific directions or entropy measures, which could lead to more effective adversarial examples.
- Then lines 176-181 are also confusing since most of the literature deals with avoiding false negatives, i.e., examples that are considered negatives but have the same class as the anchor. The paper needs to clarify why the proposed method addresses the false negative issue more effectively than existing approaches. The explanation of how the method avoids false negatives is not clear and needs further elaboration.
- There exists research that has explored neighbor-based perturbation strategies to enhance contrastive adversarial robustness, e.g., [4,5] and many works in graph learning. Lines 200-208 provide a proof-of-concept experiment that needs more depth to convincingly support the paper's claims, as it compares the effectiveness of the proposed perturbations solely with random noise. It would be best if this was an ablation study comparison with SoTA methods. The comparison with random noise is insufficient to demonstrate the effectiveness of the proposed perturbation strategy. A more comprehensive comparison with existing state-of-the-art methods is needed to validate the claims of the paper.
- To my understanding, SFL results reported in Table 3 are the same as the ones reported in Table 2 (CIFAR 10). The information could be condensed so that the paper presents both SFL and ALF results across all datasets.

### Questions
- Does using silhouette scores to find the optimal number of clusters K involve manual interpretation?
- How does the method perform over existing clustering-based ACL methods?
- What does "act as a positive sample in regular contrastive" mean for grayed-out examples in Fig. 2?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces an adversarial contrastive learning framework called NCP-ACL (Neighboring-Cluster Pursuit Adversarial Contrastive Learning). The framework leverages the cluster structure of the representation space learned through standard contrastive learning to generate adversarial examples that challenge the decision boundary. Building on a pretrained standard contrastive learning encoder, the method identifies each data point's cluster centroid and its second-nearest neighboring cluster to create adversarial perturbations. Experimental results across three downstream tasks demonstrate the effectiveness of the proposed approach.

### Strengths
- This paper introduces related work and the background knowledge in a clear way.
- Experimental setting is clear and apparent.

### Weaknesses
 - Lack of theoretical / empirical supporting arguments for claims.
   - Why the second nearest neighbor is used instead of the nearest neighbor to generate adversaries? Even in the appendix, there is only comparison using between second, third, and fourth nearest neighbors.
   - The theoretical explanation of why choosing K with the highest Silhouette scores is good for clustering.
   - The main motivation of this work is existing adversarial contrastive learning works don't guarantee that the generated adversarial examples are cross the decision boundary. Then, with the fine-tuned linear classifier, can you compare the success rate that how much generated adversarial examples are cross the decision boundary for both baseline methods and yours?
   - Why do you leverage 5-PGD during training which is relatively weaker than existing standard PGD attack with more attack steps? Since using weaker adversaries lead to a better clean accuracy, evaluating models with much stronger attack seems to be essential.
- Need more experiments with diverse recent attacks (e.g., PGD-100, CW, LGV, SPSA, DeepFool)

### Questions
- Is this method robust against diverse pretrained encoder with different learning algorithms such as BYOL or BarlowTwins?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a new adversarial contrastive learning framework that leverages the clustering structure in the representation space, using the silhouette score to select the optimal number of clusters without extra hyperparameter tuning. Additionally, the authors demonstrate that their method achieves fully robust representations, where adversarial fine-tuning has minimal impact compared to standard fine-tuning, and outperforms state-of-the-art methods in robust accuracy against PGD and Auto-Attack, with a slight improvement in standard accuracy. However, some concerns about writing and methods remain as follows.

### Strengths
1.	The authors propose to use cluster-driven adversarial perturbations to improve model’s robustness, such framework makes fully use of the spherical K-means method on contrastive learning.
2.	They empirically show that perturbations generated through the method are harder for models to process compare to random perturbations.
3.	They conduct extensive experiments on CIFAR10, CIFAR100, and STL-10 for classification tasks and robustness evaluation, which verify the effectiveness of the proposed method.

### Weaknesses
1.  The motivation for this work is not clear. The authors claim that “the effectiveness of this approach is influenced by the composition of positive and negative examples in a minibatch, which is not explicitly controllable.”. However, what is the effect of positive and negative examples in a minibatch? What is the relation of the adversarial perturbations to positive and negative examples?
2.  I am concerned about the significance of this work. Traditional contrastive learning can obtain a model with high standard accuracy, but if adversarial samples are added to the training, will it lead to a significant decrease in standard accuracy like traditional adversarial training [A][B], even though robustness is improved? If this problem exists, can we achieve more friendly standard accuracy and/or robust accuracy by combining adversarial purification [C][D] and adversarial detection [E][F] after obtaining a standard model through traditional contrastive learning?
3.  The experiments in Table 1 are not convincing to me, comparing only random noise is insufficient. Noise generated under the same paradigm[G][H][I] should be compared, otherwise, the improvement cannot be attributed to breaking the decision boundary.
4.  In Experiment 4.2, the statement “We believe that it was a trade-off” lacks supporting evidence. Additional experiments or academic references are needed to substantiate this claim.
5.  The experiments in Table 3 focus on the small dataset (CIFAR-10) and do not demonstrate the upper limit of the proposed method's generalization ability. Could more complex datasets be considered?

### Questions
1.	In Lines 52-53 and 193, why do you want to push the adversarial sample to other classes for sure? Is there some supported theory or experiment?
2.	Why the key challenge in the approach is to determine a sufficiently large number of clusters? What is its effect? It seems that the results in Fig. 3 show that we can obtain a modest performance if we take a cluster number greater than 30.
3.	What is the motivation of employing the silhouette score?
4.	For the adversarial contrastive learning, what kind of encoder is considered to have well-structured clusters (Line 196)? What impact would it have on your method if the clustering ability itself is not very good?
5.	What the advantages of Eqn. (4) compared with Eqn. (2) in theory?
6.	In Section 3.1, the rationale for choosing the second-nearest neighbor lacks clarity— is there a theoretical explanation beyond empirical justification?
7.	In the introduction, the assumption that "there is no guarantee that the created perturbations will be adversarial with respect to the decision boundary" is intuitive. Could this assumption be validated through some experiments?
8.	The experiments in Table 4 show an improvement in robustness, but a decrease in standard accuracy on the CIFAR-10/100 datasets. Can a reasonable explanation be provided for this?
9.	As I understand it, each cluster should have a first-nearest neighbor cluster. If that's the case, why is the n=1 data missing in the ablation experiments in Table 5?

**Minor issues**
1. The concept “adversarial linear fine-tuning” and “standard linear finetuning” are referenced before definition.
2. In Lines 262 and 269, Should the encoder used for generating adversarial samples be $f_{\theta_1}$?
3. In line 20, page 2, "vulnerablility" should be "vulnerability".
4. In line 31, page 2, "roubstness" should be "robustness".
5. In line 27, page 6, "Consitent" should be "Consistent".
6. The section on contrastive learning could be strengthened by incorporating additional related papers, such as [J-M].
7. Would it make better if samples of different classes in Figure 1 were labeled with different colors?

**Reference**

[A]	Towards deep learning models resistant to adversarial attacks. ICLR 2018.

[B]	Improving robustness using generated data. NeurIPS 2021.

[C]	Diffusion models for adversarial purification. ICML 2022.

[D]	Adversarial purification with score-based generative models. ICML 2021.

[E]	Detecting adversarial data by probing multiple perturbations using expected perturbation score. ICML 2023.

[F]	 A practical bayesian approach to adversarial detection. CVPR 2021.

[G]	Decoupled adversarial contrastive learning for self-supervised adversarial robustness. ECCV 2022.

[H]	 Rethinking the effect of data augmentation in adversarial contrastive learning. ICLR 2023.

[I]	Enhancing adversarial contrastive learning via adversarial invariant regularization. NeurIPS 2023.

[J]	Intra- and Inter-Slice Contrastive Learning for Point Supervised OCT Fluid Segmentation. IEEE Trans. Image Process. 2022.

[K]	Unsupervised Domain Adaptation Via Contrastive Adversarial Domain Mixup: A Case Study on COVID-19. IEEE Trans. Emerg. Top. Comput. 2024.

[L]	Cycle contrastive adversarial learning with structural consistency for unsupervised high-quality image deraining transformer. Neural Networks, 2024.

[M]	 Semi-Supervised Dual-Stream Self-Attentive Adversarial Graph Contrastive Learning for Cross-Subject EEG-based Emotion Recognition. IEEE Trans. Affective Comput. 2024.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper proposes a novel approach to adversarial contrastive learning, leveraging clustering within the representation space. The method, named Neighboring-Cluster Pursuit Adversarial Contrastive Learning (NCP-ACL), generates adversarial perturbations by directing them toward neighboring clusters in the learned representation space. This technique aims to address limitations in existing adversarial contrastive learning methods by making perturbations more effective in crossing decision boundaries in downstream classifiers. The paper demonstrates significant improvements in robust accuracy against adversarial attacks compared to state-of-the-art methods.

### Strengths
- The paper addresses a notable limitation in current adversarial contrastive learning techniques, where perturbations may not be effective in crossing decision boundaries. By utilizing the clustering structure in the representation space, the proposed NCP-ACL method generates more meaningful perturbations.

- The experimental results on CIFAR-10, CIFAR-100, and STL-10 datasets show that NCP-ACL outperforms existing methods in terms of both robust and standard accuracy. The approach yields consistent improvements across different datasets and settings, with up to 5.05% improvement in robust accuracy against Auto-Attack.

- The use of silhouette scores to automatically determine the optimal number of clusters is a practical approach that simplifies hyperparameter tuning.

### Weaknesses
 - The paper should discuss the computational cost introduced by the additional clustering step. It would be helpful to provide an analysis of how the clustering affects training time compared to baseline methods.
- The method’s reliance on spherical K-means clustering could pose scalability challenges for high-dimensional representation spaces. Specifically, the computational complexity of K-means increases with dimensionality, and the paper does not adequately address this potential bottleneck. Furthermore, the convergence of K-means is not guaranteed, and the paper lacks discussion on the potential impact of suboptimal cluster assignments on the adversarial training process.
- The paper would benefit from a discussion on the theoretical implications or guarantees provided by the method. For instance, can the clustering structure always ensure that perturbations cross decision boundaries effectively, and under what conditions? The paper lacks a formal analysis on how the cluster structure relates to the decision boundaries of downstream classifiers. It is unclear if the method is guaranteed to generate perturbations that are more effective than random perturbations, or if the method is only effective under certain data distributions or classifier architectures.

### Questions
1. How does the clustering step, including the calculation of silhouette scores, affect the overall computational time? Is there a significant increase in training time compared to other adversarial contrastive learning methods?

2. What assumptions are made regarding the quality of the clustering in the representation space? Could the proposed method perform poorly if the representation space is not well-clustered, and if so, under what specific conditions might this occur?

3. The paper shows results for standard and adversarial linear fine-tuning. Have you tried adversarial full fine-tuning (AFF)?

### Soundness
3

### Presentation
4

### Contribution
3
