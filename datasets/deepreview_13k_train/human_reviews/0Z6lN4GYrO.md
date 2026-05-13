# S4G: Breaking the Bottleneck on Graphs with Structured State Spaces

- Decision: Reject
- Scores: 3, 3, 8

## Abstract
The majority of GNNs are based on message-passing mechanisms, however, message-passing neural networks (MPNN) have inherent limitations in capturing long-range interactions. The exponentially growing node information is compressed into fixed-size representations through multiple rounds of message passing, bringing the over-squashing problem, which severely hinders the flow of information on the graph and creates a bottleneck in graph learning. The natural idea of introducing global attention to point-to-point communication, as adopted in graph Transformers (GT), lacks inductive biases on graph structures and relies on complex positional encodings to enhance their performance in practical tasks. In this paper, we observe that the sensitivity between nodes in MPNN decreases exponentially with the shortest path distance. Contrarily, GT has a constant sensitivity, which leads to its loss of inductive bias. To address these issues, we introduce structured state spaces to capture the hierarchical structure of rooted-trees, achieving linear sensitivity with theoretical guarantees. We further propose a novel graph convolution based on the state-space model, resulting in a new paradigm that retains both the strong inductive biases from MPNN and the long-range modeling capabilities from GT. Extensive experimental results on long-range and general graph benchmarks demonstrate the superiority of our approach.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new architecture for graph representation learning to address the limitations of message passing neural networks. Specifically, to generate the representation for a target node, representations of nodes that are at the same hop are summed up, and then a structured state space model (S4) is applied to the sequence of hop representations. 
This paper demonstrates the long-range modeling capacity of the proposed architecture by analyzing the sensitivity between distant nodes. The proposed model shows good empirical performance on a series of graph benchmarks.

### Strengths
- The idea of extending S4 to graphs is interesting and novel to the graph ML domain.
- The sensitivity analysis is intuitive and clear to explain why S4 can help to utilize the information of distant nodes.
- The model shows good empirical performance.

### Weaknesses
 - Over-smoothing and over-squashing: The paper claims that the proposed model can address both over-smoothing and over-squashing. However, over-smoothing is caused by the lack of local neighborhood information. S4 aims to better capture distant information, which seems to be in the opposite direction of addressing over-smoothing. The experiments didn’t touch over-smoothing either. Furthermore, the argument that S4 avoids over-smoothing because it doesn't perform message passing on the original graph structure is not fully convincing. While it's true that message passing can lead to Laplacian smoothing, the core issue is the aggregation of node features, and the proposed method still aggregates features from different hops, which could still lead to similar issues if not handled carefully.
- Lack of expressiveness analysis: By converting a neighborhood into a sequence, the model considers the shortest distance, but would inevitably lose other structural information. E.g., the model doesn’t know the edges between hop $k-1$ and hop $k$, i.e., for a certain node at hop $k-1$ which nodes at hop $k$ are connected to it. This questions the expressiveness of the proposed model. The model essentially treats the neighborhood as a sequence of concentric circles, ignoring the graph structure within each circle and between circles. This simplification could severely limit the model's ability to capture complex graph patterns. Theoretical analysis is necessary to justify the expressiveness and support the empirical results, but it’s missing.
- According to the experiments, the performance of S4G itself is not good enough on several datasets, while S4G+, which contains an extra MPNN layer, can do significantly better. This implies that S4G itself may lose some structural information (together with the above point). The fact that a simple MPNN layer significantly boosts performance suggests that the sequential processing of hop information alone is insufficient for capturing all relevant graph features, and that the model may be discarding crucial local structural information.

### Questions
- More details of the experimental setup should be given, such as hyper-parameters (e.g., is the hidden dimension very large? (since the HIPPO matrix is fixed))
- What is the specific difference for those baselines with asterisk? Did the proposed model follow the asterisk setting?

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
The paper proposes a new model based on structured state spaces, termed S4G, for enabling better information flow in graph neural networks without losing the graph inductive bias. The fundamental idea builds on two observations: (1) Graph neural networks have strong relational inductive bias, but they are subject to an exponential decay in information with increasing number of layers and (2) Graph transformers are subject to only constant decay in information but they typically lack appropriate graph inductive biases. The idea is to use "structured state spaces" to capture the hierarchical structure of rooted-trees from the source nodes, and to keep strong inductive bias while having only linear decay of information. Authors present experimental results on long-range and general graph benchmarks.

### Strengths
- **Problem setup**: It remains challenging to capture long-range interactions using graph neural networks for various reasons discussed in the paper, so the problem formulation is important and meaningful.

### Weaknesses
 - **Scholarship**: The paper fails to present a good coverage of the related work which also makes the contributions questionable. This is particularly the case with the coverage of recent multi-hop approaches. Authors mention that multi-hop models do not help with e.g. over-squashing as they rely on taking the powers of the adjacency matrix which amplifies the over-squashing problem. This is true, but this is exactly the reason why other multi-hop approaches have been studied extensively, see e.g. [1], where the idea is to directly aggregate information from higher-order neighbours obtained using shortest path distances (a sensitivity analysis is also conducted).

- **Novelty, Originality, and Significance**: To the best of my understanding, the proposed idea of this paper appears to be largely covered by [1], since rooted trees are essentially constructed in the exact same way and aggregation is over the respective neighbourhoods $N_1...N_k$ of a particular node. Moreover, the graphormer model [2] follows essentially a very similar path: it aggregates over the neighbors at different shortest path distances directly. I do not see a fundamentally new or novel aspect in the present work, and neither a significant contribution. I'm happy to re-evaluate if the authors could better frame their approach in the existing literature and can identify the differences and contributions.

- **Experiments on Long Range Graph Benchmarks**: The empirical results do appear promising, but unfortunately, the benchmark of Dwiwedi et al has been criticised recently [3] and it turns out that the gap between GNNs and graph transformers either disappears or becomes insignificant after a systematic tuning of the GNN models. This is a very recent finding and the current paper cannot be held responsible, but given that this is one of the two experiments conducted, the validity of the proposal remains questionable. It is also unclear whether the above-mentioned approaches, i.e., graphormers, would match the presented results. 

- **Technical limitations**: There are many limitations of the sensitivity analysis of Topping et al (and other approaches are proposed recently see eg  [4]). It requires bounded derivatives (which may not hold in practice) and also a normalised adjacency matrix. It is easy to see that without the assumption on the latter the values will explode rather than vanishing. On the other hand, it is easy to show that simple tricks (such as a fully connected layer, or adding a virtual node) can theoretically "maximize" this bound, and a systematic evaluation is needed against these simple model variations to clearly identify the benefit of the proposed idea.

### Questions
Please refer to my review.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors propose a new graph NN architecture, S4G, using structured state space. S4G maintains similar inductive biases induced by regular MPNN but has the sensitivity with a linear decay. In this way, the message bottleneck problem is largely alleviated. Unlike transformer-based architecture, S4G does not need positional encodings or positional structures, which usually require a heuristic design. Empirical study shows that S4G consistently has superior performance over long-range tasks, which also corroborates their theoretical claims.

### Strengths
1. The paper is well-written for most of the part. 
2. The proposed method appears novel and provides an effective way to solve the message bottleneck problem while maintaining the inductive bias induced by regular MPNNs.

### Weaknesses
The calculation of  $\bar{K}$ could be expensive and requires preprocessing for efficient training. A discussion on how much time is needed to preprocess for different datasets could make the results stronger.

### Questions
Please see the Weaknesses section.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
