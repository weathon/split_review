# A Fast and Effective Alternative to Graph Transformers

- Decision: Reject
- Scores: 3, 6, 5

## Abstract
Graph Neural Networks (GNNs) have shown impressive performance in graph representation learning. However, GNNs face challenges in capturing long-range dependencies that limit their expressive power. To tackle this challenge, Graph Transformers (GTs) were introduced that utilize the self-attention mechanism to effectively model pairwise node relationships. Despite their advantages, GTs typically suffer from quadratic complexity with respect to the number of nodes in a graph, hindering their applicability to large graph datasets. In this work, we present Graph-Enhanced Contextual Operator (GECO), a fast and effective alternative to GTs that leverages shallow neighborhood propagation and global convolutions to effectively capture local and global dependencies. Evaluations on an extensive collection of benchmarks showcase that GECO consistently achieves superior or comparable quality compared to the existing GTs across graphs of various types and scales, improving the SOTA up to 4.5%. Remarkably, these accomplishments are realized while maintaining quasilinear time and memory scaling, making GECO a promising solution for large-scale graph representation learning.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This article proposes a new operator-GECO to replace the graph transformer to solve the computational complexity problem of MHA (multi-head attention) on large-scale graphs. GECO introduces the Hyena architecture into graph convolution calculations, using a combination of long convolutions and gating to compute local and global context. Subsequent experiments have proven that GECO can ensure accuracy while reducing time complexity, on large-scale and small-scale data sets. The main contributions of the article are 1. There is no trade-off between quality and scalability while ensuring both; 2. It confirms that the Hyena architecture can replace MHA in graph neural networks, and global context can improve the performance of GNN.

### Strengths
A new operator-GECO to replace the graph transformer to solve the computational complexity problem of MHA (multi-head attention) on large-scale graphs.

