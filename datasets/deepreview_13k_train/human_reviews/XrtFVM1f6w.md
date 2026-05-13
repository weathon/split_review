# Towards characterizing the value of edge embeddings in graph neural networks

- Decision: Reject
- Scores: 6, 5, 5, 5

## Abstract
Graph neural networks (GNNs) are the dominant approach to solving machine learning problems defined over graphs. Despite much theoretical and empirical work in recent years, our understanding of finer-grained aspects of architectural design for GNNs remains impoverished. In this paper, we consider the benefits of architectures that maintain and update edge embeddings. On the theoretical front, under a suitable computational abstraction for a layer in the model, as well as memory constraints on the embeddings, we show that there are natural tasks on graphical models for which architectures leveraging edge embeddings can be much shallower. Our techniques are inspired by results on time-space tradeoffs in theoretical computer science.  Empirically, we show architectures that maintain edge embeddings almost always improve on their node-based counterparts---frequently significantly so in topologies that have ``hub'' nodes.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper explores the architectural benefits of graph neural networks (GNNs) that maintain and update edge embeddings, highlighting both theoretical and empirical advantages. Theoretically, under certain computational and memory constraints, edge-embedding-based architectures can achieve greater efficiency, solving some graph tasks with fewer layers compared to node-based models. Empirically, these architectures often outperform node-only models in graph structures with hub nodes.

### Strengths
1.The paper is well-structured, with clear explanations of the theoretical models and empirical methodologies.
2.The paper provides proofs showing that edge-based GNNs can achieve better depth/memory trade-offs than node-based GNNs under certain conditions.
3. Cases where edge embedding substantially help is interesting

### Weaknesses
1. For dense graphs, maintaining edge embeddings requires substantial memory and can introduce considerable computational overhead, which may limit the scalability of edge-based architectures. Specifically, the memory requirements scale with the number of edges, which can be quadratic in the number of nodes for dense graphs, making it impractical for large-scale applications. This overhead is not just in storage but also in computation, as updating edge embeddings involves operations on all edges, leading to increased runtime complexity compared to node-based methods that only operate on nodes.

2. Although the paper provides insights into the role of edge embeddings into graphs with hub nodes. The paper generally lacks practical guidance on which types of graphs would benefit most from edge embeddings. Providing examples or criteria for when edge embeddings are advantageous would enhance its applicability. For instance, it would be beneficial to discuss the characteristics of graphs, beyond just the presence of hub nodes, where edge embeddings offer a clear advantage. This could include graph density, specific structural motifs, or the nature of the task being performed on the graph. Without such guidance, it's difficult for practitioners to determine when to use edge-based GNNs.

3. With more depths, node embedding can simulate edge embeddings. Would be good to see such experiments and memory consumption comparison. It is not clear how much depth is required for node embeddings to achieve comparable performance to edge embeddings, and whether the memory overhead of increased depth in node-based models would still be less than that of edge-based models. A thorough comparison of memory consumption and performance trade-offs between deep node-based models and edge-based models is needed to fully understand the practical implications of each approach.

### Questions
please see weaknesses

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces the significance of edge embeddings in GNNs to improve understanding of GNN architecture design. The authors present theoretical insights indicating that edge embeddings can allow for shallower network architectures in specific graph topologies by considering memory constraints, thus offering a fresh perspective beyond traditional invariance-based views. Empirical results demonstrate that GNNs utilizing edge embeddings consistently outperform those based solely on node features, particularly in graphs featuring hub nodes. Additionally, the paper proposes a novel method for layer parameterization using edge embeddings, establishing its expressiveness compared to conventional approaches. The authors highlight the computational costs of using edge embeddings in dense graphs and suggest future research directions aimed at developing more efficient edge-based architectures that retain their advantages.

### Strengths
1. The paper presents a novel perspective on the comparative advantages of edge-based architectures in GNNs, contributing fresh theoretical insights to an evolving field. The separation results are particularly noteworthy, addressing a significant gap in the understanding of message-passing protocols.

2. Theoretical rigor is evident throughout the paper, with clear definitions, theorems, and proofs that are well-structured and logically sound. The methodology for proving depth separation between node and edge message-passing protocols is a solid contribution to the literature.

3. The writing is generally clear and accessible, effectively communicating complex ideas in a manner that is understandable for readers familiar with GNNs.

