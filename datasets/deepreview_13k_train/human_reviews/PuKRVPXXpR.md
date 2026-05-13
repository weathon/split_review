# ResTran: A GNN Alternative To Learn Graph With Features

- Decision: Reject
- Scores: 3, 3, 5, 3

## Abstract
This paper considers a vertex classification task where we are given a graph and associated vector features.
The modern approach to this task is graph neural networks (GNNs). 
However, due to the nature of GNN architectures, GNNs are known to be biased to primarily learn homophilous information.
To overcome this bias in GNN architectures, we take a simpler alternative approach to GNNs.
Our approach is to obtain a vector representation capturing both features and the graph topology.
We then apply standard vector-based learning methods to this vector representation.
For this approach, we propose a simple transformation of features, which we call \textit{Resistance Transformation} (abbreviated as \textit{ResTran}).
We provide theoretical justifications for ResTran from the effective resistance, $k$-means, and spectral clustering points of view.
We empirically demonstrate that ResTran is more robust to the homophilous bias than established GNN methods.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes ResTran as an alternative to GNNs that may not suffer from homophilous bias and over-smoothing. ResTran is to first transform node features using graph spectral information so that graph structural information can be preserved in the transformed features. After that, one can directly apply vector-based learning methods on the transformed features, e.g., SVM, for node classification tasks on graph-structured data. The authors justify ResTran theoretically by drawing connections from effective resistance, k-means, and spectral clustering and justify it empirically by comparing with three traditional GNN architectures over 11 datasets. The experiments show that ResTran can perform comparably with baselines on homophilous datasets and outperform them on heterophilous datasets.

### Strengths
1. ResTran may not be biased towards homophilous data like traditional GCNs.
2. The proposed feature transformation is simple and may already be effective in capturing topology information.

### Weaknesses
1. It seems to me ResTran is closely related to 1-layer message-passing neural networks (MPNNs), since it utilizes $L^+$ to transform node features $X$ and it is known that $ L^+_{ij} $ represents the effective resistance between two end nodes in the graph interpreted as an electrical network. While traditional MPNNs utilize adjacent matrix $A$ to transform $X$ and have weight 0 when there is no edge between two nodes, I find the key idea is similar, which sounds like ResTran is still in some sense a GNN. The core operation of ResTran, using the pseudo-inverse of the Laplacian, is a form of global message passing, where every node's feature is influenced by all other nodes to some degree, weighted by effective resistance. This is conceptually similar to a single layer of a GNN with a global receptive field, making the distinction less clear than presented.

2. I do not really see that ResTran is simpler than existing GNNs. Depending on the definition of complexity, I find the feature transformation is already non-trivial as it includes utilizing Krylov subspace method to approximate the transformed features. After that, from the experiments, it seems it still needs complex neural networks to get decent results, i.e., AVAE, and using simple methods such as SVM does not seem to work. The claim of simplicity is further undermined by the need for Krylov subspace methods for approximation, which introduces additional computational overhead and complexity. The fact that simple models like SVM perform poorly suggests that the transformed features are not inherently more amenable to simple classification, requiring more complex models to extract useful information.

3. The authors claim that ResTran may not suffer from over-smoothing and can overcome homophilous bias, and I think these need to be further discussed. It appears it is because ResTran only utilizes $L^+$ transforms features **once** (somewhat like a 1-layer MPNN) that it does not suffer from those issues, but it may come at the cost of the capability of capturing topological information in graphs. More experiments need to be done to demonstrate its capability, for example, comparing ResTran with [1], where some simple tricks were proposed to improve GCNs and, even with different splits, it seems it significantly outperforms ResTran, especially on heterophilous datasets. The single transformation with $L^+$ might indeed mitigate over-smoothing, but it also limits the model's ability to learn hierarchical or multi-hop relationships, which are often crucial for complex graph tasks. The comparison with [1] highlights that simply avoiding over-smoothing is not sufficient; the model must also effectively capture relevant topological information, which ResTran seems to struggle with.

4. I am unsure if the comparison is fair. Different from traditional GNNs, which propagate features with $A$, use MLPs to make predictions, and train the network with a classification loss, it seems critical for ResTran to use some semi-supervised models such as VAT and AVAE to get good results. However, the node representations yielded by those GNNs are not trained in the same way, e.g., VAT involves adversarial training--it is known that adversarial training can also further improve GNNs' performance [2]. The reliance on semi-supervised methods like VAT and AVAE for ResTran introduces a confounding factor, as these methods involve additional training mechanisms (e.g., adversarial training in VAT) that are not present in the baseline GNNs. This makes it difficult to isolate the specific contribution of the ResTran feature transformation and raises concerns about the fairness of the comparison.

