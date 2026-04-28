# Primphormer: Leveraging Primal Representation for Graph Transformers

- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 6, 6, 5

## Abstract
Graph Transformers (GTs) have emerged as a promising approach for graph representation learning. Despite their successes, the quadratic complexity of GTs limits scalability on large graphs due to their pair-wise computations. To fundamentally reduce the computational burden of GTs, we introduce Primphormer, a primal-dual framework that interprets the self-attention mechanism on graphs as a dual representation and then models the corresponding primal representation with linear complexity. Theoretical evaluations demonstrate that Primphormer serves as a universal approximator for functions on both sequences and graphs, showcasing its strong expressive power. Extensive experiments on various graph benchmarks demonstrate that Primphormer achieves competitive empirical results while maintaining a more user-friendly memory and computational costs.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes an efficient graph Transformer model using an asymmetric kernel trick. Specifically, the model does not need to compute pair-wise scores, so there is no extra computational burden. The key analysis of this model is based on (or, say, similar to) [1], which reformulates the original problem to a dual problem. This primal-dual approach leverages the graph information to adjust the basis of outputs and has more expressive power. Furthermore, the authors prove that the proposed model, namely Primphormer, could be a good universal approximator for arbitrary continuous functions. Experimental results also show the proposed model has better performance while using less memory and computational costs.

### Strengths
1. The formulation of primal graph Transformer algorithm to dual is interesting. The dual problem gives a nice solution via KKT condition. The primal-dual formulation gives some nice theoretical properties.

2. The experimental results look promising. Compared with current state-of-the-art method, the proposed mehthods have better performance over all while using less memory and computation resources.

### Weaknesses
In general, the paper proposes a new method for graph presentation learning. The experimental results look promising. However, I found this paper is heavily based on a previous work (see [1]). Hence, the overall novelty is very limited. Some weaknessnes are listed as follows:

1. Concern about the definition of primal problem: The formulation of original problem of graph Transformer is defined as in (2.4). Why is this definition is the right one?

2. Concern about the overal novelty of this paper: The formulation of (2.4) is very similar to the formulation used in [1]. I would believe that the theorems and dual formulation will largely follow the techniques used in [1]. If not, please explain what are the differences between these two. At this point, the overall novelty of this paper is limited.

3. Some definition is missing citation: The Definition of (2.4) is very similar to Definition 2.1 of [1]. It would be more helpful if the authors put citation here as the definition is not original.

4. Difference between Theorem 4 and Lemma 4.2 in [1]. I found a large context of this Theorem and Lemma 4.2 in [1] is quite similar. Please explain more on the difference between these two.

### Questions
See the weakness section.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces Primphormer, which reduces computational complexity from quadratic to linear by representing self-attention as a dual representation and modeling it in primal space.

### Strengths
The idea is interesting and it reduces the time complexity using primal space.

The authors provide clear pseudocode and detailed implementation guidelines, making the work practical for real-world applications.


The experimental evaluation is comprehensive, including lots of datasets from different domains.

### Weaknesses
1. Using virtual nodes could potentially bring bottlenecks in information flow for graphs with complex hierarchical structures or when important information needs to be preserved across distant nodes. The virtual nodes, while facilitating global information exchange, might not effectively capture the nuances of local interactions, especially in graphs where the relationships between immediate neighbors are crucial. This could lead to a loss of fidelity in representing the graph's structure, particularly in scenarios where hierarchical relationships are not strictly tree-like but involve more intricate dependencies.


2. The transition to primal space requires specific mathematical conditions, such as accommodating the inherent asymmetry of attention scores, which limits its applicability. Specifically, the method's reliance on a specific kernel function to map the attention scores into the primal space might not be universally applicable. The choice of kernel and its parameters could significantly affect the performance, and the paper does not provide a comprehensive analysis of how to select the optimal kernel for different types of attention matrices. This lack of flexibility in handling various attention score distributions could limit the method's practical use.

### Questions
None

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work introduces the use of primal representation for Graph Transformers, aiming to enhance computational efficiency. Inspired by a similar approach applied to sequences, the authors present a method tailored to graphs. They formulate the dual representation and explore the relationship between primal and dual forms. A theoretical analysis of the universal approximation capabilities of their method is provided. They integrate their approach into an MPNN+Transformer combination, as previously proposed by GraphGPS, replacing the Transformer component with their efficient variant while retaining the same MPNN architectures.

### Strengths
1. **Relevance**: The work addresses the critical challenge of developing efficient Transformer variants for graphs.
2. **Motivation**: The study is well-justified and motivated, with clear objectives and potential impacts.
3. **Results**: The authors present compelling results, showing promising improvements in both memory and time efficiency.
4. **Comprehensiveness**: The work covers both theoretical and practical aspects, providing a fairly thorough analysis in each area.

### Weaknesses
1. **Clarity and Readability of the Method**
   The method is challenging to follow, especially in certain sections:
   - **Equation 2.2**: It is unclear whether $\mathbf{\alpha}_i$ and $\mathbf{\omega}$ are scalars or vectors. The notations section suggests they are vectors, yet the equation starts with a vector and seems to become scalar. If they are indeed scalars, the connection to the attention mechanism remains unexplained. This lack of clarity makes it difficult to understand how the primal representation is derived and how it relates to the attention weights.
   - **Equation 2.4**: This equation introduces several new variable names and vector dimensions without clear definitions, making it difficult to understand. Specifically, the dimensions of the vectors and matrices involved are not specified, and the relationship to the Transformer architecture is not clearly established in this section. The connection between the variables in this equation and the standard Transformer architecture, particularly the query, key, and value matrices, is not made explicit.

