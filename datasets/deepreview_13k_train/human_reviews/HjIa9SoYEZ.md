# CTRL: Graph condensation via crafting rational trajectory matching

- Decision: Reject
- Scores: 5, 6, 5, 3

## Abstract
Training on large-scale graphs has achieved remarkable results in graph representation learning, but its cost and storage have raised growing concerns. Generally,
existing graph distillation methods address these issues by employing gradient
matching, but these strategies primarily emphasize matching directions of the
gradients. We empirically demonstrate this can result in deviations in the matching
trajectories and disparities in the frequency distribution. Accordingly, we propose
CrafTing RationaL trajectory (CTRL), a novel graph dataset distillation method.
CTRL introduces gradient magnitude matching during the gradient matching process by incorporating the Euclidean distance into the criterion. Additionally, to
prevent the disregard for the evenness of feature distribution and the lack of variation that the naive random sampling initialization may introduce, we adopt a simple
initialization approach that ensures evenly distributed features. CTRL not only
achieves state-of-the-art performances in 34 cases of experiments on 12 datasets
with lossless performances on 5 datasets but can also be easily integrated into other
graph distillation methods based on gradient matching.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigates key modules within graph condensation. Firstly, it points out that using cosine similarity as the loss in graph condensation fails to account for gradient magnitude, prompting the adoption of a loss incorporating Euclidean distance. Secondly, the paper highlights that the completely random initialization in graph condensation is suboptimal, leading to the utilization of a clustering algorithm on node features to enhance initialization quality. Extensive experiments demonstrate that the proposed approach improves the quality of the condensed graph and reveals the relationship between graph frequency distribution and gradient magnitude.

### Strengths
1. The paper is easy to follow and generally well-written.
2. The motivation appears to be both reasonable and clear.
3. The experiments are thorough and comprehensive.

### Weaknesses
 1. Novelty of the proposed methods is limited, which seems a simple adaptation of an existing method from CV literature, and the proposed methods do not appear to be specifically designed for graphs. Firstly, the loss formula (Equation 3) that considers gradient magnitude is identical to Equation 9 in [1]. Secondly, the initialization step using k-means is performed on node features, which overlooks the influence of graph structure. For instance, if two nodes have the same features but significantly differ in their neighbors, the approach described in the paper would not select both nodes simultaneously, even though they would have completely different embeddings after message passing.

 2. The setup of the ablation experiments is not clearly defined. It is not specified which loss was used to train the models in Figure 3 (c) and (d). It is not specified what initialization was used for the model in Figure 3 (e).

 Minor comments:
 There are quite a few typos in the paper where "ogbn-arxiv" is misspelled.

### Questions
1. Are there any differences in applying CTRL to graphs compared to its application in computer vision?
2. What is the value of beta in the training of models in Figure 3 (c) and (d)? How is the models in Figure 3 (e) initialized?
3. Some of the compared methods, such as GCond, had their code updated recently. Has the performance of these methods been re-evaluated, specifically regarding the results presented in Table 1?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies a newly proposed graph condensation method. The authors argue that existing methods focus solely on matching gradient directions, which can lead to issues. To address this, the authors propose CTRL, a novel method that incorporates gradient magnitude matching using Euclidean distance and ensures an even feature distribution. CTRL outperforms existing methods in experiments on multiple datasets, making it a promising addition to graph distillation techniques.

### Strengths
1. It is crucial to address the issue of existing costs in training large-scale graphs through graph condensation and summarization, as it remains an under-explored problem.
2. It is interesting to observe how the authors have justified a strong correlation between the frequency distribution and the gradient magnitude during training GNN models.
3. Various experiments are conducted, including the generalization experiments

### Weaknesses
 1. In section A.2, it is stated, 'We match gradients smaller than this threshold on both direction and magnitude, while gradients exceeding the threshold are matched solely based on their directions.' Can the authors provide a detailed demonstration of why considering both gradient matching based on direction and magnitude may not be helpful? This is essential for assessing the effectiveness of CTRL for large datasets, and it appears to be missing from the conducted experiments.
