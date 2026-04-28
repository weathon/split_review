# Exploring High-Order Message-Passing in Graph Transformers

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 5, 3

## Abstract
The Transformer architecture has demonstrated promising performance on graph learning tasks. However, the existing attention mechanism used in Graph Transformers (GT) cannot capture high-order correlations that exist in complex graphs, thereby limiting their expressiveness. In this paper, we present a High-Order message-passing strategy within the Transformer architecture (HOtrans) to learn long-range, high-order relationships for graph representation. Recognizing that some nodes share similar properties, we extract communities from the entire graph and introduce a virtual node to connect all nodes in the community. Operating on the community, we adopt a three-step message-passing approach: capture the high-order information of the community into a virtual node; propagate long-range dependent information between communities; aggregate community-level representations back to graph nodes.  This facilitates effective global information passing. Virtual nodes capture the high-order community information and support the long-range information passing as the bridge. 
We demonstrate that many existing GTs can be regarded as special cases of this framework. Our experimental results illustrate that our proposed HOtrans consistently achieves highly competitive results across several node classification tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work proposes a virtual node based graph transformer to capture the high-order structure information of the graph. The designed approach is by (1) node clustering by ClusterGCN or random walk-based GraphSaint, (2) attentions at three levels including node-to-virtual-node, virtual-node-to-virtual-node, and virtual-node-to-node. This work is evaluated by node classification tasks on both homophily and heterophily graphs, which show better or competitive performance over the state-of-the-art baselines.

### Strengths
1. This work introduces an interesting approach to leveraging virtual nodes to improve the capability of graph transformers to capture graph high-order information, for node-level tasks. Prior works leverage virtual nodes to solve graph-level tasks (e.g., graph classification).

2. The designed approach is to some extent generic and can be specified into different types of GNNs according to how communities/clusters are defined.

3. The proposed method indeed performs better than the state-of-the-art on most datasets, except ogbn-arxiv dataset. Ablation studies are done to show the effectiveness of different components.

### Weaknesses
1. It is not clear how theorem 4.1 can demonstrate the power of the designed method from the theoretical perspective. In other words, given that the proof of Theorem 4.1 is based on top of Proposition 4.1 while there's no approximation error provided, it is vague to define `arbitrarily well' mentioned in Theorem 4.1. The connection between the proposition and the theorem is not strong enough to justify the claim of arbitrary approximation. The absence of a concrete error bound makes it difficult to assess the practical implications of the theoretical result.

2. The explanations of why positional encoding hurts the performance are a bit insufficient. I agree with the authors that Laplacian PE can hurt the performance on heterophily datasets since heterophily graph usually requires non-low-pass filters for aggregations. However, it's not clear why random walk based encoding also performs worse. Besides, both encoding methods hurt the performance on both homophily and heterophily datasets. The explanation that random walk PE encodes local connections is not sufficient to explain why it consistently degrades performance across different graph types. A more detailed analysis of the interaction between the proposed method and different positional encodings is needed.

3. Eq. 3 seems to be incorrect. \bar{x}_i is defined as a zero vector, as described in the paper, so \bar{q}_i is essentially just a zero vector and thus carries no information at all. This raises concerns about the initialization of the virtual node representations and how they effectively contribute to the overall message passing process. The lack of initial information in \bar{q}_i could potentially hinder the model's ability to learn meaningful representations.

### Questions
1. How do you define 'arbitrarily well' in Theorem 4.1 mathematically? 
2. Can you elaborate more about the reasons why positional encodings perform generally worse than not using positional encodings on both homophily and heterophily datasets?
3. Why is \bar{x}_i defined as a zero vector?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this work, the authors propose a new architecture for graph learning, HOtrans, specializing in transductive node classification tasks. The approach involves three steps: (a) community detection, (b) self-attention between community representations, and (c) update of the node representations from community representations. The authors compare their model on various node classification datasets, including both homophilic and heterophilic graphs.

### Strengths
**Strengths:**
- The paper addresses an important problem.
- The proposed model compares well against most of the presented baselines
- The empirical study is thorough, and the paper presents ablation studies to gain further understanding of the essential components of the proposed architecture.

### Weaknesses
 **Weaknesses** (in the order of importance):
- The most important issue with this work is that the empirical results of the proposed model are not very convincing. Overall, the presented improvements of HOtrans are well within the standard deviation of prior works such as Graphormer [1]. The only exception to this are Texas and Wisconsin, where HOtrans is significantly better than previous models. On Actor, the authors also improve significantly over Gapformer but are not significantly better than a standard transformer with Laplacian encodings [2]. Considering that HOtrans is overall very close in performance to Gapformer and the fact that Gapformer also explores applying self-attention to pooled representations of sets of nodes, it is not convincing that HOtrans adds much value over Gapformer. Specifically, the reported performance gains on most datasets are marginal, often within the range of random fluctuations, and do not demonstrate a clear and consistent advantage. The fact that HOtrans only shows a significant improvement on two out of ten datasets raises concerns about the generalizability of the proposed method. The similarity in performance to Gapformer, a model that also uses pooled node representations, further weakens the argument for the novelty and unique contribution of HOtrans.

