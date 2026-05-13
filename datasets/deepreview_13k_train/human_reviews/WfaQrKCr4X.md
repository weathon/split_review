# A Unifying Framework for Representation Learning

- Decision: Accept
- Scores: 6, 5, 6, 8

## Abstract
As the field of unsupervised learning grows, there has been a proliferation of different loss functions to solve different classes of problems. We find that a large collection of modern loss functions can be generalized by a single equation rooted in information theory. In particular, we introduce I-Con, a framework that shows that several broad classes of machine learning methods are precisely minimizing an integrated KL divergence between two marginal distributions: the supervisory and learned representations. This viewpoint exposes a hidden information geometry underlying clustering, spectral methods, dimensionality reduction, contrastive learning, and supervised learning. I-Con enables the development of new loss functions by combining successful techniques from across the literature. We not only present a wide array of proofs, connecting over 11 different approaches, but we also leverage these theoretical results to create state of the art unsupervised image classifiers that achieve a +8\% improvement over the prior state-of-the-art on unsupervised classification on ImageNet-1K.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a novel framework called I-Con, which unifies various machine learning methods, including clustering, contrastive learning, dimensionality reduction, and supervised learning, under a single equation based on the Kullback-Leibler (KL) divergence between two distributions: the supervisory and learned representations. The authors demonstrate that many existing methods are instances of this unified framework, providing a mathematical foundation that enables the transfer of ideas across domains. The paper also presents new state-of-the-art results in unsupervised image classification on the ImageNet-1K dataset, achieving an 8% improvement over previous methods. Multiple proofs and empirical evaluations back these claims, illustrating the broad applicability of I-Con to various learning problems.

### Strengths
- Theoretical Contributions: The I-Con framework offers a unified theoretical foundation for a wide range of machine learning methods, showing that several existing approaches can be viewed as specific instances of a general KL divergence minimization problem. This not only provides a deeper understanding of these methods but also opens up the possibility of creating new methods by mixing and matching components.
- Comprehensive Theoretical Justification: The paper provides detailed mathematical proofs, connecting 11 different approaches to the I-Con framework. 
- Cross-Domain Applicability: By unifying disparate learning paradigms (clustering, dimensionality reduction, contrastive learning, etc.), the framework facilitates the transfer of techniques across domains, allowing innovations from one area (e.g., contrastive learning) to improve methods in another (e.g., clustering).
- Empirical Performance: The framework's potential is validated through unsupervised image classification on ImageNet-1K, where the I-Con-based method outperforms state-of-the-art methods, demonstrating its practical significance.

### Weaknesses
 - Innovation and Breadth: While the authors introduce the I-Con framework, which attempts to unify multiple existing learning methods, the actual novelty and breadth of this framework might be questionable. Many of the connections between the methods discussed have already been noted in previous works, and the core contribution seems to be more about integrating existing ideas rather than offering fundamentally new insights. Actually, most methods and loss functions can be implemented in a likelihood framework, which is equivalent to minimizing KL distance.
- Limited Guidance According to The Theorem: Several techniques like adaptive neighborhoods, debiased contrastive learning, neighbor propagation are transfered to create a state-of-the-art unsupervised image classification system. However, these methods can be thought out without the I-Con framework as many articles have established. Actually, inspiring or taking ideas from other domains is natural during research. Thus, based on the theorem, it will be more valuable to discuss how to choose the mechanism according to the I-Con framework. 
- Limited Generalization and Insufficient Experimental Validation: While the paper provides some experimental results demonstrating improvements in unsupervised classification, these are mainly focused on clustering on ImageNet-1K. The generalizability of the I-Con framework to other applications and datasets is still underexplored, lacking broader experimental comparisons across a variety of tasks and datasets.
I would be glad to improve my score if my concerns could be addressed.

### Questions
See weakness.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The manuscript attempts to build a universal framework for loss functions corresponding to different representation learning methods. It minimizes an integrated KL divergence between two marginal distributions: the supervisory and learned representations. The proposed framework encompass 11 machine learning methods, including dimensionality reduction, contrastive learning, clustering, and supervised learning, among others.

### Strengths
One advantage is that it can leverage losses from other domains to enhance a particular domain method within this framework. For instance, in experiments, spectral clustering, t-SNE, debiased contrastive learning, and SCAN were utilized to develop an unsupervised image classification system.

