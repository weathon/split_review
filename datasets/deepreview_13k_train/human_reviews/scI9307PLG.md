# Bundle Neural Network for message diffusion on graphs

- Decision: Accept
- Scores: 8, 6, 8

## Abstract
The dominant paradigm for learning on graph-structured data is message passing. Despite being a strong inductive bias, the local message passing mechanism suffers from pathological issues such as over-smoothing, over-squashing, and limited node-level expressivity.
To address these limitations we propose Bundle Neural Networks (BuNN), a new type of GNN that operates via \emph{message diffusion} over \emph{flat vector bundles} – structures analogous to connections on Riemannian manifolds that augment the graph by assigning to each node a vector space and an orthogonal map. A BuNN layer evolves the features according to a diffusion-type partial differential equation. When discretized, BuNNs are a special case of Sheaf Neural Networks (SNNs), a recently proposed MPNN capable of mitigating over-smoothing. The continuous nature of message diffusion enables BuNNs to operate on larger scales of the graph and, therefore, to mitigate over-squashing. Finally, we prove that BuNN can approximate any feature transformation over nodes on any (potentially infinite) family of graphs given injective positional encodings, resulting in universal node-level expressivity. We support our theory via synthetic experiments, and showcase the strong empirical performance of BuNNs over a range of real-world tasks, achieving state-of-the-art results on several standard benchmarks in transductive and inductive settings.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper extends previous work on graph neural networks equipped with cellular sheaves by introducing a more efficient way of computing the heat diffusion over bundles. The key idea of the authors is to assume a simpler form for the sheaves, namely a flat vector bundle, which can be thought of as an orthogonal map associated with each node (as opposed to one associated with each node-edge pair). This assumption significantly simplifies the computations necessary to learn the bundles from data. In particular, the heat diffusion kernel can now be computed efficiently during the learning of the bundles. This enables the authors to use spectral methods to run the diffusion process for long periods of time addressing the over-squashing problem on graphs. This flat vector bundles also bring the strength of the cellular sheaves in that the fixed point of diffusion is no longer a trivial state where all nodes share the same features. Rather, the long time limit now has richer structure where variation is allowed across the nodes. This addresses the over-smoothing problem. The authors propose GNN architecture using flat vector bundles and heat kernels (computed both using Taylor expansions and spectral methods) and demonstrate improved performance on synthetic data sets and real data sets.

### Strengths
This reviewer generally liked the paper. The idea of simplifying cellular sheaves using flat vector bundles is clever. This idea seems to solve the key problem with the computational complexity challenges faced by neural sheaf diffusion. Another strength of the paper is the clever synthetic toy models which demonstrate the gain from the proposed bundle architecture very clearly, especially when it comes to the over-squashing problem. The empirical performance of the proposed method is also impressive, especially on heterophilic graphs like minesweeper. The novel notion of expressivity introduced by the authors is also intriguing.

### Weaknesses
A weakness of this paper is that the central idea is arguably a simple extension of the neural sheaf diffusion paper. It is not clear that this constitute significant advance. This is balanced by the impressive empirical results in the paper.

The authors highlight well the advantages of replacing the cellular sheaves with flat vector bundles. However, it is not clear what is the cost of doing so. How does expressivity suffer with this assumption? Are there circumstances under which this simplification works better? For example, does the sparsity of the graph play role. More discussion on this would have helped the reader. The authors nicely show the existence of fixed points for the diffusion process under flat vector bundles and that features across nodes are related by orthogonal transformations. How does this compare with the structure of fixed points under general cellular sheaves? How does this impact the expressivity of the bundle neural networks compared with their sheave counterpart?

This reviewer struggled at times to understand how much the principled geometric approach brought over from topology and differential geometry contributed to formulation of the proposed GNN. Although interesting, can the author's approach be though of as learning a transformation on each node. With the formality relaxed, it is not clear if this transformation needs to be orthogonal. The authors seems to go to quite a bit of trouble to ensure that the learned matrices at each node are orthogonal. Of course, Riemannian manifolds require this, but is it really needed? Would invertible matrices done just as good of a job? It seems like in practice they are limited to using only 2-dimensional vector spaces on each node, with the transformation matrices parameterized explicitly to be orthogonal.

This reviewer was bothered at times by the strong use of language by the authors. The claim that the proposed bundle approach solves the over-squashing problem is over-stated. Any spectral method will address over-squashing. The authors have proposed an efficient way to compute the heat kernel more efficiently by replacing cellular sheaves with flat vector bundles. This allows them to run diffusion for longer times. There is no conceptual new solution to over-squashing.