- The motivation of HOtrans is quite weak. The authors mention that HOtrans was developed to capture long-range dependencies and to aggregate the information of sets of nodes instead of single nodes. However, such approaches have already been explored, e.g., with the Graph-ViT [3]. Further, the ability of graph transformers to capture long-range dependencies has already been demonstrated in e.g., GraphGPS [4] and even in the context of transductive node classification [2]. It would be helpful if the authors could empirically compare their approach to these prior works. The paper lacks a clear explanation of how HOtrans differs fundamentally from these existing methods in its approach to capturing long-range dependencies and aggregating node information. The authors need to articulate the specific mechanisms that make HOtrans unique and advantageous compared to these established techniques.

- The datasets used for heterophilic node classification, in particular Cornell, Texas, and Wisconsin, have recently been shown to have substantial weaknesses, such as their very small size and imbalanced classes [5]. The claim that HOtrans performs favorably to graph transformers on heterophilic datasets could be further substantiated by additional results on more suitable datasets such as the ones in [5]. On Actor, which is the only heterophilic dataset that does not suffer from the aforementioned issues, HOtrans performs no better than a standard transformer with Laplacian encodings [2] (as already mentioned above).

In summary, while the proposed model, HOtrans, outperforms most presented baselines, it only outperforms the best prior method on each dataset on 2/10 datasets. Most crucially, the empirical results are very close to those of Gapformer on nearly all datasets and it is not made clear how the proposed method is otherwise favorable to Gapformer.

### Questions
What added value does HOTrans provide compared to Gapformer considering that both models perform nearly the same across all datasets?

How does HOtrans perform to prior graph transformers that aggregate sets of nodes (e.g., Graph-ViT) or have demonstrated to capture long-range dependencies (e.g., GraphGPS)?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a Transformer architecture called HOtrans, which employs a higher-order message passing strategy. The model initially extracts communities, each centered around a virtual node, from the entire graph. Subsequently, the proposed attention mechanism comprises three steps: first, information is aggregated towards higher-order virtual nodes; second, information is exchanged among representations of these higher-order virtual nodes; and finally, the updated information is relayed back to the original graph nodes. In the experimental study, the authors demonstrate the effectiveness of HOtrans in node classification tasks.

### Strengths
1. The proposed method not only delivers competitive performance on homophilic datasets but also surpasses the state-of-the-art methods on heterophilic datasets.

2. The proposed HOtrans is scalable to large graphs.

### Weaknesses
1. The novelty of the paper appears somewhat limited. Both community sampling techniques and the virtual node design have been previously introduced in other studies. This work seems to primarily amalgamate these existing strategies. The specific combination of these techniques, while potentially effective, does not present a fundamentally new approach to graph representation learning. The paper lacks a detailed analysis of how the proposed combination offers advantages beyond the sum of its parts. It would be beneficial to see a more in-depth discussion of the unique properties arising from this specific integration.

2. The proposed method may not be competitive to some linear graph transformers. For example, NodeFormer [1], with less computational resource and fewer training samples, gets better results on full attention graphs, e.g., on Cora with 88.80% accuracy versus 88.11% obtained by the proposed method. The performance difference, while seemingly small, raises questions about the practical advantages of the proposed method, especially considering the added complexity of the higher-order message passing. A more thorough comparison, including computational cost and parameter efficiency, is needed to justify the use of HOtrans over simpler alternatives.

3. It is claimed that the proposed method can capture long-range dependency in graphs. Results on some long-range graph datasets are expected, e.g., PascalVOC-SP from LRGB [2]. The absence of experiments on such datasets makes it difficult to validate this claim. The paper should include experiments on datasets specifically designed to test long-range dependency modeling to provide empirical evidence for this assertion.

4. It would be interesting to try learning-based community sampling methods to assess its effect to the proposed model.

### Questions
Please refer to the weaknesses.

### Soundness
3 good

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
This paper proposes a new graph representation learning method called HOtrans, which builds upon the Transformer architecture. HOtrans introduces a three-step message-passing approach to capture high-order correlations and long-range dependent information in graphs. Specifically, it first constructs communities, and then involves message passing between node to virtual node, virtual node to virtual node, and virtual node to a node. Experiments results showed the effectiveness on Homophilic and Heterophilic graphs.

### Strengths
1.  The proposed HOtrans can utilize high order information, and serves as a general framework for many existing graph transformers.

2. HOtrans achieves a competitive performance.

3. This paper is clearly presented and easy to follow.

### Weaknesses
1. The key components of HOtrans are basically built upon existing concepts, e.g., virtual node, community sampling etc, which makes this paper less disruptive.

2 . High order information is important and existing solutions usually adopt hypergraph method. The proposed HOtrans resembles hypergraph convolutional networks, and there exist many hypergraph solutions, but the authors didn’t discuss the differences, without making compasions in the experiments. 

3. I think the community sampling method will have a big impact on the model performance and should be datasets dependent. However, this paper is mainly based on existing random walk and sepctal clustering.

minor: 

1. I cannot find the corresponding text for table 3. What is this table for?

2. Typos: A.1, gapformer should be HOtrans?  Also, I suggest the authors to have a table summarizing the complexity compasions with existing models.

### Questions
1. How the proposed method compared with hypergraph approaches?

2. Can the proposed HOtrans be applied to graph level tasks and how about the performance?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
