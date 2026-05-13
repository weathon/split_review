# GRAIN: Exact Graph Reconstruction from Gradients

- Decision: Accept
- Scores: 6, 5, 6, 6, 5

## Abstract
Federated learning allows multiple parties to train collaboratively while only Federated learning allows multiple parties to train collaboratively while only sharing gradient updates. However, recent work has shown that it is possible to exactly reconstruct private data such as text and images from gradients for both fully connected and transformer layers in the honest-but-curious setting. In this work, we present GRAIN, the first exact reconstruction attack on graph-structured data that recovers both the structure of the graph and the associated node features. Concretely, we focus on Graph Convolutional Networks (GCN), a powerful framework for learning on graphs. Our method first utilizes the low-rank structure of GCN layer updates to efficiently reconstruct and filter building blocks, which are subgraphs of the input graph. These building blocks are then joined to complete the input graph. Our experimental evaluation on molecular datasets shows that GRAIN can perfectly reconstruct up to 70\% of all molecules, compared to at most 20\% correctly positioned nodes and 32\% recovered node features for the baseline.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes GRAIN, a gradient inversion attack on GNNs. GRAIN identifies subgraphs within gradients and filters them iteratively by layer to construct the full input graph through a depth-first search approach. New evaluation metrics are introduced to measure similarity between reconstructed and original graphs for graph gradient inversion attacks. GRAIN has a desirable performance on the molecule benchmarks.

### Strengths
- This paper proposes the first gradient inversion attack on GNNs. This topic is interesting and unexplored. This paper could inspire further investigation on this topic.
- A new metric is proposed to measure the similarity between graphs.
- The proposed GRAIN achieves a desirable performance compared with existing attacks.

### Weaknesses
 - It is mentioned that $\mathcal{T}_0$ is the cross-product of all possible feature values. It seems to be impractical for general attributed graphs and only possible for molecular graphs where the node features are in a small set with low dimensionality. The paper does not adequately address the computational complexity of generating $\mathcal{T}_0$ for graphs with high-dimensional or continuous node features. Specifically, the method appears to rely on an exhaustive search over all possible feature combinations, which would become intractable for even moderately sized feature spaces. 
- It would be helpful to include a Threat Model section to introduce the attack settings, such as the adversary's knowledge, capability, and objective. What is the function $f$ in Algorithm 2? Is it the exact target GNN model? The paper lacks a clear definition of the adversary's capabilities and the specific information they have access to, which makes it difficult to assess the practical relevance of the attack. The description of function $f$ is also vague, and it is unclear whether it represents the true target model or an approximation.
- The introduction mentions federated learning as a practical scenario of gradient inversion attacks. However, the methodology part does not include any specific FL settings (such as local models and global models). Is FL a necessary requirement for implementing GRAIN? The connection between the proposed attack and federated learning is not clearly established, and the paper does not explain how the attack would be implemented in a federated setting. It is unclear if the attack requires access to local gradients or if it can be performed using only aggregated gradients.
- The challenge of gradient inversion attacks on GNNs is understated. Why GRAIN is not a trivial adaptation of existing methods [1] to GNNs and what unique challenge does GRAIN overcome while other methods fail to? The paper does not adequately explain why existing gradient inversion methods cannot be directly applied to GNNs, and what specific challenges are addressed by the proposed GRAIN method. The paper should clarify the unique difficulties posed by the graph structure and the non-Euclidean nature of GNN inputs.
- The introduction of proposed algorithm is not clear enough. It would be better to introduce the detailed algorithm following a single direction (e.g., from input to output). And it would be helpful to add a notation table. The description of the algorithm is difficult to follow, and the paper would benefit from a more structured and step-by-step explanation. A notation table would also be helpful to clarify the meaning of the various symbols and variables used in the algorithm.

### Questions
Please see Weaknesses.

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents GRAIN, the first exact reconstruction attack specifically designed to target GCNs. By leveraging the low-rank structure of GCN layer updates, GRAIN can accurately reconstruct both the graph structure and the associated node features from the gradients shared under federated learning setting. This attack demonstrates a significant privacy vulnerability in GCN training within the federated learning framework.

### Strengths
1. It is the first work that explores extracting the structure of a graph from gradients. 
2. The framework demonstrates promising performance across different scenario.