### Questions
What price is paid for going rom the full cellular sheaves to the flat vector bundle in expressivity? In practice, in what settings is the flat vector bundle approach good enough? For example, it seems like that for sparse graphs the orthogonal maps associated with each node would be good enough.

Similarly, can the authors provide a comparison between the structure of the fixed points for cellular sheaves and flat vector bundles? It seems like some of the "richness" of the long time limit of diffusion is lost with the flat vector bundles. How does this reflect on expressivity of flat vector bundles compared with cellular sheaves?

Does the transformation learned for each node need to be orthogonal in practice? It seems that the approach is somewhat limited because the learned matrices must be orthogonal. It is difficult to learn matrices that are constrained to be orthogonal. Can the authors relax this requirement in practice and use invertible matrices or a fully unconstrained matrix?

It seems like a key aspect of the proposed approach is how the orthogonal transformations at each node are learned? The authors mention MLPs or even GNNs that take in the graph structure and positional encodings of the nodes. What type of positional encodings are best for learning the orthogonal transformations? Why are the node features not taken into account when computing the orthogonal map for each node? Are the authors trying to keep the graph geometry distinct from the feature information? 

In Table 3, how does the BuNN approach outperform the NSD for the data sets in which memory is not a limit for NSD? Is the depth of the models in BuNN larger helped by spectral methods? It seems like depth was 1 for the amazon-ratings data set. Does NSD overfit the data because of its use of cellular sheaves?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper proposes a new graph neural network architecture called Bundle Neural Networks (BuNNs). The architecture is based on message diffusion on flat vector bundles which are topological structures that assign to each node a vector space and an orthogonal map. They seem to be inspired from Sheaf neural networks and, in different forms, are claimed to address the problems of overs-moothing and over-squashing. Theoretical analysis on the feature transformation with injective positional encodings shows uniform expressivity. Further analysis on the properties of BuNNs and experimental results on both synthetic and real-world datasets, are provided for validating the proposed model.

### Strengths
1. The paper addresses an important problem of oversmoothing and oversquashing seen in GNNs via vector bundles, building on cellular sheafs in GNNs.
1. The use of flat vector bundles with orthogonal maps to reduce the computational complexity is interesting.
1. The paper is well-organized.

### Weaknesses
1. The experiments to validate oversmoothing and oversquashing are not comprehensive. The authors can test the oversquashing on Neighbours match dataset [1], which has been used well in multiple papers. Further the authors can explore using effective resistance metric to measure oversquashing [3] and [4].

2. Related works which are designed via dirichlet energy optimization like [2] are not discussed. May help to discuss the difference with [2] in terms of results on oversmoothing.

### Questions
Please see weaknesses

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes to perform message-passing over a diffused graph using flat vector bundles. This is achieved by transforming each node state within its own vector space using a learned and distinct orthogonal map. This is the message that a node sends to each neighbor, where the inverse of the orthongonal map from the receiving node is used as a decoding mapping. The authors show that this can avoid over-smoothing, over-squashing, and can be a compact uniform approximation over a set of graphs. Experiments show the effectiveness of the proposed approach.

### Strengths
The proposed method is sound and very general. BuNNs have many favorable and interesting properties. I particularly like the property regarding fixed points. The paper is nicely written and mostly understandable.

### Weaknesses
 * Eq. 2: From the theoretical derivation, this step does not seem needed as $\mathcal{H}_B$ already applies $O_v$ and $O_u$. The only provided reason is that it helps to prove Theorem 5.3. Are there other reasons why $W$ and $b$ are introduced? What happens when these are removed?
* BuNNs and their properties are mostly compared to MPNNs applied to the original. It seems fairer to me to also compare its properties to Graph Transformers and infinite-depth MPNNs (e.g. [1]) (Table 1).
* Theorem 5.3:
    * This statement is quite interesting but I do not fully understand it. In which cases are injective positional encodings achievable? Would it be satisfied when $\mathcal{G}$ is a set of WL distinguishable graphs and we use WL colors are positional encodings?
    * How does it deal with two nodes $u,v$ in the same graph with the same WL unfolding tree? By my understanding of the injective positional encodings, they could still have the same initial state. The MLP (Eq. 1) would produce the same $\mathbf{O}_v = \mathbf{O}_u$ for both nodes.
    * Which changes would be needed for graph transformers to also satisfy this universality?
* Table 2: A comparison with Graph Transformers or infinite-depth MPNNs would be insightful
* Table 3: It seems like the authors performed experiments for NSD and BuNN, but hyperparameter ranges and optimal hyperparameters are only presented for BuNN.
* Details about runtimes are missing. It would be important to have execution times for at least one experiment for BuNN for a comprehensive evaluation.

### Questions
* See weaknesses

### Soundness
3

### Presentation
2

### Contribution
2