2. **Connection to Virtual Nodes**
   While the authors’ approach of linking their presentation to virtual nodes is intriguing, it raises a question: does this imply that many underlying theories in this work are already established? For instance, Appendix E in the Exphormer paper [1] includes discussions about virtual nodes that appear to overlap with the concepts in this work. The use of virtual nodes, while potentially simplifying the analysis, may not be as novel as presented, and the authors should clearly delineate the differences and contributions of their approach.

3. **State-of-the-Art (SoTA) Comparison**
   Although the paper claims to achieve SoTA results across several datasets, it does not compare against models that report better results, such as GRIT [2] or certain optimized results in [3]. For example, paperswithcode provides relevant leaderboard results:
   - [CIFAR10](https://paperswithcode.com/sota/graph-classification-on-cifar10-100k)
   - [MNIST](https://paperswithcode.com/sota/graph-classification-on-mnist)
   - [Pascal-VOC](https://paperswithcode.com/sota/node-classification-on-pascalvoc-sp-1)
   - [COCO-SP](https://paperswithcode.com/sota/node-classification-on-coco-sp)
   In comparison with these benchmarks, the paper’s results do not convincingly indicate SoTA performance. The lack of direct comparison with these top-performing methods makes it difficult to assess the true contribution of this work.

4. **Graph Edges and Model Efficiency**
   The paper argues that previous methods are inefficient due to the use of graph edges, while their Transformer does not rely on them. However, this advantage becomes less pronounced when the proposed method is combined with the Message Passing Neural Network (MPNN). Therefore, the claim that their method is entirely independent of the number of edges seems somewhat overstated. The computational cost of the MPNN, which inherently depends on the number of edges, might overshadow any efficiency gains from the edge-independent Transformer component, making the overall advantage less clear.

### Questions
1. Usually, there are parameter constraints on datasets like CIFAR10 and MNIST benchmarks. Does your method meet these parameter constraints? For reference, you can check the constraints outlined in the GraphGPS paper.

2. How does the universal approximation on graphs that considers edges (page 6, lines 270-281) as inputs relate to your method? Your tokens are nodes, which seems to be significantly different from a theory that includes edge information.

3. How can the ability to solve the graph isomorphism problem—which is discrete and not continuous—be inferred from your universal approximation theorems, which are based on continuous function assumptions?

4. What are the connections between this work and linear kernel trick methods such as Nodeformer [1] and Polynormer [2]? The formulations seem very similar in practice.

---------
[1] Wu, Q., et al. "Nodeformer: A scalable graph structure learning transformer for node classification." *Advances in Neural Information Processing Systems* 35 (2022).

[2] Deng, C., et al. "Polynormer: Polynomial-expressive graph transformer in linear time." International Conference on Learning Representations (ICLR) 2024.

### Soundness
3

### Presentation
2

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
The authors introduced Primphormer, a primal representation for graph transformers that eliminates the need for intensive pairwise computations by utilizing a kernel trick. This proposed technique has been demonstrated to serve as a universal approximator within a compact domain, showcasing superior performance compared to the current state-of-the-art.

### Strengths
* The authors introduce a novel primal representation for graph transformers, offering a comprehensive formulation that clearly delineates the distinctions between their method and traditional self-attention, which according to the paper relies on pairwise computations.  
* The paper includes rigorous theoretical analysis and proofs that highlight the advantages of the proposed method, establishing its capability as a universal approximator.  
* Extensive experiments were conducted, with results compared against benchmark models, demonstrating the significant performance improvements achieved by the proposed method.

### Weaknesses
 * A minor concern arises regarding the notations used throughout the paper. A central explanation or summary may enhance reader comprehension, as there are instances where notations are utilized before being defined, or are left inadequately defined. For example, the notation ( N_s ) is introduced in the complexity analysis without prior definition.  
* A fundamental issue regarding claims of computational complexity savings is the authors' assumption that all pairwise attentions in standard self-attention must be computed, which reflects an upper bound as indicated by big-O notation. In practice, attention mechanisms may focus only on local subgraphs or PPR sampled neighborhood, suggesting that neglecting very long-hop attention could have minimal impact. Consequently, the actual necessary computations may be significantly less than the proposed upper bound. It remains unclear whether this approximation or relax is applicable to the kernel trick mentioned. Furthermore, the paper does not adequately address the practical implications of using a kernel method in terms of memory usage, especially when dealing with large graphs. The kernel matrix, even if implicitly computed, can pose significant memory challenges that are not discussed.
* The significance of the universal approximation property is not adequately demonstrated in the paper and lacks experimental validation. The theoretical claim is not connected to any specific practical benefit or task. It is unclear how this property translates to improved performance in real-world scenarios or if it is merely a theoretical construct. The paper would benefit from a discussion on the limitations of this property and how it might be relevant in the context of graph transformers.
* In Figure 1(a), the necessity of residual connections prior to the merging of MPNN and ATTN is not well justified, raising concerns about the potential for added computational cost compared to applying the residual connections after the merge. The paper does not provide any ablation studies or empirical evidence to support this specific architectural choice. It is unclear why the residual connection is placed before the merge rather than after, and what the impact of this choice is on the overall performance and training dynamics.

### Questions
See the detailed comments in the weakness part

### Soundness
3

### Presentation
3

### Contribution
3