### Weaknesses
1. The article seems to be largely based on the theories presented in [1] and then adapted it for GCNs, particularly Theorem 3.1. However, for readers unfamiliar with this work, it may be quite challenging to comprehend. We hope the authors can provide more discussion on why the filtering mechanism can be effective.
2. Following the previous question, what is the difficulties encountered when applying the methods from [1] to graph data? A detailed explanation of the challenges encountered during this adaptation, including any limitations or obstacles that were overcome, would help clarify the novelty of the work presented.
3. The article uses the degree of a node as a node feature; however, this approach may limit the application scope. For instance, in the case of chemical molecules mentioned in the article, relevant features are more likely to include chemical properties. We suggest that the authors discuss this point and conduct further experiments.

### Questions
see Weaknesses

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The main contribution of this paper is that it is the first to address gradient inversion attacks on graph data, highlighting privacy risks in graph federated learning. Based on the theorem from Petrov et al. (2024), the authors propose a method capable of reconstructing both the graph structure and node features. They reconstruct the graph step-by-step, from low-degree to high-degree levels, with each step involving the filtering of unlikely candidates through a span check. Finally, by leveraging degree information in the features, they generate the final prediction using a depth-first search (DFS) algorithm to combine the remaining candidates.

In experiments, the proposed method outperforms other baselines. The authors also conduct a hyperparameter analysis by adjusting L and d', representing the number of GNN layers and the hidden dimension, respectively. Additionally, they test varying numbers of nodes, identifying limitations as discussed in Section 7.

### Strengths
1. As the authors mention, this paper addresses a crucial yet unexplored problem: gradient inversion attacks in graph federated learning.
2. Constructing both the graph structure and features is a challenging task, but it is interesting to see experimental results that accurately reconstruct the input graph, even if restricted to chemistry graphs.
3. This paper suggests future directions for gradient inversion attacks in the graph domain, as discussed in Section 7 (Limitations).
4. The paper is well-written and easy to follow.

### Weaknesses
1. I agree on the importance of exploring gradient inversion attacks in the graph domain, and this could be a notable contribution of the paper as it is the first to address this issue. However, the scope is quite limited in terms of graph types. Specifically, the paper focuses only on chemistry datasets. To fully substantiate its contribution as a pioneering work in gradient inversion attacks on graph data, the authors should demonstrate that this method is applicable to other types of graph datasets, such as citation networks (e.g., Cora, PubMed) or transaction networks (e.g., Elliptic). This is especially important since molecular graphs may be relatively less privacy-sensitive than other graph types (e.g., transaction networks), and federated learning in molecular graphs may be less common. I suggest that the authors provide additional evaluations on other categories of graph datasets.  

2. As shown in Table 2, the proposed method only works well when the input graph has a limited number of nodes (i.e., $\leq 25$). I understand that, given the step-by-step approach of combining building blocks, this limitation leads to higher computational costs and a greater risk of error as the graph size increases.  The authors should provide a more detailed analysis of the computational complexity, particularly how the runtime scales with the number of nodes and edges. Furthermore, it would be beneficial to explore potential optimizations or approximations to mitigate this issue.

3. The claim that using the degree as a feature is widely adopted in training GCNs is not entirely convincing. Using degree values as features is more common in graphs lacking attributes or in structural learning tasks. However, since this paper addresses gradient inversion attacks in federated learning, it should consider more practical settings where degree values may not be used as features. How might this method be adapted if degree information is not available as a feature? The reliance on degree as a feature could be a significant limitation in real-world scenarios where such information is not readily available or is considered sensitive.

### Questions
1. In Table 3, $d' = [200, 300, 400]$ represents quite a large hidden dimension for training graphs with a small number of nodes (i.e., $\leq 25$). I wonder if this method will still work when the hidden dimension is much smaller (e.g., 32, 64, 128).

