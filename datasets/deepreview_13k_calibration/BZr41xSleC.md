# Rethinking Message Passing for Algorithmic Alignment on Graphs

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 3, 6, 5

## Abstract
Most Graph Neural Networks are based on the principle of message-passing, where all neighboring nodes exchange messages with each other simultaneously. We want to challenge this paradigm by introducing the Flood and Echo Net, a novel architecture that aligns neural computation with the principles of distributed algorithms. 
In our method, nodes sparsely activate upon receiving a message, leading to a wave-like activation pattern that traverses the graph. Through these sparse but parallel activations, the Net becomes more expressive than traditional MPNNs which are limited by the 1-WL test and also is provably more efficient in terms of message complexity.
Moreover, the mechanism's ability to generalize across graphs of varying sizes positions it as a practical architecture for the task of algorithmic learning. We test the Flood and Echo Net on a variety of synthetic tasks and find that the algorithmic alignment of the execution improves generalization to larger graph sizes. Moreover, our method significantly improves generalization and correct execution in terms of graph accuracy on the SALSA-CLRS benchmark.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes the flood and echo algorithm, that simply works by selecting an origin node, sending messages outward from this node. When the messages reach the end of the graph when centered at the origin node, they reflect back and trace the same path back to the origin node. It is theoretically proven that for the distance, path-finding and prefix sum tasks, the proposed model is a perfect fit.

### Strengths
* The proposed approach is theoretically and empirically validated.
* The paper is well written.
* There are other algorithmic tasks in the experiments than the ones tailored to the proposed approach.

### Weaknesses
 * The proposed algorithm does not generalize to other algorithmic tasks as well as the tasks it is designed for.

### Questions
* The impact of the algorithm is not clear, which real world use-cases would the proposed approach be the most beneficial for?
* What is the dependency of the proposed method to the chosen origin node?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a message-passing graph neural network called Flood and Echo Network (EF Net). The message-passing structure mimics a breadth-first traversal (BFS) starting from a source node. The authors demonstrate that EF Net is more expressive than traditional MPNNs, which are limited by the 1-WL test, and is also provably more efficient in terms of message complexity. Applied to the SALSA-CLRS benchmark, EF Net shows improvements in generalization and correct execution, achieving higher accuracy on this benchmark.

### Strengths
1.	This paper introduces a message-passing neural network that operates similarly to a breadth-first traversal, requiring O(m) messages, where m is the number of edges in the graph. For many tasks evaluated, FE Net requires fewer messages compared to several other APNN models.
2.	The authors demonstrate that FE Net can be more expressive than standard APNN models, particularly in the context of the Weisfeiler-Lehman (WL) test performance.
3.	The paper evaluates FE Net on a subset of tasks from the SALSA-CLRS benchmark using randomly generated ER graphs. According to this benchmark, FE Net shows improved generalization compared to GIN and other APNN models.

### Weaknesses
1.	I recommend revising the introduction to clarify that the paper specifically focuses on "neural algorithmic reasoning on graphs." While the title mentions this, the introduction could be clearer, as it currently suggests a focus on general graph learning. Additionally, there is no evidence provided that FE Net outperforms MPNNs on typical supervised or semi-supervised tasks, such as node classification and link prediction.
2.	The exact aggregation and update operations used in FE Net are not clearly discussed. For instance, GIN has been shown to be more expressive with sum pooling as the message aggregator. To establish the expressiveness of FE Net, it would be beneficial to specify these operators explicitly. Furthermore, Theorem 4.2 could be strengthened by showing that FE Net does not fail in cases where the 1-WL test succeeds, in addition to distinguishing graphs where the 1-WL test fails.
3.	Some assumptions in the paper require further clarification. For instance, it seems to assume that a typical MPNN exchanges O(m) messages per layer, where m is the number of edges. However, the actual number of messages depends on the computational graph. If there is a batch of k nodes with an average degree of d, a 2-layer GCN will involve O(kd^2) messages. Additionally, models like GraphSAGE use sampling to reduce message volume, so O(m) messages per layer may not apply to most APNNs.
4.	FE Net operates similarly to a BFS traversal, where nodes at the same distance from the source are processed together. Given that the algorithms studied also use BFS-like traversal, it is unsurprising that FE Net outperforms some other GNN models. It is unclear, however, how FE Net would perform with algorithms that don’t resemble BFS, as FE Net (and other GNNs) struggled with generalizing to tasks like DFS and MST.
5.	Most of the experiments in the paper are conducted with Erdős-Rényi (ER) graphs, which may not fully represent practical graph structures. Showing results on scale-free graphs or real-world graphs could provide more comprehensive insights into FE Net’s performance.
6.	Since FE Net begins from a source node and reaches all nodes in a connected component, it is unclear how it would handle graphs with multiple connected components. Providing a discussion on this aspect would improve understanding of FE Net's applicability to such cases.

### Questions
1.	Do the authors have any insights on how EF Net performs on scale-free graphs?
2.	Can EF Net be applied to semi-supervised learning tasks, such as node classification?
3.	Is EF Net suitable for non-BFS style algorithms, like clustering or triangle counting?
4.	What specific aggregation and update operations are employed in EF Net?
5.	How is it ensured that EF Net does not fail in cases where the 1-WL test succeeds?
6.	In the experiments with GIN, how many layers were used?
7.	Does EF Net's performance decline when applied to high-diameter graphs, such as road networks?
8.	How does EF Net handle graphs with multiple connected components?

### Soundness
2

### Presentation
3

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
This work proposes a framework, Flood and Echo network (FENet), which breaks the synchronous limit of MPNNs. Theoretically they prove that FENet has higher expressivity than 1WL. Empirically they show great performance of FENet on three algorithmic alignment tasks.

