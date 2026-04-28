# Diversifying Spurious Subgraphs for Graph Out-of-Distribution Generalization

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 6, 5

## Abstract
Environment augmentation methods have gained some success in overcoming the out-of-distribution (OOD) generalization challenge in Graph Neural Networks (GNNs). Yet, there exists a challenging trade-off in the augmentation: On one hand, it requires the generated graphs as diverse as possible to extrapolate to unseen environments. On the other hand, it requires the generated graphs to preserve the invariant substructures causally related to the targets. Existing approaches have proposed various environment augmentation strategies to enrich spurious patterns for OOD generalization. However, we argue that these methods remain limited in diversity and precision of the generated environments for two reasons: i) the deterministic nature of the graph composition strategy used for environment augmentation may limit the diversity of the generated environments, and ii) the presence of spurious correlations may lead to the exclusion of invariant subgraphs and reduce the precision of the generated environments. To address this trade-off, we propose a novel paradigm that accurately identifies spurious subgraphs, and an environment augmentation strategy called spurious subgraph diversification, which extrapolates to maximally diversified spurious subgraphs by randomizing the spurious subgraph generation, while preserving the invariant substructures.  Our method is theoretically sound and demonstrates strong empirical performance on both synthetic and real-world datasets, outperforming the second-best method by up to 24.19% across 17 baseline methods, underscoring its superiority in graph OOD generalization.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
One big challenge for graph machine learning (GML) is that real-world graph data continuously evolves over time, introducing changes in graph structure and node/edge features, causing graph distribution shift. However, retaining GNN models every time the graph is updated is expensive or sometimes infeasible. How to handle the out-of-distribution (OOD) problem in GNN model training becomes a challenging problem. This paper proposes a novel theory to identify the invariant subgraphs, whose edges exhibits high predicted probabilities in the learnable data transformation to the target graph labels, and the spurious subgraph, whose edges exhibit lowest predicted probabilities. The proposed  learning framework based on the theory exhibits stable and good performance over existing baseline models on 7 real-world datasets with an average of 2.38%

### Strengths
* The paper proposes a novel theory to identify the invariant subgraphs and spurious subgraphs. The paper shows that with the proposed edge dropping function t, the graph size constraint loss L_e and the spurious subgraph diversification loss L_{div}, the proposed method can identify the invariant graphs and the spurious graphs. Furthermore, the evaluation in section 7.5 demonstrates that the proposed method can distinguish G_c and G_s using the GOOD-Motif datasets.
* The proposed methods shows stable and good performance over existing baseline models on 7 real-world datasets with an average of 2.38%.

### Weaknesses
 * The whole method assumes that for every label y, there exists only one G_c. Is it possible that there are more than one G_c correspond to a label y? Will all the assumptions and theorems hold in such cases? The paper does not explore the implications of multiple invariant subgraphs for a single label, which is a significant limitation given the complexity of real-world graph data. For example, in a molecular graph, multiple functional groups might contribute to the same property, and the method's ability to handle this is unclear.
* The proposed method can not handle OOD cases on graph tasks like node classification, link prediction, etc. This limit the scope of the method. The method's focus on graph-level tasks neglects the importance of node-level and link-level predictions, which are crucial in many applications. The paper lacks a discussion on how the proposed method could be adapted to these tasks, particularly when node features are crucial for prediction.
* Hyper-parameter \eta (L215) and K (L249) are critical to the size of G_s and are thus critical to the method. Theorem 4.1 and 4.2 rely on these two hyper-parameters. How to select the right value for these hyper-parameters without knowing the size of G_c is not discussed. The paper does not provide a clear strategy for selecting these hyperparameters, which are crucial for the method's performance. The lack of guidance on how to choose these parameters, especially when the size of the invariant subgraph is unknown, makes the method difficult to use in practice.
* Some proves are missing:
    * Why Theorem 3.1 is hold is not proved.
    * Why P(X^’_{ij}) = 1/|G_s| is enforced by L_{div} is not well explained.

### Questions
I would suggest to move definition 2 before Theorem 3.1.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a novel augmentation strategy for out-of-distribution (OOD) generalization by diversifying spurious subgraphs. The method, termed spurious subgraph diversification, employs randomized spurious subgraph generation to maximize diversity while preserving invariant substructures. This approach achieves state-of-the-art results on both synthetic and real-world datasets.

### Strengths
1. The authors provide a unified theoretical framework for Learnable Data Transformation under graph OOD scenarios, demonstrating a solid theoretical foundation.
2. The proposed iSSD framework is easy but effective. Extensive experimental results demonstrate the superiority of proposed method.
3. The paper is well-written, and easy to follow. I really enjoy reading this paper.

### Weaknesses
1. The proposed graph size constraint loss (Eq. 7) aims to prune edges from the spurious subgraphs. However, the mechanism by which this is guaranteed is not entirely clear. While the loss ensures edge removal based on a predefined budget, it is possible that minimizing Eq. 7 could be achieved by removing edges from the causal subgraph instead. This ambiguity undermines the claim that the method selectively targets spurious edges and requires further clarification. Specifically, how does the interaction between the graph size constraint loss and the overall objective function ensure that the optimization process preferentially removes edges from the spurious subgraph as opposed to the causal subgraph, given that both actions could potentially minimize the loss? 

