# Adaptive Expansion for Hypergraph Learning

- Decision: Reject
- Avg Score: 5.50
- Scores: 3, 8, 6, 5

## Abstract
Hypergraph, with its powerful ability to capture higher-order complex relationships, has attracted substantial attention recently. Consequently, an increasing number of hypergraph neural networks (HyGNNs) have emerged to model the high-order relationships among nodes and hyperedges. In general, most HyGNNs leverage typical expansion methods, such as clique expansion (CE), to convert hypergraphs into graphs for representation learning. However, they still face the following limitations in hypergraph expansion: (i) Some expansion methods expand hypergraphs in a straightforward manner, resulting in information loss and redundancy; (ii) Most expansion methods often employ fixed edge weights while ignoring the fact that nodes having similar attribute features within the same hyperedge are more likely to be connected compared with nodes with dissimilar features. In light of these challenges, we design a novel CE-based \textbf{Ad}aptive \textbf{E}xpansion method called \textbf{AdE} to expand hypergraphs into weighted graphs that preserve the higher-order hypergraph structure information. Specifically, we first introduce a Global Simulation Network to pick two representative nodes for symbolizing each hyperedge in an adaptive manner. We then connect the rest of the nodes within the same hyperedge to the corresponding selected nodes. Instead of leveraging the fixed edge weights, we further design a distance-aware kernel function to dynamically adjust the edge weights to make sure that node pairs having similar attribute features within the corresponding hyperedge are more likely to be connected with large weights. After obtaining the adaptive weighted graphs, we employ graph neural networks to model the rich relationships among nodes for downstream tasks. Extensive theoretical justifications and empirical experiments over five benchmark hypergraph datasets demonstrate that AdE has excellent rationality, generalization, and effectiveness compared to classic expansion models.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a new hypergraph learning method based on the previous work of HyeprGCN, by expanding the hypergraph into a weighted graph and then running a graph neural network over the expanded graph. Experiments show that the proposed method marginally outperforms selected baselines.

### Strengths
1. The authors have made a good observation that hypergraph expansion has grown to be an important area of study in hypergraph-related learning and analysis. Therefore, I think the subject of study is very meaningful.

2. The experiments are well designed to support the main claims in the methodology. They are also quite extensive in coverage of various expansion methods (Table 1) as well as hypergraph learning methods (Table 2)

### Weaknesses
1. I am not fully convinced about the design choice that, regardless of the size of the hyperedge, always two nodes are chosen as representative nodes. Why is it not three or an adaptive number of representative nodes? Also, in expansion, this essentially always approximate any internal connectivity within a hypergraph by a "bar-bell" shaped graph, which does not look very intuitive to me. Can the authors explain more on this matter?

2. I remains very unclear to me why we should use S, the sum of scaled attribute features, to select representative nodes. In other words, why would having a large (or small) sum of scaled attributes be an important factor to consider when choosing the representative nodes? 

3. The propositions 1-4 all seem to discuss something straightforward to me. It is easy to see that the distance metric defined in Eq. (3) is non-negative, commutative, and assign higher values to more similar pairs of attributes due to its weighted sum of square.  For Proposition 4, AdE by its design would obviously connect every pair of nodes in a hyperedge with only 3 nodes. 

4. The numerical results in both Table 1 and Table 2 show that the proposed method is very marginally higher than the best baseline.

Minor typo:
"... in a 3-unifirm hyperedge", in the last paragraph of Section 4;

### Questions
See Weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work proposes an adaptive method called AdE to convert the hypergraph into a weighted graph in an adaptive manner. First, it designs a global simulation network called GSi-Net to select two representative nodes to represent the corresponding hyperedge adaptively. After connecting the rest of the nodes with the two representative nodes, this work designs a distance-aware kernel function to dynamically learn the edge weights among node pairs. With the adaptive weighted graph, AdE leverages GNNs to learn the graph representatives for the downstream classification tasks. Moreover, this work provides comprehensive experiments and extensive theoretical justifications to demonstrate the effectiveness and rationality of AdE.

### Strengths
1. The idea of adaptively learning a weighted graph from the hypergraph is useful. Most existing works merely expand the hypergraph into a graph roughly and feed the converted graph into neural networks for representation learning, which results in information loss or information redundancy.
2. From my perspective, the model design of AdT including GSi-Net and the distance-aware kernel function is novel and rational, with theoretical proof and extensive experiments over five benchmark datasets.
3. Comprehensive experiments including comparison experiments, ablation studies, embedding visualization, and complexity analysis are conducted to demonstrate the effectiveness and its generalization. 
4. The presentation is clear, making it easy to follow the key points of this work.

### Weaknesses
1. This work discusses three existing expansion methods, i.e., clique expansion, line expansion, and star expansion.  As this work introduces these three methods briefly in related Works, I do not get the difference between AdE, CE, LE, and SE. I am curious about the advantages and disadvantages of each method.
2. This work claims that AdE is equivalent to the weighted clique expansion in 3-uniform hypergraphs in Proposition 4. I am a bit confused about that as AdE is designed to dynamically learn the edge weights among node pairs. But most existing works, let us say, weighted clique expansion, assign a fixed weight between the node pair. Why is AdE equal to weighted clique expansion from the edge weight perspective? 
3. This work conducts experiments over five benchmark hypergraph datasets, i.e., Cora-CA, DBLP, Cora, Citeseer, and Pubmed. I am a bit curious about the format of these datasets. It looks like these datasets are commonly used in graphs.  What are the differences between these hypergraphs and graphs? Do hyperedges in these hypergraphs have hyperedge features?