### Weaknesses
1. While the theoretical contributions are substantial, the empirical validation relies on a relatively small set of benchmarks and synthetic tasks. Expanding the experiments to include more diverse datasets and real-world applications would strengthen the claims made about the edge-based architecture's advantages. Specifically, the absence of link prediction tasks, which are often considered a natural fit for edge-based models, is a notable omission. Given that edge embeddings are designed to model relationships between nodes, evaluating their performance on link prediction tasks would be highly relevant. The current experiments focus on graph classification and regression, as well as image classification, which do not fully capture the potential of edge-based architectures.

2. The paper primarily focuses on comparing two architectures (node-based and edge-based) without considering hybrid approaches or other recent advancements in GNN architectures that might offer competitive performance. A broader comparative analysis could provide a more comprehensive view of the landscape. For instance, architectures that combine node and edge features, or those that use attention mechanisms on edges, could provide valuable insights into the relative strengths and weaknesses of the proposed approach. The current analysis is limited to a direct comparison, which may not fully capture the nuances of GNN architecture design.

3. While theoretical insights are valuable, the paper could benefit from a deeper discussion on the practical implications of adopting edge-based architectures. Addressing potential challenges in implementation, particularly regarding scalability and computational resources, would provide a more rounded perspective. The paper acknowledges the computational costs of using edge embeddings in dense graphs, but a more detailed analysis of these costs, along with potential mitigation strategies, would be beneficial. For example, the memory footprint of storing edge embeddings for large graphs could be a significant hurdle in practice, and this should be addressed more thoroughly.

4. The exploration of symmetry constraints in Theorem 5 is interesting, but the practical relevance of this focus could be questioned. Clarifying how these theoretical results translate into actionable insights for GNN design would enhance the paper's impact. While the theoretical analysis of symmetry is important, the connection to practical design choices is not immediately clear. The paper could benefit from a discussion on how these symmetry constraints can be used to guide the development of more effective GNN architectures.

### Questions
1. Could the authors elaborate on the intuition behind the theoretical separation results for edge and node message-passing protocols? Specifically, what practical implications arise from the hub node bottleneck, and how might this influence GNN architecture decisions?

2. How generalizable are the findings in Theorems 1 and 4 to other types of graphs beyond the specific constructions discussed? Are there certain classes of graphs where edge-based protocols are expected to perform particularly poorly, or vice-versa?

3. Could you consider incorporating visual representations of key concepts to enhance reader understanding and engagement in the main content?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors investigate the conditions under which a local edge processing framework is better than the more common, node-wise message passing framework in the processing of graphs. They present theoretical results that indicate a limitation of the latter on certain tasks and under severe memory restrictions, whereas the local edge processing framework is more efficient in these tasks. What remains unclear is if the converse also holds, namely how are the performances of the local edge processing framework compete with classical message passing on tasks that are more suited to the node-centric view.

The authors also show that the two paradigm are almost equivalent, up to a round of “message passing”, if no memory constraints are imposed. Finally, the authors support the theoretical findings with experiments that show the potential benefits of the local edge processing framework.

### Strengths
The authors rightly point out that theoretical contributions in the graph machine learning field are quite scarce if one leaves the “expressiveness” bubble. Contributions like this one are very welcome, especially when they bridge the gap with a set of well-known frameworks like LOCAL that were mostly ignored over the decades by the graph machine learning community. 

The contributions of the paper are novel (to the best of my knowledge), and the author make us think about kinds of problems that are easier to solve with slightly different processing frameworks than classical message passing. This is a worthy contribution as it contributes to the development of a mostly stagnating field.

The empirical contribution focuses mostly on showing how the edge processing paradigm can lead to better performances in some synthetic and real world benchmarks. The authors’ intent is not to provide a full-scale empirical comparison nor to establish a better performing model, which is ok considering the theoretical contributions and nature of the paper. While one might argue that with more rounds of message passing GCN would have obtained the same result as Edge-GCN in Table 1, but the assumption here is that GCN had been properly cross-validated by the authors of Dwiedi et al. [*]

Practically speaking, the results of Section 7 are the most realistic and relevant, as they establish an equivalence between the two methodologies up to an extra round of message passing, where the rather unrealistic memory restrictions of the previous sections are relaxed. This might open to new ways of studying the nature of node and edge embeddings under different families of graphs, which looks like an interesting research direction.

[*] actually we know this not to be true, since Tönshoff et al, 2023 showed how GCN could achieve much better results when properly cross-validated. The reviewer is assuming the authors performed a thorough model selection to identify the best number of hidden neurons and graph convolutional layers.

Finally, I did not check thoroughly the proofs in the Appendix, but overall the technical contribution of the paper seems valuable to the graph machine learning community.