2. As I mentioned in W1, I suggest that the authors provide additional evaluations on other categories of graph datasets.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents GRAIN, a novel gradient inversion attack designed for Graph Convolutional Networks (GCNs) in the federated learning (FL) setting. GRAIN leverages an efficient filtering mechanism to identify subgraphs of the input graphs, which are then pieced together using a depth-first traversal to recover the full original graph. This method enables the exact reconstruction of graph structures and node features from gradient updates clients share with the federated server. The main contribution is extending gradient inversion attacks to GCNs under harder FL settings, which is a significant step toward understanding the privacy vulnerabilities of federated learning when applied to graph-structured data. The introduction of new evaluation metrics for graph similarity (e.g., GRAPH-N) is also an excellent contribution, providing valuable insights into partial and exact graph reconstructions. Lastly, this paper presents extensive rigorous experiments on molecular data, demonstrating that GRAIN significantly outperforms existing baseline attacks regarding exact graph reconstruction accuracy in the chemical domain. The empirical performance convincingly highlights client privacy risks associated with FL for graph-structured data, making this work relevant to a broad audience.

Overall, I am leaning toward acceptance of this paper. The novelty of GRAIN, its strong experimental results, and its contribution to the discussion on privacy risks in federated learning make it a valuable and impactful addition to the conference. However, there are some limitations and concerns that require further clarification and improvement (see weaknesses).

### Strengths
1. Technical novelty.
2. Strong experimental results.
3. Contribution to the discussion on privacy risks in federated learning.

### Weaknesses
One major limitation is that GRAIN struggles with larger graphs due to the high computational cost. As mentioned in the paper, the method times out for large molecules. Have you considered any strategies for reducing the computational complexity of GRAIN, such as parallelizing the depth-first search or using pruning techniques? Furthermore, more detailed comparisons of the convergence time of GRAIN versus the baseline methods might be beneficial, particularly for larger graphs. Could you provide more quantitative details on the computational overhead of GRAIN in comparison to other baselines, specifically detailing the time complexity of each step (e.g., subgraph filtering, depth-first search, feature reconstruction) and how these scale with graph size (number of nodes and edges)?

I noticed several similarities between the algorithms and figures in this paper and those in your reference DAGER. I would appreciate more clarification on how this paper differentiates itself and introduces novel contributions beyond the existing work. Highlighting the differences, extensions, and innovations more clearly and explaining your considerations on adaptions might strengthen the paper's contribution. It would be beneficial to explicitly outline the limitations of DAGER when applied to GCNs and how GRAIN overcomes these limitations, including a discussion of the theoretical and practical challenges of extending gradient inversion attacks to graph-structured data.

Finally, in the experimental section, the paper notes that GRAIN cannot recover multivalent interactions, an edge property that GCNs not able to capture. However, given multivalent interactions are associated with features like "valence structures" in the MoleculeNet benchmark datasets, whether other node features such as valence structures be fully used in graph filter and node-feature recovery? This raises the question of whether GRAIN has limitations in effectively utilizing feature vectors of the input nodes. It would be helpful if the authors could clarify whether GRAIN could recover some other complex critical chemical characteristics with all feature vectors and the reasons behind them. Furthermore, could you provide a more detailed analysis of the types of node and edge properties that GRAIN can and cannot recover, and why?

For the experiments, the following should be addressed.

1.	It would be helpful to see more experiments that vary the value of chosen threshold tau in the span check mechanism to better understand its role in filtering performance. Specifically, how does the choice of tau affect the trade-off between the number of correctly identified subgraphs and the number of false positives, and what is the sensitivity of the overall reconstruction accuracy to this parameter?

2.	For the scenario where exact reconstruction is not achieved, what proportion of nodes and edges are typically misplaced, and how? Additional discussion on this and how it affects real-world privacy concerns would provide a more comprehensive picture of the method's practical implications. A more detailed analysis of the types of errors that occur during reconstruction (e.g., node misplacement, edge addition/deletion, feature corruption) and their frequency would be valuable.

3.	As the proposed graph similarity metric is novel and potentially valuable, I have some concerns regarding the fairness and comparability of the results. Specifically, how do you ensure that the comparison is fair, given that the baseline methods were not specifically designed for graph-structured data? Additionally, it would be helpful to include a more detailed explanation of why common, widely used metrics were not used for comparison in the meantime. This clarification would strengthen the validity of your results and provide a clearer understanding of how the proposed metric aligns with established evaluation standards. It would be beneficial to include a discussion of the limitations of the proposed metric and how it might bias the results in favor of GRAIN.

