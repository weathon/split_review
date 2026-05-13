# Beyond Layers: A Global Message-Passing Mechanism for Heterophilic Graphs

- Decision: Reject
- Scores: 3, 3, 3, 3

## Abstract
The effectiveness of most graph neural networks is largely attributed to the message-passing mechanism.
Despite the significant success in homophilic graphs (i.e., similar nodes are connected by edges), message-passing mechanism in heterophilic graphs (i.e., dissimilar nodes are connected by edges) is still challenging.
Due to the existence of low-order but dissimilar neighbor nodes in a path, messages from similar but high-order neighbor nodes are often weakened. 
In this paper, firstly, we conduct both theoretical and empirical analysis of the layer-by-layer local nature of the message-passing mechanism.
Then, we propose a novel GloMP-GNN for heterophilic graphs by comprehensively introducing global insights into the message-passing mechanism.1) During the message propagation phase, the global insight is introduced from the perspective of graph structure. 
We design a structure-based global propagation strategy, where messages can be effectively propagated with the bridge of virtual edges between a global virtual node and graph nodes.
Moreover, a global edge adaption approach is included to aggregate messages with adaptive edge weight adjustment.
2) During the feature updating phase, the global insight is introduced with a feature-augmented compensatory updating method.
Through a multi-view feature updating mechanism, the node feature representation can be effectively augmented by compensating the weakened message from different views.
Finally, we conduct extensive experimental evaluations on eight datasets, which demonstrate the superiority of our proposed GloMP-GNN. As broader impacts, GloMP-GNN consistently performs well across multiple layers and also effectively prevents the over-smoothing problem.
Codes are available on Github with https://github.com/Anonymous-GloMP-GNN/GloMP-GNN.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies the node classification problem on graphs beyond heterophiliy. Its core idea is to add an extra virtual node.

### Strengths
S1. This paper is very clear and easy to understand.

S2. The experimental section includes many baseline methods and datasets.

### Weaknesses
W1. The main weakness of this paper is its novelty, which is very low, to the extent that many statements and ideas are well-known in the graph machine learning community. I would name a few:

W1.1 Theorem 1 claims that with the increase of propagation steps, the multiplication of (normalized) edge weights will be 0, which is a well-known fact that originated from the very early study regarding PageRank. The theorem, as stated, lacks the necessary constraints to be meaningful. Specifically, it does not specify the conditions under which the normalized edge weights will lead to a product of zero. For instance, if the graph is fully connected, the normalized weights will not necessarily lead to a zero product with increasing propagation steps. The theorem needs to explicitly state the graph structure and edge weight conditions for the claim to hold.

W1.2 Theorem 2 is a very obvious fact that, to be frank, cannot even be named a "Theorem."

W1.3 Eqs 8 and 9, which are the core methods of the section "FEATURE-AUGMENTED COMPENSATORY UPDATE," are just the same as the PageRank with different normalization (e.g., row normalization or symmetric normalization). The equations, while using different normalization schemes, still perform a form of iterative message passing that is fundamentally similar to PageRank. The core idea of propagating information based on normalized edge weights is not novel, and the specific normalization choices (mean and degree-based) do not introduce a significant departure from existing methods.

W1.4 The core idea of this paper, adding a global virtual node into the given graph to improve connectivity, has been thoroughly studied. For example, as early as one of the standard methods in the OGB benchmark [1], and some recent studies like [2] and [3]. The paper fails to adequately differentiate its approach from these existing methods. The mere addition of a virtual node is not sufficient to claim novelty; the specific way it is integrated and utilized within the proposed framework needs to be significantly different from prior work to justify the contribution.

W2. Some strong and recent baselines [4-7] are missing. After adding them back, the proposed method is not the best-performed one. The experimental section needs to be more comprehensive by including recent state-of-the-art methods. The current results are not convincing enough to demonstrate the superiority of the proposed method.

W3. This is a minor concern compared to the previous two. No theoretical analysis shows why the proposed method can work so effectively. The paper lacks a theoretical justification for why the proposed method is effective, especially in heterophilic settings. A more rigorous analysis is needed to explain the method's performance.