### Questions
1. Are there any particular reasons for using a different dataset split instead of the one that has been widely used in the previous literature?
2. I was wondering how AVAE is used exactly for node classification tasks. Will ResTran + MLP + Cross-entropy work?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors proposed a simple architecture for node classification tasks in graph formatted dataset name ResTran. It utilized the well-known spectral clustering methods to first generate vector representation of nodes in graph that incorporate both node features and graph connectivity, then apply standard vector based ML methods to them for downstream task. ResTran was claimed to be robust to homophilous bias which is commonly seem in traditional GNN settings.

### Strengths
Pros: 
- Extensive summary of spectral clustering and other preliminaries. 
- Overall good written and easy to follow.
- Simplify structure.

### Weaknesses
Overall, I found the paper raise more concerns than it claimed to solve. Here are some of my major concerns: 
- Not much novelty from traditional spectral clustering methods, most part of the papers are well-known results or naive extension of existing methods.  The core idea of using spectral embeddings for node classification is not new, and the paper does not sufficiently demonstrate a significant advancement over existing spectral methods. The specific adaptation to graph data, while mentioned, lacks a clear theoretical justification for its superiority compared to directly applying spectral clustering on the adjacency matrix, especially given the extensive literature on graph spectral analysis.
- Most of the background or preliminaries can be distilled into shorter context or put in appendix such as propositions from previous papers, it’s currently taking more than 2 pages of the main paper. The paper spends a disproportionate amount of space on well-established concepts, which detracts from the core contribution.  For instance, the detailed exposition of spectral clustering and related mathematical propositions could be significantly condensed or moved to an appendix, allowing for a more focused presentation of the proposed method and its unique aspects. This would improve the readability and impact of the paper.
- No complexity analysis to support the claim that it’s less complicated than GNN. While the authors claim simplicity, there is no formal analysis of the computational complexity of ResTran, especially in comparison to GNNs. A detailed analysis of time and space complexity, considering factors like graph size and feature dimensions, is crucial to substantiate the claim of reduced complexity. Without this, the claim remains unsubstantiated.
- Using the shifted graph Laplacian term b to control the heterphilous information in feature map seems to require a lot of fine tuning. How to choose the hyperparameters (b, r, etc) in experiment section is not clear to me, based on the appendix the authors used a fixed value, some ablation study would be nice to see. The use of the shifted graph Laplacian with parameter 'b' to control heterophily is not well-justified. The paper lacks a clear explanation of how 'b' should be chosen, and the experimental section does not provide sufficient ablation studies to demonstrate the impact of this parameter.  The lack of a principled method for parameter selection raises concerns about the robustness and generalizability of the approach.
- There are multiple works in GNN that already support heterophilous dataset without over-smoothing. The authors’ claim about the lack of GNN is not valid. I would suggest the authors to at least do some comparison with the recent ones. The paper's assertion that GNNs are inadequate for heterophilous graphs is not accurate. There are several GNN architectures that have been specifically designed to handle heterophily without over-smoothing. The authors need to acknowledge these works and provide a more nuanced comparison.
- Experiment section lack of comparison to more recent GNN works that also targeting at heterophilous datasets.

### Questions
It seems like the authors didn't include most recent works in heterophilous GNNs and most of the claims against GNNs are lack of support. To name a few, JKNet [Xu et al., 2018], H2GCN [Zhu et al., 2020a], Geom-GCN [Pei et al., 2020],  GPR-GNN [Chien et al., 2020], GPNN [Yang et al., 2022] and many more are all methods that work with heterophilous graph dataset. I would recommend the authors to at least go over the literature before making the final conclusion.

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper seeks to addresses the vertex classification problem in a manner different to standard GNN research. The idea is to utilize standard spectral methods such as clustering and sparsification methods to define new embeddings. The authors experimentally demonstrate that these embeddings out-perform standard GNNs on some datasets. Specifically, the authors propose "Resistance Transformation" on feature vectors X: Simply transform X by utilizing the Laplacian basis used to compute effective resistances, and feed the resulting data to standard vectorial learning algorithms.

