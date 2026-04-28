# Graph-level Representation Learning with Joint-Embedding Predictive Architectures

- Decision: Reject
- Scores: 3, 3, 6

## Abstract
Joint-Embedding Predictive Architectures (JEPAs) have recently emerged as a novel and powerful technique for self-supervised representation learning. They aim to learn an energy-based model by predicting the latent representation of a target signal $y$ from the latent representation of a context signal $x$. JEPAs bypass the need for negative and positive samples, traditionally required by contrastive learning while avoiding the overfitting issues associated with generative pretraining. In this paper, we show that graph-level representations can be effectively modeled using this paradigm by proposing a Graph Joint-Embedding Predictive Architecture (Graph-JEPA). In particular, we employ masked modeling and focus on predicting the \emph{latent} representations of masked subgraphs starting from the latent representation of a context subgraph. To endow the representations with the implicit hierarchy that is often present in graph-level concepts, we devise an alternative prediction objective that consists of predicting the coordinates of the encoded subgraphs on the unit hyperbola in the 2D plane. Through multiple experimental evaluations, we show that Graph-JEPA can learn highly semantic and expressive representations, as shown by the downstream performance in graph classification, regression, and distinguishing non-isomorphic graphs. The code will be made available upon acceptance.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes Graph-JEPA, the first Joint-Embedding Predictive Architectures (JEPAs) for the graph domain.
The application of JEPA to graphs seems to be novel.

### Strengths
- The proposed method is technically sound
- Based on the experimental results, the improvement between Graph-JEPA over the baselines seems to be strong

### Weaknesses
- The overall method seems to be a direct application of JEPA to graphs.
- The discussion of "why does graph-JPEA works" is useful, but not information. Any theoretical analysis here will be useful.
- The experimental settings are confusing. It is unclear to me why "GCN", a GNN model, can be compared with "Graph-JEPA", which is a graph self-supervised training method.
- All the figures and tables are not professional and could be improved to be more appealing. Font sizes and colors should be improved.

### Questions
- What makes applying JEPA to graphs special and non-trivial?

### Soundness
3 good

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose Graph-JEPA. Graph-JEPA uses two encoders to receive the input and one of the encoders predicts the latent representation of the input signal based on another encoder.

### Strengths
The writing is clear. First JEPA for graph. The authors provide an analysis to explain why JEPA works for the graph domain.

### Weaknesses
1. The method is not novel. The proposed Graph-JEPA is very similar to MLM in BERT, which utilizes the context to predict the masked word type. 

2.  The proposed method is too simple and the motivation is not clear. We have graph MAE and contrastive learning. Why do we need JEPA for the graph domain?

3. Compared with graph MAE and S2GAE, the performance is not good enough to show it can inspire future research.

### Questions
N/A

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes a new self-supervised technique for graph neural networks. Grounded on joint-embedding predictive architecture (JEPAs), the proposed Graph-JEPA is designed to predict the latent embeddings for multiple subgraphs based on a random subgraph. Experiments are performed on graph-level tasks.

### Strengths
1.	The design of the loss objective is good.

2.	The ablation studies and discussion are detailed and insightful.

### Weaknesses
1.	Missing literature in related work. In addition to contrastive methods and generative methods, self-supervised graph representation should also include existing predictive methods [1]. For example, CCA-SSG [2] and LaGraph [3] are two existing works using latent embedding prediction. Such predictive methods should be discussed in related works, and they should be used as baseline methods to compare results. 

2.	The performance improvement is marginal based on the main results in Table 1. 

3.	Most existing SSL methods can handle both graph-level and node-level tasks. However, the proposed Graph-JEPA only supports graph-level downstream tasks. 

[1]. Xie, Yaochen, et al. "Self-supervised learning of graph neural networks: A unified review." IEEE transactions on pattern analysis and machine intelligence 45.2 (2022): 2412-2429.

[2]. Zhang, Hengrui, et al. "From canonical correlation analysis to self-supervised graph neural networks." Advances in Neural Information Processing Systems 34 (2021): 76-89.

[3]. Xie, Yaochen, Zhao Xu, and Shuiwang Ji. "Self-supervised representation learning via latent graph prediction." International Conference on Machine Learning. PMLR, 2022.

### Questions
1.	Authors claim that the Graph-JEPA is more efficient than contrastive methods since it doesn’t require data augmentations or negative samples. I’m wondering how efficient it is. Could you add a quantitative comparison for the efficiency?

2.	The proposed Graph-JEPA uses Transformer encoder blocks. However, most baseline models are based on simpler models like GIN and GCN. Is it an unfair comparison? Can you use GIN/GCN encoder?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