### Questions
Please check the weaknesses I mentioned.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper analyzes the limitations of the message-passing mechanism in heterophilic graphs and introduces a novel approach called GloMP-GNN. GloMP-GNN incorporates global insights into both the message propagation and feature updating phases, using virtual edges and a multi-view feature updating mechanism to enhance node feature representation. Extensive experiments on eight datasets show that GloMP-GNN outperforms existing methods and mitigates the over-smoothing problem.

### Strengths
1. Improving virtual nodes using a Gram matrix is an interesting idea, and the proposed model appears to perform well on benchmarks.

### Weaknesses
1. **Method**

   - The approach proposed in the paper relies on the Gram matrix, which requires maintaining a matrix quadratic in relation to the number of nodes, making the model unscalable. While the authors claim the Gram matrix is computed only once, the memory footprint during this preprocessing step is still a major concern for large graphs. The quadratic memory requirement will severely limit the applicability of this method to graphs with even moderate numbers of nodes, making it impractical for real-world scenarios.

   - The multi-view proposed in the paper seems quite ad-hoc. Why were these three views chosen? It seems to be just a simple combination of GAT variant (the first view), APPNP (the second view), and GCN (the third view). Can this be understood as an ensemble model? This work incorporates too many previous methods as components, lacking sufficient motivation. The combination of these specific models, without a clear theoretical justification for their interaction, raises questions about the novelty and the principled design of the approach. The lack of ablation studies to assess the contribution of each view further weakens the argument for this particular combination.

2. **Experiments**: The datasets used in the paper are not large in scale (with at most 20,000+ nodes), and do not demonstrate the scalability of the proposed method. The absence of experiments on larger, more challenging datasets makes it difficult to assess the practical applicability of the method, especially given the memory concerns associated with the Gram matrix.

### Questions
1. In line 258 and line 283, the author mentioned "multi-head attention" twice, but why does the formula 3 author provided not include the multi-head mechanism?

### Soundness
2

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
4

### Summary
The authors propose a new graph neural network (GloMP-GNN), which can work well in both homophilic and heterophilic graphs.

The authors first analyze the limitations of layer-by-layer GNNs, indicating that the information is getting weaker as the propagation path is getting longer.

Based on this limitation, GloMP-GNN uses a global-level virtual node to mitigate this "vanishing information" phenomenon.

The authors experimentally verified the superiority of the proposed method compared to the several existing GNNs.

### Strengths
- S1. The paper is generally well-written and can be easily understood.
- S2. The provided figure provides an overview of the proposed method well.

### Weaknesses
 - ***W1. Concerns on theories.*** My first concern is about the soundness of the theory. Theorem 1 indicates that the infinity-length path leads to zero information. In practice, since we do not stack a very large number of GNN layers, this result hardly highlights the limitation of the existing GNN methods. Rather, I think discussing diminishing ratio (i.e., information is shrinking with the exponential to the number of layers or quadratic to the number of layers, etc...) could be more adequate to pinpoint the limitation. Specifically, the theorem does not address the practical scenario where GNNs operate with a limited number of layers, and thus the theoretical motivation for a global node is not strongly supported. The analysis should focus on how information degrades with a realistic number of layers, not just at infinity. Thus, I think the proposed theorem cannot well motivate the proposed method.

- ***W2. Concerns of novelty.*** My second concern is about the novelty of the proposed method. In my opinion, the proposed method is a reasonable combination of the existing method. (1) Global node is an idea widely used in graph transformers, (2) graph attention is also widely used in various GAT-based methods, and (3) embedding concatenation is proposed in H2GCN. While each component is individually effective, the combination seems incremental. The paper does not sufficiently demonstrate how the specific combination of these techniques leads to a novel approach that is more than the sum of its parts. A more detailed explanation of how these components interact to address the vanishing information problem would be beneficial. Overall, while each component is adequate, I feel the proposed method somewhat lacks novelty.

