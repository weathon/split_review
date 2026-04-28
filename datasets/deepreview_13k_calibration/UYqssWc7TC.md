# Labels Are Not All You Need: Evaluating Node Embedding Quality without Relying on Labels

- Decision: Reject
- Avg Score: 3.67
- Scores: 5, 3, 3

## Abstract
Graph Neural Network (GNN) based node embedding methods are a promising approach to learning node representations for downstream tasks such as link prediction, node classification, and node clustering. GNN-based methods usually work in an unsupervised or semi-supervised manner, learning node representations without or with limited label information. We empirically show, however, that the performance of learned node embeddings on downstream tasks may be heavily impacted by the GNN-method's hyperparameter configuration. Unfortunately, existing hyperparameter optimisation methods typically rely on labeled data for evaluation, making them unsuitable for unsupervised scenarios. This raises the question: *how can we tune the hyperparameters of GNNs without using label information to obtain high quality node embeddings?* To answer this, we propose a framework for evaluating node embedding quality without relying on labels. Specifically, our framework consists of two steps: *building prior beliefs* that characterise high-quality node embeddings, and *quantifying the extent* to which those prior beliefs are satisfied. More importantly, we instantiate our framework from two different but complementary perspectives: spatial and spectral information. First, we introduce the Consensus-based Space Occupancy Rate (CSOR) method that evaluates node embedding quality from a spatial view. It conducts pairwise comparisons of the spatial distances between node embeddings obtained from various hyperparameter configurations. Next, we present the Spectral Space Occupancy Rate (SSOR) method, which takes a spectral perspective and evaluates the embedding quality by examining the singular values of the node embedding matrices. Extensive experiments on seven GNN models with four benchmark datasets demonstrate the effectiveness of both CSOR and SSOR. Specifically, both methods consistently prioritise hyperparameter configurations that yield high-quality node embeddings for downstream tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors propose a framework for evaluating node embedding quality in Graph Neural Networks (GNNs) without relying on label information. This framework introduces two novel metrics: the Consensus-based Spatial Occupancy Rate (CSOR) and the Spectral Space Occupancy Rate (SSOR).
CSOR and SSOR aim to assess embedding quality from spatial and spectral perspectives, respectively. The authors use unsupervised graph representation learning algorithms to build the framework for unsupervised training.
The authors also conduct experiments on different combinations of HP across multiple GNN models and citation network graph datasets, showing that these metrics can rank hyperparameter configurations effectively, identifying those that yield high-quality embeddings for downstream tasks.
The study provides unsupervised metrics for node embedding evaluation, potentially benefiting applications where labeled data is costly or unavailable.

### Strengths
New Metrics: The framework introduces two new metrics, CSOR and SSOR, which provide spatial and spectral assessments of embedding quality without labels. This is an innovative approach that aligns with the growing interest in unsupervised learning methods within GNN research.
Clarity: The paper is well-organized, and the explanations of CSOR and SSOR are detailed.

### Weaknesses
1. Method Comparison Clarity:
The proposed CSOR and SSOR methods may have limited significance, as their performance is generally inferior to that of RankMe. The authors do not provide a clear rationale for using CSOR or SSOR over RankMe, nor do they clarify the relationship between CSOR and SSOR. This lack of clarity makes it difficult to determine whether to prioritize HP chosen by CSOR or SSOR in future applications, thereby limiting the practical utility of these methods. Specifically, the paper lacks a detailed analysis of scenarios where CSOR or SSOR might outperform RankMe, or what specific characteristics of the embeddings each metric captures that might be useful in different contexts. The absence of such analysis makes it difficult to justify the introduction of these new metrics.

2. Use of Modified Models:
In the Node_Embedding_models.py file, the authors modify the original training methods of GAT and GIN, using them as encoders within the framework of the Graph Autoencoder (GAE) model for unsupervised training. However, this adaptation is not clearly stated in the paper, which could lead to confusion about the actual use of these models. This modification is significant because it changes the underlying training paradigm of these models, and the results may not be directly comparable to their original implementations. The paper needs to explicitly state and justify this architectural choice, and discuss its potential impact on the observed results.

3. Lack of Comparative Experiment with Contrastive Learning:
The paper overlooks an important comparative experiment in unsupervised learning between generative learning and contrastive learning. Contrastive learning (eg. GraphCL), which focuses on distinguishing between similar and dissimilar instances at an abstract semantic level, offers simpler models with stronger capabilities compared to generative methods like GAE or VGAE. The absence of a comparison with contrastive learning methods leaves a gap in the evaluation of the proposed framework, as it is unclear how CSOR and SSOR would perform in the context of embeddings learned through contrastive approaches. This is a significant omission given the widespread use and effectiveness of contrastive learning in unsupervised graph representation learning.

