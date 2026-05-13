# Residual Connections and Normalization Can Provably Prevent Oversmoothing in GNNs

- Decision: Accept
- Scores: 8, 6, 8, 6

## Abstract
Residual connections and normalization layers have become standard design choices for graph neural networks (GNNs), and were proposed as solutions to the mitigate the oversmoothing problem in GNNs. 
However, how exactly these methods help alleviate the oversmoothing problem from a theoretical perspective is not well understood. 
In this work, we provide a formal and precise characterization of (linearized) GNNs with residual connections and normalization layers. 
We establish that (a) for residual connections, the incorporation of the initial features at each layer can prevent the signal from becoming too smooth, and determines the subspace of possible node representations;
(b)~batch normalization prevents a complete collapse of the output embedding space to a one-dimensional subspace through the individual rescaling of each column of the feature matrix. This results in the convergence of node representations to the top-$k$ eigenspace of the message-passing operator;
(c)~moreover, we show that the centering step of a normalization layer --- which can be understood as a projection --- alters the graph signal in message-passing in such a way that relevant information can become harder to extract. 
We therefore introduce a novel, principled normalization layer called \Graphnorm~in which the centering step is learned such that it does not distort the original graph signal in an undesirable way. 
Experimental results confirm the effectiveness of our method.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper provides a theoretical foundation for understanding how residual connections and normalization layers affect oversmoothing in GNNs. It offers a detailed analysis of the mechanisms behind these techniques and proposes a new normalization layer that enhances the expressive power and performance of GNNs. The contributions are supported by both theoretical proofs and empirical evaluations.

### Strengths
1. It provides a thorough theoretical analysis of oversmoothing for residual connections and normalization layers. 
2. The paper introduces a novel normalization layer that addresses a specific limitation of existing methods. The method is simple but effective. Random weights

### Weaknesses
1. The analysis is conducted only on linearized GNNs (except Remark 4.6) with random weights.   
    a. Most GNNs are nonlinear, so we are more concerned with the properties of GNNs under nonlinearity. Can the analysis be generalized to nonlinear cases? It is unclear how the insights from the linearized model translate to the behavior of GNNs with common nonlinear activation functions like ReLU or tanh, which introduce significant complexities not captured in the linear analysis. The theoretical results may not hold in practice for non-linear GNNs.
    b. Random weights usually appear during initialization. A network may have bad properties when it is initialized and good properties when it is trained, so we are more concerned about the trained GNNs which weights are not random. The analysis should consider the properties of trained weights, as the behavior of the network can change drastically after training. The theoretical analysis should be extended to trained networks, as the random initialization is not the final state of the model.

2. The results for residual connections are not surprise. In equation (4), the update rule uses initial residual connections $\alpha X^{(0)}W_2^{(t)}$. In most cases ($W_2 ^ {(t)} $is not particularly bad), $X ^ {(t)} $contains $X ^ {(0)} $, will therefore not be collapsed. So the results are pretty obvious. The contribution of residual connections in preventing oversmoothing seems trivial, as the initial features are directly added to the subsequent layers. This is not a novel finding.

    For Proposition 4.2, if $x_i=0$, The conclusion is not valid. Please state the proposition strictly. For Proposition 4.3, I think it is smillar to Theorem 2 in GCNII [1], which is just a different statement. It is better to cite the relevant conclusions.


### Questions
1. From Figure 1, we can see that residual connection performs better than other normalizations (even graphnorm2).  So why use normalization layers? It seems that the residual connection is enough to prevent oversmoothing. GCNII can perform well under very deep architectures [1], but the performances of different normalization layers decrease.Results in Table 1 valide this.
   
2. Some results in Table 1 are strange. The performance of GIN with BatchNorm,PairNorm, GraphNorm, PowerEmbed and GroupNorm are not better than no norm on ogbn-arxiv, and worse than no norm very much for #layer=20 (6% v.s. 25.7). Is there any mistake? If the results are correct, this is confusing. Section 4.2 states that batch normalization is able to prevent collapse, but its performance is worse than no norm.

[1] Ming Chen, Zhewei Wei, Zengfeng Huang, Bolin Ding, and Yaliang Li. Simple and deep graph
convolutional networks. In ICML, 2020.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Residual connections and normalization layers are commonly used layers in deep learning. 
The paper provides a theoretical analysis of the roles of residual connections and batch normalization in graph neural networks (GNNs) to mitigate the over-smoothing phenomenon. 
Furthermore, it introduces a new normalization layer, GraphNormv2, which demonstrates enhanced performance in both graph classification and node classification tasks.