Minor comments:
1)	In the Abstract, there is redundancy in the first sentence (e.g. “Federated learning allows multiple parties to train collaboratively while only Federated learning…”).
2)	In the third line in 5.1, the symbol is a subset instead of an overlap.
3)	In 5.1, the third sentence in Additional structure-based filtering and likelihood ordering, the grammar of “Specifically, we for every…” is wrong. The last sentence in the same subsection “lines 3–13 of Algorithm 1” should be 3-14.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a method for gradient inversion attack on graph neural networks. This problem differs from previous gradient inversion attacks in that not only the node features but also the graph structures. The proposed method involves a recursive construction process that continually glues small building blocks to build large graphs. The authors propose some new metrics for this new task of gradient inversion attack on graphs, and show that the proposed method achieves state-of-the-art performance compared to other existing gradient inversion attacks.

### Strengths
1. This paper tackles a new problem of gradient inversion attack on graphs. More importantly, gradient inversion attack on graphs is different from GIA for other types of data, in that graphs not only have feature vectors, but also have graph structures. 
2. This paper proposes a new evaluation metric to evaluate GIA on graphs, which would help future efforts in this field. At present, this research field is blank without any existing evaluation protocols, so the first such protocol or metric is nice to have.

### Weaknesses
1. The presentation of this paper requires significant improvements. The technical methodology of this paper is very hard to understand.

- The abstract contains a redundant sentence 'Federated learning allows multiple parties to train collaborative while'.

- It is suggested that the authors should clearly state the attack setting. For example, who is the attacker (server or client), what does the attacker know (model parameters, gradients, anything else).

- The authors should revise the use of the term 'degree'. It is used simultaneously to describe 'the number of edges connected to a node', as well as 'the number of hops of a subgraph'. This makes the paper very confusing to read. The second usage of degree can be replaced to something like 'hop'.

- For Theorem 3.1, the authors should define the concept of 'rowspan' and 'colspan', and briefly state the implication of the theorem. The same holds for Lemma 5.1.

- It is not clear how to obtain $T_0$.

2. This paper makes unrealistic assumptions about the problem and the data.

- In Lemma 5.1, the authors assume that $\tilde{A}$ is full rank. However, this is an unrealistic assumption, in that in practice, the adjacency matrix of most graphs are low-rank [1,2]. Therefore, for this Lemma to work, the authors either need to show that real-world graphs are almost full rank, or discuss what happens when the adjacency matrix is low-rank.

- In Page 4, Lines 183-190, the authors say that 'we leverage that the degree of a node is a widely used node feature', and subsequently assume that the degree is a known knowledge. However, this is not always true. When the node features are bag-of-word vectors, word embeddings, etc., the assumption may not hold. It is suggested that the authors should at least explicitly state the assumption.

- In Section 6.2, the authors say that 'we provide the attack with the correct number of nodes'. However, in practice, this is often not the case --- how can the attacker know the number of nodes before attacking? The authors should either justify the assumption, or discuss what happens when the attacker does not know the information.

- In Section 5.1 and Figure 2, the authors show that the gluing operation actually merges the same node $v$ in two building blocks, and merge edges similarly. However, I did not quite understand how the information of 'two nodes in two different building blocks correspond to the same node' is obtained. The authors should state how to obtain this information, as in practice, all reconstructed nodes are not given node indices and are only identified with features (which are inaccurate by themselves).

3. The authors' claim that the proposed method is 'exact' should be an overclaim. In fact, the proposed GRAIN can reconstruct 30-70% of all molecules (Table 1), which, in my opinion, is not sufficient to claim 'exact'. The authors should revise the claim to better fit the actual effectiveness of GRAIN.

### Questions
1. Please briefly explain the unclear parts stated in Weakness 1. 

2. Please briefly discuss how the assumptions in Weakness 2 hold in practice, and what will happen when they do not hold.   

3. In practice, graph data are often organized in a batch, and the gradients are an average of all samples in the batch. Does GRAIN assume batch_size=1? Will this change the effectiveness of GRAIN?

4. In the case with more complex/adaptive node-wise relations, such as Graph Attention Networks, will GRAIN still work? From my understanding of Lemma 5.1, $\tilde{A}$ plays an important role, and in GAT, the actual message passing topology is not $\tilde{A}$ .

### Soundness
2

### Presentation
1

### Contribution
2
