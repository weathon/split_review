# Fractal-Inspired Message Passing Neural Networks with Fractal Nodes

- Decision: Reject
- Scores: 6, 5, 5, 6

## Abstract
Graph Neural Networks (GNNs) have emerged as powerful tools for learning on graph-structured data, but they struggle to balance local and global information processing. While graph Transformers aim to address these issues, they often neglect the inherent locality of Message Passing Neural Networks (MPNNs). Inspired by the fractal nature of real-world networks, we propose a novel concept, '*fractal nodes*', that addresses the limitations of both MPNN and graph Transformer. The approach draws insights from renormalization techniques to design a message-passing scheme that captures both local and global structural information. Our method enforces feature self-similarity into nodes by creating fractal nodes that coexist with the original nodes. Fractal nodes adaptively summarize subgraph information and are integrated into MPNN. We show that fractal nodes alleviate an over-squashing problem by providing direct shortcuts to pass fractal information over long distances. Experiments show that our method achieves comparable or better performance to the graph Transformers while maintaining the computational efficiency of MPNN by improving the long-range dependencies of MPNN.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents an approach to enhance Graph Neural Networks (GNNs) by introducing the concept of so called fractal nodes. Most common GNN architectures are based on the Message Passing Framework (Message Passing Neural Networks (MPNNs)). Such architectures face challenges in balancing the incorporation of global information with local information propagation mechanisms. In particular, MPNNs struggle with problems like over-smoothing and over-squashing, which hinder their performance in capturing long-range dependencies. Here, Graph Transformers provide a mechanism to incorporate long-range interactions. However, they can be computationally expensive and often overlook the local structures that MPNNs excel at capturing. To overcome these problems in MPNNs, the authors find inspiration  in the fractal nature of many real-world networks, which exhibit self-similarity across different scales. The authors propose that this property can be leveraged to enhance information flow in GNNs: In order to do so, so called "Fractal Nodes" are introduced into given graphs: The proposed fractal nodes coexist with original nodes and each fractal node summarizes information from its corresponding subgraph while maintaining direct connections to the original nodes. This design allows for an aggregation of both local and global information.
Experiments demonstrate that GNNs enhanced with fractal nodes achieve performance comparable to or better than state-of-the-art graph Transformers on various graph-level-task datasets. It is also shown that this approach shows certain benefits when tackling oversquashing.

### Strengths
The paper is well structured. With its focus on the incorporation of long-range information distillation into message passing networks, it adresses a timely and important problem. The idea of aggregating local subgraph information into aggregate nodes is well founded. It is great to see that the proposed architecture is able to match or superseed transformer performance on graph level datasets. Beyond this, it is good to see that the authors did not only investigate their method solely in this setting, but in total investigate four different aspects of their proposed model in the experimental section. In particular the performance gain that the proposed fractal nodes bring in the synthetic expressivity setting of Section 5.2 is intriguing. The conducted ablation studies round off the paper well.

### Weaknesses
I would argue that a main weakness of the experimental section is the lack of (real world) node level tasks. I am aware that The TreeNeighboursMatch task is a node level task, and I think that it is great that this is included. However, it would be good to see how significant the inclusion of the proposed fractal nodes is for standard node classification benchmarks. Are long-range interactions a problem here and do the proposed fractal nodes alleviate the problem if it exists in this setting?

I am unsure how strong the connection to renormalization techniques is. From a heuristic perspective, I understand that a coarse graining nature is present in both the renormalization group in Physics and when summarizing subgraphs into single nodes. But are there any deeper connections between these two settings? If not, it might be good to make it clearer that this is only used as a heuristic comparison in the present paper.



It seems to be a missed opportunity that no (even preliminary) theoretical analysis of expressivity and mitigation of the oversquashing phenomenon was conducted. Could the authors add some details here?

### Questions
In principle, a different sub-graph partitioning could be used to determine how to select subgraphs and assign additional nodes.  Why is it sensible to use self-similarity as a criterion to select these subgraphs?

I have questions regarding the equation (2-4) encapsulating message passing with fractal nodes: As far as I can tell, from eq. (2), there is only messge passing _within_ each subgraph $G_c$, as there is a subscript $c$ present for all 

$h^{(\ell)}_{u,c}$

aggregated in the message function $\Psi^{(\ell)}$. Is this just a problem in the notation (I assume that the statement $u \in \mathcal{N}_\nu$

 is supposed to mean that infact not only the intersection of $G_c$ and the neighbourhood $\mathcal{N}_\nu$ is relevant).