### Weaknesses
- It falls short of truly encompassing all representation learning methods, such as autoencoder-based representation learning, masked pretraining-based representation learning, and other general self-supervised representation learning methods. Therefore, the proposed framework does not entirely unify all representation learning methods. I believe that this unified framework is for clustering methods but not a generic representation learning framework.
- The motivation/benefits for unifying representation learning methods claimed in this paper do not entirely convince me personally. Could you give more discussions on whether this unified framework provides advantages beyond facilitating cross-domain insights? For example, does it provide a new method to address all limitations of different representation learning frameworks once?
- Typically, evaluating representation learning methods involves assessing if a model has learned good representations that generalize well across various downstream tasks. However, I did not observe such experiments.
- The choice of data augmentation strategies is crucial in contrastive learning methods. Are data augmentation-based contrastive learning methods also unified within this framework?
- Are there differences in the task purposes between clustering and contrastive learning tasks? My understanding is that clustering aims to discover different clusters, while contrastive learning aims to learn generic representations that can be easily transferred to different downstream tasks. Could you provide further discussion on this?

### Questions
Please see Weakness.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the challenge of the variety of unsupervised representation learning methods by introducing I-Con, a unified interpretation grounded in a single mathematical framework. The authors provide a theoretical proof that I-Con unifies existing methods by minimizing the KL divergence between the supervisory and parameterized neighborhood distribution. Furthermore, the authors effectively transferred perspectives of various representation learning approaches into a state-of-the-art unsupervised classification network and showed both quantitative and qualitative improvements.

### Strengths
- This paper discusses various methods in representation learning in terms for their proposal.
- The proposed framework is well demonstrated throughout the paper including theoretical evidences.
- The proposed method showed significant improvements compared to state-of-the-art unsupervised classification network.

### Weaknesses
 - The motivation for the need for a unified framework of (unsupervised) representation learning is not clear. As discussed in introduction section, “difficult to understand which particular loss function to choose for a given problem or domain”, does not directly match with the proposed method, as I-CON still contains the choice of $p_{\theta}$ for each existing method and does not provide a suitable loss function for given domain.
- The term ‘I-Con’ is ambiguous, as it is used with two different meanings. In section 3.1, term ‘I-Con’ represents a unified representation learning algorithm that can that can serve as the foundation for various methods. However in section 3.2, it is also used to describe integrated (new) representation learning method, causing confusion in the following results. To avoid confusion, use distinct terms to clearly differentiate between I-Con as a framework and I-Con as a specific method.
- Section 3.3 is not easy to follow, especially the sub-section ‘Adaptive neighborhoods’. Paraphrasing the explanations and providing a more detailed demonstration would enhance clarity for the readers.
- Random seeds are not considered in the experimental results. Providing results of multiple runs (e.g., 5 or 10) with standard variations (or error bars) would give stronger evidence for the claimed significant improvements.
- Although the authors claim that I-Con does not require additional regularization, the ablation study in Section 4.3 reveals sensitivity to hyperparameters such as \(\alpha\) and propagation size, which still necessitate tuning. This seems to contradict the claim of not needing additional regularization, as these parameters effectively act as regularizers by controlling the influence of neighborhood information during training.
- In Table 2, error bars are missing for the baseline methods and the scores in Table 3, making it difficult to assess the statistical significance of the reported improvements. The absence of these error bars makes it challenging to determine if the observed gains are consistent across different runs or due to random fluctuations.
- It remains unclear whether I-Con (Ours) in Table 2 refers to the integrated method discussed in Section 3.3 or the best result among the methods explored in Table 3. This ambiguity makes it difficult to interpret the results in Table 2, as it is not clear if the reported performance is due to a specific configuration or the best-performing one. Referring to the best among them as I-Con (Ours) in Table 2 may not be a fair comparison.
- The paper does not address whether the gains observed in Table 3 would be maintained when using k-NN classifiers, as done in DiNO [1]. This is an important consideration, as k-NN classification is a common evaluation method for self-supervised learning, and it is unclear if the proposed method's performance would generalize to this setting.
- Table 2 in the first line in Section 4.2, does not have a link to it.