### Weaknesses
Although one might argue that the memory assumptions of the Sections up to 6 are quite unrealistic, and therefore some results might not be of great interest after all, the biggest weakness of the paper is definitely the presentation and its organization.

In general, it is extremely difficult not to get lost. The organization of the paper seems to reflect more the thought process of the authors, instead of developing a narrative that helps the reader to follow. Truth be told, there seems to be an effort of the authors in presenting the same topics in an informal way before moving to the details, but in doing so the authors achieved two unintended effects: 1) duplicating a lot of information, some of which is also inconsistent (for example O(1) in lines 137-138 becomes O(log n) in lines 381-382); and 2) not having the space to explain the theoretical and empirical setups in detail. For instance, proof sketches take entire pages of the main paper, and the proofs in the appendix are not easy to follow, so merging them into a unique proof in the appendix might be useful; most empirical details of the experiments are missing from the paper/appendix (hyper-parameters, evaluation procedures, anything that might help to reproduce results without accessing the code) except for partial information in Appendix E. Notation is also extremely verbose, and there would have been tons of ways to improve their readability.

Another problem is that the introduction of the paper does not have a proper structure. It is generally not a good idea to introduce message passing in an introduction for a general reader (being the paper submitted to ICLR and not LoG), and notation is introduced before its time in Section 4.

The paper makes a few overstatements, claiming that the edge framework is more expressive, then it is stated that it is “at least as expressive”, and in Section 7 it becomes “equivalent” when memory constraints are relaxed. My recommendation is to take particular care when making statements about expressiveness that cannot be proven.

Overall, it is my current belief that the structure of the paper needs to be substantially revised and the paper resubmitted. The contributions are certainly valid but the authors should improve the accessibility of the paper if they want it to have success and spread through the graph community and perhaps beyond it. I will not propose a full reject, though, because the contribution has technical merits.

### Questions
- Are there more practical/real-world problems where you envision a particularly successful application of the edge framework compared to classical message passing?
- Do you think it would be better to replace "symmetry" with "weight sharing"? Symmetry might refer to group theory concepts being applied to GNNs.
- Could the authors at least try to revise the notation during the rebuttal to make it less verbose and more readable?

### Soundness
3

### Presentation
1

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
In this paper, the authors investigate the influence of embedding edges instead of embedding nodes in GNN models. By proving a series of theorems, the authors claim that the representational power of edge-based GNNs is inherently superior to that of node-based GNNs. The authors further validate their theorems through multiple experiments.

### Strengths
1. The authors provide a systematic analysis of edge-based GNN models, which have been under-investigated in previous literature.
2.  The writing is well-structured and helps readers quickly grasp the main ideas, despite the theory-heavy style of the paper.

### Weaknesses
1. I am not sure if I missed anything, but I feel the proof of the main theorem is somewhat inconsistent. First, the authors assume the graph has $O(N)$ edges, implying a constant degree for the graph. However, in the proof, the authors leverage a $\sqrt{n}$-path graph, where a hub node connects to every node in the graph. In this situation, the assumption no longer holds, as the hub node has a degree of $O(n)$.

2. Following the above point, in Theorem 1, it seems that we assume constant memory for each embedding. However, if there is a hub node with a degree of $O(N)$, the total memory leveraged to absorb the hub node's information will be $O(N)$ for edge-based GNNs, whereas for node-based GNNs, we only have constant memory. This difference could explain why the authors achieve their final proof result. However, this comparison is unfair and not realistic for real-world applications. If a real-world graph has an approximately constant average degree, I believe that by increasing the memory by a constant factor for node-based GNN models, they could achieve the same theoretical power as edge-based models. On the other hand, if the graph has a degree around $O(N)$, the edge-based GNN model would use significantly more memory, which becomes impractical if $N$ is extremely large.

3. In the real-world experiments, although the absolute metrics of edge-based GNN models are better, the improvement is marginal. Considering the extra memory used by the edge-based GNN model to store embeddings, I question the practical value of this approach.

4. Regarding the synthetic task, I wonder if the authors constrained the total memory available to node-based and edge-based models. For example, suppose a graph with $N$ nodes and $E$ edges, where the embedding sizes for node-based and edge-based models are $d_n$ and $d_e$, respectively. We should have $N * d_n = E * d_e$ for each GNN layer to ensure a fair comparison.

### Questions
See above. Please correct me if I misunderstand it.

### Soundness
3

### Presentation
3

### Contribution
2