Furthermore: As far as I can tell, there is no message passing between the fractal nodes. This information mixing only (potentially) happens in the last layer via the MLP mixer (c.f. eq. (8)). Why not also consider  message passing on the coarse grained graph made up of all the fractal nodes?

How self-similar are the two graph structures (original graph and graph with fractal nodes)? It seems the METIS algorithm does not maximize self-similarity as its objective, but rather maximizes in-cluster connections while minimizing inter-cluster connections. This makes me wonder how adept the name fractal nodes truly is.

In Figure 5, why is there essentially no drop in accuracy until $r = 7$ with a stark drop (to zero) when $r = 8$? Could the authors comment on the origin of this  abrupt change?

Could you explain in more detail how the norm distribution experiment (at the beginning of Section 4.1) allows to draw conclusion about local and global information.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes 'fractal nodes' to enhance Graph Neural Networks, addressing the over-squashing. By integrating these nodes into GNN, the method improves long-range dependency modeling, achieving competitive performance with graph Transformers while maintaining computational efficiency.

### Strengths
1. The method is straightforward with low complexity and seems to be effective based on the results obtained.

2. The authors conducted a variety of benchmarking experiments and meticulously outlined the settings for each benchmarking experiment.

### Weaknesses
1. The proposed framework appears to lack novelty, resembling a combination of ClusterGCN[1] and VirtualNode methodologies. The use of Metis clustering, akin to ClusterGNN, and the introduction of fractal nodes that connect to all nodes within a cluster, essentially reflect a variation of the VirtualNode concept.

2. The misapplication of LPF and HPF is evident. As per the definition of LPF (Equation 6), it represents the mean of every node feature within a cluster, failing to capture the graph structure or low-frequency graph signal components. Similarly, HPF (Equation 7), calculated as the original feature minus LPF, also fail in capturing high-frequency graph signal components. It is crucial for the authors to revisit the fundamentals of spectral graph theory to refine their understanding of these concepts.

3. The analysis of the properties in Section 4 appears superficial. The L2 norm distribution of node feature merely indicates the smoothing of node features and does not inherently reveal whether local or global information is being captured. The claim that the proposed method is more balanced lacks rigor, it is essential to provide concrete metrics for comparing differences before making such assertions.

4. The analysis comparing the proposed method to graph coarsening techniques and virtual nodes is inaccurate. Firstly, the fractal nodes are not dynamically generated during training, they are precomputed by METIS. Secondly, virtual nodes do not always utilize mean pooling as an aggregator, instead, they commonly function as regular graph nodes, sharing the same hidden space with other nodes in most scenarios.

5. The author claim the core concept of 'fractal nodes for enforcing self-similarity,' yet upon reviewing the entire paper, the practical impact of 'self-similarity' on enhancing GNN performance remains unclear to me.

### Questions
1. The expressive power evaluation in Section 5.2 is impressive. However, given the absence of a formal proof regarding this expressive power, could you share the code detailing how the method achieved a score of 100 in CSL and SR25?

2. Additionally, we were unable to reproduce the results shown in the paper using the provided source code.
    - Runtime (seconds per epoch) on a 3090 machine: 58s (our evaluation) vs 5.03s (paper) 
    - 0.27, 0.252, and 0.2474 in 3 runs vs 0.2464±0.0014 (paper); Could the authors clarify the number of runs used to obtain the best result?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces 'fractal nodes' to enhance MPNNs by capturing both local and global information efficiently. Fractal nodes address the over-squashing problem, allowing information to travel over long distances without significant loss, thereby addressing key limitations in standard MPNNs.

### Strengths
1. The paper has a clear logical structure, making it relatively easy to read.
2. The concept of using fractal nodes is interesting.

### Weaknesses
1. The performance improvements of the proposed method in the experiments are not particularly significant.
2. The paper could benefit from more in-depth discussion of the experimental results, beyond simply listing which method performs better.

### Questions
1. In Table 2, the experiments focus mainly on graph-level tasks. How does the method perform on node-level tasks, such as node classification on the ogbn-arxiv dataset? Additionally, can you discuss any potential challenges or modifications needed to apply the proposed method to node-level tasks?
2. In Table 2, why does GCN+FN_M perform worse than GINE/GatedGCN+FN_M? Additionally, what factors contribute to the proposed method performing worse than GRIT and only comparably to Graph-ViT/MLP-Mixer and Exphormer on MNIST/CIFAR10? Can you explore specific architectural differences that might explain the performance gaps?
3. When splitting graphs into subgraphs, how many nodes are contained in each subgraph in the experiments? Does each subgraph have a similar number of nodes, and how does the number of nodes in each subgraph affect performance?  Is there any trade-off involved in choosing subgraph sizes?
4. Lines 510–513 mention that 'the higher the number of fractal nodes, C, the better the performance.' What is the ratio of fractal nodes to the total number of nodes? Is there a threshold where increasing C leads to a decrease in performance?

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
2

### Summary
This paper introduces a novel concept called "fractal nodes" to enhance Message Passing Neural Networks (MPNNs) by addressing their limitations in balancing local and global information processing. The approach is inspired by the fractal nature of real-world networks and renormalization techniques. The key innovation lies in creating fractal nodes that coexist with original nodes, where each fractal node summarizes subgraph information and integrates into the MPNN architecture. The method aims to improve long-range dependencies while maintaining MPNN's computational efficiency, presenting an alternative to graph Transformers.

### Strengths
1. Originality
- The concept of fractal nodes is novel and well-motivated by real-world network properties
- The approach offers a fresh perspective on handling the local-global information trade-off
- Creative adaptation of renormalization concepts into neural network architecture

2. Quality
- Strong theoretical foundation drawing from established concepts in network science
- Clear connection between fractal properties and the proposed solution
- Comprehensive experimental validation including performance comparisons and ablation studies
- Addresses known MPNN limitations (over-squashing) with a principled approach

3. Clarity
- Well-structured presentation with clear motivation and problem statement
- Effective use of figures to illustrate concepts (especially Figure 1)
- Logical flow from theoretical inspiration to practical implementation

4. Significance
- Provides an efficient alternative to computationally expensive graph Transformers
- Maintains MPNN's computational advantages while improving its capabilities
- Potentially applicable across various graph-based learning tasks

### Weaknesses
Weaknesses

1. Theoretical Analysis
- The paper could benefit from a more rigorous theoretical analysis of why fractal nodes help with over-squashing. Specifically, the mechanism by which these nodes alleviate the information bottleneck in deep MPNNs should be explored more thoroughly. The current explanation lacks a formal treatment of how the fractal structure impacts gradient flow and information propagation.
- Limited discussion on the optimal number or size of fractal nodes. The paper does not provide clear guidelines on how to determine the appropriate number of fractal nodes for a given graph. It is unclear whether there is a relationship between graph properties (e.g., size, density, diameter) and the optimal number of fractal nodes. Furthermore, the impact of varying fractal node sizes (i.e., the size of the subgraphs they represent) is not sufficiently explored.

2. Experimental Validation
- The truncated content doesn't show complete experimental results, making it difficult to fully assess the method's performance. The absence of full experimental results limits the ability to compare the proposed method with existing state-of-the-art approaches.
- Need for more extensive comparisons with other approaches addressing similar limitations. While the paper compares against standard MPNNs, it lacks a comprehensive comparison with other methods specifically designed to address over-squashing, such as those using virtual nodes or graph rewiring techniques. A more thorough comparison would help to contextualize the contribution of the proposed method.
- Absence of ablation studies on the impact of different subgraph partitioning strategies. The method relies on subgraph partitioning to create fractal nodes, but the paper does not investigate how different partitioning algorithms affect performance. It is unclear whether the choice of partitioning method is critical or if the method is robust to different partitioning strategies.

3. Practical Considerations
- Limited discussion on the computational overhead of creating and maintaining fractal nodes. The paper does not provide a detailed analysis of the computational cost associated with creating and updating fractal nodes, particularly for large graphs. This is crucial for assessing the practical applicability of the method.
- Unclear scalability analysis for very large graphs. While the paper claims the method is scalable, it lacks a detailed analysis of its performance on extremely large graphs, including memory usage and training time. The scalability analysis should include a discussion of how the method scales with respect to the number of nodes and edges.
- No discussion on potential limitations or failure cases. The paper does not discuss scenarios where the proposed method might fail or perform poorly. Understanding these limitations is important for practical application and further research.

### Questions
How sensitive is the method to different subgraph partitioning strategies? 
What criteria should be used to determine optimal partitioning?

### Soundness
3

### Presentation
3

### Contribution
3