### Strengths
- Overall, the idea is pretty interesting and highly novel. 
- The writing is clear and good, also the illustrations make sense for understanding the framework. 
- The theory is sound.
- The performance of FENet is validated in experiment part.

### Weaknesses
 - One concern of FENet is over-squashing problem. The sensitivity of a node to the original node is unclear, the message from the origin node pass out to the furthest nodes, then gathered back, the over-squashing issue on large graph may not be solved, even aggravated. Specifically, the repeated flooding and echoing might exacerbate information loss as messages travel through multiple hops, potentially making it harder for distant nodes to retain meaningful information about the origin node. This could be particularly problematic in graphs with long paths or high degrees.
- Though the theoretical runtime complexity is the same as MPNN, the messages are executed in sequence, while in MPNN it is in parallel. Modern GPUs can handle large batches of data executed in parallel, but this sequential property of FENet might make it super slow on GPU, especially with a lot of phases. The sequential nature of the message passing, where nodes are updated based on their distance from the origin, introduces a significant bottleneck for parallel processing. This contrasts with MPNNs, which can leverage GPUs to perform updates across the entire graph simultaneously. The practical implication is that FENet might not scale as well as MPNNs on large graphs, especially when many phases are required.
- One minor point, please make the tables more readable, for example, highlight the best candidate in the table, so it is clearer to readers.
- Some design details are not quite clear to me. See questions below.

### Questions
- Why do you pick FCrossConv to exchange messages between nodes at the same distance?
- Why the FConv and FCrossConv are reversed in the echo phase?
- For _fixed_ mode, how exactly do you design which node to be the origin node? 
- The authors claim FENet message passing is more efficient. If I understand correctly, in a whole phase, the number of node updates as well as messages conveyed are not reduced. It's just the origin node is able to reach further neighbors in a phase. 
- Is there a reason why you evaluate the framework on algorithmic alignment? Certainly it performs well, but it can also be a general framework for other tasks, say molecular prediction etc.

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
5

### Summary
The authors propose a novel mechanism where messages are propagated outwards from an origin node and then back to the node. This is shown to be more expressive than 1-WL and have less memory complexity than standard MPNNs. The authors then demonstrate through experiments that the method can generalize better to larger graph sizes on some tasks.

### Strengths
To my knowledge, the mechanism is novel and using an origin node relates to other methods (eg. Subgraph GNNs) whilst the propagation mechanism is more efficient. Seeing this approach will be beneficial to the community and could impact other areas outside algorithmic alignment such as improving long-range interactions. 

The paper is well-written and the memory complexity and expressivity improvements are argued with diagrams, text and theorems. It is very clear what the contributions and goals of the method are and many experiments have been run to ablate the model.

### Weaknesses
[Enhanced Expressiveness]

The paper claims that the enhanced expressiveness arises from the ‘unique message propagation strategy’ and the ‘structured activations of the nodes’. However, Theorem 4.3 demonstrates that the expressivity gains stem solely from marking a node. The core issue is that the propagation scheme itself is not shown to contribute to the enhanced expressivity beyond the effect of the marked node. The choice of node to mark also significantly impacts expressivity, and randomly selecting a node can be suboptimal [1]. This is a concern when the task does not inherently align with a specific node choice, potentially limiting the method's applicability.


[Generalize to large graph sizes]

The theoretical justification for improved generalization is not fully convincing. The argument that the message-passing scheme is more natural because it inherently involves the entire graph is weak. Standard message-passing can be extended to the whole graph (e.g., Graph Transformers), and it is not clear that this alone would improve generalization. The specific architectural aspects that contribute to improved generalization, beyond simply involving the entire graph, are not clearly identified. Furthermore, the experimental results are not entirely convincing. While the method improves on PrefixSum (a path graph where all nodes interact), the [all, random] variants perform worse than RecGNN on the other two tasks. The method only outperforms **old baselines** on **some** of the SALSA-CLRS tasks. This contrasts with concurrent work [2] that appears to solve these tasks, suggesting that the improvement of the proposed method is not substantial.

[Minor Weaknesses]

- The paper focuses solely on size generalization and does not consider other factors such as changes in connectivity distributions, which are also important for real-world applications.
- Time comparisons to RecGNN are needed, especially since it outperforms the proposed approach on some tasks. This would give a more complete picture of the method's practical efficiency.
- The benchmarks used seem to have a natural ordering of nodes. The method breaks symmetries through the origin node, which may be less beneficial for tasks without this inherent ordering, potentially limiting its applicability to a specific class of problems.

### Questions
- GIN will struggle to solve tasks that require long-range interactions due to over-squashing and under-reaching. For example, for path graphs of size 100, you may need a large number of layers so that two nodes interact. If your method improves over GIN on unseen larger graphs - does that actually imply that it is better at generalizing?  (Given that GIN won’t be able to solve the task on these larger graphs even when they are in the training set). To me, it is less about generalization and more about efficient long-range interactions.
- Is your method easily parallelizable? Although message complexity may be less it is not clear to me that this method would have a favorable runtime.
- How would your method work with directed or disconnected graphs? Wouldn’t this mean that some nodes will never receive information from other nodes. Additionally for Theorem 4.2, as well as being connected, do you not also need the graphs to be undirected? For example, a path graph where the direction of the edges is the same way. If I pick the last node as the origin node then would I be less expressive (I guess depends on the implementation)?

[1] Efficient Subgraph GNNs by Learning Effective Selection Policies. Bevilacqua et al. ICLR 2024. 

[2] Discrete Neural Algorithmic Reasoning. Rodionov et al.

### Soundness
3

### Presentation
4

### Contribution
2
