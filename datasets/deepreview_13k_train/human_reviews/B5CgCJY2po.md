# Flood and Echo: Algorithmic Alignment of GNNs with Distributed Computing

- Decision: Reject
- Scores: 8, 3, 3, 5

## Abstract
Graph Neural Networks are a natural fit for learning algorithms. They can directly represent tasks through an abstract but versatile graph structure and handle inputs of different sizes. This opens up the possibility for scaling and extrapolation to larger graphs, one of the most important advantages of an algorithm. However, this raises two core questions i) How can we enable nodes to gather the required information in a given graph ($\textit{information exchange}$), even if is far away and ii) How can we design an execution framework which enables this information exchange for extrapolation to larger graph sizes ($\textit{algorithmic alignment for extrapolation}$). We propose a new execution framework that is inspired by the design principles of distributed algorithms: Flood and Echo Net. It propagates messages through the entire graph in a wave like activation pattern, which naturally generalizes to larger instances. Through its sparse but parallel activations it is provably more efficient in terms of message complexity. We study the proposed model and provide both empirical evidence and theoretical insights in terms of its expressiveness, efficiency, information exchange and ability to extrapolate.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper applies flood and echo, a distributed computing algorithm, to graph-based learning tasks. Theoretical and empirical analysis verifies that the proposed method enjoys better expressiveness than massage-passing NN.

### Strengths
- This paper presents a novel technique for graph-based learning tasks.
- Experiments show that flood and echo algorithm achieves overwhelming advantages.
- A novel task (PrefixSum task) is introduced in this paper for verifying the expressiveness of the proposed method.
- Theoretical analysis is provided.

### Weaknesses
 - The implementation of the proposed framework might be complex as it is not supported by the existing graph learning frameworks such as DGL and PyG.
- The computation is more expensive than GNN. Each round of full-graph traverse can only compute one node's embedding.



### Questions
- How to implement the proposed algorithm? 

- Typo: 'ob' in the first paragraph of section 3

- This is a curious question. The idea of Flood and Echo is borrowed from distributed computing. Can we apply it to distributed GNN training/inference? What are the benefits we can expect?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a simple algorithm that mimics the "flood and echo" algorithm in distributed computing as a new computing framework on graphs. The basic idea also is inside part of rooted subgraph GNNs that consider a subgraph with a root node and distance-to-root features. The authors propose this "new" execution framework for GNNs to improve its scalability and its extrapolation ability. The author test its extrapolation ability on some basic tasks comparing with baselines like GIN and RecGNN.

### Strengths
1. The authors present the paper in a very easy-to-follow manner. The central idea is simple and easy to get. 
2. The angle of viewing propagation mechanisms as execution framework is kind of new, and it seems that the proposed execution framework is valuable in terms of improving extrapolation on mimic some graph algorithms. 
3. The author discuss many perspectives of the proposed execution framework like expressivity and information message complexity.

### Weaknesses
1. The underlying idea is not new in many perspectives. First, it is studied in rooted subgraph based GNNs, along with distance-to-root feature usage. One can refer to Bohang Zhang's ICML 23 paper. Second, it shares certain similarity to "Agent-based Graph Neural Network". In principle, I feel the author mainly provide another angle of viewing it as kind of execution mechanism of GNNs. 

2. The expressivity study/proof is technique-wise simple. Also the author need to discuss the expressivity comparison inside permutation equivalent setting. We don't discuss expressivity for permutation sensitive model as it can achieve universality easily. Hence here the author should focus on Flood And Echo All when discussing expressivity. The current analysis lacks a rigorous comparison to established permutation-equivariant GNNs, especially in terms of distinguishing graph structures beyond the capabilities of the 1-WL test. The expressivity analysis should delve into the specific types of graph structures that the proposed method can and cannot differentiate, providing a more nuanced understanding of its theoretical limitations.

3. I feel experimental wise the tasks are limited and datasets are small, baselines are also limited. The experiments are primarily conducted on synthetic datasets, which may not fully reflect the complexities of real-world graph data. The baselines, such as GIN and RecGNN, are not sufficient to demonstrate the superiority of the proposed method. A more comprehensive evaluation should include a wider range of GNN architectures, including those that incorporate higher-order message passing or attention mechanisms, to provide a more robust comparison.

### Questions
1. The way of "backward and forward" "wave" technique is also used in another paper "A Practical, Progressively-Expressive GNN", where they proved that doing this kind of wave back and forth multiple times towards convergence is the most powerful one. I'm wandering whether the author tested doing the flood and echo multiple times. 

2. All this method shares similarity to subgraph GNNs, I'm wandering whether the author can provide some comparison of subgraph GNNs for these extrapolation tasks.

### Soundness
2 fair

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The work introduces Flood and Echo Net, which is inspired by the design of certain algorithms coming from distributed systems. The work analyzes the procedure from the point of view of expressiveness and efficiency. In regards to efficiency, the authors are particularly interested in how many messages are required to be exchanged. The work provides an empirical evaluation for certain algorithmic benchmarks.

### Strengths
The paper proposes a unique message-passing scheme that is inspired by existing literature from distributed systems. The principle of aligning message passing with existing algorithmic paradigms is interesting and was shown by the authors to be fruitful on certain tasks. I also appreciated the theoretical analysis relating the procedure to WL and GIN as it is not obvious that the Flood and Echo network can simulate GIN.

### Weaknesses
While the work is interesting I believe there are some weaknesses that need to be addressed.

W1) While the overall design of the Flood and Echo net is motivated by being aligned to distributed systems, it is not motivated why this specific message-passing design may be useful/desired for real-world tasks that likely do not follow such a dynamical aggregation pattern. In other words, the inductive bias given by such a message-passing procedure may be put into question. 

W2) While the authors aim to answer "i) How can we enable nodes to gather the required information in a given graph (information exchange), even if is far away", the authors do not relate this to existing work on over-squashing [1, 2]. I believe that while this is not necessary, it would greatly strengthen such claims as the phenomenon is highly related to this question. 

W3) The authors evaluate on highly specific benchmarks which seem to be extremely aligned to the Flood and Echo net. It would be more valuable if the authors evaluated on existing algorithmic benchmarks from the field of Neural Algorithmic Reasoning [3].

### Questions
Regarding W1. 

Q1) Would the authors be able to give further motivation for the specific design of the message-passing scheme, beyond specific solutions to certain algorithmic problems? 

Regarding W2.

Q2) Would the authors be able to provide some comments regarding the over-squashing effect of their model? 

Regarding W3. 

Q3) Would the authors be able to provide a reason for why they did not evaluate on existing algorithmic benchmarks such as CLRS-30? 

Q4) Is the technique designed specifically with only algorithmic tasks in mind or do the authors envision the technique to work on non-algorithmic tasks? 

To address W3, it would be important to provide further experimental results on a broader range of tasks.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies an information propagation scheme, named flood and echo. 

In standard GNN message passing, node only exchange information with their immediate 1-hop neighbor in each round. The authors argue that this type of message passing is inefficient with complexity of O(D m ), where D is the diameter of graph and m is the number of edges.

As an alternative, the authors propose “Flood and Echo” which propagates messages in a wave like pattern throughout the entire graph. Starting from a center node, “Flood and Echo”  floods the messages outwards, then the flow reverses and is echoed back. The authors claims this could reduce the complexity to O(m), where m is the number of edges.

The presentation of this paper can be improved. Besides, I have doubt on the complexity part, authors need better explaination on this.

### Strengths
This paper aims at proposing a new message passing schema to replace the ordinary GNN's message passing (i.e., each node propagate to its 1-hop neighbors). 

The algorithm is inspired by distributed learning. Making connection between different field is interesting.

The authors also explore from 1-WL test based expressiveness.

### Weaknesses
It is not clear to me how the computation graph of a single node is constructed in this case. In ordinary GNN, the computation graph is a tree structure, first layer is 1-hop neighbors, second layer is 2-hop neighbors, etc. But I cannot tell how the representation of a single node is computed. If we want the node representation of a node that is not the chosen start node, what is its node representation's computaiton graph?

The flood and echo mainly focused on the forward propagation part. But how its gradient are computed? To compute the gradient for weight parameters, we have to use the “gradient with respect to hidden representations output” and “the input node representation that multiplied to the weight parameters”. In flood and echo, it seems like we have to save the hidden embeddings for each node to compute gradient?

Compared to ordinary message passing GNN, the major difference if the selection of neighbors and the number of propagation steps (aka the number of layers in GNN). In order to propagate information to the full graph, the proposed “flood and echo” requires twice the propagation steps of ordinary message passing GNN due to echo back. I am not sure I understand this correctly and how this can benefit in terms of efficiency.

The "flood" part seems to me is the forward propagation of ordinary GNN, where this GNN's depth is the diameter of the graph?

### Questions
- What is FloodConv and FloodCrossConv on line 7 & 8 in Algorithm 1?
- What is phases stands for on line 5 in Algorithm 1?
- The final node representation might be different if the flood start node is chosen randomly each time?
- In the paragraph above Section 4, the authors said “in every run, we only keep the node embedding for the chosen start node”, but why? If we need to compute the embeddings for all nodes in the graph and compute its gradient, shouldn’t we save this for all nodes?

### Soundness
1 poor

### Presentation
1 poor

### Contribution
1 poor