### Questions
### Questions
- Theoretical evidences for I-Con across various method are given (appendix). However, are there any experimental results in practical environments (e.g., InfoNCE on ImageNet) that shows the I-CON framework can reproduce (or improve) the original representation learning methods?
- In Figure 3, is there a reason for using different dataset (ImageNet-1K and subset of MNIST)? Why not use ImageNet for both the quantitative and qualitative results (or vice versa)?
- Is I-Con (Ours) stated in Table 2 result of integrated method discussed in Section 3.3, or is it the best among them? Table 3 shows results of each transferred intuitions, and results of I-Con (Ours) stated in Table 2 appears to be the best among them. Referring to the best among them as I-Con (Ours) in Table 2 may not be a fair comparison.
- As stated in Section 4.2, I-Con has claimed to have the benefit of not requiring additional hyper-parameter tuning compared to TEMI and SCAN. However, doesn’t I-Con require hyper-parameter tuning, such as /alpha and n-walks (Figure 4, Table 4), for notable improvements?
- DiNO[1] also showed results of k-NN classifiers[2] in the paper. Could results in Table 3 maintain its gains when using k-NN classifiers[2] as stated in [1]?
### Modifications
- Table 2 in the first line in Section 4.2, do not have a link to it.
- Like in t-SNE this addition helps… → Like in t-SNE, this addition helps…

[1] Mathilde Caron, Hugo Touvron, Ishan Misra, Herv´ e J´ egou, Julien Mairal, Piotr Bojanowski, and Armand Joulin. Emerging properties in self-supervised vision transformers, 2021.

[2] Zhirong Wu, Yuanjun Xiong, Stella X Yu, and Dahua Lin. Unsupervised feature learning via non-parametric instance discrimination. In CVPR, 2018.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper provides a unified framework I-Con that can recover many state-of-the-art approaches in various ML tasks as special examples. The main idea behind the I-Con framework is to minimize the KL divergence between two distributions: a "neighborhood" distribution that is given by data and a proposed distribution that encodes some supervisory information, which is similar to the idea behind variational approaches.

### Strengths
1. The paper is very well written and well organized, which conducts a comprehensive survey across different fields and insightfully extracts the similarities behind state-of-the-art methods.
2. It is novel to transfer the proposed distribution across domains and the improvement in performance shown in Section 4 is solid.

### Weaknesses
1. The connection with variational Bayesian methods can be elaborated, where the main idea is to find a proper proposed distribution q_{\phi}. Specifically, the paper should discuss how the choice of the family of distributions for q_{\phi} impacts the optimization and the quality of the learned representations. The current discussion lacks details on how the properties of the chosen distribution family (e.g., unimodal vs. multimodal, heavy-tailed vs. light-tailed) affect the framework's ability to capture complex data relationships. For example, if the true underlying data distribution is multimodal, a unimodal q_{\phi} might lead to suboptimal results.
2. This paper provides a comprehensive survey, but it would be better if the authors could have a paragraph to compare with other survey papers, e.g.
	- Tschannen, Michael, Josip Djolonga, Paul K. Rubenstein, Sylvain Gelly, and Mario Lucic. "On mutual information maximization for representation learning." arXiv preprint arXiv:1907.13625 (2019).
It is important to clarify how the I-Con framework addresses the limitations of mutual information maximization highlighted in the cited work, such as the challenges in estimating mutual information in high-dimensional spaces and the potential for the learned representations to be sensitive to the choice of the estimator. The paper should also discuss whether the I-Con framework is susceptible to similar issues.


### Questions
1. [Naming] In terms of I-Con = Information Contrastive learning, I was wondering if it would be more precise to relate the name to "divergence" or "cross-entropy" since the I-Con framework is essentially the KL minimization and nature of "contrastive learning" is not very intuitive without specification of the proposed distribution q_{\phi}.
2. [Experiments] It is interesting to the improvement in performance when transferring the ideas of proposed q_{\phi} across domains. I was wondering if the improvement is also significant beyond the domain of clustering. It would also be good if some related work that transfers the SOTA q_{\phi} across domains could be provided.
3. Please see "weakness" section. I'll be happy to adjust my score if the connection with variation Bayesian methods can be elaborated.

### Soundness
3

### Presentation
4

### Contribution
3
