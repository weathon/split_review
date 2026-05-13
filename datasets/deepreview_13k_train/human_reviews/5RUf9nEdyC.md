# TEDDY: Trimming Edges with Degree-based Discrimination Strategy

- Decision: Accept
- Scores: 5, 6, 6, 8, 5

## Abstract
Since the pioneering work on the lottery ticket hypothesis for graph neural networks (GNNs) was proposed in \citet{chen2021unified}, the study on finding graph lottery tickets (GLT) has become one of the pivotal focus in the GNN community, inspiring researchers to discover sparser GLT while achieving comparable performance to original dense networks. In parallel, the graph structure has gained substantial attention as a crucial factor in GNN training dynamics, also elucidated by several recent studies. Despite this, contemporary studies on GLT, in general, have not fully exploited inherent pathways in the graph structure and identified tickets in an iterative manner, which is time-consuming and inefficient. To address these limitations, we introduce \textsc{Teddy}, a one-shot edge sparsification framework that leverages structural information by incorporating \textit{edge-degree} statistics. Following the edge sparsification, we encourage the parameter sparsity during training via simple projected gradient descent on the $\ell_0$ ball. Given the target sparsity levels for both the graph structure and the model parameters, our \textsc{Teddy} facilitates efficient and rapid realization of GLT within a \textit{single} training. Remarkably, our experimental results demonstrate that \textsc{Teddy} significantly surpasses conventional iterative approaches in generalization, even when conducting one-shot sparsification that solely utilizes graph structures, without taking feature information into account.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces several techniques to sparsify graph data and networks in order to build a sparse graph learning model. The important aspects are as follows:
1) Degree-based graph sparsification to remove low-degree edges and make graphs sparse;
2) Distillation by matching the classification logits of the model pre-trained on the whole graphs;
3) Parameter sparsification by using a subset of parameters (i.e., Projected Gradient Descent).

When applied to classical GNNs such as GCN/GAT/GIN, the experimental results validate the proposed method by showing some performance improvements.

### Strengths
The proposed methods are generally straightforward and concise. They empirically improve performance compared to the baselines. The whole process is clearly stated in Algorithm 1.

### Weaknesses
1. Baseline GNN models are somewhat outdated. Traditional GNNs such as GCN/GAT/GIN are known to suffer from limited expressivity, resulting in restricted empirical performances in many cases. Several studies have done expressiveness analysis, to name a few references [3,4]. Later works, such as graph transformers and expressive GNNs [1,2,3], have proven to be more powerful and meaningful for empirical studies. The paper does not adequately address how the proposed techniques would perform on more expressive models, which is a significant limitation given the current state of the field.

2. Detailed ablation experiments are lacking, which are necessary to clearly validate the effectiveness of each component. The paper presents some ablation results, but a more thorough analysis is needed to understand the isolated impact of each proposed technique. Specifically, the interplay between graph sparsification, model distillation, and parameter sparsification is not fully explored. For example, it is unclear how much performance gain is attributable to edge sparsification alone, without the influence of distillation or weight pruning.

3. The theoretical analysis concerning the motivation behind preserving low-degree edges seems somewhat disconnected from the main idea. The paper's theoretical justification for preserving low-degree edges, based on the analysis of the symmetrically normalized adjacency matrix, is not clearly linked to the empirical observations. The assumptions made in the theoretical analysis, such as the existence of a Lipschitz constant, are not well-justified in the context of the GNN models used. Furthermore, the paper does not explore the implications of removing high-degree edges, which could also be a valid approach based on the same theoretical analysis.

4. Some claims regarding training efficiency and generalization performance appear to be misleading. The paper claims that the proposed method achieves a single training, but this is misleading since the method requires pre-training a model on the full graph for distillation. The claims regarding generalization performance are not sufficiently supported by the experimental results, and the paper does not provide a clear definition of what constitutes 'generalization' in this context. The computational efficiency claims are also not validated with detailed timing experiments, making it difficult to assess the practical benefits of the proposed approach.

### Questions
1. Conventional GNNs are empirically seen to suffer from limited expressivity. How do the latest transformer-based GNNs or more expressive models like GPS[1], Specformer[2], and PPGN[3] compare when applying the proposed techniques? These newer models have already surpassed the empirical performance of older baselines like GCN/GAT/GIN. Validating the proposed techniques on these latest methods rather than older models would make the arguments more convincing.

2. About Figure 1: What is the precise step for removing high-degree or low-degree edges? Given a graph sparsity value, how exactly is the subgraph generated? Is random sampling involved in this process? If so, could you provide the results of multiple runs (e.g., mean and standard deviation) to separate the training-related noise?

