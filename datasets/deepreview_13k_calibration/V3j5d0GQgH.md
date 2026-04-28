# FedLoGe: Joint Local and Generic Federated Learning under Long-tailed Data

- Decision: Accept
- Avg Score: 6.00
- Scores: 5, 8, 6, 5

## Abstract
Federated Long-Tailed Learning (Fed-LT), a paradigm wherein data collected from decentralized local clients manifests a globally prevalent long-tailed distribution, has garnered considerable attention in recent times. 
In the context of Fed-LT, existing works have predominantly centered on addressing the data imbalance issue to enhance the efficacy of the generic global model while neglecting the performance at the local level. 
In contrast, conventional Personalized Federated Learning (pFL) techniques are primarily devised to optimize personalized local models under the presumption of a balanced global data distribution. 
This paper introduces an approach termed \textbf{Fed}erated \textbf{Lo}cal and \textbf{Ge}neric Model Training in Fed-LT (FedLoGe), which enhances both local and generic model performance through the integration of representation learning and classifier alignment within a neural collapse framework. 
Our investigation reveals the feasibility of employing a shared backbone as a foundational framework for capturing overarching global trends, while concurrently employing individualized classifiers to encapsulate distinct refinements stemming from each client’s local features.
Building upon this discovery, we establish the Static Sparse Equiangular Tight Frame Classifier (SSE-C), inspired by neural collapse principles that naturally prune extraneous noisy features and foster the acquisition of potent data representations. 
Furthermore, leveraging insights from imbalance neural collapse's classifier norm patterns, we develop Global and Local Adaptive Feature Realignment (GLA-FR) via an auxiliary global classifier and personalized Euclidean norm transfer to align global features with client preferences. Extensive experimental results on CIFAR-10/100-LT, ImageNet-LT, and iNaturalist demonstrate the advantage of our method over state-of-the-art pFL and Fed-LT approaches.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper addresses Federated Learning with global long-tailedness. The proposed method is inspired by the neural collapse idea and contains three steps: 1) global representation learning with SSE-C classification head, and 2) & 3) global and local feature realignment.  In step 1, a classifier head is learned with sparsity while maintaining the Equiangular Tight Frame (ETF) properties, which is then broadcast to clients for learning backbone $\theta$ and personalized classifier head $\psi$. In step 2 & 3, the backbone $\theta$ and global classifier $\psi$ and local classifier $\phi$ is respectively updated and realigned. Empirical results on a few benchmarks show the effectiveness of the proposed approach over prior work on data heterogeneous FL or Long-tailed FL.

### Strengths
\+ This paper tackles a crucial and intriguing problem in federated learning with global long-tailedness.

\+ The key idea of using ETF to build a classifier as regularized consensus is well-motivated.

\+ Experiments and ablation studies are well-designed and comprehensively conducted.

### Weaknesses
- Too many technical details are missing. For example, it is vague to me why performing personal classifier realignment in Eq (7) helps in tackling local data heterogeneity. Specifically, the mechanism by which the local classifier norm influences the global classifier and how this addresses the issue of varying class distributions across clients is not clearly explained. The connection between the norm adjustment and the mitigation of local heterogeneity needs further elaboration.

- Authors need to provide detailed motivation of each step in the proposed algorithm, such as the motivation of keeping two classifier heads for clients: $\phi_k$ and $\psi_k$, and realignment of the global classifier $\psi$ in Eq 6. The rationale behind having both a global and local classifier for each client is unclear. It's not obvious why a single personalized classifier wouldn't suffice, or how the interaction between the two classifiers leads to improved performance, especially in the context of long-tailed data. The specific benefit of realigning the global classifier $\psi$ using local information also needs to be better justified.

- Writing: Certain citation formats need to be fixed; Figure 1 is difficult to comprehend. The figure lacks clear labeling and a detailed explanation of what is being visualized. It's hard to understand the relationship between the plotted data and the claims made about feature collapse and sparsity. The axes are not clearly defined, and the visual representation is not intuitive.

- Missing discussion and comparison with related work on long-tailed FL. Authors should specify the technical contributions of the proposed method over other prior work, especially FedETF, which shows much resemblance to the proposed work. The novelty of the approach compared to existing methods, particularly FedETF, is not clearly articulated. The specific differences in the optimization process, the handling of long-tailed data, and the overall architecture need to be highlighted to demonstrate the unique contribution of this work.

### Questions
How to optimize Eq (4) that contains a maximization over $j$? 

What is the purpose of introducing sparsity to the SSE-C classifier, besides its empirical effectiveness?

Why do we need two classifier heads  $\phi_k$ and $\psi_k$ for each of the clients $k$ instead of just one?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper considers federated learning with long-tailed global distribution and non-iid client distributions. the authors propose a Federated Local and Generic Model Training (FedLoGe) to train a model that can perform well both on long-tailed global distribution and local client distributions. First, the proposed Static Sparse Equiangular Tight Frame Classifier fosters the acquisition of potent data representations. Second, the Global and Local Adaptive Feature Realignment (GLA-FR) is used to align global features with client preferences.

### Strengths
* (originality) The authors proposed a novel method by neural collapse and realignment of local and global classifiers. Though neural collapse has been used for handling data heterogeneity, the realignment is novel to address the local-generic problem.
* (significance) The proposed method can significantly outperform baselines in the concerned settings.
* (clarity) The figure 2 is appreciated for clarifying the method.
* (quality) The experiments are well designed for the problem setting. Multiple baselines are compared to demonstrate the effectiveness of the proposed method both in boosting local and generic performance.

