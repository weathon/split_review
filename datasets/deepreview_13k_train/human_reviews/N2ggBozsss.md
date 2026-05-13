# Centroid-Based Learning for Malware Detection and Novel Family Identification

- Decision: Reject
- Scores: 5, 3, 3

## Abstract
Detecting out-of-distribution (OOD) data categories while preserving the accuracy of existing classifications is a pressing challenge in many domains. Conventional methods often falter when tasked with generating or identifying new data classes, especially when dealing with graphical data and the problem of graph isomorphism. In this paper, we present a novel approach, the Graph Centroid Model (GCM), which combines Control Flow Graphs (CFGs) with a Graph Neural Network (GNN) to address this challenge effectively. The GCM assigns embeddings produced by a GNN to partitions that support the classification of both known and new classes, even those absent during training.

Our approach quantifies the differences between samples in the embedding space, enabling the identification of multiple distinct representations of familiar classes during training while providing a straightforward mechanism for detecting new classes during testing. This not only improves classification accuracy but also offers intuitive visualizations that provide valuable insights.When applied to a benchmark malware dataset (BODMAS), our method reveals structural commonalities among samples from different malware families while effectively discerning new, previously unseen classes based on their distance from learned representatives in the embedding space.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a novel method for detecting new data classes based on Control Flow Graphs. They employ Graph Neural Network and Centroid Nets to embed the control flow graphs into a latent space. By quantifying the dissimilarities among samples in the embedding space, the authors enable the identification of multiple distinct representations of familiar classes.

### Strengths
1.The paper demonstrates clear logic and a well-defined motivation.

2. The research topic is of significant importance.

### Weaknesses
1. The design of Centroid Nets is ambiguous. The paper lacks a detailed explanation of how the centroids are initialized, updated, and used during the training process. The description does not clarify whether the centroids are learned parameters or derived from the data. The iterative process of updating centroids and embedding samples is not clearly defined, making it difficult to understand the model's behavior. Furthermore, the equations (1), (2), (3), and (5) are indeed identical, and this repetition does not provide any additional insight into the model's functionality.
2. There is a lack of comparison with recent methods for detecting new class families. The authors only compare their method with GCN and GraphSAGE, which are not specifically designed for out-of-distribution detection. This comparison does not adequately demonstrate the effectiveness of the proposed algorithm against state-of-the-art methods in the relevant domain. The absence of a comparison with methods tailored for new class family detection makes it difficult to assess the novelty and performance of the proposed approach.


### Questions
1.	The author did not provide a clear explanation of the training process for Centroid Nets. Additionally, equations (1), (2), (3), and (5) are identical, and these repetitive equations do not offer any additional useful information.
2.	The author should compare the recent approaches for new class family detection in Table 1, as solely comparing with GCN and GraphSAGE does not demonstrate the effectiveness of the algorithm.
3.	In practical usage, there is no separate validation set consisting of samples from new families to determine hyperparameters. In this scenario, how should epsilon be determined?

### Soundness
3 good

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes a GCN-based classification model to detect known and unknown malware with the centroid net method.

### Strengths
The task of detecting unknown malware families is very practical because new families come along all the time.

### Weaknesses
1. Unknown malware detection has been researched for a long time, such as [1]. The proposed method is not a very novel method.

2. Baselines are very limited and only include GCN and GraphSage. (Also, they should called baselines rather than benchmarks). The baselines should cover other OOD methods like one-class SVM.

3. From the visualization in Figure 5, some families cannot be well clustered, which may affect the classification performance.

4. The dataset does not contain the benign software dataset. In practical usage, the model should divide the benign and malicious software.

5. The paper was written in an unprofessional manner: For example, Equation (1), (2), (3), and (5) are the same. The dataset subsection should not be put in the Methods section. All figures have no explanations after the figure title. Training loss figures should not be presented in the main text.

### Questions
1. What is the concrete family in the testing set and training set?

2. The baselines GCN and GraphSage cannot reject the class (for an unknown family), so the new family accuracy should be 0. Why there is still acc reported in Table 1?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper combines graph neural networks to model a control flow in binaries with centroid based losses. Since both paradigms are well known (authors fails to reference centroid based losses such as arc-face [1] or center loss [2]. The approach to out-of-distribution detection (ood) is similar to that in [3], albeit that in the proposed paper might be computationally cheaper due to replacing k-nn with a distance to a center. 
I think that the paper is a solid work, but targets the wrong audience. ICLR papers, in my opinion, should be more about new general approaches or new domains which are important and very different from other domains, such that they require special methods or the prior art is failing. This manuscript is more about combining existing tools in a nice application and would be more suited to a good security conference.
As a comment, I do not think that the proposed approach solves the ood. I see the problem of OOD inherent to NN implementing injective map (not surjective). This means that many semantically different samples gets mapped by NN to the same region with the same score. The proposed method decrease this problem, but does not remove it.



[1] Deng, Jiankang, et al. "Arcface: Additive angular margin loss for deep face recognition." Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. 2019.

[2] Wen, Yandong, et al. "A discriminative feature learning approach for deep face recognition." Computer Vision–ECCV 2016: 14th European Conference, Amsterdam, The Netherlands, October 11–14, 2016, Proceedings, Part VII 14. Springer International Publishing, 2016.

[3] Sun, Yiyou, et al. "Out-of-distribution detection with deep nearest neighbors." International Conference on Machine Learning. PMLR, 2022.

### Strengths
The proposed combination of GNN with center loss makes sense for the application.

### Weaknesses
The paper combines graph neural networks to model a control flow in binaries with centroid based losses. Since both paradigms are well known (authors fails to reference centroid based losses such as arc-face [1] or center loss [2]. The approach to out-of-distribution detection (ood) is similar to that in [3], albeit that in the proposed paper might be computationally cheaper due to replacing k-nn with a distance to a center.
I think that the paper is a solid work, but targets the wrong audience. ICLR papers, in my opinion, should be more about new general approaches or new domains which are important and very different from other domains, such that they require special methods or the prior art is failing. This manuscript is more about combining existing tools in a nice application and would be more suited to a good security conference.
As a comment, I do not think that the proposed approach solves the ood. I see the problem of OOD inherent to NN implementing injective map (not surjective). This means that many semantically different samples gets mapped by NN to the same region with the same score. The proposed method decrease this problem, but does not remove it.

### Questions
* Can you elaborate on that OOD might be caused by NN implementing injective map (not surjective)?

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor
