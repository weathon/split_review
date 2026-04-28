# DeepNT: Path-Centric Graph Neural Networks for Network Tomography

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 6, 5

## Abstract
Network tomography is a crucial problem in network monitoring, where observable path measurements are used to infer unmeasured network properties, making it essential for tasks such as route selection, fault diagnosis, and traffic control. However, most existing methods assume that the network topology is fully known—an assumption that rarely holds in practice. The incomplete topology introduces significant challenges in extracting path information for predicting path performance. Furthermore, these approaches are typically designed for a single path performance metric and lack the flexibility to handle multiple metrics that may be of interest in a single network. To address these limitations, we propose Deep Network Tomography (DeepNT), a new framework that simultaneously infers the adjacency matrix and predicts unmeasured paths by leveraging Graph Neural Networks (GNNs) as backbones to learn path-centric end-node pair representations under incomplete network topology. To ensure that the learned adjacency matrix aligns with the characteristics of real-world networks, we propose a novel learning objective that constrains the model in terms of connectivity, sparsity, and path performance bounds, enabling robust generalization across a variety of performance metrics. Extensive experiments on real-world and synthetic datasets demonstrate the superiority of DeepNT in predicting performance metrics and inferring graph topology compared to state-of-the-art methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a neural approach for network tomography called DeepNT. The proposed approach jointly learns the network topology and the GNN for predicting path metrics using alternating optimization. In particular, the path metrics are predicted based on a path aggregation layer that is trained to predict pairwise metrics based on observations. Moreover, triangle inequality is incorporated into the loss to enforce the best path to be selected (according to some objective metric). The graph is learned as an adjacency matrix with an L1 penalty and a connectivity constraint based on its second eigenvalue. The authors propose an alternating optimization scheme (GNN and graph learning) that uses projection to minimize L1 and guarantee a valid matrix. Ten datasets and six baselines are considered in the experiments. The results show that DeepNT consistently outperforms the baselines.

### Strengths
- The paper addresses a relevant problem
- Multiple classical approaches are considered as baselines
- The empirical results described are promising

### Weaknesses
 - The contributions of the paper are limited
- Some important baselines are missing
- The evidences supporting the proposed method are purely empirical

Detailed comments:

1) Contributions: graph learning has already been extensively studied in the context of GNNs and the proposed path aggregation layer does not seem particularly novel. 

2) The proposed graph learning approach could be combined with any GNN in the literature. It is not clear that the proposed path aggregation is significantly better than typical GNN aggregation or the subgraph aggregation using by link prediction methods such as SEAL. Moreover, there are many graph learning approaches, including bilevel optimization, that are not compared against the one proposed in the paper.

3) Supporting evidence for proposed solution: while the results presented are promising, it would be important to provide some theoretical support or at least better intuition on why NeuroNT is a good solution. For instance, are there any guarantees that the predicted pairwise metrics are near optimal given enough observations? This would definitely strengthen the paper.


** Comments after the rebuttal:
I'm increasing my score for this paper based on the most recent reviews. The updated results show that the baselines considered earlier were not good enough. The original paper didn't cite the path neural networks paper but now uses its expressiveness proof. The related work and contributions of the paper need to be adjusted accordingly and the path neural networks approach should be included as a baseline.

### Questions
- What are the major contributions of the paper?

- What other baselines could be considered from the GNN literature?

- Is there any theoretical evidence supporting the proposed solution?

### Soundness
3

### Presentation
2

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
The paper presents DeepNT, a path-centric graph neural network (GNN) framework for network tomography that predicts unobserved path performance metrics (PPMs), such as latency and bandwidth, by leveraging partially observed network data. DeepNT introduces a unique approach by combining data-driven learning with partial prior knowledge, addressing limitations in traditional methods that require complete topology knowledge. Key contributions include a path-centric GNN that aggregates node embeddings along paths, as well as connectivity, sparsity, and triangle inequality constraints that enhance the accuracy of inferred topologies and metrics. Extensive experiments demonstrate that DeepNT outperforms existing methods in predicting multiple types of PPMs across real-world and synthetic datasets, showing strong scalability and robustness.

### Strengths
1. The proposed DeepNT can effectively integrate connectivity, sparsity and triangle inequality constraint to enable robust inference on network topology and path performance metrics under the incomplete data setting.

### Weaknesses
1. The paper currently limits node embedding to path-centric methods and relies primarily on DeepWalk-inspired random walks and SVD-based HOPE embeddings. This focus might overlook more complex embeddings, like graph attention or spectral approaches, which could capture different node relationships and further improve performance. Specifically, the paper does not explore how incorporating node features, if available, could be integrated into the embedding process. The current approach also lacks a discussion on how the choice of path sampling strategy impacts the quality of the learned embeddings and the overall performance of DeepNT. For instance, biased random walks that prioritize certain types of nodes or edges could be beneficial in specific network topologies.
2. While DeepNT demonstrates favorable scalability in empirical evaluations, the paper could benefit from a deeper theoretical analysis of its computational complexity, particularly regarding training on large-scale graphs. A formal complexity analysis for different network sizes, embedding types, and constraint applications would clarify computational trade-offs, especially since training with large adjacency matrices and triangle inequality constraints may become a bottleneck. The paper should also discuss the memory requirements of the proposed method, especially when dealing with very large graphs, as storing and processing large adjacency matrices can be computationally expensive. Furthermore, the analysis should consider the impact of the number of training iterations and the size of the sampled triplets on the overall computational cost.

### Questions
1. While the article's method of updating the adjacency matrix by imposing constraints on connectivity and sparsity appears simple and effective, it lacks necessary theoretical discussions, such as an analysis of overall training complexity, convergence studies, and comparisons of computational efficiency with previous methods.
2. In the synthetic graph experiments, it would be beneficial to test other topologies beyond Erdős-Rényi graphs, such as small-world and power-law graphs.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This article introduces a new framework named DeepNT, aimed at solving the challenges in network tomography by integrating path-centric GNNs. Network tomography involves using observable PPMs to infer network characteristics. The authors point out that traditional methods, which rely on a complete understanding of network topology, and recent purely data-driven approaches both have their limitations. In contrast, DeepNT combines data-driven techniques with appropriate inductive biases from partial prior knowledge.

### Strengths
1. The DeepNT model introduces a path-centric GNN, providing a new theoretical framework for network tomography. Unlike traditional GNNs that focus on nodes or entire graphs, the path-centric GNN concentrates on learning the dynamic performance of networks through the aggregation of information from sequences of nodes. This method allows the model to capture interactions and dependencies along paths more intricately, thereby enabling more accurate predictions of PPMs (Path Performance Metrics) that are not directly observable in the network.
2. During its training process, the DeepNT model integrates structural constraints with performance constraints. The core idea of this design philosophy is to merge the fundamental principles of network theory with the optimization process of machine learning, aimed at ensuring that the learned network topology not only complies with physical or logical feasibility but also reflects the actual network performance. This hybrid approach enhances the model's ability to infer the intrinsic structure and performance of the network.
3. DeepNT exhibits a clear advantage in predicting path performance metrics compared to other existing state-of-the-art technologies. Moreover, DeepNT demonstrates particular robustness when dealing with large-scale and complex network structures. The experimental design of DeepNT takes into account various factors such as latency, bandwidth, packet loss rate, different network topologies, and various network operation scenarios. Furthermore, the experiments utilize multiple evaluation metrics to ensure the accuracy and reliability of the results

### Weaknesses
1. Pooling operations, although helpful in simplifying data and reducing dimensions, can also lead to the loss of important information. Particularly in cases where paths are long or there is significant variation in node features, a single pooling operation may not be sufficient to capture all critical feature information, limiting the model's flexibility and accuracy in handling different types of network structures. For instance, if a path traverses several bottleneck nodes with highly variable latency characteristics, a simple pooling operation might average out these critical variations, leading to inaccurate performance predictions. The model needs a more adaptive pooling mechanism that can preserve the nuanced information along the path.

2. Network states and structures in real-world applications are often dynamic, including the dynamic addition or removal of nodes and edges, as well as real-time changes in network traffic and congestion. These dynamic characteristics require network tomography models to be highly flexible and rapidly adaptable. If the DeepNT model relies primarily on static graph structures and previously learned features, its ability to quickly adapt to such dynamic changes may be limited. Especially when the model depends on long training periods and extensive historical data to predict network performance accurately, its responsiveness and accuracy in dealing with real-time or near-real-time network state changes may be inadequate. For example, a sudden surge in traffic due to a flash crowd could drastically alter network performance, and the model might fail to adapt quickly enough if it relies on pre-computed static features.

3. The DeepNT model does not consider the sequentiality of node paths, i.e., the order of nodes in the path, which might affect the model's performance in network tomography. Ignoring the sequentiality could lead to inaccurate predictions of certain network performance metrics. For instance, in a network where congestion is location-specific, the order in which nodes are traversed could significantly impact the observed latency, and a model that ignores this order might miss crucial performance patterns.

4. The DeepNT model trains using only a portion of the information available in the graph, which may result in poor performance when the model encounters network configurations or conditions that are not represented in the training data, i.e., poor generalization. For example, if the training data primarily consists of paths within a specific geographical region, the model might struggle to accurately predict performance in a different region with different network characteristics.

### Questions
See the above weakness.

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
3

### Summary
This paper proposed Deep Network Tomography (DeepNT), a new framework that learns a path-centric graph neural network for predicting path performance metrics. The key contributions of this paper include (1) the path-centric graph neural network that infers the path performance metrics (PPM) values of a path by learning its path embedding, and (2) a learning objective that imposes connectivity and sparsity constraints on topology and path performance triangle inequality over PPMs.

### Strengths
1. The ideas in this paper are clearly expressed.
2. The experimental results demonstrate the improvements of the proposed method over existing approaches. 
3. The paper presents interesting findings and contributes to the field of network tomography.

### Weaknesses
 - DeepNT proposed in this paper suppose the adjacent matrix is unknown or incomplete. Then how to construct the path sets $P_{uv}$ that represent the set of all possible paths from the node $u$ to $v$ without a specific adjacent matrix? How do we know which path has the optimal path performance? If the path performance can be tested by sending numbers of end-to-end probes, should the probing overhead be considered before the model training? Additionally, how to control the probes to traverse the specific routing paths is also a tough question since many networks do not support source routing.
- On contribution of this paper is the design of the path performance triangle inequality. However, in many scenarios, the triangle inequality may not hold. For example, the delay between $<u,v>$ may not always be less than the delay of $<u,z> + <z,v>$ due to the load balancing policy in the current network. It is even less applicable in social networks.
- In the experiments, the comparison with the baselines may not be entirely fair. In the scenarios of social networks, it's more like doing a matrix completion task. The seven baselines in the experiments are all within the area of network performance tomography, which were originally designed for network performance measurement. Hence, a more reasonable way is to compare DeepNT with matrix completion methods in such a scenario.
- Network topology reconstruction is an important contribution in this paper. However, the experiments did not fully demonstrate the advantages in this part. The author only carried out the experiments when the topological error rate was set to 0.2. More experiments (e.g., higher missing rates or block missing) are required to validate the effectiveness of DeepNT.

### Questions
The questions I would like the authors to address have already been raised in the "Weaknesses" section. I hope the authors can provide more information on these aspects.

### Soundness
2

### Presentation
3

### Contribution
2