- ***W3. Complexity.*** The authors highlight the limitation of the existing graph transformers (quadratic complexity w.r.t. number of nodes, lines 77-79), I think the proposed method shares this limitation, since the proposed method is also computing the gram matrix, which is $XX^{T}$. The computation of the Gram matrix, even if done as a preprocessing step, still requires a quadratic computation with respect to the number of nodes. This preprocessing step could become a bottleneck for large graphs, which contradicts the claim of efficiency. Did I correctly understand this limitation?

### Questions
Please see the weakness section. Thank you.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper points out the existence of low-order but dissimilar neighbor nodes, where the messages can be smoothed during the propagation. To better utilize their information, the authors propose two strategies: 1) structure-based global message-passing, and 2) feature-augmented compensation. The extensive experiments and ablation study show the effectiveness of the proposed scheme.

### Strengths
**S1.** The idea of receiving messages from distant nodes is reasonable. In addition, some figures (e.g., Fig 1) improve the readability of the manuscript

**S2.** The definitions and theorems are clearly defined

**S3.** Extensive experiments and ablation study show the effectiveness of the proposed method

### Weaknesses
**W1.** The novelty of the proposed method is quite vague. For example,
* Definition 1 (Global Intensity), definition 2 (Path Intensity), and definition 3 (k-order neighbors) are obvious as they are normalized based on the number of adjacent neighbors during propagation.
* The concept of Theorem 1 (over-smoothing) is already discussed and several studies propose to solve this problem [1, 2]. In addition, [3] proved that even GAT converges on an exponential rate. Lastly, the method of non-local message-passing free from node order is introduced in [4].
  * [1] Two sides of the same coin: Heterophily and oversmoothing in graph convolutional neural networks, ICDM '22
  * [2] Not too little, not too much: a theoretical analysis of graph (over) smoothing, NeurIPS '22
  * [3] Demystifying oversmoothing in attention-based graph neural networks, NeurIPS '24
  * [4] Non-local graph neural networks, TPAMI '22  

Q1) Could you please explicitly state how the proposed definitions and theorem differ (if at all) from existing work?


**W2.** As mentioned by the authors, the proposed GEA (Global Edge Adaptation) extends the concept of GVN (Global Virtual Node) by applying the attention layer, which is the same as the GAT.  

Q2) How does GEA specifically differs from or improves upon GAT? Could you please elaborate on the specific similarities and differences between these methods?


**W3.** The author suggests the integration of Gram matrix (which is the same as MLP) by measuring the similarity of initial node features and insist that this can increase the generalization ability. However, this contradicts to the bias-variance tradeoff. Generally, the prediction variance gets higher if it is trained without neighboring nodes (MLP). Even under the high heterophily, it has been shown [5] that utilizing the neighboring nodes can boost the performance by discovering the patterns of the adjacent nodes. From my view, the authors need to prove that the Gram matrix $M_G$ improves the generalization ability theoretically.
  * [5] Revisiting heterophily for graph neural networks, NeurIPS '22  

Q3) How does this approach balance the bias-variance tradeoff and improves generalization, particularly in comparison to methods that utilize neighboring nodes? Could you provide a theoretical guarantee that Gram matrix improves the generalization ability of GNN?

**W4.** In equation 6, $\beta$ is given as trainable parameter, which can balance the influence of the retrieved edge coefficients. From my thinking, it can be biased towards 0 or 1 without specific constraint. The author needs to show the change of this value in the experiment section.  

Q4) Could you please analyze how does this value evolves during training across different datasets or model configurations?


**W5.** The suggested feature-augmented compensatory update (Sec 3.2) looks like a simple combination of the previous methods as, 
  * Eq. 7: Gram matrix (heterophily)
  * Eq. 8: GraphSAGE (homophily)
  * Eq. 9: GCN (homophily)

Q5) How does the combination of these methods improve the overall performance? It seems like Gram matrix (Eq. 7) contradicts to the others (Eq. 8 and 9). Can you please provide some explanation that this can improve the quality of the prediction?

### Questions
Please see the weaknesses

### Soundness
2

### Presentation
3

### Contribution
2