3. Ablation Studies: Could you provide detailed ablation studies on the effectiveness of the proposed three components? a) graph sparsification by removing edges; b) model distillation; c) parameter sparsification with projected gradient descent. It seems that these components could be applied separately to any of the baseline training methods (UGS/WD-GLT) in empirical studies.
In Figure 13, there are some comparisons made. Graph sparsification doesn’t seem to improve empirical performance at all. There are no curves representing UGS/WD-GLT without distillation loss. Although considering multi-hop subgraphs appears to be effective in a way, this concept is not new in graph learning literature (e.g., k-WL GNNs [4]).

4. The theoretical analysis involving the upper bound of the symmetrically normalized adjacency matrix is somewhat unclear.
a) Concerning the mentioned analysis, how realistic is the assumption of the Lipschitz constant being present?
b) If the aforementioned assumptions hold true for the specified models, how plausible is it that removing low-degree edges actually increases the term $\\frac{\\text{deg}\_\text{max} + 1}{\\text{deg}\_\text{min} + 1}$? This aspect may be specific to datasets and could possibly be numerically simulated.
c) Conversely, removing high-degree edges appears to reduce the generalization gap by lowering $\\text{deg}\_\text{max}$, according to the preceding analysis. What is the reason this aspect is not emphasized or motivated more within the discussion?

4. In Eq. (5), the edge score is always symmetric. How does this approach apply to directed graphs?

5. How crucial is the distillation training? It appears to undermine the purpose of utilizing sparse graphs, as there is a necessity to initially train the model on the full graphs. This approach also seems to contradict the claim of "a single training," a statement that is reiterated numerous times throughout the paper.

6. The paper asserts that "TEDDY significantly surpasses conventional iterative approaches in generalization." Could you provide more details to substantiate this claim? Which sections or aspects of the experiments corroborate this assertion regarding generalization?

7. The paper claims that the employed PGD training saves computation time compared to the iterative approach. Could you provide additional results to validate this claim, such as comparing training hours using the same GPU hardware?

[1] Recipe for a general, powerful, scalable graph transformer. NeurIPS 2022.\
[2] Specformer: Spectral Graph Neural Networks Meet Transformers. ICLR 2023.\
[3] Provably Powerful Graph Networks. NeurIPS 2019.\
[4] Weisfeiler and Leman Go Neural: Higher-order Graph Neural Networks. AAAI 2019.

### Soundness
2 fair

### Presentation
2 fair

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
This paper proposes a one shot graph pruning algorithm to find Graph Lotttery Tickets (GLTs) by (i) deleting graph edges from nodes with higher degrees and (ii) sparsifying node parameters using $l_0$ regularization with Projected Gradient Descent.
The sparse networks obtained by the authors are shown to improve performance over existing Graph Lottery Ticket methods.

### Strengths
1. The proposed method finds GLTs using a one shot training approach outperforming existing iterative graph pruning algorithms.

### Weaknesses
1. While the proposed idea of sparsifying the graph edges based on the degree information is simple and makes intuitive sense (as also shown empirically), why do the authors consider only the degree information as opposed to other metrics like spectral information of the graph or centrality which might convey more information about the graph. Is the degree information sufficient in this regard to obtain a sufficiently sparse graph in comparison with these other metrics? Recent work has shown randomly dropping graph edges can also help training, in comparison to the proposed idea in Yu et al.  [1], how does randomly pruning graph edges compare?

2. The parameters sparsification method used is PGD with $l_0$ regularization. But there is no justification provided for using this particular method. There are other continuous sparsification schemes that have shown to achieve highly sparse networks in a single training run for feedforward networks like Kusupati et al. [2] and Louizos et al. [3]. The authors should provide a comparison with these methods to justify their choice of PGD with $l_0$ regularization.

3. The authors use GATs and GCNs in their experiments. However, the structure of GATs allows them to inherit some degree information in the form of attention while GCNs do not. Does this difference change the performance of the proposed graph pruning criterion for either architectures? Specifically, the attention mechanism in GATs could potentially mitigate the effect of degree-based pruning, as the attention weights might implicitly capture similar information. It would be beneficial to see a more detailed analysis of how the pruning strategy interacts with the attention mechanism in GATs.

4. The results in Table 1 might be better visualized via a heatmap showing how much Graph sparsity and Weight sparsity can be achieved and if there is a tradeoff between the two. This would provide a clearer picture of the method's performance under different sparsity configurations.

### Questions
1. The proposed method uses a pretraining strategy on the full graph before the pruning step. Are the parameters reinitialized at the end of the pruning stage like lottery tickets or does training continue after graph sparsification?