### Strengths
Devising novel positional encodings, to the extent of eliminating the need for message-passing mechanisms, might be a worthwhile idea to explore. The authors also place their method within the homoplily/heterophily narrative, arguing that their embedding has lesser homophilious bias as compared to standard GNNs.

### Weaknesses
I am not sure about the computational complexity of these methods: The authors should have included some experimental results on time complexity to indicate whether the usually expensive eigenvector computations can be justified instead of simple combinatorial message passing. Specifically, the authors should have provided a breakdown of the time spent on computing the Laplacian basis versus the time spent on the downstream learning algorithm. It is unclear if the reported runtimes include the spectral computations or only the downstream learning phase. Furthermore, the authors should have clarified if they are using full eigendecomposition or Krylov subspace methods to accelerate the computation, and how this affects the overall runtime, particularly on sparse graphs.

Spectral embeddings/methods have inherent limitations in the kind of data they can capture from a graph: They fail to capture relational aspects of data (such as node/edge-colors) and so on, unlike combinatorial message-passing algorithms. The proposed method seems to treat all nodes as if they are of the same type, which is a severe limitation in many real-world networks. If the authors propose such a radical departure from standard GNN methods, they should investigate their method on a variety of datasets, such as molecular graphs or synthetic graphs arising from relational sources. The lack of experiments on graphs with rich node and edge attributes makes it difficult to assess the general applicability of the proposed approach.

### Questions
1. The computational cost of spectral methods typically goes to O(n^3). Can the authors comment on the running time complexity of the Krylov-subspace based embedding and compare it with the run-time costs of a standard message-passing GNN? Have the authors carried out any experiments to compare the run-time costs of the two approaches? Especially, I would like to know the status on sparse graphs, where the pseudo-inversions might be way more costly than message-passing. And how does the time complexity scale with graph size? The empirical investigation considers only medium-sized graphs.

2. How does the proposed method differ from the commonly used positional encodings based on spectral properties of the input graph?

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors propose an unsupervised method that first combine the node feature with graph topology into a node-wise embedding. Then apply any standard machine learning method for the downstream tasks.

### Strengths
-	The connection to some unsupervised graph learning method is interesting.

### Weaknesses
 -  Insufficient literature survey on the related work.
-  The novelty is extremely limited. See comments below.
-  The claim that existing GNNs can only work well on heterophilic graphs with complicated architecture is false. The authors not only ignore the complete literature of spectral GNNs but also LINKX method.

My first concern with the work is that its literature survey on prior related works is insufficient. Note that one major claim of this paper is that current GNNs can not handle heterophilic graphs if not using complex architecture. However, this is apparent wrong as the line of spectral GNNs research tackles this problem with a very simple design [1,2,3]. Also, LINKX [4] is another simple architecture that has been shown superior performance on heterophilic graphs. Notably, spectral GNNs are shown to be capable of learning ``any’’ graph spectral filtering that is beyond just low-pass (homophily) and high-pass (heterophily) cases. It is surprising that the authors completely ignore this literature.

On the other hand, the idea of obtaining node embedding from node features and graph topology in an unsupervised fashion has also been proposed previously. One of the early model SIGN [5] propose to compute propagated features $X, AX, A^2X,\cdots,A^KX$ first (with $A$ being potentially normalized or use $L$ instead) and concatenate them as the node embedding for applying MLP in downstream tasks. This work has also led to a series of works focusing on scalable graph learning methods such as SAGN [6] and GAMLP [7] with similar ideas. The ResTrans method is just using the embedding $L^{-1/2}X$. Note that one potential drawback of ResTrans is its computational complexity. Indeed, as the authors mentioned, naively compute $L^{-1/2}$ is computationally infeasible. They propose to apply the Krylov subspace method, which essentially computes $X,LX,L^2X,\cdots,L^rX$ and is very similar to SIGN design. It is a surprise to me that the authors completely miss this line of work as well. Compared to these prior works, I think the novelty of the proposed method is relatively limited.

I would suggest the authors explain the difference of their method to at least SIGN and compare them carefully in the experiments. Also, I think the authors should also compare to some spectral GNN baselines such as those in [1,2,3]. Otherwise, it is hard to convince me that ResTrans is a good method for heterophilic graphs.

### Questions
1.	Discuss and compare with spectral GNNs [1,2,3] in both methodologies for heterophilic graphs and experiments.
2.	Compare with SIGN methods in both methodology and experiments.

### Soundness
1 poor

### Presentation
2 fair

### Contribution
1 poor