### Weaknesses
- The technical contribution is limited. According to  this survey [2], the proposed LCB module can be treated as the GNN-as-Auxiliary-Modules in the Alternatively form (Figure 1 in [2]). Additionally, the writing of this paper seems rushed. Many details are missing and hard to understand. For example, in Algorithm 1, line 3, what is $V_t \leftarrow (P)_t FFTConv(F_i, V)_t$. Actually, I found more details of this algorithm in Algorithm 3,  page 8, [link](https://arxiv.org/pdf/2302.10866.pdf)[1]. The forward pass of GCB Operator is nearly identical to Hyena, which is not new. The core of the GCB operator, involving FFT convolutions and gating, directly mirrors the Hyena architecture, with only minor adaptations for the graph domain. The paper does not sufficiently articulate the novelty of these adaptations beyond the existing Hyena framework.

- Using positional  embedding to encode the graph structural information is not new. The paper uses standard positional encodings, which are well-established in the literature, and does not introduce any novel method for incorporating structural information. The application of these encodings is not a significant contribution.

- The paper claims that the proposed model is "fast", and provides detailed time complexity analysis. Unfortunately, from the theoretical perspective, GECO has the same level complexity as Message-passing GNN $O(NlogN+M)$ and it can only surpass vallia transformer when $M<<N^2$. Additionally, no experiments regarding the running time efficiency are presented. The analysis does not consider practical runtime, and the theoretical analysis is not compelling since the condition $M << N^2$ is a common property of sparse graphs, which is the main reason why GNNs are used in the first place. The paper should include empirical runtime comparisons to validate the claim of being "fast".

- It's necessary make more comparisons with more baselines of Graph Transformer. Please refer to [2] for more baselines.

### Questions
See weakness.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper targets the quadratic complexity issue in training graph transformers with full-attention over large graph datasets, and proposes GECO, which is a Hyena-based operator that captures both local and global dependencies to replace the original attention operator. The authors conduct extensive experiments in demonstrating GECO’s effectiveness over long-range and large graph datasets. In addition, the authors empirically demonstrate GECO’s insensitivity to node ordering wrt. performance.

### Strengths
1.	The targeted quadratic complexity issue reside in graph transformers is meaningful. The designed GECO not only makes it sub-quadratic, but also remains in a considerable performance level.
2.	The experiments are conducted extensively. The results seem promising.

### Weaknesses
1.	The presentation of this paper may be improved for coherence. For example, in Sec. 3.3, the GCB module is designed/modified based on Hyena, the key component for sub-quadratic complexity. The authors may want to include a short description of it in the main context rather than the appendix. Otherwise, it may introduce difficulties in comprehension. In addition, the proposition in the main context assists in analyzing the complexity, which is presented in the appendix. It seems like they can be excluded from the main context.
2.	The motivation is to make the model parameters sub-quadratic to the number of nodes. While theoretical analysis is conducted, I would like to see empirical results (e.g., training time) in GECO’s training efficiency compared with other baselines.

### Questions
1.	In the Graph-to-sequence conversion part, the authors state “time-correlated sequences, aligning node IDs with time (t)”. Where does the ‘time’ come from? What does it mean?
2.	The LCB module conducts neighborhood information propagation for each node. It directly utilizes the connectivity information via adjacency matrix. In the meantime, GECO is implicitly learning this ‘connectivity’ via the convolutional filters. Is there any information overlap here?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper focuses on a good question, i.e., the scalability of Graph Transformers (GTs). GTs suffer from quadratic complexity when the node number in a certain graph is very large. The authors propose a somewhat improvement of GTs. An improved (the authors define it as an alternative) dense attention mechanism is utilized to reduce the computing complexity of GTs. It is claimed that the proposed GECO can capture long-range dependencies. The proposed method shows some improvements in a limit number of datasets. The appendix is of a lot content including details of experimental settings, related work, a brief discussion of computational complexity discussion, etc.

### Strengths
-This paper focuses on a good and significant research question and poses a very smart improvement by modifying dense attention mechanisms of GTs.

-This paper includes rich contents. An additional appendix containing many details that can help to clearly understand the paper.

-The proposed method shows some acceptable experimental results when comparing with baselines and good ablation experiments.

### Weaknesses
 -The innovation is not strong enough, which diminishes the significance of the paper. Essentially, the authors replaced the multi-head self-attention module in the original Transformer with a global convolutional module, and then they claim their proposal is to improve efficiency. However, the necessity of this replacement needs to be considered, and it appears to be of limited significance. The primary issue lies in the absence of self-attention mechanism, resulting in a diminished capability to capture long-range dependencies. Experimental results on large datasets, such as PCQM and COCO, indicate that the model's performance is inferior to other Graph Transformer methods.

-Lacking experimental results to verify “fast” of the proposed method. Specifically, there is no emphasis in the experimental results, no parameter complexity analysis, no comparison of computing resource consumption or computing time. These are fundamental experiments in verifying “fast” of a certain method. And the results provided to demonstrate the 'effectiveness' of the proposed method in capturing long-distance dependencies, as shown in Tables 1, 2, and 4, may not offer sufficiently strong evidence for its superior performance. Overall, the title of this paper is ambitious and likely to capture attention with insufficient innovative approach, even though the authors claimed “they are the first to”.

-The design, organization, and writing of this paper are not very clear to me. Firstly, the motivation seems to enhance GT, but the authors care a lot about capturing long-range dependencies, which I have illustrated in last point, the results are not impressive enough. If the authors want to show the outperformance of trade-off between capturing long-range dependencies and fast calculation/computation, there is a lack of comparison of baselines including those methods not using Transformers. Then, If the authors want to show the improvement of the enhanced GT in effectiveness, the results are not competitive. And I think the authors also need to refer to some recent studies such as “Hierarchical Transformer for Scalable Graph Learning”. Next, the authors aim to illustrate that their proposed method is fast and has distinct difference from GraphGPS. But why GraphGPS? It confuses me.

### Questions
-What exact problem the authors want to solve? And how you directly verified that the problem is well solved, with what metric/way? 

-How to balance the trade-off between fast and efficiency? Why is your method the best?

-I am well aware that the comparison of computation complexity (theoretically) among several models including GECO. But what about the experimental verification?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