2. The authors mention the use of multilevel degree information for the graph pruning criterion in Eq. 4. However, it is not clear if the number of hops considered is determined by the number or layers in the network or is a hyperparameter that is tuned?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes TEDDY, a novel edge sparsification framework that considers the structural information of the graph. TEDDY sparsifies graph edges based on scores designed by utilizing edge degrees, and sparsifies parameters via projected gradient descent on $l_0$ ball. In particular, sparsification of both edges and parameters can be done in one-shot and the edge sparsification part does not to consider node features. Then the paper demonstrates the effectiveness of TEDDY over iterative GLT methods with comprehensive experiments.

### Strengths
1.	The paper is overall easy to follow.
2.	The experiments are diverse and thorough.
3.	It is an interesting observation that low-degree edges are important, which is supported both empirically and theoretically. The proposed method is thus principally designed.
4.	The proposed method is one-shot and efficient (but seems still need to train a dense network first; see weaknesses).
5.	The proposed method does more than just preserving the performance of vanilla dense GNNs---it actually improves the original performance in many settings. This is an impressive and interesting result.

### Weaknesses
 1. The main part of the proposed method and some discussion of the edge degrees are not clear and confusing.
- It is not very clear to me how T in eq.(5) is actually used (just dropping the edges with the lowest scores)? Also it seems that T computes all scores for all node pairs. How to deal the case when there is no edge between two nodes?
- Typo in eq.(5)? Should it not include specific node v instead?
- The analysis of the effect of edge degree in Section 4 only applies for first-order degrees, yet the paper discusses why higher-order edge degrees need to be considered heuristically via a toy example and claims TEDDY is based on “multi-level consideration of degree information“ in section 5.1. Then in the experiments, it never touches upon higher-order edge degree information and only discusses about first-order edge degrees in Figure 8.
2. The loss objective involves distillation (6), meaning that one still needs to train a dense network on the entire graph first, weakening the efficiency of the proposed method.

### Questions
1. Have you evaluated the zero-shot performance of the proposed edge sparsification method (with dense weights)? Intuitively it seems that it might able to work in the zero-shot setting, and in this way, one can single out the effect of sparse subgraph on the boost of performance.
2.	What happens if the distillation term in (6) is removed (so one does not to try a dense network at first)? How significantly the performance would be affected? Could you provide an ablation study on this?
3.	Would TEDDY work if one trains on small graphs and then applies to large graphs?
4.	Any intuition why TEDDY is still able to improve the performance of vanilla GNNs under extreme sparsity?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper observes the importance of low-degree edges in the graph and proposes a one-shot edge sparsification framework that leverages edge-degree to find graph lottery tickets (GLT). They achieve superior performances on diverse benchmark datasets.

### Strengths
The graph lottery tickets problem is an important direction, and the solution proposed in this paper is simple and elegant by utilizing the low-degree edges. The experimental results are also convincing.

### Weaknesses
Could the authors compare the consumed time of the proposed method with other baselines to further emphasize the efficiency?

### Questions
Could the authors compare the consumed time of the proposed method with other baselines to further emphasize the efficiency?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces an intuitively derived graph sparsification technique based on edge degrees, and integrates network distillation techniques for weight sparsification. The pruning process is independent of IMP and operates in a one-shot manner.

### Strengths
S1. This work demonstrates that high degree edges are less important via empirical observations, which is  significant in LTH community.

S2. Although many prior efforts have explored one-shot GLT; nevertheless, this paper seems to well strike the balance between efficiency and performance.

### Weaknesses
W1. The authors have avoided discussions concerning complexity, yet it appears that $T_{edge}$ might necessitate an $O(N^2)$ space complexity. Any comments on this?

W2. This work appears to be a fusion of two research lines:
- From the perspective of graph sparsification, there have already been efforts to prune edges based on edge properties and graph connectivity. The assertions made in [3] closely align with this study, suggesting that the removal of "non-bridge" edges (corresponding to the "low-degree edges") has minimal impact on graph information flow. Furthermore, it provides theoretical support and error bound analysis.
- From the perspective of weight sparsification, [1, 2] have extensively explored the feasibility of using PGD for parameter pruning. I cannot see the substantial differences or new contributions in this paper.

W3. While the innovations are intuitively appealing, they still lack theoretical substantiation. The assertion that high-degree edges should be pruned is not a trivial conclusion. I find the similar claim in [3], which examines graph connectivity, to be more appealing.

### Questions
The baseline performance depicted in Fig 6 and 11 appears highly questionable, displaying a significant drop compared to the results reported in [4, 5], as well as my previous replications. Perhaps the authors should consider presenting a more rigorously established and fair baseline performance.

The references can be found in the weakness part.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