2. The overall method is similar to the recently proposed graph condensation methods (especially GCond as it also uses a gradient matching scheme). The novelty is somewhat limited, although the struggle to capture the feature distribution in this problem is interesting.
3. Can the authors explain in detail why leveraging gradient magnitude matching is correlated with frequency distribution? Did the authors also measure the correlation between gradient direction matching (cosine similarity between gradients) and frequency distribution? These correlations can be investigated through running some experiments.

### Questions
My major questions on the experimental evaluation. It would tremendously strengthen this work by addressing the concerns listed in the Weakness section.

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
This paper studies the weaknesses of previous graph condensation methods, specifically GCOND, which aims to synthetic a small graph to replace the original graph by matching model gradients. This paper points out two shortcomings: First, GCOND uses cosine distance to measure the similarity of gradients, ignoring the magnitude of gradients. Second, the random initialization of GCOND results in poor diversity. To improve the performance, this paper introduces Euclidean distance and clustering-based sampling, highlighting that they can preserve the frequency distribution of the original graph. Extensive experiments demonstrate the effectiveness of the proposed method.

### Strengths
1. This paper presents a new perspective on the relationship between gradient matching methods and the frequency distribution of signals.

2. The extensive experiments, including performance, generalization, visualization, and neural architecture search, validate the effectiveness of the proposed method. Besides, the proposed method achieves state-of-the-art performances in most cases.

### Weaknesses
1. The Euclidean distance has been widely used in the trajectory matching [1]. Replacing the cosine distance with Euclidean distance in gradient matching is not very surprising.

2. The empirical results of this paper show that minimizing the Euclidean distance between model gradients can align the frequency distribution between synthetic and real graphs. However, there is no theoretical analysis of the relationship between gradient magnitude and frequency distribution. Additionally, it is unclear to me why matching the frequency distribution of graphs helps the distillation process.

3. There is no ablation study to evaluate the roles of direction-based matching, magnitude-based matching, and their combination. 

4. This paper does not report of performance of SFGC [2], which is a strong graph condensation baseline, in Tables 3 and 4.

5. Minor Typo. In several instances, the authors mistakenly write ‘Ogbn-arxiv’ as ‘Ogbn-arvix’.

### Questions
See weaknesses.

### Soundness
2 fair

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
This paper extends the gradient-matching approach for graph condensation by not only leveraging cosine similarity to align gradient directions but also incorporating a regularization term based on Euclidean distance. Empirical evidence suggests that this added Euclidean distance component aids in aligning the frequency distribution with that of the original data. Experimental outcomes demonstrate that the introduced method marginally outperforms existing benchmarks in both node and graph classification evaluations.

### Strengths
S1: The exploration of integrating the Euclidean distance component into gradient matching, and its potential impact on frequency alignment, offers insights that could be valuable to the community.

S2: The paper is well-organized and presents a clear narrative. The experiments showcased are comprehensive and thoughtfully executed.

### Weaknesses
W1: The core techniques introduced in this paper, including the Euclidean distance component and replacing the random initialization of the synthetic data by selecting nodes from sub-clusters formulated by K-means, have all been previously adopted for dataset condensation [1][2]. This makes the proposed method appear to be a straightforward mash-up of multiple existing methods in dataset condensation, resulting in limited novelty.

W2: Although the authors repeatedly emphasize that their method considers the impact of matching gradient magnitude rather than only matching directions, in actual implementation, they introduced a regularization term based on the Euclidean distance between gradients. This is somewhat inconsistent with their statement and might be misleading, as the Euclidean distance also considers differences beyond just the magnitude of vectors.

W3: From the presented results, it seems that the proposed method does not offer significant improvements over the compared state-of-the-art.

### Questions
Q1: Following up on W2, in Equation 3, I'm curious about why you did not directly address the magnitude differences between gradients. That is,  instead of using the proposed Euclidean distance between gradients, $ \lVert \mathbf{G}{\mathbf{i}}^{\mathcal{S}}-\mathbf{G}{\mathbf{i}}^{\mathcal{T}} \rVert $, why not directly employ $ \lVert \mathbf{G}{\mathbf{i}}^{\mathcal{S}} \rVert  - \lVert\mathbf{G}{\mathbf{i}}^{\mathcal{T}}\lVert $?

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor
