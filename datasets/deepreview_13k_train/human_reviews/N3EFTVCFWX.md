# Spectral Highways: Injecting Homophily into Heterophilic Graphs

- Decision: Reject
- Scores: 3, 5, 3, 3

## Abstract
It is widely assumed that standard GNNs perform better on graphs with high homophily, leading to the development of specialised algorithms for heterophilic datasets in recent years. In this work, we both challenge and leverage this assumption. Rather than creating new algorithms, we emphasise the importance of understanding and enriching the data. We introduce a novel data engineering technique, \textit{Spectral Highways}, that enhances the performance of both heterophilic and non-heterophilic GNNs on heterophilic datasets. Our method augments a given heterophilic graph by adding supernodes, thereby creating a network of highways connecting spectral clusters in the graph. It facilitates additional paths to bring similar nodes closer than dissimilar ones by reducing the average shortest path lengths. We draw both intuitive and empirical connections between the relative decreases in intraclass and interclass average shortest path lengths and shifts in the graph's homophily levels, providing a novel perspective that extends beyond traditional homophily measures. We conduct extensive experiments on seven heterophilic datasets using various GNN architectures and also compare with data-centric techniques, demonstrating significant improvements in node classification performance. Furthermore, our empirical findings highlight the strong sensitivity of several recent GNNs to the random seed used for data splitting, underscoring the importance of this often-overlooked factor in GNN evaluation.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents a graph data augmentation method called Spectral Highway (SH). It involves dividing existing nodes into clusters using spectral clustering and then adding a layer of nodes on top of them. Each new node corresponds to a spectral cluster in the original graph. The new nodes form a fully connected subgraph, and they are connected to the original nodes belonging to their respective clusters in a principled way.

**Experiments.**
The authors tested the improvement in node classification performance on several classic *small-scale* datasets, showing *significant* results on ChameleonF and SquirrelF. They also compared SH with several rewiring and data-centric methods, demonstrating the advantages of SH as a graph augmentation method.

**Analysis.**
The authors mainly considered the impact of SH on homophily *intuitively and through experiments*, as well as the effect on intra-class and inter-class average shortest path lengths.

### Strengths
1. The method and illustrations in the paper are clear.
2. The approach is very simple, but it shows significant results on ChameleonF and SquirrelF.
3. The paper organizes existing motivations for heterophilic graphs and addresses them in the analysis section.

### Weaknesses
1. The algorithm is difficult to run on larger datasets. The paper emphasizes the impact of random seeds, which is reflected in the large variance of results. This is largely due to the small size of the datasets involved (Cornell, Texas, Wisconsin). Because of this, the authors should conduct experiments on larger datasets. However, the algorithm depends on spectral clustering, which seems to prevent it from scaling to larger datasets.

2. Few rewiring, data-centric/graph-augmentation methods are compared in the paper. 

3. The paper empirically discusses SH’s impact on homophily across various metrics. However, aside from the decrease in Aggregated Homophily on many datasets, the observed improvements are *not significant* in terms of numerical values.

4. According to Table 7, SH only works on heterophilic graphs. But at the same time, as shown in Table 1&2, SH is not compared to stronger baselines in heterophilic graphs, e.g., Table.1 in [1].

### Questions
Please check weaknesses.

### Soundness
2

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
The paper proposes Spectral Highways, a technique that enhances the performance of Graph Neural Networks on heterophilic graphs with additional nodes and connections forming highways over the original graph.

### Strengths
1. The story is interesting.
2. It tested on rich datasets.

### Weaknesses
1. The addition of nodes and connections is a common approach in graph augmentation. For example, methods such as [1] use similar upsampling approaches. To better showcase the novelty, I suggest that the authors emphasize these unique aspects more explicitly and explore how these modifications lead to improvements over [1] and similar methods. Specifically, the paper should delve deeper into the spectral properties of the added nodes and edges, and how these properties differ from existing augmentation techniques. A more detailed analysis of the specific spectral characteristics that enable the proposed method to outperform alternatives is necessary.
2. While enriching the graph can enhance performance, it may also introduce considerable computational overhead, especially on large-scale datasets. I recommend that the authors include a detailed analysis of time and space complexity. Specifically, it would be beneficial to compare the construction time of Spectral Highways relative to the original graph size, as well as its impact on downstream GNN runtime. This analysis should include a breakdown of the computational cost associated with each step of the Spectral Highway construction, such as the spectral decomposition and the addition of new nodes and edges. Furthermore, the memory footprint of the augmented graph should be compared to the original graph.
3. Since datasets are already introduced in Section 2.1, Section 2.2 could be streamlined to focus primarily on algorithmic contributions without redundancies. In table 2, The analysis could be expanded to include comparisons that consider performance gains across dataset characteristics, such as homophily levels, graph sizes, and class distributions. This additional detail would make the results more informative and enable better comparisons across datasets. For example, it would be useful to see how the performance gains vary across datasets with different homophily levels, and whether the proposed method is more effective on certain types of graphs.

### Questions
See Weakness.

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
3

### Summary
This paper proposes a new technique called Spectral Highways that is designed to improve the performance of GNNs on heterophilic datasets. Namely, supernodes are added to the graph, each supernode is linked to a particular cluster and supernodes are linked to each other. This allows better information exchange between different regions of the graph.

### Strengths
The idea proposed in the paper is reasonable and improves on the concept of virtual nodes.

### Weaknesses
 - Most of the datasets used in the experiments are small and have certain flows. Namely, Cornell, Texas and Wisconsin are extremely small and are unbalanced (so, accuracy should not be used as a performance metric). Then, Squirrel Filtered and Chameleon Filtered are used by Platonov et al. (2023) to illustrate the flows of the original Squirrel and Chameleon and are not advised for further usage. The new datasets proposed by Platonov et al. (2023) are not used in this paper. Similarly, only one dataset from Lim et al. (2021) is used. The authors write that "We could not take other datasets like pokec, genius, wiki, etc., as their experiments ran out of memory, and twitch-gamers due to resource constraint." Does this apply to all models? For instance, Platonov et al. (2023) use several simple models that show good results on their datasets. The absence of experiments on realistic datasets reduces the reliability of conclusions made in the paper.
- From the description of the proposed approach it is not clear why one would expect it to work on heterophilic datasets. In particular, it is not obvious why it should improve homophily. As I understand, new edges are added independently of whether they are homophilic. Thus, it seems that edges with neutral homophily are added which agrees with the results reported in Table 3: adding neutral edges to heterophilic graphs makes them more homophilous (adjusted homophily, in most cases, becomes closer to zero), and adding neutral edges to homophilic graphs makes them more heterophilous (again, adjusted homophily becomes closer to zero).
- In lines 208-232 the authors discuss several options for their algorithm and write that it is not always the case that the intuitive option works and thus all the options need to be tried on a particular dataset. Thus, the proposed approach is not so well supported by the intuition described in the text.
- Equation (1) is claimed to be a formal mathematical description of the proposed algorithm, but it is not a valid mathematical expression and thus complicates the reading.
- If I am not mistaken, code for reproducing the results is not provided.
- Some of the ideas of the proposed approach are related to the concept of virtual nodes, so I suggest discussing related work on this topic (e.g., Hwang et al., 2022; Qian et al., 2024). For instance, similarly to the proposed approach, Hwang et al. (2022) cluster the initial graph and assign a virtual node to each cluster (however, there are no edges between the virtual nodes).

### Questions
Q1. What is the main intuition on why the method is expected to work well on heterophilic graphs?

### Soundness
2

### Presentation
2

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
This paper aims to propose a technique for better performance on heterophilic graphs.
The authors introduce additional virtual nodes to the graph that improve the connectivity of the nodes within clusters.
The experiments are conducted on seven heterophilic graphs.

### Strengths
1. The idea is simple and works well.

### Weaknesses
1. This paper is written poorly.
2. There is not enough justification for the design of the proposed method. The core idea of adding virtual nodes to improve connectivity is not sufficiently motivated, and the specific choice of spectral clustering for creating these nodes lacks a clear rationale. The paper does not adequately explain why this particular approach is superior to other potential methods for enhancing connectivity in heterophilic graphs.
3. There is no ablation study in the experiments. The absence of a thorough ablation study makes it difficult to assess the contribution of different components of the proposed method. For example, the impact of the number of virtual nodes, the specific spectral clustering parameters, and the connectivity patterns between virtual nodes and original nodes are not explored. This lack of analysis limits the understanding of the method's behavior and optimal configuration.

### Questions
1. The introduction is written poorly. There is no paragraph pointing out the existing challenges of node classification on heterophilic graphs. This makes the last paragraph of contribution very abrupt and lacks motivation. I would recommend adding a paragraph pointing out the current challenges.
2. Again, the related works provide little context or motivation with respect to the proposed method. As this is not a survey paper, these paragraphs are not helpful. This section should serve as a motivation for proposing your work.
3. In line 158, in heterophilic networks, vertices with high similarity are usually 2 steps away. “Far away” is an ambiguous description.
4. Figure 1 does not look like a heterophilic graph, as most edges are connected by the nodes with the same label.
5. The connectivity between the spectral nodes seems redundant. It would be helpful to have an ablation study of removing all the edges between the spectral nodes. Moreover, there is no ablation study at all.
6. In Table 2, most baselines have different base GNN models and make the results not comparable. Dir-SAGE and SH (Dir-SAGE) seem to be comparable, but the results are statistically tied.
7. Section 6 should be moved forward to be right after the proposed method section, to justify the design of the proposed method. However, most analyses are indirect to the reason for performance improvement, and do not help understand why the method works. A theoretical analysis would largely improve the completeness of the paper.
8. In Table 7, using SH hurts the performance in the homophilic graphs most times. In real-world, given a graph with limited labels, knowing whether it is homophilic or heterophilic is not an easy problem. This is important but also not discussed in the paper.

### Soundness
2

### Presentation
2

### Contribution
2