### Questions
According to the weakness, I list my questions as follows:
1. What are the advantages of AdE compared with these expansion methods?
2. In Proposition 4, why AdE equal the weighted clique expansion from the edge weight perspective? 
3. What are the differences between these benchmark hypergraphs and the corresponding graphs? 
4. Does the hyperedge in hypergraphs have the attribute features? Does the node in hypergraphs share the same attribute features as graphs?

### Soundness
3 good

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
The authors propose a method to project a hypergraph to a corresponding graph where the edge weights are not straightforwardly copied from the hyperedges, but an adaptive approach calculates them. The proposed approach is comprised of two steps - using GS-Net to identify representative nodes, followed by a distance-aware kernel to compute the edge weights.

### Strengths
1. The problem space is very interesting. There is very little attention paid to finding innovative ways to convert hypergraphs to graphs by preserving the desired properties. 
2. The proposed method outperforms the existing baselines. The ablation study provides an understanding of the contribution of different components.

### Weaknesses
1. Existing works like node-degree preserving hypergraph projection [1] are not considered. Clique/star-based expansions are not the right representative of SOTA methods. 
2. The idea of using node features to compute edge weights assumes that there is an underlying homophily, which was not well captured by hyperedges (hence, the existence of a hyperedge does not mean the constituent nodes share the same strengthened bond), but the projected graph will capture it better. It requires more justification. (please provide additional justification if I got the idea wrong).
3. The current write-up lacks motivation behind the proposed steps in the method. A short text explaining the intuition behind the reason for selecting representative nodes and follow-up steps would be helpful.

### Questions
1. What is the rationale behind having a representative pair of nodes for each hyperedge? Also, provide an explanation on how this approach will cater to hyperedges of varying sizes (it can be 1 to n).
2. How does this approach work on a hypergraph where nodes do not have any attributes? Several domains, such as computational biology, where hypergraphs have extensive applications, but getting node-level features is challenging. 
3. Provide more details on the hypergraph datasets, such as their size, average degree distribution, average hyperedge size, etc. This will help explain the result trends. 
4. Does the proposed method apply to tasks other than node classification? (such as clustering, hyperedge prediction, etc.)

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposed a new algorithm for clique expansion in hypergraph. Clique expansion in the previous methods have the same edge weight for all edges. In this paper, the author proposed an adaptive algorithm which can calculate the edge weight based on the hyperedge. The proposed model solves two challenges: 1) the previous model directly apply a clique expansion causes information loss/redundancy. 2) the fixed edge weight ignores the potential strong connection in one hyperedge. 

The model contains two steps. First, a global simulation network is applied to choose the most representative node pair $(v_{e^-}, v_{e^+})$. Secondly, an kernel function calculates the edge weights(distances) from two nodes in the node pair to other nodes. The new graph thus contains three kinds of edges: $(v_{e^-}, v_{e^+})$, $(v_{e^-}, v_{m})$, $(v_{m}, v_{e^+})$. For validation, the task is a classification task. The loss is applied to both two networks(global simulation network and kernel function) separately, which indicates it's not an end-to-end model. 

The performance show that the paper outperform several baselines. The ablation study shows that each module is helpful and combining them together make the performance better.

### Strengths
The paper is well written and easy to follow. The challenges are clear, the authors proposed a new model solved it. The Gaussian Kernel and the adaptive edge weight seems to be novel in this field. The proposed model is equivalent to weighted clique expansion in 3-uniform hypergraphs, which somehow guarantee the expression power.

### Weaknesses
One concern is that the performance doesn't outperform the baseline too much. For some datasets the proposed model only has a performance gain smaller than 1 std, like Cora-CA in table 1 and 2, Cora in table 2.

Also, the proposed model is mainly based on HyperGCN. But other models, such as AllSet, have a completely different scheme. They apply star expansion instead of clique expansion. The reason is that the traditional clique expansion is not able to represent the high order information. Let's say there are four nodes: a,b,c,d. The clique expansion can't tell the difference that whether abc have a strong connection or ab and bc have a connection while ac have no connection. This is one example, it can be more nodes. Although in the proposed model, they have an edge weight to help them classify. But I'm still concerning about if it really helps distinguish between these situations. Since edge weight are pair-wise relation. Hypergraph deals with high-order relation. I wonder if authors have more discussion regarding this.

Meanwhile, since each time the model needs to reconstruct the graph, find the maximum distance in one hypergraph. The time complexity will be a problem if the average $d(e)$ is larger. 

Furthermore, some other models using hypergraph contrastive learning performs better than You are AllSet(AllDeepSet) and other models. It seems that the performance is not good enough.

### Questions
See weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