4. Dataset Scope and Variety:
The paper primarily focuses on unsupervised learning for graphs, where the most common references are large-scale graph datasets due to the significant challenges posed by labeling costs. However, the four datasets used in this study are small-scale graphs, which do not fully reflect the real-world applicability of the proposed methods in large-scale settings. The authors should consider using larger graph datasets (eg. Reddit, OGBN-ARXIV) to strengthen the relevance of their work to large-scale graph learning scenarios. Additionally, the choice of datasets is limited to citation networks, which may not represent the diverse range of graph structures encountered in real-world applications. To increase the generalizability of the findings, the authors should consider using datasets from a variety of domains, such as social networks, protein interaction networks, or recommendation systems, which would better highlight the robustness of CSOR and SSOR in different contexts.

5. Minor Comments:
Figure3: The caption is stated that RankMe is represented by "green circles" in the plots; however, the actual legend used is "white diamonds."
There are multiple instances where "hyperparameters" is misspelled as "hyperparamters"; please correct these throughout the paper.
In Section 5 "SSOR", the formula may contain an error where r should possibly be r−1. 
Detailed code specifications (as the versions used) are missing.

### Questions
Please refer to the weaknesses above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper first empirically demonstrates that the effectiveness of learned node embeddings for downstream tasks is sensitive to the GNN method's hyperparameter settings. Then it introduces a framework to evaluate the quality of node embeddings without using labels. The proposed framework is comprised of two steps: building prior beliefs and quantifying the extent. Specifically, it instantiates the proposed frameworks with two methods: a Consensus-based Space Occupancy Rate (CSOR) method and a Spectral Space Occupancy Rate (SSOR). Extensive experiments on seven GNN methods demonstrate the effectiveness of the proposed methods.

### Strengths
1. This paper studies an interesting problem of how to evaluate the embedding quality without using labels.
2. Extensive empirical 
3. This paper is easy to follow and understand.

### Weaknesses
1. The problems of the motivating experiments presented in Fig. 1
- Experiments are solely conducted for a single model (VGAE). More popular GNNs such as GCN, GAT or recent Transformer based methods should be used.
- Experiments are conducted on a single dataset (Cora), and a single task (node classification). Will other datasets or tasks also exhibit a similar trend?
2. It is not clear how the authors compute the distance between embedding matrices that have different embedding sizes, e.g., $Z_1\in\mathbb{R}^{N\times d_1}$ and  $Z_2\in\mathbb{R}^{N\times d_2}$.
3. Event with the same hyper-parameters, for the same node $x$, models $f_1, f_2$ trained with different seeds could learn embeddings $z_1$ and $z_2$ at different positions in the space. I'm not fully convinced that we can directly use the embedding distance as an evaluation unless more evidence is provided.
4. According to the formulation in 270-303, essentially, CSOR measures the distance between embeddings obtained by one HP $Z$ with the averaged embeddings obtained by all other HPs. Therefore, CSOR could give those bad-performing configurations a high score, which can also be observed in Fig 42. Do you have any ideas or insights for solving this problem?
5. There is a major issue for SSOR: if the learned embedding matrix is sort of random, then it seems that it will have a very high SSOR score. 
6. It is not quite clear what's the relation between UDR in sec.2 and CSOR and SSOR introduced in the following sections.

### Questions
1. Please refer to weaknesses.
2. Have you tried other distance metrics other than Manhattan distance?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper proposed a new hyperparameter optimization method for unsupervised graph learning scheme. The new method leveraged a observation-driven scheme, which is to find prior belief (heuristic on the correlation between certain properties of the embeddings over hyperparameter configurations and the quality of the embedding) given observations and visualization over existing graph data and then rank the hyperparameter settings based on the observed heuristic scores. Specifically for graph, the paper proposed two beliefs: spectral based and spatial based to quantify the quality of the learned embeddings, corresponding to the separability of the learned embeddings. The experiments is conducted over four homophilic graph datasets and compared against existing hyperparameter optimization approaches, showing some improvements overall.

### Strengths
1. The presentation of the paper in the main text is clear and easy to follow. The motivation and the problem is clear and interesting. As a graph domain researcher, I personally find the sensitivity of the GNN models' performance over hyperparameter annoying and it took time to obtain optimal results especially when a deeper GNN is needed to alleviate oversmoothing.
2. The observation-driven approach is simple and the intuition is logical.
3. The visualization and analysis over the experimental data is comprehensive.

### Weaknesses
1. While the observation-driven approach is simple, I am not convinced that such CSOR or SSOR based heuristic is suitable for all graph datasets. As the experiments are carried only on limited four homophilic datasets, it is hard to be convinced that such heuristic can be generalized to other graph datasets.
2. The time complexity over both approaches are very high, especially for the Spectral based approach that involve SVD operation, which is known to be computationally expensive.
3. The improvements of the proposed approach is very limited compared to existing approaches such as RankMe.
4. There lack theoretical analysis on the embedding singular value over the quality of the embeddings, such as separability or the distance between embeddings over different HP configuration related to it separability.

### Questions
See weakness. Additionally, I am curious how many datasets are used to establish the prior belief in the experiment or is there random generated graph used?

### Soundness
3

### Presentation
3

### Contribution
2