### Strengths
1). The writing and organization of this paper are very clear.

2). Provided theoretical support for the use of residual connections and normalization layers in GNNs.

### Weaknesses
1). The standard deviations for MUTAG, PROTEINS, PTC-MR, and Cora in Table 1 are quite large, making the experimental results less convincing, and why are the standard deviations for GIN so large? Why graphv2 does show significant improvement for GIN on the ogbn-arxiv dataset, but not for GCN and GAT?

2). Could you add a curve that shows the performance changes of different baselines and GraphNormv2 as the number of layers in GNNs increases?

3). There is an error in line 118.

### Questions
Refer to the content in the Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Residual connections and normalization layers are commonly used in GNN models in order to hinder the oversmoothing phenomenon. Although successfully supported by empirical results, no theoretical investigations were undergone to explain this improvement. The authors of this paper bridge this gap and provide a better understanding as to why these heuristics are effective against oversmoothing.

Furthermore, backed by their findings, they propose a novel normalization layer that circumvents the highlighted limitation of existing approaches, namely the alteration of the information carried by the graph signal upon normalizing. Finally, extensive experiments are conducted, in support of their findings.

### Strengths
The presentation is very clear, with a nice balance of theoretical investigations coupled with empirical evaluations. The exposure is gradual, with relevant connections to existing literature. I really enjoyed reading this paper.

The technical results are detailed and extensive.

The authors conduct experiments on various real-world datasets, and the presented results display convincing performance.

### Weaknesses
 The theoretical investigations consider the simplified setting of linearized GNNs. As mentioned in the paper, I acknowledge that you already consider bridging this gap in future work. Would it be possible to provide some insights into what specific challenges do you anticipate in extending the analysis to non-linear GNNs ?

You show that residual connections and normalization layers help against oversmoothing through different mechanisms. Do you think it would it be possible to quantify which of the two has the most significant impact against the oversmoothing phenomenon (be it through bounds or empirical measurement ) ?

### Questions
Please refer to the Weaknesses section.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper provides a formal and precise theoretical analysis of linearized Graph Neural Networks (GNNs) with residual connections and normalization layers. Notably, it reveals how the centering step in normalization can modify the message-passing mechanism of graph signals. Building on this insight, the authors propose a novel, theoretically-grounded normalization layer, GraphNormv2. Experimental results support the efficacy of GraphNormv2, showing its ability to enhance performance across diverse GNN architectures and tasks.

### Strengths
The paper presents valuable contributions by providing a theoretical foundation that enhances understanding of existing techniques for addressing the oversmoothing problem and informs the design of novel normalization layers in GNNs, notably GraphNormv2. The work is well-written, concise, logically structured, and easy to follow, making it accessible to a broad audience. Additionally, the experimental evidence supports the effectiveness of GraphNormv2 across various GNN architectures and tasks.

### Weaknesses
The experimental results are limited and do not sufficiently support the paper's claims, particularly regarding the effectiveness of GraphNormv2 across diverse GNN architectures and tasks.

1. The authors test their method solely on homophilic graphs, limiting the generalizability of their findings. Is there any rationale reason for choosing only homophilic datasets? The oversmoothing problem is particularly pronounced in heterophilic graphs, so it would be valuable to evaluate GraphNormv2 on heterophilic datasets as well. I suggest including experiments on heterophilic datasets such as Texas, Cornell, and at least one large-scale dataset, like Arxiv-year, to better demonstrate the robustness and effectiveness of GraphNormv2 across diverse graph structures.

2. Additionally, whether the theoretical analysis suggests any potential challenges or differences in applying GraphNormv2 to heterophilic graphs compared to homophilic ones?

3. The proposed method is tested on a limited range of GNN architectures, specifically GCN, GAT, and GIN. However, other types of GNNs, such as GraphSAGE and diffusion-based models like Graph Diffusion Networks (GDNs) and Diffusion Convolutional Neural Networks (DCNN), are also susceptible to oversmoothing. So, whether theoretical analysis does suggest any potential challenges or differences in applying GraphNormv2 to heterophilic graphs compared to homophilic ones? If not, testing GraphNormv2 on a broader set of GNN architectures would provide a more comprehensive evaluation and further validate its effectiveness across diverse model types.

### Questions
Please see the weakness.

### Soundness
3

### Presentation
3

### Contribution
3
