# Can Data be Myopic? Outlier Detection in High-Dimensional Tabular Data via Subspaces

- Decision: Reject
- Scores: 3, 5, 3

## Abstract
Outlier detection in high-dimensional tabular data is an important task in data mining, essential for many downstream tasks and applications. Existing unsupervised outlier detection algorithms face one or more problems, including inlier assumption (IA), curse of dimensionality (CD), and multiple views (MV). To address these issues, we introduce Generative Subspace Adversarial Active Learning (GSAAL), a novel approach that uses a Generative Adversarial Network with multiple adversaries. These adversaries learn the marginal class probability functions over different data subspaces, while a single generator in the full space models the entire distribution of the inlier class. GSAAL is specifically designed to address the MV limitation while also handling the IA and CD, being the only method to do so. We provide a mathematical formulation of MV, convergence guarantees for the discriminators, and scalability results for GSAAL. Our extensive experiments demonstrate the effectiveness and scalability of GSAAL, highlighting its superior performance compared to other popular OD methods, especially in MV scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors propose Generative Subspace Adversarial Active Learning (GSAAL), a method using a Generative Adversarial Network with multiple adversaries to learn marginal class probabilities in different subspaces, while a single generator models the inlier class distribution. GSAAL uniquely addresses MV, IA, and CD issues, with theoretical guarantees, a scalability analysis. Finally, experimental results showing its superior performance, particularly in MV scenarios.

### Strengths
1) The technique appears sound.

2) The presentation is clear and easy to follow.

3) The experimental results are sufficient.

### Weaknesses
1. The concept of using one generator with multiple discriminators is not novel, as it has been explored in several works, such as [1] MCL-GAN: Generative Adversarial Networks with Multiple Specialized Discriminators and [2] DREAM: Domain-agnostic Reverse Engineering Attributes of Black-box Models. The authors should discuss these related works in their paper.

2. Given the challenges commonly faced in training GANs, what can be said about the convergence of the proposed method?

3. Additionally, what is the motivation for using active learning in the context of outlier detection? Could the authors provide a more detailed explanation?

### Questions
Please address the concerns above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper addresses the issue of multiple views in tabular outlier detection, where certain complex correlations between features are observable only in specific feature subspaces. Specifically, the authors extend the GAAL method by training multiple detectors via active learning. This paper provides a mathematical formulation of the multiple views issue, theoretical support for the proposed method, and a complexity analysis.

### Strengths
This paper effectively addresses the critical issue of multiple views in tabular outlier detection, providing valuable insights into this significant challenge. The authors strengthen their proposed method with robust theoretical support, including a detailed mathematical formulation of multi-view approaches and a convergence guarantee. Additionally, they offer a complexity analysis, and further validate their approach through extensive experiments conducted on both real and synthetic datasets.

### Weaknesses
1.While the authors provide an example addressing the issues of Multiple Views (MV), Instance Ambiguity (IA), and Concept Drift (CD), Figure 1 lacks clarity due to the absence of a decision boundary in the 3D space visualization. Furthermore, the figure does not clearly define the cluster-based and locality-based methods it references.
2.Although the authors conducted experiments on 22 real datasets, the detailed performance results in Table 5 of the Appendix reveal that the proposed method achieves the best results on only 5 datasets. This suggests that the method does not consistently outperform existing methods.
3.Despite comparing their approach to several classical methods, the authors would benefit from including comparisons with more recent and powerful tabular anomaly detection methods, such as MCM [1], ICL [2], SLAD [3], and NeuTraL AD [4].
4.The paper would benefit from a clearer illustration of the proposed method's framework, which would help readers gain a better understanding of the approach.
5.While the training process is provided in Algorithm 1 in the Appendix, the paper should also include a description of the inference process to offer a complete understanding of the proposed methodology.


[1] MCM: Masked Cell Modeling FOR ANOMALY DETECTION IN TABULAR DATA

[2] Anomaly Detection For Tabular Data with Internal Contrastive Learning, ICLR2022

[3] Fascinating Supervisory Signals and Where to Find Them: Deep Anomaly Detection with Scale Learning, ICML2023

[4] Neural Transformation Learning for Deep Anomaly Detection Beyond Images, ICML202

### Questions
The paper addresses noteworthy issues and solutions but suffers from unclear writing and suboptimal experimental results. The authors could respond by clarifying Figure 1, enhancing the method's consistency across datasets, comparing it with recent methods like MCM and ICL, illustrating the framework more clearly, and detailing the inference process. These improvements would significantly enhance the paper's impact and clarity.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper aims to solve the issues of inlier assumption, curse of dimensionality, and multiviews (subspaces) of outlier detection. It proposed a method based on the generative adversarial network with multiple adversaries.

### Strengths
1. This work aims to address three important problems in outlier detection. The objective is clear and important.
2. The paper presented the subspace issue of outlier detection clearly.
3. The experiments included both synthetic and real datasets.

### Weaknesses
1. The novelty is not significant. The major difference compared to previous works is that the proposed method trains multiple discriminators for GAN.
2. It is not clear why learning multiple discriminators handles the MV/subspace issues. Theorem 1 is not sufficient to support the claim. 
3. The details of the setting for the multiple discriminators are missing. Suppose $x$ has d attributes, how did the authors partition them into $k$ groups for the $k$ discriminators to handle? Just randomly? Using the same partition strategy, we can apply another OD method to each group of attributes and then combine the results. This could be a necessary baseline to compare in the experiments.
4. In Section 4.1.1, how the authors generated the outliers for the synthetic data hasn't been described. And the high-dimensional setting is unrealistic since most features of a real dataset are mutually correlated.
5. The baselines compared in the experiments are too old, while there are many deep learning based OD or anomaly detection methods published after 2020. For instance, in Table 3, none of the compared methods is based on deep learning, while the proposed method is a deep learning method. The authors compared Deep SVDD on the real datasets but not on the synthetic datasets, why? Why didn't include deep learning methods in Figure 3 to compare the time cost?
6. The improvement given by the proposed method on real datasets is not significant. In Table 5, the proposed method was outperformed by many baselines on many datasets.

### Questions
Please see the content about weakness.

### Soundness
2

### Presentation
2

### Contribution
1