### Weaknesses
 * (quality) The generic-local setting looks self-contradictive to me. When the personalized federated learning targets training models personalized for each client, is it necessary to consider a model adapted for global or generic distribution? In personalized federated learning, the assumption is that each client has its own data distribution and it aims to learn a model adapted for the specific distribution. If the global or generic distribution is considered, which client will be expected to use the model? The paper does not adequately justify the need for a global model in this context, especially given that the goal is personalized models. It's unclear why a client would benefit from a model trained on a potentially very different global distribution.
* (significance) Because of my concerns about the problem setting, I am afraid that the proposed method may have a limited impact on a few specific problems. The focus on a generic-local setting, which seems at odds with the core principles of personalized federated learning, raises questions about the practical applicability and broad relevance of the proposed approach. The method's utility may be restricted to scenarios where a global model is somehow beneficial, which is not well-established in the paper.
* (clarity) The technical motivation is not clear. The neural collapse has been used for handling data heterogeneity and classifiers should be fixed by the neural collapse theorem. It is unclear why the realignment is still needed. Why the fixed classifier cannot be used for all clients? The paper does not sufficiently explain why a fixed classifier, as suggested by neural collapse, is insufficient for all clients. The need for realignment, especially given the neural collapse argument, is not well-motivated. The paper needs to clarify why a single, fixed classifier is inadequate for diverse client data distributions.
* (clarity) The paper is hard to follow. Specifically, the motivation experiments in the introduction are hard to understand. Why the mean and variance of class means are evaluated in Figure 1? I cannot follow the logic in the discussion quoted below.
> However, preliminary experiments benchmarking ETF with CIFAR-100 in Fed-LT suggest that only a few features have relatively large means, while most of the small-mean features are contaminated by severe noise, as shown in Fig. 1(a). Such observations are inconsistent with the feature collapse property, and we coin it as feature degeneration.

  How do the mean and variance of features relate to the feature collapse? The connection between the mean and variance of features and the concept of feature collapse is not clearly explained. The paper needs to provide a more detailed explanation of how these metrics relate to the neural collapse phenomenon and why the observed behavior is considered 'feature degeneration'.

### Questions
* Please provide clear motivation for the generic-local setting. When the personalized federated learning targets training models personalized for each client, is it necessary to consider a model adapted for global or generic distribution? In personalized federated learning, the assumption is that each client has its own data distribution and it aims to learn a model adapted for the specific distribution. If the global or generic distribution is considered, which client will be expected to use the model?
* How do the mean and variance of features relate to the feature collapse in the quoted content?
> However, preliminary experiments benchmarking ETF with CIFAR-100 in Fed-LT suggest that only a few features have relatively large means, while most of the small-mean features are contaminated by severe noise, as shown in Fig. 1(a). Such observations are inconsistent with the feature collapse property, and we coin it as feature degeneration.

=== after rebuttal ===
The authors' responses have address my concerns.

### Soundness
2 fair

### Presentation
1 poor

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
This paper presented a model training framework that enhances the performance of both local and generic models in Fed-LT settings in the unified perspective of neural collapse. The proposed framework is comprised of SSE-C, a component developed inspired by the feature collapse phenomenon to enhance representation learning, and GLA-FR, which enables fast adaptive feature realignment for both global and local models. As a result, the proposed method attains significant performance gains over current methods in personalized and long-tail federated learning.

### Strengths
S1. This work focuses on addressing the data imbalance issue to simultaneously enhance the efficacy of the generic global model and its performance at the local level, which is an interesting topic.

S2. This paper is well-written and has a good presentation.

S3. The proposed SSE-C can address the problem of feature degeneration well, which is a promising finding.

### Weaknesses
W1. Convergence analysis is missing, which is very important for the optimization process of federated learning. Please analyze it from the experimental and theoretical point of view.

W2. Lack of discussion about privacy. Federated learning is proposed to protect the privacy of the client, but the method in this paper has the risk of gradient disclosure, please add the discussion of privacy in this work.

W3. The communication overhead of the model seems to be very large, which will restrict the practical application. Please increase the experiment and analysis of the communication overhead.

W4. The related work is simply a list of existing methods. Please add a discussion of the differences between this work and previous work to further clarify the contribution of this paper.

### Questions
Please see the Weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper aims to address the long-tailed data in FL. The authors propose a new method called FedLoGe to improve both local and global model performance of FL under this scenario. FedLoGe introduces a Static Sparse Equiangular Tight Frame Classifier (SSE-C) to enhance data representations. It also contains feature realignment at both global and local levels.

### Strengths
- The long-tailed problem in FL is an emerging problem that is worth studying.
- The paper is generally well structured.
- Figure 2 provides a good illustration of the proposed method.
- The proposed method seems to work and the experiments demonstrate the effectiveness of the proposed method.
- Evaluation are conducted on various backbones and different scales of datasets.

### Weaknesses
 - The content of the paper is not very easy to follow. For example, the message from Figure 1 is a bit hard to interpret. In the first paragraph of the third page (where Figure 1 (a) is explained), it is not quite clear what large mean and small mean imply. The explanation lacks sufficient detail regarding the feature distribution and how the proposed method alters it. Specifically, it's unclear how the 'sparse allocation' is achieved and what its direct impact is on feature quality. The connection between the observed variance changes and the claimed improvement in feature conciseness and effectiveness is not sufficiently substantiated.
- Notations seem to be inconsistent, the notation for the number of clients is K in Section 3, but N in Section 4.
- Probably a typo: “…. personalized classifier by multiple the norm of … “ Should it be “by multiplying… “?
- The method of fixing the classifier and backbone alternatively for training is proposed in previous papers on personalized FL.
- Some settings are not clear: e.g., the number of clients participating in training each round and the number of local epochs.

### Questions
- How many clients participate in training each round?
- Does the paper focus on cross-silo FL, cross-device FL, or both?
- Why the proposed method can improve performance on FL with long-tailed problem?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