2. The joint selection of parameters $K$ and $\eta$ appears to be a non-trivial task, particularly in the motif dataset. For real-world datasets or practical deployments, the optimal values of $K$ and $\eta$ might not be known a priori. The paper lacks a clear strategy for choosing these parameters when prior knowledge about the scale of "spurious subgraphs" is unavailable. This raises concerns about the general applicability and robustness of the proposed method in real-world scenarios where such information is often inaccessible. How sensitive is the model's performance to different values of $K$ and $\eta$, and what are the potential consequences of suboptimal parameter choices?

3. This study focuses on augmentation-based methods for graph OOD generalization. However, it would be beneficial to include additional baselines or a more comprehensive discussion about augmentation-based graph OOD generalization methods, such as those presented in [1-2]. This would provide a more complete context for evaluating the proposed method's performance and contribution to the field.

### Questions
Please address my concern in weakness part.

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a novel environment augmentation method for graph out-of-distribution (OOD) generalization. Input graphs are assumed to be composed of an invariant/causal subgraph $G_c$ that predicts the target and a spurious subgraph $G_s$ that encodes environment variability. Their approach involves learning a data transformation with high sampling probability for edges in $G_c$ and a low sampling probability for edges in $G_s$. This is done via a combination of cross-entropy loss and two new regularization terms: (1) Graph size constraint $L_e$ to control the number of pruned edges during transformation; (2) Spurious subgraph diversification $L_{div}$ to maximize randomness in the spurious subgraphs retained after transformation. This is supplemented by theoretical proofs showing that $L_e$ tightens OOD generalization bound while $L_{div}$ improves OOD generalization. To empirically verify these claims, they benchmark performance against 17 baseline methods across 4 dataset classes, perform ablation studies on the regularization terms, evaluate sensitivity to hyper-parameters, and other in-depth analysis.

### Strengths
1. The paper is well-written and all claims and design choices are well-motivated with appropriate references to literature. 
2. It presents a novel idea grounded in theory to tackle OOD graph generalization, a problem of interest for broader graph community
3. Along with performance comparison against baseline methods, they include sufficient empirical analysis to justify their design choices and insights to support theoretical claims.

### Weaknesses
1. Limited data diversity: Apart from the synthetic GOODMotif dataset, all others pertain to molecules. In these datasets, it may be possible to ascribe target graph label to specific functional groups and thus, ascertain the invariant subgraphs. While it is alright to limit the scope of experiments, I wonder how the proposed method performs against datasets from other application domains (CMNIST, GOOD-Arxiv). It may be useful to provide more insight or comment on the broader applicability of proposed approach.

### Questions
1. Do we have an intuition on why the performance drops for Motif-Base dataset on going from K=90 to 70 and rises again for K=50 for all $\eta$ in Figure 2?
2.  Do we have an insight into the cause of higher variance on removing either $L_e$ or $L_{div}$?
3. Why was ERM pre-training used? Was it used with other baseline methods as well? If not, why? Could we include performance w/o ERM training to isolate and analyze performance gains from proposed techniques?
4. Both the GOOD datasets use covariate shift split. Is the method applicable to concept shift?
5. How restrictive is the regularization from $L_e$? Do we know how the number of edges are distributed in graphs sampled from $t(G)$?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
Environment augmentation methods have shown promise in addressing out-of-distribution (OOD) generalization challenges in Graph Neural Networks (GNNs), but they face a trade-off between generating diverse graphs and preserving invariant substructures. Current methods are limited by deterministic graph composition strategies and the risk of excluding important subgraphs due to spurious correlations. To overcome these challenges, the authors propose a method called spurious subgraph diversification, which randomizes spurious subgraph generation while maintaining key invariant structures, achieving up to 24.19% better performance than 17 baseline methods on both synthetic and real-world datasets.

### Strengths
- The problem of graph OOD generalization is important.
- The framework provides detailed theoretical analysis, including bounds on generalization performance.
- The empirical results, involving comparisons with 17 baselines across multiple datasets, demonstrate the effectiveness of the method.
- The paper includes detailed ablation studies and sensitivity analyses to highlight the importance of each component of the iSSD framework.

### Weaknesses
 - A major concern is about the soundness of the method "to idenitfy edges from spurious subgraphs accurately, we utilize the bottom K% of edges with the lowest predicted probabilities as estimated spurious edges". First, this identification of spurious subgraphs may not hold in many scenarios, where some spurious edges have strong correlations with the labels for the model to exploit, and thus for these edges model has high predicted probabilities. Second, in this way, there no supervision signals for capturing spurious edges, how do the authors guarantee that the captured edges are indeed spurious? Third, a surge of works in graph ood generalization propose different methods to capture spurious/variant subgraphs, how do this method surpass these methods?

- Another major concern is about the novelty of the method. Diversifying the spurious subgraphs, or environments, to improve graph ood generalization performance has been explored in many related works, e.g., EERM in ICLR22, which is not compared as baseline.  Also, the learnable data transformation module is similar to DIR in ICLR22.

- (minor) typo. In line 72,  "idenitfy".

### Questions
see weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2
